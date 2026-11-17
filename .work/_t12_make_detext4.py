# -*- coding: utf-8 -*-
"""Tập 12 — vá 3 nền còn vấn đề sau vòng 2 (vòng 4), mỗi nền 2 biến thể.

Nguyên tắc vá (A11 #171 + #175 + #179): KHÔNG nêu tên vật thể mang chữ (không
"badge", "emblem", "nameplate", "label", "frame", "keypad digits"…) vì chính từ
đó gợi AI vẽ ra; thay bằng mô tả bề mặt TRƯNG + đổi BỐ CỤC cho vật thể đó
không còn xuất hiện trong khung hình.

  t12_state_department_empty_corridor : tường còn 1 khung tranh nhỏ (~15x40 px) có vết như chữ
  t12_urgent_appeal_dark_office       : núm bàn phím điện thoại còn vết trắng giống số
  t12_official_vehicle_closed_road    : nắp xe còn một badge nhỏ (~12x12 px)

Ghi:
  .work/bg_jobs_tap12_detext4.json   (6 bien the cho Kaggle)
  .work/bg_jobs_tap12_v2.json         (cap nhat prompt chinh — bien the A)
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
JOBS_V2 = ROOT / ".work/bg_jobs_tap12_v2.json"
OUT = ROOT / ".work/bg_jobs_tap12_detext4.json"

PATCH = {
    "t12_state_department_empty_corridor": (
        "Hành lang bộ Ngoại giao trống nhìn thẳng dọc hành lang, chỉ có cửa gỗ khép kín, cửa sổ cao và trần giáo dục, tường bê tông trơn trọn không treo gì, bàn gác thị sự bỏ trống ở cuối hành lang.",
        "An empty government department corridor seen from a low angle looking straight down the hall, only closed wooden doors, tall windows and a plain suspended ceiling in frame, walls of bare painted concrete that are smooth, unbroken and completely bare, a bare reception desk far down the hall, cold institutional daylight, no people, completely blank and unmarked with no writing at all, no text of any kind",
        "khung tranh nhỏ trên tường trái có vết như chữ",
    ),
    "t12_urgent_appeal_dark_office": (
        "Bàn làm việc trong văn phòng Quốc hội lúc đêm, điện thoại bàn đen úp sấp trên bàn, chồng hồ sơ trống và một tờ giấy trắng trơn dưới ánh sáng lạnh.",
        "A dark congressional office at night, a plain black desk telephone lying face down on the desk so that only its smooth blank back and the handset are visible, stacks of closed blank folders and a single completely blank unmarked sheet of paper on the desk, a tall cold window behind, one pool of pale light, heavy shadow, no people, completely blank and unmarked with no writing at all, no text of any kind",
        "núm bàn phím còn vết trắng giống số",
    ),
    "t12_official_vehicle_closed_road": (
        "Xe sedan boxy không nhãn hiệu đậu ở tư thế nghiêng bên trên đường đất đỏ vắng lặng trong rừng, thân xe trơn tru, cổng bê tông trắng trơn không biển.",
        "A plain anonymous boxy sedan standing in side profile on a red dirt road cutting through dense jungle, smooth unbroken painted bodywork, plain concrete gate pillars with nothing on them, a closed metal gate behind, cold flat overcast light, mist swallowing the distance, no people, no faces, no writing, no text of any kind",
        "badge nhỏ trên nắp xe",
    ),
}

# bien the B: doi bo cuc them mot lan nua
VARIANT_B = {
    "t12_state_department_empty_corridor": (
        "Hành lang dài bê tông trơn và kính, máy quay nhìn vào đoạn hành lang trống, tường mịn liên tục không vật gì, chỉ cửa đóng và cửa sổ trọn cao, sàn bóng loáng.",
        "A long empty corridor of bare concrete and glass, the camera looking at an open stretch of hallway where the walls are smooth, continuous and completely bare, only closed doors and floor-to-ceiling windows, a polished floor with soft reflections, cold white daylight, no people, completely blank and unmarked with no writing at all, no text of any kind",
    ),
    "t12_urgent_appeal_dark_office": (
        "Bàn làm việc trống trong văn phòng lúc đêm bên cạnh cửa sổ cao lạnh, chồng hồ sơ đóng và một tờ giấy trắng trơn, điện thoại đen nằm nghiêng trên bàn.",
        "A dark empty office desk at night beside a tall cold window, closed blank folders and a single completely blank unmarked sheet of paper on the desk, a plain black telephone lying on its side on the desk, heavy shadow, one pool of pale light, no people, no writing, no text of any kind",
    ),
    "t12_official_vehicle_closed_road": (
        "Một chiếc xe boxy ẩn danh đậu xa trên đường đất đỏ trong rừng, nhìn từ phía sau, nhỏ trong khung hình, thân xe trơn và đèn hậu tròn đơn giản, cổng bê tông trơn ở tiền cảnh.",
        "A plain anonymous boxy car parked far in the distance on a red dirt road in dense jungle, seen from behind, small in the frame, smooth plain bodywork and simple round tail lights, bare concrete gate pillars in the foreground with nothing on them, cold flat overcast light, heavy mist, no people, no writing, no text of any kind",
    ),
}

SEEDS = {
    "t12_state_department_empty_corridor": (35001, 35002),
    "t12_urgent_appeal_dark_office": (35003, 35004),
    "t12_official_vehicle_closed_road": (35005, 35006),
}

jobs = json.loads(JOBS_V2.read_text(encoding="utf-8"))
by = {j["name"]: j for j in jobs}
out = []
for name, (desc, prompt, why) in PATCH.items():
    if name not in by:
        raise SystemExit(f"khong tim thay job {name}")
    by[name]["desc"] = desc
    by[name]["prompt"] = prompt
    by[name]["seed"] = SEEDS[name][0]
    desc_b, prompt_b = VARIANT_B[name]
    for tag, sd, p, d in (("a", SEEDS[name][0], prompt, desc),
                          ("b", SEEDS[name][1], prompt_b, desc_b)):
        j = dict(by[name])
        j["name"] = f"{name}_{tag}"
        j["prompt"] = p
        j["desc"] = d
        j["seed"] = sd
        j["why"] = why
        out.append(j)

JOBS_V2.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"vong 4: {len(PATCH)} nen x 2 bien the = {len(out)} anh")
for j in out:
    print(f"  {j['name']:52s} seed {j['seed']}")
print(f"-> {OUT.name}")
