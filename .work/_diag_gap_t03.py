#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dieu tra: shot nao bat dau/TRIEU HON cau dau tien, va co cho trong giua cac shot khong?"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

tl = json.loads((W / "timeline_s_t03.json").read_text(encoding="utf-8-sig"))
shots = json.loads((W / "shots_t03.json").read_text(encoding="utf-8-sig"))["shots"]
SENT = {i["id"]: i for i in tl["items"]}

print("=== 1. SO KHOANG TRONG GIUA CAC SHOT ===")
gaps = []
for a, b in zip(shots, shots[1:]):
    g = round(b["start"] - a["end"], 3)
    if g > 0.001:
        gaps.append((a["id"], a["end"], b["id"], b["start"], g))
print(f"So khoang trong: {len(gaps)}")
for g in gaps[:20]:
    print(f"   {g[0]} ket {g[1]:.2f}  ->  {g[2]} bat dau {g[3]:.2f}   TRONG {g[4]:.2f}s")
if gaps:
    print(f"   Tong thoi luong trong: {sum(g[4] for g in gaps):.2f}s")
    print(f"   Tran toi da: {max(g[4] for g in gaps):.2f}s")

print("\n=== 2. DEVIAX shot.start - cau_dau.start ===")
dev = []
for s in shots:
    if not s["sentences"]:
        continue
    d = s["start"] - SENT[s["sentences"][0]]["start"]
    dev.append((s["id"], round(d, 3)))
pos = [d for _, d in dev if d > 0.001]
neg = [d for _, d in dev if d < -0.001]
print(f"Shot bat dau SAU cau dau (loi thoi bi bo qua): {len(pos)}")
for i, d in [(i, d) for i, d in dev if d > 0.001][:10]:
    print(f"   {i} +{d}")
print(f"Shot bat dau TRUOC cau dau (vao canh): {len(neg)} · bien do {min(neg):.3f} .. {max(neg):.3f}")

print("\n=== 3. DEVIAX shot.end - cau_cuoi.end ===")
dev2 = []
for s in shots:
    if not s["sentences"]:
        continue
    d = s["end"] - SENT[s["sentences"][-1]]["end"]
    dev2.append((s["id"], round(d, 3)))
over = sorted([d for _, d in dev2 if d > 0.05], reverse=True)
print(f"Shot vuot qua cau cuoi > 0,05 s: {len(over)} · lon nhat {over[:8] if over else 'khong co'}")

print("\n=== 4. SHOT NAO CO CAU, NHUNG CAU KE TIEP CHUA CO SHOT NAO BAO PHU ===")
covered = set()
for s in shots:
    covered.update(s["sentences"])
uncov = [i["id"] for i in tl["items"] if i["id"] not in covered]
print(f"Cau khong thuoc shot nao: {len(uncov)} {uncov[:10]}")
if uncov:
    for cid in uncov[:6]:
        it = SENT[cid]
        print(f"   [{cid}] {it['start']:.2f}-{it['end']:.2f} — {it['text'][:90]}")

print("\n=== 5. 5 SHOT DAU TIEN ===")
for s in shots[:6]:
    ss = s["sentences"]
    print(f"   {s['id']} {s['start']:8.2f}-{s['end']:8.2f}  sent={ss[:3]}  bg={s['bg']}")

print("\n=== 6. EBUR128: DOC DUNG DI DINH GHE ===")
for lbl, path in (("wav", W / "audio_master_t03.wav"),
                  ("mp4", Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\xuat_ban\Tap03_master.mp4"))):
    r = subprocess.run([str(FF), "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = r.stderr[-700:]
    pk = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", r.stderr)
    lu = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", r.stderr)
    print(f"   [{lbl}] LUFS={lu[-1] if lu else '?'} · PEAK={pk[-1] if pk else '?'} dBFS · (so peak doc duoc: {len(pk)})")
    if not pk:
        print("   ---- 200 ky tu cuoi stderr ----")
        print("   " + tail.replace("\n", "\n   "))
