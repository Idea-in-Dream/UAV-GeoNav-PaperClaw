from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients.github_ops import daily_report_matches_digest
from run_rs_daily_workday import _date_already_completed
from services.digest_builder import UAV_GEONAV_REPORT_MARKER, build_digest_with_llm


class FakeRepo:
    def __init__(self, issue, report_text):
        self.issue = issue
        self.report_text = report_text

    def get_issues(self, state="open"):
        return [self.issue]

    def get_contents(self, path):
        return SimpleNamespace(decoded_content=self.report_text.encode("utf-8"))


class DailyReportCompletionTest(unittest.TestCase):
    def setUp(self):
        self.date = "20260722"
        self.body = (
            "# 日报 20260722\n\n"
            "| 标题 | Issue |\n"
            "|---|---|\n"
            "| RIM | [#1](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/1) |"
        )
        self.issue = SimpleNamespace(
            number=3,
            title=f"日报 {self.date}",
            body=self.body,
        )

    def test_report_matches_current_digest_body(self):
        repo = FakeRepo(self.issue, self.body.strip() + "\n")

        self.assertTrue(daily_report_matches_digest(repo, self.date, self.issue))

    def test_generated_report_has_pages_scope_marker(self):
        report = build_digest_with_llm(
            self.date,
            [],
            stats={"candidate_count": 0, "llm_selected_count": 0},
        )

        self.assertIn(UAV_GEONAV_REPORT_MARKER, report)

    def test_stale_inherited_report_does_not_count_as_completed(self):
        repo = FakeRepo(
            self.issue,
            "# 日报 20260722\n\n[#950](https://github.com/thinson/RS-PaperClaw/issues/950)\n",
        )

        with patch("run_rs_daily_workday._get_repo", return_value=repo):
            completed, reason = _date_already_completed(self.date)

        self.assertFalse(completed)
        self.assertEqual(reason, "daily report file does not match digest issue")

    def test_matching_report_with_linked_paper_counts_as_completed(self):
        repo = FakeRepo(self.issue, self.body.strip() + "\n")

        with patch("run_rs_daily_workday._get_repo", return_value=repo):
            completed, reason = _date_already_completed(self.date)

        self.assertTrue(completed)
        self.assertEqual(reason, "digest=#3 papers=1")


if __name__ == "__main__":
    unittest.main()
