# Kết quả xử lý mapping kịch bản ↔ prompt ảnh — Tập 25 → 68 (24/11/2026)

Tiếp theo `BaoCao_LechMapping_Prompt_Anh_Tap25-68_20261124.md`. Chưa sinh ảnh nào, chưa dựng video, chưa sửa kịch bản.

## 1. Cổng mới `.work/qc_bg_mapping.py`
`py -3 .work/qc_bg_mapping.py [XX ...]` — exit 1 nếu có tập TRƯỢT.
- **M1** mọi mã `sentences` phải tồn tại trong kịch bản VN hiện tại · **M2** không có hai tập trùng prompt · **M4** ≥ 90 % prompt khác nhau (bộ mẫu chung 17 prompt = TRƯỢT, H22/H25) · **M5** mọi câu kịch bản được ≥ 1 job phủ · M3 chỉ cảnh báo (tên Việt/Hoa không có trong prompt tiếng Anh).
- Script phụ: `apply_manual_map.py` (áp bảng xếp tay `manual_map_tapXX.json`), `remap_bg_codes.py` / `align_bg_codes.py` (tự động — **không dùng**: chia tỉ lệ / khớp từ khoá chỉ đúng ~60 %).

## 2. Trạng thái từng tập (đo ngày 24/11/2026)
Tổng 6.109 job cho tập 25–68. **38 tập ĐẠT** M1+M2+M4+M5.

| Nhóm | Tập | Việc đã làm |
|---|---|---|
| Viết prompt MỚI theo kịch bản hiện tại (đúng H25) | 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 67 | Bộ cũ sai vụ án / mẫu chung 17 prompt / bố cục kịch bản cũ ⇒ viết lại; mỗi job 1–3 câu liền kề, phủ 100 % câu |
| Xếp tay lại mã, **giữ prompt và ảnh đã sinh** | 25, 27, 28, 29, 40 | Mã câu khớp kịch bản; ~15–32 % job khớp lỏng (xem 4) |
| Giữ nguyên, nhưng TRƯỢT M5 mới | 26 (phủ 203/240), 30 (phủ 155/240) | Mã hợp lệ, prompt riêng; thiếu job cho 37 và 85 câu ⇒ parse_shots sẽ mượn nền. Cần quyết định bổ sung job |
| **Chưa làm** | 49, 64, 66, 68 | Kịch bản chỉ 61/52/61/49 câu (chưa xong) — chờ người dùng |

## 3. Ảnh đã dời vào `.work/_cu/bg_old_20261124/` (L5, có thể quay lại)
t31 (170), t32 (152), t34 (145), t35 (148), t37 (148), t38 (146), t39 (152), 3 ảnh ghế điện của t40 (`t40_a5_03/04/06`) — tổng ~1.063 ảnh. Cùng nơi: bản sao `bg_jobs` cũ của 32, 35, 37, 38, 39, 42, 45, 47, 48, 49, 31, 34. Bản trước-khi-xếp-tay của 28, 29 và các bản remap tạm ở `.work/_cu/bg_jobs_remap_20261124/`. `provenance.json` còn dòng của các ảnh đã dời (và 3 ảnh t40) — chưa dọn.
Hiện `assets/bg` chỉ còn ảnh t25–t30, t40 cho dải 25–68.

## 4. Cần người dùng quyết
1. **Tập 29 (Dahmer)** — ~25 job vẽ dao, xương, hoá chất, phân huỷ, tạ trong tù (V9/H4) đã có ảnh sinh sẵn; ~46 job khớp lỏng. Bỏ các job V9 / viết lại?
2. **Tập 28** — ~19 job hồi 3 vẽ cảnh gây án mà kịch bản mới không còn (phân tích tâm lý). **Tập 27** — 5 job bỏ trốn/phi tang hồi 3 khớp gượng; job bế em bé, em bé ngủ, nạn nhân trẻ mở cổng, di ảnh nạn nhân cần soi H1.
3. **Tập 25** — job búa tạ, giày dính dấu vết, vật lộn; ~20 job có thể bị AI vẽ chữ.
4. **Tập 26, 30** — bổ sung job cho câu chưa phủ?
5. **Tập 49, 64, 66, 68** — kịch bản có hoàn thiện chưa?
6. Số ảnh nhiều bất thường: tập 50 (190 job), 55 (193), 38 (188), 44 (167), 60 (169) — gộp bớt nếu muốn giảm thời gian sinh ảnh.
7. Sinh ảnh: chưa chạy. Hạn mức tài khoản Claude có lúc chạm 5 giờ; sinh ảnh Kaggle là việc riêng.

