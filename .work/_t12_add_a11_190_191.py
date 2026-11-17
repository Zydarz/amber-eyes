# -*- coding: utf-8 -*-
"""Thêm 2 dòng A11 (mục 190, 191) vào TIEU_CHUAN_DUNG_VIDEO.md — thao tác dòng, không ghi lại toàn file.

Dùng: py -3 .work/_t12_add_a11_190_191.py
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

backup = ROOT / ".work" / "_cu" / f"a11_190_191_{datetime.now():%Y%m%d_%H%M}"
backup.mkdir(parents=True, exist_ok=True)
shutil.copy2(P, backup / P.name)
print(f"backup -> {backup}")

rows = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := re.match(r"^\| (\d+) \|", l))]
have = {n for _, n in rows}
if 190 in have or 191 in have:
    print(">> A11 190/191 da ton tai - khong chen them")
    sys.exit(0)

row190 = (
    "| 190 | **Kaggle CLI đọc file `~/.kaggle/access_token` TRƯỚC `credentials.json` ⇒ khi token hết hạn (12 h) "
    "thì MỌI lệnh Kaggle chết, và báo lỗi NHẦM về quyền kernel.** AMBER EYES (16/11/2026): token hết hạn lúc 21:00 "
    "⇒ `kernels status` trả *\"Permission 'kernels.get' was denied\"*, `kernels list` trả *\"Authentication required\"* — "
    "trong khi kernel vẫn chạy bình thường ⇒ dễ tưởng mất tài khoản | **Dấu hiệu**: lỗi xuất hiện ĐỒNG LOẠT trên mọi "
    "`kaggle ...` trong khi `kaggle kernels list --mine` cũng báo *\"Authentication required\"*. Cách sửa: chạy "
    "`.work/kaggle_flux/refresh_kaggle_token.py` (SDK `generate_access_token()` → ghi lại `credentials.json` + "
    "`access_token`, có backup `.bak`) | Token hết hạn KHÔNG làm mất tài khoản; **đừng `kaggle auth login`** (cần thao tác "
    "trình duyệt) — chỉ cần refresh bằng `refresh_token` đã lưu trong `credentials.json` |"
)
row191 = (
    "| 191 | **Ảnh nền noir quá tối ⇒ montage thường ra ĐEN XÌ, soi bằng bản gốc là soi vô nghĩa — phải TĂNG SÁNG "
    "bản QC (không sửa file gốc).** AMBER EYES (16/11/2026): 8 ảnh vòng 5 có luminance trung bình **39–51/255** ⇒ "
    "montage 512 px nhìn như **không có ảnh** (đen toàn bộ) dù nội dung có; người QC dễ kết luận nhầm \"ảnh hỏng\" | "
    "1) Dựng thêm **bản QC tăng sáng** (gain 2,0–2,2 + tương phản 1,15) — **chỉ dùng để soi**, file gốc giữ nguyên. "
    "2) Công cụ: `.work/_t12_bright_montage.py` (montage có gain) + `.work/_t12_crop_batch.py` (crop N vùng → gộp 1 tờ "
    "để soi 1 lần). 3) Đo trước bằng `ImageStat` để biết ảnh có thật sự tối không | Bản QC sáng có thể **lộ ra chữ mà "
    "bản gốc không thấy** ⇒ soi bản sáng **và** bản gốc, không thay bản nào cho bản nào |"
)

last_idx = max(i for i, n in rows)
lines.insert(last_idx + 1, row190)
lines.insert(last_idx + 2, row191)
P.write_text(nl.join(lines), encoding="utf-8", newline="")

check = P.read_text(encoding="utf-8")
nums = [int(m.group(1)) for l in check.split(nl) if (m := re.match(r"^\| (\d+) \|", l))]
print("max A11 =", max(nums), "| 190 co:", 190 in nums, "| 191 co:", 191 in nums)
print("CRCRLF:", check.count("\r\r\n"), "| dong:", len(check.split(nl)))
