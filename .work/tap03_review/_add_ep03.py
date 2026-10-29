#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thêm khối EPISODES["03"] vào .work/edition.py (kịch bản vụ Edmund Kemper).

Giá trị cue đã đối chiếu với build_audio3.py:
  act1_cue   -> mốc NHẠC mở đầu hồi 1  -> 1.14 [BGM] "Cello u uất hòa cùng tiếng piano chậm rãi"
  silence_cue-> mốc NGHI (có start/end)   -> 1.11 [NGHI] "Nhạc nền dừng lại, chỉ còn tiếng bước chân..."
  click_cues -> mốc SFX "băng ghi âm bật"  -> 1.08 [SFX] "Tiếng băng ghi âm bật nhẹ 'Tách'."
(Note trong REVIEW E1 dùng 1.02 / 1.10 / 1.02 — sai theo docstring của builder, đã sửa ở đây.)
"""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ED = Path(r"D:\TEST\Gax\Audi\.work\edition.py")
raw = ED.read_text(encoding="utf-8")

assert '"03": {' not in raw, "EPISODES['03'] da ton tai — khong chen lai"

NEED = ["1.05#3", "1.10#1", "1.10#10", "1.13#7", "2.04#5", "2.06#2", "3.05#7", "3.05#10",
        "3.08#8", "3.08#10", "4.05#15", "4.05#19", "4.08#2", "5.02#5", "5.02#7", "5.02#12",
        "5.05#4", "5.05#5", "5.08#3"]

BLOCK = '''    "03": {
        "script": WORK / "script_tap03.json",
        "dir": "Tap03",
        "plan": "KeHoach_Video_Tap03.md",
        "master": "Tap03_master",
        "srt": "Tap03.srt",
        "n_element": {"1.09": "N1", "2.09": "N2"},
        "acting": WORK / "acting_tap03.json",
        "sfx_sheet": WORK / "sfx_tap03.json",
        "act1_cue": "1.14", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_piano_minimal.mp3"),
                2: ("bgm_ambient_deep.mp3",),
                3: "bgm_cello_sad_v2.mp3",
                4: "bgm_sub_drone.mp3",
                5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("IQ 145", "GƯƠNG"),
        "thumb_bg": "t3_brain_mirror",
        "title": "Gã Khổng Lồ IQ 145 — Hồ sơ Edmund Kemper & nguyên lý FBI dựng chữ ký tâm lý",
        "act_titles": {1: "Kẻ Khổng Lồ Trong Bóng Tối",
                       2: "Đêm Của Mẹ",
                       3: "Cái Hầm Của Kẻ Săn Nhân",
                       4: "Khoảnh Khắc Bị Bắt Quả Tang",
                       5: "Công Cố Tội Ác Và Những Câu Hỏi Chưa Có Lời Giải"},
        "summary": ("1.03#1", "5.08#1"),
        "need": {need},
        "case": "Kemper",
        "n1": ("TRỰC BAN CẢNH SÁT SANTA CRUZ", "Người trực đêm", "TRỰC BAN"),
        "n2": ("CẢNH SÁT QUÁN RƯỢU", "Đồng nghiệp tại The Jury Room", "CẢNH SÁT"),
        "cast": None,                  # dùng giọng mặc định của kênh (bộ A)
    },
'''.replace("{need}", repr(NEED).replace("'", '"'))

# chen ngay truoc khoi "04"
anchor = '    "04": {\n'
assert raw.count(anchor) == 1, "khong tim thay khoi 04"
raw = raw.replace(anchor, BLOCK + anchor, 1)

ED.write_text(raw, encoding="utf-8")
print(f"Da chen EPISODES['03'] vao {ED}")
print(f"  need: {len(NEED)} ma cau")
