# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 20 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Khoảnh Khắc Sụp Đổ Trước Ống Kính — Ám Ảnh Rình Rập & Phản Ứng Đóng Băng Kỳ Dị (Hồ Sơ Stephen McDaniel — 2011)  
> **Thời điểm thẩm định:** 07/11/2026 (Bản nâng cấp kịch bản quy mô lớn > 200 câu theo tiêu chuẩn mới)  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118, #119).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap20/kichban_tap20_23102026.md`](kichban_tap20_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap20_EN/kichban_tap20_EN.md`](../Tap20_EN/kichban_tap20_EN.md) (và bản sao [`01_KICH_BAN/Tap20/kichban_tap20_EN.md`](kichban_tap20_EN.md))  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap20_JA/kichban_tap20_JA.md`](../Tap20_JA/kichban_tap20_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap20_KO/kichban_tap20_KO.md`](../Tap20_KO/kichban_tap20_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và bộ công cụ kiểm thử QC tự động (`.work/_qc_all_4scripts_tap20.py` & `.work/_qc_ko_parity.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **51** | **51** | **51** | **51** | **Khớp 100% (51/51)** |
| **Lượt lời thoại (LOI)** | **32** | **32** | **32** | **32** | **Khớp 100% (32/32)** |
| **Tổng số câu đọc (Sentences)** | **212** | **212** | **212** | **212** | **Khớp 1:1 tuyệt đối** |
| **Số cue âm thanh (BGM / SFX)** | 19 (7 BGM / 12 SFX) | 19 | 19 | 19 | **Khớp 100% vị trí & thứ tự** |
| **Tổng số từ (Word count)** | 6.260 từ | 4.169 từ | 212 đoạn | 3.362 từ | Chuẩn tự nhiên từng ngữ |
| **Lỗi định dạng dòng (CR thừa)** | 0 (`\r\r\n` = 0) | 0 | 0 | 0 | Tuân thủ Bẫy #119 |
| **Lỗi từ cấm bạo lực (V9)** | 0 lỗi | 0 lỗi | 0 lỗi | 0 lỗi | 100% YouTube Safe |
| **Lỗi dấu ngắt lửng (G1)** | 0 dấu `...`/`…` | 0 | 0 | 0 | Giọng đọc mượt mà |
| **Ước tính thời lượng lời** | ~25,5 phút | ~25,0 phút | ~26,0 phút | ~25,2 phút | Chuẩn tập lớn (24–27 phút) |

### Phân bổ số câu theo từng Hồi:
- **Hồi 1 (The Hook & Phát hiện định mệnh trên sóng truyền hình):** VN = 50 | EN = 50 | JA = 50 | KO = 50
- **Hồi 2 (Bức tượng đá trong phòng hỏi cung & Chứng cứ vật chất):** VN = 41 | EN = 41 | JA = 41 | KO = 41
- **Hồi 3 (Giải phẫu tâm lý: Kẻ rình rập ngầm & Phản ứng đóng băng):** VN = 43 | EN = 43 | JA = 43 | KO = 43
- **Hồi 4 (Phiên tòa phán quyết, Lời thú tội & Bản án chung thân):** VN = 47 | EN = 47 | JA = 47 | KO = 47
- **Hồi 5 (Bài học cảnh tỉnh, Cải cách thể chế & 4 Cảnh báo đỏ):** VN = 31 | EN = 31 | JA = 31 | KO = 31

### Phân bổ tỷ lệ thoại giữa các vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 19 lượt thoại, 122 câu (**57,5%**) — *Đúng chuẩn Host-Driven Documentary (~55–60%)*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 6 lượt thoại, 37 câu (**17,5%**) — *Đạt chuẩn (~15–20%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 5 lượt thoại, 36 câu (**17,0%**) — *Đạt chuẩn (~15–20%)*.
- **Người bình thường (N1/N2) — Chân thật, cảm xúc:** 2 lượt thoại, 17 câu (**8,0%**) — *N1 (Bạn học): 8 câu (`1.07`), N2 (Đại diện gia đình): 9 câu (`4.09`)*.

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
  - Khuyết tật thấu cảm cảm xúc (Affective Empathy Deficit) và Thuyết tâm trí (Theory of Mind). Hành vi thị dâm săn mồi (Predatory Voyeurism) kích hoạt sự hưng phấn quyền lực (power arousal).

