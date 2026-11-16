#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo bảng âm thanh stereo Tập 16: sfx_tap16.json, sfx_tap16_EN.json, sfx_tap16_JA.json.
Tuân thủ tiêu chuẩn A4.4 của kênh Amber Eyes và AGENTS.md (A1, A2, A12).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

data = {
    "_doc": "Bảng âm thanh stereo Tập 16 — Hồ Sơ John List. Đọc bởi build_audio3.py::place_sheet().",
    "ambience": [
        ["1.02#1", "1.11#5", "amb_ceiling_fan.wav", -35],
        ["2.02#1", "2.10#8", "clock_tick.wav", -35],
        ["3.02#1", "3.08#5", "amb_ceiling_fan.wav", -35],
        ["4.02#1", "4.12#4", "amb_crowd_murmur_courtroom.wav", -35],
        ["5.02#1", "5.05#18", "amb_ocean_waves_soft.wav", -34]
    ],
    "cues": [
        ["1.03", "start", 0.0, "police_siren_distant.wav", -14],
        ["1.03", "start", 1.2, "fx_footsteps_run_wet_pavement.wav", -14],
        ["1.05", "start", 0.0, "paper_rustle.wav", -14],
        ["1.05", "start", 1.0, "clock_tick.wav", -14],
        ["1.08", "start", 0.0, "t16/fx_metal_lock_open.wav", -12],
        ["1.08", "start", 1.2, "t16/fx_footsteps_dusty_wood_slow.wav", -12],
        ["2.03", "start", 0.0, "t16/fx_scissors_cut_paper.wav", -12],
        ["2.03", "start", 1.0, "paper_rustle.wav", -14],
        ["2.05", "start", 0.0, "t16/amb_train_horn_distant_night.wav", -14],
        ["2.07", "start", 0.0, "paper_rustle.wav", -14],
        ["2.07", "start", 1.2, "typewriter.wav", -14],
        ["4.03", "start", 0.0, "t16/fx_chisel_hammer_clay.wav", -12],
        ["4.03", "start", 1.2, "t16/fx_breathing_focused_artist.wav", -14],
        ["4.05", "start", 0.0, "fx_phone_ring_landline_night.wav", -12],
        ["4.05", "start", 1.2, "amb_tv_camera_operator.wav", -16],
        ["4.07", "start", 0.0, "fx_car_tire_screech_stop.wav", -12],
        ["4.07", "start", 1.2, "door_creak.wav", -12],
        ["5.05#18", "end", -0.5, "folder_close.wav", -8]
    ],
    "music_drop": {
        "_doc": "Tắt nhạc có giai điệu (giữ nền môi trường) ở các câu hé lộ — Rule A1/V4. [từ câu, đến câu]",
        "ranges": [
            ["1.09#1", "1.09#7"],
            ["2.04#1", "2.04#8"],
            ["4.08#1", "4.08#5"]
        ]
    }
}

for name in ["sfx_tap16.json", "sfx_tap16_EN.json", "sfx_tap16_JA.json"]:
    p = ROOT / name
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created {p} successfully!")
