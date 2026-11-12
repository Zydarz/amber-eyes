# HỒ SƠ SẢN XUẤT TẬP 01 · "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A) — các mã A0…A13 trong file này trỏ về đó.
**Kịch bản:** `01_KICH_BAN/Tap01/` · **Thành phẩm:** `02_SAN_XUAT/Tap01/xuat_ban/`
**Dùng làm mẫu:** tập mới sao chép file này thành `02_SAN_XUAT/TapXX/KeHoach_Video_TapXX.md` rồi thay nội dung.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md` — **viết lại 09/11/2026** (205 câu, 10 chỉ dấu tâm lý) |
| Lượt nói / câu / từ | 33 / **205** / 5679 — Host 41% · Điều tra viên 28% · Chuyên gia tâm lý 25% · Người dân (Cừu) 3% · Khán giả (Mèo) 2% |
| N1 / N2 | `1.07` Người dân (Cừu) / `4.03` Khán giả (Mèo) |
| Thời lượng đo | **1753,36 s (29:13)** — intro 0–22,41 s (`.work/timeline_s.json`, mốc đo bằng ASR master) |
| Mốc hồi | Hồi 2 · 06:08 · Hồi 3 · 11:53 · Hồi 4 · 16:46 · Hồi 5 · 22:30 |
| Bảng shot | **203 dòng** = 198 shot có lời + 5 dòng không lời (4 thẻ chuyển hồi T10 + 1 thẻ kết) |
| Nền dùng | **44 ảnh** `assets/bg/` (dùng chung cho cả 3 ngôn ngữ — H17) |
| Ảnh tĩnh | **203 ảnh** 1920×1080 (`.work/video3/stills/`) — cổng QC trước khi dựng video (H9) |
| Ngoại lệ H10 vế 1 | 7 shot > 15 s · 2 shot < 3 s — câu khiếu ngôn ngữ nói dài hơn 15 s, **không cắt được** vì chữ phải nguyên văn (H6/V3) |

## B2. Kết quả và việc còn lại

| Hạng mục | Kết quả |
|---|---|
| Kịch bản | Viết lại 09/11/2026: 205 câu / 5 hồi · mã câu giữ nguyên cấu trúc, đồng bộ 1-1 cho VN·EN·JA |
| Timeline | Đo thật từ master mp3 mới bằng ASR (faster-whisper `small`, căn chỉnh theo độ phủ ký tự + mốc từ thật): **VN 205/205 · EN 205/205 · JA 201/205** câu khớp ≥ 0,45 (cổng G1 ≥ 97% — đạt) |
| Bảng shot | 203 dòng · phủ 205/205 câu · chữ trên hình = **nguyên văn câu kịch bản** (H6/V3, QC 0 lỗi) |
| Ảnh tĩnh | 203 ảnh/ngôn ngữ · QC H9 (độ tương phản chữ — 57 shot bật `text_scrim`), H10 (thời lượng + nền lặp), H12 (thẻ kết), H13 (khớp 3 chiều) — xem `BaoCao_QC_Tap01_20261109.md` |
| Video hoàn thiện | Đã dựng & xuất bản video cả 3 ngôn ngữ (12/11/2026): VN (1.753 s, 665 MB), EN (1.669 s, 632 MB), JA (1.959 s, 740 MB). 100% đạt chuẩn QC (H14, A7, A1, H17) — xem `BaoCao_DungVideo_Tap01_20261112.md` |
| Phụ đề & Đóng gói | Đã sinh phụ đề SRT (VN 466, EN 475, JA 414 cues), thumbnail 3 thứ tiếng, mô tả đầy đủ mốc chương |
| **Còn lại trước khi đăng** | ① Điền nguồn cho 9 mã câu trong `need` · ② Người dùng nghe duyệt toàn tập |

## B3. Ánh xạ riêng của Tập 01 (trong `parse_shots.py`)

| Biến | Giá trị |
|---|---|
| `COMBO` / `INSET` / `BG2` | **rỗng** — bảng shot mới ghi nền trực tiếp trong cột *Nền* (mã shot cũ không còn tồn tại) |
| `route_pins` | `1-29` → ("SPRINGFIELD, MISSOURI", "WISCONSIN") (mẫu T7 tuyến đường) |
| `text_scrim` | 57 shot cần lớp tối mềm (đo H9, hợp 3 ngôn ngữ) |
| Nhân vật | `n_element`: `1.07` → N1 (Cừu) · `4.03` → N2 (Mèo) |

## 6. DANH SÁCH SHOT — TẬP 01 (bảng mẫu, viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `✦` = lần đầu xuất hiện (thẻ giới thiệu) · `→X` = đổi vai · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `◼` tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` (chỉ hình, shot I-01 → I-04, chi tiết ở A5.7) ở 0,00 s. Không câu thoại nào thuộc intro.

