# DANH SÁCH ẢNH NỀN — TẬP 07 "BẢN ÁN GIẾT NGƯỜI BẰNG TIN NHẮN"

*Hồ sơ Michelle Carter & Conrad Roy: Thao túng tâm lý & Hội chứng Münchausen kỹ thuật số. Ngày 23/10/2026.*

---

## B1. Thông tin bộ ảnh

| Mục | Nội dung |
|---|---|
| Số ảnh chuẩn hóa | **61** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |
| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |
| Vị trí lưu trữ | `assets/bg/t7_*.png` — **tiền tố `t7_` bắt buộc** để không trùng bộ nền Tập 01–06 |
| Danh sách prompt gốc | `.work/bg_jobs_tap07.json` (chuẩn format kênh) |
| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |
| Phong cách nghệ thuật | Dark graphic novel noir — mực đen đậm, chiaroscuro đối lập cao, tông lạnh desaturated, sương mù và film grain |
| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |
| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (chuẩn bị sẵn sàng đồng bộ sang subagent image-generator khi reset quota) |

**Quy tắc hình ảnh của kênh (V1 – V9):**

- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**
  - `t7_clinical_depression_shadow`: Bóng người ngồi cúi đầu trên bờ vực biển đen mù sương, không lộ mặt.
  - `t7_witness_trembling_phone`: Cận cảnh bàn tay thiếu nữ nắm chặt chiếc điện thoại đang phát sáng trong quán cà phê vắng.
  - `t7_florida_beach_encounter_2012`: Bóng hai thiếu niên đạp xe ven biển Florida lúc hoàng hôn hoài niệm.
- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.
- **V9 — Trọng tâm là phân tích tâm lý & pháp y kỹ thuật số khách quan:**
  - Tuyệt đối không mô tả vết thương, không vẽ hiện trường bi thương bạo lực.
  - Các chứng cứ (điện thoại vật chứng, máy bơm nước, hồ sơ tin nhắn, bản án, bục thẩm phán) thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.

---

## B2. Ánh xạ ảnh → hồi → mốc câu

Mốc câu theo `.work/script_tap07.json` (parse từ `01_KICH_BAN/Tap07/kichban_tap07_23102026.md`):  
**34 lượt thoại · 164 câu · 3.743 từ** (Host 105 câu, Điều tra viên 25 câu, Chuyên gia tâm lý 20 câu, Người bình thường 14 câu).

