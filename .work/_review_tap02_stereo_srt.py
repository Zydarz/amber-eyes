# -*- coding: utf-8 -*-
"""Kiem chung stereo that + dung phu de (SRT) khop timeline bang noi dung cau."""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
VID = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"
SRT = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02.srt"

out = {}

# ---------- 1. stereo that: giai ma 60 s thanh giua, tinh tuong quan L-R ----------
r = subprocess.run([str(FF), "-v", "error", "-ss", "800", "-t", "60", "-i", str(VID),
                    "-vn", "-f", "s16le", "-ac", "2", "-ar", "48000", "-"],
                   capture_output=True)
a = np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0
a = a.reshape(-1, 2)
L, R = a[:, 0], a[:, 1]
mid = (L + R) / 2
side = (L - R) / 2
corr = float(np.corrcoef(L, R)[0, 1])
out["stereo_check"] = {
    "n_samples": len(L),
    "L_rms_db": round(float(20 * np.log10(np.sqrt(np.mean(L ** 2)) + 1e-12)), 2),
    "R_rms_db": round(float(20 * np.log10(np.sqrt(np.mean(R ** 2)) + 1e-12)), 2),
    "mid_rms_db": round(float(20 * np.log10(np.sqrt(np.mean(mid ** 2)) + 1e-12)), 2),
    "side_rms_db": round(float(20 * np.log10(np.sqrt(np.mean(side ** 2)) + 1e-12)), 2),
    "side_over_mid_db": round(float(20 * np.log10(np.sqrt(np.mean(side ** 2)) /
                                                 (np.sqrt(np.mean(mid ** 2)) + 1e-12))), 2),
    "LR_correlation": round(corr, 6),
    "identical_channels": bool(np.allclose(L, R)),
}

# ---------- 2. phu de khop timeline: khop bang NOI DUNG ----------
tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
items = tl["items"]
raw = SRT.read_text(encoding="utf-8")
cues = []
for b in re.split(r"\n\s*\n", raw.strip()):
    Ln = b.splitlines()
    if len(Ln) < 3:
        continue
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", Ln[1])
    if len(ts) < 2:
        continue
    a0 = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z0 = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    txt = " ".join(x.strip() for x in Ln[2:])
    cues.append({"i": Ln[0], "a": a0, "z": z0, "text": txt})

out["srt_cues_parsed"] = len(cues)
out["srt_first_3"] = cues[:3]
out["srt_last_2"] = cues[-2:]


def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9à-ỹ ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


ncues = [norm(c["text"]) for c in cues]
nitems = [(it["id"], norm(it["text"]), it) for it in items]
matched = []
for iid, nt, it in nitems:
    hit = None
    for ci, nc in enumerate(ncues):
        if nc and (nt in nc or nc in nt) and nt:
            hit = ci
            break
    if hit is None:
        # khop theo token chung
        toks = set(nt.split())
        for ci, nc in enumerate(ncues):
            ct = set(nc.split())
            if toks and len(toks & ct) / len(toks) > 0.8:
                hit = ci
                break
    if hit is not None:
        c = cues[hit]
        matched.append({"id": iid, "cue": c["i"], "cue_start": c["a"], "tl_start": it["start"],
                        "diff": round(c["a"] - it["start"], 3),
                        "tl_role": it["role"], "cue_text": c["text"][:40]})
out["subtitle_sync"] = {
    "items": len(items),
    "matched": len(matched),
    "unmatched": len(items) - len(matched),
    "diff_min": min([m["diff"] for m in matched], default=None),
    "diff_max": max([m["diff"] for m in matched], default=None),
    "abs_diff_gt_0.1": sum(1 for m in matched if abs(m["diff"]) > 0.1),
    "abs_diff_gt_0.25": sum(1 for m in matched if abs(m["diff"]) > 0.25),
    "worst": sorted(matched, key=lambda m: -abs(m["diff"]))[:8],
}

# ---------- 3. moi mau chu vao phu de co khop vai khong ----------
ROLE_VN = {"H": ["HOST", "CÚ"], "D": ["ĐIỀU TRA VIÊN", "ĐIỀU TRA VIEN", "SÓI"],
           "C": ["CHUYÊN GIA", "CHUYEN GIA", "CÁO"], "N1": ["N1"], "N2": ["N2"]}
tag_hist = {}
for c in cues:
    tag = c["text"].split("—")[0].strip().split("\n")[0][:22]
    tag_hist[tag] = tag_hist.get(tag, 0) + 1
out["srt_role_tags"] = dict(sorted(tag_hist.items(), key=lambda kv: -kv[1])[:12])

# ---------- 4. do dai phu de theo vai (kiem tra cue co tinh) ----------
print(json.dumps(out, ensure_ascii=False, indent=2))
