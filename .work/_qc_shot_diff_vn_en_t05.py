#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So bang shot VN vs EN Tap05 — tim moi lech (A11 #78).

Cau (cot 2) · Vai (cot 3) · Mau (cot 4) · Nen (cot 5)
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")


def rows(p):
    t = pathlib.Path(p).read_text(encoding="utf-8-sig")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", t, re.M)
    sec = t[m.end():]
    sec = sec[:re.search(r"^\*\*Tổng:", sec, re.M).start()]
    out = {}
    for l in sec.splitlines():
        if not re.match(r"\|\s*[1-5]-\d+", l):
            continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        out[c[0]] = c
    return out


vn = rows(ROOT / "02_SAN_XUAT" / "Tap05" / "KeHoach_Video_Tap05.md")
en = rows(ROOT / "02_SAN_XUAT" / "Tap05_EN" / "KeHoach_Video_Tap05_EN.md")
print(f"VN {len(vn)} dong · EN {len(en)} dong\n")
print(f"{'SHOT':6} {'CAU (VN)':22} {'CAU (EN)':22} {'VAI':10} {'NEN':10} LECH")
diff = 0
for sid in sorted(set(vn) | set(en), key=lambda s: (int(s.split('-')[0]), int(s.split('-')[1]))):
    a, b = vn.get(sid), en.get(sid)
    if not a or not b:
        print(f"{sid:6} {'THIEU' if not a else '':22} {'THIEU' if not b else '':22}")
        diff += 1
        continue
    cau_v, cau_e = a[1], b[1]
    vai_v, vai_e = a[2], b[2]
    nen_v = re.findall(r"`([a-z_0-9]+)`", a[4])
    nen_e = re.findall(r"`([a-z_0-9]+)`", b[4])
    nen_v = [x for x in nen_v if x not in ("push", "pull", "still", "pan", "hero")] or ["-"]
    nen_e = [x for x in nen_e if x not in ("push", "pull", "still", "pan", "hero")] or ["-"]
    notes = []
    if cau_v != cau_e:
        notes.append("CAU")
    if vai_v.replace("—", "") != vai_e.replace("—", "") and vai_v != vai_e:
        notes.append(f"VAI({vai_v}|{vai_e})")
    if nen_v != nen_e:
        notes.append(f"NEN({','.join(nen_v)}|{','.join(nen_e)})")
    if notes:
        diff += 1
        print(f"{sid:6} {cau_v:22} {cau_e:22} {vai_v[:4]:10} {'/'.join(nen_e)[:10]:10} {' , '.join(notes)}")
print(f"\n=> {diff} dong lech giua VN va EN")