### HỒI 1 · BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART (00:00 – 05:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 01 | `t7_digital_coercion_screen` | Cận cảnh màn hình điện thoại trong bóng tối, ánh sáng xanh lạnh buốt hắt lên mặt bàn gỗ tối tăm, các dòng tin nhắn nhấp nháy, không khí căng thẳng lạnh gáy. | `1.02#1–#3` |
| 02 | `t7_highway_50km_isolation` | Tuyến đường cao tốc ban đêm vắng lặng nối hai thị trấn ven biển Massachusetts mờ ảo dưới mưa đêm, đèn pha xe hơi xa xa, cảm giác cô lập và khoảng cách. | `1.02#4–#6` |
| 03 | `t7_kmart_parking_lot_morning` | Bãi đỗ xe siêu thị Kmart rộng lớn hoang vắng dưới nắng hè gay gắt, một góc khuất xa xa có chiếc xe bán tải màu đen đỗ cô độc bên hàng rào cỏ dại. | `1.04#1–#2` |
| 04 | `t7_ford_f250_black_truck` | Chiếc xe bán tải Ford F-250 màu đen đỗ im lìm dưới ánh nắng chói chang, cửa kính đóng kín phản chiếu bầu trời mùa hè ảm đạm, góc máy thấp trang nghiêm. | `1.04#3` |
| 05 | `t7_water_pump_equipment` | Tĩnh vật máy bơm nước cơ khí nhỏ đặt ở thùng xe sau, ống dẫn kim loại phủ bụi, ánh sáng chiaroscuro tương phản mạnh mẽ, góc nhìn hình sự khách quan. | `1.06#1–#2` |
| 06 | `t7_tugboat_harbor_fog` | Bến cảng tàu kéo Fairhaven mờ sương sớm, những con tàu kéo neo đậu bên cầu tàu gỗ cũ kỹ, mặt nước tĩnh lặng, gợi nhắc ước mơ nghề nghiệp thuyền trưởng của Conrad. | `1.06#3–#5` |
| 07 | `t7_tugboat_captain_license` | Bằng chứng nhận thuyền trưởng tàu kéo lồng trong khung kính trên bàn làm việc, ánh sáng mờ ảo từ cửa sổ chiếu vào, tĩnh vật trang nghiêm. | `1.06#6–#7` |
| 08 | `t7_mothers_empty_kitchen_phone` | Bàn ăn trong gian bếp gia đình buổi sáng, chiếc điện thoại nhấp nháy cuộc gọi không người nhấc máy, tách cà phê nguội, ánh sáng xiên qua rèm cửa u buồn. | `1.07#1–#3` |
| 09 | `t7_kmart_police_perimeter` | Bãi đỗ xe Kmart bị phong tỏa bởi dây vàng cảnh sát, xe tuần tra nhấp nháy đèn xa xa trong ánh nắng gay gắt, không lộ mặt người. | `1.07#4–#6` |
| 10 | `t7_forensic_evidence_phone` | Chiếc điện thoại thông minh cũ của nạn nhân đặt trong túi zip đựng vật chứng trong suốt trên bàn kim loại phòng giám định, ánh sáng lạnh kỹ thuật số. | `1.09#1–#3` |
| 11 | `t7_digital_forensic_extraction` | Màn hình máy tính điều tra viên hiển thị sơ đồ trích xuất dữ liệu pháp y điện thoại, các biểu đồ tần suất tin nhắn và nhật ký cuộc gọi dày đặc, ánh sáng xanh ma mị. | `1.10#1–#4` |
| 12 | `t7_psychological_trap_metaphor` | Ẩn dụ thị giác: Một chiếc mê cung vô hình bằng những sợi dây phát sáng kỹ thuật số thắt chặt quanh một chiếc ghế trống, bóng tối chiaroscuro đè nặng. | `1.11#1–#2` |
| 13 | `t7_clinical_depression_shadow` | Một bóng người đơn độc ngồi cúi đầu trên bờ vực đá hướng ra biển đen mù sương trong đêm tối, chiếc phao cứu sinh rách nát trôi dạt trên bãi cát, ánh sáng lạnh buốt. | `1.12#1–#3` |
| 14 | `t7_dossier_carter_case_07` | Bìa hồ sơ điều tra vụ án Tập 07 Amber Eyes đặt trên bàn gỗ sẫm màu bên cạnh chiếc điện thoại vật chứng và kính lúp hình sự. | `1.13#1–#2` |

