#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soi cuối: 12 nền có VẬT THỂ NHỎ (nơi chữ cỡ nhỏ dễ lọt) — ô 700 px, 2 cột.

Toán: ô hiệu dụng = cell * 1568 / (cols*(cell+4)). cols=2, cell=700 ⇒ 700 px.
2 tờ × 6 ô = 12 ảnh.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / ".work" / "_t11" / "sheets"

SMALL_PROPS = [
    "six_8mm_tapes_bag", "six_tapes_on_floor", "closing_dossier_stamp",
    "handheld_camera_lens", "control_room_dark_monitors", "narcissistic_mirror_vanity",
    "evidence_bags_lab_bench", "calendar_counting_to_freedom",
    "christmas_1990_halothane_bottle", "constitutional_legal_deadlock",
    "galligan_inquiry_report_reforms", "dangerous_offender_life_sentence",
]
BG = ROOT / "assets" / "bg"
names = [n for n in SMALL_PROPS if (BG / f"t11_{n}.png").exists()]
print(f"{len(names)} nen co vat the nho")
for i in range(0, len(names), 6):
    chunk = names[i:i + 6]
    tag = f"fin{i // 6 + 1:02d}"
    f = OUT / f"list_{tag}.json"
    f.write_text(json.dumps({"must": chunk}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  {tag}: {chunk}")
