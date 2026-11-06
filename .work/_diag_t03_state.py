#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — chẩn đoán trạng thái script / timeline / shots so với master mp3."""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
MASTER = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp3"

tl = json.loads((WORK / "timeline_s_t03.json").read_text(encoding="utf-8"))
script = json.loads((WORK / "script_tap03.json").read_text(encoding="utf-8"))
shots = json.loads((WORK / "shots_t03.json").read_text(encoding="utf-8"))

out = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration",
                      "-of", "default=noprint_wrappers=1:nokey=1", str(MASTER)],
                     capture_output=True, text=True).stdout.strip()
dur = float(out)

print(f"MASTER duration      = {dur:.3f}s")
print(f"timeline total       = {tl['total']:.3f}s   -> LECH {dur - tl['total']:+.3f}s")
print(f"timeline intro       = {tl['intro']}")
items = tl["items"]
print(f"timeline items       = {len(items)}")
print(f"  first item         = {items[0]['id']} start={items[0]['start']} end={items[0]['end']}")
print(f"  last  item         = {items[-1]['id']} start={items[-1]['start']} end={items[-1]['end']}")
print(f"  max end            = {max(i['end'] for i in items):.3f}")
print(f"timeline acts        = {json.dumps(tl['acts'], ensure_ascii=False)}")
mk = {}
for m in tl["markers"]:
    mk[m["type"]] = mk.get(m["type"], 0) + 1
print(f"timeline markers     = {mk}")
for m in tl["markers"]:
    if m["type"] == "ACT":
        print(f"   ACT {m['act']}: {m['start']:.3f} -> {m['end']:.3f}")

# script side
sents = []
for e in script:
    if e.get("kind") == "LOI":
        for s in e.get("sentences", []):
            sents.append((e["id"], s["id"], s["text"]))
print(f"\nscript_tap03 LOI sentences = {len(sents)}")
print(f"script elements       = {len(script)}")
tl_ids = [i["id"] for i in items]
sc_ids = [s[1] for s in sents]
print(f"same id set?          = {set(tl_ids) == set(sc_ids)}")
print(f"same order?           = {tl_ids == sc_ids}")
only_tl = [x for x in tl_ids if x not in set(sc_ids)]
only_sc = [x for x in sc_ids if x not in set(tl_ids)]
print(f"only in timeline      = {only_tl[:10]}")
print(f"only in script        = {only_sc[:10]}")

# text equality for common ids
tmap = {i["id"]: i["text"] for i in items}
diff = [(i, tmap[i], t) for (e, i, t) in sents if i in tmap and tmap[i] != t]
print(f"text mismatches       = {len(diff)}")
for d in diff[:5]:
    print("   ", d)

# shots
print(f"\nshots count           = {len(shots)}")
ids = [s.get("id") for s in shots]
print(f"unique shot ids       = {len(set(ids))} / {len(ids)}")
dup = [x for x in set(ids) if ids.count(x) > 1]
print(f"duplicate ids         = {dup}")
if shots:
    print(f"shot keys             = {list(shots[0].keys())}")
    print(f"shot[0]               = {json.dumps(shots[0], ensure_ascii=False)[:400]}")
    print(f"shot[-1]              = {json.dumps(shots[-1], ensure_ascii=False)[:400]}")
