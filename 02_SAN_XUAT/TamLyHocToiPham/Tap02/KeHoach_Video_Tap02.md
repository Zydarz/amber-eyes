# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 02 — HỢP LÝ HÓA (RATIONALIZATION) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 1: Cơ chế Phòng vệ Vô thức |
| Tên tập (VI) | **Tập 02: Hợp lý hóa (Rationalization)** |
| Tên tập (EN) | **Ep. 02: Rationalization** |
| Tên tập (JA) | **第02話：合理化（ラショナライゼーション）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap02_hop_ly_hoa_rationalization.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap02.json` |
| Chủ đề chuyên sâu | Nhóm 1: Cơ chế Phòng vệ Vô thức — Phần 2: Hợp Lý Hóa (Rationalization) & Chiếc Áo Khoác Đạo Đức. |
| Hồ sơ dẫn chứng | Đại án lừa đảo Bernard Madoff (64,8 tỷ đô la tại Phố Wall, bị bắt ngày 11/12/2008, án 150 năm tù) & Tâm lý tội phạm cổ cồn trắng. |
| Quy mô kịch bản (đo thật) | **223 câu thoại** · **6,045 từ** · **47 phần tử** (26 lượt nói) · 5 hồi · ước lượng ~**43.2 phút** |
| Cấu trúc phân vai | **Điều tra viên (Sói)**: 67 câu · **Chuyên gia Tâm lý (Cáo)**: 64 câu · **Host (Cú)**: 57 câu · **Người dân N1 (Cừu)**: 14 câu · **Người dân N2 (Mèo)**: 11 câu · **Người dân N3 (Khách mời đường phố)**: 10 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **223 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap02/bg_jobs_tlhtp_tap02.json` — **171 job ảnh** (độc lập: **171** · trạng thái: **ĐẠT H25/H27 (sẵn sàng sinh ảnh)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap02.json` (**223 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap02/` (VI) · `Tap02_EN/` (EN) · `Tap02_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **223 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap02[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap02.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — KHI TỘI ÁC MẶC LỄ PHỤC (00:00 – 05:00) (27 câu thoại · ~713 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ. Một tiếng lách cách đều đặn như bàn phím máy tính làm việc trong đêm khuya.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (27 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "LÝ DO BẠN ĐƯA RA CÓ THẬT KHÔNG?" (05:00 – 10:30) (47 câu thoại · ~1144 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng, mang màu sắc phóng sự đời sống.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (47 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: BẤT HÒA NHẬN THỨC, TAM GIÁC GIAN LẬN & ĐẠI ÁN BERNARD MADOFF (10:30 – 18:30) (73 câu thoại · ~2089 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc Synth lạnh lẽo, nhịp điệu chậm rãi mang tính mổ xẻ bản chất tâm lý.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (73 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: SỰ THÍCH NGHI CỦA NÃO BỘ — VÌ SAO DỐI TRÁ CÓ TÍNH GÂY NGHIỆN? (18:30 – 23:30) (38 câu thoại · ~1053 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc đồng hồ cơ học gõ nặng trĩu.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (38 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00) (38 câu thoại · ~1046 từ)
- **Nhạc nền mở hồi (BGM):** Piano ấm dần lên trên nền Ambient tĩnh lặng, mang màu sắc thanh lọc nhận thức.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (38 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

