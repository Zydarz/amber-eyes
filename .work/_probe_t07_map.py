#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In cau truc script_tap07.json (moi) + timeline_s_t07.json + shots_t07.json (cu)."""
import json
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


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8-sig"))


new = load(W / "script_tap07.json")
old_raw = subprocess.run(["git", "show", "HEAD:.work/script_tap07.json"],
                         cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
old = json.loads(old_raw.stdout) if old_raw.returncode == 0 else None

print("### SCRIPT MOI: %d item" % len(new))
for it in new[:6]:
    print(json.dumps(it, ensure_ascii=False)[:700])
print("...")
print("kinds:", sorted({it.get("kind") for it in new}))

print()
print("### SCRIPT CU (git HEAD): %s" % (len(old) if old else "KHONG DOC DUOC"))
if old:
    for it in old[:4]:
        print(json.dumps(it, ensure_ascii=False)[:700])

print()
print("### TIMELINE")
tl = load(W / "timeline_s_t07.json")
print("keys:", list(tl.keys()))
print("items:", len(tl["items"]), "markers:", len(tl["markers"]))
print("item0:", json.dumps(tl["items"][0], ensure_ascii=False)[:400])
print("marker0:", json.dumps(tl["markers"][0], ensure_ascii=False)[:300])
print("total:", tl.get("total"), "intro:", tl.get("intro"))
print("items[-1]:", json.dumps(tl["items"][-1], ensure_ascii=False)[:400])

print()
print("### SHOTS CU")
sh = load(W / "shots_t07.json")
print("keys:", list(sh.keys()), "n_shots:", len(sh["shots"]))
print("shot0:", json.dumps(sh["shots"][0], ensure_ascii=False)[:600])
print("shot[-1]:", json.dumps(sh["shots"][-1], ensure_ascii=False)[:600])

print()
print("### DANH SACH ID CU (shot -> sentences)")
for s in sh["shots"]:
    print(f"{s['id']:>6} | act{s['act']} | role={s['role']} | bg={s['bg']} | "
          f"{s['sentences'][0] if s['sentences'] else '-'} .. "
          f"{s['sentences'][-1] if s['sentences'] else '-'} | n={len(s['sentences'])}")
