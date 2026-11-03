#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Canh cau CU (git HEAD) -> cau MOI, theo text, de lay bang do id.

Quy tac: doi chieu theo KHOA TEN (sentence id), khong theo chi so thu tu.
Ket qua ghi .work/_t07_oldnew_map.json + bao cao bang console.
"""
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"


def norm(t):
    t = re.sub(r"\s+", " ", (t or "")).strip()
    return t


def flat(script):
    """{sentence_id: (element_id, role, text)} theo thu tu kich ban."""
    out = {}
    order = []
    for it in script:
        if it.get("kind") not in ("LOI", "NGHI"):
            continue
        role = it.get("role", "")
        for s in it.get("sentences", []):
            out[s["id"]] = (it["id"], role, norm(s["text"]))
            order.append(s["id"])
    return out, order


new_s = json.loads((W / "script_tap07.json").read_text(encoding="utf-8-sig"))
raw = subprocess.run(["git", "show", "HEAD:.work/script_tap07.json"],
                     cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
old_s = json.loads(raw.stdout)

old_map, old_order = flat(old_s)
new_map, new_order = flat(new_s)
print(f"cau CU = {len(old_order)} · cau MOI = {len(new_order)}")

# --- 1. gom theo element, doi chieu text ---
old_by_el = {}
for sid in old_order:
    old_by_el.setdefault(old_map[sid][0], []).append(sid)
new_by_el = {}
for sid in new_order:
    new_by_el.setdefault(new_map[sid][0], []).append(sid)

mapping = {}          # old_id -> new_id
deleted = []          # old_id khong co doi chieu
changed = []          # (old_id, new_id) doi chieu theo thu tu trong block "replace"
added = []            # new_id moi hoan toan

for el in sorted(set(old_by_el) | set(new_by_el)):
    o = old_by_el.get(el, [])
    n = new_by_el.get(el, [])
    if not o:
        added += n
        continue
    if not n:
        deleted += o
        continue
    sm = difflib.SequenceMatcher(
        None, [old_map[s][2] for s in o], [new_map[s][2] for s in n], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                mapping[o[i1 + k]] = n[j1 + k]
        elif tag == "delete":
            deleted += o[i1:i2]
        elif tag == "insert":
            added += n[j1:j2]
        else:  # replace: doi chieu theo thu tu trong block
            ob, nb = o[i1:i2], n[j1:j2]
            for k in range(min(len(ob), len(nb))):
                mapping[ob[k]] = nb[k]
                if old_map[ob[k]][2] != new_map[nb[k]][2]:
                    changed.append((ob[k], nb[k]))
            for extra in ob[len(nb):]:
                deleted.append(extra)
            for extra in nb[len(ob):]:
                added.append(extra)

print(f"khop nguyen van = {len(mapping) - len(changed)} · doi chieu = {len(changed)} "
      f"· xoa = {len(deleted)} · them moi = {len(added)}")
print()
print("--- CAU BI XOA (cu -> khong con) ---")
for s in deleted:
    print(f"  {s:>10}  [{old_map[s][1]}] {old_map[s][2][:95]}")
print()
print("--- CAU MOI ---")
for s in added:
    print(f"  {s:>10}  [{new_map[s][1]}] {new_map[s][2][:95]}")
print()
print("--- CAU DOI CHUU ---")
for o, n in changed:
    print(f"  {o:>10} -> {n:<10}")
    print(f"      CU : {old_map[o][2][:150]}")
    print(f"      MOI: {new_map[n][2][:150]}")

out = {
    "mapping": mapping,
    "deleted": deleted,
    "added": added,
    "changed": changed,
    "old_order": old_order,
    "new_order": new_order,
    "old_text": {k: v[2] for k, v in old_map.items()},
    "new_text": {k: v[2] for k, v in new_map.items()},
    "old_role": {k: v[1] for k, v in old_map.items()},
    "new_role": {k: v[1] for k, v in new_map.items()},
    "old_element": {k: v[0] for k, v in old_map.items()},
    "new_element": {k: v[0] for k, v in new_map.items()},
}
(W / "_t07_oldnew_map.json").write_text(json.dumps(out, ensure_ascii=False, indent=1),
                                        encoding="utf-8")
print()
print("da ghi .work/_t07_oldnew_map.json")
