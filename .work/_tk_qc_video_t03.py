#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC clip TikTok Tap03: ffprobe + kiem tra anh nen dung theo timeline.

Check:
1. ffprobe: 1080x1920, 30 fps, H.264 + AAC 48k, duration bang audio master.
2. Moi shot: rut frame tai giay bat dau shot, so sanh voi nen mong doi
   (vector xam 16x28) -> nen nao giong nhat. Nen dung = pass.

Dung:  py -3 .work/_tk_qc_video_t03.py [--lang VN]
"""
import glob
import json
import os
import pathlib
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
FP = FF.replace("ffmpeg.exe", "ffprobe.exe")
LANGDIR = {"VN": "Tap03", "EN": "Tap03_EN", "JA": "Tap03_JA"}
CLIPS = ["TK1", "TK2", "TK3", "TK4", "TK5"]
BGDIR = ROOT / "assets" / "bg"


def probe(path):
    out = subprocess.check_output([FP, "-v", "error", "-show_entries",
                                   "stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels:"
                                   "format=duration,size,bit_rate",
                                   "-of", "json", str(path)]).decode()
    return json.loads(out)


def vec(img):
    g = img.convert("L").resize((16, 28), Image.BILINEAR)
    a = np.asarray(g, dtype=np.float32)
    a = a - a.mean()
    n = np.linalg.norm(a)
    return a / n if n > 0 else a


def frame_at(video, t, tmpdir):
    p = os.path.join(tmpdir, f"f_{t:.2f}.png")
    subprocess.run([FF, "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(video),
                    "-frames:v", "1", p], check=True)
    return Image.open(p).convert("RGB")


def main():
    args = sys.argv[1:]
    lang = "VN"
    if "--lang" in args:
        lang = args[args.index("--lang") + 1].upper()
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / LANGDIR[lang]
    bgcache = {}

    def bvec(name):
        if name not in bgcache:
            bgcache[name] = vec(Image.open(BGDIR / f"{name}.png"))
        return bgcache[name]

    allok = True
    with tempfile.TemporaryDirectory() as tmp:
        for cid in CLIPS:
            n = cid[2:]
            mp4 = d / f"TK{n}_video.mp4"
            tl_path = d / f"timeline_tk{n}.json"
            if not mp4.exists():
                print(f"{cid}: THIEU {mp4.name}")
                allok = False
                continue
            info = probe(mp4)
            v = next(s for s in info["streams"] if s["codec_type"] == "video")
            a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
            dur = float(info["format"]["duration"])
            mbs = int(info["format"]["size"]) / 1e6
            print(f"\n=== {cid} {mp4.name}")
            print(f"    video: {v['codec_name']} {v['width']}x{v['height']} @{v['r_frame_rate']}  "
                  f"audio: {a['codec_name'] if a else 'NONE'} {a['sample_rate'] if a else '-'}Hz "
                  f"{a['channels'] if a else '-'}ch")
            print(f"    duration={dur:.2f}s  size={mbs:.1f} MB  bitrate={int(info['format'].get('bit_rate',0))/1e6:.2f} Mbps")
            ok_spec = (v["width"] == 1080 and v["height"] == 1920 and v["r_frame_rate"] == "30/1"
                       and v["codec_name"] == "h264" and a is not None
                       and a["codec_name"] == "aac" and a["sample_rate"] == "48000" and mbs <= 500)
            print(f"    spec: {'PASS' if ok_spec else 'FAIL'} (1080x1920/30fps/H264/AAC48k/<=500MB)")
            allok = allok and ok_spec
            if not tl_path.exists():
                print("    THIEU timeline -> bo qua kiem tra anh nen")
                continue
            tl = json.loads(tl_path.read_text(encoding="utf-8-sig"))
            hits = 0
            for l in tl:
                t = l["start"] + 0.35
                if t >= dur - 0.2:
                    t = max(0.0, dur - 0.5)
                fr = vec(frame_at(mp4, t, tmp))
                scores = {b: float(np.linalg.norm(fr - bvec(b))) for b in {x["bg"] for x in tl}}
                best = min(scores, key=scores.get)
                exp = l["bg"]
                good = best == exp
                hits += good
                mark = "OK " if good else "FAIL"
                alt = "" if good else f"  (nhat={best} d={scores[best]:.3f} vs mong doi {exp} d={scores[exp]:.3f})"
                print(f"    {mark} {l['id']:<12} t={t:6.2f}s  nen={exp}{alt}")
            print(f"    anh nen khop: {hits}/{len(tl)}")
            allok = allok and (hits == len(tl))
    print("\nTAT CA PASS" if allok else "\nCO MUC CHUA PASS")


if __name__ == "__main__":
    main()
