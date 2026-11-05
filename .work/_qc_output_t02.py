import subprocess
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path("D:/TEST/Gax/amber-eyes")
FF = ROOT / ".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
PROBE = ROOT / ".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
MP4 = ROOT / "02_SAN_XUAT/Tap02/xuat_ban/Tap02_master.mp4"
TL = ROOT / ".work/timeline_s_t02.json"
SRT = ROOT / "02_SAN_XUAT/Tap02/xuat_ban/Tap02.srt"

print(f"=== QC BẮT BUỘC ĐẦU RA CHO {MP4.name} ===")

# 1. Stream probes
cmd = [
    str(PROBE), "-v", "error",
    "-show_entries", "format=duration,size,bit_rate",
    "-show_entries", "stream=index,codec_name,codec_type,width,height,r_frame_rate,duration,nb_frames",
    "-of", "json", str(MP4)
]
probe_data = json.loads(subprocess.run(cmd, capture_output=True, text=True, check=True).stdout)

v_stream = next(s for s in probe_data["streams"] if s["codec_type"] == "video")
a_stream = next(s for s in probe_data["streams"] if s["codec_type"] == "audio")
fmt = probe_data["format"]

v_dur = float(v_stream.get("duration", fmt["duration"]))
a_dur = float(a_stream.get("duration", fmt["duration"]))
fmt_dur = float(fmt["duration"])
diff = abs(v_dur - a_dur)

print(f"\n1. THÔNG SỐ STREAM:")
print(f"  - Kích thước file: {int(fmt['size']) / 1024 / 1024:.2f} MB")
print(f"  - Video codec: {v_stream['codec_name']}, {v_stream['width']}x{v_stream['height']} @ {v_stream['r_frame_rate']} fps")
print(f"  - Tổng số frames: {v_stream.get('nb_frames')}")
print(f"  - Audio codec: {a_stream['codec_name']}")
print(f"  - Thời lượng Video: {v_dur:.3f} s")
print(f"  - Thời lượng Audio: {a_dur:.3f} s")
print(f"  - Độ lệch hình / tiếng: {diff*1000:.1f} ms ({diff:.4f} s) — Ngưỡng H14: <= 50 ms (0.05 s) -> {'ĐẠT (OK)' if diff <= 0.05 else 'KHÔNG ĐẠT (FAIL)'}")

# 2. Decode integrity check (0 errors)
print("\n2. KIỂM TRA LỖI GIẢI MÃ TOÀN BỘ MP4 (DECODE CHECK):")
decode_cmd = [str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"]
res_dec = subprocess.run(decode_cmd, capture_output=True, text=True)
err_lines = [l for l in res_dec.stderr.splitlines() if l.strip()]
print(f"  - Lỗi giải mã: {len(err_lines)} lỗi -> {'ĐẠT (OK)' if len(err_lines) == 0 else 'CẢNH BÁO'}")
if err_lines:
    for e in err_lines[:5]:
        print(f"    ! {e}")

# 3. Audio loudness & True Peak check
print("\n3. ĐO ĐỘ LỚN ÂM THANH (EBU R128 TRÊN CHÍNH MP4):")
loud_cmd = [str(FF), "-i", str(MP4), "-af", "ebur128=framelog=verbose", "-f", "null", "-"]
p_loud = subprocess.run(loud_cmd, capture_output=True, text=True, errors="ignore")
lines = p_loud.stderr.splitlines()
summary = []
rec = False
for l in lines:
    if "Summary:" in l:
        rec = True
    if rec:
        summary.append(l)

integrated = None
true_peak = None
lra = None
for l in summary:
    if "I:" in l and "LUFS" in l:
        m = re.search(r"I:\s+([-\d.]+)\s+LUFS", l)
        if m: integrated = float(m.group(1))
    if "Peak:" in l and "dBFS" in l:
        m = re.search(r"Peak:\s+([-\d.]+)\s+dBFS", l)
        if m: true_peak = float(m.group(1))
    if "LRA:" in l and "LU" in l:
        m = re.search(r"LRA:\s+([-\d.]+)\s+LU", l)
        if m: lra = float(m.group(1))

print(f"  - Integrated Loudness: {integrated} LUFS (Tiêu chuẩn: -16 ± 1 LUFS) -> {'ĐẠT (OK)' if integrated and abs(integrated - (-16.0)) <= 1.0 else 'CẢNH BÁO'}")
print(f"  - True Peak (Sample Peak): {true_peak} dBFS (Tiêu chuẩn: <= -1.5 dBFS) -> {'ĐẠT (OK)' if true_peak and true_peak <= -1.5 else 'CẢNH BÁO'}")
print(f"  - Loudness Range (LRA): {lra} LU")

# 4. Check silence > 0.3s
print("\n4. KIỂM TRA KHOẢNG LẶNG (V4: KHÔNG IM LẶNG TUYỆT ĐỐI > 0.3s @ -60dB):")
sil_cmd = [str(FF), "-i", str(MP4), "-af", "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"]
p_sil = subprocess.run(sil_cmd, capture_output=True, text=True, errors="ignore")
sil_matches = re.findall(r"silence_duration:\s+([\d.]+)", p_sil.stderr)
print(f"  - Số khoảng lặng > 0.3s phát hiện: {len(sil_matches)} -> {'ĐẠT (OK)' if len(sil_matches) == 0 else 'CẢNH BÁO'}")
if sil_matches:
    print(f"    Khoảng lặng: {sil_matches[:5]}")

# 5. Subtitle & Timeline parity
tl_data = json.loads(TL.read_text(encoding="utf-8"))
srt_content = SRT.read_text(encoding="utf-8")
cue_count = len(re.findall(r"\d+\r?\n\d\d:\d\d:\d\d", srt_content))
print("\n5. KIỂM TRA PHỤ ĐỀ (SUBTITLES & TIMELINE):")
print(f"  - Số câu kịch bản: {len(tl_data['items'])} câu")
print(f"  - Số cue phụ đề SRT: {cue_count} cue")
print(f"  - Cue đầu tiên: {tl_data['items'][0]['start']:.2f}s -> {tl_data['items'][0]['text'][:40]}...")
print(f"  - Cue cuối cùng: {tl_data['items'][-1]['end']:.2f}s -> {tl_data['items'][-1]['text'][:40]}...")

# 6. Check faststart
print("\n6. KIỂM TRA FASTSTART (MOOV ATOM AT BEGINNING):")
with open(MP4, "rb") as f:
    header = f.read(1024)
    moov_pos = header.find(b"moov")
    print(f"  - 'moov' atom tìm thấy trong 1KB đầu: {moov_pos != -1} -> {'ĐẠT (OK)' if moov_pos != -1 else 'KHÔNG ĐẠT'}")

print("\n=== HOÀN TẤT ĐO ĐẠC QC ===")
