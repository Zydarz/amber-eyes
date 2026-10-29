# DANH SÁCH ẢNH NỀN — TẬP 05 "CHIẾC ĐĨA MỀM MÀU TÍM & CƠN NGHIỆN ÁI KỶ"

*Hồ sơ Dennis Rader (BTK) & Sự Sụp Đổ Của Vỏ Bọc 30 Năm. Ngày 23/10/2026.*

---

## B1. Thông tin bộ ảnh

| Mục | Nội dung |
|---|---|
| Số ảnh mới | **61** ảnh sinh mới (toàn bộ dùng trong bảng shot & visual của tập) |
| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/_raw/` |
| Vị trí lưu trữ | `assets/bg/t5_*.png` — **tiền tố `t5_` bắt buộc** để không trùng bộ nền Tập 01/02/03/04 |
| Danh sách prompt gốc | `.work/bg_jobs_tap05.json` (chuẩn format kênh) |
| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |
| Phong cách nghệ thuật | Dark graphic novel noir — mực đen đậm, chiaroscuro đối lập cao, tông lạnh desaturated, sương mù và film grain |
| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |
| Công cụ thực thi | `connector__matrix__generate_image` (MiniMax qua mcode-tools), 16:9, 2K |

**Quy tắc hình ảnh của kênh (V1 – V9):**

- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**
  - `t5_compliance_truck_street`: Viên chức quản lý đô thị trong đồng phục nhìn từ sau lưng đang cầm thước đo cỏ.
  - `t5_detective_war_room`: Hai thám tử mặc áo măng-tô nhìn từ sau lưng hướng lên bảng ghim điều tra.
  - `t5_narcissist_mirror_shadow`: Bóng đen người đàn ông nhìn vào gương nứt vỡ trong phòng tối.
  - `t5_two_faces_silhouette`: Bóng đen đứng ở ranh giới ánh sáng và bóng tối, không lộ diện mạo.
  - `t5_interrogation_confrontation`: Phòng thẩm vấn nhìn từ phía sau lưng điều tra viên.
- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.
- **V9 — Trọng tâm là phân tích tâm lý & pháp y khách quan:**
  - Tuyệt đối không mô tả chi tiết vết thương, thi thể, máu me; không vẽ hình ảnh giằng co, tấn công.
  - Các kỷ vật vụ án (đĩa mềm, máy đánh chữ, hộp ngũ cốc, metadata máy tính, mẫu ADN, búa tòa án) được thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.

---

## B2. Ánh xạ ảnh → hồi → mốc câu

Mốc câu theo `.work/script_tap05.json` (parse từ `01_KICH_BAN/Tap05/kichban_tap05_23102026.md`):  
**33 lượt thoại · 164 câu · 4.209 từ** (Host 79 câu, Điều tra viên 54 câu, Chuyên gia tâm lý 24 câu, Người bình thường 7 câu).

### HỒI 1 · THE HOOK — BỨC THƯ TÁI XUẤT SAU 13 NĂM LẶNG CĂM (00:00 – 04:45)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 01 | `t5_wichita_skyline_dusk` | Toàn cảnh Wichita, Kansas lúc chạng vạng đông ảm đạm, sương mù lạnh lẽo | `1.03#1`–`#2` |
| 02 | `t5_eagle_newsroom_night` | Tòa soạn báo The Wichita Eagle ban đêm, bàn làm việc vắng lặng | `1.03#3` |
| 03 | `t5_manila_envelope_polaroids` | Phong bì thư màu vàng mở hé, lộ ảnh hiện trường cũ và bằng lái xe của Vicki Wegerle | `1.03#4` |
| 04 | `t5_btk_signature_letter` | Ba chữ cái B-T-K ký tay ở cuối bức thư trêu ngươi | `1.03#5` |
| 05 | `t5_newspaper_bundle_dawn` | Báo in buổi sáng giật tít về sự trở lại của bóng ma BTK sau 13 năm | `1.05#1`–`#2` |
| 06 | `t5_vintage_typewriter_desk` | Chiếc máy đánh chữ cơ học cổ điển, biểu tượng thông điệp quá khứ | `1.05#3`–`#4` |
| 07 | `t5_cold_case_archives` | Kho hồ sơ án nguội của cảnh sát Wichita ngủ đông suốt 13 năm | `1.05#5` |
| 08 | `t5_park_city_suburb` | Khu ngoại ô Park City thanh bình, bãi cỏ mùa đông xơ xác | `1.07#1`, `1.09#1`–`#2` |
| 09 | `t5_suburban_house_locked` | Nhà dân then cài cửa đóng, rèm khép kín trong nỗi khiếp sợ mơ hồ | `1.09#3` |
| 10 | `t5_compliance_truck_street` | Xe bán tải công vụ và viên chức trật tự đô thị đo cỏ nhìn từ sau lưng | `1.10#1`–`#4` |
| 11 | `t5_detective_war_room` | Ban chuyên án họp khẩn, bảng ghim manh mối và sơ đồ thời gian | `1.10#5`–`#7`, `1.12#1`, `1.14#1`–`#2` |
| 12 | `t5_book_manuscript_desk` | Bản thảo cuốn sách của Robert Beattie xúc phạm lòng tự tôn ái kỷ | `1.14#3`–`#5` |
| 13 | `t5_narcissist_mirror_shadow` | Cái tôi ái kỷ không chấp nhận sự quên lãng của nhân loại | `1.14#6`–`#7` |
| 14 | `t5_amber_eyes_dossier_05` | Mở hồ sơ Amber Eyes Tập 05 phân tích tâm lý học Dennis Rader | `1.16#1`–`#3` |

