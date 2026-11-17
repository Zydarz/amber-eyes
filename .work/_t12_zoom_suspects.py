# -*- coding: utf-8 -*-
"""Tập 12 — cắt 4 góc phóng to (native px) cho các nền nghi có chữ AI."""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t12" / "zoom"
OUT.mkdir(parents=True, exist_ok=True)

SUSPECTS = [
    "archive_boxes_metal_shelf",
    "closed_circle_of_stools",
    "empty_trunk_open_padlock",
    "official_vehicle_closed_road",
    "old_radio_receiver_dark",
    "ordinary_lives_work_gloves",
    "reel_to_reel_archive_recorder",
    "sinking_bundles_muddy_road",
    "state_department_empty_corridor",
    "survivor_empty_chair_doorway",
    "testimony_room_single_chair",
    "urgent_appeal_dark_office",
    "memorial_stone_candles_dawn",
    "call_to_action_muted_desk",
]

for name in SUSPECTS:
    f = BG / f"t12_{name}.png"
    if not f.exists():
        print("THIEU", name)
        continue
    im = Image.open(f)
    w, h = im.size
    # 4 góc: trái-trên, phải-trên, trái-dưới, phải-dưới (chồng lấn 25%)
    quads = {
        "q1": (0, 0, int(w * 0.6), int(h * 0.6)),
        "q2": (int(w * 0.4), 0, w, int(h * 0.6)),
        "q3": (0, int(h * 0.4), int(w * 0.6), h),
        "q4": (int(w * 0.4), int(h * 0.4), w, h),
    }
    for tag, box in quads.items():
        im.crop(box).save(OUT / f"{name}__{tag}.png")
    print(f"ok {name}")

print(f"\n-> {OUT}  ({len(SUSPECTS) * 4} file)")
