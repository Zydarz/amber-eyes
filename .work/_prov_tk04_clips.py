# -*- coding: utf-8 -*-
"""Them provenance cho 15 clip TikTok Tap 04 (L7 / T9).

Ghi nguon: nen doc tk04_*.png (co dong provenance rieng) + master audio tap + logo H29.
Backup provenance truoc khi ghi.
"""
import json
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
PP = ROOT / "provenance.json"
BAK = ROOT / ".work" / "_cu" / "provenance_tk04_20261127" / "provenance.json"
BAK.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(PP, BAK)
print("backup:", BAK)

data = json.loads(PP.read_text(encoding="utf-8-sig"))
items = data if isinstance(data, list) else (data.get("tai_san") or data.get("items") or [])
have = {it.get("file") for it in items}

LANGS = [("VI", "Tap04", "tiếng Việt"), ("EN", "Tap04_EN", "tiếng Anh"), ("JA", "Tap04_JA", "tiếng Nhật")]
NOTES = {
    ("EN", "TK2"): "LƯU Ý: master audio EN TK2 chỉ có 9/11 câu — thiếu TK2.01#10 (vai C) và TK2.01#11 (CTA vai H), đuôi 14,76 s chỉ có nhạc nền (đo bằng ASR + kiểm RMS). Cần người dùng quyết định cách sửa.",
    ("VI", "TK1"): "LƯU Ý: clip có từ cấm A9.2 'sát hại' ở câu TK1.01#6 (cổng T13 trượt) — cần người dùng duyệt kịch bản.",
    ("VI", "TK3"): "LƯU Ý: clip có từ cấm A9.2 'sát hại' ở câu TK3.01#9 (cổng T13 trượt) — cần người dùng duyệt kịch bản.",
}

new = []
for tag, d, langname in LANGS:
    for n in range(1, 6):
        clip = "TK%d" % n
        f = "02_SAN_XUAT/TIKTOK/%s/%s_video.mp4" % (d, clip)
        if f in have:
            continue
        ghi_chu = ("Dung clip TikTok 9:16 cho Tap 04 (%s). Nguon hinh: nen doc goc assets/bg/tk04_*.png "
                   "(23 nen, 1080x1920, co dong provenance rieng) + camera still/push/pull/pan. "
                   "Logo kenh ghep theo H29 (assets/brand/watermark.png, 96 px, do mo 35%%) tai x 684-780, y 60-156 "
                   "(A11 #198). Am thanh: master san co %s/%s_master_audio.mp3 (Higgs Audio v3 + BGM/SFX tap). "
                   "Khong co chu tren hinh (H26). QC 14 cong T1-T14: xuat .work/_qc_tk04_clip.json."
                   % (langname, d, clip))
        if (tag, clip) in NOTES:
            ghi_chu += " " + NOTES[(tag, clip)]
        new.append({
            "file": f,
            "loai": "clip TikTok dọc 9:16 cho Tập 04 (%s)" % langname,
            "cong_cu": ("Pillow + ffmpeg/libopenh264 trên máy (script .work/_build_tk_tap04_video_notext.py); "
                        "mốc thời gian dựng lại bằng faster-whisper small + Needleman–Wunsch "
                        "(.work/_tk_asr_timeline_t04.py) vì WAV từng câu đã bị xoá"),
            "ngay": "2026-11-27",
            "prompt": "",
            "seed": None,
            "nguon_anh_tham_chieu": None,
            "kich_thuoc_goc": [1080, 1920],
            "dieu_khoan": ("Logo + nền do dự án tự vẽ (không dùng tài sản bên thứ ba). "
                           "Giọng đọc: Higgs Audio v3 (giọng nội bộ). "
                           "Nhạc nền: theo SPEC (bgm_ambient_tension.mp3) — file gốc KHÔNG còn trên đĩa, "
                           "chưa truy vết được nguồn ⇒ cần người dùng xác nhận T9."),
            "kiem_tra_thuong_mai": ("cần xác nhận: nguồn nhạc nền/SFX của clip chưa truy vết được "
                                    "(T9/L7) — chưa đủ điều kiện đăng"),
            "ghi_chu": ghi_chu,
        })

items.extend(new)
print("them %d dong provenance (tong %d)" % (len(new), len(items)))
# Giu NGUYEN format goc: indent=2, CRLF, khong BOM (do bang loi 211k dong diff khi ghi indent=1/LF)
out = json.dumps(data, ensure_ascii=False, indent=2).replace("\n", "\r\n")
PP.write_bytes(out.encode("utf-8"))
print("da ghi", PP)
