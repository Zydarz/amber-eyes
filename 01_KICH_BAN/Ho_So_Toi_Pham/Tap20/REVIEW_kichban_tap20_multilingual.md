# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 20 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Khoảnh Khắc Sụp Đổ Trước Ống Kính — Ám Ảnh Rình Rập & Phản Ứng Đóng Băng Kỳ Dị (Hồ Sơ Stephen McDaniel — 2011)  
> **Thời điểm thẩm định:** 14/11/2026 (Bản nâng cấp kịch bản quy mô lớn 241 câu theo tiêu chuẩn mới, bổ sung phân tích tâm lý 5 chủ thể)  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118, #119).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Ho_So_Toi_Pham/Tap20/kichban_tap20_23102026.md`](kichban_tap20_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Ho_So_Toi_Pham/Tap20_EN/kichban_tap20_EN.md`](../Tap20_EN/kichban_tap20_EN.md) (và bản sao [`01_KICH_BAN/Ho_So_Toi_Pham/Tap20/kichban_tap20_EN.md`](kichban_tap20_EN.md))  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Ho_So_Toi_Pham/Tap20_JA/kichban_tap20_JA.md`](../Tap20_JA/kichban_tap20_JA.md) (và bản sao [`01_KICH_BAN/Ho_So_Toi_Pham/Tap20/kichban_tap20_JA.md`](kichban_tap20_JA.md))  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Ho_So_Toi_Pham/Tap20_KO/kichban_tap20_KO.md`](../Tap20_KO/kichban_tap20_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và bộ công cụ kiểm thử QC tự động (`.work/_qc_all_4scripts_tap20.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **51** | **51** | **51** | **51** | **Khớp 100% (51/51)** |
| **Lượt lời thoại (LOI)** | **32** | **32** | **32** | **32** | **Khớp 100% (32/32)** |
| **Tổng số câu đọc (Sentences)** | **241** | **241** | **241** | **241** | **Khớp 1:1 tuyệt đối** |
| **Số cue âm thanh (BGM / SFX)** | 19 (7 BGM / 12 SFX) | 19 | 19 | 19 | **Khớp 100% vị trí & thứ tự** |
| **Tổng số từ (Word count)** | 7.208 từ | 4.749 từ | 241 đoạn | 3.829 từ | Chuẩn tự nhiên từng ngữ |
| **Lỗi định dạng dòng (CR thừa)** | 0 (`\r\r\n` = 0) | 0 | 0 | 0 | Tuân thủ Bẫy #119 |
| **Lỗi từ cấm bạo lực (V9)** | 0 lỗi | 0 lỗi | 0 lỗi | 0 lỗi | 100% YouTube Safe |
| **Lỗi dấu ngắt lửng (G1)** | 0 dấu `...`/`…` | 0 | 0 | 0 | Giọng đọc mượt mà |
| **Ước tính thời lượng lời** | ~28,5 phút | ~28,0 phút | ~29,0 phút | ~28,2 phút | Chuẩn tập lớn (27–31 phút) |

### Phân bổ số câu theo từng Hồi (Đồng bộ 100% cả 4 ngôn ngữ):
- **Hồi 1 (The Hook & Phát hiện định mệnh trên sóng truyền hình):** VN = 55 | EN = 55 | JA = 55 | KO = 55
- **Hồi 2 (Bức tượng đá trong phòng hỏi cung & Chứng cứ vật chất):** VN = 47 | EN = 47 | JA = 47 | KO = 47
- **Hồi 3 (Giải phẫu tâm lý: Kẻ rình rập ngầm & Phản ứng đóng băng):** VN = 49 | EN = 49 | JA = 49 | KO = 49
- **Hồi 4 (Phiên tòa phán quyết, Lời thú tội & Bản án chung thân):** VN = 54 | EN = 54 | JA = 54 | KO = 54
- **Hồi 5 (Bài học cảnh tỉnh, Cải cách thể chế & 4 Cảnh báo đỏ):** VN = 36 | EN = 36 | JA = 36 | KO = 36
- **TỔNG CỘNG:** **241 câu** (Mỗi ngôn ngữ khớp từng câu, từng nhân vật và từng cue âm thanh).

