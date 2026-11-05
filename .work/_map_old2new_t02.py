# -*- coding: utf-8 -*-
"""Lập bản đồ dòng shot CŨ -> MỚI của bảng shot VN tập 2, để mang lớp phủ chữ EN/JA sang bảng mới.

Cách khớp: theo tập câu mà dòng phủ (chuỗi id câu `1.03#1`...).
Dòng không lời ("giữ ...") khớp theo vị trí tương đối trong cùng hồi.
"""
import re, json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r'D:/TEST/Gax/amber-eyes')
OLD = ROOT / ".work/_cu/shot_table_t02_20261105_135553/KeHoach_Video_Tap02.md"
NEW = ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md"


def read_rows(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    i0 = next(i for i, l in enumerate(lines) if l.startswith("## 6. DANH SÁCH SHOT"))
    i1 = next(i for i, l in enumerate(lines) if i > i0 and l.startswith("**Tổng:"))
    rows = []
    for l in lines[i0:i1 + 1]:
        m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
        if not m:
            continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        rows.append(dict(sid=m.group(1), cells=c, raw=l))
    return rows


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


old = read_rows(OLD)
new = read_rows(NEW)
print(f"OLD rows = {len(old)}   NEW rows = {len(new)}")

# index theo tập câu
old_by_key = {}
for r in old:
    k = tuple(sents(r['cells'][1]))
    old_by_key.setdefault(k, []).append(r)

exact, changed, nomatch = [], [], []
for r in new:
    k = tuple(sents(r['cells'][1]))
    cand = old_by_key.get(k)
    if not cand:
        nomatch.append(r)
        continue
    o = cand.pop(0)
    if o['cells'][5].strip() == r['cells'][5].strip() and o['cells'][6].strip() == r['cells'][6].strip():
        exact.append((o, r))
    else:
        changed.append((o, r))

print(f"\nKhop y nguyen (chữ+beat giong) : {len(exact)}")
print(f"Khop cau nhung chu/beat DOI       : {len(changed)}")
print(f"KHONG khop (cau moi)              : {len(nomatch)}")

# dòng cũ không được dùng
used_old = {o['sid'] for o, _ in exact + changed}
unused = [r for r in old if r['sid'] not in used_old]
print(f"Dong OLD bi bo (khong con dung)   : {len(unused)}")

json.dump(
    {
        "exact": [[o['sid'], r['sid']] for o, r in exact],
        "changed": [[o['sid'], r['sid']] for o, r in changed],
        "nomatch": [r['sid'] for r in nomatch],
        "unused_old": [r['sid'] for r in unused],
    },
    open(ROOT / ".work/_old2new_t02.json", "w", encoding="utf-8"),
    ensure_ascii=False, indent=1)

print("\n=== DANH SACH DONG CHU/ BEAT DOI ===")
for o, r in changed:
    print(f"\n[{o['sid']} -> {r['sid']}]  cau: {o['cells'][1]}  ==> {r['cells'][1]}")
    print(f"  CHU cu : {o['cells'][5]}")
    print(f"  CHU moi: {r['cells'][5]}")
    if o['cells'][6] != r['cells'][6]:
        print(f"  BEAT cu: {o['cells'][6]}")
        print(f"  BEAT moi: {r['cells'][6]}")

print("\n=== DONG KHONG KHOP (can viet lai) ===")
for r in nomatch:
    print(f"  [{r['sid']}] {r['cells'][1]} | CHU: {r['cells'][5][:120]}")

print("\n=== DONG CU BI BO ===")
for r in unused:
    print(f"  [{r['sid']}] {r['cells'][1]} | CHU: {r['cells'][5][:110]}")
