# Báo cáo điều tra: lệch mapping kịch bản ↔ prompt ảnh (`bg_jobs`) ↔ ảnh nền — Tập 25 → 68

**Ngày:** 24/11/2026 · **Phạm vi:** `bg_jobs_tapXX.json`, `assets/bg/tXX_*.png`, kịch bản VN hiện tại trong `01_KICH_BAN/Ho_So_Toi_Pham/TapXX/`. Chỉ đọc, chưa sửa/xoá/sinh gì.

## 1. Kết luận ngắn

Sau khi xáo thứ tự, **các file `bg_jobs_tapXX.json` không được đổi theo**. Hai kiểu lỗi, đều đo bằng script:

- **Lỗi A — SAI VỤ ÁN (nặng nhất):** `bg_jobs` của tập XX mô tả vụ án khác. Có **9 tập**: 32, 35, 39, 42, 43/48 (một trong hai), 45, 47, 49.
- **Lỗi B — ĐÚNG VỤ ÁN nhưng MÃ CÂU SAI:** trường `sentences` trỏ tới mã câu không còn tồn tại trong kịch bản hiện tại. Gặp ở **hầu hết tập 25–67 có jobs** (xem bảng). Tập chỉ 0 mã sai: **26, 30**.
- **Chưa có `bg_jobs` (chưa lập):** 51, 52, 54, 58, 60, 62, 64, 65, 66, 68. (Tập 54 chỉ có ảnh TikTok `tk54_*`.)

## 2. Lỗi A — bộ prompt không thuộc đúng tập

Bằng chứng: (i) các file có **prompt trùng 100 %** (md5); (ii) nhãn "Hồi N Tập XX (…)" nằm trong `desc` là số tập CŨ; (iii) đếm tên riêng trong kịch bản hiện tại (vd 0 lần "Dennehy" ở Tập 39).

| Tập hiện tại (kịch bản) | `bg_jobs` đang mô tả | Trùng với | Ảnh đã sinh? | Kết luận |
|---|---|---|---|---|
| **32** Trương Tử Cường (HK) | Ted Bundy, hồ Sammamish 1974 | Tập 40 (prompt trùng 100 %) | **152 ảnh t32_* = cảnh Bundy** (0 ảnh trùng byte với t40, tức đã sinh 2 lượt) | **SAI** — cần job mới + sinh lại |
| **35** Hello Kitty (HK) | Nguyễn Đức Anh, Đồng Nai | Tập 37 (trùng 100 %) | **148 ảnh t35_* = cảnh Đồng Nai** | **SAI** — cần job mới + sinh lại |
| **39** Lao Vinh Chi & Pháp Tử Anh (TQ) | Joanna Dennehy, Peterborough | Tập 50 (trùng 100 %, nhãn "Tập 39") | **152 ảnh t39_* = cảnh Dennehy** | **SAI** — cần job mới + sinh lại |
| **42** Miyazaki (Nhật) | **Lai**: tên/prompt đổi sang Iruma–Saitama nhưng `desc` vẫn là văn Dutroux ("sông Sambre", "Marc") | Tập 46 | chưa có ảnh | **HỎNG** — `desc` và `prompt` không khớp nhau; còn có `_backup_bg_jobs_tap42_old.json` (đang sửa dở) |
| **43** Suzane von Richthofen | Richthofen (nhãn "Tập 48") | Tập 48 (trùng 100 %) | chưa | **ĐÚNG cho 43** |
| **48** David Bain (NZ) | Richthofen | Tập 43 | chưa | **SAI** — cần job mới |
| **45** Lâm Quá Vân (HK) | Moses Sithole, Highveld (nhãn "Tập 45") | Tập 63 (trùng 100 %) | chưa | **SAI** |
| **63** Moses Sithole | Sithole | Tập 45 | chưa | ĐÚNG cho 63 |
| **47** Thùng Xi Măng Tân Trang (Đài Loan) | Cedric Maake, Wemmer Pan | Tập 67 (trùng 100 %) | chưa | **SAI** |
| **67** Cedric Maake | Maake | Tập 47 | chưa | ĐÚNG cho 67 |
| **49** Charles Sobhraj | Pedro López, Andes (nhãn "Tập 49") | Tập 59 (trùng 100 %) | chưa | **SAI** |
| **59** Pedro López | López | Tập 49 | chưa | ĐÚNG cho 59 |
| **37** Nguyễn Đức Anh · **40** Bundy · **50** Dennehy | đúng vụ | — | 37, 40 có ảnh | Đúng vụ (nhưng xem Lỗi B) |

Hệ quả: **3 bộ ảnh đã sinh sai hoàn toàn (t32, t35, t39 = 452 ảnh)**; 6 tập còn lại chưa sinh ảnh nên chưa tốn credit nhưng sẽ sinh sai nếu chạy nguyên trạng.

Các tập khớp vụ án (đã đối chiếu tên riêng trong kịch bản): 25, 26, 27, 28, 29, 30, 31, 33, 34, 36, 38, 40, 41, 44, 46, 50, 53, 55, 56, 57, 61. (Nhãn số tập cũ trong `desc` của 30, 31, 33, 34, 36, 41, 44, 53, 55–57, 61 lệch số hiện tại nhưng **nội dung đúng vụ** — chỉ là nhãn.)

