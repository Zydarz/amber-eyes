# BÁO CÁO BỔ SUNG & KIỂM ĐỊNH MÔ TẢ TẬP 20 (4 NGÔN NGỮ)

**Hồ sơ vụ án:** Stephen McDaniel (Khoảnh Khắc Sụp Đổ Trước Ống Kính — Ám Ảnh Rình Rập & Phản Ứng Đóng Băng Kỳ Dị)  
**Thời gian thực hiện:** 07/11/2026  
**Căn cứ quy chuẩn:** `AGENTS.md` (L1–L10, K1–K10, V9), `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Mục A2c — Hệ sinh thái 10 chỉ dấu tâm lý & hành vi bắt buộc, giới hạn YouTube Description $\le 5.000$ ký tự).

---

## 1. TỔNG QUAN CÔNG VIỆC THỰC HIỆN

1. **Kiểm tra chính tả & chuẩn hóa ngôn ngữ 4 bản (VN, EN, JA, KO):**
   - **Bản Tiếng Việt (VN):** Kiểm tra ngữ pháp, dấu câu, cặp ngoặc đối xứng; tinh chỉnh cụm từ "khả năng thấu cảm cảm xúc" thành "năng lực thấu cảm" nhằm tránh lỗi vấp lặp từ kép ("cảm cảm") khi TTS đọc; loại bỏ 100% từ cấm bạo lực theo V9 (`thi thể` -> `phát hiện đau lòng`).
   - **Bản Tiếng Anh (EN):** Chuẩn hóa US English đồng nhất (`labored`); rút gọn tên trường luật ở phần mở đầu tránh chia tách câu sai do viết tắt có dấu chấm (`Mercer University School of Law`); kiểm tra 0 lỗi ngữ pháp.
   - **Bản Tiếng Nhật (JA):** Loại bỏ dấu chấm nội bộ `。` giữa các vế câu trong cùng một lượt thoại để đảm bảo đối ứng câu 1:1 tuyệt đối với bản gốc; chuẩn hóa địa danh Katakana (`バリスターズ・ホール`).
   - **Bản Tiếng Hàn (KO):** Bổ sung thuật ngữ Latinh gốc trong ngoặc đơn đi kèm Hangul để vượt qua cổng kiểm định A9-KO (`_qc_ko_parity.py`); định dạng tiêu đề các hồi theo cú pháp `## 막 1: ...` đến `## 막 5: ...`.

2. **Bổ sung và tối ưu hóa phần mô tả video cho cả 4 ngôn ngữ (VN, EN, JA, KO):**
   - Đảm bảo đầy đủ 7 khối nội dung bắt buộc:
     1. Tiêu đề chuẩn SEO và nhận diện thương hiệu `Amber eyes`.
     2. 2 đoạn văn tóm lược hồ sơ / hook mở đầu tạo tò mò khoa học.
     3. **Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi (§A2c)** được tóm gọn súc tích, sắc bén.
     4. Mốc thời gian các chương (Timestamps) 5 hồi khớp cấu trúc kịch bản.
     5. Khuyến cáo pháp lý, chuẩn mực an toàn V9 và công bố AI.
     6. Danh mục nguồn tư liệu tư pháp chính thức (Tòa Thượng thẩm Hạt Bibb, DA, Macon PD, GBI, WGXA, Gavin de Becker, FBI BAU).
     7. Đường dây nóng bảo vệ và hỗ trợ khủng hoảng tại từng quốc gia / khu vực.
   - **Tuân thủ nghiêm ngặt giới hạn $\le 5.000$ ký tự của YouTube:** Tất cả 4 ngôn ngữ đều nằm trong ngưỡng an toàn tuyệt đối.

---

## 2. BẢNG ĐO LƯỜNG SỐ LIỆU MÔ TẢ (RULE L3)

