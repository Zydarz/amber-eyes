# BÁO CÁO THẨM ĐỊNH & REVIEW CHẤT LƯỢNG BỘ ẢNH NỀN TẬP 08
## "KHI CÁC THIÊN TÀI BỊ TẨY NÃO" (SHOKO ASAHARA & GIÁO PHÁI AUM SHINRIKYO)

*Ngày lập báo cáo: 23/10/2026 · **Cập nhật 09/11/2026** — bộ ảnh đã sinh lại bằng **MiniMax**, số đo đo lại từ file thật.*

---

## I. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

| Tiêu chí | Kết quả thẩm định | Trạng thái | Ghi chú kỹ thuật |
|---|:---:|:---:|---|
| **Số lượng ảnh** | **74 / 74 ảnh** | **ĐẠT (100%)** | Đúng 100% danh sách trong `.work/bg_jobs_tap08.json` |
| **Kích thước & Tỷ lệ** | **2112 × 1188 (16:9 2K)** | **ĐẠT (100%)** | 74/74 ảnh full-bleed, không viền đen letterbox |
| **Kiểm tra viền & Khung vẽ (QC)** | **1 lỗi → đã sửa** | **ĐẠT** | `t8_matsumoto_court_dossier` bị MiniMax để lại khung trắng ~45 px → **cắt bằng code** (không tốn credit); hiện 74/74 sạch |
| **Sổ nguồn gốc (`provenance.json`)** | **74 / 74 bản ghi** | **ĐẠT (100%)** | Đầy đủ prompt, công cụ tạo ảnh, kích thước gốc; **điều khoản thương mại: CHƯA kiểm tra** |
| **Độ sáng trung bình (Mean Luminance)** | **61.0 / 255** | **ĐẠT CHUẨN NOIR** | Khoảng 30.9 – 138.5 |
| **Độ tương phản (Chiaroscuro Std)** | **50.7** | **XUẤT SẮC** | max 82.9 (`t8_dropped_novel_glasses`) |
| **Tuân thủ quy tắc V5 (Nhân vật thật)** | **100% Bóng lưng / Khuất mặt** | **ĐẠT (100%)** | Không ảnh nào lộ mặt Shoko Asahara, Ikuo Hayashi, Hideo Murai, Masami Tsuchiya |
| **Tuân thủ quy tắc V9 (An toàn nội dung)** | **100% Không bạo lực, máu me** | **ĐẠT (100%)** | Trọng tâm phân tích tâm lý học giáo phái, hiện tượng trống rỗng hiện sinh, thiết bị PSI và 4 Red Flags |
| **Chữ / số do AI vẽ trong nền** | **2 ảnh → đã sinh lại** | **ĐẠT** | `t8_dossier_elite_scientists` (sách *UNIVERSITY REGISTRY*) và `t8_sarin_synthesis_laboratory` (màn hình hiện số) đã sinh lại với negative mạnh hơn |
| **Bảng tổng hợp (Contact Sheet)** | **Đã xuất bản** | **HOÀN THÀNH** | 7 tờ nền: `02_SAN_XUAT/Tap08/contact_sheet_nen_t08_p1..p7.png` |

---

## II. PHÂN TÍCH QUANG HỌC & ĐẶC TÍNH THỊ GIÁC

Dữ liệu trích xuất từ phân tích ma trận điểm ảnh toàn bộ 74 file `assets/bg/t8_*.png`:

1. **Phân bổ sắc độ (Luminance Distribution):**
   - **Ảnh tối nhất:** `t8_subway_platform_tunnel_dark` (Mean = 30.9).
   - **Ảnh sáng nhất:** `t8_dropped_novel_glasses` (Mean = 138.5).
   - **Trung bình toàn bộ:** 61.0 — cao hơn bộ procedural cũ (26,3) vì ảnh MiniMax là **cảnh thật** có vùng sáng (đèn, kính, giấy), không phải texture tối.
2. **Độ tương phản Chiaroscuro:**
   - **74/74 ảnh** có Std > 25 (chuẩn noir của kênh).
   - Giá trị cực đại 82.9 (`t8_dropped_novel_glasses`); trung bình 50.7 (bộ procedural cũ chỉ đạt 11/74 ảnh vượt ngưỡng).
