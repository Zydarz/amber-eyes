"""Chan doo F0 theo thoi gian cho 3 cau bi loai F0 + mau doi chieu.

Cau hoi: cau bi loai co bi 'giong khac' (ca clip thap) hay chi 'ngu dieu tut cuoi cau'?
Tieu chi: median nua dau vs nua cuoi + p10/p50/p90 toan clip.
"""
import json
import pathlib
import sys

import numpy as np
import soundfile as sf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from voxcpm_yin_f0 import yin  # noqa: E402

PROD = HERE / "kaggle_higgs" / "out_higgs_prod_t04" / "out_higgs_prod_t04"

TARGET = {
    "2.08#1": "2_08_1_D_D3_SH_t0.8_s0.wav",
    "3.02#2": "3_02_2_H_H_t0.8_s0.wav",
    "5.08#5": "5_08_5_H_H_t0.8_s0.wav",
}
# mau doi chieu: cung vai, neutral, lech < 1 nk
REF = {
    "H mau (3_02_2 khac bien)": None,
    "H binh thuong": "1_03_1_H_H_t0.8_s0.wav",
    "H binh thuong 2": "1_16_3_H_H_t0.8_s2.wav",
    "D binh thuong": "1_14_2_D_D3_SH_t0.8_s2.wav",
}


def stats(path):
    x, sr = sf.read(str(path), dtype="float32")
    if x.ndim > 1:
        x = x.mean(axis=1)
    y = yin(x, sr)
    f0 = y[y > 0]
    if len(f0) == 0:
        return None
    # frame rate cua yin: uoc luong bang so frame / do dai
    n_frames = len(y)
    hop_s = 0.010
    dur = len(x) / sr
    n = len(f0)
    # chia theo phan bao thoi gian uoc luong: lay theo vi tri phan bo cua f0
    q = np.percentile(f0, [10, 25, 50, 75, 90])
    return dict(dur=round(dur, 2), n=len(f0), p10=round(float(q[0]), 1), p25=round(float(q[1]), 1),
                p50=round(float(q[2]), 1), p75=round(float(q[3]), 1), p90=round(float(q[4]), 1),
                fmin=round(float(f0.min()), 1), fmax=round(float(f0.max()), 1))


print("== 3 CAU BI LOAI ==")
for sid, fn in TARGET.items():
    st = stats(PROD / fn)
    print("%-9s %-30s %s" % (sid, fn, st))

print("\n== MAU DOI CHIEU ==")
for label, fn in REF.items():
    if fn is None:
        continue
    st = stats(PROD / fn)
    print("%-26s %-30s %s" % (label, fn, st))

# Trajectory: median f0 theo phan bao thoi gian cua clip (dung 6 cua)
print("\n== TRAJECTORY (median F0 theo 6 doan thoi gian, Hz) ==")


def traj(path, nseg=6):
    x, sr = sf.read(str(path), dtype="float32")
    if x.ndim > 1:
        x = x.mean(axis=1)
    seg = len(x) // nseg
    out = []
    for i in range(nseg):
        s = x[i * seg:(i + 1) * seg]
        if len(s) < 100:
            out.append(None)
            continue
        y = yin(s, sr)
        f = y[y > 0]
        out.append(round(float(np.median(f)), 1) if len(f) else None)
    return out


for sid, fn in list(TARGET.items()):
    print("%-9s %-30s %s" % (sid, fn, traj(PROD / fn)))
for label, fn in REF.items():
    if fn:
        print("%-26s %-30s %s" % (label, fn, traj(PROD / fn)))
