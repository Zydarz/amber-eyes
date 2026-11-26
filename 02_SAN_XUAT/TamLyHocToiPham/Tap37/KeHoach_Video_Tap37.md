# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 37 — HIỆU ỨNG NGƯỜI NGOÀI CUỘC (BYSTANDER EFFECT) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 5: Tâm lý học Xã hội & Động lực Nhóm |
| Tên tập (VI) | **Tập 37: Hiệu ứng người ngoài cuộc (Bystander Effect)** |
| Tên tập (EN) | **Ep. 37: The Bystander Effect** |
| Tên tập (JA) | **第37話：傍観者効果（バイスタンダー効果）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap37_hieu_ung_nguoi_ngoai_cuoc_bystander.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap37.json` |
| Chủ đề chuyên sâu | Nhóm 5: Tâm lý học xã hội & Động lực nhóm — Phần 4: Hiệu Ứng Người Ngoài Cuộc (Bystander Effect) & Huyền Thoại Ba Mươi Tám Nhân Chứng. |
| Hồ sơ dẫn chứng | Vụ án Catherine "Kitty" Genovese (Kew Gardens, Queens, New York, ngày mười ba tháng ba năm một nghìn chín trăm sáu mươi tư), Hai thí nghiệm kinh điển của John Darley và Bibb Latané (năm một nghìn chín trăm sáu mươi tám) & Nghiên cứu camera CCTV đa quốc gia của Richard Philpot (tạp chí American Psychologist năm hai nghìn không trăm mười chín). |
| Quy mô kịch bản (đo thật) | **227 câu thoại** · **6,843 từ** · **40 phần tử** (23 lượt nói) · 5 hồi · ước lượng ~**48.9 phút** |
| Cấu trúc phân vai | **Chuyên gia Tâm lý (Cáo)**: 72 câu · **Host (Cú)**: 57 câu · **Điều tra viên (Sói)**: 50 câu · **Người dân N1 (Cừu)**: 19 câu · **Người dân N2 (Mèo)**: 15 câu · **Người dân N3 (Khách mời đường phố)**: 14 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **227 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap37/bg_jobs_tlhtp_tap37.json` — **140 job ảnh** (độc lập: **140** · trạng thái: **ĐẠT H25/H27 (sẵn sàng sinh ảnh)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap37.json` (**227 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap37/` (VI) · `Tap37_EN/` (EN) · `Tap37_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **227 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap37[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap37.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — TIẾNG KÊU CỨU TRONG ĐÊM ĐÔNG NEW YORK (00:00 – 04:45) (27 câu thoại · ~777 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng còi xe cảnh sát hú lên mờ ảo rồi chìm vào tiếng gió buốt giá.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (27 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ DÁM LÀ NGƯỜI ĐẦU TIÊN BƯỚC RA?" (04:45 – 10:15) (61 câu thoại · ~1491 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (61 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: KHOA HỌC THỰC NGHIỆM, NGHIÊN CỨU HIỆN ĐẠI & SỰ THẬT VỤ ÁN KITTY GENOVESE (10:15 – 19:30) (79 câu thoại · ~2755 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (79 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI DO DỰ TRƯỚC SỰ NGUY HIỂM? AI CŨNG CÓ NGUY CƠ? (19:30 – 23:30) (29 câu thoại · ~881 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (29 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 27:30) (31 câu thoại · ~939 từ)
- **Nhạc nền mở hồi (BGM):** Piano ấm dần lên trên nền Ambient tĩnh lặng, mang màu sắc thức tỉnh và hành động dũng cảm.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (31 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

