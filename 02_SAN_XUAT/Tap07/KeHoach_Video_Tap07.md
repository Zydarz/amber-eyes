# HỒ SƠ SẢN XUẤT TẬP 07 · "BẢN ÁN GIẾT NGƯỜI BẰNG TIN NHẮN" (PHẦN B)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 07: Bản Án Giết Người Bằng Tin Nhắn** |
| Vụ án | Michelle Carter và Conrad Roy (Fairhaven / Plainville, Massachusetts, 2014–2017) |
| Chủ đề | Thao túng tâm lý kỹ thuật số, Hội chứng Münchausen qua mạng, Trách nhiệm hình sự từ xa |
| Tổng thời lượng | ~21–22 phút · 5 hồi · 147 câu thoại |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên Scott Gordon) · Cáo (Chuyên gia tâm lý) · N1 (Bà Lynn Roy) · N2 (Samantha Boardman) |
| Bộ ảnh nền | 61 ảnh 16:9 2K (`assets/bg/t7_*.png`), phong cách Dark graphic novel noir |
| Âm thanh | Stereo 3 lớp: BGM theo hồi + Ambience môi trường liên tục + SFX tiếng động (`.work/sfx_tap07.json`) |

## B2. Trạng thái kiểm soát chất lượng (QC)

- [x] Kịch bản chuẩn A2, loại bỏ 100% từ cấm V9, chuẩn hóa trích dẫn `“…”` (147/147 câu).
- [x] Bộ ảnh 61/61 ảnh 2112×1188 full-bleed tràn viền, V5 người thật chỉ hiện bóng lưng / không lộ mặt.
- [x] Bảng âm thanh `sfx_tap07.json` đầy đủ 9 dải ambience, 17 cue tiếng động, 4 đoạn music_drop.
- [x] Cấu hình `edition.py` đã hiệu chỉnh `act1_cue: 1.03`, `silence_cue: 2.11`, BGM H3 `bgm_cello_sad.mp3`.

> **⚠ DỰNG LẠI 06/11/2026 — kịch bản đã viết lại (05/11/2026, 147 câu / 50 element).**
> Bảng shot (mục 6) và timeline (`.work/timeline_s_t07.json` · 147 câu · 21:39) đã dựng lại theo
> kịch bản mới; lớp chữ trên hình viết lại cho khớp lời đọc mới. Timeline là **tạm** (đo theo
> tỉ lệ từ timeline cũ) — audio master cũ đã upload/dọn, cần đo lại khi dựng video.
> Ảnh tĩnh 3 ngôn ngữ: `.work/video3_t07/stills` · `.work/video3_EN_t07/stills` · `.work/video3_JA_t07/stills`.

