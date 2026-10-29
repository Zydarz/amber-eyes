#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua nhanh: doi ten file bi gan nham + don cac dong manifest cu da 'cu'."""
import json
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R = Path(r"D:\TEST\Gax\Audi")
INBOX = R / "02_SAN_XUAT" / "sfx_youtube"
MAP = R / ".work" / "yt_map.tsv"
STATE = R / ".work" / "yt_watch_state.json"

# file 'Phone Alerts And Rings 0:19' bi gan nham sang fx_footsteps_run_wet_pavement
src = INBOX / "fx_footsteps_run_wet_pavement.mp3"
dst = INBOX / "fx_dtmf_touch_tone_beep.mp3"
if src.exists() and not dst.exists():
    shutil.move(str(src), str(dst))
    print("renamed -> fx_dtmf_touch_tone_beep.mp3")

st = json.loads(STATE.read_text(encoding="utf-8"))
used = set(st.get("used", []))
used.discard("fx_footsteps_run_wet_pavement")
used.add("fx_dtmf_touch_tone_beep")
st["used"] = sorted(used)
STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")

# giu cac dong dang cho (chua co file): cac ma nay se tay tai
keep_mas = set(sys.argv[1:]) if len(sys.argv) > 1 else set()
rows = []
for raw in MAP.read_text(encoding="utf-8-sig").splitlines():
    if not raw.strip():
        continue
    f = (raw.split("\t") + [""] * 6)[:6]
    ma = f[1].strip()
    if ma and ma not in used and ma not in keep_mas:
        print("drop manifest:", f[0], "|", ma)
        continue
    rows.append("\t".join(f))
MAP.write_text("\n".join(rows) + "\n", encoding="utf-8")
print("manifest con %d dong, state used %d ma" % (len(rows), len(used)))
