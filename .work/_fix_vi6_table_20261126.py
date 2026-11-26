#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cập nhật bảng kiểm kê VI.6 theo số đo thực tế 26/11/2026."""
import json
import re
import shutil
import collections
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md"
CU = ROOT / ".work" / "_cu"
BG = ROOT / "assets" / "bg"

cnt = collections.Counter()
for f in BG.iterdir():
    if f.is_file() and f.suffix.lower() == ".png":
        m = re.match(r"t(\d+)_", f.name)
        if m and 1 <= int(m.group(1)) <= 68:
            cnt[int(m.group(1))] += 1

jobs = {}
for ep in range(1, 69):
    p = ROOT / ".work" / f"bg_jobs_tap{ep}.json"
    if p.exists():
        d = json.loads(p.read_text(encoding="utf-8"))
        if isinstance(d, dict):
            for k in ("jobs", "items", "shots"):
                if k in d:
                    d = d[k]
                    break
        jobs[ep] = len(d)

NOTE_OLD = "cũ trước xáo (sai vụ án), không dùng lại"
NOTE_NEW = "cũ trước xáo (sai vụ án), không dùng lại"
NOTE_DONE = "✔ đã đủ ảnh (26/11)"

txt = REPORT.read_text(encoding="utf-8")

# 1. Dòng tập 49
old49 = "  - **`bg_jobs` trượt cổng (1 tập):** 49 — *[25/11: ĐÃ viết lại 190 prompt, cần sinh 190 ảnh — xem VI.7]*."
new49 = ("  - ~~**`bg_jobs` trượt cổng (1 tập):** 49~~ → **[25/11/2026: ĐÃ viết lại toàn bộ 190 prompt, cổng ĐẠT; "
         "vẫn cần sinh 190 ảnh — xem VI.7.]**")
if old49 in txt:
    txt = txt.replace(old49, new49)
    print("da sua dong tap 49")
else:
    print("!! dong tap 49 khong khop")

# 2. Bảng VI.6: dựng lại từ số đo
lines = txt.split("\n")
out = []
in_tbl = False
n_row = 0
for line in lines:
    m = re.match(r"^\| (\d{2}) \| (\d+) \| (\d+) \| (.*) \|$", line)
    if m:
        in_tbl = True
        ep = int(m.group(1))
        job = jobs.get(ep)
        have = cnt.get(ep, 0)
        note = m.group(4)
        if job is None:
            job_s, have_s, note = "—", str(have), "chưa có `bg_jobs` (chờ kịch bản mở rộng — H23)"
        else:
            job_s, have_s = str(job), str(have)
            if have >= job:
                note = NOTE_DONE
            elif have == 0:
                note = NOTE_NEW
            else:
                note = f"thiếu {job - have} ảnh"
        out.append(f"| {ep} | {job_s} | {have_s} | {note} |")
        n_row += 1
        continue
    if in_tbl and not line.startswith("|"):
        in_tbl = False
    out.append(line)
txt = "\n".join(out)
print(f"da dong lai {n_row} dong bang VI.6")

# 3. Cập nhật tiêu đề VI.6 cho ghi rõ ngày đo
txt = txt.replace(
    "### VI.6. KIỂM KÊ ẢNH TRONG `assets/bg/` THEO TẬP (đo 25/11/2026, quét từng file `tNN_*.png|jpg`)",
    "### VI.6. KIỂM KÊ ẢNH TRONG `assets/bg/` THEO TẬP (đo 25/11/2026 · **đo lại 26/11/2026**, quét từng file `tNN_*.png|jpg`)",
)

CU.mkdir(parents=True, exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d_%H%M")
bak = CU / f"BaoCao_ThongKe_68_truoc_bang_VI6_{stamp}.md"
shutil.copy2(REPORT, bak)
REPORT.write_text(txt, encoding="utf-8")
print(f"backup: {bak.name}")
