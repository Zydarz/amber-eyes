# -*- coding: utf-8 -*-
"""Tập 12 — VÒNG 3: vá 1 nền còn dính chữ AI (reel_to_reel_archive_recorder).

Vòng 2 đã vá prompt nhưng AI VẪN vẽ chữ ở mặt máy (zoom6x rõ: hàng ký tự nhỏ bên
trái + dãy số bên phải). Nguyên nhân theo A11 #179: VẬT THỂ CÓ SẴN CHỖ CHỮ
(mặt phẳng điều khiển của máy ghi âm) ⇒ phải ĐỔI CẢ BỐ CỤC, không chỉ đổi bề mặt.

Cách sửa vòng 3: XOAY LƯNG máy lại ⇒ khung hình chỉ có VỎ THÉP trơn + 2 cuộn băng
trên đỉnh; KHÔNG còn mặt phẳng nào để AI đặt bảng tên. Đồng thời KHÔNG nhắc tới
dial/knob/nameplate trong prompt (A11 #171: gỡ mọi gợi ý vật thể mang chữ).

Sinh 2 BIẾN THỂ (2 kernel = 2 phiên Kaggle độc lập = 2 GPU chạy song song):
  A  seed 34001 — máy xoay 3/4, thấy vỏ bên + 2 cuộn băng
  B  seed 34002 — máy nằm nghiêng, cuộn băng hướng lên, chỉ thấy góc thép trơn
→ soi, chọn 1, đổi tên về t12_reel_to_reel_archive_recorder.

Ghi:
  .work/bg_jobs_tap12_detext3.json   (2 bien the cho Kaggle)
  .work/bg_jobs_tap12_v2.json         (cap nhat prompt chinh)
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
JOBS_V2 = ROOT / ".work/bg_jobs_tap12_v2.json"
OUT = ROOT / ".work/bg_jobs_tap12_detext3.json"

NAME = "t12_reel_to_reel_archive_recorder"

DESC = ("Máy ghi âm cuộn cuộn xoay lưng lại, chỉ thấy hai cuộn băng trên đỉnh và "
        "vỏ thép trơn trọn, đặt trên kệ thép trong phòng lưu trữ tối, tường trống trải.")

PROMPT_A = (
    "A vintage reel-to-reel tape recorder turned away from the camera so that only the "
    "two empty tape reels on top and the smooth plain steel side of its casing are "
    "visible, plain brushed metal with nothing on it, standing on a steel shelf in a "
    "dark archive room with bare empty walls, one tape half spooled, a single cold lamp "
    "from the side, dust in the air, no people, no hands, completely blank and unmarked "
    "with no writing at all, no text of any kind"
)
PROMPT_B = (
    "A vintage reel-to-reel tape recorder lying on its side on a steel shelf in a dark "
    "archive room, the two tape reels facing upward and the metal casing turned away so "
    "that only smooth featureless steel is visible, bare empty walls, a single cold lamp "
    "from the side, dust in the air, no people, no hands, completely blank and unmarked "
    "with no writing at all, no text of any kind"
)

VARIANTS = [
    ("t12_reel_to_reel_archive_recorder_a", 34001, PROMPT_A, "may xoay 3/4"),
    ("t12_reel_to_reel_archive_recorder_b", 34002, PROMPT_B, "may nam nghieng"),
]

jobs = json.loads(JOBS_V2.read_text(encoding="utf-8"))
hit = 0
for j in jobs:
    if j["name"] == NAME:
        j["desc"] = DESC
        j["prompt"] = PROMPT_A
        j["seed"] = 34001
        hit += 1
if hit != 1:
    raise SystemExit(f"khong tim thay dung 1 job {NAME} (tim thay {hit})")
JOBS_V2.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")

base = next(j for j in jobs if j["name"] == NAME)
out = []
for vname, seed, prompt, why in VARIANTS:
    j = dict(base)
    j["name"] = vname
    j["prompt"] = prompt
    j["seed"] = seed
    j["why"] = why
    out.append(j)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"vong 3: 1 nen, {len(out)} bien the")
for j in out:
    print(f"  {j['name']:44s} seed {j['seed']}  ({j['why']})")
print(f"-> {OUT.name}")
