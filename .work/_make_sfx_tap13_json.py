#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo bảng âm thanh stereo Tập 13: sfx_tap13.json, sfx_tap13_EN.json, sfx_tap13_JA.json.
Tuân thủ tiêu chuẩn A4.4 của kênh Amber Eyes và AGENTS.md (A1, A2).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

data = {
    "_doc": "Bảng âm thanh stereo Tập 13 — Vỏ Bọc 'Con Nhà Người Ta' (Hồ Sơ Jennifer Pan). Đọc bởi build_audio3.py::place_sheet().",
    "ambience": [
        ["1.02#1", "1.11#4", "clock_tick.wav", -35],
        ["2.02#1", "2.11#6", "t2/amb_basement.wav", -34],
        ["3.02#1", "3.08#4", "amb_ceiling_fan.wav", -35],
        ["4.02#1", "4.10#4", "amb_hospital_monitor_heartbeat.wav", -34],
        ["5.02#1", "5.05#23", "clock_tick.wav", -35]
    ],
    "cues": [
        ["1.03", "start", 0.0, "clock_tick.wav", -16],
        ["1.05", "start", 0.0, "t13/fx_sandpaper_scrape_eraser.wav", -12],
        ["1.08", "start", 0.0, "paper_rustle.wav", -14],
        ["2.03", "start", 0.0, "fx_phone_vibrate.wav", -12],
        ["2.05", "start", 0.0, "lock_door.wav", -12],
        ["2.05", "start", 1.2, "t13/fx_footsteps_wood_heavy.wav", -12],
        ["2.07", "start", 0.0, "t13/fx_gunshots_pistol_inside.wav", -10],
        ["2.09", "start", 0.0, "fx_dtmf_touch_tone_beep.wav", -14],
        ["2.09", "start", 0.8, "t13/fx_crying_female_phone.wav", -12],
        ["2.09", "start", 2.5, "police_siren_distant.wav", -14],
        ["4.04", "start", 0.0, "heart_beep.wav", -14],
        ["4.07", "start", 0.0, "t13/fx_metal_door_push_open.wav", -12],
        ["4.07", "start", 1.2, "paper_rustle.wav", -14],
        ["5.05#23", "end", -0.5, "folder_close.wav", -8]
    ],
    "music_drop": {
        "_doc": "Tắt nhạc có giai điệu (giữ nền môi trường) ở các câu hé lộ — Rule A1/V4. [từ câu, đến câu]",
        "ranges": [
            ["1.06#1", "1.06#4"],
            ["2.08#1", "2.08#5"],
            ["4.06#1", "4.06#6"]
        ]
    }
}

for name in ["sfx_tap13.json", "sfx_tap13_EN.json", "sfx_tap13_JA.json"]:
    p = ROOT / name
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created {p} successfully!")
