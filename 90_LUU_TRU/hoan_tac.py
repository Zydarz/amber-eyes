# Hoàn tác việc sắp xếp ngày 22/10/2026: chuyển mọi file về chỗ cũ.
import json, shutil
from pathlib import Path
R = Path(r'D:\TEST\Gax\Audi')
for m in reversed(json.loads((R / '90_LUU_TRU/_nhat_ky_di_chuyen.json').read_text(encoding='utf-8'))):
    s, d = R / m['den'], R / m['tu']
    if s.exists() and not d.exists():
        d.parent.mkdir(parents=True, exist_ok=True); shutil.move(str(s), str(d))
print('đã hoàn tác')
