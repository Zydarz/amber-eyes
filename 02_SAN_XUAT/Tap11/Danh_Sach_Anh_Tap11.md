# DANH SÁCH ẢNH NỀN — TẬP 11 "CẶP ĐÔI KEN & BARBIE"

*Hồ sơ Paul Bernardo & Karla Homolka — Hội Chứng Điên Cuồng Đôi (Folie à Deux) & 'Thỏa Thuận Với Quỷ Dữ'. Ngày 23/10/2026.*

---

## B1. Thông tin bộ ảnh

| Mục | Nội dung |
|---|---|
| Số ảnh chuẩn hóa | **70** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |
| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |
| Vị trí lưu trữ | `assets/bg/t11_*.png` — **tiền tố `t11_` bắt buộc** để không trùng bộ nền Tập 01–10 |
| Danh sách prompt gốc | `.work/bg_jobs_tap11.json` & `.work/gemini_image_prompts_tap11.json` |
| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |
| Phong cách nghệ thuật | Dark graphic novel noir — nét mực đen đậm, chiaroscuro đối lập cao, bảng màu hổ phách/hồng tro/slate/lạnh, hạt phim cổ điển |
| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |
| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (Amber Eyes Noir Graphic Renderer — 100% tự chủ) |

**Quy tắc hình ảnh của kênh (V1 – V9):**

- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**
  - `t11_paul_bernardo_dashing_car`: Bóng người đàn ông lịch lãm bên xe thể thao dưới đèn đường ngoại ô.
  - `t11_karla_veterinary_clinic`: Bóng cô gái áo blouse trắng chăm sóc thú y bên cửa sổ nắng.
  - `t11_society_gala_inseparable_couple`: Bóng đôi vợ chồng trẻ khiêu vũ quấn quýt trong dạ tiệc.
  - `t11_interrogation_bruised_facade`: Bóng người phụ nữ gục đầu khóc trong văn phòng luật sư.
  - `t11_holding_video_camera_director`: Bóng bàn tay cầm máy quay 8mm chỉ đạo hào hứng.
  - `t11_joliette_prison_gate_release`: Bóng người phụ nữ bước ra cổng trại Joliette giữa rừng ống kính.
  - `t11_light_of_justice_prevails`: Ngọn đèn công lý xua tan bóng tối và những giọt nước mắt cá sấu.
- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.
- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:**
  - Tuyệt đối không mô tả bạo lực tình dục, nhục hình hay tổn thương thể xác trực diện của các nạn nhân (Leslie Mahaffy, Kristen French, Tammy Homolka).
  - Các chứng cứ (ngôi nhà màu hồng số 57 Bayview, đèn pin kim loại, ADN Scarborough, 6 cuộn băng 8mm trên trần nhà, hồ sơ thỏa thuận nhận tội, báo cáo Thẩm phán Galligan) thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.

---

## B2. Ánh xạ ảnh → hồi → mốc câu

Mốc câu theo `.work/script_tap11.json` (parse từ `01_KICH_BAN/Tap11/kichban_tap11_23102026.md`):  
**33 lượt thoại · 165 câu · 4.347 từ** (Host 83 câu, Điều tra viên 37 câu, Chuyên gia tâm lý 30 câu, Người bình thường 15 câu).

