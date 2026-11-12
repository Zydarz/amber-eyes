# -*- coding: utf-8 -*-
"""Tim nguyen nhan 807k px khac biet o 2-05 / 3-09: vung nao trong anh?"""
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

for sid in ["1-11", "3-09", "2-05"]:
    s = {x["id"]: x for x in SH}[sid]
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)

    old = np.asarray(b.render(fi).convert("RGB"), dtype=np.int16)

    new = b.bg_frame(s, t, fi)
    for e in b.build_elements(s):
        e.draw(new, t)
    b.draw_characters(new, t, fi, s)
    new = np.asarray(new.convert("RGB"), dtype=np.int16)

    d = np.abs(old - new).max(axis=2)
    ys, xs = np.where(d > 0)
    print(f"\n=== {sid} ===")
    print(f"  duration={s['end']-s['start']:.1f}s  transition={s.get('transition')}  inherit={s.get('inherit')}"
          f"  hold={s.get('hold')}  template={s['template']}")
    if len(ys) == 0:
        print("  KHONG KHAC")
    else:
        print(f"  px khac: {len(ys)}  bbox y[{ys.min()}..{ys.max()}] x[{xs.min()}..{xs.max()}]"
              f"  maxdelta={d.max()}")
        print(f"  -> vung {'TOAN ANH (nen/gran)' if len(ys) > 400000 else 'VUNG NHO (badge/bust/text)'}")
