#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra cuoi: so dong du lieu trong muc 4.2, so file WAV/BGM, so muc provenance."""
import glob
import io
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:\TEST\Gax\Audi"
TICK = chr(96)

d = io.open(os.path.join(ROOT, "02_SAN_XUAT", "Danh_Sach_SFX_Tap03-29.md"), encoding="utf-8").read()
sec = d.split("### 4.2.")[1].split("## 5.")[0]
rows = [l for l in sec.splitlines()
        if l.startswith("| ") and l.count("|") == 8 and TICK in l and not l.startswith("| # |")]
codes = [l.split("|")[2].strip().strip(TICK) for l in rows]
print("muc 4.2 : %d dong du lieu" % len(rows))
print("  ma trung nhau:", len(codes) - len(set(codes)))
print("  dong co ghi chu:", sum(1 for l in rows if l.split("|")[7].strip()))

wav = glob.glob(os.path.join(ROOT, "assets", "sfx", "**", "*.wav"), recursive=True)
print("tong WAV assets/sfx:", len(wav))
missing = [c for c in codes
           if not glob.glob(os.path.join(ROOT, "assets", "sfx", "**", c + ".wav"), recursive=True)]
print("  ma trong 4.2 chua co file:", len(missing), missing[:5])

bgm = glob.glob(os.path.join(ROOT, "assets", "bgm", "*.mp3"))
print("BGM assets/bgm:", len(bgm))

prov = json.load(io.open(os.path.join(ROOT, "provenance.json"), encoding="utf-8"))
yt = [e for e in prov if str(e.get("cong_cu", "")).startswith("YouTube Audio Library")]
print("provenance muc YouTube Audio Library:", len(yt))
print("  co track_youtube:", sum(1 for e in yt if e.get("track_youtube")))
