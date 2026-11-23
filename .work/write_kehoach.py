import os

kehoach_vn = """# HỒ SƠ SẢN XUẤT TẬP 26 · "NỮ HỘ SINH KOTOBUKI & TỘI ÁC DƯỚI LỚP VỎ BỌC TỪ THIỆN" — VI EDITION

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 26: Nữ Hộ Sinh Kotobuki & Tội Ác Dưới Lớp Vỏ Bọc Từ Thiện — Sự Suy Đồi Đạo Đức & Kỹ Thuật Tự Biện Minh Hậu Chiến (Hồ Sơ Miyuki Ishikawa)** |
| Vụ án | Vụ bê bối Nhà hộ sinh Kotobuki chấn động thủ đô Tokyo (Nhật Bản, 1944 – 1948) |
| Chủ đề tâm lý | Sự suy đồi đạo đức trong khủng hoảng (*Moral Decay in Post-War Crisis*) · Trục lợi từ sự cùng quẫn (*Exploitation of Desperation*) · Vỏ bọc từ thiện nhân ái (*Benevolent Façade*) · Kỹ thuật trung hòa đạo đức & tự biện minh (*Moral Neutralization & Rationalization*) · Phi nhân tính hóa thủ tục hành chính (*Administrative Dehumanization*) · Khuếch tán trách nhiệm đồng phạm (*Diffusion of Responsibility*) · Giải mã cơ chế Ăn năn chân thực (*Affective Remorse*) vs Tự thương hại bản ngã bệnh lý (*Pathological Self-Pity / Narcissistic Collapse*) · Chấn thương tâm lý đạo đức thứ cấp của người mẹ (*Survivor's Guilt & Complicity Self-Blame*) |
| Định dạng | Podcast Tài liệu Phân tích Tâm lý Tội phạm (Host-Driven Documentary) — 5 Hồi chuẩn A2c/K10 |
| Cấu trúc phân vai | 4 Giọng đọc: **Host** (Cú vọ - 133 câu) · **Điều tra viên** (Chó săn - 43 câu) · **Chuyên gia Tâm lý** (Cáo bạc - 47 câu) · **Người bình thường** (N1 Cảnh sát tuần tra Waseda 1948: 8 câu & N2 Người mẹ mất con: 9 câu) |
| Quy mô kịch bản sản xuất | **240 câu thoại** (Chuẩn hóa toàn diện 100% khớp Golden Benchmark A2c/K10) · 51 phần tử (Elements) · 32 lượt thoại |
| Tình trạng đồng bộ đa ngôn ngữ | Đồng bộ cấu trúc **Parity 1:1 tuyệt đối** cho 4 ngôn ngữ: **Tiếng Việt (VN - 240 câu)**, **Tiếng Anh (EN - 240 câu)**, **Tiếng Nhật (JA - 240 câu)**, **Tiếng Hàn (KO - 240 câu)** |
| Tiêu chuẩn an toàn | **Tuân thủ tuyệt đối Quy tắc V9 (100% YouTube Safe)**: 0% mô tả bạo lực gore, máu me hay chi tiết cơ học đau đớn; 100% tập trung phân tích khoa học hành vi, lịch sử pháp y, trách nhiệm quản lý nhà nước và 4 cảnh báo đỏ bảo vệ trẻ em trước các cơ sở chăm sóc trục lợi |
| Tài nguyên hình ảnh | **135 ảnh nền chuẩn 2112×1188 (16:9 2K)** tiền tố `t26_` tại `assets/bg/` · Phong cách Dark Graphic Novel Noir |
| Bộ nhạc nền (BGM) | Cello u uất chiến tranh → Deep Ambient lạnh lẽo → Minimalist Piano học thuật lâm sàng → Violin trầm hùng tòa án → Warm Piano đúc kết nhân văn sâu sắc |

---

## B2. Kế hoạch Triển khai & Đồng bộ Đa ngôn ngữ (Pipeline Roadmap)

### 1. Đồng bộ Hồ sơ & Kịch bản (Đã hoàn tất)
- [x] Thẩm tra dữ kiện lịch sử & pháp lý đạt độ chính xác 100% qua hồ sơ Sở Cảnh sát Tokyo (MPD), Bác sĩ pháp y Yurie Taniguchi (Đại học Tokyo) và các bản án tòa án Tokyo 1948/1952 (`01_KICH_BAN/Ho_So_Toi_Pham/Tap26/REVIEW_kichban_tap26.md`).
- [x] Hoàn thiện bản nghiên cứu chuyên sâu 5 chủ thể và cơ chế hối hận đa chiều (`01_KICH_BAN/Ho_So_Toi_Pham/Tap26/NghienCuu_TamLy_BoSung_KichBan_Tap26.md`).
- [x] Đồng bộ hóa toàn bộ 4 ngôn ngữ (VN, EN, JA, KO) đạt chuẩn **chính xác 240 câu thoại** khớp 1:1 từng mã câu thoại (`1.02#1` đến `5.05#18`).
- [x] Biên dịch và xác thực kịch bản sản xuất sang `.work/script_tap26.json`, `.work/script_tap26_EN.json`, `.work/script_tap26_JA.json`, `.work/script_tap26_KO.json`.

### 2. Các bước Sản xuất Tiếp theo (Cổng kiểm theo `AGENTS.md`)
1. **Bước 1 (Duyệt kịch bản):** Kịch bản gốc 240 câu chuẩn hóa đã sẵn sàng cho cả 4 ngôn ngữ.
2. **Bước 2 (Tách kịch bản):** Đã phân tách chuẩn xác 51 phần tử (32 lượt thoại) vào hệ thống `.work/script_tap26*.json`.
3. **Bước 3 (Diễn xuất & Nhịp nghỉ):** Chuẩn bị file diễn xuất `acting_tap26.json` (kiểm soát ngắt nhịp và khoảng câm theo `qc_pause_gate.py`).
4. **Bước 4 (Đọc giọng TTS):** Tổng hợp âm thanh giọng đọc theo cấu hình `CAST` của `edition.py` (MiniMax / Higgs Audio v3).
5. **Bước 5 (Kiểm định giọng theo vai):** Chạy `voice_role_check.py` đảm bảo mỗi vai thể hiện 1 nhân vật nhất quán xuyên suốt 5 hồi.
6. **Bước 6 (Master Audio):** Trộn 3 lớp âm thanh (Voice + SFX + BGM) đạt chuẩn EBUR128 (-16 LUFS, TP ≤ -1.5 dBFS).
7. **Bước 7 (Bảng shot):** Khớp 100% câu thoại với 135 ảnh nền dùng chung `t26_*` qua `parse_shots.py`.
8. **Bước 8 (Dựng hình & Đóng gói):** Render video bằng `build_video3.py` và đóng gói phụ đề srt qua `package.py --mux`.

---

## B3. Cấu trúc 5 Hồi Chi tiết & Danh mục Ảnh Nền Liên kết

Toàn bộ 135 ảnh nền (`assets/bg/t26_*.png`) được phân bổ chặt chẽ theo nhịp kịch bản 5 hồi:

### HỒI 1: ĐÊM ĐÔNG TOKYO 1948 & CHIẾC XE KÉO BÍ ẨN TRÊN PHỐ VẮNG (54 câu thoại · 31 ảnh)
- Cảnh tượng hoang tàn sau chiến tranh, người dân đói rét và đợt bùng nổ dân số hậu chiến.
- Hai cảnh sát tuần tra đồn Waseda phát hiện chiếc xe kéo chở 5 thi thể trẻ sơ sinh rạng sáng 12/1/1948.
- Cuộc đột kích khẩn cấp Nhà hộ sinh Kotobuki ngày 15/1/1948 và phát hiện pháp y chấn động của Bác sĩ Yurie Taniguchi.
- Phân tích tâm lý học hành vi: Trực giác lương tri của hai cảnh sát trẻ đối đầu với sự bàng quan tập thể của xã hội.

### HỒI 2: ĐẾ CHẾ KOTOBUKI & ĐƯỜNG DÂY TRỤC LỢI TỪ NỖI TUYỆT VỌNG (46 câu thoại · 24 ảnh)
- Quy trình trục lợi khép kín từ luật cấm phá thai và sự cùng quẫn của các bậc cha mẹ nghèo.
- Vỏ bọc từ thiện và bản hợp đồng nhận con nuôi với mức phí 4.000 – 5.000 yên.
- Cơ chế tâm lý đồng phạm: Khuếch tán trách nhiệm của người chồng Takeshi Ishikawa và Phi nhân tính hóa thủ tục hành chính của bác sĩ Shiro Nakayama.
- Thái độ ngạo mạn, chối bỏ tội lỗi và đổ lỗi ngược cho các bậc cha mẹ của Miyuki Ishikawa.

### HỒI 3: GIẢI MÃ TÂM LÝ: SỰ SUY ĐỒI ĐẠO ĐỨC & CƠ CHẾ TỰ BIỆN MINH HẬU CHIẾN (52 câu thoại · 28 ảnh)
- Sự trượt dốc đạo đức và kỹ thuật trung hòa đạo đức (*Moral Neutralization*).
- Hiện tượng Khử nhạy cảm cảm xúc (*Emotional Desensitization*) và lòng tham triệt tiêu lương tâm y đức.
- Câu hỏi cốt lõi: Tại sao Miyuki Ishikawa không hề hối hận chân thực?
- Phân biệt bản chất: Ăn năn chân thực (*Affective Remorse*) vs Tự thương hại bản ngã bệnh lý (*Pathological Self-Pity / Narcissistic Collapse*).
- Cơ chế nhận tội của đồng phạm: Nỗi sợ trừng phạt và bản năng tự bảo toàn sinh tồn.

### HỒI 4: BẢN ÁN TRƯỚC VÀNH MÓNG NGỰA & BƯỚC NGOẶT THỂ CHẾ HẬU CHIẾN (52 câu thoại · 28 ảnh)
- Diễn biến phiên tòa Tokyo tháng 10/1948 và sức ép từ chứng cứ pháp y Đại học Tokyo.
- Nỗi đau đớn tột cùng và "Mặc cảm tội lỗi của người trao con" (*Survivor's Guilt & Complicity Self-Blame*) của những người mẹ nghèo.
- Phán quyết sơ thẩm 8 năm tù và phúc thẩm giảm xuống 4 năm tù gây chấn động dư luận.
- Bước ngoặt thể chế: Sự thức tỉnh của xã hội Nhật Bản, dẫn đến việc ban hành Luật Bảo vệ Thể chất Ưu sinh 1948 và thành lập hệ thống phúc lợi trẻ em hiện đại.

### HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ BẢO VỆ TRẺ EM TRƯỚC CÁC CƠ SỞ TRỤC LỢI (36 câu thoại · 24 ảnh)
- Lời cảnh tỉnh nhân văn về trách nhiệm cộng đồng trong việc bảo bọc những mầm sống yếu thế.
- 4 Cảnh báo đỏ nhận diện cơ sở chăm sóc trẻ em trục lợi:
  1. Hoạt động mập mờ, thiếu cấp phép và giám sát độc lập.
  2. Bắt buộc thanh toán trọn gói, thương mại hóa hợp đồng nhận nuôi.
  3. Cắt đứt liên lạc, cấm đoán thăm nom và cách ly trẻ với gia đình.
  4. Sử dụng uy tín cá nhân để né tránh quy trình kiểm tra minh bạch.
- Đúc kết triết lý nhân văn: Công lý của lương tri nhân loại và sự bảo vệ sự sống.

---

## B4. Danh mục Tệp Thành phẩm & Tài liệu Sản xuất

| Tệp | Vị trí | Trạng thái |
|---|---|:---:|
| Kịch bản tiếng Việt (240 câu) | `01_KICH_BAN/Ho_So_Toi_Pham/Tap26/kichban_tap26_23102026.md` | **Đã hoàn tất** |
| Kịch bản tiếng Anh (240 câu) | `01_KICH_BAN/Ho_So_Toi_Pham/Tap26_EN/kichban_tap26_EN.md` | **Đã hoàn tất** |
| Kịch bản tiếng Nhật (240 câu) | `01_KICH_BAN/Ho_So_Toi_Pham/Tap26_JA/kichban_tap26_JA.md` | **Đã hoàn tất** |
| Kịch bản tiếng Hàn (240 câu) | `01_KICH_BAN/Ho_So_Toi_Pham/Tap26_KO/kichban_tap26_KO.md` | **Đã hoàn tất** |
| JSON kịch bản biên dịch | `.work/script_tap26*.json` (đủ 4 ngôn ngữ) | **Đã hoàn tất** |
| Thẩm định dữ kiện & lịch sử | `01_KICH_BAN/Ho_So_Toi_Pham/Tap26/REVIEW_kichban_tap26.md` | **Đã hoàn tất** |
| Bản nghiên cứu chuyên sâu 5 chủ thể | `01_KICH_BAN/Ho_So_Toi_Pham/Tap26/NghienCuu_TamLy_BoSung_KichBan_Tap26.md` | **Đã hoàn tất** |
| Danh sách 135 ảnh nền 2K | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap26/Danh_Sach_Anh_Tap26.md` | **Đã hoàn tất** |
| Kế hoạch sản xuất tiếng Việt | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap26/KeHoach_Video_Tap26.md` | **Đã hoàn tất** |
| Kế hoạch sản xuất tiếng Anh | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap26_EN/KeHoach_Video_Tap26_EN.md` | **Đã hoàn tất** |
| Kế hoạch sản xuất tiếng Nhật | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap26_JA/KeHoach_Video_Tap26_JA.md` | **Đã hoàn tất** |
| Kế hoạch sản xuất tiếng Hàn | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap26_KO/KeHoach_Video_Tap26_KO.md` | **Đã hoàn tất** |
"""

os.makedirs('02_SAN_XUAT/Ho_So_Toi_Pham/Tap26', exist_ok=True)
with open('02_SAN_XUAT/Ho_So_Toi_Pham/Tap26/KeHoach_Video_Tap26.md', 'w', encoding='utf-8') as f:
    f.write(kehoach_vn)

print('Wrote 02_SAN_XUAT/Ho_So_Toi_Pham/Tap26/KeHoach_Video_Tap26.md')
