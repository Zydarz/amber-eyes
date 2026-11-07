# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 15 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Jodi Arias — Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới & Thảm Kịch Phòng Tắm  
> **Thời điểm thẩm định:** 07/11/2026  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap15/kichban_tap15_23102026.md`](kichban_tap15_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md`](../Tap15_EN/kichban_tap15_EN.md)  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md`](../Tap15_JA/kichban_tap15_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md`](../Tap15_KO/kichban_tap15_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và các công cụ kiểm tra tự động độc lập:

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **63** | **63** | **63** | **63** | **Khớp 100% (63/63)** |
| **Lượt lời thoại (LOI)** | **36** | **36** | **36** | **36** | **Khớp 100% (36/36)** |
| **Tổng số câu đọc (Sentences)** | **203** | **203** | **203** | **203** | **Khớp 1:1 tuyệt đối** |
| **Số điểm ngắt nghỉ (NGHI)** | 11 | 11 | 11 | 11 | **Khớp 100% (cùng giây)** |
| **Số cue âm thanh (BGM / SFX)** | 16 (6 BGM / 10 SFX) | 16 | 16 | 16 | **Khớp 100% vị trí & thứ tự** |
| **Số câu trích dẫn (Quotes)** | 1 (`4.10`) | 1 (`‘...’`) | 1 (`「...」`) | 1 (`‘...’`) | **Khớp 100%** |
| **Dung lượng văn bản** | 4.815 từ / 22.140 ký tự | 3.620 từ / 23.410 ký tự | 11.230 ký tự | 3.010 từ / 13.450 ký tự | Chuẩn tỷ lệ đa ngôn ngữ |
| **Ước tính thời lượng lời** | ~25,8 phút | ~25,4 phút | ~26,2 phút | ~25,6 phút | Chuẩn tập 25–28 phút |

### Phân bổ số câu theo từng Hồi:
- **Hồi 1 (The Hook & Ám ảnh độc hại):** VN = 39 | EN = 39 | JA = 39 | KO = 39
- **Hồi 2 (Dấu vết kỹ thuật số & Chiếc bình xăng):** VN = 38 | EN = 38 | JA = 38 | KO = 38
- **Hồi 3 (Giải mã tâm lý BPD & Cơn cuồng nộ ruồng bỏ):** VN = 37 | EN = 37 | JA = 37 | KO = 37
- **Hồi 4 (Trò ảo thuật phòng thẩm vấn & Phiên tòa truyền hình):** VN = 46 | EN = 46 | JA = 46 | KO = 46
- **Hồi 5 (Phán quyết chung thân & 4 Cảnh báo đỏ sinh tồn):** VN = 43 | EN = 43 | JA = 43 | KO = 43

### Phân bổ tỷ lệ thoại giữa các vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 23 lượt thoại, 97 câu (**47,8%**) — *Đạt chuẩn thiết kế (~45–50%)*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 6 lượt thoại, 53 câu (**26,1%**) — *Đạt chuẩn thiết kế (~25%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 5 lượt thoại, 45 câu (**22,2%**) — *Đạt chuẩn thiết kế (~25%)*.
- **Người bình thường (Cừu/Mèo) — Chân thật:** 2 lượt thoại, 8 câu (**3,9%**) — N1 (1.07: 4 câu) & N2 (4.06: 4 câu).

---

## 2. Thẩm định chi tiết Hệ sinh thái 10 Chỉ Dấu Tâm Lý & Hành Vi (A2c)

Toàn bộ 10 chỉ dấu đã được rà soát đối chiếu chéo trong cả 4 ngôn ngữ, bảo đảm chiều sâu khoa học hành vi pháp y:

1. **Ảnh hưởng & Dư chấn xã hội (Social Impact & Public Fascination):**  
   - Thể hiện tại `1.03`, `1.10`, `4.10`, `5.04`.
   - Phân tích hiện tượng "Rạp xiếc truyền thông" (Media Circus), áp lực dư luận lên bồi thẩm đoàn thời kỳ bùng nổ mạng xã hội và cuộc cải cách tư pháp về hạn chế ghi hình tại tòa án.

2. **Cách hung thủ nhìn nhận nạn nhân & Vì sao (Victim Perception & Objectification):**  
   - Thể hiện tại `1.08`, `2.07`, `3.05`, `3.08`.
   - Vật hóa (Objectification) nạn nhân thành công cụ cảm xúc để khỏa lấp lỗ hổng căn tính trống rỗng; sự triệt tiêu lòng trắc ẩn và khiếm khuyết Thuyết tâm trí (Theory of Mind).

3. **Cách hung thủ nhìn nhận người thân & Phân mảnh tâm lý (Compartmentalization):**  
   - Thể hiện tại `2.05`, `2.08`, `3.08`.
   - Cơ chế Chia ngăn nhận thức: Ngăn người cháu gái ngoan ngoãn ở Yreka vs. Ngăn kẻ săn mồi chuẩn bị 3 can xăng; ngay sau án mạng gặp gỡ người đàn ông khác tại Utah với nụ cười rạng rỡ.

4. **Thái độ tâm lý trước bản án (Narcissistic Collapse & Pathological Self-Pity):**  
   - Thể hiện tại `4.10`, `4.11`, `5.02`.
   - Cú sốc sụp đổ bản ngã ái kỷ khi bị tuyên có tội; chuyển từ ngông cuồng thách thức sang tự thương hại bệnh lý, xin nhận án tử hình để tránh nhục nhã rồi lại kháng cáo xin giảm án.

5. **Hệ thống tự bào chữa & Trung hòa đạo đức (Techniques of Neutralization):**  
   - Thể hiện tại `3.08`, `4.07`, `4.08`.
   - 3 tầng ngụy biện: Phủ nhận trách nhiệm $\rightarrow$ Đổ lỗi cho nạn nhân và bôi nhọ người đã khuất $\rightarrow$ Đóng vai nạn nhân tự vệ bị bạo hành.

6. **Ngòi nổ & Điểm gãy tâm lý (Precipitating Stressor & Tipping Point):**  
   - Thể hiện tại `1.08`, `3.05`.
   - Cuối tháng 5/2008, khi biết tin Travis chuẩn bị cùng người phụ nữ khác đi Cancun; đây là giọt nước tràn ly kích hoạt nỗi sợ bị ruồng bỏ tối hậu và sự tổn thương cái tôi ái kỷ.

7. **Dấu ấn Signature vs Thủ đoạn MO:**  
   - Thể hiện tại `2.05`, `2.07`, `4.08`.
   - MO (thủ đoạn thay đổi để trốn tránh): Thuê xe ở xa, nhuộm tóc, tắt điện thoại, mang 3 can xăng dự trữ để tránh quẹt thẻ, bỏ máy ảnh vào máy giặt.
   - Signature (dấu ấn tâm lý bất biến): Chụp lại những bức ảnh cuối cùng trong buồng tắm; mức độ gây hại dồn dập (Overkill) phản ánh cơn cuồng nộ cá nhân thù hận tột độ.

8. **Chu kỳ ảo tưởng & Quỹ đạo leo thang (Escalation Cycle):**  
   - Thể hiện tại `1.05`, `1.07`, `1.08`, `2.07`.
   - 4 giai đoạn leo thang: Lý tưởng hóa & Thần tượng $\rightarrow$ Lấn ranh giới & Rình rập $\rightarrow$ Phá hoại tài sản $\rightarrow$ Cuồng nộ hủy diệt (Borderline Rage).

9. **Hiệu ứng Hào quang & Điểm mù xã hội (Halo Effect & Collective Blindspots):**  
   - Thể hiện tại `1.05`, `1.07`, `4.03`.
   - Vẻ ngoài nữ tính, thanh lịch, đoan trang và phong thái trí thức đã tạo nên một tấm khiên hào quang che mắt xã hội và khiến nạn nhân mất cảnh giác.

10. **Nạn nhân học & Cảnh báo đỏ sinh tồn (Victimology & Survival Red Flags):**  
    - Thể hiện tại `1.05`, `1.08`, `5.04`, `5.06`, `5.07`, `5.08`, `5.10`.
    - Trả lại nhân phẩm trọn vẹn cho Travis Alexander; phân tích nguy cơ khi không kiên quyết thiết lập ranh giới cứng rắn.
    - 4 Tín hiệu cảnh báo đỏ sinh tồn thực tế từ nguyên lý *The Gift of Fear* của Gavin de Becker.

---

## 3. Kết quả rà soát chính tả & quy chuẩn kỹ thuật âm thanh

Đã thực hiện kiểm định tự động toàn diện qua các công cụ `.work/_spellcheck_tap15.py` và `.work/_qc_all_4scripts_tap15.py`:

| Ngôn ngữ | Kiểm tra chính tả & Spacing | Lỗi dấu câu / Kết câu | Quy tắc G1 (Chấm lửng `...`) | Quy tắc V9 (Từ cấm bạo lực) | Trạng thái |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **VN** | 0 lỗi telex, 0 lỗi dấu thanh, 0 lặp từ | 100% kết thúc bằng `.?!` | 0 vi phạm (0 chấm lửng) | 0 từ cấm | ✅ **100% PASS** |
| **EN** | 0 typo (Pyspellchecker + Whitelist) | 100% kết thúc bằng `.?!` | Đã chuẩn hóa câu `4.10#2` (dùng dấu phẩy `,` và trích dẫn `‘...’`) | 0 từ cấm | ✅ **100% PASS** |
| **JA** | 0 typo Kanji/Kana, 0 double space | 100% kết thúc bằng `。！？「」` | 0 vi phạm (0 chấm lửng) | 0 từ cấm | ✅ **100% PASS** |
| **KO** | 0 typo Hangul, 0 lỗi 띄어쓰기 | 100% kết thúc bằng `.?!` | 0 vi phạm (0 chấm lửng) | 0 từ cấm | ✅ **100% PASS** |

---

## 4. Kết luận thẩm định

1. **Parity 1:1:** Khớp 100% giữa 4 ngôn ngữ VN, EN, JA, KO về số Hồi (5), số Element (63), số câu (203), số lượt thoại (36), và mốc thời gian nghỉ.
2. **Quy tắc an toàn V9 & A9.2:** Hoàn toàn sạch từ cấm, không chứa nội dung bạo lực kích động (0 lỗi trên cả 4 ngôn ngữ).
3. **Quy tắc âm thanh G1:** 0 dấu chấm lửng giữa câu trên cả 4 ngôn ngữ.
4. **Sẵn sàng sản xuất:** Hồ sơ kịch bản đã sẵn sàng cho các công đoạn tiếp theo (Diễn xuất & Tổng hợp âm thanh TTS).
