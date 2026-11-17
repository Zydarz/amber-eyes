# -*- coding: utf-8 -*-
"""Tập 12 — đưa biến thể thắng QC vào assets/bg + đồng bộ jobs/provenance (dùng chung).

Dùng:
  py -3 .work/_t12_promote.py --target t12_reel_to_reel_archive_recorder --winner a `
      --jobs .work/bg_jobs_tap12_detext4.json --stage .work/_t12/detext4

- Sao lưu ảnh cũ vào .work/_cu/t12_promote_<ngay>/ (L5)
- Copy staging/<mã>_<biến thể>.png -> assets/bg/<mã>.png
- Cập nhật desc/prompt/seed trong .work/bg_jobs_tap12_v2.json
- Cập nhật dòng provenance.json
- Kiểm tra kích thước 2112x1188
"""
import argparse
import json
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BG = ROOT / "assets" / "bg"
JOBS = WORK / "bg_jobs_tap12_v2.json"
PROV = ROOT / "provenance.json"

ap = argparse.ArgumentParser()
ap.add_argument("--target", required=True)
ap.add_argument("--winner", required=True, choices=["a", "b"])
ap.add_argument("--jobs", required=True)
ap.add_argument("--stage", required=True)
args = ap.parse_args()

JOBSF = ROOT / args.jobs if not Path(args.jobs).is_absolute() else Path(args.jobs)
STAGE = ROOT / args.stage if not Path(args.stage).is_absolute() else Path(args.stage)
BASE = ROOT / args.target if not Path(args.target).is_absolute() else Path(args.target)

variants = {j["name"]: j for j in json.loads(JOBSF.read_text(encoding="utf-8"))}
wname = f"{BASE.name}_{args.winner}"
wjob = variants.get(wname)
if not wjob:
    raise SystemExit(f"khong co bien the {wname} trong {JOBSF.name}")
src = STAGE / f"{wname}.png"
if not src.exists():
    raise SystemExit(f"khong co file staging: {src}")
with Image.open(src) as im:
    size = im.size
if size != (2112, 1188):
    raise SystemExit(f"sai kich thuoc {size} (can 2112x1188)")

today = str(date.today())
backup = WORK / "_cu" / f"t12_promote_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
dst = BG / f"{BASE.name}.png"
if dst.exists():
    shutil.copy2(dst, backup / dst.name)
    print(f">>> backup anh cu: {backup / dst.name}")
shutil.copy2(src, dst)
print(f">>> da thay: {dst} (bien the {args.winner}, seed {wjob['seed']})")

jobs = json.loads(JOBS.read_text(encoding="utf-8"))
hit = 0
for j in jobs:
    if j["name"] == BASE.name:
        j["desc"] = wjob["desc"]
        j["prompt"] = wjob["prompt"]
        j["seed"] = wjob["seed"]
        hit += 1
if hit != 1:
    raise SystemExit(f"khong tim thay dung 1 job {BASE.name} ({hit})")
JOBS.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
print(f">>> bg_jobs_tap12_v2.json: prompt + seed cua bien the {args.winner}")

prov = json.loads(PROV.read_text(encoding="utf-8"))
fp = f"assets/bg/{BASE.name}.png"
entry = {
    "file": fp,
    "loai": "nen 16:9 dung chung 3 ngon ngu",
    "cong_cu": "Kaggle FLUX.2-klein-4B (1 tien trinh / 1 GPU, KHONG Real-ESRGAN)",
    "ngay": today,
    "prompt": wjob["prompt"],
    "seed": wjob["seed"],
    "nguon_anh_tham_chieu": None,
    "kich_thuoc_goc": [2112, 1188],
    "dieu_khoan": "FLUX.2 Open Model License / Creative Commons Commercial",
    "kiem_tra_thuong_mai": "dat",
    "ghi_chu": f"Sinh moi nen Tap 12 theo H25; vong bo chu AI (bien the {args.winner}), {today}",
}
n = 0
for i, r in enumerate(prov):
    if r.get("file") == fp:
        prov[i] = entry
        n += 1
if n == 0:
    prov.append(entry)
PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")
print(f">>> provenance.json: cap nhat {n} dong (tong {len(prov)} dong)")
