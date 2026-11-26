# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 03 — PHẢN ỨNG NGƯỢC (REACTION FORMATION) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 1: Cơ chế Phòng vệ Vô thức |
| Tên tập (VI) | **Tập 03: Phản ứng ngược (Reaction Formation)** |
| Tên tập (EN) | **Ep. 03: Reaction Formation** |
| Tên tập (JA) | **第03話：反動形成（リアクション・フォーメーション）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap03_phan_ung_nguoc_reaction_formation.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap03.json` |
| Chủ đề chuyên sâu | Nhóm 1: Cơ chế Phòng vệ Vô thức — Phần 3: Phản Ứng Ngược (Reaction Formation) & Mặt Nạ Của Sự Thánh Thiện. |
| Hồ sơ dẫn chứng | Vụ án Jim Jones và giáo phái Đền thờ Dân tộc (Peoples Temple, 1955–1978 — từ hình tượng nhà hoạt động nhân đạo, Chủ tịch Ủy ban Nhà ở San Francisco đến thảm kịch Jonestown ngày 18/11/1978). |
| Quy mô kịch bản (đo thật) | **218 câu thoại** · **5,788 từ** · **43 phần tử** (24 lượt nói) · 5 hồi · ước lượng ~**41.3 phút** |
| Cấu trúc phân vai | **Chuyên gia Tâm lý (Cáo)**: 64 câu · **Điều tra viên (Sói)**: 62 câu · **Host (Cú)**: 57 câu · **Người dân N1 (Cừu)**: 15 câu · **Người dân N2 (Mèo)**: 10 câu · **Người dân N3 (Khách mời đường phố)**: 10 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **218 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap03/bg_jobs_tlhtp_tap03.json` — **187 job ảnh** (độc lập: **187** · trạng thái: **ĐẠT H25/H27 (sẵn sàng sinh ảnh)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap03.json` (**218 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap03/` (VI) · `Tap03_EN/` (EN) · `Tap03_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **218 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap03[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap03.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — KẺ LỚN TIẾNG NHẤT CHÍNH LÀ KẺ CÓ TỘI (00:00 – 05:00) (26 câu thoại · ~702 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng chuông đồng hồ cổ kính điểm từng nhịp chậm rãi, u tịch.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (26 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ TIN VÀO SỰ HOÀN HẢO?" (05:00 – 10:30) (48 câu thoại · ~1095 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient mang tính chiêm nghiệm xã hội.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (48 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: SỰ ĐỀN BÙ QUÁ MỨC & VỎ BỌC MỤC SƯ JIM JONES (10:30 – 18:30) (66 câu thoại · ~1989 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc Synth u tối, tiếng bass rền nghẹt thở.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (66 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI PHẢI ĐEO MẶT NẠ? CÓ PHẢI AI CŨNG CÓ NGUY CƠ? (18:30 – 23:30) (39 câu thoại · ~982 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại lạnh lùng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (39 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00) (39 câu thoại · ~1020 từ)
- **Nhạc nền mở hồi (BGM):** Piano ấm áp dần lên, không khí thanh lọc nhận thức.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (39 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

