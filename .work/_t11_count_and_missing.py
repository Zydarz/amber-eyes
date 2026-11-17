# -*- coding: utf-8 -*-
"""Tập 11 — đếm ảnh nền thực tế trên đĩa, đối chiếu 136 job, tạo file jobs cho phần còn thiếu."""
import json
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
BG = ROOT / "assets" / "bg"
jobs = json.loads((ROOT / ".work/bg_jobs_tap11_v3.json").read_text(encoding="utf-8"))
names = [j["name"] for j in jobs]

have = [n for n in names if (BG / f"{n}.png").exists()]
missing = [n for n in names if not (BG / f"{n}.png").exists()]
on_disk = sorted(p.stem for p in BG.glob("t11_*.png"))

print(f"job trong bg_jobs_tap11.json : {len(names)}")
print(f"file t11_*.png trên đĩa      : {len(on_disk)}")
print(f"  có file & có job           : {len(have)}")
print(f"  còn THIẾU file             : {len(missing)}")
extra = [n for n in on_disk if n not in set(names)]
print(f"  file thừa (không có job)   : {len(extra)} {extra}")

# kích thước + kiểm tra ảnh hỏng
from PIL import Image
bad = []
for n in have:
    p = BG / f"{n}.png"
    try:
        im = Image.open(p)
        if im.size != (2112, 1188):
            bad.append((n, im.size))
    except Exception as e:
        bad.append((n, str(e)[:40]))
print(f"  sai kích thước / hỏng     : {len(bad)} {bad[:5]}")

# file jobs cho phần thiếu
by = {j["name"]: j for j in jobs}
mj = [by[n] for n in missing]
(ROOT / ".work/bg_jobs_tap11_missing.json").write_text(
    json.dumps(mj, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\n-> .work/bg_jobs_tap11_missing.json ({len(mj)} job)")
print("   " + ", ".join(missing[:6]) + " ...")
