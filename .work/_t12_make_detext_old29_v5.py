# -*- coding: utf-8 -*-
"""Tập 12 — VÒNG 5: vá các nền CŨ còn dính chữ sau vòng vá đầu (29 nền x 2 biến thể).

Kết quả QC vòng vá đầu (58 ảnh):
  - phần lớn sạch (21/29 nền có ít nhất 1 biến thể sạch)
  - vẫn dính chữ: new_west (chữ trên giấy máy đánh chữ + ống phim)
                   redflag1 (AI tự vẽ badge "1" + chữ "ISOLATION")
                   redflag3 (đồng hồ có số + mảnh giấy có chữ)
                   press_corps (màn hình có chữ hãng + bảng điều khiển có số)

Nguyên tắc: BỎ HẲN vật thể mang chữ khỏi khung hình + không nhắc tên chúng.
Ghi: .work/bg_jobs_tap12_old29_v5.json (cho Kaggle) + cập nhật bg_jobs_tap12_v2.json
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
JOBS_V2 = ROOT / ".work/bg_jobs_tap12_v2.json"
OUT = ROOT / ".work/bg_jobs_tap12_old29_v5.json"

PATCH = {
    "t12_new_west_investigative_draft": (
        "Bàn điều tra nửa đêm: kính lúp đặt trên chồng giấy trắng trơn, cuộn phim 35mm, đèn bàn kim loại, bóng sâu.",
        "Journalistic investigative desktop at midnight, a magnifying glass resting on a stack of completely blank unmarked loose sheets, a strip of 35mm film negatives curling across the desk, a plain metal desk lamp, deep shadow, urgent investigative tension, moody slate and amber noir, no writing, no text of any kind",
    ),
    "t12_redflag1_total_social_isolation": (
        "Mạng nhện sắt khổng lồ giăng qua phố đổ nát, cắt ngang dây điện thoại, một điểm sáng đỏ rực giữa bóng tối xanh.",
        "Conceptual noir warning visual: a severe iron spiderweb grid stretching across a ruined street, severing telephone lines and wires, a single glowing crimson point of light cutting across cold slate darkness, total severance of human contact, no writing, no text of any kind",
    ),
    "t12_redflag3_escalating_commitment_trap": (
        "Bánh răng cương công nghiệp nghiền đĩa kim loại trơn và mảnh giấy gấp trắng vào cơ máy tối.",
        "Conceptual noir warning visual: interlocking heavy industrial gear teeth relentlessly dragging dull unmarked metal discs and folded blank paper slips down into dark churning machinery, no writing, no text of any kind",
    ),
    "t12_press_corps_cameras_microphones": (
        "Dụng cụ phóng sự trên bàn: máy quay 16mm thân trơn, máy ảnh rangefinder 35mm, micro kim loại, tường đá trơn.",
        "Journalistic field equipment still life, a heavy 16mm film camera with a completely plain unmarked body, a 35mm rangefinder camera with a telephoto lens, a plain metal directional microphone lying on the desk, a dark bare stone wall, ready for hostile environment fact-finding mission, no writing, no text of any kind",
    ),
}

SEED_A, SEED_B = 36200, 36300

jobs = json.loads(JOBS_V2.read_text(encoding="utf-8"))
by = {j["name"]: j for j in jobs}
missing = [n for n in PATCH if n not in by]
if missing:
    raise SystemExit(f"khong tim thay job: {missing}")
out = []
for i, (name, (desc, prompt)) in enumerate(PATCH.items()):
    by[name]["desc"] = desc
    by[name]["prompt"] = prompt
    for tag, seed in (("a", SEED_A + i), ("b", SEED_B + i)):
        j = dict(by[name])
        j["name"] = f"{name}_{tag}"
        j["prompt"] = prompt
        j["desc"] = desc
        j["seed"] = seed
        out.append(j)

JOBS_V2.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"vong 5: {len(PATCH)} nen x 2 bien the = {len(out)} anh (seed {SEED_A}+, {SEED_B}+)")
for j in out:
    print(f"  {j['name']:52s} seed {j['seed']}")
print(f"-> {OUT.name}")
