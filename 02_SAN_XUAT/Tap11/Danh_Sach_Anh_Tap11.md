# DANH SÁCH ẢNH NỀN — TẬP 11 "CẶP ĐÔI KEN & BARBIE"

*Hồ sơ Paul Bernardo & Karla Homolka — Hội Chứng Điên Cuồng Đôi (Folie à Deux) & 'Thỏa Thuận Với Quỷ Dữ'.*

**Cập nhật 16/11/2026 — bộ nền tách theo H25 (sinh ảnh theo SHOT, 1,5–2 shot/nền).**

---

## B1. Thông tin bộ ảnh

| Mục | Nội dung |
|---|---|
| Số ảnh nền | **136 ảnh** phục vụ trọn vẹn 5 hồi |
| Số shot | **271 shot** (223 dòng bảng shot, gồm 4 thẻ chuyển hồi T10 + 1 thẻ kết T2) — 2100 s |
| Mật độ nền | **1.99 shot/nền** (mục tiêu H25: 1,5–2) · **0** nền vượt 3 shot/30 s (H22) |
| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |
| Vị trí lưu trữ | `assets/bg/t11_*.png` — **tiền tố `t11_` bắt buộc** để không trùng bộ nền Tập 01–10 |
| Danh sách prompt gốc | `.work/bg_jobs_tap11.json` (136 job = 66 mã cũ + 70 mã mới) |
| Sổ nguồn gốc tài sản | `provenance.json` (L7) |
| Công cụ sinh ảnh | **Kaggle GPU · FLUX.2-klein-4B** — Deep Noir 4 tầng, LANCZOS 2K, dìm màu 35 % · vignette · grain 35 mm. **KHÔNG dùng Real-ESRGAN** (`QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` §1.2) |
| Nguyên tắc H17 / A8.1 | Nền là **tài sản dùng chung cho MỌI ngôn ngữ** — không hậu tố `_EN/_JA/_KO`, chữ luôn do Pillow vẽ lúc dựng |
| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 · người thật chỉ hiện bóng · không vẽ nạn nhân |

**Quy tắc hình ảnh của kênh (V1 – V9):**

- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn.**
- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.
- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:** tuyệt đối không mô tả bạo lực, thương tích hay thi thể của các nạn nhân (Leslie Mahaffy, Kristen French, Tammy Homolka).
- **H2/H5 — Nền sạch chữ 100 %:** mọi chữ trên hình do Pillow vẽ lúc dựng; nền có chữ lạ phải sinh lại đúng tên.
- **H19 — Nền phải có nội dung cảnh:** đọc tên nền phải ra một cảnh cụ thể; nền chỉ là gradient/ánh sáng thì vô dụng.

---

## B2. Ánh xạ ảnh → hồi → mốc câu

Mỗi mã nền = **một cảnh riêng**; các shot liền mạch cùng một khoảnh khắc được gom chung mã, còn dùng lại cùng nơi ở khoảng cách xa thì **phải là cảnh khác** (đổi góc / giờ / bố cục) nên tách mã riêng.

