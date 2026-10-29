# -*- coding: utf-8 -*-
"""Review độc lập — vòng 2: hồ sơ loudness, độ rộng stereo, sync phụ đề/hình.
Chỉ đo, không sửa file thành phẩm.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BIN = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FF = BIN / "ffmpeg.exe"
VID = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"
SRT = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02.srt"
WAV = WORK / "audio_master_t02.wav"

out = {}


def run(cmd):
    return subprocess.run([str(c) for c in cmd], capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


# ---------- 1. loudness CHÍNH stream trong mp4 (thành phẩm thật) ----------
r = run([FF, "-hide_banner", "-nostats", "-i", VID, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"])
tail = r.stderr.split("Summary:")[-1]
res = {}
for pat, name in [(r"^\s*I:\s*(-?\d+\.?\d*)\s*LUFS", "I"),
                  (r"^\s*LRA:\s*(-?\d+\.?\d*)\s*LU", "LRA"),
                  (r"^\s*Peak:\s*(-?\d+\.?\d*)\s*dBFS", "Peak")]:
    m = re.search(pat, tail, re.M)
    if m:
        res[name] = float(m.group(1))
out["mp4_audio_ebur128"] = res

# ---------- 2. hồ sơ loudness ngắn hạn: cắt 20s, đo integrated LUFS ----------
segs = []
dur = 1605.7
for s in range(0, int(dur) - 10, 20):
    r = run([FF, "-hide_banner", "-nostats", "-ss", str(s), "-t", "20", "-i", VID,
             "-vn", "-af", "ebur128", "-f", "null", "-"])
    t = r.stderr.split("Summary:")[-1]
    m = re.search(r"I:\s*(-?\d+\.?\d*)\s*LUFS", t)
    if m:
        segs.append({"t": s, "lufs": float(m.group(1))})
out["short_term_profile_20s"] = segs
if segs:
    vals = [x["lufs"] for x in segs]
    out["profile_stats"] = {"min": min(vals), "max": max(vals),
                             "median": float(np.median(vals)),
                             "min_at_s": segs[int(np.argmin(vals))]["t"],
                             "max_at_s": segs[int(np.argmax(vals))]["t"]}

# ---------- 3. độ rộng stereo: mid/side theo từng khối 30s ----------
r = run([FF, "-hide_banner", "-nostats", "-i", VID, "-vn",
         "-af", "pan=mono|c0=0.5*c0+0.5*c1,astats=metadata=1:reset=0", "-f", "null", "-"])
r2 = run([FF, "-hide_banner", "-nostats", "-i", VID, "-vn",
          "-af", "pan=mono|c0=0.5*c0-0.5*c1,astats=metadata=1:reset=0", "-f", "null", "-"])
mids = re.findall(r"RMS level dB:\s*(-?\d+\.?\d*)", r.stderr)
sides = re.findall(r"RMS level dB:\s*(-?\d+\.?\d*)", r2.stderr)
if mids and sides:
    mid = float(mids[0]); side = float(sides[0])
    out["stereo_width"] = {"mid_rms_db": mid, "side_rms_db": side,
                           "side_below_mid_db": round(side - mid, 2),
                           "width_pct": round(10 ** ((side - mid) / 20) * 100, 2)}
# kiem tra phai truc tiep: so sanh 2 kenhh mp4
r = run([FF, "-hide_banner", "-nostats", "-i", VID, "-vn",
         "-af", "channelsplit=channel_layout=stereo[l][r];[l][r]astats=metadata=1:reset=0",
         "-f", "null", "-"])
chrms = re.findall(r"Channel: (\d+)[\s\S]{0,400}?RMS level dB:\s*(-?\d+\.?\d*)", r.stderr)
out["per_channel_rms_db"] = chrms[:6]

# ---------- 4. sync: phu de (SRT) vs timeline ----------
tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
items = tl["items"]
srt_txt = SRT.read_text(encoding="utf-8")
cues = [b for b in re.split(r"\n\s*\n", srt_txt.strip()) if b.strip()]
def sec(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
srt_rows = []
for b in cues:
    L = b.splitlines()
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    a = sec(*ts[0]); z = sec(*ts[1])
    srt_rows.append({"i": L[0], "a": a, "z": z, "text": " ".join(L[2:])})
out["srt_cue_count"] = len(srt_rows)
out["timeline_item_count"] = len(items)
out["srt_first"] = srt_rows[0] if srt_rows else None
out["srt_last"] = srt_rows[-1] if srt_rows else None
# so cac muc thoi gian
if srt_rows and items:
    diffs = []
    for r_, it in zip(srt_rows, items):
        diffs.append(round(r_["a"] - it["start"], 3))
    out["srt_vs_timeline_start_diff"] = {
        "min": min(diffs), "max": max(diffs),
        "abs_max": max(abs(d) for d in diffs),
        "over_0.05": sum(1 for d in diffs if abs(d) > 0.05),
        "sample": diffs[:8],
    }
# cue nao tran (overlap) / gap
over = []
for i in range(1, len(srt_rows)):
    gap = round(srt_rows[i]["a"] - srt_rows[i - 1]["z"], 3)
    if gap < 0:
        over.append({"from": srt_rows[i - 1]["i"], "to": srt_rows[i]["i"], "overlap_s": round(-gap, 3)})
out["srt_overlaps"] = over[:10]
out["srt_overlap_count"] = len(over)
gaps = [round(srt_rows[i]["a"] - srt_rows[i - 1]["z"], 3) for i in range(1, len(srt_rows))]
out["srt_gap_stats"] = {"max": max(gaps), "min": min(gaps),
                        "n_over_1s": sum(1 for g in gaps if g > 1.0)}
# do dai phu de toan bo video
out["srt_coverage_pct"] = round(100 * sum(r_["z"] - r_["a"] for r_ in srt_rows) / dur, 2)

# ---------- 5. kiem tra moi video: co khoang den/den khong (black frames) ----------
r = run([FF, "-hide_banner", "-nostats", "-i", VID, "-vf", "blackdetect=d=0.2:pix_th=0.10",
         "-an", "-f", "null", "-"])
blacks = re.findall(r"black_start:([\d.]+) black_end:([\d.]+) black_duration:([\d.]+)", r.stderr)
out["black_intervals"] = [{"s": float(a), "e": float(b), "d": float(c)} for a, b, c in blacks]
out["black_count"] = len(blacks)

# ---------- 6. freeze frame: co hinh dung lai khong (giong hinh) ----------
r = run([FF, "-hide_banner", "-nostats", "-i", VID, "-vf", "freezedetect=n=-60dB:d=1.5", "-an", "-f", "null", "-"])
fz = re.findall(r"freeze_start:\s*([\d.]+).*?freeze_duration:\s*([\d.]+)", r.stderr)
out["freeze_intervals"] = [{"start": float(a), "dur": float(b)} for a, b in fz]
out["freeze_count"] = len(fz)
out["freeze_total_s"] = round(sum(b for _, b in fz), 2)

print(json.dumps(out, ensure_ascii=False, indent=2))