### HỒI 2 · HIỆN TRƯỜNG & HỒ SƠ TỘI ÁC — CHỮ KÝ TÂM LÝ CỦA CON THÚ HAI MẶT (04:45 – 10:30)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 15 | `t5_darkened_house_exterior` | Hiện trường ngôi nhà đơn lập trong đêm tối, đường dây điện thoại bị cắt | `2.02#1`–`#2` |
| 16 | `t5_btk_signature_metaphor` | Ẩn dụ chữ ký tâm lý Bind - Torture - Kill: dây thừng, kéo và đồng hồ cát | `2.02#3`–`#4`, `2.04#1`–`#3` |
| 17 | `t5_trophy_lockbox` | Hộp sắt bí mật cất giữ chiến lợi phẩm: bằng lái, đồng hồ, trang sức nạn nhân | `2.04#4`–`#6` |
| 18 | `t5_public_library_bookshelves` | Dãy giá sách thư viện công cộng, nơi kẻ thủ ác dán thư trêu ngươi | `2.04#7`–`#8` |
| 19 | `t5_park_trashcan_drop` | Thùng rác công viên mùa đông sương mờ - điểm thả bưu kiện bí mật | `2.04#9`–`#10` |
| 20 | `t5_gloves_forensic_desk` | Đôi găng tay da đen và các công cụ tỉ mỉ, kiên nhẫn không để lại dấu vân | `2.05#1`–`#4` |
| 21 | `t5_air_force_service_era` | Kỷ vật 4 năm Không quân Mỹ và bằng cử nhân Quản trị tư pháp | `2.06#1`–`#2` |
| 22 | `t5_rader_house_park_city` | Ngôi nhà 6220 Independence tại Park City - vỏ bọc gia đình mẫu mực | `2.06#3` |
| 23 | `t5_lutheran_church_exterior` | Nhà thờ Lutheran Chúa Kitô (Christ Lutheran Church) tôn nghiêm | `2.06#4` |
| 24 | `t5_church_council_altar` | Bục giảng và bàn thờ nhà thờ - nơi Chủ tịch hội đồng phụng sự | `2.06#5` |
| 25 | `t5_scout_camp_campfire` | Đống lửa trại hướng đạo sinh Cub Scout - người thầy dạy thắt dây thừng | `2.06#6` |
| 26 | `t5_compliance_measuring_tape` | Thước dây đo chiều cao bãi cỏ và tập biên bản xử phạt của Park City | `2.06#7` |
| 27 | `t5_two_faces_silhouette` | Sự tương phản ghê rợn giữa công dân mẫu mực ban ngày và quái vật ban đêm | `2.07#1`–`#4` |

