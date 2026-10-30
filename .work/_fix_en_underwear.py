import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
p = Path(__file__).resolve().parents[1] / ".work" / "shots_text_tap02_EN.json"
d = json.loads(p.read_text(encoding="utf-8"))
old = "**WOMEN'S UNDERWEAR AND PERSONAL BELONGINGS**"
new = "**WOMEN'S PERSONAL BELONGINGS**"          # khớp đúng chữ trên hình của bản VN (ĐỒ RIÊNG TƯ CỦA PHỤ NỮ)
n = 0
for k, v in d.items():
    if isinstance(v, list) and v and isinstance(v[0], str) and old in v[0]:
        d[k][0] = v[0].replace(old, new)
        n += 1
p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"đã sửa {n} dòng: {old} -> {new}")
