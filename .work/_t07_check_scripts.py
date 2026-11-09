#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap07 — check whether script_*.json match the NEW 219-câu scripts."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

KB = {
    "vi": ("01_KICH_BAN/Tap07/kichban_tap07_23102026.md", "script_tap07.json"),
    "en": ("01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md", "script_tap07_EN.json"),
    "ja": ("01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md", "script_tap07_JA.json"),
}
for lang, (kb, js) in KB.items():
    els = parse_file(str(ROOT / kb))
    want = []
    for e in els:
        for i, s in enumerate(e.get("sentences") or [], 1):
            want.append((f"{e['id']}#{i}", s["text"]))
    p = W / js
    if not p.exists():
        print(f"[{lang}] {js} MISSING -> cần sinh lại ({len(want)} câu)")
        continue
    have = json.loads(p.read_text(encoding="utf-8"))
    got = []
    for e in have:
        for i, s in enumerate(e.get("sentences") or [], 1):
            got.append((f"{e['id']}#{i}", s["text"]))
    same_ids = [a[0] for a in want] == [g[0] for g in got]
    same_txt = [a[1] for a in want] == [g[1] for g in got]
    print(f"[{lang}] {js}: file={len(got)} câu · script mới={len(want)} câu · "
          f"id khớp={same_ids} · text khớp={same_txt}")
    if not same_txt:
        for a, g in zip(want, got):
            if a[1] != g[1]:
                print(f"    khác tại {a[0]}:\n      file: {g[1][:90]}\n      mới : {a[1][:90]}")
                break
