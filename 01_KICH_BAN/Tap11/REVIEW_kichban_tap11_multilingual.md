# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 11 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Paul Bernardo & Karla Homolka — Cặp đôi Ken & Barbie và Thỏa thuận với Quỷ dữ  
> **Thời điểm thẩm định:** 07/11/2026  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, G1, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap11/kichban_tap11_23102026.md`](kichban_tap11_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md`](../Tap11_EN/kichban_tap11_EN.md) (và bản copy tại `01_KICH_BAN/Tap11/kichban_tap11_EN.md`)  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md`](../Tap11_JA/kichban_tap11_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap11_KO/kichban_tap11_KO.md`](../Tap11_KO/kichban_tap11_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và các công cụ kiểm tra tự động độc lập (`.work/_qc_all_4scripts_tap11.py`, `.work/verify_en_script.py`, `.work/_qc_ja.py`, `.work/_qc_ko_parity.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **59** | **59** | **59** | **59** | **Khớp 100% (59/59)** |
| **Lượt lời thoại (LOI)** | **33** | **33** | **33** | **33** | **Khớp 100% (33/33)** |
| **Tổng số câu đọc (Sentences)** | **218** | **218** | **218** | **218** | **Khớp 1:1 tuyệt đối ($\ge 200$)** |
| **Số điểm ngắt nghỉ (NGHI)** | 8 | 8 | 8 | 8 | **Khớp 100% (cùng 1.5s)** |
| **Số cue âm thanh (BGM / SFX)** | 18 (8 BGM / 10 SFX) | 18 | 18 | 18 | **Khớp 100% vị trí & thứ tự** |
| **Số mục danh sách (Bullets)** | 8 | 8 | 8 | 8 | **Khớp 100% (vị trí `2.04` & `5.07`)** |
| **Số câu trích dẫn (Quotes)** | 28 | 28 | 28 | 28 (`‘...’`) | **Khớp 100% (28/28)** |
| **Dung lượng văn bản** | 5.867 từ / 33.773 ký tự | 3.823 từ / 33.209 ký tự | 16.001 ký tự | 3.282 từ / 19.165 ký tự | Chuẩn tỷ lệ đa ngôn ngữ |
| **Ước tính thời lượng lời** | ~27,9 phút | ~26,8 phút | ~27,5 phút | ~27,0 phút | Chuẩn tập 25–28 phút |

### Phân bổ số câu theo từng Hồi:
- **Hồi 1 (The Hook & Vỏ bọc hoàn hảo):** VN = 38 | EN = 38 | JA = 38 | KO = 38
- **Hồi 2 (Hiện trường & 4 nấc thang leo thang):** VN = 44 | EN = 44 | JA = 44 | KO = 44
- **Hồi 3 (Điên cuồng đôi & Trung hòa đạo đức):** VN = 44 | EN = 44 | JA = 44 | KO = 44
- **Hồi 4 (Thỏa thuận với Quỷ dữ & 6 cuộn băng):** VN = 46 | EN = 46 | JA = 46 | KO = 46
- **Hồi 5 (Phán quyết & 4 Cảnh báo đỏ):** VN = 46 | EN = 46 | JA = 46 | KO = 46
*(Tổng cộng: 38 + 44 + 44 + 46 + 46 = 218 câu)*

### Phân bổ tỷ lệ thoại giữa 4 vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 21 lượt thoại, 106 câu (**48,6%**) — *Đạt chuẩn thiết kế (~45–50%)*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 6 lượt thoại, 56 câu (**25,7%**) — *Đạt chuẩn thiết kế (~25%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 4 lượt thoại, 48 câu (**22,0%**) — *Đạt chuẩn thiết kế (~20–25%)*.
- **Người bình thường (Cừu/Mèo) — Cảm xúc, chân thật:** 2 lượt thoại, 8 câu (**3,7%**) — *Đạt chuẩn thiết kế (~3–5%)*.
  - N1 (`1.06`): Người hàng xóm Port Dalhousie (4 câu).
  - N2 (`4.08`): Nhân viên điều tra / Công tố viên nhận án (4 câu).

---

## 2. Kết quả vượt qua các cổng kiểm thử tự động (QC Gates)

1. **Kiểm tra đồng bộ 4 ngôn ngữ (`.work/_qc_all_4scripts_tap11.py`):**
   - 4 ngôn ngữ đều đạt chuẩn 218 câu ($\ge 200$).
   - 0 lỗi vi phạm an toàn YouTube V9 (không từ ngữ bạo lực, máu me, thô tục).
   - 0 lỗi ngắt câu G1 (không dấu ba chấm `...` hay thẻ ngắt vụn).
   - Kết quả: **ALL GREEN - PASSED**.

2. **Kiểm tra bản tiếng Anh (`.work/verify_en_script.py 11`):**
   - 59 elements, 218 sentences đối chiếu chéo 1:1 với bản tiếng Việt.
   - Kết quả: **PASSED (100% matched)**.

3. **Kiểm tra bản tiếng Nhật (`.work/_qc_ja.py 11`):**
   - Số câu: VN=218, JA=218. Số lượt: VN=33, JA=33. Lượt lệch câu: 0.
   - Cấu trúc header & bảng Production Brief: Khớp 100%.
   - Thuật ngữ glossary bắt buộc: Đầy đủ `共有妄想（フォリー・ドゥ）`, `虐待された女性の症候群`, `4つの赤い警告`, `赤い警告`.
   - 0 từ cấm YouTube Safe (`殺害` $\rightarrow$ `凶行`/`命を奪う`; `強制` $\rightarrow$ `強要`).
   - Tên riêng giữ chuẩn Latin: `Bayview Drive 57番地`.
   - Kết quả: **OK (1/1 tập đạt)**.

4. **Kiểm tra bản tiếng Hàn (`.work/_qc_ko_parity.py`):**
   - Tỷ lệ Hangul đạt 86,1% ($\ge 60\%$).
   - 0 ký tự Hán tự (Hanja), 0 dấu tiếng Việt sót lại.
   - Parity số liệu: Đầy đủ số Ả Rập `15세` (`2.06`), `35세` (`5.04`).
   - Parity tên riêng Latin: Đầy đủ `Paul Bernardo`, `Karla Homolka`, `Scarborough Rapist`.
   - Parity Quotes: 28/28 quotes khớp 1:1 tuyệt đối giữa dấu `'...'` (VN) và `‘...’` (KO).
   - Kết quả: **PASS (100% matched)**.

---

## 3. Cập nhật cấu hình hệ thống (`.work/edition.py`)
- `n_element`: Đã cập nhật chính xác `{"1.06": "N1", "4.08": "N2"}`.
- `summary`: Đã cập nhật `("1.03#1", "3.02#1")` (trỏ đúng câu thoại thật, không trỏ vào BGM/SFX, tuân thủ Luật A12).
- `act_titles`: Đã cập nhật 5 tiêu đề Hồi theo chuẩn Hệ sinh thái 10 chỉ dấu.
- Cú pháp python đã được kiểm định an toàn bằng `import edition` và `py_compile`.

---

## 4. Kết luận
Bộ kịch bản Tập 11 với đầy đủ 4 ngôn ngữ (VN, EN, JA, KO) đã hoàn thành xuất sắc, vượt ngưỡng số câu quy định (218 câu), đáp ứng trọn vẹn Hệ sinh thái 10 chỉ dấu tâm lý và hành vi, sẵn sàng 100% cho các bước sản xuất tiếp theo.
