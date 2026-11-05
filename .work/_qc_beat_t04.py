#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — kiểm cụm beat (cột Beat) có còn trong câu mới không.

Cột Beat ghi `... ở "cụm từ"` — renderer bắn SFX đúng lúc đọc tới cụm đó.
Cụm phải nằm trong câu đang đọc của shot, nếu không SFX sẽ không bao giờ kích hoạt.

Dùng:  py -3 .work/_qc_beat_t04.py [vi|en|ja]
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

W = ROOT / ".work"
LANG = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
KB = {"vi": "01_KICH_BAN/Tap04/kichban_tap04_23102026.md",
      "en": "01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md",
      "ja": "01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md"}[LANG]
idx = {}
for el in parse_file(str(ROOT / KB)):
    if el["kind"] == "LOI":
        idx[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]
sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
BO = W / f"_t04_beat_{LANG}.json"
OVER = json.loads(BO.read_text(encoding="utf-8")) if BO.exists() else {}


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"')
    return " ".join(re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE).split())


bad = []
for r in sk["rows"]:
    if r["kind"] != "shot":
        continue
    beat = OVER.get(r["sid"], r["cells"][6])
    eid, a, b = r["spans"][0]
    ctx = norm(" ".join(t for _, t in idx[eid][a - 1:b]))
    for phrase in re.findall(r"\"([^\"]+)\"", beat):
        f = norm(phrase)
        if f and f not in ctx:
            bad.append((r["sid"], phrase, r["from"]))
print(f"[{LANG}] shot có beat: {sum(1 for r in sk['rows'] if r['kind'] == 'shot' and r['cells'][6].strip() not in ('', '—'))} · cụm KHÔNG khớp: {len(bad)}")
for sid, ph, frm in bad:
    print(f"  ✗ {sid} (cũ {frm}): «{ph}»")