### 3. Hung thủ nhìn nhận người thân & Nghịch lý chia ngăn (Family Dynamics & Compartmentalization)
- **Vị trí:** `3.07`, `4.08`, `4.09`
- **Nội dung:** 
  - **Cơ chế Chia ngăn nhận thức (Cognitive Compartmentalization):** Bộ não McDaniel vận hành hai thế giới riêng biệt: một ngăn sinh viên luật cần mẫn ôn thi luật sư; một ngăn bóng tối là kẻ rình rập săn mồi ban đêm.
  - Bi kịch sụp đổ niềm tin của bạn bè trường luật và gia đình nạn nhân trước sự trơ tráo của kẻ thủ ác.

### 4. Thái độ trước bản án nhận được (Attitude Toward Sentence)
- **Vị trí:** `4.04`, `4.11`
- **Nội dung:** 
  - **Đối lập giữa Hối hận chân chính vs. Tự thương hại bệnh lý (Pathological Self-Pity):** McDaniel không hề khóc vì xót thương nạn nhân; ánh mắt đờ đẫn là biểu hiện của **Sự sụp đổ cái tôi ái kỷ (Narcissistic Collapse)** khi nhận ra toàn bộ tương lai và danh vọng cá nhân đã tan tành.
  - Ký thỏa thuận nhận tội vì toan tính hèn nhát để tránh án tử hình.

### 5. Hệ thống tự bào chữa & Trung hòa đạo đức (Moral Disengagement)
- **Vị trí:** `3.07`
- **Nội dung:** 
  - Kỹ thuật trung hòa đạo đức (Techniques of Neutralization): Đóng vai nạn nhân bị xã hội ruồng bỏ, đổ lỗi cho sự cự tuyệt của phụ nữ, tự cho mình quyền trừng phạt người từ chối mình.

### 6. Ngòi nổ & Điểm gãy tâm lý (Trigger & Stressors)
- **Vị trí:** `3.04`, `3.05`
- **Nội dung:** 
  - **Biến cố kích hoạt (Precipitating Stressor):** Lauren tốt nghiệp xuất sắc và chuẩn bị chuyển về Atlanta. Các thùng các-tông đóng gói đồ đạc báo trước khoảng cách địa lý sẽ tước đoạt vĩnh viễn quyền kiểm soát ngầm của hắn.
  - Nỗi sợ mất quyền kiểm soát gây ra tổn thương ái kỷ dữ dội (Narcissistic Injury), kích hoạt quyết định đột nhập và tước đoạt sinh mạng.

### 7. Dấu ấn Signature vs Thủ đoạn MO (Signature vs. Modus Operandi)
- **Vị trí:** `2.08`, `2.09`
- **Nội dung:** 
  - **Thủ đoạn (MO):** Trộm chìa khóa vạn năng của ban quản lý, đột nhập lúc 4:30 sáng khi nạn nhân ngủ say, tính toán phi tang vào thùng rác trước giờ xe thu gom đến.
  - **Chữ ký tâm lý (Signature):** Rình rập quay lén nhiều tháng từ ban công, theo dõi nạn nhân trong phòng ngủ, lưu trữ dữ liệu số làm chiến lợi phẩm bệnh lý (nhu cầu thỏa mãn cảm xúc bệnh hoạn bất biến).

### 8. Chu kỳ ảo tưởng & Quỹ đạo leo thang (Escalation Trajectory)
- **Vị trí:** `2.10`
- **Nội dung:** 
  - Cơ chế dung nạp kích thích (Tolerance Buildup): Từ rình mò qua cửa sổ $\rightarrow$ tìm kiếm kỹ thuật bẻ khóa $\rightarrow$ quay video đêm qua ban công $\rightarrow$ đột nhập bằng chìa khóa vạn năng khi nạn nhân ngủ.

