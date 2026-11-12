# HỒ SƠ SẢN XUẤT TẬP 07 · "BẢN ÁN GIẾT NGƯỜI BẰNG TIN NHẮN" (PHẦN B)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 07: Bản Án Giết Người Bằng Tin Nhắn** |
| Vụ án | Michelle Carter và Conrad Roy (Fairhaven / Plainville, Massachusetts, 2014–2017) |
| Chủ đề | Thao túng tâm lý kỹ thuật số, Hội chứng Münchausen qua mạng, Trách nhiệm hình sự từ xa |
| Tổng thời lượng | **30:43** (ước lượng — timeline tạm, chưa có audio master bản mới) · 5 hồi · **219 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên Scott Gordon) · Cáo (Chuyên gia tâm lý) · N1 (Bà Lynn Roy) · N2 (Samantha Boardman) |
| Bộ ảnh nền | 61 ảnh 16:9 2K (`assets/bg/t7_*.png`), phong cách Dark graphic novel noir |
| Âm thanh | Stereo 3 lớp: BGM theo hồi + Ambience môi trường liên tục + SFX tiếng động (`.work/sfx_tap07.json`) |

## B2. Trạng thái kiểm soát chất lượng (QC)

- [x] Kịch bản chuẩn A2, loại bỏ 100% từ cấm V9, chuẩn hóa trích dẫn `“…”` (219/219 câu).
- [x] Bảng shot mục 6 dựng lại 09/11/2026: **223 dòng** (218 shot nội dung + 4 thẻ chuyển hồi + 1 thẻ kết) · H10 đạt (0 shot > 15 s).
- [x] Bộ ảnh 61/61 ảnh 2112×1188 full-bleed tràn viền, V5 người thật chỉ hiện bóng lưng / không lộ mặt.
- [x] Bảng âm thanh `sfx_tap07.json` đầy đủ 9 dải ambience, 17 cue tiếng động, 4 đoạn music_drop.
- [x] Cấu hình `edition.py` đã hiệu chỉnh `act1_cue: 1.03`, `silence_cue: 2.11`, BGM H3 `bgm_cello_sad.mp3`.

> **⚠ DỰNG LẠI 09/11/2026 — kịch bản đã viết lại (07/11/2026, 219 câu / 50 element).**
> Bảng shot (mục 6) và timeline (`.work/timeline_s_t07.json` · 219 câu · **30:43**) đã dựng lại theo
> kịch bản mới; lớp chữ trên hình = **nguyên văn câu kịch bản** của shot (219/219 câu).
> Timeline là **tạm** (ước lượng theo RATE ký tự/s của timeline cũ — chưa có audio master bản mới);
> thời lượng shot trong bảng là số ước lượng, cần đo lại khi dựng video.
> Ảnh tĩnh 3 ngôn ngữ (223 ảnh/ngôn ngữ): `.work/video3_t07/stills` · `.work/video3_EN_t07/stills` · `.work/video3_JA_t07/stills`.
> **H9**: `text_scrim` 65 shot (đo thật bằng `_t07_scan_contrast.py`, ngưỡng >8% nét chữ bị chìm; hợp 3 ngôn ngữ) — sau khi áp: **0 shot** vượt ngưỡng ở cả 3 bản (max 6,7% / 6,6% / 7,8%).
> **H12**: `OUTRO` 10 s → **6 s** ⇒ thẻ kết (shot `5-37`) dài 7,5 s ⇒ ảnh tĩnh chụp ở giữa shot **không còn bị fade đen** (max 249 · 25,2% pixel sáng).
> Thẻ giới thiệu nhân vật (first-appearance card) đặt lên cao + có nền tối (`edition.py`: `intro_card_pos` / `intro_card_panel` / `intro_card_hold`) ⇒ hết chữ đè chữ ở `1-01` / `1-22` / `1-32`; hồi quy Tập 01: hash ảnh tĩnh **không đổi**.

