#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat muc III (bang 45 tap chuyen de) bang so do that tu index_45_tap.json + tieu de."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / "BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md"
lines = MD.read_text(encoding="utf-8").split("\n")

idx = {int(x["ep"]): x for x in json.loads((ROOT / ".work" / "tlhtp" / "index_45_tap.json").read_text(encoding="utf-8"))}

# --- 1. Tieu de muc II: 68 -> 69 ---
for i, l in enumerate(lines):
    if l.startswith("## II. CHI TIẾT SERIES 1: 68 HỒ SƠ VỤ ÁN CÓ THẬT"):
        lines[i] = "## II. CHI TIẾT SERIES 1: 69 HỒ SƠ VỤ ÁN CÓ THẬT (ĐÃ SẮP XẾP XEN KẼ HÀI HÒA)"
        print("OK: tieu de muc II"); break

# --- 2. Tieu de muc III + ghi chu tro ve series 140 tap ---
for i, l in enumerate(lines):
    if l.startswith("## III. CHI TIẾT SERIES 2: 45 TẬP CHUYÊN ĐỀ TÂM LÝ HỌC TỘI PHẠM"):
        lines[i] = ("## III. CHI TIẾT SERIES 2: 45 TẬP CHUYÊN ĐỀ TÂM LÝ HỌC TỘI PHẠM"
                    "  ·  *(+ Series 3: 140 tập \"Bảy Tâm Lý Và Hành Vi\" — xem mục IX.4)*")
        lines.insert(i + 1, "")
        lines.insert(i + 2, "> **Đo lại 27/11/2026 (nguồn: `.work/tlhtp/index_45_tap.json`):** 45 tập · **10.545 câu thoại** · "
                          "**229.559 từ** · 4.295 job ảnh nền · **14/45 tập đạt ngưỡng H25/H27** "
                          "(01–07, 29, 30, 35–38, 40) · 8 tập trùng prompt (29, 30, 31, 32, 33, 34, 39, 43) · "
                          "4 tập chưa có `bg_jobs` (41, 42, 44, 45). Cột \"Lượt thoại\" / \"Độ dài (từ)\" dưới đây "
                          "đã cập nhật theo số đo này (bản cũ ghi \"681 lượt / 125.132 từ\" — chỉ là mẫu chung).")
        print("OK: tieu de muc III + ghi chu do lai"); break

# --- 3. Cap nhat 2 cot cuoi cua 45 dong bang ---
n = 0
for i, l in enumerate(lines):
    m = re.match(r"^\| \*\*Tập (\d{2})\*\* \| (.*)$", l)
    if not m:
        continue
    ep = int(m.group(1))
    if ep not in idx:
        continue
    # tach phan cuoi: | <luot thoai> | <do dai> |
    mm = re.match(r"^(.*\| )\*\*\d+\*\* \| [\d,]+ \|$", l)
    if not mm:
        continue
    head = mm.group(1)
    lines[i] = "%s**%d** | %s |" % (head, idx[ep]["sentences"], format(idx[ep]["words"], ",").replace(",", "."))
    n += 1
print("OK: cap nhat %d/45 dong bang muc III" % n)
assert n == 45, n

MD.write_text("\n".join(lines), encoding="utf-8")
print("da ghi:", MD)
