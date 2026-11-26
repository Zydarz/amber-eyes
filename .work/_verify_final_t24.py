#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra cuối Tập 24 — 3 ngôn ngữ (sau khi dựng hình + đóng gói).

  py -3 .work/_verify_final_t24.py
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
PROD = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"
FP = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

LANGS = {
    "vi": ("Tap24", "timeline_s_t24.json", "Tap24_master.mp4", "Tap24.srt"),
    "en": ("Tap24_EN", "timeline_s_EN_t24.json", "Tap24_EN_master.mp4", "Tap24_EN.srt"),
    "ja": ("Tap24_JA", "timeline_s_JA_t24.json", "Tap24_JA_master.mp4", "Tap24_JA.srt"),
}


def probe(p):
    r = subprocess.run([str(FP), "-v", "error", "-show_entries",
                        "format=duration:stream=codec_name,width,height,r_frame_rate",
                        "-of", "json", str(p)], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def main():
    allok = True
    for lang, (d, tlname, mp4, srt) in LANGS.items():
        print(f"===== {lang} =====")
        out = PROD / d / "xuat_ban"
        tl = json.loads((WORK / tlname).read_text(encoding="utf-8"))
        total = float(tl["total"])

        mp4p = out / mp4
        if not mp4p.exists():
            print(f"  !! THIEU {mp4p}")
            allok = False
            continue
        info = probe(mp4p)
        dur = float(info["format"]["duration"])
        vs = [s for s in info["streams"] if "width" in s][0]
        print(f"  mp4      : {dur:.3f} s (timeline {total:.3f} s · lệch {dur-total:+.3f} s) "
              f"· {vs['width']}x{vs['height']} @ {vs['r_frame_rate']} "
              f"· {mp4p.stat().st_size/1e6:.1f} MB")
        if abs(dur - total) > 0.05:
            print("  !! H14 TRƯỢT: |hình - audio| > 0,05 s")
            allok = False

        for name in ("thumbnail.png", srt):
            p = out / name
            print(f"  {name:<14}: {'OK ' if p.exists() else 'THIEU '}"
                  f"{p.stat().st_size/1e6:.2f} MB" if p.exists() else "")

        pic = WORK / ("video3" + ("" if lang == "vi" else ("_EN" if lang == "en" else "_JA")) + "_t24") / "picture.mp4"
        if pic.exists():
            d2 = float(probe(pic)["format"]["duration"])
            print(f"  picture.mp4: {d2:.3f} s")
        else:
            print("  !! THIEU picture.mp4")
            allok = False

        desc = out / "mo_ta.txt"
        if desc.exists():
            t = desc.read_text(encoding="utf-8")
            i = t.find("⏱")
            block = [l for l in t[i:].split("\n") if l[:2].isdigit() and ":" in l[:5]][:6]
            print("  mốc chương :", " | ".join(x[:5] for x in block))
    print("\nKẾT QUẢ:", "ĐẠT" if allok else "TRƯỢT")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
