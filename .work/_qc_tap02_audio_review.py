# -*- coding: utf-8 -*-
"""QC audio thuần cho Tap02_master.mp4 — chỉ đo, không sửa gì.
Chạy: py -3 .work/_qc_tap02_audio_review.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
FF = ROOT / ".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
FP = ROOT / ".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
VID = ROOT / "02_SAN_XUAT/Tap02/xuat_ban/Tap02_master.mp4"
MP3 = ROOT / "02_SAN_XUAT/Tap02/xuat_ban/Tap02_master.mp3"

out = {}


def run(cmd):
    return subprocess.run([str(c) for c in cmd], capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


# ---------- 1. giai ma: loi hong ----------
r = run([FF, "-v", "error", "-i", VID, "-f", "null", "-"])
err_lines = [l for l in r.stderr.splitlines() if l.strip()]
out["decode_errors"] = len(err_lines)
out["decode_error_sample"] = err_lines[:15]

# ---------- 2. ebur128 (lufs, LRA, true peak) ----------
r = run([FF, "-hide_banner", "-nostats", "-i", MP3, "-af", "ebur128=peak=true", "-f", "null", "-"])
txt = r.stderr
tail = txt.split("Summary:")[-1] if "Summary:" in txt else txt[-4000:]
vals = {}
for key in ("I:", "LRA:", "Peak:", "LRA low:", "LRA high:", "Threshold:"):
    m = re.search(re.escape(key) + r"\s*(-?\d+\.?\d*) LUFS|", tail) if key in ("I:", "LRA:") else None
for pat, name in [
    (r"^\s*I:\s*(-?\d+\.?\d*)\s*LUFS", "integrated_lufs"),
    (r"^\s*LRA:\s*(-?\d+\.?\d*)\s*LU", "lra"),
    (r"^\s*Peak:\s*(-?\d+\.?\d*)\s*dBFS", "true_peak_dbtp"),
]:
    m = re.search(pat, tail, re.M)
    if m:
        vals[name] = float(m.group(1))
out["ebur128"] = vals
out["ebur128_tail"] = "\n".join([l for l in tail.splitlines() if l.strip()][-14:])

# ---------- 3. silencedetect: im lang > 0.3s (V4) ----------
r = run([FF, "-hide_banner", "-nostats", "-i", MP3,
         "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"])
sils = []
for m in re.finditer(r"silence_start:\s*(-?\d+\.?\d*)\s*\|\s*silence_end:\s*(-?\d+\.?\d*)", r.stderr):
    s = float(m.group(1)); e = float(m.group(2))
    sils.append({"start": s, "end": e, "dur": round(e - s, 3)})
out["silences_gt_0.3s_at_-60dB"] = sils
out["silence_count"] = len(sils)
out["silence_total_s"] = round(sum(s["dur"] for s in sils), 3)
out["silence_max_s"] = round(max([s["dur"] for s in sils], default=0), 3)

# ---------- 4. do lon cua nhac nen (spectrum: co nhac khong) ----------
# lay 3 khoang 10s: dau, giua, cuoi -> RMS + so do kieng (flat spectrum = nhac nen)
for tag, ss in [("dau_60s", 60), ("giua_800s", 800), ("cuoi_1500s", 1500)]:
    r = run([FF, "-hide_banner", "-nostats", "-ss", str(ss), "-t", "10", "-i", MP3,
             "-af", "astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level",
             "-f", "null", "-"])
    rms = re.findall(r"lavfi\.astats\.Overall\.RMS_level=(-?\d+\.?\d*)", r.stderr)
    r2 = run([FF, "-hide_banner", "-nostats", "-ss", str(ss), "-t", "10", "-i", MP3,
              "-af", "volumedetect", "-f", "null", "-"])
    mean = re.search(r"mean_volume:\s*(-?\d+\.?\d*) dB", r2.stderr)
    maxv = re.search(r"max_volume:\s*(-?\d+\.?\d*) dB", r2.stderr)
    out.setdefault("segments", {})[tag] = {
        "rms_db": [float(x) for x in rms][:6],
        "mean_db": float(mean.group(1)) if mean else None,
        "max_db": float(maxv.group(1)) if maxv else None,
    }

# ---------- 5. stereo hay mono? kiem tra kenhh truong / mono ----------
r = run([FF, "-hide_banner", "-nostats", "-i", MP3,
         "-af", "astats=metadata=1:reset=0", "-f", "null", "-"])
ch = {}
for m in re.finditer(r"Channel:\s*(\d+)", r.stderr):
    ch[m.group(1)] = ch.get(m.group(1), 0) + 1
out["channel_stats_header"] = "\n".join(r.stderr.splitlines()[:40])

# ---------- 6. doi chieu video/audio dua tren PTS cuoi ----------
r = run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries",
         "frame=pts_time", "-read_intervals", "%+#1", "-of", "csv=p=0", VID])
r2 = run([FP, "-v", "error", "-select_streams", "a:0", "-show_entries",
          "frame=pts_time", "-read_intervals", "%+#1", "-of", "csv=p=0", VID])
out["first_pts"] = {"v": r.stdout.strip(), "a": r2.stdout.strip()}

print(json.dumps(out, ensure_ascii=False, indent=2))
