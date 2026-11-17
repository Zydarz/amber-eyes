#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Danh sách shot dùng 32 nền vừa sinh lại (để render lại ảnh tĩnh + đo lại H9)."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT = WORK / "_t11" / "shots_changed.json"

V = {r["name"] for r in json.loads((WORK / "_t11" / "violations_t11.json").read_text(encoding="utf-8"))}

res = {}
for tag, f in [("vi", "shots_t11.json"), ("en", "shots_EN_t11.json"), ("ja", "shots_JA_t11.json")]:
    sh = json.loads((WORK / f).read_text(encoding="utf-8"))["shots"]
    ids = [s["id"] for s in sh if s.get("bg") in V]
    res[tag] = ids
    print(f"{tag}: {len(ids)}/223 shot dung nen doi")

allids = sorted(set(res["vi"]) | set(res["en"]) | set(res["ja"]))
print(f"union: {len(allids)} shot")
res["union"] = allids
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"ghi {OUT.relative_to(ROOT)}")