| Ngôn ngữ | Số ký tự (Chars) | Giới hạn YouTube | Dung lượng an toàn (Dư) | Trạng thái |
|---|---:|---:|---:|:---:|
| **Tiếng Việt (VN)** | **4.696** | 5.000 | +304 ký tự | **ĐẠT (SAFE)** |
| **Tiếng Anh (EN)** | **4.648** | 5.000 | +352 ký tự | **ĐẠT (SAFE)** |
| **Tiếng Nhật (JA)** | **2.308** | 5.000 | +2.692 ký tự | **ĐẠT (SAFE)** |
| **Tiếng Hàn (KO)** | **2.472** | 5.000 | +2.528 ký tự | **ĐẠT (SAFE)** |

---

## 3. DANH MỤC FILE ĐÃ TẠO VÀ CẬP NHẬT TRÊN HỆ THỐNG

### Bản Tiếng Việt (VN):
- `02_SAN_XUAT/Tap20/mo_ta.txt` (4.696 ký tự)
- `02_SAN_XUAT/Tap20/xuat_ban/mo_ta.txt` (4.696 ký tự)
- `02_SAN_XUAT/Tap20/nguon_mo_ta.txt` (Hồ sơ nguồn đầy đủ)
- `02_SAN_XUAT/Tap20/nguon_tham_khao.md`
- `02_SAN_XUAT/Tap20/xuat_ban/nguon_tham_khao.md`

### Bản Tiếng Anh (EN):
- `02_SAN_XUAT/Tap20_EN/description.txt` (4.648 ký tự)
- `02_SAN_XUAT/Tap20_EN/mo_ta.txt` (4.648 ký tự)
- `02_SAN_XUAT/Tap20_EN/xuat_ban/description.txt` (4.648 ký tự)
- `02_SAN_XUAT/Tap20_EN/xuat_ban/mo_ta.txt` (4.648 ký tự)
- `02_SAN_XUAT/Tap20_EN/nguon_tham_khao_EN.md`
- `02_SAN_XUAT/Tap20_EN/xuat_ban/nguon_tham_khao_EN.md`

### Bản Tiếng Nhật (JA):
- `02_SAN_XUAT/Tap20_JA/description.txt` (2.308 ký tự)
- `02_SAN_XUAT/Tap20_JA/mo_ta.txt` (2.308 ký tự)
- `02_SAN_XUAT/Tap20_JA/xuat_ban/description.txt` (2.308 ký tự)
- `02_SAN_XUAT/Tap20_JA/xuat_ban/mo_ta.txt` (2.308 ký tự)
- `02_SAN_XUAT/Tap20_JA/nguon_tham_khao_JA.md`
- `02_SAN_XUAT/Tap20_JA/xuat_ban/nguon_tham_khao_JA.md`

### Bản Tiếng Hàn (KO):
- `02_SAN_XUAT/Tap20_KO/description.txt` (2.472 ký tự)
- `02_SAN_XUAT/Tap20_KO/mo_ta.txt` (2.472 ký tự)
- `02_SAN_XUAT/Tap20_KO/xuat_ban/description.txt` (2.472 ký tự)
- `02_SAN_XUAT/Tap20_KO/xuat_ban/mo_ta.txt` (2.472 ký tự)
- `02_SAN_XUAT/Tap20_KO/nguon_tham_khao_KO.md`
- `02_SAN_XUAT/Tap20_KO/xuat_ban/nguon_tham_khao_KO.md`

---

## 4. KẾT QUẢ KIỂM ĐỊNH TOÀN DIỆN (GATE QC)

1. **QC Kịch bản 4 ngôn ngữ (`_qc_all_4scripts_tap20.py`):**
   - 100% PASS (51 elements, 32 lượt thoại, 212 câu thoại đối ứng 1:1).
   - 0 lỗi V9 (không từ cấm bạo lực).
   - 0 lỗi G1 (không dấu `...` hay thẻ ngắt trái quy định).
   - 0 lỗi double CR (`\r\r\n`).

2. **QC Đối ứng Tiếng Hàn (`_qc_ko_parity.py`):**
   - 100% PASS (Tỷ lệ Hangul 92,6%, đối ứng 100% cấu trúc, khớp mốc nghỉ và số liệu).

3. **Cửa ngõ YouTube Description:**
   - 100% các file mô tả $\le 5.000$ ký tự, sẵn sàng đăng tải và xuất bản.
