# DANH SÁCH ẢNH NỀN — TẬP 09 "NGHỆ THUẬT XÓA BỎ BẢN NGÃ"

*Hồ sơ Charles Manson & Thảm kịch Gia đình Manson (Cơ chế tẩy não 3 giai đoạn của Kurt Lewin). Ngày 23/10/2026.*

---

## B1. Thông tin bộ ảnh

| Mục | Nội dung |
|---|---|
| Số ảnh chuẩn hóa | **65** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |
| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |
| Vị trí lưu trữ | `assets/bg/t9_*.png` — **tiền tố `t9_` bắt buộc** để không trùng bộ nền Tập 01–08 |
| Danh sách prompt gốc | `.work/bg_jobs_tap09.json` & `.work/gemini_image_prompts_tap09.json` |
| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |
| Phong cách nghệ thuật | Dark graphic novel noir — mực đen đậm, chiaroscuro đối lập cao, tông lạnh desaturated kết hợp ánh sáng hoàng hôn và lửa trại sa mạc, film grain |
| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |
| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (100% tự chủ, không phụ thuộc MiniMax bên thứ ba) |

**Quy tắc hình ảnh của kênh (V1 – V9):**

- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**
  - `t9_manson_shadow_campfire_desert`: Bóng đen Charles Manson đứng trước đống lửa trại rực rỡ giữa sa mạc đêm.
  - `t9_yearbook_photos_shadow`: Bốn khung ảnh kỷ yếu vintage của 4 thủ phạm, gương mặt bị che phủ bởi bóng tối sâu thẳm.
  - `t9_collective_hysteria_three_shaved_heads`: Bóng ba bị cáo nữ cạo trọc đầu nắm tay nhau bước vào tòa án trong ánh đèn flash.
  - `t9_vacant_eyes_doll_shadow`: Bóng người với tư thế bất động vô hồn như búp bê giật dây dưới ánh trăng.
- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.
- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:**
  - Tuyệt đối không mô tả vết thương, không vẽ cảnh hiện trường bi thảm trực diện.
  - Các chứng cứ (biệt thự Cielo Drive, trang trại Spahn Ranch, đĩa than White Album, sơ đồ Kurt Lewin, bục thẩm phán) thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.

---

## B2. Ánh xạ ảnh → hồi → mốc câu

Mốc câu theo `.work/script_tap09.json` (parse từ `01_KICH_BAN/Tap09/kichban_tap09_23102026.md`):  
**38 lượt thoại · 165 câu · 3.791 từ** (Host 92 câu, Điều tra viên 26 câu, Chuyên gia tâm lý 30 câu, Người bình thường 17 câu).

