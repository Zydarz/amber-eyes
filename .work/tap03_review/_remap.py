import io
import json
import re
import subprocess
import sys
from difflib import SequenceMatcher

BASE = r"D:\TEST\Gax\Audi"
OLD_MD = BASE + r"\01_KICH_BAN\Tap03\kichban_tap03_22102026_ban_goc.md"
OLD_JSON = BASE + r"\.work\tap03_review\parsed_old.json"
NEW_JSON = BASE + r"\.work\tap03_review\parsed_final.json"

try:
    old = json.load(io.open(OLD_JSON, encoding="utf-8"))
except Exception:
    subprocess.run([sys.executable, BASE + r"\.work\parse_kichban.py", OLD_MD, OLD_JSON], check=True)
    old = json.load(io.open(OLD_JSON, encoding="utf-8"))

new = json.load(io.open(NEW_JSON, encoding="utf-8"))


def sentences(els):
    out = {}
    for e in els:
        if e["kind"] != "LOI":
            continue
        for s in e["sentences"]:
            out[s["id"]] = s["text"]
    return out


os_ = sentences(old)
ns_ = sentences(new)
print("old sentences:", len(os_), "| new sentences:", len(ns_))

# similarity map old_id -> (best_new_id, ratio)
mapping = {}
for oid, otxt in os_.items():
    best, bratio = None, 0.0
    for nid, ntxt in ns_.items():
        r = SequenceMatcher(None, otxt.lower(), ntxt.lower()).ratio()
        if r > bratio:
            best, bratio = nid, r
    mapping[oid] = (best, round(bratio, 3))

# anchors referenced by the manifest
MANIFEST = BASE + r"\02_SAN_XUAT\Tap03\Danh_Sach_Anh_Tap03.md"
txt = io.open(MANIFEST, encoding="utf-8").read()
ids = sorted(set(re.findall(r"`(\d\.\d\d)(?:#(\d+))?`", txt)))
for m in re.finditer(r"`(\d\.\d\d)(?:#(\d+))?`", txt):
    pass
print("\n--- anchor translation ---")
for m in re.finditer(r"`(\d\.\d\d)(?:#(\d+))?`", txt):
    act, num_s = m.group(1), m.group(2)
    old_id = act
    if num_s:
        old_id = f"{act}#{num_s}"
    if old_id not in mapping:
        cue = [e for e in old if e["kind"] != "LOI" and e["id"] == old_id]
        print(f"{old_id:<9} (cue {cue[0]['kind'] if cue else '?'}) -> NO MATCH")
        continue
    nid, ratio = mapping[old_id]
    flag = "" if ratio >= 0.45 else "   <-- LOW SIMILARITY, VERIFY"
    print(f"{old_id:<9} -> {nid:<10} ratio={ratio}{flag}")
    print(f"          OLD: {os_[old_id][:110]}")
    print(f"          NEW: {ns_.get(nid,'')[:110]}")
