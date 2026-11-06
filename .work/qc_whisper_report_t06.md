# QC Whisper + UTMOS — t06

ASR: `openai/whisper-large-v3` (greedy, Kaggle GPU) · CER = `vi_cer.cer_pair` (Q3a). MOS: `utmos22_strong` — mô hình tiếng Anh, **chỉ so tương đối** giữa các bản/vai.

| Vai | n | CER tb | CER max | file > 2% | UTMOS tb | UTMOS min |
|---|---:|---:|---:|---:|---:|---:|
| C | 94 | 1.49% | 9.2% | 28 | 2.82 | 2.24 |
| D | 113 | 5.05% | 82.5% | 51 | 3.14 | 2.66 |
| H | 218 | 1.69% | 9.1% | 69 | 2.39 | 1.86 |
| N1 | 10 | 10.37% | 75.8% | 7 | 2.73 | 2.38 |
| N2 | 10 | 1.22% | 4.0% | 3 | 3.19 | 2.79 |

## Câu mà MỌI bản đều > 2% (46/212 câu)

| Câu | Vai | CER tốt nhất | CER bỏ tên riêng | UTMOS | Bản chép (bản tốt nhất) |
|---|---|---:|---:|---:|---|
| 1.02#4 | H | 3.7% | 11.3% | 2.42 | mắt cộng đồng vùng ngoại ô Norwood Park. Ông ta là John Wayne Gacy, một nhà thầu xây dựng thành đạt và là người đội trưở |
| 1.04#1 | H | 4.2% | 11.2% | 2.51 | Nhưng, chính chiếc áo vest sang trọng và lớp phấn trắng vẻ mặt của chú hề ấy đã dệt nên một hiệu ứng hào quan hoàn hảo,  |
| 1.06#2 | H | 4.3% | 0.0% | 2.82 | Hôm ấy là ngày sinh nhật tròn 46 tuổi của bà Elizabeth Pierce. |
| 1.06#3 | H | 8.9% | 11.6% | 2.53 | Tụi mẹ ấy lái xe đến hiệu thuốc Nixon Pharmacy để đón cậu con trai 15 tuổi Robert Pietanka làm thêm sau giờ học. |
| 1.06#4 | H | 2.5% | 0.0% | 2.48 | Robert Pierce là một học sinh danh dự lớp 10 của trường trung học Main West, một thiếu niên chăm chỉ, lễ phép và chưa từ |
| 1.08#6 | H | 6.1% | 0.0% | 2.52 | Cậu bé Robert Pierce đã biến mất không một dấu vết. |
| 1.09#1 | N1 | 4.6% | 5.1% | 2.84 | Mỗi hôm đó, hiệu thuốc chúng tôi đang sửa chữa một số giấy tủ kệ và nhà thầu John Gacy đã ở đó suốt buổi chiều. |
| 1.09#2 | N1 | 3.0% | 3.0% | 2.44 | Chúng ta nói chuyện rất vui vẻ, cởi mở với tất cả nhân viên và tỏ ra là một người lớn vô cùng tốt bụng. |
| 1.11#2 | H | 4.1% | 0.0% | 2.61 | gia đình Pierce kiên quyết khẳng định con trai họ không bao giờ tự ý bỏ đi. |
| 1.12#4 | D | 4.4% | 4.6% | 3.30 | Nhưng Gacy đã viện cớ xe bị sa lầy tuyết và công việc bận rộn để trị hoãn cuộc thẩm vấn suốt nhiều giờ đồng hồ. |
| 1.12#5 | D | 5.5% | 5.5% | 2.84 | Ở đến tận rạng sáng hôm sau, hắn mới thông thả bước vào phòng làm việc của ban chuyên án với một phong thái vô cùng bình |
| 1.12#6 | D | 2.9% | 0.0% | 3.21 | Hắn hoàn toàn phủ nhận việc mình từng nói chuyện hay hứa hẹn bất kỳ công việc nào với cậu bé Robert P.S. |
| 1.13#2 | H | 5.7% | 5.7% | 2.50 | Nhưng sự ngạo mạng ấy đã để lộ một sơ hở chí mạng ngay trước mắt các điều tra viên dày dạng kinh nghiệm. |
| 1.14#1 | D | 4.2% | 4.3% | 3.20 | Dù tuyên bố chỉ ở nhà và văn phòng ấm cúng suốt đêm, nhưng trên gấu quần và đế dậy của Gacy lại dính đầy những vệt bụng  |
| 1.15#1 | C | 2.9% | 9.6% | 3.08 | Và lăng kính tâm lý học hành vi, John Wayne Gacy là hiện thân kinh điển của rối loạn nhân cách chống đối xã hội kết hợp  |
| 1.15#3 | C | 4.9% | 8.6% | 3.02 | cơ chế tâm lý của Gacy, việc khoát lên mình bộ trang phục chú hề Pogo hay bắt tay các chính khách quyền lực phục vụ hai  |
| 1.16#1 | H | 3.0% | 1.0% | 2.27 | Cuộc đối đầu tại đồn cảnh sát Death Plains vào rạng sáng ngày 12 tháng 12 năm 1978 chính là phát súng mở màng cho một cu |
| 2.03#2 | D | 4.0% | 4.0% | 3.24 | Nhưng nhờ khả năng ngụy trang tâm lý siêu hạn và tài lấy lòng ban giám thị hắn đã được đánh giá là một tù nhân kiểu mẫu |
| 2.05#1 | H | 2.5% | 4.6% | 2.06 | nhận thức được mức độ nguy hiểm tột cùng của kẻ săn mồi đội lốt nhà hảo tâm. Trung úy Kozenchak hiểu rằng tính mạng của  |
| 2.07#5 | D | 4.5% | 4.3% | 3.25 | nhất là một cuốn biên nhận ảnh của hiệu thuốc Nissan, chứng minh rõ ràng việc Gacy đã tiếp xúc với nhân viên quậy thuốc  |
| 2.07#6 | D | 2.8% | 1.0% | 2.73 | Thứ hai là một chiếc nhẫn tốt nghiệp trung học năm 1975 có khắc ba chữ lộng TRS. |
| 2.08#1 | H | 3.1% | 0.0% | 2.72 | Một cuộc tra cứu danh tính khẩn cấp xác định chiếc nhẫn JAS thuộc về John Allen Sykes, một thanh niên 19 tuổi, đã mất tí |
| 2.08#2 | H | 4.5% | 1.6% | 2.55 | Khi cảnh sát chất vấn về nguồn gốc chiếc nhẫn, Jaycee thẳng nhiên bịa ra một câu chuyện rằng hắn mua lại nó từ một người |
| 2.08#3 | H | 3.5% | 7.0% | 2.59 | Tuy nhiên, sự xuất hiện của kỹ vật thuộc về một người mất tích đã xác nhận một nghi vấn trùng mình. Robert Pierce không  |
| 2.09#7 | D | 2.7% | 2.7% | 3.32 | là việc lưu giữ các chiến lợi phẩm như chiếc nhẫn tốt nghiệp, ví tiện và bằng lái xe của các nạn nhân để thỏa mãn cơn đó |
| 2.10#1 | H | 4.0% | 0.0% | 2.24 | Tại thời điểm đó, cảnh sát vẫn chưa có đủ chứng cứ vật chất trực tiếp về nơi ở của Robert Pierce hay thi thể của John Si |
| 2.10#2 | H | 4.5% | 7.2% | 2.30 | Các nguy cơ kẻ thủ ác có thể tiêu hủy chứng cứ hoặc tiếp tục gây hại. Trung úy Kosensak quyết định tung ra một chiến thu |
| 2.10#6 | H | 3.6% | 0.7% | 2.59 | Thay vì sợ hãi, tìm cách lẫn trốn, Gai Xi lại biến cuộc theo dõi gắt gao của lực lượng chức năng thành một sàn diễn cá n |
| 2.10#8 | H | 3.0% | 3.0% | 2.19 | Vào những đêm đông lạnh giá, hắn thẳng nhiên dựng xe, bước sang gõ cửa kính và mời các sĩ quan đang bán theo vào nhà hàn |
| 2.12#2 | H | 3.0% | 3.3% | 2.56 | và một sơ hở xuất hiện từ chính hệ thống sử ấm trong căn nhà Summerdale đã trở thành chìa khóa mở toan cánh cửa dẫn xuốn |
| 3.02#1 | H | 2.2% | 0.0% | 2.44 | Ngày 20 tháng 12 năm 1978, khi đến văn phòng luật sư riêng để tìm cách đối phó với lệnh triệu tập, Gai Xi đã bộc lộ dấu  |
| 3.03#4 | D | 10.0% | 6.7% | 3.44 | Cũng úy, cô Jen Sack đã chú ý đến một chi tiết kỳ lạ mà các sĩ quan phát hiện trong lần khám xét trước. |
| 3.03#5 | D | 3.0% | 3.0% | 2.98 | Mỗi khi hệ thống lò sử ấm sàn nhà được bật lên, một luồng không khí hồi thối nồng nặc và ngột ngạt lại bốc lên qua các k |
| 3.06#1 | D | 2.4% | 2.4% | 3.14 | để tiến vào bên trong khoảng không gian bò ấy. Các điều tra viên phải cởi bỏ quân phục, mặc đồ bảo hộ và nằm sắp trên nề |
| 3.06#3 | D | 2.5% | 2.5% | 3.10 | Khi ánh đèn pin quét qua nền đất, phủ đầy bụi vôi trắng, chúng tôi phát hiện những rảnh đất đã bị sới sáo và lấp vội vàn |
| 3.06#4 | D | 2.3% | 2.5% | 3.10 | một chiếc sẻn được cắm sâu xuống lớp đất xốp ẩm ướt ngay phía dưới phòng ngủ của Gacy. |
| 3.10#6 | D | 4.0% | 4.9% | 3.39 | nạn nhân xấu xấu cuối cùng trong đó có cậu bé Robert Piest bị Gacy ném xuống dòng sông Des Plaines băng giá khi nền đất  |
| 3.11#4 | C | 2.3% | 2.3% | 2.78 | Năng kéo thứ nhất là thế giới ba ngày của một nhà thầu PDM cần mẫn, một người con trai hiếu thảo hết lòng phụng dưỡng mẹ |
| 3.11#5 | C | 2.5% | 5.0% | 2.81 | Hắn sử dụng chính gia đình và người mẹ của mình như một lá trắng bình thường hóa hoàn hảo để bảo chứng cho danh dự công  |
| 3.12#3 | H | 3.7% | 3.7% | 2.56 | Nó sống ngay giữa một khu dân cư kiểu mẫu, miễn cười chào hỏi hàng xóm mỗi sáng và khoát lên mình bộ trang phục sạc sở c |
| 4.02#2 | H | 6.2% | 6.2% | 2.36 | Nhưng kẻ ái kỷ ác tính này không hề có dấu hiệu ăn năng hay chấp nhận thất bại. |
| 4.03#4 | D | 4.3% | 5.3% | 3.82 | AC ranh mảnh đổ toàn bộ hành vi tội ác lên đầu thực thể, Jack Hanley. |
| 4.05#4 | N2 | 3.2% | 3.5% | 3.34 | Hắn còn bình thẳng cầm bút dạ, tự tay vẽ sơ đồ chi tiết từng vị trí trôn cất dưới khoảng không gian bò Summerdale cho ch |
| 4.06#1 | H | 3.6% | 4.3% | 2.45 | Vào tháng 2 năm 1980, tại tòa án Hạt Quốc, phiên tòa xét xử John Wayne Gacy chính thức mở mạng dưới sự quan tâm theo dõi |
| 5.06#6 | H | 4.0% | 0.0% | 2.48 | Gần nửa thế kỷ đã trôi qua kể từ buổi tối định mệnh của cậu bé Robert Pierce. |
| 5.06#9 | H | 3.4% | 9.6% | 2.43 | Dấu hiệu thứ nhất, cảnh giác trước sự hào nhoán của các giỏ bọc từ thiện và địa vị xã hội. |

## 10 file UTMOS thấp nhất (nghe kiểm tạp âm / méo)

| File | Vai | UTMOS | CER |
|---|---|---:|---:|
| 5_06_17_H_H_t0.8_s0.wav | H | 1.86 | 0.0% |
| 2_05_1_H_H_t0.8_s0.wav | H | 1.94 | 7.5% |
| 5_04_1_H_H_t0.8_s0.wav | H | 1.95 | 0.0% |
| 4_11_4_H_H_t0.8_s0.wav | H | 1.96 | 4.2% |
| 4_02_3_H_H_t0.8_s0.wav | H | 2.01 | 1.4% |
| 1_08_7_H_H_t0.8_s0.wav | H | 2.01 | 1.3% |
| 2_02_2_H_H_t0.8_s0.wav | H | 2.03 | 0.9% |
| 4_02_1_H_H_t0.8_s1.wav | H | 2.04 | 1.1% |
| 1_08_2_H_H_t0.8_s0.wav | H | 2.06 | 0.0% |
| 5_04_3_H_H_t0.8_s1.wav | H | 2.06 | 0.8% |