### HỒI 1 · VỎ BỌC HOÀN HẢO CỦA CẶP ĐÔI KEN & BARBIE

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu | Shot dùng |
|---|---|---|---|---|
| 01 | `t11_pink_house_57_bayview` | Ngôi nhà màu hồng số 57 Đại lộ Bayview Drive tại thị trấn ven hồ Port Dalhousie trong nắng mai thập niên 1990. | 1.03#1 · 1.03#2 | 1-01 · 1-02 (20.9 s) |
| 02 | `t11_suburban_admiration_facade` | Khu dân cư trung lưu thanh bình ven hồ Ontario với những hàng cây rợp bóng và ánh nhìn ngưỡng mộ của xóm giềng. | 1.03#3 · 1.07#4 | 1-03 · 1-19 (21.8 s) |
| 03 | `t11_paul_bernardo_dashing_car` | Bóng người đàn ông lịch lãm trong bộ âu phục bên chiếc xe thể thao bóng loáng dưới ánh đèn đường ngoại ô. | 1.03#4 | 1-04 (10.2 s) |
| 04 | `t11_karla_veterinary_clinic` | Bóng cô gái trẻ trong chiếc áo blouse trắng tại phòng khám thú y bên khung cửa sổ ngập nắng ấm áp. | 1.03#5 | 1-05 (7.8 s) |
| 05 | `t11_ken_barbie_golden_illusion` | Hai con búp bê biểu tượng Ken và Barbie đặt trên bệ kính phủ rèm nhung, ánh sáng vàng óng ả nhưng bóng đổ dài ma quái. | 1.03#6 | 1-06 (12.3 s) |
| 06 | `t11_fairytale_wedding_carriage` | Cỗ xe ngựa trắng và hàng trăm đóa hoa hồng trong đám cưới mùa hè 1991, khung cảnh cổ tích huyền ảo. | 1.05#1 · 1.08#4 | 1-07 · 1-23 (20.6 s) |
| 07 | `t11_society_gala_inseparable_couple` | Bóng đôi vợ chồng trẻ quấn quýt bên nhau trong dạ tiệc khiêu vũ, tâm điểm của sự trầm trồ ngưỡng mộ. | 1.05#2 | 1-08 (9.2 s) |
| 08 | `t11_blind_adoration_shadow` | Bóng người phụ nữ cúi mình trước ngai vàng quyền lực đen tối trong phòng khách mờ ảo, sự tôn sùng mù quáng. | 1.05#3 · 4.07#4 | 1-09 · 4-21 (19.5 s) |
| 09 | `t11_narcissistic_mirror_vanity` | Góc nhìn phòng thay đồ sang trọng, lược chải tóc mạ vàng và chiếc gương phản chiếu bóng lưng chải chuốt kiêu hãnh. | 1.05#4 · 3.06#13 | 1-10 · 3-32 (15.7 s) |
| 10 | `t11_closed_pink_door_abyss` | Cánh cửa sơn hồng đóng kín hé lộ khe tối sâu thẳm bên trong, tương phản giữa vẻ ngoài kẹo ngọt và vực thẳm tội ác. | 1.05#5 · 5.07#3 | 1-11 · 5-25 (12.5 s) |
| 11 | `t11_lakeside_evening_dog_walk` | Bờ hồ Ontario bảng lảng chiều tà, bóng cặp đôi tay trong tay dắt hai chú chó đi dạo bên sóng nước dập dềnh. | 1.06#1 · 1.06#2 | 1-12 · 1-13 (12.4 s) |
| 12 | `t11_backyard_barbecue_lawn` | Bữa tiệc nướng sân sau với khói lam chiều ấm cúng, bàn ăn ngoài trời phủ hoa cỏ của khu phố kiểu mẫu. | 1.06#3 · 5.04#5 | 1-14 · 5-12 (20.3 s) |
| 13 | `t11_lace_curtain_window_illusion` | Khung cửa sổ rèm hoa vintage thắt nơ tinh tế, ánh đèn ấm cúng che giấu chiếc mặt nạ lừa dối cả cộng đồng. | 1.06#4 · 2.09#10 | 1-15 · 2-44 (18.5 s) |
| 14 | `t11_pink_house_winter_dusk` | Cùng ngôi nhà màu hồng nhưng giữa chiều đông buồn, cửa sổ tắt và tuyết bắt đầu rơi. | 1.07#1 · 1.13#5 | 1-16 · 1-39 (17.9 s) |
| 15 | `t11_expert_desk_lamp` | Bàn chuyên gia chỉ một chiếc đèn bàn, hồ sơ đóng và quân cờ đứng lặng. | 1.07#2 · 3.05#5 | 1-17 · 3-19 (13.1 s) |
| 16 | `t11_ideal_couple_veil_gold` | Cặp đôi trẻ trong lớp mạ vàng ảo tưởng của buổi tiệc xã hội, ánh sáng vàng nhạt phủ lên vật liệu. | 1.07#3 · 1.13#4 | 1-18 · 1-38 (16.7 s) |
| 17 | `t11_niagara_lakeshore_fog_night` | Bờ hồ Ontario đêm với hai vệt lốt xe song song dẫn vào rừng tối trong sương dày. | 1.08#1 · 1.12#6 | 1-20 · 1-34 (15.3 s) |
| 18 | `t11_bus_stop_night_desolation` | Trạm xe buýt vắng tanh lúc đêm ở ngoại ô Scarborough, đèn đường hắt bóng dài trên mặt đường ướt. | 1.08#2 · 1.10#5 | 1-21 · 1-28 (14.1 s) |
| 19 | `t11_empty_crossroads_searchlight` | Ngã tư đường ngoại ô lúc đêm không một ai, chỉ một cây đèn trời đơn đội hắt vệt sáng. | 1.08#3 · 1.13#3 | 1-22 · 1-37 (13.7 s) |
| 20 | `t11_scarborough_nocturnal_shadow` | Vùng ngoại ô Scarborough chìm trong màn sương đêm lạnh lẽo, bóng đen đột nhập lén lút qua rèm cửa sổ. | 1.10#1 · 1.10#2 | 1-24 · 1-25 (19.0 s) |
| 21 | `t11_scarborough_taskforce_archive` | Bàn điều tra chuyên án đặc nhiệm Scarborough với bản đồ ghim cờ đỏ dán tường và hồ sơ truy tìm không dấu vân tay. | 1.10#3 · 1.10#4 | 1-26 · 1-27 (20.8 s) |
| 22 | `t11_church_parking_lot_ambush` | Bãi đỗ xe nhà thờ St. Catharines vắng lặng trong cơn mưa chiều tháng 4, chiếc cặp nữ sinh rơi bên lề đường. | 1.12#1 · 1.12#2 | 1-29 · 1-30 (18.5 s) |
| 23 | `t11_burlington_house_dusk_empty` | Ngôi nhà ngoại ô ở Burlington lúc chiều muộn, hiên trống và cổng khoá, không một bóng người. | 1.12#3 | 1-31 (10.4 s) |
| 24 | `t11_lake_gibson_fog_depths` | Vùng hồ Lake Gibson âm u trong làn sương mù sớm, bóng mặt nước phẳng lặng che giấu đáy hồ sâu thẳm. | 1.12#4 · 1.12#5 | 1-32 · 1-33 (19.2 s) |
| 25 | `t11_map_proximity_dark_crossroads` | Bản đồ khu vực Niagara với vòng tròn khoanh đỏ nối ngôi nhà số 57 Bayview với các địa điểm chấn động, bóng đen bao trùm. | 1.13#1 · 1.13#2 | 1-35 · 1-36 (14.8 s) |
| 26 | `t11_neighbourhood_winter_evening` | Khu phố ven hồ trong chiều đông, đèn nhà bật qua màn tuyết và những con đường vắng. | 1.13#6 · 5.04#6 | 1-40 · 5-13 (9.8 s) |
| 27 | `t11_amber_eyes_redflag_intro` | Biểu tượng Amber Eyes rực sáng trên nền đen huyền bí, dẫn nhập 4 dấu hiệu cảnh báo đỏ nhận diện kẻ thao túng. | 1.15#1 · 1.15#2 | 1-41 · 1-42 (14.3 s) |
| 28 | `t11_closed_dossier_desk` | Bàn làm việc tối với hồ sơ bìa đen đóng lại, chỉ một vệt sáng mỏng chiếu xuống. | 1.15#3 · 4.08#5 | 1-43 · 4-31 (21.9 s) |
| 29 | `t11_folie_a_deux_resonance` | Hai chiếc bóng đối xứng giao thoa trong buồng cộng hưởng xoắn ốc ma mị, biểu tượng Hội chứng Điên cuồng đôi. | 1.15#4 | 1-44 (9.1 s) |
| 30 | `t11_amber_eyes_closing_dossier_bernardo` | Tập hồ sơ Amber Eyes khép lại trang nghiêm trên bàn gỗ sồi, biểu tượng mắt cú hổ phách mạ vàng bừng sáng, lời chào tạm biệt Tập 11. | 1.15#5 · 1.15#6 | 1-45 · 1-46 (13.8 s) |

