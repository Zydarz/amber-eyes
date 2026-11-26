from PIL import Image
from pathlib import Path
W = Path(r"D:/TEST/Gax/amber-eyes/.work/qc_montage")
CW, PAD, LAB = 512, 4, 42+8
ROW = int(CW*9/16) + LAB + PAD
for tag, rows in (("A",[0,6]), ("B",[2,3])):
    im = Image.open(W/f"ep36_bg_{tag}.jpg")
    for r in rows:
        box = (0, r*ROW, im.width, min((r+1)*ROW, im.height))
        im.crop(box).save(W/f"row_{tag}{r}.jpg", quality=92)
        print(f"row_{tag}{r}.jpg", box)