3. **An toàn kiểm duyệt YouTube & Chuẩn nhận diện:**
   - Không ảnh nào vượt ngưỡng chói lóa (Mean > 160): 0.
   - Không ảnh nào bị bệt đen hoàn toàn (Mean < 20): 0.
   - 74/74 ảnh không viền đen letterbox, không khung trắng (1 khung trắng đã cắt).

---

## III. ĐÁNH GIÁ MẠCH KỂ THỊ GIÁC (VISUAL STORYTELLING) THEO 5 HỒI

### 1. Hồi 1: Buổi sáng định mệnh dưới lòng đất Tokyo (24 ảnh)
- `t8_tokyo_dawn_fog` — Bầu trời Tokyo sáng sớm ngày 20/03/1995 mờ sương lạnh lẽo, những tòa nhà cao tầng chìm trong bóng tối chiaroscuro.
- `t8_commuter_crowd_station` — Dòng người hối hả giờ cao điểm đổ dồn xuống cửa ga tàu điện ngầm Tokyo, bóng người đen dài trên nền gạch lát sáng loáng.
- `t8_tokyo_stock_crash_1990` — Ẩn dụ kinh tế bong bóng sụp đổ: Các bảng điện tử chỉ số chứng khoán lao dốc phản chiếu trên mặt vũng nước mưa phố Tokyo.
- `t8_subway_tracks_perspective` — Phối cảnh sâu hun hút vào đường hầm ngầm của 3 tuyến tàu Chiyoda, Marunouchi và Hibiya, đường ray thép lấp loáng dưới đèn báo hiệu.
- `t8_kasumigaseki_facade` — Mặt tiền uy nghiêm của khu phức hợp các Bộ ngành chính phủ tại Kasumigaseki trong ánh ban mai xám xịt.
- `t8_corporate_salaryman_cogs` — Không gian văn phòng công ty Nhật Bản những năm 90 với hàng dãy bàn làm việc giống hệt nhau, áp lực đè nặng bánh răng cỗ máy xã hội.
- `t8_chemical_structure_sarin` — Bản vẽ cấu trúc phân tử chất độc Sarin mờ ảo trên nền bảng đen kỹ thuật hình sự, ánh sáng xanh lạnh ma mị.
- `t8_umbrella_puncture_action` — Cận cảnh đầu nhọn chiếc ô kim loại đâm thủng lớp màng bọc nylon, giọt chất lỏng trong suốt rỉ ra sàn tàu.
- `t8_newspaper_wrapped_package` — Tĩnh vật bọc giấy báo chứa túi nylon bí mật đặt cạnh chân ghế toa tàu, góc chụp thấp noir căng thẳng.
- `t8_train_doors_closing` — Cửa toa tàu điện ngầm đóng sập lại, bóng phản chiếu mờ ảo trên kính toa xe khi đoàn tàu lao vào hầm tối.
- `t8_subway_car_mist_vapor` — Toa tàu đông đúc với làn hơi độc vô hình bay là là trên sàn, ánh đèn neon nhấp nháy tạo bầu không khí ngột ngạt nghẹt thở.
- `t8_hospital_triage_corridor` — Hành lang cấp cứu bệnh viện dã chiến với các bình dưỡng khí và cột truyền dịch xếp dài, chiaroscuro xanh lạnh.
- `t8_ambulances_tokyo_street` — Đèn cứu thương đỏ rực nhấp nháy trên đường phố Tokyo xám xịt trong buổi sáng thảm họa, hàng dài xe khẩn cấp.
- `t8_dropped_novel_glasses` — Cuốn tiểu thuyết bỏ dở và chiếc kính mắt gọng kim loại vỡ nứt rơi trên sàn gạch sân ga, tĩnh lặng lạnh gáy.
- `t8_subway_platform_tunnel_dark` — Sân ga ngầm u tối nhìn sâu vào lòng hầm hun hút, ánh đèn vàng mờ nhạt, cảm giác ngột ngạt và mù lòa của nạn nhân.
- `t8_subway_stairs_escape` — Cầu thang gạch men dẫn từ ga ngầm lên mặt đất, các bóng đen hoảng loạn bò tìm lối thoát trong ánh sáng yếu ớt.
- `t8_tokyo_police_hq` — Trụ sở Cơ quan Cảnh sát Quốc gia Nhật Bản (Keishicho) uy nghiêm trong đêm điều tra khẩn cấp, xe tuần tra nhấp nháy đèn.
- `t8_incident_board_map` — Bản đồ mạng lưới tàu điện ngầm Tokyo trong phòng tác chiến cảnh sát với các mốc đỏ đánh dấu các ga bị tấn công.
- `t8_aum_shinrikyo_emblem_shadow` — Biểu tượng chữ Phạn bí truyền của giáo phái Aum Shinrikyo chìm trong bóng tối bí ẩn, ánh sáng chiaroscuro đe dọa.
- `t8_dossier_elite_scientists` — Bìa hồ sơ điều tra chuyên án bí mật của cảnh sát Tokyo với danh sách các nhà khoa học tinh hoa bị nghi vấn.
- `t8_chemical_plant_reactor` — Dàn tháp phản ứng và máy móc tổng hợp hóa chất hữu cơ bằng thép không gỉ sáng bóng bên trong Satyam số 7.
- `t8_broken_hippocratic_oath` — Bản Lời thề Hippocrates bằng giấy da bị rách một đường dài, chiếc dao mổ phẫu thuật bằng thép sáng loáng nằm bên cạnh trong bóng tối.
- `t8_intellectual_hubris_chess` — Quân vua cờ bằng ngà voi đứng cô độc trên bàn cờ đá cẩm thạch đen, đổ bóng dài méo mó thành hình chiếc bóng tà ác, ẩn dụ cái tôi trí tuệ.
- `t8_cosmic_physics_observatory` — Đài thiên văn vật lý với kính viễn vọng lớn hướng lên bầu trời đêm đầy sao, biểu trưng cho sự nghiệp của nhà vật lý Hideo Murai.

