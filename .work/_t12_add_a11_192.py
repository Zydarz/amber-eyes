# -*- coding: utf-8 -*-
"""Thêm dòng A11 #192 (rút kinh nghiệm: tại sao phải sinh ảnh nhiều lần) — thao tác dòng, không ghi lại toàn file.

Dùng: py -3 .work/_t12_add_a11_192.py
"""
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "00_TIEU_CHUAN" / "TIEU_CHUAN_DUNG_VIDEO.md"

raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
lines = raw.split(nl)

backup = ROOT / ".work" / "_cu" / f"a11_192_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
shutil.copy2(P, backup / P.name)
print(f"backup -> {backup}")

rows = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := re.match(r"^\| (\d+) \|", l))]
if 192 in {n for _, n in rows}:
    print(">> A11 192 da ton tai - khong chen them")
    sys.exit(0)

row192 = (
    "| 192 | **Vì sao phải gọi tạo ảnh nhiều lần: 233 ảnh render cho 152 nền (81 ảnh thừa = 34,9 %) — 5 nguyên nhân "
    "đo được, và quy trình 5 bước để không lặp lại.** Tập 12 (17/11/2026): lô 83 ảnh (13/11) **chưa từng qua cổng chữ** ⇒ "
    "chiến dịch vá 29 nền tốn **58 ảnh (24,9 % tổng lượt)**; QC vòng 1 ở mức montage ô 390 px bỏ sót chữ ~10 px ⇒ "
    "4/7 \"PASS\" thực ra còn vết ⇒ **15 lượt** sinh lại cho cùng 3 nền; 2 biến thể/nền tốn gấp đôi lượt (dùng 33–38 %); "
    "mệnh đề phủ định không cứu được vật thể có sẵn \"chỗ chữ\"; cụm nhãn trong prompt bị AI dùng làm chữ để vẽ. "
    "Chi phí: **81 × ~75 s ≈ 101 phút GPU** + **≈ 4,7 giờ chờ hàng đợi** (56/78/75/75 phút đo được) | "
    "**Quy trình 5 bước TRƯỚC khi push (tập sau)**: 1) quét prompt bằng `_t12_prompt_textscan.py`; 2) bỏ cụm nhãn + "
    "không nhắc tên vật thể mang chữ, vật thể có sẵn chỗ chữ thì **đổi bố cục** (A11 #171/#175/#188); 3) **sinh 2 biến thể/nền "
    "ngay** trong đúng 2 kernel song song; 4) QC = montage (lập danh sách nghi) → **crop 8–16× từng vùng có giấy/bìa/thước/"
    "ống kính/la bàn/phim/ảnh ghim** → dùng **bản tăng sáng** cho ảnh noir (A11 #191); 5) **QC 100 % toàn bộ nền của tập**, "
    "kể cả lô cũ — **không \"mặc định đạt\" cho ảnh sinh trước đó** (A11 #182). Ước tính áp dụng từ đầu: **152 ảnh thay vì 233**. "
    "Báo cáo đầy đủ: `02_SAN_XUAT/Tap12/BaoCao_QC_Tap12_20261116.md` §4.8 |"
)

last_idx = max(i for i, n in rows)
lines.insert(last_idx + 1, row192)
P.write_text(nl.join(lines), encoding="utf-8", newline="")

check = P.read_text(encoding="utf-8")
nums = [int(m.group(1)) for l in check.split(nl) if (m := re.match(r"^\| (\d+) \|", l))]
print("max A11 =", max(nums), "| 192 co:", 192 in nums, "| CRCRLF:", check.count("\r\r\n"),
      "| dong:", len(check.split(nl)))
