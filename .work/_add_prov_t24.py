#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thêm dòng provenance cho thumbnail Tập 24 (VI/EN/JA) vào provenance.json.

Dùng:  py -3 .work/_add_prov_t24.py
"""
import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "provenance.json"
BACKUP = ROOT / ".work" / "_cu" / f"provenance_t24_{date.today().isoformat().replace('-', '')}"
TODAY = date.today().isoformat()

THUMB = {
    "vi": ("02_SAN_XUAT/Ho_So_Toi_Pham/Tap24/xuat_ban/thumbnail.png", "segoeuib.ttf",
           "KÝ ỨC · HWASEONG"),
    "en": ("02_SAN_XUAT/Ho_So_Toi_Pham/Tap24_EN/xuat_ban/thumbnail.png", "segoeuib.ttf",
           "MEMORIES · HWASEONG"),
    "ja": ("02_SAN_XUAT/Ho_So_Toi_Pham/Tap24_JA/xuat_ban/thumbnail.png", "YuGothB.ttc",
           "記憶 · ファセオン"),
}


def main():
    rows = json.loads(PROV.read_text(encoding="utf-8"))
    existing = {r.get("file") for r in rows}
    BACKUP.mkdir(parents=True, exist_ok=True)
    shutil.copy(PROV, BACKUP / "provenance.json")
    added = 0
    for lang, (f, font, words) in THUMB.items():
        if f in existing:
            continue
        rows.append({
            "file": f,
            "loai": "ảnh đại diện 1280×720 (RGB)",
            "cong_cu": f".work/package.py thumbnail() — nền t24_a1_30_prison_cell_embroidery_desk_30 "
                      f"+ chữ Pillow ({font})",
            "ngay": TODAY,
            "prompt": None,
            "seed": None,
            "dieu_khoan": "Nền tự tạo theo kịch bản Tập 24 (Cloudflare Workers AI FLUX); "
                          "linh thú & logo kênh",
            "kiem_tra_thuong_mai": "đạt",
            "ghi_chu": f'Dòng chữ: {words} (EPISODES["24"]["thumb"] nhánh {lang.upper()}).',
        })
        added += 1
    PROV.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"provenance: +{added} dòng · tổng {len(rows)} · backup: {BACKUP/'provenance.json'}")


if __name__ == "__main__":
    main()
