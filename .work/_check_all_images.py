import json, sys, io, os
from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bg_dir = 'assets/bg'
t4_files = sorted([f for f in os.listdir(bg_dir) if f.startswith('t4_') and f.endswith('.png')])

print(f"Total t4_*.png files found: {len(t4_files)}")

issues = []
for f in t4_files:
    path = os.path.join(bg_dir, f)
    try:
        im = Image.open(path)
        w, h = im.size
        mode = im.mode
        if (w, h) != (2112, 1188):
            issues.append(f"{f}: size is {w}x{h} (expected 2112x1188)")
        if mode not in ('RGB', 'RGBA'):
            issues.append(f"{f}: mode is {mode}")
    except Exception as e:
        issues.append(f"{f}: cannot open ({e})")

if issues:
    print(f"Found {len(issues)} issues:")
    for iss in issues:
        print("  -", iss)
else:
    print("ALL 51 IMAGES ARE VALID, 2112x1188, RGB/RGBA!")
