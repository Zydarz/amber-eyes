#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — kiểm tra cột "Chữ" của skeleton so với câu MỚI.

Với mỗi shot: tách "Chữ" thành các mảnh (bold / italic / quote), rồi kiểm mảnh
nào còn nằm trong câu mới của shot đó (bỏ qua khác biệt dấu câu/dấu tiếng Việt).

Cũng kiểm: số trên hình phải truy được về câu; trích dẫn phải nguyên văn.

Xuất: .work/_t04_textcheck.txt
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

W = ROOT / ".work"
NEW_KB = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026.md"

new_idx = {e["id"]: [(s["id"], s["text"]) for s in e.get("sentences", [])]
           for e in parse_file(str(NEW_KB)) if e["kind"] == "LOI"}
sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


def contains(frag, ctx):
    f, c = norm(frag), norm(ctx)
    if not f:
        return True
    if f in c:
        return True
    fw, cw = f.split(), c.split()
    for i in range(len(cw) - len(fw) + 1):
        if cw[i:i + len(fw)] == fw:
            return True
    return False


out = []
need = 0
for r in sk["rows"]:
    if r["kind"] != "shot":
        continue
    ctx = " ".join(t for eid, a, b in r["spans"] for _, t in new_idx[eid][a - 1:b])
    chu = r["cells"][5]
    frags = [(m.group(0), m.group(1) or m.group(2) or m.group(3))
             for m in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", chu)]
    bad = [t for _, t in frags if not contains(t, ctx)]
    # số trên hình
    nums = re.findall(r"\d[\d.,]*", chu)
    badnum = [n for n in nums if n.strip(".,") and not contains(n, ctx)]
    if bad or badnum:
        need += 1
    out.append({
        "sid": r["sid"], "from": r["from"], "el": r["el"],
        "spans": r["spans"], "chu_cu": chu, "ctx": ctx,
        "bad_frag": bad, "bad_num": badnum,
        "cells": r["cells"],
    })

json.dump(out, open(W / "_t04_textcheck.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
lines = []
for o in out:
    flag = "⚠" if (o["bad_frag"] or o["bad_num"]) else "✔"
    lines.append(f"{flag} {o['sid']} (từ {o['from']}) {o['el']} {o['spans'][0][1]}-{o['spans'][0][2]}")
    lines.append(f"    CHỮ CŨ: {o['chu_cu']}")
    if o["bad_frag"]:
        lines.append(f"    SAI: {o['bad_frag']}")
    if o["bad_num"]:
        lines.append(f"    SỐ SAI: {o['bad_num']}")
    lines.append(f"    CÂU: {o['ctx'][:600]}")
    lines.append("")
open(W / "_t04_textcheck.txt", "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print(f"shot: {len(out)} · cần viết lại: {need} · giữ được: {len(out) - need}")