### HỒI 2 · HIỆN TRƯỜNG & VỰC THẲM LEO THANG — 4 NẤC THANG TỘI ÁC

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu | Shot dùng |
|---|---|---|---|---|
| 31 | `t11_marsh_hunting_ground_night` | Vùng đầm lầy ngoại ô ban đêm, cây gỗ trụi và nước đọng phản chiếu ánh sáng lạnh. | 2.02#1 · 2.02#2 | 2-01 · 2-02 (17.4 s) |
| 32 | `t11_destructive_flame_alliance` | Ngọn lửa đen bùng cháy từ hai nhánh bấc quyện vào nhau, sự khuếch đại tội ác xóa bỏ mọi ranh giới lương tri. | 2.02#3 · 2.02#4 | 2-03 · 2-04 (17.8 s) |
| 33 | `t11_four_floor_stairwell_shadow` | Cầu thang bê tông bốn tầng của nhà cũ, bóng đổ dài trên tường và bóng đèn trần trơ trọi. | 2.02#5 · 2.02#6 | 2-05 · 2-06 (12.3 s) |
| 34 | `t11_investigation_board_four_stages` | Bảng ghim điều tra với bốn tấm ảnh tối và sợi chỉ đỏ nối bốn giai đoạn. | 2.04#1 | 2-07 (6.6 s) |
| 35 | `t11_scarborough_night_street_lurking` | Con đường ngoại ô Scarborough về đêm, dãy đèn vàng và những chiếc xe đậu im lìm trong sương. | 2.04#2 · 2.04#3 | 2-08 · 2-09 (15.1 s) |
| 36 | `t11_christmas_1990_halothane_bottle` | Lọ thuốc mê Halothane đánh cắp từ phòng khám thú y đặt cạnh ly rượu Giáng sinh 1990 tại tư gia Homolka. | 2.04#4 · 2.04#5 | 2-10 · 2-11 (23.3 s) |
| 37 | `t11_bayview_basement_concrete` | Tầng hầm bê tông dưới ngôi nhà số 57 Bayview, cửa sổ nhỏ cao và một chiếc ghế kim loại. | 2.04#6 · 2.04#7 | 2-12 · 2-13 (16.2 s) |
| 38 | `t11_church_parking_daytime_abduction` | Bãi xe nhà thờ Saint Catharines giữa ban ngày xám xịt, hàng xe đậu vắng tanh. | 2.04#8 · 2.04#9 | 2-14 · 2-15 (15.5 s) |
| 39 | `t11_lake_gibson_culvert_darkness` | Kênh đào bê tông dưới lòng đất nơi tang vật bị giấu, nước đục và một tia sáng xám từ trên cao. | 2.04#10 · 2.04#11 | 2-16 · 2-17 (14.4 s) |
| 40 | `t11_equal_partner_in_cruelty` | Hai chiếc ghế ngang hàng trong phòng thu bằng chứng, phơi bày quan hệ đối tác bình đẳng và khoái cảm quyền lực đen tối. | 2.04#12 | 2-18 (5.9 s) |
| 41 | `t11_silent_christmas_tragedy` | Cây thông Noel mờ ảo trong phòng khách vắng lặng sau cơn bi kịch ngạt thở của cô em gái mười lăm tuổi. | 2.06#1 · 2.06#2 · 3.06#9 | 2-19 · 2-20 · 3-28 (24.4 s) |
| 42 | `t11_frozen_justice_gavel` | Chiếc búa công lý bị đóng băng dưới lớp tuyết lạnh Ontario, trước khi bước ngoặt định mệnh xuất hiện. | 2.06#3 · 2.06#4 | 2-21 · 2-22 (16.7 s) |
| 43 | `t11_snowbound_patrol_road` | Con đường tỉnh phủ tuyết trắng xoá, lốt xe mới và một chiếc xe tuần tra đứng lặng lẽ. | 2.06#5 | 2-23 (7.7 s) |
| 44 | `t11_light_of_justice_prevails` | Ngọn đèn bão công lý bừng sáng đẩy lùi bóng tối ma quỷ, chân lý lương tri chiến thắng những giọt nước mắt cá sấu. | 2.06#6 · 5.08#11 · 5.08#12 | 2-24 · 5-48 · 5-49 (21.2 s) |
| 45 | `t11_quiet_window_closing` | Cửa sổ lặng tĩnh lúc xanh dương, bậu cửa trống và ánh đèn thị trấn xa nhòe mờ. | 2.06#10 · 2.06#7 · 5.10#9 | 2-25 · 2-28 · 5-58 (21.1 s) |
| 46 | `t11_empty_chair_black_ribbon` | Chiếc ghế trống buộc ruy băng đen trong căn phòng bỏ hoang, ánh sáng xám từ cửa sổ. | 2.06#8 · 3.06#3 | 2-26 · 3-22 (16.8 s) |
| 47 | `t11_february_arrest_dna_match` | Mẫu tinh thể DNA và kính hiển vi phòng thí nghiệm pháp y đối chiếu với hồ sơ bắt giữ Paul Bernardo ngày 17/02/1993. | 2.06#9 · 2.12#4 · 2.12#5 | 2-27 · 2-53 · 2-54 (22.3 s) |
| 48 | `t11_flashlight_shattered_hallway` | Chiếc đèn pin kim loại cỡ lớn rơi trên sàn gỗ hành lang giữa những mảnh vỡ đồ đạc, vết nứt đầu tiên của cặp đôi vàng. | 2.07#1 · 2.07#2 | 2-29 · 2-30 (11.5 s) |
| 49 | `t11_two_dossier_folders_desk` | Hai thư mục hồ sơ đen trên bàn thép lạnh, tách bạch hai hướng điều tra. | 2.07#3 · 4.06#5 · 4.08#1 | 2-31 · 4-18 · 4-27 (15.7 s) |
| 50 | `t11_chilling_polaroid_camera` | Chiếc máy ảnh chụp lấy liền Polaroid nằm trên mặt bàn bên găng tay cao su, sự máu lạnh tột cùng phản bội máu mủ. | 2.07#4 · 2.07#5 | 2-32 · 2-33 (13.5 s) |
| 51 | `t11_handheld_camera_lens` | Ống kính máy quay cầm tay cũ trong bóng tối, phản chiếu mờ một căn phòng trống. | 2.07#6 · 2.09#7 | 2-34 · 2-41 (16.2 s) |
| 52 | `t11_holding_video_camera_director` | Bóng bàn tay cầm chiếc máy quay phim gia đình 8mm, kẻ chỉ đạo chủ động và hào hứng trong tội ác. | 2.09#1 · 2.09#2 | 2-35 · 2-36 (12.5 s) |
| 53 | `t11_tripod_camera_dark_room` | Máy quay video trên tripod trong căn phòng tối trơ trọi, ánh sáng lọt qua khe cửa. | 2.09#3 · 2.09#8 | 2-37 · 2-42 (12.6 s) |
| 54 | `t11_morbid_thrill_abyss` | Cửa sổ phòng ngủ nhìn ra màn đêm thăm thẳm, sự kích thích trước quyền lực tàn bạo và nỗi sợ hãi bệnh lý bị bỏ rơi. | 2.09#4 · 2.09#5 | 2-38 · 2-39 (12.5 s) |
| 55 | `t11_videotape_reels_stack` | Những cuộn băng video cũ xếp chồng trên mặt bàn gỗ bụi bặm, nắng lạnh từ cửa sổ. | 2.09#6 · 2.09#9 | 2-40 · 2-43 (15.3 s) |
| 56 | `t11_curtained_window_closed_room` | Phòng khách về đêm nhìn về phía cửa sổ rèm ren, một bóng người mờ ảo trên tường. | 2.10#1 · 2.10#2 | 2-45 · 2-46 (16.8 s) |
| 57 | `t11_coupled_shadows_mirror` | Hai chiếc ghế trống đối diện nhau dưới tấm gương lớn, bóng tối phản chiếu lặp lại. | 2.10#3 · 2.10#4 | 2-47 · 2-48 (14.7 s) |
| 58 | `t11_consultation_room_two_chairs` | Phòng tư vấn trống, hai ghế đối diện và một cửa sổ lạnh lẽo. | 2.10#5 · 3.06#10 | 2-49 · 3-29 (11.9 s) |
| 59 | `t11_st_catharines_hospital_night` | Bệnh viện St. Catharines trong đêm mưa gió, ánh đèn cấp cứu đỏ hắt qua vũng nước loang trên mặt đường. | 2.12#1 · 2.12#2 | 2-50 · 2-51 (14.7 s) |
| 60 | `t11_evidence_bags_lab_bench` | Túi niêm phong bằng chứng trên bàn thép phòng thí nghiệm, ánh sáng huỳnh quang lạnh. | 2.12#3 | 2-52 (5.3 s) |
| 61 | `t11_cold_calculation_desk` | Bàn tính toán lạnh lùng: tờ giấy trắng, bút chì và máy tính dưới đèn một bóng. | 2.12#6 · 3.06#14 | 2-55 · 3-33 (13.8 s) |

