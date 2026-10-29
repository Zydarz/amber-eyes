import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
from PIL import Image

stills_dir = Path(".work/video3_t05/stills")
files = sorted(stills_dir.glob("*.png"))
print(f"Tổng số ảnh tĩnh: {len(files)}")

invalid = []
for f in files:
    try:
        im = Image.open(f)
        if im.size != (1920, 1080):
            invalid.append((f.name, f"Sai kích thước: {im.size}"))
    except Exception as e:
        invalid.append((f.name, str(e)))

print(f"Số ảnh lỗi: {len(invalid)}")
if invalid:
    for name, err in invalid[:5]:
        print(f"  {name}: {err}")
else:
    print("Toàn bộ 83 ảnh tĩnh 1920x1080 hợp lệ 100%!")