### 2. Hồi 2: Căn cứ dưới chân núi Phú Sĩ & Phòng thí nghiệm tử thần (24 ảnh)
- `t8_mount_fuji_dawn_somber` — Núi Phú Sĩ sừng sững trong sương sớm u ám lạnh lẽo, những rặng thông đen bao quanh chân núi cô lập.
- `t8_hazmat_officers_formation` — Đội hình đặc nhiệm cảnh sát trong trang phục phòng chống vũ khí hóa học và mặt nạ dưỡng khí tiến vào căn cứ.
- `t8_police_convoy_kamikuishiki` — Đoàn xe cảnh sát và đặc nhiệm phòng hóa rầm rộ nối đuôi nhau trên con đường làng Kamikuishiki vắng lặng.
- `t8_asahara_empty_dock` — Vành móng ngựa gỗ sau tấm kính chắn trong suốt, một chiếc ghế trống dưới ánh đèn rọi duy nhất, chấm dứt cơn cuồng vọng.
- `t8_satyam_compound_aerial` — Quần thể Satyam gồm những khối nhà bê tông thô ráp xám xịt, hàng rào thép gai và tháp quan sát canh phòng cẩn mật.
- `t8_satyam_7_exterior` — Mặt ngoài tòa nhà Satyam số 7 không cửa sổ, các ống thông gió công nghiệp khổng lồ chạy ngoằn ngoèo trên tường.
- `t8_chemical_precursor_drums` — Hàng trăm thùng phi chứa hóa chất tiền chất độc hại xếp chồng trên pallet gỗ trong kho ngầm, ánh đèn neon lạnh.
- `t8_mi17_helicopter_hangar` — Chiếc trực thăng quân sự Mi-17 xám bạc đậu im lìm trong hangar tối om, cánh quạt khổng lồ rủ bóng nặng nề.
- `t8_chemical_plant_reactor` — Dàn tháp phản ứng và máy móc tổng hợp hóa chất hữu cơ bằng thép không gỉ sáng bóng bên trong Satyam số 7.
- `t8_tsukuba_chemistry_lab` — Phòng thí nghiệm hóa hữu cơ Đại học Tsukuba với bảng đen chi chít công thức hóa học hữu cơ phân tử, ghế xoay trống vắng.
- `t8_newspaper_wrapped_package` — Tĩnh vật bọc giấy báo chứa túi nylon bí mật đặt cạnh chân ghế toa tàu, góc chụp thấp noir căng thẳng.
- `t8_aum_shinrikyo_emblem_shadow` — Biểu tượng chữ Phạn bí truyền của giáo phái Aum Shinrikyo chìm trong bóng tối bí ẩn, ánh sáng chiaroscuro đe dọa.
- `t8_apocalypse_prophecy_scroll` — Bản thảo thư pháp viết tay về ngày tận thế và chiến tranh hủy diệt Armageddon đặt cạnh những mô hình tên lửa và đám mây hình nấm.
- `t8_iron_gate_closing` — Cánh cổng sắt bọc thép gai của khu căn cứ Kamikuishiki đóng chặt lại bằng ổ khóa lớn, biểu tượng của sự bẫy kín và cắt đứt thế giới.
- `t8_moral_rationalization_books` — Những cuốn sách giáo trình khoa học đỉnh cao xếp xen lẫn kinh sách tận thế dưới ánh nến leo lét trong thư viện tối.
- `t8_matsumoto_night_1994` — Con phố dân cư tĩnh mịch tại Matsumoto đêm mùa hè 1994, sương mờ bao phủ chiếc xe tải cải tiến bí ẩn.
- `t8_yoga_meditation_incense` — Phòng tập yoga và thiền Aum Shinsen no Kai thời kỳ đầu với thảm trắng, khói trầm hương lượn lờ và sơ đồ vật lý lượng tử treo tường.
- `t8_sakamoto_lawyer_desk` — Bàn làm việc vắng bóng người của Luật sư Sakamoto tại văn phòng Yokohama, tập tài liệu bảo vệ nạn nhân và điện thoại rơi.
- `t8_mountain_grave_memorial` — Khung cảnh rừng thông miền núi Gunma mù sương nơi hài cốt gia đình luật sư dũng cảm được tìm thấy, trang nghiêm đượm buồn.
- `t8_matsumoto_court_dossier` — Hồ sơ tài liệu vụ kiện đất đai của giáo phái tại Tòa án Matsumoto nằm dưới ánh đèn bàn làm việc ban đêm.
- `t8_sarin_synthesis_laboratory` — Phòng thí nghiệm chưng cất hóa chất với bình cầu thủy tinh, ống sinh hàn và đồng hồ đo áp suất tinh vi.
- `t8_weapons_of_mass_destruction` — Tĩnh vật hình sự: Bình chứa khí nén kim loại, ống nghiệm vi sinh và tài liệu mật của giáo phái dưới đèn spotlight.
- `t8_devotion_altar_kneeling` — Bóng những tín đồ thanh niên mặc áo choàng trắng quỳ rạp trước đài sen cao trong đại sảnh nghi lễ mờ khói nhang.
- `t8_buddhist_mandala_distortion` — Bức tranh cát Mandala Phật giáo Tây Tạng thiêng liêng bị xáo trộn và biến dạng thành những đường nét sắc nhọn đen tối, biểu tượng bóp méo giáo lý.

