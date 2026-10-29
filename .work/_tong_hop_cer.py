import json
from pathlib import Path
rows = json.loads(Path(r"D:\TEST\Gax\Audi\.work\cer_bo_a_tap02\rows_fixed.json").read_text(encoding="utf-8"))
groups = {}
for r in rows:
    groups.setdefault((r["role"], r["voice"]), []).append(r["cer"])
for (role, vid), cs in sorted(groups.items()):
    cs = sorted(cs)
    med = cs[len(cs)//2]; mean = sum(cs)/len(cs)
    over = sum(1 for c in cs if c > 0.02)
    print(f"{role:5s} {vid:32s} n={len(cs):2d}  trung viet {100*med:5.1f}%  trung binh {100*mean:5.1f}%  max {100*cs[-1]:5.1f}%  >2%: {over}/{len(cs)}")
print()
print("Tong so cau do:", len(rows))