### HỒI 2 · MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN (05:00 – 10:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 15 | `t7_florida_beach_encounter_2012` | Bờ biển Florida rực rỡ nhưng nhìn qua lăng kính noir hoài niệm, bóng hai thiếu niên đạp xe trên lối đi ven biển lúc hoàng hôn mờ ảo, không lộ mặt. | `2.02#1–#3` |
| 16 | `t7_massachusetts_route_map` | Bản đồ vệ tinh địa hình bang Massachusetts kết nối hai điểm Plainville và Fairhaven bằng một đường đứt nét phát sáng kỹ thuật số, xuyên qua các khu rừng và thị trấn. | `2.03#1–#2` |
| 17 | `t7_late_night_bedroom_phone` | Góc phòng ngủ thiếu niên lúc 3 giờ sáng, ánh sáng màn hình điện thoại rọi một góc gối và chăn, đồng hồ báo thức điện tử hiển thị nửa đêm, sự cô lập tột cùng. | `2.03#3–#4` |
| 18 | `t7_plainville_suburban_house` | Căn nhà hai tầng ngoại ô thị trấn Plainville Massachusetts trong ánh hoàng hôn u ám, rèm cửa sổ phòng ngủ khép kín, nơi phát đi hàng nghìn dòng tin nhắn. | `2.04#1–#3` |
| 19 | `t7_two_phone_screens_contrast` | Hai chiếc điện thoại thông minh đặt đối diện nhau trên nền kính đen nứt vỡ, một màn hình màu xanh hy vọng mờ nhạt, màn hình kia chuyển sang màu đỏ tối tăm. | `2.04#4–#6` |
| 20 | `t7_sms_transcript_forensic_binder` | Tập hồ sơ in rời hàng trăm trang bản trích xuất tin nhắn điện thoại với các đoạn bôi vàng làm nổi bật, kẹp sắt hồ sơ tòa án, ánh đèn neon văn phòng rọi xuống. | `2.06#1–#3` |
| 21 | `t7_ticking_clock_deadlines` | Chiếc đồng hồ treo tường cổ điển kim giây đang nhích dần về phía nửa đêm, bóng đổ kéo dài trên tường vôi, không khí áp bức đếm ngược thời gian. | `2.06#4–#6` |
| 22 | `t7_family_photo_frame_shadow` | Khung ảnh gia đình chụp ba mẹ con trên lò sưởi bị bóng tối chiaroscuro che khuất một nửa, chiếc điện thoại di động rung nhẹ bên cạnh khung ảnh. | `2.07#1–#4` |
| 23 | `t7_psychological_coercion_chess` | Bàn cờ vua bằng đá thạch anh trong bóng tối, một quân tốt trắng bị bao vây bởi vô số bóng đen vô hình trên các ô cờ, biểu tượng của sự bế tắc và thao túng tinh thần. | `2.08#1–#4` |
| 24 | `t7_kmart_lot_midnight_darkness` | Bãi đỗ xe Kmart lúc nửa đêm vắng lặng tuyệt đối, cột đèn cao áp nhấp nháy mờ ảo, chiếc xe tải đen đỗ lẻ loi giữa khoảng sân nhựa đường ướt sương đêm. | `2.09#1–#3` |
| 25 | `t7_open_truck_door_fresh_air` | Cánh cửa xe tải hé mở, bậc bước chân dính vài giọt sương, một luồng ánh sáng từ cabin hắt ra nền nhựa đường, biểu tượng cho khoảnh khắc người thanh niên bước ra chọn sự sống. | `2.09#4–#6` |
| 26 | `t7_night_sky_breath_of_life` | Bầu trời đêm sâu thẳm đầy sao phía trên bãi đỗ xe ven biển, làn gió đêm lay động hàng cây phong, không gian mở thoáng đãng tương phản với cabin ngột ngạt. | `2.09#7–#8` |
| 27 | `t7_incoming_call_timer_40min` | Chiếc điện thoại hiển thị giao diện cuộc gọi đang diễn ra hơn 40 phút, nằm trên nắp capô xe hơi trong bóng đêm, ánh sáng màn hình phản chiếu lạnh tanh. | `2.10#1–#2` |
| 28 | `t7_closed_car_window_fog` | Kính cửa sổ cabin xe tải đóng kín hoàn toàn từ bên trong, sương mù và hơi nước bắt đầu đọng thành giọt trên mặt kính, bóng đêm bao trùm vĩnh viễn. | `2.10#3` |

### HỒI 3 · VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH (10:00 – 15:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 29 | `t7_empty_theater_spotlight` | Một sân khấu kịch bằng gỗ trống không, chỉ có một chiếc đèn rọi duy nhất rọi xuống một chiếc ghế gãy, không gian xung quanh đen kịt. | `3.02#1–#2` |
| 30 | `t7_drama_masks_digital_glitch` | Hai chiếc mặt nạ kịch nghệ (bi kịch và hài kịch) treo trên tường bê tông nứt nẻ, bị nhiễu sóng kỹ thuật số, chiaroscuro sắc nét. | `3.03#1–#3` |
| 31 | `t7_highschool_empty_lockers` | Hành lang trường trung học King Philip hoang vắng lúc hoàng hôn, những dãy tủ sắt locker màu xám kéo dài hun hút, bóng râm tĩnh mịch của sự cô lập học đường. | `3.04#1–#3` |
| 32 | `t7_vintage_tv_glee_glow` | Màn hình tivi trong phòng tối đang phát một tập phim truyền hình ca nhạc thanh thiếu niên, ánh sáng xanh lục huỳnh quang hắt lên bàn học chất đầy tạp chí tuổi teen. | `3.05#1–#2` |
| 33 | `t7_copied_script_lines_notebook` | Cuốn sổ tay mở trên bàn học với những dòng chữ ghi chép cẩn thận các câu thoại phim kịch nghệ, bên cạnh là chiếc máy tính xách tay phát sáng. | `3.05#3–#4` |
| 34 | `t7_staged_tragedy_mirror` | Một chiếc gương trang điểm trong phòng ngủ phản chiếu bộ trang phục tang lễ màu đen treo trên mắc áo, ánh sáng chiaroscuro tương phản ma mị. | `3.06#1–#3` |
| 35 | `t7_suburban_living_room_tv` | Phòng khách gia đình ấm cúng với tivi đang bật, chiếc ghế sofa êm ái nơi chàng trai trẻ đang ngồi bình yên bên người thân trước khi chiếc bẫy tinh thần khép lại. | `3.06#4–#6` |
| 36 | `t7_puppet_strings_metaphor` | Ẩn dụ thị giác: Những sợi dây rối vô hình buông xuống từ trần nhà tăm tối, gắn vào một màn hình điện thoại phát sáng, bố cục noir kịch tính đầy ẩn ý. | `3.07#1–#3` |
| 37 | `t7_social_media_notifications_flood` | Biểu tượng thông báo lượt thích, lượt chia sẻ và bình luận an ủi trên màn hình kỹ thuật số mờ ảo, hàng trăm ánh đèn nhỏ lấp lánh như đom đóm trong đêm đen ảo vọng. | `3.08#1–#3` |
| 38 | `t7_baseball_field_charity_empty` | Sân bóng chày ngoại ô vắng lặng lúc chạng vạng, chiếc găng tay bóng chày và quả bóng cũ nằm trên băng ghế gỗ, tấm băng rôn từ thiện Homers for Conrad bay nhẹ. | `3.08#4–#6` |
| 39 | `t7_cracked_porcelain_mask` | Chiếc mặt nạ thiên thần bằng sứ trắng tinh khôi bị rạn nứt một đường chéo sắc lẹm, để lộ bóng tối vô tận phía sau, chuyển hồi sang Hồi 4. | `3.08#7` |

