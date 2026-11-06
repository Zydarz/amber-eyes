#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chèn bảng số đo đầu ra (từ log QC) vào báo cáo QC Tập 03, thay khối <!-- FINAL_METRICS -->."""
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
REPORT = ROOT / "90_LUU_TRU/BaoCao_QC_Tap03_VN_MasterVideo_20261106.md"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
MP4 = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp4"
QCLOG = WORK / "_qc_final_t03.log"

def read_text_any(p):
    """Tee-Object ghi UTF-16 LE; file do python ghi UTF-8."""
    b = p.read_bytes()
    for enc in ("utf-8-sig", "utf-16", "cp1252"):
        try:
            return b.decode(enc)
        except (UnicodeDecodeError, UnicodeError):
            continue
    return b.decode("utf-8", errors="replace")


qc = read_text_any(QCLOG) if QCLOG.exists() else ""
verdict = "ĐẠT" if "KẾT LUẬN: ĐẠT" in qc else "CÓ LỖI"
failed = []
for line in qc.splitlines():
    if line.startswith("[LOI]"):
        failed.append(line.strip())

pr = subprocess.run([str(FF), "-v", "error", "-show_entries",
                     "stream=codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels,bit_rate",
                     "-show_entries", "format=duration,size,format_name,bit_rate",
                     "-of", "json", str(MP4)], capture_output=True, text=True).stdout
import json
info = json.loads(pr)
v = next(s for s in info["streams"] if s["codec_type"] == "video")
a = next(s for s in info["streams"] if s["codec_type"] == "audio")
dur = float(info["format"]["duration"])
size_mb = int(info["format"]["size"]) / 1e6

def grab(pattern, default="?"):
    m = re.search(pattern, qc)
    return m.group(1) if m else default

lufs = grab(r"LUFS=(-?[\d.]+)")
lra = grab(r"LRA=(-?[\d.]+)")
peak = grab(r"true peak=(-?[\d.]+)")
av = grab(r"lệch âm thanh: ([+-][\d.]+) ms")
sil = grab(r"\[G4 V4[^\n]*", "")

rows = []
for line in qc.splitlines():
    m = re.match(r"\[(OK  |LOI)\] (.+?) — (.*)$", line.strip())
    if m:
        rows.append((m.group(1).strip(), m.group(2).strip(), m.group(3).strip()))

table = ["| # | Cổng QC đầu ra | Kết quả | Đo được |", "|---|---|---|---|"]
for i, (st, name, det) in enumerate(rows, 1):
    mark = "✔" if st == "OK" else "✗"
    table.append(f"| {i} | {name} | {mark} | {det} |")

block = f"""
## 2.7. ĐẦU RA CUỐI — `Tap03_master.mp4` (đo trên chính file thành phẩm)

| Thuộc tính | Giá trị đo được |
|---|---|
| Container | `{info['format']['format_name']}` · {size_mb:.1f} MB · {dur:.3f} s |
| Video | {v['codec_name']} {v['width']}×{v['height']} @ {v['r_frame_rate']} fps |
| Audio | {a['codec_name']} {a['sample_rate']} Hz · {a['channels']} ch · {int(a.get('bit_rate', 0))//1000} kbps |
| Loudness | **{lufs} LUFS** (chuẩn −16 ± 1) · LRA {lra} |
| True peak | **{peak} dBFS** (trần −1,5 dBFS) |
| Lệch A/V | {av} (chuẩn ± 50 ms) |

**Kết luận các cổng QC đầu ra: {verdict}**

{chr(10).join(table)}
"""

if failed:
    block += "\n\n> **Các cổng chưa đạt:**\n" + "\n".join(f"> - {f}" for f in failed) + "\n"

txt = REPORT.read_text(encoding="utf-8")
if "<!-- FINAL_METRICS -->" in txt:
    txt = txt.replace("<!-- FINAL_METRICS -->", block.strip())
else:
    txt = txt.rstrip() + "\n" + block
REPORT.write_text(txt, encoding="utf-8")
print(f"Đã cập nhật báo cáo: {REPORT}")
print(f"Kết luận: {verdict} · {len(rows)} cổng · {len(failed)} lỗi")
