# -*- coding: utf-8 -*-
"""Tập 12 — quét từ khoá rủi ro chữ, BỎ các mệnh đề phủ định (no X / without X)."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RISK = [
    "titled", "labeled", "labelled", "inscribed", "newspaper", "reading", "writing",
    "labels", "label", "headline", "placard", "caption", "sign", "signage",
    "poster", "emblem", "crest", "badge", "nameplate", "letter", "lettering",
    "words", "text", "slogan", "motto", "engraved", "carved", "scrawl", "note",
    "memo", "document", "card", "ticket", "stamp", "number", "numbers", "dial",
    "scoreboard", "price", "brand", "logo", "chalk", "unlettered", "scroll",
]
jobs = json.loads(Path(".work/bg_jobs_tap12_new69.json").read_text(encoding="utf-8"))
flag = []
for j in jobs:
    p = j["prompt"].lower()
    # bỏ mệnh đề phủ định: "no X, " / "no X" / "without X"
    clean = re.sub(r"\b(?:no|without)\s+[a-z ]{0,40}?(?=,|\.|;|$)", " ", p)
    clean = re.sub(r"\bno\b", " ", clean)
    hits = sorted({w for w in RISK if re.search(r"\b" + re.escape(w), clean)})
    if hits:
        flag.append((j["name"], hits))

print(f"{len(jobs)} prompt · {len(flag)} có rủi ro thật (sau khi bỏ mệnh đề phủ định)\n")
for n, h in flag:
    print(f"  {n:45s} {h}")
if not flag:
    print("KHÔNG có từ khoá rủi ro thật.")