### HỒI 1 — KHOẢNH KHẮC ĐỨT GÃY NIỀM TIN & ĐIỂM MÙ XÃ HỘI · nền chủ đạo `house_night`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.03#1`–`#2` (8,8 s) | H | T1 | `house_night`, `pull` | **Ngày 14 tháng 6 năm 2015.** → *Tại thị trấn yên bình Springfield thuộc bang Missouri, nước Mỹ.* | — | ✦ Cú |  |
| 1-02 | `1.03#3` (6,7 s) | H | T1 | `night_street`, `still` | *Đó là một buổi tối mùa hè ngột ngạt khi màn đêm bắt đầu bao trùm lên những con phố ngoại ô tĩnh lặng.* | — | — |  |
| 1-03 | `1.03#4` (11,2 s) | H | T1 | `phone_dark`, `push` | *Trên trang Facebook chung của hai mẹ con nổi tiếng nhất vùng – bà Dee Dee Blanchard và cô con gái tật nguyền Gypsy Rose – bỗng xuất hiện một dòng trạng thái ngắn ngủi đầy hằn học.* | — | — |  |
| 1-04 | `1.03#5` (7,3 s) | H | T1 | `phone_dark`, `pan` | *Dòng tin nhắn thông báo rằng người mẹ đã qua đời trong căn nhà nhỏ, khiến cả khu phố rơi vào hoảng loạn tột cùng.* | — | — |  |
| 1-05 | `1.05#1` (2,0 s) | H | T1 | `crowd_house`, `pull` | *Hàng xóm lập tức vây quanh ngôi nhà nhỏ sơn màu hồng phấn ở số 2103 đường Bắc Volunteer.* | — | — |  |
| 1-06 | `1.05#2` (13,4 s) | H | T1 | `charity`, `still` | *Ngôi nhà ấy vốn được xây dựng và trao tặng bởi tổ chức từ thiện danh tiếng Habitat for Humanity.* | — | — |  |
| 1-07 | `1.05#3` (8,7 s) | H | T1 | `charity`, `push` | *Nơi đây còn được tổ chức Make-A-Wish tài trợ các chuyến du lịch trọn gói và sự hỗ trợ tài chính liên tục từ các nhà hảo tâm khắp nơi.* | — | — |  |
| 1-08 | `1.05#4` (9,2 s) | H | T1 | `crowd_house`, `pan` | *Hàng trăm tình nguyện viên và cư dân địa phương từng rơi nước mắt khi chung tay lắp đặt đoạn đường dốc dành riêng cho xe lăn trước hiên nhà.* | — | — |  |
| 1-09 | `1.05#5` (6,4 s) | H | T1 | `house_night`, `pull` | *Suốt nhiều năm ròng rã, nơi đây từng được xem là biểu tượng cao đẹp nhất của tình mẫu tử thiêng liêng.* | — | — |  |
| 1-10 | `1.05#6` (9,3 s) | H | T1 | `house_night`, `still` | *Để hiểu sự bàng hoàng và cú sốc tinh thần của cộng đồng lớn đến mức nào, chúng ta hãy lắng nghe chia sẻ từ một người dân sống cùng khu phố.* | — | →N1 |  |
| 1-11 | `1.07#1` (6,8 s) | N1 | T1 | `house_night`, `push` | *Trong mắt tất cả chúng tôi ở thị trấn này, ngôi nhà màu hồng ấy là nơi chở che một phép màu của lòng nhân ái.* | — | ✦ Cừu |  |
| 1-12 | `1.07#2` (9,3 s) | N1 | T1 | `house_night`, `pan` | *Bà Dee Dee là một người mẹ đơn thân vĩ đại, người đã từ bỏ mọi hạnh phúc riêng tư để chăm sóc cô con gái Gypsy Rose nhỏ bé bất hạnh.* | — | — |  |
| 1-13 | `1.07#3` (13,2 s) | N1 | T1 | `wheelchair_room`, `pull` | *Cô bé mắc một danh sách bệnh tật dài đặc kín: bại liệt hoàn toàn từ thắt lưng trở xuống, ung thư máu giai đoạn nặng, loạn dưỡng cơ, động kinh triền miên và trí tuệ chỉ dừng lại ở mức đứa trẻ lên bảy.* | — | — |  |
| 1-14 | `1.07#4` (7,1 s) | N1 | T1 | `wheelchair_gypsy`, `still` | *Hình ảnh người mẹ gầy gò nhẫn nại đẩy chiếc xe lăn qua từng góc phố đã in sâu vào ký ức của mọi gia đình nơi đây.* | — | — |  |
| 1-15 | `1.07#5` (5,8 s) | N1 | T1 | `crowd_house`, `push` | *Bất kỳ ai nhìn thấy hai mẹ con cũng đều nghẹn ngào rơi nước mắt cảm phục trước nghị lực phi thường của họ.* | — | — |  |
| 1-16 | `1.07#6` (5,8 s) | N1 | T1 | `house_night`, `pan` | *Chúng tôi đã hoàn toàn tin tưởng rằng bà ấy là một vị thánh sống giữa đời thực.* | — | →H |  |
| 1-17 | `1.08#1` (8,8 s) | H | T1 | `house_police`, `pull` | *Thế nhưng, khi cảnh sát quyết định phá then cửa bước vào bên trong ngôi nhà lạnh ngắt đêm hôm đó, một bức tranh hoàn toàn trái ngược đã phơi bày.* | — | — |  |
| 1-18 | `1.08#2` (5,7 s) | H | T1 | `bedroom_door`, `still` | *Người mẹ – bà Dee Dee Blanchard – được phát hiện đã bất động vĩnh viễn trên giường ngủ.* | — | ⊘ |  |
| 1-19 | `1.08#3` (5,2 s) | H | T1 | `bedroom_door`, `push` | *Không gian bên trong căn phòng nồng nặc mùi ẩm mốc và sự u ám đến nghẹt thở.* | — | — |  |
| 1-20 | `1.08#4` (4,8 s) | H | T1 | `empty_room`, `pan` | *Còn cô con gái tật nguyền Gypsy Rose thì hoàn toàn biến mất không một dấu vết.* | — | — |  |
| 1-21 | `1.08#5` (6,0 s) | H | T1 | `wheelchair_room`, `pull` | *Chiếc xe lăn chuyên dụng mà cô bé dùng để di chuyển mỗi ngày vẫn nằm im lìm trong góc phòng khách.* | — | — |  |
| 1-22 | `1.08#6` (8,6 s) | H | T1 | `clinical`, `still` | *Hàng chục bình oxy, máy hút đờm và hàng trăm lọ thuốc đặc trị duy trì sự sống vẫn còn nguyên vẹn trên kệ tủ.* | — | ⊘ |  |
| 1-23 | `1.08#7` (4,1 s) | H | T1 | `spotlight`, `push` | *Một sự tĩnh lặng đến rợn người bao trùm lên toàn bộ hiện trường vụ án.* | — | — |  |
| 1-24 | `1.08#8` (6,2 s) | H | T1 | `night_screen`, `pan` | *Cả nước Mỹ bàng hoàng rơi vào một cơn ác mộng tập thể khi hay tin dữ.* | — | — |  |
| 1-25 | `1.08#9` (10,1 s) | H | T1 | `night_street`, `pull` | *Người dân lo sợ rằng một kẻ sát nhân tàn độc đã sát hại người mẹ thánh thiện, rồi bắt cóc một thiếu nữ không thể tự bước đi dù chỉ nửa bước.* | — | — |  |
| 1-26 | `1.08#10` (7,7 s) | H | T1 | `pinboard`, `still` | *Một cuộc săn lùng quy mô liên bang được kích hoạt với giả định nạn nhân có thể tử vong bất cứ lúc nào nếu thiếu thuốc men điều trị.* | — | — |  |
| 1-27 | `1.08#11` (7,4 s) | H | T1 | `interrogation`, `push` | *Chúng ta hãy lắng nghe Điều tra viên tái hiện lại thời khắc bước ngoặt lịch sử khi lực lượng chức năng tiếp cận được nghi phạm.* | — | →D |  |
| 1-28 | `1.11#1` (7,9 s) | D | T1 | `pinboard`, `pan` | *Suốt 48 giờ đầu tiên, toàn bộ lực lượng điều tra làm việc không ngừng nghỉ với tâm thế chạy đua cứu mạng một đứa trẻ tật nguyền nguy kịch.* | — | ✦ Sói |  |
| 1-29 | `1.11#2` (11,8 s) | D | T7 tuyến đường | `route_night`, `pull` | *Dấu vết kỹ thuật số từ địa chỉ IP đăng tải dòng trạng thái trên mạng xã hội đã dẫn chúng tôi tới một căn nhà tại thị trấn Big Bend, thuộc bang Wisconsin, cách hiện trường hơn 800 cây số.* | — | — |  |
| 1-30 | `1.11#3` (6,8 s) | D | T1 | `interrogation_gypsy`, `still` | *Tại đây, lực lượng hành pháp đã bắt giữ một thanh niên tên là Nicholas Godejohn cùng một cô gái trẻ.* | — | — |  |
| 1-31 | `1.11#4` (6,2 s) | D | T1 | `interrogation_gypsy`, `push` | *Nhưng khoảnh khắc cánh cửa phòng thẩm vấn mở ra, một sự thật chấn động đã đánh sập toàn bộ nhận thức của chúng tôi.* | — | — |  |
| 1-32 | `1.11#5` (5,4 s) | D | T1 | `interrogation_gypsy`, `pan` | *Bước vào phòng thẩm vấn ngày hôm đó, Gypsy Rose Blanchard không hề ngồi trên xe lăn.* | — | — |  |
| 1-33 | `1.11#6` (3,1 s) | D | T1 | `interrogation_gypsy`, `pull` | *Cô ta tự bước đi vững chãi bằng chính đôi chân của mình với một phong thái hoàn toàn bình thường.* | — | — |  |
| 1-34 | `1.11#7` (8,7 s) | D | T1 | `spotlight`, `still` | *Đôi mắt cô sáng rõ và linh hoạt, hoàn toàn không có vẻ gì của một bệnh nhân đang cận kề cái chết.* | — | — |  |
| 1-35 | `1.11#8`–`#9` (6,0 s) | D | T1 | `clinical`, `push` | *Không hề có dấu vết của bệnh ung thư máu.* → *Không hề có tổn thương tủy sống hay chứng loạn dưỡng cơ.* | — | — |  |
| 1-36 | `1.11#10` (7,1 s) | D | T1 | `brain_desk`, `pan` | *Trí não của cô hoàn toàn minh mẫn, sắc sảo của một phụ nữ 23 tuổi chứ không phải tâm trí của một đứa trẻ lên bảy.* | — | — |  |
| 1-37 | `1.11#11` (7,8 s) | D | T1 | `two_shadows`, `pull` | *Và người chủ mưu lên kế hoạch chấm dứt mạng sống của người mẹ thánh mẫu kia...* → *không ai khác chính là cô con gái mà cả nước Mỹ từng thương xót.* | — | →H |  |
| 1-38 | `1.13#1` (4,9 s) | H | T1 | `podcast_desk`, `still` | *Chào mừng bạn đến với hồ sơ phân tích tâm lý học tội phạm của Amber eyes.* | — | — |  |
| 1-39 | `1.13#2` (16,7 s) | H | T1 | `house_night`, `push` | *Hôm nay, chúng ta sẽ bước qua ngưỡng cửa của ngôi nhà màu hồng ở Springfield để giải mã một trong những bi kịch kỳ dị và tàn khốc nhất từng được ghi nhận trong lịch sử y khoa và tư pháp hiện đại: Hồ sơ Gypsy Rose Blanchard.* | — | — |  |
| 1-40 | `1.13#3` (21,4 s) | H | T1 | `brain_desk`, `pan` | *Chúng ta sẽ cùng bóc tách hai cơ chế đen tối: Hội chứng Münchausen qua trung gian và Sự bất lực tập nhiễm – để trả lời câu hỏi nhức nhối:* → *Làm thế nào một chiếc lồng giam y tế có thể tồn tại suốt 23 năm giữa thanh thiên bạch nhật, dưới ánh hào quang của lòng từ thiện?* | — | — |  |
| 1-41 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **HIỆN TRƯỜNG & QUỸ ĐẠO LEO THANG CỦA VỰC THẲM** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ Y TẾ — QUỸ ĐẠO LEO THANG CỦA VỰC THẲM · nền chủ đạo `wheelchair_room`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (8,5 s) | H | T1 | `brain_desk`, `pull` | *Để hiểu tại sao một cô gái trẻ lại đi đến quyết định đoạt mạng chính mẹ ruột của mình để tìm kiếm lối thoát, chúng ta phải bắt đầu từ hiện trường thực sự của vụ án.* | — | — |  |
| 2-02 | `2.02#2` (10,5 s) | H | T1 | `bedroom_door`, `still` | *Hiện trường thực sự của thảm kịch này không phải là căn phòng ngủ tại Missouri vào đêm tháng 6 năm 2015.* | — | — |  |
| 2-03 | `2.02#3` (7,8 s) | H | T1 | `wheelchair_room`, `push` | *Hiện trường thực sự chính là thân xác của Gypsy Rose, bị giam hãm và xâm lấn suốt 23 năm ròng rã.* | — | — |  |
| 2-04 | `2.02#4` (6,5 s) | H | T1 | `clinical`, `pan` | *Một cô gái với dáng người nhỏ thó, đôi mắt trũng sâu và toàn bộ hàm răng bị nhổ bỏ hoàn toàn.* | — | — |  |
| 2-05 | `2.02#5` (9,4 s) | H | T1 | `pinboard`, `pull` | *Một hành trình tha hóa bệnh lý không xuất hiện trong một sớm một chiều, mà được xây dựng qua 4 nấc thang leo thang hành vi y tế kéo dài hơn hai thập kỷ.* | — | — |  |
| 2-06 | `2.02#6` (4,8 s) | H | T1 | `records`, `still` | *Xin mời Điều tra viên công bố chi tiết hồ sơ bệnh án thu giữ được.* | — | →D |  |
| 2-07 | `2.04#1` (10,3 s) | D | T1 | `records`, `push` | *Lật lại hàng ngàn trang hồ sơ lưu trữ từ nhiều bệnh viện, chúng tôi đã phục dựng lại toàn bộ quỹ đạo lạm dụng y khoa mà bà Dee Dee áp đặt lên Gypsy Rose qua 4 giai đoạn leo thang rõ rệt:* | — | — |  |
| 2-08 | `2.04#2` (4,4 s) | D | T1 | `pinboard`, `pan` | *Nấc thang thứ nhất: Gieo mầm triệu chứng giả.* | — | — |  |
| 2-09 | `2.04#3` (5,2 s) | D | T1 | `house_dawn`, `pull` | *Gypsy Rose sinh năm 1991 hoàn toàn khỏe mạnh bình thường.* | — | — |  |
| 2-10 | `2.04#4` (9,5 s) | D | T1 | `clinical`, `still` | *Nhưng khi đứa trẻ mới tròn 3 tháng tuổi, bà Dee Dee bắt đầu bế con đến các phòng cấp cứu và khẳng định đứa trẻ mắc chứng ngưng thở khi ngủ không rõ nguyên nhân.* | — | — |  |
| 2-11 | `2.04#5` (12,6 s) | D | T1 | `wheelchair_room`, `push` | *Đến năm Gypsy lên 7 tuổi, sau một tai nạn trầy xước nhẹ ở đầu gối khi đi xe ba bánh,* → *bà Dee Dee tuyên bố con gái bị chấn thương tủy sống nghiêm trọng và ép cô bé phải ngồi xe lăn vĩnh viễn kể từ đó.* | — | — |  |
| 2-12 | `2.04#6`–`#7` (10,2 s) | D | T1 | `pinboard`, `pan` | *Nấc thang thứ hai: Xâm lấn thể xác và lạm dụng dược chất.* → *Khi những lời khai man không còn đủ thỏa mãn, bà Dee Dee bắt đầu can thiệp trực tiếp vào sinh học của con gái.* | — | — |  |
| 2-13 | `2.04#8` (7,4 s) | D | T1 | `clinical`, `pull` | *Bà bắt Gypsy uống thuốc chống động kinh liều cao Tegretol suốt nhiều năm dù các kết quả điện não đồ đều hoàn toàn bình thường.* | — | — |  |
| 2-14 | `2.04#9` (11,7 s) | D | T1 | `clinical`, `still` | *Tác dụng phụ của thuốc kết hợp cùng sự thiếu hụt dinh dưỡng kéo dài đã khiến men răng của cô bé bị phá hủy hoàn toàn, dẫn đến việc toàn bộ hàm răng bị mục nát và bác sĩ buộc phải nhổ bỏ sạch sẽ.* | — | ⊘ |  |
| 2-15 | `2.04#10` (9,1 s) | D | T1 | `clinical`, `push` | *Bà yêu cầu bác sĩ phẫu thuật đặt ống truyền thức ăn trực tiếp vào dạ dày của con, biến một người có khả năng ăn uống bình thường thành người phụ thuộc hoàn toàn vào dịch truyền.* | — | ⊘ |  |
| 2-16 | `2.04#11` (9,4 s) | D | T1 | `clinical`, `pan` | *Thậm chí, bà còn thuyết phục bệnh viện nhi Children’s Mercy thực hiện ca mổ cắt bỏ tuyến nước bọt của Gypsy sau khi bí mật tiêm thuốc gây khô miệng.* | — | ⊘ |  |
| 2-17 | `2.04#12` (4,5 s) | D | T1 | `pinboard`, `pull` | *Nấc thang thứ ba: Thao túng hệ thống và vô hiệu hóa cơ chế kiểm tra.* | — | — |  |
| 2-18 | `2.04#13` (8,0 s) | D | T1 | `records`, `still` | *Dee Dee từng có thời gian làm hộ lý, nên bà ta sử dụng thành thạo các thuật ngữ chuyên môn để mô tả triệu chứng đánh lừa bác sĩ.* | — | — |  |
| 2-19 | `2.04#14` (8,9 s) | D | T1 | `clinical`, `push` | *Trước mỗi lần khám bệnh, bà bí mật tiêm thuốc tê hoặc bôi hóa chất gây kích ứng để tạo triệu chứng giả trên cơ thể con gái.* | — | — |  |
| 2-20 | `2.04#15` (11,3 s) | D | T1 | `storm`, `pan` | *Năm 2005, khi cơn bão Katrina quét qua bang Louisiana,* → *bà đã lợi dụng thảm họa để tuyên bố toàn bộ hồ sơ bệnh án gốc bị lũ cuốn trôi, từ đó xóa sạch dấu vết đối chiếu.* | — | — |  |
| 2-21 | `2.04#16` (4,2 s) | D | T1 | `pinboard`, `pull` | *Nấc thang thứ tư: Xóa bỏ hoàn toàn nhân dạng và quyền tự chủ.* | — | — |  |
| 2-22 | `2.04#17` (5,3 s) | D | T1 | `deedee_room`, `still` | *Dee Dee cạo trọc đầu con gái định kỳ, tuyên bố tóc rụng do hóa trị ung thư máu.* | — | — |  |
| 2-23 | `2.04#18` (9,7 s) | D | T1 | `dress_hanger`, `push` | *Bà ép Gypsy mặc những bộ váy công chúa của trẻ nhỏ, đeo kính mắt dày cộp và cấm cô tiếp xúc với bất kỳ ai nếu không có sự giám sát trực tiếp của mẹ.* | — | →H |  |
| 2-24 | `2.06#1` (8,6 s) | H | T1 | `brain_desk`, `pan` | *Dưới góc nhìn của khoa học hành vi, sự kiểm soát này phản ánh một Phương thức hành động và Dấu ấn tâm lý cực kỳ đặc thù.* | — | — |  |
| 2-25 | `2.06#2` (6,6 s) | H | T1 | `pinboard`, `pull` | *Xin mời Chuyên gia tâm lý phân tích sự khác biệt giữa thủ đoạn và chữ ký tâm lý của hung thủ.* | — | →C |  |
| 2-26 | `2.07#1` (5,3 s) | C | T9 thuật ngữ | `brain_desk`, `still` | **Thủ đoạn (Modus Operandi) và Chữ ký tâm lý (Signature)** · *Trong tâm lý học tội phạm, chúng ta luôn phân biệt rạch ròi giữa Thủ đoạn (Modus Operandi) và Chữ ký tâm lý (Signature):* | — | ✦ Cáo |  |
| 2-27 | `2.07#2` (4,6 s) | C | T1 | `records`, `push` | *Thủ đoạn là những gì hung thủ làm để thực hiện hành vi và né tránh sự trừng phạt.* | — | — |  |
| 2-28 | `2.07#3` (10,5 s) | C | T1 | `pinboard`, `pan` | *Ở Dee Dee, thủ đoạn của bà ta liên tục biến đổi: bà ta áp dụng kỹ thuật*“Doctor shopping” | — | — |  |
| 2-29 | `2.07#4` (13,5 s) | C | T1 | `records`, `pull` | *Vào năm 2007, bác sĩ nhi khoa thần kinh Bernardo Flasterstein tại Missouri đã ghi rõ trong bệnh án rằng ông không phát hiện bất kỳ dấu hiệu bại liệt hay loạn dưỡng cơ nào, và nghi ngờ người mẹ mắc chứng giả bệnh.* | — | — |  |
| 2-30 | `2.07#5` (5,2 s) | C | T1 | `interrogation`, `still` | *Vị bác sĩ đã thẳng thắn đối chất với Dee Dee về kết quả kiểm tra thể chất bình thường của cô bé.* | — | — |  |
| 2-31 | `2.07#6` (8,8 s) | C | T1 | `house_return`, `push` | *Nhận thấy nguy cơ bị lật tẩy, Dee Dee lập tức cắt đứt liên lạc với vị bác sĩ này, giận dữ cáo buộc ông thiếu y đức và đưa con sang một hệ thống y tế khác.* | — | — |  |
| 2-32 | `2.07#7` (5,4 s) | C | T1 | `brain_desk`, `pan` | *Ngược lại, Chữ ký tâm lý (Signature) là thứ bất biến,* → *sinh ra để thỏa mãn nhu cầu cảm xúc bệnh lý cốt lõi.* | — | — |  |
| 2-33 | `2.07#8`–`#9` (12,8 s) | C | T1 | `doll`, `pull` | *Chữ ký của Dee Dee thể hiện rõ qua hành vi Tước đoạt tuổi trưởng thành (Infantilization).* → *Bà ta khai man ngày sinh, biến Gypsy từ một thiếu nữ 20 tuổi thành một đứa trẻ 16 tuổi trên giấy tờ.* | — | — |  |
| 2-34 | `2.07#10` (5,2 s) | C | T1 | `doll`, `still` | *Bà ta bắt con gái đội tóc giả sặc sỡ, ôm thú bông và nói bằng giọng the thé của trẻ thơ.* | — | — |  |
| 2-35 | `2.07#11` (9,6 s) | C | T1 | `spotlight_deedee`, `push` | *Dee Dee không chỉ muốn con mình bệnh tật; bà ta khao khát biến con gái thành một con búp bê vĩnh viễn không bao giờ lớn, hoàn toàn phụ thuộc vào sự tồn tại của bà.* | — | →H |  |
| 2-36 | `2.08#1` (7,1 s) | H | T1 | `brain_desk`, `pan` | *Bên cạnh chữ ký tâm lý đó, cách Dee Dee nhìn nhận con gái mình cũng phơi bày bản chất tàn nhẫn của căn bệnh.* | — | — |  |
| 2-37 | `2.08#2` (7,0 s) | H | T1 | `spotlight_deedee`, `pull` | *Dee Dee không hề xem Gypsy là một con người có tri giác, có cảm xúc và có quyền được sống khỏe mạnh.* | — | — |  |
| 2-38 | `2.08#3` (10,9 s) | H | T1 | `glass_box`, `still` | *Trong tâm trí của bà ta, Gypsy đã bị giáng cấp thành một “đạo cụ sống” – một công cụ sinh học để sản xuất ra sự thương cảm và sự tôn sùng từ xã hội.* | — | — |  |
| 2-39 | `2.08#4` (6,9 s) | H | T1 | `clinical`, `push` | *Mỗi mũi tiêm, mỗi ca phẫu thuật không cần thiết không hề gợi lên trong Dee Dee sự xót xa của một người mẹ.* | — | — |  |
| 2-40 | `2.08#5` (5,2 s) | H | T1 | `cage`, `pan` | *Chúng chỉ là những chiếc đinh được đóng thêm vào chiếc lồng kính giam cầm số phận của một con người.* | — | — |  |
| 2-41 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **GIẢI PHẪU TÂM LÝ — BÊN TRONG BỘ NÃO KẺ MẮC FDIA** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI PHẪU TÂM LÝ — BÊN TRONG BỘ NÃO CỦA KẺ MẮC FDIA · nền chủ đạo `brain_desk`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (4,9 s) | H | T1 | `void`, `pull` | *Đến đây, bất kỳ ai trong chúng ta cũng đều đối diện với một câu hỏi nhức nhối:* | — | — |  |
| 3-02 | `3.02#2` (7,0 s) | H | T1 | `fog_deedee`, `still` | *Điều gì có thể thúc đẩy một người mẹ làm ra những điều tàn độc như vậy với chính giọt máu của mình suốt 23 năm?* | — | — |  |
| 3-03 | `3.02#3` (8,3 s) | H | T1 | `charity`, `push` | *Nhiều người vội vàng nhận định rằng Dee Dee làm tất cả chỉ vì tiền trợ cấp và những chuyến du lịch miễn phí đến Disneyland.* | — | — |  |
| 3-04 | `3.02#4` (7,9 s) | H | T1 | `records`, `pan` | *Nhưng nếu chỉ vì lòng tham tài chính thông thường, kẻ phạm tội sẽ chọn những phương thức lừa đảo ít phiền phức và tốn kém hơn nhiều.* | — | — |  |
| 3-05 | `3.02#5` (4,8 s) | H | T1 | `brain_desk`, `pull` | *Dưới góc độ tâm thần học pháp y, vật chất chỉ là sản phẩm phụ bên ngoài.* | — | — |  |
| 3-06 | `3.02#6` (10,4 s) | H | T1 | `brain_desk`, `still` | *Động cơ cốt lõi chi phối toàn bộ hành vi của Dee Dee Blanchard xuất phát từ một hội chứng tâm thần phức tạp: Hội chứng Münchausen qua trung gian (Factitious Disorder Imposed on Another – FDIA).* | — | — |  |
| 3-07 | `3.02#7` (6,6 s) | H | T1 | `brain_desk`, `push` | *Xin mời Chuyên gia tâm lý giải mã các tầng nhận thức bên trong tâm trí của một kẻ mắc hội chứng này.* | — | →C |  |
| 3-08 | `3.04#1` (7,7 s) | C | T9 thuật ngữ | `clinical`, `pan` | **DSM-5-TR** · *Theo cẩm nang chẩn đoán tâm thần DSM-5-TR, hội chứng FDIA hoàn toàn khác biệt với hành vi Giả bệnh trục lợi thông thường (Malingering).* | — | — |  |
| 3-09 | `3.04#2` (4,5 s) | C | T1 | `records`, `pull` | *Kẻ giả bệnh trục lợi sẽ dựng chuyện để kiếm tiền rồi bí mật hưởng thụ trong bóng tối.* | — | — |  |
| 3-10 | `3.04#3` (6,7 s) | C | T9 thuật ngữ | `spotlight_deedee`, `still` | **Sự cung cấp ái kỷ (Narcissistic Supply)** · *Nhưng người mắc hội chứng FDIA thì đói khát một thứ chất gây nghiện tinh vi hơn nhiều: đó là Sự cung cấp ái kỷ (Narcissistic Supply).* | — | — |  |
| 3-11 | `3.04#4`–`#5` (8,3 s) | C | T1 | `brain_desk`, `push` | *Khi giải phẫu tâm lý của Dee Dee Blanchard, chúng ta nhìn thấy 3 tầng động cơ bệnh lý đan xen:* → *Tầng thứ nhất: Cơn nghiện ánh hào quang của Vị thánh tử đạo.* | — | — |  |
| 3-12 | `3.04#6` (13,4 s) | C | T1 | `fog`, `pan` | *Trước khi sinh con, cuộc đời Dee Dee là một chuỗi dài những thất bại ê chề: bà từng có tiền sử trộm cắp vặt, bị gia đình ghẻ lạnh, và cuộc hôn nhân với người chồng Rod Blanchard tan vỡ nhanh chóng khi bà mới 24 tuổi.* | — | — |  |
| 3-13 | `3.04#7` (3,8 s) | C | T1 | `fog`, `pull` | *Bà ta là một cá nhân mờ nhạt, thiếu vắng sự công nhận xã hội.* | — | — |  |
| 3-14 | `3.04#8` (6,2 s) | C | T1 | `house_night`, `still` | *Nhưng khoảnh khắc bà khoác lên mình chiếc áo*“người mẹ đơn thân kiên cường nuôi con tàn tật” | — | — |  |
| 3-15 | `3.04#9` (8,5 s) | C | T1 | `crowd_house`, `push` | *Đi đến đâu, Dee Dee cũng nhận được những ánh nhìn kính nể từ các bác sĩ, những giọt nước mắt cảm phục từ hàng xóm và những bài báo ca ngợi trên truyền thông.* | — | — |  |
| 3-16 | `3.04#10` (5,8 s) | C | T1 | `void`, `pan` | *Sự chú ý của đám đông đã khỏa lấp hoàn toàn cảm giác tự ti và trống rỗng bệnh lý bên trong con người bà ta.* | — | — |  |
| 3-17 | `3.04#11` (9,4 s) | C | T1 | `clinical`, `pull` | *Mỗi lời khen ngợi*“Bà là người mẹ vĩ đại nhất” | — | →H |  |
| 3-18 | `3.06#1` (3,8 s) | H | T1 | `house_night`, `still` | *Nhưng ánh hào quang xã hội mới chỉ là lớp vỏ ngoài.* | — | — |  |
| 3-19 | `3.06#2` (5,0 s) | H | T1 | `house_closed`, `push` | *Điều gì đã diễn ra trong mối quan hệ giữa Dee Dee và những người thân xung quanh bà ta?* | — | — |  |
| 3-20 | `3.06#3` (5,2 s) | H | T1 | `records`, `pan` | *Chúng ta hãy nghe Điều tra viên chia sẻ về hồ sơ gia đình của người phụ nữ này.* | — | →D |  |
| 3-21 | `3.07#1` (9,7 s) | D | T1 | `records`, `pull` | *Khi chúng tôi lật lại lời khai từ gia đình bên ngoại của Dee Dee tại bang Louisiana, những người thân trong gia đình đều bày tỏ sự sợ hãi đối với tính cách của bà ta.* | — | — |  |
| 3-22 | `3.07#2` (6,7 s) | D | T1 | `locked_door`, `still` | *Họ tiết lộ rằng ngay từ thời trẻ, Dee Dee đã thể hiện thói quen thao túng tâm lý và kiểm soát cực đoan.* | — | — |  |
| 3-23 | `3.07#3` (6,3 s) | D | T1 | `locked_door`, `push` | *Người nhà thậm chí nghi ngờ bà ta từng có những hành vi gây hại sức khỏe cho chính mẹ đẻ trước khi bà qua đời.* | — | — |  |
| 3-24 | `3.07#4` (6,2 s) | D | T1 | `corridor`, `pan` | *Một người dì ruột của Dee Dee còn khai nhận rằng gia đình từng bắt quả tang bà ta cố tình bỏ thuốc độc vào thức ăn.* | — | — |  |
| 3-25 | `3.07#5` (8,2 s) | D | T1 | `house_closed`, `pull` | *Sau khi sinh Gypsy, Dee Dee hoàn toàn cắt đứt liên lạc với gia đình ruột thịt và cô lập đứa trẻ khỏi người cha là ông Rod Blanchard.* | — | — |  |
| 3-26 | `3.07#6` (10,9 s) | D | T1 | `records`, `still` | *Mỗi tháng, người cha vẫn đều đặn gửi tiền chu cấp nuôi con, nhưng Dee Dee liên tục nói dối rằng con gái bị tổn thương não nặng nề và không thể nghe điện thoại hay gặp mặt cha.* | — | — |  |
| 3-27 | `3.07#7` (5,2 s) | D | T1 | `locked_door`, `push` | *Ông Rod Blanchard thậm chí từng bị cấm xuất hiện tại các buổi lễ trao nhà thiện nguyện của con gái.* | — | — |  |
| 3-28 | `3.07#8` (8,2 s) | D | T1 | `crowd_away`, `pan` | *Gia đình bị biến thành một mối đe dọa cần phải loại bỏ, bởi họ là những người duy nhất có khả năng nhìn thấu bản chất của bà ta.* | — | →C |  |
| 3-29 | `3.08#1` (5,7 s) | C | T9 thuật ngữ | `brain_desk`, `pull` | **Cơ chế chia ngăn nhận thức (Compartmentalization)** · *Chính từ sự cô lập này, chúng ta nhận diện được Tầng tâm lý thứ hai: Cơ chế chia ngăn nhận thức (Compartmentalization).* | — | — |  |
| 3-30 | `3.08#2` (4,2 s) | C | T1 | `hands`, `still` | *Não bộ của Dee Dee đã khóa chặt hai thế giới riêng biệt không bao giờ giao thoa:* | — | — |  |
| 3-31 | `3.08#3` (6,4 s) | C | T1 | `hands`, `push` | *Một ngăn là hình ảnh người mẹ chu đáo, thức trắng đêm xoa bóp cho con, hát ru và tự tay nấu từng bữa ăn lỏng.* | — | — |  |
| 3-32 | `3.08#4` (6,6 s) | C | T1 | `deedee_room`, `pan` | *Ngăn còn lại là một kẻ thủ ác lạnh lùng, sẵn sàng trói tay con gái vào thành giường để ép cô bé uống thuốc độc hại.* | — | — |  |
| 3-33 | `3.08#5` (7,0 s) | C | T1 | `glass_box`, `pull` | *Dee Dee sử dụng tình mẫu tử như một*“Lá chắn bình thường hóa” | — | — |  |
| 3-34 | `3.08#6` (4,9 s) | C | T9 thuật ngữ | `brain_desk`, `still` | **Kỹ thuật trung hòa đạo đức** · *Và Tầng tâm lý thứ ba chính là: Kỹ thuật trung hòa đạo đức và Sự thiếu hụt thấu cảm cảm xúc.* | — | — |  |
| 3-35 | `3.08#7`–`#8` (10,2 s) | C | T1 | `records`, `push` | *Dee Dee mắc một khuyết tật nghiêm trọng về Thuyết tâm trí (Theory of Mind).* → *Bà ta hoàn toàn vô cảm trước những nỗi đau đớn thể xác mà Gypsy phải gánh chịu sau mỗi mũi kim tiêm hay ca phẫu thuật.* | — | — |  |
| 3-36 | `3.08#9` (9,3 s) | C | T1 | `hands`, `pan` | *Bà ta tự thuyết phục mình bằng những lý lẽ lệch lạc:*“Con bé quá yếu ớt, thế giới ngoài kia sẽ hủy hoại nó, chỉ có sự kiểm soát của mình mới giữ được sinh mạng cho nó” | — | — |  |
| 3-37 | `3.08#10` (6,6 s) | C | T1 | `void`, `pull` | *Bà ta đổ lỗi cho hoàn cảnh, cho sự bất công của số phận và tự phong cho mình quyền năng quyết định sinh tử của con gái.* | — | — |  |
| 3-38 | `3.08#11` (7,5 s) | C | T1 | `house_night`, `still` | *Sự ngụy biện này vô hiệu hóa mọi cảm giác tội lỗi, cho phép Dee Dee ngủ ngon mỗi đêm ngay bên cạnh đứa con đang quằn quại trong bệnh tật nhân tạo.* | — | — |  |
| 3-39 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **GÓC NHÌN NẠN NHÂN — TẠI SAO GYPSY KHÔNG ĐỨNG DẬY?** | — | ⊘ | ◼ |