### Phân bổ tỷ lệ thoại giữa các vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 19 lượt thoại, 132 câu (**54,8%**) — *Đúng chuẩn Host-Driven Documentary (~55%)*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 6 lượt thoại, 43 câu (**17,8%**) — *Đạt chuẩn (~15–20%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 5 lượt thoại, 42 câu (**17,4%**) — *Đạt chuẩn (~15–20%)*.
- **Người bình thường (N1/N2) — Chân thật, cảm xúc:** 2 lượt thoại, 19 câu (**7,9%**) — *N1 (Bạn học): 10 câu (`1.07`), N2 (Đại diện gia đình): 9 câu (`4.09`)*.

---

## 2. Thẩm định chi tiết Hệ sinh thái 10 Chỉ Dấu Tâm Lý & Hành Vi (A2c)

Toàn bộ 10 chỉ dấu đã được đối soát chéo trên cả 4 ngôn ngữ, đảm bảo truyền tải trọn vẹn góc nhìn khoa học hành vi:

### 1. Ảnh hưởng & Dư chấn xã hội (Social Impact & Collective Paranoia)
- **Vị trí:** `1.02`, `1.04`, `5.02`
- **Nội dung:** 
  - Nỗi hoang tưởng tập thể tại Trường Luật Mercer: các cử nhân luật am hiểu trật tự pháp lý hoang mang tột độ, khóa chặt chốt cửa trong đêm hè oi ả và nghi kỵ lẫn nhau.
  - Đại cải cách thể chế: Quy chuẩn an toàn cư trú sinh viên trên toàn nước Mỹ được siết chặt tối đa (quản lý chìa khóa vạn năng, kiểm tra lý lịch nhân sự bảo trì, mạng lưới camera an ninh).

### 2. Hung thủ nhìn nhận nạn nhân & Vì sao (Perception of Victims)
- **Vị trí:** `2.08`, `3.03`
- **Nội dung:** 
  - **Vật hóa (Objectification) & Phi nhân hóa:** Lauren không được nhìn nhận như con người có tri giác và hoài bão, mà bị giáng cấp thành "đạo cụ" cung cấp sự thỏa mãn ái kỷ.
  - **Lý do gốc rễ:** Khuyết tật Thuyết tâm trí (Theory of Mind) và sự thiếu hụt thấu cảm cảm xúc (Affective Empathy Deficit). Hành vi thị dâm săn mồi (Predatory Voyeurism) quay lén qua cửa sổ nhằm tìm kiếm sự kích thích quyền lực.

### 3. Hung thủ nhìn nhận người thân & Nghịch lý chia ngăn (Compartmentalization)
- **Vị trí:** `3.07`, `4.08`, `4.09`
- **Nội dung:** 
  - **Chia ngăn nhận thức:** Một ngăn là sinh viên luật cần mẫn ôn thi luật sư; một ngăn bóng tối là kẻ rình rập săn mồi ban đêm.
  - **Mặc cảm người ngoài cuộc (Bystander Guilt):** Sự giằng xé tự trách của bạn bè cùng trường luật khi không kịp thời tin vào trực giác của nạn nhân.

### 4. Thái độ trước bản án & Cơ chế hối hận (Remorse & Narcissistic Collapse)
- **Vị trí:** `4.04`, `4.06`, `4.11`
- **Nội dung:** 
  - **TRỌNG TÂM — Ăn năn chân chính vs. Tự thương hại bệnh lý (Pathological Self-Pity):** McDaniel không hề bộc lộ sự hối hận vì sinh mạng đã tước đoạt; ánh mắt đờ đẫn là biểu hiện của Sự sụp đổ cái tôi ái kỷ khi nhận ra toàn bộ tương lai đã tan tành.
  - **Hối hận công cụ (Instrumental Remorse):** Thỏa thuận nhận tội xuất phát từ sự tính toán sinh tồn hèn nhát để đổi lấy việc thoát án tử hình, chứ không phải thức tỉnh lương tri.

