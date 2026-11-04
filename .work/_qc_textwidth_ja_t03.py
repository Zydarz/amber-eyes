#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo bề rộng chữ trên hình JA so với bề rộng khung của từng template.

Bề rộng khung lấy đúng từ build_video3.py:
  T1 : text_block(spec, 1180 hoặc 1240)   T8 : 880
  T9 : 1050                                T10: 1500
Font JA: YuGothB.ttc (head/lab), YuGothM.ttc (sub/quote/mono).
Mục tiêu: tiêu đề đậm (head) nên nằm trên 1 dòng; dòng con có thể xuống 2 dòng.
"""
import json
import re
import sys
from pathlib import Path

from PIL import ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
FONTS = Path(r"C:\Windows\Fonts")


def F(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


F_HEAD = lambda s=64: F("YuGothB.ttc", s)
F_LAB = lambda s=26: F("YuGothB.ttc", s)
F_SUB = lambda s=32: F("YuGothM.ttc", s)
F_QUOTE = lambda s=56: F("YuGothM.ttc", s)
F_GEO = lambda s=72: F("YuGothB.ttc", s)
F_MONO = lambda s=28: F("YuGothM.ttc", s)

TPL = {
    "T1": (1180, {"head": F_HEAD(66), "lab": F_LAB(28), "quote": F_QUOTE(48), "sub": F_SUB(34)}),
    "T2": (1000, {"head": F_HEAD(60), "lab": F_LAB(28), "quote": F_QUOTE(48), "sub": F_SUB(34)}),
    "T3": (1000, {"head": F_HEAD(60), "lab": F_LAB(28), "quote": F_QUOTE(48), "sub": F_SUB(34)}),
    "T4": (1000, {"head": F_HEAD(60), "lab": F_LAB(28), "quote": F_QUOTE(48), "sub": F_SUB(34)}),
    "T5": (1000, {"head": F_HEAD(60), "lab": F_LAB(28), "quote": F_QUOTE(48), "sub": F_SUB(34)}),
    "T8": (880, {"head": F_SUB(42), "lab": F_SUB(42), "quote": F_QUOTE(48), "sub": F_SUB(42)}),
    "T9": (1050, {"head": F_HEAD(70), "lab": F_LAB(28), "quote": F_QUOTE(48), "sub": F_SUB(34)}),
    "T10": (1500, {"head": F_GEO(70), "lab": F_MONO(30), "quote": F_QUOTE(48), "sub": F_SUB(34)}),
}

shots = json.loads((ROOT / ".work/shots_JA_t03.json").read_text(encoding="utf-8-sig"))["shots"]
rows = []
for s in shots:
    tpl = s.get("template") or "T1"
    lim, fonts = TPL.get(tpl, TPL["T1"])
    for seg in s["segments"]:
        for kind, txt in seg["elems"]:
            if kind == "bold":
                f, role = fonts["head"], "HEAD"
            elif kind == "quote":
                f, role = fonts["quote"], "QUOTE"
            elif kind == "ital":
                f, role = fonts["lab"] if tpl == "T9" and len(txt) < 40 else fonts["sub"], "SUB"
            else:
                continue
            if not txt.strip():
                continue
            w = f.getlength(txt)
            rows.append((s["id"], tpl, role, round(w), lim, txt))

over = [r for r in rows if r[3] > r[4]]
print(f"do {len(rows)} phan tu chu tren hinh · vuot khung = {len(over)}")
for sid, tpl, role, w, lim, txt in over:
    print(f"  {sid} [{tpl}/{role}] {w}px > {lim}px :: {txt[:70]}")
print()
print("--- HEAD vuot khang (nen rut gon) ---")
for r in over:
    if r[2] == "HEAD":
        print(f"  {r[0]} [{r[1]}] {r[3]}px > {r[4]}px :: {r[5]}")
