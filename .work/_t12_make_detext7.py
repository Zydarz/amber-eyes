# -*- coding: utf-8 -*-
"""Tập 12 — vá prompt 7 nền có chữ/số/logo AI (soi mắt 16/11/2026).

Áp dụng đúng 3 việc của A11 #171:
  1. GỠ mọi thông tin chữ khỏi prompt (tên riêng, 'labeled/inscribed/dial/label/number…')
  2. Mô tả bề mặt TRƯNG + BỎ HẲN vật thể có sẵn "chỗ chữ"
     (ô nhãn hộp · khung thông báo · mặt radio có số · biển số · logo lưới xe · bàn phím số)
  3. Thêm "completely blank and unmarked with no writing at all"

Ghi:
  .work/bg_jobs_tap12_detext7.json   (7 job cho Kaggle)
  .work/bg_jobs_tap12_v2.json         (cập nhật prompt của 7 job đó)
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
JOBS_V2 = ROOT / ".work/bg_jobs_tap12_v2.json"
OUT = ROOT / ".work/bg_jobs_tap12_detext7.json"

# name -> (desc_vi mới, prompt_en mới, lý do vi phạm)
PATCH = {
    "t12_archive_boxes_metal_shelf": (
        "Chồng hộp lưu trữ xám trên kệ thép trong phòng lưu trữ mờ, mặt hộp trơn trọn không ô nhãn, một hộp bị kéo lệch ra nửa chừng, bụi và ánh đèn lạnh.",
        "Stacks of plain grey archive boxes with completely blank unmarked surfaces and no label holders, no stickers and no slots anywhere, on metal shelving in a dim archive room, one box pulled half out, a cold fluorescent tube, dust, the weight of a hidden record, no labels, no writing, no text of any kind, no people",
        "ô nhãn mặt hộp có chữ AI",
    ),
    "t12_official_vehicle_closed_road": (
        "Xe sedan boxy không nhãn hiệu đậu trên đường đất đỏ vắng lặng trong rừng, lưới xe trơn không hãng, cổng bê tông trắng trơn không biển.",
        "A plain anonymous boxy sedan seen from behind on a red dirt road cutting through dense jungle, completely blank grille with no badge or emblem anywhere, no licence plate at all, plain unmarked concrete gate pillars with no signs or plaques, cold flat overcast light, mist swallowing the distance, closed metal gate behind, no people, no faces, no logos, no text of any kind",
        "logo lưới xe + biển số + bảng trên cổng",
    ),
    "t12_old_radio_receiver_dark": (
        "Một tủ radio cũ đóng kín đặt trên bàn gỗ trong hành lang tối, mặt trước phẳng trơn không đồng hồ không số, hành lang trống trải không treo gì.",
        "An old valve radio cabinet with a completely plain closed front panel with no dials, no numbers, no markings and no lettering at all, standing on a rough wooden table in a dark corridor, bare corridor walls with nothing hanging on them, a bare bulb far down the hall, dust, oppressive stillness, no people, no hands, no writing, no text of any kind",
        "mặt radio có số + khung tranh trên tường có chữ",
    ),
    "t12_reel_to_reel_archive_recorder": (
        "Máy ghi âm cuộn cuộn trên kệ thép trong phòng lưu trữ tối, mặt máy trơn không nhãn, một cuộn băng đang dở dang, bức tường trống trải.",
        "A reel-to-reel tape recorder with a completely plain front panel with no labels or markings of any kind, on a steel shelf in a dark archive room with bare walls and nothing hanging on them, one tape half spooled, a single cold lamp, dust, the record of a crime, no people, no hands, no labels, no writing, no text of any kind",
        "nhãn nhỏ trên mặt máy ghi âm",
    ),
    "t12_sinking_bundles_muddy_road": (
        "Những bó vải bọc đồ đạc chìm dần trong bùn xám ven con đường rừng, dây thừng quấn quanh, trời xám xịt.",
        "Tied cloth bundles and burlap sacks sinking slowly into grey mud at the edge of a jungle road, a coil of rope among them, no boxes, no papers, no parcels, flat overcast light, no people, no faces, no labels, no writing, no text of any kind",
        "nhãn trên thùng + tờ giấy có chữ",
    ),
    "t12_state_department_empty_corridor": (
        "Hành lang bộ Ngoại giao trống với cửa sổ cao và những cánh cửa gỗ khép kín, tường trơn trọn không treo khung không biển, một bàn gác thị sự bỏ trống.",
        "An empty government department corridor with tall windows and closed wooden doors, completely bare walls with no framed notices, no signs, no plaques and nothing hanging on them, a bare reception desk, cold institutional daylight, no people, no lettering, no text of any kind",
        "khung thông báo trên tường có chữ",
    ),
    "t12_urgent_appeal_dark_office": (
        "Bàn làm việc trong văn phòng Quốc hội lúc đêm, điện thoại bàn đen với bàn phím trơn không số, chồng hồ sơ trống dưới ánh sáng lạnh.",
        "A dark congressional office at night, a plain black desk telephone with a completely blank keypad with no digits or numbers at all, stacks of closed blank folders and a single completely blank unmarked sheet of paper on the desk, a tall cold window behind, one pool of pale light, heavy shadow, no people, no writing, no labels, no text of any kind",
        "bàn phím điện thoại có số",
    ),
}

SEED_BASE = 33000

jobs = json.loads(JOBS_V2.read_text(encoding="utf-8"))
by = {j["name"]: j for j in jobs}
out = []
for i, (name, (desc, prompt, why)) in enumerate(PATCH.items(), start=1):
    if name not in by:
        raise SystemExit(f"khong tim thay job {name}")
    by[name]["desc"] = desc
    by[name]["prompt"] = prompt
    j = dict(by[name])
    j["seed"] = SEED_BASE + i
    j["why"] = why
    out.append(j)

JOBS_V2.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"da va prompt {len(out)} nen co chu AI:")
for j in out:
    print(f"  {j['name']:38s} seed {j['seed']}  ({j['why']})")
print(f"-> {OUT.name}")
