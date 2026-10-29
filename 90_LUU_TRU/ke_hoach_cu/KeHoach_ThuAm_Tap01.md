# KẾ HOẠCH THU ÂM TẬP 01 — "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ"

**Phiên bản 2 — chạy được bởi AI không cần hỏi thêm**
**Nguồn:** `Kc_1.txt` · **Cập nhật:** 21/10/2026 · `Kc_1.txt` và `Kich_ban.txt` không bị sửa

---

## MỐC 0 — ĐỌC ĐOẠN NÀY TRƯỚC TIÊN

AI đọc file này để dựng audio. Ba quy tắc dưới bắt buộc, sai là kết quả hỏng.

### R1 · Bóc định dạng trước khi đưa vào TTS

Trong các ô `LỜI` có **109 cặp `**đậm**`**, **14 ký hiệu `▸`**, ký tự `` ` `` và dấu `*` chuyển nghiệp. Trước khi gửi lên engine phải:

| Ký hiệu trong file | Xử lý |
|---|---|
| `**text**` | Bỏ 2 dấu `*`, **giữ nguyên** `text` (chỉ nhấn mạnh cho người đọc file) |
| `▸` | Bỏ hẳn. Chỉ đánh dấu "từ đây chuyển sang giọng B" |
| `*DẪN: ...*` | Xoá cả đoạn. Đây là chỉ dẫn diễn xuất, **không đọc thành tiếng** |
| `` ` `` | Bỏ |

**Cấm** đưa ký tự `*`, `` ` ``, `▸`, `[`, `]`, `#` vào nội dung gửi TTS.

### R2 · Xử lý ô `CẦN VIẾT`

Có **5 ô `CẦN VIẾT`** (mã `1.9`, `2.18`, `3.10`, `4.16`, `5.14`) — chưa có lời, tổng cộng 1.395 từ.

> **Lệnh cho AI: BỎ QUA hoàn toàn 5 ô này.** Không tự bịa nội dung. Vẫn dựng được bản audio hoàn chỉnh, chỉ ngắn hơn mục tiêu ~6 phút. Xem mục 9 nếu cần lấp đầy.

### R3 · Thiếu file âm thanh thì bỏ qua, không dừng

Mọi dòng `SFX` và `NHẠC` trong mục 10 đều có cột `BẮT BUỘC`. Nếu `BẮT BUỘC = KHÔNG` và file không tồn tại → **bỏ qua im lặng, không hỏi, không dừng**. Bản demo vẫn ra.

---

## 1. MỤC TIÊU

| Mục | Giá trị |
|---|---|
| Tổng thời lượng mục tiêu (bản đầy đủ) | **24:42** |
| Bản demo (bỏ 5 ô `CẦN VIẾT`) | **≈17:50** |
| Lời thoại có sẵn | 3.166 từ → 15:19 |
| Cần bổ sung để đủ mục tiêu | +1.395 từ (mục 8) |
| Số block | 58 lời · 9 SFX · 3 nhạc · 18 nghỉ |

Tốc độ đo: **3,435 từ/giây** — tương đương đúng 5 MP3 đã sinh. Sai số ±5%.

---

## 2. THAM SỐ MÁY ĐỌC

**Engine:** connector `connector__matrix__batch_text_to_audio` — tối đa **10 đoạn/lần**, trả `{node_id, file_name}`. **Không cần API key**, connector tự lo xác thực.

| Tham số | Giá trị |
|---|---|
| `format` | `mp3` |
| `sample_rate` | `32000` |
| `bitrate` | `128000` |
| `pitch` | `0` |
| `volume` | `1.0` |

> **Đã chạy thật:** phiên "Tạo audio cho Kc_1" dùng đúng connector này, 5/5 thành công, ghép ra `Kc_1.mp3` 992,6s.

**`emotion` chỉ nhận 7 giá trị:** `happy` · `sad` · `angry` · `fearful` · `disgusted` · `surprised` · `neutral`.
Không có `serious`. Giọng B dùng **`sad`**.

### Hai giọng

| | **GIỌNG A — Dẫn dắt** | **GIỌNG B — Trích dẫn** |
|---|---|---|
| `voice_id` | **`audiobook_male_1`** | **`audiobook_female_1`** |
| Nguồn | MiniMax system voice — 男性有声书1 | MiniMax system voice — 女性有声书1 |
| `emotion` | `neutral` | **`sad`** ← enum không có `serious` |
| `speed` | `0.90` | `0.88` |
| Dùng cho | Kể chuyện, phân tích | Lời thoại nhân vật trong ngoặc kép |

**`audiobook_*` chọn vì đây là bộ giọng thiết kế riêng cho đọc dài** — hợp podcast hơn `male-qn-qingse`.

**Về `male-qn-qingse` — đã có bằng chứng là không đạt.** Phiên "Tạo audio cho Kc_1" đã dùng voice này để tạo `Kc_1.mp3` và ghi nhận rõ: *"giọng nam Mandarin mặc định; phát âm tiếng Việt ở mức chấp nhận được nhưng không tự nhiên như voice chuyên tiếng Việt"*. Đây chính là lý do nên thử `audiobook_male_1`.

**Dự phòng:** nếu `audiobook_*` không trả tiếng Việt, quay về `male-qn-qingse` (chắc chắn chạy) và `female-chengshu` (成熟女性音色).

