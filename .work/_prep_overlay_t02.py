# -*- coding: utf-8 -*-
"""Chuẩn bị dữ liệu đầu vào cho lớp phủ chữ trên hình (EN/JA/KO).

Với mỗi ngôn ngữ L, sinh:
  .work/_ovl_ref_{L}.md   : bảng tham chiếu cho người viết lớp phủ (sid | câu | chữ VN | beat VN | chữ {L} cũ | cụm beat {L} cũ)
  .work/_ovl_draft_{L}.json: lớp phủ khởi đầu (mang sang từ bảng cũ theo ánh xạ old->new; dòng mới để trống)

Ánh xạ old->new lấy từ .work/_old2new_t02.json (khớp theo tập câu phủ).
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
old2new = {}
for grp in ("exact", "changed"):
    for o, n in m2n[grp]:
        old2new[o] = n
print(f"dong moi = {len(new_rows)}   anh xa old->new = {len(old2new)}")

for L in ("EN", "JA"):
    ovl_p = W / f"shots_text_tap02_{L}.json"
    old_ovl = json.loads(ovl_p.read_text(encoding="utf-8"))
    old_ovl = {k: v for k, v in old_ovl.items() if not k.startswith("_")}

    draft = {}
    lines = []
    lines.append(f"# BẢNG THAM CHIẾU LỚP PHỦ CHỮ TRÊN HÌNH · TẬP 02 · BẢN {L}")
    lines.append("")
    lines.append("Cột `CHỮ {L} CŨ` = giá trị cũ trong `shots_text_tap02_{L}.json` (mã shot CŨ) — dùng làm "
                 "mẫu/khoảng cách, KHÔNG dùng nguyên văn nếu nội dung VN đã đổi.")
    lines.append("")
    for r in new_rows:
        sid = r["sid"]
        c = r["cells"]
        # tìm mã shot cũ tương ứng (ngược ánh xạ)
        olds = [o for o, n in old2new.items() if n == sid]
        osid = olds[0] if olds else None
        o = old_ovl.get(osid) if osid else None
        o_chu = (o[0] if o else "")
        o_ph = (o[1] if o else [])
        o_ov = (o[2] if o and len(o) > 2 else None)
        beat_ph = re.findall(r'ở "([^"]+)"', c[6])
        draft[sid] = {
            "text": o_chu if o_chu else "",
            "phrases": list(o_ph),
            "override": o_ov,
            "_src_old_sid": osid,
            "_vn_chu": c[5],
            "_vn_beat": c[6],
            "_beat_phrases_vn": beat_ph,
            "_sent": c[1],
        }
        lines.append(f"## {sid}  ({c[1]})")
        lines.append(f"- CHỮ VN : {c[5]}")
        lines.append(f"- BEAT VN: {c[6]}")
        lines.append(f"- CHỮ {L} CŨ [{osid}]: {o_chu if o_chu else '(chưa có)'}")
        if beat_ph:
            lines.append(f"- cụm beat cần có trong câu {L} (theo cột Beat): {beat_ph}")
        if o_ph:
            lines.append(f"- cụm beat {L} cũ: {o_ph}")
        lines.append("")

    (W / f"_ovl_ref_{L}.md").write_text("\n".join(lines), encoding="utf-8")
    out = {"_note": f"shot_id -> [chu_{L}, [beat_phrase...], beat_override|null]  (KHAI BÁO SẴN - SỬA LẠI)",
           **{k: [v["text"], v["phrases"], v["override"]] for k, v in draft.items()}}
    (W / f"_ovl_draft_{L}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    blank = [k for k, v in draft.items() if not v["text"] and v["_vn_chu"].strip() != "—"]
    print(f"{L}: ref {len(lines)} dong · can viet lai {len(blank)} dong: {blank[:12]}...")
