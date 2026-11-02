#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""(1) tim block SRT lo; (2) so chu in dam JA voi VN de kiem chung quy tac H6."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def blocks_of(p):
    txt = Path(p).read_bytes().decode("utf-8-sig", errors="replace").replace("\r\n", "\n")
    return [x for x in txt.strip().split("\n\n") if x.strip()]


print("=== 1. BLOCK SRT LO (JA moi) ===")
bl = blocks_of(ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt")
for n, b in enumerate(bl, 1):
    ls = b.splitlines()
    if len(ls) < 3 or " --> " not in ls[1]:
        print(f"  #{n} so dong={len(ls)}")
        print("     repr =", repr(b[:400]))
print(f"  tong block = {len(bl)}")

print("\n=== 2. SO CHU IN DAM: JA vs VN (cung quy tac H6) ===")


def bold_check(shots_file, tl_file, tag, strip_ja_punct=False):
    tl = json.loads(Path(tl_file).read_text(encoding="utf-8-sig"))
    sent = {it["id"]: it for it in tl["items"]}
    sh = json.loads(Path(shots_file).read_text(encoding="utf-8-sig"))["shots"]
    ok = bad = 0
    badlist = []
    for s in sh:
        if not s["sentences"]:
            continue
        txt = " ".join(sent[i]["text"] for i in s["sentences"])
        norm = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’()（）\-—–…]", "", t)
        ntxt = norm(txt)
        for seg in s["segments"]:
            for kind, val in seg["elems"]:
                if kind != "bold":
                    continue
                if norm(val) in ntxt:
                    ok += 1
                else:
                    bad += 1
                    badlist.append((s["id"], val, txt[:90]))
    print(f"  [{tag}] bold khop cau = {ok} · khong khop = {bad}")
    return badlist


bl_ja = bold_check(W / "shots_JA_t02.json", W / "timeline_s_JA_t02.json", "JA")
bl_vn = bold_check(W / "shots_t02.json", W / "timeline_s_t02.json", "VN")

print("\n  --- mau JA khong khop (15 dau) ---")
for sid, v, t in bl_ja[:15]:
    print(f"    {sid}: bold={v!r}")
    print(f"            cau = {t!r}")

print("\n  --- mau VN khong khop (8 dau) ---")
for sid, v, t in bl_vn[:8]:
    print(f"    {sid}: bold={v!r}")
    print(f"            cau = {t!r}")

print("\n=== 3. BAO CAO DO PHU % (chi giu dau, doi ky tu dac biet) ===")
for tag, sfile, tfile in [("JA", W / "shots_JA_t02.json", W / "timeline_s_JA_t02.json"),
                           ("VN", W / "shots_t02.json", W / "timeline_s_t02.json")]:
    tl = json.loads(Path(tfile).read_text(encoding="utf-8-sig"))
    sent = {it["id"]: it for it in tl["items"]}
    sh = json.loads(Path(sfile).read_text(encoding="utf-8-sig"))["shots"]
    n = sum(1 for s in sh for seg in s["segments"] for k, v in seg["elems"] if k == "bold")
    print(f"  {tag}: {n} doan chu in dam · {len(bl_ja if tag=='JA' else bl_vn)} doan khong khop nguyen van")
