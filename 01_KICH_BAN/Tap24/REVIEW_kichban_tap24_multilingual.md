# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 24 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Ký Ức Kẻ Sát Nhân Hwaseong — Sự Thật 33 Năm Dưới Lớp Sương Mù & Lời Thú Tội Muộn Màng (Hồ Sơ Lee Choon-jae & Kỳ Án Oan Yoon Sung-yeo)  
> **Thời điểm thẩm định:** 07/11/2026 (Bản nâng cấp kịch bản quy mô lớn > 200 câu)  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap24/kichban_tap24_23102026.md`](kichban_tap24_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap24_EN/kichban_tap24_EN.md`](../Tap24_EN/kichban_tap24_EN.md)  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap24_JA/kichban_tap24_JA.md`](../Tap24_JA/kichban_tap24_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap24_KO/kichban_tap24_KO.md`](../Tap24_KO/kichban_tap24_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`), công cụ đối soát tự động (`.work/_verify_all_tap24_parity.py`) và công cụ kiểm định chuẩn tiếng Hàn (`.work/_qc_ko_parity.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **51** | **51** | **51** | **51** | **Khớp 100% (51/51)** |
| **Lượt lời thoại (LOI)** | **32** | **32** | **32** | **32** | **Khớp 100% (32/32)** |
| **Tổng số câu (Sentences)** | **210** | **210** | **210** | **210** | **Khớp 100% (210/210)** |
| **Phân vai H / D / C / N** | 122 / 36 / 35 / 17 | 122 / 36 / 35 / 17 | 122 / 36 / 35 / 17 | 122 / 36 / 35 / 17 | **Khớp 100% từng lượt thoại** |
| **Số câu Hồi 1** | 51 | 51 | 51 | 51 | **1:1 Tuyệt đối** |
| **Số câu Hồi 2** | 40 | 40 | 40 | 40 | **1:1 Tuyệt đối** |
| **Số câu Hồi 3** | 42 | 42 | 42 | 42 | **1:1 Tuyệt đối** |
| **Số câu Hồi 4** | 45 | 45 | 45 | 45 | **1:1 Tuyệt đối** |
| **Số câu Hồi 5** | 32 | 32 | 32 | 32 | **1:1 Tuyệt đối** |
| **Số cue BGM & SFX** | 19 (10 BGM / 9 SFX) | 19 (10 BGM / 9 SFX) | 19 (10 BGM / 9 SFX) | 19 (10 BGM / 9 SFX) | **Giữ nguyên thẻ tiếng Anh** |
| **Số lượng câu trích (Quotes)** | 2 | 2 | 2 | 2 | **Khớp 100% vị trí** |
| **Tỷ lệ Hangul bản KO** | — | — | — | **92,5%** (Chuẩn $\ge 60\%$) | **✅ ĐẠT** |
| **Hanja / Chữ Hán trong KO** | — | — | — | **0 ký tự** | **✅ ĐẠT** |
| **Dấu tiếng Việt sót trong KO** | — | — | — | **0 ký tự** | **✅ ĐẠT** |

---

## 2. Chi tiết phân bố 210 câu thoại theo 32 lượt lời (LOI Turn-by-Turn Parity)

| ID Turn | Hồi | Vai trò | Tên nhân vật | Số câu thoại | Nội dung chính |
|:---:|:---:|:---:|:---:|:---:|---|
| **1.02** | 1 | **H** | Host | **8** | Bối cảnh Hwaseong cuối thập niên 80, chuỗi 10 vụ án mạng ngoài đồng, thiếu thốn đèn đường và camera |
| **1.04** | 1 | **H** | Host | **9** | Chiến dịch điều tra 2 triệu lượt cảnh sát, điểm mù nhóm máu B sai lệch từ mẫu tạp chất |
| **1.06** | 1 | **H** | Host | **7** | Nỗi hoang tưởng tập thể, vết thương 33 năm, công lý không bỏ cuộc |
| **1.07** | 1 | **N** | N1 (Cư dân) | **8** | Nỗi sợ hãi của người dân trong làng, tiếng còi xe cảnh sát, tin đồn áo đỏ đêm mưa |
| **1.09** | 1 | **H** | Host | **8** | Đột phá công nghệ ADN năm 2019 của NFS, giải mã vật chứng các vụ số 5, 7, 9, tìm ra Lee Choon-jae |
| **1.10** | 1 | **D** | Điều tra viên | **7** | Cảm giác của điều tra viên, hồ sơ tù nhân kiểu mẫu tại Trại giam Busan, hết thời hiệu truy tố |
| **1.11** | 1 | **H** | Host | **4** | Lên đường tới Busan, chuẩn bị bước vào cuộc đấu trí tâm lý cân não |
| **2.02** | 2 | **H** | Host | **5** | Vẻ ngoài hiền lành, lịch sự giả tạo của Lee Choon-jae trong những ngày đầu thẩm vấn |
| **2.04** | 2 | **H** | Host | **8** | Chiến thuật xây dựng lòng tin của profiler, chạm vào cái tôi ái kỷ, ADN phá vỡ phòng tuyến |
| **2.06** | 2 | **D** | Điều tra viên | **7** | Lời thú tội lạnh gáy: 14 vụ giết người, vẽ sơ đồ hiện trường chính xác từng bụi rậm sau 30 năm |
| **2.08** | 2 | **H** | Host | **7** | Trớ trêu của quá khứ: Lee Choon-jae từng bị giữ thẩm vấn 3 lần nhưng lọt lưới vì nhóm máu O |
| **2.09** | 2 | **D** | Điều tra viên | **5** | Câu hỏi tại sao thú tội khi hết thời hiệu: câu nói ngạo nghễ 'Tôi cứ nghĩ các ông phải bắt được tôi từ lâu rồi chứ' |
| **2.10** | 2 | **H** | Host | **8** | Vụ án oan số 8 của Yoon Sung-yeo: 20 năm tù oan vì bị tra tấn ép cung, mở ra cuộc đại phẫu tư pháp |
| **3.02** | 3 | **H** | Host | **5** | Dạng sát nhân kiểm soát quyền lực (Power-Control), cơ chế chia ngăn nhận thức cực đoan |
| **3.03** | 3 | **C** | Chuyên gia tâm lý | **9** | Khung lý thuyết Holmes & DeBurger, phân biệt rạch ròi Thủ đoạn MO vs Chữ ký Signature (trói bằng đồ cá nhân) |
| **3.04** | 3 | **H** | Host | **4** | Thái độ bình thản khi kể lại tội ác, kỹ thuật trung hòa đạo đức (Moral Disengagement) |
| **3.05** | 3 | **C** | Chuyên gia tâm lý | **9** | Sợ hãi biến mất khi hết thời hiệu, chu kỳ ảo tưởng và quỹ đạo leo thang (Escalation Cycle), ái kỷ ác tính |
| **3.06** | 3 | **H** | Host | **3** | Sự sụp đổ của ảo tưởng quyền lực trước lòng kiên trinh và sự thật |
| **3.07** | 3 | **C** | Chuyên gia tâm lý | **8** | Bóc tách hiện tượng Lời thú tội cưỡng bức (Coerced Confession), suy sụp ý chí dưới đòn tra tấn kéo dài |
| **3.08** | 3 | **H** | Host | **4** | Khép lại phân tích tâm lý học, hướng về phiên tòa tái thẩm lịch sử phục hồi danh dự |
| **4.02** | 4 | **H** | Host | **7** | Phiên tòa tái thẩm Suwon năm 2020: kẻ sát nhân thật sự và nạn nhân oan đối mặt nhau trước tòa |
| **4.04** | 4 | **H** | Host | **5** | Tuyên trắng án lịch sử ngày 17/12/2020, tòa án chính thức xin lỗi ông Yoon Sung-yeo |
| **4.06** | 4 | **D** | Điều tra viên | **7** | Giám đốc Cảnh sát tỉnh Gyeonggi Nambu Bae Yong-ju cúi đầu họp báo tạ tội trước nhân dân |
| **4.08** | 4 | **H** | Host | **4** | Lee Choon-jae tiếp tục thụ án chung thân không ân xá, bản án lương tâm và lịch sử |
| **4.09** | 4 | **N** | N2 (Bạn ông Yoon) | **9** | Lời kể nghẹn ngào của người bạn: 20 năm tuổi trẻ bị cướp mất, danh dự phục hồi, nhắn nhủ niềm tin vào công lý |
| **4.10** | 4 | **D** | Điều tra viên | **6** | Đạo luật Taewan (2015) bãi bỏ thời hiệu truy tố giết người, bắt buộc ghi âm ghi hình chống ép cung |
| **4.11** | 4 | **C** | Chuyên gia tâm lý | **4** | Bài học loại bỏ thiên kiến nhận thức, sự kết hợp giữa đạo đức nghề nghiệp và khoa học chính xác |
| **4.12** | 4 | **H** | Host | **3** | Khép lại 33 năm sương mù, trả lại phẩm giá cho các nạn nhân nữ xấu số |
| **5.02** | 5 | **H** | Host | **5** | Hwaseong ngày nay chuyển mình thành đô thị hiện đại, đèn đường và camera an ninh thắp sáng |
| **5.03** | 5 | **D** | Điều tra viên | **4** | Bài học thực thi pháp luật: không bao giờ tự mãn, bảo quản vật chứng cho khoa học tương lai giải mã |
| **5.04** | 5 | **C** | Chuyên gia tâm lý | **5** | Bản chất kẻ săn mồi ban đêm, trực giác sinh tồn là món quà tiến hóa (The Gift of Fear) |
| **5.05** | 5 | **H** | Host | **18** | Đúc kết 4 cảnh báo đỏ sinh tồn: (1) Tránh lộ trình đơn độc cố định; (2) Nhận diện bám đuôi; (3) Chống phân tâm điện thoại/tai nghe; (4) Nhận diện bạo lực ngầm ở người quen |

---

## 3. Kết quả các cổng kiểm tra kỹ thuật (QC Gateways)

1. **Pipeline Parser QC (`parse_kichban.py`)**:
   - `01_KICH_BAN/Tap24/kichban_tap24_23102026.md` $\rightarrow$ 51 elements, 32 LOI turns, 210 sentences. ✅ **PASS**
   - `01_KICH_BAN/Tap24_EN/kichban_tap24_EN.md` $\rightarrow$ 51 elements, 32 LOI turns, 210 sentences. ✅ **PASS**
   - `01_KICH_BAN/Tap24_JA/kichban_tap24_JA.md` $\rightarrow$ 51 elements, 32 LOI turns, 210 sentences. ✅ **PASS**
   - `01_KICH_BAN/Tap24_KO/kichban_tap24_KO.md` $\rightarrow$ 51 elements, 32 LOI turns, 210 sentences. ✅ **PASS**

2. **Multilingual Parity QC (`_verify_all_tap24_parity.py`)**:
   - 100% Perfect 1:1 Parity across all 4 languages. ✅ **PASS**

3. **Korean Script Formal QC (`_qc_ko_parity.py`)**:
   - Acts: 5/5 ✅ **PASS**
   - Role matching: 32/32 ✅ **PASS**
   - Sentence count per element: 32/32 ✅ **PASS**
   - Hangul share: 92,5% (ngưỡng $\ge 60\%$) ✅ **PASS**
   - Zero Vietnamese diacritics in KO ✅ **PASS**
   - Zero Hanja / Chinese ideographs in KO ✅ **PASS**
   - Quote synchronization: 2/2 ✅ **PASS**
   - Latin Proper names matching ✅ **PASS**

---

## 4. Kết luận

Cả 4 phiên bản ngôn ngữ của Tập 24 (Tiếng Việt, Tiếng Anh, Tiếng Nhật, Tiếng Hàn) đã hoàn tất quá trình tái cấu trúc theo tiêu chuẩn mới, đạt quy mô 210 câu thoại và tích hợp đầy đủ 10 chỉ dấu tâm lý hành vi. Tất cả các cổng kiểm định chất lượng đều xanh.
