# -*- coding: utf-8 -*-
import sys
from pathlib import Path
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

stills_dir = Path(".work/video3_EN_t06/stills")
files = list(stills_dir.glob("*.png"))
print(f"Total stills: {len(files)}")

invalid = []
for f in files:
    try:
        with Image.open(f) as im:
            w, h = im.size
            if (w, h) != (1920, 1080):
                invalid.append((f.name, f"Size {w}x{h} != 1920x1080"))
    except Exception as e:
        invalid.append((f.name, str(e)))

if invalid:
    print(f"ERROR: {len(invalid)} invalid stills:", invalid)
    sys.exit(1)

print("PASS: All 73 stills are valid 1920x1080 PNG images!")

# Inspect key stills sizes
for name in ["1-00", "1-01", "1-16", "3-09", "4-03", "5-14"]:
    matches = list(stills_dir.glob(f"*{name}*.png"))
    if matches:
        p = matches[0]
        print(f"Sample: {p.name} ({p.stat().st_size / 1024:.1f} KB)")
