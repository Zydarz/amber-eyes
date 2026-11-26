#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng hình Tập 24 theo lô để tránh vượt giới hạn 3600 s của một lệnh nền.

  py -3 .work/_render_t24.py --part 1 --of 4    # lô 1/4
  py -3 .work/_render_t24.py --concat --of 4     # nối 4 lô -> picture.mp4

Môi trường:  AE_EP=24  AE_LANG=vi|en|ja  (AE_WORKERS để đổi số worker, mặc định 4)

Ghi chú hiệu năng (26/11/2026): 8 worker làm máy tràn RAM (mỗi worker ~500 MB private,
ffmpeg mỗi tiến trình 30 thread) -> phân trang đĩa, tốc độ chỉ ~6,7 fps cho cả 8 worker.
4 worker giữ máy ổn định; có thể chỉnh bằng AE_WORKERS.
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

FF = (Path(subprocess.run(["where", "ffmpeg"], capture_output=True, text=True).stdout.strip().splitlines()[0])
      if subprocess.run(["where", "ffmpeg"], capture_output=True, text=True).stdout.strip()
      else WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe")
WORKERS = int(os.environ.get("AE_WORKERS", "4"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, default=0, help="so lot (1..of)")
    ap.add_argument("--of", type=int, default=4, help="so lot chia deu")
    ap.add_argument("--concat", action="store_true")
    a = ap.parse_args()

    vd = ED.w("video3")
    tl = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
    total = float(tl["total"])

    def seg_path(k):
        return vd / f"seg{k}_of{a.of}.mp4"

    if a.concat:
        segs = [seg_path(k) for k in range(1, a.of + 1)]
        missing = [s.name for s in segs if not s.exists()]
        if missing:
            raise SystemExit(f"THIEU lot: {missing}")
        lst = vd / f"segs_of{a.of}.txt"
        lst.write_text("".join(f"file '{s.as_posix()}'\n" for s in segs), encoding="utf-8")
        out = vd / "picture.mp4"
        subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0",
                        "-i", str(lst), "-c", "copy", str(out)], check=True)
        print("concat ->", out)
        return

    if not (1 <= a.part <= a.of):
        raise SystemExit(f"--part phai trong 1..{a.of}")
    step = total / a.of
    t0 = (a.part - 1) * step
    t1 = total if a.part == a.of else a.part * step
    out = seg_path(a.part)
    print(f"render lot {a.part}/{a.of}: {t0:.2f} -> {t1:.2f}  ({t1 - t0:.2f}s video, {WORKERS} worker)",
          flush=True)
    subprocess.run([sys.executable, str(WORK / "build_video3.py"),
                    "--from", f"{t0:.3f}", "--to", f"{t1:.3f}",
                    "--workers", str(WORKERS), "--out", str(out)], check=True)
    print("done ->", out)


if __name__ == "__main__":
    main()
