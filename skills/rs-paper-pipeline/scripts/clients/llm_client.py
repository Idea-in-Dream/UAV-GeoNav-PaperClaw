#!/usr/bin/env python3
from __future__ import annotations

import json
import urllib.request

from pipeline_config import install_urllib_proxy, load_config


CONFIG = load_config()
install_urllib_proxy()


def load_prompt(filename: str) -> str:
    path = CONFIG.prompts_dir / filename
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def build_chat_payload(
    prompt: str,
    max_tokens: int,
    thinking: str = "disabled",
) -> dict:
    thinking_mode = (thinking or "disabled").strip().lower()
    if thinking_mode not in {"enabled", "disabled"}:
        raise ValueError("thinking must be 'enabled' or 'disabled'")
    return {
        "model": CONFIG.llm_model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
        "thinking": {"type": thinking_mode},
        "stream": False,
    }


def call_llm(
    prompt: str,
    max_tokens: int = 4096,
    timeout: int = 300,
    thinking: str = "disabled",
) -> str:
    if not CONFIG.llm_api_key:
        raise RuntimeError("Missing required environment variable: LLM_API_KEY")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CONFIG.llm_api_key}",
    }
    data = build_chat_payload(prompt, max_tokens, thinking=thinking)
    try:
        req = urllib.request.Request(
            CONFIG.llm_api_url,
            data=json.dumps(data).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return payload["choices"][0]["message"]["content"]
    except Exception as exc:
        print(f"    ❌ LLM 调用失败: {exc}")
        return ""