## 3. Lỗi B — mã câu trong `sentences` không còn tồn tại

Đo bằng `parse_kichban.py` chạy lại trên kịch bản hiện tại, so từng mã `A.EE#k` của job. "Mã sai" = mã không có câu nào trong kịch bản.

| Tập | Số job | Mã sai | | Tập | Số job | Mã sai |
|---|---:|---:|---|---|---:|---:|
| 25 | 140 | 12 | | 44 | 152 | 46 |
| 26 | 135 | **0** | | 45 | 150 | 69 |
| 27 | 152 | 99 | | 46 | 152 | 47 |
| 28 | 152 | 101 | | 47 | 148 | 58 |
| 29 | 152 | 78 | | 48 | 152 | 89 |
| 30 | 155 | **0** | | 49 | 146 | 98 (kịch bản chỉ có 61 câu) |
| 31 | 170 | 91 | | 50 | 152 | 46 |
| 32 | 152 | 116 | | 53 | 152 | 46 |
| 33 | 152 | 46 | | 55 | 146 | 71 |
| 34 | 145 | 73 | | 56 | 148 | 67 |
| 35 | 148 | 88 | | 57 | 148 | 47 |
| 36 | 145 | 88 | | 59 | 146 | 77 |
| 37 | 148 | 89 | | 61 | 152 | 46 |
| 38 | 146 | 95 | | 63 | 150 | 45 |
| 39 | 152 | 83 | | 67 | 148 | 73 |
| 40 | 152 | 110 | | 41/42/43 | 150/152/152 | 63/74/46 |

Mẫu hình hay gặp: tập 33, 36, 39, 41–50, 53–63, 67 có job đầu tiên là `1.01#1`, nhưng ở kịch bản hiện tại `1.01` chỉ là thẻ `[BGM]` không có câu thoại → toàn bộ mã lệch một nấc (jobs lập theo bản kịch bản cũ chưa có thẻ BGM đứng riêng). Ngoài ra số câu cũng đổi: Tập 49 chỉ còn 61 câu, Tập 64/66/68 chỉ 49–61 câu (có vẻ kịch bản chưa viết xong, cần bạn xác nhận).

## 4. Tầng phụ: `_parsed_TapXX.json` cũng cũ

`.work/_parsed_TapXX.json` của các tập **30–51, 53–59, 61–63, 65–68** không khớp câu nào với kịch bản hiện tại (ví dụ `_parsed_Tap32.json` vẫn là văn Bundy "Vào giữa thập niên 1970…"). Chỉ 25–29, 52, 60, 64 khớp. Tôi chưa xác định file này có nằm trong đường dẫn dựng thật hay không (pipeline chính đọc `script_tapXX.json` do `parse_kichban.py` sinh); nếu có thì nó là nguồn lệch thứ hai.

## 5. Những gì tôi KHÔNG kết luận được (nói rõ)

- Tôi **chưa mở xem ảnh** nào; "ảnh sai" suy ra từ tên file/prompt/hash, không phải nhìn bằng mắt.
- Cố thử đo "ảnh khớp lời" bằng so từ khoá `desc` ↔ câu kịch bản: **kết quả nhiễu** (cả Tập 26 và 30, vốn mã hợp lệ, vẫn ra ~75 % "lệch") nên **tôi không dùng** chỉ số đó. Với tập đúng vụ nhưng mã đã sai (Lỗi B), mức độ ảnh lệch lời thật sự chỉ biết được sau khi gán lại mã.
- Tập 25 (12/140 mã sai) và 26/30 (0 mã sai) có vẻ ổn nhất; chưa kiểm bảng shot sau `parse_shots.py` vì phần lớn tập chưa có bảng shot trong `KeHoach_Video_TapXX.md`.

## 6. Đề xuất xử lý (chờ bạn duyệt — tốn credit/ghi đè nên cần L4)

1. **Dừng sinh ảnh và dựng video** cho tập 27–67 cho tới khi sửa mapping (tránh tốn thêm credit Kaggle).
2. Tập 43, 63, 67, 59, 40, 37, 50: **giữ prompt** (đúng vụ), chỉ **đánh mã câu lại** theo kịch bản hiện tại.
3. Tập 32, 35, 39, 42, 45, 47, 48, 49: **viết lại bộ prompt mới** theo bảng shot của đúng kịch bản (H25: mỗi shot một nền); với 32/35/39 phải **đưa ảnh cũ vào `.work/_cu/`** rồi sinh lại (L5) — nên xác nhận trước khi tốn credit.
4. Tập 51, 52, 54, 58, 60, 62, 64–66, 68: lập `bg_jobs` mới từ đầu (kịch bản 64/66/68 còn quá ngắn).
5. Thêm **cổng kiểm** vào pipeline: (a) mọi mã `sentences` của job phải tồn tại trong kịch bản; (b) không có hai tập trùng md5 prompt; (c) tên vụ án chính của kịch bản phải xuất hiện trong `desc` của ≥ 1 job. Có thể gộp vào `qc_bg_usage.py --plan`.

Script đo (nằm ở scratchpad phiên làm việc, chưa đưa vào repo): đối chiếu mã câu bằng `parse_kichban.py`, nhóm md5 prompt, so hash ảnh `t32↔t40`, `t35↔t37`.