## 6. DANH SÁCH SHOT — TẬP 07 (viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### HỒI 1 — BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART · nền chủ đạo `t7_kmart_parking_lot_morning`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s) | — | T1 | `t7_digital_coercion_screen` hiện dần từ đen | *HỒI 01 · BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART* | — | ⊘ |  |
| 1-01 | `1.02#1`–`#3` | H | T4 trích dẫn | `t7_digital_coercion_screen`, `pan` | *Thảm kịch không có hung khí, không có dấu vết vật lý tại hiện trường — hai nhân vật chính cách nhau hơn năm mươi cây số đường bộ.* | — | ✦ Cú |  |
| 1-02 | `1.02#4`–`#6` | H | T1 | `t7_highway_50km_isolation`, `still` | *Tất cả khởi nguồn từ những dòng tin nhắn phát sáng trong đêm và một chiếc bẫy tâm lý vô hình — vụ án tạo nên cơn sốt truyền thông và nỗi hoang tưởng tập thể.* | — | — |  |
| 1-03 | `1.04#1` | H | T1 | `t7_kmart_parking_lot_morning`, `pull` | *Sáng ngày 13 tháng 7 năm 2014, tại bãi đỗ xe của siêu thị Kmart ở thị trấn ven biển Fairhaven, bang Massachusetts.* | — | — |  |
| 1-04 | `1.04#2`–`#3` | H | T1 | `t7_ford_f250_black_truck`, `pan` | *Chiếc xe bán tải hiệu Ford F-250 màu đen đỗ im lìm ở một góc khuất; khi cảnh sát tìm đến, người bên trong cabin đã không còn dấu hiệu sinh tồn.* | — | — |  |
| 1-05 | `1.06#1`–`#2` | H | T1 | `t7_water_pump_equipment`, `still` | *Bên trong cabin xe, Conrad Henri Roy Đệ Tam nằm bất động trong nỗi tuyệt vọng cô độc.* | — | — |  |
| 1-06 | `1.06#3`–`#5` | H | T1 | `t7_tugboat_harbor_fog`, `pull` | *Conrad Roy không phải là một thanh niên ngỗ ngược hay bất hảo — cậu là một chàng trai khôi ngô, giàu lòng nhân hậu, vừa tốt nghiệp trung học và nhận được tấm bằng thuyền trưởng điều khiển tàu kéo.* | — | — |  |
| 1-07 | `1.06#6`–`#7` | H | T1 | `t7_tugboat_captain_license`, `pan` | *Phía sau nụ cười hiền lành là một tâm hồn mong manh, thường xuyên phải vật lộn với những cơn trầm cảm nặng và nỗi âu lo triền miên.* | — | — |  |
| 1-08 | `1.06#8` | H | T1 | `t7_mothers_empty_kitchen_phone`, `pull` | *Hãy hình dung nỗi đau xé lòng của mẹ cậu, bà Lynn Roy, trong buổi sáng định mệnh hôm ấy.* | — | →N1 |  |
| 1-09 | `1.07#1`–`#3` | N1 | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *Cả buổi sáng linh cảm có điều gì đó chẳng lành — bà gọi liên tục, chỉ nhận lại tiếng chuông reo vô vọng trong khoảng không.* | — | ✦ Cừu |  |
| 1-10 | `1.07#4`–`#5` | N1 | T1 | `t7_kmart_police_perimeter`, `pull` | *Ban đầu bà chỉ nghĩ con mình mệt mỏi vì cuộc chiến với trầm cảm — không thể ngờ có kẻ săn mồi vô hình đã tước đi đứa con yêu quý từ khoảng cách xa xôi.* | — | →H |  |
| 1-11 | `1.09#1`–`#3` | H | T1 | `t7_forensic_evidence_phone`, `pan` | *Chiếc điện thoại di động thông minh — nơi lưu giữ toàn bộ dữ liệu giao tiếp những ngày cuối đời của Conrad Roy — được thu giữ để giám định pháp y.* | — | →D |  |
| 1-12 | `1.10#1`–`#4` | D | T4 trích dẫn | `t7_digital_forensic_extraction`, `still` | *Trích xuất pháp y phát hiện một kho lưu trữ khổng lồ: hàng nghìn dòng tin nhắn văn bản, và người trao đổi dày đặc nhất chính là một nữ sinh mười bảy tuổi tên Michelle Carter.* | — | ✦ Sói · →H |  |
| 1-13 | `1.11#1`–`#2` | H | T1 | `t7_psychological_trap_metaphor`, `pull` | *Không phải lời an ủi hay động viên chia sẻ — mà là một chiến dịch thúc ép có hệ thống, một chiếc bẫy tinh vi giăng ra để triệt tiêu mọi lối thoát của nạn nhân.* | — | →C |  |
| 1-14 | `1.12#1`–`#3` | C | T1 | `t7_clinical_depression_shadow`, `pan` | *Người rơi vào trạng thái trầm cảm nặng có cấu trúc nhận thức phân mảnh, giằng xé giữa bản năng sinh tồn và mong muốn thoát khỏi nỗi đau tâm trí.* | — | ✦ Cáo · →H |  |
| 1-15 | `1.13#1`–`#2` | H | T2 thẻ hồ sơ | `t7_dossier_carter_case_07`, `still` | *Những dòng chữ phát sáng trên màn hình không còn là công cụ giao tiếp vô hại, mà đã trở thành vũ khí đoạt mạng người tàn nhẫn.* | — | — |  |

