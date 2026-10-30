from PIL import Image
from pathlib import Path
import sys

BG = Path(__file__).resolve().parents[1] / "assets" / "bg"

def fix_crop(name, l, t, r, b):
    p = BG / name
    if not p.exists():
        print(f"File {name} not found")
        return
    im = Image.open(p)
    w, h = im.size
    cropped = im.crop((l, t, w - r, h - b))
    cw, ch = cropped.size
    # Adjust to exact 16:9
    target_aspect = 16 / 9
    if cw / ch > target_aspect:
        nw = int(ch * target_aspect)
        offset = (cw - nw) // 2
        cropped = cropped.crop((offset, 0, offset + nw, ch))
    else:
        nh = int(cw / target_aspect)
        offset = (ch - nh) // 2
        cropped = cropped.crop((0, offset, cw, offset + nh))
    resized = cropped.resize((2112, 1188), Image.LANCZOS)
    resized.save(p)
    print(f"Fixed {name}: cropped ({l}, {t}, {r}, {b}) -> resized to (2112, 1188)")

# 1. t6_abusive_childhood_shadow.png: bottom=32, left=29, right=29, top=33
fix_crop("t6_abusive_childhood_shadow.png", 35, 38, 35, 38)

# 2. t6_crawlspace_subterranean_tunnel.png: bottom=25
fix_crop("t6_crawlspace_subterranean_tunnel.png", 0, 0, 0, 30)

# 3. t6_forensic_trowel_damp_soil.png: top=17, bottom=17, left=10, right=10
fix_crop("t6_forensic_trowel_damp_soil.png", 15, 22, 15, 22)

# 4. t6_gas_station_neon_midnight.png: top=13, bottom=17, left=11, right=11
fix_crop("t6_gas_station_neon_midnight.png", 15, 22, 15, 22)

# 5. t6_psychiatric_evaluation_room.png: top=34, bottom=36, left=31, right=31
fix_crop("t6_psychiatric_evaluation_room.png", 36, 40, 36, 40)

# 6. check t6_redflag_externalized_blame.png
p6 = BG / "t6_redflag_externalized_blame.png"
im6 = Image.open(p6)
print("t6_redflag_externalized_blame size:", im6.size)
