from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from repair_issue_format import repair_issue_body, repaired_labels
from services.labels import has_confirmed_public_code
from services.paper_analysis import format_resource_links_md


class IssueFormatRepairTest(unittest.TestCase):
    def test_removes_obsolete_baseline_relation_section(self):
        body = """# Paper

### 复现难度
中

### 与 GeoVINS / NGPS / PiLoT v2 的关系
不需要的比较内容

### 对当前无人机定位项目的价值
可作为检索模块。
"""

        repaired = repair_issue_body("Paper", body)

        self.assertNotIn("GeoVINS / NGPS / PiLoT v2", repaired)
        self.assertIn("### 对当前无人机定位项目的价值", repaired)

    def test_bare_url_before_chinese_parenthesis_is_safely_wrapped(self):
        text = "代码URL：https://example.com/code/（尚未发布）"

        self.assertEqual(
            format_resource_links_md(text),
            "代码URL：<https://example.com/code/>（尚未发布）",
        )

    def test_removes_repeated_resource_field_caption(self):
        body = """# Paper

### 代码链接
代码链接与开放资源
- 论文中未发现公开代码链接。

### 是否融合 VIO/IMU
未融合。
"""

        repaired = repair_issue_body("Paper", body)

        self.assertEqual(repaired.count("公开代码与资源"), 1)
        self.assertNotIn("代码链接与开放资源", repaired)

    def test_offnadirloc_uses_project_link_and_marks_code_unpublished(self):
        body = """# OffNadirLoc

### 代码链接
- 代码URL：https://montalario.github.io/offnadirloc/（will be released）。

### 是否融合 VIO/IMU
未融合。
"""

        repaired = repair_issue_body("OffNadirLoc", body)
        labels = repaired_labels(["Code-Available", "Dataset-Benchmark"], repaired)

        self.assertIn("[OffNadirLoc](https://montalario.github.io/offnadirloc/)", repaired)
        self.assertIn("代码：尚未发布", repaired)
        self.assertNotIn("Code-Available", labels)
        self.assertFalse(has_confirmed_public_code(repaired))

    def test_confirmed_repository_keeps_code_available(self):
        answer = "公开代码：[Repository](https://github.com/example/project)"

        self.assertTrue(has_confirmed_public_code(answer))
        self.assertIn("Code-Available", repaired_labels(["Code-Available"], "### 公开代码与资源\n" + answer))


if __name__ == "__main__":
    unittest.main()
