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
| 1-01 | `1.02#1`–`#3` | H | T4 trích dẫn | `t7_digital_coercion_screen`, `pan` | *Cận cảnh màn hình điện thoại trong bóng tối, ánh sáng xanh lạnh buốt hắt lên ...* | — | ✦ Cú |  |
| 1-02 | `1.02#4`–`#6` | H | T1 | `t7_highway_50km_isolation`, `still` | *Tuyến đường cao tốc ban đêm vắng lặng nối hai thị trấn ven biển Massachusetts...* | — | — |  |
| 1-03 | `1.04#1`–`#2` | H | T1 | `t7_kmart_parking_lot_morning`, `pull` | *Bãi đỗ xe siêu thị Kmart rộng lớn hoang vắng dưới nắng hè gay gắt, một góc kh...* | — | — |  |
| 1-04 | `1.04#3` | H | T1 | `t7_ford_f250_black_truck`, `pan` | *Chiếc xe bán tải Ford F-250 màu đen đỗ im lìm dưới ánh nắng chói chang, cửa k...* | — | — |  |
| 1-05 | `1.06#1`–`#2` | H | T1 | `t7_water_pump_equipment`, `still` | *Tĩnh vật máy bơm nước cơ khí nhỏ đặt ở thùng xe sau, ống dẫn kim loại phủ bụi...* | — | — |  |
| 1-06 | `1.06#3`–`#5` | H | T1 | `t7_tugboat_harbor_fog`, `pull` | *Bến cảng tàu kéo Fairhaven mờ sương sớm, những con tàu kéo neo đậu bên cầu tà...* | — | — |  |
| 1-07 | `1.06#6`–`#7` | H | T1 | `t7_tugboat_captain_license`, `pan` | *Bằng chứng nhận thuyền trưởng tàu kéo lồng trong khung kính trên bàn làm việc...* | — | — |  |
| 1-08 | `1.06#8` | H | T1 | `t7_mothers_empty_kitchen_phone`, `pull` | *Gian bếp gia đình im lặng trong buổi sáng, chiếc điện thoại úp trên bàn ăn bên tách cà phê đã nguội ngắt...* | — | →N1 | — |
| 1-09 | `1.07#1`–`#3` | N1 | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *Bàn ăn trong gian bếp gia đình buổi sáng, chiếc điện thoại nhấp nháy cuộc gọi...* | — | ✦ Cừu |  |
| 1-10 | `1.07#4`–`#5` | N1 | T1 | `t7_kmart_police_perimeter`, `pull` | *Bãi đỗ xe Kmart bị phong tỏa bởi dây vàng cảnh sát, xe tuần tra nhấp nháy đèn...* | — | →H |  |
| 1-11 | `1.09#1`–`#3` | H | T1 | `t7_forensic_evidence_phone`, `pan` | *Chiếc điện thoại thông minh cũ của nạn nhân đặt trong túi zip đựng vật chứng ...* | — | →D |  |
| 1-12 | `1.10#1`–`#4` | D | T4 trích dẫn | `t7_digital_forensic_extraction`, `still` | *Màn hình máy tính điều tra viên hiển thị sơ đồ trích xuất dữ liệu pháp y điện...* | — | ✦ Sói · →H |  |
| 1-13 | `1.11#1`–`#2` | H | T1 | `t7_psychological_trap_metaphor`, `pull` | *Ẩn dụ thị giác: Một chiếc mê cung vô hình bằng những sợi dây phát sáng kỹ thu...* | — | →C |  |
| 1-14 | `1.12#1`–`#3` | C | T1 | `t7_clinical_depression_shadow`, `pan` | *Một bóng người đơn độc ngồi cúi đầu trên bờ vực đá hướng ra biển đen mù sương...* | — | ✦ Cáo · →H |  |
| 1-15 | `1.13#1`–`#2` | H | T2 thẻ hồ sơ | `t7_dossier_carter_case_07`, `still` | *Bìa hồ sơ điều tra vụ án Amber Eyes đặt trên bàn gỗ sẫm màu, dây thừ buộc chắc bên cạnh chiếc kính lúp và cây bút sắt cạnh...* | — | — |  |

