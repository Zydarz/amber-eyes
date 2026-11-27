# -*- coding: utf-8 -*-
"""Thêm dòng A11 #201: ASR phải chạy trên VOICE STEM, không phải master đã trộn BGM.

Thao tác theo DÒNG, giữ nguyên line-ending gốc.
Dùng: py -3 .work/_tk_add_a11_201.py
"""
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "00_TIEU_CHUAN" / "TIEU_CHUAN_DUNG_VIDEO.md"

raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
lines = raw.split(nl)
print("line-ending:", "CRLF" if nl == "\r\n" else "LF")

backup = ROOT / ".work" / "_cu" / f"a11_201_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
shutil.copy2(P, backup / P.name)
print("backup ->", backup)

rows = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := re.match(r"^\| (\d+) \|", l))]
nums = [n for _, n in rows]
if 201 in nums:
    print(">> A11 201 da ton tai - khong chen them")
    sys.exit(0)
print("A11 max =", max(nums))

row201 = (
    "| 201 | **ASR phải chạy trên VOICE STEM (giọng thuần), KHÔNG chạy trên master ĐÃ TRỘN BGM — BGM làm ASR nhiễu mạnh, "
    "timeline vỡ thành nhiều dòng NOI SUY.** TikTok Tap 04 EN TK2 (27/11/2026): sau khi trộn BGM + ambience vào master, "
    "chạy lại ASR trên chính master đó ⇒ **9/11 dòng lỗi** (`NOI SUY` 2 dòng, `MATCH YEU` 6 dòng, `asr_end` chỉ 68,48/72,34 s) "
    "dù audio hoàn toàn đúng ⇒ nghi nhầm \"sai timeline\". Chạy ASR trên **file giọng thuần** (voice stem, trước khi trộn) "
    "⇒ **11/11 câu khớp 100 %, 0 dòng lỗi, `asr_end` 72,00/72,34 s** | "
    "**Quy trình bắt buộc khi dựng lại master có BGM:** (1) **LƯU voice stem** ra file riêng (`<clip>_voice_stem.mp3`) "
    "**NGAY KHI tạo**, trước khi trộn — không có stem thì phải khôi phục từ master cũ trong `.work/_cu/`; "
    "(2) script trộn phải **idempotent**: đọc voice từ stem nếu có, không đọc lại master đã trộn (đọc lại ⇒ trộn 2 lần); "
    "(3) builder timeline nhận `--audio <file>` để trỏ ASR sang voice stem — **mốc thời gian không đổi** vì trộn không dịch/lùi voice; "
    "(4) **luôn kiểm tra `asr_end` ≈ thời lượng master**; nếu lệch > 1 s ⇒ đổi nguồn ASR sang stem trước khi kết luận audio/kịch bản sai. "
    "Bài học chung: **khi sửa audio, phải tách 2 lớp — voice (đo mốc thời gian) và bed (trộn)** |"
)

last_idx = max(i for i, n in rows)
lines.insert(last_idx + 1, row201)
P.write_text(nl.join(lines), encoding="utf-8", newline="")

check = P.read_text(encoding="utf-8")
cnums = [int(m.group(1)) for l in check.split(nl) if (m := re.match(r"^\| (\d+) \|", l))]
print("max A11 =", max(cnums), "| 201 co:", 201 in cnums, "| CRCRLF:", check.count("\r\r\n"))
