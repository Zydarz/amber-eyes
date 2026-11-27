# -*- coding: utf-8 -*-
"""Thêm luật H30 vào AGENTS.md: nguồn master audio + ASR phải chạy theo cửa sổ.

Thao tác theo DÒNG, giữ nguyên line-ending gốc.
Dùng: py -3 .work/_add_h30.py
"""
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "AGENTS.md"

raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
print("line-ending:", "CRLF" if nl == "\r\n" else "LF")
lines = raw.split(nl)

backup = ROOT / ".work" / "_cu" / f"agents_h30_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
shutil.copy2(P, backup / P.name)
print("backup ->", backup)

if any(l.startswith("| **H30** |") for l in lines):
    print(">> H30 da ton tai - khong chen them")
    sys.exit(0)

row = (
    "| **H30** | **Dựng timeline từ master audio: nguồn phải là MP3 (đúng file renderer dùng), và ASR PHẢI chạy theo CỬA SỔ "
    "ngắn — ASR trên cả file dài (> 55 s) có thể IM LẶNG bỏ mất đuôi, dễ bị kết luận nhầm là \"audio thiếu câu\".** "
    "TikTok Tap 04 EN TK2 (27/11/2026): master mp3 mới 72,34 s **có đủ 11/11 câu**, nhưng `faster-whisper` transcribe **cả file** "
    "chỉ trả về tới **57,72 s** ⇒ 2 câu cuối bị ghi \"NOI SUY\" ⇒ nghi nhầm audio thiếu (đã từng báo nhầm cho người dùng). "
    "Kiểm chứng: ASR riêng đuôi ⇒ **nhận đủ 2 câu**; **WAV cũ 70,90 s cũng đủ 11 câu** ⇒ **không phiên bản nào thiếu câu**. "
    "Thêm: builder đọc `.wav` (24/11) còn renderer đọc `.mp3` (27/11) ⇒ **lệch phiên bản âm thanh** | "
    "**BẮT BUỘC:** (1) builder đọc `.mp3` + **in cảnh báo khi wav/mp3 lệch > 0,05 s**; (2) ASR **theo cửa sổ 20,5 s, overlap 4 s, "
    "cửa sổ cuối neo vào cuối file** + khử trùng theo (text, mốc) < 0,6 s; (3) giải mã bằng **`f32le`** (không dùng `s16le` — đo được "
    "`s16le` cắt sớm hơn 9,5 s); (4) **đừng kết luận \"audio thiếu câu\" khi ASR thiếu** — phải kiểm chứng bằng ASR riêng đuôi + "
    "envelope RMS + đối chiếu thời lượng wav/mp3; (5) **kiểm tra phủ đuôi MỌI clip**: `timeline_end` cách `speech_end` "
    "(RMS > −45 dBFS) ≤ 1,5 s (`.work/_check_tail_coverage.py`); (6) **đo nền im lặng của master** — master **không có nhạc nền** "
    "(nền ≈ −70 dB, > 5 % file im lặng tuyệt đối) ⇒ **trượt T6** (khoảng câm > 0,3 s) + **true peak vượt trần** nếu không hạ đỉnh. "
    "Luật chi tiết: **A11 #200** | TikTok Tap 04 EN TK2 (27/11/2026): builder đọc wav 24/11 (70,90 s) còn renderer đọc mp3 27/11 "
    "(72,34 s) ⇒ 2 câu cuối bị mất khỏi timeline. Đo được: nền im lặng master mới **−70,6 dB** (14 clip khác −16…−17 dB), "
    "**8,1 % file im lặng tuyệt đối**, **11 khoảng câm > 0,3 s** (dài nhất 0,843 s), **true peak +1,25 dBFS** với 312 mẫu > 0 dBFS |"
)

# Chen ngay sau dong H29
idx = next(i for i, l in enumerate(lines) if l.startswith("| **H29** |"))
lines.insert(idx + 1, row)
P.write_text(nl.join(lines), encoding="utf-8", newline="")

check = P.read_text(encoding="utf-8")
print("H30 co:", any(l.startswith("| **H30** |") for l in check.split(nl)),
      "| CRCRLF:", check.count("\r\r\n"), "| dong:", len(check.split(nl)))
