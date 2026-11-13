# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 11 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Paul Bernardo & Karla Homolka — Cặp đôi Ken & Barbie và Thỏa thuận với Quỷ dữ  
> **Thời điểm nâng cấp & thẩm định:** 13/11/2026  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, G1, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap11/kichban_tap11_23102026.md`](kichban_tap11_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md`](../Tap11_EN/kichban_tap11_EN.md) (và bản copy tại `01_KICH_BAN/Tap11/kichban_tap11_EN.md`)  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md`](../Tap11_JA/kichban_tap11_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap11_KO/kichban_tap11_KO.md`](../Tap11_KO/kichban_tap11_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và các công cụ kiểm tra tự động độc lập (`.work/verify_en_script.py`, `.work/_qc_ja.py`, `.work/_qc_ko_parity.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **65** | **65** | **65** | **65** | **Khớp 100% (65/65)** |
| **Lượt lời thoại (LOI)** | **39** | **39** | **39** | **39** | **Khớp 100% (39/39)** |
| **Tổng số câu đọc (Sentences)** | **272** | **272** | **272** | **272** | **Khớp 1:1 tuyệt đối ($\ge 200$)** |
| **Số điểm ngắt nghỉ (NGHI)** | 7 | 7 | 7 | 7 | **Khớp 100% (cùng 1.5s)** |
| **Số cue âm thanh (BGM / SFX)** | 19 (9 BGM / 10 SFX) | 19 | 19 | 19 | **Khớp 100% vị trí & thứ tự** |
| **Số mục danh sách (Bullets)** | 0 | 0 | 0 | 0 | **Khớp 100%** |
| **Số câu trích dẫn (Quotes)** | 28 | 28 | 28 | 28 (`‘...’`) | **Khớp 100% (28/28)** |
| **Dung lượng ký tự** | 43.405 ký tự | 42.578 ký tự | 20.092 ký tự | 23.303 ký tự | Chuẩn tỷ lệ đa ngôn ngữ |
| **Ước tính thời lượng** | ~32–34 phút | ~31–33 phút | ~32–34 phút | ~31–33 phút | Chuẩn tập chuyên sâu |

### Phân bổ số câu theo từng Hồi:
- **Hồi 1 (The Hook & Vỏ bọc hoàn hảo Ken & Barbie):** VN = 46 | EN = 46 | JA = 46 | KO = 46
- **Hồi 2 (Hiện trường & Quỹ đạo leo thang 4 nấc thang):** VN = 55 | EN = 55 | JA = 55 | KO = 55
- **Hồi 3 (Điên cuồng đôi, Vật hóa & Chia ngăn nhận thức):** VN = 50 | EN = 50 | JA = 50 | KO = 50
- **Hồi 4 (Thỏa thuận với Quỷ dữ & Sự sụp đổ của mặt nạ nạn nhân):** VN = 63 | EN = 63 | JA = 63 | KO = 63
- **Hồi 5 (Phán quyết, Di sản tư pháp & 4 Cảnh báo đỏ):** VN = 58 | EN = 58 | JA = 58 | KO = 58
*(Tổng cộng: 46 + 55 + 50 + 63 + 58 = 272 câu)*

### Phân bổ tỷ lệ thoại giữa 4 vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 20 lượt thoại, 125 câu (**46,0%**) — *Đạt chuẩn thiết kế (~45–50%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 8 lượt thoại, 72 câu (**26,5%**) — *Đạt chuẩn thiết kế (~25%)*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 9 lượt thoại, 66 câu (**24,3%**) — *Đạt chuẩn thiết kế (~25%)*.
- **Người bình thường (Cừu/Mèo) — Cảm xúc, chân thật:** 2 lượt thoại, 9 câu (**3,3%**) — *Đạt chuẩn thiết kế (~3–5%)*.
  - N1 (`1.06`): Người hàng xóm Port Dalhousie (4 câu).
  - N2 (`4.11`): Nhân viên điều tra / Công tố viên nhận án (5 câu).

---

## 2. Kết quả vượt qua các cổng kiểm thử tự động (QC Gates)

1. **Kiểm tra bản tiếng Anh (`.work/verify_en_script.py 11`):**
   - 65 elements, 272 sentences đối chiếu chéo 1:1 tuyệt đối với bản tiếng Việt.
   - Kết quả: **✅ Episode 11 PASSED: 65 elements, 272 sentences perfectly matched!**

2. **Kiểm tra bản tiếng Nhật (`.work/_qc_ja.py 11`):**
   - Số câu: VN=272, JA=272. Số lượt: VN=39, JA=39. Lượt lệch câu: 0.
   - Cấu trúc header & bảng Production Brief: Khớp 100%.
   - Thuật ngữ glossary bắt buộc: Đầy đủ `共有妄想（フォリー・ドゥ）`, `ハロー効果`, `客体化`, `非人間化`, `4つの赤い警告`.
   - 0 lỗi ký tự sót tiếng Việt, 0 chữ Hán giản thể Trung Quốc.
   - Kết quả: **OK (1/1 tập đạt)**.

3. **Kiểm tra bản tiếng Hàn (`.work/_qc_ko_parity.py`):**
   - Tỷ lệ Hangul đạt 86,9% ($\ge 60\%$).
   - 0 ký tự Hán tự (Hanja), 0 dấu tiếng Việt sót lại.
   - Parity số liệu: Đầy đủ số Ả Rập theo turns (`57`, `1987`, `1990`, `1991`, `1992`, `14`, `15`, `1993`, `12`, `17`, `1994`, `6`, `1995`, `25`, `2005`, `35`, `4`, `7`).
   - Parity tên riêng Latin: Đầy đủ `Paul Bernardo`, `Karla Homolka`, `Scarborough Rapist`, `Bayview Drive`, `Kristen French`, `Leslie Mahaffy`, `Ken Murray`, `Donna French`, `Doug French`, `Leanne Bordelais`.
   - Parity Quotes: 28/28 quotes khớp 1:1 tuyệt đối giữa dấu `'...'` (VN) và `‘...’` (KO).
   - Kết quả: **PASS (100% matched, exit code 0)**.

---

## 3. Cập nhật cấu hình hệ thống (`.work/edition.py`)
- `n_element`: Đã cập nhật chính xác `{"1.06": "N1", "4.11": "N2"}` (do chèn các element tâm lý học mới trong Hồi 4).
- `act1_cue`: Đã cập nhật trỏ sang `"1.12"` (chuyển đổi bed theo cấu trúc mới).
- `click_cues`: Đã cập nhật sang `("1.03", "4.09")`.
- `summary`: Giữ chuẩn `("1.03#1", "3.02#1")` (trỏ đúng câu thoại thật, không trỏ vào BGM/SFX, tuân thủ Luật A12).
- Cú pháp python đã được kiểm định an toàn bằng `py_compile`.

---

## 4. Kết luận
Bộ kịch bản Tập 11 với đầy đủ 4 ngôn ngữ (VN, EN, JA, KO) đã hoàn thành xuất sắc nâng cấp chuyên sâu tâm lý:
1. Đạt đủ 10 chỉ dấu tâm lý & hành vi (A2c/K10) và phân tích sâu sắc 5 đối tượng (thủ phạm, đồng phạm, nạn nhân & gia đình, người nắm giữ chứng cứ, xã hội).
2. Phân biệt lâm sàng rạch ròi giữa *Sự hối hận chân thực (Authentic Remorse)* với *Sự thương hại bản thân bệnh lý (Pathological Self-Pity)* và *Chiến lược đóng vai nạn nhân thao túng (Manipulative Victimhood)*.
3. Đạt chuẩn Parity 1:1 tuyệt đối trên 65 elements, 272 câu, 39 turns thoại trên cả 4 ngôn ngữ.
4. Đã sinh đầy đủ 4 file JSON (`script_tap11.json`, `script_tap11_EN.json`, `script_tap11_JA.json`, `script_tap11_KO.json`), sẵn sàng 100% cho pipeline sản xuất tiếp theo.