### 3. Hồi 3: Nghịch lý của các thiên tài khoa học (25 ảnh)
- `t8_asahara_shadow_profile` — Bóng lưng và góc nghiêng của giáo chủ Shoko Asahara với mái tóc dài và râu rậm ngồi thiền trong bóng tối, không lộ mặt.
- `t8_todai_red_gate_shadow` — Cổng Đỏ (Akamon) của Đại học Tokyo trong mưa chiều mùa đông u tối, biểu tượng cho cánh cửa học thuật đã khép lại với kẻ thất bại.
- `t8_chinese_herbal_apothecary` — Tủ thuốc bắc cổ kính bằng gỗ tối màu với các lọ thủy tinh đựng rễ cây và dược liệu đông y, quá khứ bán thuốc giả của giáo chủ.
- `t8_devotion_altar_kneeling` — Bóng những tín đồ thanh niên mặc áo choàng trắng quỳ rạp trước đài sen cao trong đại sảnh nghi lễ mờ khói nhang.
- `t8_matsumoto_court_dossier` — Hồ sơ tài liệu vụ kiện đất đai của giáo phái tại Tòa án Matsumoto nằm dưới ánh đèn bàn làm việc ban đêm.
- `t8_yoga_meditation_incense` — Phòng tập yoga và thiền Aum Shinsen no Kai thời kỳ đầu với thảm trắng, khói trầm hương lượn lờ và sơ đồ vật lý lượng tử treo tường.
- `t8_dossier_elite_scientists` — Bìa hồ sơ điều tra chuyên án bí mật của cảnh sát Tokyo với danh sách các nhà khoa học tinh hoa bị nghi vấn.
- `t8_cosmic_physics_observatory` — Đài thiên văn vật lý với kính viễn vọng lớn hướng lên bầu trời đêm đầy sao, biểu trưng cho sự nghiệp của nhà vật lý Hideo Murai.
- `t8_virology_electron_microscope` — Kính hiển vi điện tử trong phòng nghiên cứu vi sinh của Đại học Y Kyoto, màn hình huỳnh quang xanh lục hiển thị cấu trúc virus.
- `t8_cardiac_surgery_theatre` — Phòng mổ tim mạch vô trùng hiện đại với dàn đèn phẫu thuật cực sáng chiếu xuống bàn mổ inox, sự nghiệp đỉnh cao của Bác sĩ Hayashi.
- `t8_tsukuba_chemistry_lab` — Phòng thí nghiệm hóa hữu cơ Đại học Tsukuba với bảng đen chi chít công thức hóa học hữu cơ phân tử, ghế xoay trống vắng.
- `t8_stethoscope_abandoned_drain` — Chiếc ống nghe y tế của bác sĩ nằm vắt qua đường ống cống bê tông xám xịt trong căn cứ ngầm, sự tha hóa tột cùng.
- `t8_intellectual_hubris_chess` — Quân vua cờ bằng ngà voi đứng cô độc trên bàn cờ đá cẩm thạch đen, đổ bóng dài méo mó thành hình chiếc bóng tà ác, ẩn dụ cái tôi trí tuệ.
- `t8_broken_hippocratic_oath` — Bản Lời thề Hippocrates bằng giấy da bị rách một đường dài, chiếc dao mổ phẫu thuật bằng thép sáng loáng nằm bên cạnh trong bóng tối.
- `t8_frontal_lobe_brain_scan` — Hình ảnh chụp cộng hưởng từ / PET scan lát cắt não bộ con người trên màn hình y khoa, vùng thùy trán bị bóng tối bao phủ.
- `t8_tokyo_stock_crash_1990` — Ẩn dụ kinh tế bong bóng sụp đổ: Các bảng điện tử chỉ số chứng khoán lao dốc phản chiếu trên mặt vũng nước mưa phố Tokyo.
- `t8_corporate_salaryman_cogs` — Không gian văn phòng công ty Nhật Bản những năm 90 với hàng dãy bàn làm việc giống hệt nhau, áp lực đè nặng bánh răng cỗ máy xã hội.
- `t8_moral_rationalization_books` — Những cuốn sách giáo trình khoa học đỉnh cao xếp xen lẫn kinh sách tận thế dưới ánh nến leo lét trong thư viện tối.
- `t8_fragile_boundary_mirror` — Tấm gương phẳng phản chiếu khung cảnh thành phố bình yên bị một vết nứt sâu chạy ngang, ẩn dụ về ranh giới mong manh của tâm trí.
- `t8_apocalypse_prophecy_scroll` — Bản thảo thư pháp viết tay về ngày tận thế và chiến tranh hủy diệt Armageddon đặt cạnh những mô hình tên lửa và đám mây hình nấm.
- `t8_buddhist_mandala_distortion` — Bức tranh cát Mandala Phật giáo Tây Tạng thiêng liêng bị xáo trộn và biến dạng thành những đường nét sắc nhọn đen tối, biểu tượng bóp méo giáo lý.
- `t8_bio_incubator_pathogens` — Tủ ủ vô trùng nuôi cấy vi sinh vật ngầm dán nhãn vi khuẩn bệnh Than và Botulinum trong ánh đèn tím khử trùng.
- `t8_psi_headgear_electrodes` — Cận cảnh chiếc mũ điện cực PSI (Perfect Salvation Initiation) với mớ dây điện chằng chịt và các đầu hút kim loại phát sáng ma quái.
- `t8_mountain_grave_memorial` — Khung cảnh rừng thông miền núi Gunma mù sương nơi hài cốt gia đình luật sư dũng cảm được tìm thấy, trang nghiêm đượm buồn.
- `t8_concrete_cell_isolation` — Phòng biệt giam bê tông trần xám xịt với ô cửa sổ sắt nhỏ trên cao, một tấm chăn mỏng rách rưới trên sàn đá lạnh buốt.

