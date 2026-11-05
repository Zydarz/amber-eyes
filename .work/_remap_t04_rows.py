#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — dựng lại bảng shot VN cho kịch bản MỚI.

Cơ chế:
  1. Đọc bảng shot VN cũ (83 dòng) + kịch bản cũ + kịch bản mới.
  2. Căn chỉnh câu cũ ↔ câu mới bằng difflib ở mức KÝ TỰ (char-level).
  3. Mỗi dòng shot cũ (phủ câu cũ a..b) ⇒ dòng mới phủ câu mới tương ứng.
  4. Câu mới không có dòng nào phủ ⇒ in ra để tác giả bổ sung dòng mới.
  5. Kiểm tra cột "Chữ" cũ: mảnh nào còn nằm trong câu mới (giữ), mảnh nào không (cần viết lại).

Xuất: .work/_t04_rowmap.json  (skeleton dòng mới + cờ cần viết lại chữ)
      .work/_t04_rowmap.txt   (báo cáo đọc được)
"""
import difflib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

PLAN = ROOT / "02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md"
OLD_KB = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026_ban_goc.md"
NEW_KB = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026.md"
W = ROOT / ".work"


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def index(els):
    d = {}
    for el in els:
        if el["kind"] == "LOI":
            d[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]
    return d


old_idx = index(parse_file(str(OLD_KB)))
new_idx = index(parse_file(str(NEW_KB)))


def align(old_sents, new_sents):
    """Căn chỉnh 2 list câu (char-level) -> dict old_i -> new_i."""
    def cat(lst):
        parts, offs, pos = [], [], 0
        for i, (_, t) in enumerate(lst):
            offs.append((pos, pos + len(t)))
            parts.append(t)
            pos += len(t) + 1
        return " ".join(parts), offs

    o_txt, o_off = cat(old_sents)
    n_txt, n_off = cat(new_sents)

    def locate(offs, a, b):
        for i, (s, e) in enumerate(offs):
            if a < e and b > s:
                return i
        return None

    sm = difflib.SequenceMatcher(None, o_txt, n_txt, autojunk=False)
    out = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            continue
        oi = locate(o_off, i1, i2)
        nj = locate(n_off, j1, j2)
        if oi is not None and nj is not None:
            out.setdefault(oi, nj)
    return out


# ---- đọc bảng shot cũ
text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[:re.search(r"^\*\*Tổng:", sec, re.M).start()]
raw_rows = [cells(l) for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]

# ---- gom dòng theo element
rows_by_el = {}
order = []
for r in raw_rows:
    sid = r[0]
    ids = re.findall(r"`(\d)\.(\d+)(?:#(\d+))?`", r[1])
    el = f"{ids[0][0]}.{ids[0][1]}" if ids else None
    if el is None:
        order.append((sid, r, None, None, None))
        continue
    rng = re.findall(r"`(\d\.\d+)#(\d+)`(?:\s*[–-]\s*`?#(\d+)`?)?", r[1])
    spans = []
    for ma, a, b in rng:
        spans.append((ma, int(a), int(b or a)))
    order.append((sid, r, el, spans, None))

# ---- ánh xạ câu cũ -> mới
mapping = {}          # "eid#old_i" -> new_i
for eid in sorted(old_idx, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]))):
    o = old_idx[eid]
    n = new_idx.get(eid, [])
    if not n:
        continue
    al = align(o, n)
    for oi, nj in al.items():
        mapping[f"{eid}#{oi + 1}"] = nj + 1

covered_new = set()
out_rows = []
for sid, r, el, spans, _ in order:
    if el is None:
        out_rows.append({"sid": sid, "kind": "meta", "row": r, "el": None,
                         "spans": None, "new_spans": None, "need_text": False})
        continue
    new_spans = []
    for eid, a, b in spans:
        mj = [mapping.get(f"{eid}#{i}") for i in range(a, b + 1)]
        mj = [x for x in mj if x]
        if mj:
            new_spans.append((eid, min(mj), max(mj)))
        else:
            new_spans.append((eid, None, None))
    for eid, na, nb in new_spans:
        if na:
            for k in range(na, nb + 1):
                covered_new.add(f"{eid}#{k}")
    out_rows.append({"sid": sid, "kind": "shot", "row": r, "el": el,
                     "spans": spans, "new_spans": new_spans, "need_text": False})

all_new = {f"{eid}#{i + 1}" for eid, v in new_idx.items() for i in range(len(v))}
missing = sorted(all_new - covered_new, key=lambda x: (int(x.split(".")[0]),
                                                       int(x.split("#")[0].split(".")[1]),
                                                       int(x.split("#")[1])))

# ---- kiểm tra cột Chữ cũ: mảnh nào còn trong câu mới
def norm(s):
    s = s.lower()
    s = re.sub(r"[^\w\sđáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ\s]", " ", s)
    return " ".join(s.split())


def frag_ok(frag, ctx):
    f = norm(frag)
    if not f:
        return True
    c = norm(ctx)
    if f in c:
        return True
    # cho phép sai khác dấu cách / dấu câu: thử khớp theo từ
    fw, cw = f.split(), c.split()
    for i in range(len(cw) - len(fw) + 1):
        if cw[i:i + len(fw)] == fw:
            return True
    return False


report = []
for row in out_rows:
    if row["kind"] != "shot":
        continue
    ctx = " ".join(t for eid, na, nb in (row["new_spans"] or []) if na
                   for _, t in new_idx.get(eid, [])[na - 1:nb])
    chu = row["row"][5] if len(row["row"]) > 5 else ""
    if chu.strip() in ("", "—"):
        row["ctx"] = ctx
        continue
    frags = [m.group(0) for m in re.finditer(r"\*\*.+?\*\*|\*.+?\*|“.+?”", chu)]
    bad = [f for f in frags if not frag_ok(f, ctx)]
    row["ctx"] = ctx
    row["need_text"] = bool(bad)
    row["bad_frags"] = bad
    if bad:
        report.append((row["sid"], row["el"], row["new_spans"], bad, ctx))

json.dump({"rows": out_rows, "missing": missing,
           "mapping": mapping},
          open(W / "_t04_rowmap.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print(f"dòng cũ: {len(raw_rows)} · câu mới: {len(all_new)} · đã phủ: {len(covered_new)}")
print(f"câu mới CHƯA có dòng: {len(missing)}")
print("   " + ", ".join(missing))
print(f"\ndòng cần viết lại cột Chữ: {len(report)}/{len(out_rows)}")
with open(W / "_t04_rowmap.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(f"dòng cũ: {len(raw_rows)} · câu mới: {len(all_new)} · đã phủ: {len(covered_new)}\n")
    f.write(f"câu mới CHƯA có dòng ({len(missing)}): {missing}\n\n")
    for row in out_rows:
        if row["kind"] == "shot":
            f.write(f"--- {row['sid']} el={row['el']} spans={row['spans']} -> {row['new_spans']}\n")
            f.write(f"    CHỮ CŨ: {row['row'][5][:220]}\n")
            f.write(f"    CÂU MỚI: {row['ctx'][:400]}\n")
            if row.get("bad_frags"):
                f.write(f"    ⚠ SAI: {row['bad_frags']}\n")
