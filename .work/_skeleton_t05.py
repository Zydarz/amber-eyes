#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — dựng skeleton bảng shot MỚI cho kịch bản MỚI (60 element / 209 câu).

Nguyên tắc (giống Tập 04, đã kiểm chứng):
  * Giữ thiết kế hình cũ: nền, mẫu, vai, beat, nhân vật, trạng thái.
  * Chia lại câu theo kịch bản mới: mỗi shot cũ nhận số câu tỉ lệ với số câu cũ,
    tách thêm dòng nếu vượt MAX_SENT (giữ nhịp hình 3–15 s).
  * Shot ID đánh số lại liên tục theo hồi (N-NN).
  * Element MỚI (3.09, 3.10) = chèn thủ công từ file `_t05_new_rows.json`.
  * Xuất bản đồ old_id -> new_id.

Dùng:  py -3 .work/_skeleton_t05.py [MAX_SENT]
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

MAX_SENT = int(sys.argv[1]) if len(sys.argv) > 1 else 3
PLAN = ROOT / "02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md"
NEW_KB = ROOT / "01_KICH_BAN/Tap05/kichban_tap05_23102026.md"
# Dòng thủ công cho element MỚI (3.09, 3.10) — do AI soạn, phải truy được về câu.
EXTRA = W / "_t05_new_rows.json"


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


# ---------------------------------------------------------------- gom theo element
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

# ------------------------------------------------------- chèn dòng MỚI cho element mới
extra = json.loads(EXTRA.read_text(encoding="utf-8")) if EXTRA.exists() else []
extra_by_el = {}
for e in extra:
    extra_by_el.setdefault(e["el"], []).append(e)

# element mới phải nằm đúng chỗ: sau element cuối cùng của cùng hồi
new_groups = []
pending_extra = dict(extra_by_el)
for kind, payload, extra_rows in groups:
    new_groups.append((kind, payload, extra_rows))

# đánh số lại
act_counters = {}
out_rows = []
idmap = {}


def new_id(act):
    # Dòng ĐẦU TIÊN của bảng = thẻ mở đầu, PHẢI giữ ID "1-00"
    # (parse_shots.py đặc biệt hoá: sid == "1-00" -> chạy từ 20.5 s tới lời đầu).
    if not out_rows:
        act_counters[act] = 0
        return "1-00"
    act_counters[act] = act_counters.get(act, 0) + 1
    return f"{act}-{act_counters[act]:02d}"


def emit_extra(act):
    """Chèn các dòng thủ công của element mới, theo sau element cuối của hồi đó."""
    for e in extra:
        if e["el"].split(".")[0] != str(act):
            continue
        if e.get("_done"):
            continue
        e["_done"] = True
        sid = new_id(act)
        c = list(e["cells"])
        c[0] = sid
        out_rows.append({"sid": sid, "kind": "shot", "cells": c, "el": e["el"],
                         "spans": [(e["el"], e["a"], e["b"])], "from": e["el"] + "#NEW",
                         "manual": True})
        idmap[e["el"] + "#NEW"] = sid


last_act = None
for kind, payload, extra_rows in groups:
    if kind == "meta":
        r = payload
        act = int(r[0].split("-")[0])
        sid = new_id(act)
        out_rows.append({"sid": sid, "kind": "meta", "cells": r, "el": None,
                         "spans": [], "from": r[0]})
        if last_act is not None and act != last_act:
            emit_extra(last_act)
        last_act = act
        continue

    eid, rows = payload, extra_rows
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
    # element mới xuất hiện sau element cuối cùng của hồi này?
    if act == last_act or True:
        pass
    # chèn element mới sau khi element cuối cùng của hồi đã xử lý
    if eid == max((g[1] for g in groups if g[0] == "el" and int(g[1].split(".")[0]) == act),
                   key=lambda x: int(x.split(".")[1]), default=None):
        emit_extra(act)

# phần element mới thuộc hồi 5 (nếu có) chèn cuối
for a in sorted({int(e["el"].split(".")[0]) for e in extra if not e.get("_done")}):
    emit_extra(a)

cov = {f"{eid}#{k}" for r in out_rows if r["kind"] == "shot"
       for eid, a, b in r["spans"] for k in range(a, b + 1)}
allnew = {f"{eid}#{i + 1}" for eid, v in new_idx.items() for i in range(len(v))}
assert cov == allnew, f"thiếu {sorted(allnew - cov)} · thừa {sorted(cov - allnew)}"

json.dump({"rows": out_rows, "idmap": idmap},
          open(W / "_t05_skeleton.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

n_shot = sum(1 for r in out_rows if r["kind"] == "shot")
cnt = [r["spans"][0][2] - r["spans"][0][1] + 1 for r in out_rows if r["kind"] == "shot"]
per_act = {}
for r in out_rows:
    a = r["sid"].split("-")[0]
    per_act[a] = per_act.get(a, 0) + 1
print(f"MAX_SENT={MAX_SENT} · dòng {len(out_rows)} (shot {n_shot}) · câu phủ {len(cov)}/{len(allnew)}")
print(f"câu/shot: min {min(cnt)} max {max(cnt)} trung bình {sum(cnt)/len(cnt):.2f}")
print("shot theo hồi:", per_act)
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
open(W / "_t05_worklist.txt", "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("worklist -> .work/_t05_worklist.txt")
