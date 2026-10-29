#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua mapping sau khi xac minh noi dung bang audios_understand."""
import json
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R = Path(r"D:\TEST\Gax\Audi")
INBOX = R / "02_SAN_XUAT" / "sfx_youtube"
CONF = INBOX / "_conflict"
MAP = R / ".work" / "yt_map.tsv"
STATE = R / ".work" / "yt_watch_state.json"

# 1) file trong _conflict chinh la 'Cell Phone Vibrate' -> ve ten dung
c = CONF / "fx_dtmf_touch_tone_beep_74c73e9c-4853-4655-9c26-56a3d49d77bf.mp3"
if c.exists():
    shutil.move(str(c), str(INBOX / "fx_phone_vibrate.mp3"))
    print("conflict -> fx_phone_vibrate.mp3")

# 2) amb_crowd_mourning_outdoor thuc ra la 'Footsteps on fallen leaves'
old = INBOX / "amb_crowd_mourning_outdoor.mp3"
if old.exists():
    shutil.move(str(old), str(INBOX / "fx_footsteps_chase_forest.mp3"))
    print("amb_crowd_mourning_outdoor -> fx_footsteps_chase_forest.mp3")

st = json.loads(STATE.read_text(encoding="utf-8"))
used = set(st.get("used", []))
used.discard("amb_crowd_mourning_outdoor")
used.discard("fx_phone_vibrate")
used.add("fx_footsteps_chase_forest")
used.add("fx_phone_vibrate")
st["used"] = sorted(used)
STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")

# 3) manifest: bo dong co ma trung bi sai, them dong moi cho 'Human Group Cry Out'
rows = []
for raw in MAP.read_text(encoding="utf-8-sig").splitlines():
    if not raw.strip():
        continue
    f = (raw.split("\t") + [""] * 6)[:6]
    ma = f[1].strip()
    if ma == "amb_lab_equipment" and f[0].strip() == "Machine Rumble":
        print("drop manifest (ma trung):", f[0], "|", ma)
        continue
    if ma == "amb_crowd_mourning_outdoor":
        f[5] = "105.00"
    rows.append("\t".join(f))
# them dong cho 'Human Group Cry Out' 1:45 (se tai lai)
if not any(r.split("\t")[1].strip() == "amb_crowd_mourning_outdoor" for r in rows):
    rows.append("Human Group Cry Out\tamb_crowd_mourning_outdoor\tnen_moi_truong\t\tĐám đông\t105.00")
MAP.write_text("\n".join(rows) + "\n", encoding="utf-8")
print("manifest %d dong, used %d ma" % (len(rows), len(used)))
