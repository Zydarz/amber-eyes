#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — dựng skeleton bảng shot MỚI (bản chuẩn hoá) cho kịch bản MỚI.

Nguyên tắc:
  * Giữ nguyên thiết kế hình ảnh cũ: nền, mẫu, vai, beat, nhân vật, trạng thái.
  * Chia lại câu theo kịch bản mới: mỗi shot cũ nhận số câu tỉ lệ với số câu cũ,
    rồi TÁCH thêm dòng nếu vượt MAX_SENT (giữ nhịp hình ~3-15 s).
  * Shot ID đánh số lại liên tục theo hồi (N-NN) — QC đọc bằng int().
  * Xuất bản đồ old_id -> new_id để remap cấu hình theo shot ID (text_scrim...).

Dùng:  py -3 .work/_skeleton_t04.py [MAX_SENT]
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

MAX_SENT = int(sys.argv[1]) if len(sys.argv) > 1 else 3
PLAN = ROOT / "02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md"
NEW_KB = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026.md"
W = ROOT / ".work"


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


new_els = parse_file(str(NEW_KB))
new_idx = {e["id"]: [(s["id"], s["text"]) for s in e.get("sentences", [])]
           for e in new_els if e["kind"] == "LOI"}

text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[:re.search(r"^\*\*Tổng:", sec, re.M).start()]
old_rows = [cells(l) for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]


def row_spans(cau):
    return [(ma, int(a), int(b or a)) for ma, a, b in
            re.findall(r"`(\d\.\d+)#(\d+)`(?:\s*[–-]\s*`?#(\d+)`?)?", cau)]


groups, cur_el, cur_rows = [], None, []
for r in old_rows:
    spans = row_spans(r[1])
    if spans:
        eid = spans[0][0]
        if eid != cur_el:
            if cur_el is not None:
                groups.append(("el", cur_el, cur_rows))
            cur_el, cur_rows = eid, []
        cur_rows.append((r, spans))
    else:
        if cur_el is not None:
            groups.append(("el", cur_el, cur_rows))
            cur_el, cur_rows = None, []
        groups.append(("meta", r, None))
if cur_el is not None:
    groups.append(("el", cur_el, cur_rows))

# ---------------- đánh số lại: dòng đầu hồi 1 giữ "1-00" ----------------
act_counters = {}
out_rows = []
idmap = {}          # old_id -> new_id (dòng đầu của nhóm tách)


def new_id(act):
    act_counters[act] = act_counters.get(act, 0) + 1
    return f"{act}-{act_counters[act]:02d}"


first_of_act = set()
for kind, payload, extra in groups:
    if kind == "meta":
        r = payload
        act = int(r[0].split("-")[0])
        if act not in first_of_act:
            first_of_act.add(act)
            sid = "1-00" if (act == 1 and r[0] == "1-00") else new_id(act)
        else:
            sid = new_id(act)
        out_rows.append({"sid": sid, "kind": "meta", "cells": r, "el": None,
                         "spans": [], "from": r[0]})
        continue

    eid, rows = payload, extra
    N = len(new_idx.get(eid, []))
    counts = [sum(b - a + 1 for _, a, b in sp) for _, sp in rows]
    M = sum(counts) or 1
    raw = [c * N / M for c in counts]
    alloc = [max(1, int(round(x))) for x in raw]
    while sum(alloc) > N:
        i = max(range(len(alloc)), key=lambda k: alloc[k] - raw[k])
        if alloc[i] <= 1:
            break
        alloc[i] -= 1
    while sum(alloc) < N:
        i = min(range(len(alloc)), key=lambda k: raw[k] - alloc[k])
        alloc[i] += 1
    while sum(alloc) > N:
        j = max(range(len(alloc)), key=lambda k: alloc[k])
        if alloc[j] <= 1:
            break
        alloc[j] -= 1
    assert sum(alloc) == N, f"{eid}: {sum(alloc)} != {N}"

    pos = 1
    act = int(eid.split(".")[0])
    for (r, spans), k in zip(rows, alloc):
        a = pos
        pos += k
        left, cur = k, a
        parts = []
        while left > 0:
            take = min(MAX_SENT, left)
            parts.append((cur, cur + take - 1))
            cur += take
            left -= take
        for pi, (sa, sb) in enumerate(parts):
            sid = new_id(act)
            cau = f"`{eid}#{sa}`" if sa == sb else f"`{eid}#{sa}`–`#{sb}`"
            c = list(r)
            c[0], c[1] = sid, cau
            out_rows.append({"sid": sid, "kind": "shot", "cells": c, "el": eid,
                             "spans": [(eid, sa, sb)], "from": r[0],
                             "split_of": r[0] if pi else None})
            if pi == 0:
                idmap[r[0]] = sid

cov = {f"{eid}#{k}" for r in out_rows if r["kind"] == "shot"
       for eid, a, b in r["spans"] for k in range(a, b + 1)}
allnew = {f"{eid}#{i + 1}" for eid, v in new_idx.items() for i in range(len(v))}
assert cov == allnew, f"thiếu {sorted(allnew - cov)}"

json.dump({"rows": out_rows, "idmap": idmap},
          open(W / "_t04_skeleton.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

n_shot = sum(1 for r in out_rows if r["kind"] == "shot")
cnt = [r["spans"][0][2] - r["spans"][0][1] + 1 for r in out_rows if r["kind"] == "shot"]
print(f"MAX_SENT={MAX_SENT} · dòng {len(out_rows)} (shot {n_shot}) · câu phủ {len(cov)}/{len(allnew)}")
print(f"câu/shot: min {min(cnt)} max {max(cnt)} trung bình {sum(cnt)/len(cnt):.2f}")
print("idmap:", json.dumps(idmap, ensure_ascii=False))

lines = []
for r in out_rows:
    if r["kind"] != "shot":
        lines.append(f"[META] {r['sid']} (từ {r['from']}) | {r['cells'][1]} | chữ={r['cells'][5][:70]}")
        continue
    ctx = " ".join(t for eid, a, b in r["spans"] for _, t in new_idx[eid][a - 1:b])
    lines.append(f"### {r['sid']} (từ {r['from']}) el={r['el']} {r['spans'][0][1]}-{r['spans'][0][2]}")
    lines.append(f"    vai={r['cells'][2]} | mẫu={r['cells'][3]} | nền={r['cells'][4]}")
    lines.append(f"    CHỮ CŨ: {r['cells'][5]}")
    lines.append(f"    CÂU MỚI: {ctx}")
    lines.append(f"    beat: {r['cells'][6]} | nv: {r['cells'][7]} | tr: {r['cells'][8]}")
    lines.append("")
open(W / "_t04_worklist.txt", "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("worklist -> .work/_t04_worklist.txt")
