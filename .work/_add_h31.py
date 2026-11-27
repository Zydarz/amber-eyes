# -*- coding: utf-8 -*-
"""Them luat H31 vao AGENTS.md: tach VOICE STEM khi trộn master co BGM.

Thao tac theo DONG, giu nguyen line-ending goc.
Dung: py -3 .work/_add_h31.py
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

backup = ROOT / ".work" / "_cu" / f"agents_h31_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
shutil.copy2(P, backup / P.name)
print("backup ->", backup)

if any(l.startswith("| **H31** |") for l in lines):
    print(">> H31 da ton tai - khong chen them")
    sys.exit(0)

row = (
    "| **H31** | **Khi trộn lại master audio có BGM: PHẢI tách VOICE STEM và LƯU ra file riêng — và mọi phép đo mốc thời gian "
    "(ASR) phải chạy trên STEM, không chạy trên master đã trộn.** TikTok Tap 04 EN TK2 (27/11/2026): sau khi trộn "
    "`bgm_ambient_deep` + ambience vào master, chạy lại ASR trên chính master ⇒ **9/11 dòng lỗi** (2 `NOI SUY`, 6 `MATCH YEU`, "
    "`asr_end` 68,48/72,34 s) dù audio hoàn toàn đúng ⇒ nghi nhầm \"sai timeline\"; chạy lại trên **voice thuần** ⇒ **11/11 câu "
    "khớp 100 %, 0 lỗi**. Thêm: `faster-whisper` trên file có BGM bị nhiễu nặng hơn hẳn file giọng thuần | "
    "**Quy trình bắt buộc:** (1) **LƯU voice stem** (`<clip>_voice_stem.mp3`) **ngay khi tạo**, trước khi trộn — mất stem thì "
    "chỉ còn khôi phục được từ master cũ trong `.work/_cu/`; (2) script trộn **idempotent**: đọc voice từ stem nếu có, **không** "
    "đọc lại master đã trộn (đọc lại ⇒ trộn 2 lần); (3) builder timeline nhận `--audio <file>` để trỏ ASR sang stem — **mốc thời "
    "gian không đổi** vì trộn không dịch/lùi voice; (4) **kiểm tra `asr_end` ≈ thời lượng master** (lệch > 1 s ⇒ đổi nguồn ASR "
    "sang stem TRƯỚC khi kết luận audio hay kịch bản sai); (5) khi trộn, **giữ headroom**: hạ voice về peak −6 dBFS và raw mix về "
    "−3 dBFS trước khi ghi WAV 16-bit — nếu không, WAV clip cứng ⇒ `measured_TP` sai ⇒ **loudnorm 2-pass cho kết quả sai** "
    "(đo được: peak +19,49 dBFS ⇒ output TP −12,11 dBFS thay vì −4,5). Luật chi tiết: **A11 #201** |"
    "TikTok Tap 04 EN TK2 (27/11/2026): master mới 72,34 s đủ 11/11 câu nhưng **không có nhạc nền** (nền −70,6 dB, 8,1 % file "
    "im lặng tuyệt đối) ⇒ **11 khoảng câm > 0,3 s (trượt T6)** + **peak +1,25 dBFS, 312 mẫu > 0 dBFS (vượt trần A7)**. "
    "Sau khi trộn lại: **0 khoảng câm, 0 mẫu clip, I −16,0 LUFS, TP −4,48 dBFS** |"
)

idx = next(i for i, l in enumerate(lines) if l.startswith("| **H30** |"))
lines.insert(idx + 1, row)
P.write_text(nl.join(lines), encoding="utf-8", newline="")

check = P.read_text(encoding="utf-8")
print("H31 co:", any(l.startswith("| **H31** |") for l in check.split(nl)),
      "| CRCRLF:", check.count("\r\r\n"), "| dong:", len(check.split(nl)))
