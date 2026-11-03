#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong provenance.json cho thanh pham Tap06 (L7).

Chay SAU khi package.py --mux xong.
"""
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PROV = ROOT / "provenance.json"
NGAY = "2026-11-02"

NEW = [
    {
        "file": "02_SAN_XUAT/Tap06/xuat_ban/Tap06_master.mp3",
        "loai": "audio master tiếng Việt (Higgs Audio v3) — 1265,4 s · −16,2 LUFS · true peak −1,6 dBFS · 154/154 câu",
        "cong_cu": "Higgs Audio v3 (Boson AI) chạy trên Kaggle GPU — bộ giọng thật tiếng Việt: H `H` · D `D3_SH` · C `C2_AB03` · N1 `W6_LOW` · N2 `W5_HIGH`; không thẻ cảm xúc",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Boson AI Higgs Audio — https://www.boson.ai/higgs-audio (ghi công trong mô tả YouTube theo QUY_TAC_AUDIO_HIGGS §2)",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "3 lượt TTS (309 file → 62 file → 12 file đổi chữ); CER vòng 3 = 0%; QC thứ hai bằng Whisper large-v3 + UTMOS trên Kaggle; danh sách nghe ở 02_SAN_XUAT/Tap06/CanNghe_Tap06_higgs.md",
    },
    {
        "file": "02_SAN_XUAT/Tap06/xuat_ban/Tap06_master.mp4",
        "loai": "video 1920×1080@30 H.264 + AAC (21:05) — dựng lại từ bảng shot 73 shot viết lại theo 154 câu",
        "cong_cu": ".work/build_video3.py --workers 6 (hình) + .work/package.py --mux (ghép âm thanh, alimiter latency=1)",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự vẽ bằng code (assets/bg/t6_*) + chữ vẽ bằng Pillow; không dùng tài sản tải ngoài",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Bảng shot viết lại theo nội dung câu (A11 #67): sửa 26 dòng, thêm shot 1-15 (1.08#6), xoá shot 3-04; sửa 10 dòng sai cột Vai; sửa số trên hình không có trong câu + câu trích không nguyên văn; đưa handoff →X về đúng cột (0/73 shot → 18/73)",
    },
    {
        "file": "02_SAN_XUAT/Tap06/xuat_ban/Tap06.srt",
        "loai": "phụ đề (324 cue, UTF-8 không BOM, CRLF)",
        "cong_cu": ".work/subtitles.py — tách từ timeline_s_t06.json, nhãn vai [HOST]/[ĐỀU TRA VIÊN]/[CHUYÊN GIA TÂM LÝ]/[KIM BYERS]/[MIKE ALBRECHT]",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Kênh tự tạo",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Lời đầu 00:00:23,000; cue cuối kết ở 00:20:55,810 (âm thanh kết 1255,8 s)",
    },
    {
        "file": "02_SAN_XUAT/Tap06/xuat_ban/thumbnail.png",
        "loai": "ảnh đại diện 1920×1080",
        "cong_cu": ".work/package.py thumbnail() — nền t6_clown_mirror_chiaroscuro + chữ Pillow",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Nền tự vẽ bằng code; không dùng tài sản tải ngoài",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Dòng chữ: NỤ CƯỜI CHÚ HỀ · 29 BÍ MẬT DƯỚI SÀN",
    },
    {
        "file": "02_SAN_XUAT/Tap06/xuat_ban/mo_ta.txt",
        "loai": "mô tả YouTube (sinh ra, KHÔNG sửa tay — sửa ở package.py + edition.py)",
        "cong_cu": ".work/package.py description()",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Kênh tự tạo",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Có dòng ghi công Higgs Audio (voice_credit) + dòng hashtag; mốc chương lấy từ timeline_s_t06.json",
    },
    {
        "file": "02_SAN_XUAT/Tap06/xuat_ban/nguon_tham_khao.md",
        "loai": "danh mục nguồn tham khảo (NGƯỜI DÙNG điền — AI không bịa link)",
        "cong_cu": ".work/package.py nguon()",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Kênh tự tạo",
        "kiem_tra_thuong_mai": "chưa — cần người dùng điền link nguồn cho từng dữ kiện nói về người thật",
        "ghi_chu": "Còn để trống link cho người dùng điền (A10)",
    },
]

prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
before = len(prov)
prov = [e for e in prov if not (e.get("file") or "").startswith("02_SAN_XUAT/Tap06/xuat_ban/")]
removed = before - len(prov)
prov.extend(NEW)
PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"provenance.json: {before} -> {len(prov)} dong (thay {removed} dong Tap06 cu, them {len(NEW)})")
