#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cập nhật 3 tài liệu sau khi sinh xong acting_tap03.json."""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
AMTH = ROOT / "02_SAN_XUAT" / "Tap03" / "AmThanh_Tap03.md"
MANIF = ROOT / "02_SAN_XUAT" / "Tap03" / "Danh_Sach_Anh_Tap03.md"
REVIEW = ROOT / "01_KICH_BAN" / "Tap03" / "REVIEW_kichban_tap03.md"

# ---------------------------------------------------------------- AmThanh
a = AMTH.read_text(encoding="utf-8")
old = "| 4 | Diễn xuất từng câu cho TTS | **Chưa** — Tập 02 có `.work/make_acting_tap02.py`; Tap03 cần bản tương tự (215 câu) |"
new = ("| 4 | Diễn xuất từng câu cho TTS | ✅ **Đã làm 23/10** — `.work/make_acting_tap03.py` → `.work/acting_tap03.json`: "
       "215 câu, 162 mốc then chốt, 60 khoảng lặng thêm (29,3 s — cùng mức Tập 02: 27,2 s), "
       "bộ tham số an toàn (cảm xúc neutral·sad·fearful·surprised, cao độ luôn 0) |")
assert a.count(old) == 1
a = a.replace(old, new, 1)

old2 = "| 3 | Chạy `build_audio3.py` cho tập 3 | **Chưa** — phụ thuộc 2 việc trên |"
new2 = "| 3 | Chạy `build_audio3.py` cho tập 3 | **Chưa** — khối `EPISODES[\"03\"]` + `acting_tap03.json` + bảng âm thanh đã xong; còn cần bảng shot để dựng hình |"
assert a.count(old2) == 1
a = a.replace(old2, new2, 1)

# them muc ve dien xuat vao phan gioi hanh
old3 = "## 4. Giới hạn thật — đọc trước khi dựng"
new3 = """### 3.4 Diễn xuất TTS — `.work/acting_tap03.json`

Sinh bởi `.work/make_acting_tap03.py` (bản riêng cho Tập 03, không sửa bản Tập 02):

| | Tập 02 | Tập 03 |
|---|---:|---:|
| Số câu | 215 | 215 |
| Mốc then chốt được soạn tay | ~60 | **162** |
| Cảm xúc (neutral / sad / fearful / surprised) | 160 / 28 / 14 / 13 | 139 / **49** / 19 / 8 |
| Khoảng lặng thêm giữa câu | 70 chỗ · 27,2 s | 60 chỗ · **29,3 s** |
| Lời đọc riêng (chỉ thêm ngắt nghỉ) | có | 6 câu |

**Bộ tham số an toàn (giữ nguyên từ Tập 02):** cao độ **luôn = 0**; cảm xúc chỉ trong
`neutral · sad · fearful · surprised` — bộ giọng đã thử ở Tập 02 chỉ được kiểm ở cao độ 0.
Lệch tốc độ kẹp trong `[-0,06 · +0,02]`, phân bố 5 bậc (Tập 03 có **độ tương phản tốt hơn**
Tập 02: không bậc nào chiếm quá 32 %, Tập 02 dồn 51 % vào một bậc).

**Quy tắc bất biến:** lời đọc riêng chỉ được **thêm ngắt nghỉ**, tuyệt đối **không đổi chữ** —
phụ đề và chữ trên hình giữ nguyên kịch bản. Đã kiểm tự động: bỏ hết thẻ `<#..#>` rồi so
với câu gốc, **215/215 câu giống hệt**, không còn dấu nháy kép trong lời đọc.

## 4. Giới hạn thật — đọc trước khi dựng"""
assert a.count(old3) == 1
a = a.replace(old3, new3, 1)
AMTH.write_text(a, encoding="utf-8")
print("  OK  AmThanh_Tap03.md")

# ---------------------------------------------------------------- Manifest
m = MANIF.read_text(encoding="utf-8")
oldm = "| 8 | Dựng audio TTS + trộn cho Tập 03 | ⚠️ **Khối `EPISODES[\"03\"]` đã thêm xong** (mục 3) — còn thiếu `.work/acting_tap03.json` (diễn xuất 215 câu) và bảng shot thì `build_audio3.py` mới chạy trọn |"
newm = "| 8 | Dựng audio TTS + trộn cho Tập 03 | ⚠️ `EPISODES[\"03\"]` + `acting_tap03.json` (215 câu) + bảng âm thanh **đã xong** — còn thiếu **bảng shot** thì `build_audio3.py` mới dựng trọn được |"
assert m.count(oldm) == 1
m = m.replace(oldm, newm, 1)
MANIF.write_text(m, encoding="utf-8")
print("  OK  Danh_Sach_Anh_Tap03.md")

# ---------------------------------------------------------------- REVIEW
r = REVIEW.read_text(encoding="utf-8")
oldr = """**Còn thiếu**: `KeHoach_Video_Tap03.md` (bảng shot) · `.work/acting_tap03.json` (diễn xuất TTS) · `.work/shots.json` · `Tap03_master.mp3` · `Tap03.srt`."""
newr = """**Đã có thêm (23/10)**: `.work/acting_tap03.json` — 215 câu, sinh bởi `.work/make_acting_tap03.py` (162 mốc then chốt, 60 khoảng lặng · 29,3 s, bộ tham số an toàn cao độ = 0).
**Còn thiếu**: `KeHoach_Video_Tap03.md` (bảng shot) · `.work/shots.json` · `Tap03_master.mp3` · `Tap03.srt`."""
assert r.count(oldr) == 1
r = r.replace(oldr, newr, 1)
REVIEW.write_text(r, encoding="utf-8")
print("  OK  REVIEW_kichban_tap03.md")
print("\nDa cap nhat 3 tai lieu.")
