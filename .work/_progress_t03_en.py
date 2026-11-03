#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Doc tien do render tu BO DEM KHUNG trong log (log cua Tee-Object PS 5.1 la UTF-16LE).
Khong dung kich thuoc file part_*.mp4 (ffmpeg ghi mdat theo lo -> uoc luong sai gap 2 lan)."""
import datetime
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
LOG = pathlib.Path("D:/TEST/Gax/amber-eyes/.work/_render_t03_en.log")
TOTAL = 49398
WORKERS = 6
PER = TOTAL // WORKERS          # 8233


def read_log(p: pathlib.Path) -> str:
    b = p.read_bytes()
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return b.decode("utf-16")
    if b.count(0) > len(b) * 0.02:
        return b.decode("utf-16-le")
    return b.decode("utf-8-sig", errors="replace")


txt = read_log(LOG)
done = {}
for m in re.finditer(r"\[part_(\d+)\.mp4\]\s+(\d+)/(\d+)", txt):
    done[m.group(1)] = int(m.group(2))
frames = sum(done.values())
print("=== tien do render EN Tap03 ===")
print(f"  workers: {len(done)} · frame xong: {frames} / {TOTAL} ({100*frames/TOTAL:.1f}%)")
for k in sorted(done, key=int):
    print(f"    part_{k}: {done[k]:5d} / {PER}  ({100*done[k]/PER:.0f}%)")
if frames:
    # moc thoi gian bat dau = thoi gian tao process cha cu renderer (khong dung mtime cua part:
    # ffmpeg ghi lai file lien tuc => mtime luon la "bay gio")
    import subprocess
    # lay PID cua process cha roi dung Get-Process .StartTime (CIM CreationDate co dinh dang rieng)
    out = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "$p = Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
         "Where-Object { $_.CommandLine -like '*_render_patched.py*' -and "
         "$_.CommandLine -notlike '*multiprocessing.spawn*' } | Select-Object -First 1; "
         "if ($p) { (Get-Process -Id $p.ProcessId).StartTime.ToString('o') }"],
        capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()
    t0 = None
    m = re.search(r"(\d{4}-\d\d-\d\d)[T ](\d\d:\d\d:\d\d)", out)
    if m:
        t0 = datetime.datetime.fromisoformat(f"{m.group(1)} {m.group(2)}").timestamp()
    if not t0:
        t0 = min(p.stat().st_mtime for p in
                 pathlib.Path("D:/TEST/Gax/amber-eyes/.work/video3_EN_t03").glob("part_*.mp4"))
    elapsed = datetime.datetime.now().timestamp() - t0
    fps = frames / elapsed
    rem = (TOTAL - frames) / fps if fps > 0 else 0
    print(f"  bat dau {datetime.datetime.fromtimestamp(t0).strftime('%H:%M:%S')}"
          f" · elapsed ~{elapsed/60:.1f} phut · toc do ~{fps:.1f} fps")
    print(f"  con lai ~{rem/60:.0f} phut · ETA ~"
          f"{(datetime.datetime.now() + datetime.timedelta(seconds=rem)).strftime('%H:%M:%S')}")
