# -*- coding: utf-8 -*-
"""Them bay T37 (ten nen trong spec clip TikTok) vao KE_HOACH_TIKTOK.md."""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
p = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK", "KE_HOACH_TIKTOK.md")

ROW = ("| **T37** | **Spec clip phải trỏ tới ảNH DỌC (`tkXX_*`), không phải tên ảnh gốc 16:9 (`tXX_*`)** — "
       "script dựng đọc `assets/bg/<nen>.png`; ảnh gốc 16:9 chỉ nằm ở `assets/bg/_raw/` ⇒ clip sẽ crash "
       "`THIEU NEN assets/bg/t3_*.png` | Tập 03 (20/11/2026): kế hoạch + 3 spec (VN/EN/JA) vẫn dùng `t3_*` "
       "sau khi đã dựng xong 28 nền dọc. Đã sửa: 51×4 giá trị `bg` → `tk03_*`, `NEN_SRC` trong "
       "`.work/_build_tk_tap03.py` → `\"tk03_x\": \"t3_x\"` (**bản gốc chỉ có 27/28 — thiếu `t3_self_observation`** "
       "⇒ QC #8 báo thiếu raw), chạy lại generator ⇒ 12/12 cổng đạt. **Bẫy khi tự vá:** `re.sub` với "
       "`\"tk03_\\1\"` trên chuỗi đã có `t3_` cho ra `tk03_t3_x`; thay trong `NEN_SRC` phải giữ **một** cặp dấu nháy. "
       "**Luôn kiểm:** mọi tên trong `bg` của spec phải **tồn tại** ở `assets/bg/` |\n")

s = io.open(p, encoding="utf-8").read()
if "**T37**" in s:
    print("T37 da co - khong them")
    sys.exit(0)

# chen ngay sau dong T34 (dong cuoi cung cua bang bay)
lines = s.split("\n")
out = []
done = False
for ln in lines:
    out.append(ln)
    if not done and ln.startswith("| **T34**"):
        out.append(ROW.rstrip("\n"))
        done = True
if not done:
    print("KHONG tim thay dong T34 de chen")
    sys.exit(1)
io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("da them T37 vao KE_HOACH_TIKTOK.md")
