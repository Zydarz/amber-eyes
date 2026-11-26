# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 41 — CHIẾN LỢI PHẨM & THỜI GIAN NGUỘI (TROPHIES & COOLING-OFF PERIOD) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 6: Hành vi Hiện trường & Phân tích Tội phạm (Offender Profiling) |
| Tên tập (VI) | **Tập 41: Chiến lợi phẩm & Thời gian nguội (Trophies & Cooling-off Period)** |
| Tên tập (EN) | **Ep. 41: Trophies & Cooling-Off Period** |
| Tên tập (JA) | **第41話：戦利品（トロフィー）と冷却期間** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap41_chien_loi_pham_va_cooling_off.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap41.json` |
| Chủ đề chuyên sâu | Nhóm 6: Chiến Lợi Phẩm (Trophies & Souvenirs) & Chu Kỳ Thời Gian Nguội (Cooling-off Period). |
| Hồ sơ dẫn chứng | Phân loại tội phạm giết người hàng loạt (Serial Killer) vs. Giết người liên hoàn bộc phát (Spree Killer), Hội thảo FBI năm hai nghìn không trăm linh năm, Mô hình bảy giai đoạn của Tiến sĩ Joel Norris & Hồ sơ Jeffrey Dahmer (Milwaukee, Wisconsin năm một nghìn chín trăm chín mươi mốt). |
| Quy mô kịch bản (đo thật) | **178 câu thoại** · **4,965 từ** · **35 phần tử** (19 lượt nói) · 5 hồi · ước lượng ~**35.5 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 79 câu · **Điều tra viên (Sói)**: 35 câu · **Chuyên gia Tâm lý (Cáo)**: 32 câu · **Người dân N3 (Khách mời đường phố)**: 12 câu · **Người dân N1 (Cừu)**: 11 câu · **Người dân N2 (Mèo)**: 9 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **178 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap41/bg_jobs_tlhtp_tap41.json` — **0 job ảnh** (độc lập: **0** · trạng thái: **CHỜ LẬP BẢNG SHOT & PROMPT (H25/H27)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap41.json` (**178 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap41/` (VI) · `Tap41_EN/` (EN) · `Tap41_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **178 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap41[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap41.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 06:00) (43 câu thoại · ~1168 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng tích tắc kim đồng hồ kim loại gõ chậm, tạo cảm giác bức bách nghẹt thở.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (43 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "KỶ VẬT VÀ NHU CẦU NEO GIỮ CẢM XÚC" (06:00 – 12:00) (40 câu thoại · ~968 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (40 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: KHOA HỌC PHÁC HỌA TÂM LÝ VỀ CHU KỲ SÁT NHÂN & HỒ SƠ JEFFREY DAHMER (12:00 – 20:00) (46 câu thoại · ~1494 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (46 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (20:00 – 25:30) (25 câu thoại · ~752 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (25 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (25:30 – 30:00) (24 câu thoại · ~583 từ)
- **Nhạc nền mở hồi (BGM):** Tiếng Cello ấm dần nhưng vẫn u buồn, tiếng mưa rơi tí tách ngoài cửa sổ.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (24 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