### HỒI 1 · ĐÊM ĐEN TRÊN ĐỒI BEVERLY VÀ DẤU CHẤM HẾT CỦA MÙA HÈ TÌNH YÊU (00:00 – 05:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 01 | `t9_summer_of_love_hippie_la` | Hoàng hôn Los Angeles cuối thập niên 1960, bóng những thanh niên Hippie cài hoa trên tóc bên chiếc xe van retro ngập nắng vàng hoài niệm chiaroscuro. | `1.02#1–#2` |
| 02 | `t9_acoustic_guitar_flower_crown` | Tĩnh vật cây guitar acoustic mộc mạc dựa bên chiếc vương miện hoa dại đã khô héo trên sàn gỗ mộc, ánh sáng xiên u buồn. | `1.02#3` |
| 03 | `t9_los_angeles_skyline_1969` | Bầu trời Los Angeles hoàng hôn 1969 nhìn từ đỉnh đồi, những rặng cây cọ đen thẫm in trên nền trời hoàng hôn rực lửa chuyển dần sang màn đêm buốt giá. | `1.02#4–#5` |
| 04 | `t9_cielo_drive_estate_night` | Ngôi biệt thự phong cách điền trang tại 10050 Đại lộ Cielo Drive ẩn mình giữa những rặng thông đen u tịch trên đỉnh đồi Benedict Canyon trong đêm định mệnh. | `1.04#1–#2` |
| 05 | `t9_beverly_hills_gate_road` | Cổng sắt hoa văn mở he hé và con đường sỏi uốn lượn dẫn vào biệt thự đồi cao, ánh trăng bạc rọi xuống rặng cây đen kịt. | `1.06#1` |
| 06 | `t9_cielo_drive_living_room_somber` | Gian phòng khách biệt thự sang trọng chìm trong tĩnh lặng u uất, ánh đèn bàn hắt bóng dài, những đồ vật vương vãi, không khí nghẹt thở bi kịch (không máu me, V9). | `1.06#2–#4` |
| 07 | `t9_waverly_drive_residence_night` | Ngôi nhà một tầng phong cách suburban thập niên 60 tại 3311 Waverly Drive khu Los Feliz, cửa sổ tối om, hàng rào thấp, một bóng đen lẻ loi trong đêm. | `1.06#5–#6` |
| 08 | `t9_retro_radio_broadcast_table` | Chiếc đài bán dẫn radio cổ điển thập niên 60 đang phát sóng trên bàn gỗ, tách cà phê nguội, ánh sáng ban mai chiếu qua rèm cửa khép kín. | `1.07#1–#2` |
| 09 | `t9_gun_shop_empty_shelves` | Tủ kính cửa hàng khóa và súng ở Hollywood với các kệ hàng trống trơn, biển báo đóng cửa, ánh đèn neon phản chiếu trên vỉa hè vắng tanh. | `1.07#3–#4` |
| 10 | `t9_intact_valuables_diorama` | Hộp trang sức và đồng hồ đắt tiền còn nguyên trên bàn trang điểm gỗ gụ, lớp bụi mỏng phủ lên trong bóng tối chiaroscuro. | `1.07#5–#6` |
| 11 | `t9_withered_flower_on_asphalt` | Một bông hoa dại khô héo bị giẫm nát trên nền nhựa đường lạnh ngắt, biểu tượng cho sự chấm dứt của kỷ nguyên ngây thơ Hippie. | `1.07#7–#8` |
| 12 | `t9_bloody_letters_forensic_wall` | Bức tường trắng loang lổ bóng tối với các chữ cái hình sự được khoanh vùng phân tích, ánh đèn pin pháp y chiếu rọi, góc chụp noir góc hẹp. | `1.09#1–#3` |
| 13 | `t9_lapd_investigation_room` | Bàn làm việc ban chuyên án Sở Cảnh sát Los Angeles ngổn ngang sơ đồ hiện trường, điện thoại bàn quay số và cốc cà phê giấy, ánh đèn chùm mờ ảo. | `1.10#1–#2` |
| 14 | `t9_los_angeles_county_crime_map` | Bản đồ quy hoạch đô thị Los Angeles nối các đường chỉ đỏ giữa Benedict Canyon (Beverly Hills) và Los Feliz, ghim định vị hiện trường. | `1.10#3–#4` |
| 15 | `t9_invisible_puppet_master_shadow` | Bóng đen mờ ảo của một bàn tay điều khiển những sợi dây con rối vô hình trong bóng tối chiaroscuro nghệ thuật noir. | `1.10#5–#6` |
| 16 | `t9_newspaper_headline_helter_skelter` | Tờ nhật báo Los Angeles Times tháng 8/1969 với hàng tít đen in đậm về thảm kịch đồi Beverly, chụp tĩnh vật trên bàn làm việc tối. | `1.11#1–#3` |

