#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chon ban Higgs tot nhat cho tung cau T04 (§7) + danh sach can vong 2 (P8).

- moi cau co 2 bien (variant 0/1) x 2 luot ASR; rows giu CER = luot XAU HON
- chon bien co CER nho nhat
- cau vong 2 = (CER tot nhat > 2%) HOAC bi loai boi kiem tra F0 (semitone)
Xuat:
  .work/higgs_selection_t04.json   {id: variant}
  .work/higgs_round2_t04.json      danh sach id can sinh lai
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
W = ROOT / ".work"
THRESH = 0.02

rows = json.loads((W / "higgs_cer_rows_t04.json").read_text(encoding="utf-8-sig"))
by_id = {}
for r in rows:
    by_id.setdefault(r["id"], []).append(r)

excl = set()
p = W / "higgs_exclude_f0_t04.json"
if p.exists():
    ex = json.loads(p.read_text(encoding="utf-8-sig"))
    files = {e if isinstance(e, str) else e.get("file") for e in ex}
    for r in rows:
        if r["file"] in files:
            excl.add(r["id"])

sel, r2, stat = {}, [], []
for sid, lst in sorted(by_id.items()):
    ok = [r for r in lst if r.get("cer_ok") and r.get("cer") is not None]
    if not ok:
        r2.append(sid)
        stat.append((sid, None, "KHONG CO CER"))
        continue
    best = min(ok, key=lambda r: (r["cer"], r["duration_s"]))
    sel[sid] = best["variant"]
    c = best["cer"]
    flag = ""
    if c > THRESH:
        flag = "CER"
        r2.append(sid)
    if sid in excl:
        flag = (flag + "+F0").strip()
        if sid not in r2:
            r2.append(sid)
    stat.append((sid, c, flag))

n = len(stat)
nc = sum(1 for s in stat if s[2].startswith("CER"))
nf = sum(1 for s in stat if "F0" in s[2])
print("so cau:", n)
print("CER tot nhat > 2%%: %d (%.1f%%)" % (nc, nc / n * 100))
print("bi loai F0: %d" % nf)
print("can vong 2 (P8): %d" % len(r2))
print("duong cong CER tot nhat: %.2f%%" % (sum(s[1] for s in stat if s[1] is not None) / n * 100))
mx = max(stat, key=lambda s: (s[1] if s[1] is not None else -1))
print("worst best-CER:", mx[0], round((mx[1] or 0) * 100, 2), "%", mx[2])

# theo vai
by_role = {}
for sid, lst in by_id.items():
    best = min([r for r in lst if r.get("cer_ok") and r.get("cer") is not None],
               key=lambda r: r["cer"], default=None)
    if best:
        by_role.setdefault(best["role"], []).append(best["cer"])
print("\nCER tot nhat theo vai:")
for role, cs in sorted(by_role.items()):
    over = sum(1 for c in cs if c > THRESH)
    print("  %-3s n=%3d  tb=%.2f%%  max=%.1f%%  >2%%: %d"
          % (role, len(cs), sum(cs) / len(cs) * 100, max(cs) * 100, over))

(W / "higgs_selection_t04.json").write_text(
    json.dumps(sel, ensure_ascii=False, indent=1), encoding="utf-8")
(W / "higgs_round2_t04.json").write_text(
    json.dumps(sorted(r2), ensure_ascii=False, indent=1), encoding="utf-8")
print("\n-> .work/higgs_selection_t04.json (%d cau)" % len(sel))
print("-> .work/higgs_round2_t04.json (%d cau)" % len(r2))
print("danh sach vong 2:", " ".join(sorted(r2)))
