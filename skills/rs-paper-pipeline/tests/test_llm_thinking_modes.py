from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from clients.llm_client import build_chat_payload
from services.paper_analysis import summarize_paper, translate_text


class LLMThinkingModesTest(unittest.TestCase):
    def test_chat_payload_supports_enabled_and_disabled_modes(self):
        disabled = build_chat_payload("filter", 100, thinking="disabled")
        enabled = build_chat_payload("analyze", 100, thinking="enabled")

        self.assertEqual(disabled["thinking"], {"type": "disabled"})
        self.assertEqual(enabled["thinking"], {"type": "enabled"})

    def test_translation_forces_thinking_disabled(self):
        with patch("services.paper_analysis.call_llm", return_value="翻译") as llm_mock:
            translate_text("source")

        self.assertEqual(llm_mock.call_args.kwargs["thinking"], "disabled")

    def test_full_paper_analysis_uses_configured_thinking_mode(self):
        response = "摘要翻译: 中文摘要内容足够用于测试。\n" + "\n".join(
            f"A{i}: 第{i}项结构化分析结论和证据。" for i in range(1, 13)
        )
        config = SimpleNamespace(llm_thinking_mode="enabled")

        with patch("services.paper_analysis.CONFIG", config):
            with patch("services.paper_analysis.call_llm", return_value=response) as llm_mock:
                analysis = summarize_paper("Title", "Author", "Abstract", "Full text")

        self.assertEqual(analysis["q12"], "第12项结构化分析结论和证据。")
        self.assertEqual(llm_mock.call_args.kwargs["thinking"], "enabled")

    def test_invalid_thinking_mode_is_rejected(self):
        with self.assertRaises(ValueError):
            build_chat_payload("prompt", 100, thinking="auto")


if __name__ == "__main__":
    unittest.main()
