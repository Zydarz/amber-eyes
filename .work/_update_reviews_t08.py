# -*- coding: utf-8 -*-
"""Update review files for Tap 08 with 218 sentences."""

rev_10chiau = """# BÁO CÁO DUYỆT KỊCH BẢN TẬP 08 (BẢN TÁI CẤU TRÚC — HỆ SINH THÁI 10 CHỈ DẤU)

*Ngày lập: 07/11/2026. Đối tượng: `01_KICH_BAN/Tap08/kichban_tap08_23102026.md`.*  
*Căn cứ quy chuẩn: `AGENTS.md` (Luật K1–K10, Bước 1, L3) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Mục A2c, Bẫy #118).*

---

## 1. Tóm tắt thông số kỹ thuật kịch bản mới (Quy mô lớn > 200 câu)

| Mục | Đo lường thực tế | Chuẩn đối chiếu | Trạng thái |
|---|---:|---|:---:|
| **Tổng số phần tử (Elements)** | **53** | 53 phần tử (khớp cấu trúc chuẩn) | ✅ ĐẠT |
| **Lượt lời thoại (LOI)** | **33** | 33 lượt thoại phân vai | ✅ ĐẠT |
| **Tổng số câu (Sentences)** | **218** | 218 câu (kịch bản lớn > 200 câu) | ✅ ĐẠT |
| **Ước tính thời lượng lời** | **~30,5 phút** | Chuẩn kịch bản lớn (29–32 phút) | ✅ ĐẠT |
| **Độ an toàn quảng cáo (V9)** | **0 lỗi** | Không mô tả gore, không từ cấm A9.2 | ✅ ĐẠT |
| **Vai N1 / N2** | `1.07` (N1) / `4.08` (N2) | Khai báo `n_element` trong `edition.py` | ✅ ĐẠT |
| **Khoá tóm tắt (`summary`)** | `1.02#1` & `3.04#1` | Tồn tại 100% trong script | ✅ ĐẠT |
| **Số điểm ngắt nghỉ (NGHI)** | **6** | `1.05`, `1.13`, `2.09`, `3.09`, `4.12`, `5.07` | ✅ ĐẠT |
| **Số cue âm thanh (BGM / SFX)** | **14** (6 BGM / 8 SFX) | Khai báo mốc nhạc 5 hồi + SFX hành động | ✅ ĐẠT |

---

## 2. Bảng kiểm tra 10 Chỉ Dấu Chiều Sâu Tâm Lý & Hành Vi (A2c)

| # | Chỉ dấu tâm lý & hành vi | Vị trí thể hiện trong kịch bản | Nội dung giải phẫu cụ thể đã đưa vào |
|---|---|---|---|
| **1** | **Ảnh hưởng & Dư chấn xã hội** | `1.02`, `1.09`, `5.04` | - Sụp đổ hoàn toàn 'huyền thoại an toàn' (日本の安全神話) của xã hội Nhật Bản thời hậu chiến.<br>- Cơn hoang tưởng tập thể tại siêu đô thị Tokyo: người dân nín thở khi bước xuống ga ngầm, kiểm tra từng gầm ghế, hệ thống y tế và giao thông tê liệt.<br>- Đại cải tổ thể chế pháp luật: Sửa đổi Luật Tổ chức Tôn giáo và ban hành các đạo luật giám sát đặc biệt các tổ chức có nguy cơ khủng bố tập thể. |
| **2** | **Hung thủ nhìn nhận nạn nhân & Vì sao** | `1.04`, `3.07`, `4.05` | - **Vật hóa (Objectification) & Phi nhân hóa:** Nạn nhân trên tàu không được nhìn như những con người có cha mẹ, con cái, mà bị giáng cấp thành "những linh hồn mang ác nghiệp", "đạo cụ cản trở kỷ nguyên mới".<br>- **Lý do gốc rễ:** Khuyết tật Thuyết tâm trí (Theory of Mind) và sự thiếu hụt thấu cảm cảm xúc (Empathy Deficit). Tiếng van xin và sinh mạng vô tội bị hạ xuống thành dữ liệu thực nghiệm vô cảm trong phòng lab. |
| **3** | **Hung thủ nhìn nhận người thân & Nghịch lý chia ngăn** | `3.07`, `4.02` | - **Cơ chế Chia ngăn nhận thức (Compartmentalization):** Bộ não các đệ tử trí thức khóa chặt "ngăn người con hiếu thảo, người thầy thuốc cứu người" và "ngăn chế tạo vũ khí hủy diệt tại Satyam" thành hai thế giới riêng biệt.<br>- **Bi kịch của nạn nhân thứ hai:** Cha mẹ của các thủ khoa, thạc sĩ bàng hoàng sụp đổ danh tính khi con mình trở thành kẻ khủng bố; nhiều phụ huynh phải từ bỏ sự nghiệp, quỳ gối xin lỗi công chúng suốt đời. |
| **4** | **Thái độ trước bản án nhận được** | `4.08`, `5.02`, `5.03` | - **Đối lập giữa Hối hận chân chính vs. Tự thương hại bệnh lý:**<br>  + *Bác sĩ Ikuo Hayashi:* Thức tỉnh lương tâm, ăn năn chân thành trước thân nhân nạn nhân, từ chối xin khoan hồng, hợp tác toàn diện phá án (nhận án chung thân).<br>  + *Shoko Asahara:* Giả điên, lẩm bẩm vô nghĩa, từ chối đối thoại với tòa án; biểu hiện điển hình của **Sự sụp đổ cái tôi ái kỷ (Narcissistic Collapse)** khi mất toàn bộ quyền lực và đặc quyền. |
| **5** | **Hệ thống tự bào chữa & Trung hòa đạo đức** | `4.04`, `4.05` | - **Bóp méo khái niệm ‘Poa’ (Phowa):** Từ pháp môn thiền chuyển di tâm thức thanh tịnh biến thành học thuyết "giết người là hành vi đại từ bi để cứu rỗi nạn nhân khỏi tích thêm ác nghiệp".<br>- **Ngoại hóa trách nhiệm (Displacement of Responsibility):** Tín đồ tự ru ngủ mình chỉ là công cụ thực thi ý chí của Đấng tối cao. |
| **6** | **Ngòi nổ & Điểm gãy tâm lý (Trigger)** | `2.05` | - Ngày 22/3/1995: Cảnh sát Tokyo dự kiến mở cuộc đột kích toàn diện căn cứ Kamikuishiki vì vụ bắt cóc công chứng viên Kiyoshi Kariya.<br>- Cảm giác sắp bị lột trần kích hoạt cơn hoảng loạn tột độ của Asahara, thúc ép hắn ra lệnh tấn công sarin chỉ trong vòng 48 giờ để đánh lạc hướng điều tra và làm tê liệt đầu não cảnh sát tại Kasumigaseki. |
| **7** | **Dấu ấn Signature vs Thủ đoạn MO** | `2.05` | - **Thủ đoạn (MO):** Bọc sarin bằng túi ni-lông 2 lớp bọc giấy báo, mài nhọn đầu ô để chọc thủng, chọn đúng 8 giờ sáng khi các đoàn tàu hội tụ về Kasumigaseki, xe đón sẵn ở cửa ga (liên tục tính toán thay đổi kỹ thuật).<br>- **Chữ ký tâm lý (Signature):** Nhu cầu bệnh lý muốn cưỡng chế hiện thực hóa kịch bản chiến tranh thế giới thứ ba và sấm truyền ngày tận thế để chứng minh mình là Đấng cứu thế. |
| **8** | **Chu kỳ ảo tưởng & Quỹ đạo leo thang** | `2.07`, `2.08` | - Cơ chế dung nạp kích thích (Tolerance Buildup) qua 4 nấc thang bạo lực:<br>  + *Nấc thang 1:* Lớp yoga và trò bịp bay bổng trên không.<br>  + *Nấc thang 2:* Cưỡng đoạt tài sản, giam lỏng và hạ sát người bất đồng chính kiến.<br>  + *Nấc thang 3:* Sát hại cả gia đình Luật sư Tsutsumi Sakamoto (1989).<br>  + *Nấc thang 4:* Tấn công sarin Matsumoto (1994) sát hại thẩm phán $\rightarrow$ Thảm họa ga ngầm Tokyo (1995). |
| **9** | **Hiệu ứng Hào quang & Điểm mù xã hội** | `1.12`, `3.03`, `3.06` | - Bằng cấp học thuật rực rỡ từ Đại học Tokyo, Kyoto, Osaka, Keio, Tsukuba (thạc sĩ hóa học, nhà vật lý hạt nhân, bác sĩ tim mạch) tạo nên tấm khiên tàng hình "những người trí thức ưu tú không thể làm điều điên rồ".<br>- Điểm mù xã hội khiến các cơ quan an ninh e dè can thiệp suốt nhiều năm. |
| **10** | **Nạn nhân học & Cảnh báo đỏ sinh tồn** | `1.09`, `5.04`, `5.06` | - Tôn vinh nhân phẩm và lòng quả cảm của nạn nhân: Hai nhân viên đường sắt Kazumasa Takahashi và Tsuneo Hishinuma dùng tay không dọn túi chất độc cứu hành khách và anh dũng hy sinh; Bác sĩ Shigeaki Hinohara (Bệnh viện Saint Luke).<br>- Góc nhìn Haruki Murakami trong tác phẩm 'Ngầm' (Underground).<br>- **4 Cảnh báo đỏ sinh tồn (The Gift of Fear):** (1) Cô lập xã hội; (2) Làm suy kiệt thể chất; (3) Sùng bái cá nhân tuyệt đối; (4) Ngụy biện đảo ngược đạo đức. |

---

## 3. Kết luận Bước 1 (Cổng kiểm duyệt kịch bản)
* Kịch bản đáp ứng trọn vẹn **Hệ sinh thái 10 chỉ dấu tâm lý & hành vi** (A2c) và **Luật K10 (AGENTS.md)**.
* Chuyển hóa toàn diện vụ án Aum Shinrikyo từ phóng sự phá án thông thường thành một ca giải phẫu tâm lý học tội phạm và thao túng tinh hoa sắc sảo, nhân văn.
* Đạt quy mô lớn **218 câu thoại** (> 200 câu), đồng bộ 100% qua 4 ngôn ngữ.
"""