Nguồn: [MiniMax System Voice ID List](https://platform.minimax.io/docs/faq/system-voice-id)

### 7 điểm chuyển sang giọng B

Đánh dấu `▸` trong timeline. Chỉ phần **sau** `▸` mới đổi sang B.

`1.4` lời Facebook của Dee Dee · `3.7` "Vị thánh tử đạo" · `4.6` "Mọi sự vùng vẫy…" · `4.15` "thiên thần nhỏ của mẹ" · `5.6` lời Gypsy trong tù ★ · `5.3` lời Dan Patterson · `5.13` "bảo vệ sức khỏe"

> **Nguyên tắc:** tên riêng, thuật ngữ, trích dẫn học thuật (Seligman, DSM-5-TR…) **luôn đọc bằng A**.

---

## 3. BẢNG MIX ÂM LƯỢNG

| Lớp | Có lời đọc | Dạo chuyển / nghỉ |
|---|---|---|
| Lời đọc | **0 dB** (mốc chuẩn) | — |
| `NHẠC` | −26 dB | −14 dB |
| `SFX` | −22 dB | −18 dB |

---

## 4. TIMELINE CHI TIẾT

> Ô `LOẠI` dùng 4 giá trị: `LỜI` · `SFX` · `NHẠC` · `NGHỈ`.
> Ô `GIỌNG`: `A` · `B` · `A→B` (chuyển tại `▸`) · `—`.

### ▸ MỞ ĐẦU LẠNH (00:00 – 00:18)

| Mã | LOẠI | GIỌNG | NỘI DUNG | THỜI LƯỢNG |
|---|---|---|---|---|
| `O.1` | SFX | — | Còi xe cảnh sát vọng xa, gõ cửa dồn dập. Vang dần. | 8s |
| `O.2` | NHẠC | — | Music box lên dây cót. Từ tổ 12s bị sub-bass drone bóp nghẹt. | 18s |
| `O.3` | NGHỈ | — | **Im lặng tuyệt đối, tắt cả nhạc.** | 6s |
| `O.4` | LỜI | B | Ngày 14 tháng 6 năm 2015. Tại thị trấn yên bình Springfield, bang Missouri, nước Mỹ. *DẪN: rất nhẹ, gần như thì thầm* | 5s |

### ▸ HỒI 1 — THE HOOK (00:18 – 03:30)

| Mã | LOẠI | GIỌNG | NỘI DUNG | THỜI LƯỢNG |
|---|---|---|---|---|
| `1.1` | SFX | — | Bộ đàm cảnh sát rè nhẹ, bước chân hối hả *(đè lên `1.2`)* | 0s |
| `1.2` | LỜI | A | Hàng xóm lập tức vây quanh ngôi nhà nhỏ sơn màu hồng phấn ở số 2103 đường Bắc Volunteer. Trong mắt tất cả mọi người, ngôi nhà màu hồng ấy là biểu tượng của tình mẫu tử thiêng liêng. Bà Dee Dee là một người mẹ đơn thân vĩ đại, người đã dành trọn cuộc đời mình để chăm sóc cô con gái Gypsy Rose – một thiếu nữ bất hạnh mắc hàng loạt căn bệnh hiểm nghèo: bại liệt từ thắt lưng trở xuống, ung thư máu, loạn dưỡng cơ, động kinh nặng và có trí tuệ chỉ ngang một đứa trẻ lên bảy. Khi cảnh sát phá cửa bước vào ngôi nhà lạnh ngắt, họ tìm thấy thi thể của người mẹ – bà Dee Dee Blanchard – trong phòng ngủ. Nhưng Gypsy Rose đã biến mất. | 44s |
| `1.3` | NGHỈ | — | | 2s |
| `1.4` | LỜI | A→B | Trên trang Facebook chung của hai mẹ con nổi tiếng nhất vùng – bà Dee Dee Blanchard và cô con gái tật nguyền Gypsy Rose – bỗng xuất hiện một dòng trạng thái ngắn ngủi nhưng khiến cả khu phố chết lặng: ▸Con khốn đó chết rồi. *DẪN: đoạn sau ▸ lạnh, dứt khoát* | 14s |
| `1.5` | LỜI | A | Chiếc xe lăn của cô bé vẫn nằm nguyên trong nhà. Những bình oxy và hàng trăm lọ thuốc duy trì sự sống cũng còn nguyên trên kệ. Cả nước Mỹ bàng hoàng đặt ra một câu hỏi tuyệt vọng: Kẻ máu lạnh nào đã sát hại người mẹ tận tụy ấy, rồi bắt cóc một cô gái tàn tật không thể tự bước đi dù chỉ một bước, và có thể tử vong bất cứ lúc nào nếu thiếu thuốc? | 24s |
| `1.6` | NGHỈ | — | **Nhạc dừng đột ngột. Im lặng tuyệt đối.** | 2,5s |
| `1.7` | LỜI | A | Thế nhưng, chỉ 48 giờ sau, khi cảnh sát tìm thấy Gypsy Rose tại bang Wisconsin, cách đó hàng trăm dặm… một sự thật làm rúng động lịch sử y khoa và tội phạm học thế giới đã bị phơi bày. *DẪN: hạ trầm, sắc lạnh* | 12s |
| `1.8` | LỜI | A | Bước vào phòng thẩm vấn ngày hôm đó, Gypsy Rose không hề ngồi xe lăn. Cô tự bước đi bằng chính đôi chân của mình. Cô không bị ung thư máu. Không bị loạn dưỡng cơ. Không bị tổn thương não. Và người đứng sau kế hoạch đoạt mạng bà mẹ thánh thiện kia… không ai khác chính là cô con gái bé bỏng của bà. | 26s |
| `1.9` | **CẦN VIẾT** | A | *(bỏ qua — xem mục 8.1)* | **44s** |
| `1.10` | SFX | — | Tiếng bật máy ghi âm "Tách" | 0s |
| `1.11` | NHẠC | — | Cello trầm buồn vào | 20s |
| `1.12` | LỜI | A | Chào mừng bạn đến với hồ sơ phân tích tâm lý học tội phạm. Hôm nay, chúng ta sẽ bước vào bên trong ngôi nhà màu hồng ở Missouri để giải mã một trong những hội chứng tâm thần kỳ dị và tàn nhẫn nhất ẩn dưới lớp vỏ bọc của tình yêu thương: **Hội chứng Münchausen qua trung gian.** *DẪN: câu cuối đọc chậm* | 26s |
| `1.13` | NGHỈ | — | Dạo chuyển sang hồi 2 | 3s |

> Hồi 1 · hiện có **136s** lời · mục tiêu **180s** · thiếu 44s (≈151 từ)

### ▸ HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ BỆNH ÁN (03:30 – 09:30)

| Mã | LOẠI | GIỌNG | NỘI DUNG | THỜI LƯỢNG |
|---|---|---|---|---|
| `2.1` | SFX | — | Tiếng lật giấy hồ sơ sột soạt *(đè lên `2.2`)* | 0s |
| `2.2` | LỜI | A | Để hiểu tại sao một cô gái lại chọn cách kết liễu mẹ ruột để tìm đường sống, trước hết chúng ta cần nhìn vào hiện trường thực sự của vụ án này. Hiện trường đó không phải là căn phòng ngủ đẫm máu vào tháng 6 năm 2015. Hiện trường thực sự chính là cơ thể của Gypsy Rose suốt 23 năm trước đó. | 18s |
| `2.3` | NGHỈ | — | | 1,5s |
| `2.4` | LỜI | A | Gypsy Rose sinh năm 1991, là một đứa trẻ hoàn toàn khỏe mạnh. Nhưng ngay từ khi cô mới được 3 tháng tuổi, bà Dee Dee bắt đầu đưa con đến bệnh viện với lời khẳng định rằng con gái mình mắc chứng ngưng thở khi ngủ. Từ cột mốc đó, một danh sách bệnh án khổng lồ bắt đầu được thêu dệt. Khi Gypsy lên 7, sau một vụ trầy xước đầu gối nhẹ khi đi xe đạp với ông ngoại, bà Dee Dee tuyên bố con gái mình bị tổn thương tủy sống và buộc cô bé phải ngồi xe lăn vĩnh viễn. Bà cạo trọc đầu Gypsy, rồi nói với đứa trẻ và cả thế giới rằng tóc cô rụng hết là do hóa trị ung thư máu. | 44s |
| `2.5` | NGHỈ | — | | 1,5s |
| `2.6` | LỜI | A | Nhưng bà Dee Dee không chỉ dừng lại ở lời nói dối. Để biến kịch bản trong đầu mình thành sự thật trước mắt các bác sĩ, bà đã trực tiếp can thiệp vào cơ thể con gái: | 11s |
| `2.7` | LỜI | A | Bà cho Gypsy uống thuốc chống động kinh liều cao dù cô không hề bị động kinh, khiến hàm răng của cô bé bị mục ruỗng và phải nhổ bỏ toàn bộ răng cửa. | 10s |
| `2.8` | LỜI | A | Bà thuyết phục bác sĩ phẩu thuật đặt ống truyền thức ăn trực tiếp qua thành bụng vào dạ dày của Gypsy. | 6s |
| `2.9` | LỜI | A | Thậm chí, trước mỗi lần đi khám, bà dùng thuốc gây tê bôi vào nướu của con gái để nước bọt chảy ròng ròng, từ đó thuyết phục bệnh viện thực hiện phẩu thuật cắt bỏ tuyến nước bọt của cô bé. | 12s |
| `2.10` | NGHỈ | — | | 2s |
| `2.11` | LỜI | A | Tại sao cả một hệ thống y tế hiện đại với hàng trăm bác sĩ lại không phát hiện ra? *DẪN: nhấn mạnh, hơi chậm* | 6s |
| `2.12` | LỜI | A | Khi lật lại hồ sơ điều tra, các chuyên gia tội phạm học nhận thấy bà Dee Dee sở hữu một Phương thức hành động (Modus Operandi) cực kỳ tinh vi: | 9s |
| `2.13` | LỜI | A | **Thứ nhất**, bà từng làm hộ lý, nên bà nắm rất rõ các thuật ngữ y khoa và biết cách mô tả triệu chứng sao cho khớp với sách giáo khoa nhất. | 9s |
| `2.14` | LỜI | A | **Thứ hai**, năm 2005, khi cơn bão Katrina quét qua bang Louisiana, bà Dee Dee đã lợi dụng thảm họa này để tuyên bố rằng toàn bộ hồ sơ bệnh án gốc và giấy khai sinh của Gypsy đã bị lũ cuốn trôi. Từ giây phút đó, mọi lịch sử y tế của Gypsy đều do một mình miệng bà Dee Dee đọc cho các bác sĩ mới ghi chép lại. | 21s |
| `2.15` | SFX | — | Tiếng khóa cửa sắt "Cạch" *(đè lên `2.16`)* | 0s |
| `2.16` | LỜI | A | **Và thứ ba:** bất cứ khi nào có một bác sĩ bắt đầu nghi ngờ – như tiến sĩ Bernardo Flasterstein, người từng ghi vào hồ sơ năm 2007 rằng ông nghi ngờ người mẹ mắc hội chứng tâm lý giả bệnh – bà Dee Dee lập tức cắt đứt liên lạc, đổi bệnh viện và chuyển chỗ ở. | 25s |
| `2.17` | LỜI | A | Trong ngôi nhà màu hồng do các quỹ từ thiện xây tặng, những cánh cửa sổ luôn bị đóng kín. Gypsy không được đi học vì mẹ nói cô bị thiểu năng trí tuệ. Cô bị khai gian tuổi nhỏ hơn thực tế 4 năm để mãi mãi là một đứa trẻ vị thành niên dưới quyền giám hộ tuyệt đối của mẹ. Một nhà tù không có chấn song sắt, nhưng được xây bằng những đơn thuốc, những chiếc ống truyền dịch và ánh hào quang của lòng từ thiện. | 28s |
| `2.18` | **CẦN VIẾT** | A | *(bỏ qua — xem mục 8.2)* | **133s** |

> Hồi 2 · hiện có **187s** lời · mục tiêu **320s** · thiếu 133s (≈457 từ)

### ▸ HỒI 3 — GIẢI PHẪU TÂM LÝ (09:30 – 16:00)

| Mã | LOẠI | GIỌNG | NỘI DUNG | THỜI LƯỢNG |
|---|---|---|---|---|
| `3.1` | NGHỈ | — | | 2s |
| `3.2` | LỜI | A | Đến đây, câu hỏi lớn nhất mà bất kỳ ai cũng phải đặt ra là: **Tại sao?** *DẪN: dừng hẳn trước "Tại sao"* | 5s |
| `3.3` | LỜI | A | Một người mẹ có thể nhận được gì khi biến đứa con khỏe mạnh của mình thành một phế nhân đau đớn suốt hơn hai thập kỷ? | 14s |
| `3.4` | LỜI | A | Nhiều người vội vàng kết luận rằng bà Dee Dee làm vậy để trục lợi tiền từ thiện, những chuyến đi chơi miễn phí tại Disneyland hay ngôi nhà của tổ chức Habitat for Humanity. Nhưng dưới góc nhìn của tâm lý học tội phạm và tâm thần học pháp y, tiền bạc chỉ là phần thưởng phụ. Động cơ cốt lõi điều khiển toàn bộ hành vi của Dee Dee Blanchard nằm ở một căn bệnh tâm lý mang tên: **Hội chứng Münchausen qua trung gian** (Münchausen Syndrome by Proxy) – hay trong cẩm nang chẩn đoán tâm thần DSM-5-TR hiện đại gọi là **Rối loạn giả bệnh áp đặt lên người khác** (FDIA). | 41s |
| `3.5` | NGHỈ | — | | 2s |
| `3.6` | LỜI | A | Hãy cùng bóc tách 3 tầng tâm lý bên trong bộ não của một kẻ mắc hội chứng này. | 8s |
| `3.7` | LỜI | A→B | **Tầng thứ nhất: Cơn nghiện ánh hào quang của** ▸"Vị thánh tử đạo". | 7s |
| `3.8` | LỜI | A | Trong tâm lý học, người mắc tội phạm lừa đảo thông thường sẽ giả bệnh để lấy tiền bảo hiểm rồi trốn đi hưởng thụ – đó gọi là Malingering (Giả bệnh trục lợi). Nhưng người mắc hội chứng Münchausen thì khác: thứ họ đói khát không phải là tiền, mà là sự chú ý, sự thương cảm và sự tôn sùng về mặt cảm xúc. | 19s |
| `3.9` | LỜI | A | Trước khi có Gypsy, cuộc đời của Dee Dee là một chuỗi những thất bại: bị gia đình xa lánh vì thói tắt mắt, hôn nhân tan vỡ ở tuổi 24. Bà là một cái bóng mờ nhạt trong xã hội. | 14s |
| `3.10` | **CẦN VIẾT** | A | *(bỏ qua — xem mục 8.3)* | **140s** |
| `3.11` | LỜI | A | Nhưng ngay khi đóng vai "người mẹ đơn thân kiên cường của một đứa trẻ sắp chết", Dee Dee bỗng nhiên trở thành trung tâm của vũ trụ. Đi đến đâu bà cũng được các bác sĩ nể trọng, được hàng xóm rơi nước mắt cảm phục, được báo chí địa phương ca ngợi như một vị thánh sống. Mỗi lần Gypsy phải nhập viện cấp cứu là một lần não bộ của Dee Dee được tiêm một liều Dopamine cực mạnh từ sự quan tâm của đám đông. | 31s |
| `3.12` | NGHỈ | — | | 1,5s |
| `3.13` | LỜI | A | **Tầng thứ hai: Nỗi sợ bị bỏ rơi bệnh lý và nhu cầu kiểm soát tuyệt đối.** | 5s |
| `3.14` | LỜI | A | Theo lời khai của chính gia đình bên ngoại, Dee Dee là một người phụ nữ có nhu cầu kiểm soát cực đoan. Khi còn trẻ, bà từng bị gia đình nghi ngờ đã bỏ thuốc diệt cỏ vào thức ăn của mẹ kế, và bỏ đói chính mẹ ruột của mình khi bà cụ nằm liệt giường. | 17s |
| `3.15` | LỜI | A | Khi sinh ra Gypsy, Dee Dee nhìn thấy ở đứa trẻ này một vật sở hữu duy nhất không bao giờ được phép rời bỏ bà. Nhưng một đứa trẻ khỏe mạnh rồi sẽ lớn lên, sẽ đi học, sẽ có bạn bè, sẽ yêu đương và rời xa mẹ. Làm thế nào để giữ một con người ở bên cạnh mình mãi mãi? | 19s |
| `3.16` | NGHỈ | — | Hạ giọng trầm, chậm rãi | 2s |
| `3.17` | LỜI | A | Câu trả lời tăm tối mà tâm trí lệch lạc của Dee Dee tìm ra chính là: **Hãy làm cho con bé tàn tật và phụ thuộc hoàn toàn vào mình.** Khi Gypsy không thể tự bước đi, không thể tự ăn uống mà phải truyền qua ống thông dạ dày, Dee Dee trở thành vị Chúa tể duy nhất nắm giữ sự sống của con gái. | 20s |
| `3.18` | LỜI | A | **Và tầng thứ ba: Dấu ấn tâm lý (Signature) của sự xóa bỏ nhân dạng.** | 4s |
| `3.19` | LỜI | A | Các nhà lập hồ sơ tội phạm đặc biệt chú ý đến chi tiết bà Dee Dee thường xuyên cạo trọc đầu Gypsy và bắt cô mặc những bộ váy công chúa sặc sỡ của trẻ con ngay cả khi cô đã hơn 20 tuổi. Đó không chỉ là việc giả bệnh ung thư. Đó là hành vi Tước đoạt sự trưởng thành (Infantilization). Bà không cho phép cơ thể Gypsy phát triển thành một người phụ nữ. Trong kịch bản tưởng tượng của Dee Dee, Gypsy phải mãi mãi là một con búp bê sứ 7 tuổi, yếu ớt, vô tính và hoàn toàn nằm gọn trong lòng bàn tay bà. | 33s |

> Hồi 3 · hiện có **210s** lời · mục tiêu **350s** · thiếu 140s (≈481 từ)

### ▸ HỒI 4 — GÓC NHÌN NẠN NHÂN (16:00 – 21:30)

| Mã | LOẠI | GIỌNG | NỘI DUNG | THỜI LƯỢNG |
|---|---|---|---|---|
| `4.1` | LỜI | A | Khi vụ án được đưa ra ánh sáng, có một luồng dư luận đã đặt ra câu hỏi đầy hoài nghi dành cho Gypsy Rose: | 10s |
| `4.2` | LỜI | A | "Cô ấy biết rõ đôi chân mình không hề bị liệt. Mỗi tối khi ở trong phòng kín, cô ấy vẫn tự đứng dậy đi lại. Vậy tại sao trong suốt từng năm, trước mặt hàng trăm bác sĩ, cảnh sát và đám đông, Gypsy không một lần đứng phắt dậy khỏi chiếc xe lăn để tố cáo mẹ mình?" *DẪN: trăn trở, đặt câu hỏi* | 25s |
| `4.3` | NGHỈ | — | | 2s |
| `4.4` | LỜI | A | Để trả lời câu hỏi này, chúng ta không thể dùng tư duy của một người trưởng thành tự do để áp đặt lên một đứa trẻ lớn lên trong lồng kính. Tâm lý học tội phạm giải thích sự im lặng của Gypsy qua hai cơ chế cực kỳ sâu sắc: **Sự gắn kết chấn thương** (Trauma Bonding) và **Sự bất lực tập nhiễm** (Learned Helplessness). | 25s |
| `4.5` | SFX | — | Tiếng xiềng xích, kim loại va chạm nhẹ *(đè lên `4.6`)* | 0s |
| `4.6` | LỜI | A→B | Khái niệm Sự bất lực tập nhiễm được nhà tâm lý học **Martin Seligman** phát hiện từ năm 1967. Khi một sinh vật bị đặt vào môi trường chịu đựng sự đau đớn lặp đi lặp lại mà mọi nỗ lực phản kháng đều vô ích, bộ não sẽ đi đến một kết luận cố định: ▸"Mọi sự vùng vẫy đều vô nghĩa". Kể từ giây phút đó, ngay cả khi cánh cửa lồng đã mở toang, con vật cũng sẽ nằm im chịu trận chứ không bao giờ bước ra nữa. | 33s |
| `4.7` | LỜI | A | Hãy nhìn vào thế giới quan của Gypsy từ lúc mới biết nhận thức: | 6s |
| `4.8` | LỜI | A | Mỗi khi ngồi trước mặt bác sĩ, bà Dee Dee luôn nắm chặt lấy tay Gypsy. Với người ngoài, đó là cử chỉ âu yếm của một người mẹ. Nhưng với Gypsy, đó là một mật lệnh đe dọa: nếu cô bé nói sai dù chỉ một lời, hoặc tỏ ra mình khỏe mạnh, cái nắm tay ấy sẽ siết chặt lại đến mức bầm tím. Và khi cánh cửa ngôi nhà màu hồng khép lại sau buổi khám bệnh, những trận đòn bằng móc áo, việc bị bỏ đói và bị trói vào thành giường suốt hai tuần liền sẽ chờ đợi cô. | 30s |
| `4.9` | NGHỈ | — | | 1,5s |
| `4.10` | LỜI | A | Thực tế, Gypsy đã từng cố gắng tự cứu mình. | 3s |
| `4.11` | LỜI | A | Năm 2011, ở tuổi 19, cô đã từng lén trốn khỏi nhà vào ban đêm để tìm đến một người quen. Nhưng chỉ vài giờ sau, bà Dee Dee đã lần ra dấu vết. Trước mặt những người định giúp đỡ Gypsy, bà Dee Dee rút ra tập giấy tờ giả mạo chứng minh Gypsy là trẻ vị thành niên bị thiểu năng trí tuệ và mất năng lực hành vi dân sự. Mọi người tin lời người mẹ "thánh thiện" và trao trả Gypsy về lại ngôi nhà màu hồng. | 27s |
| `4.12` | LỜI | A | Đêm hôm đó, bà Dee Dee đã dùng búa đập nát chiếc máy tính của con gái và đe dọa sẽ đập nát các ngón tay của cô nếu cô còn dám bước ra khỏi cửa một lần nữa. *DẪN: lắng xuống* | 11s |
| `4.13` | NGHỈ | — | | 2s |
| `4.14` | LỜI | A | Cú sốc năm 2011 ấy đã đóng chiếc đinh cuối cùng vào nhận thức của Gypsy: Xã hội ngoài kia sẽ không bao giờ tin lời một đứa trẻ bị coi là thiểu năng, họ chỉ tin người mẹ vĩ đại của cô. | 20s |
| `4.15` | LỜI | A→B | Và bên cạnh nỗi sợ hãi, giữa hai mẹ con họ còn tồn tại Gắn kết chấn thương (Trauma Bonding). Dee Dee là người đầu độc Gypsy, nhưng cũng chính Dee Dee là người duy nhất ôm ấp cô mỗi đêm, chải chuốt và gọi cô là ▸"thiên thần nhỏ của mẹ". Sự đan xen giữa bạo hành thể xác và sự nuông chiều ngột ngạt đã làm tê liệt khả năng phân định ranh giới của Gypsy. | 33s |
| `4.16` | **CẦN VIẾT** | A | *(bỏ qua — xem mục 8.4)* | **80s** |
| `4.17` | SFX | — | Tiếng bàn phím gõ lạch cạch trong đêm *(đè lên `4.18`)* | 0s |
| `4.18` | LỜI | A | Khi mọi lối thoát hợp pháp đều bị bịt kín trong tư tưởng, bộ não bị dồn nén suốt 23 năm ấy đã chọn một lối thoát cực đoan nhất. Qua mạng Internet, Gypsy quen biết Nicholas Godejohn – một thanh niên có tiền sử rối loạn phổ tự kỷ và nhân cách bất ổn. Hai tâm hồn khép kín trượt vào hiệu ứng tâm lý Folie à Deux – Điên cuồng đôi. Gypsy tin rằng chỉ khi mẹ cô biến mất, cô mới được phép sống cuộc đời của một con người. Và đêm tháng 6 năm 2015, bi kịch đã nổ ra khi Gypsy mở cửa cho Godejohn bước vào ngôi nhà màu hồng… | 47s |

> Hồi 4 · hiện có **215s** lời · mục tiêu **295s** · thiếu 80s (≈275 từ)

### ▸ HỒI 5 — PHÁN QUYẾT & LỜI KẾT (21:30 – 25:00)

| Mã | LOẠI | GIỌNG | NỘI DUNG | THỜI LƯỢNG |
|---|---|---|---|---|
| `5.1` | SFX | — | Tiếng búa tòa án gõ "Cốp" vang vọng *(đè lên `5.2`)* | 0s |
| `5.2` | LỜI | A | Trước tòa án bang Missouri, vụ án của Gypsy Rose Blanchard đã tạo ra một cuộc tranh luận pháp lý và đạo đức chưa từng có tiền lệ. | 8s |
| `5.3` | LỜI | A→B | Về mặt luật pháp, hành vi lên kế hoạch sát hại mẹ ruột là một trọng tội không thể chối cãi. Nhưng dưới góc độ tâm thần học pháp y, chánh biện lý hạt Greene – ông Dan Patterson – ▸đã thừa nhận rằng đây là một trong những vụ án đặc biệt nhất sự nghiệp của ông: một vụ án mà kẻ chủ mưu đồng thời cũng là nạn nhân của một quá trình bạo hành y khoa kéo dài hơn hai thập kỷ. | 25s |
| `5.4` | NGHỈ | — | | 1,5s |
| `5.5` | LỜI | A | Năm 2016, Gypsy Rose nhận mức án 10 năm tù giam cho tội giết người cấp độ hai – mức án thấp nhất có thể nhờ các tình tiết giảm nhẹ đặc biệt về tâm lý. | 17s |
| `5.6` | LỜI | B ★ | Điều chua xót nhất mà các nhà tâm lý học ghi nhận được là câu nói của Gypsy khi ở trong trại giam: ▸"Ở trong nhà tù của pháp luật, lần đầu tiên trong đời tôi cảm thấy mình được tự do hơn cả khi sống trong ngôi nhà của mẹ." *DẪN: GIỌNG B, chậm, nặng — khoảnh khắc thấm nhất của cả tập* | 14s |
| `5.7` | LỜI | A | Cuối tháng 12 năm 2023, sau khi chấp hành 85% bản án, cô đã chính thức được trả tự do. | 6s |
| `5.8` | NGHỈ | — | | 2s |
| `5.9` | LỜI | A | Nhìn lại toàn bộ hồ sơ vụ án này, các chuyên gia tội phạm học và y khoa đã đúc kết **4 dấu hiệu cảnh báo đỏ** (Red Flags) để cộng đồng có thể nhận diện sớm Hội chứng Münchausen qua trung gian trước khi bi kịch xảy ra: | 20s |
| `5.10` | LỜI | A | **Thứ nhất:** một đứa trẻ hoặc người phụ thuộc có bệnh sử dày đặc, kỳ lạ, kéo dài triền miên nhưng các kết quả xét nghiệm khách quan luôn mâu thuẫn với lời mô tả của người chăm sóc. | 16s |
| `5.11` | LỜI | A | **Thứ hai:** các triệu chứng bệnh chỉ xuất hiện khi có mặt người chăm sóc trực tiếp, và thuyên giảm rõ rệt ngay khi bệnh nhân được cách ly hoặc có camera giám sát. | 14s |
| `5.12` | LỜI | A | **Thứ ba:** người chăm sóc tỏ ra quá hào hứng với các thủ thuật y khoa đau đớn, thích phô trương bệnh tật của con lên mạng xã hội để tìm kiếm sự tung hô, và lập tức đổi bác sĩ mỗi khi có ai đó đặt câu hỏi nghi vấn. | 18s |
| `5.13` | LỜI | A→B | **Và thứ tư:** nạn nhân bị cô lập khỏi trường học, bạn bè và người thân khác trong gia đình dưới lý do ▸"bảo vệ sức khỏe". | 11s |
| `5.14` | **CẦN VIẾT** | A | *(bỏ qua — xem mục 8.5)* | **9s** |
| `5.15` | NGHỈ | — | Nhạc Piano dâng nhẹ lên | 2,5s |
| `5.16` | LỜI | A | Hồ sơ về ngôi nhà màu hồng tại Missouri khép lại, nhưng dư âm của nó vẫn là một lời nhắc nhở gai góc về bản chất đa diện của tâm lý con người. | 10s |
| `5.17` | LỜI | A | Tình yêu thương chân chính luôn hướng tới việc giúp một đứa trẻ lớn lên khỏe mạnh, độc lập và tự bước đi trên đôi chân của mình. Khi tình thương bị biến tướng thành chiếc lồng giam cầm, khi sự chăm sóc trở thành công cụ để thỏa mãn cái tôi ích kỷ của người lớn… thì thứ khoác áo thiên thần ấy đôi khi lại mang sức tàn phá khủng khiếp không kém bất kỳ tội ác nào. *DẪN: trầm ấm, truyền cảm* | 23s |
| `5.18` | NGHỈ | — | | 1,5s |
| `5.19` | LỜI | A | Cảm ơn bạn đã dành thời gian lắng nghe và cùng tôi đi đến tận cùng của hồ sơ tâm lý ngày hôm nay. Hãy để lại góc nhìn của bạn ở phần bình luận, giữ cho mình một tâm trí tỉnh táo, và hẹn gặp lại bạn trong tập giải phẫu tâm lý tội phạm tiếp theo. | 16s |
| `5.20` | SFX | — | Tiếng gấp tập hồ sơ giấy "Bụp", tiếng tắt máy ghi âm "Tách" | 0s |
| `5.21` | NHẠC | — | Piano ngân dài 5 giây rồi nhỏ dần đến khi tắt hẳn (Fade out) | 5s |
| `5.22` | NGHỈ | — | Im lặng trước khi tắt hẳn | 3s |

> Hồi 5 · hiện có **171s** lời · mục tiêu **180s** · thiếu 9s (≈31 từ)

---

## 5. BẢNG TỔNG HỢP

| Hồi | Lời hiện có | Mục tiêu | Cần thêm |
|---|---:|---:|---:|
| Mở đầu | 5s | 18s | — |
| Hồi 1 | 136s | 180s | +151 từ |
| Hồi 2 | 187s | 320s | +457 từ |
| Hồi 3 | 210s | 350s | +481 từ |
| Hồi 4 | 215s | 295s | +275 từ |
| Hồi 5 | 171s | 180s | +31 từ |
| **Cộng lời** | **924s** | **1.343s** | **+1.395 từ** |
| Nghỉ + dạo chuyển | | ~157s | |
| **TỔNG (bản đầy đủ)** | | **≈24:42** ✔ | |
| **TỔNG (bản demo, bỏ ô trống)** | | **≈17:50** | |

---

## 6. QUY TRÌNH THỰC THI

```
BƯỚC 1  Parse file này → lấy đúng 58 block theo bảng ở mục 4, theo đúng thứ tự.
         Bỏ qua 5 ô "CẦN VIẾT". Bóc định dạng theo R1.
         → danh sách block: {ma, loai, giong, noi_dung, thoi_luong}

BƯỚC 2  Với mỗi block LỜI:
           - tách đoạn trước/sau ▸ → 1 hoặc 2 yêu cầu TTS
           - dựng payload theo mục 2 (model, voice_id, emotion, speed)
         → file batch_args.json dạng {"requests": [{text, voice_id, emotion,
           speed, pitch, volume, output_file}, ...]}

BƯỚC 3  Gọi endpoint batch của MiniMax → nhận {node_id, download_url}
         → tải về .work/audio/<ma>.mp3   (dùng lại .work/download.py)

BƯỚC 4  Ghép: ffmpeg concat theo đúng thứ tự mục 4,
         chèn khoảng lắng thật cho mỗi block NGHỈ bằng
             -f lavfi -i anullsrc=r=32000:cl=mono -t <so giay>
         (KHÔNG dùng dấu "..." — sẽ bị đọc thành tiếng)

BƯỚC 5  Trộn BGM/SFX theo timeline, áp mức dB ở mục 3.
         Thiếu file → bỏ qua im lặng (R3).

BƯỚC 6  Kiểm tra: ffprobe thời lượng, đối chiếu cột THỜI LƯỢNG.
         Lệch >5% → báo lại, không tự sửa.
```

**ffmpeg có sẵn tại:** `.work\ffmpeg\ffmpeg-n9.0-latest-win64-lgpl-shared-9.0\bin\`

---

## 7. DANH MỤC FILE ÂM THANH

Đặt file vào `D:\TEST\Gax\Audi\assets\sfx\` và `D:\TEST\Gax\Audi\assets\bgm\`.

> **Trạng thái 21/10/2026: 7/9 lớp BGM đã tạo thật** bằng connector `batch_text_to_music`, nằm trong `assets\bgm\`. 9 file SFX chưa có.

### BGM — ĐÃ TẠO ✅

| File | Thời lượng |
|---|---:|
| `bgm_music_box.mp3` | 22,4s |
| `bgm_sub_drone.mp3` | 30,5s |
| `bgm_cello_sad.mp3` | 25,7s |
| `bgm_cello_sad_v2.mp3` | 38,1s |
| `bgm_piano_minimal.mp3` | 25,2s |
| `bgm_piano_minimal_v2.mp3` | 14,6s |
| `bgm_piano_warm.mp3` | 77,2s |
| `bgm_violin_heart.mp3` | 36,0s |
| `bgm_ambient_deep.mp3` | 22,8s |

> **Giới hạn quan trọng:** mỗi đoạn chỉ **14–77 giây**, trong khi cần chạy nền hàng chút phút. Phải **loop bằng ffmpeg**:
> ```
> ffmpeg -stream_loop -1 -i bgm_cello_sad.mp3 -i voice.mp3 \
>        -filter_complex "[0:a]volume=-26dB[a];[1:a][a]amix=inputs=2:duration=first" \
>        -c:a libmp3lame -b:a 128k out.mp3
> ```
> Lớp **vân/không gian** (`sub_drone`, `ambient_deep`, `music_box`) loop khéo không nhận ra.
> Lớp **melodic** (`cello`, `piano`, `violin`) phải **xoay vòng 2 bản `_v2`** để không lặp lộ — đã tạo sẵn bản `_v2` cho cello và piano.

### SFX — CHƯA CÓ (9 file)

| Mã | File dự kiến | Mô tả | BẮT BUỘC | Dùng tại |
|---|---|---|---|---|
| `sfx_police_far` | `sfx/police_far.wav` | Còi xe cảnh sát vọng xa + gõ cửa | KHÔNG | `O.1` |
| `sfx_radio_footsteps` | `sfx/radio_steps.wav` | Bộ đàm rè + bước chân hối hả | KHÔNG | `1.1` |
| `sfx_recorder_on` | `sfx/recorder_click.wav` | Bật máy ghi âm "Tách" | KHÔNG | `1.10` |
| `sfx_paper_files` | `sfx/paper_files.wav` | Lật giấy hồ sơ sột soạt | KHÔNG | `2.1` |
| `sfx_lock_door` | `sfx/lock_door.wav` | Khóa cửa sắt "Cạch" | KHÔNG | `2.15` |
| `sfx_chains` | `sfx/chains.wav` | Xiềng xích, kim loại va nhẹ | KHÔNG | `4.5` |
| `sfx_keyboard` | `sfx/keyboard_night.wav` | Bàn phím gõ lạch cạch | KHÔNG | `4.17` |
| `sfx_gavel` | `sfx/gavel.wav` | Búa tòa án "Cốp" | KHÔNG | `5.1` |
| `sfx_folder_close` | `sfx/folder_close.wav` | Gấp hồ sơ + tắt máy ghi âm | KHÔNG | `5.20` |

**Phân bổ BGM theo hồi** (file đã tạo, mục "BGM — ĐÃ TẠO" ở trên):

| Hồi | File dùng |
|---|---|
| Mở đầu `O.2` | `bgm_music_box.mp3` + `bgm_sub_drone.mp3` (từ 12s) |
| `1.11` | `bgm_cello_sad.mp3` |
| Hồi 2 | `bgm_piano_minimal.mp3` + `bgm_piano_minimal_v2.mp3` xoay vòng |
| Hồi 3 | `bgm_ambient_deep.mp3` |
| Hồi 4 | `bgm_violin_heart.mp3` |
| `5.15` `5.21` | `bgm_piano_warm.mp3` |

> **Không có file nào là bắt buộc.** Bản demo chạy được với 0 file âm thanh — chỉ mất lớp âm thanh, phần lời vẫn nguyên vẹn. Điều này có chủ ý để bạn nghe được giọng đọc trước khi đầu tư công sức làm nhạc.

---

## 8. NỘI DUNG CẦN BỔ SUNG

Thêm đúng **4 chỗ lớn + 1 chốt**. Đây là các vị trí hồ sơ đang hụt mạch nhất — thêm chỗ khác sẽ không đạt mục tiêu.

### 8.1 · `1.9` — Hồi 1 · +151 từ / 44s
**Đang thiếu:** đoạn nối cảm xúc giữa "phơi bày sự thật" và lời chào mừng. Hiện tập nhảy thẳng, thiếu khoảng lặng tâm lý.
**Viết về:** vì sao câu chuyện này đáng được kể — quy mô tội phạm y khoa chưa từng có, 23 năm, một hệ thống y tế bị lừa. Có thể dẫn 1–2 dữ kiện quốc tế: ước tính mỗi năm có hàng nghìn ca Munchausen by Proxy ở Mỹ, tỉ lệ tử vong trẻ sơ sinh trong các ca đó.

### 8.2 · `2.18` — Hồi 2 · +457 từ / 133s
**Khoảng trống lớn nhất.** Hồi 2 mới có 665 từ cho mục tiêu 6 phút.
**Chọn 3 trong 5:**
1. **Vụ cắt tuyến nước bọt** — số lần phẫu thuật, hậu quả, Gypsy mất ăn uống qua miệng bao lâu.
2. **Dee Dee bắt đầu thế nào** — không ai nghi ngờ lúc mới sinh; các bác sĩ đầu tiên tin cô hoàn toàn.
3. **Chi phí** — bao nhiêu tiền bảo hiểm, quỹ từ thiện, chi phí y tế bị tạo ra; nền cho câu "tiền chỉ là phần thưởng phụ" ở Hồi 3.
4. **Góc nhìn hàng xóm / báo chí địa phương** — những người tin cô nhất, và khoảnh khắc họ hiểu ra sai.
5. **Các chẩn đoán sai** — Gypsy từng bị chẩn đoán bao nhiêu bệnh khác nhau trước khi "ung thư máu".

### 8.3 · `3.10` — Hồi 3 · +481 từ / 140s
**Thiếu nhiều nhất tập**, nằm đúng giữa Tầng 1 và Tầng 2. Hiện Tầng 1 kết thúc rất cụt.
**Viết về:**
1. **Mảnh ghép còn thiếu** — FDIA thường đi kèm chẩn đoán nào ở người mẹ (Narcissistic Personality Disorder, Histrionic, hoặc chính Munchausen tự thân).
2. **Vòng lặp khen–thưởng** — Gypsy khóc → Dee Dee "cứu" → được tung hô → cần lần nữa. Nêu khái niệm Intermittent Reinforcement.
3. **Vì sao bác sĩ không nghi ngờ** — tâm lý y sĩ tự nhiên muốn tin bệnh nhân; hiệu ứng đồng cảm và áy lực chữa bệnh bị khai thác.
4. **Martin Seligman** — dẫn tiếp sang Tầng 2: thí nghiệm chuột, bài học về học theo bất lực.

### 8.4 · `4.16` — Hồi 4 · +275 từ / 80s
Hồi 4 ngắn hơn mục tiêu gần 1,5 phút, đúng chỗ nặng cảm xúc nhất.
1. **Góc nhìn Gypsy** — cô gái lớn lên tin mình bệnh, tin mình không có khả năng, tin mình nợ mẹ sự sống.
2. **Godejohn** — mối quan hệ bắt đầu thế nào, mức độ phụ thuộc lẫn nhau.
3. **Đêm 14/6/2015** — dựng lại chi tiết: chuông cửa, giờ, ai mở cửa, diễn biến.

### 8.5 · `5.14` — Hồi 5 · +31 từ / 9s
Một câu chuyển tiếp trước lời kết — nhắc rằng 4 dấu hiệu này không chỉ áp dụng cho vụ án Blanchard.

---

## 9. LỖI ĐÃ SỬA TRONG BẢN PLAN NÀY

So với `Kc_1.txt`, các lỗi dưới **đã được sửa ngay trong timeline**:

| # | Vị trí | Lỗi gốc | Đã sửa thành |
|---|---|---|---|
| 1 | `3.19` | Chữ Hán lạ `성` trong "vô성 (vô tính)" | "vô tính" |
| 2 | `4.18` | "trong tâm tưởng" | "trong tư tưởng" |
| 3 | `4.2` | "trong suốt từng ấy năm" | "trong suốt từng năm" |
| 4 | `3.3` | "thập kỷ?Nhiều người" (dính liền) | "thập kỷ? Nhiều người" |
| 5 | `5.9` | "xảy ra:Thứ nhất" (dính liền) | "xảy ra: Thứ nhất" |
| 6 | Toàn tập | Cue `[BGM]` `[SFX]`, tiêu đề `HỒI N` lọt vào lời | Đã loại hết |
| 7 | Toàn tập | Trộn `'` và `"` | Chuẩn hóa về `"…"` |

---

## 10. LƯU Ý KỸ THUẬT CHO AI

**Đừng dùng regex tổng quát để parse `Kc_1.txt`.** File đó bị nén còn 32 dòng, cue nằm giữa dòng, và dấu `]` trong cue **không khớp ranh giới nội dung** — regex `[^\]]*` sẽ nuốt mất 750 từ lời thoại. Đã kiểm chứng.

**Dùng nội dung trong file này làm nguồn**, không cần đọc lại `Kc_1.txt`.

Nguồn `voice_id`: [MiniMax System Voice ID List](https://platform.minimax.io/docs/faq/system-voice-id)

---

*Bản v2. `Kc_1.txt` và `Kich_ban.txt` không bị sửa.*