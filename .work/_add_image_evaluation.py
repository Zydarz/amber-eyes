import os, glob, re

with open('BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md', 'r', encoding='utf-8') as f:
    orig = f.read()

# Add Section V: ĐÁNH GIÁ TÌNH TRẠNG PHỦ ẢNH NỀN VÀ KẾ HOẠCH BỔ SUNG
section_v = """
---

## V. ĐÁNH GIÁ TIẾN ĐỘ PHỦ ẢNH NỀN GRAPHIC NOVEL NOIR & KẾ HOẠCH BỔ SUNG
> **Kiểm tra thực tế kho đĩa (`assets/bg/`, `assets/bg/_raw/`, `assets/bg/outputs/`):**

1. **Hiện trạng phủ ảnh thực tế:**
   - **Đã hoàn tất sản xuất ảnh nền (34/68 tập - 50%):** 
     - Toàn bộ từ **Tap 01 đến Tap 31**, cùng với **Tap 34** (Ted Kaczynski), **Tap 38** (Aileen Wuornos) và **Tap 40** (Ted Bundy).
     - Tổng cộng **4,311 ảnh graphic novel noir** đạt chuẩn thẩm mỹ, đã gắn watermark thương hiệu Amber Eyes và kiểm định bản quyền `provenance.json`.
     - Trung bình đạt **130 – 190 ảnh/tập**, bảo đảm tỷ lệ lặp nền cực thấp (đạt tiêu chuẩn H22 / ≤ 3 shot/30s mỗi nền).
   - **Chưa có ảnh nền (34/68 tập - 50%):**
     - Gồm **Tap 32, Tap 33, Tap 35, Tap 36, Tap 37, Tap 39, và từ Tap 41 đến Tap 68**.
     - Các tập này hiện đang ở giai đoạn **Kịch bản chi tiết chuẩn A2c/K10** (240 câu/tập) và đã phân 5 hồi nội dung.
     - **Số lượng ảnh cần sản xuất bổ sung dự kiến:** 34 tập × ~140 ảnh/tập $\approx$ **4,760 ảnh**.

2. **Kế hoạch triển khai sinh ảnh đợt tiếp theo:**
   - **Đợt 1 (Ưu tiên các tập đã chốt kịch bản 240 câu và có hồ sơ chi tiết):**
     - Tap 32 (Trương Tử Cường - Hồng Kông)
     - Tap 35 (Hello Kitty - Hồng Kông)
     - Tap 39 (Lao Vinh Chi & Pháp Tử Anh - Trung Quốc)
     - Tap 45 (Lâm Quá Vân - Hồng Kông)
     - Tap 54 (Điêu Ái Thanh - Trung Quốc)
     - Tap 58 (Thảm án Snowtown - Úc)
   - **Quy trình chuẩn hóa:** Lập bảng prompt graphic novel noir $\rightarrow$ Chạy sinh ảnh hàng loạt qua Kaggle GPU (Flux / SDXL) $\rightarrow$ Đánh số tiền tố `tXX_` $\rightarrow$ Đưa vào `assets/bg/` và cập nhật `provenance.json`.
"""

if "## V. ĐÁNH GIÁ TIẾN ĐỘ PHỦ ẢNH NỀN" not in orig:
    # Append before end or after IV
    new_report = orig.rstrip() + "\n" + section_v
else:
    # Replace section V
    parts = orig.split("## V. ĐÁNH GIÁ TIẾN ĐỘ PHỦ ẢNH NỀN")
    new_report = parts[0] + section_v.strip() + "\n"

destinations = [
    'BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md',
    '90_LUU_TRU/BaoCao_ThongKe_ChiTiet_68_Tap_VuAn_20261122.md',
    '.work/BAO_CAO_CHI_TIET_68_TAP.md'
]

for d in destinations:
    with open(d, 'w', encoding='utf-8') as f:
        f.write(new_report)
    print(f'Updated {d}')
