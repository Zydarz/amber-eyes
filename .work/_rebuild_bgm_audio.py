# -*- coding: utf-8 -*-
"""Dựng lại audio sau khi sửa bed BGM (T02 VN, T07 VN, T02 EN).

Chạy tuần tự (không chạy song song 2 lượt dựng - luật T3).
Mỗi lượt: sao lưu file cũ -> build_audio3.py -> so thời lượng master cũ/mới.
"""
import os
import pathlib
import shutil
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
PY = sys.executable

JOBS = [
    ("T02 VN", {"AE_EP": "02"}, WORK / "audio_master_t02.wav",
     ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp3"),
    ("T07 VN", {"AE_EP": "07"}, WORK / "audio_master_t07.wav",
     ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "Tap07_master.mp3"),
    ("T02 EN", {"AE_EP": "02", "AE_LANG": "en"}, WORK / "audio_master_EN_t02.wav",
     ROOT / "02_SAN_XUAT" / "Tap02_EN" / "xuat_ban" / "Tap02_EN_master.mp3"),
]

FFPROBE = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"


def dur(p):
    if not p.exists():
        return None
    out = subprocess.run([str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    try:
        return round(float(out.stdout.strip()), 2)
    except ValueError:
        return None


log = WORK / "rebuild_bgm_audio.log"
lines = []


def logp(s):
    print(s, flush=True)
    lines.append(s)


logp(f"=== BAT DAU {time.strftime('%Y-%m-%d %H:%M:%S')} ===")
for label, envs, wav, mp3 in JOBS:
    logp(f"\n---------- {label} ({envs}) ----------")
    bak = WORK / "_cu"
    bak.mkdir(exist_ok=True)
    if wav.exists():
        b = bak / f"{wav.name}.bak_bgm"
        shutil.copy2(wav, b)
        logp(f"  sao luu wav -> {b.name}  ({dur(wav)} s)")
    if mp3.exists():
        b = bak / f"{mp3.name}.bak_bgm"
        shutil.copy2(mp3, b)
        logp(f"  sao luu mp3 -> {b.name}  ({dur(mp3)} s)")

    e = dict(os.environ)
    e.update(envs)
    t0 = time.time()
    r = subprocess.run([PY, str(WORK / "build_audio3.py")], cwd=str(ROOT), env=e,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    dt = time.time() - t0
    tail = "\n".join((r.stdout or "").strip().splitlines()[-12:])
    logp(f"  exit={r.returncode}  ({dt:.0f} s)")
    if tail:
        logp("  " + tail.replace("\n", "\n  "))
    if r.returncode != 0:
        logp("  !! LOI:\n" + (r.stderr or "")[-1500:])
        logp(f"=== DUNG TAI {label} ===")
        break
    logp(f"  master moi: wav={dur(wav)} s  mp3={dur(mp3)} s")

logp(f"\n=== XONG {time.strftime('%Y-%m-%d %H:%M:%S')} ===")
log.write_text("\n".join(lines), encoding="utf-8")
