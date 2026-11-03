#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lại PHỤ LỤC A của hồ sơ Tập 06.

- Giữ nguyên phần "Chi danh" da tay (giau hon truong `direction` cua script).
- Cap nhat lai So cau / So tu theo script hien tai (154 cau).
- Sua lai "Chi danh" cho 11 element da doi so cau (noi dung da tach lai).
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PLAN = ROOT / "02_SAN_XUAT" / "Tap06" / "KeHoach_Video_Tap06.md"
SCRIPT = json.loads((ROOT / ".work" / "script_tap06.json").read_text(encoding="utf-8-sig"))

ROLE_LABEL = {"H": "Cú · Host", "D": "**Sói · Điều tra viên**", "C": "**Cáo · Chuyên gia**"}
N_LABEL = {"1.09": "**Cừu · N1**", "4.04": "**Mèo · N2**"}

# "Chi danh" moi cho 11 element doi so cau (noi dung da tach lai 01/11/2026)
NOTE_FIX = {
    "1.06": "Đêm 11/12/1978 · bà Elizabeth Piest đón Robert tan ca ở hiệu thuốc Nisson",
    "1.08": "Mức lương 5 đô/giờ · Robert đi vào tiệm và không bao giờ quay lại",
    "1.09": "Kim Byers - giọng nữ trẻ 17 tuổi bàng hoàng, nghẹn ngào",
    "1.14": "Một chi tiết nhỏ: quần áo của Gacy dính đầy bùn đất",
    "3.05": "Mở nắp sàn xuống tầng dưới ngôi nhà · điều mình lo sợ nhất thành sự thật",
    "3.07": "Ánh đèn pin quét qua mặt đất phủ đầy bụi bặm · sự thật kinh hoàng xé toạc màn đêm",
    "3.09": "Đội ngũ pháp y lần lượt xác định thêm nhiều nạn nhân",
    "3.10": "Giải phẫu tâm lý: không gian chôn giấu và nhu cầu chiếm hữu ở mức bệnh hoạn",
    "4.08": "Luận cứ đanh thép: hành động có kế hoạch từ trước, đào rãnh dưới nền nhà, mánh khóe lừa gạt",
    "5.02": "14 năm biệt giam Menard, tranh chú hề và tuyên bố 'nạn nhân thứ ba mươi tư'",
    "5.04": "Thi hành án tử hình đêm 10/05/1994 tại Trại giam Stateville",
}

# ---- doc bang PHU LUC A hien tai
text = PLAN.read_text(encoding="utf-8-sig")
lines = text.split("\n")
i_a = next(k for k, l in enumerate(lines) if l.startswith("## PHỤ LỤC A"))
i_b = next(k for k, l in enumerate(lines) if l.startswith("## PHỤ LỤC B"))
old_note, old_vai = {}, {}
for l in lines[i_a:i_b]:
    m = re.match(r"^\|\s*`(\d\.\d+)`\s*\|(.*)$", l)
    if not m:
        continue
    eid = m.group(1)
    rest = m.group(2)
    parts = [c.strip() for c in rest.split("|")]
    if len(parts) >= 4:
        old_vai[eid] = parts[0]
        old_note[eid] = parts[3]

rows, tot_sent, tot_word = [], 0, 0
for el in SCRIPT:
    eid, kind = el["id"], el.get("kind")
    if kind == "LOI":
        n = len(el.get("sentences") or [])
        w = len((el.get("text") or "").split())
        vai = N_LABEL.get(eid) or ROLE_LABEL.get(el.get("role"), f"*{el.get('role')}*")
    elif kind == "BGM":
        n = w = 0
        vai = "*BGM*"
    elif kind == "SFX":
        n = w = 0
        vai = "*SFX*"
    else:
        n = w = 0
        vai = f"*Nghỉ {el.get('sec')} s*"
    note = NOTE_FIX.get(eid) or old_note.get(eid, "")
    tot_sent += n
    tot_word += w
    rows.append(f"| `{eid}` | {vai} | {n if n else '—'} | {w if w else '—'} | {note} |")
rows.append(f"| | **Tổng** | **{tot_sent}** | **{tot_word:,}** | |".replace(",", "."))

# ---- thay the bang cu (tu dong duong tieu de bang den het truoc PHU LUC B)
i_hdr = next(k for k in range(i_a, i_b) if lines[k].startswith("| Mã |"))
i_sep = i_hdr + 1
assert lines[i_sep].startswith("|---"), lines[i_sep][:40]
new = lines[:i_sep + 1] + rows + [""] + lines[i_b:]
PLAN.write_text("\n".join(new), encoding="utf-8")
print(f"PHU LUC A: {len(rows) - 1} dong · tong {tot_sent} cau · {tot_word} tu")
