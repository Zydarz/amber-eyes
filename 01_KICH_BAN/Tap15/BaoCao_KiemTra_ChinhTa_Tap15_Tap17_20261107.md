# BÁO CÁO KIỂM TRA CHÍNH TẢ & ĐỊNH DẠNG TOÀN DIỆN KỊCH BẢN TẬP 15 VÀ TẬP 17
*Ngày thực hiện: 07/11/2026*  
*Người thực hiện: Antigravity AI Pair Programmer*  
*Quy chuẩn áp dụng: AGENTS.md (Luật L3, L6, G1, V9, K9, K10), TIEU_CHUAN_DUNG_VIDEO.md*

---

## 1. TỔNG QUAN VÀ MỤC TIÊU KIỂM TOÁN

Thực hiện rà soát, kiểm tra chính tả, ngữ pháp, quy chuẩn định dạng và quy tắc kênh Amber Eyes trên toàn bộ hệ thống file kịch bản của hai tập:
- **Tập 15** (*Vụ án Jodi Arias & Travis Alexander*): 4 ngôn ngữ (Tiếng Việt, Tiếng Anh, Tiếng Nhật, Tiếng Hàn).
- **Tập 17** (*Hồ sơ Gia đình Turpin – Ngôi nhà Bí mật tại Perris*): 4 ngôn ngữ (Tiếng Việt, Tiếng Anh, Tiếng Nhật, Tiếng Hàn).

### Các tiêu chí kiểm tra:
1. **Quy tắc V9 (Từ cấm nội dung nhạy cảm/bạo lực):** 0 từ vi phạm danh mục YouTube monetization.
2. **Quy tắc G1 (Ngắt âm & dấu ba chấm):** Tuyệt đối không dùng dấu ba chấm (`...` hoặc `…`) trong lời thoại LOI cũng như các chỉ dẫn âm thanh SFX.
3. **Chính tả & Ngữ pháp tiếng Việt:** Không dính phím gõ Telex thừa, không lặp từ vô nghĩa, chuẩn hóa dấu hỏi/ngã và từ ngữ pháp lý/tâm lý học.
4. **Định dạng dấu câu đa ngôn ngữ:**
   - Không có khoảng trắng đứng trước dấu câu (`,`, `.`, `!`, `?`, `:`) trong tiếng Việt, tiếng Anh và tiếng Hàn.
   - Tiếng Nhật kết câu chuẩn bằng dấu `。`, `！`, `？` hoặc ngoặc kép `」`.
5. **Tính toàn vẹn đối soát chéo Parity 1:1:** Đảm bảo số lượng element, lượt thoại LOI và số câu đọc khớp tuyệt đối giữa 4 ngôn ngữ để phục vụ dựng timeline song song.

---

## 2. KẾT QUẢ ĐO LƯỜNG TRƯỚC VÀ SAU XỬ LÝ (RULE L3)

| Tập | Ngôn ngữ | Số Element | Số Lượt LOI | Số Câu Đọc | Số Từ / Ký tự | Lỗi Phát Hiện Trước Fix | Lỗi Sau Fix | Trạng Thái Parity |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Tập 15** | **VN** | 63 | 36 | **203** | 5.322 từ | 2 (Lặp từ L54; Dấu `...` L255) | **0** | **Khớp 100%** |
| | **EN** | 63 | 36 | **203** | 3.518 từ | 1 (Dấu `...` L255) | **0** | **Khớp 100%** |
| | **JA** | 63 | 36 | **203** | 242 chuỗi (ja_split) | 1 (Dấu `…` L255) | **0** | **Khớp 100%** |
| | **KO** | 63 | 36 | **203** | 2.727 từ | 1 (Dấu `...` + space L255) | **0** | **Khớp 100%** |
| **Tập 17** | **VN** | 51 | 32 | **210** | 6.060 từ | 1 (Lặp từ `đối đối` L313) | **0** | **Khớp 100%** |
| | **EN** | 51 | 32 | **210** | 3.677 từ | 0 | **0** | **Khớp 100%** |
| | **JA** | 51 | 32 | **210** | 216 chuỗi (ja_split) | 0 | **0** | **Khớp 100%** |
| | **KO** | 51 | 32 | **210** | 3.002 từ | 0 | **0** | **Khớp 100%** |

---

## 3. CHI TIẾT CÁC ĐIỂM ĐÃ XỬ LÝ VÀ CHUẨN HÓA