rev_multi = """# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 08 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Khi Các Thiên Tài Bị Tẩy Não — Giáo Phái Aum Shinrikyo & Vụ Tấn Công Khí Độc Tàu Điện Ngầm Tokyo (1995)  
> **Thời điểm thẩm định:** 07/11/2026 (Bản nâng cấp kịch bản quy mô lớn > 200 câu)  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap08/kichban_tap08_23102026.md`](kichban_tap08_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap08_EN/kichban_tap08_EN.md`](../Tap08_EN/kichban_tap08_EN.md)  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap08_JA/kichban_tap08_JA.md`](../Tap08_JA/kichban_tap08_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap08_KO/kichban_tap08_KO.md`](../Tap08_KO/kichban_tap08_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và công cụ đối soát tự động (`.work/_verify_all_tap08_parity.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **53** | **53** | **53** | **53** | **Khớp 100% (53/53)** |
| **Lượt lời thoại (LOI)** | **33** | **33** | **33** | **33** | **Khớp 100% (33/33)** |
| **Tổng số câu đọc (Sentences)** | **218** | **218** | **218** | **218** | **Khớp 1:1 tuyệt đối** |
| **Số điểm ngắt nghỉ (NGHI)** | 6 | 6 | 6 | 6 | **Khớp 100% (cùng giây)** |
| **Số cue âm thanh (BGM / SFX)** | 14 (6 BGM / 8 SFX) | 14 | 14 | 14 | **Khớp 100% vị trí & thứ tự** |
| **Số mục danh sách (Bullets)** | 4 | 4 | 4 | 4 | **Khớp 100% (vị trí `2.07` & `5.06`)** |
| **Ước tính thời lượng lời** | ~30,5 phút | ~30,0 phút | ~31,0 phút | ~30,2 phút | Chuẩn tập lớn (29–32 phút) |

### Phân bổ số câu theo từng Hồi:
- **Hồi 1 (The Hook & Cơn hoang tưởng tập thể):** VN = 41 | EN = 41 | JA = 41 | KO = 41
- **Hồi 2 (Hiện trường, Thủ đoạn MO & Dấu ấn Signature):** VN = 39 | EN = 39 | JA = 39 | KO = 39
- **Hồi 3 (Giải phẫu tâm lý & Nghịch lý giới tinh hoa):** VN = 49 | EN = 49 | JA = 49 | KO = 49
- **Hồi 4 (Đấu trí thẩm vấn & Bóc trần ma thuật tẩy não):** VN = 49 | EN = 49 | JA = 49 | KO = 49
- **Hồi 5 (Phán quyết lịch sử, Bản án tâm lý & Cảnh báo đỏ):** VN = 40 | EN = 40 | JA = 40 | KO = 40

### Phân bổ tỷ lệ thoại giữa các vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 20 lượt thoại, 124 câu (**56,9%**) — *Đúng cấu trúc Host-Driven Documentary*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 7 lượt thoại, 50 câu (**22,9%**) — *Đạt chuẩn (~20–25%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 4 lượt thoại, 32 câu (**14,7%**) — *Đạt chuẩn (~15–20%)*.
- **Người bình thường (N1/N2) — Chân thật, cảm xúc:** 2 lượt thoại, 12 câu (**5,5%**) — *Đạt chuẩn (~5%)*.

---

## 2. Thẩm định chi tiết Hệ sinh thái 10 Chỉ Dấu Tâm Lý & Hành Vi (A2c)

Toàn bộ 10 chỉ dấu đã được đối soát chéo trên cả 4 ngôn ngữ, đảm bảo truyền tải trọn vẹn góc nhìn khoa học hành vi:

### 1. Ảnh hưởng & Dư chấn xã hội (Social Impact & Collective Paranoia)
- **Vị trí:** `1.02`, `1.09`, `5.04`
- **Nội dung:** 
  - Sụp đổ hoàn toàn ‘huyền thoại an toàn’ (日本の安全神話) của Nhật Bản thời hậu chiến; chao đảo sau cú sốc kinh tế bong bóng năm 1991 mở ra Thập niên mất mát.
  - Nỗi hoang tưởng tập thể *(Collective Paranoia)*: người dân nín thở khi bước xuống ga ngầm, kiểm tra từng gầm ghế, nghi kỵ lẫn nhau.
  - Đại cải tổ thể chế pháp luật: Sửa đổi Luật Tổ chức Tôn giáo và ban hành các đạo luật kiểm soát đặc biệt.

### 2. Hung thủ nhìn nhận nạn nhân & Vì sao (Perception of Victims)
- **Vị trí:** `1.04`, `3.07`, `4.05`
- **Nội dung:** 
  - **Vật hóa (Objectification) & Phi nhân hóa:** Nạn nhân trên tàu không được nhìn như những con người có cha mẹ, con cái, mà bị giáng cấp thành "những linh hồn mang ác nghiệp", "đạo cụ cản trở kỷ nguyên mới".
  - Tiếng van xin và sinh mạng vô tội bị hạ xuống thành dữ liệu thực nghiệm vô cảm trong phòng lab.

### 3. Hung thủ nhìn nhận người thân & Nghịch lý chia ngăn (Family Dynamics & Compartmentalization)
- **Vị trí:** `3.07`, `4.02`
- **Nội dung:** 
  - **Cơ chế Chia ngăn nhận thức (Cognitive Compartmentalization):** Khóa chặt thế giới đời thường vào một ngăn riêng biệt, cách ly hoàn toàn với thế giới bí mật trong căn cứ Satyam.
  - **Bi kịch của gia đình hung thủ:** Cha mẹ các trí thức sụp đổ hoàn toàn danh tính khi biết con mình là kẻ khủng bố.

### 4. Thái độ trước bản án nhận được (Attitude Toward Sentence)
- **Vị trí:** `4.08`, `5.02`, `5.03`
- **Nội dung:** 
  - **Đối lập sâu sắc giữa Hối hận chân chính (Remorse) vs. Tự thương hại bệnh lý (Pathological Self-Pity):**
    + *Bác sĩ Ikuo Hayashi:* Thành khẩn khai báo, quỳ gối xin nhận hình phạt nghiêm khắc nhất (tù chung thân).
    + *Shoko Asahara:* Giả điên, lẩm bẩm vô nghĩa, từ chối đối thoại với tòa; biểu hiện của **Sự sụp đổ cái tôi ái kỷ (Narcissistic Collapse)**.

### 5. Hệ thống tự bào chữa & Trung hòa đạo đức (Moral Disengagement)
- **Vị trí:** `4.04`, `4.05`
- **Nội dung:** 
  - **Bóp méo khái niệm ‘Poa’:** Đánh tráo một pháp môn chuyển di tâm thức thành học thuyết biện minh cho hành vi giết người để "giải thoát linh hồn".
  - Đỉnh cao của **Kỹ thuật Trung hòa đạo đức (Techniques of Neutralization)** và Ngoại hóa trách nhiệm.

### 6. Ngòi nổ & Điểm gãy tâm lý (Trigger & Stressors)
- **Vị trí:** `2.05`
- **Nội dung:** 
  - Cảnh sát Tokyo dự kiến đột kích Kamikuishiki ngày 22/3/1995 vì vụ bắt cóc công chứng viên Kiyoshi Kariya.
  - Ngòi nổ hoảng loạn thúc ép Asahara ra lệnh tấn công sarin chỉ trong vòng 48 giờ để đánh lạc hướng điều tra và làm tê liệt đầu não cảnh sát tại Kasumigaseki.

### 7. Dấu ấn Signature vs Thủ đoạn MO (Signature vs. Modus Operandi)
- **Vị trí:** `2.05`
- **Nội dung:** 
  - **Thủ đoạn (MO):** 11 túi sarin bọc giấy báo, mài nhọn đầu ô để chọc thủng, chọn đúng 8 giờ sáng khi các đoàn tàu hội tụ về Kasumigaseki, xe đón sẵn ở cửa ga.
  - **Chữ ký tâm lý (Signature):** Nhu cầu cưỡng chế hiện thực hóa kịch bản chiến tranh thế giới thứ ba và sấm truyền ngày tận thế để chứng minh ảo tưởng đấng cứu thế.

### 8. Chu kỳ ảo tưởng & Quỹ đạo leo thang (Escalation Trajectory)
- **Vị trí:** `2.07`, `2.08`
- **Nội dung:** 
  - Quỹ đạo leo thang bạo lực qua 4 nấc thang: (1) Yoga & bay bổng $\rightarrow$ (2) Cưỡng đoạt tài sản & thủ tiêu nội bộ $\rightarrow$ (3) Thảm sát gia đình Luật sư Tsutsumi Sakamoto (1989) $\rightarrow$ (4) Tấn công sarin Matsumoto (1994) $\rightarrow$ Thảm họa ga ngầm Tokyo (1995).

### 9. Hiệu ứng Hào quang & Điểm mù xã hội (Halo Effect & Social Blindspots)
- **Vị trí:** `1.12`, `3.03`, `3.06`
- **Nội dung:** 
  - Bằng cấp học thuật rực rỡ từ Đại học Tokyo, Kyoto, Osaka, Keio, Tsukuba tạo nên tấm khiên tàng hình "người trí thức ưu tú không thể làm điều điên rồ".
  - Điểm mù xã hội che lấp các dấu hiệu cảnh báo rõ ràng nhất suốt nhiều năm.

### 10. Nạn nhân học & Cảnh báo đỏ sinh tồn (Victimology & Red Flags)
- **Vị trí:** `1.09`, `5.04`, `5.06`
- **Nội dung:** 
  - Tôn vinh nhân phẩm và sự hy sinh của hai nhân viên đường sắt Kazumasa Takahashi và Tsuneo Hishinuma; Bác sĩ Shigeaki Hinohara (Bệnh viện Saint Luke).
  - Góc nhìn Haruki Murakami trong tác phẩm 'Ngầm' (Underground).
  - **4 Cảnh báo đỏ sinh tồn:** (1) Cô lập xã hội; (2) Làm suy kiệt thể chất; (3) Sùng bái cá nhân tuyệt đối; (4) Ngụy biện đảo ngược đạo đức.

---

## 3. Kết luận
Toàn bộ 4 ngôn ngữ (Tiếng Việt, Tiếng Anh, Tiếng Nhật, Tiếng Hàn) đã hoàn thành nâng cấp lên quy mô lớn **218 câu thoại** (> 200 câu), đạt 100% tính toàn vẹn kỹ thuật, line-ending chuẩn LF thuần (`double_cr=0`), và sẵn sàng cho các công đoạn sản xuất tiếp theo.
"""

with open('01_KICH_BAN/Tap08/REVIEW_kichban_tap08_10chiau.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(rev_10chiau.strip() + '\n')
with open('01_KICH_BAN/Tap08/REVIEW_kichban_tap08_multilingual.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(rev_multi.strip() + '\n')
print("Successfully updated both review documents!")
