#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Try the managed OAuth token against the LLM gateway (both protocols)."""
import json
from pathlib import Path

import httpx

AUTHJ = json.loads(Path(r"C:\Users\ADMIN\.minimax\auth\prod\en\mcode-public\auth.json").read_text(encoding="utf-8"))
rec = list(AUTHJ["records"].values())[0]
TOKEN = rec["accessToken"]
BASE = "https://agent.minimax.io/mavis/api/v1/llm/v1"
MODEL = "MiniMax-M3.1-Flash"

TESTS = [
    ("anthropic/messages + bearer", f"{BASE}/messages", "anthropic"),
    ("chat/completions + bearer", f"{BASE}/chat/completions", "openai"),
]

for name, url, kind in TESTS:
    if kind == "anthropic":
        body = {"model": MODEL, "max_tokens": 64,
                "messages": [{"role": "user", "content": "Reply with exactly: PING-OK"}]}
    else:
        body = {"model": MODEL, "max_tokens": 64,
                "messages": [{"role": "user", "content": "Reply with exactly: PING-OK"}]}
    h = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
    try:
        with httpx.Client(timeout=60) as c:
            r = c.post(url, headers=h, json=body)
        print(f"[{name}] HTTP {r.status_code} :: {r.text[:400]}")
    except Exception as e:
        print(f"[{name}] ERROR {type(e).__name__}: {e}")