### HỒI 3 · GIẢI MÃ LIÊN MINH BỆNH HOẠN — ĐIÊN CUỒNG ĐÔI & TRUNG HÒA ĐẠO ĐỨC

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu | Shot dùng |
|---|---|---|---|---|
| 62 | `t11_unanswered_question_corridor` | Hành lang vắng với một cánh cửa mở toả ra vệt sáng lạnh trên nền bê tông. | 3.02#1 · 3.02#2 | 3-01 · 3-02 (16.0 s) |
| 63 | `t11_hostage_puppet_facade` | Bức tranh ẩn dụ bóng người phụ nữ bị xiềng xích vô hình, tấm lá chắn pháp lý che đậy sự đồng lõa ác tính. | 3.02#3 · 3.02#4 | 3-03 · 3-04 (13.2 s) |
| 64 | `t11_half_truth_dossier_shadow` | Tập hồ sơ lời khai mở ra một nửa dưới bóng tối chiếc đèn bàn, hé lộ bức màn tâm thần học ma quái. | 3.02#5 · 3.02#6 | 3-05 · 3-06 (14.5 s) |
| 65 | `t11_two_shadows_one_wall` | Hai bóng người chồng lên nhau trên tường bê tông từ một nguồn sáng duy nhất. | 3.04#1 · 3.04#2 | 3-07 · 3-08 (13.6 s) |
| 66 | `t11_malignant_narcissist_throne` | Chiếc ngai vàng đen tối trong tâm trí kẻ ái kỷ cuồng quyền lực, bóng bàn tay muốn thống trị sinh mạng đồng loại. | 3.04#3 · 3.04#4 | 3-09 · 3-10 (13.0 s) |
| 67 | `t11_covert_sociopath_profile` | Sơ đồ giải phẫu tâm thần học bộc lộ chứng thái nhân cách ngầm và sự thiếu hụt hoàn toàn cảm giác tội lỗi. | 3.04#5 · 3.04#6 | 3-11 · 3-12 (13.0 s) |
| 68 | `t11_dark_cinema_empty_seats` | Rạp chiếu phim bỏ trống, màn chiếu lạnh lẽo và bụi lơ lửng trong luồng đèn máy chiếu. | 3.04#7 · 3.04#8 | 3-13 · 3-14 (12.5 s) |
| 69 | `t11_unholy_sacrament_altar` | Bàn thờ tình yêu biến thái bị bao bọc trong bóng tối, nơi mọi lương tri bị thiêu rụi bởi thứ tôn giáo tội ác. | 3.05#1 · 3.05#2 | 3-15 · 3-16 (13.6 s) |
| 70 | `t11_christmas_snow_front_porch` | Hiên nhà phủ tuyết dịp Giáng Sinh, chỉ một bóng đèn vàng ấm trên cánh cửa lạnh. | 3.05#3 · 3.05#4 · 5.04#1 | 3-17 · 3-18 · 5-08 (22.4 s) |
| 71 | `t11_featureless_peg_dolls` | Hàng búp bê gỗ đồng dạng không nét mặt trong kho tối, một bóng đèn trần trơ trọi. | 3.06#1 · 3.06#2 | 3-20 · 3-21 (9.8 s) |
| 72 | `t11_grieving_parents_wedding_mask` | Bức ảnh cưới lộng lẫy đặt cạnh di ảnh người em gái trong cùng một ngôi nhà, sự dối trá đến gai người. | 3.06#4 · 3.06#5 · 5.04#2 | 3-23 · 3-24 · 5-09 (20.4 s) |
| 73 | `t11_divided_room_two_doors` | Căn phòng bị chia làm hai ngăn: một bên đồ gia dụng ấm, một bên trống trơn lạnh lẽo. | 3.06#6 · 3.06#7 | 3-25 · 3-26 (12.9 s) |
| 74 | `t11_moral_licence_blank_notes` | Mặt bàn nhà bếp với giấy gấp trống, tách trà nguội và chiếc thìa đặt cạnh nhau. | 3.06#8 · 4.07#1 | 3-27 · 4-19 (16.6 s) |
| 75 | `t11_steel_wall_lifeless` | Vách tường thép liền mạch trong không gian lạnh, chỉ ánh đèn trần phản chiếu mờ. | 3.06#11 · 5.02#6 | 3-30 · 5-06 (13.1 s) |
| 76 | `t11_composure_in_mirror` | Gương phòng tắm chỉ phản chiếu một bóng người bình tĩnh, mặt không có nét. | 3.06#12 · 4.13#6 | 3-31 · 4-53 (16.5 s) |
| 77 | `t11_cracked_mirror_hallway` | Hành lang hẹp có tấm gương nứt, ánh sáng lọt từ cánh cửa mở phía sau. | 3.08#1 · 3.08#2 | 3-34 · 3-35 (11.9 s) |
| 78 | `t11_flashlight_beam_floor` | Vệt sáng đèn pin quét trên nền bê tông trần, bụi lơ lửng trong tia sáng. | 3.08#3 | 3-36 (8.5 s) |
| 79 | `t11_escape_to_parents_porch` | Ngôi nhà cha mẹ đẻ trong đêm đông lạnh giá, chiếc valy vội vã để lại bậc thềm trước khi bước vào nương náu. | 3.08#4 · 3.08#5 | 3-37 · 3-38 (14.8 s) |
| 80 | `t11_police_raid_night_house` | Ngôi nhà bao vây đêm bởi những bóng người cảnh sát từ phía sau, đèn xe chiếu vào sân. | 3.08#6 · 3.08#7 | 3-39 · 3-40 (16.8 s) |
| 81 | `t11_escape_ladder_night` | Chiếc thang kim loại dựng qua tường bê tông cao giữa đêm, cỏ ướt và ánh trăng lạnh. | 3.08#8 | 3-41 (6.8 s) |
| 82 | `t11_interrogation_bruised_facade` | Bóng người phụ nữ gục đầu trong văn phòng luật sư với khăn tay đẫm nước mắt, tạo dựng hình ảnh nạn nhân đáng thương. | 3.09#1 · 3.09#2 | 3-42 · 3-43 (13.7 s) |
| 83 | `t11_pleading_victim_tears` | Góc nhìn cận cảnh chiếc khăn tay thấm nước mắt bên tách trà nguội trên bàn thẩm vấn, vở kịch vô tội hoàn hảo. | 3.09#3 · 4.06#1 | 3-44 · 4-15 (18.9 s) |
| 84 | `t11_weaponized_victim_playing` | Cán cân công lý bị nghiêng lệch bởi những giọt nước mắt giả tạo, đỉnh cao của kỹ thuật thao túng đóng vai nạn nhân. | 3.09#4 · 3.09#5 | 3-45 · 3-46 (11.5 s) |
| 85 | `t11_victim_playing_camouflage_mirror` | Tấm gương hai mặt: một bên là giọt nước mắt mong manh, một bên là móng vuốt của kẻ săn mồi đội lốt nạn nhân. | 3.11#1 · 3.11#2 · 4.06#4 | 3-47 · 3-48 · 4-17 (21.1 s) |
| 86 | `t11_press_scrum_silhouettes` | Cơn hỗn loạn phóng viên giơ máy quay, tất cả chỉ là bóng tối trong hành lang lạnh. | 3.11#3 · 3.11#4 | 3-49 · 3-50 (10.5 s) |

