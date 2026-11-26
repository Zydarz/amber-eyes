# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 17 — BÓP MÉO HOẶC PHỚT LỜ HẬU QUẢ (DISTORTION OF CONSEQUENCES) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 2: Cơ chế Ngắt kết nối Đạo đức (Moral Disengagement) |
| Tên tập (VI) | **Tập 17: Bóp méo hoặc phớt lờ hậu quả (Distortion of Consequences)** |
| Tên tập (EN) | **Ep. 17: Distortion of Consequences** |
| Tên tập (JA) | **第17話：結果の歪曲・無視（ディストーション・オブ・コンシクエンシズ）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap17_phot_lo_hau_qua_distortion_of_consequences.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap17.json` |
| Chủ đề chuyên sâu | Nhóm 2: Cơ chế Ngắt kết nối đạo đức (Albert Bandura) — Phần 8: Bóp Méo Hoặc Phớt Lờ Hậu Quả (Disregard or Distortion of Consequences) & Khoảng Cách Vô Cảm. |
| Hồ sơ dẫn chứng | Tội phạm lừa đảo công nghệ cao xuyên quốc gia (*Cybercrime & Romance Scams*) & Hiện tượng game hóa tội ác (*Gamification of Crime*). |
| Quy mô kịch bản (đo thật) | **242 câu thoại** · **4,376 từ** · **37 phần tử** (23 lượt nói) · 5 hồi · ước lượng ~**31.3 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 91 câu · **Chuyên gia Tâm lý (Cáo)**: 89 câu · **Điều tra viên (Sói)**: 30 câu · **Người dân N1 (Cừu)**: 12 câu · **Người dân N2 (Mèo)**: 10 câu · **Người dân N3 (Khách mời đường phố)**: 10 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **242 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap17/bg_jobs_tlhtp_tap17.json` — **39 job ảnh** (độc lập: **39** · trạng thái: **ĐÃ CHUYỂN JSON · CẦN MỞ RỘNG SHOT H25 (39 job)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap17.json` (**242 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap17/` (VI) · `Tap17_EN/` (EN) · `Tap17_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **242 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap17[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap17.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — CÔNG TẮC GÂY HẠI TỪ KHOẢNG CÁCH NGÀN DẶM (40 câu) (40 câu thoại · ~687 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng nhấp chuột máy tính "Cạch" vang lên trong không gian tĩnh mịch.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (40 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "KHÔNG NHÌN THẤY THÌ KHÔNG THẤY CÓ TỘI?" (48 câu) (49 câu thoại · ~992 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (49 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: KHOA HỌC VỀ KHOẢNG CÁCH TÂM LÝ & ĐẠI BẢN DOANH LỪA ĐẢO TRỰC TUYẾN (58 câu) (59 câu thoại · ~968 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (59 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CÔNG NGHỆ LÀM CON NGƯỜI VÔ CẢM HƠN? AI CŨNG CÓ NGUY CƠ? (50 câu) (50 câu thoại · ~851 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (50 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (44 câu) (44 câu thoại · ~878 từ)
- **Nhạc nền mở hồi (BGM):** Piano ấm áp dần lên, hòa vào tiếng Cello sâu lắng, mang màu sắc đúc kết và thức tỉnh toàn bộ chặng đường của Nhóm 2.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (44 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

