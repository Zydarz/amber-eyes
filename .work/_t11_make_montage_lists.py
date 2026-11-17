# -*- coding: utf-8 -*-
"""Tạo danh sách nhãn cho qc_montage (bỏ tiền tố t11_) — 70 nền mới / 66 nền cũ / nhóm rủi ro chữ."""
import json
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
OUT = ROOT / ".work/_t11"
OUT.mkdir(parents=True, exist_ok=True)

v3 = json.loads((ROOT / ".work/bg_jobs_tap11_v3.json").read_text(encoding="utf-8"))
v2 = {j["name"] for j in json.loads((ROOT / ".work/bg_jobs_tap11_v2.json").read_text(encoding="utf-8"))}
new = [j["name"].replace("t11_", "") for j in v3 if j["name"] not in v2]
old = [j["name"].replace("t11_", "") for j in v3 if j["name"] in v2]

# nhóm rủi ro chữ / giấy bìa → soi ô lớn (>=900 px) theo luật H20
risky = ["deal_with_the_devil_contract", "galligan_inquiry_report_reforms",
         "christmas_1990_halothane_bottle", "calendar_counting_to_freedom",
         "prosecution_clock_pressure", "amber_eyes_redflag_intro",
         "amber_eyes_closing_dossier_bernardo", "constitutional_legal_deadlock",
         "dangerous_offender_life_sentence", "redflag1_evading_accountability",
         "closed_dossier_desk", "two_dossier_folders_desk", "evidence_bags_lab_bench",
         "newspapers_fury", "sealed_document_folder", "moral_licence_blank_notes",
         "untitled_letter_desk", "calendar_pages_tearing", "cold_calculation_desk",
         "investigation_board_four_stages", "closing_dossier_stamp", "closing_card_dossier",
         "contract_table_shadow", "empty_evidence_box", "blank_photographs_in_hands",
         "six_tapes_on_floor", "videotape_reels_stack", "spinning_tape_reels",
         "handheld_camera_lens", "haunted_new_identity_shadow"]

for fn, data in [("montage_new70.json", new),
                 ("montage_old66.json", old),
                 ("montage_risky_text.json", sorted(set(risky)))]:
    (OUT / fn).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{fn}: {len(data)} mã")
print("\nlệnh montage sau khi ảnh về:")
print("  py -3 .work/qc_montage.py --ep 11 --kind bg --list .work/_t11/montage_new70.json --cell 512 --cols 7 --out .work/qc_montage/ep11_bg_new70.jpg")
print("  py -3 .work/qc_montage.py --ep 11 --kind bg --list .work/_t11/montage_old66.json --cell 512 --cols 8 --out .work/qc_montage/ep11_bg_old66.jpg")
print("  py -3 .work/qc_montage.py --ep 11 --kind bg --list .work/_t11/montage_risky_text.json --cell 900 --cols 4 --out .work/qc_montage/ep11_bg_risky_text.jpg")
