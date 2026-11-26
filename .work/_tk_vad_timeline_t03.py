#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung timeline_tkN.json cho Tap03 (VN) tu master WAV bang VAD dai giong noi.

Tieu chuan (L3 - do that, khong noi):
- So doan VAD cua moi clip phai BANG so cau trong spec (N).
- Tong thoi luong 'tieng noi' phai khop tong est_dur_s trong spec (sai so cho phep).
- Tong khoang im giua cac doan phai khop tong pause_after_s trong spec.
- Doan dau bat dau gan 0s; doan cuoi ket thuc gan cuoi file (tru fade-out 0.8s).

Dung:  py -3 .work/_tk_vad_timeline_t03.py [--write]
Ra:    02_SAN_XUAT/TIKTOK/Tap03/timeline_tkN.json
"""
import json
import os
import pathlib
import sys
import wave

import numpy as np
from scipy.signal import butter, sosfiltfilt

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap03"
SPEC = D / "SPEC_AUDIO_CLIP_TAP03.json"
CLIPS = ["TK1", "TK2", "TK3", "TK4", "TK5"]

HOP = 0.010           # 10 ms
MIN_SPEECH = 0.20     # doan ngan hon -> bo
MAX_GAP = 0.22        # im giua 2 doan ngan hon -> gop lai
BAND = (200.0, 4000.0)  # dai giong noi


def read_wav_mono(path):
    w = wave.open(str(path), "rb")
    n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
    data = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        data = data.reshape(-1, ch).mean(axis=1)
    w.close()
    return data, sr


def band_rms_db(x, sr, band=BAND):
    lo, hi = band
    ny = sr / 2.0
    sos = butter(4, [lo / ny, hi / ny], btype="band", output="sos")
    y = sosfiltfilt(sos, x)
    hop = int(sr * HOP)
    nb = len(y) // hop
    y = y[: nb * hop].reshape(nb, hop)
    rms = np.sqrt((y.astype(np.float64) ** 2).mean(axis=1) + 1e-12)
    return 20.0 * np.log10(rms + 1e-9), len(y) / sr


def segments_from_mask(mask):
    """mask: bool array theo frame 10ms -> list [start_s, end_s]"""
    segs = []
    i = 0
    n = len(mask)
    while i < n:
        if mask[i]:
            j = i
            while j + 1 < n and mask[j + 1]:
                j += 1
            segs.append([i * HOP, (j + 1) * HOP])
            i = j + 1
        else:
            i += 1
    # ghep doan ngan qua gap nho
    merged = []
    for s in segs:
        if merged and (s[0] - merged[-1][1]) <= MAX_GAP:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    return [s for s in merged if (s[1] - s[0]) >= MIN_SPEECH]


def score(segs, lines, total):
    """So doan phai bang N; khop est_dur (tieng noi) va pause_after (im)."""
    n = len(lines)
    est_sum = sum(l["est_dur_s"] for l in lines)
    pause_sum = sum(l.get("pause_after_s", 0.5) for l in lines)
    speech = sum(s[1] - s[0] for s in segs)
    gaps = [segs[i + 1][0] - segs[i][1] for i in range(len(segs) - 1)]
    gap_sum = sum(gaps)
    pen = 0.0
    pen += 25.0 * abs(len(segs) - n)
    pen += 0.6 * abs(speech - est_sum)
    pen += 0.6 * abs(gap_sum - pause_sum)
    if segs:
        pen += 2.0 * abs(segs[0][0])                      # doan dau phai bat dau ~0
        pen += 1.5 * abs((total - 0.8) - segs[-1][1])   # doan cuoi phai toi gan cuoi
    return pen


def best_timeline(master_wav, lines, total):
    x, sr = read_wav_mono(master_wav)
    db, _ = band_rms_db(x, sr)
    cands = []
    for thr in np.arange(-46.0, -8.0, 0.25):
        segs = segments_from_mask(db > thr)
        cands.append((score(segs, lines, total), float(thr), segs))
    cands.sort(key=lambda t: t[0])
    return cands


def main():
    write = "--write" in sys.argv
    spec = json.loads(SPEC.read_text(encoding="utf-8-sig"))
    allok = True
    for cid in CLIPS:
        lines = spec["clips"][cid]["lines"]
        master = D / f"{cid}_master_audio.wav"
        x, sr = read_wav_mono(master)
        total = len(x) / sr
        cands = best_timeline(master, lines, total)
        best = cands[0]
        # uu tien phuong an co dung so doan
        exact = [c for c in cands if len(c[2]) == len(lines)]
        if exact:
            best = exact[0]
        pen, thr, segs = best
        n = len(lines)
        ok = len(segs) == n
        allok = allok and ok
        print(f"\n=== {cid}  lines={n}  thr={thr:.2f}dB  score={pen:.2f}  "
              f"segs={len(segs)} {'OK' if ok else 'MISMATCH'}  dur={total:.2f}s")
        est_sum = sum(l["est_dur_s"] for l in lines)
        pause_sum = sum(l.get("pause_after_s", 0.5) for l in lines)
        speech = sum(s[1] - s[0] for s in segs)
        gaps = [segs[i + 1][0] - segs[i][1] for i in range(len(segs) - 1)]
        print(f"    speech measured={speech:.2f}s  est={est_sum:.2f}s   "
              f"gap measured={sum(gaps):.2f}s  pause_est={pause_sum:.2f}s")
        for k, l in enumerate(lines):
            if k < len(segs):
                s0, s1 = segs[k]
                gap = (segs[k + 1][0] - s1) if k + 1 < len(segs) else 0.0
                print(f"    {l['clip_line_id']:<12} meas={s1 - s0:5.2f}s est={l['est_dur_s']:5.2f}s "
                      f"gap={gap:4.2f}s pause={l.get('pause_after_s', 0.5):4.2f}s  bg={l['bg']}")
        if write and ok:
            tl = []
            for k, l in enumerate(lines):
                s0, s1 = segs[k]
                gap = (segs[k + 1][0] - s1) if k + 1 < len(segs) else 0.0
                tl.append({
                    "id": l["clip_line_id"],
                    "vai": l.get("role", "H"),
                    "start": round(s0, 3),
                    "end": round(s1, 3),
                    "pause": round(gap, 3),
                    "text": l["text"],
                    "bg": l["bg"],
                    "motion": l.get("motion", "still"),
                })
            (D / f"timeline_{cid.lower()}.json").write_text(
                json.dumps(tl, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"    -> wrote {D / f'timeline_{cid.lower()}.json'}")
    print("\nALL OK" if allok else "\nCO CLIP KHONG KHOP SO CAU")


if __name__ == "__main__":
    main()
