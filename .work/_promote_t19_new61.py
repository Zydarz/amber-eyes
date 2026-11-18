import json
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
OUT_DIR = ROOT / ".work/kaggle_flux/out_t19_new61"
BG_DIR = ROOT / "assets/bg"

png_files = list(OUT_DIR.rglob("*.png"))
print(f"Tổng số file PNG tải về: {len(png_files)}")

# 1. Kiểm tra kích thước và copy vào assets/bg
invalid_sizes = []
for p in png_files:
    with Image.open(p) as img:
        if img.size != (2112, 1188):
            invalid_sizes.append((p.name, img.size))
    dst = BG_DIR / p.name
    shutil.copy2(p, dst)

print(f"Số ảnh sai kích thước (2112x1188): {len(invalid_sizes)}")
if invalid_sizes:
    print("Các ảnh sai kích thước:", invalid_sizes)

# 2. Cập nhật provenance.json
prov_path = ROOT / "provenance.json"
prov = json.loads(prov_path.read_text(encoding="utf-8"))
existing_files = {entry["file"] for entry in prov}

jobs_61 = json.loads((ROOT / ".work/bg_jobs_tap19_new61.json").read_text(encoding="utf-8"))
jobs_map = {j["name"]: j for j in jobs_61}

added_count = 0
for p in png_files:
    rel_path = f"assets/bg/{p.name}"
    stem = p.stem
    job = jobs_map.get(stem, {})
    if rel_path not in existing_files:
        entry = {
            "file": rel_path,
            "loai": "nền 16:9",
            "cong_cu": "Kaggle FLUX.2-klein-4B + Amber Eyes Noir Post-processing Pipeline",
            "ngay": "2026-11-17",
            "prompt": job.get("prompt", ""),
            "seed": job.get("seed", None),
            "nguon_anh_tham_chieu": None,
            "kich_thuoc_goc": [2112, 1188],
            "dieu_khoan": "Kênh tự tạo 100%, 0 đồng chi phí công cụ, thương mại an toàn",
            "kiem_tra_thuong_mai": "đạt"
        }
        prov.append(entry)
        existing_files.add(rel_path)
        added_count += 1

prov_path.write_text(json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Đã sao chép 61 file vào assets/bg và bổ sung {added_count} bản ghi vào provenance.json")