### 4. Hồi 4: Ma thuật tẩy não & Khái niệm "Poa" (28 ảnh)
- `t8_concrete_cell_isolation` — Phòng biệt giam bê tông trần xám xịt với ô cửa sổ sắt nhỏ trên cao, một tấm chăn mỏng rách rưới trên sàn đá lạnh buốt.
- `t8_malnutrition_solitary_bowl` — Chiếc bát sứ sứt mẻ đựng chút cơm nguội và vài cọng rau luộc đặt lẻ loi trên bậc thềm đá, biểu tượng của sự bỏ đói thể xác.
- `t8_frontal_lobe_brain_scan` — Hình ảnh chụp cộng hưởng từ / PET scan lát cắt não bộ con người trên màn hình y khoa, vùng thùy trán bị bóng tối bao phủ.
- `t8_hidden_ceiling_hideout` — Khoang hầm bí mật chật hẹp giữa trần nhà Satyam số 6, bọc tiền yen và những thỏi vàng nằm lăn lóc trên thanh xà gỗ phủ bụi.
- `t8_yoga_meditation_incense` — Phòng tập yoga và thiền Aum Shinsen no Kai thời kỳ đầu với thảm trắng, khói trầm hương lượn lờ và sơ đồ vật lý lượng tử treo tường.
- `t8_psi_headgear_electrodes` — Cận cảnh chiếc mũ điện cực PSI (Perfect Salvation Initiation) với mớ dây điện chằng chịt và các đầu hút kim loại phát sáng ma quái.
- `t8_hallucinogen_ritual_hall` — Sảnh nghi lễ chìm trong ánh sáng tím huyền bí và khói mờ ảo giác, các chai thuốc hướng thần và ống nghiệm trên bàn tế.
- `t8_bio_incubator_pathogens` — Tủ ủ vô trùng nuôi cấy vi sinh vật ngầm dán nhãn vi khuẩn bệnh Than và Botulinum trong ánh đèn tím khử trùng.
- `t8_chemical_precursor_drums` — Hàng trăm thùng phi chứa hóa chất tiền chất độc hại xếp chồng trên pallet gỗ trong kho ngầm, ánh đèn neon lạnh.
- `t8_virology_electron_microscope` — Kính hiển vi điện tử trong phòng nghiên cứu vi sinh của Đại học Y Kyoto, màn hình huỳnh quang xanh lục hiển thị cấu trúc virus.
- `t8_poa_twisted_doctrine` — Ẩn dụ thị giác: Bông sen trắng tinh khiết bị dìm vào vũng mực đen kịt, cành sen gãy đôi, biểu tượng cho khái niệm 'Poa' đẫm máu.
- `t8_buddhist_mandala_distortion` — Bức tranh cát Mandala Phật giáo Tây Tạng thiêng liêng bị xáo trộn và biến dạng thành những đường nét sắc nhọn đen tối, biểu tượng bóp méo giáo lý.
- `t8_broken_hippocratic_oath` — Bản Lời thề Hippocrates bằng giấy da bị rách một đường dài, chiếc dao mổ phẫu thuật bằng thép sáng loáng nằm bên cạnh trong bóng tối.
- `t8_devotion_altar_kneeling` — Bóng những tín đồ thanh niên mặc áo choàng trắng quỳ rạp trước đài sen cao trong đại sảnh nghi lễ mờ khói nhang.
- `t8_apocalypse_prophecy_scroll` — Bản thảo thư pháp viết tay về ngày tận thế và chiến tranh hủy diệt Armageddon đặt cạnh những mô hình tên lửa và đám mây hình nấm.
- `t8_moral_rationalization_books` — Những cuốn sách giáo trình khoa học đỉnh cao xếp xen lẫn kinh sách tận thế dưới ánh nến leo lét trong thư viện tối.
- `t8_weapons_of_mass_destruction` — Tĩnh vật hình sự: Bình chứa khí nén kim loại, ống nghiệm vi sinh và tài liệu mật của giáo phái dưới đèn spotlight.
- `t8_dr_hayashi_umbrella_subway` — Bóng người đàn ông trung niên trong áo khoác dài cầm chiếc ô đen đứng lẻ loi trên sân ga đông đúc, bóng tối nội tâm đè nặng.
- `t8_cardiac_surgery_theatre` — Phòng mổ tim mạch vô trùng hiện đại với dàn đèn phẫu thuật cực sáng chiếu xuống bàn mổ inox, sự nghiệp đỉnh cao của Bác sĩ Hayashi.
- `t8_tokyo_court_witness_stand` — Bục nhân chứng bằng gỗ tại Tòa án Tokyo, chiếc micro kim loại đơn độc dưới ánh đèn rọi thẳng từ trần nhà, không khí trang nghiêm nghẹn ngào.
- `t8_grand_courtroom_proceedings` — Toàn cảnh đại phòng xử án Tòa án Quận Tokyo với bục ba vị thẩm phán uy nghiêm, dãy bàn luật sư và không gian xử án đồ sộ.
- `t8_stethoscope_abandoned_drain` — Chiếc ống nghe y tế của bác sĩ nằm vắt qua đường ống cống bê tông xám xịt trong căn cứ ngầm, sự tha hóa tột cùng.
- `t8_murai_assassination_cameras` — Ống kính máy quay truyền hình và đèn flash máy ảnh rọi sáng hỗn loạn trong đêm tối bên ngoài văn phòng Aum ở Minami-Aoyama.
- `t8_police_convoy_kamikuishiki` — Đoàn xe cảnh sát và đặc nhiệm phòng hóa rầm rộ nối đuôi nhau trên con đường làng Kamikuishiki vắng lặng.
- `t8_asahara_shadow_profile` — Bóng lưng và góc nghiêng của giáo chủ Shoko Asahara với mái tóc dài và râu rậm ngồi thiền trong bóng tối, không lộ mặt.
- `t8_iron_gate_closing` — Cánh cổng sắt bọc thép gai của khu căn cứ Kamikuishiki đóng chặt lại bằng ổ khóa lớn, biểu tượng của sự bẫy kín và cắt đứt thế giới.
- `t8_tokyo_court_gavel_strike` — Chiếc búa gỗ thẩm phán đập dứt khoát xuống đế gỗ tròn trong phòng xử án, khẳng định công lý hình sự.
- `t8_matsumoto_court_dossier` — Hồ sơ tài liệu vụ kiện đất đai của giáo phái tại Tòa án Matsumoto nằm dưới ánh đèn bàn làm việc ban đêm.