### HỒI 4 — GÓC NHÌN NẠN NHÂN — TẠI SAO GYPSY KHÔNG ĐỨNG DẬY? · nền chủ đạo `locked_door`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (7,3 s) | H | T1 | `night_screen`, `push` | *Khi sự thật về vụ án chấn động được công bố, một làn sóng hoài nghi dữ dội từ dư luận đã lập tức bùng nổ.* | — | — |  |
| 4-02 | `4.02#2` (6,0 s) | H | T1 | `night_screen`, `pan` | *Rất nhiều người không thể chấp nhận hành vi của Gypsy Rose và đặt ra những câu hỏi đầy định kiến.* | — | — |  |
| 4-03 | `4.02#3` (7,2 s) | H | T1 | `spotlight`, `pull` | *Họ cho rằng một người trưởng thành hoàn toàn có đủ khả năng cầu cứu hoặc tìm đường trốn thoát khỏi sự kìm kẹp.* | — | — |  |
| 4-04 | `4.02#4` (5,2 s) | H | T1 | `podcast_desk`, `still` | *Chúng ta hãy lắng nghe một thắc mắc rất phổ biến từ phía công chúng theo dõi vụ án.* | — | →N2 |  |
| 4-05 | `4.03#1` (8,0 s) | N2 | T1 | `house_night`, `push` | *Thực sự có một điều khiến tôi vô cùng khó hiểu: Cô ấy biết rất rõ rằng đôi chân của mình hoàn toàn khỏe mạnh.* | — | ✦ Mèo |  |
| 4-06 | `4.03#2` (6,6 s) | N2 | T1 | `house_night`, `pan` | *Mỗi đêm khi cửa phòng đóng kín, cô ấy vẫn tự mình đứng dậy đi lại và lục tìm đồ ăn trong tủ lạnh.* | — | — |  |
| 4-07 | `4.03#3` (6,8 s) | N2 | T1 | `crowd_house`, `pull` | *Cô ấy từng tham dự các hội nghị người hâm mộ khoa học viễn tưởng và có nhiều cơ hội tiếp xúc với người lạ.* | — | — |  |
| 4-08 | `4.03#4` (14,6 s) | N2 | T1 | `wheelchair_room`, `still` | *Tại sao suốt hàng chục năm trời, trước mặt hàng trăm bác sĩ, y tá, cảnh sát và các tình nguyện viên từ thiện, Gypsy chưa từng một lần đứng bật dậy khỏi chiếc xe lăn để kêu cứu và vạch trần người mẹ của mình?* | — | →H |  |
| 4-09 | `4.05#1` (6,5 s) | H | T1 | `spotlight`, `push` | *Đó là một câu hỏi tự nhiên của những người đứng ngoài nhìn vào bằng lăng kính của một cá nhân tự do.* | — | — |  |
| 4-10 | `4.05#2` (12,8 s) | H | T1 | `brain_desk`, `pan` | *Thế nhưng, để giải mã sự bất động của Gypsy, chúng ta không thể dùng lý trí thông thường mà phải nhìn vào hai gông cùm tâm lý vô hình: Sự bất lực tập nhiễm và Sự gắn kết chấn thương.* | — | — |  |
| 4-11 | `4.05#3` (4,2 s) | H | T1 | `clinical`, `pull` | *Xin mời Chuyên gia tâm lý phân tích cơ chế giam hãm nhận thức này.* | — | →C |  |
| 4-12 | `4.07#1` (7,3 s) | C | T9 thuật ngữ | `clinical`, `still` | **Sự bất lực tập nhiễm (Learned Helplessness)** · *Năm 1967, nhà tâm lý học lỗi lạc Martin Seligman đã công bố học thuyết kinh điển về Sự bất lực tập nhiễm (Learned Helplessness).* | — | — |  |
| 4-13 | `4.07#2` (12,6 s) | C | T1 | `cage`, `push` | *Trong các thí nghiệm nổi tiếng, khi một sinh vật bị nhốt trong phòng kín và phải chịu những cú sốc điện ngẫu nhiên mà không có cách nào né tránh, sau nhiều lần thử phản kháng thất bại, sinh vật đó sẽ hoàn toàn từ bỏ ý chí chiến đấu.* | — | — |  |
| 4-14 | `4.07#3` (8,3 s) | C | T1 | `cage_open`, `pan` | *Kể cả khi người ta mở toang cửa lồng và không còn dòng điện nào cản trở, con vật vẫn nằm im cam chịu và rên rỉ thay vì bước chân ra ngoài.* | — | — |  |
| 4-15 | `4.07#4` (7,2 s) | C | T1 | `brain_desk`, `pull` | *Bộ não khi bị tổn thương tâm lý sâu sắc sẽ đi đến một kết luận cố định:*“Mọi sự kháng cự đều là vô nghĩa” | — | — |  |
| 4-16 | `4.07#5` (8,0 s) | C | T1 | `hands`, `still` | *Hãy nhìn vào tuổi thơ của Gypsy: Từ lúc mới bi bô tập nói, mỗi khi ngồi trước mặt bác sĩ, Dee Dee luôn nắm chặt lấy bàn tay con gái.* | — | — |  |
| 4-17 | `4.07#6` (3,3 s) | C | T1 | `hands`, `push` | *Người ngoài nhìn vào tưởng đó là cái nắm tay chan chứa yêu thương.* | — | — |  |
| 4-18 | `4.07#7` (8,5 s) | C | T1 | `hands`, `pan` | *Nhưng với Gypsy, đó là một tín hiệu đe dọa chết người: Nếu cô bé nói sai một lời hoặc nhúc nhích đôi chân, bàn tay mẹ sẽ siết chặt đến bầm tím.* | — | ⊘ |  |
| 4-19 | `4.07#8` (6,3 s) | C | T1 | `brain_desk`, `pull` | *Bà Dee Dee đã lập trình vào đầu con gái rằng cô mắc bệnh tâm thần và chỉ có mẹ mới biết điều gì là an toàn cho cô.* | — | — |  |
| 4-20 | `4.07#9` (6,9 s) | C | T1 | `house_closed`, `still` | *Và đằng sau cánh cửa đóng kín của ngôi nhà màu hồng là những trận đòn roi, những ngày bị bỏ đói và lời đe dọa tước đoạt sinh mạng.* | — | →H · ⊘ |  |
| 4-21 | `4.09#1`–`#2` (14,4 s) | H | T1 | `house_closed`, `push` | *Gypsy không phải chưa từng cố gắng bỏ trốn.* → *Trong hồ sơ lưu trữ, Điều tra viên đã ghi lại một biến cố then chốt xảy ra vào năm 2011 – biến cố đã đánh gãy tia hy vọng cuối cùng của cô gái này.* | — | →D |  |
| 4-22 | `4.10#1` (7,3 s) | D | T1 | `night_street`, `pan` | *Năm 2011, khi Gypsy 19 tuổi, cô đã thu hết can đảm để thực hiện một cuộc trốn chạy trong đêm.* | — | — |  |
| 4-23 | `4.10#2` (6,5 s) | D | T1 | `night_street_gypsy`, `pull` | *Cô lén trườn ra khỏi nhà và tìm đến căn hộ của một người quen trong vùng để cầu xin sự giúp đỡ.* | — | — |  |
| 4-24 | `4.10#3` (4,7 s) | D | T1 | `house_night`, `still` | *Cô gái run rẩy van xin những người xung quanh hãy giấu cô đi và đừng để mẹ cô tìm thấy.* | — | — |  |
| 4-25 | `4.10#4` (5,8 s) | D | T1 | `records`, `push` | *Thế nhưng chỉ vài giờ sau, Dee Dee đã xuất hiện cùng một tập hồ sơ y tế giả mạo dày cộp.* | — | — |  |
| 4-26 | `4.10#5` (10,8 s) | D | T1 | `crowd_house`, `pan` | *Trước mặt những người xung quanh, bà ta khóc lóc và khẳng định con gái mình bị thiểu năng trí tuệ bẩm sinh, đang trong cơn hoang tưởng và không có năng lực hành vi dân sự.* | — | — |  |
| 4-27 | `4.10#6` (5,5 s) | D | T1 | `crowd_house`, `pull` | *Mọi người lập tức tin lời người mẹ thánh mẫu và trao trả Gypsy về lại ngôi nhà màu hồng.* | — | — |  |
| 4-28 | `4.10#7` (4,9 s) | D | T1 | `house_closed`, `still` | *Sau đêm đó, Dee Dee dùng búa đập nát chiếc máy tính của con gái ngay trước mắt cô.* | — | — |  |
| 4-29 | `4.10#8` (8,1 s) | D | T1 | `cage`, `push` | *Bà ta dùng xích sắt trói cô vào khung giường suốt hai tuần liên tiếp và cảnh cáo rằng cảnh sát sẽ không bao giờ tin lời một kẻ điên như cô.* | — | →H · ⊘ |  |
| 4-30 | `4.11#1` (13,6 s) | H | T1 | `void`, `pan` | *Cú sốc năm 2011 ấy đã đóng chặt chiếc đinh cuối cùng vào tâm trí Gypsy: Xã hội ngoài kia chỉ tin vào chiếc áo choàng thánh thiện của mẹ cô, còn tiếng nói của cô hoàn toàn vô hình.* | — | — |  |
| 4-31 | `4.11#2` (6,0 s) | H | T1 | `clinical`, `pull` | *Và bên cạnh nỗi khiếp sợ, Chuyên gia tâm lý còn chỉ ra một sợi dây trói buộc thứ hai.* | — | →C |  |
| 4-32 | `4.12#1` (2,0 s) | C | T9 thuật ngữ | `hands`, `still` | **Gắn kết chấn thương (Trauma Bonding)** · *Đó chính là Gắn kết chấn thương (Trauma Bonding).* | — | — |  |
| 4-33 | `4.12#2` (9,2 s) | C | T1 | `hands`, `push` | *Dee Dee là kẻ đầu độc thể xác Gypsy, nhưng cũng chính bà là người duy nhất ôm ấp cô mỗi đêm, chải tóc và thủ thỉ rằng Gypsy là thiên thần duy nhất của cuộc đời bà.* | — | — |  |
| 4-34 | `4.12#3` (10,4 s) | C | T1 | `glass_box`, `pan` | *Sự xen kẽ tàn nhẫn giữa bạo lực khủng khiếp và sự vỗ về ngọt ngào đã làm tê liệt hoàn toàn hệ thống phòng vệ tâm lý của nạn nhân, khiến Gypsy vừa căm hận vừa phụ thuộc sâu sắc vào mẹ mình.* | — | — |  |
| 4-35 | `4.12#4` (8,4 s) | C | T1 | `void`, `pull` | *Trong thế giới quan bị cô lập hoàn toàn, tình yêu và sự bạo hành đã hòa lẫn làm một, khiến nạn nhân không thể nào tự vạch ra ranh giới sinh tồn.* | — | →H |  |
| 4-36 | `4.14#1` (10,2 s) | H | T1 | `cage`, `still` | *Khi mọi cánh cửa pháp lý và xã hội đều bị đóng sập trong tâm tưởng, bản năng sinh tồn bị dồn nén đến đường cùng đã tìm kiếm một lối thoát cực đoan nhất.* | — | — |  |
| 4-37 | `4.14#2` (12,7 s) | H | T1 | `godejohn_screen`, `push` | *Năm 2012, qua mạng Internet bí mật, Gypsy làm quen với Nicholas Godejohn – một thanh niên 24 tuổi có tiền sử rối loạn nhân cách và tự kỷ.* | — | — |  |
| 4-38 | `4.14#3` (9,6 s) | H | T9 thuật ngữ | `two_shadows`, `pan` | **Folie à Deux** · *Hai tâm hồn cô lập và bất ổn đã va vào nhau, trượt dài vào hiện tượng tâm lý nguy hiểm: Folie à Deux – Hội chứng Điên cuồng đôi.* | — | — |  |
| 4-39 | `4.14#4` (5,8 s) | H | T1 | `two_shadows`, `pull` | *Ảo tưởng về một cuộc tình giải cứu đã thôi thúc cả hai đi đến một kế hoạch đoạt mạng tàn khốc.* | — | — |  |
| 4-40 | `4.14#5` (8,3 s) | H | T1 | `house_night`, `still` | *Và đêm 14 tháng 6 năm 2015, cánh cửa ngôi nhà màu hồng đã được mở ra trong bóng tối...* | — | — |  |
| 4-41 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT PHÁP Y, BẢN ÁN TÂM LÝ & CẢNH BÁO ĐỎ** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT PHÁP Y, BẢN ÁN TÂM LÝ & CẢNH BÁO ĐỎ SINH TỒN · nền chủ đạo `court_dawn`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (11,4 s) | H | T1 | `court_dawn`, `push` | *Phiên tòa xét xử vụ án Gypsy Rose Blanchard tại bang Missouri đã trở thành một trong những vụ án gây chia rẽ và thách thức đạo lý sâu sắc nhất trong lịch sử tư pháp Hoa Kỳ.* | — | — |  |
| 5-02 | `5.02#2` (7,8 s) | H | T1 | `court_dawn`, `pan` | *Về mặt pháp luật hình sự, hành vi tham gia lên kế hoạch đoạt mạng mẹ ruột là một tội ác không thể dung thứ.* | — | — |  |
| 5-03 | `5.02#3` (8,7 s) | H | T1 | `records`, `pull` | *Thế nhưng, trước những chứng cứ y khoa kinh hoàng về 23 năm bị tra tấn và lạm dụng thân xác, chánh công tố viên hạt Greene – ông Dan Patterson – đã phải đối diện với một nghịch lý chưa từng có tiền lệ.* | — | — |  |
| 5-04 | `5.02#4` (19,8 s) | H | T1 | `court_dawn`, `still` | *Công tố viên thừa nhận rằng đây là vụ án đặc biệt nhất trong sự nghiệp của mình:* → *một kẻ chủ mưu giết người nhưng đồng thời cũng là nạn nhân sống sót sau một chuỗi tội ác kéo dài suốt hai thập kỷ.* | — | — |  |
| 5-05 | `5.02#5` (10,1 s) | H | T1 | `spotlight`, `push` | *Đây là trường hợp hy hữu mà cán cân công lý buộc phải cân đo giữa sự trừng phạt hình sự và sự đồng cảm sâu sắc đối với nạn nhân của sự lạm dụng tột cùng.* | — | — |  |
| 5-06 | `5.04#1` (13,3 s) | H | T1 | `prison_window`, `pan` | *Năm 2016, thông qua thỏa thuận nhận tội, Gypsy Rose Blanchard bị tuyên phạt 10 năm tù giam về tội giết người cấp độ hai – mức án khoan hồng nhất có thể áp dụng cho một vụ án mạng.* | — | — |  |
| 5-07 | `5.04#2` (8,2 s) | H | T1 | `prison_window`, `pull` | *Trong khi đó, Nicholas Godejohn phải nhận bản án tù chung thân không ân xá cho hành vi trực tiếp gây án.* | — | — |  |
| 5-08 | `5.04#3` (9,4 s) | H | T1 | `court_dawn`, `still` | *Bản án 10 năm tù cho Gypsy được xem là giải pháp dung hòa giữa tính nghiêm minh của pháp luật và tính nhân văn của tư pháp học.* | — | — |  |
| 5-09 | `5.04#4` (7,3 s) | H | T1 | `prison_window`, `push` | *Chúng ta hãy lắng nghe Điều tra viên chia sẻ về nghịch lý tâm lý đằng sau cánh cửa nhà tù của người con gái này.* | — | →D |  |
| 5-10 | `5.05#1` (9,6 s) | D | T1 | `prison_window`, `pan` | *Khi bước vào Trại cải tạo phụ nữ Chillicothe, Gypsy Rose đã đưa ra một lời thú nhận khiến tất cả các chuyên gia tâm lý học pháp y phải nghẹn ngào.* | — | — |  |
| 5-11 | `5.05#2` (9,3 s) | D | T1 | `prison_window`, `pull` | *Cô nói rằng:*“Sống trong nhà tù của pháp luật, lần đầu tiên trong cuộc đời tôi cảm thấy mình thực sự được tự do hơn cả khi sống trong ngôi nhà của mẹ.” | — | — |  |
| 5-12 | `5.05#3` (5,1 s) | D | T1 | `prison_window`, `still` | *Tại nhà tù, thân xác cô bị giam giữ sau song sắt, nhưng linh hồn cô được giải thoát.* | — | ⊘ |  |
| 5-13 | `5.05#4` (11,8 s) | D | T1 | `house_dawn`, `push` | *Cô được phép nuôi lại mái tóc dài tự nhiên, được tự do ăn những món ăn yêu thích bằng miệng, được vứt bỏ chiếc xe lăn và đi lại trên chính đôi chân của mình mà không còn sợ hãi những mũi kim tiêm hành hạ.* | — | — |  |
| 5-14 | `5.05#5` (7,0 s) | D | T1 | `clinical`, `pan` | *Các bác sĩ tại trại giam đã tiến hành lắp đặt một hàm răng giả hoàn chỉnh cho cô, giúp cô tìm lại nụ cười của một con người.* | — | — |  |
| 5-15 | `5.05#6` (4,6 s) | D | T1 | `house_dawn`, `pull` | *Cô cũng hoàn thành chương trình giáo dục phổ thông và lần đầu tiên được học tập một cách bình thường.* | — | — |  |
| 5-16 | `5.05#7` (12,7 s) | D | T1 | `house_free`, `still` | *Vào ngày 28 tháng 12 năm 2023, sau khi chấp hành đủ 85% thời hạn bản án, Gypsy Rose Blanchard đã chính thức bước qua cổng trại giam để bắt đầu lại cuộc đời.* | — | →H |  |
| 5-17 | `5.06#1` (11,0 s) | H | T1 | `spotlight`, `push` | *Dư chấn xã hội từ vụ án Blanchard đã gióng lên một hồi chuông cảnh tỉnh sâu sắc cho toàn bộ hệ thống bảo vệ trẻ em và ngành y tế công cộng trên toàn thế giới.* | — | — |  |
| 5-18 | `5.06#2` (10,6 s) | H | T1 | `records`, `pan` | *Nó phơi bày lỗ hổng chết người của việc thiếu kết nối dữ liệu y khoa tập trung, cho phép những kẻ mắc hội chứng Münchausen qua trung gian dễ dàng qua mặt hàng loạt bệnh viện.* | — | — |  |
| 5-19 | `5.06#3` (11,1 s) | H | T1 | `records`, `pull` | *Nhiều bang tại Mỹ sau đó đã siết chặt quy trình phối hợp liên ngành giữa bệnh viện, trường học và cơ quan an sinh xã hội để bảo vệ trẻ em khỏi nạn bạo hành y tế.* | — | — |  |
| 5-20 | `5.06#4` (12,0 s) | H | T1 | `brain_desk`, `still` | *Để bảo vệ những đứa trẻ vô tội và ngăn chặn những thảm kịch tương tự tái diễn, chúng ta sẽ cùng Chuyên gia tâm lý và Điều tra viên đúc kết Bộ 4 Tín hiệu Cảnh báo Đỏ sinh tồn (Survival Red Flags).* | — | →C |  |
| 5-21 | `5.07#1` (6,1 s) | C | T1 | `clinical`, `push` | *Dưới góc độ tâm lý và lâm sàng y khoa, cộng đồng cần đặc biệt lưu tâm đến 2 chỉ dấu cảnh báo đầu tiên:* | — | — |  |
| 5-22 | `5.07#2` (4,5 s) | C | T8 cờ | `clinical`, `pan` | *01* · **Cảnh báo đỏ thứ nhất: Bệnh sử phức tạp bất thường và mâu thuẫn xét nghiệm.** | — | — |  |
| 5-23 | `5.07#3` (10,0 s) | C | T1 | `records`, `pull` | *Nạn nhân có một danh sách bệnh tật hiểm nghèo kéo dài triền miên, nhưng các kết quả kiểm tra cận lâm sàng khách quan luôn bình thường hoặc mâu thuẫn hoàn toàn với những lời kể nghiêm trọng của người chăm sóc.* | — | — |  |
| 5-24 | `5.07#4` (3,3 s) | C | T8 cờ | `clinical`, `still` | *02* · **Cảnh báo đỏ thứ hai: Triệu chứng xuất hiện có điều kiện.** | — | — |  |
| 5-25 | `5.07#5` (9,2 s) | C | T1 | `records`, `push` | *Các biểu hiện bệnh lý lạ lùng chỉ khởi phát khi có mặt người chăm sóc, và lập tức thuyên giảm rõ rệt khi bệnh nhân được cách ly hoặc nằm trong khu vực có camera giám sát độc lập.* | — | — |  |
| 5-26 | `5.07#6` (6,5 s) | C | T1 | `clinical`, `pan` | *Khi tách rời khỏi người chăm sóc, sức khỏe của người bệnh thường hồi phục một cách kỳ diệu mà không cần can thiệp y tế chuyên sâu.* | — | →D |  |
| 5-27 | `5.08#1` (4,3 s) | D | T1 | `pinboard`, `pull` | *Dưới góc độ điều tra hành vi xã hội, chúng tôi khuyến cáo 2 dấu hiệu tiếp theo:* | — | — |  |
| 5-28 | `5.08#2` (4,6 s) | D | T8 cờ | `pinboard`, `still` | *03* · **Cảnh báo đỏ thứ ba: Thói quen đổi bác sĩ và nghiện sự chú ý.** | — | — |  |
| 5-29 | `5.08#3` (13,8 s) | D | T1 | `records`, `push` | *Người chăm sóc có xu hướng*“Doctor shopping” | — | — |  |
| 5-30 | `5.08#4` (3,7 s) | D | T8 cờ | `house_closed`, `pan` | *04* · **Và cảnh báo đỏ thứ tư: Sự cô lập tuyệt đối khỏi cộng đồng.** | — | — |  |
| 5-31 | `5.08#5` (8,6 s) | D | T1 | `crowd_away`, `pull` | *Nạn nhân bị cắt đứt hoàn toàn khỏi trường học, bạn bè đồng trang lứa và những người thân khác trong gia đình dưới chiêu bài*“bảo vệ sức khỏe yếu ớt” | — | — |  |
| 5-32 | `5.08#6` (5,5 s) | D | T1 | `spotlight`, `still` | *Họ luôn muốn mình là người duy nhất nắm quyền kiểm soát dòng thông tin và sự sống của nạn nhân.* | — | →H |  |
| 5-33 | `5.10#1` (10,7 s) | H | T1 | `house_dawn`, `push` | *Hồ sơ về ngôi nhà màu hồng tại thành phố Springfield khép lại, nhưng những câu hỏi về bản chất của lòng nhân ái và đạo đức con người vẫn còn vang vọng mãi.* | — | — |  |
| 5-34 | `5.10#2` (10,5 s) | H | T1 | `house_dawn`, `pan` | *Tình yêu thương chân chính của cha mẹ là đôi cánh giúp một đứa trẻ lớn lên khỏe mạnh, vững vàng bước đi trên đôi chân của chính mình và tự do khám phá thế giới.* | — | — |  |
| 5-35 | `5.10#3` (16,9 s) | H | T1 | `cage_open`, `pull` | *Khi tình mẫu tử bị bóp méo thành một công cụ sở hữu ích kỷ, khi sự chăm sóc trở thành chiếc lồng giam tàn độc để nuôi dưỡng cái tôi bệnh hoạn của người lớn...* → *thì thứ nhân danh tình yêu ấy đôi khi lại mang sức tàn phá khủng khiếp hơn bất kỳ lưỡi dao nào.* | — | — |  |
| 5-36 | `5.10#4` (8,2 s) | H | T1 | `charity`, `still` | *Lòng tốt và sự trắc ẩn nếu thiếu đi sự tỉnh táo sẽ vô tình trở thành mảnh đất màu mỡ cho tội ác sinh sôi.* | — | — |  |
| 5-37 | `5.10#5` (12,9 s) | H | T1 | `house_dawn`, `push` | *Bài học đắt giá nhất mà hồ sơ này để lại chính là lời nhắc nhở chúng ta: Đừng bao giờ để chiếc áo choàng thánh thiện của bất kỳ ai ru ngủ trực giác tỉnh táo và lương tri cảnh giác của chính mình.* | — | — |  |
| 5-38 | `5.12#1` (8,1 s) | H | T1 | `podcast_desk`, `pan` | *Cảm ơn các khách mời đã tham gia phân tích hồ sơ, và cảm ơn bạn đã đồng hành lắng nghe đến những phút cuối cùng của câu chuyện hôm nay.* | — | — |  |
| 5-39 | `5.12#2` (8,5 s) | H | T1 | `house_night`, `pull` | *Sự đồng cảm và suy ngẫm của bạn là động lực để chúng tôi tiếp tục soi rọi những góc khuất tăm tối nhất của tâm lý con người.* | — | — |  |
| 5-40 | `5.12#3` (13,0 s) | H | T1 | `podcast_desk`, `still` | *Hãy chia sẻ suy ngẫm của bạn ở phần bình luận bên dưới, giữ cho mình một tâm trí sáng suốt, và hẹn gặp lại bạn trong hồ sơ giải phẫu tâm lý tội phạm tiếp theo.* | — | — |  |
| 5-41 | hết tập (7.0 s) | — | T1 | `void` | **HỒ SƠ TẬP 01 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | — | ⊘ | ◼ |

