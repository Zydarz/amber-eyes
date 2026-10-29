#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xác minh CHÍNH THỨC: parse file JA bằng parse_kichban rồi so với file VN.

Tiêu chí (theo đúng parser chính):
  1. số lượt (LOI) giống nhau
  2. số câu trong từng lượt giống nhau
  3. tổng số câu giống nhau
  4. số phần tử theo loại (LOI/SFX/BGM/NGHI) giống nhau
  5. mọi câu JA đều không rỗng và có dấu kết câu
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

WORK = Path(__file__).parent
OUT = WORK / "_ja_verify.txt"
lines = []
ok_ep = 0
bad_ep = 0


def parse(path):
    out = WORK / f"_vfy_{path.stem}.json"
    subprocess.run([sys.executable, str(WORK / "parse_kichban.py"), str(path), str(out)],
                   check=True, capture_output=True)
    els = json.loads(out.read_text(encoding="utf-8"))
    out.unlink()
    return els


for i in range(1, 30):
    ep = f"{i:02d}"
    ja_path = WORK.parent / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not ja_path.exists():
        lines.append(f"---  Tap{ep}: CHƯA CÓ file JA")
        bad_ep += 1
        continue
    vn = parse(M.canonical_vn(ep))
    ja = parse(ja_path)

    def by_kind(els):
        d = {}
        for e in els:
            d[e["kind"]] = d.get(e["kind"], 0) + 1
        return d

    kv, kj = by_kind(vn), by_kind(ja)
    lv = [e for e in vn if e["kind"] == "LOI"]
    lj = [e for e in ja if e["kind"] == "LOI"]
    sv = [len(e["sentences"]) for e in lv]
    sj = [len(e["sentences"]) for e in lj]
    tv, tj = sum(sv), sum(sj)

    problems = []
    if kv.get("LOI", 0) != kj.get("LOI", 0):
        problems.append(f"lượt: VN={kv.get('LOI')} JA={kj.get('LOI')}")
    if tv != tj:
        problems.append(f"tổng câu: VN={tv} JA={tj} (lệch {tj - tv})")
    if len(lv) == len(lj):
        diff = [(i + 1, a, b) for i, (a, b) in enumerate(zip(sv, sj)) if a != b]
        if diff:
            problems.append(f"lượt lệch câu: {diff[:8]}")
    for k in ("SFX", "BGM", "NGHI"):
        if kv.get(k, 0) != kj.get(k, 0):
            problems.append(f"{k}: VN={kv.get(k,0)} JA={kj.get(k,0)}")
    # câu JA rỗng
    empty = sum(1 for e in lj for s in e["sentences"] if not s["text"].strip())
    if empty:
        problems.append(f"câu rỗng: {empty}")
    # câu JA không có dấu kết câu
    noend = sum(1 for e in lj for s in e["sentences"]
                if not any(ch in s["text"] for ch in "。！？"))
    if noend:
        problems.append(f"câu không có 。？！: {noend}")

    if problems:
        bad_ep += 1
        lines.append(f"LỖI Tap{ep}: " + " | ".join(problems))
    else:
        ok_ep += 1
        lines.append(f"OK   Tap{ep}: {tv} câu / {len(lv)} lượt · "
                     f"SFX={kj.get('SFX',0)} BGM={kj.get('BGM',0)} NGHI={kj.get('NGHI',0)}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
print(f"\n==> {ok_ep}/{ok_ep + bad_ep} tập đạt · -> {OUT}")