### HỒI 2 — MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN · nền chủ đạo `t7_late_night_bedroom_phone`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#3` | H | T1 | `t7_florida_beach_encounter_2012`, `pan` | *Bờ biển Florida rực rỡ nhưng nhìn qua lăng kính noir hoài niệm, bóng hai thiế...* | — | →D |  |
| 2-02 | `2.03#1`–`#2` | D | T7 tuyến đường | `t7_massachusetts_route_map`, `still` | *Bản đồ vệ tinh địa hình bang Massachusetts kết nối hai điểm Plainville và Fai...* | — | — |  |
| 2-03 | `2.03#3`–`#4` | D | T5 ngày | `t7_late_night_bedroom_phone`, `pull` | *Góc phòng ngủ thiếu niên lúc ba giờ sáng, ánh sáng màn hình điện thoại xanh lạnh rọi xuống chăn nhàu nát...* | — | →H |  |
| 2-04 | `2.04#1`–`#3` | H | T4 trích dẫn | `t7_plainville_suburban_house`, `pan` | *Căn nhà hai tầng ngoại ô thị trấn Plainville Massachusetts trong ánh hoàng hô...* | — | — |  |
| 2-05 | `2.04#4`–`#6` | H | T1 | `t7_two_phone_screens_contrast`, `still` | *Hai chiếc điện thoại thông minh đặt đối diện nhau trên nền kính đen nứt vỡ, m...* | — | →D |  |
| 2-06 | `2.06#1` | D | T4 trích dẫn | `t7_sms_transcript_forensic_binder`, `pull` | *Tập hồ sơ in rời hàng trăm trang bản trích xuất tin nhắn điện thoại với các đ...* | — | — |  |
| 2-07 | `2.06#2` | D | T5 ngày | `t7_ticking_clock_deadlines`, `pan` | *Chiếc đồng hồ treo tường cổ điển kim giây đang nhích dần về phía nửa đêm, bón...* | — | →H |  |
| 2-08 | `2.07#1`–`#2` | H | T1 | `t7_family_photo_frame_shadow`, `still` | *Khung ảnh gia đình chụp ba mẹ con trên lò sưởi bị bóng tối chiaroscuro che kh...* | — | →C |  |
| 2-09 | `2.08#1`–`#4` | C | T1 | `t7_psychological_coercion_chess`, `pull` | *Bàn cờ vua bằng đá thạch anh trong bóng tối, một quân tốt trắng bị bao vây bở...* | — | →H |  |
| 2-10 | `2.09#1`–`#2` | H | T1 | `t7_kmart_lot_midnight_darkness`, `pan` | *Bãi đỗ xe Kmart lúc nửa đêm vắng lặng tuyệt đối, cột đèn cao áp nhấp nháy mờ ...* | — | — |  |
| 2-11 | `2.09#3`–`#4` | H | T1 | `t7_open_truck_door_fresh_air`, `still` | *Cánh cửa xe tải hé mở, bậc bước chân dính vài giọt sương, một luồng ánh sáng ...* | — | ⊘ |  |
| 2-12 | `2.09#5`–`#6` | H | T1 | `t7_night_sky_breath_of_life`, `pull` | *Bầu trời đêm sâu thẳm đầy sao phía trên bãi đỗ xe ven biển, làn gió đêm lay đ...* | — | ⊘ · →D |  |
| 2-13 | `2.10#1`–`#2` | D | T1 | `t7_incoming_call_timer_40min`, `pan` | *Chiếc điện thoại nằm trên nắp xe ướt đầy nước mưa, sóng âm thanh xanh lạnh nhấp nháy trên màn hình dưới ánh trăng mờ...* | — | — |  |
| 2-14 | `2.10#3` | D | T1 | `t7_closed_car_window_fog`, `still` | *Kính cửa sổ cabin xe tải đóng kín hoàn toàn từ bên trong, sương mù và hơi nướ...* | — | ⊘ · →H |  |

