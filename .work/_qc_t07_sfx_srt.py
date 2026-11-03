#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC: sheet SFX Tap07 (cau co ton tai?) + spot-check SRT moi."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

script = json.loads((ROOT / ".work/script_tap07.json").read_text(encoding="utf-8-sig"))
sent = set()
for el in script:
    for i, s in enumerate(el.get("sentences") or [], 1):
        sent.add(f"{el['id']}#{i}")

sfx = json.loads((ROOT / ".work/sfx_tap07.json").read_text(encoding="utf-8-sig"))
print("=== sfx_tap07.json ===")
print("type:", type(sfx).__name__, "· keys:", list(sfx.keys())[:12] if isinstance(sfx, dict) else len(sfx))
bad = []
n = 0
if isinstance(sfx, dict):
    for k, v in sfx.items():
        if isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    n += 1
                    ids = []
                    for key in ("at", "cau", "sentence", "sid", "after"):
                        if key in item:
                            ids.append(str(item[key]))
                    for i in ids:
                        if re.fullmatch(r"\d\.\d+#\d+", i) and i not in sent:
                            bad.append((k, i))
            print(f"  {k}: {len(v)} muc")
else:
    for item in sfx:
        n += 1
print(f"  tong muc: {n} · tham chieu cau khong ton tai: {len(bad)}")
for b in bad[:20]:
    print("   ", b)

print()
print("=== SRT moi: spot-check ===")
srt = (ROOT / "02_SAN_XUAT/Tap07/xuat_ban/Tap07.srt").read_text(encoding="utf-8-sig")
blocks = [b for b in srt.strip().split("\n\n")]
print("so cue:", len(blocks))
tags = re.findall(r"\[([^\]]+)\]", srt)
from collections import Counter
print("tag:", Counter(tags))
# kiem tra cue cuoi + cac cue co tag N1/N2
for b in blocks:
    if "[BÀ ROY]" in b or "[SAMANTHA" in b:
        print("  ---")
        print("  " + b.replace("\n", " | "))
        break
for b in blocks:
    if "[SAMANTHA" in b:
        print("  ---")
        print("  " + b.replace("\n", " | "))
        break
print("--- cue cuoi ---")
print(blocks[-1])
# kiem tra trung timestamp
ts = re.findall(r"(\d\d):(\d\d):(\d\d),(\d\d\d) --> (\d\d):(\d\d):(\d\d),(\d\d\d)", srt)
prev_end = None
prob = []
for t in ts:
    a = int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2]) + int(t[3]) / 1000
    b = int(t[4]) * 3600 + int(t[5]) * 60 + int(t[6]) + int(t[7]) / 1000
    if b <= a:
        prob.append(("end<=start", a, b))
    if prev_end is not None and a < prev_end - 0.01:
        prob.append(("overlap", prev_end, a))
    prev_end = b
print(f"timestamp van: {len(ts)} · loi: {len(prob)}")
for p in prob[:8]:
    print("   ", p)
durs = [(int(t[4]) * 3600 + int(t[5]) * 60 + int(t[6]) + int(t[7]) / 1000)
         - (int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2]) + int(t[3]) / 1000)
         for t in ts]
print("do dai cue toi da:", round(max(durs), 3))
