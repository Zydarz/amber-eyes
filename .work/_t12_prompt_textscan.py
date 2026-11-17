# -*- coding: utf-8 -*-
"""Tập 12 — quét từ khoá rủi ro chữ trong prompt của 69 nền mới (A11 #171)."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
JOBS = Path(".work/bg_jobs_tap12_new69.json")
RISK = [
    "titled", "labeled", "labelled", "inscribed", "newspaper", "reading", "writing",
    "labels", "label", "headline", "placard", "caption", "sign", "signage", "banner",
    "banner", "poster", "banner", "emblem", "crest", "badge", "nameplate", "letter",
    "lettering", "words", "text", "slogan", "motto", "engraved", "carved", "scrawl",
    "note", "memo", "document", "paperwork", "card", "ticket", "stamp", "number",
    "numbers", "clock face", "dial", "scoreboard", "price", "brand", "logo",
]
jobs = json.loads(JOBS.read_text(encoding="utf-8"))
flag = []
for j in jobs:
    p = j["prompt"].lower()
    hits = sorted({w for w in RISK if re.search(r"\b" + re.escape(w), p)})
    if hits:
        flag.append((j["name"], hits, j["prompt"][:170]))

print(f"{len(jobs)} prompt · {len(flag)} có từ khoá rủi ro\n")
for n, h, p in flag:
    print(f"  {n}\n     hits: {h}\n     {p}\n")
if not flag:
    print("KHÔNG có từ khoá rủi ro.")