### HỒI 2 — MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN · nền chủ đạo `t7_late_night_bedroom_phone`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#3` | H | T1 | `t7_florida_beach_encounter_2012`, `pan` | *Hai người tình cờ gặp nhau lần đầu năm 2012 tại bang Florida: Conrad mười sáu tuổi, Michelle Carter vừa tròn mười lăm tuổi.* | — | →D |  |
| 2-02 | `2.03#1`–`#2` | D | T7 tuyến đường | `t7_massachusetts_route_map`, `still` | *Michelle Carter sống tại Plainville, chỉ cách nơi Conrad ở tại Fairhaven khoảng ba mươi lăm dặm — chưa đầy một giờ lái xe.* | — | — |  |
| 2-03 | `2.03#3`–`#4` | D | T1 | `t7_late_night_bedroom_phone`, `pull` | *Hơn hai năm duy trì mối quan hệ, họ chỉ gặp mặt trực tiếp đúng vài lần ngắn ngủi; toàn bộ thế giới tình cảm tồn tại trên không gian số.* | — | →H |  |
| 2-04 | `2.04#1`–`#3` | H | T4 trích dẫn | `t7_plainville_suburban_house`, `pan` | *Trong giai đoạn đầu, Michelle Carter tỏ ra là một người bạn gái biết lắng nghe và sẻ chia — thậm chí từng khuyên Conrad nên tìm đến chuyên gia tâm lý và bác sĩ điều trị.* | — | — |  |
| 2-05 | `2.04#4`–`#6` | H | T1 | `t7_two_phone_screens_contrast`, `still` | *Bước sang đầu tháng 7 năm 2014, một bước ngoặt tâm lý lạnh lùng: Michelle quay ngoắt một trăm tám mươi độ và trở thành người thúc đẩy thảm kịch.* | — | →D |  |
| 2-06 | `2.06#1` | D | T4 trích dẫn | `t7_sms_transcript_forensic_binder`, `pull` | *Trích xuất hồ sơ điện thoại từ đầu tháng 7 cho thấy mức độ dày đặc và lạnh lùng đến rợn người của các tin nhắn thúc ép.* | — | — |  |
| 2-07 | `2.06#2` | D | T1 | `t7_ticking_clock_deadlines`, `pan` | *Michelle liên tục trách móc rằng Conrad chỉ giỏi nói mà không làm, và thúc giục cậu không được tiếp tục trì hoãn nữa.* | — | →H |  |
| 2-08 | `2.07#1`–`#2` | H | T1 | `t7_family_photo_frame_shadow`, `still` | *Khi Conrad lo sợ cha mẹ và hai em gái sẽ đau lòng, Michelle lạnh lùng tước bỏ rào cản đạo đức đó: gia đình rồi sẽ hiểu và chấp nhận thực tế.* | — | →C |  |
| 2-09 | `2.08#1`–`#4` | C | T1 | `t7_psychological_coercion_chess`, `pull` | *Chu kỳ ảo tưởng và quỹ đạo leo thang dung nạp kích thích: khi cảm giác quan trọng bị lờn, cô ta chuyển sang thao túng đánh thẳng vào lòng tự trọng và sự xấu hổ của nạn nhân.* | — | →H |  |
| 2-10 | `2.09#1`–`#2` | H | T1 | `t7_kmart_lot_midnight_darkness`, `pan` | *Đêm ngày 12 tháng 7 năm 2014, chiếc bẫy tâm lý vô hình ấy đã sập xuống hoàn toàn.* | — | — |  |
| 2-11 | `2.09#3`–`#4` | H | T1 | `t7_open_truck_door_fresh_air`, `still` | *Ngay lằn ranh mong manh giữa sự sống và cái chết, bản năng sinh tồn trỗi dậy: Conrad hoảng sợ, mở cửa cabin bước ra ngoài tìm không khí và sự an toàn.* | — | ⊘ |  |
| 2-12 | `2.09#5`–`#6` | H | T1 | `t7_night_sky_breath_of_life`, `pull` | *Cậu giữ máy điện thoại kết nối liên tục với Michelle Carter, nhưng điều nhận được không phải lời can ngăn hay một chiếc phao cứu sinh kéo cậu về phía cuộc sống.* | — | ⊘ · →D |  |
| 2-13 | `2.10#1`–`#2` | D | T1 | `t7_incoming_call_timer_40min`, `pan` | *Cuộc gọi đêm hôm ấy kéo dài hơn bốn mươi phút và không được hệ thống viễn thông ghi âm trực tiếp.* | — | — |  |
| 2-14 | `2.10#3` | D | T1 | `t7_closed_car_window_fog`, `still` | *Cô ta không gọi cấp cứu 911, không hề báo cho gia đình nạn nhân, mà lạnh lùng giữ máy cho đến khi mọi âm thanh bên kia đầu dây hoàn toàn im bặt.* | — | ⊘ · →H |  |