## 6. DANH SÁCH SHOT — TẬP 07 (viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### HỒI 1 — BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART · nền chủ đạo `t7_kmart_parking_lot_morning`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.02#1` (3,6 s) | H | T1 | `t7_digital_coercion_screen`, `pull` | *Chào mừng quý vị đã quay trở lại với Amber Eyes.* | — | ✦ Cú |  |
| 1-02 | `1.02#2` (10,8 s) | H | T1 | `t7_highway_50km_isolation`, `still` | *Hôm nay, chúng ta cùng giải phẫu một hồ sơ tội phạm đặc biệt chưa từng có tiền lệ: Tội phạm không chạm tay và sự thao túng tâm lý trong không gian số.* | — | — |  |
| 1-03 | `1.02#3` (11,2 s) | H | T1 | `t7_digital_lighthouse_beacon`, `push` | *Hãy hình dung một thảm kịch không có hung khí vật lý, không có dấu vết xô xát tại hiện trường, và hai nhân vật chính ở cách xa nhau hơn năm mươi sáu cây số.* | — | — |  |
| 1-04 | `1.02#4` (8,2 s) | H | T1 | `t7_social_media_notifications_flood`, `pan` | *Thế nhưng, một thiếu nữ khi ấy mới mười bảy tuổi về sau vẫn phải nhận bản án ngộ sát lịch sử trước tòa án Hoa Kỳ.* | — | — |  |
| 1-05 | `1.02#5` (8,4 s) | H | T1 | `t7_night_sky_breath_of_life`, `pull` | *Toàn bộ bi kịch khởi nguồn từ những dòng tin nhắn phát sáng âm thầm trong đêm khuya và một chiếc bẫy tâm lý vô hình.* | — | — |  |
| 1-06 | `1.02#6` (8,5 s) | H | T1 | `t7_digital_coercion_screen`, `still` | *Vụ án đã tạo nên một cơn sốt truyền thông toàn cầu cùng nỗi hoang tưởng tập thể, làm rúng động toàn bộ dư luận xã hội.* | — | — |  |
| 1-07 | `1.02#7` (8,9 s) | H | T1 | `t7_highway_50km_isolation`, `push` | *Một lời cảnh tỉnh nghiêm khắc về mặt tối của thế giới kết nối ảo, nơi ngôn từ có thể biến thành vũ khí đoạt mạng con người.* | — | — |  |
| 1-08 | `1.04#1` (10,1 s) | H | T1 | `t7_kmart_parking_lot_morning`, `pan` | *Sáng ngày 13 tháng 7 năm 2014, tại bãi đỗ xe của siêu thị Kmart thuộc thị trấn ven biển Fairhaven, bang Massachusetts.* | — | — |  |
| 1-09 | `1.04#2` (10,0 s) | H | T1 | `t7_ford_f250_black_truck`, `pull` | *Một chiếc xe bán tải hiệu Ford F-250 màu đen đỗ im lìm suốt nhiều giờ liền ở một góc khuất vắng vẻ phía sau siêu thị.* | — | — |  |
| 1-10 | `1.04#3` (10,2 s) | H | T1 | `t7_kmart_police_perimeter`, `still` | *Khi lực lượng cảnh sát địa phương tiếp cận và mở cửa phương tiện, người bên trong cabin đã không còn dấu hiệu sinh tồn.* | — | — |  |
| 1-11 | `1.04#4` (8,2 s) | H | T1 | `t7_closed_car_window_fog`, `push` | *Một bầu không khí ngột ngạt bao trùm toàn bộ không gian chiếc xe kín mít dưới cái nắng hè oi ả.* | — | — |  |
| 1-12 | `1.04#5` (10,1 s) | H | T1 | `t7_water_pump_equipment`, `pan` | *Mặt trời buổi sáng rọi chiếu xuống bãi đỗ xe nhựa đường bốc hơi nóng nhưng bên trong cabin lại lạnh lẽo sự tuyệt vọng.* | — | — |  |
| 1-13 | `1.04#6` (7,7 s) | H | T1 | `t7_kmart_parking_lot_morning`, `pull` | *Không hề có dấu vết của sự giằng co, đồ đạc của nạn nhân vẫn còn nguyên vẹn trên ghế phụ.* | — | — |  |
| 1-14 | `1.06#1` (7,9 s) | H | T1 | `t7_water_pump_equipment`, `still` | *Bên trong cabin xe, chàng trai trẻ mười tám tuổi Conrad Henri Roy Đệ Tam nằm bất động trong nỗi tuyệt vọng cô độc.* | — | — |  |
| 1-15 | `1.06#2` (5,6 s) | H | T1 | `t7_tugboat_harbor_fog`, `push` | *Cậu đã tự tước đoạt mạng sống của chính mình sau những giằng xé nội tâm đau đớn.* | — | — |  |
| 1-16 | `1.06#3` (7,3 s) | H | T1 | `t7_tugboat_captain_license`, `pan` | *Conrad Roy không phải là một thanh niên ngỗ ngược hay hư hỏng như nhiều định kiến xã hội thường lầm tưởng.* | — | — |  |
| 1-17 | `1.06#4` (7,6 s) | H | T1 | `t7_highschool_empty_lockers`, `pull` | *Cậu là một chàng trai khôi ngô, giàu lòng nhân ái, chăm chỉ và có một tương lai nghề nghiệp xán lạn phía trước.* | — | — |  |
| 1-18 | `1.06#5` (9,7 s) | H | T1 | `t7_family_photo_frame_shadow`, `still` | *Conrad vừa xuất sắc tốt nghiệp trung học và vinh dự nhận được tấm bằng thuyền trưởng điều khiển tàu kéo để tiếp nối truyền thống của gia đình.* | — | — |  |
| 1-19 | `1.06#6` (10,4 s) | H | T1 | `t7_water_pump_equipment`, `push` | *Thế nhưng, phía sau nụ cười hiền lành ấy là một tâm hồn mong manh, thường xuyên phải vật lộn với những cơn trầm cảm nặng và nỗi âu lo xã hội triền miên.* | — | — |  |
| 1-20 | `1.06#7` (8,7 s) | H | T1 | `t7_tugboat_harbor_fog`, `pan` | *Cậu đã từng nhiều lần chủ động tìm kiếm sự giúp đỡ y tế và gặp gỡ các chuyên gia trị liệu để cố gắng vượt qua bóng tối tâm lý.* | — | — |  |
| 1-21 | `1.06#8` (6,8 s) | H | T1 | `t7_tugboat_captain_license`, `pull` | *Hãy lắng nghe nỗi đau xé lòng của mẹ cậu, bà Lynn Roy, trong buổi sáng định mệnh kinh hoàng hôm ấy.* | — | →N1 |  |
| 1-22 | `1.07#1` (7,8 s) | N1 | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *Cả buổi sáng hôm đó, linh cảm người mẹ mách bảo tôi rằng có một điều gì đó vô cùng bất an đang xảy ra với con trai mình.* | — | ✦ Cừu |  |
| 1-23 | `1.07#2` (7,6 s) | N1 | T1 | `t7_incoming_call_timer_40min`, `push` | *Tôi liên tục bấm số gọi cho Conrad, nhưng đáp lại chỉ là những hồi chuông dài vô vọng rơi vào khoảng không tĩnh lặng.* | — | — |  |
| 1-24 | `1.07#3` (7,7 s) | N1 | T1 | `t7_witness_trembling_phone`, `pan` | *Khoảnh khắc nhận cuộc gọi thông báo từ cảnh sát địa phương, toàn bộ thế giới xung quanh tôi hoàn toàn sụp đổ tan tành.* | — | — |  |
| 1-25 | `1.07#4` (8,4 s) | N1 | T1 | `t7_late_night_bedroom_phone`, `pull` | *Ban đầu, tôi chỉ nghĩ trong đau đớn cùng cực rằng con mình đã đầu hàng trước căn bệnh trầm cảm dai dẳng mà cậu bé phải gánh chịu.* | — | — |  |
| 1-26 | `1.07#5` (9,7 s) | N1 | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *Gia đình chúng tôi không thể nào ngờ được rằng, có một kẻ săn mồi giấu mặt đã liên tục giật dây tâm lý và đẩy con tôi vào chỗ chết từ một nơi rất xa.* | — | — |  |
| 1-27 | `1.07#6` (7,3 s) | N1 | T1 | `t7_incoming_call_timer_40min`, `push` | *Nỗi đau mất đi đứa con trai yêu quý sẽ mãi mãi là vết thương hằn sâu không bao giờ lành trong tâm can người mẹ.* | — | →H |  |
| 1-28 | `1.09#1` (7,5 s) | H | T1 | `t7_dossier_carter_case_07`, `pan` | *Bi kịch tưởng chừng đã khép lại như một sự việc đau lòng của thanh thiếu niên trong sổ lưu trữ của cảnh sát thị trấn.* | — | — |  |
| 1-29 | `1.09#2` (8,0 s) | H | T1 | `t7_forensic_evidence_phone`, `pull` | *Thế nhưng, quy trình điều tra chuẩn mực bắt buộc các sĩ quan phải thu giữ và giám định toàn bộ tư trang cá nhân của nạn nhân.* | — | — |  |
| 1-30 | `1.09#3` (7,5 s) | H | T1 | `t7_sms_transcript_forensic_binder`, `still` | *Chiếc điện thoại di động thông minh của Conrad Roy lập tức được chuyển giao cho bộ phận giám định pháp y kỹ thuật số.* | — | — |  |
| 1-31 | `1.09#4` (7,2 s) | H | T1 | `t7_digital_forensic_extraction`, `push` | *Họ cần tìm kiếm bất kỳ manh mối nào có thể giải thích cho quyết định đột ngột của một thanh niên vừa tốt nghiệp.* | — | →D |  |
| 1-32 | `1.10#1` (7,0 s) | D | T1 | `t7_digital_forensic_extraction`, `pan` | *Hồ sơ vụ án do Thám tử Scott Gordon thuộc Sở Cảnh sát Fairhaven trực tiếp thụ lý và tiến hành trích xuất dữ liệu.* | — | ✦ Sói |  |
| 1-33 | `1.10#2` (10,1 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *Khi các kỹ thuật viên pháp y số trích xuất toàn bộ dữ liệu bộ nhớ điện thoại, họ đã khai quật một kho lưu trữ khổng lồ gồm hơn hai mươi nghìn dòng tin nhắn văn bản.* | — | — |  |
| 1-34 | `1.10#3` (9,3 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *Người trao đổi dày đặc nhất với Conrad trong những tuần cuối đời chính là một nữ sinh mười bảy tuổi sống tại thị trấn Plainville tên là Michelle Carter.* | — | — |  |
| 1-35 | `1.10#4` (8,1 s) | D | T1 | `t7_sms_transcript_forensic_binder`, `push` | *Và những gì hiển hiện trên từng dòng tin nhắn đã khiến những sĩ quan điều tra dày dạn kinh nghiệm nhất cũng phải rùng mình kinh hãi.* | — | — |  |
| 1-36 | `1.10#5` (5,9 s) | D | T1 | `t7_digital_forensic_extraction`, `pan` | *Đó hoàn toàn không phải là những lời an ủi hay động viên vụng về của lứa tuổi học trò mới lớn.* | — | — |  |
| 1-37 | `1.10#6` (7,5 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *Đó là một chiến dịch thúc ép tinh vi, có hệ thống và đầy tính toán nhằm đảm bảo rằng nạn nhân không thể quay đầu rút lui.* | — | — |  |
| 1-38 | `1.10#7` (6,0 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *Từng câu chữ như những mũi gai tâm lý siết chặt lấy sự yếu đuối của một tâm hồn đang khủng hoảng.* | — | →H |  |
| 1-39 | `1.11#1` (6,3 s) | H | T1 | `t7_psychological_trap_metaphor`, `push` | *Một phát hiện làm đảo lộn toàn bộ nhận định ban đầu của cơ quan thực thi pháp luật hạt Bristol.* | — | — |  |
| 1-40 | `1.11#2` (8,3 s) | H | T1 | `t7_psychological_coercion_chess`, `pan` | *Chiếc điện thoại di động không chỉ là phương tiện liên lạc đơn thuần, mà đã trở thành hiện trường của một vụ án mạng vô hình.* | — | — |  |
| 1-41 | `1.11#3` (7,0 s) | H | T1 | `t7_puppet_strings_metaphor`, `pull` | *Nạn nhân bị dẫn dắt từng bước vào một chiếc bẫy tâm lý được giăng sẵn mà chính bản thân không hề hay biết.* | — | — |  |
| 1-42 | `1.11#4` (6,0 s) | H | T1 | `t7_digital_cage_smartphone_glow`, `still` | *Màn hình cảm ứng phát sáng trở thành chiếc lồng giam vô hình bóp nghẹt mọi nỗ lực cầu cứu.* | — | →C |  |
| 1-43 | `1.12#1` (8,5 s) | C | T1 | `t7_clinical_depression_shadow`, `push` | *Trong tâm lý học hành vi, một cá nhân đang trải qua cơn trầm cảm nặng thường rơi vào trạng thái suy giảm nghiêm trọng chức năng nhận thức và ý chí phản kháng.* | — | ✦ Cáo |  |
| 1-44 | `1.12#2` (7,4 s) | C | T1 | `t7_psychological_coercion_chess`, `pan` | *Họ mất đi khả năng tự bảo vệ tâm lý, tầm nhìn thu hẹp lại và trở nên cực kỳ phụ thuộc vào nguồn kích thích cảm xúc duy nhất từ bên ngoài.* | — | — |  |
| 1-45 | `1.12#3` (9,1 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *Khi một kẻ thao túng ác tính bước vào không gian khép kín đó, những lời phán xét sẽ nhanh chóng biến thành mệnh lệnh mang tính cưỡng chế tuyệt đối lên tâm trí nạn nhân.* | — | — |  |
| 1-46 | `1.12#4` (6,7 s) | C | T1 | `t7_night_sky_breath_of_life`, `still` | *Thuyết tâm trí bị bẻ gãy khiến người yếu thế không còn nhận thức được rằng người đối diện đang lợi dụng sự đau khổ của mình.* | — | — |  |
| 1-47 | `1.12#5` (6,6 s) | C | T1 | `t7_clinical_depression_shadow`, `push` | *Sự cô lập cảm xúc trong không gian số tạo nên một môi trường lý tưởng để kẻ thao túng thiết lập quyền kiểm soát tuyệt đối.* | — | — |  |
| 1-48 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN** | — | ⊘ | ◼ |

### HỒI 2 — MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN · nền chủ đạo `t7_late_night_bedroom_phone`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (9,0 s) | H | T1 | `t7_florida_beach_encounter_2012`, `pan` | *Để hiểu được bản chất của chiếc bẫy tâm lý ấy, chúng ta phải quay ngược thời gian về mùa hè năm 2012 tại bang Florida.* | — | — |  |
| 2-02 | `2.02#2` (10,1 s) | H | T1 | `t7_two_phone_screens_contrast`, `pull` | *Khi ấy, Conrad Roy mười sáu tuổi và Michelle Carter mười lăm tuổi tình cờ gặp nhau trong một kỳ nghỉ hè cùng gia đình thăm người thân.* | — | — |  |
| 2-03 | `2.02#3` (11,3 s) | H | T1 | `t7_social_media_notifications_flood`, `still` | *Giữa hai thiếu niên nhanh chóng nảy sinh sự đồng cảm bởi cả hai đều có những tổn thương tâm lý và nỗi cô đơn khó giãi bày cùng bạn bè đồng trang lứa.* | — | — |  |
| 2-04 | `2.02#4` (6,2 s) | H | T1 | `t7_massachusetts_route_map`, `push` | *Họ trao đổi số điện thoại và giữ liên lạc sau khi cùng trở về bang Massachusetts.* | — | — |  |
| 2-05 | `2.02#5` (6,4 s) | H | T1 | `t7_plainville_suburban_house`, `pan` | *Một tình bạn kỳ lạ bắt đầu hình thành và phát triển qua từng dòng tin nhắn văn bản.* | — | — |  |
| 2-06 | `2.02#6` (11,0 s) | H | T7 tuyến đường | `t7_massachusetts_route_map`, `pull` | *Thị trấn Plainville nơi Michelle sinh sống chỉ cách thị trấn Mattapoisett của Conrad khoảng ba mươi lăm dặm đường bộ, tức chưa đầy một giờ lái xe.* | — | — |  |
| 2-07 | `2.02#7` (10,1 s) | H | T1 | `t7_florida_beach_encounter_2012`, `still` | *Thế nhưng, một điều nghịch lý là trong suốt hơn hai năm duy trì mối quan hệ tình cảm, họ chỉ gặp mặt trực tiếp đúng vài lần ngắn ngủi.* | — | — |  |
| 2-08 | `2.02#8` (9,1 s) | H | T1 | `t7_two_phone_screens_contrast`, `push` | *Mối quan hệ của họ gần như tồn tại một trăm phần trăm trong không gian ảo của những chiếc màn hình điện thoại phát sáng.* | — | — |  |
| 2-09 | `2.02#9` (10,9 s) | H | T1 | `t7_social_media_notifications_flood`, `pan` | *Họ chia sẻ với nhau những bí mật sâu kín nhất, những bất an thầm lặng và cả những suy nghĩ tăm tối nhất mà không hề phải đối mặt ngoài đời thực.* | — | — |  |
| 2-10 | `2.02#10` (9,5 s) | H | T1 | `t7_massachusetts_route_map`, `pull` | *Không gian mạng đã tạo ra một ảo tưởng về sự thân mật tuyệt đối nhưng lại hoàn toàn thiếu vắng sự kiểm chứng hành vi thực tế.* | — | →C |  |
| 2-11 | `2.03#1` (10,0 s) | C | T1 | `t7_late_night_bedroom_phone`, `still` | *Trong giai đoạn đầu, các dòng tin nhắn cho thấy Michelle Carter từng đóng vai một người bạn chu đáo, khuyên Conrad nên tìm đến bác sĩ tâm thần và uống thuốc đều đặn.* | — | — |  |
| 2-12 | `2.03#2` (7,2 s) | C | T1 | `t7_copied_script_lines_notebook`, `push` | *Thế nhưng, bước ngoặt quái gở bắt đầu xuất hiện vào đầu tháng 7 năm 2014, khoảng mười ngày trước khi thảm kịch xảy ra.* | — | — |  |
| 2-13 | `2.03#3` (5,3 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pan` | *Thái độ của Michelle đột ngột quay ngoắt một trăm tám mươi độ một cách đầy bất thường.* | — | — |  |
| 2-14 | `2.03#4` (10,4 s) | C | T1 | `t7_staged_tragedy_mirror`, `pull` | *Thay vì tiếp tục động viên bạn trai kiên trì điều trị, cô ta bắt đầu chủ động gợi ý, khuyến khích và thúc giục Conrad biến những ý nghĩ tiêu cực thành hành động dứt khoát.* | — | — |  |
| 2-15 | `2.03#5` (6,0 s) | C | T1 | `t7_late_night_bedroom_phone`, `still` | *Đây chính là giai đoạn kích hoạt cơ chế Dung nạp ảo tưởng và Bẫy leo thang cam kết đầy nguy hiểm.* | — | — |  |
| 2-16 | `2.03#6` (6,5 s) | C | T1 | `t7_copied_script_lines_notebook`, `push` | *Kẻ thao túng bắt đầu thèm khát một cái kết kịch tính để hoàn tất bức tranh tưởng tượng trong tâm trí mình.* | — | →D |  |
| 2-17 | `2.05#1` (8,0 s) | D | T1 | `t7_sms_transcript_forensic_binder`, `pan` | *Hồ sơ kỹ thuật số lưu trữ những đoạn hội thoại khiến bất kỳ ai đọc lại cũng phải lạnh gáy trước sự tàn nhẫn của Michelle.* | — | — |  |
| 2-18 | `2.05#2` (7,9 s) | D | T1 | `t7_confession_message_turn`, `pull` | *Khi Conrad bày tỏ sự do dự và sợ hãi, Michelle liên tục dùng những từ ngữ cay nghiệt để công kích lòng tự trọng của cậu.* | — | — |  |
| 2-19 | `2.05#3` (7,4 s) | D | T4 trích dẫn | `t7_witness_trembling_phone`, `still` | *Cô ta nhắn tin:*“Anh cứ nói là anh muốn làm điều đó, nhưng anh chẳng bao giờ thực hiện, anh chỉ toàn trì hoãn.” | — | — |  |
| 2-20 | `2.05#4` (9,6 s) | D | T1 | `t7_psychological_coercion_chess`, `push` | *Khi Conrad lo lắng rằng cha mẹ và hai em gái sẽ đau đớn tột cùng nếu cậu ra đi, Michelle lạnh lùng gạt bỏ rào cản đạo đức cuối cùng của nạn nhân.* | — | — |  |
| 2-21 | `2.05#5` (9,0 s) | D | T4 trích dẫn | `t7_sms_transcript_forensic_binder`, `pan` | *Cô ta viết:*“Gia đình anh sẽ buồn một thời gian thôi, rồi họ sẽ vượt qua được, họ sẽ hiểu rằng anh không còn phải chịu đựng đau khổ nữa.” | — | — |  |
| 2-22 | `2.05#6` (9,8 s) | D | T1 | `t7_confession_message_turn`, `pull` | *Michelle thậm chí còn đi xa đến mức hướng dẫn tỉ mỉ cho Conrad cách chuẩn bị các công cụ máy móc và chọn một địa điểm kín đáo để không ai phát hiện.* | — | — |  |
| 2-23 | `2.05#7` (7,8 s) | D | T1 | `t7_witness_trembling_phone`, `still` | *Sự thúc ép diễn ra không ngừng nghỉ với tần suất hàng chục tin nhắn mỗi giờ, bủa vây mọi suy nghĩ của chàng trai trẻ.* | — | — |  |
| 2-24 | `2.05#8` (7,6 s) | D | T1 | `t7_psychological_coercion_chess`, `push` | *Cô ta tra hỏi cậu từng chi tiết nhỏ: đã mua máy bơm chưa, đã sạc điện thoại chưa, và khi nào thì bắt đầu thực hiện.* | — | →H |  |
| 2-25 | `2.06#1` (6,4 s) | H | T1 | `t7_puppet_strings_metaphor`, `pan` | *Dưới góc độ tâm lý học điều tra, đây là một kỹ thuật Thao túng tâm lý cưỡng chế cực kỳ nguy hiểm.* | — | — |  |
| 2-26 | `2.06#2` (8,2 s) | H | T1 | `t7_psychological_coercion_chess`, `pull` | *Kẻ săn mồi không sử dụng bạo lực thể xác, mà tấn công trực diện vào mặc cảm tội lỗi và sự yếu đuối sâu kín nhất của nạn nhân.* | — | — |  |
| 2-27 | `2.06#3` (9,0 s) | H | T1 | `t7_digital_cage_smartphone_glow`, `still` | *Bằng cách tước đoạt toàn bộ mạng lưới nâng đỡ tinh thần từ gia đình, Michelle đã đẩy Conrad vào một đường hầm nhận thức bế tắc hoàn toàn.* | — | — |  |
| 2-28 | `2.06#4` (9,3 s) | H | T1 | `t7_psychological_trap_metaphor`, `push` | *Cậu tin rằng cách duy nhất để chứng minh giá trị bản thân và không làm người bạn gái thất vọng là phải thực hiện đến cùng cam kết đau lòng ấy.* | — | — |  |
| 2-29 | `2.06#5` (7,3 s) | H | T1 | `t7_puppet_strings_metaphor`, `pan` | *Chiếc bẫy vô hình đã khép chặt miệng nắp khi nạn nhân bị cô lập hoàn toàn giữa thế giới thực và không gian số.* | — | — |  |
| 2-30 | `2.06#6` (7,8 s) | H | T1 | `t7_psychological_coercion_chess`, `pull` | *Mọi lối thoát tinh thần của chàng trai mười tám tuổi đều bị chặn đứng bởi những dòng tin nhắn ngọt ngào nhưng tàn nhẫn.* | — | — |  |
| 2-31 | `2.08#1` (4,3 s) | H | T1 | `t7_kmart_lot_midnight_darkness`, `still` | *Đêm ngày 12 tháng 7 năm 2014, chiếc bẫy tâm lý tàn độc ấy đã sập xuống hoàn toàn.* | — | — |  |
| 2-32 | `2.08#2` (7,1 s) | H | T1 | `t7_water_pump_equipment`, `push` | *Conrad Roy lái chiếc xe bán tải Ford F-250 đến bãi đỗ xe Kmart ở Fairhaven và bắt đầu khởi động cỗ máy bơm xả khói trong cabin đóng kín.* | — | — |  |
| 2-33 | `2.08#3` (7,1 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pan` | *Thế nhưng, khi luồng khí nguy hại bắt đầu lan tỏa và bản năng sinh tồn trỗi dậy mãnh liệt, chàng trai mười tám tuổi đã vô cùng hoảng sợ.* | — | — |  |
| 2-34 | `2.08#4` (5,3 s) | H | T1 | `t7_closed_car_window_fog`, `pull` | *Cậu mở cửa xe, bước ra ngoài hít thở không khí trong lành và tìm cách tự cứu lấy mạng sống của mình.* | — | — |  |
| 2-35 | `2.08#5` (5,5 s) | H | T1 | `t7_night_sky_breath_of_life`, `still` | *Chuỗi nhân quả của ý định dại dột khi ấy đã chính thức bị bẻ gãy bởi nỗ lực sinh tồn của chính nạn nhân.* | — | — |  |
| 2-36 | `2.08#6` (4,6 s) | H | T1 | `t7_kmart_lot_midnight_darkness`, `push` | *Lúc đó, Conrad vẫn đang kết nối điện thoại trực tiếp với Michelle Carter ở Plainville.* | — | — |  |
| 2-37 | `2.08#7` (5,9 s) | H | T1 | `t7_water_pump_equipment`, `pan` | *Và chính tại khoảnh khắc ranh giới mong manh giữa sự sống và cái chết ấy, một quyết định tàn nhẫn đã được đưa ra.* | — | — |  |
| 2-38 | `2.08#8` (4,9 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pull` | *Một lời nói thốt ra trong bóng tối đã tước đoạt toàn bộ cơ hội được sống của chàng trai trẻ.* | — | →D |  |
| 2-39 | `2.09#1` (6,6 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *Đây chính là tình tiết mang tính bước ngoặt định đoạt toàn bộ bản chất pháp lý của vụ án.* | — | — |  |
| 2-40 | `2.09#2` (11,4 s) | D | T1 | `t7_confession_message_turn`, `push` | *Qua cuộc điện thoại kéo dài nhiều phút, khi nghe Conrad khóc lóc nói rằng mình sợ hãi và đã bước ra khỏi xe, Michelle Carter không hề khuyên bạn dừng lại.* | — | — |  |
| 2-41 | `2.09#3` (9,0 s) | D | T1 | `t7_ticking_clock_deadlines`, `pan` | *Cô ta không hề gọi điện báo cảnh sát, không hề liên lạc với mẹ của Conrad dù biết rõ địa chỉ nhà và số điện thoại của bà.* | — | — |  |
| 2-42 | `2.09#4` (9,5 s) | D | T4 trích dẫn | `t7_incoming_call_timer_40min`, `pull` | *Thay vào đó, Michelle đã lạnh lùng phát ra một mệnh lệnh bằng lời nói đanh thép qua ống nghe:*“Hãy quay trở lại xe ngay lập tức.” | — | — |  |
| 2-43 | `2.09#5` (10,9 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *Chính mệnh lệnh trực tiếp ấy đã dập tắt tia hy vọng sống sót cuối cùng của nạn nhân, ép cậu phải bước ngược trở lại vào cabin đầy khói xả nguy hiểm.* | — | — |  |
| 2-44 | `2.09#6` (6,6 s) | D | T1 | `t7_confession_message_turn`, `push` | *Một hành vi vô nhân đạo thể hiện sự coi thường tột cùng đối với sinh mạng của đồng loại.* | — | — |  |
| 2-45 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH** | — | ⊘ | ◼ |

### HỒI 3 — VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH · nền chủ đạo `t7_empty_theater_spotlight`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (5,8 s) | H | T1 | `t7_empty_theater_spotlight`, `pan` | *Một câu hỏi lớn khiến toàn bộ dư luận xã hội và các chuyên gia pháp đình bàng hoàng:* | — | — |  |
| 3-02 | `3.02#2` (10,2 s) | H | T1 | `t7_cracked_porcelain_mask`, `pull` | *Động cơ thực sự nào có thể thôi thúc một nữ sinh trung học mười bảy tuổi, sống trong một gia đình khá giả và êm ấm, lại hành động tàn nhẫn đến như vậy?* | — | — |  |
| 3-03 | `3.02#3` (8,7 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *Cô ta không hề có thù oán cá nhân, không có tranh chấp tiền bạc, và cũng chẳng thể trục lợi bảo hiểm từ cái chết của Conrad Roy.* | — | — |  |
| 3-04 | `3.02#4` (7,1 s) | H | T1 | `t7_staged_tragedy_mirror`, `push` | *Để tìm lời giải đáp, chúng ta buộc phải giải phẫu sâu vào cấu trúc nhân cách bệnh lý của Michelle Carter.* | — | — |  |
| 3-05 | `3.02#5` (7,5 s) | H | T1 | `t7_empty_theater_spotlight`, `pan` | *Một tâm lý méo mó được nuôi dưỡng bởi cơn khát khao sự chú ý tột cùng và nỗi ám ảnh đóng vai nạn nhân bi kịch.* | — | — |  |
| 3-06 | `3.02#6` (5,8 s) | H | T1 | `t7_cracked_porcelain_mask`, `pull` | *Ẩn sâu sau gương mặt nữ sinh trong sáng là một khoảng trống rỗng hiện sinh không đáy.* | — | — |  |
| 3-07 | `3.02#7` (8,6 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *Một tâm hồn lạc lối sẵn sàng đánh đổi cả sinh mạng của bạn trai để mua lấy vài khoảnh khắc trở thành tâm điểm của sự ngưỡng mộ.* | — | →C |  |
| 3-08 | `3.03#1` (7,7 s) | C | T1 | `t7_highschool_empty_lockers`, `push` | *Dưới góc độ tâm thần học pháp y, hành vi của Michelle Carter bộc lộ những đặc điểm kinh điển của Rối loạn nhân cách kịch tính kết hợp nét ái kỷ bệnh lý.* | — | — |  |
| 3-09 | `3.03#2` (7,3 s) | C | T1 | `t7_cracked_porcelain_mask`, `pan` | *Tại trường Trung học King Philip Regional, Michelle là một nữ sinh mờ nhạt, vụng về trong giao tiếp xã hội và hầu như không có bạn bè thân thiết.* | — | — |  |
| 3-10 | `3.03#3` (7,0 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *Cô ta luôn cảm thấy mình vô hình, bị cô lập và khao khát đến tuyệt vọng việc trở thành tâm điểm của sự chú ý và thương cảm từ người khác.* | — | — |  |
| 3-11 | `3.03#4` (8,1 s) | C | T1 | `t7_vintage_tv_glee_glow`, `still` | *Để bù đắp cho sự trống rỗng bên trong, bộ não ái kỷ của cô ta đã tự sáng tác nên một kịch bản phim truyền hình lãng mạn đầy nước mắt do chính mình thủ vai chính.* | — | — |  |
| 3-12 | `3.03#5` (6,3 s) | C | T1 | `t7_highschool_empty_lockers`, `push` | *Và chàng trai Conrad Roy đáng thương đã vô tình bị cô ta lựa chọn để trở thành “đạo cụ sống” hoàn hảo cho màn kịch đời mình.* | — | — |  |
| 3-13 | `3.03#6` (5,7 s) | C | T1 | `t7_cracked_porcelain_mask`, `pan` | *Sự vật hóa người khác biến bạn trai thành một công cụ cung cấp nguồn thỏa mãn cảm xúc ái kỷ không hơn không kém.* | — | — |  |
| 3-14 | `3.03#7` (4,8 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *Khi đối tượng không còn phục vụ cho ảo tưởng đó, kẻ thao túng sẵn sàng đẩy họ vào sự hủy diệt.* | — | →H |  |
| 3-15 | `3.04#1` (9,8 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *Tại phiên tòa xét xử, bên công tố đã chứng minh Michelle Carter có một nỗi ám ảnh kỳ lạ đối với loạt phim truyền hình âm nhạc nổi tiếng Glee.* | — | — |  |
| 3-16 | `3.04#2` (5,6 s) | H | T1 | `t7_suburban_living_room_tv`, `push` | *Đặc biệt, cô ta thần tượng cuồng nhiệt nữ diễn viên Lea Michele ngoài đời thực.* | — | — |  |
| 3-17 | `3.04#3` (9,2 s) | H | T1 | `t7_drama_masks_digital_glitch`, `pan` | *Vào năm 2013, nam diễn viên Cory Monteith, bạn diễn và cũng là người yêu của Lea Michele, đã đột ngột qua đời vì dùng thuốc quá liều.* | — | — |  |
| 3-18 | `3.04#4` (13,6 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Hình ảnh Lea Michele xuất hiện trước công chúng trong trang phục đen kiêu sa, nhận được muôn vàn sự thương xót, ngưỡng mộ và vỗ về từ hàng triệu người hâm mộ đã găm sâu vào tâm trí Michelle Carter.* | — | — |  |
| 3-19 | `3.04#5` (7,5 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *Cô ta khao khát có được vị thế của một “người bạn gái góa phụ bi thương” được cả cộng đồng vây quanh an ủi.* | — | — |  |
| 3-20 | `3.04#6` (6,5 s) | H | T1 | `t7_suburban_living_room_tv`, `push` | *Một ảo tưởng bệnh hoạn bắt đầu nảy nở và biến thành nỗi ám ảnh cưỡng chế không thể kiểm soát.* | — | — |  |
| 3-21 | `3.04#7` (9,5 s) | H | T1 | `t7_drama_masks_digital_glitch`, `pan` | *Cô ta thậm chí còn sao chép từng câu thoại trong phim vào những dòng tin nhắn gửi cho bạn bè để làm dày thêm kịch bản bi thương của mình.* | — | →D |  |
| 3-22 | `3.06#1` (8,2 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *Dữ liệu tin nhắn do Thám tử Gordon phục hồi đã phơi bày một sự thật ớn lạnh về hành vi chuẩn bị tâm lý của Michelle.* | — | — |  |
| 3-23 | `3.06#2` (10,3 s) | D | T1 | `t7_social_media_notifications_flood`, `still` | *Vào ngày 10 và 11 tháng 7 năm 2014, tức là hai ngày trước khi Conrad qua đời, Michelle đã bắt đầu gửi hàng loạt tin nhắn cho các bạn cùng trường.* | — | — |  |
| 3-24 | `3.06#3` (10,9 s) | D | T1 | `t7_confession_message_turn`, `push` | *Cô ta khóc lóc bịa đặt rằng Conrad đã biến mất, rằng cậu ấy có thể đã tự tước đoạt mạng sống và cô ta đang vô cùng suy sụp vì không thể cứu được bạn trai.* | — | — |  |
| 3-25 | `3.06#4` (9,4 s) | D | T1 | `t7_ticking_clock_deadlines`, `pan` | *Trong khi thực tế vào thời điểm đó, Conrad Roy vẫn đang sống hoàn toàn bình thường cùng gia đình và chưa hề có hành động tự hại nào.* | — | — |  |
| 3-26 | `3.06#5` (11,2 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *Michelle đã viết sẵn kịch bản bi kịch, phân vai cho tất cả mọi người, và điều duy nhất còn thiếu để hoàn tất vở kịch chính là sự ra đi thực sự của chàng trai.* | — | — |  |
| 3-27 | `3.06#6` (7,8 s) | D | T1 | `t7_social_media_notifications_flood`, `still` | *Cô ta đã lỡ thông báo cho bạn bè, và một khi vở kịch đã được công bố, cô ta không cho phép kịch bản bị đổ bể.* | — | — |  |
| 3-28 | `3.06#7` (8,1 s) | D | T1 | `t7_confession_message_turn`, `push` | *Sự chuẩn bị tinh vi này chứng minh đây là một chuỗi hành vi có toan tính lạnh lùng từ trước chứ không hề bộc phát.* | — | →H |  |
| 3-29 | `3.07#1` (4,3 s) | H | T1 | `t7_cracked_porcelain_mask`, `pan` | *Đây chính là Ngòi nổ và Điểm gãy tâm lý mang tính quyết định của toàn bộ vụ án.* | — | — |  |
| 3-30 | `3.07#2` (7,9 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Khi đã trót loan tin với bạn bè rằng Conrad mất tích và gặp chuyện chẳng lành, Michelle rơi vào một nỗi sợ hãi bệnh lý: sợ bị lật tẩy là kẻ dối trá.* | — | — |  |
| 3-31 | `3.07#3` (8,2 s) | H | T1 | `t7_puppet_strings_metaphor`, `still` | *Nếu Conrad đổi ý và tiếp tục sống, chiếc mặt nạ bi kịch mà cô ta dày công dựng lên sẽ lập tức tan thành mây khói, biến cô ta thành trò cười trước bạn bè.* | — | — |  |
| 3-32 | `3.07#4` (3,5 s) | H | T1 | `t7_night_sky_breath_of_life`, `push` | *Cái tôi ái kỷ không cho phép điều đó xảy ra dưới bất kỳ giá nào.* | — | — |  |
| 3-33 | `3.07#5` (7,1 s) | H | T1 | `t7_cracked_porcelain_mask`, `pan` | *Chính vì vậy, vào đêm 12 tháng 7, sự thúc ép của Michelle đã chuyển từ khuyến khích thông thường sang một cơn cuồng loạn cưỡng bách.* | — | — |  |
| 3-34 | `3.07#6` (5,8 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Sự ra đi của Conrad trở thành điều kiện sống còn để bảo vệ sự toàn vẹn cho lời nói dối bệnh hoạn của cô ta.* | — | — |  |
| 3-35 | `3.07#7` (5,4 s) | H | T1 | `t7_puppet_strings_metaphor`, `still` | *Một sinh mạng con người bị đem ra làm vật thế chấp chỉ để cứu vãn thể diện mong manh của kẻ nói dối.* | — | →C |  |
| 3-36 | `3.08#1` (7,7 s) | C | T1 | `t7_suburban_living_room_tv`, `push` | *Ở đây, chúng ta chứng kiến sự vận hành tinh vi của Cơ chế Chia ngăn nhận thức và Kỹ thuật Trung hòa đạo đức.* | — | — |  |
| 3-37 | `3.08#2` (12,0 s) | C | T1 | `t7_clinical_depression_shadow`, `pan` | *Trước mặt cha mẹ và thầy cô tại thị trấn Plainville, Michelle vẫn giữ trọn vẹn vỏ bọc một cô con gái ngoan ngoãn, học hành chăm chỉ và tham gia các hoạt động thiện nguyện.* | — | — |  |
| 3-38 | `3.08#3` (10,5 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *Nhưng trong ngăn kéo kỹ thuật số bí mật, cô ta lạnh lùng giáng cấp một sinh mạng con người xuống thành một con tốt thí trên bàn cờ cảm xúc của mình.* | — | — |  |
| 3-39 | `3.08#4` (10,3 s) | C | T1 | `t7_psychological_coercion_chess`, `still` | *Michelle tự ru ngủ lương tâm bằng ngụy biện rằng mình đang “giúp đỡ” Conrad giải thoát khỏi nỗi đau đớn trần gian để lên một thế giới tốt đẹp hơn.* | — | — |  |
| 3-40 | `3.08#5` (10,4 s) | C | T1 | `t7_suburban_living_room_tv`, `push` | *Sự thiếu hụt hoàn toàn năng lực thấu cảm đã biến cô ta thành một kẻ săn mồi lạnh lùng vô cảm mà bề ngoài vẫn khoác chiếc áo thiên thần thánh thiện.* | — | — |  |
| 3-41 | `3.08#6` (7,6 s) | C | T1 | `t7_clinical_depression_shadow`, `pan` | *Kỹ thuật ngắt kết nối đạo đức cho phép cô ta ngủ ngon mỗi đêm sau khi đã gửi đi những thông điệp đoạt mạng.* | — | — |  |
| 3-42 | `3.08#7` (6,7 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *Bộ não tội phạm tự bào chữa rằng mọi lỗi lầm thuộc về số phận và mong muốn của chính nạn nhân.* | — | →H |  |
| 3-43 | `3.09#1` (7,9 s) | H | T1 | `t7_baseball_field_charity_empty`, `still` | *Ngay sau khi Conrad qua đời, Michelle Carter lập tức bước lên vũ đài trung tâm mà cô ta hằng ao ước suốt bao năm tháng.* | — | — |  |
| 3-44 | `3.09#2` (9,5 s) | H | T1 | `t7_social_media_notifications_flood`, `push` | *Cô ta đăng tải hàng loạt bài viết bi thương trên mạng xã hội, chia sẻ những kỷ niệm xúc động và nhận về hàng trăm lượt chia sẻ, an ủi từ bạn bè.* | — | — |  |
| 3-45 | `3.09#3` (9,5 s) | H | T1 | `t7_confession_message_turn`, `pan` | *Chưa dừng lại ở đó, Michelle còn đứng ra tổ chức một giải đấu bóng mềm từ thiện mang tên Homers for Conrad để gây quỹ ủng hộ sức khỏe tinh thần.* | — | — |  |
| 3-46 | `3.09#4` (8,7 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Cô ta xuất hiện rạng rỡ, phát biểu trước đám đông và nhận hoa như một biểu tượng của lòng vị tha và sự kiên cường vượt qua mất mát.* | — | — |  |
| 3-47 | `3.09#5` (12,5 s) | H | T1 | `t7_baseball_field_charity_empty`, `still` | *Chữ ký tâm lý của kẻ thủ ác đã hiện rõ mồn một: Cô ta tận hưởng từng giây phút được đắm chìm trong sự chú ý của công chúng, xây dựng danh tiếng trên nỗi đau của người bạn trai vừa nằm xuống.* | — | — |  |
| 3-48 | `3.09#6` (5,7 s) | H | T1 | `t7_social_media_notifications_flood`, `push` | *Một sự thỏa mãn ái kỷ tột cùng được ngụy trang hoàn hảo dưới vỏ bọc của lòng nhân ái.* | — | — |  |
| 3-49 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **DÒNG TIN NHẮN ĐẦY TỘI LỖI & BẢN ÁN LỊCH SỬ** | — | ⊘ | ◼ |

### HỒI 4 — DÒNG TIN NHẮN ĐẦY TỘI LỖI VÀ BẢN ÁN LỊCH SỬ · nền chủ đạo `t7_taunton_courthouse_exterior`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (8,9 s) | H | T1 | `t7_confession_message_turn`, `pan` | *Thế nhưng, chiếc mặt nạ hoàn hảo của người bạn gái thánh thiện không thể tồn tại mãi mãi trước ánh sáng của sự thật.* | — | — |  |
| 4-02 | `4.02#2` (11,0 s) | H | T1 | `t7_confession_text_timestamp`, `pull` | *Trong tâm lý học tội phạm, những kẻ ái kỷ kịch tính luôn có một điểm yếu chí mạng: nhu cầu khoe khoang và khẳng định vai trò quyền lực của mình.* | — | — |  |
| 4-03 | `4.02#3` (9,0 s) | H | T1 | `t7_psychological_trap_metaphor`, `still` | *Michelle Carter không thể kìm nén được thôi thúc muốn kể cho ai đó nghe về “chiến tích” giật dây vô hình của bản thân.* | — | — |  |
| 4-04 | `4.02#4` (9,7 s) | H | T1 | `t7_cracked_porcelain_mask`, `push` | *Chính sự tự mãn mù quáng ấy đã dẫn đến sự xuất hiện của một mẩu bằng chứng bằng vàng, chôn vùi toàn bộ tương lai của kẻ thủ ác.* | — | — |  |
| 4-05 | `4.02#5` (7,4 s) | H | T1 | `t7_confession_message_turn`, `pan` | *Hai tháng sau ngày Conrad vĩnh viễn ra đi, một dòng tin nhắn định mệnh đã được gửi đi trong đêm.* | — | — |  |
| 4-06 | `4.02#6` (7,1 s) | H | T1 | `t7_confession_text_timestamp`, `pull` | *Một lời tự thú bất cẩn bóc trần toàn bộ tội ác được che giấu sau những giọt nước mắt cá sấu.* | — | →N2 |  |
| 4-07 | `4.03#1` (8,8 s) | N2 | T1 | `t7_confession_text_timestamp`, `still` | *Vào tối ngày 15 tháng 9 năm 2014, tôi bất ngờ nhận được một dòng tin nhắn dài từ Michelle Carter gửi qua điện thoại.* | — | ✦ Mèo |  |
| 4-08 | `4.03#2` (8,8 s) | N2 | T1 | `t7_witness_trembling_phone`, `push` | *Khi mở màn hình ra đọc, toàn thân tôi run lên bần bật vì không thể tin nổi vào những con chữ đang hiện ra trước mắt.* | — | — |  |
| 4-09 | `4.03#3` (7,1 s) | N2 | T4 trích dẫn | `t7_incoming_call_timer_40min`, `pan` | *Michelle viết:*“Cái chết của anh ấy là lỗi của tớ, thực sự là tớ đã có thể ngăn anh ấy lại.” | — | — |  |
| 4-10 | `4.03#4` (10,3 s) | N2 | T4 trích dẫn | `t7_two_phone_screens_contrast`, `pull` | *Cô ấy viết tiếp:*“Tớ đã nói chuyện điện thoại với anh ấy, anh ấy bước ra khỏi xe vì sợ hãi, nhưng tớ đã bảo anh ấy hãy quay trở lại xe.” | — | — |  |
| 4-11 | `4.03#5` (9,3 s) | N2 | T1 | `t7_confession_text_timestamp`, `still` | *Tôi chết lặng trong nỗi kinh hoàng tột độ khi nhận ra cô bạn gái mà cả trường đang thương xót bấy lâu nay thực chất là ai.* | — | — |  |
| 4-12 | `4.03#6` (5,3 s) | N2 | T1 | `t7_witness_trembling_phone`, `push` | *Dòng tin nhắn ấy đã ám ảnh tâm trí tôi suốt nhiều tháng ngày sau đó.* | — | →D |  |
| 4-13 | `4.05#1` (10,8 s) | D | T1 | `t7_bristol_county_indictment_stamp`, `pan` | *Dòng tin nhắn tự thú gửi cho Samantha Boardman lập tức trở thành chứng cứ đanh thép nhất trong hồ sơ khởi tố của Cơ quan Công tố hạt Bristol.* | — | — |  |
| 4-14 | `4.05#2` (11,0 s) | D | T1 | `t7_taunton_courthouse_exterior`, `pull` | *Đầu năm 2015, Michelle Carter chính thức bị đại bồi thẩm đoàn truy tố về tội Ngộ sát không tự ý trước sự ngỡ ngàng của toàn thể dư luận nước Mỹ.* | — | — |  |
| 4-15 | `4.05#3` (9,7 s) | D | T1 | `t7_empty_courtroom_bench_trial`, `still` | *Vụ án được đưa ra xét xử vào tháng 6 năm 2017 tại Tòa án Vị thành niên hạt Bristol thuộc thị trấn Taunton, bang Massachusetts.* | — | — |  |
| 4-16 | `4.05#4` (7,9 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *Đáng chú ý, bị cáo đã chủ động từ bỏ quyền được xét xử bởi bồi thẩm đoàn gồm các công dân bình thường.* | — | — |  |
| 4-17 | `4.05#5` (9,0 s) | D | T1 | `t7_bristol_county_indictment_stamp`, `pan` | *Michelle và đội ngũ pháp lý lựa chọn hình thức xét xử trực tiếp bởi một thẩm phán duy nhất: Thẩm phán Lawrence Moniz.* | — | — |  |
| 4-18 | `4.05#6` (7,4 s) | D | T1 | `t7_taunton_courthouse_exterior`, `pull` | *Một canh bạc pháp lý đầy rủi ro nhằm né tránh làn sóng phẫn nộ dữ dội của công chúng địa phương.* | — | — |  |
| 4-19 | `4.05#7` (8,2 s) | D | T1 | `t7_empty_courtroom_bench_trial`, `still` | *Họ hy vọng một thẩm phán chuyên nghiệp sẽ phán quyết thuần túy theo câu chữ của điều luật thay vì cảm xúc.* | — | — |  |
| 4-20 | `4.05#8` (6,7 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *Thế nhưng, chính sự thật trần trụi của các chứng cứ số đã định đoạt số phận của cô ta.* | — | →H |  |
| 4-21 | `4.06#1` (7,1 s) | H | T1 | `t7_courtroom_projection_screen`, `pan` | *Phiên tòa trở thành tâm điểm chú ý của toàn cầu với cuộc đối đầu gay gắt giữa hai luồng quan điểm pháp lý và tâm lý học.* | — | — |  |
| 4-22 | `4.06#2` (7,7 s) | H | T1 | `t7_us_constitution_amendment1`, `pull` | *Luật sư bào chữa Joseph Cataldo lập luận rằng Michelle không hề có mặt tại bãi đỗ xe và không sử dụng bất kỳ hung khí bạo lực nào.* | — | — |  |
| 4-23 | `4.06#3` (7,4 s) | H | T1 | `t7_sms_transcript_forensic_binder`, `still` | *Phía bào chữa khẳng định những dòng tin nhắn chỉ là ngôn từ tự do được bảo vệ bởi Tu chính án thứ nhất của Hiến pháp Hoa Kỳ.* | — | — |  |
| 4-24 | `4.06#4` (7,6 s) | H | T1 | `t7_taunton_courthouse_exterior`, `push` | *Ngược lại, Phó Công tố viên Katie Rayburn đã trình chiếu hàng nghìn trang tin nhắn chứng minh một chiến dịch tàn độc có chủ đích.* | — | — |  |
| 4-25 | `4.06#5` (7,0 s) | H | T1 | `t7_courtroom_projection_screen`, `pan` | *Công tố viên nhấn mạnh rằng Michelle đã dùng lời nói như một mũi tên độc bắn thẳng vào tâm trí suy kiệt của nạn nhân.* | — | — |  |
| 4-26 | `4.06#6` (4,7 s) | H | T1 | `t7_us_constitution_amendment1`, `pull` | *Từng luận điểm sắc bén đã bóc trần sự tàn nhẫn không thể biện minh của bị cáo.* | — | →C |  |
| 4-27 | `4.07#1` (6,0 s) | C | T1 | `t7_prescription_pill_bottle_celexa`, `still` | *Để bào chữa cho thân chủ, phía luật sư bị cáo đã thuê một chuyên gia tâm thần học là Tiến sĩ Peter Breggin.* | — | — |  |
| 4-28 | `4.07#2` (8,3 s) | C | T1 | `t7_clinical_depression_shadow`, `push` | *Họ lập luận rằng Michelle rơi vào trạng thái “say thuốc không tự nguyện” do tác dụng phụ của thuốc chống trầm cảm Celexa, làm mất khả năng đồng cảm.* | — | — |  |
| 4-29 | `4.07#3` (6,2 s) | C | T1 | `t7_courtroom_projection_screen`, `pan` | *Tuy nhiên, lập luận ngụy biện này đã bị cơ quan công tố và các chuyên gia tâm lý học hành vi bẻ gãy hoàn toàn.* | — | — |  |
| 4-30 | `4.07#4` (7,8 s) | C | T1 | `t7_psychological_coercion_chess`, `pull` | *Hành vi của Michelle mang tính toán tuần tự, che giấu dấu vết, dặn bạn bè xóa tin nhắn và tổ chức sự kiện gây quỹ một cách cực kỳ tỉnh táo.* | — | — |  |
| 4-31 | `4.07#5` (8,4 s) | C | T1 | `t7_prescription_pill_bottle_celexa`, `still` | *Đó không phải là sự mất kiểm soát hành vi do dược chất, mà là sự toan tính lạnh lùng của một nhân cách ái kỷ đang vận hành kỹ thuật trung hòa đạo đức.* | — | →D |  |
| 4-32 | `4.08#1` (8,9 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *Ngày 16 tháng 6 năm 2017, toàn bộ phòng xử án nín thở khi Thẩm phán Lawrence Moniz bắt đầu công bố bản phán quyết.* | — | — |  |
| 4-33 | `4.08#2` (9,8 s) | D | T1 | `t7_courtroom_breathless_silence`, `pan` | *Thẩm phán phân tích sâu sắc rằng: Khi Conrad bước ra khỏi xe, cậu đã tự phá vỡ chuỗi nhân quả tự hại và giành lại cơ hội sống.* | — | — |  |
| 4-34 | `4.08#3` (11,4 s) | D | T1 | `t7_courtroom_projection_screen`, `pull` | *Thế nhưng, hành động ra lệnh “hãy quay trở lại xe” của Michelle cùng sự im lặng hoàn toàn không cứu giúp cấu thành hành vi liều lĩnh và cố ý vô cớ.* | — | — |  |
| 4-35 | `4.08#4` (11,5 s) | D | T1 | `t7_ticking_clock_deadlines`, `still` | *Thẩm phán nhận định bị cáo đã tạo ra một tình thế hiểm nghèo đối với nạn nhân và hoàn toàn thất bại trong việc thực hiện nghĩa vụ cứu giúp tối thiểu.* | — | — |  |
| 4-36 | `4.08#5` (7,7 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *Không một cuộc gọi nào được thực hiện đến số 911 dù bị cáo biết chính xác vị trí chiếc xe đang đỗ.* | — | — |  |
| 4-37 | `4.08#6` (6,2 s) | D | T1 | `t7_courtroom_breathless_silence`, `pan` | *Thẩm phán Moniz dõng dạc tuyên bố: Michelle Carter phạm tội Ngộ sát không tự ý.* | — | — |  |
| 4-38 | `4.08#7` (9,0 s) | D | T1 | `t7_courtroom_projection_screen`, `pull` | *Một phán quyết mang tính lịch sử, phá vỡ định kiến cho rằng lời nói truyền từ xa không thể cấu thành tội giết người.* | — | →H |  |
| 4-39 | `4.09#1` (8,5 s) | H | T1 | `t7_court_verdict_document_guilty`, `still` | *Vào tháng 8 năm 2017, Michelle Carter bị tuyên phạt hai năm rưỡi tù giam, với mười lăm tháng phải chấp hành thực tế sau song sắt.* | — | — |  |
| 4-40 | `4.09#2` (8,7 s) | H | T1 | `t7_bristol_county_jail_bars`, `push` | *Tại khoảnh khắc nghe bản án, thiếu nữ từng kiêu hãnh và lạnh lùng đã hoàn toàn gục ngã, run rẩy bật khóc nức nở ngay tại bàn bị cáo.* | — | — |  |
| 4-41 | `4.09#3` (8,4 s) | H | T1 | `t7_courtroom_breathless_silence`, `pan` | *Nhưng các chuyên gia tâm lý nhận định: Những giọt nước mắt ấy hoàn toàn không phải là sự ăn năn chân chính dành cho Conrad Roy.* | — | — |  |
| 4-42 | `4.09#4` (9,7 s) | H | T1 | `t7_cracked_porcelain_mask`, `pull` | *Đó là biểu hiện kinh điển của Sự sụp đổ cái tôi ái kỷ khi toàn bộ hào quang ảo tưởng, danh dự và tự do của bản thân bị tước đoạt trước mắt thiên hạ.* | — | — |  |
| 4-43 | `4.09#5` (6,7 s) | H | T1 | `t7_court_verdict_document_guilty`, `still` | *Kẻ thao túng đã phải đối diện với chiếc gương công lý tàn nhẫn nhất bóc trần bản chất thật của mình.* | — | — |  |
| 4-44 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD** | — | ⊘ | ◼ |

### HỒI 5 — ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD · nền chủ đạo `t7_digital_lighthouse_beacon`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (6,9 s) | H | T1 | `t7_massachusetts_state_house_dome`, `push` | *Bản án dành cho Michelle Carter không chỉ khép lại một vụ án hình sự chấn động tại bang Massachusetts.* | — | — |  |
| 5-02 | `5.02#2` (7,9 s) | H | T1 | `t7_conrads_law_legislative_bill`, `pan` | *Nó mở ra một cuộc cách mạng sâu sắc trong nhận thức pháp lý và đạo đức của nhân loại trong kỷ nguyên số hóa toàn cầu.* | — | — |  |
| 5-03 | `5.02#3` (10,4 s) | H | T1 | `t7_digital_lighthouse_beacon`, `pull` | *Lần đầu tiên trong lịch sử tư pháp hiện đại, tòa án công nhận rằng: Khoảng cách địa lý và màn hình điện thoại không bao giờ là tấm khiên che chở cho tội ác.* | — | — |  |
| 5-04 | `5.02#4` (9,9 s) | H | T1 | `t7_massachusetts_route_map`, `still` | *Ngôn từ không chỉ mang tính biểu đạt cảm xúc, mà khi được sử dụng với ác ý thao túng cưỡng bách, nó hoàn toàn có thể trở thành một vũ khí đoạt mạng.* | — | — |  |
| 5-05 | `5.02#5` (8,7 s) | H | T1 | `t7_night_sky_breath_of_life`, `push` | *Phán quyết đã tạo nên một tiền lệ tư pháp vững chắc để bảo vệ những tâm hồn yếu thế trước bạo lực tinh thần trên không gian mạng.* | — | — |  |
| 5-06 | `5.02#6` (8,1 s) | H | T1 | `t7_massachusetts_state_house_dome`, `pan` | *Một ranh giới đạo đức rõ ràng đã được thiết lập giữa quyền tự do ngôn luận và hành vi bức hại đồng loại qua thế giới ảo.* | — | — |  |
| 5-07 | `5.02#7` (7,2 s) | H | T1 | `t7_conrads_law_legislative_bill`, `pull` | *Một bài học pháp lý đắt giá dành cho tất cả những ai đang sử dụng các nền tảng công nghệ kết nối hàng ngày.* | — | — |  |
| 5-08 | `5.02#8` (10,3 s) | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Từ nỗi đau tột cùng của sự mất mát, bà Lynn Roy, mẹ của Conrad, cùng các nhà lập pháp bang Massachusetts đã không ngừng nghỉ đấu tranh suốt nhiều năm qua.* | — | — |  |
| 5-09 | `5.02#9` (5,8 s) | H | T1 | `t7_massachusetts_route_map`, `push` | *Họ kiên trì vận động cho một dự luật mang tính bước ngoặt mang tên “Đạo luật Conrad”.* | — | — |  |
| 5-10 | `5.02#10` (11,2 s) | H | T1 | `t7_night_sky_breath_of_life`, `pan` | *Mục tiêu cốt lõi của đạo luật là chính thức hình sự hóa hành vi ép buộc, thao túng hoặc xúi giục người khác tự tước đoạt sinh mạng, với mức án lên tới năm năm tù giam.* | — | — |  |
| 5-11 | `5.02#11` (7,6 s) | H | T1 | `t7_massachusetts_state_house_dome`, `pull` | *Đạo luật nhằm bịt kín lỗ hổng pháp lý nguy hiểm mà các vụ bạo lực tinh thần kỹ thuật số tinh vi có thể lẩn tránh.* | — | — |  |
| 5-12 | `5.02#12` (9,0 s) | H | T1 | `t7_conrads_law_legislative_bill`, `still` | *Biến nỗi đau khôn nguôi thành hành động cụ thể để bảo vệ những đứa trẻ khác không bao giờ phải rơi vào hoàn cảnh bi thương của Conrad.* | — | →C |  |
| 5-13 | `5.03#1` (6,2 s) | C | T1 | `t7_digital_cage_smartphone_glow`, `push` | *Vụ án để lại một di chứng tâm lý xã hội sâu sắc đối với các bậc phụ huynh trong thời đại bùng nổ của điện thoại thông minh.* | — | — |  |
| 5-14 | `5.03#2` (10,0 s) | C | T1 | `t7_suburban_living_room_tv`, `pan` | *Nhiều cha mẹ bàng hoàng nhận ra rằng: Ngay cả khi con cái họ đang ngồi an toàn trong phòng ngủ gia đình, chúng vẫn có thể đang bị thao túng bởi những kẻ săn mồi giấu mặt từ khoảng cách hàng nghìn dặm.* | — | — |  |
| 5-15 | `5.03#3` (5,8 s) | C | T1 | `t7_family_photo_frame_shadow`, `pull` | *Màn hình điện thoại có thể trở thành một cánh cổng nguy hiểm nếu thiếu đi sự quan tâm và kết nối cảm xúc thực tế.* | — | — |  |
| 5-16 | `5.03#4` (6,3 s) | C | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *Để khép lại hồ sơ, chúng ta cần trả lại nhân phẩm và sự tôn trọng trọn vẹn nhất cho chàng trai trẻ Conrad Henri Roy Đệ Tam.* | — | — |  |
| 5-17 | `5.03#5` (7,2 s) | C | T1 | `t7_digital_cage_smartphone_glow`, `push` | *Cậu không phải là một con số thống kê lạnh lùng, mà là một thanh niên tài năng, một thuyền trưởng tàu kéo đầy nhiệt huyết và giàu lòng trắc ẩn.* | — | — |  |
| 5-18 | `5.03#6` (6,6 s) | C | T1 | `t7_suburban_living_room_tv`, `pan` | *Sự ra đi của Conrad là một mất mát to lớn, nhưng câu chuyện của cậu đã gióng lên một hồi chuông cảnh tỉnh thức tỉnh cả nhân loại.* | — | — |  |
| 5-19 | `5.03#7` (6,3 s) | C | T1 | `t7_digital_lighthouse_beacon`, `pull` | *Một lời nhắc nhở rằng lòng trắc ẩn và sự lắng nghe chân thành là chiếc khiên vững chắc nhất bảo vệ con người trước bóng tối.* | — | →H |  |
| 5-20 | `5.04#1` (11,6 s) | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Từ góc nhìn của khoa học tâm lý học tội phạm và nguyên lý Món quà của nỗi sợ, chúng ta rút ra những bài học sinh tồn sống còn để nhận diện những kẻ thao túng độc hại.* | — | — |  |
| 5-21 | `5.04#2` (9,3 s) | H | T1 | `t7_redflag1_isolated_virtual_bubble`, `push` | *Trong không gian mạng đầy rẫy những mối quan hệ ảo, có bốn tín hiệu cảnh báo đỏ nguy hiểm mà mỗi người cần đặc biệt khắc cốt ghi tâm.* | — | — |  |
| 5-22 | `5.04#3` (7,9 s) | H | T1 | `t7_redflag2_manipulative_text_provocation`, `pan` | *Những dấu hiệu nhận biết sớm giúp bảo vệ bản thân và người thân khỏi những chiếc bẫy thao túng tâm lý cưỡng bức.* | — | — |  |
| 5-23 | `5.04#4` (2,7 s) | H | T8 cờ | `t7_redflag1_isolated_virtual_bubble`, `pull` | *01* · **CẢNH BÁO ĐỎ 1: SỰ CÔ LẬP CÓ HỆ THỐNG.** | — | — |  |
| 5-24 | `5.04#5` (10,9 s) | H | T1 | `t7_redflag3_performative_grief_stage`, `still` | *Kẻ thao túng luôn tìm cách gieo rắc sự ngờ vực, chia rẽ bạn với gia đình, người thân và bạn bè ngoài đời thực để biến chúng thành điểm tựa cảm xúc duy nhất.* | — | — |  |
| 5-25 | `5.04#6` (3,8 s) | H | T8 cờ | `t7_redflag2_manipulative_text_provocation`, `push` | *02* · **CẢNH BÁO ĐỎ 2: KIỂM SOÁT CƯỠNG CHẾ ĐỘI LỐT QUAN TÂM.** | — | — |  |
| 5-26 | `5.04#7` (9,6 s) | H | T1 | `t7_redflag4_disconnect_phone_dawn`, `pan` | *Mọi hành động, tin nhắn và lịch trình của bạn đều bị giám sát dày đặc dưới chiêu bài của “tình yêu chân thành” hoặc sự thấu cảm giả tạo.* | — | — |  |
| 5-27 | `5.04#8` (4,7 s) | H | T8 cờ | `t7_redflag3_performative_grief_stage`, `pull` | *03* · **CẢNH BÁO ĐỎ 3: TẤN CÔNG LÒNG TỰ TRỌNG VÀ ĐẢO NGƯỢC VỊ THẾ ĐẠO ĐỨC.** | — | — |  |
| 5-28 | `5.04#9` (11,3 s) | H | T1 | `t7_closing_dossier_white_rose`, `still` | *Kẻ độc hại liên tục khiến bạn cảm thấy có lỗi, biến sự yếu đuối của bạn thành công cụ để sỉ nhục và bắt bạn phải chứng minh tình cảm bằng những hành vi cực đoan.* | — | — |  |
| 5-29 | `5.04#10` (4,8 s) | H | T8 cờ | `t7_redflag4_disconnect_phone_dawn`, `push` | *04* · **CẢNH BÁO ĐỎ 4: NUÔI DƯỠNG BÓNG TỐI THAY VÌ TÌM KIẾM GIẢI PHÁP Y TẾ.** | — | — |  |
| 5-30 | `5.04#11` (11,8 s) | H | T1 | `t7_digital_lighthouse_beacon`, `pan` | *Khi bạn bế tắc, thay vì khuyến khích bạn gặp bác sĩ hay tìm người giúp đỡ, chúng lại cổ vũ những suy nghĩ tiêu cực và biến bi kịch thành một thứ lãng mạn hóa nguy hiểm.* | — | — |  |
| 5-31 | `5.04#12` (13,1 s) | H | T1 | `t7_redflag1_isolated_virtual_bubble`, `pull` | *Nếu bạn hoặc những người xung quanh đang phải trải qua những cơn khủng hoảng tâm lý nặng nề hoặc có những suy nghĩ bế tắc, xin hãy nhớ rằng: Bạn không bao giờ phải đơn độc trong bóng tối.* | — | — |  |
| 5-32 | `5.04#13` (7,2 s) | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Luôn có những bàn tay ấm áp và sự hỗ trợ chuyên môn sẵn sàng đồng hành cùng bạn để vượt qua giông bão.* | — | — |  |
| 5-33 | `5.04#14` (11,1 s) | H | T1 | `t7_open_truck_door_fresh_air`, `push` | *Tại Việt Nam, xin vui lòng gọi ngay đến Tổng đài Quốc gia Bảo vệ Trẻ em 111, hoặc Đường dây nóng Ngày Mai hỗ trợ người trầm cảm qua số điện thoại 096 306 1414.* | — | — |  |
| 5-34 | `5.04#15` (8,1 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pan` | *Tại Hoa Kỳ và quốc tế, hãy liên hệ ngay Đường dây nóng Khủng hoảng và Ngăn ngừa Tự hại 988 để được hỗ trợ kịp thời.* | — | — |  |
| 5-35 | `5.04#16` (6,9 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pull` | *Hãy dũng cảm chia sẻ và tìm kiếm sự trợ giúp từ những người thực sự yêu thương bạn ngoài đời thực.* | — | — |  |
| 5-36 | `5.04#17`–`#18` (10,0 s) | H | T1 | `t7_redflag2_manipulative_text_provocation`, `still` | *Hồ sơ Tập 07 xin được chính thức khép lại tại đây.* → *Cảm ơn quý vị đã luôn đồng hành và lắng nghe những phân tích chuyên sâu của Amber Eyes.* | — | — |  |
| 5-37 | hết tập (7,5 s) | — | T1 | `t7_closing_dossier_white_rose`, `pull` | **HỒ SƠ TẬP 07 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | — | ⊘ | ◼ |

**Tổng:** 223 shot · 219 câu · 31 element lời (5 hồi) · nền dùng 62 loại. Bảng dựng lại 09/11/2026 theo kịch bản viết lại 07/11/2026 (219 câu). Thời lượng shot là **ước lượng** (chưa có audio master bản mới).
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
