# -*- coding: utf-8 -*-
"""Sinh tài liệu tham chiếu + bản khởi đầu cho lớp phủ chữ trên hình bản TIẾNG HÀN (KO).

KO chưa có bảng shot cũ -> toàn bộ 161 dòng phải viết mới.
Tham chiếu: cột CHỮ VN (nguồn chuẩn) + CHỮ EN cũ (để nắm ngữ nghĩa, KHÔNG dùng nguyên văn).
"""
import json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r'D:/TEST/Gax/amber-eyes')
W = ROOT / ".work"


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
        rows.append(dict(sid=m.group(1), cells=c))
    return rows


new_rows = read_rows(ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md")
m2n = json.loads((W / "_old2new_t02.json").read_text(encoding="utf-8"))
old2new = {o: n for grp in ("exact", "changed") for o, n in m2n[grp]}
en_ovl = json.loads((W / "shots_text_tap02_EN.json").read_text(encoding="utf-8"))
en_ovl = {k: v for k, v in en_ovl.items() if not k.startswith("_")}

lines = ["# BẢNG THAM CHIẾU LỚP PHỦ CHỮ TRÊN HÌNH · TẬP 02 · BẢN TIẾNG HÀN (KO)", "",
         "Nguồn chuẩn = cột CHỮ VN. Cột CHỮ EN chỉ để nắm ngữ nghĩa (KHÔNG dùng nguyên văn).", ""]
draft = {}
for r in new_rows:
    sid, c = r["sid"], r["cells"]
    olds = [o for o, n in old2new.items() if n == sid]
    osid = olds[0] if olds else None
    o = en_ovl.get(osid) if osid else None
    en_chu = o[0] if o else ""
    en_ph = o[1] if o else []
    beat_ph = re.findall(r'ở "([^"]+)"', c[6])
    draft[sid] = {"text": "", "phrases": list(en_ph), "override": None,
                  "_vn_chu": c[5], "_vn_beat": c[6], "_sent": c[1]}
    lines.append(f"## {sid}  ({c[1]})")
    lines.append(f"- CHỮ VN : {c[5]}")
    lines.append(f"- BEAT VN: {c[6]}")
    lines.append(f"- CHỮ EN [{osid}]: {en_chu if en_chu else '(không có)'}")
    if beat_ph:
        lines.append(f"- cụm beat cần có trong câu KO (theo cột Beat): {beat_ph}")
    if en_ph:
        lines.append(f"- cụm beat EN cũ (tham chiếu): {en_ph}")
    lines.append("")

(W / "_ovl_ref_KO.md").write_text("\n".join(lines), encoding="utf-8")
out = {"_note": "shot_id -> [chu_KO, [beat_phrase...], beat_override|null]  (KHAI BÁO SẴN - CẦN VIẾT LẠI TOÀN BỘ)",
       **{k: [v["text"], v["phrases"], v["override"]] for k, v in draft.items()}}
(W / "_ovl_draft_KO.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"KO: {len(draft)} dong · ref -> .work/_ovl_ref_KO.md")
