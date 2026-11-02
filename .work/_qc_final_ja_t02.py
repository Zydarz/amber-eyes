#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC CUOI bản JA Tap02 (A9.1 am thanh · A9.2 chu · A9.4 file cuoi · H13 khop 3 chieu).

Chay sau khi package.py --mux xong.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"

OUT = ROOT / "02_SAN_XUAT" / "Tap02_JA" / "xuat_ban"
WAV = W / "audio_master_JA_t02.wav"
MP4 = OUT / "Tap02_JA_master.mp4"
MP3 = OUT / "Tap02_JA_master.mp3"
SRT = OUT / "Tap02_JA.srt"
THUMB = OUT / "thumbnail.png"
PIC = W / "video3_JA_t02" / "picture.mp4"

tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
total = tl["total"]
fails = []


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def dur(p):
    r = run([str(FF), "-i", str(p)])
    for line in (r.stderr or "").splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return None


print("=" * 72)
print("A9.1  ÂM THANH")
print("=" * 72)
if WAV.exists():
    r = run([str(FF), "-i", str(WAV), "-af", "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"])
    sil = re.findall(r"silence_start: ([\d.]+)", r.stderr or "")
    print(f"  doan im lap > 0,3 s (nen -60 dB): {len(sil)}  {sil[:8]}")
    if sil:
        fails.append(f"A9.1: {len(sil)} doan im > 0.3s")
    r = run([str(FF), "-i", str(WAV), "-af", "ebur128=peak=true", "-f", "null", "-"])
    i = (r.stderr or "").rfind("I:")
    tail = (r.stderr or "")[-700:]
    m = re.findall(r"I:\s*(-?[\d.]+) LUFS", tail)
    pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", tail)
    print(f"  LUFS  = {m[-1] if m else '?'}  (chuan -16 ± 1)")
    print(f"  Peak  = {pk[-1] if pk else '?'} dBFS  (tran <= -1,5)")
    if m and not (-17.0 <= float(m[-1]) <= -15.0):
        fails.append(f"A9.1: LUFS {m[-1]} ngoai -16±1")
    if pk and float(pk[-1]) > -1.5:
        fails.append(f"A9.1: peak {pk[-1]} > -1.5 dBFS")
else:
    fails.append("A9.1: thieu audio_master_JA_t02.wav")

dmp3 = dur(MP3) if MP3.exists() else None
print(f"  master mp3 = {dmp3} s (timeline {total:.2f} s)")
if dmp3 and abs(dmp3 - total) > 0.05:
    fails.append(f"A9.1: mp3 {dmp3} lech timeline {total:.2f}")

print()
print("=" * 72)
print("A9.2  CHU + PHAU DE")
print("=" * 72)
sent = {it["id"]: it for it in tl["items"]}
allids = [it["id"] for it in tl["items"]]
cov = []
for s in shots:
    cov += s["sentences"]
miss = [i for i in allids if i not in cov]
extra = [c for c in cov if c not in allids]
dup = [c for c in set(cov) if cov.count(c) > 1]
print(f"  phu cau: {len(cov)}/{len(allids)} · thieu {len(miss)} · thua {len(extra)} · trung {len(dup)}")
if miss or extra or dup:
    fails.append(f"A9.2: phu cau sai ({len(miss)}/{len(extra)}/{len(dup)})")

txt = SRT.read_bytes().decode("utf-8-sig", errors="replace").replace("\r\n", "\n")
blocks = [b for b in txt.strip().split("\n\n") if b.strip()]


def sec(ts):
    h, m, s = ts.split(":")
    s, ms = s.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


bad = [i for i, b in enumerate(blocks, 1) if len(b.splitlines()) < 3 or " --> " not in b.splitlines()[1]]
blank = [i for i, b in enumerate(blocks, 1) if any(x.strip() == "" for x in b.splitlines()[2:])]
last = sec(blocks[-1].splitlines()[1].split(" --> ")[1])
print(f"  SRT: {len(blocks)} cue · khoi lo {len(bad)} · dong trong {len(blank)} · het {last:.2f}s")
if bad or blank:
    fails.append(f"A9.2: SRT co {len(bad)} khoi lo / {len(blank)} dong trong")
