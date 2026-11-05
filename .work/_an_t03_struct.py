#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A2 — structural diff old vs new Tap03 script (JSON) + raw markdown stats.

Answers: did the rewrite add spoken content? did roles/kinds/durations change?
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"


def load_json_git(path):
    out = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=ROOT, capture_output=True)
    return json.loads(out.stdout.decode("utf-8"))


old = load_json_git(".work/script_tap03.json")
new = json.loads((W / "script_tap03.json").read_text(encoding="utf-8"))

print("=" * 72)
print("1) SO SÁNH CẤU TRÚC ELEMENT (JSON đã parse)")
print("=" * 72)
om = {e["id"]: e for e in old}
nm = {e["id"]: e for e in new}
role_ch, kind_ch, sec_ch, desc_ch = [], [], [], []
for eid in sorted(set(om) | set(nm)):
    o, n = om.get(eid), nm.get(eid)
    if not o or not n:
        print(f"  {eid}: THIẾU Ở MỘT BÊN")
        continue
    if o.get("role") != n.get("role"):
        role_ch.append((eid, o.get("role"), n.get("role")))
    if o.get("kind") != n.get("kind"):
        kind_ch.append((eid, o.get("kind"), n.get("kind")))
    if o.get("sec") != n.get("sec"):
        sec_ch.append((eid, o.get("sec"), n.get("sec")))
    if o.get("desc") != n.get("desc"):
        desc_ch.append(eid)
print(f"ĐỔI VAI      : {len(role_ch)} {role_ch}")
print(f"ĐỔI KIND     : {len(kind_ch)} {kind_ch}")
print(f"ĐỔI THỜI LƯỜNG NGHỈ: {len(sec_ch)} {sec_ch}")
print(f"ĐỔI DESC(BGM/SFX): {len(desc_ch)} {desc_ch}")

print("\n--- phân bố vai (số câu) ---")


def dist(els):
    d = {}
    for e in els:
        for s in (e.get("sentences") or []):
            d[e.get("role") or "?"] = d.get(e.get("role") or "?", 0) + 1
    return d


do, dn = dist(old), dist(new)
for k in sorted(set(do) | set(dn)):
    print(f"  {k:<3} cũ={do.get(k,0):<4} mới={dn.get(k,0):<4} {'<<< ĐỔI' if do.get(k,0) != dn.get(k,0) else ''}")

print("\n--- tổng số từ trong phần lời đọc ---")
for tag, els in (("CŨ ", old), ("MỚI", new)):
    w = sum(s["words"] for e in els for s in (e.get("sentences") or []))
    c = sum(len(s["text"]) for e in els for s in (e.get("sentences") or []))
    print(f"  {tag}: {w} từ · {c} ký tự · {sum(len(e.get('sentences') or []) for e in els)} câu")

print("\n" + "=" * 72)
print("2) THỐNG KÊ MARKDOWN THÔ (file nguồn)")
print("=" * 72)
md = "01_KICH_BAN/Tap03/kichban_tap03_22102026.md"
old_md = subprocess.run(["git", "show", f"HEAD:{md}"], cwd=ROOT, capture_output=True).stdout.decode("utf-8")
new_md = (ROOT / md).read_text(encoding="utf-8")


def md_stats(t, tag):
    lines = t.splitlines()
    spoken = [l for l in lines if l.lstrip().startswith(("HOST", "ĐẶC VỤ", "CHUYÊN GIA", "CẢNH SÁT", '"', "'"))]
    ends = len(re.findall(r"[.!?…](?=\s|$|[\"'])", t))
    print(f"  {tag}: {len(t)} ký tự · {len(t.split())} từ (split thô) · {len(lines)} dòng · {ends} dấu kết câu")


md_stats(old_md, "CŨ ")
md_stats(new_md, "MỚI")

print("\n--- các element có câu đổi (kiểm lại bằng chuỗi câu) ---")
of = {s["id"]: s["text"] for e in old for s in (e.get("sentences") or [])}
nf = {s["id"]: s["text"] for e in new for s in (e.get("sentences") or [])}
chg = [k for k in nf if of.get(k) != nf[k]]
for k in chg:
    a, b = of.get(k, ""), nf[k]
    # bỏ dấu nháy để xem có khác nội dung thật không
    norm = lambda s: re.sub(r"[\"'\u201c\u201d]", "", s).strip()
    print(f"  {k}: {'CHỈ KHÁC DẤU NHÁY' if norm(a) == norm(b) else 'KHÁC NỘI DUNG THẬT'}")
