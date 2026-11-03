# QC Whisper + UTMOS — t07

ASR: `openai/whisper-large-v3` (greedy, Kaggle GPU) · CER = `vi_cer.cer_pair` (Q3a). MOS: `utmos22_strong` — mô hình tiếng Anh, **chỉ so tương đối** giữa các bản/vai.

| Vai | n | CER tb | CER max | file > 2% | UTMOS tb | UTMOS min |
|---|---:|---:|---:|---:|---:|---:|
| C | 40 | 1.04% | 4.9% | 9 | 3.03 | 2.52 |
| D | 48 | 5.89% | 83.6% | 21 | 3.23 | 2.65 |
| H | 210 | 2.02% | 19.1% | 71 | 2.56 | 2.03 |
| N1 | 10 | 1.87% | 7.5% | 3 | 2.90 | 2.54 |
| N2 | 6 | 0.00% | 0.0% | 0 | 3.31 | 2.97 |

## Câu mà MỌI bản đều > 2% (25/147 câu)

| Câu | Vai | CER tốt nhất | CER bỏ tên riêng | UTMOS | Bản chép (bản tốt nhất) |
|---|---|---:|---:|---:|---|
| 1.02#1 | H | 2.1% | 0.0% | 2.80 | Chào mừng quý vị đã quay trở lại với AmberEyes. |
| 1.04#2 | H | 3.0% | 19.3% | 2.48 | Một chiếc xe bán tải hiệu Ford F-250 đã đổ im liềm suốt nhiều giờ liền ở một góc khuất. |
| 1.06#6 | H | 6.2% | 6.2% | 2.89 | nhưng phía sau nụ cười hiền lành ấy là một tâm hồn mong manh. |
| 1.06#7 | H | 4.0% | 4.0% | 2.46 | Cậu thường xuyên phải giật lộn với những cơm trầm cảm và sự âu lo triền miên. |
| 1.06#8 | H | 3.0% | 0.0% | 2.53 | Hãy hình dung nỗi đau của mẹ cậu, bà Linh Roy, trong buổi sáng hôm ấy. |
| 1.07#2 | N1 | 5.7% | 5.7% | 2.86 | Tinh tính mắc bảo bà rằng điều tồi tệ nhất đã xảy ra |
| 1.12#2 | C | 3.9% | 3.9% | 3.37 | Họ luôn dằn xé giữa bản năng sinh tồn và mong muốn chấm dứt nỗi đau tâm trí. |
| 2.03#2 | D | 2.5% | 0.0% | 3.32 | Michelle Carter sống tại thị trấn Plainview, chỉ cách nơi Conrad ở khoảng 35 dặm, tức là chưa đầy một giờ lái xe. |
| 2.04#1 | H | 2.6% | 0.0% | 2.62 | Trong phần lớn thời gian, Michel Carter tỏ ra là một người bạn biết lắng nghe. |
| 2.09#2 | H | 2.1% | 2.4% | 2.83 | Conrad lái chiếc xe bán tải đến bãi đổ xe Kmart. |
| 2.09#4 | H | 8.8% | 8.8% | 2.51 | Con rác hoảng sợ và bước ra khỏi xe. |
| 2.09#6 | H | 4.9% | 4.9% | 2.63 | Nhưng, điều mà cậu nhận lại không phải là một bàn tay kéo cậu về phía ánh sáng. |
| 2.10#1 | D | 6.9% | 6.9% | 3.56 | Cục gọi ấy không được ghi âm |
| 2.10#3 | D | 13.1% | 13.1% | 2.98 | Cô ta không gọi 911, không thông báo cho gia đình cậu. |
| 3.02#1 | H | 2.4% | 7.8% | 2.44 | Câu hỏi lớn nhất khiến toàn bộ dư luận nước Mỹ bàn hoàng khi vụ án vỡ lỡ là tại sao? |
| 3.05#2 | D | 3.8% | 1.9% | 3.25 | Năm 2013, nằm diễn viên Cory Montic, bạn diễn ngoại đời thực của Lea Michele, đột ngột qua đời vì sốc thuốc. |
| 3.08#5 | H | 2.6% | 3.1% | 2.38 | Các mặt nạ của người bạn gái thiên thần tưởng chừng đã giúp Michelle Carter hoàn thành vai diễn để đời của mình. |
| 3.08#6 | H | 3.6% | 3.6% | 2.42 | Cho đến một ngày, sự ngạo mạng và thói quen phô trương của kẻ thủ ác đã tự tay giật phăn lớp giỏ bọc hoàn hảo đó. |
| 4.07#1 | C | 3.2% | 3.5% | 2.95 | Bị cáo thậm chí còn thuê một bác sĩ tâm thần nổi tiếng để lập luận rằng Michelle bị mất kiểm soát hành vi do tác dụng ph |
| 4.08#3 | H | 2.9% | 4.1% | 2.50 | Cảm phán Moniz nhận định rằng khi Conrad bước ra khỏi xe, chính Michelle Carter đã bảo cậu quay trở lại. |
| 5.02#5 | H | 2.8% | 2.8% | 2.27 | Chữ luật này nhằm hình sự hóa hành vi ép buộc hoặc xúi dục người khác tự tước đoạt mạng sống, để bịt lỗ hổng pháp lý mà  |
| 5.04#11 | H | 4.1% | 11.6% | 2.49 | Dấu hiệu thứ tư, lắng nghe bản năng sinh tồn và dứt khoát các đức liên lạc. |
| 5.04#12 | H | 3.4% | 3.4% | 2.41 | Một khoảnh khắc bạn cảm thấy sợ hãi hoặc nhận ra sự độc hại trong lời nói của đối phương, đó chính là tiếng gọi của sự s |
| 5.04#16 | H | 11.2% | 17.3% | 2.42 | Nếu bạn hoặc người thân đang trải qua khủng hoảng tâm lý hoặc có suy nghĩ tiêu cực, xin hãy nhớ rằng bạn không đơn độc,  |
| 5.04#17 | H | 2.3% | 8.5% | 2.79 | Cảm ơn quý vị đã đồng hành cùng Amber Eyes trong tập hồ sơ mở mạng mùa 2 ngày hôm nay. |

## 10 file UTMOS thấp nhất (nghe kiểm tạp âm / méo)

| File | Vai | UTMOS | CER |
|---|---|---:|---:|
| 1_02_6_H_H_t0.8_s1.wav | H | 2.03 | 0.0% |
| 5_04_13_H_H_t0.8_s0.wav | H | 2.09 | 0.0% |
| 5_04_1_H_H_t0.8_s1.wav | H | 2.09 | 2.1% |
| 5_04_3_H_H_t0.8_s1.wav | H | 2.10 | 1.1% |
| 3_08_4_H_H_t0.8_s1.wav | H | 2.11 | 0.0% |
| 3_08_6_H_H_t0.8_s0.wav | H | 2.12 | 7.3% |
| 4_02_1_H_H_t0.8_s1.wav | H | 2.13 | 3.8% |
| 5_04_11_H_H_t0.8_s0.wav | H | 2.13 | 5.4% |
| 3_06_3_H_H_t0.8_s0.wav | H | 2.16 | 1.0% |
| 3_08_5_H_H_t0.8_s0.wav | H | 2.16 | 5.3% |
