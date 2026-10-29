#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra cuoi cung cho bo anh nen Tap03: 45 anh, kich thuoc, vien, provenance, manifest."""
import json
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
BG = ROOT / "assets" / "bg"
WORK = ROOT / ".work"
OUT = ROOT / "02_SAN_XUAT" / "Tap03"

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


jobs = json.loads((WORK / "bg_jobs_tap03.json").read_text(encoding="utf-8"))
names = [j["name"] for j in jobs]
files = sorted(BG.glob("t3_*.png"))
# t3_gavel: connector tu choi 500 lien tuc -> dung t2_gavel cua Tap 02 (xem manifest B3.2)
FALLBACK = {"t3_gavel"}
EXPECT = len(jobs) - len(FALLBACK)

chk("Job file co 47 muc (45 goc + 2 sinh sau review)", len(jobs) == 47, f"{len(jobs)}")
chk("Khong trung ten", len(set(names)) == len(names))
chk(f"{EXPECT} file t3_*.png tren dia", len(files) == EXPECT, f"{len(files)}")

missing = [n for n in names if n not in FALLBACK and not (BG / f"{n}.png").exists()]
extra = [f.stem for f in files if f.stem not in names]
chk("Khong thieu anh", not missing, ", ".join(missing))
chk("Khong co anh thua", not extra, ", ".join(extra))

for n in FALLBACK:
    chk(f"{n} co fallback tu Tap 02", (BG / f"{n.replace('t3_', 't2_')}.png").exists())

bad_size = [f.name for f in files if Image.open(f).size != (2112, 1188)]
chk("Tat ca 2112x1188", not bad_size, ", ".join(bad_size))

# khong dung ten trung voi tap khac
clash = [f.name for f in files if f.stem in {p.stem for p in BG.glob("*.png")
                                            if not p.stem.startswith("t3_")}]
chk("Khong dung ten anh tap khac", not clash, ", ".join(clash))

prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
t3 = [p for p in prov if p.get("file", "").startswith("assets/bg/t3_")]
chk(f"provenance co {EXPECT} ban ghi t3_", len(t3) == EXPECT, f"{len(t3)}")
chk("provenance khong trung file",
    len({p["file"] for p in t3}) == len(t3))
nofile = [p["file"] for p in t3 if not (ROOT / p["file"]).exists()]
chk("Moi ban ghi provenance deu co file that", not nofile, ", ".join(nofile))
noprov = [f"assets/bg/{f.stem}.png" for f in files
          if f"assets/bg/{f.stem}.png" not in {p["file"] for p in t3}]
chk("Moi anh deu co dong provenance", not noprov, ", ".join(noprov))

chk("Manifest ton tai", (OUT / "Danh_Sach_Anh_Tap03.md").exists())
chk("Contact sheet ton tai", (OUT / "contact_sheet_t3.png").exists())
chk("script_tap03.json ton tai", (WORK / "script_tap03.json").exists())

# anh co nguoi: phai la 6 anh xac dinh
PERSON = {"t3_hitchhiker", "t3_bar_stool_shadow", "t3_two_agents",
          "t3_interview_room", "t3_giant_doorway", "t3_mother_shadow"}
chk("6 anh co nguoi (V5) deu co file",
    all((BG / f"{n}.png").exists() for n in PERSON), ", ".join(sorted(PERSON)))

print("\n" + ("TAT CA DA DAT" if ok else "CO VIEC CHUA XONG"))
sys.exit(0 if ok else 1)