### HỒI 4 · THỎA THUẬN VỚI QUỶ DỮ & SỰ SỤP ĐỔ CỦA MẶT NẠ NẠN NHÂN

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu | Shot dùng |
|---|---|---|---|---|
| 87 | `t11_prosecution_clock_pressure` | Chiếc đồng hồ cát và những dòng tít báo chí dồn dập, cơ quan công tố đánh mất sự cẩn trọng nghề nghiệp. | 4.02#1 · 4.02#2 | 4-01 · 4-02 (22.9 s) |
| 88 | `t11_silent_interview_corridor` | Hành lang dài những cánh cửa thép khép kín, chỉ một ngọn đèn mờ ở cuối hành lang. | 4.02#3 · 4.06#2 · 4.08#3 | 4-03 · 4-16 · 4-29 (21.1 s) |
| 89 | `t11_testimony_figure_shadow` | Một người phụ nữ seen từ sau lưng ngồi ở bàn ký, mái tóc bắt sáng lạnh, mặt chìm hoàn toàn. | 4.02#4 · 4.02#5 · 4.07#8 | 4-04 · 4-05 · 4-25 (23.1 s) |
| 90 | `t11_folded_coat_empty_chair` | Chiếc áo khoác nhàu nằm trên ghế trống trong phòng ký lạnh, một bóng đèn treo ở trên. | 4.02#6 · 4.07#3 | 4-06 · 4-20 (19.7 s) |
| 91 | `t11_missing_evidence_dilemma` | Bàn làm việc của điều tra viên với những tập hồ sơ còn thiếu bằng chứng then chốt, áp lực nghẹt thở của thời gian. | 4.04#1 · 4.04#2 | 4-07 · 4-08 (19.3 s) |
| 92 | `t11_empty_evidence_box` | Hộp vật chứng rỗng mở toang trên nền nhà văn phòng lạnh, một bóng đèn trần trơ trọi. | 4.04#3 · 5.04#4 | 4-09 · 5-11 (16.9 s) |
| 93 | `t11_deal_with_the_devil_contract` | Bản thỏa thuận nhận tội tháng 05/1993 ký giữa Tổng chưởng lý và Karla Homolka, bản án 12 năm đổi lấy lời khai. | 4.04#4 · 4.04#5 | 4-10 · 4-11 (18.7 s) |
| 94 | `t11_sealed_document_folder` | Hồ sơ đóng dấu sáp nằm trên bàn gỗ dưới ánh đèn thấp, mặt ngoài trơn trống. | 4.04#6 · 4.07#7 | 4-12 · 4-24 (14.3 s) |
| 95 | `t11_triumphant_smile_deal_with_devil` | Ánh sáng màn hình phản chiếu bản thỏa thuận nhận tội bị xé toạc trong tâm tưởng, nỗi cay đắng của công lý. | 4.04#7 · 4.04#8 | 4-13 · 4-14 (15.3 s) |
| 96 | `t11_contract_table_shadow` | Tờ giấy trắng trơn trên bàn tối với bóng dài của một kẻ ngồi vô hình. | 4.07#5 · 4.11#5 | 4-22 · 4-47 (13.5 s) |
| 97 | `t11_untitled_letter_desk` | Bàn nhỏ trong buồng giam với mấy tờ giấy trắng và cây bút chì dưới song sắt. | 4.07#6 · 5.07#9 | 4-23 · 5-31 (18.7 s) |
| 98 | `t11_calendar_counting_to_freedom` | Tờ lịch nhà tù với những ô ngày bị gạch chéo, người đàn bà trong ngôi nhà màu hồng đếm ngược ngày về tự do. | 4.07#9 · 5.02#7 | 4-26 · 5-07 (13.9 s) |
| 99 | `t11_six_tapes_on_floor` | Sáu cuộn băng video xếp thành hàng trên sàn gỗ trần, ánh sáng xám từ cửa sổ. | 4.08#2 · 4.09#5 | 4-28 · 4-36 (16.5 s) |
| 100 | `t11_ken_murray_obstruction_charge` | Bàn làm việc luật sư với ngăn kéo khóa kín cất giấu tang vật 17 tháng và cáo trạng cản trở công lý. | 4.08#4 · 4.10#3 · 4.10#4 | 4-30 · 4-39 · 4-40 (20.3 s) |
| 101 | `t11_gavel_dark_bench` | Búa tòa nằm trên bàn gỗ tối của phòng thiết bị trống, một luồng sáng lạnh. | 4.09#1 · 4.09#2 · 5.04#3 | 4-32 · 4-33 · 5-10 (21.1 s) |
| 102 | `t11_six_8mm_tapes_bag` | Chiếc túi vải chứa sáu cuộn băng video 8mm định mệnh được luật sư John Rosen bàn giao cho cảnh sát mùa thu 1994. | 4.09#3 · 4.09#4 | 4-34 · 4-35 (20.3 s) |
| 103 | `t11_bathroom_ceiling_vent_hiding` | Chiếc quạt thông gió trần phòng tắm hé mở, để lộ hốc bí mật nơi sáu cuộn băng bị che giấu suốt nhiều năm. | 4.10#1 · 4.10#2 | 4-37 · 4-38 (18.6 s) |
| 104 | `t11_dark_screening_room_projector` | Chùm sáng từ máy chiếu 8mm cắt ngang căn phòng tối, bóng các điều tra viên ngồi chết lặng trước màn hình. | 4.10#5 · 4.10#6 | 4-41 · 4-42 (10.2 s) |
| 105 | `t11_investigator_nausea_monitor` | Góc nhìn từ sau lưng nhân viên điều tra run rẩy nhìn vào màn hình CRT phát sáng trong đêm, sự thật trần trụi. | 4.11#1 · 4.11#2 | 4-43 · 4-44 (12.2 s) |
| 106 | `t11_spinning_tape_reels` | Hai cuộn băng quay trần trong cơ chế máy, sợi băng chạy qua rãnh tối. | 4.11#3 · 4.11#4 | 4-45 · 4-46 (14.9 s) |
| 107 | `t11_obedient_accomplice_strings` | Một con rối gỗ nằm trên sàn tối với dây điều khiển quấn lại đầy đờ. | 4.13#1 · 4.13#2 | 4-48 · 4-49 (10.8 s) |
| 108 | `t11_idealised_portrait_dark` | Bức chân dung đôi trai trẻ được vẽ quá hoàn hảo trên bếp lửa, khuôn mặt nhòe đi. | 4.13#3 · 5.07#5 | 4-50 · 5-27 (17.7 s) |
| 109 | `t11_mockery_of_justice_tears` | Chiếc mặt nạ kịch nghệ vỡ vụn trên bục nhân chứng, những giọt nước mắt tại tòa chỉ là màn diễn xuất vị kỷ. | 4.13#4 · 4.13#5 | 4-51 · 4-52 (15.6 s) |
| 110 | `t11_fragile_beauty_manipulation` | Bộ đồ hồng hoàn hảo treo trong rạp hậu trường dưới một bóng đèn trần trơ trọi. | 4.13#7 · 4.13#8 | 4-54 · 4-55 (10.7 s) |
| 111 | `t11_outraged_citizens_protest` | Biển người biểu tình mang biểu ngữ đòi công lý cho Leslie Mahaffy và Kristen French trước tòa nhà Quốc hội Ontario. | 4.14#1 · 4.14#2 · 5.07#2 | 4-56 · 4-57 · 5-24 (21.0 s) |
| 112 | `t11_constitutional_legal_deadlock` | Cuốn sách luật hiến pháp và chiếc còng số tám bị khóa chặt, cái bẫy tư pháp không lối thoát bảo vệ kẻ thủ ác. | 4.14#3 · 4.14#4 | 4-58 · 4-59 (19.0 s) |
| 113 | `t11_steel_gate_brick_wall` | Cánh cổng thép khép kín giữa tường gạch nhà tù lúc chiều, ánh sáng lạnh rơi xiên. | 4.14#5 · 5.07#1 | 4-60 · 5-23 (19.4 s) |
| 114 | `t11_dangerous_offender_life_sentence` | Bản án chung thân không ân xá và dấu mộc 'Dangerous Offender' giam giữ vô thời hạn Paul Bernardo tại nhà tù Kingston. | 4.14#6 · 5.02#1 | 4-61 · 5-01 (18.6 s) |

