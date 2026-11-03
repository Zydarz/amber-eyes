#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng H14 / A11 #55 — picture.mp4 phải khớp timeline.total ±0,05 s và thẻ kết phải lên hình.

Chạy sau khi build_video3.py xong, trước khi package.py --mux.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")

PIC = ED.w("video3") / "picture.mp4"
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))["shots"]
OUTDIR = ED.w("qc_h14")
OUTDIR.mkdir(parents=True, exist_ok=True)

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK  ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


def run(a):
    r = subprocess.run(a, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout, r.stderr, r.returncode


print("=== H14: picture.mp4 vs timeline ===")
out, _, _ = run([str(FP), "-v", "error", "-show_entries", "format=duration",
                  "-of", "default=noprint_wrappers=1:nokey=1", str(PIC)])
d = float(out.strip())
tot = TL["total"]
print(f"   picture.mp4 = {d:.3f} s · timeline.total = {tot:.3f} s · lệch {d - tot:+.3f} s")
chk("picture.mp4 khớp timeline.total ±0,05 s (H14)", abs(d - tot) <= 0.05, f"{d - tot:+.3f} s")

out, _, _ = run([str(FP), "-v", "error", "-select_streams", "v:0", "-show_entries",
                 "stream=width,height,r_frame_rate,nb_frames", "-of", "default=noprint_wrappers=1", str(PIC)])
print("   " + out.replace("\n", " "))
frames = int(re.search(r"nb_frames=(\d+)", out).group(1))
chk("1920x1080 @30 fps", "width=1920" in out and "height=1080" in out and "r_frame_rate=30/1" in out)
chk("Số khung = round(duration x 30)", frames == round(d * 30), f"{frames} khung vs {round(d*30)}")

print("=== A11 #55: thẻ kết — kiểm ở GIỮA shot cuối (không phải total−2 s: renderer mờ đen 3 s cuối) ===")
last = SH[-1]
mid_last = (last["start"] + last["end"]) / 2
p_mid = OUTDIR / "frame_endcard_mid.png"
run([str(FF), "-y", "-v", "error", "-ss", f"{mid_last:.3f}", "-i", str(PIC),
     "-frames:v", "1", str(p_mid)])
chk("Đã trích khung giữa shot cuối", p_mid.exists() and p_mid.stat().st_size > 10000,
    f"{p_mid.name} ({p_mid.stat().st_size if p_mid.exists() else 0} byte)")


def bright_ratio(path):
    from PIL import Image
    im = Image.open(path).convert("L")
    px = list(im.getdata())
    return 100.0 * sum(1 for v in px if v > 90) / len(px)


if p_mid.exists():
    br = bright_ratio(p_mid)
    print(f"   % pixel sáng ở giữa shot cuối: {br:.2f} %")
    chk("Thẻ kết có chữ trên hình (> 1 % pixel sáng)", br > 1.0, f"{br:.2f} %")
print(f"   shot cuoi = {last['id']} · {last['start']:.2f} → {last['end']:.2f} s · "
      f"nền={last['bg']} · vai={last['role']}")

p_tail = OUTDIR / "frame_total_minus_2s.png"
run([str(FF), "-y", "-v", "error", "-ss", f"{tot - 2:.3f}", "-i", str(PIC),
     "-frames:v", "1", str(p_tail)])
if p_tail.exists():
    print(f"   (tham khảo) % pixel sáng tại total−2 s: {bright_ratio(p_tail):.2f} % "
          f"— renderer mờ dần 3 s cuối (dùng chung T01–T03)")

print("=== thẻ kết: shot cuoi phải có chữ (H12) ===")
lastshot = SH[-1]
segs = lastshot.get("segments") or []
txt = " ".join(e[1] for s in segs for e in s["elems"])
print(f"   chữ shot cuối: {txt[:120]}")
chk("Cột Chữ shot cuối không rỗng (H12)", bool(txt.strip()))
chk("Có nhãn HỒ SƠ TẬP 07 + AMBER EYES", "HỒ SƠ TẬP 07" in txt and "AMBER EYES" in txt)

print()
print("TẤT CẢ ĐẠT" if ok else "CÓ LỖI")
sys.exit(0 if ok else 1)
