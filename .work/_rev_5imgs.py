import sys
from pathlib import Path
from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')
bg_dir = Path("assets/bg")

five_images = [
    "t5_btk_signature_letter.png",
    "t5_newspaper_classified_494.png",
    "t5_metadata_screen.png",
    "t5_handwritten_note_floppy.png",
    "t5_church_website_search.png"
]

print("=== 5. KIỂM TRA 5 ẢNH CÓ NGUY CƠ CHỮ AI ===")
for fn in five_images:
    fp = bg_dir / fn
    im = Image.open(fp)
    w, h = im.size
    arr = np.asarray(im.convert("L"), np.float32)
    print(f"Ảnh: {fn:<35} | Kích thước: {w}x{h} | Mean Lum: {arr.mean():.1f} | Std: {arr.std():.1f}")
