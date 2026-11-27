#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra tinh toan ven clip EN TK2 moi render: stream, decode loi, khoang cam, anh nen theo shot."""
import glob
import json
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
FP = FF.replace("ffmpeg.exe", "ffprobe.exe")
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"
VID = D / "TK2_video.mp4"


def probe(path):
    r = subprocess.run([FP, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
                       capture_output=True, text=True, errors="replace")
    return json.loads(r.stdout)


def main():
    info = probe(VID)
    for s in info["streams"]:
        extra = ""
        if s["codec_type"] == "video":
            extra = f" {s['width']}x{s['height']} {s.get('avg_frame_rate')} fps={s.get('nb_frames')}"
        print(f"  {s['codec_type']:9} {s['codec_name']:10}{extra}")
    print(f"  duration = {float(info['format']['duration']):.3f}s   size = {int(info['format']['size'])/1e6:.1f} MB")

    # giai ma toan bo de dem loi
    r = subprocess.run([FF, "-v", "error", "-i", str(VID), "-f", "null", "-"],
                       capture_output=True, text=True, errors="replace")
    errs = [l for l in r.stderr.splitlines() if l.strip()]
    print(f"  loi giai ma = {len(errs)}")
    for e in errs[:5]:
        print("     ", e)

    # so sanh audio stream voi master
    tl = json.loads((D / "timeline_tk2.json").read_text(encoding="utf-8"))
    total = float(info["format"]["duration"])
    print("\n  --- shot theo timeline (nen nen) ---")
    spec = json.loads((D / "SPEC_AUDIO_CLIP_TAP04.json").read_text(encoding="utf-8-sig"))
    meta = {l["clip_line_id"]: (l["bg"], l.get("motion", "still")) for l in spec["clips"]["TK2"]["lines"]}
    for k, l in enumerate(tl):
        s0 = 0.0 if k == 0 else l["start"]
        s1 = tl[k + 1]["start"] if k + 1 < len(tl) else total
        bg, mo = meta[l["id"]]
        print(f"    {l['id']:<12} {s0:6.2f}-{s1:6.2f} ({s1-s0:5.2f}s) {bg:<28} {mo:<6} match={l.get('match_ratio')}")

    # kiem tra anh nen ton tai
    missing = [meta[l["id"]][0] for l in tl
               if not (ROOT / "assets" / "bg" / (meta[l["id"]][0] + ".png")).exists()]
    print(f"\n  nen thieu = {missing if missing else 'KHONG CO'}")


if __name__ == "__main__":
    main()