### HỒI 1 · VỎ BỌC HOÀN HẢO CỦA 'CẶP ĐÔI KEN & BARBIE' (00:00 – 05:30)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 01 | `t11_pink_house_57_bayview` | Ngôi nhà màu hồng số 57 Đại lộ Bayview Drive tại thị trấn ven hồ Port Dalhousie trong nắng mai thập niên 1990. | `1.02#1` |
| 02 | `t11_suburban_admiration_facade` | Khu dân cư trung lưu thanh bình ven hồ Ontario với những hàng cây rợp bóng và ánh nhìn ngưỡng mộ của xóm giềng. | `1.02#2` |
| 03 | `t11_paul_bernardo_dashing_car` | Bóng người đàn ông lịch lãm trong bộ âu phục bên chiếc xe thể thao bóng loáng dưới ánh đèn đường ngoại ô. | `1.02#3` |
| 04 | `t11_narcissistic_mirror_vanity` | Góc nhìn phòng thay đồ sang trọng, lược chải tóc mạ vàng và chiếc gương phản chiếu bóng lưng chải chuốt kiêu hãnh. | `1.02#4` |
| 05 | `t11_karla_veterinary_clinic` | Bóng cô gái trẻ trong chiếc áo blouse trắng tại phòng khám thú y bên khung cửa sổ ngập nắng ấm áp. | `1.02#5` |
| 06 | `t11_ken_barbie_golden_illusion` | Hai con búp bê biểu tượng Ken và Barbie đặt trên bệ kính phủ rèm nhung, ánh sáng vàng óng ả nhưng bóng đổ dài ma quái. | `1.02#6` |
| 07 | `t11_fairytale_wedding_carriage` | Cỗ xe ngựa trắng và hàng trăm đóa hoa hồng trong đám cưới mùa hè 1991, khung cảnh cổ tích huyền ảo. | `1.04#1` |
| 08 | `t11_society_gala_inseparable_couple` | Bóng đôi vợ chồng trẻ quấn quýt bên nhau trong dạ tiệc khiêu vũ, tâm điểm của sự trầm trồ ngưỡng mộ. | `1.04#2` |
| 09 | `t11_blind_adoration_shadow` | Bóng người phụ nữ cúi mình trước ngai vàng quyền lực đen tối trong phòng khách mờ ảo, sự tôn sùng mù quáng. | `1.04#3–#4` |
| 10 | `t11_closed_pink_door_abyss` | Cánh cửa sơn hồng đóng kín hé lộ khe tối sâu thẳm bên trong, tương phản giữa vẻ ngoài kẹo ngọt và vực thẳm tội ác. | `1.04#5–#6` |
| 11 | `t11_lakeside_evening_dog_walk` | Bờ hồ Ontario bảng lảng chiều tà, bóng cặp đôi tay trong tay dắt hai chú chó đi dạo bên sóng nước dập dềnh. | `1.05#1–#2` |
| 12 | `t11_backyard_barbecue_lawn` | Bữa tiệc nướng sân sau với khói lam chiều ấm cúng, bàn ăn ngoài trời phủ hoa cỏ của khu phố kiểu mẫu. | `1.05#3–#4` |
| 13 | `t11_lace_curtain_window_illusion` | Khung cửa sổ rèm hoa vintage thắt nơ tinh tế, ánh đèn ấm cúng che giấu chiếc mặt nạ lừa dối cả cộng đồng. | `1.05#5–#6` |
| 14 | `t11_scarborough_nocturnal_shadow` | Vùng ngoại ô Scarborough chìm trong màn sương đêm lạnh lẽo, bóng đen đột nhập lén lút qua rèm cửa sổ. | `1.07#1–#3` |
| 15 | `t11_scarborough_taskforce_archive` | Bàn điều tra chuyên án đặc nhiệm Scarborough với bản đồ ghim cờ đỏ dán tường và hồ sơ truy tìm không dấu vân tay. | `1.08#1–#2` |
| 16 | `t11_lake_gibson_fog_depths` | Vùng hồ Lake Gibson âm u trong làn sương mù sớm, bóng mặt nước phẳng lặng che giấu đáy hồ sâu thẳm. | `1.08#3–#4` |
| 17 | `t11_church_parking_lot_ambush` | Bãi đỗ xe nhà thờ St. Catharines vắng lặng trong cơn mưa chiều tháng 4, chiếc cặp nữ sinh rơi bên lề đường. | `1.08#5–#7` |
| 18 | `t11_map_proximity_dark_crossroads` | Bản đồ khu vực Niagara với vòng tròn khoanh đỏ nối ngôi nhà số 57 Bayview với các địa điểm chấn động, bóng đen bao trùm. | `1.09#1–#5` |

