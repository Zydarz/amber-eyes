from PIL import Image
import numpy as np, pathlib
for name in ("shot_1-13","shot_2-21","shot_1-25"):
    p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_t03\stills")/f"{name}.png"
    a = np.array(Image.open(p).convert("RGB"))
    band = a[60:100].mean(axis=2) > 150
    c = np.where(band.any(axis=0))[0]
    print(f"  {name}: vung badge x {c.min()}..{c.max()}  (khung 1920)")
