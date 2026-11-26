# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 44 — SỰ BẤT LỰC TẬP NHIỄM (LEARNED HELPLESSNESS) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 7: Tâm lý học Nạn nhân & Sinh tồn (Victimology) |
| Tên tập (VI) | **Tập 44: Sự bất lực tập nhiễm (Learned Helplessness)** |
| Tên tập (EN) | **Ep. 44: Learned Helplessness** |
| Tên tập (JA) | **第44話：学習性無力感（ラーンド・ヘルプレスネス）** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap44_su_bat_luc_tap_nhiem.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap44.json` |
| Chủ đề chuyên sâu | Nhóm 7: Nạn Nhân Học & Cơ Chế Sinh Tồn — Sự Bất Lực Tập Nhiễm (Learned Helplessness) & Xiềng Xích Vô Hình. |
| Hồ sơ dẫn chứng | Thí nghiệm tâm lý của Martin Seligman & Steven Maier (năm một nghìn chín trăm sáu mươi bảy) & Ba nghìn không trăm chín mươi sáu ngày bị giam cầm trong hầm tối của Natascha Kampusch (Áo, giai đoạn một nghìn chín trăm chín mươi tám đến năm hai nghìn không trăm lẻ sáu). |
| Quy mô kịch bản (đo thật) | **215 câu thoại** · **4,974 từ** · **33 phần tử** (18 lượt nói) · 5 hồi · ước lượng ~**35.5 phút** |
| Cấu trúc phân vai | **Host (Cú)**: 94 câu · **Chuyên gia Tâm lý (Cáo)**: 47 câu · **Điều tra viên (Sói)**: 39 câu · **Người dân N1 (Cừu)**: 14 câu · **Người dân N2 (Mèo)**: 12 câu · **Người dân N3 (Khách mời đường phố)**: 9 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **215 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap44/bg_jobs_tlhtp_tap44.json` — **0 job ảnh** (độc lập: **0** · trạng thái: **CHỜ LẬP BẢNG SHOT & PROMPT (H25/H27)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap44.json` (**215 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap44/` (VI) · `Tap44_EN/` (EN) · `Tap44_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **215 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap44[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap44.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 05:00) (46 câu thoại · ~1007 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng Sub-bass rền nhẹ phía dưới. Một tiếng tích tắc kim đồng hồ kim loại gõ chậm, tạo cảm giác bức bách nghẹt thở.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (46 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN ĐÃ TỪNG TỪ BỎ VÌ TIN RẰNG MÌNH KHÔNG THỂ?" (05:00 – 10:30) (42 câu thoại · ~927 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (42 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: THÍ NGHIỆM SELIGMAN & 3.096 NGÀY ĐỊA NGỤC CỦA NATASCHA KAMPUSCH (10:30 – 16:30) (58 câu thoại · ~1416 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (58 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (16:30 – 21:30) (33 câu thoại · ~842 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (33 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (21:30 – 27:00) (36 câu thoại · ~782 từ)
- **Nhạc nền mở hồi (BGM):** Tiếng Cello ấm dần nhưng vẫn u buồn, tiếng mưa rơi tí tách ngoài cửa sổ.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (36 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