### HỒI 2 · CHIẾC MẶT NẠ RƠI XUỐNG VÀ THỎA THUẬN VỚI QUỶ DỮ (05:30 – 11:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 19 | `t11_flashlight_shattered_hallway` | Chiếc đèn pin kim loại cỡ lớn rơi trên sàn gỗ hành lang giữa những mảnh vỡ đồ đạc, vết nứt đầu tiên của cặp đôi vàng. | `2.02#1–#3` |
| 20 | `t11_st_catharines_hospital_night` | Bệnh viện St. Catharines trong đêm mưa gió, ánh đèn cấp cứu đỏ hắt qua vũng nước loang trên mặt đường. | `2.04#1–#2` |
| 21 | `t11_escape_to_parents_porch` | Ngôi nhà cha mẹ đẻ trong đêm đông lạnh giá, chiếc valy vội vã để lại bậc thềm trước khi bước vào nương náu. | `2.04#3` |
| 22 | `t11_february_arrest_dna_match` | Mẫu tinh thể DNA và kính hiển vi phòng thí nghiệm pháp y đối chiếu với hồ sơ bắt giữ Paul Bernardo ngày 17/02/1993. | `2.04#4–#5` |
| 23 | `t11_interrogation_bruised_facade` | Bóng người phụ nữ gục đầu trong văn phòng luật sư với khăn tay đẫm nước mắt, tạo dựng hình ảnh nạn nhân đáng thương. | `2.05#1–#3` |
| 24 | `t11_pleading_victim_tears` | Góc nhìn cận cảnh chiếc khăn tay thấm nước mắt bên tách trà nguội trên bàn thẩm vấn, vở kịch vô tội hoàn hảo. | `2.05#4–#6` |
| 25 | `t11_battered_woman_syndrome_file` | Tập hồ sơ chẩn đoán 'Hội chứng Người phụ nữ bị Bạo hành' với bút phê của chuyên gia tâm thần học. | `2.06#1–#3` |
| 26 | `t11_hostage_puppet_facade` | Bức tranh ẩn dụ bóng người phụ nữ bị xiềng xích vô hình, tấm lá chắn pháp lý che đậy sự đồng lõa ác tính. | `2.06#4–#5` |
| 27 | `t11_fragile_beauty_manipulation` | Chiếc mặt nạ thạch cao thiên thần trắng muốt nứt rạn đặt trên nền bàn gỗ đen, biểu tượng sự thao túng lòng trắc ẩn. | `2.07#1–#2` |
| 28 | `t11_weaponized_victim_playing` | Cán cân công lý bị nghiêng lệch bởi những giọt nước mắt giả tạo, đỉnh cao của kỹ thuật thao túng đóng vai nạn nhân. | `2.07#3–#5` |
| 29 | `t11_missing_evidence_dilemma` | Bàn làm việc của điều tra viên với những tập hồ sơ còn thiếu bằng chứng then chốt, áp lực nghẹt thở của thời gian. | `2.08#1–#2` |
| 30 | `t11_prosecution_clock_pressure` | Chiếc đồng hồ cát và những dòng tít báo chí dồn dập, cơ quan công tố đánh mất sự cẩn trọng nghề nghiệp. | `2.08#3–#5` |
| 31 | `t11_deal_with_the_devil_contract` | Bản thỏa thuận nhận tội tháng 05/1993 ký giữa Tổng chưởng lý và Karla Homolka, bản án 12 năm đổi lấy lời khai. | `2.09#1–#3` |

### HỒI 3 · GIẢI MÃ HỘI CHỨNG ĐIÊN CUỒNG ĐÔI (FOLIE À DEUX) (11:00 – 16:30)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 32 | `t11_half_truth_dossier_shadow` | Tập hồ sơ lời khai mở ra một nửa dưới bóng tối chiếc đèn bàn, hé lộ bức màn tâm thần học ma quái. | `3.02#1–#3` |
| 33 | `t11_folie_a_deux_resonance` | Hai chiếc bóng đối xứng giao thoa trong buồng cộng hưởng xoắn ốc ma mị, biểu tượng Hội chứng Điên cuồng đôi. | `3.03#1–#2` |
| 34 | `t11_destructive_flame_alliance` | Ngọn lửa đen bùng cháy từ hai nhánh bấc quyện vào nhau, sự khuếch đại tội ác xóa bỏ mọi ranh giới lương tri. | `3.03#3–#5` |
| 35 | `t11_malignant_narcissist_throne` | Chiếc ngai vàng đen tối trong tâm trí kẻ ái kỷ cuồng quyền lực, bóng bàn tay muốn thống trị sinh mạng đồng loại. | `3.04#1–#3` |
| 36 | `t11_obedient_accomplice_strings` | Những sợi dây rối vô hình gắn kết giữa hai kẻ lệch lạc, mối quan hệ cộng sinh độc hại. | `3.04#4` |
| 37 | `t11_covert_sociopath_profile` | Sơ đồ giải phẫu tâm thần học bộc lộ chứng thái nhân cách ngầm và sự thiếu hụt hoàn toàn cảm giác tội lỗi. | `3.05#1–#2` |
| 38 | `t11_morbid_thrill_abyss` | Cửa sổ phòng ngủ nhìn ra màn đêm thăm thẳm, sự kích thích trước quyền lực tàn bạo và nỗi sợ hãi bệnh lý bị bỏ rơi. | `3.05#3–#4` |
| 39 | `t11_toxic_devotion_cruelty` | Chiếc nhẫn cưới bằng thép gai đặt cạnh hoa khô tàn úa, biểu tượng lòng trung thành mù quáng và tàn nhẫn. | `3.05#5–#6` |
| 40 | `t11_christmas_1990_halothane_bottle` | Lọ thuốc mê Halothane đánh cắp từ phòng khám thú y đặt cạnh ly rượu Giáng sinh 1990 tại tư gia Homolka. | `3.06#1–#3` |
| 41 | `t11_silent_christmas_tragedy` | Cây thông Noel mờ ảo trong phòng khách vắng lặng sau cơn bi kịch ngạt thở của cô em gái mười lăm tuổi. | `3.06#4` |
| 42 | `t11_chilling_polaroid_camera` | Chiếc máy ảnh chụp lấy liền Polaroid nằm trên mặt bàn bên găng tay cao su, sự máu lạnh tột cùng phản bội máu mủ. | `3.06#5–#7` |
| 43 | `t11_grieving_parents_wedding_mask` | Bức ảnh cưới lộng lẫy đặt cạnh di ảnh người em gái trong cùng một ngôi nhà, sự dối trá đến gai người. | `3.07#1–#3` |
| 44 | `t11_unholy_sacrament_altar` | Bàn thờ tình yêu biến thái bị bao bọc trong bóng tối, nơi mọi lương tri bị thiêu rụi bởi thứ tôn giáo tội ác. | `3.08#1–#4` |
| 45 | `t11_frozen_justice_gavel` | Chiếc búa công lý bị đóng băng dưới lớp tuyết lạnh Ontario, trước khi bước ngoặt định mệnh xuất hiện. | `3.09#1–#3` |

