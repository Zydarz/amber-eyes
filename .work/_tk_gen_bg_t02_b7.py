# -*- coding: utf-8 -*-
"""Sinh 5 nen AI con lai (batch 7) - chay lai duoc, khong ghi de file cu."""
import io, json, os, sys, time
sys.path.insert(0, r"D:/TEST/Gax/amber-eyes/.work")
from _tk_gen_bg_t02 import PAIRS, RAW, ROOT, build, generate, summarize, upload

todo = [p for p in PAIRS if p[0] in
        ("tk02_gavel", "tk02_uniform_fire", "tk02_red_flags", "tk02_town_snow", "tk02_cottage_search")]
reqs = []
for name, ref in todo:
    p = os.path.join(RAW, ref)
    if not os.path.exists(p):
        print("THIEU:", p)
        continue
    u = upload(p)
    if not u:
        print("UPLOAD FAIL", ref)
        continue
    reqs.append(build(name, ref, u))
    print("upload ok:", ref)
if not reqs:
    sys.exit(1)
rc, j = generate(reqs, "t02_b7")
print("rc=", rc)
print(summarize(j))