### HỒI 3 — VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH · nền chủ đạo `t7_empty_theater_spotlight`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1`–`#2` | H | T1 | `t7_empty_theater_spotlight`, `pan` | *Câu hỏi lớn khiến công chúng bàng hoàng: động cơ thực sự phía sau hành vi tàn nhẫn này là gì?* | — | →C |  |
| 3-02 | `3.03#1`–`#3` | C | T1 | `t7_drama_masks_digital_glitch`, `still` | *Rối loạn nhân cách kịch tính kết hợp Hội chứng Münchausen kỹ thuật số: Conrad Roy bị “Vật hóa” thành một món đạo cụ phục vụ vở kịch ái kỷ của cô ta.* | — | →H |  |
| 3-03 | `3.04#1`–`#3` | H | T1 | `t7_highschool_empty_lockers`, `pull` | *Tại trường trung học King Philip, Michelle Carter là một nữ sinh mờ nhạt, vụng về trong giao tiếp và luôn cảm thấy mình bị bạn bè cô lập.* | — | →D |  |
| 3-04 | `3.05#1`–`#2` | D | T1 | `t7_vintage_tv_glee_glow`, `pan` | *Tại tòa án, cơ quan công tố vạch trần một phát hiện rùng mình: Michelle Carter bị ám ảnh sâu sắc bởi loạt phim truyền hình ca nhạc nổi tiếng Glee.* | — | — |  |
| 3-05 | `3.05#3`–`#4` | D | T1 | `t7_copied_script_lines_notebook`, `still` | *Các chuyên viên pháp y phát hiện Michelle đã chép lại nguyên văn nhiều câu thoại đẫm nước mắt trong bộ phim đó để gửi cho bạn bè và cho Conrad.* | — | →H |  |
| 3-06 | `3.06#1`–`#3` | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Michelle Carter muốn có một bi kịch của riêng mình để trở thành tâm điểm của sự ngưỡng mộ và an ủi — và điều kiện tiên quyết là Conrad phải biến mất khỏi cõi đời.* | — | — |  |
| 3-07 | `3.06#4` | H | T1 | `t7_suburban_living_room_tv`, `pan` | *Cô ta đóng vai một người bạn gái đang hoảng loạn tột độ, dù chính cô ta là người nắm giữ toàn bộ diễn biến qua chiếc điện thoại.* | — | →C |  |
| 3-08 | `3.07#1`–`#3` | C | T1 | `t7_puppet_strings_metaphor`, `still` | *Cơ chế “Chia ngăn nhận thức” kết hợp kỹ thuật trung hòa đạo đức để vô hiệu hóa hoàn toàn cảm giác tội lỗi.* | — | →H |  |
| 3-09 | `3.08#1`–`#3` | H | T1 | `t7_social_media_notifications_flood`, `pull` | *Ngay sau khi Conrad qua đời, Michelle Carter đăng trạng thái thương tiếc đẫm lệ và tổ chức giải bóng mềm từ thiện mang tên “Homers for Conrad”.* | — | — |  |
| 3-10 | `3.08#4`–`#5` | H | T1 | `t7_baseball_field_charity_empty`, `pan` | *Trong sự kiện ấy, Michelle Carter xuất hiện rạng rỡ ở vị trí trung tâm, đón nhận sự thán phục của cộng đồng địa phương — chiếc mặt nạ hoàn hảo nhất của cuộc đời cô ta.* | — | — |  |
| 3-11 | `3.08#6` | H | T1 | `t7_cracked_porcelain_mask`, `still` | *Cho đến một ngày, thói quen chia sẻ bệnh lý và sự ngạo mạn đã tự tay giật phăng lớp vỏ bọc tinh vi đó.* | — | — |  |

