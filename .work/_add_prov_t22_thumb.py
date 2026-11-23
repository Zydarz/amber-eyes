import json
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROV = ROOT / "provenance.json"
BACKUP = ROOT / ".work" / "_cu" / f"provenance.json.bak_{int(time.time())}"

shutil.copy2(PROV, BACKUP)
print("Backup created:", BACKUP)

with open(PROV, "r", encoding="utf-8") as f:
    data = json.load(f)

entries = [
    {
        "file": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap22/xuat_ban/thumbnail.png",
        "loai": "ảnh đại diện 1280×720 (RGB)",
        "cong_cu": ".work/package.py thumbnail() — nền t22_a1_07_theatrical_grief_knees_collapse + chữ Pillow (segoeuib.ttf)",
        "ngay": "2026-11-23",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự tạo theo kịch bản Tập 22; linh thú & logo kênh",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": 'Dòng chữ: NƯỚC MẮT · CÁ SẤU (EPISODES["22"]["thumb"]).',
    },
    {
        "file": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap22_EN/xuat_ban/thumbnail.png",
        "loai": "ảnh đại diện 1280×720 (RGB)",
        "cong_cu": ".work/package.py thumbnail() — nền t22_a1_07_theatrical_grief_knees_collapse + chữ Pillow (segoeuib.ttf)",
        "ngay": "2026-11-23",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự tạo theo kịch bản Tập 22; linh thú & logo kênh",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": 'Dòng chữ: CROCODILE TEARS · ON CAMERA (EPISODES["22"]["thumb"] nhánh EN).',
    },
    {
        "file": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap22_JA/xuat_ban/thumbnail.png",
        "loai": "ảnh đại diện 1280×720 (RGB)",
        "cong_cu": ".work/package.py thumbnail() — nền t22_a1_07_theatrical_grief_knees_collapse + chữ Pillow (YuGothB.ttc)",
        "ngay": "2026-11-23",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự tạo theo kịch bản Tập 22; linh thú & logo kênh",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": 'Dòng chữ: カメラの前の · 偽りの涙 (EPISODES["22"]["thumb"] nhánh JA).',
    },
]

existing_files = {e["file"]: i for i, e in enumerate(data) if isinstance(e, dict) and "file" in e}
for item in entries:
    if item["file"] in existing_files:
        data[existing_files[item["file"]]] = item
        print("Updated:", item["file"])
    else:
        data.append(item)
        print("Added:", item["file"])

with open(PROV, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("Provenance successfully updated. Total entries:", len(data))
