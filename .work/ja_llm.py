#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ja_llm — client gọi MiniMax qua gateway (anthropic /messages) dùng token OAuth của runtime.

Gateway: https://agent.minimax.io/mavis/api/v1/llm/v1/messages
Auth: token trong %USERPROFILE%\.minimax\auth\prod\en\mcode-public\auth.json (Bearer).
Token được đọc lại từ đĩa mỗi lần gọi (runtime tự refresh) + retry khi 401.
"""
import json
import time
from pathlib import Path

import httpx

AUTH_JSON = Path(r"C:\Users\ADMIN\.minimax\auth\prod\en\mcode-public\auth.json")
BASE = "https://agent.minimax.io/mavis/api/v1/llm/v1/messages"
DEFAULT_MODEL = "MiniMax-M3.1-Flash"  # free


def _token() -> str:
    data = json.loads(AUTH_JSON.read_text(encoding="utf-8"))
    rec = max(data["records"].values(), key=lambda r: r.get("expiresAtMs", 0))
    return rec["accessToken"]


def call(prompt: str, system: str = "", model: str = DEFAULT_MODEL, *,
         max_tokens: int = 8192, temperature: float = 0.2, timeout: float = 300,
         thinking: bool = True, retries: int = 4) -> str:
    """Gọi 1 lần, trả về phần text của assistant (bỏ khối thinking).

    M3.1-Flash bắt buộc adaptive thinking => mặc định KHÔNG gửi tham số thinking.
    """
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }
    if system:
        body["system"] = system
    if thinking is False:
        body["thinking"] = {"type": "disabled"}
    last = None
    for attempt in range(retries):
        try:
            h = {"Content-Type": "application/json", "Authorization": f"Bearer {_token()}"}
            with httpx.Client(timeout=timeout) as c:
                r = c.post(BASE, headers=h, json=body)
            if r.status_code == 200:
                data = r.json()
                text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
                if text.strip():
                    return text
                last = "empty text"
            elif r.status_code == 429 or r.status_code >= 500:
                last = f"HTTP {r.status_code}: {r.text[:200]}"
            elif r.status_code == 401:
                last = f"HTTP 401: {r.text[:200]}"
                time.sleep(3)
            else:
                last = f"HTTP {r.status_code}: {r.text[:300]}"
                if r.status_code == 400:
                    break
        except Exception as e:  # network hiccup
            last = f"{type(e).__name__}: {e}"
        time.sleep(min(2 ** attempt, 20))
    raise RuntimeError(f"LLM call failed after {retries} tries: {last}")
