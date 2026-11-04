#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem doc lap audio master EN Tap05 co khop timeline khong (T17/A11 #117).

Khong dung ASR: do moc nang luong de tim moc bat dau l noi, roi so voi
moc thoi gian trong timeline_s_EN_t05.json.

Neu |onset - moc_timeline| nho => timeline mo ta DUNG audio master.
Chay: py -3 .work/_qc_audio_onset_en_t05.py
"""
import json
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MP3 = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "Tap05_EN_master.mp3"
WAV = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "Tap05_EN_master.mp3"
TL = json.loads((WORK / "timeline_s_EN_t05.json").read_text(encoding="utf-8"))
SR = 16000
HOP = 160          # 10 ms
WIN = 480          # 30 ms


def decode(path):
    p = subprocess.run([str(FF), "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR),
                        "-f", "s16le", "-"], capture_output=True)
    if p.returncode != 0:
        raise SystemExit(p.stderr.decode("utf-8", "replace")[:400])
    return np.frombuffer(p.stdout, dtype="<i2").astype(np.float32) / 32768.0


print("===== Kiem muc bat dau l noi: mp3 master vs timeline EN Tap05 =====")
x = decode(MP3)
print(f"  audio: {len(x)/SR:.2f} s · {SR} Hz mono")
n = (len(x) - WIN) // HOP
rms = np.sqrt(np.maximum(1e-12, np.array([np.mean(x[i * HOP:i * HOP + WIN] ** 2) for i in range(n)])))
db = 20 * np.log10(rms)
floor = np.percentile(db, 10)
thr = max(floor + 12.0, -45.0)
print(f"  nen {floor:.1f} dB · nguong {thr:.1f} dB")
act = db > thr

# moc bat dau: khung 'phat' sau 'im'
onsets = []
i = 1
while i < len(act):
    if act[i] and not act[i - 1]:
        j = i
        while j < len(act) and act[j]:
            j += 1
        if (j - i) * HOP / SR >= 0.12:          # bo qua tieng ngan
            onsets.append(i * HOP / SR)
    i += 1
onsets = np.array(onsets)
print(f"  phat hien {len(onsets)} moc bat dau l noi")

items = TL["items"]
rows, miss = [], 0
for it in items:
    t = it["start"]
    if len(onsets) == 0:
        break
    k = int(np.searchsorted(onsets, t))
    cand = onsets[max(0, k - 3):k + 4]
    if len(cand) == 0:
        miss += 1
        continue
    d = cand - t
    j = int(np.argmin(np.abs(d)))
    if abs(d[j]) > 0.45:
        miss += 1
        rows.append((it["id"], t, float(d[j]), "LECH-LON"))
    else:
        rows.append((it["id"], t, float(d[j]), "ok"))

dev = np.array([r[2] for r in rows if r[3] == "ok"])
print(f"  khop: {len(dev)}/164 cau · lech > 0,45 s: {miss} cau")
if len(dev):
    print(f"  lech (giay): trung binh {dev.mean():+.3f} · trung vi {np.median(dev):+.3f} · "
          f"max |{np.abs(dev).max():.3f}| · TB |dev| {np.abs(dev).mean():.3f}")
    worst = sorted(rows, key=lambda r: -abs(r[2]))[:8]
    for r in worst:
        print(f"    {r[0]:10} moc {r[1]:9.3f}  lech {r[2]:+.3f}  {r[3]}")
    verdict = "PASS" if np.abs(dev).max() <= 0.30 and miss <= 2 else "CANH BAO"
    print(f"  => {verdict}: timeline mo ta DUNG audio master "
          f"(max |lech| {np.abs(dev).max():.3f} s)")
