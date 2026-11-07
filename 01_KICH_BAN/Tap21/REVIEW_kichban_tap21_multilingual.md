# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 21 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Hồ Sơ Andrea Yates — Bi Kịch Của Cơn Loạn Thần Sau Sinh & Khi Ảo Giác Đánh Cắp Thiên Chức Làm Mẹ (Houston, Texas, 2001)  
> **Thời điểm thẩm định:** 07/11/2026 (Bản nâng cấp kịch bản quy mô lớn > 200 câu theo tiêu chuẩn mới)  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118, #119).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap21/kichban_tap21_23102026.md`](kichban_tap21_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap21_EN/kichban_tap21_EN.md`](../Tap21_EN/kichban_tap21_EN.md) (và bản sao [`01_KICH_BAN/Tap21/kichban_tap21_EN.md`](kichban_tap21_EN.md))  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap21_JA/kichban_tap21_JA.md`](../Tap21_JA/kichban_tap21_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap21_KO/kichban_tap21_KO.md`](../Tap21_KO/kichban_tap21_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và bộ công cụ kiểm thử QC tự động (`.work/_qc_all_4scripts_tap21.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **51** | **51** | **51** | **51** | **Khớp 100% (51/51)** |
| **Lượt lời thoại (LOI)** | **32** | **32** | **32** | **32** | **Khớp 100% (32/32)** |
| **Tổng số câu đọc (Sentences)** | **212** | **212** | **212** | **212** | **Khớp 1:1 tuyệt đối** |
| **Số cue âm thanh (BGM / SFX)** | 19 (7 BGM / 12 SFX) | 19 | 19 | 19 | **Khớp 100% vị trí & thứ tự** |
| **Tổng số từ (Word count)** | 6.538 từ | 3.982 từ | 212 đoạn | 3.198 từ | Chuẩn tự nhiên từng ngữ |
| **Lỗi định dạng dòng (CR thừa)** | 0 (`\r\r\n` = 0) | 0 | 0 | 0 | Tuân thủ Bẫy #119 |
| **Lỗi từ cấm bạo lực (V9)** | 0 lỗi | 0 lỗi | 0 lỗi | 0 lỗi | 100% YouTube Safe |
| **Lỗi dấu ngắt lửng (G1)** | 0 dấu `...`/`…` | 0 | 0 | 0 | Giọng đọc mượt mà |
| **Ước tính thời lượng lời** | ~25,5 phút | ~25,0 phút | ~26,0 phút | ~25,2 phút | Chuẩn tập lớn (24–27 phút) |

### Phân bổ số câu theo từng Hồi:
- **Hồi 1 (Cuộc gọi 911 rạng sáng & Ngôi nhà im lìm tại Houston):** VN = 50 | EN = 50 | JA = 50 | KO = 50
- **Hồi 2 (Vực thẳm của sự cô độc & Tiếng chuông cảnh báo bị phớt lờ):** VN = 41 | EN = 41 | JA = 41 | KO = 41
- **Hồi 3 (Giải mã tâm lý: Loạn thần sau sinh & Hoang tưởng cứu chuộc):** VN = 43 | EN = 43 | JA = 43 | KO = 43
- **Hồi 4 (Phiên tòa lịch sử & Phán quyết Không có tội vì lý do tâm thần):** VN = 47 | EN = 47 | JA = 47 | KO = 47
- **Hồi 5 (Bài học cảnh tỉnh & 4 Cảnh báo đỏ nhận diện Loạn thần sau sinh):** VN = 31 | EN = 31 | JA = 31 | KO = 31

### Phân bổ tỷ lệ thoại giữa các vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 19 lượt thoại, 122 câu (**57,5%**) — *Đúng chuẩn Host-Driven Documentary (~55–60%)*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 6 lượt thoại, 37 câu (**17,5%**) — *Đạt chuẩn (~15–20%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 5 lượt thoại, 36 câu (**17,0%**) — *Đạt chuẩn (~15–20%)*.
- **Người bình thường (N1/N2) — Chân thật, cảm xúc:** 2 lượt thoại, 17 câu (**8,0%**) — *N1 (Hàng xóm): 8 câu (`1.07`), N2 (Bồi thẩm viên): 9 câu (`4.09`)*.

---

## 2. Thẩm định chi tiết Hệ sinh thái 10 Chỉ Dấu Tâm Lý & Hành Vi (A2c)

Toàn bộ 10 chỉ dấu đã được đối soát chéo trên cả 4 ngôn ngữ, đảm bảo truyền tải trọn vẹn góc nhìn khoa học hành vi:

### 1. Ảnh hưởng & Dư chấn xã hội (Social Impact & Collective Shock)
- **Vị trí:** `1.02`, `1.06`, `5.02`
- **Nội dung:** 
  - Vụ án làm rung chuyển toàn bộ nước Mỹ, đặt ra câu hỏi về ranh giới giữa bệnh tâm thần hiểm nghèo và tội ác cố ý.
  - Đại cải cách thể chế trong y tế: Đưa việc sàng lọc sức khỏe tâm thần sau sinh vào quy trình chuẩn của các bệnh viện phụ sản toàn cầu; thành lập Quỹ Tưởng niệm Trẻ em Yates.

### 2. Hung thủ nhìn nhận nạn nhân & Vì sao (Altruistic Filicide & Delusions of Salvation)
- **Vị trí:** `1.10`, `3.03`, `3.04`
- **Nội dung:** 
  - Hung thủ yêu thương các con tha thiết, không có động cơ thù hận hay tư lợi.
  - Dưới tác động của cơn loạn thần nặng và niềm tin tôn giáo cực đoan, hung thủ tin rằng các con bị quỷ Satan ám và việc kết thúc sinh mạng trần thế là con đường duy nhất để cứu rỗi linh hồn chúng lên thiên đàng cùng Chúa.

