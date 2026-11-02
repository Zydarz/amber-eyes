from PIL import Image
import numpy as np, pathlib
D = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_t03\stills")
for n in ("shot_4-01","shot_1-01","shot_5-01"):
    a = np.array(Image.open(D/f"{n}.png").convert("RGB"))
    band = a[380:570].mean(axis=2) > 150
    c = np.where(band.any(axis=0))[0]
    print(f"  {n:12s} chu lon x {c.min()}..{c.max()}  {'<<< TRAN KEH' if c.max()>1900 else 'OK'}")