### HỒI 3 · GIẢI PHẪU TÂM LÝ — BÊN TRONG BỘ NÃO ÁI KỶ ÁC TÍNH (10:30 – 16:45)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 28 | `t5_compartmentalization_cabinet` | Ẩn dụ Sự phân mảnh tâm trí tuyệt đối: chiếc tủ cổ với nhiều ngăn khóa kín | `3.02#1`–`#3` |
| 29 | `t5_concrete_wall_divide` | Bức tường bê tông vô hình ngăn cách cuộc sống gia đình và hưng tưởng tội ác | `3.02#4`–`#5` |
| 30 | `t5_factor_x_shadow` | Ảo tưởng "Nhân tố X" (Factor X) - bóng ma ký sinh thao túng tâm trí | `3.02#6`–`#7`, `3.04#1`–`#3` |
| 31 | `t5_projection_mask` | Cơ chế Phóng chiếu và Ngụy biện: mặt nạ vô tội rũ bỏ trách nhiệm đạo đức | `3.05#1`–`#3` |
| 32 | `t5_family_dinner_warmth` | Bàn ăn tối gia đình đầm ấm đối nghịch với tội ác tàn nhẫn | `3.05#4`–`#5` |
| 33 | `t5_narcissistic_throne` | Ẩn dụ Ái kỷ ác tính & Cơn nghiện được chú ý: chiếc ghế bành dưới ánh đèn độc tôn | `3.06#1`–`#3`, `3.07#1`–`#2` |
| 34 | `t5_secret_scrapbook` | Cuốn sổ tay lưu niệm bí mật dán đầy các bài báo về chính mình | `3.07#3`–`#4` |
| 35 | `t5_fear_of_oblivion` | Nỗi sợ bị lãng quên của kẻ ái kỷ còn lớn hơn cả bản năng sợ vào tù | `3.07#5`–`#7` |
| 36 | `t5_hubris_chessboard` | Bàn cờ vua: sự tự phụ mù quáng của quân cờ tự cho mình toàn năng | `3.08#1`–`#3` |

### HỒI 4 · ĐẤU TRÍ THẨM VẤN & BẪY CÔNG NGHỆ ĐĨA MỀM (16:45 – 21:45)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 37 | `t5_winter_home_depot` | Bãi đỗ xe Home Depot Wichita giữa mùa đông giá buốt | `4.02#1`–`#4` |
| 38 | `t5_cereal_box_pickup` | Hộp ngũ cốc đặt trên thùng xe bán tải chứa mẩu giấy định mệnh | `4.02#5` |
| 39 | `t5_handwritten_note_floppy` | Mẩu giấy viết tay hỏi cảnh sát: *"Có thể giao tiếp bằng đĩa mềm không?"* | `4.02#6`–`#9` |
| 40 | `t5_newspaper_classified_494` | Mục rao vặt 494 báo The Wichita Eagle: *"Rex, it will be OK"* | `4.04#1`–`#5` |
| 41 | `t5_ksas_tv_station` | Đài truyền hình KSAS-TV tiếp nhận bưu phẩm chứa đĩa mềm | `4.04#6`–`#7` |
| 42 | `t5_purple_floppy_disk` | Chiếc đĩa mềm Memorex 1.44MB màu tím đặt trên bàn giám định | `4.04#8` |
| 43 | `t5_digital_forensics_lab` | Phòng pháp y kỹ thuật số quét dữ liệu bằng phần mềm EnCase | `4.06#1`–`#2` |
| 44 | `t5_metadata_screen` | Màn hình hiển thị thuộc tính siêu dữ liệu (Metadata): Dennis & Christ Lutheran Church | `4.06#3`–`#6` |
| 45 | `t5_church_website_search` | Tra cứu website nhà thờ: Chủ tịch Hội đồng Dennis Rader | `4.08#1`–`#3` |
| 46 | `t5_traffic_camera_pickup` | Camera an ninh ghi nhận chiếc xe bán tải đen khớp với các điểm gửi thư | `4.08#4`–`#5` |
| 47 | `t5_dna_pap_smear_vial` | Mẫu tế bào y tế Pap smear của con gái Kerri xác nhận ADN huyết thống 100% | `4.08#6`–`#9` |
| 48 | `t5_highway_takedown_arrest` | Đoàn xe cảnh sát chặn đầu bắt giữ Rader khi đang lái xe về nhà ăn trưa | `4.10#1`–`#4` |
| 49 | `t5_interrogation_confrontation` | Cuộc đối chất trong phòng thẩm vấn: *"Tại sao anh lại nói dối tôi?"* | `4.12#1`–`#4` |
| 50 | `t5_shattered_mask_confession` | Chiếc mặt nạ vỡ vụn, 30 giờ đồng hồ khai cung không ngớt | `4.12#5`–`#8` |
| 51 | `t5_kerri_rawson_tears` | Nỗi đau của con gái Kerri Rawson: tuổi thơ sụp đổ trước sự thật man rợ | `4.14#1`–`#2`, `4.15#1`–`#4` |

