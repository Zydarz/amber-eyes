# -*- coding: utf-8 -*-
"""Tập 12 — ghép 4 góc phóng của MỖI nền nghi thành 1 tảng 2x2 để soi 1 lần/ảnh."""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t12" / "zoom2"
OUT.mkdir(parents=True, exist_ok=True)

SUSPECTS = [
    "archive_boxes_metal_shelf",
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
    q = {
        "q1": (0, 0, int(w * 0.6), int(h * 0.6)),
        "q2": (int(w * 0.4), 0, w, int(h * 0.6)),
        "q3": (0, int(h * 0.4), int(w * 0.6), h),
        "q4": (int(w * 0.4), int(h * 0.4), w, h),
    }
    sheet = Image.new("RGB", (w, h), (0, 0, 0))
    for tag, box in q.items():
        sheet.paste(im.crop(box), (0, 0) if tag == "q1" else
                    ((w // 2, 0) if tag == "q2" else
                     (0, h // 2) if tag == "q3" else (w // 2, h // 2)))
    sheet.save(OUT / f"{name}.jpg", quality=92)
    print("ok", name)
print("->", OUT)
