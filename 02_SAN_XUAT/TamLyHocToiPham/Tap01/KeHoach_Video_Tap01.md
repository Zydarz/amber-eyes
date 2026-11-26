# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 01 — PHÓNG CHIẾU (PROJECTION) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 1: Cơ chế Phòng vệ Vô thức |
| Tên tập (VI) | **Tập 01: Phóng chiếu (Projection)** |
| Tên tập (EN) | **Ep. 01: Projection** |
| Tên tập (JA) | **第01話：投影（プロジェクション）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap01_phong_chieu_projection.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap01.json` |
| Chủ đề chuyên sâu | Nhóm 1: Cơ chế Phòng vệ Vô thức — Phần 1: Phóng Chiếu (Projection) & Chiếc Gương Vỡ Của Bản Ngã. |
| Hồ sơ dẫn chứng | Vụ án Richard Farley (Bốn năm đeo bám và phóng chiếu tội lỗi lên Laura Black tại ESL Incorporated — Sunnyvale, California, 1984–1988). |
| Quy mô kịch bản (đo thật) | **230 câu thoại** · **5,995 từ** · **47 phần tử** (26 lượt nói) · 5 hồi · ước lượng ~**42.8 phút** |
| Cấu trúc phân vai | **Điều tra viên (Sói)**: 70 câu · **Chuyên gia Tâm lý (Cáo)**: 68 câu · **Host (Cú)**: 55 câu · **Người dân N1 (Cừu)**: 14 câu · **Người dân N2 (Mèo)**: 13 câu · **Người dân N3 (Khách mời đường phố)**: 10 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **230 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap01/bg_jobs_tlhtp_tap01.json` — **177 job ảnh** (độc lập: **177** · trạng thái: **ĐẠT H25/H27 (sẵn sàng sinh ảnh)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap01.json` (**230 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap01/` (VI) · `Tap01_EN/` (EN) · `Tap01_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **230 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap01[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap01.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — KHI BẢN NGÃ TỰ ĐÓNG VAI NẠN NHÂN (00:00 – 05:00) (22 câu thoại · ~572 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng tích tắc đồng hồ kim loại gõ chậm, tạo cảm giác bức bách.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (22 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ BIẾT PHÓNG CHIẾU LÀ GÌ KHÔNG?" (05:00 – 10:30) (49 câu thoại · ~1047 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng, mang màu sắc phóng sự điều tra xã hội.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (49 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: TỪ CHIẾC GƯƠNG CỦA FREUD ĐẾN HỒ SƠ ÁN ĐẪM MÁU (10:30 – 18:30) (74 câu thoại · ~2127 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc Minimalist với tiếng đàn Synth lạnh lẽo, nhịp điệu chậm rãi mang tính mổ xẻ khoa học.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (74 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? QUỸ ĐẠO LEO THANG VÀ ĐIỂM MÙ XÃ HỘI (18:30 – 23:30) (44 câu thoại · ~1114 từ)
- **Nhạc nền mở hồi (BGM):** Drone kỳ ảo u tối xen kẽ tiếng gõ kim loại nhịp đều đặn, không khí mang tính chất vấn hiện sinh.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (44 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00) (41 câu thoại · ~1135 từ)
- **Nhạc nền mở hồi (BGM):** Tiếng Piano ấm dần lên trên nền Ambient tĩnh lặng, mang màu sắc thanh lọc và thức tỉnh nội tâm.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (41 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