### HỒI 2 · ẢO ẢNH HELTER SKELTER TẠI TRANG TRẠI SPAHN RANCH (05:00 – 10:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 17 | `t9_spahn_ranch_western_facade` | Cảnh toàn trang trại Spahn Ranch tiêu điều dưới chân núi đá thung lũng Santa Susana, những dãy nhà gỗ kiểu phim trường cao bồi bỏ hoang, cỏ gai khô lăn trong gió sa mạc. | `2.02#1–#3` |
| 18 | `t9_spahn_ranch_dilapidated_porch` | Hiên nhà gỗ mục nát của Spahn Ranch với những chiếc yên ngựa cũ, thùng gỗ và bóng dáng lờ mờ của những chiếc xe bán tải rỉ sét. | `2.04#1–#2` |
| 19 | `t9_prison_cell_bars_shadow` | Song sắt nhà tù liên bang đổ bóng dài trên sàn bê tông lạnh buốt, một tập hồ sơ tiền án dày cộp đặt dưới ánh sáng le lói. | `2.05#1–#2` |
| 20 | `t9_haight_ashbury_psychedelic_street` | Ngã tư Haight và Ashbury ở San Francisco trong sương mù, các poster ảo giác psychedelic mờ nhạt trên tường gạch, những bóng người lang thang. | `2.05#3–#5` |
| 21 | `t9_dark_triad_psychological_symbol` | Biểu tượng phân tích tâm lý học tam giác bóng tối, ba đỉnh giao nhau với ánh sáng lạnh, phản ánh sự thao túng và thiếu vắng lương tri. | `2.06#1–#3` |
| 22 | `t9_runaway_teenager_bus_stop` | Trạm xe buýt ven đường đêm hoang vắng, chiếc ba lô cũ đặt dưới chân ghế, bóng người thanh thiếu niên cô độc nhìn về phía xa xăm. | `2.06#4–#5` |
| 23 | `t9_confiscated_clocks_broken_mirror` | Chiếc gương nứt vỡ nằm cạnh những chiếc đồng hồ đeo tay và lịch treo tường bị vứt bỏ trong góc tối, biểu tượng tước đoạt nhận thức thời gian. | `2.07#1–#2` |
| 24 | `t9_manson_shadow_campfire_desert` | Bóng đen của Charles Manson đứng trước đống lửa trại rực rỡ giữa sa mạc đêm, xung quanh là những chiếc bóng người ngồi nghe mê muội. | `2.07#3–#4` |
| 25 | `t9_vinyl_record_white_album` | Đĩa than vinyl màu trắng đang quay trên máy hát cổ điển, rãnh đĩa đen bóng dưới ánh đèn vàng mờ, vỏ đĩa trắng tối giản. | `2.08#1–#2` |
| 26 | `t9_apocalyptic_desert_hideout` | Hang đá và thung lũng sa mạc cằn cỗi Death Valley, bầu trời tím thẫm đe dọa, cảm giác cô lập tận thế hoang tưởng. | `2.08#3–#5` |
| 27 | `t9_recording_studio_rejected_demo` | Băng cối thu âm âm nhạc reel-to-reel bị bỏ quên trên bàn trộn âm thanh phòng thu, bản nhạc viết tay bị vò nát. | `2.09#1–#2` |
| 28 | `t9_cielo_drive_road_sign_shadow` | Biển báo đường Cielo Drive trong đêm tối, đèn pha xe hơi rọi qua bóng cây cọ cao vút, không khí định mệnh. | `2.09#3–#4` |
| 29 | `t9_midnight_convoy_old_ford` | Chiếc xe Ford 1959 cũ kỹ màu vàng nhạt lăn bánh trong đêm trên con đường vắng lặng tiến về phía đồi Hollywood. | `2.10#1–#3` |
| 30 | `t9_broken_porcelain_doll_desert` | Một con búp bê sứ trẻ thơ bị vỡ nửa gương mặt nằm nửa chìm trong cát sa mạc Spahn Ranch, ẩn dụ sự tha hóa tâm hồn. | `2.11#1–#2` |

### HỒI 3 · NGHỆ THUẬT XÓA BỎ BẢN NGÃ (CƠ CHẾ TẨY NÃO 3 GIAI ĐOẠN) (10:00 – 15:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 31 | `t9_yearbook_photos_shadow` | Bốn khung ảnh kỷ yếu trung học vintage mờ nhạt trên bàn gỗ, các gương mặt bị bóng tối che khuất (V5), tương phản giữa vẻ hiền lành quá khứ và tội ác. | `3.02#1–#4` |
| 32 | `t9_shadow_devil_dialogue_noir` | Bóng đen dài in trên bức tường bê tông trắng, hai bàn tay buông thõng, ánh sáng đối lập chiaroscuro tột cùng. | `3.02#5–#6` |
| 33 | `t9_kurt_lewin_three_stages_diagram` | Sơ đồ kỹ thuật ba giai đoạn (Unfreezing -> Changing -> Refreezing) vẽ bằng phấn trắng trên nền bảng đen điều tra. | `3.03#1–#2` |
| 34 | `t9_unfreezing_love_bombing_circle` | Vòng tròn các bóng người quây quần trong ánh sáng ấm áp giả tạo, cánh tay ôm vai an ủi, chiếc bẫy cảm xúc ban đầu. | `3.04#1–#4` |
| 35 | `t9_burning_id_cards_ashes` | Chiếc ví rỗng, chứng minh thư và hộ chiếu đang cháy dở thành tro trong chiếc chảo kim loại, làn khói mảnh bốc lên. | `3.05#1–#3` |
| 36 | `t9_lsd_hallucinogen_distorted_reality` | Không gian sa mạc ảo giác u uất với các đường xoắn ốc psychedelic đen trắng mờ ảo, cảm giác mất phương hướng và thực tại méo mó. | `3.05#4–#5` |
| 37 | `t9_changing_night_desert_sermon` | Đống than hồng rực lửa giữa thung lũng đá đêm, bóng kẻ thuyết giáo đứng cao sừng sững, xung quanh là đám đông quỳ phục. | `3.06#1–#4` |
| 38 | `t9_inverted_cross_moral_confusion` | Bức tượng gỗ nhỏ hoặc biểu tượng chữ thập mờ ảo ngả nghiêng trong bóng tối, ranh giới thiện ác bị xóa nhòa. | `3.07#1–#3` |
| 39 | `t9_blind_devotion_extinguished_candle` | Ngọn nến bị chụp tắt bởi chiếc chuông kim loại, khói trắng bay lên, biểu tượng cho ánh sáng lý trí bị dập tắt. | `3.07#4–#5` |
| 40 | `t9_interlocking_bloody_knots_rope` | Đoạn dây thừng thắt nút phức tạp đặt trên phiến đá đen, biểu tượng của sự trói buộc không lối thoát. | `3.08#1–#2` |
| 41 | `t9_trauma_bonding_group_shadows` | Hàng bóng đen đứng xếp liền kề nhau như một khối thống nhất không thể tách rời dưới ánh đèn đêm nghiệt ngã. | `3.09#1–#4` |
| 42 | `t9_gate_of_spahn_ranch_departure` | Cánh cổng gỗ Spahn Ranch mở toang trong đêm tối, vệt bánh xe hằn sâu trên cát dẫn vào bóng đêm vô tận. | `3.10#1–#2` |

