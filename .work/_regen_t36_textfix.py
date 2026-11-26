#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lại 3 ảnh nền Tập 36 bị lỗi chữ AI vẽ (H20/H26) — giữ nguyên TÊN/MÃ, chỉ sửa prompt.

Lỗi phát hiện bằng mắt trên montage (25/11/2026):
  a1_05_small_fiat_leaving_florence_night  -> biển số xe ghi "FISC7AL / 1LR 21IS" + chữ hãng xe
  a3_29_quantico_profile_1989_loner...     -> logo "FBI" + chữ vô nghĩa "TFEPNN" trên hộp
  a4_06_postman_bicycle_and_slow_lonely... -> chữ graffiti vô nghĩa "TEE" trên tường

Quy trình: dời ảnh cũ vào .work/_cu/bg_old_<ngày>/t36_replaced/ -> sửa prompt trong
bg_jobs_tap36.json -> sinh lại cùng tên -> cập nhật provenance.json.
"""
import json
import shutil
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL  # noqa: E402

BG = ROOT / "assets" / "bg"
JOBS_FILE = WORK / "bg_jobs_tap36.json"
PROV_FILE = ROOT / "provenance.json"
OLD_DIR = WORK / "_cu" / f"bg_old_{date.today().strftime('%Y%m%d')}" / "t36_replaced"

NO_TEXT = (
    " absolutely no text anywhere, no letters, no words, no numbers, no logos, no signage, "
    "no labels, no badges, no license plate characters, no graffiti, all surfaces blank and unmarked"
)

FIX = {
    "t36_a1_05_small_fiat_leaving_florence_night":
        "A distant wide rear view of a small vintage 1960s Italian compact car driving away from "
        "the lit rooftops and dome of Florence at late night, the car small and far in the frame, "
        "taillights glowing on a dark road, deep blue night haze over the city, "
        "the rear bumper and plate area completely blank and unmarked" + NO_TEXT,
    "t36_a3_29_quantico_profile_1989_loner_manual_laborer_map":
        "A dim government behavioural analysis office in 1989 with a corkboard of plain blank sheets "
        "forming a loose human outline of a lone middle-aged laborer silhouette, a toy-like model car "
        "and a plain hill contour map on the table, cold desk lamp, heavy shadow, "
        "no emblems or insignia on any object" + NO_TEXT,
    "t36_a4_06_postman_bicycle_and_slow_lonely_silhouette":
        "A rural Italian dirt lane at dusk with a postman's bicycle leaning against a plain unplastered "
        "wall and a lone slow-moving silhouette of a heavyset man standing in the distance, faces hidden, "
        "empty bare wall surface" + NO_TEXT,
}


def update_provenance(rec):
    prov = json.loads(PROV_FILE.read_text(encoding="utf-8"))
    by_file = {r["file"]: i for i, r in enumerate(prov)}
    entry = {
        "file": rec["file"], "loai": "nền 16:9 dùng chung 4 ngôn ngữ",
        "cong_cu": f"Cloudflare Workers AI ({DEFAULT_MODEL})", "ngay": str(date.today()),
        "prompt": rec["prompt"], "seed": None, "nguon_anh_tham_chieu": None,
        "kich_thuoc_goc": [2112, 1188], "dieu_khoan": "Cloudflare Workers AI Terms of Service",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Sinh nền bằng Cloudflare FLUX.1 schnell, chuẩn Deep Noir H21/H25/H26, crop 16:9 và resize 2112x1188",
    }
    if rec["file"] in by_file:
        prov[by_file[rec["file"]]] = entry
    else:
        prov.append(entry)
    PROV_FILE.write_text(json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    if not get_credentials()[0]:
        print("LỖI: thiếu Cloudflare credentials")
        sys.exit(1)
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    OLD_DIR.mkdir(parents=True, exist_ok=True)

    for j in jobs:
        if j["name"] not in FIX:
            continue
        old = BG / f"{j['name']}.png"
        if old.exists():
            shutil.move(str(old), str(OLD_DIR / old.name))
            print(f"-> Dời ảnh cũ: {old.name} -> {OLD_DIR.relative_to(ROOT)}")
        j["prompt"] = FIX[j["name"]]

    JOBS_FILE.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
    print("-> Đã cập nhật prompt trong bg_jobs_tap36.json")

    ok = 0
    for j in jobs:
        if j["name"] not in FIX:
            continue
        dst = BG / f"{j['name']}.png"
        t0 = time.perf_counter()
        try:
            img = generate_16_9_background(prompt=j["prompt"], steps=4,
                                           out_size=(2112, 1188), with_noir_style=True)
            img.save(dst, "PNG", optimize=True)
            print(f"XONG {j['name']} ({dst.stat().st_size//1024} KB, {time.perf_counter()-t0:.1f}s)")
            update_provenance({"file": f"assets/bg/{j['name']}.png", "prompt": j["prompt"]})
            ok += 1
        except Exception as e:
            print(f"LỖI {j['name']}: {e}")
    print(f"\nHOÀN TẤT: {ok}/{len(FIX)} ảnh sinh lại.")


if __name__ == "__main__":
    main()
