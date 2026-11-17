# -*- coding: utf-8 -*-
import cv2
import os
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
out_dir = ROOT / ".work/qc_crops_t18"
out_dir.mkdir(parents=True, exist_ok=True)

targets = [
    # (ten file, crop_box: x0, y0, x1, y1)
    ("t18_b1_evasive_phone_screen_gloom", 600, 300, 1500, 900),
    ("t18_b1_abandoned_plea_dusty_desk", 700, 400, 1600, 1000),
    ("t18_b1_court_summons_envelope_shadow", 600, 300, 1500, 900),
    ("t18_b1_investigative_vehicle_gravel_driveway", 500, 300, 1600, 900),
    ("t18_b2_silent_press_briefing_hall", 600, 300, 1500, 900),
    ("t18_b2_bank_vault_safety_box_ajar", 600, 300, 1500, 900),
    ("t18_b2_forensic_evidence_boxes_stacked", 600, 300, 1500, 900),
    ("t18_b3_unmarked_ledger_closed_vault", 600, 300, 1500, 900),
    ("t18_b4_court_reporter_transcription_chair", 600, 300, 1500, 900),
    ("t18_b4_prison_transport_van_iron_grate", 500, 300, 1600, 900),
    ("t18_b4_deliberation_whiteboard_blank_notes", 600, 300, 1500, 900),
    ("t18_b4_cassette_tape_spool_macro_gloom", 600, 300, 1500, 900),
    ("t18_b4_justice_scales_brass_counterbalance", 600, 300, 1500, 900),
    ("t18_b4_solitary_hourglass_sand_running_out", 600, 300, 1500, 900),
    ("t18_b5_hollowed_book_empty_cavity", 600, 300, 1500, 900),
    ("t18_b5_cracked_sundial_overcast_sky", 600, 300, 1500, 900),
]

for name, x0, y0, x1, y1 in targets:
    fpath = ROOT / "assets/bg" / (name + ".png")
    if not fpath.exists():
        continue
    img = cv2.imread(str(fpath))
    crop = img[y0:y1, x0:x1]
    out_p = out_dir / f"crop_{name}.png"
    cv2.imwrite(str(out_p), crop)
    print(f"Da crop: {out_p}")