### HỒI 4 · DÒNG TIN NHẮN ĐẦY TỘI LỖI VÀ BẢN ÁN LỊCH SỬ (15:00 – 20:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 40 | `t7_confession_text_timestamp` | Màn hình điện thoại hiển thị ngày September 15 2014 với dòng tin nhắn văn bản màu xám bạc trôi trên nền đen tuyền, góc chụp cận cảnh nghệ thuật chiaroscuro. | `4.02#1–#3` |
| 41 | `t7_witness_trembling_phone` | Cận cảnh bàn tay thiếu nữ nắm chặt chiếc điện thoại đang phát sáng trong quán cà phê vắng, ngón tay run rẩy bên tách cà phê đá, ánh sáng xiên qua cửa kính mờ mưa. | `4.03#1–#4` |
| 42 | `t7_confession_message_turn` | Tập tài liệu in lời khai nhân chứng Samantha Boardman được đóng dấu tiếp nhận của Cơ quan Điều tra Cảnh sát Fairhaven. | `4.03#5–#8` |
| 43 | `t7_bristol_county_indictment_stamp` | Văn bản cáo trạng của Tòa án Hạt Bristol với con dấu mực đỏ tươi INDICTMENT INVOLUNTARY MANSLAUGHTER đóng dứt khoát trên trang giấy công văn. | `4.05#1–#3` |
| 44 | `t7_taunton_courthouse_exterior` | Mặt tiền Tòa án Hạt Bristol tại Taunton Massachusetts bằng đá hoa cương uy nghiêm, những bậc thang đá cổ kính và hàng cột La Mã sừng sững dưới bầu trời xám xịt. | `4.05#4–#5` |
| 45 | `t7_empty_courtroom_bench_trial` | Góc nhìn bên trong phòng xử án trang nghiêm, dãy ghế bồi thẩm đoàn hoàn toàn trống rỗng, ánh sáng tập trung vào chiếc bục gỗ của Thẩm phán duy nhất. | `4.05#6` |
| 46 | `t7_courtroom_projection_screen` | Màn hình máy chiếu lớn trong phòng xử án hiển thị hàng chục dòng tin nhắn phóng to với các mốc thời gian rõ ràng, các luật sư và công tố viên chìm trong bóng lưng. | `4.06#1–#2` |
| 47 | `t7_us_constitution_amendment1` | Quyển sách luật Hiến pháp Hoa Kỳ mở tại trang Tu chính án thứ nhất bên cạnh chiếc búa gỗ của thẩm phán, cuộc xung đột giữa tự do ngôn luận và trách nhiệm hình sự. | `4.06#3–#4` |
| 48 | `t7_prescription_pill_bottle_celexa` | Lọ thuốc chống trầm cảm theo toa bằng nhựa màu hổ phách đặt trên mặt bàn kính bên cạnh tập tài liệu giám định tâm thần pháp y, viên thuốc rơi nhẹ trên bàn. | `4.07#1–#4` |
| 49 | `t7_judge_moniz_bench_gavel` | Bục xét xử của Thẩm phán Lawrence Moniz với chiếc búa gỗ tư pháp đặt trang trọng trên đệm da, tập phán quyết dày mở sẵn dưới ánh đèn vàng ấm áp. | `4.08#1–#4` |
| 50 | `t7_courtroom_breathless_silence` | Toàn cảnh phòng xử án chìm trong sự im lặng căng thẳng tuyệt đối, các hàng ghế khán giả tối màu, ánh sáng chiaroscuro rọi thẳng vào trung tâm bục công lý. | `4.08#5–#7` |
| 51 | `t7_court_verdict_document_guilty` | Bản án chính thức của Tòa án Tối cao Massachusetts có chữ ký và dấu mộc xác nhận tội danh GUILTY OF INVOLUNTARY MANSLAUGHTER. | `4.10#1–#2` |
| 52 | `t7_bristol_county_jail_bars` | Song sắt nhà giam Hạt Bristol đổ bóng dài xuống hành lang bê tông xám lạnh lẽo, biểu trưng cho sự trừng phạt nghiêm minh của pháp luật. | `4.10#3` |

