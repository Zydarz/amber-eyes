#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sanh nhip (pacing) T2 EN: timeline CUOI (Higgs) vs timeline HEAD (git) + shots cu.

Ket qua: bang do dai moi shot, do lech moi cau, canh bao shot < 3 s hoac > 15 s (H10).
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8-sig"))

def git_show(path):
    r = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{path}"],
                       capture_output=True)
    if r.returncode != 0:
        return None
    return json.loads(r.stdout.decode("utf-8-sig"))

new = load(WORK / "timeline_s_EN_t02.json")
old = git_show(".work/timeline_s_EN_t02.json")
shots_old = load(WORK / "shots_EN_t02.json")

print("=" * 78)
print("TAP 02 EN — SO SANH NHIP: audio MiniMax (cu) vs audio Higgs (moi)")
print("=" * 78)

if old:
    print(f"OLD total = {old['total']:.1f}s   items = {len(old['items'])}")
    print(f"NEW total = {new['total']:.1f}s   items = {len(new['items'])}")
    print(f"CHENH LECH = {new['total'] - old['total']:+.1f}s "
          f"({(new['total']/old['total']-1)*100:+.1f}%)")
else:
    print("OLD timeline khong lay duoc tu git")

print("\n--- THEO HOI ---")
print(f"{'act':<5}{'OLD start':>10}{'OLD end':>10}{'OLD dur':>10}"
      f"{'NEW start':>11}{'NEW end':>10}{'NEW dur':>10}{'delta':>10}{'%':>8}")
for a in range(1, 6):
    ok = old and str(a) in old["acts"]
    nk = str(a) in new["acts"]
    if ok and nk:
        o = old["acts"][str(a)]
        n = new["acts"][str(a)]
        d = n[1] - n[0]
        print(f"act {a:<2}{o[0]:>10.1f}{o[1]:>10.1f}{o[1]-o[0]:>10.1f}"
              f"{n[0]:>11.1f}{n[1]:>10.1f}{d:>10.1f}{d-(o[1]-o[0]):>+10.1f}"
              f"{(d/(o[1]-o[0])-1)*100:>+8.1f}")
    elif nk:
        n = new["acts"][str(a)]
        print(f"act {a:<2}{'-':>10}{'-':>10}{'-':>10}{n[0]:>11.1f}{n[1]:>10.1f}"
              f"{n[1]-n[0]:>10.1f}")

print("\n--- DO DAI TUNG CAU (so voi len tieng goc) ---")
if old:
    om = {i["id"]: i for i in old["items"]}
    nm = {i["id"]: i for i in new["items"]}
    only_new = sorted(set(nm) - set(om))
    only_old = sorted(set(om) - set(nm))
    print(f"cau chi co moi: {len(only_new)} {only_new[:8]}")
    print(f"cau chi co cu  : {len(only_old)} {only_old[:8]}")
    common = [i for i in nm if i in om]
    nd = [nm[i]["end"] - nm[i]["start"] for i in common]
    od = [om[i]["end"] - om[i]["start"] for i in common]
    print(f"cau chung: {len(common)}")
    print(f"  thoi luong goc  TB {sum(od)/len(od):.2f}s  tong {sum(od):.1f}s")
    print(f"  thoi luong moi TB {sum(nd)/len(nd):.2f}s  tong {sum(nd):.1f}s")
    print(f"  ti le giai doan TB {(sum(nd)/sum(od)-1)*100:+.1f}%")
    short_old = sum(1 for d in od if d < 1.0)
    short_new = sum(1 for d in nd if d < 1.0)
    print(f"  cau < 1.0s:  cu {short_old}  ->  moi {short_new}")

    # per-act voice duration
    print("\n--- THOI LUONG LOI (theo hoi) ---")
    for a in range(1, 6):
        oc = sum(om[i]["end"] - om[i]["start"] for i in common if nm[i]["act"] == a)
        nc = sum(nm[i]["end"] - nm[i]["start"] for i in common if nm[i]["act"] == a)
        if oc:
            print(f"  act {a}: {oc:7.1f}s -> {nc:7.1f}s  ({(nc/oc-1)*100:+.1f}%)")

print("\n--- SHOT CU (tu 25/10, dua tren audio cu) ---")
print(f"shots.json total = {shots_old['total']}   so shot = {len(shots_old['shots'])}")
durs = [(s["end"] - s["start"], s["id"]) for s in shots_old["shots"]]
print(f"  dai nhat  {max(durs)[0]:.1f}s ({max(durs)[1]})   ngan nhat {min(durs)[0]:.1f}s ({min(durs)[1]})")
viol = [(d, i) for d, i in durs if d < 3.0 or d > 15.0]
print(f"  shot vi pham H10 (3-15s): {len(viol)}")
for d, i in sorted(viol)[:12]:
    print(f"     {i}  {d:.1f}s")