### 3.1. Kịch bản Tập 15:
1. **Tiếng Việt (`01_KICH_BAN/Tap15/kichban_tap15_23102026.md`):**
   - *Dòng 54 (Chỉ dẫn diễn xuất)*: Phát hiện lặp từ `tái hiện hiện trường`.
     - **Trước:** `**HOST** *(giọng căng thẳng, tái hiện hiện trường)*:`
     - **Sau:** `**HOST** *(giọng căng thẳng, tái hiện bối cảnh hiện trường)*:`
   - *Dòng 255 (SFX thẻ búa tòa án)*: Phát hiện dấu ba chấm vi phạm Quy tắc G1.
     - **Trước:** `**[SFX]:** Tiếng búa gỗ của thẩm phán gõ đanh thép "Cốp... cốp... cốp", tiếng xì xào của phòng xử án.`
     - **Sau:** `**[SFX]:** Tiếng búa gỗ của thẩm phán gõ ba tiếng đanh thép dứt khoát, tiếng xì xào của phòng xử án.`
2. **Tiếng Anh (`01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md` & `01_KICH_BAN/Tap15/kichban_tap15_EN.md`):**
   - *Dòng 255*: Loại bỏ dấu ba chấm và lặp từ trong hiệu ứng âm thanh.
     - **Trước:** `The judge’s wooden gavel strikes authoritatively three times "Bang... bang... bang", murmurs ripple through the gallery.`
     - **Sau:** `**[SFX]:** The judge’s wooden gavel strikes three times with authoritative finality, murmurs ripple through the gallery.`
3. **Tiếng Nhật (`01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md`):**
   - *Dòng 255*: Loại bỏ dấu ba chấm trong hiệu ứng búa gõ.
     - **Trước:** `**[SFX]:** 裁判長の木槌が威厳をもって3度響く音「カン…カン…カン」、傍聴席のざわめき。`
     - **Sau:** `**[SFX]:** 裁判長の木槌が威厳をもって3度きっぱりと響く音、傍聴席のざわめき。`
4. **Tiếng Hàn (`01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md`):**
   - *Dòng 255*: Loại bỏ dấu ba chấm và khoảng trắng thừa trước dấu phẩy.
     - **Trước:** `**[SFX]:** 판사의 법봉이 단호하게 세 번 울리는 소리 "탕... 탕... 탕", 방청석에서 웅성거리는 탄식.`
     - **Sau:** `**[SFX]:** 판사의 법봉이 단호하게 세 번 울리는 소리, 방청석에서 웅성거리는 탄식.`

---

### 3.2. Kịch bản Tập 17:
1. **Tiếng Việt (`01_KICH_BAN/Tap17/kichban_tap17_23102026.md`):**
   - *Dòng 313 (Câu thoại `5.04#1` của Chuyên gia Tâm lý)*: Phát hiện lặp cụm từ `tuyệt đối đối với` tạo âm tiết trùng `đối đối`.
     - **Trước:** `Dưới góc độ bảo vệ quyền con người, bài học sâu sắc nhất từ thảm kịch này là sự tôn trọng tuyệt đối đối với quyền độc lập và phẩm giá của trẻ em.`
     - **Sau:** `Dưới góc độ bảo vệ quyền con người, bài học sâu sắc nhất từ thảm kịch này là sự tôn trọng tuyệt đối quyền độc lập và phẩm giá của trẻ em.`
2. **Tiếng Anh (`01_KICH_BAN/Tap17_EN/kichban_tap17_EN.md` & `01_KICH_BAN/Tap17/kichban_tap17_EN.md`):**
   - Đạt 0 lỗi chính tả, 0 vi phạm V9 (đã thay thế thành ngữ nhạy cảm ở lượt trước), 210 câu chuẩn xác.
3. **Tiếng Nhật (`01_KICH_BAN/Tap17_JA/kichban_tap17_JA.md`):**
   - Đạt 0 lỗi chính tả, dấu phân ngắt câu chuẩn xác, 210 câu khớp 1:1.
4. **Tiếng Hàn (`01_KICH_BAN/Tap17_KO/kichban_tap17_KO.md`):**
   - Đạt 0 lỗi chính tả, kính ngữ chuẩn mực, 210 câu khớp 1:1.

---

## 4. ĐỒNG BỘ DỮ LIỆU CẤU TRÚC JSON

Toàn bộ các file cấu trúc dữ liệu JSON dùng cho pipeline sản xuất âm thanh, hình ảnh và dựng phụ đề tự động đã được cập nhật đồng bộ thông qua `parse_kichban.py`:
- `.work/script_tap15.json` (VN)
- `.work/script_tap15_EN.json` (EN)
- `.work/script_tap15_JA.json` (JA)
- `.work/script_tap15_KO.json` (KO)
- `.work/script_tap17.json` (VN)
- `.work/script_tap17_EN.json` (EN)
- `.work/script_tap17_JA.json` (JA)
- `.work/script_tap17_KO.json` (KO)

## 5. KẾT LUẬN
Cả hai tập kịch bản **Tập 15** và **Tập 17** trên cả 4 ngôn ngữ (8 file kịch bản chính và 2 file bản sao EN) đều đã hoàn tất khâu kiểm tra chính tả, định dạng và đạt tiêu chuẩn sản xuất tuyệt đối (100% PASS trên tất cả các công cụ kiểm toán tự động).