### HỒI 4 — DÒNG TIN NHẮN ĐẦY TỘI LỖI VÀ BẢN ÁN LỊCH SỬ · nền chủ đạo `t7_taunton_courthouse_exterior`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1`–`#4` | H | T4 trích dẫn | `t7_confession_text_timestamp`, `pan` | *Ngày 15 tháng 9 năm 2014, hai tháng sau cái chết của Conrad, Michelle đã gửi một dòng tin nhắn định mệnh cho người bạn thân Samantha Boardman.* | — | →N2 |  |
| 4-02 | `4.03#1`–`#2` | N2 | T1 | `t7_witness_trembling_phone`, `still` | *Michelle thừa nhận đang nói chuyện điện thoại khi Conrad sợ hãi bước ra ngoài xe, và chính cô ta đã ra lệnh cho cậu quay trở lại cabin.* | — | ✦ Mèo |  |
| 4-03 | `4.03#3` | N2 | T4 trích dẫn | `t7_confession_message_turn`, `pull` | *Người bạn gái ngày nào cũng khóc lóc tỏ vẻ đau thương trước mặt mọi người, hóa ra chính là kẻ đã lạnh lùng đẩy Conrad vào chỗ chết.* | — | →H |  |
| 4-04 | `4.05#1`–`#3` | H | T2 thẻ hồ sơ | `t7_bristol_county_indictment_stamp`, `pan` | *Dòng tin nhắn tự thú cùng kho dữ liệu trích xuất đã trở thành bằng chứng thép để khởi tố Michelle Carter — phiên tòa mở màn tháng 6 năm 2017 tại Taunton.* | — | — |  |
| 4-05 | `4.05#4`–`#5` | H | T1 | `t7_taunton_courthouse_exterior`, `still` | *Cô ta từ bỏ quyền được xét xử bởi bồi thẩm đoàn, đặt toàn bộ số phận pháp lý vào tay một người duy nhất: Thẩm phán Lawrence Moniz.* | — | — |  |
| 4-06 | `4.05#6` | H | T1 | `t7_empty_courtroom_bench_trial`, `pull` | *Một canh bạc nhằm tránh sự phẫn nộ cảm xúc từ công chúng để dựa vào các lập luận kỹ thuật pháp lý khô khan.* | — | →D |  |
| 4-07 | `4.06#1`–`#2` | D | T4 trích dẫn | `t7_courtroom_projection_screen`, `pan` | *Luật sư bào chữa Joseph Cataldo lập luận thân chủ không hề có mặt tại hiện trường và dẫn Tu chính án đầu tiên của Hiến pháp Hoa Kỳ về quyền tự do ngôn luận.* | — | — |  |
| 4-08 | `4.06#3`–`#4` | D | T1 | `t7_us_constitution_amendment1`, `still` | *Phó Công tố viên Katie Rayburn trình chiếu hàng loạt chuỗi tin nhắn với mốc thời gian chi tiết và đanh thép, chứng minh đây là một chuỗi thúc ép có tính toán tỉ mỉ.* | — | →C |  |
| 4-09 | `4.07#1`–`#4` | C | T1 | `t7_prescription_pill_bottle_celexa`, `pull` | *Lập luận tự bào chữa cho rằng Carter bị “say thuốc không tự nguyện” do tác dụng phụ của thuốc Celexa — nhưng tòa án đã bác bỏ hoàn toàn.* | — | →H |  |
| 4-10 | `4.08#1`–`#4` | H | T1 | `t7_judge_moniz_bench_gavel`, `pan` | *Ngày 16 tháng 6 năm 2017, Thẩm phán Lawrence Moniz đọc bản phán quyết bằng giọng đanh thép: việc Carter ra lệnh cho Conrad quay trở lại xe cấu thành hành vi liều lĩnh và vô lương tâm.* | — | — |  |
| 4-11 | `4.08#5` | H | T1 | `t7_courtroom_breathless_silence`, `still` | *Thẩm phán tuyên bố đanh thép: Michelle Carter phạm tội ngộ sát.* | — | — |  |
| 4-12 | `4.10#1`–`#2` | H | T2 thẻ hồ sơ | `t7_court_verdict_document_guilty`, `pull` | *Tháng 8 năm 2017, Michelle Carter bị kết án hai năm rưỡi tù giam, với mười lăm tháng phải chấp hành thực tế sau song sắt.* | — | — |  |
| 4-13 | `4.10#3` | H | T1 | `t7_bristol_county_jail_bars`, `pan` | *Sự sụp đổ cái tôi ái kỷ và nỗi tự thương hại bản thân bệnh lý khi chiếc mặt nạ danh dự vỡ vụn trước toàn thế giới.* | — | — |  |

