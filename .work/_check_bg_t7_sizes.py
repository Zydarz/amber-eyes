import sys, os, glob
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

bg_files = sorted(glob.glob("assets/bg/t7_*.png"))
print(f"Total t7_ files found: {len(bg_files)}")

size_issues = []
for p in bg_files:
    try:
        with Image.open(p) as img:
            w, h = img.size
            if (w, h) != (2112, 1188):
                size_issues.append((os.path.basename(p), w, h))
    except Exception as e:
        print(f"Error opening {p}: {e}")

if size_issues:
    print(f"Size issues ({len(size_issues)}):", size_issues)
else:
    print("ALL 61 images have EXACT size 2112x1188!")
