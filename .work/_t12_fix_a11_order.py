# -*- coding: utf-8 -*-
"""Tập 12 — sắp xếp lại các dòng A11 (giữ nguyên nội dung, chỉ đổi thứ tự)."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = Path(__file__).resolve().parents[1] / "00_TIEU_CHUAN" / "TIEU_CHUAN_DUNG_VIDEO.md"
raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
lines = raw.split(nl)

idx = {}
for i, l in enumerate(lines):
    if l.startswith("| ") and l[2:5].strip().isdigit():
        idx[int(l[2:5].strip())] = i

mine = {188: lines[idx[188]], 189: lines[idx[189]]}
# xoa 2 dong cua minh
for k in (188, 189):
    lines[idx[k]] = None
# khoi phuc dong 184 (bi xoa nham) — chen ngay sau dong 183
row184 = ("| 184 | **Mục tập trong `edition.py` thiếu nhánh EN/JA ⇒ cổng `--plan`/`qc_bg_usage` "
          "ở EN/JA ĐỌC NHẦM bảng shot VI và vẫn báo ĐẠT (số liệu 3 ngôn ngữ giống hệt = dấu hiệu).** "
          "Tập 11 trước 16/11 chỉ có `\"dir\": \"Tap11\"`. Trước khi tin cổng nhiều ngôn ngữ: in `ED.PLAN`, "
          "`ED.EP['dir']`, `ED.EP['script']` cho từng `AE_LANG` | Đã vá `edition.py` mục \"11\" theo mẫu "
          "Tập 10 (script/dir/plan/master/srt/acting/sfx/thumb/title/act_titles/roles_*) |")
lines = [l for l in lines if l is not None]
# vi tri moi cua 183
pos183 = next(i for i, l in enumerate(lines) if l.startswith("| 183 |"))
lines.insert(pos183 + 1, row184)
# them 188/189 sau dong 187
pos187 = next(i for i, l in enumerate(lines) if l.startswith("| 187 |"))
lines.insert(pos187 + 1, mine[188])
lines.insert(pos187 + 2, mine[189])

P.write_text(nl.join(lines), encoding="utf-8", newline="")
print("da sap xep lai: 184 khoi phuc, 188/189 chuyen xuong cuoi")
for l in lines:
    if l.startswith("| 18") or l.startswith("| 19"):
        print("  " + l[:60])
