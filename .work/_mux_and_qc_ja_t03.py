#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mux + toàn bộ QC cho JA Tap03 — chạy 1 lệnh sau khi picture.mp4 xong.

Thứ tự:
  1. kiểm picture.mp4 (H14) và khớp timeline
  2. package.py --mux  -> Tap03_JA_master.mp4 (+ thumbnail + description)
  3. _qc_final_ja_t03.py            (13 cổng đầu ra)
  4. _qc_sync_ja_t03.py             (lệch A/V, FFT + self-test)
  5. _check_stills_vs_video_ja_t03.py (ảnh tĩnh ↔ khung hình thật)
"""
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "03"
os.environ["PYTHONIOENCODING"] = "utf-8"

FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
PIC = W / "video3_JA_t03" / "picture.mp4"
MP4 = ROOT / "02_SAN_XUAT" / "Tap03_JA" / "xuat_ban" / "Tap03_JA_master.mp4"


def hdr(t):
    print("\n" + "#" * 76)
    print("#", t)
    print("#" * 76, flush=True)


def sh(cmd, logname=None):
    if logname:
        with open(W / logname, "w", encoding="utf-8") as fh:
            return subprocess.run(cmd, cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def dur(p):
    r = subprocess.run([str(FF), "-i", str(p)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    for line in (r.stderr or "").splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return None


hdr("1. KIỂM TRA picture.mp4")
if not PIC.exists():
    raise SystemExit(f"CHUA CO {PIC} — render chua xong")
d = dur(PIC)
import json  # noqa: E402
tl = json.loads((W / "timeline_s_JA_t03.json").read_text(encoding="utf-8-sig"))
total = float(tl["total"])
print(f"  picture.mp4 = {d:.3f} s · timeline.total = {total:.3f} s · lệch = {abs(d-total):.3f} s")
if abs(d - total) > 0.05:
    raise SystemExit("FAIL H14: picture lệch timeline > 0,05 s — KHONG mux")
print("  H14 PASS")

hdr("2. package.py --mux")
t0 = time.time()
r = sh([sys.executable, str(W / "package.py"), "--mux"], "_package_mux_ja_t03.log")
print(f"  rc={r.returncode} · {time.time()-t0:.1f}s · log=_package_mux_ja_t03.log")
if r.returncode != 0:
    print((W / "_package_mux_ja_t03.log").read_text(encoding="utf-8", errors="replace")[-2000:])
    raise SystemExit("MUX THAT BAI")
if not MP4.exists():
    raise SystemExit("MUX xong nhung khong co file cuoi")
print(f"  -> {MP4} · {MP4.stat().st_size/1e6:.1f} MB")

hdr("3. QC CUOI (13 cổng)")
r = sh([sys.executable, str(W / "_qc_final_ja_t03.py")], "_qc_final_ja_t03.log")
qc1 = (W / "_qc_final_ja_t03.log").read_text(encoding="utf-8", errors="replace")
print(qc1[-6000:])

hdr("4. LỆCH A/V (FFT + self-test)")
r = sh([sys.executable, str(W / "_qc_sync_ja_t03.py")], "_qc_sync_ja_t03.log")
qc2 = (W / "_qc_sync_ja_t03.log").read_text(encoding="utf-8", errors="replace")
print(qc2[-2500:])

hdr("5. ẢNH TĨNH ↔ KHUNG HÌNH THẬT")
r = sh([sys.executable, str(W / "_check_stills_vs_video_ja_t03.py")], "_check_stills_ja_t03.log")
qc3 = (W / "_check_stills_ja_t03.log").read_text(encoding="utf-8", errors="replace")
print(qc3[-1200:])

hdr("TÓM TẮT")
for name, log, rc in [("QC cuoi", "_qc_final_ja_t03.log", None),
                      ("Lech A/V", "_qc_sync_ja_t03.log", None),
                      ("Stills vs video", "_check_stills_ja_t03.log", None)]:
    txt = (W / log).read_text(encoding="utf-8", errors="replace")
    tail = [l for l in txt.splitlines() if "KET QUA" in l or "PASS" in l or "OK:" in l or "FAIL" in l]
    print(f"  {name}: {tail[-1] if tail else '?'}")
print(f"\n  mp4 cuối: {MP4} · {MP4.stat().st_size/1e6:.1f} MB")
