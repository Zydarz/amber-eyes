from PIL import Image
from pathlib import Path
W = Path(r"D:/TEST/Gax/amber-eyes/.work/qc_montage")
CW, PAD, LAB = 512, 4, 42+8
ROW = int(CW*9/16) + LAB + PAD
done = {("A",0),("A",6),("B",2),("B",3)}
for tag in ("A","B"):
    im = Image.open(W/f"ep36_bg_{tag}.jpg")
    n = (im.height + ROW - 1)//ROW
    for r in range(n):
        if (tag,r) in done: continue
        im.crop((0, r*ROW, im.width, min((r+1)*ROW, im.height))).save(W/f"row_{tag}{r}.jpg", quality=92)
print("xong")
