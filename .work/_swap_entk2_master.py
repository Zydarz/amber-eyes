# -*- coding: utf-8 -*-
"""Thay master EN TK2 bang ban da tron (mp3 + wav dong bo).

- Backup master cu vao .work/_cu/ (da co san) + them file .bak_ cu de an toan
- Ghi de TK2_master_audio.mp3 va TK2_master_audio.wav bang ban moi
"""
import pathlib
import shutil
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"

stamp = datetime.now().strftime("%Y%m%d_%H%M")
bakdir = ROOT / ".work" / "_cu" / f"entk2_master_premix_{stamp}"
bakdir.mkdir(parents=True, exist_ok=True)

for name in ["TK2_master_audio.mp3", "TK2_master_audio.wav"]:
    src = D / name
    if src.exists():
        shutil.copy2(src, bakdir / name)
        print("backup:", name, "->", bakdir)

for name in ["TK2_master_audio.mp3", "TK2_master_audio.wav"]:
    new = D / f"{name[:-4]}_new{name[-4:]}"
    if not new.exists():
        raise SystemExit(f"THIEU file moi: {new}")
    shutil.move(str(new), str(D / name))
    print("thay:", name, "<-", new.name, f"({(D/name).stat().st_size} bytes)")

print("\nket qua:", bakdir)
for f in sorted(D.glob("TK2_master_audio*")):
    print(f"   {f.name:34} {f.stat().st_size:>10} bytes")