### 3. Hung thủ nhìn nhận người thân & Nghịch lý chia ngăn (Family Dynamics & Compartmentalization)
- **Vị trí:** `2.04`, `2.06`, `2.09`
- **Nội dung:** 
  - Sự cô lập và áp lực gia đình đông con: sống trong xe buýt 35 mét vuông, gánh vác việc tự dạy học cho 5 con nhỏ.
  - Sự xem nhẹ các khuyến cáo y khoa nghiêm khắc của gia đình và người chồng, dẫn đến việc tiếp tục mang thai khi hệ thần kinh chưa kịp hồi phục.

### 4. Thái độ trước bản án nhận được (Attitude Toward Sentence & Moral Awakening)
- **Vị trí:** `3.07`, `4.08`, `4.10`
- **Nội dung:** 
  - Khi thuốc chống loạn thần phát huy tác dụng trong bệnh viện, lớp sương mù hoang tưởng tan biến, thực tại đau lòng ập xuống khiến Andrea rơi vào sự giằng xé lương tâm khôn nguôi.
  - Tự nguyện từ chối các phiên điều trần xin phóng thích định kỳ, lựa chọn sống trọn phần đời còn lại trong Bệnh viện Bang Kerrville để đối diện với nỗi đau của chính mình.

### 5. Hệ thống tự bào chữa & Trung hòa đạo đức (Moral Disengagement & The M'Naghten Rule)
- **Vị trí:** `1.10`, `3.05`
- **Nội dung:** 
  - Phân định giữa nhận thức pháp lý bề mặt với niềm tin đạo đức bên trong theo Quy tắc M'Naghten.
  - Trong thế giới hoang tưởng, việc cứu linh hồn các con là mệnh lệnh thiêng liêng cao hơn luật pháp loài người; Andrea sẵn sàng đón nhận án tử hình để tiêu diệt con quỷ trong thể xác mình.

### 6. Ngòi nổ & Điểm gãy tâm lý (Trigger & Precipitating Stressors)
- **Vị trí:** `2.06`, `2.08`, `2.09`
- **Nội dung:** 
  - Sinh 5 con liên tiếp trong 5 năm; cái chết đột ngột của người cha ruột đầu năm 2001; bác sĩ mới cắt thuốc chống loạn thần Haldol 2 tuần trước thảm kịch.
  - "Khoảng trống định mệnh một giờ" khi người chồng đi làm và người mẹ chồng chưa kịp đến, tạo cơ hội cho cơn loạn thần bùng phát hoàn toàn.

### 7. Dấu ấn Signature vs Thủ đoạn MO (Signature vs. Modus Operandi)
- **Vị trí:** `1.04`, `1.10`, `2.09`
- **Nội dung:** 
  - **Thủ đoạn (MO):** Tận dụng khoảng thời gian 60 phút ở nhà một mình; chủ động gọi 911 và gọi chồng về ngay sau khi sự việc xảy ra.
  - **Chữ ký tâm lý (Signature):** Sự tĩnh lặng kỳ dị, không trốn chạy hay che giấu dấu vết; lập tức nhận trách nhiệm và giải thích động cơ cứu rỗi các con.

### 8. Chu kỳ ảo tưởng & Quỹ đạo leo thang (Psychotic Escalation Trajectory)
- **Vị trí:** `2.04`, `2.06`, `2.08`
- **Nội dung:** 
  - Từ trầm cảm sau sinh (PPD) năm 1999 $\rightarrow$ xuất hiện ảo thanh và hai lần toan tự hại $\rightarrow$ nhập viện điều trị $\rightarrow$ tái mang thai đứa con thứ năm $\rightarrow$ mất điểm tựa gia đình $\rightarrow$ bùng phát loạn thần cấp tính (Postpartum Psychosis).

### 9. Hiệu ứng Hào quang & Điểm mù xã hội (Halo Effect & Normalcy Bias)
- **Vị trí:** `1.07`, `2.04`
- **Nội dung:** 
  - Từng là thủ khoa trung học, y tá gương mẫu tại Trung tâm Ung bướu MD Anderson; gia đình ngoan đạo mẫu mực.
  - Vỏ bọc người mẹ hoàn hảo tạo ra điểm mù xã hội lớn, khiến cộng đồng không nhận ra vực thẳm tâm thần bên trong.

### 10. Nạn nhân học & Cảnh báo đỏ sinh tồn (Victimology & Survival Red Flags)
- **Vị trí:** `1.04`, `4.09`, `5.04`, `5.05`
- **Nội dung:** 
  - Tôn vinh nhân phẩm và sự trong sáng của 5 đứa trẻ vô tội (Noah, John, Paul, Luke, Mary).
  - 4 Cảnh báo đỏ kinh điển nhận diện Loạn thần sau sinh (PPP):
    1. Thay đổi hành vi đột ngột, ánh mắt thất thần, mất kết nối thực tại (Catatonia / Dissociation).
    2. Xuất hiện các ý nghĩ hoang tưởng kỳ quái, sợ con bị quỷ ám hoặc tin mình bị nguyền rủa.
    3. Ảo thanh ra lệnh hoặc ảo giác giác quan bên tai.
    4. Mất ngủ triền miên nhiều ngày kết hợp kiệt quệ cảm xúc hoặc kích động tâm thần vận động.
