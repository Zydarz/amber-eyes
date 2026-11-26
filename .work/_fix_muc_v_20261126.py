#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sửa mục V của BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md (26/11/2026)."""
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md"
CU = ROOT / ".work" / "_cu"

NEW_V = """1. **Hiện trạng phủ ảnh thực tế (đo lại 26/11/2026 — quét từng file `assets/bg/`):**
   - **Đã có ảnh nền và đủ theo job (26/68 tập - 38.2%):**
     - Gồm: **Tap 10 → Tap 30**, **Tap 36, Tap 37, Tap 38, Tap 39, Tap 40** (liên tục 10–30, rồi 36–40).
     - Tổng cộng **4,020 ảnh graphic novel noir** theo tiền tố tập trên ổ cứng, đã kiểm định bản quyền `provenance.json` (6.709 dòng).
     - **Tap 30 (Nguyễn Đức Nghĩa)** đã đủ **204 ảnh** = số job; **Tap 37/38/39 đã đủ 122/188/135 ảnh** (đợt Cloudflare 25–26/11 — xem mục VIII).
   - **Chưa có ảnh nền (42/68 tập - 61.8%):**
     - Gồm: **Tap 01–09** (ảnh gốc còn nằm trong `assets/bg/_raw/`, không theo tiền tố `tNN_`), **Tap 31–35**, **Tap 41–68** (trừ Tap 64, 66, 68 chưa có `bg_jobs`).
     - **Số lượng ảnh cần sản xuất bổ sung:** **4,622 ảnh** cho 30 tập đã có `bg_jobs_tapXX.json` (31, 32, 33, 34, 35, 41–63, 65, 67).

2. **Kế hoạch triển khai sinh ảnh đợt tiếp theo:**
   - **Đợt 1 (Ưu tiên các tập kịch bản 240 câu tiêu biểu, theo số lượng ảnh tăng dần):**
     - Tap 45 (Lâm Quá Vân - Hồng Kông, 174 ảnh)
     - Tap 54 (Điêu Ái Thanh - Trung Quốc, 158 ảnh)
     - Tap 58 (Thảm án Snowtown - Úc, 150 ảnh)
   - **Nguồn sinh ảnh:** **Cloudflare Workers AI FLUX.1-schnell** (user chốt 25/11/2026 — không dùng Kaggle). Hạn mức 10.000 neurons/tài khoản/ngày × 6 tài khoản ⇒ ~360 ảnh/ngày; chia 3 tiến trình song song, mỗi tập ghim 1 account.
   - **Quy trình chuẩn hóa:** Lập bảng prompt graphic novel noir → Chạy sinh ảnh hàng loạt qua Cloudflare FLUX → Đánh số tiền tố `tXX_` → Đưa vào `assets/bg/` và cập nhật `provenance.json` → soi mắt 100 % → `map_shot_anh.py --check`.
   - **Quy tắc bắt buộc khi sinh ảnh (bài học Tập 37–39, mục VIII.4):** không dùng câu cấm chữ (*no text / no signage*) — FLUX bỏ qua và còn vẽ chữ; phải **loại vật thể mang chữ khỏi khung** và mô tả bề mặt trơn (*blank / unmarked / plain*).
"""


def main():
    txt = REPORT.read_text(encoding="utf-8-sig")
    start = txt.index("1. **Hiện trạng phủ ảnh thực tế:**")
    end = txt.index("## VI. CẬP NHẬT 25/11/2026")
    tail = txt[end:]
    head = txt[:start]
    new = head + NEW_V + "\n" + tail

    CU.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    bak = CU / f"BaoCao_ThongKe_68_truoc_sua_muc_V_{stamp}.md"
    shutil.copy2(REPORT, bak)
    REPORT.write_text(new, encoding="utf-8")
    print(f"Da sua muc V. backup: {bak.name}")


if __name__ == "__main__":
    main()