### 5. Hồi 5: Phán quyết lịch sử & Bài học về sự tự do tư tưởng (20 ảnh)
- `t8_grand_courtroom_proceedings` — Toàn cảnh đại phòng xử án Tòa án Quận Tokyo với bục ba vị thẩm phán uy nghiêm, dãy bàn luật sư và không gian xử án đồ sộ.
- `t8_tokyo_court_gavel_strike` — Chiếc búa gỗ thẩm phán đập dứt khoát xuống đế gỗ tròn trong phòng xử án, khẳng định công lý hình sự.
- `t8_fragile_boundary_mirror` — Tấm gương phẳng phản chiếu khung cảnh thành phố bình yên bị một vết nứt sâu chạy ngang, ẩn dụ về ranh giới mong manh của tâm trí.
- `t8_concrete_cell_isolation` — Phòng biệt giam bê tông trần xám xịt với ô cửa sổ sắt nhỏ trên cao, một tấm chăn mỏng rách rưới trên sàn đá lạnh buốt.
- `t8_thirteen_death_verdicts` — Mười ba tập hồ sơ bản án bìa đen mang con dấu đỏ của Tòa án Tối cao Tokyo xếp ngay ngắn trên bàn gỗ sẫm màu.
- `t8_dossier_elite_scientists` — Bìa hồ sơ điều tra chuyên án bí mật của cảnh sát Tokyo với danh sách các nhà khoa học tinh hoa bị nghi vấn.
- `t8_iron_gate_closing` — Cánh cổng sắt bọc thép gai của khu căn cứ Kamikuishiki đóng chặt lại bằng ổ khóa lớn, biểu tượng của sự bẫy kín và cắt đứt thế giới.
- `t8_matsumoto_court_dossier` — Hồ sơ tài liệu vụ kiện đất đai của giáo phái tại Tòa án Matsumoto nằm dưới ánh đèn bàn làm việc ban đêm.
- `t8_tokyo_detention_house_dawn` — Trại tạm giam Tokyo tại Kosuge sừng sững trong ánh bình minh tháng 7 năm 2018, những bức tường bê tông cao vút và dây thép gai.
- `t8_murakami_underground_book` — Cuốn sách 'Underground' (Ngầm) của Haruki Murakami đặt trên bàn gỗ bên cạnh tách trà xanh nguội và bản đồ ga tàu Tokyo.
- `t8_tokyo_dawn_restored_peace` — Toàn cảnh đường chân trời Tokyo lúc bình minh rạng rỡ, ánh sáng vàng hổ phách xua tan sương mù, biểu tượng của sự hồi sinh và bình yên.
- `t8_buddhist_mandala_distortion` — Bức tranh cát Mandala Phật giáo Tây Tạng thiêng liêng bị xáo trộn và biến dạng thành những đường nét sắc nhọn đen tối, biểu tượng bóp méo giáo lý.
- `t8_corporate_salaryman_cogs` — Không gian văn phòng công ty Nhật Bản những năm 90 với hàng dãy bàn làm việc giống hệt nhau, áp lực đè nặng bánh răng cỗ máy xã hội.
- `t8_moral_rationalization_books` — Những cuốn sách giáo trình khoa học đỉnh cao xếp xen lẫn kinh sách tận thế dưới ánh nến leo lét trong thư viện tối.
- `t8_redflag1_social_isolation` — Dấu hiệu 1 (Cô lập): Sợi dây điện thoại bàn bị cắt đứt trên mặt bàn làm việc, cánh cửa gỗ khóa chặt trong bóng tối.
- `t8_redflag2_physical_exhaustion` — Dấu hiệu 2 (Kiệt quệ): Chiếc đồng hồ bấm giờ cổ điển, chiếc giường sắt chăn gối xộc xệch, bóng đèn trần leo lét, biểu tượng suy kiệt.
- `t8_redflag3_cult_of_personality` — Dấu hiệu 3 (Sùng bái): Bức tượng bán thân bằng đá khổng lồ trên bệ cao trong bóng tối, tất cả luồng sáng đều hướng lên một người.
- `t8_redflag4_moral_inversion` — Dấu hiệu 4 (Ngụy biện đạo đức): Thanh kiếm sắc bén phản chiếu cành ô liu hòa bình bị bẻ gãy, biểu tượng sự tha hóa đạo đức.
- `t8_malnutrition_solitary_bowl` — Chiếc bát sứ sứt mẻ đựng chút cơm nguội và vài cọng rau luộc đặt lẻ loi trên bậc thềm đá, biểu tượng của sự bỏ đói thể xác.
- `t8_tokyo_dawn_fog` — Bầu trời Tokyo sáng sớm ngày 20/03/1995 mờ sương lạnh lẽo, những tòa nhà cao tầng chìm trong bóng tối chiaroscuro.

