#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — cập nhật B1 (thống kê) + PHỤ LỤC A (bảng cấu trúc kịch bản) của bảng shot VN."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402
import edition as ED  # noqa: E402

PLAN = ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md"
KB = ROOT / "01_KICH_BAN/Tap06/kichban_tap06_23102026.md"
N_ELEM = ED.EPISODES["06"].get("n_element") or {}

ROLE_LABEL = {"H": "Cú · Host", "D": "**Sói · Điều tra viên**",
              "C": "**Cáo · Chuyên gia**", "N1": "**Cừu · N1**", "N2": "**Mèo · N2**"}

els = parse_file(str(KB))
tl = json.loads((W / "timeline_s_t06.json").read_text(encoding="utf-8"))
shots = json.loads((W / "shots_t06.json").read_text(encoding="utf-8"))["shots"]

# ---------------------------------------------------------------- thống kê
loi = [e for e in els if e.get("kind") == "LOI"]
words = {}
sent_by_role = {}
for e in loi:
    role = N_ELEM.get(e["id"], e.get("role"))
    n_w = sum(len(s["text"].split()) for s in e.get("sentences", []))
    words[e["id"]] = n_w
    sent_by_role.setdefault(role, [0, 0])
    sent_by_role[role][0] += len(e.get("sentences", []))
    sent_by_role[role][1] += n_w
total_words = sum(words.values())
total_sents = sum(len(e.get("sentences", [])) for e in loi)
total_el = len(els)
dur = tl["total"]
n_bg = len({s["bg"] for s in shots if s.get("bg")})

pct = {r: 100.0 * v[0] / total_sents for r, v in sent_by_role.items()}
role_txt = " · ".join(
    f"{ROLE_LABEL[r].replace('*','')} {pct[r]:.1f}%" for r in
    ["H", "D", "C", "N2", "N1"] if r in pct)

print(f"element {total_el} · câu {total_sents} · từ {total_words} · {dur:.1f}s · nền {n_bg}")

t = PLAN.read_text(encoding="utf-8")

# ---- B1: dòng thống kê ------------------------------------------------------
t = re.sub(r"\| Lượt nói / câu / từ \|.*\|",
           f"| Lượt nói / câu / từ | {total_el} lượt · **{total_sents}** câu · "
           f"{total_words:,} — {role_txt} |".replace(",", "."), t, count=1)

t = re.sub(r"\| N1 / N2 \|.*\|",
           "| N1 / N2 | `1.09` Kim Byers - nhân viên hiệu thuốc Nisson (Cừu) / `4.05` "
           "Sĩ quan Mike Albrecht - cảnh sát Des Plaines (Mèo) |", t, count=1)

t = re.sub(r"\| Thời lượng \|.*\|",
           f"| Thời lượng | **{dur:.1f} s ({int(dur // 60)}:{int(dur % 60):02d})** — "
           "*timeline tạm, chờ thu âm lại kịch bản mới* |", t, count=1)

t = re.sub(r"\| Nền dùng \|.*\|",
           f"| Nền dùng | {n_bg} nền `t6_*` + `charity` + `void` (2112×1188 16:9 2K noir) |",
           t, count=1)

# ---- PHỤ LỤC A: bảng cấu trúc kịch bản ------------------------------------
i = t.find("## PHỤ LỤC A")
j = t.find("## PHỤ LỤC B")
assert i > 0 and j > i, "không tìm thấy PHỤ LỤC A/B"
appendix = t[i:j]

rows = ["| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |",
        "|---|---|---:|---:|---|"]
for e in els:
    eid = e["id"]
    kind = e.get("kind")
    if kind == "LOI":
        role = N_ELEM.get(eid, e.get("role"))
        n = len(e.get("sentences", []))
        w = words[eid]
        vai = ROLE_LABEL.get(role, role)
        desc = e.get("direction", "")
        cells = (f"| `{eid}` | {vai} | {n} | {w} | {desc} |")
    else:
        if kind == "BGM":
            vai = "*BGM*"
        elif kind == "SFX":
            vai = "*SFX*"
        else:
            vai = f"*Nghỉ {e.get('sec', 1.5)} s*"
        cells = f"| `{eid}` | {vai} | — | — | {e.get('desc', '')} |"
    rows.append(cells)
rows.append(f"| | **Tổng** | **{total_sents}** | **{total_words}** | |")

# thay bảng cũ (từ header "| Mã | Vai / loại |" tới dòng "**Tổng**")
k0 = appendix.find("| Mã | Vai / loại |")
k1 = appendix.find("**Tổng**")
assert k0 > 0 and k1 > k0, "không tìm thấy bảng phụ lục A"
k1 = appendix.find("\n", k1) + 1
new_appendix = appendix[:k0] + "\n".join(rows) + "\n" + appendix[k1:]
t = t[:i] + new_appendix + t[j:]

PLAN.write_text(t, encoding="utf-8")
print("-> da cap nhat", PLAN.name)
