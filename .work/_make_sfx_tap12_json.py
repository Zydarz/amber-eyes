#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo bảng âm thanh stereo Tập 12: sfx_tap12.json, sfx_tap12_EN.json, sfx_tap12_JA.json.
Tuân thủ tiêu chuẩn A4.4 của kênh Amber Eyes và AGENTS.md (A1, A2).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

data = {
    "_doc": "Bảng âm thanh stereo Tập 12 — Thảm Kịch Jonestown (Jim Jones & Peoples Temple). Đọc bởi build_audio3.py::place_sheet().",
    "ambience": [
        ["1.02#1", "1.11#5", "t12/amb_wind_tropical.wav", -33],
        ["2.02#1", "2.07#8", "t12/amb_crowd_singing_acoustic.wav", -32],
        ["2.09#1", "2.13#8", "t12/amb_tractor_engine.wav", -33],
        ["3.02#1", "3.08#4", "amb_ceiling_fan.wav", -35],
        ["4.02#1", "4.11#6", "t12/amb_crowd_arguing_indoor.wav", -32],
        ["5.02#1", "5.05#23", "t12/amb_wind_tropical.wav", -33]
    ],
    "cues": [
        ["1.03", "start", 0.0, "paper_rustle.wav", -14],
        ["1.05", "start", 0.0, "amb_helicopter_far.wav", -12],
        ["1.08", "start", 0.0, "t12/amb_loudspeaker_jungle_echo.wav", -12],
        ["2.03", "start", 0.0, "t12/amb_crowd_singing_acoustic.wav", -12],
        ["2.05", "start", 0.0, "t12/amb_small_plane_engine.wav", -14],
        ["2.08", "start", 0.0, "amb_alarm_siren_distant.wav", -12],
        ["2.08", "start", 1.5, "t12/fx_gunshots_rifle_shotgun.wav", -10],
        ["2.10", "start", 0.0, "fx_mic_hum_feedback.wav", -14],
        ["2.12", "start", 0.0, "t12/amb_crowd_arguing_indoor.wav", -14],
        ["4.03", "start", 0.0, "footsteps.wav", -14],
        ["4.05", "start", 0.0, "fx_knock_table.wav", -10],
        ["4.05", "start", 1.2, "fx_mic_hum_feedback.wav", -14],
        ["5.05#23", "end", -0.5, "folder_close.wav", -8]
    ],
    "music_drop": {
        "_doc": "Tắt nhạc có giai điệu (giữ nền môi trường) ở các câu hé lộ — Rule A1/V4. [từ câu, đến câu]",
        "ranges": [
            ["1.06#1", "1.06#8"],
            ["2.09#1", "2.09#5"],
            ["4.06#1", "4.06#4"]
        ]
    }
}

for name in ["sfx_tap12.json", "sfx_tap12_EN.json", "sfx_tap12_JA.json"]:
    p = ROOT / name
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created {p} successfully!")
