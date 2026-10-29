import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

bin_dir = Path(".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin")
ffmpeg_exe = str(bin_dir / "ffmpeg.exe")
ffprobe_exe = str(bin_dir / "ffprobe.exe")

video_path = r"02_SAN_XUAT\Tap06\xuat_ban\Tap06_master.mp4"
audio_path = r".work\audio_master_t06.wav"

print(f"=== KIỂM ĐỊNH THÀNH PHẨM MASTER TẬP 06 ===")
print(f"File video : {video_path}")
print(f"Kích thước : {os.path.getsize(video_path):,} bytes ({os.path.getsize(video_path)/1024/1024:.2f} MB)")

# 1. FFprobe video duration & streams
probe_cmd = [
    ffprobe_exe, "-v", "quiet", "-print_format", "json",
    "-show_format", "-show_streams", video_path
]
res = subprocess.run(probe_cmd, capture_output=True, text=True)
data = json.loads(res.stdout)

video_stream = next(s for s in data['streams'] if s['codec_type'] == 'video')
audio_stream = next(s for s in data['streams'] if s['codec_type'] == 'audio')

v_dur = float(video_stream['duration'])
a_dur = float(audio_stream['duration'])
format_dur = float(data['format']['duration'])

diff = abs(v_dur - a_dur)
print(f"\n1. ĐO ĐẠC THỜI LƯỢNG:")
print(f"  - Video stream duration : {v_dur:.3f} s")
print(f"  - Audio stream duration : {a_dur:.3f} s")
print(f"  - Format duration       : {format_dur:.3f} s")
print(f"  - Độ phân giải          : {video_stream['width']}x{video_stream['height']} @ {video_stream['r_frame_rate']} fps")
print(f"  - Codec Video / Audio   : {video_stream['codec_name']} / {audio_stream['codec_name']}")
print(f"  - Độ lệch Hình - Tiếng  : {diff:.4f} s (Quy tắc Bước 10: <= 0.05 s) -> {'ĐẠT CHUẨN XUẤT SẮC' if diff <= 0.05 else 'KHÔNG ĐẠT'}")

# 2. Decode test for 0 errors
print(f"\n2. KIỂM TRA GIẢI MÃ TOÀN BỘ FILE (0 LỖI):")
decode_cmd = [ffmpeg_exe, "-v", "error", "-i", video_path, "-f", "null", "-"]
decode_res = subprocess.run(decode_cmd, capture_output=True, text=True)
err = decode_res.stderr.strip()
if not err:
    print("  - Giải mã hoàn toàn sạch: 0 LỖI (Zero decoding errors) -> ĐẠT CHUẨN!")
else:
    print(f"  - Lỗi giải mã: {err}")

# 3. Check chapters
chapters = data.get('chapters', [])
print(f"\n3. CÁC HỒI / CHAPTERS:")
for ch in chapters:
    t_start = float(ch['start_time'])
    t_end = float(ch['end_time'])
    title = ch.get('tags', {}).get('title', 'Unknown')
    print(f"  - [{t_start/60:02.0f}:{t_start%60:02.0f} -> {t_end/60:02.0f}:{t_end%60:02.0f}] {title}")

# 4. Check thumbnail and srt
srt_path = r"02_SAN_XUAT\Tap06\xuat_ban\Tap06.srt"
thumb_path = r"02_SAN_XUAT\Tap06\xuat_ban\thumbnail.png"
print(f"\n4. TÀI SẢN PHÁT HÀNH ĐI KÈM:")
print(f"  - Phụ đề SRT  : {os.path.exists(srt_path)} ({os.path.getsize(srt_path):,} bytes)")
print(f"  - Thumbnail   : {os.path.exists(thumb_path)} ({os.path.getsize(thumb_path):,} bytes)")

