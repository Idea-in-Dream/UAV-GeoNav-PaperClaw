from pathlib import Path
from unittest.mock import patch
import json
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients.arxiv_client import has_remote_sensing_signal
from daily_arxiv_cross_filter import has_ai_signal, llm_cross_filter
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

    def test_ordinary_detection_and_tracking_are_not_prefiltered(self):
        for paper in self.cases["negative"]:
            text = f"{paper['title']}\n{paper['abstract']}"
            with self.subTest(paper=paper["name"]):
                self.assertFalse(has_remote_sensing_signal(text))

    def test_structured_llm_decisions_keep_required_cases_and_exclude_detection(self):
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
                {"arxiv_id": paper["arxiv_id"], "reason": "普通检测或跟踪"}
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
        }
        self.assertTrue(required.issubset(set(config["rs_query_terms"])))

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