**Tổng:** 203 dòng (198 shot có lời + 4 thẻ chuyển hồi + 1 thẻ kết) · 205 câu · 33 element lời (5 hồi) · nền dùng 44 loại. Bảng dựng lại 09/11/2026 theo kịch bản viết lại 09/11/2026 (205 câu); thời lượng shot đo từ master mp3 mới (ASR).
**Xuất hiện của linh thú (ước tính):**

| Nhân vật | Lượt nói | Bán thân (câu đầu lượt + `🅑`) | Lần được mời (`→`) |
|---|---:|---:|---:|
| Cú · Host | 21 | ~22 (21 đầu lượt + 3 `🅑` − 2 đầu lượt bị `⊘`) | — |
| Sói · Điều tra viên | 4 | 7 | 4 |
| Cáo · Chuyên gia | 6 | 9 | 5 |
| Cừu · N1 | 1 | 2 | 1 |
| Mèo · N2 | 1 | 2 | 1 |

Badge hiện **suốt** mọi lượt của cả 5 nhân vật.

---

---

## PHỤ LỤC A (Tập 01) — CẤU TRÚC KỊCH BẢN (`parse_kichban.py` trên `kichban_tap01_22102026_v2.md`, 22/10/2026)

B1 phải sinh ra **đúng bảng này**; khác là dừng và báo.

| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |
|---|---|---:|---:|---|
| `1.01` | *BGM* | — | — | Hộp nhạc lên dây cót, bị drone bóp nghẹt |
| `1.02` | *SFX* | — | — | Còi cảnh sát xa, gõ cửa dồn dập |
| `1.03` | Cú · Host | 3 | 70 | Chậm, trầm, giữ khoảng cách khách quan |
| `1.04` | *Nghỉ 2,0 s* | — | — | |
| `1.05` | Cú · Host | 2 | 66 | (kế thừa) |
| `1.06` | *SFX* | — | — | Băng ghi âm "Tách" |
| `1.07` | **Cừu · N1** | 3 | 105 | Xúc động, chân thật như trả lời phỏng vấn |
| `1.08` | Cú · Host | 6 | 151 | Đẩy nhanh nhịp độ |
| `1.09` | *Nghỉ 2,0 s* | — | — | Nhạc dừng đột ngột (giữ drone −40 dB) |
| `1.10` | *SFX* | — | — | Bộ đàm rè, mở cửa phòng thẩm vấn |
| `1.11` | **Sói · Điều tra viên** | 8 | 143 | Hạ trầm, sắc lạnh, dứt khoát |
| `1.12` | *SFX* | — | — | "Tách", cello vào |
| `1.13` | Cú · Host | 2 | 60 | — |
| `2.01` | *BGM* | — | — | Máy đo nhịp tim + piano |
| `2.02` | Cú · Host | 3 | 68 | Đều đặn, dẫn dắt |
| `2.03` | *SFX* | — | — | Lật giấy hồ sơ |
| `2.04` | Cú · Host | 5 | 131 | (kế thừa) |
| `2.05` | *Nghỉ 1,5 s* | — | — | |
| `2.06` | Cú · Host | 3 | 57 | (kế thừa) |
| `2.07` | **Sói · Điều tra viên** | 10 | 348 | Đanh thép, nhấn từng chứng cứ |
| `2.08` | *SFX* | — | — | Khoá cửa sắt "Cạch" |
| `2.09` | Cú · Host | 4 | 91 | Trầm lắng |
| `3.01` | *BGM* | — | — | Ambient sâu, học thuật |
| `3.02` | Cú · Host | 5 | 159 | — |
| `3.03` | *Nghỉ 2,0 s* | — | — | |
| `3.04` | Cú · Host | 2 | 43 | — |
| `3.05` | **Cáo · Chuyên gia** | 9 | 239 | Phân tích chuyên môn, rõ ràng |
| `3.06` | *Nghỉ 1,5 s* | — | — | |
| `3.07` | Cú · Host | 2 | 69 | — |
| `3.08` | **Cáo · Chuyên gia** | 6 | 147 | Hạ giọng trầm, chậm rãi hơn |
| `3.09` | *Nghỉ 2,0 s* | — | — | |
| `3.10` | **Cáo · Chuyên gia** | 6 | 122 | (kế thừa) |
| `4.01` | *BGM* | — | — | Nhịp tim chậm + violin |
| `4.02` | Cú · Host | 2 | 55 | Trăn trở |
| `4.03` | **Mèo · N2** | 3 | 74 | Băn khoăn, hoài nghi |
| `4.04` | *Nghỉ 2,0 s* | — | — | |
| `4.05` | Cú · Host | 2 | 72 | — |
| `4.06` | *SFX* | — | — | Xiềng xích, kim loại |
| `4.07` | **Cáo · Chuyên gia** | 8 | 207 | — |
| `4.08` | *Nghỉ 1,5 s* | — | — | |
| `4.09` | Cú · Host | 3 | 61 | — |
| `4.10` | **Sói · Điều tra viên** | 5 | 135 | Trầm, thuật lại hồ sơ |
| `4.11` | *Nghỉ 2,0 s* | — | — | Host lắng xuống |
| `4.12` | Cú · Host | 2 | 66 | — |
| `4.13` | **Cáo · Chuyên gia** | 3 | 70 | — |
| `4.14` | *SFX* | — | — | Bàn phím gõ trong đêm |
| `4.15` | Cú · Host | 5 | 116 | — |
| `5.01` | *BGM* | — | — | Búa tòa án → piano ấm |
| `5.02` | Cú · Host | 3 | 116 | Điềm đạm, tổng kết |
| `5.03` | *Nghỉ 1,5 s* | — | — | |
| `5.04` | Cú · Host | 3 | 107 | (kế thừa) |
| `5.05` | *Nghỉ 2,0 s* | — | — | |
| `5.06` | Cú · Host | 1 | 60 | (kế thừa) |
| `5.07` | **Cáo · Chuyên gia** | 2 | 77 | Nhấn mạnh từng ý, góc lâm sàng |
| `5.08` | **Sói · Điều tra viên** | 2 | 82 | Tiếp lời, góc hành vi xã hội |
| `5.09` | *Nghỉ 2,5 s* | — | — | Piano dâng nhẹ |
| `5.10` | Cú · Host | 3 | 114 | Trầm ấm, truyền cảm |
| `5.11` | *Nghỉ 1,5 s* | — | — | |
| `5.12` | Cú · Host | 2 | 64 | (kế thừa) |
| `5.13` | *SFX* | — | — | Gấp hồ sơ "Bụp", tắt máy ghi âm "Tách" |
| `5.14` | *BGM* | — | — | Piano ngân 5 s rồi tắt |
| | **Tổng** | **128** | **3.545** | |

