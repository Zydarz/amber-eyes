# -*- coding: utf-8 -*-
"""Cap nhat bao cao anh nen doc Tap 03: them muc doi ten nen t3_* -> tk03_*."""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
p = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK", "Tap03", "BAO_CAO_ANH_NEN_DOC_TAP03.md")

s = io.open(p, encoding="utf-8").read()

OLD = """---

## 6. Việc còn lại (người dùng / lần sau)"""

NEW = """---

## 5b. Sửa tên nền trong kịch bản clip: `t3_*` → `tk03_*` (20/11/2026)

**Vấn đề:** cột Nền trong bảng shot (mục 2.1–2.5) và trường `bg` trong `SPEC_AUDIO_CLIP_TAP03.json` vẫn trỏ tới `t3_*` — tên ảnh gốc **16:9**. Script dựng video đọc `assets/bg/<nen>.png` ⇒ khi chạy sẽ crash `THIEU NEN assets/bg/t3_*.png` (28/28 ảnh đó không tồn tại trong `assets/bg/`, chỉ nằm ở `assets/bg/_raw/`).

**Cách sửa (theo đúng quy ước Tập 02 — `tk02_*` trong clip, `t2_*` là ảnh gốc):**

| Nơi | Sửa |
|---|---|
| `.work/_build_tk_tap03.py` | 51 giá trị `bg` trong tuple → `tk03_*`; `NEN_SRC` 28 mục → `"tk03_x": "t3_x"`; **bổ sung mục thiếu** `tk03_self_observation` (bản gốc chỉ có 27/28 ⇒ QC #8 báo thiếu raw) |
| `.work/_build_tk_tap03_multilang.py` | 102 giá trị `bg` → `tk03_*` |
| `SPEC_AUDIO_CLIP_TAP03.json` (VN/EN/JA) | 51 × 3 trường `bg` → `tk03_*` |
| `KE_HOACH_CLIP_TAP03.md` | 51 dòng bảng shot → `tk03_*` |

**Kiểm chứng sau khi chạy lại generator:** cả 3 spec trỏ đúng 28 nền `tk03_*` và **mọi file được trỏ tới đều tồn tại**; bảng shot VN 51/51 dòng dùng `tk03_*`; caption + mô tả ngắn/dài **không đổi** (so từng file với backup); 12 cổng tự kiểm của generator vẫn **ĐẠT TOÀN BỘ** (kể cả #8 "28/28 nền có file raw").

Backup trước khi sửa: `.work/_cu/tk03_bgname_20261120_2312/` (file kế hoạch + spec) · `.work/_cu/tk03_regen_20261120_2316/` (thư mục sản xuất Tap03 VN/EN/JA).

> ⚠ **Bẫy khi tự vá tên:** `re.sub(r'"tk03_\\1"', ...)` trên chuỗi đã chứa `t3_` sẽ ra `tk03_t3_x`; và thay thế trong `NEN_SRC` phải giữ **một** cặp dấu nháy. Đã sửa lại và kiểm bằng `.work/_tk_audit_nensrc.py` (28/28 đúng, 0 lỗi `tk03_t3_`).

---

## 6. Việc còn lại (người dùng / lần sau)"""

if OLD not in s:
    print("KHONG tim thay moc chen")
    sys.exit(1)
s = s.replace(OLD, NEW, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("da them muc 5b vao bao cao")
