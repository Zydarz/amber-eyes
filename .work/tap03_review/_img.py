from PIL import Image
import os
p = r"D:\TEST\Gax\Audi\assets\bg\t3_trapdoor.png"
if os.path.exists(p):
    im = Image.open(p); print("t3_trapdoor.png:", im.size, im.mode)
else:
    print("t3_trapdoor.png MISSING")
raw = r"D:\TEST\Gax\Audi\assets\bg\_raw"
if os.path.isdir(raw):
    print("raw files:", [f for f in os.listdir(raw) if "trapdoor" in f or "backyard" in f])
