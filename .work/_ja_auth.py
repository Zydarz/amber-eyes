#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find which auth header the LLM gateway wants. Tries a few combos, prints status only."""
import json
from pathlib import Path

import httpx

AUTH = json.loads(Path(r"C:\Users\ADMIN\.minimax\local-runtime.auth.json").read_text(encoding="utf-8"))
TOKEN = AUTH["auth"]["accessToken"]
BASE = "https://agent.minimax.io/mavis/api/v1/llm/v1"
MODEL = "MiniMax-M3.1-Flash"

BODY = {
    "model": MODEL,
    "max_tokens": 64,
    "messages": [{"role": "user", "content": "Reply with exactly: PING-OK"}],
}

COMBOS = {
    "bearer-only": {"Authorization": f"Bearer {TOKEN}"},
    "xapikey-only": {"x-api-key": TOKEN},
    "both": {"Authorization": f"Bearer {TOKEN}", "x-api-key": TOKEN},
    "bearer+realuser": {"Authorization": f"Bearer {TOKEN}", "X-Real-User-ID": AUTH["auth"].get("realUserID", "")},
}

for name, hdr in COMBOS.items():
    h = {"Content-Type": "application/json"}
    h.update(hdr)
    try:
        with httpx.Client(timeout=60) as c:
            r = c.post(f"{BASE}/messages", headers=h, json=BODY)
        body = r.text[:300].replace("\n", " ")
        print(f"[{name}] HTTP {r.status_code} :: {body}")
    except Exception as e:
        print(f"[{name}] ERROR {type(e).__name__}: {e}")
