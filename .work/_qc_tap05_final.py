import subprocess, json, sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

FF = Path(".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe")
FP = Path(".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe")
mp4 = Path("02_SAN_XUAT/Tap05/xuat_ban/Tap05_master.mp4")

# 1. File size
size_mb = mp4.stat().st_size / (1024 * 1024)
print(f"Kích thước file: {size_mb:.2f} MB")

# 2. Probe streams
r_probe = subprocess.run([
    str(FP), "-v", "error", "-show_entries",
    "format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate,duration,nb_frames",
    "-of", "json", str(mp4)
], capture_output=True, text=True, encoding="utf-8")

info = json.loads(r_probe.stdout)
fmt = info.get("format", {})
streams = info.get("streams", [])

print(f"Tổng thời lượng container: {float(fmt.get('duration', 0)):.3f} s")
print(f"Bitrate: {int(fmt.get('bit_rate', 0))/1000:.1f} kbps")

for s in streams:
    kind = s.get("codec_name")
    if s.get("width"):
        print(f"Video Stream: {kind} {s.get('width')}x{s.get('height')} @ {s.get('r_frame_rate')} fps, duration={float(s.get('duration', 0)):.3f} s, frames={s.get('nb_frames')}")
    else:
        print(f"Audio Stream: {kind}, duration={float(s.get('duration', 0)):.3f} s")

# 3. Check video/audio sync (|v_dur - a_dur| <= 0.05s)
v_stream = next((s for s in streams if s.get("width")), None)
a_stream = next((s for s in streams if not s.get("width")), None)
if v_stream and a_stream:
    v_dur = float(v_stream.get("duration", 0))
    a_dur = float(a_stream.get("duration", 0))
    diff = abs(v_dur - a_dur)
    print(f"Lệch hình / tiếng: {diff:.4f} s (Chuẩn <= 0.05 s -> {'ĐẠT' if diff <= 0.05 else 'LỆCH!'})")

# 4. Check decoder errors (ffmpeg -v error -i ... -f null -)
print("\nĐang kiểm tra lỗi giải mã toàn bộ video...")
r_err = subprocess.run([str(FF), "-v", "error", "-i", str(mp4), "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8")
err_lines = r_err.stderr.strip().splitlines() if r_err.stderr.strip() else []
print(f"Số lỗi giải mã: {len(err_lines)} -> {'ĐẠT 100%' if len(err_lines) == 0 else 'CÓ LỖI'}")
if err_lines:
    for l in err_lines[:5]:
        print(" ", l)
