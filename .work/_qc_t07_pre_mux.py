#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra tham chieu cau trong sheet SFX Tap07 + dung luong dia + git tracking."""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

script = json.loads((ROOT / ".work/script_tap07.json").read_text(encoding="utf-8-sig"))
sent, elems = set(), set()
for el in script:
    elems.add(el["id"])
    for i, s in enumerate(el.get("sentences") or [], 1):
        sent.add(f"{el['id']}#{i}")

sfx = json.loads((ROOT / ".work/sfx_tap07.json").read_text(encoding="utf-8-sig"))
refs = []
for item in sfx["ambience"]:
    refs += [item[0], item[1]]
for rng in sfx["music_drop"].get("ranges", []):
    refs += list(rng)
for item in sfx["cues"]:
    refs.append(item[0])
bad = []
for r in refs:
    if "#" in r:
        if r not in sent:
            bad.append(r)
    elif r not in elems:
        bad.append(r)
print(f"sfx: {len(sfx['cues'])} cue · {len(sfx['ambience'])} ambience · "
      f"{len(sfx['music_drop'].get('ranges', []))} music_drop")
print(f"tham chieu: {len(refs)} · KHONG TON TAI: {len(bad)} -> {bad}")

print()
tot, used, free = shutil.disk_usage(str(ROOT))
print(f"dia: tong {tot/1e9:.1f} GB · da dung {used/1e9:.1f} GB · con trong {free/1e9:.1f} GB")

print()
for f in ("02_SAN_XUAT/Tap07/xuat_ban/Tap07_master.mp4",
          "02_SAN_XUAT/Tap07/xuat_ban/Tap07_master.mp3",
          "02_SAN_XUAT/Tap07/xuat_ban/Tap07.srt",
          "02_SAN_XUAT/Tap07/xuat_ban/thumbnail.png"):
    p = ROOT / f
    r = subprocess.run(["git", "ls-files", "--error-unmatch", f], cwd=ROOT,
                       capture_output=True, text=True)
    print(f"  {f}\n     ton tai={p.exists()} size={(p.stat().st_size/1e6 if p.exists() else 0):.1f} MB "
          f"git_tracked={'co' if r.returncode == 0 else 'KHONG'}")
