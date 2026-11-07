# BÁO CÁO KIỂM TRA CHÍNH TẢ & ĐỊNH DẠNG TOÀN DIỆN KỊCH BẢN TẬP 19 (4 NGÔN NGỮ)
*Ngày thực hiện: 07/11/2026*  
*Người thực hiện: Antigravity AI Pair Programmer*  
*Quy chuẩn áp dụng: AGENTS.md (Luật L1–L10, K1–K10, G1, V9), TIEU_CHUAN_DUNG_VIDEO.md (Mục A2c)*

---

## 1. TỔNG QUAN VÀ MỤC TIÊU KIỂM TOÁN

Thực hiện rà soát chuyên sâu từng câu thoại, kiểm tra chính tả, ngữ pháp, quy chuẩn định dạng và quy tắc kênh **Amber eyes** trên toàn bộ hệ thống file kịch bản của **Tập 19** (*Hồ sơ Nikolas Cruz: Parkland Shooting & Màn kịch giả bệnh tâm thần trong phòng hỏi cung*):
- **Bản Tiếng Việt (VN):** `01_KICH_BAN/Tap19/kichban_tap19_23102026.md`
- **Bản Tiếng Anh (EN):** `01_KICH_BAN/Tap19_EN/kichban_tap19_EN.md` & `01_KICH_BAN/Tap19/kichban_tap19_EN.md`
- **Bản Tiếng Nhật (JA):** `01_KICH_BAN/Tap19_JA/kichban_tap19_JA.md` & `01_KICH_BAN/Tap19/kichban_tap19_JA.md`
- **Bản Tiếng Hàn (KO):** `01_KICH_BAN/Tap19_KO/kichban_tap19_KO.md` & `01_KICH_BAN/Tap19/kichban_tap19_KO.md`

### Các tiêu chí kiểm tra:
1. **Quy tắc V9 (Từ cấm nội dung nhạy cảm/bạo lực):** 0 từ vi phạm chính sách kiếm tiền và nguyên tắc an toàn cộng đồng YouTube (máu, thi thể, xác, tự sát, cắt cổ...).
2. **Quy tắc G1 (Dấu ba chấm & ngắt âm):** Tuyệt đối không dùng dấu ba chấm (`...` hoặc `…`) trong lời thoại cũng như các chỉ dẫn âm thanh.
3. **Chính tả, từ vựng & ngữ nghĩa Tiếng Việt:** Không dính phím Telex, không lặp từ vô nghĩa/dư thừa ngữ nghĩa, chuẩn hóa từ láy/từ ghép, thuật ngữ pháp lý và tâm lý học tội phạm.
4. **Ngữ pháp & Chính tả Tiếng Anh:** Rà soát ngữ pháp, dấu nháy đơn sở hữu cách (apostrophe `'`), danh xưng học thuật (`Doctor`), không lỗi chính tả.
5. **Chính tả Tiếng Nhật & Tiếng Hàn:** Rà soát Kanji/Kana, trợ từ tiếng Nhật; rà soát chính tả Hangul và thuật ngữ chuyên ngành pháp y tâm thần tiếng Hàn.
6. **Định dạng khoảng trắng & Dấu câu:** 0 lỗi khoảng trắng kép, 0 lỗi khoảng trắng trước dấu câu, ngắt dấu chuẩn.
7. **Parity đối soát chéo 1:1:** Khớp tuyệt đối 100% giữa 4 ngôn ngữ về số phần tử (51 elements), lượt thoại LOI (32 lượt), và số câu thoại (210 câu).

---

## 2. KẾT QUẢ ĐO LƯỜNG TRƯỚC VÀ SAU XỬ LÝ (RULE L3)

| Tập | Ngôn ngữ | Số Phần tử | Số Lượt LOI | Số Câu Đọc | Số Từ / Ký tự | Số lỗi phát hiện | Lỗi sau Fix | Parity 1:1 |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Tập 19** | **Tiếng Việt (VN)** | 51 | 32 | **210** | 6.298 từ | 3 (ôm chồm; trò đùa bông đùa; gi-lê / giật chuông) | **0** | **Khớp 100%** |
| | **Tiếng Anh (EN)** | 51 | 32 | **210** | 3.679 từ | 0 | **0** | **Khớp 100%** |
| | **Tiếng Nhật (JA)** | 51 | 32 | **210** | 226 chuỗi (ja_split) | 0 | **0** | **Khớp 100%** |
| | **Tiếng Hàn (KO)** | 51 | 32 | **210** | 3.075 từ | 1 (Gõ thừa ký tự `사법정신각학`) | **0** | **Khớp 100%** |

---

## 3. CHI TIẾT CÁC ĐIỂM ĐÃ PHÁT HIỆN & CHUẨN HÓA

### 3.1. Kịch bản Tiếng Việt (`01_KICH_BAN/Tap19/kichban_tap19_23102026.md`)
1. **Câu `2.08#3` (Từ dùng sai ngữ cảnh):**
   - **Gốc:** `Hai anh em ôm chồm lấy nhau, và trong khoảnh khắc đó, sự phân chia ngăn cách nhận thức của hung thủ bộc lộ rõ rệt hơn bao giờ hết.`
   - **Phân tích:** Trong tiếng Việt, *"ôm chồm"* là hành động chồm người tới phía trước; cử chỉ ôm siết lấy một người với niềm xúc động nghẹn ngào chuẩn xác phải là **"ôm chầm"**.
   - **Đã chuẩn hóa:** `Hai anh em ôm chầm lấy nhau, và trong khoảnh khắc đó, sự phân chia ngăn cách nhận thức của hung thủ bộc lộ rõ rệt hơn bao giờ hết.`
