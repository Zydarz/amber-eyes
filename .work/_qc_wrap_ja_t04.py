#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check wrapping for JA Tap04: orphan chars, broken Latin words."""
import json
import re
import sys
from pathlib import Path

from PIL import ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
FONTS = Path(r"C:\Windows\Fonts")
F = lambda n, s: ImageFont.truetype(str(FONTS / n), s)

NO_START = "、。，．・？！：；ー）〕］｝」』〉》"


def wrap_ja(text, fnt, width):
    lines, cur = [], ""
    for c in text:
        t = cur + c
        if fnt.getlength(t) <= width or not cur:
            cur = t
        elif c in NO_START:
            cur = t
        else:
            lines.append(cur)
            cur = c
    if cur:
        lines.append(cur)
    return lines


TPL = {
    "T1": (1180, {"head": F("YuGothB.ttc", 66), "sub": F("YuGothM.ttc", 34), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothB.ttc", 28)}),
    "T2": (1080, {"head": F("YuGothB.ttc", 60), "sub": F("YuGothM.ttc", 34), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothB.ttc", 28)}),
    "T3": (1080, {"head": F("YuGothB.ttc", 60), "sub": F("YuGothM.ttc", 34), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothB.ttc", 28)}),
    "T4": (1080, {"head": F("YuGothB.ttc", 60), "sub": F("YuGothM.ttc", 34), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothB.ttc", 28)}),
    "T5": (1080, {"head": F("YuGothB.ttc", 60), "sub": F("YuGothM.ttc", 34), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothB.ttc", 28)}),
    "T8": (880, {"head": F("YuGothM.ttc", 42), "sub": F("YuGothM.ttc", 42), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothM.ttc", 42)}),
    "T9": (1050, {"head": F("YuGothB.ttc", 70), "sub": F("YuGothM.ttc", 34), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothB.ttc", 28)}),
    "T10": (1500, {"head": F("YuGothB.ttc", 70), "sub": F("YuGothM.ttc", 34), "quote": F("YuGothM.ttc", 48), "lab": F("YuGothM.ttc", 30)}),
}

shots = json.loads((ROOT / ".work/shots_JA_t04.json").read_text(encoding="utf-8-sig"))["shots"]
issues = []
for s in shots:
    tpl = s.get("template") or "T1"
    lim, fonts = TPL.get(tpl, TPL["T1"])
    for seg in s["segments"]:
        for kind, txt in seg["elems"]:
            f = fonts.get("head" if kind == "bold" else "quote" if kind == "quote" else "sub", fonts["sub"])
            lines = wrap_ja(txt, f, lim)
            if len(lines) > 1 and len(lines[-1]) <= 1 and lines[-1] not in "」』）":
                issues.append((s["id"], f"dòng cuối cụt: {lines[-1]}", txt[:30]))
            # Check broken Latin words
            for i in range(len(lines) - 1):
                if re.search(r"[A-Za-z]$", lines[i]) and re.search(r"^[A-Za-z]", lines[i + 1]):
                    issues.append((s["id"], f"cắt giữa từ Latin: {lines[i][-5:]}|{lines[i+1][:5]}", txt[:30]))

print(f"Tổng issues wrap: {len(issues)}")
for iss in issues:
    print("  ISSUE:", iss)
print("KẾT QUẢ:", "PASS" if len(issues) == 0 else "FAIL")
