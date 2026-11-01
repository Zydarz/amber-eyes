#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""quet moi file TTS EN T2: duoi im lang, dau im lang, do dai - so voi audio MiniMax cu."""
import json
import struct
import sys
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
AD = W / "audio_s_higgs_EN_t02"

man = {m["id"]: m for m in json.loads((W / "tts_manifest_EN_t02.json").read_text(encoding="utf-8-sig"))}

old_dur = {}
r = json.loads(__import__("subprocess").run(
    ["git", "-C", str(ROOT), "show", "HEAD:.work/timeline_s_EN_t02.json"],
    capture_output=True).stdout.decode("utf-8-sig"))
for i in r["items"]:
    old_dur[i["id"]] = i["end"] - i["start"]


def envelope(p):
    with wave.open(str(p), "rb") as wf:
        sr = wf.getframerate()
        n = wf.getnframes()
        raw = wf.readframes(n)
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if wf.getnchannels() > 1:
        x = x.reshape(-1, wf.getnchannels()).mean(axis=1)
    win = max(1, int(sr * 0.02))
    k = len(x) // win
    e = np.abs(x[:k * win]).reshape(k, win).max(axis=1)
    return sr, x, e


def edges(e, sr, thr_db=-45.0, win_s=0.02):
    thr = 10 ** (thr_db / 20)
    idx = np.where(e > thr)[0]
    if len(idx) == 0:
        return None, None, None
    lead = idx[0] * win_s
    tail = (len(e) - idx[-1] - 1) * win_s
    return lead, tail, len(e) * win_s


print(f"{'id':<10}{'dur':>8}{'speech':>8}{'lead':>7}{'tail':>8}{'old':>8}  {'flag'}")
print("-" * 74)
bad = []
for sid in sorted(man, key=lambda s: [int(p) for p in s.replace("#", ".").split(".")]):
    f = man[sid]["file"]
    p = AD / f
    if not p.exists():
        p = p.with_suffix(".wav")
    if not p.exists():
        print(f"{sid:<10}  THIEU FILE {f}")
        continue
    sr, x, e = envelope(p)
    lead, tail, total = edges(e, sr)
    if lead is None:
        bad.append((sid, total, tail, "IM LANG TOAN BO"))
        print(f"{sid:<10}{total:>8.2f}{0:>8.2f}{'-':>7}{'-':>8}{old_dur.get(sid,0):>8.2f}  <- rong")
        continue
    speech = total - lead - tail
    flag = ""
    if tail > 3.0:
        flag = f"<<< DUOI IM LANG {tail:.1f}s"
    elif tail > 1.5:
        flag = f"<< duoi im lang {tail:.1f}s"
    if flag:
        bad.append((sid, total, tail, flag))
    print(f"{sid:<10}{total:>8.2f}{speech:>8.2f}{lead:>7.2f}{tail:>8.2f}"
          f"{old_dur.get(sid,0):>8.2f}  {flag}")

print()
print("=" * 74)
print(f"TONG {len(bad)} file co van de duoi im lang:")
for sid, total, tail, flag in sorted(bad, key=lambda x: -x[2]):
    print(f"  {sid:<10} {total:7.2f}s  tail {tail:6.2f}s   {flag}")
