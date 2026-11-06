#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — so CÂU CŨ vs CÂU MỚI theo cùng mã (X.YY#N).

Đo: bao nhiêu câu giữ nguyên nội dung, bao nhiêu câu đã đổi.
Câu đổi nội dung ⇒ chữ trên hình của câu đó phải soạn lại.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402


def norm(s):
    return " ".join(re.sub(r"[^\w\s]", " ", s.lower(), flags=re.UNICODE).split())


CASES = [
    ("VN", "01_KICH_BAN/Tap05/kichban_tap05_23102026.md", "script_tap05.json"),
    ("EN", "01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md", "script_tap05_EN.json"),
    ("JA", "01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md", "script_tap05_JA.json"),
]

for lang, kb, old_json in CASES:
    new = parse_file(str(ROOT / kb))
    old = json.loads((W / old_json).read_text(encoding="utf-8"))
    o = {s["id"]: s["text"] for e in old if e.get("kind") == "LOI" for s in e.get("sentences", [])}
    n = {s["id"]: s["text"] for e in new if e.get("kind") == "LOI" for s in e.get("sentences", [])}
    same = changed = 0
    ch = []
    for k in sorted(set(o) & set(n), key=lambda x: (int(x.split(".")[0]), int(x.split("#")[0].split(".")[1]), int(x.split("#")[1]))):
        if norm(o[k]) == norm(n[k]):
            same += 1
        else:
            changed += 1
            ch.append(k)
    print("=" * 78)
    print(f"### {lang}: câu giữ nguyên {same} · câu ĐỔI NỘI DUNG {changed} · câu mới thêm {len(set(n)-set(o))}")
    print("  câu đổi:", " ".join(ch))
