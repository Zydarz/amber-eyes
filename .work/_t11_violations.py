#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Danh sách nền Tập 11 có chữ AI — kết quả soi mắt 100 % (9 tờ montage + 13 ảnh gốc).

Mỗi dòng: tên file · nơi phát hiện · mức độ · mô tả chữ thấy được.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / ".work" / "_t11" / "violations_t11.json"

# (mã không tiền tố, mức, mô tả)
V = [
    # --- nhóm A: đã có trong bản vá detext sẵn (10) ---
    ("amber_eyes_redflag_intro", "A", "tiêu đề lớn trên thẻ intro, sai chính tả"),
    ("amber_eyes_closing_dossier_bernardo", "A", "chữ 'AMBER' + phụ đề vô nghĩa trên bìa hồ sơ"),
    ("calendar_counting_to_freedom", "A", "số và chữ vô nghĩa trên tờ lịch"),
    ("christmas_1990_halothane_bottle", "A", "nhãn chữ trên lọ thuốc"),
    ("constitutional_legal_deadlock", "A", "chữ trên bìa sách luật"),
    ("dangerous_offender_life_sentence", "A", "dòng chữ trên tờ bản án"),
    ("deal_with_the_devil_contract", "A", "nhiều dòng chữ trên hợp đồng"),
    ("galligan_inquiry_report_reforms", "A", "tiêu đề trên bìa sách báo cáo"),
    ("prosecution_clock_pressure", "A", "chữ báo chí vô nghĩa"),
    ("redflag1_evading_accountability", "A", "chữ khắc trên biển 'RED FLAG'"),
    # --- nhóm B: phát hiện mới khi soi 100 % (20) ---
    ("covert_sociopath_profile", "B", "chữ vô nghĩa trên sơ đồ não"),
    ("narcissistic_mirror_vanity", "B", "nhãn chữ vô nghĩa trên lọ nước hoa"),
    ("february_arrest_dna_match", "B", "chữ trên tờ báo cáo ADN"),
    ("half_truth_dossier_shadow", "B", "chữ viết tay trên sổ"),
    ("haunted_new_identity_shadow", "B", "chữ báo chí"),
    ("joliette_prison_gate_release", "B", "chữ trên cổng nhà tù"),
    ("ken_murray_obstruction_charge", "B", "chữ trên tờ cáo buộc"),
    ("map_proximity_dark_crossroads", "B", "nhãn chữ trên bản đồ"),
    ("missing_evidence_dilemma", "B", "chữ trên báo ảnh cắt"),
    ("outraged_citizens_protest", "B", "chữ trên biển rôn"),
    ("pleading_victim_tears", "B", "chữ viết tay trên thư"),
    ("six_8mm_tapes_bag", "B", "chữ trên nhãn băng + thông báo dán tường"),
    ("six_tapes_on_floor", "B", "chữ trên nhãn băng cassette"),
    ("st_catharines_hospital_night", "B", "chữ trên biển bệnh viện"),
    ("triumphant_smile_deal_with_devil", "B", "chữ trên màn hình TV"),
    ("scarborough_taskforce_archive", "B", "chữ trên bản đồ treo tường + nhãn bìa"),
    ("handheld_camera_lens", "B", "chữ khắc trên vòng ống kính"),
    ("evidence_bags_lab_bench", "B", "chữ trên túi bằng chứng + thông báo tường"),
    ("investigator_nausea_monitor", "B", "chữ trên áp phích tường"),
    ("unholy_sacrament_altar", "B", "chữ khắc trên vòm kiến trúc"),
    # --- nhóm C: mức nhẹ, chữ cực nhỏ / nổi ---
    ("closing_dossier_stamp", "C", "chữ nổi trên mặt con dấu"),
    ("control_room_dark_monitors", "C", "ký tự vô nghĩa cỡ nano trên bảng điều khiển"),
]

rows = [{"name": f"t11_{n}", "level": lv, "why": w} for n, lv, w in V]
OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

from collections import Counter
c = Counter(r["level"] for r in rows)
print(f"ghi {OUT.relative_to(ROOT)} · tong {len(rows)} nen co chu AI")
for k in sorted(c):
    print(f"  muc {k}: {c[k]}")

# doi chieu voi danh sach 136 nen tren dia
BG = {p.stem for p in (ROOT / "assets" / "bg").glob("t11_*.png")}
miss = [r["name"] for r in rows if r["name"] not in BG]
print("khong ton tai tren dia:", miss or "khong co")
