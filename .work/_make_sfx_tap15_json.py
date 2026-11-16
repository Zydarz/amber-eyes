#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo bảng âm thanh stereo Tập 15: sfx_tap15.json, sfx_tap15_EN.json, sfx_tap15_JA.json.
Tuân thủ tiêu chuẩn A4.4 của kênh Amber Eyes và AGENTS.md (A1, A2, A12).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

data = {
    "_doc": "Bảng âm thanh stereo Tập 15 — Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới (Jodi Arias). Đọc bởi build_audio3.py::place_sheet().",
    "ambience": [
        ["1.03#1", "1.18#3", "amb_ceiling_fan.wav", -35],
        ["2.02#1", "2.08#9", "clock_tick.wav", -35],
        ["3.02#1", "3.11#6", "amb_ceiling_fan.wav", -35],
        ["4.03#1", "4.12#6", "amb_crowd_murmur_courtroom.wav", -35],
        ["5.02#1", "5.12#4", "amb_ocean_waves_soft.wav", -34]
    ],
    "cues": [
        ["1.03#1", "start", 0.0, "police_siren_distant.wav", -14],
        ["1.03#1", "start", 1.2, "radio_chatter.wav", -14],
        ["1.05#1", "start", 0.0, "fx_phone_ring_landline_night.wav", -12],
        ["1.05#1", "start", 1.5, "keyboard_night.wav", -14],
        ["1.08#1", "start", 0.0, "t15/fx_crime_scene_tape_pull.wav", -12],
        ["1.08#1", "start", 1.0, "t15/fx_footsteps_shoes_scuff.wav", -14],
        ["2.03#1", "start", 0.0, "fx_mouse_click_rapid.wav", -14],
        ["2.03#1", "start", 1.0, "t15/fx_computer_beep_restore.wav", -12],
        ["2.05#1", "start", 0.0, "t15/fx_mechanical_keyboard.wav", -12],
        ["2.05#1", "start", 1.5, "fx_inkjet_printer_run.wav", -14],
        ["2.07#1", "start", 0.0, "paper_rustle.wav", -14],
        ["2.07#1", "start", 1.2, "t15/fx_evidence_room_door.wav", -12],
        ["4.03#1", "start", 0.0, "fx_knock_table.wav", -12],
        ["4.03#1", "start", 1.2, "paper_rustle.wav", -14],
        ["4.05#1", "start", 0.0, "amb_tv_camera_operator.wav", -16],
        ["4.07#1", "start", 0.0, "fx_mic_hum_feedback.wav", -14],
        ["4.07#1", "start", 1.0, "amb_crowd_murmur_courtroom.wav", -16],
        ["5.12#4", "end", -0.5, "folder_close.wav", -8]
    ],
    "music_drop": {
        "_doc": "Tắt nhạc có giai điệu (giữ nền môi trường) ở các câu hé lộ — Rule A1/V4. [từ câu, đến câu]",
        "ranges": [
            ["1.10#1", "1.10#3"],
            ["2.07#1", "2.07#6"],
            ["4.08#1", "4.08#5"]
        ]
    }
}

for name in ["sfx_tap15.json", "sfx_tap15_EN.json", "sfx_tap15_JA.json"]:
    p = ROOT / name
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created {p} successfully!")
