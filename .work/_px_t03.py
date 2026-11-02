from PIL import Image
import numpy as np, pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_t03\stills\shot_1-13.png")
im = Image.open(p).convert("RGB"); a = np.array(im)
print("size:", im.size)
# vung chu trang (quote): y 300..480
band = a[300:480]
mask = band.mean(axis=2) > 170
cols = np.where(mask.any(axis=0))[0]
print("vung chu 1-13: x tu", cols.min(), "den", cols.max(), " (khung 1920)")
# dong text phu
band2 = a[50:110]
m2 = band2.mean(axis=2) > 150
c2 = np.where(m2.any(axis=0))[0]
print("vung badge: x tu", c2.min(), "den", c2.max())
