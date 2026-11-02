#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong provenance cho tai san JA Tap 02 (L7: moi tai san phai co dong).

Ghi them vao provenance.json (danh sach 2148 dong). Backup truoc.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROV = ROOT / "provenance.json"
BK = W / "_cu" / "provenance_pre_ja_t02_20261102.json"
if not BK.exists():
    shutil.copy2(PROV, BK)
    print(f"backup -> {BK.relative_to(ROOT)}")

data = json.loads(PROV.read_text(encoding="utf-8-sig"))
existing = {r.get("file") for r in data}
print(f"truoc: {len(data)} dong")

refs = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/refs.json").read_text(encoding="utf-8-sig"))
ROLE_JA = {"H": "ホスト (Cú) · 122,1 Hz · CER mẫu 1,2%",
           "D": "捜査官 (Sói) · 87,4 Hz · CER mẫu 1,9%",
           "C": "心理学者 (Cáo)", "N1": "証人 (Cừu)", "N2": "視聴者 (Mèo)"}
SRC_FILE = {"H": "assets/voice_ref_voxcpm2_ja3/H_JA.wav",
            "D": "assets/voice_ref_voxcpm2_ja3/D_JA.wav",
            "C": "assets/voice_ref_voxcpm2_ja3/C_JA.wav",
            "N1": "assets/voice_ref_voxcpm2_ja3/N1_JA.wav",
            "N2": "assets/voice_ref_voxcpm2_ja3/N2_JA.wav"}
FALLBACK = {"H": "W6_LOW_lowwarm_ja3_t01", "D": "D_smokerbass_ja3_t02",
            "C": "C_altobrisk_ja3_t01", "N1": "W6_LOW_huskycontralto_ja3_t01",
            "N2": "W6_LOW_deepalto_ja3_t01"}

new = []


def add(file, loai, cong_cu, ngay, prompt=None, seed=None, dieu_khoan=None, kiem=None, **kw):
    if file in existing:
        return
    row = {"file": file, "loai": loai, "cong_cu": cong_cu, "ngay": ngay,
           "prompt": prompt, "seed": seed, "dieu_khoan": dieu_khoan,
           "kiem_tra_thuong_mai": kiem}
    row.update(kw)
    new.append(row)
    existing.add(file)


# 1) intro JA
add("assets/brand/intro_kenh_JA_t02.mov", "intro (chỉ hình) — bản tiếng Nhật",
    ".work/make_intro.py — Pillow + ffmpeg, từ logo tự vẽ",
    "2026-10-25", None, None, "Kênh tự tạo", "đạt (phần hình)",
    ghi_chu="Cắt 0–20,50 s trong renderer; 20,50–22,80 s shot 1-00 mở dần từ đuôi đen intro")

# 2) bo giong mau JA (VoxCPM2 vong 3) + phien ban da dung cho Higgs
add("assets/voice_ref_voxcpm2_ja3/", "bộ giọng mẫu tiếng Nhật (VoxCPM2 vòng 3) — 40 clip ứng viên",
    "VoxCPM2 (OpenBMB) — Voice Design, qua .work/higgs_make_refs_voxcpm.py",
    "2026-10-31", "control_instruction tiếng Anh mô tả chất giọng + target_text tiếng Nhật (xem refs.json)",
    "seed 7 (nhóm D) / seed 77 (nhóm C)", "VoxCPM2 — cần kiểm tra điều khoản thương mại", "chưa",
    ghi_chu="5 clip được chọn làm giọng mẫu vai: " + ", ".join(f"{k}←{FALLBACK[k]}" for k in ROLE_JA))

for role, desc in ROLE_JA.items():
    add(SRC_FILE[role], f"giọng mẫu JA vai {role} — {desc}",
        "VoxCPM2 (OpenBMB) — Voice Design, cắt từ clip ứng viên vòng 3, đóng gói làm dataset Higgs",
        "2026-10-31", None, None, "VoxCPM2 — cần kiểm tra điều khoản thương mại", "chưa",
        ghi_chu=f"Nguồn: assets/voice_ref_voxcpm2_ja3/{FALLBACK[role]}.wav")

# 3) audio san xuat Higgs JA Tap 02
add(".work/audio_s_higgs_JA_t02/", "audio TTS tiếng Nhật — 203 câu (vòng r2)",
    "Higgs Audio v3 trên Kaggle GPU — .work/higgs_prod_r2_JA_t02_kaggle.ipynb + .work/install_higgs_audio.py",
    "2026-11-01", "clone từ giọng mẫu JA (Voice Design của VoxCPM2)", None,
    "Higgs Audio v3 — cần kiểm tra điều khoản thương mại", "chưa",
    ghi_chu="35/203 câu vượt ngưỡng CER 2% (xem .work/higgs_cer_report_JA_t02.md) — đã có bản vòng 2 chọn ưu tiên")

# 4) thanh pham va video JA Tap 02
add("02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp3", "audio tổng bản tiếng Nhật (1791,85 s)",
    "TTS Higgs Audio v3 (203 câu) + nhạc assets/bgm + tiếng động assets/sfx (kênh tự tổng hợp bằng code) "
    "ghép bằng .work/build_audio3.py (loudnorm I=-16, trần đỉnh -1,5 dBFS)",
    "2026-11-01", None, None, "TTS: Higgs — cần kiểm tra; nhạc/SFX: kênh tự tạo", "chưa",
    ghi_chu="Lời đầu 23,0 s · lời cuối hết 1865,3 s · hồi 1: 23,0–374,0 · hồi 5: 1501,4–1865,3 (timeline_s_JA_t02.json)")

add("02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp4", "video tổng bản tiếng Nhật",
    ".work/build_video3.py (Pillow + ffmpeg libopenh264, 6 worker) ghép .work/package.py --mux "
    "(AAC 192k, alimiter latency=1)",
    "2026-11-02", None, None, "Hình: kênh tự tạo · nhạc/SFX: kênh tự tạo", "chưa",
    ghi_chu="151 shot · nền dùng lại 100% từ assets/bg của bản VN/EN · chữ do Pillow vẽ bằng YuGothB/YuGothM")

# 5) phu de JA
add("02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt", "phụ đề bản tiếng Nhật (212 cue)",
    ".work/subtitles.py — tách từ timeline_s_JA_t02.json, nhãn vai [ホスト]/[捜査官]/[心理学者]/[証人]/[視聴者]",
    "2026-11-02", None, None, "Kênh tự tạo", "đạt",
    ghi_chu="UTF-8 không BOM, CRLF — cùng định dạng với bản VN/EN")

for r in new:
    print("  +", r["file"])
print(f"\nthem: {len(new)} dong")
PROV.write_text(json.dumps(data + new, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"sau: {len(data) + len(new)} dong · file = {PROV.stat().st_size} byte")
