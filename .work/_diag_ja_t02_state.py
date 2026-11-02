#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trạng thái hiện tại của bản JA Tap02: audio master vs timeline vs shots vs picture.mp4 cũ."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def dur(p):
    if not Path(p).exists():
        return None
    r = subprocess.run([str(FF), "-i", str(p)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    for line in (r.stderr or "").splitlines():
        if "Duration:" in line:
            ts = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = ts.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return None


def jload(p):
    p = Path(p)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8-sig"))


print("=== 1. FILE ===")
for rel in [
    "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp3",
    "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt",
    "02_SAN_XUAT/Tap02_JA/xuat_ban/thumbnail.png",
    ".work/timeline_s_JA_t02.json",
    ".work/shots_JA_t02.json",
    ".work/script_tap02_JA.json",
    ".work/acting_tap02_JA.json",
    ".work/video3_JA_t02/picture.mp4",
    ".work/video3_EN_t02/picture.mp4",
]:
    p = ROOT / rel
    ex = p.exists()
    d = dur(p) if ex and p.suffix in (".mp3", ".mp4") else None
    print(f"  {rel:<58} {'OK ' if ex else 'THIEU'} {d if d else ''}")

print("\n=== 2. TIMELINE JA t02 ===")
tl = jload(W / "timeline_s_JA_t02.json")
if tl:
    tot = tl.get("total")
    print("  total =", tot, "| keys:", list(tl.keys())[:12])
    items = tl.get("items") or tl.get("lines") or []
    print("  so phan tu =", len(items))
    if items:
        print("  dau:", json.dumps(items[0], ensure_ascii=False)[:220])
        print("  cuoi:", json.dumps(items[-1], ensure_ascii=False)[:220])

print("\n=== 3. SHOTS JA t02 ===")
sh = jload(W / "shots_JA_t02.json")
if sh:
    print("  type =", type(sh).__name__)
    if isinstance(sh, dict):
        print("  keys:", list(sh.keys())[:14])
        shots = sh.get("shots") or []
        for k in ("total", "n", "count", "timeline_total"):
            if k in sh:
                print(f"  {k} =", sh[k])
    elif isinstance(sh, list):
        shots = sh
    if shots:
        print("  so shot =", len(shots))
        print("  shot dau:", json.dumps(shots[0], ensure_ascii=False)[:400])
        print("  shot cuoi:", json.dumps(shots[-1], ensure_ascii=False)[:400])
        ends = [s.get("end", 0) for s in shots if isinstance(s, dict)]
        starts = [s.get("start", 0) for s in shots if isinstance(s, dict)]
        if ends:
            print("  start[0]=", starts[0], " end[-1]=", max(ends))

print("\n=== 4. SRT JA ===")
srt = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt"
if srt.exists():
    txt = srt.read_text(encoding="utf-8-sig", errors="replace")
    blocks = [b for b in txt.strip().split("\n\n") if b.strip()]
    print("  so khoi phu de =", len(blocks))
    print("  khoi cuoi:", blocks[-1].replace("\n", " | ")[:220] if blocks else "-")
