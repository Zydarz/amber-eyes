#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A3 — old(HEAD) vs new script diff for EN / JA / KO Tap03."""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]


def flat(els):
    d = {}
    for e in els:
        for s in (e.get("sentences") or []):
            d[s["id"]] = s["text"]
    return d


def norm(s):
    return re.sub(r"[\"\u201c\u201d\u2018\u2019]", "", s).strip()


for lang, suf in (("EN", "_EN"), ("JA", "_JA"), ("KO", "_KO")):
    p = f".work/script_tap03{suf}.json"
    r = subprocess.run(["git", "show", f"HEAD:{p}"], cwd=ROOT, capture_output=True)
    if not r.stdout:
        print(f"{lang}: HEAD KHÔNG CÓ file này (chưa từng commit)")
        continue
    try:
        old = json.loads(r.stdout.decode("utf-8"))
    except Exception as e:
        print(f"{lang}: HEAD parse lỗi {e}")
        continue
    new = json.loads((ROOT / f".work/script_tap03{suf}.json").read_text(encoding="utf-8"))
    o, n = flat(old), flat(new)
    chg = [k for k in n if k in o and o[k] != n[k]]
    real = [k for k in chg if norm(o[k]) != norm(n[k])]
    onlyq = [k for k in chg if k not in real]
    added = [k for k in n if k not in o]
    removed = [k for k in o if k not in n]
    print(f"{lang}: HEAD={len(o)} câu | MỚI={len(n)} câu | đổi={len(chg)} "
          f"(nội dung thật={len(real)}, chỉ dấu nháy={len(onlyq)}) | câu mới={len(added)} | câu mất={len(removed)}")
    if real:
        print(f"    đổi thật: {real[:10]}")
    if added:
        print(f"    mới: {added[:10]}")
    if removed:
        print(f"    mất: {removed[:10]}")
    # role/kind change
    om = {e["id"]: e for e in old}
    nm = {e["id"]: e for e in new}
    rc = [(k, om[k].get("role"), nm[k].get("role")) for k in om if k in nm and om[k].get("role") != nm[k].get("role")]
    kc = [(k, om[k].get("kind"), nm[k].get("kind")) for k in om if k in nm and om[k].get("kind") != nm[k].get("kind")]
    print(f"    đổi vai: {len(rc)} {rc[:6]} | đổi kind: {len(kc)} {kc[:6]}")
