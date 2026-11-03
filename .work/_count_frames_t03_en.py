#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dem khung that cua chunk C (va A/B de doi chieu) bang ffprobe -count_frames."""
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FP = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
EXPECT = {"A": 16470, "B": 16470, "C": 16458}
bad = False
for k, exp in EXPECT.items():
    p = W / f"video3_EN_t03_c{k}" / f"chunk{k}.mp4"
    if not p.exists():
        print(f"chunk {k}: THIEU {p}")
        bad = True
        continue
    r = subprocess.run([str(FP), "-v", "error", "-select_streams", "v:0", "-count_frames",
                        "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate",
                        "-of", "default=nw=1", str(p)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    info = dict(l.split("=", 1) for l in r.stdout.splitlines() if "=" in l)
    nf = int(info.get("nb_read_frames", 0))
    ok = nf == exp
    bad = bad or not ok
    print(f"chunk {k}: {nf} khung (mong doi {exp}) · {info.get('width')}x{info.get('height')} "
          f"@ {info.get('r_frame_rate')} · {p.stat().st_size / 1e6:.1f} MB -> {'OK' if ok else 'LECH!'}")
print("TONG:", sum(EXPECT.values()), "khung · mong doi", int(1646.620 * 30))
sys.exit(1 if bad else 0)