### 9. Hiệu ứng Hào quang & Điểm mù xã hội (Halo Effect & Social Blindspots)
- **Vị trí:** `1.04`
- **Nội dung:** 
  - Vỏ bọc sinh viên trường luật lập dị, nhút nhát, chỉ biết vùi đầu vào sách vở ("người bạn kỳ quặc vô hại") tạo nên tấm khiên che mắt xã hội hoàn hảo (Normalcy Bias), khiến cộng đồng xung quanh hoàn toàn mất cảnh giác.

### 10. Nạn nhân học & Cảnh báo đỏ sinh tồn (Victimology & Survival Red Flags)
- **Vị trí:** `1.07`, `4.09`, `5.04`, `5.05`
- **Nội dung:** 
  - Tôn vinh phẩm giá, tài năng và lòng nhân ái của Lauren Giddings (thủ lĩnh sinh viên ưu tú, nụ cười rạng rỡ, tương lai rộng mở); tuyệt đối không đổ lỗi nạn nhân.
  - Bài học sinh tồn từ nguyên lý *The Gift of Fear* của Gavin de Becker: Trực giác sinh tồn là radar cảnh báo chính xác nhất; 4 dấu hiệu cảnh báo đỏ kinh điển giúp nhận diện và phòng ngừa kẻ rình rập ngầm từ sớm.

---

## 3. Kết quả các cổng kiểm thử tự động

1. **Kiểm tra Parity chéo 1:1 (`.work/_qc_all_4scripts_tap20.py`):**
   - VN vs EN: **PASS (100% matched across 51 elements, 32 turns, 212 sentences)**
   - VN vs JA: **PASS (100% matched across 51 elements, 32 turns, 212 sentences)**
   - VN vs KO: **PASS (100% matched across 51 elements, 32 turns, 212 sentences)**
2. **Kiểm tra cổng tiếng Hàn khắt khe (`.work/_qc_ko_parity.py`):**
   - `51 elements aligned (kind/role/sentence-count/pause)`: **PASS**
   - `total sentences: 212`: **PASS**
   - `hangul share of narration: 92.6%`: **PASS**
   - `no vietnamese-only diacritics`: **PASS**
   - `no hanja/chinese characters`: **PASS**
   - `Exit code 0 — PASS kichban_tap20_KO.md`: **PASS**
3. **Kiểm tra tính an toàn nội dung (Rule V9):**
   - `0 forbidden word hits` trên toàn bộ 4 ngôn ngữ.
4. **Kiểm tra giọng đọc mượt mà (Rule G1):**
   - `0 ellipsis hits` (`...` và `…` = 0) trên toàn bộ 4 ngôn ngữ.
5. **Kiểm tra mã liên kết trong pipeline (`.work/edition.py`):**
   - `summary` keys `1.02#1` và `3.02#1`: **Tồn tại 100%** trong script.
   - `n_element` (`1.07`: N1, `4.09`: N2): **Khớp 100%**.
   - `act1_cue` (`1.10`), `silence_cue` (`1.06`), `click_cues` (`1.03`, `4.05`): **Khớp 100%**.

---

## 4. Kết luận
Kịch bản Tập 20 đã được tái cấu trúc thành công vượt bậc:
- **Đạt quy mô lớn 212 câu thoại** (> 200 câu), đáp ứng hoàn hảo yêu cầu của người dùng và chuẩn mực các tập lớn (T02: 203 câu, T08: 218 câu, T10: 208 câu).
- **Hoàn thành trọn vẹn trên cả 4 ngôn ngữ (VN, EN, JA, KO)** với độ chuẩn xác và tương thích Parity 1:1 tuyệt đối.
- **Tích hợp sâu sắc toàn diện Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c)**, biến vụ án thành một ca giải phẫu tâm lý học pháp y mẫu mực.
- **Sẵn sàng 100%** cho các bước diễn xuất và sản xuất âm thanh/hình ảnh tiếp theo.
