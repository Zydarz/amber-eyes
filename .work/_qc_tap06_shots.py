# -*- coding: utf-8 -*-
"""QC A9.2 cho Tập 06 — Bảng shot vs kịch bản vs assets/bg."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"
PLAN_FILE = ROOT / "02_SAN_XUAT" / "Tap06" / "KeHoach_Video_Tap06.md"

with open(WORK / "script_tap06.json", encoding="utf-8") as f:
    script = json.load(f)

sent_dict = {}
for el in script:
    role = el.get("role")
    for s in el.get("sentences", []):
        sent_dict[s["id"]] = {"role": role, "text": s["text"]}

all_sids = list(sent_dict.keys())
print(f"Tổng số câu kịch bản: {len(all_sids)}")

# Đọc bảng shot từ PLAN_FILE
plan_text = PLAN_FILE.read_text(encoding="utf-8")

# Parse các dòng bảng shot (dòng bắt đầu bằng | X-XX |)
shot_pattern = r'^\|\s*(\d+-\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|'
lines = plan_text.splitlines()

shots = []
for line in lines:
    m = re.match(shot_pattern, line.strip())
    if m:
        shot_id = m.group(1).strip()
        cues = m.group(2).strip()
        vai = m.group(3).strip()
        mau = m.group(4).strip()
        nen = m.group(5).strip()
        chu = m.group(6).strip()
        beat = m.group(7).strip()
        nv = m.group(8).strip()
        shots.append({
            "id": shot_id, "cues": cues, "vai": vai, "mau": mau,
            "nen": nen, "chu": chu, "beat": beat, "nv": nv
        })

print(f"Tổng số shot parse được: {len(shots)}")

ok = True
errs = []

def check(label, condition, msg=""):
    global ok
    if condition:
        print(f"[OK  ] {label}" + (f": {msg}" if msg else ""))
    else:
        ok = False
        print(f"[FAIL] {label}" + (f": {msg}" if msg else ""))
        errs.append(f"{label}: {msg}")

# 1. Kiểm tra phủ câu
covered_sids = []
dups = []
for sh in shots:
    cues_str = sh["cues"].replace('`', '').replace('–', '-').replace('—', '-')
    # Tách các khoảng
    parts = [p.strip() for p in cues_str.split(',')]
    for part in parts:
        if '-' in part:
            sp = part.split('-')
            start_p = sp[0].strip()
            end_p = sp[1].strip()
            if '#' in end_p and not '.' in end_p:
                prefix = start_p.split('#')[0]
                end_p = f"{prefix}{end_p}"
            elif not '#' in end_p and start_p.startswith(('1.', '2.', '3.', '4.', '5.')):
                prefix = start_p.split('#')[0]
                end_p = f"{prefix}#{end_p}"
            
            if start_p in all_sids and end_p in all_sids:
                i1 = all_sids.index(start_p)
                i2 = all_sids.index(end_p)
                for i in range(i1, i2 + 1):
                    sid = all_sids[i]
                    if sid in covered_sids:
                        dups.append((sid, sh["id"]))
                    covered_sids.append(sid)
            else:
                # Có thể là cue dạng 1.01 hoặc hết tập
                pass
        else:
            if part in all_sids:
                sid = part
                if sid in covered_sids:
                    dups.append((sid, sh["id"]))
                covered_sids.append(sid)

missing = [s for s in all_sids if s not in covered_sids]
check("1. Phủ câu đầy đủ", len(missing) == 0, f"Đã phủ {len(set(covered_sids))}/{len(all_sids)} câu. Sót: {missing}")
check("2. Không trùng lặp câu", len(dups) == 0, f"Trùng: {dups}")

# 3. Kiểm tra ảnh nền tồn tại trong assets/bg
bg_files = {p.stem: p for p in BG_DIR.glob("*.png")}
missing_bgs = []
for sh in shots:
    nen_field = sh["nen"]
    # Trích tên file trong dấu backtick hoặc từ đầu tiên
    m_bg = re.search(r'`(t6_[^`]+)`', nen_field)
    if not m_bg:
        m_bg = re.search(r'(t6_\w+)', nen_field)
    if m_bg:
        bg_name = m_bg.group(1)
        if bg_name not in bg_files:
            missing_bgs.append((sh["id"], bg_name))

check("3. Ảnh nền tồn tại trên đĩa", len(missing_bgs) == 0, f"Thiếu {len(missing_bgs)} ảnh: {missing_bgs}")

# 4. Kiểm tra Shot cuối H12
last_shot = shots[-1]
h12_pass = ("HỒ SƠ TẬP 06 · ĐÃ ĐÓNG" in last_shot["chu"] and "AMBER EYES" in last_shot["chu"])
check("4. Shot cuối H12 đúng chuẩn", h12_pass, f"Shot {last_shot['id']}: {last_shot['chu']}")

# 5. Kiểm tra từ cấm V9 trong cột chữ
banned_words = ["hiếp dâm", "chặt xác", "cắt cổ", "máu me", "tự tử", "thắt cổ"]
banned_found = []
for sh in shots:
    for bw in banned_words:
        if bw in sh["chu"].lower():
            banned_found.append((sh["id"], bw))
check("5. Không từ cấm V9 trong cột Chữ", len(banned_found) == 0, f"Phát hiện: {banned_found}")

print("--- KẾT QUẢ QC BẢNG SHOT TẬP 06 ---")
if ok:
    print(">>> TẤT CẢ CÁC BƯỚC QC ĐỀU ĐẠT CHUẨN XUẤT SẮC! <<<")
else:
    print(f">>> CÓ {len(errs)} LỖI CẦN XỬ LÝ! <<<")
