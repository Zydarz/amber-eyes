# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 04 — TRÍ TUỆ HÓA (INTELLECTUALIZATION) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 1: Cơ chế Phòng vệ Vô thức |
| Tên tập (VI) | **Tập 04: Trí tuệ hóa (Intellectualization)** |
| Tên tập (EN) | **Ep. 04: Intellectualization** |
| Tên tập (JA) | **第04話：知性化（インテレクチュアライゼーション）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap04_tri_tue_hoa_intellectualization.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap04.json` |
| Chủ đề chuyên sâu | Nhóm 1: Cơ chế Phòng vệ Vô thức — Phần 4: Trí Tuệ Hóa (Intellectualization) & Sự Lạnh Lùng Của Tri Thức. |
| Hồ sơ dẫn chứng | Vụ án Nathan Leopold & Richard Loeb (Chicago, ngày 21/05/1924 — hai sinh viên Đại học Chicago bị ám ảnh bởi diễn giải méo mó triết lý "Siêu nhân" của Nietzsche và phiên tòa lịch sử của luật sư Clarence Darrow). |
| Quy mô kịch bản (đo thật) | **208 câu thoại** · **5,446 từ** · **41 phần tử** (23 lượt nói) · 5 hồi · ước lượng ~**38.9 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 62 câu · **Điều tra viên (Sói)**: 59 câu · **Chuyên gia Tâm lý (Cáo)**: 56 câu · **Người dân N1 (Cừu)**: 13 câu · **Người dân N2 (Mèo)**: 10 câu · **Người dân N3 (Khách mời đường phố)**: 8 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **208 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap04/bg_jobs_tlhtp_tap04.json` — **167 job ảnh** (độc lập: **167** · trạng thái: **ĐẠT H25/H27 (sẵn sàng sinh ảnh)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap04.json` (**208 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap04/` (VI) · `Tap04_EN/` (EN) · `Tap04_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **208 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap04[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap04.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — KHI TRÁI TIM ĐƯỢC THAY BẰNG THƯỚC ĐO (00:00 – 05:00) (31 câu thoại · ~627 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient lạnh lẽo, âm thanh máy đo nhịp tim kêu chậm, đều đặn, phẳng lặng như không có cảm xúc.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (31 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN DÙNG LÝ TRÍ ĐỂ TRỐN TRÁNH ĐIỀU GÌ?" (05:00 – 10:30) (43 câu thoại · ~1065 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng, mang màu sắc phóng sự phỏng vấn.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (43 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: SỰ TÁCH RỜI CẢM XÚC & VỤ ÁN THẾ KỶ LEOPOLD VÀ LOEB (10:30 – 18:30) (62 câu thoại · ~1823 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng gõ kim loại nhịp nhàng khô khốc.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (62 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: XÃ HỘI DUY LÝ & NGUY CƠ VÔ CẢM CỦA CON NGƯỜI HIỆN ĐẠI (18:30 – 23:30) (36 câu thoại · ~973 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại lạnh lùng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (36 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00) (36 câu thoại · ~958 từ)
- **Nhạc nền mở hồi (BGM):** Piano ấm dần lên trên nền Ambient tĩnh lặng, mang màu sắc thanh lọc nhận thức.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (36 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

