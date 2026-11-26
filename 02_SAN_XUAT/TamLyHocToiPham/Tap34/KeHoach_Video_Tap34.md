# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 34 — PHI CÁ NHÂN HÓA (DEINDIVIDUATION) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 5: Tâm lý học Xã hội & Động lực Nhóm |
| Tên tập (VI) | **Tập 34: Phi cá nhân hóa (Deindividuation)** |
| Tên tập (EN) | **Ep. 34: Deindividuation** |
| Tên tập (JA) | **第34話：没個性化（ディインディビジュエーション）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap34_phi_ca_nhan_hoa_deindividuation.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap34.json` |
| Chủ đề chuyên sâu | Nhóm 5: Tâm Lý Học Đám Đông — Phi Cá Nhân Hóa (Deindividuation) & Hiệu Ứng Mặt Nạ Vô Danh. |
| Hồ sơ dẫn chứng | Thảm họa sân vận động Heysel (Bỉ năm một nghìn chín trăm tám mươi lăm) & Làn sóng bắt nạt hội đồng trên không gian mạng dẫn đến cái chết của Hana Kimura (năm hai nghìn không trăm hai mươi). |
| Quy mô kịch bản (đo thật) | **243 câu thoại** · **4,950 từ** · **49 phần tử** (32 lượt nói) · 5 hồi · ước lượng ~**35.4 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 146 câu · **Chuyên gia Tâm lý (Cáo)**: 42 câu · **Điều tra viên (Sói)**: 37 câu · **Người dân N1 (Cừu)**: 7 câu · **Người dân N2 (Mèo)**: 7 câu · **Người dân N3 (Khách mời đường phố)**: 4 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **243 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap34/bg_jobs_tlhtp_tap34.json` — **175 job ảnh** (độc lập: **129** · trạng thái: **ĐÃ CHUYỂN JSON · CẢNH BÁO TRÙNG PROMPT (129/175)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap34.json` (**243 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap34/` (VI) · `Tap34_EN/` (EN) · `Tap34_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **243 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap34[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap34.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:30) (41 câu thoại · ~825 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng tích tắc kim đồng hồ kim loại gõ chậm, tạo cảm giác bức bách nghẹt thở.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (41 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ DÁM LÀM ĐIỀU ÁC KHI KHÔNG AI BIẾT MÌNH LÀ AI?" (04:30 – 09:15) (48 câu thoại · ~898 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (48 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: KHOA HỌC VỀ DEINDIVIDUATION & HAI THẢM ÁN ĐÁM ĐÔNG (09:15 – 14:15) (59 câu thoại · ~1308 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (59 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (14:15 – 19:15) (51 câu thoại · ~1052 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (51 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (19:15 – 25:30) (44 câu thoại · ~867 từ)
- **Nhạc nền mở hồi (BGM):** Tiếng Cello ấm dần nhưng vẫn u buồn, tiếng mưa rơi tí tách ngoài cửa sổ.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (44 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