### B4.1 SFX đã có trong master (22/10/2026)

Ngoài tiếng "Tách" (tổng hợp bằng code trong `build_audio3.py`), tập đã có **11 file SFX** tự tổng hợp bằng `.work/make_sfx.py` (không tải file ngoài → không vướng bản quyền). Đặt theo bảng `SFX_CUES` trong `build_audio3.py`; `offset` âm = đặt **trước** mốc để tiếng nối vào câu thoại kế tiếp.

| File | Mốc | Offset | Mức | Mô tả |
|---|---|---:|---:|---|
| `police_siren_distant.wav` | `1.02` | −2,80 s | −3 dB | Còi xe cảnh sát vọng xa |
| `door_knock.wav` | `1.02` | −0,90 s | −2 dB | Gõ cửa dồn dập trong đêm |
| `radio_chatter.wav` | `1.10` | −3,00 s | −6 dB | Bộ đàm rè + tiếng mở cửa phòng thẩm vấn |
| `heart_beep.wav` | `2.01` | −5,03 s | −18 dB | Máy đo nhịp tim "Bíp… Bíp…" |
| `paper_rustle.wav` | `2.03` | −1,00 s | −8 dB | Lật giấy hồ sơ sột soạt |
| `lock_door.wav` | `2.08` | −1,10 s | −2 dB | Khoá cửa sắt "Cạch" |
| `heartbeat_slow.wav` | `4.01` | −4,97 s | −18 dB | Nhịp tim đập chậm (Hồi 4) |
| `chains.wav` | `4.06` | −2,50 s | −5 dB | Xiềng xích, kim loại va nhẹ |
| `keyboard_night.wav` | `4.14` | −2,20 s | −12 dB | Bàn phím gõ trong đêm |
| `gavel.wav` | `5.01` | −1,10 s | +1 dB | Búa tòa án gõ "Cốp" |
| `folder_close.wav` | `5.13` | −0,47 s | −8 dB | Gấp hồ sơ giấy "Bụp" |