### HỒI 4 · SÁU CUỐN BĂNG TRÊN TRẦN NHÀ VÀ SỰ SỤP ĐỔ CỦA MỘT ẢO TƯỞNG (16:30 – 21:30)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 46 | `t11_six_8mm_tapes_bag` | Chiếc túi vải chứa sáu cuộn băng video 8mm định mệnh được luật sư John Rosen bàn giao cho cảnh sát mùa thu 1994. | `4.02#1–#2` |
| 47 | `t11_bathroom_ceiling_vent_hiding` | Chiếc quạt thông gió trần phòng tắm hé mở, để lộ hốc bí mật nơi sáu cuộn băng bị che giấu suốt nhiều năm. | `4.03#1–#2` |
| 48 | `t11_ken_murray_obstruction_charge` | Bàn làm việc luật sư với ngăn kéo khóa kín cất giấu tang vật 17 tháng và cáo trạng cản trở công lý. | `4.03#3–#5` |
| 49 | `t11_dark_screening_room_projector` | Chùm sáng từ máy chiếu 8mm cắt ngang căn phòng tối, bóng các điều tra viên ngồi chết lặng trước màn hình. | `4.04#1–#3` |
| 50 | `t11_investigator_nausea_monitor` | Góc nhìn từ sau lưng nhân viên điều tra run rẩy nhìn vào màn hình CRT phát sáng trong đêm, sự thật trần trụi. | `4.05#1–#3` |
| 51 | `t11_holding_video_camera_director` | Bóng bàn tay cầm chiếc máy quay phim gia đình 8mm, kẻ chỉ đạo chủ động và hào hứng trong tội ác. | `4.05#4–#5` |
| 52 | `t11_triumphant_smile_deal_with_devil` | Ánh sáng màn hình phản chiếu bản thỏa thuận nhận tội bị xé toạc trong tâm tưởng, nỗi cay đắng của công lý. | `4.05#6–#9` |
| 53 | `t11_equal_partner_in_cruelty` | Hai chiếc ghế ngang hàng trong phòng thu bằng chứng, phơi bày quan hệ đối tác bình đẳng và khoái cảm quyền lực đen tối. | `4.07#1–#3` |
| 54 | `t11_mockery_of_justice_tears` | Chiếc mặt nạ kịch nghệ vỡ vụn trên bục nhân chứng, những giọt nước mắt tại tòa chỉ là màn diễn xuất vị kỷ. | `4.07#4–#5` |
| 55 | `t11_outraged_citizens_protest` | Biển người biểu tình mang biểu ngữ đòi công lý cho Leslie Mahaffy và Kristen French trước tòa nhà Quốc hội Ontario. | `4.08#1–#3` |
| 56 | `t11_constitutional_legal_deadlock` | Cuốn sách luật hiến pháp và chiếc còng số tám bị khóa chặt, cái bẫy tư pháp không lối thoát bảo vệ kẻ thủ ác. | `4.09#1–#3` |
| 57 | `t11_dangerous_offender_life_sentence` | Bản án chung thân không ân xá và dấu mộc 'Dangerous Offender' giam giữ vô thời hạn Paul Bernardo tại nhà tù Kingston. | `4.10#1–#2` |
| 58 | `t11_calendar_counting_to_freedom` | Tờ lịch nhà tù với những ô ngày bị gạch chéo, người đàn bà trong ngôi nhà màu hồng đếm ngược ngày về tự do. | `4.10#3` |

