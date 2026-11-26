# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP 19 — BẮN PHÁ & THU HỒI TÌNH CẢM (LOVE BOMBING & DEVALUATION) (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — Nhóm 3: Các dạng Thao túng & Kiểm soát Đầu độc |
| Tên tập (VI) | **Tập 19: Bắn phá & Thu hồi tình cảm (Love Bombing & Devaluation)** |
| Tên tập (EN) | **Ep. 19: Love Bombing & Devaluation** |
| Tên tập (JA) | **第19話：ラブボミングと価値下げ** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap19_love_bombing_devaluation.md` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap19.json` |
| Chủ đề chuyên sâu | Nhóm 3: Các dạng Thao túng & Kiểm soát cưỡng chế — Phần 2: Bắn Phá Tình Cảm & Thu Hồi Tình Cảm (Love Bombing & Devaluation) & Cơn Nghiện Thao Túng. |
| Hồ sơ dẫn chứng | Vụ lừa đảo tình ái xuyên quốc gia Shimon Hayut (tự xưng Simon Leviev — *The Tinder Swindler*) & Chu kỳ bạo lực ái kỷ (Tâng bốc → Hạ bệ → Vứt bỏ). |
| Quy mô kịch bản (đo thật) | **240 câu thoại** · **4,373 từ** · **37 phần tử** (23 lượt nói) · 5 hồi · ước lượng ~**31.2 phút** |
| Cấu trúc phân vai | **Chuyên gia Tâm lý (Cáo)**: 89 câu · **Host (Cú)**: 88 câu · **Điều tra viên (Sói)**: 32 câu · **Người dân N1 (Cừu)**: 11 câu · **Người dân N2 (Mèo)**: 10 câu · **Người dân N3 (Khách mời đường phố)**: 10 câu |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **240 câu** |
| Tài nguyên hình ảnh nền | `02_SAN_XUAT/TamLyHocToiPham/Tap19/bg_jobs_tlhtp_tap19.json` — **41 job ảnh** (độc lập: **41** · trạng thái: **ĐÃ CHUYỂN JSON · CẦN MỞ RỘNG SHOT H25 (41 job)**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap19.json` (**240 câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap19/` (VI) · `Tap19_EN/` (EN) · `Tap19_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **240 câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap19[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap19.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

### HỒI 1: THE HOOK — CƠN MƯA HOA HỒNG TRƯỚC VỰC THẲM (40 câu) (40 câu thoại · ~630 từ)
- **Nhạc nền mở hồi (BGM):** Một đoạn vĩ cầm du dương ngọt ngào vang lên, nhưng ẩn phía dưới là tiếng Sub-bass rền nhẹ đe dọa.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (40 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 2: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ TỪNG YÊU MỘT NGƯỜI QUÁ HOÀN HẢO?" (48 câu) (48 câu thoại · ~955 từ)
- **Nhạc nền mở hồi (BGM):** Nhạc lofi ambient nhẹ nhàng mang tính tự sự đời thường.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (48 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 3: CƠ CHẾ GÂY NGHIỆN HÓA SINH & THỦ ĐOẠN CỦA KẺ LỪA ĐẢO TÌNH ÁI (58 câu) (58 câu thoại · ~1036 từ)
- **Nhạc nền mở hồi (BGM):** Dark Ambient sâu thẳm, tiếng bass dập dồn căng thẳng.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (58 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 4: VÌ SAO CON NGƯỜI DỄ SẬP BẪY? AI CŨNG CÓ NGUY CƠ? (50 câu) (50 câu thoại · ~812 từ)
- **Nhạc nền mở hồi (BGM):** Dark Drone u ám, tiếng tích tắc kim loại nặng nề.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (50 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

### HỒI 5: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (44 câu) (44 câu thoại · ~940 từ)
- **Nhạc nền mở hồi (BGM):** Piano ấm dần lên trên nền Ambient tĩnh lặng, mang màu sắc thanh lọc và tỉnh thức.
- **Trạng thái đồng bộ 3 ngôn ngữ:** VI (44 câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)

