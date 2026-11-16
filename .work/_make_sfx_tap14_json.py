#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo bảng âm thanh stereo Tập 14: sfx_tap14.json, sfx_tap14_EN.json, sfx_tap14_JA.json.
Tuân thủ tiêu chuẩn A4.4 của kênh Amber Eyes và AGENTS.md (A1, A2).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

data = {
    "_doc": "Bảng âm thanh stereo Tập 14 — Bi kịch Betty Broderick. Đọc bởi build_audio3.py::place_sheet().",
    "ambience": [
        ["1.02#1", "1.11#4", "amb_ocean_waves_soft.wav", -34],
        ["2.02#1", "2.10#7", "clock_tick.wav", -35],
        ["3.02#1", "3.08#4", "amb_ceiling_fan.wav", -35],
        ["4.02#1", "4.12#4", "clock_tick.wav", -35],
        ["5.02#1", "5.05#24", "amb_ocean_waves_soft.wav", -34]
    ],
    "cues": [
        ["1.03", "start", 0.0, "t14/fx_baby_crying_night.wav", -14],
        ["1.03", "start", 1.5, "t14/fx_sewing_machine.wav", -12],
        ["1.05", "start", 0.0, "fx_glasses_clink.wav", -14],
        ["1.05", "start", 1.0, "amb_party_crowd_outdoor.wav", -18],
        ["1.08", "start", 0.0, "clock_tick.wav", -14],
        ["1.08", "start", 1.0, "fx_phone_ring_landline_night.wav", -12],
        ["2.03", "start", 0.0, "fx_car_tire_screech_stop.wav", -12],
        ["2.03", "start", 1.0, "t14/fx_vehicle_impact_metal.wav", -10],
        ["2.03", "start", 1.5, "fx_glass_smash_vehicle_crash.wav", -10],
        ["2.05", "start", 0.0, "gavel.wav", -10],
        ["2.05", "start", 1.2, "paper_rustle.wav", -14],
        ["2.07", "start", 0.0, "fx_envelope_tear.wav", -12],
        ["2.07", "start", 1.2, "coin_clink.wav", -14],
        ["4.03", "start", 0.0, "door_creak.wav", -12],
        ["4.03", "start", 1.2, "t14/fx_footsteps_barefoot_stairs.wav", -12],
        ["4.05", "start", 0.0, "t14/fx_gunshots_revolver_5.wav", -8],
        ["4.05", "start", 2.5, "t14/fx_phone_hangup_click.wav", -10],
        ["4.07", "start", 0.0, "fx_car_door_close.wav", -12],
        ["4.07", "start", 1.0, "police_siren_distant.wav", -14],
        ["5.05#24", "end", -0.5, "folder_close.wav", -8]
    ],
    "music_drop": {
        "_doc": "Tắt nhạc có giai điệu (giữ nền môi trường) ở các câu hé lộ — Rule A1/V4. [từ câu, đến câu]",
        "ranges": [
            ["1.06#1", "1.06#7"],
            ["2.08#1", "2.08#7"],
            ["4.06#1", "4.06#6"]
        ]
    }
}

for name in ["sfx_tap14.json", "sfx_tap14_EN.json", "sfx_tap14_JA.json"]:
    p = ROOT / name
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Created {p} successfully!")