Mức tính theo RMS lời, hiệu chuẩn bằng cách nghe thật trong bản thành phẩm (mốc tham chiếu: tiếng "Tách" ở −6 dB). Ba tiếng "Tách" (mã `1.06`, `1.12`, `5.13`) vẫn do `build_audio3.py` tổng hợp trực tiếp, không cần file.

**Kiểm chứng**
- Có mặt đúng chỗ: tương quan chéo với stem SFX lossless → **14/14** (NCC = 1,000).
- Có thật trong bản xuất: so năng lượng dải tần đặc trưng giữa master mới và master cũ (chưa có SFX) → **11/11 tăng 22–47 dB**.
- Nghe rõ: nghe thử trên bản thành phẩm (nhạc nền + lời đọc) → **11/11 CLEAR**, khớp đúng nghĩa.
- Loudness sau khi thêm SFX: **−16,2 LUFS**, true peak −4,3 dBFS (chuẩn: −16 LUFS / ≤ −1,5 dBFS).
- Luồng hình của MP4 **không đổi** (MD5 giống hệt bản cũ — chỉ thay lớp âm thanh).

---

## PHỤ LỤC B (Tập 01) — 23 CHỖ GIẢM BẠO LỰC (`kichban_tap01_22102026.md` → `_v2.md`)

