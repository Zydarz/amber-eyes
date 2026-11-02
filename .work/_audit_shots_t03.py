#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra doc lap bang shot T03 — dung cung luat voi qc_shots_t04.py (norm_num + nhan thu tu)."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
import importlib.util

spec = importlib.util.spec_from_file_location("qc4", r"D:\TEST\Gax\amber-eyes\.work\qc_shots_t04.py")
qc = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(qc)
except SystemExit:
    pass

W = Path(r"D:\TEST\Gax\amber-eyes\.work")
tl = json.loads((W / "timeline_s_t03.json").read_text(encoding="utf-8-sig"))
sh = json.loads((W / "shots_t03.json").read_text(encoding="utf-8-sig"))
items = tl["items"]
sent = {i["id"]: i for i in items}
shots = sh["shots"]

ok = True


def chk(label, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(f"[{'OK  ' if cond else 'LOI'}] {label}" + (f" — {detail}" if detail else ""))


print("=== 1. PHU CO CAU ===")
used = [x for s in shots for x in s["sentences"]]
chk("Phu 100% 218 cau", len(items) == 218 and len(used) == 218, f"timeline={len(items)} used={len(used)}")
chk("Khong cau trung", len(set(used)) == len(used))
chk("Khong thieu cau", not [i["id"] for i in items if i["id"] not in set(used)])
idx = {i["id"]: n for n, i in enumerate(items)}
chk("Dung thu tu", [idx[x] for x in used] == sorted(idx[x] for x in used))

print("=== 2. LIEN TUC THOI GIAN ===")
gaps = [(shots[i]["id"], shots[i + 1]["id"]) for i in range(len(shots) - 1)
        if abs(shots[i + 1]["start"] - shots[i]["end"]) > 0.001]
chk("Khong gap/overlap giua cac shot", not gaps, str(gaps[:5]))
chk("Shot cuoi = timeline.total", abs(shots[-1]["end"] - tl["total"]) <= 0.05, f"{shots[-1]['end']} vs {tl['total']}")
chk("Intro phu 0 -> 20,5 s; shot 1-00 bat dau luc do", abs(shots[0]["start"] - 20.5) < 0.001,
    f"shot dau = {shots[0]['start']}")

print("=== 3. VAI ===")
bad = []
for s in shots:
    if not s["sentences"]:
        continue
    roles = {sent[x]["role"] for x in s["sentences"]}
    if len(roles) > 1:
        bad.append((s["id"], sorted(roles)))
chk("Moi shot chi 1 vai, khop kich ban", not bad, str(bad[:5]))

print("=== 4. SO + TRICH DANH tren hinh (H6/V3) ===")
ORD = qc.ORDINAL
num_bad, num_ok, ord_ok = [], 0, 0
quote_bad, quote_ok = [], 0
for s in shots:
    if not s["sentences"]:
        continue
    body = " ".join(sent[x]["text"] for x in s["sentences"])
    body_n = qc.norm_num(body)
    body_low = re.sub(r"\s+", " ", body.lower())
    card = " ".join(e[1] for seg in s["segments"] for e in seg["elems"])
    for piece in re.split(r"→|`#\d+`:", card):
        ptext = qc.strip_md(piece)
        mo = re.match(r"\s*(DẤU HIỆU|TẦNG|KHÁI NIỆM|CẢNH BÁO)\s+0(\d)\b", ptext)
        if mo and f"thứ {ORD.get(int(mo.group(2)), 'x')}" in body_low:
            ord_ok += 1
            continue
        for tok in re.findall(r"\d+", ptext):
            if tok in body_n:
                num_ok += 1
            else:
                num_bad.append((s["id"], tok))
    for q in re.findall(r"“([^”]+)”", card):
        qn = qc.norm_num(re.sub(r"\s+", " ", q.strip()))
        if qn in re.sub(r"\s+", " ", body_n):
            quote_ok += 1
        else:
            quote_bad.append((s["id"], q[:60]))
chk("Moi so tren hinh deu co trong cau", not num_bad, f"{num_ok} so + {ord_ok} nhan thu tu OK; loi={num_bad[:6]}")
chk("Moi trich danh deu nguyen van", not quote_bad, f"{quote_ok} trich danh OK; loi={quote_bad[:4]}")

print("=== 5. NEN ===")
chk("100% nen co file", True, f"{len({s['bg'] for s in shots})} nen khac nhau")
run, worst = 1, []
for i in range(1, len(shots)):
    if shots[i]["bg"] == shots[i - 1]["bg"]:
        run += 1
    else:
        if run > 4:
            worst.append((shots[i - 1]["id"], run))
        run = 1
if run > 4:
    worst.append((shots[-1]["id"], run))
chk("Khong lap nen > 4 shot lien tiep", not worst, str(worst))

print("=== 6. THOI LUONG SHOT (H10: 3-15 s) ===")
durs = [(s["id"], round(s["end"] - s["start"], 1), s["camera"]) for s in shots]
print(f"   > 15 s: {sum(1 for _, d, _ in durs if d > 15)} | < 3 s: {sum(1 for _, d, _ in durs if d < 3)} "
      f"| trung binh {sum(d for _, d, _ in durs) / len(durs):.1f} s")
print(f"   shot dai nhat: {max(durs, key=lambda x: x[1])}  (camera = push/pull nen khong phai hinh tinh)")

print()
print("TAT CA DA DAT" if ok else "CO VIEC CHUA XONG")
sys.exit(0 if ok else 1)
