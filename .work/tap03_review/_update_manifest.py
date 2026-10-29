#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cập nhật manifest ảnh Tập 03 sau khi sinh thêm 2 ảnh + sửa viền t3_textbooks.
Mọi thay thế đều có assert (đúng 1 lần khớp) để không sửa nhầm chỗ."""
import io
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
MD = ROOT / "02_SAN_XUAT" / "Tap03" / "Danh_Sach_Anh_Tap03.md"
raw = MD.read_text(encoding="utf-8")
orig = raw

REPL = [
    # B1 — số ảnh
    ("| Số ảnh mới | **46** sinh mới — **45 dùng trong bảng shot** (`t3_car_door` không dùng, xem B3.3) + 1 dùng lại từ Tập 02 (`t2_gavel` — xem B3.2) |",
     "| Số ảnh mới | **47** sinh mới — **46 dùng trong bảng shot** (`t3_car_door` không dùng, xem B3.3) + 1 dùng lại từ Tập 02 (`t2_gavel` — xem B3.2) |"),

    # B2 — hàng mới trong bảng Hồi 2 + nới mốc của t3_ravine (không còn chồng 2.06#2)
    ("| `t3_ravine` | Vực sâu hẻo lánh dọc dãy núi Santa Cruz — hiện trường bị xóa sạch | `2.06#1`–`#3` |",
     "| `t3_ravine` | Vực sâu hẻo lánh dọc dãy núi Santa Cruz — hiện trường bị xóa sạch | `2.06#1`, `2.06#3`–`#4` |\n"
     "| `t3_backyard_garden` | **Khu vườn sau nhà** — nơi chôn đầu nạn nhân *(ảnh trống: không hố, không vật thể, tránh V9)* | `2.06#2` |"),

    # B3.1 — số ảnh qua QC
    ("**Soi bằng mắt** (toàn bộ 46 ảnh):",
     "**Soi bằng mắt** (toàn bộ 47 ảnh):"),
    ("| Kích thước | **46/46** đúng 2112×1188 |",
     "| Kích thước | **47/47** đúng 2112×1188 |"),
    ("| `t3_textbooks` | **Khung trắng + đường mực** quanh cả ảnh | Cắt 15 px ở 4 cạnh |",
     "| `t3_textbooks` | **Khung trắng + đường mực** quanh cả ảnh | Cắt 15 px ở 4 cạnh; lần quét sau phát hiện còn sót **đường sáng 3–4 px** ở mép → cắt thêm 6 px (lần 2, gốc ở `_raw/t3_textbooks.framefix2.png`) |"),

    # B3.3 — bảng "lệch nội dung nhẹ": thêm ảnh mới
    ("| `t3_case_photos` | Tông sepia ấm | Chấp nhận — chỉ dùng 1 shot, hợp \"không gian hồ sơ\" |",
     "| `t3_case_photos` | Tông sepia ấm | Chấp nhận — chỉ dùng 1 shot, hợp \"không gian hồ sơ\" |\n"
     "| `t3_backyard_garden` | Có **mưa** trong ảnh | Chấp nhận — khớp đêm mưa của Hồi 2 (cue `2.01` là mưa trên mui xe). Dùng 1 shot ở `2.06#2` |"),

    # B3.4 — ảnh sinh thêm
    ("| — | `3.05#7` (\"cửa bẩy dưới bàn ăn\") **chưa có ảnh nào** | ✅ Sinh mới `t3_trapdoor` |",
     "| — | `3.05#7` (\"cửa bẩy dưới bàn ăn\") **chưa có ảnh nào** | ✅ Sinh mới `t3_trapdoor` |\n"
     "| — | `2.06#2` (\"khu vườn sau nhà\" — nơi chôn đầu nạn nhân) **chưa có ảnh nào** | ✅ Sinh mới `t3_backyard_garden` — vườn sau nhà đêm mưa; **không vẽ hố, không vẽ vật thể** (V9) |"),

    # B4.1 — số prompt trong file job
    ("| `.work/bg_jobs_tap03.json` | Danh sách prompt 45 ảnh (format giống `bg_jobs.json` / `bg_jobs_tap02.json`) |",
     "| `.work/bg_jobs_tap03.json` | Danh sách prompt **48 ảnh** (47 đã sinh + `t3_gavel` chờ connector ổn định; format giống `bg_jobs.json` / `bg_jobs_tap02.json`) |"),

    # B5 — nhịp ảnh
    ("Bộ 45 ảnh này vẫn hợp lý: 45 ảnh / 25,8 phút = **1 ảnh ≈ 34 s**",
     "Bộ 46 ảnh dùng được này vẫn hợp lý: 46 ảnh / 25,8 phút = **1 ảnh ≈ 34 s**"),
    ("nếu dùng đủ 45 ảnh thì cần **giảm nhịp hoặc tái neo ảnh này** cho một câu khác; còn 44 ảnh thì không vấn đề.",
     "nếu dùng đủ 47 ảnh thì cần **giảm nhịp hoặc tái neo ảnh này** cho một câu khác; còn 46 ảnh thì không vấn đề."),
]

for old, new in REPL:
    n = raw.count(old)
    assert n == 1, f"KHONG DUNG MOT LAN ({n}): {old[:80]!r}"
    raw = raw.replace(old, new, 1)
    print(f"  OK  {old[:70]}")

# Thêm mục mới: bảng âm thanh Tập 03 ở cuối mục B4
old_b4 = """| 6 | Bảng nguồn tham khảo theo từng câu (A10) | ✅ `02_SAN_XUAT/Tap03/xuat_ban/nguon_tham_khao.md` — đã tạo, 19 câu + phụ lục nguyên văn tiếng Anh; **cần người dùng điền link** |"""
new_b4 = old_b4 + """
| 7 | Bảng âm thanh Tập 03 | ✅ `.work/sfx_tap03.json` (10 nền + 20 tiếng động) — xem `02_SAN_XUAT/Tap03/AmThanh_Tap03.md` |
| 8 | Dựng audio TTS + trộn cho Tập 03 | **Chưa làm** — cần `EPISODES["03"]` trong `.work/edition.py` (mục 3, 4 ở trên) trước khi `build_audio3.py` chạy được |"""
assert raw.count(old_b4) == 1
raw = raw.replace(old_b4, new_b4, 1)
print("  OK  them muc 7-8 vao B4")

MD.write_text(raw, encoding="utf-8")
print(f"\nDa ghi {MD}  ({len(orig)} -> {len(raw)} byte)")