2. **Câu `2.10#2` (Thuật ngữ trang bị & hành động):**
   - **Gốc:** `Về mặt thủ đoạn, hắn chuẩn bị áo gi-lê chiến thuật, giấu súng trong bao đàn guitar, bắt xe dịch vụ đến trường và cố tình giật chuông báo cháy để gom các nạn nhân lại.`
   - **Phân tích:** Đồng bộ hóa thuật ngữ *"áo vest chiến thuật"* (tactical vest) thống nhất với toàn bộ tài liệu dự án; thao tác hộp báo cháy chuẩn là *"kéo chuông báo cháy"* (pull the fire alarm) thay vì *"giật chuông"*.
   - **Đã chuẩn hóa:** `Về mặt thủ đoạn, hắn chuẩn bị áo vest chiến thuật, giấu súng trong bao đàn guitar, bắt xe dịch vụ đến trường và cố tình kéo chuông báo cháy để gom các nạn nhân lại.`
3. **Câu `5.05#5` (Lặp từ ngữ nghĩa / Tautology):**
   - **Gốc:** `Đừng bao giờ xem nhẹ bất kỳ lời đe dọa nào như một trò đùa bông đùa của lứa tuổi học trò.`
   - **Phân tích:** Cụm từ *"trò đùa bông đùa"* bị trùng lặp nghĩa (đùa - bông đùa).
   - **Đã chuẩn hóa:** `Đừng bao giờ xem nhẹ bất kỳ lời đe dọa nào như một trò bông đùa của lứa tuổi học trò.`

### 3.2. Kịch bản Tiếng Hàn (`01_KICH_BAN/Tap19_KO/kichban_tap19_KO.md`)
1. **Câu `3.02#1` (Lỗi gõ thừa ký tự chuyên ngành):**
   - **Gốc:** `역사적인 재판을 준비하기 위해 검찰 측은 미국 최고의 사법정신각학 권위자 중 한 명인 찰스 스콧 박사를 초빙했습니다.`
   - **Phân tích:** Thuật ngữ Giám định Tâm thần Pháp y tiếng Hàn là **사법정신의학** (*Forensic Psychiatry*). Văn bản gốc vô tình gõ thừa ký tự `각` thành `사법정신각학`.
   - **Đã chuẩn hóa:** `역사적인 재판을 준비하기 위해 검찰 측은 미국 최고의 사법정신의학 권위자 중 한 명인 찰스 스콧 박사를 초빙했습니다.`

### 3.3. Kịch bản Tiếng Anh & Tiếng Nhật
- **Tiếng Anh (210 câu):** 0 lỗi chính tả, 0 lỗi ngữ pháp, danh xưng `Doctor Charles Scott` nhất quán, các mốc thời gian dạng chữ đọc chuẩn G11 (`twenty twenty-two`, `twenty twenty-three`).
- **Tiếng Nhật (210 câu):** 0 lỗi chính tả, trợ từ tự nhiên, thuật ngữ tâm thần pháp y và mô hình BTAM chuẩn xác (`メリンガリング`, `反社会性パーソナリティ障害`, `行動脅威アセスメント`, `リーケージ`, `フィクセーション`, `アンカー・ロス`, `タクティカル・プレパレーション`).

---

## 4. ĐỒNG BỘ HÓA TÀI NGUYÊN PIPELINE

Đã đồng bộ hóa 100% các sửa đổi chính tả vào:
1. Script sinh tự động: `.work/_generate_tap19_210_vn.py`, `.work/_generate_tap19_210_ko.py`.
2. File kịch bản gốc và phụ trợ: `01_KICH_BAN/Tap19/kichban_tap19_23102026.md`, `01_KICH_BAN/Tap19_KO/kichban_tap19_KO.md`, `01_KICH_BAN/Tap19/kichban_tap19_KO.md`, `01_KICH_BAN/Tap19/REVIEW_kichban_tap19_10chiau.md`.
3. File JSON pipeline parsed: `.work/script_tap19.json`, `script_tap19_EN.json`, `script_tap19_JA.json`, `script_tap19_KO.json`.
4. File mô tả YouTube: `02_SAN_XUAT/Tap19/mo_ta.txt` và `02_SAN_XUAT/Tap19/xuat_ban/mo_ta.txt` (4.853 ký tự $\le 5.000$).

---

## 5. KẾT LUẬN

Bộ kịch bản 4 ngôn ngữ của **Tập 19** đạt trạng thái **ALL GREEN** tuyệt đối:
- **0 lỗi chính tả, 0 lỗi từ vựng, 0 lỗi định dạng.**
- **0 lỗi V9 (từ cấm bạo lực), 0 lỗi G1 (dấu ba chấm).**
- **Đạt chuẩn 100% Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (Tiêu chuẩn A2c / Luật K10).**
- **Parity 1:1 đồng bộ hoàn hảo 210 câu thoại $\times$ 4 ngôn ngữ.**
Kịch bản đã sẵn sàng cho Bước 2 (Diễn xuất & TTS).
