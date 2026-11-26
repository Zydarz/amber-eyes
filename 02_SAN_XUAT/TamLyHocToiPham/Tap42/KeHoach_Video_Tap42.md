# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 42 — HỘI CHỨNG HEROSTRATUS & HIỆU ỨNG BẮT CHƯỚC (COPYCAT EFFECT) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 6: Hành vi Hiện trường & Phân tích Tội phạm (Offender Profiling) |
| Tên tập (VI) | **Tập 42: Hội chứng Herostratus & Hiệu ứng bắt chước (Copycat Effect)** |
| Tên tập (EN) | **Ep. 42: Herostratus Syndrome & Copycat Effect** |
| Tên tập (JA) | **第42話：ヘロストラトス症候群と模倣犯効果** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap42_hoi_chung_herostratus_copycat.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap42.json` |
| Chủ đề chuyên sâu | Nhóm 6: Hội Chứng Herostratus & Hiệu Ứng Bắt Chước (Copycat Effect / Media Contagion). |
| Hồ sơ dẫn chứng | Vụ phóng hỏa Đền thờ Artemis (Herostratus — 356 TCN), Thảm sát trường trung học Columbine (1999) & Làn sóng lây nhiễm truyền thông. |
| Quy mô kịch bản (đo thật) | **225 câu thoại** · **5,626 từ** · **39 phần tử** (21 lượt nói) · 5 hồi · ước lượng ~**40.2 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 96 câu · **Chuyên gia Tâm lý (Cáo)**: 53 câu · **Điều tra viên (Sói)**: 39 câu · **Người bình thường (Vox Pop)**: 37 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **225 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap42/bg_jobs_tlhtp_tap42.json` — **0 job ảnh** (độc lập: **0** · trạng thái: **CHỜ LẬP BẢNG SHOT & PROMPT (H25/H27)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap42.json` (**225 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap42/` (VI) · `Tap42_EN/` (EN) · `Tap42_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **225 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap42[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap42.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — NGỌN LỬA CỦA KẺ KHÁT DANH (00:00 – 05:00) (51 câu thoại · ~1163 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng tích tắc kim đồng hồ kim loại gõ chậm, tạo cảm giác bức bách nghẹt thở.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (51 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — KHÁT KHAO NỔI TIẾNG BẰNG MỌI GIÁ (05:00 – 10:00) (44 câu thoại · ~1119 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (44 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: KHOA HỌC VỀ HIỆU ỨNG WERTHER & SỰ LÂY NHIỄM TRUYỀN THÔNG (10:00 – 16:30) (59 câu thoại · ~1543 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (59 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: CƠ CHẾ TÂM LÝ SÂU THẲM & CUỘC CHIẾN CHỐNG LÂY NHIỄM (16:30 – 21:30) (37 câu thoại · ~982 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (37 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (21:30 – 26:30) (34 câu thoại · ~819 từ)
- **Nhạc nền mở hồi (BGM):** Tiếng Cello ấm dần nhưng vẫn u buồn, tiếng mưa rơi tí tách ngoài cửa sổ.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (34 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

