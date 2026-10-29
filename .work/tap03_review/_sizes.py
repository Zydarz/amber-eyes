from PIL import Image
import os
for f in ["t3_backyard_garden", "t3_trapdoor"]:
    p = rf"D:\TEST\Gax\Audi\assets\bg\{f}.png"
    im = Image.open(p)
    raw = rf"D:\TEST\Gax\Audi\assets\bg\_raw\{f}.png"
    r = Image.open(raw).size if os.path.exists(raw) else None
    print(f, "final:", im.size, " raw:", r)
