# -*- coding: utf-8 -*-
"""Quét mọi khoảng lặng trong một hồi, đối chiếu 2 file nhạc nền cạnh tranh.

Dùng để trả lời: master MỚI đang chơi file nào ở hồi đó (và bản CŨ chơi gì).
"""
import json
import pathlib
import subprocess
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BGM = ROOT / "assets" / "bgm"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
TMP = WORK / "_qc_tmp48"
TMP.mkdir(exist_ok=True)


def to48k_mono(mp3):
    out = TMP / (mp3.stem + "_48k.wav")
    if not out.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-i", str(mp3), "-ar", "48000",
                        "-ac", "1", str(out)], check=True)
    with wave.open(str(out), "rb") as w:
        n = w.getnframes()
        return np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0


def read_master(p):
    with wave.open(str(p), "rb") as w:
        n, ch, sr = w.getnframes(), w.getnchannels(), w.getframerate()
        d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return (d.reshape(-1, ch) if ch == 2 else d), sr


def max_corr(window, src):
    L = len(window)
    if len(src) <= L:
        return 0.0
    size = 1 << int(np.ceil(np.log2(len(src) + L)))
    corr = np.fft.irfft(np.fft.rfft(src, size) * np.conj(np.fft.rfft(window, size)), size)
    corr = corr[:len(src) - L + 1]
    k = int(np.argmax(np.abs(corr)))
    den = float(np.sqrt((window ** 2).sum() * (src[k:k + L] ** 2).sum())) or 1e-12
    return float(corr[k]) / den


CANDS = ["bgm_cello_sad.mp3", "bgm_cello_sad_v2.mp3", "bgm_sub_drone.mp3",
         "bgm_ambient_deep.mp3", "bgm_piano_minimal.mp3", "bgm_violin_heart.mp3",
         "bgm_piano_warm.mp3"]
SRC = {c: to48k_mono(BGM / c) for c in CANDS}

label, act_no = "T07 VN", 3
tl = json.loads((WORK / "timeline_s_t07.json").read_text(encoding="utf-8"))
items = tl["items"]
s, e = tl["acts"][str(act_no)]
gaps = []
for i in range(len(items) - 1):
    it, nx = items[i], items[i + 1]
    if it["act"] != act_no or nx["act"] != act_no:
        continue
    if nx["start"] - it["end"] >= 0.9:
        gaps.append(((it["end"] + nx["start"]) / 2, nx["start"] - it["end"]))
gaps = [g for g in gaps if s <= g[0] <= e]
print(f"{label} — H{act_no} ({s:.1f}-{e:.1f}s): {len(gaps)} khoang lang >= 0,9 s\n")

for tag, p in (("CU ", WORK / "_cu" / "audio_master_t07.wav.bak_bgm"),
               ("MOI", WORK / "audio_master_t07.wav")):
    a, sr = read_master(p)
    mono = a.mean(axis=1) if a.ndim > 1 else a
    agg = {c: (0.0, 0) for c in CANDS}
    for t, dur in gaps:
        i = int(t * sr)
        w = mono[i:i + sr]
        if w.size < sr:
            continue
        for c in CANDS:
            v = max_corr(w, SRC[c])
            if v > agg[c][0]:
                agg[c] = (v, t)
    order = sorted(agg.items(), key=lambda kv: -kv[1][0])
    print(f"  bản {tag}: " + "   ".join(
        f"{c.replace('bgm_', '').replace('.mp3', '')}={v[0]:.3f}@{v[1]:.0f}s" for c, v in order[:4]))
