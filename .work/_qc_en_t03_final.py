#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng kiểm cuối cho bản tiếng Anh Tập 03 (chạy SAU khi package.py --mux).

Bổ sung cho _qc_final_generic.py: kiểm thẻ kết ở timeline.total-2 s (H14),
đo lại loudness/peak TRÊN CHÍNH mp4 cuối (A7/A11 #38), đối chiếu SRT với
timeline, và soi nhãn vai trong phụ đề.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
os_env = {"AE_EP": "03", "AE_LANG": "en"}
import os  # noqa: E402
os.environ.update(os_env)
import edition as ED  # noqa: E402

FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
MP4 = ED.OUT_DIR / (ED.MASTER + ".mp4")
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
TOTAL = TL["total"]
QC = W / "qc_final_EN_t03"
QC.mkdir(parents=True, exist_ok=True)

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK  ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


def run(args):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")


print("=== file cuoi ===")
out = run([str(FP), "-v", "error", "-show_entries", "format=duration",
           "-of", "default=nw=1:nk=1", str(MP4)]).stdout.strip()
d = float(out)
print(f"   mp4 = {d:.3f} s ({int(d // 60)}:{d % 60:05.2f})   timeline.total = {TOTAL:.3f} s")
chk("Do dai mp4 == timeline.total (±0,05 s)", abs(d - TOTAL) <= 0.05, f"lech {d - TOTAL:+.3f} s")

out = run([str(FP), "-v", "error", "-select_streams", "v:0", "-show_entries",
           "stream=width,height,r_frame_rate,nb_frames,codec_name", "-of", "default=nw=1", str(MP4)]).stdout
print("   " + out.replace("\n", " "))
chk("Video 1920x1080 @30 fps", "width=1920" in out and "height=1080" in out and "r_frame_rate=30/1" in out)
nf = int(re.search(r"nb_frames=(\d+)", out).group(1))
# renderer dung int(t*FPS) => LAM CHAN, khong phai round (build_video3.py: f0,f1 = int(a.t0*FPS), int(a.t1*FPS))
exp_nf = int(TOTAL * 30)
chk("So khung == int(total*30) (khung cuoi cua timeline)", nf == exp_nf, f"{nf} khung (mong doi {exp_nf})")

out = run([str(FP), "-v", "error", "-show_entries", "stream=codec_type,codec_name",
           "-of", "default=nw=1", str(MP4)]).stdout
print("   " + out.replace("\n", " "))
chk("Co 1 video + 1 audio", out.count("video") == 1 and out.count("audio") == 1)

print("=== giai ma toan bo ===")
r = run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"])
chk("Giai ma khong loi", r.returncode == 0 and not r.stderr.strip(), r.stderr.strip()[:300])

print("=== am thanh tren CHINH mp4 cuoi (A7) ===")
r = run([str(FF), "-i", str(MP4), "-af", "ebur128=peak=true", "-f", "null", "-"])
sum_txt = r.stderr.split("Summary:")[-1] if "Summary:" in r.stderr else r.stderr
tail = [l for l in sum_txt.splitlines() if "I:" in l][-1].strip() if any("I:" in l for l in sum_txt.splitlines()) else ""
m = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", tail)
lufs = float(m.group(1)) if m else None
peak = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", sum_txt)
lra = re.findall(r"LRA:\s*(-?[\d.]+)\s*LU", sum_txt)
print("   " + tail)
chk("Loudness -16 ± 1 LUFS tren mp4", lufs is not None and -17 <= lufs <= -15, f"{lufs} LUFS")
if peak:
    chk("True peak <= -1,5 dBFS tren mp4", float(peak[-1]) <= -1.5, f"{peak[-1]} dBFS")
else:
    chk("True peak <= -1,5 dBFS tren mp4", False, "khong doc duoc True Peak tu ebur128")
if lra:
    print(f"   LRA = {lra[-1]} LU")

r = run([str(FF), "-i", str(MP4), "-af", "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"])
sil = re.findall(r"silence_start:\s*([\d.]+)", r.stderr)
chk("Khong co khoang cam tuyet doi > 0,3 s (V4)", not sil, f"{len(sil)} doan {sil[:5]}")

print("=== the ket (H14) ===")
for label, t in (("end_minus2", TOTAL - 2.0), ("end_minus5", TOTAL - 5.0), ("intro_1s", 1.0)):
    p = QC / f"{label}.png"
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(MP4),
                    "-frames:v", "1", str(p)], check=True)
    print(f"   trich khung {t:.2f} s -> {p}")
chk("Da trich duoc khung the ket", (QC / "end_minus2.png").exists())

print("=== phu de ===")
srt = (ED.OUT_DIR / ED.SRT).read_text(encoding="utf-8")
blocks = [b for b in re.split(r"\n\s*\n", srt.strip()) if b.strip()]
last = 0.0
bad = []
tags = set()
for b in blocks:
    L = b.splitlines()
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    a = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    if a < last:
        bad.append(L[0])
    if z <= a:
        bad.append(f"{L[0]} (ket <= bat dau)")
    last = z
    for t in re.findall(r"\[([^\]]+)\]", "\n".join(L[2:])):
        tags.add(t)
chk("Khong co cue chong lap / vo trong", not bad, ", ".join(bad[:5]))
print(f"   {len(blocks)} cue · cue cuoi {last:.1f} s · video {d:.1f} s")
print(f"   nhan vai trong phu de: {sorted(tags)}")
chk("Nhan vai dung Tap03 (khong phai Tap01)", "SPRINGFIELD RESIDENT" not in tags and "RESIDENT" not in tags,
    f"{sorted(tags)}")

print()
print("TAT CA DA DAT" if ok else "CO VIEC CHUA XONG")
sys.exit(0 if ok else 1)
