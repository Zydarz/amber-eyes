#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem che phu de T03: text cua phu de phai khop loi thoai trong timeline (== kich ban).

- Moi cau thoai -> cac cue phu de nam trong [start, end] -> noi dung phai khop.
- Chuoi (khong dau) de so sanh.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
OUT = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\xuat_ban")

tl = json.loads((W / "timeline_s_t03.json").read_text(encoding="utf-8-sig"))
srt = (OUT / "Tap03.srt").read_text(encoding="utf-8-sig")

cues = []
for b in re.split(r"\n\s*\n", srt.strip()):
    L = b.splitlines()
    if len(L) < 3:
        continue
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    a = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    txt = " ".join(x.strip() for x in L[2:] if x.strip())
    cues.append((a, z, txt))


def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[^0-9a-zA-ZÀ-ỹ]+", " ", s.lower())
    return " ".join(s.split())


ok = True
missing, mismatch, cover = [], [], []
for it in tl["items"]:
    a, z = it["start"], it["end"]
    sel = [c for c in cues if c[0] >= a - 0.35 and c[1] <= z + 0.35]
    if not sel:
        sel = [c for c in cues if c[0] < z and c[1] > a]
    if not sel:
        missing.append(it["id"])
        continue
    got = norm(" ".join(c[2] for c in sel))
    want = norm(it["text"])
    if want and want not in got and got not in want:
        mismatch.append((it["id"], want[:70], got[:70]))
    cover.append((it["id"], len(sel)))

print(f"Cau thoai: {len(tl['items'])} · cue phu de: {len(cues)}")
print(f"Khong co cue nao che cau: {len(missing)} {missing[:10]}")
print(f"Noi dung phu de KHOP kich ban: {len(tl['items']) - len(missing) - len(mismatch)}/{len(tl['items'])}")
if mismatch:
    print("\nSAI (5 dong dau):")
    for m in mismatch[:5]:
        print(f"  [{m[0]}]")
        print(f"    kich ban: {m[1]}")
        print(f"    phu de  : {m[2]}")
multi = [c for c in cover if c[1] > 1]
print(f"Cau duoc tach thanh nhieu cue: {len(multi)} (vi du: {[c[0] for c in multi[:6]]})")
if missing or mismatch:
    ok = False
print("\nKET QUA:", "DAT" if ok else "CO VIEC")
sys.exit(0 if ok else 1)
