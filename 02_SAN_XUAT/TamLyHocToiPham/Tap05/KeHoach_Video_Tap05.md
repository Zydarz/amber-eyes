# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 05 — CHUYỂN DỊCH (DISPLACEMENT) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 1: Cơ chế Phòng vệ Vô thức |
| Tên tập (VI) | **Tập 05: Chuyển dịch (Displacement)** |
| Tên tập (EN) | **Ep. 05: Displacement** |
| Tên tập (JA) | **第05話：置き換え（ディスプレイスメント）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap05_chuyen_dich_displacement.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap05.json` |
| Chủ đề chuyên sâu | Nhóm 1: Cơ chế Phòng vệ Vô thức — Phần 5: Chuyển Dịch (Displacement) & Bia Đỡ Đạn Của Sự Hèn Nhát. |
| Hồ sơ dẫn chứng | Các vụ án bạo lực gia đình bột phát & Vụ án Luby's Cafeteria tại Killeen, Texas (ngày 16/10/1991 — George Hennard, 23 người thiệt mạng và 27 người bị thương). |
| Quy mô kịch bản (đo thật) | **215 câu thoại** · **5,263 từ** · **43 phần tử** (24 lượt nói) · 5 hồi · ước lượng ~**37.6 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 62 câu · **Chuyên gia Tâm lý (Cáo)**: 59 câu · **Điều tra viên (Sói)**: 55 câu · **Người dân N1 (Cừu)**: 15 câu · **Người dân N2 (Mèo)**: 13 câu · **Người dân N3 (Khách mời đường phố)**: 11 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **215 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap05/bg_jobs_tlhtp_tap05.json` — **162 job ảnh** (độc lập: **162** · trạng thái: **ĐẠT H25/H27 (sẵn sàng sinh ảnh)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap05.json` (**215 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap05/` (VI) · `Tap05_EN/` (EN) · `Tap05_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **215 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap05[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap05.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — CƠN GIẬN TÌM KẺ YẾU THẾ (00:00 – 05:00) (27 câu thoại · ~588 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient nặng nề, tiếng Sub-bass rền nhẹ phía dưới như một cơn giông bão đang tích tụ.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (27 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN ĐÃ TRÚT GIẬN LÊN AI?" (05:00 – 10:30) (53 câu thoại · ~1163 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (53 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: GÂY HẤN CHUYỂN DỊCH & THẢM KỊCH LUBY'S CAFETERIA NĂM 1991 (10:30 – 18:30) (58 câu thoại · ~1519 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (58 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: QUY LUẬT DÒNG CHẢY NĂNG LƯỢNG & KẺ BẠO CHÚA SAU CÁNH CỬA (18:30 – 23:30) (35 câu thoại · ~903 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (35 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00) (42 câu thoại · ~1090 từ)
- **Nhạc nền mở hồi (BGM):** Piano ấm dần lên trên nền Ambient tĩnh lặng, mang màu sắc thanh lọc và chữa lành.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (42 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

