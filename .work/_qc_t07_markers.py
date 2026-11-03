#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC A6: ranh giới hồi trong timeline khớp với các mốc nhạc nền đã ghi ở Phụ lục C."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

tl = json.loads((ROOT / ".work/timeline_s_t07.json").read_text(encoding="utf-8-sig"))
print("timeline.total =", tl["total"])
print()
print("=== marker theo loai ===")
for m in tl["markers"]:
    print(f"  {m.get('type','?'):<8} act={m.get('act')} {m.get('id') or '':<8} "
          f"{m.get('start')} → {m.get('end')}")

print()
print("=== cau dau tien moi hoi (moc chuong YouTube) ===")
starts = {}
for it in tl["items"]:
    a = it.get("act")
    if a and a not in starts:
        starts[a] = it["start"]
for a in sorted(starts):
    t = int(starts[a] + 0.5)
    print(f"  Hoi {a}: {starts[a]:8.2f} s -> {t // 60:02d}:{t % 60:02d}")

print()
print("=== doi chieu moc da ghi trong Phu luc C (23,0 / 249,5 / 460,7 / 666,3 / 894,2) ===")
ref = [23.0, 249.5, 460.7, 666.3, 894.2]
for i, a in enumerate(sorted(starts)):
    d = starts[a] - ref[i]
    print(f"  Hoi {a}: timeline {starts[a]:8.2f} · hồ sơ {ref[i]:8.2f} · lệch {d:+.2f} s "
          f"{'OK' if abs(d) < 1.0 else 'LECH'}")

print()
print("=== audio master vs timeline.total ===")
import subprocess
FF = ROOT / ".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
for label, p in (("master wav", ROOT / ".work/audio_master_t07.wav"),
                 ("master mp3", ROOT / "02_SAN_XUAT/Tap07/xuat_ban/Tap07_master.mp3")):
    r = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                       capture_output=True, text=True)
    d = float(r.stdout.strip())
    print(f"  {label:<12} {d:.3f} s · lệch với timeline.total = {d - tl['total']:+.3f} s")
