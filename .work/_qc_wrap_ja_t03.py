#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mô phỏng wrap JA của build_video3.wrap() để tìm:
  - dòng cuối quá ngắn (<=3 ký tự) -> coi như lỗi hiển thị
  - cắt giữa một từ Latin (vd "MIN|DHUNTER")
"""
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

shots = json.loads((ROOT / ".work/shots_JA_t03.json").read_text(encoding="utf-8-sig"))["shots"]
seen = set()
issues = []
for s in shots:
    tpl = s.get("template") or "T1"
    lim, fonts = TPL.get(tpl, TPL["T1"])
    for seg in s["segments"]:
        for kind, txt in seg["elems"]:
            if kind not in ("bold", "quote"):
                continue
            f = fonts["head"] if kind == "bold" else fonts["quote"]
            key = (s["id"], kind, txt)
            if key in seen:
                continue
            seen.add(key)
            lines = wrap_ja(txt, f, lim)
            if len(lines) < 2:
                continue
            last = lines[-1]
            orphan = len(last.strip()) <= 3
            latin_break = bool(re.match(r"^[\x00-\x7F]+$", last.strip())) and len(last.strip()) >= 2 and \
                bool(re.search(r"[A-Za-z]$", lines[-2].strip()))
            if orphan or latin_break:
                issues.append((s["id"], tpl, kind, lines, orphan, latin_break))

print(f"pham loi xuong dong xau = {len(issues)}")
for sid, tpl, kind, lines, orphan, latin in issues:
    tag = "ORPHAN" if orphan else "CUT-LATIN"
    print(f"  [{tag}] {sid} {tpl}/{kind}")
    for l in lines:
        print(f"      | {l}")