Nguyên tắc: **giữ dữ kiện và luận điểm tâm lý, bỏ chi tiết thể xác**. Không thêm dữ kiện mới. Số câu và mã câu không đổi.

| Câu | Bản gốc | Bản v2 |
|---|---|---|
| `1.03#3` | …khiến cả khu phố chết lặng: *"Con khốn đó chết rồi."* | …một dòng trạng thái ngắn ngủi, đầy hằn học, thông báo rằng bà Dee Dee đã qua đời – khiến cả khu phố chết lặng |
| `1.08#1` | họ tìm thấy thi thể của người mẹ… | họ phát hiện người mẹ… đã qua đời trong phòng ngủ |
| `1.08#5` | Kẻ máu lạnh nào đã sát hại người mẹ tận tụy ấy, rồi bắt cóc… | Ai đã gây ra cái chết của người mẹ tận tụy ấy, rồi đưa đi… |
| `1.11#8` | kế hoạch đoạt mạng bà mẹ "thánh thiện" | kế hoạch dẫn đến cái chết của bà mẹ "thánh thiện" |
| `2.02#1` | chọn cách kết liễu mẹ ruột | đi đến một lựa chọn cực đoan với chính mẹ ruột |
| `2.02#2` | căn phòng ngủ đẫm máu | căn phòng ngủ |
| `2.07#1` | trực tiếp hủy hoại cơ thể con gái | trực tiếp tác động lên sức khỏe con gái |
| `2.07#2` | hàm răng bị mục ruỗng và phải nhổ bỏ toàn bộ răng cửa | sức khỏe răng miệng của cô bé bị tổn hại nghiêm trọng |
| `2.07#3` | phẫu thuật đặt ống truyền thức ăn trực tiếp qua thành bụng vào dạ dày | đặt ống nuôi ăn qua dạ dày |
| `2.07#4` | bôi thuốc gây tê vào nướu để nước bọt chảy ròng ròng… cắt bỏ tuyến nước bọt | tạo ra những triệu chứng giả trước mắt bác sĩ… một ca phẫu thuật tuyến nước bọt không cần thiết |
| `3.02#2` | biến đứa con… thành một phế nhân đau đớn | khiến đứa con… phải sống như một người bệnh |
| `3.07#2` | bị nghi bỏ thuốc diệt cỏ vào thức ăn của mẹ kế và bỏ đói mẹ ruột… | bị nghi có những hành vi gây hại cho chính người thân trong gia đình |
| `3.08#5` | Hãy làm cho con bé tàn tật và phụ thuộc hoàn toàn vào mình | Hãy khiến con bé tin rằng mình bệnh tật và phụ thuộc hoàn toàn vào mẹ |
| `3.08#6` | không thể tự ăn uống mà phải truyền qua ống thông dạ dày… vị Chúa tể duy nhất nắm giữ sự sống | tin rằng mình… không thể tự chăm sóc bản thân… người duy nhất nắm giữ cuộc sống |
| `3.10#6` | yếu ớt, vô tính và… | yếu ớt và… |
| `4.07#2` | chịu đựng sự đau đớn lặp đi lặp lại | chịu đựng những áp lực tiêu cực lặp đi lặp lại |
| `4.07#7` | siết chặt lại đến mức bầm tím | siết chặt lại như một lời cảnh cáo không thành tiếng |
| `4.07#8` | những trận đòn bằng móc áo, bị bỏ đói và bị trói vào thành giường suốt hai tuần | những hình phạt nghiêm khắc và sự kiểm soát ngột ngạt |
| `4.10#5` | dùng búa đập nát chiếc máy tính… đe doạ đập nát các ngón tay | phá hỏng chiếc máy tính… cảnh cáo cô không bao giờ được bước ra khỏi cửa |
| `4.13#2` | người đầu độc Gypsy | người gây ra bệnh tật cho Gypsy |
| `4.13#3` | bạo hành thể xác | kiểm soát hà khắc |
| `5.02#2` | lên kế hoạch sát hại mẹ ruột | lên kế hoạch dẫn đến cái chết của mẹ ruột |
| `5.02#3` | bạo hành y khoa | lạm dụng y khoa |
| `5.08#1` | thủ thuật y khoa đau đớn | thủ thuật y khoa xâm lấn |

**Giữ nguyên có chủ đích:** "ung thư máu" (tên bệnh) · "giết người cấp độ hai" ở `5.04#1` (tên tội danh trong bản án — đổi sẽ sai sự thật) · "cạo trọc đầu", "váy công chúa" ở `2.04#5`, `3.10#2` (cốt lõi của luận điểm *tước đoạt sự trưởng thành*, không mang tính bạo lực).

---

---

*Bản sao v9 trước khi chuyển thành tiêu chuẩn: `90_LUU_TRU/ke_hoach_cu/KeHoach_LamLai_Video_Tap01_v9.md`. Không file nguồn nào bị sửa.*
