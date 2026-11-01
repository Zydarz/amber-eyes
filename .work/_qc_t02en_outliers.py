#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quet cau lech nhiep: so sanh do dai cau EN moi (Higgs) voi cu (MiniMax)."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

new = json.loads((W / "timeline_s_EN_t02.json").read_text(encoding="utf-8-sig"))
r = subprocess.run(["git", "-C", str(ROOT), "show", "HEAD:.work/timeline_s_EN_t02.json"],
                   capture_output=True)
old = json.loads(r.stdout.decode("utf-8-sig")) if r.returncode == 0 else None

O = {i["id"]: i for i in old["items"]} if old else {}
N = {i["id"]: i for i in new["items"]}

print("=" * 92)
print("QUET CAU LECH NHIEP — Tap 02 EN")
print("=" * 92)
print(f"{'id':<10}{'OLD s':>9}{'NEW s':>9}{'delta':>9}{'x':>7}  text")
print("-" * 92)

rows = []
for sid, n in N.items():
    dn = n["end"] - n["start"]
    do = (O[sid]["end"] - O[sid]["start"]) if sid in O else None
    ratio = dn / do if do else 0
    if dn > 20 or (do and (ratio > 2.2 or ratio < 0.55)):
        rows.append((dn, sid, do, ratio, n["text"]))
for dn, sid, do, ratio, txt in sorted(rows, reverse=True):
    rs = f"{ratio:.2f}" if do else "-"
    print(f"{sid:<10}{(do if do else 0):>9.2f}{dn:>9.2f}{(dn-do if do else 0):>+9.2f}{rs:>7}  {txt[:52]}")

print()
print("--- CAU > 20s (dung nhiep) ---")
long_s = [(i["end"] - i["start"], i["id"]) for i in new["items"] if i["end"] - i["start"] > 20]
for d, sid in sorted(long_s, reverse=True):
    print(f"  {sid:<10} {d:6.2f}s   (cu: {O[sid]['end']-O[sid]['start']:.2f}s)" if sid in O else f"  {sid:<10} {d:6.2f}s")
print(f"  tong {len(long_s)} cau > 20s")

print()
print("--- PHAN BO DO DAI CAU ---")
ds = sorted(i["end"] - i["start"] for i in new["items"])
import statistics as st
print(f"  min {ds[0]:.2f} · p25 {ds[len(ds)//4]:.2f} · median {st.median(ds):.2f} · "
      f"p75 {ds[len(ds)*3//4]:.2f} · max {ds[-1]:.2f}  ·  TB {sum(ds)/len(ds):.2f}")
if old:
    do = sorted(i["end"] - i["start"] for i in old["items"])
    print(f"  (cu: min {do[0]:.2f} · median {st.median(do):.2f} · max {do[-1]:.2f} · TB {sum(do)/len(do):.2f})")

print()
print("--- DO DAI FILE TTS THUC TE (audio_s_higgs_EN_t02) ---")
man = {m["id"]: m for m in json.loads((W / "tts_manifest_EN_t02.json").read_text(encoding="utf-8-sig"))}
AD = W / "audio_s_higgs_EN_t02"
suspect = []
for sid in [i["id"] for i in new["items"]]:
    f = man[sid]["file"]
    p = AD / f
    if not p.exists():
        p = p.with_suffix(".wav")
    if not p.exists():
        print(f"  {sid}: THIEU FILE {f}")
        continue
    rr = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration",
                         "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                        capture_output=True, text=True)
    try:
        dur = float(rr.stdout.strip())
    except Exception:
        continue
    if dur > 20 or dur < 0.6:
        suspect.append((dur, sid, f))
for dur, sid, f in sorted(suspect, reverse=True):
    print(f"  {sid:<10} {dur:7.2f}s  {f}")
print(f"  tong {len(suspect)} file ban lệch (<0.6s hoac >20s)")
