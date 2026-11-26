# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 36 — HỘI CHỨNG ĐIÊN LOẠN CHUNG (FOLIE À DEUX) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 5: Tâm lý học Xã hội & Động lực Nhóm |
| Tên tập (VI) | **Tập 36: Hội chứng điên loạn chung (Folie à deux)** |
| Tên tập (EN) | **Ep. 36: Folie à Deux — Shared Delusion** |
| Tên tập (JA) | **第36話：感応精神病（フォリー・ア・ドゥ）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap36_folie_a_deux_dien_loan_chung.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap36.json` |
| Chủ đề chuyên sâu | Nhóm 5: Rối Loạn Hoang Tưởng Chia Sẻ (Folie à deux / Shared Psychotic Disorder) & Cặp Đôi Tội Phạm. |
| Hồ sơ dẫn chứng | Ngôi nhà số hai mươi lăm phố Cromwell (Fred và Rose West — Gloucester, Vương quốc Anh giai đoạn một nghìn chín trăm sáu mươi bảy đến một nghìn chín trăm tám mươi bảy) & Vụ án cặp chị em song sinh Ursula và Sabina Eriksson (đường cao tốc M6, Vương quốc Anh năm hai nghìn không trăm linh tám). |
| Quy mô kịch bản (đo thật) | **230 câu thoại** · **7,425 từ** · **42 phần tử** (23 lượt nói) · 5 hồi · ước lượng ~**53.0 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 77 câu · **Chuyên gia Tâm lý (Cáo)**: 55 câu · **Điều tra viên (Sói)**: 54 câu · **Người dân N1 (Cừu)**: 18 câu · **Người dân N2 (Mèo)**: 14 câu · **Người dân N3 (Khách mời đường phố)**: 12 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **230 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap36/bg_jobs_tlhtp_tap36.json` — **139 job ảnh** (độc lập: **139** · trạng thái: **ĐẠT H25/H27 (sẵn sàng sinh ảnh)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap36.json` (**230 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap36/` (VI) · `Tap36_EN/` (EN) · `Tap36_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **230 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap36[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap36.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:45) (25 câu thoại · ~822 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng tích tắc kim đồng hồ kim loại gõ chậm, tạo cảm giác bức bách nghẹt thở.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (25 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "SỰ LÂY NHIỄM TÂM LÝ TIÊU CỰC TRONG TÌNH YÊU" (04:45 – 10:15) (57 câu thoại · ~1617 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (57 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: KHOA HỌC VỀ FOLIE À DEUX & HAI HỒ SƠ RÚNG ĐỘNG NƯỚC ANH (10:15 – 19:30) (82 câu thoại · ~2898 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (82 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (19:30 – 23:30) (33 câu thoại · ~1098 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (33 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (23:30 – 27:30) (33 câu thoại · ~990 từ)
- **Nhạc nền mở hồi (BGM):** Tiếng Cello ấm dần nhưng vẫn u buồn, tiếng mưa rơi tí tách ngoài cửa sổ.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (33 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

