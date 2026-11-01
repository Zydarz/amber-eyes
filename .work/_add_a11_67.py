# -*- coding: utf-8 -*-
"""Them bai hoc A11 #67 (T05, 01/11/2026) vao TIEU_CHUAN_DUNG_VIDEO.md."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\00_TIEU_CHUAN\TIEU_CHUAN_DUNG_VIDEO.md")
lines = p.read_text(encoding="utf-8").splitlines()

row67 = (
    "| 67 | **Tách lại kịch bản (số câu đổi) làm bảng shot + phụ đề mất hiệu lực mà không ai báo** "
    "(Tập 05, 01/11/2026): kịch bản Higgs đổi 164 → **162 câu** (2.02 4→5, 2.04 10→8, 4.02 9→10, "
    "4.12 8→6 bỏ lời thoại trực tiếp) trong khi mục 6 của hồ sơ vẫn trỏ mã cũ ⇒ `parse_shots.py` **KeyError**; "
    "các element giữ nguyên số câu nhưng **câu bị viết lại** ⇒ chữ trên hình (số, trích dẫn) không còn nằm "
    "trong câu đang đọc, vi phạm H6/V3 | "
    "Mỗi lần kịch bản đổi: (1) **QC bảng shot trước khi dựng** — `qc_shots_t04.py --ep XX` "
    "(bản riêng cho T05: `_qc_shots_t05.py`, có whitelist *có ghi chú*) để bắt \"mã câu không tồn tại\", "
    "\"thiếu câu\", \"số không có trong câu\", \"trích dẫn không nguyên văn\"; "
    "(2) **sửa bảng shot theo nội dung câu mới** (map cũ→mới bằng diff nội dung, không đoán số thứ tự) — "
    "dải mã câu, chữ trên hình, trích dẫn, và **nền** khi chủ đề câu đã bị gỡ khỏi kịch bản; "
    "(3) `parse_shots.py` → `subtitles.py` → ảnh tĩnh `--stills all` → soi mắt → mới dựng hình |"
)

idx = next(i for i, l in enumerate(lines) if l.startswith("| 66 |"))
lines.insert(idx + 1, row67)
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("da them A11 #67 tai dong", idx + 2)