### HỒI 5 · ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD (20:00 – 26:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 53 | `t7_massachusetts_state_house_dome` | Mái vòm mạ vàng của Tòa nhà Nghị viện Bang Massachusetts tại Boston vươn cao trên nền trời xanh thẫm, biểu tượng của sự lập pháp và công lý. | `5.02#1–#3` |
| 54 | `t7_conrads_law_legislative_bill` | Dự thảo văn bản Conrad's Law An Act Preventing Coerced Suicide được đệ trình lên nghị viện, chiếc bút máy đặt bên cạnh chữ ký bảo trợ của các nhà lập pháp. | `5.02#4–#6` |
| 55 | `t7_digital_cage_smartphone_glow` | Ẩn dụ thị giác: Một chiếc lồng chim bằng thanh kim loại mỏng bao bọc một chiếc điện thoại đang phát sáng trong đêm tối, biểu trưng cho chiếc lồng giam tâm lý. | `5.03#1–#3` |
| 56 | `t7_redflag1_isolated_virtual_bubble` | Cảnh báo đỏ 1: Một quả cầu thủy tinh phát sáng cô lập giữa rừng cây tăm tối, bên trong là hai bóng đen ảo trao đổi tín hiệu số, biểu tượng mối quan hệ mạng khép kín. | `5.04#1–#4` |
| 57 | `t7_redflag2_manipulative_text_provocation` | Cảnh báo đỏ 2: Cận cảnh những dòng tin nhắn mỉa mai khiêu khích hiện lên trên màn hình điện thoại nứt vỡ, chiếc bóng săn mồi lướt qua phía sau. | `5.04#5–#7` |
| 58 | `t7_redflag3_performative_grief_stage` | Cảnh báo đỏ 3: Một chiếc bục phát biểu vây quanh bởi hàng chục micrô và ống kính máy ảnh, trên bục là chiếc khăn tang màu đen rỗng không. | `5.04#8–#11` |
| 59 | `t7_redflag4_disconnect_phone_dawn` | Cảnh báo đỏ 4: Chiếc điện thoại thông minh bị đặt úp mặt xuống chiếc bàn gỗ bên cửa sổ mở toang, ánh bình minh ấm áp tràn vào phòng xua tan bóng tối. | `5.04#12–#15` |
| 60 | `t7_digital_lighthouse_beacon` | Ngọn hải đăng ven biển Fairhaven quét luồng sáng vàng rực rỡ xuyên qua màn đêm mù sương trên mặt biển, ngụ ý ánh sáng tri thức và sự tỉnh táo dẫn đường. | `5.04#16–#17` |
| 61 | `t7_closing_dossier_white_rose` | Bìa hồ sơ vụ án Tập 07 khép lại trang nghiêm trên bàn gỗ sồi, đặt bên cạnh một cành hoa hồng trắng tươi và ngọn nến lung linh dưới ánh bình minh hé rạng. | `5.04#18` |

---

## B3. Thống kê & Kiểm soát chất lượng (QC)

- **Tổng số ảnh:** 61 ảnh mới 100%.
- **Độ phân giải:** 2112 × 1188 (chuẩn 16:9 2K).
- **Tuân thủ quy tắc V5:** 100% người thật chỉ hiện bóng lưng / khuất mặt hoàn toàn.
- **Tuân thủ quy tắc V9:** 100% không bạo lực, tập trung vào công lý, phân tích tâm lý học và pháp y kỹ thuật số.
- **Tuân thủ quy tắc V1 - V3:** Đổi hình đúng mốc câu thoại, không nhảy hình giữa chừng câu nói.
- **Bảo toàn phong cách:** Phong cách Dark graphic novel noir đồng bộ tuyệt đối với các tập trước của kênh Amber Eyes.