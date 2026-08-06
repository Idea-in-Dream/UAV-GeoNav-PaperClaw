from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
import json
import sys
import unittest
import urllib.parse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients.arxiv_client import (
    build_arxiv_proxy_url,
    fetch_recent_candidates,
    fetch_url_with_retry,
    has_remote_sensing_signal,
)
from daily_arxiv_cross_filter import has_ai_signal, llm_cross_filter, obvious_common_false_positive
from services.issue_index import canonical_arxiv_id
from services.labels import allowed_paper_labels


FIXTURE = Path(__file__).resolve().parent / "fixtures" / "uav_geonav_validation.json"


class UAVGeoNavFilterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_required_papers_hit_title_abstract_prefilter(self):
        for paper in self.cases["positive"]:
            text = f"{paper['title']}\n{paper['abstract']}"
            with self.subTest(paper=paper["name"]):
                self.assertTrue(has_remote_sensing_signal(text))
                self.assertTrue(has_ai_signal(text))

    def test_broad_prefilter_defers_common_false_positives_to_llm(self):
        for paper in self.cases["negative"]:
            text = f"{paper['title']}\n{paper['abstract']}"
            with self.subTest(paper=paper["name"]):
                self.assertTrue(has_remote_sensing_signal(text))

    def test_structured_llm_decisions_keep_required_cases_and_exclude_common_false_positives(self):
        candidates = []
        for paper in self.cases["positive"] + self.cases["negative"]:
            candidates.append({
                "arxiv_id": paper["arxiv_id"],
                "title": paper["title"],
                "abstract": paper["abstract"],
                "published": "2026-08-01",
            })

        output = {
            "keep": [
                {
                    "arxiv_id": paper["arxiv_id"],
                    "labels": ["UAV-Satellite", "GNSS-Denied"],
                    "reason": "目标论文回归集",
                }
                for paper in self.cases["positive"]
            ],
            "needs_review": [],
            "exclude": [
                {"arxiv_id": paper["arxiv_id"], "reason": "普通检测、分割或跟踪"}
                for paper in self.cases["negative"]
            ],
        }

        with patch("daily_arxiv_cross_filter.call_llm", return_value=json.dumps(output)) as llm_mock:
            selected = llm_cross_filter(candidates, batch_size=20)

        selected_ids = {item["arxiv_id"] for item in selected}
        self.assertEqual(selected_ids, {paper["arxiv_id"] for paper in self.cases["positive"]})
        submitted_prompt = llm_mock.call_args.args[0]
        self.assertIn(self.cases["positive"][0]["title"], submitted_prompt)
        self.assertIn(self.cases["positive"][0]["abstract"], submitted_prompt)
        self.assertEqual(llm_mock.call_args.kwargs["thinking"], "disabled")

    def test_unclassified_candidate_is_conservatively_marked_for_review(self):
        paper = self.cases["positive"][0]
        candidate = {
            "arxiv_id": paper["arxiv_id"],
            "title": paper["title"],
            "abstract": paper["abstract"],
            "published": "2026-08-01",
        }
        with patch(
            "daily_arxiv_cross_filter.call_llm",
            return_value='{"keep": [], "needs_review": [], "exclude": []}',
        ):
            selected = llm_cross_filter([candidate])

        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["filter_status"], "needs_review")
        self.assertIn("Needs-Review", selected[0]["filter_labels"])

    def test_safety_gate_rejects_pure_uav_tracking_even_if_llm_keeps_it(self):
        candidate = {
            "arxiv_id": "2607.15004v1",
            "title": "CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking",
            "abstract": (
                "The model tracks a dynamic target through occlusion, estimates target visibility and a 2D box, "
                "and generates continuous flight actions in urban scenes."
            ),
            "published": "2026-07-16",
        }
        output = {
            "keep": [
                {
                    "arxiv_id": candidate["arxiv_id"],
                    "labels": ["Target-Geolocation"],
                    "reason": "incorrect optimistic decision",
                }
            ],
            "needs_review": [],
            "exclude": [],
        }

        with patch("daily_arxiv_cross_filter.call_llm", return_value=json.dumps(output)):
            selected = llm_cross_filter([candidate])

        self.assertEqual(selected, [])

    def test_safety_gate_rejects_ris_actuation_without_geo_output(self):
        candidate = {
            "title": "LIVE-RIS: Real-Time In-Flight Actuation of UAV-Mounted RIS",
            "abstract": "The system controls a reconfigurable intelligent surface for wireless links during flight.",
        }

        self.assertIsNotNone(obvious_common_false_positive(candidate))

    def test_arxiv_versions_share_one_canonical_id(self):
        self.assertEqual(canonical_arxiv_id("2603.20778v1"), "2603.20778")
        self.assertEqual(canonical_arxiv_id("2603.20778v12"), "2603.20778")

    def test_required_labels_are_configured(self):
        required = {
            "UAV-Satellite", "Orthophoto-Registration", "DSM-DEM-TDOM",
            "3D-Map-Registration", "3DGS-NeRF", "Map-Aided-VIO",
            "GNSS-Denied", "Cross-View-Retrieval", "Fine-Registration",
            "Target-Geolocation", "Thermal-Localization", "Dataset-Benchmark",
            "Code-Available", "Reproducible", "Needs-Review",
        }
        self.assertTrue(required.issubset(allowed_paper_labels()))

    def test_goal_search_terms_are_configured(self):
        config = json.loads((ROOT / "scripts" / "config" / "filter_keywords.json").read_text(encoding="utf-8"))
        required = {
            "UAV geo-localization", "drone geo-localization", "UAV satellite matching",
            "cross-view geo-localization", "orthophoto registration", "orthogonal map alignment",
            "DSM localization", "DEM localization", "TDOM localization",
            "terrain referenced navigation", "3D map registration UAV",
            "3DGS visual localization UAV", "map aided visual inertial navigation",
            "satellite aided VIO", "GNSS denied UAV localization",
            "UAV target geo-localization", "thermal UAV geo-localization",
            "geolocation", "visual localization", "visual place recognition",
            "camera relocalization", "absolute pose estimation", "aerial image retrieval",
            "cross-domain localization", "terrain-relative navigation", "georeferenced imagery",
        }
        self.assertTrue(required.issubset(set(config["rs_query_terms"])))
        self.assertTrue(
            {"UAV", "drone", "remote sensing", "satellite imagery"}.issubset(
                set(config["rs_context_query_terms"])
            )
        )
        self.assertTrue(
            {"cs.CV", "cs.RO", "eess.IV"}.issubset(set(config["arxiv_categories"]))
        )
        self.assertEqual(config["candidate_limit_per_day"], 50)

    def test_candidate_pool_is_capped_per_day(self):
        entries = []
        for index in range(60):
            entries.append(
                f"""
                <entry>
                  <id>https://arxiv.org/abs/2608.{index:05d}v1</id>
                  <title>Object Detection in Aerial Imagery {index}</title>
                  <summary>A detector processes satellite images for remote sensing benchmarks.</summary>
                  <published>2026-08-01T12:00:00Z</published>
                </entry>
                """
            )
        entries.append(
            """
            <entry>
              <id>https://arxiv.org/abs/2608.99999v1</id>
              <title>UAV Geo-Localization against Satellite Maps</title>
              <summary>A drone matches imagery to georeferenced orthophotos for absolute camera pose.</summary>
              <published>2026-08-01T12:00:00Z</published>
            </entry>
            """
        )
        xml_text = '<feed xmlns="http://www.w3.org/2005/Atom">' + "".join(entries) + "</feed>"

        with patch("clients.arxiv_client.fetch_url_with_retry", return_value=xml_text) as fetch_mock:
            candidates = fetch_recent_candidates(
                max_results=100,
                target_date="20260801",
                candidate_limit_per_day=50,
            )

        self.assertEqual(len(candidates), 50)
        self.assertIn("2608.99999v1", {item["arxiv_id"] for item in candidates})
        requested_url = fetch_mock.call_args.args[0]
        decoded_query = urllib.parse.unquote(requested_url)
        self.assertIn("cat:cs.CV", decoded_query)
        self.assertIn("all:UAV", decoded_query)

    def test_candidate_limit_must_be_positive(self):
        with self.assertRaises(ValueError):
            fetch_recent_candidates(candidate_limit_per_day=0)

    def test_empty_target_date_does_not_fall_back_to_unbounded_scan(self):
        empty_feed = '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
        with patch("clients.arxiv_client.fetch_url_with_retry", return_value=empty_feed) as fetch_mock:
            candidates = fetch_recent_candidates(max_results=100, target_date="20260802")

        self.assertEqual(candidates, [])
        self.assertEqual(fetch_mock.call_count, 1)

    def test_arxiv_proxy_url_encodes_the_original_query(self):
        original = "https://export.arxiv.org/api/query?search_query=cat:cs.CV&max_results=10"
        proxied = build_arxiv_proxy_url(original, "https://api.allorigins.win/raw?url=")

        self.assertEqual(
            proxied,
            "https://api.allorigins.win/raw?url=" + urllib.parse.quote(original, safe=""),
        )

    def test_arxiv_network_failure_switches_to_proxy_without_sleeping(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b"<feed/>"
        config = SimpleNamespace(
            arxiv_api_proxy_prefix="https://api.allorigins.win/raw?url=",
            arxiv_api_force_proxy=False,
            arxiv_user_agent="test-agent",
        )
        original = "https://export.arxiv.org/api/query?search_query=cat:cs.CV"

        with patch("clients.arxiv_client.CONFIG", config), patch(
                "clients.arxiv_client.urllib.request.urlopen",
                side_effect=[TimeoutError("timed out"), response],
            ) as urlopen_mock:
            output = fetch_url_with_retry(original, retries=2, timeout=1)

        self.assertEqual(output, "<feed/>")
        second_request = urlopen_mock.call_args_list[1].args[0]
        self.assertTrue(second_request.full_url.startswith(config.arxiv_api_proxy_prefix))

    def test_arxiv_force_proxy_skips_the_official_endpoint(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b"<feed/>"
        config = SimpleNamespace(
            arxiv_api_proxy_prefix="https://api.allorigins.win/raw?url=",
            arxiv_api_force_proxy=True,
            arxiv_user_agent="test-agent",
        )
        original = "https://export.arxiv.org/api/query?search_query=cat:cs.CV"

        with patch("clients.arxiv_client.CONFIG", config), patch(
                "clients.arxiv_client.urllib.request.urlopen",
                return_value=response,
            ) as urlopen_mock:
            output = fetch_url_with_retry(original, retries=1, timeout=1)

        self.assertEqual(output, "<feed/>")
        request = urlopen_mock.call_args.args[0]
        self.assertTrue(request.full_url.startswith(config.arxiv_api_proxy_prefix))

    def test_issue_prompt_and_renderer_cover_required_fields(self):
        prompt = (ROOT / "scripts" / "prompts" / "summarize_prompt.md").read_text(encoding="utf-8")
        renderer = (ROOT / "scripts" / "paper_processor.py").read_text(encoding="utf-8")
        fields = [
            "任务类型", "地图类型", "输入传感器", "定位输出", "核心方法", "实验精度",
            "运行速度与硬件", "公开代码与资源", "是否融合 VIO/IMU", "复现难度",
            "对当前无人机定位项目的价值",
        ]
        for field in fields:
            with self.subTest(field=field):
                self.assertIn(field, prompt)
                self.assertIn(field, renderer)
        self.assertNotIn("与 GeoVINS / NGPS / PiLoT v2 的关系", prompt)
        self.assertNotIn("与 GeoVINS / NGPS / PiLoT v2 的关系", renderer)


if __name__ == "__main__":
    unittest.main()