### HỒI 5 · BÀI HỌC ĐẮT GIÁ VỀ MẶT NẠ NẠN NHÂN & LỜI CẢNH TỈNH (21:30 – 26:30)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 59 | `t11_joliette_prison_gate_release` | Cánh cổng sắt Trại cải tạo Nữ Joliette mở ra ngày 04/07/2005, bóng người phụ nữ bước ra giữa rừng ống kính truyền thông. | `5.02#1–#3` |
| 60 | `t11_haunted_new_identity_shadow` | Hộ chiếu mang tên mới Leanne Teale đặt trên mặt bàn, nhưng bóng đen quá khứ vẫn phủ kín không thể xóa nhòa. | `5.02#4–#6` |
| 61 | `t11_galligan_inquiry_report_reforms` | Báo cáo thẩm tra độc lập của Thẩm phán Patrick Galligan năm 1996, cuộc cải cách triệt để quy trình thương lượng nhận tội. | `5.03#1–#4` |
| 62 | `t11_victim_playing_camouflage_mirror` | Tấm gương hai mặt: một bên là giọt nước mắt mong manh, một bên là móng vuốt của kẻ săn mồi đội lốt nạn nhân. | `5.04#1–#3` |
| 63 | `t11_disguised_predator_scales` | Cán cân phân định giữa nạn nhân chân chính và kẻ săn mồi mang mặt nạ yếu đuối, sự cảnh tỉnh nghiêm khắc. | `5.04#4–#5` |
| 64 | `t11_amber_eyes_redflag_intro` | Biểu tượng Amber Eyes rực sáng trên nền đen huyền bí, dẫn nhập 4 dấu hiệu cảnh báo đỏ nhận diện kẻ thao túng. | `5.05#1` |
| 65 | `t11_redflag1_evading_accountability` | Dấu hiệu cảnh báo 1: Chiếc khiên tổn thương dùng để cản phá mọi chất vấn pháp lý và né tránh trách nhiệm. | `5.05#2–#4` |
| 66 | `t11_redflag2_words_vs_actions_split` | Dấu hiệu cảnh báo 2: Sự phân đôi giữa lời nói ngọt ngào trước đám đông và hành vi lạnh lùng toan tính trong bóng tối. | `5.05#5–#7` |
| 67 | `t11_redflag3_guilt_tripping_trap` | Dấu hiệu cảnh báo 3: Chiếc bẫy cảm giác tội lỗi giăng ra để bẻ gãy mọi sự nghi ngờ chính đáng của người khác. | `5.05#8–#10` |
| 68 | `t11_redflag4_toxic_symbiosis_abyss` | Dấu hiệu cảnh báo 4: Vực thẳm của mối quan hệ cộng sinh độc hại, nơi tình yêu bị đánh đổi bằng việc hủy hoại lương tri. | `5.05#11–#13` |
| 69 | `t11_light_of_justice_prevails` | Ngọn đèn bão công lý bừng sáng đẩy lùi bóng tối ma quỷ, chân lý lương tri chiến thắng những giọt nước mắt cá sấu. | `5.05#14` |
| 70 | `t11_amber_eyes_closing_dossier_bernardo` | Tập hồ sơ Amber Eyes khép lại trang nghiêm trên bàn gỗ sồi, biểu tượng mắt cú hổ phách mạ vàng bừng sáng, lời chào tạm biệt Tập 11. | `5.05#15–#17` |

---

## B3. Thống kê & Kiểm soát chất lượng (QC)

- **Tổng số ảnh:** 70 ảnh mới 100%.
- **Độ phân giải:** 2112 × 1188 (chuẩn 16:9 2K).
- **Tuân thủ quy tắc V5:** 100% người thật chỉ hiện bóng lưng / khuất mặt hoàn toàn.
- **Tuân thủ quy tắc V9:** 100% không bạo lực, tập trung vào công lý, phân tích tâm lý học và tư liệu lịch sử.
- **Tuân thủ quy tắc V1 - V3:** Đổi hình đúng mốc câu thoại, không nhảy hình giữa chừng câu nói.
- **Bảo toàn phong cách:** Phong cách Dark graphic novel noir đồng bộ tuyệt đối với các tập trước của kênh Amber Eyes.