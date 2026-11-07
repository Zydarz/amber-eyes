# BÁO CÁO HOÀN THIỆN MÔ TẢ YOUTUBE & KIỂM TRA CHÍNH TẢ TẬP 21 (4 NGÔN NGỮ)
### HỒ SƠ ANDREA YATES — HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI

*Thời điểm lập: 07/11/2026*  
*Căn cứ quy chuẩn: `AGENTS.md` (L1–L10, K1–K10, V9) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2c, §A10).*

---

## 1. Kết quả kiểm tra chính tả & chuẩn hóa ngữ văn (Spelling & Typographical Audit)

1. **Chuẩn hóa bộ mã ký tự & Unicode:**
   - Toàn bộ 4 bản kịch bản (VN, EN, JA, KO) đều đạt chuẩn **NFC (Normalization Form C)**, 0 lỗi phân rã dấu tiếng Việt, Hangul hay Kanji/Kana.
2. **Kiểm tra định dạng & khoảng trắng:**
   - 0 lỗi khoảng trắng kép (`double spaces = 0`).
   - 0 lỗi dính dấu câu với từ tiếp theo (`punct_no_space = 0`).
   - 0 dấu ba chấm lửng (`...` hay `…` = 0), tuân thủ 100% Luật G1.
   - Cặp dấu nháy trích dẫn `‘…’` và `“…”` đối xứng 100% (`unmatched = 0`).
3. **Chuẩn hóa danh xưng & địa danh quốc tế (Luật K9):**
   - Đã chuẩn hóa danh xưng y khoa: `Doctor Eileen Starbranch`, `Doctor Mohammed Saeed`, `Doctor Phillip Resnick`, `Doctor Park Dietz` (không dùng viết tắt `Dr.` tránh ngắt sai câu trong pipeline Latin).
   - Tên riêng, nhân vật lịch sử, địa phương được chuẩn hóa tuyệt đối: Andrea Pia Yates, Russell Yates, David Knapp, Michael Woroniecki, Thẩm phán Belinda Hill, Luật sư George Parnham; năm đứa trẻ Noah, John, Paul, Luke, Mary; địa danh Clear Lake, Houston, Harris County, Texas, Kerrville, Vernon.
4. **An toàn quảng cáo YouTube (Quy tắc V9 & A9.2):**
   - Đạt **0 từ cấm V9** (không gore, không máu me, không chi tiết bạo lực phản cảm).

---

## 2. Bảng đo lường ký tự Mô tả YouTube (Strictly $\le 5000$ ký tự)

Tuân thủ nghiêm ngặt giới hạn ký tự YouTube Description ($< 5000$ chars):

| Ngôn ngữ | Tệp mô tả thực tế | Số ký tự đo được | Giới hạn YouTube | Trạng thái kỹ thuật |
|:---:|---|:---:|:---:|:---:|
| **Tiếng Việt (VN)** | `02_SAN_XUAT/Tap21/mo_ta.txt` | **4.636 ký tự** | $\le 5000$ | ✅ **ĐẠT CHUẨN (Dư 364 ký tự an toàn)** |
| **Tiếng Anh (EN)** | `02_SAN_XUAT/Tap21_EN/description.txt` | **4.934 ký tự** | $\le 5000$ | ✅ **ĐẠT CHUẨN (Dư 66 ký tự an toàn)** |
| **Tiếng Nhật (JA)** | `02_SAN_XUAT/Tap21_JA/description.txt` | **2.210 ký tự** | $\le 5000$ | ✅ **ĐẠT CHUẨN (Dư 2.790 ký tự an toàn)** |
| **Tiếng Hàn (KO)** | `02_SAN_XUAT/Tap21_KO/description.txt` | **2.634 ký tự** | $\le 5000$ | ✅ **ĐẠT CHUẨN (Dư 2.366 ký tự an toàn)** |

*Lưu ý: Tất cả các bản sao trong thư mục `xuat_ban/` đều đã được đồng bộ 100% nội dung và số ký tự.*

---

## 3. Nội dung cấu trúc phần mô tả đã bổ sung

Mỗi bản mô tả trên cả 4 ngôn ngữ đều được thiết kế đầy đủ các thành phần chuyên nghiệp của kênh:
1. **Tiêu đề & Hook dẫn nhập:** Giật tít kịch tính, hấp dẫn chuẩn SEO; nêu bật nghịch lý người mẹ ưu tú, tận tụy và bi kịch của căn bệnh Loạn thần sau sinh.
2. **Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c):** Giải phẫu chi tiết 10 điểm cốt lõi (Dư chấn xã hội, Nghịch lý Altruistic Filicide, Cơ chế chia ngăn gia đình, Bản án lương tâm vs Giả bệnh Malingering, Quy tắc M'Naghten, Ngòi nổ & Khoảng trống định mệnh 1 giờ, Chữ ký Signature vs MO, Quỹ đạo leo thang, Hiệu ứng hào quang, Nạn nhân học & 4 Cảnh báo đỏ).
3. **Mốc chương (Timestamps):** Khớp chính xác 5 hồi nội dung (Intro, Hồi 1, Hồi 2, Hồi 3, Hồi 4, Hồi 5).
4. **Lưu ý pháp lý & an toàn:** Tuyên bố miễn trừ giáo dục, nguồn gốc tài liệu tư pháp, linh thú nghệ thuật, AI disclosure.
5. **Nguồn tham khảo chính thức:** Trích dẫn các bản án của Tòa Quận Hạt Harris, Tòa Phúc thẩm Texas, hồ sơ giám định lâm sàng của Dr. Phillip Resnick, tác phẩm của Suzanne O'Malley, Yates Children Memorial Fund và DSM-5-TR.
6. **Đường dây nóng bảo vệ:** Cung cấp số điện thoại bảo vệ trẻ em và hỗ trợ khủng hoảng tâm lý / trầm cảm sau sinh của từng quốc gia.
7. **Bộ Hashtags:** Tối ưu hóa SEO tìm kiếm trên YouTube.
