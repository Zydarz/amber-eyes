# -*- coding: utf-8 -*-
"""Tập 11 — bản vá bỏ CHỮ cho 10 nền cũ có prompt yêu cầu chữ (H2/H5).

Nguyên tắc (bài học Tập 10, 12/11/2026): chỉ thêm "no text" vào NEGATIVE là KHÔNG đủ.
Phải GỠ MỌI thông tin chữ khỏi prompt, chỉ mô tả bề mặt TRƯNG + thêm
"completely blank and unmarked with no writing at all".

Dùng khi soi mắt xác nhận nền có chữ AI → sinh lại ĐÚNG TÊN (ghi đè file cũ).
"""
import json
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
JOBS = ROOT / ".work/bg_jobs_tap11_v3.json"
OUT = ROOT / ".work/bg_jobs_tap11_detext.json"

DETEXT = {
    "t11_deal_with_the_devil_contract":
        "Formal legal document still life: a closed official document folder lying open on a dark desk with completely blank unmarked pages, a fountain pen resting across the empty page, dark ominous crimson and charcoal noir palette, sinister bargain mood.",
    "t11_galligan_inquiry_report_reforms":
        "Dignified study still life: a closed leather-bound judicial inquiry volume with a completely blank unmarked cover and no title of any kind, brass judicial scales beside it, a pale beacon of legal reform rising from profound tragedy.",
    "t11_christmas_1990_halothane_bottle":
        "Chilling forensic still life of Christmas Eve 1990: a vintage amber medical bottle with a plain blank stopper and no label whatsoever, standing beside an ornate crystal wine goblet on a festive mahogany sideboard, heavy chiaroscuro ink.",
    "t11_calendar_counting_to_freedom":
        "Prison cell wall still life: a blank wall calendar grid whose squares are completely empty with no numbers and no writing at all, shaft of barred sunlight illuminating the countdown to early freedom, profound moral contrast.",
    "t11_prosecution_clock_pressure":
        "Tense visual metaphor: vintage brass hourglass with sands running out rapidly against a wall of folded newspapers whose surfaces are completely blank and unmarked with no writing at all, ticking pressure driving flawed prosecutorial compromise.",
    "t11_amber_eyes_redflag_intro":
        "Minimalist graphic noir emblem card: an iconic golden owl eye shape glowing through atmospheric charcoal mist, brass compass and warning beacons lighting up the dark, completely blank background with no title and no lettering.",
    "t11_amber_eyes_closing_dossier_bernardo":
        "Close-up still life of a dark leather investigative dossier closing solemnly on an antique oak desk, a plain embossed golden eye shape with no letters and no logo lettering, dignified closing frame, graphic novel noir perfection.",
    "t11_constitutional_legal_deadlock":
        "Legal still life: a heavy leatherbound law volume whose cover is completely blank and unmarked with no writing of any kind, heavy padlock clamped across its binding, scales of justice trapped in an unbreakable legal gridlock, solemn institutional tragedy.",
    "t11_dangerous_offender_life_sentence":
        "Judicial verdict still life: a blank sheet of aged parchment lying on a dark desk with a bold red rubber stamp resting on top of it, the stamp face completely blank with no lettering, an iron prison key beside it, heavy prison bars in the background.",
    "t11_redflag1_evading_accountability":
        "Conceptual graphic noir art for Red Flag 1: a cracked porcelain shield with a completely blank unmarked surface and no inscription of any kind, deflecting arrows of legitimate inquiry, evading accountability behind manufactured suffering.",
}

jobs = json.loads(JOBS.read_text(encoding="utf-8"))
out = []
for j in jobs:
    if j["name"] in DETEXT:
        j = dict(j)
        j["prompt"] = DETEXT[j["name"]]
        j["_de_text"] = True
    out.append(j)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"đã ghi {OUT.name}: {len(DETEXT)} prompt đã bỏ chữ (trong tổng {len(out)} job)")
for n in DETEXT:
    print("  -", n)
