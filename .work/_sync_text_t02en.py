#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dong bo chu T2 EN sau khi doi audio Higgs (31/10-01/11/2026).

A. tts_manifest_EN_t02.json: `display` <- script (4 cau bi cu, gay lech phu de)
B. KeHoach_Video_Tap02_EN.md: 3 dong chu tren hinh khong khop cau dang doc
"""
import json
import pathlib
import shutil
import time

ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
W = ROOT / ".work"
PLAN = ROOT / "02_SAN_XUAT" / "Tap02_EN" / "KeHoach_Video_Tap02_EN.md"
MAN = W / "tts_manifest_EN_t02.json"
SCRIPT = W / "script_tap02_EN.json"

# ---------------------------------------------------------------- A. manifest
man = json.loads(MAN.read_text(encoding="utf-8-sig"))
sc = json.loads(SCRIPT.read_text(encoding="utf-8-sig"))
cur = {s["id"]: s["text"] for e in sc for s in e.get("sentences", [])}

bak = W / "_cu" / ("tts_manifest_EN_t02_pre_sync_%s.json" % time.strftime("%Y%m%d_%H%M%S"))
shutil.copy2(MAN, bak)
print("BACKUP manifest ->", bak.name)

changed = []
for m in man:
    sid = m["id"]
    if sid in cur and m.get("display") != cur[sid]:
        changed.append(sid)
        print("  %-9s display cu : %s" % (sid, m.get("display", "")[:78]))
        print("  %-9s display moi: %s" % ("", cur[sid][:78]))
        m["display"] = cur[sid]
MAN.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
print("manifest: %d cau doi display -> %s" % (len(changed), changed))

# ---------------------------------------------------------------- B. plan
bak2 = W / "_cu" / ("KeHoach_Video_Tap02_EN_pre_sync_%s.md" % time.strftime("%Y%m%d_%H%M%S"))
shutil.copy2(PLAN, bak2)
print("\nBACKUP plan ->", bak2.name)

EDITS = [
    # (shot, old, new)
    ("4-08",
     "“…a man disguised in an officer's uniform was standing right there in the dark, watching you.”",
     "“…a predator hiding behind an officer\u2019s uniform was standing right there in the dark, watching you.”"),
    ("4-13",
     "*Footprint from the crime scene* \u00b7 *Williams's own boots*",
     "*Snow boot impression from the crime scene* \u00b7 *Williams\u2019s own boots*"),
    ("4-16",
     "*Thousands of classified photographs & meticulous logs*",
     "*Thousands of photographs & meticulous logs*"),
]

txt = PLAN.read_text(encoding="utf-8-sig")
for sid, old, new in EDITS:
    n = txt.count(old)
    assert n == 1, "shot %s: doi duoc %d lan (mong doi 1)\n  OLD=%r" % (sid, n, old)
    txt = txt.replace(old, new)
    print("  %-5s  OK  -> %s" % (sid, new[:74]))
PLAN.write_text(txt, encoding="utf-8")
print("\nplan -> %s" % PLAN)

# ---------------------------------------------------------------- verify
print("\n=== KIEM TRA LAI ===")
man2 = {m["id"]: m for m in json.loads(MAN.read_text(encoding="utf-8-sig"))}
bad = [k for k, v in cur.items() if k in man2 and man2[k]["display"] != v]
print("manifest display != script:", bad or "KHONG co")
t2 = PLAN.read_text(encoding="utf-8-sig")
for sid, old, new in EDITS:
    assert old not in t2, "van con chu cu o %s" % sid
    assert new in t2, "khong thay chu moi o %s" % sid
print("plan: 3/3 dong da doi")
for kw in ("snowshoe", "man disguised", "classified"):
    hits = [i + 1 for i, L in enumerate(t2.splitlines()) if kw in L]
    print("  con '%s' o dong: %s" % (kw, hits or "khong"))
