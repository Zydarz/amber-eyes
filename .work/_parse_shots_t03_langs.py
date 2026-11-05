#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — parse lại bảng shot cho 3 ngôn ngữ, so với bản đang dùng.

Cho biết bảng shot trong hồ sơ có khớp với bản đang render không
(JA: bảng shot được viết lại 04/11 sau lần render 03/11).

Dùng:  py -3 .work/_parse_shots_t03_langs.py
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BK = WORK / "_cu" / "t03_20261105_1800"

LANGS = [
    ("vi", "", "shots_t03.json"),
    ("en", "en", "shots_EN_t03.json"),
    ("ja", "ja", "shots_JA_t03.json"),
]

FIELDS = ["id", "act", "start", "end", "bg", "template", "role", "text", "beat", "nv"]

bad = 0
for lang, ae, name in LANGS:
    print("=" * 72)
    print(f"[{lang}] parse_shots AE_EP=03 AE_LANG={ae or '(vi)'}")
    env = dict(os.environ)
    env["AE_EP"] = "03"
    env["AE_LANG"] = ae
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, str(WORK / "parse_shots.py")],
                       cwd=ROOT, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    out = ((r.stdout or "") + (r.stderr or "")).strip()
    print("  " + "\n  ".join(out.splitlines()[-8:]))
    if r.returncode != 0:
        print("  ⚠ PARSE LỖI rc=", r.returncode)
        bad += 1
        continue

    new = json.loads((WORK / name).read_text(encoding="utf-8"))
    old = json.loads((BK / name).read_text(encoding="utf-8"))

    ns, os_ = new["shots"], old["shots"]
    print(f"  shot: mới {len(ns)} · backup {len(os_)} · total {new['total']} vs {old['total']}")
    if len(ns) != len(os_):
        print("  ⚠ SỐ SHOT KHÁC NHAU")
        bad += 1
        continue

    diffs = []
    for a, b in zip(ns, os_):
        for f in FIELDS:
            if f in a and f in b and a[f] != b[f]:
                diffs.append((a["id"], f, b[f], a[f]))
    if not diffs:
        print("  ✔ bảng shot y hệt bản đang dùng → ảnh tĩnh hiện tại vẫn đúng")
    else:
        print(f"  ⚠ {len(diffs)} trường KHÁC trong {len({d[0] for d in diffs})} shot:")
        for sid, f, ov, nv in diffs[:25]:
            print(f"     {sid}.{f}\n        cũ : {str(ov)[:150]}\n        mới: {str(nv)[:150]}")

print("=" * 72)
print("KẾT LUẬN:", "3 bản shot giống hệt bản đang dùng" if bad == 0 else "CÓ KHÁC BIỆT — cần render lại")