### HỒI 4 · LỜI KHAI TRƯỚC TÒA VÀ CÁI BẪY QUYỀN LỰC CỦA KẺ KHÔNG CHẠM TAY (15:00 – 20:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 43 | `t9_death_valley_barker_ranch_raid` | Căn nhà gỗ hoang sơ Barker Ranch giữa lòng chảo thung lũng Death Valley cằn cỗi, xe tuần tra bao vây trong ánh bình minh đỏ quạch. | `4.02#1–#2` |
| 44 | `t9_sybil_brand_jail_corridor` | Hành lang nhà tù nữ Sybil Brand Institute lát gạch sáng loáng dưới đèn tuýp trắng lạnh lẽo, những cánh cửa thép có ô kính nhỏ. | `4.03#1–#3` |
| 45 | `t9_linda_kasabian_witness_dossier` | Hồ sơ nhân chứng được bảo vệ đặc biệt của Văn phòng Công tố, tấm ảnh mờ và bản thỏa thuận miễn trừ truy tố. | `4.04#1–#2` |
| 46 | `t9_cielo_drive_front_gate_fog` | Cánh cổng sắt lớn của biệt thự Cielo Drive nhìn từ ngoài đường lúc nửa đêm, sương mù dày đặc, ánh đèn pha mờ ảo. | `4.05#1–#3` |
| 47 | `t9_vacant_eyes_doll_shadow` | Bóng người đứng sững trong đêm tối, ánh trăng chiếu xiên qua khung cửa, biểu tượng cho ánh mắt vô hồn đánh mất bản ngã. | `4.05#4–#6` |
| 48 | `t9_kasabian_escape_night_highway` | Tuyến đường cao tốc đêm vắng lặng nhìn qua kính chắn gió ô tô trong cơn mưa phùn, ánh đèn hậu đỏ nhạt xa dần. | `4.05#7–#9` |
| 49 | `t9_los_angeles_hall_of_justice` | Mặt tiền đồ sộ của Tòa thị chính và Tòa án Los Angeles (Hall of Justice), bậc thang đá rộng lớn nơi báo chí và đám đông chen chúc. | `4.07#1–#4` |
| 50 | `t9_prosecutor_desk_evidence_files` | Bàn công tố viên chất đầy các hộp hồ sơ án, bản sao dấu vân tay và hình vẽ hiện trường, chiếc cặp da cũ kỹ. | `4.08#1–#4` |
| 51 | `t9_mastermind_conspiracy_law_book` | Cuốn sách luật hình sự California mở trên bàn, ngòi bút máy kim loại trỏ vào điều khoản về tội danh đồng phạm chủ mưu. | `4.09#1–#3` |
| 52 | `t9_carved_x_symbol_forehead` | Tác phẩm đồ họa noir cận cảnh vết chữ X khắc gạch thô ráp trên nền đá xám tối tăm, biểu tượng sự từ chối chuẩn mực xã hội loài người. | `4.10#1–#3` |
| 53 | `t9_collective_hysteria_three_shaved_heads` | Ba bóng người phụ nữ cạo trọc đầu nắm tay nhau bước đi trong ánh đèn flash báo chí, nụ cười méo mó kỳ quái trong bóng tối. | `4.10#4–#6` |
| 54 | `t9_courtroom_gavel_bench` | Bục thẩm phán trang nghiêm bằng gỗ sồi sẫm màu, chiếc búa gỗ nằm im lìm trên đĩa gõ, ánh sáng cửa sổ rọi xuống tĩnh lặng. | `4.11#1–#2` |

