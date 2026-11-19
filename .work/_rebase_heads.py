#!/usr/bin/env python
# In cau truc heading cua 3 stage cho file md bi conflict
import subprocess

REPO = r"D:/TEST/Gax/amber-eyes"
FILES = [
    "02_SAN_XUAT/Tap15/KeHoach_Video_Tap15.md",
    "02_SAN_XUAT/Tap15_EN/KeHoach_Video_Tap15_EN.md",
    "02_SAN_XUAT/Tap15_JA/KeHoach_Video_Tap15_JA.md",
]

for f in FILES:
    print("=" * 100)
    print(f)
    for stage, name in ((1, "BASE(HEAD~1)"), (2, "OURS(fdde269)"), (3, "THEIRS(local)")):
        try:
            raw = subprocess.check_output(
                ["git", "-C", REPO, "show", f":{stage}:{f}"], stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            print(f"  -- {name}: khong co")
            continue
        txt = raw.decode("utf-8", errors="replace").splitlines()
        heads = [(i + 1, l) for i, l in enumerate(txt) if l.startswith("#")]
        print(f"  -- {name}: {len(txt)} dong, {len(heads)} heading")
        for ln, l in heads:
            print(f"       {ln:5d}  {l[:90]}")
