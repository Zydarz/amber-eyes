# -*- coding: utf-8 -*-
"""Tập 12 — đưa biến thể thắng QC vòng 3 vào assets/bg + đồng bộ jobs/provenance.

Dùng: py -3 .work/_t12_promote_detext3.py --winner a|b

- Sao lưu ảnh cũ (đang dính chữ) vào .work/_cu/t12_detext3_20261116/ (L5)
- Copy staging/<biến thể> -> assets/bg/t12_reel_to_reel_archive_recorder.png
- Cập nhật prompt + seed trong .work/bg_jobs_tap12_v2.json
- Cập nhật dòng provenance.json của file này
- Kiểm tra kích thước 2112x1188
"""
import argparse
import json
import shutil
import sys
from datetime import date
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
STAGE = WORK / "_t12" / "detext3"
BG = ROOT / "assets" / "bg"
JOBS = WORK / "bg_jobs_tap12_v2.json"
PROV = ROOT / "provenance.json"
BACKUP = WORK / "_cu" / "t12_detext3_20261116"
TARGET = "t12_reel_to_reel_archive_recorder"

ap = argparse.ArgumentParser()
ap.add_argument("--winner", required=True, choices=["a", "b"])
args = ap.parse_args()

variants = json.loads((WORK / "bg_jobs_tap12_detext3.json").read_text(encoding="utf-8"))
by = {j["name"]: j for j in variants}
wname = f"{TARGET}_{args.winner}"
wjob = by[wname]
src = STAGE / f"{wname}.png"
if not src.exists():
    raise SystemExit(f"khong co file staging: {src}")
with Image.open(src) as im:
    size = im.size
if size != (2112, 1188):
    raise SystemExit(f"sai kich thuoc {size} (can 2112x1188)")

BACKUP.mkdir(parents=True, exist_ok=True)
dst = BG / f"{TARGET}.png"
if dst.exists():
    shutil.copy2(dst, BACKUP / f"{TARGET}.png")
    print(f">>> backup anh cu: {BACKUP / (TARGET + '.png')}")
shutil.copy2(src, dst)
print(f">>> da thay: {dst} (bien the {args.winner}, seed {wjob['seed']})")

jobs = json.loads(JOBS.read_text(encoding="utf-8"))
hit = 0
for j in jobs:
    if j["name"] == TARGET:
        j["desc"] = wjob["desc"]
        j["prompt"] = wjob["prompt"]
        j["seed"] = wjob["seed"]
        hit += 1
if hit != 1:
    raise SystemExit(f"khong tim thay dung 1 job {TARGET} ({hit})")
JOBS.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
print(f">>> bg_jobs_tap12_v2.json: prompt + seed cua bien the {args.winner}")

prov = json.loads(PROV.read_text(encoding="utf-8"))
fp = f"assets/bg/{TARGET}.png"
today = str(date.today())
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
    "ghi_chu": (f"Sinh moi nen Tap 12 theo H25; vong 3 bo chu AI (bien the "
                f"{args.winner}), {today}"),
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