### HỒI 3 — VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH · nền chủ đạo `t7_empty_theater_spotlight`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1`–`#2` | H | T1 | `t7_empty_theater_spotlight`, `pan` | *Một sân khấu kịch bằng gỗ trống không, chỉ có một chiếc đèn rọi duy nhất rọi ...* | — | →C |  |
| 3-02 | `3.03#1`–`#3` | C | T1 | `t7_drama_masks_digital_glitch`, `still` | *Hai chiếc mặt nạ kịch nghệ (bi kịch và hài kịch) treo trên tường bê tông nứt ...* | — | →H |  |
| 3-03 | `3.04#1`–`#3` | H | T1 | `t7_highschool_empty_lockers`, `pull` | *Hành lang trường trung học King Philip hoang vắng lúc hoàng hôn, những dãy tủ...* | — | →D |  |
| 3-04 | `3.05#1`–`#2` | D | T1 | `t7_vintage_tv_glee_glow`, `pan` | *Màn hình tivi trong phòng tối đang phát một tập phim truyền hình ca nhạc than...* | — | — |  |
| 3-05 | `3.05#3`–`#4` | D | T1 | `t7_copied_script_lines_notebook`, `still` | *Cuốn sổ tay mở trên bàn học với những dòng chữ ghi chép cẩn thận các câu thoạ...* | — | →H |  |
| 3-06 | `3.06#1`–`#3` | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Một chiếc gương trang điểm trong phòng ngủ phản chiếu bộ trang phục tang lễ m...* | — | — |  |
| 3-07 | `3.06#4` | H | T1 | `t7_suburban_living_room_tv`, `pan` | *Phòng khách gia đình ấm cúng với tivi đang bật, chiếc ghế sofa êm ái nơi chàn...* | — | →C |  |
| 3-08 | `3.07#1`–`#3` | C | T1 | `t7_puppet_strings_metaphor`, `still` | *Ẩn dụ thị giác: Những sợi dây rối vô hình buông xuống từ trần nhà tăm tối, gắ...* | — | →H |  |
| 3-09 | `3.08#1`–`#3` | H | T1 | `t7_social_media_notifications_flood`, `pull` | *Biểu tượng thông báo lượt thích, lượt chia sẻ và bình luận an ủi trên màn hìn...* | — | — |  |
| 3-10 | `3.08#4`–`#5` | H | T1 | `t7_baseball_field_charity_empty`, `pan` | *Sân bóng chày ngoại ô vắng lặng lúc chạng vạng, chiếc găng tay bóng chày và q...* | — | — |  |
| 3-11 | `3.08#6` | H | T1 | `t7_cracked_porcelain_mask`, `still` | *Chiếc mặt nạ thiên thần bằng sứ trắng tinh khôi bị rạn nứt một đường chéo sắc...* | — | — |  |

### HỒI 4 — DÒNG TIN NHẮN ĐẦY TỘI LỖI VÀ BẢN ÁN LỊCH SỬ · nền chủ đạo `t7_taunton_courthouse_exterior`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1`–`#4` | H | T4 trích dẫn | `t7_confession_text_timestamp`, `pan` | *Màn hình điện thoại hiển thị ngày September 15 2014 với dòng tin nhắn văn bản...* | — | →N2 |  |
| 4-02 | `4.03#1`–`#2` | N2 | T1 | `t7_witness_trembling_phone`, `still` | *Cận cảnh bàn tay thiếu nữ nắm chặt chiếc điện thoại đang phát sáng trong quán...* | — | ✦ Mèo |  |
| 4-03 | `4.03#3` | N2 | T4 trích dẫn | `t7_confession_message_turn`, `pull` | *Tập tài liệu in lời khai nhân chứng được đóng dấu tiếp nhận, các dòng khai về tin nhắn nằm ngay ngắn dưới con dấu đỏ...* | — | →H |  |
| 4-04 | `4.05#1`–`#3` | H | T2 thẻ hồ sơ | `t7_bristol_county_indictment_stamp`, `pan` | *Văn bản cáo trạng của Tòa án Hạt Bristol với con dấu mực đỏ tươi INDICTMENT I...* | — | — |  |
| 4-05 | `4.05#4`–`#5` | H | T1 | `t7_taunton_courthouse_exterior`, `still` | *Mặt tiền Tòa án Hạt Bristol tại Taunton Massachusetts bằng đá hoa cương uy ng...* | — | — |  |
| 4-06 | `4.05#6` | H | T1 | `t7_empty_courtroom_bench_trial`, `pull` | *Góc nhìn bên trong phòng xử án trang nghiêm, dãy ghế bồi thẩm đoàn hoàn toàn ...* | — | →D |  |
| 4-07 | `4.06#1`–`#2` | D | T4 trích dẫn | `t7_courtroom_projection_screen`, `pan` | *Màn hình máy chiếu lớn trong phòng xử án hiển thị hàng chục dòng tin nhắn phó...* | — | — |  |
| 4-08 | `4.06#3`–`#4` | D | T1 | `t7_us_constitution_amendment1`, `still` | *Quyển sách luật Hiến pháp Hoa Kỳ mở tại trang Tu chính án thứ nhất bên cạnh c...* | — | →C |  |
| 4-09 | `4.07#1`–`#4` | C | T1 | `t7_prescription_pill_bottle_celexa`, `pull` | *Lọ thuốc chống trầm cảm theo toa bằng nhựa màu hổ phách đặt trên mặt bàn kính...* | — | →H |  |
| 4-10 | `4.08#1`–`#4` | H | T1 | `t7_judge_moniz_bench_gavel`, `pan` | *Bục xét xử của Thẩm phán Lawrence Moniz với chiếc búa gỗ tư pháp đặt trang tr...* | — | — |  |
| 4-11 | `4.08#5` | H | T1 | `t7_courtroom_breathless_silence`, `still` | *Toàn cảnh phòng xử án chìm trong sự im lặng căng thẳng tuyệt đối, các hàng gh...* | — | — |  |
| 4-12 | `4.10#1`–`#2` | H | T2 thẻ hồ sơ | `t7_court_verdict_document_guilty`, `pull` | *Bản án chính thức của Tòa án Tối cao Massachusetts có chữ ký và dấu mộc xác n...* | — | — |  |
| 4-13 | `4.10#3` | H | T1 | `t7_bristol_county_jail_bars`, `pan` | *Song sắt nhà giam Hạt Bristol đổ bóng dài xuống hành lang bê tông xám lạnh lẽ...* | — | — |  |

