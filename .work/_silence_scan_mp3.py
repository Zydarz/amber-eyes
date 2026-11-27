#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do khoang cam (>0.3 s) bang ffmpeg silencedetect tren master mp3 + loudnorm/TP."""
import glob
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]


def silences(path, thr=-50, min_dur=0.25):
    cmd = [FF, "-hide_banner", "-i", str(path), "-af", f"silencedetect=noise={thr}dB:d={min_dur}",
           "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    out = []
    starts = re.findall(r"silence_start: (-?[\d.]+)", r.stderr)
    ends = re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", r.stderr)
    for i, (st) in enumerate(starts):
        en = float(ends[i][0]) if i < len(ends) else None
        du = float(ends[i][1]) if i < len(ends) else None
        out.append((float(st), en, du))
    return out


def lufs(path):
    cmd = [FF, "-hide_banner", "-i", str(path), "-af", "loudnorm=I=-16:TP=-1.5:print_format=json",
           "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    m = re.findall(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S)
    if not m:
        return None
    d = dict(re.findall(r'"(\w+)":\s*"([^"]*)"', m[-1]))
    return d


def main():
    files = []
    for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
        for n in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
            files.append((ld, n, ROOT / "02_SAN_XUAT" / "TIKTOK" / ld / f"{n}_master_audio.mp3"))
    files.append(("Tap04_EN", "TK2_CU", ROOT / ".work" / "_cu" / "tk04_entk2_audio_20261127" / "TK2_master_audio_moi_1404.mp3"))
    for ld, n, p in files:
        if not p.exists():
            print(f"{ld:9} {n}: THIEU {p.name}")
            continue
        s = silences(p)
        big = [x for x in s if (x[2] or 0) > 0.3]
        li = lufs(p)
        ii = li.get("input_i", "?") if li else "?"
        tp = li.get("input_tp", "?") if li else "?"
        print(f"{ld:9} {n}: cam>0.3s = {len(big)}   LUFS={ii}  TP={tp}")
        for st, en, du in big:
            print(f"      {st:7.3f} -> {en:7.3f}  ({du:.3f}s)")


if __name__ == "__main__":
    main()
