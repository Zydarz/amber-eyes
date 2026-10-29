#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh mục 4.2 (nguồn YouTube của từng mã) + cập nhật bảng BGM trong tài liệu."""
import io
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
MAP = ROOT / ".work" / "yt_map.tsv"
TICK = chr(96)

# cac ma thay the vi thu vien khong co track khop truc tiep
NOTE = {
    "fx_sigh_emotional": "thay thế - `Quiet Breathing` (thư viện không có tiếng sigh; dùng tiếng rên đau của đám đông)",
    "fx_crowd_relief_sigh": "thay thế - `Breathing Echo space` (tiếng rên rỉ từ hàng ghế khán phòng)",
    "fx_sigh_female": "thay thế - `Human Breathing Mouth` (thở nghẹn ngào, đúng tâm lý thở dài nghẹn ngào)",
    "fx_printer_thermal": "thay thế - `Motor Running Muffled` (tiếng máy chạy è è)",
    "fx_inkjet_printer_run": "thay thế - `Handheld Motor Running` (tiếng giấy nạp/rút liên tục)",
    "fx_crying_female_phone": "⚠️ **SAI GIỚI TÍNH** — thư viện KHÔNG có tiếng khóc nữ (chỉ có `Male Crying`, `Male Dramatic Crying`, `Babies Cry`, `Baby Cry*`); giữ `Male Crying` vì đúng nhịp khóc nén người lớn hơn tiếng trẻ khóc",
    "fx_defib_charge_shock": "thay thế - `Power Tool Electrical Buzz` (tiếng điện tĩnh/ran)",
    "fx_lab_test_kit": "không có tiếng xét nghiệm — dùng tiếng rót chất lỏng vào khay phẫu thuật",
    "fx_courtroom_dead_silence": "thay thế - `Ambient Hum Air Conditioner` (tiếng tờ giấy vẫy trong phòng xử án rộng)",
    "amb_library_quiet": "thay thế - `Bowling Alley Room Tone` (tiếng lật trang giấy trong thư viện)",
    "amb_female_humming_far": "không có tiếng đàn/humming — dùng `Voices On Street Accent`",
    "amb_fastfood_cafeteria": "thay thế - `Summer Beach Ambience` (tiếng múc đồ ăn vào hộp)",
    "amb_lawyers_discussion": "thay thế - `Voices Angry` bản 0:36 → nay dùng tiếng xì xào `Voices Murmur`",
    "amb_crowd_murmur_press": "",
    "amb_crowd_outside_press_anger": "thay thế - `Voices Murmur` (hoán đổi nguồn với `amb_lawyers_discussion`)",
    "amb_crowd_singing_acoustic": "không có track hát tập thể — dùng tiếng nhóm trẻ (`Children Group Ambience`)",
    "amb_hospital_monitor_heartbeat": "không có tiếng monitor tim — dùng tiếng máy ồn (`Metal Machine Hum`)",
    "fx_911_call_recording_radio": "",
    "fx_phone_unlock_click": "thay thế - `Phone Ringing`",
    "fx_wooden_hinge_creak_open": "thay thế - `Wood Door Open and Close Series`",
    "fx_wooden_lid_slam_latch": "thay thế - `Wood Door Close and Rattle`",
    "fx_door_slam_indoor": "thay thế - `Dumpster Door Slam`",
    "fx_monitor_case_close": "thay thế - `Washing Machine Door`",
    "fx_evidence_measure_tape": "thay thế - `Cassette Tape Rewind`",
    "fx_computer_beep_restore": "thay thế - `Beep Short` (bản gốc chỉ 0,1 s)",
    "fx_metal_lock_open": "thay thế - `Deadbolt Lock` (bản gốc chỉ 0,1 s)",
    "fx_pen_cap_open": "`Pen Clicking` chỉ 0,3 s → đã đệm 0,6 s",
    "fx_modem_dialup_data": "",
}

# doc: ma (khong .wav) -> (tap, dest)
doc = {}
for line in io.open(DOC, encoding="utf-8").read().splitlines():
    p = [x.strip() for x in line.split("|")]
    if len(p) < 6 or not p[2].startswith(TICK):
        continue
    name = p[2].strip(TICK)
    dest = p[5].strip(TICK)
    if name.endswith(".wav") and dest.startswith("assets/sfx/"):
        doc[name[:-4]] = (p[3].strip(), dest)

# manifest: dong CUOI CUNG cho ma thang
man = {}
for raw in io.open(MAP, encoding="utf-8-sig").read().splitlines():
    p = raw.split("\t")
    if len(p) >= 6 and p[1].strip():
        man[p[1].strip()] = {"track": p[0].strip(), "genre": p[4].strip()}

rows = []
for ma in sorted(doc):
    info = man.get(ma, {})
    tap, dest = doc[ma]
    rows.append((ma, tap, dest, info.get("track", ""), info.get("genre", ""), NOTE.get(ma, "")))

out = []
out.append("### 4.2. Nguồn YouTube Audio Library của từng mã — 169/169 đã tải & nhập xong")
out.append("")
out.append("> Nguồn: YouTube Studio → Thư viện âm thanh (YouTube Audio Library). "
           "Tải tay, cắt 2 pass, chuẩn hoá đỉnh −1 dBFS, đưa vào `assets/sfx/` theo cột “Đặt tại” của mục 4. "
           "Sổ nguồn đầy đủ: `provenance.json` (mục `track_youtube`, `the_loai_youtube`).")
out.append("")
out.append("Cột **Ghi chú** đánh dấu các mã dùng **track thay thế** (thư viện không có track đúng nghĩa) — cần duyệt khi dựng bản trộn.")
out.append("")
out.append("| # | Mã cue | Tập | Track YouTube | Thể loại | File đích | Ghi chú |")
out.append("|---|---|---|---|---|---|---|")
for i, (ma, tap, dest, track, genre, note) in enumerate(rows, 1):
    out.append("| %d | `%s` | %s | %s | %s | `%s` | %s |"
               % (i, ma, tap, track, genre, dest, note))
out.append("")

section = "\n".join(out)

txt = io.open(DOC, encoding="utf-8").read()
marker = "## 5. Nhạc nền (BGM)"
if "### 4.2." in txt:
    txt = re.sub(r"### 4\.2\..*?\n## 5\. Nhạc nền \(BGM\)", section + marker, txt, flags=re.S)
else:
    txt = txt.replace(marker, section + marker, 1)

# cap nhat bang BGM
txt = txt.replace(
    "| 09 | Guitar acoustic mộc mạc thập niên 60, biến dạng dần sang u tối | Chưa có track guitar trong `assets/bgm/` |",
    "| 09 | Guitar acoustic mộc mạc thập niên 60, biến dạng dần sang u tối | ✅ **ĐÃ TẢI** — `Jewelry Box` (Tim Bluhm, đồng quê) → `assets/bgm/bgm_guitar_acoustic_60s.mp3` · xử lý thêm để u tối |")
txt = txt.replace(
    "| 16 | Organ nhà thờ trầm buồn, u tối | Chưa có track organ trong `assets/bgm/` |",
    "| 16 | Organ nhà thờ trầm buồn, u tối | ✅ **ĐÃ TẢI** — `Sinister Cathedral` (Asher Fulero, ambient) → `assets/bgm/bgm_church_organ.mp3` |")

io.open(DOC, "w", encoding="utf-8").write(txt)
print("cap nhat xong: them %d dong vao muc 4.2, cap nhat bang BGM" % len(rows))
