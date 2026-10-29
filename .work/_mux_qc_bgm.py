# -*- coding: utf-8 -*-
"""Ghép lại mp4 sau khi sửa bed BGM + đo QC A9.1 trên chính file mp4 cuối.

Bẫy #38: LUÔN đo ebur128 trên mp4 cuối, không đo WAV trung gian.
Chạy:  py -3 .work/_mux_qc_bgm.py
"""
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

JOBS = [
    ("T02 VN", {"AE_EP": "02"}, WORK / "audio_master_t02.wav",
     WORK / "video3_t02" / "picture.mp4",
     ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"),
    ("T07 VN", {"AE_EP": "07"}, WORK / "audio_master_t07.wav",
     WORK / "video3_t07" / "picture.mp4",
     ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "Tap07_master.mp4"),
    ("T02 EN", {"AE_EP": "02", "AE_LANG": "en"}, WORK / "audio_master_EN_t02.wav",
     WORK / "video3_EN_t02" / "picture.mp4",
     ROOT / "02_SAN_XUAT" / "Tap02_EN" / "xuat_ban" / "Tap02_EN_master.mp4"),
]


def dur(p):
    if not p.exists():
        return None
    r = subprocess.run([str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    try:
        return round(float(r.stdout.strip()), 2)
    except ValueError:
        return None


def run(args, timeout=3600):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout)


print("=" * 92)
print("GHÉP LẠI MP4 + ĐO QC A9.1 (đo trên chính file mp4 cuối)")
print("=" * 92)

for label, envs, wav, pic, final in JOBS:
    print(f"\n----------------- {label} -----------------")
    d_pic, d_wav = dur(pic), dur(wav)
    print(f"  picture.mp4 : {d_pic} s")
    print(f"  audio wav   : {d_wav} s")
    if d_pic and d_wav:
        diff = round(abs(d_pic - d_wav), 3)
        flag = "OK" if diff <= 0.5 else "!! LECH HANG > 0,5 s"
        print(f"  lech hinh/tieng: {diff} s  [{flag}]")

    e = dict(os.environ)
    e.update(envs)
    t0 = time.time()
    r = subprocess.run([PY, str(WORK / "package.py"), "--mux"], cwd=str(ROOT), env=e,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(f"  mux: exit={r.returncode} ({time.time() - t0:.0f} s)  {(r.stdout or '').strip()[-90:]}")
    if r.returncode != 0:
        print("  !! " + (r.stderr or "")[-900:])
        continue

    # ---- QC trên mp4 cuối
    d = dur(final)
    print(f"  mp4 cuoi    : {d} s  ({final.name})")
    e2 = run([str(FF), "-v", "info", "-i", str(final), "-af", "ebur128=peak=true",
              "-f", "null", "-"], timeout=1800)
    txt = (e2.stderr or "") + (e2.stdout or "")
    i = txt.rfind("Integrated loudness")
    if i != -1:
        seg = txt[i:i + 420]
        m = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", seg)
        p = re.search(r"Peak:\s*(-?[\d.]+)\s*dBFS", seg)
        lra = re.search(r"LRA:\s*(-?[\d.]+)\s*LU", seg)
        th = re.search(r"Threshold:\s*(-?[\d.]+)\s*LUFS", seg)
        I = float(m.group(1)) if m else None
        P = float(p.group(1)) if p else None
        ok_i = I is not None and -17 <= I <= -15
        ok_p = P is not None and P <= -1.5
        print(f"  LUFS        : {I}  [{'OK (-16 +-1)' if ok_i else '!! ngoai -16 +-1'}]")
        print(f"  True Peak   : {P} dBFS  [{'OK (<=-1.5)' if ok_p else '!! vuot tran -1.5'}]")
        print(f"  LRA         : {lra.group(1) if lra else '?'} LU   Threshold: {th.group(1) if th else '?'}")
    else:
        print("  !! khong doc duoc ebur128")

    # khoang cam > 0,3 s tren mp4
    s = run([str(FF), "-v", "info", "-i", str(final), "-af",
             "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"], timeout=1800)
    segs = re.findall(r"silence_duration:\s*([\d.]+)", (s.stderr or ""))
    print(f"  doan cam >0,3 s @-60dB: {len(segs)}  {segs[:5] if segs else '(khong co)'}")
    if segs:
        print("     !! VI PHAM V4 (khong duoc im lap tuc > 0,3 s)")
    dec = run([str(FF), "-v", "error", "-i", str(final), "-f", "null", "-"], timeout=1800)
    err = [x for x in (dec.stderr or "").splitlines() if x.strip()]
    print(f"  loi giai ma: {len(err)}  {err[:3] if err else '(0 loi)'}")