### HỒI 5 · PHÁN QUYẾT, BÀI HỌC CẢNH BÁO ĐỎ & LỜI KẾT (21:45 – 26:30)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 52 | `t5_sedgwick_courtroom` | Tòa án Quận Sedgwick uy nghiêm ngày tuyên án 18/08/2005 | `5.02#1`–`#2` |
| 53 | `t5_judge_gavel_verdict` | Tiếng búa công lý tuyên phạt 10 án chung thân liên tiếp (175 năm) | `5.02#3` |
| 54 | `t5_el_dorado_prison` | Nhà tù El Dorado Correctional Facility giữa vùng đồng bằng Kansas | `5.02#4`–`#5` |
| 55 | `t5_solitary_confinement_cell` | Buồng giam biệt lập xi măng xám lạnh - sự trừng phạt của im lặng vĩnh viễn | `5.04#1`–`#2` |
| 56 | `t5_redflag_rule_control` | Cảnh báo đỏ 1: Sự ám ảnh kiểm soát quy tắc cực đoan | `5.05#1`–`#3` |
| 57 | `t5_redflag_shallow_affect` | Cảnh báo đỏ 2: Sự tách biệt cảm xúc đằng sau vẻ ngoài nhiệt thành | `5.05#4`–`#5` |
| 58 | `t5_redflag_secret_trophies` | Cảnh báo đỏ 3: Thói quen bí mật lưu trữ vật dụng của người khác | `5.06#1`–`#3` |
| 59 | `t5_redflag_narcissistic_hubris` | Cảnh báo đỏ 4: Nhu cầu ái kỷ khao khát được công nhận bằng mọi giá | `5.06#4`–`#5` |
| 60 | `t5_justice_dawn_sunlight` | Ánh bình minh rọi trên chiếc đĩa mềm tím và hồ sơ đã đóng lại | `5.08#1`–`#5` |
| 61 | `t5_closing_typewriter_rose` | Máy đánh chữ tĩnh lặng bên nhành hoa hồng trắng khép lại tập 05 | `5.10#1`–`#3` |

---

## B3. Thống kê & Kiểm soát chất lượng (QC)

- **Tổng số ảnh:** 61 ảnh mới 100%.
- **Độ phân giải:** 2112 × 1188 (chuẩn 16:9 2K).
- **Tuân thủ quy tắc V5:** 100% người thật chỉ hiện bóng lưng / khuất mặt hoàn toàn.
- **Tuân thủ quy tắc V9:** 100% không máu me, không thi thể, không vết thương bạo lực.
- **Tuân thủ quy tắc V1 - V3:** Đổi hình đúng mốc câu thoại, không nhảy hình giữa chừng câu nói.
- **Bảo toàn phong cách:** Phong cách Dark graphic novel noir đồng bộ tuyệt đối với các tập trước của kênh Amber Eyes.
