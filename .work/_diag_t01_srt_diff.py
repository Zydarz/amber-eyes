#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tai sao Tap01.srt (VN) doi khi sinh lai? So text cue cu voi timeline_s.json hien tai."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"


def dur(p):
    if not Path(p).exists():
        return None
    r = subprocess.run([str(FF), "-i", str(p)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    for line in (r.stderr or "").splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return None


def sec(ts):
    h, m, s = ts.split(":")
    s, ms = s.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


# ban COMMIT cua Tap01.srt
g = subprocess.run(["git", "show", "HEAD:02_SAN_XUAT/Tap01/xuat_ban/Tap01.srt"],
                   cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
committed = g.stdout.replace("\r\n", "\n")
cblocks = [x for x in committed.strip().split("\n\n") if x.strip()]
ctexts = [" ".join(x.splitlines()[2:]) for x in cblocks]
print(f"=== Tap01.srt COMMIT: {len(cblocks)} khoi · het {sec(cblocks[-1].splitlines()[1].split(' --> ')[1]):.2f}s")

tl = json.loads((W / "timeline_s.json").read_text(encoding="utf-8-sig"))
print(f"=== timeline_s.json (T01 VN): total {tl['total']}s · {len(tl['items'])} cau")
print(f"=== timeline items: het {tl['items'][-1]['end']:.2f}s")

print("\n=== THU TU CUE: commit vs timeline (dau 8) ===")
for i in range(8):
    c = ctexts[i] if i < len(ctexts) else "-"
    t = tl["items"][i]["text"] if i < len(tl["items"]) else "-"
    same = c.replace(" ", "") == t.replace(" ", "")
    print(f"  #{i+1} {'OK ' if same else 'KHAC'}  commit={c[:70]!r}")
    if not same:
        print(f"            timeline={t[:70]!r}")

print("\n=== FILE DA XUAT TAP 01 ===")
for p in sorted((ROOT / "02_SAN_XUAT/Tap01/xuat_ban").glob("*")):
    d = dur(p) if p.suffix in (".mp4", ".mp3") else ""
    print(f"  {p.name:<34} {p.stat().st_size:>12} {d if d else ''}  {p.stat().st_mtime}")

print("\n=== TAP01 timeline / master o VN vs JA ===")
for tag, tl_file, mp3 in [
    ("VN", W / "timeline_s.json", ROOT / "02_SAN_XUAT/Tap01/xuat_ban/Tap01_master.mp3"),
    ("JA", W / "timeline_s_JA.json", ROOT / "02_SAN_XUAT/Tap01_JA/xuat_ban/Tap01_JA_master.mp3"),
]:
    t = json.loads(tl_file.read_text(encoding="utf-8-sig")) if tl_file.exists() else None
    print(f"  {tag}: timeline total = {t['total'] if t else 'NA'} · master mp3 = {dur(mp3)}")
