# -*- coding: utf-8 -*-
"""Bisect: render(fi) vs shot_layer vs bg_frame+elements+characters.
Kiem 2 gia thuyet: (A) grain phase fi%6 lech  (B) camera_box/resize lech"""
import os, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))
os.environ["AE_EP"] = "08"

import importlib
b = importlib.import_module("build_video3")
SH = b.SH
idx = {x["id"]: i for i, x in enumerate(SH)}

for sid in ["1-11", "3-09"]:
    i = idx[sid]
    s = SH[i]
    t_mid = (s["start"] + s["end"]) / 2
    fi = int(t_mid * b.FPS)
    t_render = fi / b.FPS                      # render() tu tinh lai t = fi/FPS

    print(f"\n=== {sid} ===")
    print(f"  t_mid = {t_mid:.6f}   fi = {fi}   t_render = fi/FPS = {t_render:.6f}   (chenh {abs(t_render-t_mid)*1000:.2f} ms)")

    old = np.asarray(b.render(fi).convert("RGB"), dtype=np.int16)

    # A) dung dung t_render (nhu render()) thay vi t_mid
    newA = b.bg_frame(s, t_render, fi)
    for e in b.build_elements(s):
        e.draw(newA, t_render)
    b.draw_characters(newA, t_render, fi, s)
    newA = np.asarray(newA.convert("RGB"), dtype=np.int16)
    dA = np.abs(old - newA).max(axis=2)
    print(f"  [A] dung t=fi/FPS: px khac = {int((dA>0).sum())}  maxdelta={dA.max()}")

    # B) dung t_mid
    newB = b.bg_frame(s, t_mid, fi)
    for e in b.build_elements(s):
        e.draw(newB, t_mid)
    b.draw_characters(newB, t_mid, fi, s)
    newB = np.asarray(newB.convert("RGB"), dtype=np.int16)
    dB = np.abs(old - newB).max(axis=2)
    print(f"  [B] dung t=(start+end)/2: px khac = {int((dB>0).sum())}  maxdelta={dB.max()}")

    # C) chi camera_box: so sanh box
    cb1 = b.camera_box(s, t_render)
    cb2 = b.camera_box(s, t_mid)
    print(f"  camera_box(t_render) = {cb1}")
    print(f"  camera_box(t_mid)    = {cb2}")
    print(f"  box giong het? {cb1 == cb2}")
