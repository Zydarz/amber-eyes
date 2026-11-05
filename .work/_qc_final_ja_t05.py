# -*- coding: utf-8 -*-
"""Comprehensive QC for Episode 05 Japanese (Tap05_JA)."""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

OUT = ROOT / "02_SAN_XUAT/Tap05_JA/xuat_ban"
MP4 = OUT / "Tap05_JA_master.mp4"
MP3 = OUT / "Tap05_JA_master.mp3"
SRT = OUT / "Tap05_JA.srt"
THUMB = OUT / "thumbnail.png"
PLAN = ROOT / "02_SAN_XUAT/Tap05_JA/KeHoach_Video_Tap05_JA.md"

tl = json.loads((W / "timeline_s_JA_t05.json").read_text(encoding="utf-8"))
sh = json.loads((W / "shots_JA_t05.json").read_text(encoding="utf-8"))
script = json.loads((W / "script_tap05_JA.json").read_text(encoding="utf-8"))

print("==================================================")
print("       BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG (QC)")
print("       TẬP 05 · BẢN TIẾNG NHẬT (JA)")
print("==================================================")

results = {}

# 1. Output files presence
print("\n--- 1. KIỂM TRA FILE ĐẦU RA ---")
files = [MP4, MP3, SRT, THUMB, PLAN]
for f in files:
    exists = f.exists()
    sz = f.stat().st_size if exists else 0
    print(f"  {f.name:25s}: {'EXISTS' if exists else 'MISSING'} ({sz / (1024*1024):.2f} MB)")
results["files_exist"] = all(f.exists() and f.stat().st_size > 0 for f in files)

# 2. Probe MP4
print("\n--- 2. ĐO THÔNG SỐ VIDEO MASTER MP4 ---")
cmd_probe = [
    str(FFPROBE), "-v", "error", "-show_entries",
    "format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,duration,nb_frames",
    "-of", "json", str(MP4)
]
p = subprocess.run(cmd_probe, capture_output=True, text=True, encoding="utf-8")
probe_data = json.loads(p.stdout)
fmt = probe_data.get("format", {})
streams = probe_data.get("streams", [])

v_stream = next((s for s in streams if s.get("codec_type") == "video"), {})
a_stream = next((s for s in streams if s.get("codec_type") == "audio"), {})

v_dur = float(v_stream.get("duration", fmt.get("duration", 0)))
a_dur = float(a_stream.get("duration", fmt.get("duration", 0)))
v_fps = v_stream.get("r_frame_rate", "unknown")
w, h = v_stream.get("width"), v_stream.get("height")
v_codec = v_stream.get("codec_name")
a_codec = a_stream.get("codec_name")
sync_delta = abs(v_dur - a_dur)
tl_delta = abs(v_dur - tl["total"])

print(f"  Video: {w}x{h} @ {v_fps} fps, codec: {v_codec}, duration: {v_dur:.3f} s")
print(f"  Audio: codec: {a_codec}, duration: {a_dur:.3f} s")
print(f"  Timeline total: {tl['total']:.3f} s")
print(f"  Lệch Video vs Audio: {sync_delta:.4f} s (ngưỡng <= 0.05 s) -> {'PASS' if sync_delta <= 0.05 else 'FAIL'}")
print(f"  Lệch Video vs Timeline: {tl_delta:.4f} s (ngưỡng <= 0.05 s) -> {'PASS' if tl_delta <= 0.05 else 'FAIL'}")
results["sync_delta"] = sync_delta <= 0.05
results["tl_delta"] = tl_delta <= 0.05
results["resolution"] = (w, h) == (1920, 1080)

# 3. Decode Integrity Check
print("\n--- 3. GIẢI MÃ TOÀN BỘ VIDEO (0 DECODE ERRORS) ---")
cmd_dec = [str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"]
r_dec = subprocess.run(cmd_dec, capture_output=True, text=True)
errs = [l for l in r_dec.stderr.splitlines() if l.strip()]
print(f"  Số lỗi decode: {len(errs)}")
results["decode_errors"] = len(errs) == 0

# 4. Audio Loudness & Peak Check (ebur128)
print("\n--- 4. ĐO ÂM LƯỢNG VÀ TRUE PEAK (EBUR128) ---")
cmd_loud = [
    str(FF), "-i", str(MP4), "-af", "ebur128=peak=true", "-f", "null", "-"
]
r_loud = subprocess.run(cmd_loud, capture_output=True, text=True, encoding="utf-8", errors="replace")
stderr_loud = r_loud.stderr

i_lufs, tp_dbfs, lra = None, None, None
m_i = re.search(r"Integrated loudness:\s+I:\s+([-\d.]+)\s+LUFS", stderr_loud)
if m_i:
    i_lufs = float(m_i.group(1))
m_tp = re.search(r"True peak:\s+Peak:\s+([-\d.]+)\s+dBFS", stderr_loud)
if m_tp:
    tp_dbfs = float(m_tp.group(1))
m_lra = re.search(r"LRA:\s+([-\d.]+)\s+LU", stderr_loud)
if m_lra:
    lra = float(m_lra.group(1))

print(f"  Integrated Loudness: {i_lufs} LUFS (chuẩn -16 ± 1 LUFS) -> {'PASS' if i_lufs and -17.0 <= i_lufs <= -15.0 else 'FAIL'}")
print(f"  True Peak: {tp_dbfs} dBFS (chuẩn <= -1.5 dBFS) -> {'PASS' if tp_dbfs and tp_dbfs <= -1.5 else 'FAIL'}")
print(f"  LRA: {lra} LU")
results["lufs"] = i_lufs is not None and -17.0 <= i_lufs <= -15.0
results["tp"] = tp_dbfs is not None and tp_dbfs <= -1.5

# 5. Subtitle SRT Check
print("\n--- 5. KIỂM TRA PHỤ ĐỀ SRT ---")
srt_text = SRT.read_text(encoding="utf-8-sig")
cues = [c for c in srt_text.strip().split("\n\n") if c.strip()]
print(f"  Tổng số cues: {len(cues)}")
srt_end = 0
for c in cues:
    lines = c.splitlines()
    if len(lines) >= 2 and " --> " in lines[1]:
        end_ts = lines[1].split(" --> ")[1].strip()
        h, m, s = end_ts.split(":")
        s, ms = s.split(",")
        sec = int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
        srt_end = max(srt_end, sec)
print(f"  Cue cuối kết thúc lúc: {srt_end:.3f} s (trước kết thúc video {v_dur:.3f} s)")
results["srt_ok"] = len(cues) > 0 and srt_end <= v_dur + 0.1

# 6. Thumbnail Check
print("\n--- 6. KIỂM TRA THUMBNAIL ---")
from PIL import Image
with Image.open(THUMB) as tim:
    tw, th = tim.size
print(f"  Kích thước thumbnail: {tw}x{th} -> {'PASS' if (tw, th) == (1280, 720) else 'FAIL'}")
results["thumb_ok"] = (tw, th) == (1280, 720)

# 7. Summary
all_pass = all(results.values())
print("\n==================================================")
print(f"TỔNG KẾT QC: {'TẤT CẢ ĐẠT CHUẨN (PASS)' if all_pass else 'CÓ LỖI (FAIL)'}")
print("==================================================")
for k, v in results.items():
    print(f"  {k:20s}: {'PASS' if v else 'FAIL'}")

if not all_pass:
    sys.exit(1)
