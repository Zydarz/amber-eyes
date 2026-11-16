#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo bảng âm thanh stereo Tập 17: sfx_tap17.json, sfx_tap17_EN.json, sfx_tap17_JA.json.
Tuân thủ tiêu chuẩn A4.4 của kênh Amber Eyes và AGENTS.md (A1, A2, A12).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

data = {
    "_doc": "Bảng âm thanh stereo Tập 17 — Hồ Sơ Gia Đình Turpin. Đọc bởi build_audio3.py::place_sheet().",
    "ambience": [
        ["1.02#1", "1.11#4", "amb_ceiling_fan.wav", -35],
        ["2.02#1", "2.10#7", "clock_tick.wav", -35],
        ["3.02#1", "3.08#4", "amb_ceiling_fan.wav", -35],
        ["4.02#1", "4.12#4", "amb_crowd_murmur_courtroom.wav", -35],
        ["5.02#1", "5.05#24", "amb_ocean_waves_soft.wav", -34]
    ],
    "cues": [
        ["1.03", "start", 0.0, "fx_dtmf_touch_tone_beep.wav", -14],
        ["1.03", "start", 1.0, "fx_footsteps_run_gravel.wav", -14],
        ["1.03", "start", 1.8, "fx_breathing_tense_close.wav", -14],
        ["1.05", "start", 0.0, "t17/fx_911_call_recording_radio.wav", -12],
        ["1.05", "start", 1.2, "keyboard_night.wav", -14],
        ["1.08", "start", 0.0, "door_knock.wav", -12],
        ["1.08", "start", 1.2, "lock_door.wav", -12],
        ["2.03", "start", 0.0, "t17/amb_carnival_ride_music_far.wav", -15],
        ["2.05", "start", 0.0, "chains.wav", -12],
        ["2.05", "start", 1.2, "footsteps.wav", -14],
        ["2.07", "start", 0.0, "t17/fx_candy_wrapper_open.wav", -12],
        ["2.07", "start", 1.2, "t17/fx_fridge_door_open.wav", -12],
        ["4.03", "start", 0.0, "amb_crowd_murmur_courtroom.wav", -16],
        ["4.03", "start", 1.0, "fx_mic_hum_feedback.wav", -16],
        ["4.05", "start", 0.0, "fx_sigh_emotional.wav", -14],
        ["4.05", "start", 1.2, "paper_rustle.wav", -14],
        ["4.07", "start", 0.0, "gavel.wav", -10],
        ["5.05#24", "end", -0.5, "folder_close.wav", -8]
    ],
    "music_drop": {
        "_doc": "Tắt nhạc có giai điệu (giữ nền môi trường) ở các câu hé lộ — Rule A1/V4. [từ câu, đến câu]",
        "ranges": [
            ["1.09#1", "1.09#6"],
            ["2.06#1", "2.06#7"],
            ["4.08#1", "4.08#5"]
        ]
    }
}

for name in ["sfx_tap17.json", "sfx_tap17_EN.json", "sfx_tap17_JA.json"]:
    p = ROOT / name
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created {p} successfully!")