### HỒI 5 — ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD · nền chủ đạo `t7_digital_lighthouse_beacon`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#3` | H | T1 | `t7_massachusetts_state_house_dome`, `pan` | *Mái vòm mạ vàng của Tòa nhà Nghị viện Bang Massachusetts tại Boston vươn cao ...* | — | — |  |
| 5-02 | `5.02#4`–`#5` | H | T1 | `t7_conrads_law_legislative_bill`, `still` | *Dự thảo văn bản Conrad's Law An Act Preventing Coerced Suicide được đệ trình ...* | — | →C |  |
| 5-03 | `5.03#1`–`#3` | C | T1 | `t7_digital_cage_smartphone_glow`, `pull` | *Ẩn dụ thị giác: Một chiếc lồng chim bằng thanh kim loại mỏng bao bọc một chiế...* | — | →H |  |
| 5-04 | `5.04#1`–`#2` | H | T8 cờ | `t7_redflag1_isolated_virtual_bubble`, `pan` | *01* · **CẢNH BÁO ĐỎ 1 — CẢNH GIÁC TRƯỚC CÁC MỐI QUAN HỆ ẢO SIÊU TỐC VÀ CÔ LẬP** | — | — |  |
| 5-05 | `5.04#3`–`#4` | H | T1 | `t7_redflag1_isolated_virtual_bubble`, `still` | *Bong bóng thuỷ tinh phát sáng cô lập giữa rừng cây tăm tối, bên trong là một bóng người bị giam trong không gian số khép kín không lối ra...* | — | — | — |
| 5-06 | `5.04#5`–`#7` | H | T4 trích dẫn | `t7_redflag2_manipulative_text_provocation`, `still` | *Cảnh báo đỏ 2: Cận cảnh những dòng tin nhắn mỉa mai khiêu khích hiện lên trên...* | — | — |  |
| 5-07 | `5.04#8`–`#10` | H | T8 cờ | `t7_redflag3_performative_grief_stage`, `pull` | *03* · **CẢNH BÁO ĐỎ 3 — HỘI CHỨNG KHAO KHÁT SỰ CHÚ Ý VÀ KỊCH TÍN HÓA BI KỊCH** | — | — |  |
| 5-08 | `5.04#11`–`#12` | H | T8 cờ | `t7_redflag4_disconnect_phone_dawn`, `pan` | *04* · **CẢNH BÁO ĐỎ 4 — LẮNG NGHE BẢN NĂNG SINH TỒN VÀ DỨT KHOÁT CẮT ĐỨT LIÊN LẠC** | — | — |  |
| 5-09 | `5.04#13`–`#15` | H | T1 | `t7_redflag4_disconnect_phone_dawn`, `pull` | *Chiếc điện thoại thông minh bị đặt úp mặt xuống chiếc bàn gỗ sáng bên cửa sổ bình minh, ánh nắng đầu ngày rọi qua lưng điện thoại...* | — | — | — |
| 5-10 | `5.04#16`–`#17` | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Ngọn hải đăng ven biển Fairhaven quét luồng sáng vàng rực rỡ xuyên qua màn đê...* | — | — |  |
| 5-11 | `5.04#18`–`#19` | H | T1 | `t7_closing_dossier_white_rose`, `pull` | *Chồng hồ sơ đã đóng dấu trên bàn gỗ, bên cạnh bình hoa bông hồng trắng và ngọn nến đang cháy trong buổi sáng sớm...* | — | — |  |
| 5-12 | hết tập (10 s) | — | T1 | `t7_closing_dossier_white_rose`, `pull` | *HỒ SƠ TẬP 07 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật* | — | — | — |

**Tổng: 66 shot** (1 shot mở đầu 1-00 + 64 shot theo câu thoại + 1 shot thẻ kết). Phủ kín 147 câu thoại trọn vẹn (bảng viết lại 03/11/2026 sau khi vá V9).

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
