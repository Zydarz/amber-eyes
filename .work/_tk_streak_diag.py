# -*- coding: utf-8 -*-
"""Chan doan viet ngang: in bang dong nao vuot nguong trong 2 dai chu."""
import numpy as np
from PIL import Image
import sys

HOOK = (270, 730)
SUB = (996, 1254)
X0, X1 = 120, 780
THRESH = 120
for name in sys.argv[1:]:
    p = r"D:/TEST/Gax/amber-eyes/assets/bg/tk02_%s.png" % name
    g = np.asarray(Image.open(p).convert("L"), dtype=np.float32)
    print("=== %s" % name)
    for bname, (y0, y1) in (("hook", HOOK), ("sub", SUB)):
        reg = g[y0:y1, X0:X1]
        frac = (reg > THRESH).mean(axis=1)
        rows = [(y0 + i, round(float(f), 2)) for i, f in enumerate(frac) if f > 0.70]
        if rows:
            print("  %s: %d dong >70%% (y %d..%d) · frac %.2f..%.2f · max px %.0f"
                  % (bname, len(rows), rows[0][0], rows[-1][0],
                     min(r[1] for r in rows), max(r[1] for r in rows), reg.max()))
        else:
            print("  %s: sach" % bname)