## 5. Nghi vấn kịch bản mà các lượt viết prompt phát hiện (CHƯA sửa — người dùng rà theo K1–K10)
Chỉ là ghi nhận; agent không tự tra nguồn. Mỗi mục cần đối chiếu nguồn công khai.
- **32** Trương Tử Cường: ngày thi hành án; số tiền chuộc ("gần hai tỷ" vs "bốn trăm triệu sau chia"); bồi thường 8 triệu; "sáu ngày" vs "bốn ngày" bị giam.
- **33, 67**: hai tập này bị ngắt trước khi báo cáo — chưa có danh sách nghi vấn; cần rà kịch bản riêng.
- **34** Kaczynski: chuyến bay 444 là American Airlines (kịch bản ghi United); ADX Florence vs FMC Butner (mất 2023); "mất trí nhớ phân liệt hoang tưởng" (lỗi dịch, K5); lời bà Mosser "đinh, lưỡi dao cạo" (V9); "trùng khớp 99 %"; lời Gary Wright.
- **35** Hello Kitty: tên thẩm phán, ngày tuyên án 6/12/2000, mức án; câu trích thẩm phán 4.07#4 (K2); lời nhân chứng 14 tuổi (K3); câu mô tả hiện trường cụ thể (K4).
- **36** Florence: "ba bài học" nhưng nêu bốn (5.03#1, K8); độc thoại Lotti 4.04#1–11 (K2/K3); chẩn đoán FBI 3.05#2 (K5); 4.06#9 "chấm dứt vĩnh viễn" vs tranh cãi.
- **37** Nguyễn Đức Anh: tên cô gái 17 tuổi; mốc 15 ngày kháng cáo; án 6 năm vũ khí quân dụng; giờ giấc lệch; 76 %, 31 nhát, 1,1 tỷ cần nguồn.
- **39** Lao Vinh Chi & Pháp Tử Anh: tuổi Lao Vinh Chi (19 → 46) không khớp; số nạn nhân "bảy"; mốc tử hình 12/1999 và 18/12/2023.
- **41** Shipman: "ít nhất 215" ngay sau "15 vụ"; lời thẩm phán nguyên văn 4.07#8; tên "Linh"/Linda Reynolds, Postles/Smith.
- **42** Miyazaki: mốc vụ Erika Namba (1988 hay 1989, 1.07#6); lời cha ở Hachioji gán người thật (K3); nhiều chi tiết hồi 3–5 chưa nguồn; "manga khiêu dâm" (K4).
- **43** Richthofen: "Sở Họng súng Homicide" (lỗi dịch); độc thoại 4.05; mức án 39 năm 6 tháng/38 năm; "hiện trường đẫm máu" 2.02#2 (V9).
- **44** Kinkel: "Jacob/Jake Ryker"; số súng; tuổi học sinh khống chế; phỏng vấn N2 2021 (K3).
- **45** Lâm Quá Vân: câu trích người cha 4.03#6; "ái tử thi" (K5); ngày tháng, chức danh luật sư/thẩm phán; mô tả thi thể (V9).
- **46** Dutroux: số người diễu hành; số nhà 128 Philippeville; án "chung thân" cho Martin 5.02#7 (nguồn: 30 năm); "hơn mười ba năm" vs "mười ba năm".
- **47** Thùng xi măng Tân Trang: mâu thuẫn ở chung/dọn ra; 2.03#1, 2.07#1 chẩn đoán (K5); 1.04#4 "Hắn" cho nhân vật nữ; câu trích 3.08#7.
- **48** David Bain: **hồi 3 gọi David là "hung thủ", hồi 4 nói trắng án 2009 — mâu thuẫn, vi phạm K5/K1**; 2.07#8, 3.06#8 lời gán người thật (K2/K3).
- **50** Dennehy: "điểm tuyệt đối thang Hare"; lời đồng phạm 4.05#1–8; mức án Stretch/Layton.
- **51** Ngô Tạ Vũ: số thẻ căn cước (10/30), số tiền (4 cách ghi), "200 ngày" vs "7 tháng"; "hiến tạng"; "98 %".
- **52** Setagaya: 280 vs 240 nghìn lượt cảnh sát; lời "điều tra viên" và bà Haruko (K3); từ "thi thể/chiến lợi phẩm/xác chết" (V9).
- **53** Ndlovu: số vụ/hợp đồng bảo hiểm/tiền; lời ngôi thứ nhất 1.07#2–5, 4.05; "sáu mẹ con" vs "năm đứa trẻ"; nhầm Mkhize/Kunene.
- **54** Điêu Ái Thanh: "hơn 28 năm" (1996→2026 ≈ 30); "vụ nữ sinh y Hàng Châu" không nguồn; câu 114–118, 183–184 mô tả xử lý thi thể (V9); N1/N2 (K3).
- **55** Kürten: "nghe tiếng máu chảy" (V9/K2); "hai trăm thư nhận tội", "chín bản án tử"; vợ "từng có tiền án".
- **56** Garanhuns: lời Isabel 4.06 (K2/K3); "hội chứng phụ nữ bị bạo hành" (K5); tuổi, mốc 5/2008, 71 năm.
- **57** Alègre: thứ tự thời gian hồi 4–5 (1997/2000/2002/2003); Anacrim/Homicide 31; lời Patricia 4.06; 2.06#1 chẩn đoán (K5).
- **58** Snowtown: nạn nhân đầu tiên (Lane/Trezise, K8); "tám hài cốt" vs 11/10 án; mức án; "giáo phái tử thần", chẩn đoán Bunting (K5).
- **59** Pedro López: lũ Ambato 1979 vs 1980; lời người mẹ (K3); câu thoại cha Córdoba (K2); nguồn Ron Laytner; 4.03#4–5 cơ chế thần kinh (K5).
- **60** Bạch Ngân: số vụ/tiền thưởng/"100 nghìn nam giới"; 1.04#7 nạn nhân 8 tuổi, 3.07#5 "mẫu tinh dịch" (K4); 4.04#4 lời bị can.
- **61** Heilbronn: 14/16 năm, 30/40 hiện trường (K8); độc thoại 1.07, 4.05; "71 tuổi gốc Ba Lan"; "triệu giờ công".
- **62** Adrian Lim: "Nữ tu Gerard Fernandez" (là linh mục); mốc ngày giữa các hồi; "Agnes Ng"/"Ng Siew Heok"; dấu máu tầng 7 lặp ở hồi 1 và 3.
- **63** Sithole: 4.02#5–6 "hạ gục" vs "bắt sống"; 38 tội/37 nạn nhân/2.410 năm; Mandela; "76 nạn nhân"; độc thoại Martha.
- **65** Barraza: "Hắn" vs "bà ta" (K6); lời trích Juana/José Joel (K2/K3); 16 vụ/759 năm; "Feggy Ostrosky".
- **38** Wuornos: bộ mới viết xong nhưng agent bị ngắt trước khi báo cáo — chưa có danh sách nghi vấn.
- **31** Chris Watts: tương tự.

## 6. Bẫy ghi nhận
- `bg_jobs` của 24 tập (33, 36, 39, 41–50, 53, 55–57, 59, 61, 63, 67) từng là **bộ mẫu chung 17 prompt** — các cổng cũ (H10, H22 chỉ đo lặp liền nhau) không bắt được. Đã thêm M4.
- Cổng chỉ ĐẠT khi `sentences` khớp mã thật; không đo được nghĩa ảnh ↔ lời. Vẫn phải soi mắt 100 % ảnh mới (H2/H19/H20).
- File `grp.py`/`d60.py` trong thư mục scratchpad che module chuẩn của Python làm `dump.py` lỗi; đã đổi tên `grp.py`.

## 7. Rà tuần tự bằng tay (không dùng agent) — cập nhật cuối ngày 24/11/2026
Công cụ: `.work/review_bg_ep.py XX [hồi]` (in từng job kèm câu được gán), `.work/fill_bg_gaps.py` (nhập câu lẻ vào job liền trước — CHỈ dùng khi câu thiếu lẻ; Tập 30 thử và hoàn tác vì có job gánh 343 từ).

| Tập | Kết quả rà | Thay đổi | Ảnh cần SINH LẠI/MỚI |
|---|---|---|---|
| 25 | ~90 % khớp | sửa 5 job cuối hồi 5 (thẻ kết nay ở câu cuối `5.05#20`) | 0 |
| 26 | thiếu job cho 37 câu | **+32 job mới** (`t26_a*_x*`), phủ 240/240 | 32 |
| 27 | hồi 3 lệch (cảnh gây án gán vào câu tâm lý) | **thay prompt 12 job**, ảnh cũ dời `.work/_cu/bg_old_20261124/t27_replaced/` | 12 |
| 28 | hồi 3 lệch | **thay prompt 11 job** (`t28_replaced/`); hồi 1 ổn (job 26 tiệm cầm đồ hơi lỏng); hồi 2, 4, 5 chưa rà tay | 11 |
| 29 | nhiều job V9 (dao, hoá chất, xương, thi thể, ảnh nạn nhân, tù) | **thay prompt 35 job** bằng cảnh gián tiếp (`t29_replaced/`) | 35 |
| 30 | thiếu job cho 85 câu (19 cụm) | **+49 job mới** (`t30_a*_x*`), phủ 240/240, không job nào > 90 từ | 49 |
| 40 | xếp tay lại mã từ đầu; chưa rà lần hai | — | 0 |

Chưa rà tay lần hai: 31–39, 41–48, 50–63, 65, 67 (bộ viết mới, agent viết thẳng từ câu kịch bản; mới qua cổng + quét từ cấm). Tập 63 có một số câu agent chỉ đọc 85 ký tự đầu — ưu tiên rà.
Việc còn lại: 49, 64, 66, 68; sinh ảnh; soi 100 % ảnh mới (H2/H19/H20); người dùng rà nghi vấn kịch bản (mục 5).

### 7b. Quét nội dung toàn bộ + sửa bổ sung (24/11/2026, chiều)
- Công cụ mới `.work/scan_bg_content.py [XX …] [--detail]`: đếm job > 75 từ lời, từ V9, từ gợi chữ (H26) trong prompt (bỏ qua cụm phủ định "no/blank/free of lettering").
- **Rà tay thật** (đọc từng job ↔ câu): Tập 25, 26 (chỗ thiếu), 27 hồi 3, 28 hồi 1 + hồi 3, 29 (job V9), 30 (cụm thiếu), **63 hồi 1–2 (66 job: gần như 100 % khớp)**. Các tập viết mới còn lại chỉ qua cổng + quét tự động — mẫu Tập 63 cho thấy agent viết trực tiếp từ câu kịch bản có chất lượng tốt.
- Sửa thêm: Tập 41 (3 job ống tiêm, trong đó 1 job có thiếu niên → túi bác sĩ đóng kín), 36 (bóng súng khổng lồ → bóng người), 30 (vệt máu cận cảnh → vệt nhạt dưới UV; tin nhắn/biển neon/biển cảnh báo → không chữ), 28 (con dao, nét mặt người thân → bóng), 40 (áp phích/biểu ngữ/biển motel → trơn), 29 (biển biểu tình, áp phích), 27 (tấm biển đồng). **Ảnh cũ của 14 job đã dời** `.work/_cu/bg_old_20261124/tXX_replaced/`.
- Cờ còn lại sau khi đọc prompt = vô hại ("gravel", "grave" = nghiêm trọng, "wounded ego", "bulletin", vật chứng nằm yên như vỏ đạn/súng trên khay ở Tập 36 và 61). Nên soi mắt khi có ảnh.
- Luật mới: AGENTS.md **H27** + bước 7 của quy trình; tiêu chuẩn A11 **#193**.
- Tổng ảnh phải sinh mới (ngoài bộ viết lại hoàn toàn): 139 (mục 7) + 14 = **153**.
- Trạng thái cổng: 40 tập ĐẠT; còn Tập 49 (kịch bản 61 câu, chưa xong); 64, 66, 68 chưa có `bg_jobs`.
