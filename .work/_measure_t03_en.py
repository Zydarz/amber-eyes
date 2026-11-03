#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do TAT CA so do cho bao cao QC ban tieng Anh Tap 03 — tu thang pham mp4 cuoi.

Chay sau khi package.py --mux xong.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
os.environ.update({"AE_EP": "03", "AE_LANG": "en"})
import edition as ED  # noqa: E402

FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FFMPEG, FFPROBE = FF / "ffmpeg.exe", FF / "ffprobe.exe"
MP4 = ED.OUT_DIR / (ED.MASTER + ".mp4")
WAV = W / "audio_master_EN_t03.wav"
TL = json.loads((W / "timeline_s_EN_t03.json").read_text(encoding="utf-8"))
SHOTS = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["shots"]
M = {}


def run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", **kw)


def dur(p):
    return float(run([str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
                      "-of", "default=nw=1:nk=1", str(p)]).stdout.strip())


d_mp4 = dur(MP4)
d_wav = dur(WAV)
M["mp4_duration"] = d_mp4
M["wav_duration"] = d_wav
M["timeline_total"] = TL["total"]
M["size_mb"] = MP4.stat().st_size / 1e6

out = run([str(FFPROBE), "-v", "error", "-select_streams", "v:0", "-show_entries",
           "stream=width,height,r_frame_rate,nb_frames,codec_name,bit_rate",
           "-of", "default=nw=1", str(MP4)]).stdout
M["video_stream"] = dict(l.split("=", 1) for l in out.splitlines() if "=" in l)
out = run([str(FFPROBE), "-v", "error", "-select_streams", "a:0", "-show_entries",
           "stream=codec_name,sample_rate,channels,bit_rate", "-of", "default=nw=1", str(MP4)]).stdout
M["audio_stream"] = dict(l.split("=", 1) for l in out.splitlines() if "=" in l)

# ---- am thanh tren chinh mp4 cuoi
r = run([str(FFMPEG), "-i", str(MP4), "-af", "ebur128=peak=true", "-f", "null", "-"])
# ebur128 in "Summary:" o CUOI; phai lay ca khoi summary de lay True Peak + LRA
sum_txt = r.stderr.split("Summary:")[-1] if "Summary:" in r.stderr else r.stderr
tail = [l for l in sum_txt.splitlines() if "I:" in l][-1].strip() if any("I:" in l for l in sum_txt.splitlines()) else ""
M["ebur_tail"] = tail
M["ebur_summary"] = "\n".join(l.strip() for l in sum_txt.splitlines() if l.strip())[-800:]
m = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", tail)
M["lufs"] = float(m.group(1)) if m else None
pk = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", sum_txt)
M["peak"] = float(pk[-1]) if pk else None
lr = re.findall(r"LRA:\s*(-?[\d.]+)\s*LU", sum_txt)
M["lra"] = float(lr[-1]) if lr else None
print("   ebur128 summary:", M["ebur_summary"].replace("\n", " | "))

r = run([str(FFMPEG), "-i", str(MP4), "-af", "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"])
M["sil60"] = re.findall(r"silence_start:\s*([\d.]+)", r.stderr)
r = run([str(FFMPEG), "-i", str(MP4), "-af", "silencedetect=n=-35dB:d=2.5", "-f", "null", "-"])
M["sil35"] = re.findall(r"silence_start:\s*([\d.]+)", r.stderr)

# ---- loi dau / loi cuoi (do truc tiep tren mp4)
r = run([str(FFMPEG), "-i", str(MP4), "-af", "silencedetect=n=-45dB:d=0.15", "-f", "null", "-"])
starts = [float(x) for x in re.findall(r"silence_start:\s*([\d.]+)", r.stderr)]
M["first_speech"] = min(starts) if starts else None
M["last_silence_start"] = max(starts) if starts else None

# ---- giai ma toan bo
r = run([str(FFMPEG), "-v", "error", "-i", str(MP4), "-f", "null", "-"])
M["decode_errors"] = r.stderr.strip()

# ---- the ket: do do sang pixel o cac moc thoi gian
import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402

QC = W / "qc_final_EN_t03"
QC.mkdir(exist_ok=True)
card = {}
for label, t in (("end_minus2", TL["total"] - 2.0), ("end_minus5", TL["total"] - 5.0),
                 ("mid_last_shot", (SHOTS[-1]["start"] + SHOTS[-1]["end"]) / 2)):
    p = QC / f"{label}.png"
    subprocess.run([str(FFMPEG), "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(MP4),
                    "-frames:v", "1", str(p)], check=True)
    im = np.asarray(Image.open(p).convert("L"), dtype=np.float32)
    card[label] = {"t": round(t, 2), "pct_bright": round(float((im > 90).mean()) * 100, 2),
                    "mean": round(float(im.mean()), 1)}
M["end_card"] = card

# ---- phu de
srt = (ED.OUT_DIR / ED.SRT).read_text(encoding="utf-8")
blocks = [b for b in re.split(r"\n\s*\n", srt.strip()) if b.strip()]
M["srt_cues"] = len(blocks)
M["srt_bytes"] = len(srt.encode("utf-8"))
M["srt_bom"] = srt.encode("utf-8")[:3] == b"\xef\xbb\xbf"
last = 0.0
overlap = []
maxlen = 0
for b in blocks:
    L = b.splitlines()
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    a = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    if a < last:
        overlap.append(L[0])
    last = z
    for line in L[2:]:
        maxlen = max(maxlen, len(line))
M["srt_last_end"] = round(last, 2)
M["srt_overlap"] = overlap
M["srt_maxline"] = maxlen

# ---- bang shot
L = [s["end"] - s["start"] for s in SHOTS]
M["shots_n"] = len(SHOTS)
M["shots_mean"] = round(sum(L) / len(L), 1)
M["shots_max"] = round(max(L), 1)
M["shots_max_id"] = max(SHOTS, key=lambda s: s["end"] - s["start"])["id"]
M["shots_min"] = round(min(L), 1)
M["shots_min_id"] = min(SHOTS, key=lambda s: s["end"] - s["start"])["id"]
M["shots_outside_3_15"] = sum(1 for x in L if not (3.0 <= x <= 15.0))
M["shots_hold"] = sum(1 for s in SHOTS if not s.get("sentences"))
run_ = []
worst = 0
for s in SHOTS:
    bg = s.get("bg")
    if run_ and run_[-1][0] == bg:
        run_[-1][1] += 1
        worst = max(worst, run_[-1][1])
    else:
        run_.append([bg, 1])
M["bg_max_run"] = worst
M["handoff_shots"] = sum(1 for s in SHOTS if s.get("flags", {}).get("handoff"))
M["nobust_shots"] = sum(1 for s in SHOTS if s.get("flags", {}).get("nobust"))

# ---- thumbnail
th = ED.OUT_DIR / "thumbnail.png"
M["thumbnail_exists"] = th.exists()
M["thumbnail_bytes"] = th.stat().st_size if th.exists() else 0

out_p = W / "_qc_measure_t03_en.json"
out_p.write_text(json.dumps(M, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(M, ensure_ascii=False, indent=1))
print(f"\n-> {out_p}")
