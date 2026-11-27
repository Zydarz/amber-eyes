#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Theo doi kernel Kaggle 'fix EN TK2 Tap04' va tai 2 file WAV khi xong.

Poll: kaggle kernels status -> khi status=Complete -> kaggle kernels output -p <dir>
Dung: py -3 .work/_fix_en_tk2_kaggle_watch.py [--max-min 180]
"""
import json
import pathlib
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
KB = "chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu"
OUT = ROOT / ".work" / "kaggle_higgs" / "_fix_en_tk02_out"


def sh(args):
    return subprocess.run([str(a) for a in args], capture_output=True, text=True, errors="replace")


def main():
    max_min = 180
    if "--max-min" in sys.argv:
        max_min = int(sys.argv[sys.argv.index("--max-min") + 1])
    t0 = time.time()
    last = None
    while (time.time() - t0) / 60 < max_min:
        r = sh(["py", "-3", "-m", "kaggle.cli", "kernels", "status", KB])
        s = (r.stdout + r.stderr).strip()
        if s != last:
            print("[%.1f min] %s" % ((time.time() - t0) / 60, s), flush=True)
            last = s
        if "Complete" in s:
            OUT.mkdir(parents=True, exist_ok=True)
            r2 = sh(["py", "-3", "-m", "kaggle.cli", "kernels", "output", KB, "-p", str(OUT),
                     "-f", "-o"])
            print("download rc=", r2.returncode)
            print(r2.stdout[-2000:]); print(r2.stderr[-2000:])
            wavs = list(OUT.rglob("*.wav"))
            print("WAV tai ve:", len(wavs))
            for w in wavs:
                print("  ", w, w.stat().st_size)
            return 0 if wavs else 1
        if "Error" in s or "error" in s.lower() and "0 error" not in s.lower():
            print("KERNEL LOI:", s)
            return 2
        time.sleep(60)
    print("QUA THOI GIAN CHO")
    return 3


if __name__ == "__main__":
    sys.exit(main())
