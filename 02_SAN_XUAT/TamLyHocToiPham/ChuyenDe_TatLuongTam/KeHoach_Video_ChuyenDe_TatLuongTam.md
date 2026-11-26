# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM — TẬP CHUYÊN ĐỀ: CÔNG TẮC TẮT LƯƠNG TÂM (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (Tập Chuyên Đề Đặc Biệt)** — Bản đồ Vùng Tối & Cơ chế Ngắt Kết Nối Đạo Đức |
| Tên tập (VI) | **Tập Chuyên Đề: Công Tắc Tắt Lương Tâm — Có Phải Ai Cũng Có Thể Trở Thành Ác Quỷ?** |
| Tên tập (EN) | **Special Ep.: The Conscience Switch — Moral Disengagement & The Fragile Border of the Self** |
| Tên tập (JA) | **特別編：良心のスイッチ — 道徳的不活性化（モラル・ディスエンゲージメント）と自我の境界** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_chuyende_tat_luong_tam.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_chuyende_tat_luong_tam.json` |
| Hồ sơ dẫn chứng & Thực nghiệm | Thuyết Albert Bandura (1999, 2016) · Osofsky – Bandura – Zimbardo (2005) · Vụ Bernard Madoff (2008–2009) · Bản ghi nhớ Ford Pinto (1970s) · Thí nghiệm Nhà tù Stanford (Zimbardo, 1971) · Thí nghiệm Tuân phục (Milgram, 1961–1963) · Hiệu ứng Người ngoài cuộc (Darley & Latané, 1968). |
| Quy mô kịch bản (đo thật) | **240 câu thoại** · **7,274 từ** · **41 phần tử** (27 lượt nói) · 5 hồi · ước lượng ~**36.0 phút** |
| Cấu trúc phân vai | **Chuyên gia Tâm lý (Cáo)**: 95 câu · **Host (Cú)**: 68 câu · **Điều tra viên (Sói)**: 67 câu · **Người bình thường (N1/N2)**: 10 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **240 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/ChuyenDe_TatLuongTam/bg_jobs_chuyende_tat_luong_tam.json` — **176 job ảnh** (độc lập: **176** · 0 lỗi QC · **ĐẠT H25/H27/H28 — sẵn sàng sinh ảnh**) |
| Bảng mapping shot ↔ ảnh | `02_SAN_XUAT/TamLyHocToiPham/ChuyenDe_TatLuongTam/Bang_Shot_Anh_ChuyenDe_TatLuongTam.md` (phủ 240/240 câu = 100%) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (0 lỗi bạo lực/gore), **H1/V5** (chỉ bóng người vô diện), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Mở rộng kịch bản VN lên **240 câu** (bản gốc 104 câu sao lưu tại `.work/_cu/kichban_chuyende_tat_luong_tam_104cau_backup.md`).
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_chuyende_tat_luong_tam.json` (**240 câu**, 0 lỗi cấu trúc).
- [x] Đối chiếu 8/8 nguồn công khai (K1/L2) trong `nguon_tham_khao.md` và lập `REVIEW_kichban_chuyende_tat_luong_tam.md` (đạt 10/10 chỉ dấu K10).
- [x] Lập bảng mapping **176 shot / 176 ảnh nền** (`Bang_Shot_Anh_ChuyenDe_TatLuongTam.md` + `bg_jobs_chuyende_tat_luong_tam.json`), QC 0 lỗi.
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `ChuyenDe_TatLuongTam/` (VI) · `ChuyenDe_TatLuongTam_EN/` (EN) · `ChuyenDe_TatLuongTam_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **240 câu** với bản VI.

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ 10 chỉ dấu K10.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_chuyende_tat_luong_tam[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3, kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H21/H22/H25/H27/H28):** Sinh **176 ảnh nền** trên Kaggle FLUX (2 kernel song song theo `QUY_TAC_TAO_ANH_KAGGLE_FLUX.md`), soi mắt 100% nền mới (H2/H19/H20).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: LỜI CẢNH TỈNH TỪ ĐỜI THƯỜNG — KHI LƯƠNG TÂM CÓ CÔNG TẮC (40 câu thoại · ~1,100 từ · ước từ 00:23)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới, tích tắc đồng hồ cơ học.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (40 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: BẢN ĐỒ NGẮT ĐẠO ĐỨC — BỐN CHIẾC MẶT NẠ ĐẦU TIÊN & HỒ SƠ BERNARD MADOFF (58 câu thoại · ~1,769 từ · ước từ 05:49)
- **Nhạc nền mở hồi (BGM):** Nhạc Minimalist với tiếng đàn Synth lạnh lẽo, nhịp điệu chậm rãi mang tính phân tích học thuật.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (58 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: BỐN CƠ CHẾ TÀN KHỐC NHẤT — PHI NHÂN HÓA & BỨC TƯỜNG CHIA NGĂN (50 câu thoại · ~1,460 từ · ước từ 14:28)
- **Nhạc nền mở hồi (BGM):** Dark Bass dồn dập hơn, tiếng rít kim loại nhẹ tạo cảm giác căng thẳng trong phòng hỏi cung.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (50 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: HAI THÍ NGHIỆM ĐỊA NGỤC — STANFORD, MILGRAM & CÂU HỎI HIỆN SINH (51 câu thoại · ~1,656 từ · ước từ 21:38)
- **Nhạc nền mở hồi (BGM):** Drone kỳ ảo, tiếng thì thầm mờ ảo và nhịp bass chậm tạo không khí ngột ngạt, nghi vấn hiện sinh.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (51 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & HỆ THỐNG CẢNH BÁO ĐỎ SINH TỒN (41 câu thoại · ~1,289 từ · ước từ 29:43)
- **Nhạc nền mở hồi (BGM):** Tiếng Piano rải chậm, ấm dần lên, mang màu sắc thanh lọc nhận thức và thức tỉnh.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (41 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)
