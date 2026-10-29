#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q — Tong hop cuoi: baseline (51 cau audio thanh pham) + 4 ung vien (20 cau) + tach cau ngan."""
import json
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(r"D:\TEST\Gax\Audi\.work")
OUT = WORK / "cer_xac_minh_giong_nam"
HOST_F0 = 102.6
LONG_MIN = 12          # ngan tu: duoi nguong nay CER bi phong dai


def norm(t):
    t = unicodedata.normalize("NFC", t.lower())
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def nwords(t):
    return len(norm(t).split())


def stat(rows):
    cs = sorted(r["cer"] for r in rows)
    f0s = sorted(r["f0"] for r in rows if r["f0"])
    med_f0 = f0s[len(f0s) // 2] if f0s else 0
    return {
        "n": len(cs), "mean": sum(cs) / len(cs), "med": cs[len(cs) // 2], "max": cs[-1],
        "over": sum(1 for c in cs if c > 0.02),
        "f0": med_f0, "gap": 12 * np.log2(med_f0 / HOST_F0) if med_f0 else 0}


def show(title, rows):
    s = stat(rows)
    long_rows = [r for r in rows if nwords(r["ref"]) >= LONG_MIN]
    sl = stat(long_rows) if long_rows else None
    out = [f"### {title}",
           f"- **Tất cả**: n={s['n']} · tb {100*s['mean']:.1f}% · median {100*s['med']:.1f}% · "
           f"max {100*s['max']:.1f}% · >2%: {s['over']}/{s['n']} · F0 {s['f0']:.0f} Hz · cách Host {s['gap']:+.1f} nc"]
    if sl:
        out.append(f"- **Câu dài (≥{LONG_MIN} từ)**: n={sl['n']} · tb {100*sl['mean']:.1f}% · "
                   f"max {100*sl['max']:.1f}% · >2%: {sl['over']}/{sl['n']}")
    return "\n".join(out), s


base = json.loads((OUT / "rows.json").read_text(encoding="utf-8"))          # baseline 51 cau
cand = json.loads((OUT / "rows2.json").read_text(encoding="utf-8"))         # 20 cau + 4 ung vien

groups = {}
for r in base + cand:
    groups.setdefault(r["cand"], []).append(r)

md = ["# PHA 2 — Xac minh ung vien thay the vai Dieu tra vien (Tap 02)", "",
      f"Baseline = **audio thành phẩm** của `{BASE}` (51 câu vai D, 0 lượt TTS).",
      f"Ứng viên = TTS mới với **đúng emotion/speed của từng câu** (20 câu: 3 câu khó nhất + 17 câu rải đều).",
      f"Host F0 = {HOST_F0} Hz. Câu ngắn (<{LONG_MIN} từ) bị phóng đại tỉ lệ lỗi nên tách riêng.", ""]

md.append("## BẢNG TỔNG HỢP (trên cùng tập 20 câu)")
md.append("")
md.append("| # | voice_id | n | CER tb | median | max | >2% | F0 | cách Host | nguồn |")
md.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---|")
rows_summary = []
for c, rs in groups.items():
    if "audio T2" in c:
        rs20 = [r for r in rs if r["id"] in {x["id"] for x in cand}]
    else:
        rs20 = rs
    s = stat(rs20)
    rows_summary.append((s["mean"], c, s, len(rs)))
rows_summary.sort()
for i, (mean, c, s, ntot) in enumerate(rows_summary, 1):
    src = "audio T2" if "audio T2" in c else "TTS mới"
    md.append(f"| {i} | `{c}` | {s['n']} | {100*s['mean']:.1f}% | {100*s['med']:.1f}% | {100*s['max']:.1f}% | "
              f"{s['over']}/{s['n']} | {s['f0']:.0f} Hz | {s['gap']:+.1f} | {src} |")
md.append("")

for c, rs in sorted(groups.items(), key=lambda kv: stat(kv[1])["mean"]):
    txt, _ = show(f"`{c}`" + (" — TOÀN BỘ 51 CÂU (audio thành phẩm)" if "audio T2" in c else " — 20 CÂU TTS MỚI"), rs)
    md.append(txt)
    md.append("")
    md.append("| id | CER | từ | F0 | Nghe được |")
    md.append("|---|---:|---:|---:|---|")
    for x in sorted(rs, key=lambda y: -y["cer"]):
        if x["cer"] <= 0:
            continue
        md.append(f"| `{x['id']}` | {100*x['cer']:.1f}% | {nwords(x['ref'])} | {x['f0']:.0f} | {x['hyp'][:105]} |")
    md.append("")

(OUT / "report_final.md").write_text("\n".join(md), encoding="utf-8")
print("\n".join(md[:40]))
print("\n... bang chi tiet: .work/cer_xac_minh_giong_nam/report_final.md")
