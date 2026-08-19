import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients.github_ops import daily_report_matches_digest
from reconcile_daily_issue_set import load_stats
from run_rs_daily_workday import _date_already_completed, resolve_date_range, resolve_target_dates
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

    def test_pages_deploy_follows_successful_pipeline_workflows(self):
        workflow = (ROOT.parents[1] / ".github" / "workflows" / "deploy-pages.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("workflow_run:", workflow)
        self.assertIn("UAV GeoNav PaperClaw Schedule", workflow)
        self.assertIn("UAV GeoNav PaperClaw Backfill", workflow)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", workflow)
        self.assertIn("ref: main", workflow)

    def test_daily_schedule_runs_at_0807_beijing_time(self):
        workflow = (ROOT.parents[1] / ".github" / "workflows" / "rs-pipeline-schedule.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn('cron: "7 0 * * *"', workflow)
        self.assertIn("北京时间 08:07", workflow)
        self.assertIn("SCHEDULE_ATTEMPT ${attempt}/2", workflow)
        self.assertIn("retrying the full run in 60 seconds", workflow)

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

    def test_matching_empty_report_counts_as_completed(self):
        body = build_digest_with_llm(
            self.date,
            [],
            stats={"candidate_count": 10, "llm_selected_count": 0},
        )
        issue = SimpleNamespace(number=4, title=f"日报 {self.date}", body=body)
        repo = FakeRepo(issue, body.strip() + "\n")

        with patch("run_rs_daily_workday._get_repo", return_value=repo):
            completed, reason = _date_already_completed(self.date)

        self.assertTrue(completed)
        self.assertEqual(reason, "digest=#4 papers=0")

    def test_every_day_processes_previous_calendar_day(self):
        beijing_tz = timezone(timedelta(hours=8))
        monday = datetime(2026, 8, 3, 8, 0, tzinfo=beijing_tz)

        for offset in range(7):
            current = monday + timedelta(days=offset)
            expected = (current - timedelta(days=1)).strftime("%Y%m%d")
            with self.subTest(day=current.strftime("%A")):
                self.assertEqual(resolve_target_dates(current), [expected])

    def test_backfill_date_range_is_inclusive(self):
        self.assertEqual(
            resolve_date_range("20260730", "20260802"),
            ["20260730", "20260731", "20260801", "20260802"],
        )

    def test_backfill_date_range_rejects_invalid_ranges(self):
        with self.assertRaises(ValueError):
            resolve_date_range("20260802", "20260730")
        with self.assertRaises(ValueError):
            resolve_date_range("20260101", "20260401")

    def test_reconcile_accepts_zero_selected_papers(self):
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "stats.json"
            path.write_text(
                json.dumps({"date": self.date, "selected_arxiv_ids": []}),
                encoding="utf-8",
            )
            stats = load_stats(str(path), self.date)

        self.assertEqual(stats["selected_arxiv_ids"], [])


if __name__ == "__main__":
    unittest.main()
