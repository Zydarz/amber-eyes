# QC Whisper + UTMOS — t06

ASR: `openai/whisper-large-v3` (greedy, Kaggle GPU) · CER = `vi_cer.cer_pair` (Q3a). MOS: `utmos22_strong` — mô hình tiếng Anh, **chỉ so tương đối** giữa các bản/vai.

| Vai | n | CER tb | CER max | file > 2% | UTMOS tb | UTMOS min |
|---|---:|---:|---:|---:|---:|---:|
| C | 56 | 2.15% | 8.9% | 24 | 2.90 | 2.54 |
| D | 78 | 3.42% | 82.1% | 38 | 3.32 | 2.65 |
| H | 213 | 1.94% | 23.3% | 80 | 2.46 | 1.83 |
| N1 | 14 | 2.90% | 22.2% | 5 | 3.02 | 2.51 |
| N2 | 10 | 0.00% | 0.0% | 0 | 3.36 | 2.94 |

## Câu mà MỌI bản đều > 2% (30/154 câu)

| Câu | Vai | CER tốt nhất | CER bỏ tên riêng | UTMOS | Bản chép (bản tốt nhất) |
|---|---|---:|---:|---:|---|
| 1.02#1 | H | 2.2% | 6.1% | 2.24 | Vào ngày 6 tháng 5 năm 1978, tại buổi lễ diễu hành mừng, ngày Hiến pháp Ba Lan ở thành phố Chicago, một người đàn ông tr |
| 1.02#4 | H | 3.8% | 11.9% | 2.51 | mắt cộng đồng vùng ngoại ô Norwood Park. Ông ta là John Wayne Gacy, một nhà thầu xây dựng thành đạt, người đội trưởng kh |
| 1.04#1 | H | 2.8% | 2.8% | 2.60 | Nhưng phía sau nụ cười thân thiện và lớp sơn trắng vẻ mặt của chú hề ấy là một chiếc bẫy săn mồi tàn độc đang âm thầm vậ |
| 1.06#2 | H | 2.9% | 0.0% | 3.14 | Hôm ấy là ngày sinh nhật tròn 46 tuổi của bà Elisabeth Pieste. |
| 1.06#3 | H | 5.7% | 9.2% | 2.62 | Người mẹ ấy đến hiệu thuốc Nissan Pharmacy để đón cậu con trai 15 tuổi Robert P.S. Tanka làm thêm. |
| 1.06#4 | H | 5.2% | 0.0% | 2.89 | Robert Pierce là một học sinh danh dự lớp 10 của trường trung học Main West, |
| 1.11#2 | H | 5.1% | 0.0% | 2.83 | gia đình Pierce lập tức liên lạc với Sở Cảnh sát Des Plaines. |
| 1.12#1 | D | 2.4% | 0.0% | 3.54 | Khi tiếp nhận hồ sơ vụ mất tích của Robert Pierce, cảnh sát Des Plaines nhận thấy ngay những dấu hiệu bất thường nghiêm  |
| 1.14#2 | D | 3.0% | 3.6% | 3.60 | Quần áo của Gacy dính đầy bùng đất |
| 2.06#1 | D | 2.8% | 3.0% | 3.41 | Căn nhà của Gacy là một ngôi nhà một tầng khác khang trang ở vùng ngoài ô. |
| 2.07#3 | H | 2.6% | 0.0% | 2.43 | Một cuộc tra cứu danh tính nhanh chóng xác định chiếc nhẫn đó thuộc về John Allen Seed, một chàng trai 19 tuổi đã mất tí |
| 2.07#5 | H | 4.4% | 0.0% | 2.33 | Cảnh sát chưa có đủ chứng cứ vật chất trực tiếp để ra lệnh bắt giữ Gacy, bởi họ vẫn chưa tìm thấy tung tích của Robert P |
| 2.07#6 | H | 3.1% | 4.5% | 2.43 | nhưng Trung úy Kozenchak quyết định tung ra một chiến thuật tối hậu, triển khai đội đặc nhiệm giám sát bám đuôi Geysi 24 |
| 2.08#1 | D | 2.0% | 1.2% | 3.66 | Bốn sĩ quan dày dạng kinh nghiệm gồm Mike Albrecht, Dave Hackmeister, Robert Schutz và Ron Robinson được giao nhiệm vụ t |
| 2.09#2 | H | 2.6% | 2.7% | 2.40 | Tại vì hoảng sợ tìm cách lẫn trốn hay tỏ ra thận trọng, Gacy lại biến cuộc theo dõi gắt gao của cảnh sát thành một sân k |
| 2.10#4 | C | 2.3% | 2.3% | 2.85 | bằng cách chủ động treo ngươi và kiểm soát cảm xúc của những người săn đuổi, kẻ thù ác tìm thấy ảo tưởng về sự thống trị |
| 3.02#2 | H | 5.1% | 5.1% | 2.20 | hắn trở nên bồn trồn, mất kiểm soát, như một người biết rằng dòng vay đã khép lại. |
| 3.03#2 | D | 3.4% | 3.8% | 3.31 | Lúc đó, một đội khám xét đặc biệt được trang bị lệnh khám xét thứ hai đã âm thầm tiến vào ngôi nhà số 8213 West Summerda |
| 3.06#2 | D | 3.1% | 3.1% | 3.00 | để tiến vào bên trong, các điều tra viên phải nằm sắp trên nền đất ẩm và trường về phía trước bằng khỉu tay trong bóng t |
| 3.07#1 | H | 2.3% | 2.3% | 2.56 | Ánh đèn pin quét qua mặt đất, phủ đầy bụi bậm. |
| 3.10#2 | C | 7.0% | 7.0% | 3.02 | Nó là một không gian chuông dấu được thiết lập có chủ đích. |
| 3.13#1 | H | 3.2% | 3.6% | 2.76 | Cả nước Mỹ bàn hoàng rúng động. |
| 4.02#2 | H | 2.1% | 2.1% | 3.19 | Thế nhưng, kẻ thái nhân cách này không hề suy sập. |
| 4.03#2 | D | 3.5% | 2.9% | 2.87 | tuyên bố bên trong cơ thể mình tồn tại 4 nhân cách hoàn toàn riêng biệt John nhà thầu xây dựng chăm chỉ John chính trị g |
| 4.05#1 | H | 2.5% | 3.2% | 2.36 | Tại phiên tòa xét xử mở màn vào tháng 2 năm 1980 tại tòa án Hạ Khúc, đội ngũ luật sư bào chữa đã dựa hoàn toàn vào lý do |
| 4.06#2 | C | 3.4% | 0.0% | 2.66 | Để chống chọi với cảm giác bất lực tột cùng đó, Gai Xi đã tự xây dựng nên một cấu trúc cái tôi ái kỷ khổng lồ để bù đắp. |
| 4.09#3 | C | 2.8% | 0.7% | 2.95 | Mọi hành vi của Garcia đều có chuỗi liên kết nhân quả mạch lạc, có sự chuẩn bị chú đáo và nỗ lực che giấu dấu vết tuyệt  |
| 5.03#1 | C | 3.6% | 3.6% | 2.74 | Tự coi mình là nạn nhân phơi bày tận cùng cơ chế phòng vệ đổ lỗi ngoại vi thường được mô tả ở những người mang đặc điểm  |
| 5.06#1 | H | 4.0% | 0.0% | 2.32 | Gần nửa thế kỷ đã trôi qua kể từ buổi tối định mệnh của cậu bé Robert Pierce. |
| 5.06#4 | H | 2.3% | 8.4% | 2.37 | Dấu hiệu thứ nhất, cảnh giác trước sự hào nhoán của các võ bọc từ thiện và địa vị xã hội. |

## 10 file UTMOS thấp nhất (nghe kiểm tạp âm / méo)

| File | Vai | UTMOS | CER |
|---|---|---:|---:|
| 1_08_1_H_H_t0.8_s0.wav | H | 1.83 | 0.0% |
| 5_04_3_H_H_t0.8_s0.wav | H | 1.84 | 0.0% |
| 5_06_13_H_H_t0.8_s0.wav | H | 1.90 | 0.0% |
| 5_04_3_H_H_t0.8_s1.wav | H | 1.91 | 0.0% |
| 1_16_2_H_H_t0.8_s1.wav | H | 1.97 | 0.0% |
| 5_04_1_H_H_t0.8_s0.wav | H | 1.99 | 0.0% |
| 1_02_6_H_H_t0.8_s1.wav | H | 2.05 | 0.0% |
| 5_04_1_H_H_t0.8_s1.wav | H | 2.05 | 0.0% |
| 1_13_2_H_H_t0.8_s1.wav | H | 2.08 | 1.4% |
| 5_04_2_H_H_t0.8_s1.wav | H | 2.09 | 0.8% |