### HỒI 5 · PHÁN QUYẾT, DI CHỨNG TƯ PHÁP & BÀI HỌC CẢNH BÁO ĐỎ

| Ảnh | Tên file | Nội dung phục vụ | Mốc câu | Shot dùng |
|---|---|---|---|---|
| 115 | `t11_prison_cell_stone_dark` | Buồng giam tối với cánh cửa thép nặng và ô cửa song sắt hắt một vệt sáng mỏng. | 5.02#2 · 5.02#3 | 5-02 · 5-03 (18.3 s) |
| 116 | `t11_thick_concrete_wall` | Bức tường bê tông dày trong hành lang cơ quan, một đèn trần và bóng cứng dài. | 5.02#4 · 5.02#5 | 5-04 · 5-05 (17.2 s) |
| 117 | `t11_joliette_prison_gate_release` | Cánh cổng sắt Trại cải tạo Nữ Joliette mở ra ngày 04/07/2005, bóng người phụ nữ bước ra giữa rừng ống kính truyền thông. | 5.05#1 · 5.05#2 | 5-14 · 5-15 (16.2 s) |
| 118 | `t11_blank_photographs_in_hands` | Hai bàn tay đeo găng cầm những tấm ảnh nhỏ trắng trơn, đám đông mờ phía sau. | 5.05#3 | 5-16 (9.4 s) |
| 119 | `t11_haunted_new_identity_shadow` | Hộ chiếu mang tên mới Leanne Teale đặt trên mặt bàn, nhưng bóng đen quá khứ vẫn phủ kín không thể xóa nhòa. | 5.05#4 · 5.05#5 · 5.07#4 | 5-17 · 5-18 · 5-26 (25.7 s) |
| 120 | `t11_galligan_inquiry_report_reforms` | Báo cáo thẩm tra độc lập của Thẩm phán Patrick Galligan năm 1996, cuộc cải cách triệt để quy trình thương lượng nhận tội. | 5.05#6 · 5.05#7 | 5-19 · 5-20 (15.3 s) |
| 121 | `t11_police_archive_shelves` | Hàng kệ hồ sơ vô tận trong kho lưu trữ cảnh sát, một bóng đèn đung đưa. | 5.05#8 · 5.05#9 | 5-21 · 5-22 (18.4 s) |
| 122 | `t11_empty_auditorium_dust` | Giá học vắng tanh với hàng ghế gỗ, ánh sáng nhạt xuyên qua lớp bụi mỏng. | 5.07#6 · 5.07#7 · 5.07#8 | 5-28 · 5-29 · 5-30 (23.7 s) |
| 123 | `t11_disguised_predator_scales` | Cán cân phân định giữa nạn nhân chân chính và kẻ săn mồi mang mặt nạ yếu đuối, sự cảnh tỉnh nghiêm khắc. | 5.07#10 · 5.07#11 | 5-32 · 5-33 (13.0 s) |
| 124 | `t11_delicate_paper_ornament` | Món đồ giấy gấp tinh xảo đặt trên bậu cửa sổ, hơi nước đóng thành hoa văn. | 5.07#12 · 5.07#13 | 5-34 · 5-35 (16.9 s) |
| 125 | `t11_community_shield_circle` | Vòng ghế trống xếp tròn trong hội trường cộng đồng, nhìn từ trên cao. | 5.07#14 · 5.07#15 | 5-36 · 5-37 (10.7 s) |
| 126 | `t11_four_warning_lights` | Bốn đèn cảnh báo đỏ rực trong hành lang tối, sương lạnh và bóng dài. | 5.08#1 | 5-38 (9.5 s) |
| 127 | `t11_redflag1_evading_accountability` | Dấu hiệu cảnh báo 1: Chiếc khiên tổn thương dùng để cản phá mọi chất vấn pháp lý và né tránh trách nhiệm. | 5.08#2 · 5.08#3 | 5-39 · 5-40 (19.6 s) |
| 128 | `t11_redflag2_words_vs_actions_split` | Dấu hiệu cảnh báo 2: Sự phân đôi giữa lời nói ngọt ngào trước đám đông và hành vi lạnh lùng toan tính trong bóng tối. | 5.08#4 · 5.08#5 | 5-41 · 5-42 (14.0 s) |
| 129 | `t11_redflag3_guilt_tripping_trap` | Dấu hiệu cảnh báo 3: Chiếc bẫy cảm giác tội lỗi giăng ra để bẻ gãy mọi sự nghi ngờ chính đáng của người khác. | 5.08#6 · 5.08#7 | 5-43 · 5-44 (16.8 s) |
| 130 | `t11_redflag4_toxic_symbiosis_abyss` | Dấu hiệu cảnh báo 4: Vực thẳm của mối quan hệ cộng sinh độc hại, nơi tình yêu bị đánh đổi bằng việc hủy hoại lương tri. | 5.08#8 · 5.08#9 | 5-45 · 5-46 (13.1 s) |
| 131 | `t11_noose_shadow_wall` | Bóng sắc của một vòng dây thòng lọng đổ trên tường lạnh, một nguồn sáng cứng. | 5.08#10 | 5-47 (9.4 s) |
| 132 | `t11_closing_dossier_stamp` | Hồ sơ dày đóng lại trên bàn tối cùng chiếc dấu kim loại nặng, ánh sáng trắng lạnh. | 5.10#1 · 5.10#2 | 5-50 · 5-51 (20.1 s) |
| 133 | `t11_hope_candles_dark_room` | Hàng nến nhỏ cháy trên bậu cửa sổ đêm, ánh sáng xanh bên ngoài và đốm lửa ấm. | 5.10#3 · 5.10#4 | 5-52 · 5-53 (20.3 s) |
| 134 | `t11_empty_stage_spotlight` | Sân khấu nhỏ trống với một luồng đèn rọi trên ván sàn trần, bụi lơ lửng. | 5.10#5 · 5.10#6 | 5-54 · 5-55 (9.9 s) |
| 135 | `t11_control_room_dark_monitors` | Phòng điều khiển tối với dãy màn hình đã tắt và một đèn bàn bảng điện. | 5.10#7 · 5.10#8 | 5-56 · 5-57 (8.8 s) |
| 136 | `t11_closing_card_dossier` | Nền riêng cho thẻ kết: hồ sơ đóng lại trên mặt bàn đen, vệt sáng mỏng viền. | THẺ KẾT | 5-59 (0.0 s) |

