# -*- coding: utf-8 -*-
"""Ghép lại Tập 07 (sau khi sửa lỗi summary) + đo QC A9 trên 3 file mp4 cuối."""
import os
import pathlib
import re
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
PY = sys.executable

print("=" * 96)
print("GHÉP LẠI TAP07 (đã sửa lỗi EPISODES['07']['summary'])")
print("=" * 96)
e = dict(os.environ)
e["AE_EP"] = "07"
t0 = time.time()
r = subprocess.run([PY, str(WORK / "package.py"), "--mux"], cwd=str(ROOT), env=e,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print(f"exit={r.returncode}  ({time.time()-t0:.0f} s)")
print((r.stdout or "").strip()[-600:])
if r.returncode != 0:
    print("!! " + (r.stderr or "")[-1200:])

FINALS = [
    ("T02 VN", ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"),
    ("T07 VN", ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "Tap07_master.mp4"),
    ("T02 EN", ROOT / "02_SAN_XUAT" / "Tap02_EN" / "xuat_ban" / "Tap02_EN_master.mp4"),
]


def dur(p):
    out = subprocess.run([str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    try:
        return round(float(out.stdout.strip()), 2)
    except ValueError:
        return None


print("\n" + "=" * 96)
print("QC A9 TRÊN FILE MP4 CUỐI")
print("=" * 96)
for label, f in FINALS:
    if not f.exists():
        print(f"{label}: THIEU FILE {f}")
        continue
    print(f"\n--- {label} : {f.name} ---")
    print(f"  thoi luong : {dur(f)} s")
    e2 = subprocess.run([str(FF), "-v", "info", "-i", str(f), "-af", "ebur128=peak=true",
                         "-f", "null", "-"], capture_output=True, text=True,
                        encoding="utf-8", errors="replace")
    txt = (e2.stderr or "")
    i = txt.rfind("Integrated loudness")
    if i != -1:
        seg = txt[i:i + 500]
        I = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", seg)
        P = re.search(r"Peak:\s*(-?[\d.]+)\s*dBFS", seg)
        L = re.search(r"LRA:\s*(-?[\d.]+)\s*LU", seg)
        I = float(I.group(1)) if I else None
        P = float(P.group(1)) if P else None
        print(f"  LUFS       : {I}  [{'OK (-16 +-1)' if I and -17 <= I <= -15 else '!! ngoai'}]")
        print(f"  True Peak  : {P} dBFS  [{'OK (<=-1.5)' if P and P <= -1.5 else 'VUOT TRAN -1.5 (bay #38)'}]")
        print(f"  LRA        : {L.group(1) if L else '?'} LU")
    s = subprocess.run([str(FF), "-v", "info", "-i", str(f), "-af",
                        "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    segs = re.findall(r"silence_duration:\s*([\d.]+)", (s.stderr or ""))
    print(f"  im lap >0,3s @-60dB : {len(segs)} {segs[:5] if segs else '(khong co)'}"
          f"  [{'OK' if not segs else '!! VI PHAM V4'}]")
    d = subprocess.run([str(FF), "-v", "error", "-i", str(f), "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    errs = [x for x in (d.stderr or "").splitlines() if x.strip()]
    print(f"  loi giai ma : {len(errs)}  {errs[:2] if errs else '(0 loi)'}")

print("\n--- mo ta Tap07 (da tao lai?) ---")
for f in sorted((ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban").iterdir()):
    print(f"  {f.name:<26} {f.stat().st_size:>10}  {time.strftime('%H:%M:%S', time.localtime(f.stat().st_mtime))}")