### 5. Hệ thống tự bào chữa & Trung hòa đạo đức (Techniques of Neutralization)
- **Vị trí:** `3.07`
- **Nội dung:** Đóng vai nạn nhân bị xã hội hắt hủi, đổ lỗi cho phụ nữ cự tuyệt, tự biện minh rằng trí tuệ vượt trội cho phép hắn đứng trên chuẩn mực đạo đức.

### 6. Ngòi nổ & Điểm gãy tâm lý (Trigger & Narcissistic Injury)
- **Vị trí:** `3.04`, `3.05`
- **Nội dung:** Lauren tốt nghiệp và đóng thùng chuyển đi Atlanta; khoảng cách địa lý báo trước việc tước đoạt vĩnh viễn cơ hội quan sát bí mật; cơn tổn thương ái kỷ dữ dội đánh sập chốt chặn ức chế đạo đức cuối cùng.

### 7. Dấu ấn Signature vs Thủ đoạn MO (Signature vs. Modus Operandi)
- **Vị trí:** `2.06`, `2.08`, `2.09`
- **Nội dung:** 
  - **MO:** Lợi dụng lỗ hổng quản lý trộm chìa khóa vạn năng, đột nhập lúc 4:30 sáng khi nạn nhân ngủ say, tính toán phi tang vào thùng rác trước giờ xe thu gom.
  - **Signature:** Rình rập quay lén nhiều tháng từ ban công, lưu trữ dữ liệu số làm chiến lợi phẩm bệnh lý (cơn nghiện ảo tưởng kiểm soát bất biến).

### 8. Chu kỳ ảo tưởng & Quỹ đạo leo thang (Tolerance Buildup & Escalation)
- **Vị trí:** `2.10`
- **Nội dung:** Nâng ngưỡng liều kiểm soát: từ rình mò qua cửa sổ $\rightarrow$ tìm kiếm kỹ thuật bẻ khóa $\rightarrow$ quay video đêm qua ban công $\rightarrow$ dùng chìa khóa vạn năng đột nhập khi nạn nhân ngủ.

### 9. Hiệu ứng Hào quang & Điểm mù xã hội (Halo Effect & Normalcy Bias)
- **Vị trí:** `1.02`, `1.04`
- **Nội dung:** Vỏ bọc sinh viên trường luật nhút nhát, lập dị vô hại tạo nên tấm khiên che mắt xã hội hoàn hảo, khiến bạn bè và cộng đồng xung quanh hoàn toàn mất cảnh giác.

### 10. Nạn nhân học & Cảnh báo đỏ sinh tồn (Victimology & The Gift of Fear)
- **Vị trí:** `1.07`, `4.09`, `5.04`, `5.05`
- **Nội dung:** Tôn vinh nhân phẩm và hoài bão của Lauren Giddings; bài học trực giác sợ hãi là tín hiệu tiến hóa báo trước nguy hiểm; 4 dấu hiệu cảnh báo đỏ kinh điển phòng ngừa kẻ rình rập ngầm.

---

## 3. Kết luận thẩm định
* Toàn bộ 4 ngôn ngữ (VN, EN, JA, KO) đạt chuẩn **100% GREEN (PASS)** theo kiểm định tự động `_qc_all_4scripts_tap20.py`.
* Cấu trúc 51 phần tử và 32 lượt lời thoại được giữ nguyên vẹn; dung lượng mở rộng đạt **241 câu thoại**, hoàn thành trọn vẹn yêu cầu nghiên cứu và bổ sung kịch bản đa ngôn ngữ cho Tập 20.