## B3. Thống kê & Kiểm soát chất lượng (QC)

| Hạng mục | Kết quả |
|---|---|
| Cổng H22 (kế hoạch) | `py -3 .work/qc_bg_usage.py --plan` → **ĐẠT** — 136 mã nền, 0 nền vượt 3 shot/30 s, 0 mã thiếu job, 0 job thừa |
| Cổng H22 (sau khi sinh) | `AE_EP=11 py -3 .work/qc_bg_usage.py` → chạy lại sau `parse_shots.py` |
| Cổng H17 (nền dùng chung) | `py -3 .work/qc_bg_shared.py --ep 11` → nền + nền từng shot trùng mọi ngôn ngữ |
| Soi mắt nền mới (H2/H19) | **100 %** nền mới bằng montage `.work/qc_montage.py --kind bg` (nền mới không được lược) |
| Provenance (L7) | 136 dòng `assets/bg/t11_*.png` có bản ghi trong `provenance.json` |

---

*Tài liệu sinh tự động từ `02_SAN_XUAT/Tap11/KeHoach_Video_Tap11.md` + `.work/bg_jobs_tap11.json` — ngày 16/11/2026. Khi đổi bảng shot hoặc sinh lại nền, chạy lại script `.work/_t11_gen_danh_sach_anh.py`.*