### HỒI 5 — ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD · nền chủ đạo `t7_digital_lighthouse_beacon`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#3` | H | T1 | `t7_massachusetts_state_house_dome`, `pan` | *Lần đầu tiên, hệ thống pháp luật công nhận: khoảng cách địa lý và màn hình điện thoại không bao giờ là tấm khiên che chắn cho trách nhiệm hình sự.* | — | — |  |
| 5-02 | `5.02#4`–`#5` | H | T1 | `t7_conrads_law_legislative_bill`, `still` | *Ngôn từ trong không gian số có thể mang sức mạnh thao túng tinh thần và trở thành vũ khí giết người không chạm tay.* | — | →C |  |
| 5-03 | `5.03#1`–`#3` | C | T1 | `t7_digital_cage_smartphone_glow`, `pull` | *Những chiếc màn hình phát sáng thâu đêm biến thành lồng giam tâm lý vô hình, nơi sự thao túng diễn ra mà gia đình hoàn toàn không hay biết.* | — | →H |  |
| 5-04 | `5.04#1`–`#3` | H | T4 trích dẫn | `t7_conrads_law_legislative_bill`, `pan` | *Đạo luật Conrad — dự luật được các nhà lập pháp thông qua để hình sự hóa hành vi ép buộc hoặc thao túng người khác tự hủy hoại bản thân.* | — | — |  |
| 5-05 | `5.04#4` | H | T8 cờ | `t7_redflag1_isolated_virtual_bubble`, `pan` | *01* · **CẢNH BÁO ĐỎ 1 — CẢNH GIÁC TRƯỚC CÁC MỐI QUAN HỆ ẢO SIÊU TỐC VÀ CÔ LẬP** | — | — |  |
| 5-06 | `5.04#5`–`#7` | H | T8 cờ | `t7_redflag2_manipulative_text_provocation`, `still` | *02* · **CẢNH BÁO ĐỎ 2 — NHẬN DIỆN CHIÊU BÀI KHIÊU KHÍCH TỰ TRỌNG VÀ THÁCH THỨC TIÊU CỰC** | — | — |  |
| 5-07 | `5.04#8`–`#10` | H | T8 cờ | `t7_redflag3_performative_grief_stage`, `pull` | *03* · **CẢNH BÁO ĐỎ 3 — CẢNH GIÁC VỚI KẺ THÍCH KỊCH TÍN HÓA BI KỊCH VÀ KHAO KHÁT SỰ CHÚ Ý TRÊN MẠNG XÃ HỘI** | — | — |  |
| 5-08 | `5.04#11`–`#13` | H | T8 cờ | `t7_redflag4_disconnect_phone_dawn`, `pan` | *04* · **CẢNH BÁO ĐỎ 4 — LẮNG NGHE BẢN NĂNG SINH TỒN VÀ DỨT KHOÁT CẮT ĐỨT LIÊN LẠC** | — | — |  |
| 5-09 | `5.04#14`–`#15` | H | T1 | `t7_redflag4_disconnect_phone_dawn`, `pull` | *Khoảnh khắc bạn nhận ra sự độc hại trong lời nói của đối phương, đó là tiếng gọi cứu rỗi của bản năng sống — hãy buông chiếc điện thoại xuống và bước ra ngoài thế giới thực.* | — | — |  |
| 5-10 | `5.04#16`–`#17` | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Ngôn từ trên màn hình không có trọng lượng vật lý, nhưng chúng mang sức mạnh có thể cứu rỗi hoặc hủy hoại một sinh mệnh con người.* | — | — |  |
| 5-11 | `5.04#18`–`#19` | H | T1 | `t7_closing_dossier_white_rose`, `pull` | *Cảm ơn quý vị đã đồng hành cùng Amber Eyes — hãy bấm đăng ký kênh và chia sẻ góc nhìn của bạn ở phần bình luận bên dưới.* | — | — |  |
| 5-12 | hết tập (10 s) | — | T1 | `t7_closing_dossier_white_rose`, `pull` | *HỒ SƠ TẬP 07 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật* | — | — | — |

