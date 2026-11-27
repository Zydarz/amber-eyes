# -*- coding: utf-8 -*-
"""Thêm dòng A11 #200 (bài học: ASR bỏ đuôi file dài; nguồn timeline phải là mp3 = file renderer dùng).

Thao tác theo DÒNG, không ghi lại toàn file; giữ nguyên line-ending gốc (CRLF).
Dùng: py -3 .work/_tk_add_a11_200.py
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
print(f"line-ending: {'CRLF' if nl == chr(13) + chr(10) else 'LF'}")

backup = ROOT / ".work" / "_cu" / f"a11_200_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
shutil.copy2(P, backup / P.name)
print(f"backup -> {backup}")

rows = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := re.match(r"^\| (\d+) \|", l))]
nums = [n for _, n in rows]
if 200 in nums:
    print(">> A11 200 da ton tai - khong chen them")
    sys.exit(0)
maxn = max(nums)
print(f"A11 max hien tai = {maxn} (so muc = {len(nums)})")

row200 = (
    "| 200 | **ASR trên file master DÀI (> 55 s) có thể im lặng bỏ mất đuôi — dễ bị kết luận nhầm là \"audio thiếu câu\"; và nguồn dựng timeline phải là MP3 (đúng file renderer dùng), không phải WAV.** "
    "TikTok Tap 04 EN TK2 (27/11/2026): master mp3 mới 72,34 s có **đủ 11/11 câu**, nhưng `faster-whisper` transcribe **cả file** chỉ trả về tới **57,72 s** ⇒ 2 câu cuối bị ghi \"NOI SUY\" ⇒ nghi nhầm audio thiếu. "
    "Đo lại bằng ASR riêng đoạn đuôi (58,2–72,3 s) ⇒ **nhận đủ cả 2 câu, 100 % khớp**. "
    "Nguyên nhân thật: **WAV cũ 70,90 s cũng ĐỦ cả 2 câu** (ASR riêng đuôi WAV cho ra \"Through the lens of criminal psychology…\" 56,90–62,32 s và \"Episode 4 of Amber Eyes…\" 65,88–70,06 s) ⇒ **không có câu nào bị thiếu ở bất kỳ phiên bản nào**; "
    "đường giải mã `s16le` còn làm whisper cắt sớm hơn (`f32le` thì lấy tới 67,22 s nhưng vẫn mất câu cuối) ⇒ lỗi ở **cách đọc file dài**, không ở audio. "
    "Hệ quả: timeline builder đọc `.wav` (bản 24/11) trong khi renderer đọc `.mp3` (bản 27/11) ⇒ **lệch phiên bản âm thanh** | "
    "**Quy tắc:** 1) **ASR phải chạy theo CỬA SỔ ngắn** (20,5 s, overlap 4 s, cửa sổ cuối neo vào cuối file) + **khử trùng theo (text, mốc thời gian) < 0,6 s** — đo được 11/11 câu khớp 100 %, `asr_end` 72,00/72,34 s; "
    "2) **Giải mã bằng `f32le`**, không dùng `s16le`; 3) **Builder đọc `.mp3`** (đúng file renderer dùng) và **in cảnh báo khi wav/mp3 lệch > 0,05 s**; "
    "4) **Đừng kết luận \"audio thiếu câu\" khi ASR thiếu** — phải kiểm chứng bằng (a) ASR riêng đoạn đuôi, (b) envelope RMS đo vùng im lặng, (c) đối chiếu thời lượng wav vs mp3; "
    "5) **Kiểm tra phủ đuôi cho MỌI clip**: `timeline_end` phải cách `speech_end` (RMS > −45 dBFS) ≤ 1,5 s — công cụ `.work/_check_tail_coverage.py` (15/15 clip đạt sau khi vá EN TK2). "
    "Bài học nâng cao: khi nghi \"file thiếu nội dung\", **đo lại trên chính file mới** trước khi kết luận |"
)

last_idx = max(i for i, n in rows)
lines.insert(last_idx + 1, row200)
P.write_text(nl.join(lines), encoding="utf-8", newline="")

check = P.read_text(encoding="utf-8")
cnums = [int(m.group(1)) for l in check.split(nl) if (m := re.match(r"^\| (\d+) \|", l))]
print("max A11 =", max(cnums), "| 200 co:", 200 in cnums, "| trung so:", len(cnums) != len(set(cnums)),
      "| CRCRLF:", check.count("\r\r\n"), "| dong:", len(check.split(nl)))
