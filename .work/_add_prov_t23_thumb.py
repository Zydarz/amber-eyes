# -*- coding: utf-8 -*-
"""Ghi 3 dòng provenance cho thumbnail Tập 23 (VI / EN / JA) — L7.

Nền dùng chung: assets/bg/t23_a2_19_psychological_signature_pentagram_wall.png
(đã có dòng provenance riêng: Cloudflare Workers AI FLUX.1-schnell, 20/11/2026).
"""
import json
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROV = ROOT / "provenance.json"
BACKUP = ROOT / ".work" / "_cu" / f"provenance.json.bak_t23_thumb_{int(time.time())}"

shutil.copy2(PROV, BACKUP)
print("Backup created:", BACKUP)

with open(PROV, "r", encoding="utf-8") as f:
    data = json.load(f)

BG = "t23_a2_19_psychological_signature_pentagram_wall"
entries = [
    {
        "file": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap23/xuat_ban/thumbnail.png",
        "loai": "ảnh đại diện 1280×720 (RGB)",
        "cong_cu": f".work/package.py thumbnail() — nền {BG} + chữ Pillow (segoeuib.ttf)",
        "ngay": "2026-11-25",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự tạo theo kịch bản Tập 23 (Cloudflare FLUX); linh thú & logo kênh",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": 'Dòng chữ: NIGHT STALKER · SAY MÊ KẺ ÁC (EPISODES["23"]["thumb"] nhánh VI).',
    },
    {
        "file": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap23_EN/xuat_ban/thumbnail.png",
        "loai": "ảnh đại diện 1280×720 (RGB)",
        "cong_cu": f".work/package.py thumbnail() — nền {BG} + chữ Pillow (segoeuib.ttf)",
        "ngay": "2026-11-25",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự tạo theo kịch bản Tập 23 (Cloudflare FLUX); linh thú & logo kênh",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": 'Dòng chữ: NIGHT STALKER · HYBRISTOPHILIA (EPISODES["23"]["thumb"] nhánh EN).',
    },
    {
        "file": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap23_JA/xuat_ban/thumbnail.png",
        "loai": "ảnh đại diện 1280×720 (RGB)",
        "cong_cu": f".work/package.py thumbnail() — nền {BG} + chữ Pillow (YuGothB.ttc)",
        "ngay": "2026-11-25",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự tạo theo kịch bản Tập 23 (Cloudflare FLUX); linh thú & logo kênh",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": 'Dòng chữ: ナイト・ストーカー · 犯罪者愛好症 (EPISODES["23"]["thumb"] nhánh JA).',
    },
]

existing = {e["file"]: i for i, e in enumerate(data) if isinstance(e, dict) and "file" in e}
for item in entries:
    if item["file"] in existing:
        data[existing[item["file"]]] = item
        print("Updated:", item["file"])
    else:
        data.append(item)
        print("Added:", item["file"])

with open(PROV, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("Provenance updated. Total entries:", len(data))
