import json, re, os
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\Audi")
jobs = json.loads((ROOT/".work"/"bg_jobs_tap03.json").read_text(encoding="utf-8"))
names = [j["name"] for j in jobs]
print("So muc trong bg_jobs_tap03.json:", len(jobs))
for n in ["t3_trapdoor", "t3_backyard_garden", "t3_gavel", "t3_trunk", "t3_small_bed", "t3_car_door"]:
    print(f"  {n:<22} trong jobs: {n in names}")
print()
bg = ROOT/"assets"/"bg"
disk = sorted(p.stem for p in bg.glob("t3_*.png"))
print("So anh t3_ tren dia:", len(disk))
print("Tren dia NHUNG khong trong jobs:", [d for d in disk if d not in names])
print("Trong jobs NHUNG khong tren dia:", [n for n in names if n not in disk])
extra = json.loads((ROOT/".work"/"bg_jobs_tap03_extra.json").read_text(encoding="utf-8"))
print()
print("bg_jobs_tap03_extra.json:", [j["name"] for j in extra])
