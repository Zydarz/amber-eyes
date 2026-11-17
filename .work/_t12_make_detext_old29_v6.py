# -*- coding: utf-8 -*-
"""Tập 12 — VÒNG 6: 7 nền cũ còn dính chữ ⇒ ĐỔI BỐ CỤC triệt để (14 ảnh).

Kết quả QC 2 lô (58 ảnh): 19/29 nền đã có biến thể sạch; 10 nền còn lại.
Bảng lỗi còn lại và cách vá:
  concerned_relatives_alliance : ảnh gia đình có CAPTION dưới mỗi ảnh ⇒ cho ảnh úp sấp (chỉ thấy mặt sau trắng)
  fbi_evidence_tape_q042      : thước đo có SỐ + nhãn băng ⇒ bỏ thước, băng không nhãn
  milgram_experiment_...      : bảng điều khiển có NHÃN trên núm ⇒ chỉ thấy mặt sau của máy
  moral_compass_unbroken      : mặt la bàn có CHỮ BẮC (N) ⇒ dùng vỏ la bàn đóng
  impenetrable_geographical_.. : bản đồ có TÊN ĐỊA DANH ⇒ bỏ bản đồ, dùng rừng từ trên cao
  press_corps_cameras_...     : ống kính có VẠCH SỐ ⇒ bỏ máy ảnh, chỉ cuộn phim + micro
  property_surrender_passbooks : mặt sổ có DÒNG CHỮ ⇒ bỏ sổ, chỉ ví da + chìa khóa

Ghi: .work/bg_jobs_tap12_old29_v6.json + cập nhật bg_jobs_tap12_v2.json
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
JOBS_V2 = ROOT / ".work/bg_jobs_tap12_v2.json"
OUT = ROOT / ".work/bg_jobs_tap12_old29_v6.json"

PATCH = {
    "t12_concerned_relatives_alliance": (
        "Bàn làm việc tối: ảnh gia đình đen trắng úp sấp chồng lên nhau, chỉ thấy mặt sau trắng trơn, đèn bàn kim loại.",
        "A dark desk lit by a single bare metal lamp, a stack of black-and-white family photographs lying face down so only their plain blank white backs are visible, a plain unmarked corkboard behind, somber documentary noir, no writing, no text of any kind",
    ),
    "t12_fbi_evidence_tape_q042": (
        "Cuộn băng cassette trong túi niêm phong kỹ thuật, mặt túi và mặt băng đều trơn, nằm trên bàn thép.",
        "Forensic still life of a 1970s compact cassette tape inside a sealed clear evidence plastic bag whose surface is completely blank and unmarked, the cassette itself plain with no label and no writing, resting on a stainless steel examination table, stark clinical noir, no writing, no text of any kind",
    ),
    "t12_milgram_experiment_shock_generator": (
        "Mặt sau của một máy thí nghiệm kim loại thập niên 1960 trong phòng lab tối, tấm lưới thông gió, ánh sáng xiên gay.",
        "Forensic close-up of the plain metal back panel of a 1960s laboratory machine, rows of dull ventilation grilles and switches seen from behind, harsh raking laboratory light, a shadowy psychological laboratory, no writing, no text of any kind",
    ),
    "t12_moral_compass_unbroken": (
        "Vỏ la bàn đồng cũ đóng kín trên đá tải tối, mặt nắp trơn hoàn toàn, ánh hổ phách ấm.",
        "A closed antique brass compass case lying on a dark slate surface, its plain lid completely smooth and unmarked, a warm amber luminescence radiating outward pushing back creeping pitch-black shadows, unbroken personal conscience, no writing, no text of any kind",
    ),
    "t12_impenetrable_geographical_isolation": (
        "Nhìn từ trên cao xuống vòm rừng nhiệt đới dày đặc bất tận, chỉ một đường bùn nhỏ dẫn vào khoảng trống, sương nặng.",
        "A high aerial view of endless dense tropical rainforest canopy, a single thin muddy track cutting to one tiny clearing, heavy mist swallowing the horizon, total geographic isolation, no writing, no text of any kind",
    ),
    "t12_press_corps_cameras_microphones": (
        "Dụng cụ phóng sự: cuộn phim 35mm nằm ngửa, micro định hướng kim loại, vali đen đóng kín, tường đá trơn.",
        "Journalistic field equipment still life, a coiled 35mm film reel lying flat on a worn wooden table, a plain metal directional microphone, a closed black hard case with a completely plain unmarked lid, a dark bare stone wall, cold flat light, no writing, no text of any kind",
    ),
    "t12_property_surrender_passbooks": (
        "Bàn gỗ sẫm trong văn phòng tối: ví da đóng, chùm chìa khóa đồng, khay gỗ rỗng, ánh đèn bàn xiên gay.",
        "Forensic still life on a dark mahogany desk, a plain closed leather wallet, a small bunch of brass keys, an empty wooden tray, harsh raking desk lamp light, systemic financial dispossession aesthetic, no writing, no text of any kind",
    ),
}

SEED_A, SEED_B = 36400, 36500

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
print(f"vong 6: {len(PATCH)} nen x 2 bien the = {len(out)} anh")
for j in out:
    print(f"  {j['name']:52s} seed {j['seed']}")
print(f"-> {OUT.name}")
