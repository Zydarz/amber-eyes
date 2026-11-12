# -*- coding: utf-8 -*-
"""Suy ra nguyen nhan: shot_at(t) co tro khop voi shot dang xet khong?"""
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
idx_by_id = {x["id"]: i for i, x in enumerate(SH)}

for sid in ["1-11", "3-09", "2-05", "4-14"]:
    i_id = idx_by_id[sid]
    s = SH[i_id]
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)
    i_at = b.shot_at(t)

    print(f"\n=== {sid} ===")
    print(f"  index theo ID = {i_id} | shot_at(t) = {i_at} -> ID = {SH[i_at]['id']}")
    print(f"  t = {t:.2f}  | shot tai: {SH[i_at]['start']:.2f}..{SH[i_at]['end']:.2f}")
    print(f"  transition={s.get('transition')}  inherit={s.get('inherit')}  hold={s.get('hold')}")
    if i_at != i_id:
        print(f"  !! shot_at tra ve shot KHAC -> render(fi) ve khac shot")
        print(f"     shot_at co transition? {SH[i_at].get('transition')}  t<start+0.35? {t < SH[i_at]['start']+0.35}")
        print(f"     prev shot: {SH[i_at-1]['id'] if i_at>0 else '-'}")
