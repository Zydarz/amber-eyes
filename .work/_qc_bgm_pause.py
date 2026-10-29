# -*- coding: utf-8 -*-
"""Định danh bed bằng KHOẢNG LẶNG THẬT (từ timeline), không phải điểm yên nhất.

Trong khoảng lặng, giọng đọc vắng -> bed + sàn môi trường nổi lên.
So tương quan tối đa với từng file nguồn để biết file nào đang chạy.
"""
import json
import pathlib
import subprocess
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BGM = ROOT / "assets" / "bgm"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
TMP = WORK / "_qc_tmp48"
TMP.mkdir(exist_ok=True)

CANDIDATES = ["bgm_cello_sad.mp3", "bgm_cello_sad_v2.mp3", "bgm_sub_drone.mp3",
              "bgm_piano_minimal.mp3", "bgm_piano_warm.mp3", "bgm_violin_heart.mp3",
              "bgm_ambient_deep.mp3", "bgm_church_organ.mp3", "bgm_guitar_acoustic_60s.mp3"]


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


SRC = {c: to48k_mono(BGM / c) for c in CANDIDATES}

JOBS = [
    ("T07 VN", WORK / "_cu" / "audio_master_t07.wav.bak_bgm", WORK / "audio_master_t07.wav",
     WORK / "timeline_s_t07.json"),
    ("T02 VN", WORK / "_cu" / "audio_master_t02.wav.bak_bgm", WORK / "audio_master_t02.wav",
     WORK / "timeline_s_t02.json"),
]

for label, old_p, new_p, tl_p in JOBS:
    if not old_p.exists() or not new_p.exists():
        continue
    tl = json.loads(tl_p.read_text(encoding="utf-8"))
    items = tl["items"]
    acts = {int(k): v for k, v in tl["acts"].items()}
    print(f"\n{'='*100}\n=== {label} — bed đang chạy, đo ở KHOẢNG LẶNG thật ===\n{'='*100}")
    for tag, p in (("CU ", old_p), ("MOI", new_p)):
        a, sr = read_master(p)
        mono = a.mean(axis=1) if a.ndim > 1 else a
        print(f"\n  --- bản {tag} ---")
        for act in sorted(acts):
            s, e = acts[act]
            gaps = []
            for i in range(len(items) - 1):
                it = items[i]
                nx = items[i + 1]
                if it["act"] != act or nx["act"] != act:
                    continue
                g0, g1 = it["end"], nx["start"]
                if g1 - g0 >= 1.4:
                    gaps.append((g0 + (g1 - g0) / 2, g1 - g0))
            gaps = [g for g in gaps if s <= g[0] <= e][:4]
            if not gaps:
                print(f"    H{act}: khong co khoang lang du 1,4 s")
                continue
            best = {}
            for t, dur in gaps:
                i = int(t * sr)
                w = mono[i:i + sr]
                if w.size < sr:
                    continue
                for c in CANDIDATES:
                    v = max_corr(w, SRC[c])
                    if v > best.get(c, (-1, 0))[0]:
                        best[c] = (v, t)
            top = sorted(((v[0], c, v[1]) for c, v in best.items()), reverse=True)[:4]
            s_txt = "  ".join(f"{c.replace('bgm_', '').replace('.mp3', '')}={v:.3f}@{t:.0f}s"
                               for v, c, t in top)
            print(f"    H{act} ({len(gaps)} khoang lang): {s_txt}")