if last > total + 0.05:
    fails.append(f"A9.2: SRT vuot timeline ({last} > {total})")

# font coverage
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

FONTS = Path(r"C:\Windows\Fonts")
allchars = set()
for s in shots:
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            allchars |= set(v)
allchars |= set("AMBER EYES 実際の事件記録から読み解く犯罪心理学 ホスト 捜査官 心理学者 証人 一般人 関係者 住民")


def rmask(f, ch):
    im = Image.new("L", (f.size * 2 + 20, f.size * 2 + 20), 0)
    ImageDraw.Draw(im).text((10, 10), ch, font=f, fill=255)
    return im.tobytes()


for fname in ["YuGothB.ttc", "YuGothM.ttc"]:
    f = ImageFont.truetype(str(FONTS / fname), 40)
    ref = rmask(f, "\uffff")
    ms = sorted({c for c in allchars if c not in " \n\t" and rmask(f, c) == ref})
    print(f"  font {fname}: thieu {len(ms)} ky tu {ms[:6]}")
    if ms:
        fails.append(f"A9.2: font {fname} thieu {len(ms)} ky tu")

print()
print("=" * 72)
print("A9.4  FILE CUOI")
print("=" * 72)
if not MP4.exists():
    fails.append("A9.4: thieu Tap02_JA_master.mp4")
else:
    d = dur(MP4)
    print(f"  mp4 = {d} s · timeline = {total:.2f} s · lech = {abs(d-total):.3f} s (cho phep ±0,05)")
    if abs(d - total) > 0.05:
        fails.append(f"A9.4: mp4 lech {abs(d-total):.3f}s")
    r = run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"])
    errs = [x for x in (r.stderr or "").splitlines() if x.strip()]
    print(f"  giai ma: {len(errs)} loi {errs[:4]}")
    if errs:
        fails.append(f"A9.4: giai ma {len(errs)} loi")
    r = run([str(FF), "-i", str(MP4)])
    for line in (r.stderr or "").splitlines():
        if "Stream #" in line:
            print("   ", line.strip()[:120])
    # LUFS tren chinh mp4 cuoi
    r = run([str(FF), "-i", str(MP4), "-af", "ebur128=peak=true", "-f", "null", "-"])
    tail = (r.stderr or "")[-700:]
    m = re.findall(r"I:\s*(-?[\d.]+) LUFS", tail)
    pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", tail)
    print(f"  mp4 LUFS = {m[-1] if m else '?'} (chuan -16 ± 1) · Peak = {pk[-1] if pk else '?'} dBFS")
    if m and not (-17.0 <= float(m[-1]) <= -15.0):
        fails.append(f"A9.4: mp4 LUFS {m[-1]}")
    if pk and float(pk[-1]) > -1.0:
        fails.append(f"A9.4: mp4 peak {pk[-1]} > -1.0 dBFS")

print()
print("=" * 72)
print("THE KET (A11 #55) — trich khung tai total-2s")
print("=" * 72)
lastshot = shots[-1]
print(f"  shot cuoi = {lastshot['id']} · {lastshot['start']:.2f} -> {lastshot['end']:.2f}")
tshot = lastshot["start"] + 2
print(f"  trich khung tai {tshot:.2f} s (nen thay the AMBER EYES)")
still = W / "_cu" / "ja_t02_zoom" / "final_card.png"
still.parent.mkdir(parents=True, exist_ok=True)
r = subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{tshot:.3f}", "-i", str(PIC),
                    "-frames:v", "1", str(still)], capture_output=True, text=True)
print(f"  -> {still} (rc={r.returncode})")

print()
print("=" * 72)
if fails:
    print(f"KET QUA: FAIL ({len(fails)})")
    for f in fails:
        print("  -", f)
else:
    print("KET QUA: PASS — tat ca cong do dat")
print("=" * 72)
