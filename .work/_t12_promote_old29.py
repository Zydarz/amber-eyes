# -*- coding: utf-8 -*-
"""Tập 12 — promote nhiều nền cũ đã vá: đọc map {mã nền: "a"|"b"} và đưa vào assets/bg.

Dùng: py -3 .work/_t12_promote_old29.py --map .work/_t12/old29_winners.json
Map: {"t12_memorial_918_names_monolith": "a", ...}
- Sao lưu ảnh cũ vào .work/_cu/t12_old29_<giờ>/ (L5)
- Copy staging/<mã>_<biến thể>.png -> assets/bg/<mã>.png
- Cập nhật desc/prompt/seed trong .work/bg_jobs_tap12_v2.json
- Cập nhật provenance.json
- Kiểm tra kích thước 2112x1188 cho từng ảnh
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
STAGE = WORK / "_t12" / "old29"

ap = argparse.ArgumentParser()
ap.add_argument("--map", required=True)
ap.add_argument("--jobs-file", default=".work/bg_jobs_tap12_old29.json",
                help="file job chua bien the (_v5 / _v6)")
ap.add_argument("--stage", default=".work/_t12/old29",
                help="thu muc staging chua anh bien the")
args = ap.parse_args()

STAGE = ROOT / args.stage
winners = json.loads((ROOT / args.map).read_text(encoding="utf-8"))
variants = {j["name"]: j for j in json.loads((ROOT / args.jobs_file).read_text(encoding="utf-8"))}
jobs = json.loads(JOBS.read_text(encoding="utf-8"))
by = {j["name"]: j for j in jobs}
prov = json.loads(PROV.read_text(encoding="utf-8"))
by_file = {r.get("file"): i for i, r in enumerate(prov)}
today = str(date.today())
backup = WORK / "_cu" / f"t12_old29_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)

ok, skip = [], []
for base, win in winners.items():
    vname = f"{base}_{win}"
    vjob = variants.get(vname)
    src = STAGE / f"{vname}.png"
    if not vjob or not src.exists():
        skip.append(f"{base} (thieu bien the {vname})")
        continue
    with Image.open(src) as im:
        size = im.size
    if size != (2112, 1188):
        skip.append(f"{base} (sai kich thuoc {size})")
        continue
    dst = BG / f"{base}.png"
    if dst.exists():
        shutil.copy2(dst, backup / dst.name)
    shutil.copy2(src, dst)

    if base in by:
        by[base]["desc"] = vjob["desc"]
        by[base]["prompt"] = vjob["prompt"]
        by[base]["seed"] = vjob["seed"]
    else:
        skip.append(f"{base} (khong co trong bg_jobs_tap12_v2.json)")

    fp = f"assets/bg/{base}.png"
    entry = {
        "file": fp,
        "loai": "nen 16:9 dung chung 3 ngon ngu",
        "cong_cu": "Kaggle FLUX.2-klein-4B (1 tien trinh / 1 GPU, KHONG Real-ESRGAN)",
        "ngay": today,
        "prompt": vjob["prompt"],
        "seed": vjob["seed"],
        "nguon_anh_tham_chieu": None,
        "kich_thuoc_goc": [2112, 1188],
        "dieu_khoan": "FLUX.2 Open Model License / Creative Commons Commercial",
        "kiem_tra_thuong_mai": "dat",
        "ghi_chu": (f"Sinh moi nen Tap 12 theo H25; vong bo chu AI cho nen cu 13/11 "
                    f"(bien the {win}), {today}"),
    }
    if fp in by_file:
        prov[by_file[fp]] = entry
    else:
        prov.append(entry)
        by_file[fp] = len(prov) - 1
    ok.append(f"{base} [{win}]")

JOBS.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")
print(f">>> da thay {len(ok)} nen vao assets/bg (backup: {backup})")
for s in ok:
    print(f"    + {s}")
if skip:
    print(f">>> BO SONG {len(skip)}:")
    for s in skip:
        print(f"    - {s}")
print(f">>> provenance.json: tong {len(prov)} dong")
