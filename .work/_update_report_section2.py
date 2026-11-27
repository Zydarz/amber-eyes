#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat bang Episode Series 1 (muc II) trong bao cao 68 tap."""
import pathlib, shutil, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / "BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md"
BK = ROOT / ".work" / "_cu" / "BaoCao_ThongKe_68_truoc_cap_nhat_IX_20261127.md"
BK.parent.mkdir(exist_ok=True)
if not BK.exists():
    shutil.copy2(MD, BK)
    print("sao luu ->", BK)

txt = MD.read_text(encoding="utf-8")
orig = txt

# --- 1. Lam sach o nhien tap 01-09 (corrupted " \tNN_|" -> "|") ---
bad = "Bảng shot timeline đã neo audio master · 26/11: chưa có ảnh · 26/11: ảnh gốc còn ở _raw/, chưa có file theo tiền tố \tNN_|"
good = "Bảng shot timeline đã neo audio master · 26/11: chưa có ảnh · 26/11: ảnh gốc còn ở `_raw/`, chưa có file theo tiền tố `tNN_` |"
n = txt.count(bad)
txt = txt.replace(bad, good)
print("ve sinh o nhien tap 01-09:", n)

# --- 2. Tap 64 / 66 / 68: bo "chua co anh" bi lap ---
for ep in ("64", "66", "68"):
    dup = " · 26/11: chưa có ảnh · 26/11: chưa có ảnh|"
    # xoa lan cuoi trong dong chua Tap XX
    txt = txt.replace(dup, " · 26/11: chưa có ảnh, chưa có `bg_jobs` (chờ mở rộng kịch bản H23)|")

# --- 3. Tap 41 / 42 / 43 ---
subs = [
    ("| Anh | **240** | **0** | **245** | Quy tắc chuẩn (240 câu + 5 thẻ chuyển/kết) · 26/11: còn thiếu 157 ảnh|",
     "| Anh | **240** | **157** | **245** | Quy tắc chuẩn (240 câu + 5 thẻ chuyển/kết) · **27/11: đã đủ 157/157 ảnh** (Cloudflare FLUX 26/11 — xem mục IX.1) |"),
    ("| Nhật Bản | **240** | **0** | **245** | Quy tắc chuẩn (240 câu + 5 thẻ chuyển/kết) · 26/11: còn thiếu 210 ảnh|",
     "| Nhật Bản | **240** | **210** | **245** | Quy tắc chuẩn (240 câu + 5 thẻ chuyển/kết) · **27/11: đã đủ 210/210 ảnh** (Cloudflare FLUX 26/11 — xem mục IX.1) |"),
    ("| Brazil | **240** | **0** | **245** | Quy tắc chuẩn (240 câu + 5 thẻ chuyển/kết) · 26/11: còn thiếu 159 ảnh|",
     "| Brazil | **240** | **2** | **245** | Quy tắc chuẩn (240 câu + 5 thẻ chuyển/kết) · **27/11: mới sinh 2/159 ảnh, còn thiếu 157** (đợt Cloudflare 26/11 bị dừng) |"),
]
for a, b in subs:
    assert txt.count(a) == 1, ("khong khop duy nhat", a[:60], txt.count(a))
    txt = txt.replace(a, b)
print("cap nhat dong Tap 41/42/43: OK")

# --- 4. Them dong Tap 69 sau dong Tap 68 ---
tap68_line = [l for l in txt.split("\n") if l.startswith("| **Tap 68**")]
assert len(tap68_line) == 1, tap68_line
tap69 = ("| **Tap 69** | Hồ Sơ Đoàn Văn Sáng — VỎ BỌC CÔNG QUYỀN, HỘI NHÓM KÍN VÀ MƯỜI THÁNG "
         "SỐNG HAI MẶT TẠI LẠNG SƠN | Việt Nam | **234** | **0** | **0** | "
         "**MỚI 27/11/2026** — 5 Hồi · 40 lượt thoại (H 16 · D 12 · C 10 · N 2) · "
         "chưa lập `bg_jobs`, chưa có `Bang_Shot_Anh`, chưa vào `02_SAN_XUAT` |")
txt = txt.replace(tap68_line[0], tap68_line[0] + "\n" + tap69)
print("them dong Tap 69: OK")

MD.write_text(txt, encoding="utf-8")
print("da ghi:", MD, "| thay doi:", len(orig) != len(txt))
