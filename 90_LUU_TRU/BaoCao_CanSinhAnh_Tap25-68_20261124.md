# Báo cáo: các tập cần sinh ảnh nền — Tập 25 → 68 (24/11/2026)

> **Cập nhật 22:45 ngày 24/11/2026:** Đã hoàn thành sinh và đồng bộ 100% ảnh cho **Tập 26, 27, 28, 29, 30** (+149 ảnh mới) trên Kaggle GPU bằng mô hình `FLUX.2-klein-4B`.

Cách đếm: mỗi job trong `.work/bg_jobs_tapXX.json` = 1 ảnh `assets/bg/<tên job>.png`. **Cần sinh = job chưa có file ảnh.** Không có ảnh thừa (ảnh không còn job nào dùng) ở bất kỳ tập nào. Ảnh bị loại đã dời vào `.work/_cu/bg_old_20261124/`.

**Tổng: 6.044 job · 1.112 đã có ảnh · 4.932 cần sinh** (đã loại Tập 49, xem mục 3).

## 1. Trạng thái nhóm bổ sung (Tập 25 → 30 và Tập 40)

Toàn bộ 6 tập (25 → 30) đã hoàn tất 100% ảnh nền đạt chuẩn Graphic Novel Noir 2K:

| Tập | Vụ án | Job | Đã có | **Cần sinh** | Tình trạng & Ghi chú |
|:---:|---|---:|---:|---:|---|
| **25** | Yoo Young-chul | 140 | 140 | **0** | Đủ 100% ảnh |
| **26** | Miyuki Ishikawa | 167 | 167 | **0** | **ĐÃ XONG** (+32 ảnh mới các job `_x` trên Kaggle) |
| **27** | Nguyễn Hải Dương | 152 | 152 | **0** | **ĐÃ XONG** (+13 ảnh thay thế/sửa prompt khớp lời) |
| **28** | Lê Văn Luyện | 152 | 152 | **0** | **ĐÃ XONG** (+13 ảnh thay thế hồi 3 & chi tiết) |
| **29** | Jeffrey Dahmer | 152 | 152 | **0** | **ĐÃ XONG** (+37 ảnh thay thế V9 & biển trơn) |
| **30** | Nguyễn Đức Nghĩa | 204 | 204 | **0** | **ĐÃ XONG** (+54 ảnh job `_x` và sửa cảnh nhạy cảm) |
| **40** | Ted Bundy | 149 | 145 | **4** | Cần sinh 4 ảnh (áp phích/biểu ngữ/biển motel → trơn) |

*Ghi chú:* Toàn bộ 149 ảnh mới sinh của Tập 26–30 đã được cập nhật xuất xứ vào `provenance.json` theo đúng luật L7.

---

## 2. Sinh toàn bộ — viết lại bộ prompt (34 tập, 4.928 ảnh)

| Tập | Vụ án | Ảnh | | Tập | Vụ án | Ảnh |
|---|---|---:|---|---|---|---:|
| 31 | Chris Watts | 163 | | 52 | Gia đình Setagaya | 153 |
| 32 | Trương Tử Cường | 143 | | 53 | Rosemary Ndlovu | 145 |
| 33 | Natascha Kampusch | 136 | | 54 | Điêu Ái Thanh | 158 |
| 34 | Ted Kaczynski | 148 | | 55 | Peter Kürten | 193 |
| 35 | Hello Kitty (HK) | 150 | | 56 | Bộ ba Garanhuns | 116 |
| 36 | Quái vật Florence | 157 | | 57 | Patrice Alègre | 150 |
| 37 | Nguyễn Đức Anh | 122 | | 58 | Snowtown | 150 |
| 38 | Aileen Wuornos | 188 | | 59 | Pedro López | 138 |
| 39 | Lao Vinh Chi & Pháp Tử Anh | 135 | | 60 | Sát nhân Bạch Ngân | 169 |
| 41 | Harold Shipman | 157 | | 61 | Bóng ma Heilbronn | 149 |
| 42 | Tsutomu Miyazaki | 143 | | 62 | Adrian Lim | 130 |
| 43 | Suzane von Richthofen | 159 | | 63 | Moses Sithole | 144 |
| 44 | Kip Kinkel | 167 | | 65 | Juana Barraza | 134 |
| 45 | Lâm Quá Vân | 143 | | 67 | Cedric Maake | 127 |
| 46 | Marc Dutroux | 151 | | | | |
| 47 | Thùng xi măng Tân Trang | 152 | | | | |
| 48 | David Bain | 135 | | | | |
| 50 | Joanna Dennehy | 190 | | | | |
| 51 | Ngô Tạ Vũ | 133 | | | | |

Tập nhiều ảnh nhất: 55 (193), 50 (190), 38 (188), 60 (169), 44 (167).

---

## 3. KHÔNG sinh
- **Tập 49 (Charles Sobhraj): 146 job là bộ "mẫu chung" cũ (17 prompt lặp), mã câu sai 98/146, kịch bản mới 61 câu.** Chờ kịch bản hoàn thiện rồi viết job mới.
- **Tập 64, 66, 68:** chưa có `bg_jobs` (kịch bản 52/61/49 câu, chưa xong).

---

## 4. Điều kiện trước khi sinh (H23, L4)
1. **Kịch bản phải được người dùng duyệt bản chốt** trước khi sinh (H23) — nhiều tập có nghi vấn chưa xử lý (xem `BaoCao_XuLy_Mapping_Prompt_Anh_Tap25-68_20261124.md` mục 5), đặc biệt **Tập 48** (hồi 3 gọi David Bain là "hung thủ", hồi 4 nói trắng án). Sửa kịch bản sau khi sinh ⇒ phải lập lại job (H22).
2. Mọi tập đã qua cổng `qc_bg_mapping.py` (M1, M2, M4, M5).
3. Sinh bằng Kaggle FLUX theo `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` (H21); prompt trong file job chỉ là phần cảnh, tiền tố/hậu tố phong cách thêm lúc sinh.
4. Sau sinh: soi 100 % ảnh mới bằng montage (H2/H19/H20), đặc biệt các job V9 đã chuyển thành ẩn dụ và job có vật bề mặt (dễ bị AI vẽ chữ). Ảnh hỏng ⇒ sinh lại **cùng tên**.
5. Cập nhật `provenance.json` cho ảnh mới (L7); các dòng của ảnh đã dời vẫn còn trong file, chưa dọn.
6. Sinh ảnh tốn thời gian Kaggle / hạn mức — cần người dùng đồng ý trước (L4).