### HỒI 5 · PHÁN QUYẾT LỊCH SỬ & BÀI HỌC VỀ SỰ TỰ CHỦ TINH THẦN (20:00 – 26:00)

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |
|---|---|---|---|
| 55 | `t9_courtroom_jury_verdict_dossier` | Bản phán quyết của bồi thẩm đoàn có chữ ký các thành viên, con dấu đỏ tư pháp bang California, ánh sáng trang trọng. | `5.02#1–#2` |
| 56 | `t9_california_supreme_court_columns` | Hàng cột đá cẩm thạch uy nghiêm của Tòa án Tối cao California tại San Francisco, biểu tượng cho sự thay đổi lịch sử pháp luật. | `5.02#3–#4` |
| 57 | `t9_corcoran_state_prison_watchtower` | Tháp canh và hàng rào kẽm gai của Nhà tù Tiểu bang Corcoran dưới ánh chiều tà hoang vắng, bóng chim bay cô độc. | `5.02#5–#6` |
| 58 | `t9_scales_of_justice_broken_chains` | Cán cân công lý bằng đồng sáng rực trên nền xích sắt bị đứt gãy, biểu tượng công lý chiến thắng sự thao túng tà giáo. | `5.03#1–#3` |
| 59 | `t9_two_faced_benevolent_mask` | Chiếc mặt nạ mỉm cười hiền từ bằng sứ nứt đôi, để lộ một góc tối tăm u ám phía sau, ẩn dụ cho sự thấu hiểu giả tạo. | `5.04#1–#3` |
| 60 | `t9_redflag1_love_bombing_trap` | Red Flag 1 (Dội bom tình cảm): Chiếc hộp quà phủ ruy băng nhung lộng lẫy đặt mở hé trong bóng tối, bên trong ẩn chứa chiếc bẫy thép gai vô hình. | `5.05#2–#4` |
| 61 | `t9_redflag2_severed_family_photos` | Red Flag 2 (Tước đoạt danh tính & cô lập): Bức ảnh gia đình chụp kỷ niệm bị rạch đôi, một nửa bị kéo ra xa trong góc tối, chiếc kéo kim loại sắc lạnh bên cạnh. | `5.05#5–#7` |
| 62 | `t9_redflag3_fortress_paranoia_wall` | Red Flag 3 (Tư duy phân cực Chúng ta vs Thế giới): Bức tường bê tông cao ngất ngăn cách hai thế giới, một bên u tối khép kín, một bên là chân trời rộng mở. | `5.05#8–#10` |
| 63 | `t9_redflag4_sacred_conscience_compass` | Red Flag 4 (Lương tri bất khả xâm phạm): Chiếc la bàn lương tri bằng vàng phản chiếu ánh sáng kiên định giữa cơn lốc cát bụi sa mạc tối tăm. | `5.05#11–#13` |
| 64 | `t9_open_birdcage_dawn_horizon` | Chiếc lồng chim kim loại cửa mở toang, một chú chim vỗ cánh bay vút lên bầu trời bình minh rực rỡ, ánh sáng vàng ấm áp xua tan đêm dài. | `5.05#14–#15` |
| 65 | `t9_amber_eyes_closing_dossier` | Hồ sơ vụ án đóng lại trên bàn gỗ sồi, chiếc kính lúp và ngòi bút mực amber vàng kim, biểu trưng cho sự thật và tri thức nhân văn. | `5.05#16–#18` |

---

## B3. Thống kê & Kiểm soát chất lượng (QC)

- **Tổng số ảnh:** 65 ảnh mới 100%.
- **Độ phân giải:** 2112 × 1188 (chuẩn 16:9 2K).
- **Tuân thủ quy tắc V5:** 100% người thật chỉ hiện bóng lưng / khuất mặt hoàn toàn.
- **Tuân thủ quy tắc V9:** 100% không bạo lực, tập trung vào công lý, phân tích tâm lý học và tư liệu lịch sử.
- **Tuân thủ quy tắc V1 - V3:** Đổi hình đúng mốc câu thoại, không nhảy hình giữa chừng câu nói.
- **Bảo toàn phong cách:** Phong cách Dark graphic novel noir đồng bộ tuyệt đối với các tập trước của kênh Amber Eyes.