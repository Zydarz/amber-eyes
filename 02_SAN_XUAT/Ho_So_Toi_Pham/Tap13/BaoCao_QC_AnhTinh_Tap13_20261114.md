# BÁO CÁO KIỂM ĐỊNH QC BỘ ẢNH TĨNH (STILLS) TẬP 13 — 3 NGÔN NGỮ

**Dự án:** Kênh YouTube Amber Eyes — Phân tích tâm lý học tội phạm  
**Tập:** Tập 13 — Hồ sơ Jennifer Pan (*Vỏ bọc 'Con nhà người ta' & Lời nói dối 10 năm*)  
**Ngày thực hiện:** 14/11/2026  
**Quy chuẩn áp dụng:** `AGENTS.md` (Quy tắc L1–L10, H1–H21, T23, T24), `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` v1.0.

---

## 1. Tổng quan số đo sản xuất (Quy tắc L3)

- **Kịch bản gốc nâng cấp:** 50 elements (31 LOI, 210 câu thoại đạt chuẩn Hệ sinh thái 10 chỉ dấu tâm lý & hành vi).
- **Bộ ảnh nền FLUX.2 gốc:** 81 ảnh nền (`assets/bg/t13_*.png`, kích thước 2112×1188, tỷ lệ 16:9 2K).
- **Tổng số shot mỗi ngôn ngữ:** 215 shot (210 shot câu thoại + 4 shot tiêu đề Hồi T10 + 1 shot thẻ kết T2).
- **Tổng số ảnh tĩnh (stills) đã render:** **645 ảnh tĩnh**
  - **Tiếng Việt (VI):** 215 ảnh (`.work/video3_t13/stills/shot_*.png`)
  - **Tiếng Anh (EN):** 215 ảnh (`.work/video3_EN_t13/stills/shot_*.png`)
  - **Tiếng Nhật (JA):** 215 ảnh (`.work/video3_JA_t13/stills/shot_*.png`)
- **Thời gian render pipeline song song:** 193.63 giây (~3.23 phút).
- **Tốc độ render trung bình:** 3.33 ảnh/giây.

---

## 2. Kiểm định kỹ thuật & Quy chuẩn hình ảnh

### A. Quy tắc chia sẻ ảnh nền (Rule H17, T23, T24)
- **Công cụ kiểm tra:** `qc_bg_shared.py --ep 13`
- **Kết quả:** **ĐẠT (100%)**
  - Mọi shot ở 3 ngôn ngữ (VI, EN, JA) đều dùng chung **duy nhất 1 file ảnh nền gốc** `assets/bg/t13_*.png`.
  - Không có file nền nào mang hậu tố ngôn ngữ riêng biệt.
  - Tối ưu hóa dung lượng lưu trữ và đảm bảo tính nhất quán thị giác tuyệt đối trên toàn bộ các kênh phân phối.

### B. Kiểm định độ tương phản chữ (Rule H20)
- **Công cụ kiểm tra:** `qc_contrast_t13.py` (quét dải pixel chữ Y: 700–1010 theo bảng màu linh thú `ROLE_COLOR`).
- **Kết quả:**
  - `[VI]` Quét 215 ảnh | **0 lỗi chữ chìm**
  - `[EN]` Quét 215 ảnh | **0 lỗi chữ chìm**
  - `[JA]` Quét 215 ảnh | **0 lỗi chữ chìm**
  - **Tổng kết:** **100% ĐẠT CHUẨN TƯƠNG PHẢN (Tỷ lệ tương phản r ≥ 1.6, ΔL ≥ 0.045)**.

### C. Bố cục Layout & Template chuyên dụng
- **Template T1 (Thoại tiêu chuẩn):** 200 shot (Host Cú, Điều tra viên Sói, Chuyên gia tâm lý Cáo).
- **Template T4 (Nhân chứng & Lời khai):** 11 shot
  - Hồi 1 (`1-11` đến `1-16`): Lời tâm sự từ bạn học phổ thông (`N1: BẠN HỌC`).
  - Hồi 4 (`4-16` đến `4-21`): Lời trần tình trong đau đớn của người cha sống sót (`N2: HUEI HANN PAN`).
- **Template T8 (Cảnh báo đỏ sinh tồn):** 4 shot (`5-18`, `5-22`, `5-26`, `5-30`) làm nổi bật 4 tín hiệu báo động đỏ kinh điển.
- **Template T10 (Tiêu đề chuyển hồi):** 4 shot (`1-43`, `2-42`, `3-44`, `4-43`) với chữ đậm và chuyển cảnh dip-to-black.
- **Template T2 (Thẻ kết hồ sơ):** 1 shot (`5-43`) với thông điệp đóng hồ sơ Amber Eyes.

---

## 3. Danh mục Artifact QC đã tạo

1. **Bảng Montage ảnh tĩnh Tiếng Việt:** `.work/qc_montage/ep13_stills_vi.jpg` (3104×7020, 215 ảnh, 27 hàng × 8 cột).
2. **Bảng Montage ảnh tĩnh Tiếng Anh:** `.work/qc_montage/ep13_stills_en.jpg` (3104×7020, 215 ảnh, 27 hàng × 8 cột).
3. **Bảng Montage ảnh tĩnh Tiếng Nhật:** `.work/qc_montage/ep13_stills_ja.jpg` (3104×7020, 215 ảnh, 27 hàng × 8 cột).
4. **Bảng Montage ảnh nền gốc FLUX.2:** `.work/qc_montage/ep13_bg.jpg` (3104×2860, 81 ảnh nền).
