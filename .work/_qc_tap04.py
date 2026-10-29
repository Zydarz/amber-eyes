import json
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap04" / "xuat_ban"

mp4 = OUT_DIR / "Tap04_master.mp4"
mp3 = OUT_DIR / "Tap04_master.mp3"
srt = OUT_DIR / "Tap04.srt"
thumb = OUT_DIR / "thumbnail.png"
desc = OUT_DIR / "mo_ta.txt"

print(f"=== 1. KIỂM TRA SỰ TỒN TẠI VÀ DUNG LƯỢNG ===")
for p in [mp4, mp3, srt, thumb, desc]:
    if p.exists():
        print(f"  [OK] {p.name:<18} : {p.stat().st_size / (1024*1024):.2f} MB ({p.stat().st_size:,} bytes)")
    else:
        print(f"  [MISSING] {p.name}")

print(f"\n=== 2. KIỂM TRA ĐỒNG BỘ HÌNH - TIẾNG (FFPROBE) ===")
cmd = [str(FFPROBE), "-v", "error", "-show_entries", "stream=codec_type,codec_name,duration,width,height,r_frame_rate",
       "-of", "json", str(mp4)]
r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
info = json.loads(r.stdout)

v_dur = a_dur = None
for s in info["streams"]:
    t = s["codec_type"]
    c = s["codec_name"]
    d = float(s.get("duration", 0))
    if t == "video":
        v_dur = d
        w, h = s["width"], s["height"]
        fps = eval(s["r_frame_rate"])
        print(f"  Video stream : {c} | {w}x{h} | {fps:.2f} fps | {d:.3f} s")
    elif t == "audio":
        a_dur = d
        print(f"  Audio stream : {c} | {d:.3f} s")

if v_dur is not None and a_dur is not None:
    diff = abs(v_dur - a_dur)
    print(f"  Chênh lệch |v - a| : {diff:.4f} s (yêu cầu <= 0.05 s) -> {'ĐẠT CHUẨN' if diff <= 0.05 else 'CẢNH BÁO'}")

print(f"\n=== 3. QUÉT GIẢI MÃ TOÀN BỘ VIDEO (0 LỖI) ===")
cmd_dec = [str(FF), "-v", "error", "-i", str(mp4), "-f", "null", "-"]
r_dec = subprocess.run(cmd_dec, capture_output=True, text=True, encoding="utf-8")
errs = r_dec.stderr.strip()
if not errs:
    print("  PASS: Quét toàn bộ video 100% không phát hiện bất kỳ lỗi giải mã nào (0 decode errors)!")
else:
    print(f"  Lỗi decode: {errs}")

print(f"\n=== 4. THÔNG TIN PHỤ ĐỀ ===")
srt_text = srt.read_text(encoding="utf-8")
cues = [c for c in srt_text.strip().split("\n\n") if c.strip()]
print(f"  Tổng số cue phụ đề : {len(cues)}")
print(f"  Cue đầu : {cues[0].splitlines()[1:]}")
print(f"  Cue cuối: {cues[-1].splitlines()[1:]}")
