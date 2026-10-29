#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC cuối — A9.1 (âm thanh) + A9.3 (hình) + A9.4 (file cuối) cho tập hiện hành (ED).

Chạy sau khi package.py --mux xong:
    py -3 .work/_qc_final_generic.py
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
OUT = ED.OUT_DIR
MP4 = OUT / (ED.MASTER + ".mp4")
WAV = ED.w("audio_master.wav")
QC = ED.w("qc_final")

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK  ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout, r.stderr, r.returncode


def dur(p):
    out, _, _ = run([str(FP), "-v", "error", "-show_entries", "format=duration",
                     "-of", "default=noprint_wrappers=1:nokey=1", str(p)])
    return float(out.strip())


# ---------------------------------------------------------------- A9.4
print("=== A9.4 file cuoi ===")
d_mp4, d_wav = dur(MP4), dur(WAV)
print(f"   mp4  = {d_mp4:.3f} s ({int(d_mp4 // 60)}:{d_mp4 % 60:05.2f})")
print(f"   wav  = {d_wav:.3f} s")
chk("Hinh va tieng cung thoi luong (±0,05 s)", abs(d_mp4 - d_wav) <= 0.05, f"lech {abs(d_mp4 - d_wav):.3f} s")

out, _, _ = run([str(FP), "-v", "error", "-select_streams", "v:0", "-show_entries",
                 "stream=width,height,r_frame_rate,nb_frames,codec_name", "-of", "default=noprint_wrappers=1", str(MP4)])
print("   " + out.replace("\n", " "))
chk("Video 1920x1080 @ 30 fps", "width=1920" in out and "height=1080" in out and "r_frame_rate=30/1" in out)
frames = int(re.search(r"nb_frames=(\d+)", out).group(1))
chk("So khung = so giay x 30", frames == round(d_mp4 * 30), f"{frames} khung")

print("   giai ma toan bo mp4 ...")
_, err, rc = run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"])
chk("Giai ma khong loi", rc == 0 and not err.strip(), err.strip()[:200])

# ---------------------------------------------------------------- A9.1
print("=== A9.1 am thanh ===")
_, err, _ = run([str(FF), "-i", str(WAV), "-af", "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"])
sil = re.findall(r"silence_start:\s*([\d.]+)", err)
chk("Khong co khoang cam tuyet doi > 0,3 s (V4)", not sil, f"{len(sil)} doan: {sil[:5]}")

_, err, _ = run([str(FF), "-i", str(WAV), "-af", "silencedetect=n=-35dB:d=2.5", "-f", "null", "-"])
sil2 = re.findall(r"silence_start:\s*([\d.]+)", err)
print(f"   doan im lap >= 2,5 s (chi duoc phep neu co chu dich): {len(sil2)} {sil2[:5]}")

_, err, _ = run([str(FF), "-i", str(WAV), "-af", "ebur128=peak=true", "-f", "null", "-"])
tail = [l for l in err.splitlines() if "I:" in l][-1].strip() if any("I:" in l for l in err.splitlines()) else ""
m = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", tail)
lufs = float(m.group(1)) if m else None
peak = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", tail)
print(f"   loudness: {tail}")
chk("Do lon trong khoang -16 ± 1 LUFS", lufs is not None and -17 <= lufs <= -15, f"{lufs} LUFS")
if peak:
    chk("Dinh ghe <= -1,5 dBFS", float(peak[-1]) <= -1.0, f"{peak[-1]} dBFS")

# loi dau
tl = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
first = tl["items"][0]["start"]
chk("Loi dau tien 22,8 – 23,5 s", 22.8 <= first <= 23.5, f"{first} s")

# ---------------------------------------------------------------- A9.3
print("=== A9.3 hinh: 1 khung giua moi shot lay tu chinh mp4 thanh pham ===")
sh = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))
shots = sh["shots"]
stills = ED.w("video3") / "stills_final"
stills.mkdir(parents=True, exist_ok=True)
QC.mkdir(parents=True, exist_ok=True)
for s in shots:
    mid = (s["start"] + s["end"]) / 2
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{mid:.3f}", "-i", str(MP4),
                    "-frames:v", "1", str(stills / f"{s['id']}.png")], check=True)
chk(f"Lay du {len(shots)} khung giua shot tu mp4", len(list(stills.glob("*.png"))) == len(shots))

from PIL import Image, ImageDraw, ImageFont  # noqa: E402
COLS, ROWS, TW, TH, PER = 4, 4, 480, 270, 16
try:
    fl = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 22)
except OSError:
    fl = ImageFont.load_default()
sheets = (len(shots) + PER - 1) // PER
for k in range(sheets):
    chunk = shots[k * PER:(k + 1) * PER]
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 30)), (14, 14, 17))
    d = ImageDraw.Draw(sheet)
    for i, s in enumerate(chunk):
        p = stills / f"{s['id']}.png"
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x, y = (i % COLS) * TW, (i // COLS) * (TH + 30)
        sheet.paste(im, (x, y))
        mid = (s["start"] + s["end"]) / 2
        d.text((x + 8, y + TH + 4), f"{s['id']} · {int(mid // 60)}:{mid % 60:05.2f} · {s['template']}",
               font=fl, fill=(242, 239, 233))
    sheet.save(QC / f"sheet_{k + 1:02d}.png")
print(f"   {sheets} contact sheet -> {QC}")

# ---------------------------------------------------------------- phu de
srt = (OUT / ED.SRT).read_text(encoding="utf-8")
cues = [b for b in re.split(r"\n\s*\n", srt.strip()) if b.strip()]
print(f"=== phu de: {len(cues)} cue ===")
bad = []
last = 0.0
for b in cues:
    L = b.splitlines()
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    a = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    if a < last:
        bad.append(L[0])
    if z <= a:
        bad.append(f"{L[0]} (ket thuc <= bat dau)")
    last = z
chk("Phu de khong co cue chong lap / vo trong", not bad, ", ".join(bad[:5]))
print(f"   cue cuoi ket thuc luc {last:.1f} s · video {d_mp4:.1f} s")

print()
print("TAT CA DA DAT" if ok else "CO VIEC CHUA XONG")
sys.exit(0 if ok else 1)