**Ảnh không dùng trong bảng shot hiện tại:** `t8_subway_exit_sunlight` (giữ lại làm tài sản dự phòng — không mất credit đã sinh).

---

## IV. KẾT LUẬN & ĐỀ XUẤT SẢN XUẤT

1. **Đồng bộ kịch bản:** bộ ảnh được ánh xạ theo bảng shot 218 câu (`02_SAN_XUAT/Tap08/KeHoach_Video_Tap08.md` mục 6). Rà lại 74 nền phát hiện **3 shot lệch cảnh** — đã sửa trong cả 3 hồ sơ (VN/EN/JA):

   | Shot | Câu | Nền cũ (lệch) | Nền mới (khớp) |
   |---|---|---|---|---|
   | `1-10` | 1.04#2 *“dùng đầu ô đã mài nhọn đâm thủng các túi ni-lông…”* | `t8_chemical_structure_sarin` | **`t8_umbrella_puncture_action`** |
   | `1-25` | 1.09#3 *“Bệnh viện … chuyển toàn bộ sảnh lớn thành trạm cấp cứu dã chiến”* | `t8_subway_exit_sunlight` | **`t8_hospital_triage_corridor`** |
   | `2-25` | 2.07#2 *“phòng tập yoga nhỏ và những màn biểu diễn bay bổng”* | `t8_sarin_synthesis_laboratory` | **`t8_yoga_meditation_incense`** |

2. **Nguồn ảnh & bản quyền:** toàn bộ 74 nền được sinh bằng **`connector__matrix__generate_image` (MiniMax qua mcode-tools)** — đúng công cụ đã dùng cho Tập 02–07. Bộ cũ (23/10) vẽ bằng code và **không còn dùng**. **Điều khoản thương mại của MiniMax: `kiem_tra_thuong_mai: chưa` — phải kiểm tra trước khi đăng.**

3. **Sẵn sàng dựng video:** bộ ảnh đã lưu tại `assets/bg/t8_*.png` và nạp trực tiếp vào pipeline (`parse_shots.py` → `build_video3.py`). Ảnh tĩnh đã render đủ 223 shot × 3 ngôn ngữ.

4. **Hệ quả kỹ thuật:** nền ảnh thật **sáng hơn** nền texture cũ ⇒ 42/223 shot có chữ bị “chìm” (H9) ⇒ đã bật `text_scrim` cho 42 id trong `edition.py` khối `"08"`. Đo lại: **0/223 shot** còn chìm ở cả 3 ngôn ngữ.