**Tổng:** 66 shot · 147 câu · 34 element lời (5 hồi) · nền dùng 61 loại. Bảng dựng lại 06/11/2026 theo kịch bản viết lại 05/11/2026.
---

## PHỤ LỤC C (Tập 07) — AUDIO HIGGS AUDIO v3 TRÊN KAGGLE (bắt đầu 02/11/2026)

- **Kịch bản vá V9 01/11/2026 còn 147 câu** (cũ 164; ~40 câu đổi chữ, 1.06#8 và 4.02#4 mới; 2.06, 2.07, 2.09, 3.06, 3.08, 4.03, 4.08, 5.02 bớt câu; 5.04 thêm câu đường dây nóng #16). `script_tap07.json` tách lại. ✅ **Mục 6 đã viết lại 03/11/2026 theo 147 câu** — 66 shot (thêm 4 dòng: `1-15` cho câu `1.13#1`–`#2`, `5-10`, `5-11`, và thẻ kết `5-12`; **không dòng nào bị xoá**; remap 27 dòng mã câu; tách lại khối cờ đỏ ở Hồi 5), QC A9.2 **12/12 cổng xanh**. Chi tiết: `BaoCao_QC_Tap07_20261103.md`.
- **Sao lưu bản MiniMax** (script, acting, make_acting, sfx, manifest, timeline, shots, master mp3, srt): `.work/_cu/t07_minimax_20261102/`.
- **P0 chuyển mã theo nội dung (K4):** `make_acting_tap07.py` KEY: bỏ 2.06#4/#5 và 4.03#2 cũ; đổi 1.07#6→#5 · 2.06#6→#2 · 2.07#4→#2 · 2.09#4→#3 · 2.09#6→#4 · 3.06#6→#4 · 3.08#6/#7→#5/#6 · 4.03#5→#2 (câu "bảo quay lại xe") · 4.03#8→#3 · 4.08#7→#5 · 5.04#16/17/18→#17/18/19. `sfx_tap07.json`: ambience/cue 1.07#6→#5, 3.08#7→#6, 4.03#8→#3, 5.04#18→#19; music_drop 2.10#3→**2.10#2**, 4.03#5→**4.03#2** (theo câu hé lộ). 0 mã tham chiếu thiếu; summary/act1/silence/click cue tồn tại; nhạc 5/5 hồi OK.
- **Lời đọc số (`SPOKEN` trong `make_acting_tap07.py`):** `vi_numbers` đọc sai "911" → "chín trăm mười một" và số điện thoại → số đếm. Lời đọc: 2.10#3 "chín một một"; 5.04#16 "không chín sáu, ba không sáu, một bốn một bốn" + "một một một". Phụ đề/chữ hình giữ câu gốc (G6).
- **P1/P2:** payload 147 câu, 0 chữ số, 0 `...`, 0 thẻ cảm xúc · spec 294 file (H 98 · D 21 · C 20 · N1 5 · N2 3 câu) · kernel `chiduong2026/amber-eyes-higgs-prod-t07-kaggle-gpu`, `verify: OK`.
- 5.04#16 gọi **111** là "Tổng đài Quốc gia" (111 là tổng đài bảo vệ trẻ em): **người dùng chốt giữ nguyên chữ (02/11/2026)**.
- **Kaggle:** đăng nhập lại OAuth 02/11 22:55 (token cũ hết hạn 22:37). Lượt 1 294 file (~35 phút) · vòng 2 20 file (10 câu).
- **F0 câu neutral (AC/YIN):** H 123/130 · D 87/86 · C 207/207 · N1 180 · N2 287 Hz. **G9** D–H 5,97 · C–H 8,15 · H–N1 6,86 · H–N2 14,93 · C–D 14,96 nc ✅. G8: loại 12 bản; **1.06#2 mọi bản (4/4) Host đọc trầm 93–104 Hz** (A11 #75) ⇒ dùng bản cao nhất s0, đưa vào danh sách nghe.
- **CER `listen_audio`:** lượt 1 31/147 câu có bản > 2% → sau vòng 2 còn 3: 2.10#3 / 5.04#16 là **CER giả** (ASR ghi "911", "096 306 1414" bằng chữ số) · 4.06#2 chọn tay bản s2 2,7% vì bản 2,1% đọc **"Cô ta"** thay "Ông ta" (A11 #76).
- **Whisper large-v3 + UTMOS (Kaggle, cả lượt 1 và vòng 2):** UTMOS tb H 2,54 · N1 2,92 · C 3,05 · D 3,23 · N2 3,39 (H thấp nhất, giống Tập 06). Trên bản đã chọn: 1 câu cả hai ASR cùng báo (4.06#2), 40 câu chỉ Whisper báo (đa số tên riêng: Conrad→"Con Rat", Lynn→"Linh").
- **Master** `xuat_ban/Tap07_master.mp3`: **1134,9 s · −16,2 LUFS · true peak −1,7 dBFS · 0 khoảng câm > 0,3 s ở −60 dB · lời đầu 23,0 s** ✅. 147/147 file; đuôi lặng dài nhất 0,9 s (1.10#1). Hồi: 23,0 / 249,5 / 460,7 / 666,3 / 894,2 s.
- **Danh sách nghe:** `02_SAN_XUAT/Tap07/CanNghe_Tap07_higgs.md`. Mô tả YouTube PHẢI thêm dòng ghi công Higgs (QUY_TAC_AUDIO_HIGGS §2).
- **Video cuối 03/11/2026:** `xuat_ban/Tap07_master.mp4` — **1134,867 s (18:55) · 423,5 MB · 1920×1080@30 · H.264 + AAC 48 kHz**. `picture.mp4` lệch `timeline.total` **−0,003 s** (H14 ✅). QC A9.1–A9.4 **đạt toàn bộ**: lệch A/V **0,0 ms** (r = 0,9999) · −16,0 LUFS · true peak −1,9 dBFS · 0 khoảng lặng > 0,3 s · giải mã 0 lỗi · 290 cue SRT · thẻ kết 15,34 % pixel sáng · **H10**: 0 đoạn lặp nền > 4 shot. Thumbnail đổi sang nền `t7_confession_text_timestamp` (H11). Báo cáo: `BaoCao_QC_Tap07_20261103.md`.
- **Nguồn tham khảo 03/11/2026:** đã tra cứu + kiểm chứng **54 nguồn công khai** cho **56 dữ kiện** trong lời thoại — bảng đối chiếu từng câu: `02_SAN_XUAT/Tap07/nguon_tham_khao.md`; khối nguồn rút gọn cho mô tả YouTube (23 nguồn, `mo_ta.txt` = 4.874 ký tự, dưới giới hạn 5.000): `02_SAN_XUAT/Tap07/nguon_mo_ta.txt`. Nguồn gốc là **hồ sơ Tòa Tối cao Massachusetts** (phụ lục `Commonwealth v. Carter`, 2019) — mọi dữ kiện về nguyên văn tin nhắn dẫn về đây. Kiểm tra link: 30/54 fetch HTTP 200 + 24 link bị chống bot (vẫn mở bằng trình duyệt), **0 link chết** (trang HBO đã bị gỡ ⇒ đổi sang Hulu).
  **Ba điểm đánh dấu ⚠ trong bảng:** `3.02#2` "gia đình khá giả" (chỉ có nguồn mô tả gia đình có điều kiện ổn định) · `3.03#1` khung lý thuyết HPD/Münchausen kỹ thuật số (**không phải chẩn đoán y kế**) · `5.02#5` **Đạo luật Conrad tới 11/2026 vẫn CHƯA được thông qua** (lời dẫn nói đúng là dự luật đang vận động; còn nằm ở Bill S.1109 / Quý giai 194).
- **Còn lại (03/11/2026):** nghe duyệt giọng theo `CanNghe_Tap07_higgs.md` (2 câu chọn tay + 40 câu chỉ Whisper báo). Điền nguồn: **đã xong**.
