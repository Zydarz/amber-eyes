#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soi 6 shot EN bị QC báo lệch số + câu EN tương ứng."""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
os.environ["AE_EP"] = "03"
os.environ["AE_LANG"] = "en"
sys.path.insert(0, str(ROOT / ".work"))
import edition as ED  # noqa: E402

TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))
SENT = {it["id"]: it for it in TL["items"]}
SHOTS = {s["id"]: s for s in SH["shots"]}

# số trên hình + câu
def on_screen(s):
    out = []
    for seg in s["segments"]:
        for kind, t in seg["elems"]:
            out.append((kind, t))
    return out

TARGET = ["1-02", "1-03", "1-22", "2-05"]
for sid in TARGET:
    s = SHOTS[sid]
    print("=" * 78)
    print(f"SHOT {sid} · {s['template']} · nền {s['bg']}")
    print(f"  câu: {s['sentences']}")
    for x in s["sentences"]:
        print(f"    {x} :: {SENT[x]['text']}")
    for kind, t in on_screen(s):
        nums = re.findall(r"\d[\d.,]*", t)
        print(f"  [{kind}] {t!r}   -> số trên hình: {nums}")
    print(f"  flags: {s['flags']}")

print("\n" + "=" * 78)
print("TẤT CẢ SỐ TRÊN HÌNH vs SỐ TRONG CÂU (toàn bộ shot EN)")
for sid, s in SHOTS.items():
    ctx = " ".join(SENT[x]["text"] for x in s["sentences"])
    allowed = set(re.findall(r"\d+", ctx))
    hits = []
    for kind, t in on_screen(s):
        for m in re.findall(r"\d[\d.,]*", t):
            if m.rstrip(".,") not in allowed:
                hits.append((m, kind, t[:70]))
    if hits:
        print(f"  {sid}: {hits}")
