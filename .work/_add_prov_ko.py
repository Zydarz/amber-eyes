# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
prov_p = ROOT / "provenance.json"

with open(prov_p, "r", encoding="utf-8") as f:
    data = json.load(f)

existing = {x.get("file") for x in data}

entries_ko = [
    {
        "file": "assets/brand/intro_kenh_KO_t01.mov",
        "loai": "video intro",
        "cong_cu": ".work/make_intro.py (Pillow vẽ vector + Malgun Gothic Bold, ghép ffmpeg)",
        "ngay": "2026-10-24",
        "prompt": None,
        "dieu_khoan": "Kênh tự tạo bằng code và font hệ thống Windows",
        "kiem_tra_thuong_mai": "đạt"
    },
    {
        "file": "02_SAN_XUAT/Tap01_KO/xuat_ban/Tap01_KO_master.mp3",
        "loai": "audio tổng",
        "cong_cu": "TTS MiniMax tiếng Hàn (5 giọng, 128 câu) + nhạc assets/bgm + 11 hiệu ứng âm thanh assets/sfx ghép bằng .work/build_audio3.py",
        "ngay": "2026-10-24",
        "prompt": None,
        "dieu_khoan": "<điều khoản MiniMax — cần người dùng kiểm tra>",
        "kiem_tra_thuong_mai": "chưa"
    },
    {
        "file": "02_SAN_XUAT/Tap01_KO/xuat_ban/Tap01_KO_master.mp4",
        "loai": "video",
        "cong_cu": "Hình: .work/build_video3.py từ assets/bg, assets/cast + đồ hoạ Pillow (Malgun Gothic); tiếng: Tap01_KO_master.mp3",
        "ngay": "2026-10-24",
        "prompt": None,
        "dieu_khoan": "<theo các tài sản thành phần>",
        "kiem_tra_thuong_mai": "chưa"
    },
    {
        "file": "02_SAN_XUAT/Tap01_KO/xuat_ban/thumbnail.png",
        "loai": "thumbnail",
        "cong_cu": "house_police + đồ hoạ chữ Hàn Malgun Gothic Bold, .work/package.py",
        "ngay": "2026-10-24",
        "prompt": None,
        "dieu_khoan": "<theo các tài sản thành phần>",
        "kiem_tra_thuong_mai": "chưa"
    },
    {
        "file": "02_SAN_XUAT/Tap01_KO/xuat_ban/Tap01_KO.srt",
        "loai": "phụ đề",
        "cong_cu": "Sinh từ kịch bản KO + timeline_s_KO.json, .work/subtitles.py",
        "ngay": "2026-10-24",
        "prompt": None,
        "dieu_khoan": "Kênh tự tạo",
        "kiem_tra_thuong_mai": "đạt"
    }
]

added = 0
for entry in entries_ko:
    if entry["file"] not in existing:
        data.append(entry)
        existing.add(entry["file"])
        added += 1

with open(prov_p, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {added} entries to provenance.json. Total entries now: {len(data)}")
