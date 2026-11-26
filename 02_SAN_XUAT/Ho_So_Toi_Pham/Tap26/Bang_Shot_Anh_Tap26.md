# BẢNG MAPPING SHOT ↔ ẢNH NỀN · TẬP 26

- Nguồn: `.work/bg_jobs_tap26.json` + kịch bản VN hiện tại · **176 shot · 176 ảnh khác nhau · ảnh bị dùng lặp ở >1 shot: 0** · phủ 240/240 câu
- Ảnh đã có file `assets/bg/`: **176/176** · Tổng thời lượng ƯỚC LƯỢNG: 35.0 phút (chỉ để tham khảo; thời lượng thật lấy từ `timeline_s` sau khi có audio, H14)
- **LUẬT DỰNG (AGENTS.md H28):** AI dựng video PHẢI đọc file này (hoặc `.work/shot_map_tap26.json`) và dùng **đúng ảnh ở cột Tên ảnh cho đúng câu ở cột Câu** — CẤM tự chọn ảnh theo chủ đề, CẤM lặp ảnh, CẤM đổi thứ tự. Trước khi dựng chạy `py -3 .work/map_shot_anh.py --check 26` phải ĐẠT.
- Cách dùng: dựng theo đúng thứ tự dòng; shot bắt đầu ở câu đầu của cột Câu và kéo tới hết câu cuối; ảnh = cột Tên ảnh.
- ⚠ **Ảnh có lỗi đã biết (3 ảnh đầu GIỮ NGUYÊN theo quyết định người dùng 25/11/2026; ảnh ghi MỚI đang chờ quyết định):** `t26_a1_13b_police_hq_corridor_urgent_arrest_order` — viền giấy kem 4 mép + tờ giấy dán có chữ giả trên tường trái (H2/H26); `t26_a4_23_public_outcry_tokyo_streets` — MỚI 25/11 (soi lại): chữ AI trên đầu tàu điện "RELAEL PASSEN" + biển phản đối (H26) — CHỜ quyết định sinh lại
- Lỗi mapping (cần xử lý): 0
- Shot dài ước > 15 s (H10, chỉ ước lượng — kiểm lại khi có timeline): 53 · > 30 s (H22): 0

| Shot | Hồi | Câu (đầu – cuối) | Số câu | Ước (s) | Tên ảnh (`assets/bg/<tên>.png`) | Có file | Mô tả cảnh |
|---|---|---|---|---|---|---|---|
| 1-001 | 1 | `1.02#1 – 1.02#2` | 2 | 18.1 | `t26_a1_01_tokyo_postwar_devastation` | ✅ | Tokyo sau Thế chiến II đổ nát hoang tàn, khói bụi u ám trong mùa đông kiệt quệ. |
| 1-002 | 1 | `1.02#3 – 1.02#4` | 2 | 16.5 | `t26_a1_02_starving_refugees_winter_shinjuku` | ✅ | Người dân nghèo khổ lũ lượt bồng bế con thơ giữa cái lạnh cắt da, bế tắc tuyệt vọng. |
| 1-003 | 1 | `1.02#5 – 1.02#6` | 2 | 15.9 | `t26_a1_03_ominous_shadow_over_maternity_ward` | ✅ | Bóng đen bí ẩn bao trùm lên Nhà hộ sinh Kotobuki, khởi nguồn cho chuỗi bi kịch rợn người. |
| 1-004 | 1 | `1.04#1 – 1.04#2` | 2 | 17.3 | `t26_a1_04_waseda_patrol_subzero_midnight` | ✅ | Hai sĩ quan cảnh sát tuần tra đi bộ qua con hẻm Shinjuku phủ tuyết lạnh buốt rạng sáng 12/1/1948. |
| 1-005 | 1 | `1.04#3 – 1.04#4` | 2 | 17.0 | `t26_a1_05_creepy_undertaker_wooden_cart` | ✅ | Chiếc xe kéo bằng gỗ chở các thùng hàng kín mít bị chặn lại giữa con phố vắng. |
| 1-006 | 1 | `1.04#5 – 1.04#6` | 2 | 14.0 | `t26_a1_06_macabre_crates_grim_discovery` | ✅ | Nắp thùng gỗ hé mở trong ánh đèn pin của cảnh sát, phát hiện bàng hoàng chấn động. |
| 1-007 | 1 | `1.04#7` | 1 | 7.4 | `t26_a1_07_midnight_interrogation_waseda_precinct` | ✅ | Người phu xe bị áp giải về đồn cảnh sát Waseda thẩm vấn khẩn cấp trong đêm. |
| 1-008 | 1 | `1.04#8 – 1.04#9` | 2 | 17.6 | `t26_a1_x01_private_crematorium_van_night_frost` | ✅ | Xe tải dịch vụ hỏa táng tư nhân đỗ đêm giá rét, không người. |
| 1-009 | 1 | `1.06#1` | 1 | 7.7 | `t26_a1_07b_gravedigger_statement_lamplit_bench` | ✅ | Lời khai của người làm nghề mai táng tại đồn: ông chỉ là người được thuê chở các cháu bé tới nơi hỏa táng. |
| 1-010 | 1 | `1.06#2 – 1.06#3` | 2 | 15.9 | `t26_a1_08_kotobuki_clinic_facade_shinjuku` | ✅ | Căn nhà gỗ hai tầng của Nhà hộ sinh Kotobuki tại quận Shinjuku tĩnh lặng đáng ngờ. |
| 1-011 | 1 | `1.06#4 – 1.06#5` | 2 | 15.1 | `t26_a1_09_tokyo_mpd_headquarters_mobilization` | ✅ | Sở Cảnh sát Thủ đô Tokyo kích hoạt cuộc điều tra khẩn cấp cùng đội ngũ pháp y. |
| 1-012 | 1 | `1.06#6` | 1 | 8.2 | `t26_a1_x02_case_folders_connected_by_string` | ✅ | Tường hồ sơ với các tập giấy trống nối nhau bằng sợi chỉ. |
| 1-013 | 1 | `1.07#1 – 1.07#2` | 2 | 10.3 | `t26_a1_10_patrol_officer_inner_shock` | ✅ | Sự bàng hoàng ám ảnh của sĩ quan trẻ đối diện tội ác kinh hoàng giữa mùa đông. |
| 1-014 | 1 | `1.07#3 – 1.07#4` | 2 | 10.1 | `t26_a1_11_suspicious_cart_tracks_in_snow` | ✅ | Vết bánh xe kéo in hằn trên nền tuyết trắng dẫn đến nghi vấn về đường dây tội ác. |
| 1-015 | 1 | `1.07#5 – 1.07#6` | 2 | 10.1 | `t26_a1_12_decision_at_crossroads_justice` | ✅ | Khoảnh khắc quyết định giữ xe kiểm tra, ranh giới cứu vãn sự thật khỏi bị chôn vùi. |
| 1-016 | 1 | `1.07#7` | 1 | 6.3 | `t26_a1_13_forensic_detectives_assembling_dossier` | ✅ | Các thám tử và pháp y bắt tay vào lập hồ sơ vụ án Kotobuki đầy u ám. |
| 1-017 | 1 | `1.07#8` | 1 | 7.7 | `t26_a1_x03_patrol_lantern_silhouette_snowy_street` | ✅ | Bóng người tuần tra với chiếc đèn lồng trên con phố tuyết. |
| 1-018 | 1 | `1.09#1` | 1 | 9.9 | `t26_a1_13b_police_hq_corridor_urgent_arrest_order` | ✅ ⚠ | Ba ngày sau phát hiện trên phố, cảnh sát Tokyo khẩn cấp triển khai lệnh bắt giữ những người điều hành nhà hộ sinh. — ⚠ viền giấy kem 4 mép + tờ giấy dán có chữ giả trên tường trái (H2/H26) |
| 1-019 | 1 | `1.09#2 – 1.09#3` | 2 | 20.1 | `t26_a1_14_kotobuki_raid_dawn_descent` | ✅ | Lực lượng cảnh sát và bác sĩ giám định bất ngờ đột kích vào Nhà hộ sinh Kotobuki. |
| 1-020 | 1 | `1.09#4 – 1.09#5` | 2 | 16.7 | `t26_a1_15_squalid_nursery_ward_neglect` | ✅ | Điều kiện tồi tàn bên trong cơ sở với nôi tre lạnh lẽo và không khí ẩm mốc tang thương. |
| 1-021 | 1 | `1.09#6` | 1 | 8.0 | `t26_a1_16_arrest_of_ishikawa_collaborators` | ✅ | Cảnh sát áp giải các đối tượng liên quan và đối diện người phụ nữ điều hành cơ sở. |
| 1-022 | 1 | `1.09#7` | 1 | 9.9 | `t26_a1_x04_clinic_doorway_warm_lamp_vs_bare_window` | ✅ | Cửa phòng khám sáng đèn ấm đối lập khung cửa sổ trống trải. |
| 1-023 | 1 | `1.10#1` | 1 | 8.0 | `t26_a1_16b_cold_clinic_hallway_unsettling_stillness` | ✅ | Bầu không khí lạnh lẽo, vô cảm đến rợn người khi bước vào nhà hộ sinh Kotobuki. |
| 1-024 | 1 | `1.10#2` | 1 | 8.5 | `t26_a1_17_arrogant_matron_defiant_gaze` | ✅ | Thái độ bình thản, trơ tráo và tự tin kỳ lạ của nữ hộ sinh trước cơ quan điều tra. |
| 1-025 | 1 | `1.10#3` | 1 | 9.6 | `t26_a1_18_charity_facade_false_benevolence` | ✅ | Lời bao biện trơ tráo về cái gọi là 'hành động nhân đạo cưu mang trẻ thơ'. |
| 1-026 | 1 | `1.10#4` | 1 | 6.0 | `t26_a1_19_autopsy_table_scientific_truth` | ✅ | Bàn giám định pháp y của Đại học Tokyo bóc trần nguyên nhân tử vong do bỏ mặc cố ý. |
| 1-027 | 1 | `1.10#5` | 1 | 7.4 | `t26_a1_20_handcuffs_on_clinic_desk` | ✅ | Lệnh bắt giữ khẩn cấp được thực thi ngay trong gian phòng làm việc của nhà hộ sinh. |
| 1-028 | 1 | `1.10#6` | 1 | 9.3 | `t26_a1_x05_unlit_stove_frost_covered_window` | ✅ | Lò sưởi tắt lạnh và ô cửa sổ phủ sương giá trong căn phòng trống. |
| 1-029 | 1 | `1.11#1` | 1 | 8.2 | `t26_a1_21_shinjuku_alley_snow_falling` | ✅ | Tuyết tiếp tục rơi trên con ngõ nhỏ Shinjuku khi sự thật kinh hoàng dần hé lộ. |
| 1-030 | 1 | `1.11#2` | 1 | 6.0 | `t26_a1_22_tragic_mass_dossier_pile` | ✅ | Quy mô nạn nhân kinh hoàng vượt xa mọi dự liệu ban đầu của đội điều tra. |
| 1-031 | 1 | `1.11#3` | 1 | 8.2 | `t26_a1_23_dark_staircase_hidden_horror` | ✅ | Cầu thang gỗ dốc dẫn lên căn gác xép u ám của Nhà hộ sinh Kotobuki. |
| 1-032 | 1 | `1.11#4` | 1 | 10.7 | `t26_a1_24_cold_unlit_stove_abandonment` | ✅ | Lò sưởi than nguội ngắt giữa mùa đông giá rét, minh chứng cho sự thờ ơ tàn nhẫn. |
| 1-033 | 1 | `1.11#5` | 1 | 10.7 | `t26_a1_25_weighing_scale_cold_bureaucracy` | ✅ | Chiếc cân y tế bằng kim loại lạnh lẽo dùng để đo đếm sinh mệnh như hàng hóa. |
| 1-034 | 1 | `1.11#6` | 1 | 8.0 | `t26_a1_26_closed_clinic_curtain_darkness` | ✅ | Tấm rèm vải dày kéo kín che khuất mọi ánh nhìn từ người ngoài vào trong cơ sở. |
| 1-035 | 1 | `1.11#7` | 1 | 8.5 | `t26_a1_27_detective_examining_empty_crib` | ✅ | Điều tra viên đứng lặng trước những chiếc nôi trống rỗng trong niềm xót xa khôn nguôi. |
| 1-036 | 1 | `1.11#8` | 1 | 7.4 | `t26_a1_28_corridor_of_silence_kotobuki` | ✅ | Hành lang tối om dẫn qua các gian phòng khép kín nơi tội ác diễn ra âm thầm. |
| 1-037 | 1 | `1.11#9` | 1 | 9.3 | `t26_a1_29_turning_point_lantern_light` | ✅ | Khoảnh khắc ngọn đèn tuần tra thắp sáng ranh giới giữa vùi lấp tội ác và công lý. |
| 1-038 | 1 | `1.11#10` | 1 | 6.0 | `t26_a1_30_collective_blindspot_symbolic` | ✅ | Góc phố đông người nhưng ai cũng cúi đầu bước qua, biểu tượng cho điểm mù xã hội. |
| 1-039 | 1 | `1.11#11` | 1 | 13.5 | `t26_a1_31_night_watchmen_tokyo_dawn` | ✅ | Những người canh gác màn đêm Tokyo lặng lẽ khép lại ca trực định mệnh. |
| 1-040 | 1 | `1.11#12` | 1 | 8.0 | `t26_a1_x06_tokyo_rooftops_hidden_alley_lamplight` | ✅ | Mái nhà Tokyo về đêm, ánh đèn rạn nứt dọc con hẻm. |
| 2-041 | 2 | `2.02#1 – 2.02#2` | 2 | 20.6 | `t26_a2_01_wartime_black_market_deals` | ✅ | Quy trình trục lợi tinh vi hình thành trong bối cảnh luật cấm phá thai gắt gao thời chiến. |
| 2-042 | 2 | `2.02#3` | 1 | 10.4 | `t26_a2_02_benevolent_facade_charity_trap` | ✅ | Miyuki Ishikawa dựng lên vỏ bọc mái ấm từ thiện để giăng bẫy những gia đình bế tắc. |
| 2-043 | 2 | `2.02#4 – 2.02#5` | 2 | 17.6 | `t26_a2_x01_blank_paper_notice_pinned_clinic_door` | ✅ | Tờ giấy trắng ghim trên cửa phòng khám hợp pháp. |
| 2-044 | 2 | `2.04#1` | 1 | 8.2 | `t26_a2_02b_kind_offer_across_tea_table` | ✅ | Bà ta tiếp cận cặp cha mẹ bế tắc và đưa ra lời đề nghị nghe vô cùng nhân ái. |
| 2-045 | 2 | `2.04#2 – 2.04#3` | 2 | 21.5 | `t26_a2_03_transaction_of_despair_yen_notes` | ✅ | Khoản tiền phí hỗ trợ 4.000 - 5.000 yên được trao tay trong nước mắt và sự tuyệt vọng. |
| 2-046 | 2 | `2.04#4 – 2.04#5` | 2 | 18.1 | `t26_a2_04_tearful_mother_leaving_clinic` | ✅ | Người mẹ nghèo nuốt nước mắt quay lưng rời khỏi nhà hộ sinh, tin vào lời hứa tương lai tốt đẹp. |
| 2-047 | 2 | `2.04#6` | 1 | 8.8 | `t26_a2_05_heavy_door_locks_behind_victim` | ✅ | Cánh cửa gỗ khép lại, khoản tiền rơi vào túi kẻ thủ ác và quy trình bỏ mặc bắt đầu. |
| 2-048 | 2 | `2.04#7` | 1 | 7.7 | `t26_a2_x02_locked_wooden_gate_chain_winter_fog` | ✅ | Cổng gỗ khóa xích trong sương mù mùa đông. |
| 2-049 | 2 | `2.04#8` | 1 | 9.3 | `t26_a2_x03_lavish_room_tea_set_empty_coin_purse` | ✅ | Căn phòng xa hoa với bộ trà, bên cạnh túi tiền rỗng. |
| 2-050 | 2 | `2.06#1` | 1 | 9.6 | `t26_a2_05b_indifferent_empty_desk_no_adoption_search` | ✅ | Vợ chồng Ishikawa hoàn toàn không có ý định chăm sóc hay tìm gia đình nhận nuôi cho bất kỳ đứa trẻ nào. |
| 2-051 | 2 | `2.06#2 – 2.06#3` | 2 | 12.0 | `t26_a2_06_deprived_cribs_unheated_room` | ✅ | Những đứa trẻ bị dồn vào căn phòng ẩm thấp, bị tước đoạt hoàn toàn nguồn sữa và chăm sóc. |
| 2-052 | 2 | `2.06#4 – 2.06#5` | 2 | 19.8 | `t26_a2_07_husband_takeshi_financial_ledger` | ✅ | Người chồng Takeshi Ishikawa quản lý sổ sách tài chính trục lợi tàn nhẫn. |
| 2-053 | 2 | `2.06#6 – 2.06#7` | 2 | 15.9 | `t26_a2_08_corrupt_doctor_nakayama_desk` | ✅ | Bác sĩ Shiro Nakayama ký khống hàng loạt giấy chứng tử để hợp thức hóa các cái chết. |
| 2-054 | 2 | `2.06#8 – 2.06#9` | 2 | 17.3 | `t26_a2_09_fake_death_certificates_pile` | ✅ | Các biên bản báo tử giả mạo với nguyên nhân bệnh lý thông thường chất đống. |
| 2-055 | 2 | `2.06#10 – 2.06#11` | 2 | 26.5 | `t26_a2_10_crematorium_chimney_winter_sky` | ✅ | Ống khói đài hỏa táng ngoại ô Tokyo bốc khói mỏng giữa trời đông u ám. |
| 2-056 | 2 | `2.06#12 – 2.06#13` | 2 | 19.8 | `t26_a2_11_shinjuku_temple_graveyard_records` | ✅ | Cảnh sát rà soát sổ sách mai táng tại các ngôi chùa xung quanh khu vực Shinjuku. |
| 2-057 | 2 | `2.06#14 – 2.06#15` | 2 | 15.1 | `t26_a2_x04_black_doctors_bags_bench_dim_hall` | ✅ | Những chiếc túi da của thầy thuốc xếp dài trong hành lang mờ. |
| 2-058 | 2 | `2.08#1 – 2.08#2` | 2 | 14.5 | `t26_a2_12_detectives_confronting_scale_of_crime` | ✅ | Các điều tra viên bàng hoàng trước con số nạn nhân thực tế lên tới hàng chục sinh mệnh. |
| 2-059 | 2 | `2.08#3` | 1 | 6.8 | `t26_a2_13_interrogation_room_harsh_contrast` | ✅ | Căn phòng thẩm vấn với ánh sáng đối lập gay gắt giữa sự thật và kẻ ngoan cố. |
| 2-060 | 2 | `2.08#4` | 1 | 11.0 | `t26_a2_14_matron_upright_defiance` | ✅ | Miyuki Ishikawa ngồi thẳng lưng, nhìn chằm chằm vào các điều tra viên không chút sợ hãi. |
| 2-061 | 2 | `2.08#5` | 1 | 6.8 | `t26_a2_15_chilling_monologue_justification` | ✅ | Bà ta đưa ra những lập luận ngụy biện rợn người về gánh nặng xã hội và sự giải thoát. |
| 2-062 | 2 | `2.08#6` | 1 | 10.2 | `t26_a2_x05_shuttered_registry_office_counter` | ✅ | Quầy văn phòng hộ tịch đóng cửa, sổ sách trống. |
| 2-063 | 2 | `2.09#1` | 1 | 10.4 | `t26_a2_16_rationalization_of_atrocity` | ✅ | Sự ngụy biện trơ tráo coi hành vi tước đoạt sinh mệnh là một nghĩa cử cứu rỗi. |
| 2-064 | 2 | `2.09#2` | 1 | 9.6 | `t26_a2_17_bureaucratic_callousness_symbol` | ✅ | Sự vô cảm quan liêu biến sinh mệnh con người thành những con số và con dấu khô khốc. |
| 2-065 | 2 | `2.09#3` | 1 | 8.8 | `t26_a2_18_corridor_echoes_of_unheard_cries` | ✅ | Những tiếng khóc yếu ớt không được hồi đáp bên trong gian phòng kín của Kotobuki. |
| 2-066 | 2 | `2.09#4` | 1 | 8.8 | `t26_a2_19_banknotes_hidden_in_tea_box` | ✅ | Tiền trục lợi được cất giấu cẩn thận trong các hộp trà và ngăn tủ gia đình. |
| 2-067 | 2 | `2.09#5` | 1 | 10.7 | `t26_a2_x06_pointing_hand_shadow_courtroom_wall` | ✅ | Bóng bàn tay chỉ tay lớn trên tường phòng xử, người thật nhỏ bé. |
| 2-068 | 2 | `2.10#1` | 1 | 7.1 | `t26_a2_20_forensic_psychiatry_dossier` | ✅ | Tâm thần học pháp y bắt đầu mổ xẻ hiện tượng tha hóa đạo đức của Ishikawa. |
| 2-069 | 2 | `2.10#2` | 1 | 10.4 | `t26_a2_21_historical_context_ruined_society` | ✅ | Bối cảnh lịch sử đổ nát thời hậu chiến làm mờ đi các ranh giới đạo đức thông thường. |
| 2-070 | 2 | `2.10#3` | 1 | 6.8 | `t26_a2_22_masks_of_benevolence_peeling` | ✅ | Lớp mặt nạ từ thiện rơi rụng phơi bày bản chất lạnh lùng của đường dây tội ác. |
| 2-071 | 2 | `2.10#4` | 1 | 9.3 | `t26_a2_23_distorted_definition_of_mercy` | ✅ | Sự đánh tráo khái niệm giữa lòng thương hại và tội ác giết người có tính toán. |
| 2-072 | 2 | `2.10#5` | 1 | 7.4 | `t26_a2_24_shadow_behind_the_curtain_truth` | ✅ | Bóng tối cá nhân được dung dưỡng dưới vỏ bọc hoàn cảnh lịch sử đầy cay đắng. |
| 2-073 | 2 | `2.10#6` | 1 | 7.4 | `t26_a2_25_transition_to_psychological_profiling` | ✅ | Các chuyên gia khoa học hành vi bước vào giải mã nguồn gốc của sự biến dạng tâm lý. |
| 2-074 | 2 | `2.10#7` | 1 | 7.7 | `t26_a2_x07_psychologist_silhouette_blank_profile_board` | ✅ | Bóng nhà tâm lý bên tấm bảng vẽ nghiêng khuôn mặt trống. |
| 3-075 | 3 | `3.02#1 – 3.02#2` | 2 | 22.6 | `t26_a3_01_psychological_case_study_chamber` | ✅ | Hồ sơ Ishikawa dưới lăng kính tâm lý học tội phạm và sự biến dạng nhân cách. |
| 3-076 | 3 | `3.02#3 – 3.02#4` | 2 | 18.1 | `t26_a3_02_mechanisms_of_moral_erosion` | ✅ | Quá trình tha hóa đạo đức diễn ra từng bước thông qua các cơ chế phòng vệ tâm lý. |
| 3-077 | 3 | `3.02#5` | 1 | 8.2 | `t26_a3_x01_descending_staircase_coins_each_step` | ✅ | Cầu thang đi xuống tối, đồng xu rải trên từng bậc. |
| 3-078 | 3 | `3.03#1 – 3.03#2` | 2 | 20.1 | `t26_a3_03_dehumanization_process_concept` | ✅ | Cơ chế Phi nhân tính hóa và Tự biện minh hợp lý hóa của kẻ thủ ác. |
| 3-079 | 3 | `3.03#3 – 3.03#4` | 2 | 20.6 | `t26_a3_04_midwife_compassion_fatigue` | ✅ | Từ một nữ hộ sinh chứng kiến đau khổ cùng quẫn chuyển dần sang vô cảm tuyệt đối. |
| 3-080 | 3 | `3.03#5 – 3.03#6` | 2 | 19.2 | `t26_a3_05_god_complex_fatal_delusion` | ✅ | Ảo tưởng bản thân có quyền quyết định ai được sống, ai nên ra đi vì lợi ích chung. |
| 3-081 | 3 | `3.03#7` | 1 | 8.8 | `t26_a3_06_compartmentalization_dark_mind` | ✅ | Cơ chế chia ngăn tâm lý: ban ngày làm nữ hộ sinh mẫu mực, ban đêm điều hành cỗ máy tử thần. |
| 3-082 | 3 | `3.03#8` | 1 | 9.9 | `t26_a3_x02_white_healer_coat_long_black_shadow` | ✅ | Chiếc áo choàng trắng treo trên móc đổ bóng đen dài. |
| 3-083 | 3 | `3.04#1` | 1 | 7.1 | `t26_a3_06b_compassion_mask_hairline_crack` | ✅ | Sự tự biện minh về lòng trắc ẩn chỉ là lớp vỏ bọc để xoa dịu lương tâm ban đầu. |
| 3-084 | 3 | `3.04#2 – 3.04#3` | 2 | 19.2 | `t26_a3_07_desensitization_habitual_evil` | ✅ | Hiện tượng khử nhạy cảm: khi cái ác lặp lại nhiều lần, sự cắn rứt lương tâm biến mất hoàn toàn. |
| 3-085 | 3 | `3.04#4` | 1 | 7.4 | `t26_a3_x03_abacus_blank_ledger_coins` | ✅ | Bàn tính, quyển sổ trống và những đồng xu. |
| 3-086 | 3 | `3.05#1 – 3.05#2` | 2 | 17.8 | `t26_a3_08_narcissistic_entitlement_greed` | ✅ | Lòng tham trục lợi xâm lấn và lấn át hoàn toàn những vỏ bọc trắc ẩn ban đầu. |
| 3-087 | 3 | `3.05#3 – 3.05#4` | 2 | 16.5 | `t26_a3_09_financial_gain_over_human_life` | ✅ | Sinh mệnh con người bị quy đổi thành tiền mặt phục vụ lối sống xa hoa của vợ chồng thủ ác. |
| 3-088 | 3 | `3.05#5 – 3.05#6` | 2 | 17.8 | `t26_a3_10_moral_disengagement_theory` | ✅ | Thuyết thoái thác đạo đức của Bandura: đổ lỗi cho hoàn cảnh để rũ bỏ trách nhiệm cá nhân. |
| 3-089 | 3 | `3.05#7` | 1 | 10.4 | `t26_a3_11_institutional_blindspot_complicity` | ✅ | Sự đồng lõa của các cơ quan quản lý buông lỏng tạo điều kiện cho tội ác phát triển. |
| 3-090 | 3 | `3.05#8` | 1 | 7.7 | `t26_a3_x04_stack_of_blank_certificates_ink_stamp` | ✅ | Chồng giấy trống và con dấu mực đặt trên bàn. |
| 3-091 | 3 | `3.05#9 – 3.05#10` | 2 | 14.2 | `t26_a3_x05_interlocking_gears_coin_shaped` | ✅ | Bánh răng khớp nhau, một bánh hình đồng xu. |
| 3-092 | 3 | `3.06#1` | 1 | 7.7 | `t26_a3_11b_spotless_hospital_corridor_hidden_rot` | ✅ | Sự bình thường hóa cái ác trong tâm trí Ishikawa tạo nên nghịch lý rùng mình của lịch sử y khoa Nhật Bản. |
| 3-093 | 3 | `3.06#2 – 3.06#3` | 2 | 17.8 | `t26_a3_12_perverted_maternal_archetype` | ✅ | Hình tượng 'người mẹ đen tối' (The Dark Mother) trong tâm lý học cổ mẫu Jungian. |
| 3-094 | 3 | `3.06#4 – 3.06#5` | 2 | 16.5 | `t26_a3_13_callous_unemotional_traits` | ✅ | Đặc điểm nhân cách ái kỷ lạnh lùng triệt tiêu khả năng đồng cảm tự nhiên. |
| 3-095 | 3 | `3.07#1 – 3.07#2` | 2 | 21.5 | `t26_a3_14_societal_indifference_mirror` | ✅ | Tội ác phản chiếu sự thờ ơ của toàn xã hội trước số phận của những đứa trẻ yếu thế. |
| 3-096 | 3 | `3.07#3` | 1 | 9.9 | `t26_a3_15_bureaucratic_normalization_of_death` | ✅ | Cái chết trở thành một thủ tục hành chính thường nhật được đóng dấu qua loa. |
| 3-097 | 3 | `3.07#4` | 1 | 8.8 | `t26_a3_16_dark_triad_machiavellian_cunning` | ✅ | Sự kết hợp giữa thủ đoạn Machiavelli và tính ái kỷ bệnh hoạn trong điều hành đường dây. |
| 3-098 | 3 | `3.07#5` | 1 | 8.0 | `t26_a3_17_manipulation_of_vulnerable_mothers` | ✅ | Kỹ thuật thao túng tâm lý đánh trúng mặc cảm tội lỗi của các sản phụ bần cùng. |
| 3-099 | 3 | `3.07#6` | 1 | 7.4 | `t26_a3_18_clinic_as_death_factory` | ✅ | Cơ sở y tế biến tướng thành một quy trình thanh lý sinh mệnh có hệ thống. |
| 3-100 | 3 | `3.07#7` | 1 | 9.3 | `t26_a3_19_cold_pragmatism_war_mentality` | ✅ | Tâm thức thời chiến: coi mạng người như vật tư tiêu hao trong cuộc chiến sinh tồn. |
| 3-101 | 3 | `3.07#8` | 1 | 11.0 | `t26_a3_20_self_serving_bias_in_confession` | ✅ | Thiên kiến tự phục vụ: luôn coi mình là nạn nhân của thời cuộc thay vì kẻ thủ ác. |
| 3-102 | 3 | `3.07#9` | 1 | 9.3 | `t26_a3_21_pathological_lying_and_charm` | ✅ | Khả năng nói dối bệnh lý và uy tín bằng cấp đại học danh tiếng ru ngủ người ngoài. |
| 3-103 | 3 | `3.07#10` | 1 | 9.9 | `t26_a3_22_erosion_of_medical_oath` | ✅ | Lời thề y đức bị chà đạp dưới đáy vực của lòng tham và sự vô cảm. |
| 3-104 | 3 | `3.07#11` | 1 | 8.0 | `t26_a3_23_social_darwinism_delusion` | ✅ | Ảo tưởng Darwin xã hội: cho rằng chỉ những đứa trẻ có gia đình khá giả mới đáng được sống. |
| 3-105 | 3 | `3.07#12` | 1 | 6.8 | `t26_a3_24_abnormal_lack_of_guilt` | ✅ | Sự thiếu vắng hoàn toàn cảm giác tội lỗi — dấu hiệu kinh điển của rối loạn nhân cách chống đối xã hội. |
| 3-106 | 3 | `3.07#13` | 1 | 11.0 | `t26_a3_25_systemic_failure_warning` | ✅ | Lời cảnh tỉnh: cái ác cá nhân chỉ có thể bùng phát khi cả hệ thống xã hội tê liệt. |
| 3-107 | 3 | `3.07#14` | 1 | 10.4 | `t26_a3_26_closing_the_clinical_dossier` | ✅ | Kết luận hồ sơ tâm lý: cái ác đội lốt quy trình chuyên môn luôn là mối đe dọa lớn nhất. |
| 3-108 | 3 | `3.07#15 – 3.07#16` | 2 | 16.5 | `t26_a3_x06_bowed_silhouette_hiding_face_dock` | ✅ | Bóng người cúi đầu, giấu mặt sau đôi bàn tay trên ghế bị cáo. |
| 3-109 | 3 | `3.08#1` | 1 | 7.4 | `t26_a3_27_courtroom_door_approaching` | ✅ | Bước chuyển từ giải mã tâm lý sang phiên tòa lịch sử đối diện công lý. |
| 3-110 | 3 | `3.08#2` | 1 | 8.8 | `t26_a3_28_public_reckoning_anticipation` | ✅ | Toàn thể xã hội Nhật Bản nín thở chờ đợi phiên xét xử chấn động thời hậu chiến. |
| 3-111 | 3 | `3.08#3` | 1 | 9.6 | `t26_a3_29_scales_of_justice_in_shadow` | ✅ | Cán cân công lý đối diện thách thức phán xét những lỗ hổng chết người của thể chế. |
| 3-112 | 3 | `3.08#4` | 1 | 8.5 | `t26_a3_x07_wall_cracking_under_beam_of_light` | ✅ | Bức tường ngụy biện nứt dưới chùm sáng. |
| 4-113 | 4 | `4.02#1 – 4.02#2` | 2 | 14.5 | `t26_a4_01_tokyo_district_court_1948` | ✅ | Tòa án Quận Tokyo mùa thu năm 1948, phiên tòa sơ thẩm thu hút toàn thể quốc dân. |
| 4-114 | 4 | `4.02#3 – 4.02#4` | 2 | 19.5 | `t26_a4_02_crowded_spectator_gallery_tension` | ✅ | Hàng trăm người dân chen chúc trong phòng xử án, dõi mắt về hàng ghế bị cáo. |
| 4-115 | 4 | `4.02#5 – 4.02#6` | 2 | 16.7 | `t26_a4_03_defendants_dock_trio` | ✅ | Hàng ghế bị cáo: vợ chồng Ishikawa cùng vị bác sĩ làm giả giấy chứng tử cúi đầu. |
| 4-116 | 4 | `4.02#7` | 1 | 8.5 | `t26_a4_x01_courthouse_crowd_silhouettes_winter_dusk` | ✅ | Đám đông bóng người trước tòa án lúc chiều đông. |
| 4-117 | 4 | `4.04#1 – 4.04#2` | 2 | 16.7 | `t26_a4_04_prosecutor_presenting_autopsy_evidence` | ✅ | Công tố viên đưa ra các báo cáo giám định pháp y bác bỏ luận điểm chết do bệnh lý. |
| 4-118 | 4 | `4.04#3 – 4.04#4` | 2 | 14.2 | `t26_a4_05_contract_documents_as_exhibits` | ✅ | Các hợp đồng đóng tiền của cha mẹ nghèo được trưng bày trước tòa như bằng chứng trục lợi. |
| 4-119 | 4 | `4.04#5` | 1 | 8.2 | `t26_a4_x02_closed_exam_file_blank_ledgers_lamp` | ✅ | Hồ sơ khám nghiệm đóng kín bên những quyển sổ trống. |
| 4-120 | 4 | `4.06#1 – 4.06#2` | 2 | 20.1 | `t26_a4_06_corrupt_doctor_testimony_dock` | ✅ | Bác sĩ Shiro Nakayama thừa nhận đã nhận tiền hối lộ để ký khống biên bản báo tử. |
| 4-121 | 4 | `4.06#3 – 4.06#4` | 2 | 12.8 | `t26_a4_07_detectives_solid_evidence_chain` | ✅ | Cơ quan cảnh sát trình bày chuỗi chứng cứ đanh thép về quy trình bỏ đói có tính toán. |
| 4-122 | 4 | `4.06#5 – 4.06#6` | 2 | 18.4 | `t26_a4_08_courtroom_stenographer_typing_speed` | ✅ | Người thư ký tòa ghi chép từng lời khai chấn động của vụ án lịch sử. |
| 4-123 | 4 | `4.06#7` | 1 | 8.0 | `t26_a4_x03_small_wooden_shoes_lined_doorway` | ✅ | Đôi guốc gỗ nhỏ xếp ngay ngắn bên ngưỡng cửa. |
| 4-124 | 4 | `4.08#1 – 4.08#2` | 2 | 11.2 | `t26_a4_09_weeping_mother_witness_stand` | ✅ | Người mẹ mất con nghẹn ngào bước lên bục nhân chứng trong nỗi đau xé lòng. |
| 4-125 | 4 | `4.08#3 – 4.08#4` | 2 | 16.7 | `t26_a4_10_grief_of_postwar_widow` | ✅ | Người mẹ kể lại hoàn cảnh mất chồng ngoài mặt trận và sự tuyệt vọng phải gửi con. |
| 4-126 | 4 | `4.08#5 – 4.08#6` | 2 | 15.6 | `t26_a4_11_clashing_emotions_in_courtroom` | ✅ | Cả khán phòng lặng đi trước nỗi uất hận và tiếng khóc xót xa của các bậc cha mẹ. |
| 4-127 | 4 | `4.08#7 – 4.08#8` | 2 | 19.8 | `t26_a4_12_matron_unmoved_in_dock` | ✅ | Trước những giọt nước mắt của nạn nhân, Miyuki Ishikawa vẫn giữ ánh nhìn lạnh lùng bất động. |
| 4-128 | 4 | `4.08#9 – 4.08#10` | 2 | 21.2 | `t26_a4_13_judge_listening_with_grim_expression` | ✅ | Hội đồng thẩm phán nghiêm nghị lắng nghe lời luận tội cuối cùng. |
| 4-129 | 4 | `4.08#11` | 1 | 7.4 | `t26_a4_x04_hourglass_endless_amber_sand` | ✅ | Chiếc đồng hồ cát với cát hổ phách chảy không dứt. |
| 4-130 | 4 | `4.09#1 – 4.09#2` | 2 | 13.4 | `t26_a4_14_victim_mother_direct_testimony` | ✅ | Lời khai trực tiếp của người mẹ: sự tin tưởng tuyệt đối từng gửi gắm đã bị phản bội cay đắng. |
| 4-131 | 4 | `4.09#3 – 4.09#4` | 2 | 10.9 | `t26_a4_15_revelation_of_deceit_and_shock` | ✅ | Khoảnh khắc người mẹ bàng hoàng nhận ra cơ sở từ thiện thực chất là cỗ máy tử thần. |
| 4-132 | 4 | `4.09#5` | 1 | 5.7 | `t26_a4_16_plea_for_harsh_justice` | ✅ | Tiếng kêu đòi công lý của những người mẹ nghèo vang vọng khắp phòng xử án. |
| 4-133 | 4 | `4.09#6` | 1 | 4.9 | `t26_a4_17_gavel_poised_to_strike` | ✅ | Chiếc búa tòa án nâng lên sẵn sàng cho giờ khắc tuyên án lịch sử. |
| 4-134 | 4 | `4.09#7` | 1 | 4.1 | `t26_a4_18_courtroom_silence_before_verdict` | ✅ | Cả khán phòng nín thở chờ đợi phán quyết cuối cùng của hội đồng xét xử. |
| 4-135 | 4 | `4.09#8` | 1 | 5.7 | `t26_a4_19_historical_verdict_announced` | ✅ | Bản án được tuyên vào tháng 10 năm 1948 khép lại giai đoạn sơ thẩm đầy sóng gió. |
| 4-136 | 4 | `4.09#9` | 1 | 6.3 | `t26_a4_x05_mother_silhouette_steps_worn_shawl` | ✅ | Bóng người mẹ ngồi trên bậc thềm, chiếc khăn cũ trên vai. |
| 4-137 | 4 | `4.10#1` | 1 | 12.1 | `t26_a4_20_controversial_lenient_sentence` | ✅ | Phán quyết 8 năm tù giam sơ thẩm gây ra làn sóng phẫn nộ và tranh cãi dữ dội trong dư luận. |
| 4-138 | 4 | `4.10#2` | 1 | 8.2 | `t26_a4_21_legal_loophole_omission_vs_commission` | ✅ | Lỗ hổng pháp lý thời bấy giờ: khó khăn trong việc quy kết tội giết người trực tiếp cho hành vi bỏ mặc. |
| 4-139 | 4 | `4.10#3` | 1 | 9.1 | `t26_a4_22_high_court_appeal_reduction` | ✅ | Tòa Cấp cao Tokyo sau đó tiếp tục giảm án xuống còn 4 năm tù giam, đỉnh điểm bất bình. |
| 4-140 | 4 | `4.10#4` | 1 | 10.7 | `t26_a4_23_public_outcry_tokyo_streets` | ✅ ⚠ | Làn sóng biểu tình và những bài báo phản đối bản án quá nhẹ khắp các nẻo đường Tokyo. — ⚠ MỚI 25/11 (soi lại): chữ AI trên đầu tàu điện "RELAEL PASSEN" + biển phản đối (H26) — CHỜ quyết định sinh lại |
| 4-141 | 4 | `4.10#5` | 1 | 8.2 | `t26_a4_24_wake_up_call_for_japanese_society` | ✅ | Bản án trở thành cú hích buộc toàn bộ hệ thống lập pháp và xã hội Nhật Bản phải thức tỉnh. |
| 4-142 | 4 | `4.10#6` | 1 | 10.2 | `t26_a4_x06_gavel_ripples_still_water` | ✅ | Chiếc búa tòa và những gợn sóng lan trên mặt nước tĩnh. |
| 4-143 | 4 | `4.11#1` | 1 | 9.9 | `t26_a4_25_eugenic_protection_act_passage` | ✅ | Quốc hội Nhật Bản thông qua Luật Bảo vệ Thể chất năm 1948 hợp pháp hóa việc kiểm soát sinh sản. |
| 4-144 | 4 | `4.11#2` | 1 | 10.4 | `t26_a4_26_transformation_of_child_protection` | ✅ | Sự ra đời của các quy định cấp phép hành nghề hộ sinh ngặt nghèo và mạng lưới bảo trợ trẻ em. |
| 4-145 | 4 | `4.11#3` | 1 | 8.8 | `t26_a4_27_price_paid_in_innocent_blood` | ✅ | Sự thay đổi của thể chế được đánh đổi bằng sinh mệnh của hàng trăm đứa trẻ vô tội. |
| 4-146 | 4 | `4.11#4` | 1 | 8.5 | `t26_a4_x07_old_dim_ward_corridor_into_bright_modern` | ✅ | Hành lang bệnh xá cũ mờ chuyển sang hành lang hiện đại sáng. |
| 4-147 | 4 | `4.12#1` | 1 | 10.4 | `t26_a4_28_iron_bars_and_passage_of_time` | ✅ | Bản án tù giam khép lại nhưng vết thương tâm lý và ký ức lịch sử không bao giờ phai mờ. |
| 4-148 | 4 | `4.12#2` | 1 | 9.1 | `t26_a4_29_eternal_reminder_for_humanity` | ✅ | Lời nhắc nhở muôn đời về nghĩa vụ bảo vệ những sinh mệnh yếu ớt nhất trong xã hội. |
| 4-149 | 4 | `4.12#3` | 1 | 9.3 | `t26_a4_x08_glass_dome_over_empty_wooden_cradle_warm_light` | ✅ | Mái vòm kính che chiếc nôi gỗ trống trong ánh ấm. |
| 5-150 | 5 | `5.02#1 – 5.02#2` | 2 | 18.1 | `t26_a5_01_shinjuku_modern_skyscrapers_dawn` | ✅ | Khu Shinjuku ngày nay sầm uất với những tòa cao ốc chọc trời, xóa nhòa vết tích hoang tàn năm xưa. |
| 5-151 | 5 | `5.02#3 – 5.02#4` | 2 | 19.5 | `t26_a5_02_measure_of_civilized_society` | ✅ | Thước đo văn minh của một xã hội là cách xã hội đó chăm sóc và bảo vệ những đứa trẻ yếu thế nhất. |
| 5-152 | 5 | `5.02#5` | 1 | 9.1 | `t26_a5_x01_candle_before_unmarked_small_stones` | ✅ | Ngọn nến trước những phiến đá nhỏ không khắc chữ. |
| 5-153 | 5 | `5.03#1 – 5.03#2` | 2 | 22.8 | `t26_a5_03_governance_and_uncompromising_oversight` | ✅ | Bài học quản lý nhà nước: tuyệt đối không buông lỏng việc giám sát và thanh tra các cơ sở bảo trợ. |
| 5-154 | 5 | `5.03#3` | 1 | 8.2 | `t26_a5_04_transparency_as_shield` | ✅ | Sự minh bạch và thanh tra đột xuất chính là lá chắn vững chắc bảo vệ sinh mệnh mầm non. |
| 5-155 | 5 | `5.03#4` | 1 | 9.6 | `t26_a5_x02_blank_form_pen_warm_lamp_desk` | ✅ | Tờ giấy trắng và cây bút dưới ngọn đèn ấm. |
| 5-156 | 5 | `5.04#1` | 1 | 10.7 | `t26_a5_04b_predator_shadow_over_struggling_family` | ✅ | Kẻ trục lợi khai thác sự túng quẫn, mặc cảm tội lỗi và thiếu hiểu biết của các gia đình gặp biến cố. |
| 5-157 | 5 | `5.04#2 – 5.04#3` | 2 | 18.1 | `t26_a5_05_wolves_in_sheeps_clothing` | ✅ | Cảnh giác nhận diện những kẻ trục lợi khoác áo nhà từ thiện hảo tâm. |
| 5-158 | 5 | `5.04#4 – 5.04#5` | 2 | 18.7 | `t26_a5_06_independent_verification_principle` | ✅ | Nguyên tắc sinh tồn: không phó thác mù quáng sinh mệnh con em mình cho bất kỳ ai. |
| 5-159 | 5 | `5.04#6 – 5.04#7` | 2 | 18.7 | `t26_a5_07_community_responsibility_network` | ✅ | Xây dựng mạng lưới hỗ trợ cộng đồng chính thống để không ai bị đẩy vào đường cùng. |
| 5-160 | 5 | `5.04#8` | 1 | 15.7 | `t26_a5_08_amber_eyes_four_redflags_overview` | ✅ | Bảng tổng quan 4 Dấu hiệu Cảnh báo Đỏ sinh tồn đúc kết từ hồ sơ Miyuki Ishikawa. |
| 5-161 | 5 | `5.04#9` | 1 | 8.5 | `t26_a5_x03_ring_of_linked_hands_around_small_toys` | ✅ | Vòng tay nối nhau bao quanh vài món đồ chơi nhỏ. |
| 5-162 | 5 | `5.05#1` | 1 | 16.0 | `t26_a5_08b_amber_window_parent_vigilance` | ✅ | Kênh Amber Eyes chia sẻ bốn dấu hiệu cảnh báo đỏ để phụ huynh và cộng đồng nâng cao cảnh giác. |
| 5-163 | 5 | `5.05#2 – 5.05#3` | 2 | 24.0 | `t26_a5_09_redflag1_opaque_unlicensed_operations` | ✅ | Cảnh báo đỏ 1: Cơ sở hoạt động mập mờ, thiếu cấp phép và giám sát độc lập của nhà nước. |
| 5-164 | 5 | `5.05#4 – 5.05#5` | 2 | 20.9 | `t26_a5_10_redflag1_refusal_of_legal_scrutiny` | ✅ | Từ chối cung cấp giấy tờ pháp lý hoặc yêu cầu giao dịch bí mật là dấu hiệu nguy hiểm chết người. |
| 5-165 | 5 | `5.05#6 – 5.05#7` | 2 | 21.2 | `t26_a5_11_redflag2_package_deals_without_accountability` | ✅ | Cảnh báo đỏ 2: Cơ chế thu phí trọn gói với lời hứa hẹn dễ dàng nhưng lảng tránh minh bạch tài chính. |
| 5-166 | 5 | `5.05#8` | 1 | 10.2 | `t26_a5_12_redflag3_restricted_visitation_barriers` | ✅ | Cảnh báo đỏ 3: Hạn chế tiếp xúc, cản trở việc thăm nom và kiểm tra sức khỏe của trẻ em. |
| 5-167 | 5 | `5.05#9` | 1 | 11.8 | `t26_a5_13_redflag3_evasive_complex_scheduling` | ✅ | Liên tục đưa ra lý do né tránh, yêu cầu hẹn trước phức tạp để che giấu thực tế sinh hoạt. |
| 5-168 | 5 | `5.05#10` | 1 | 9.3 | `t26_a5_14_redflag3_absolute_transparency_mandate` | ✅ | Sự minh bạch tuyệt đối và quyền thăm nom không giới hạn là tiêu chuẩn sinh tồn bắt buộc. |
| 5-169 | 5 | `5.05#11` | 1 | 7.7 | `t26_a5_15_redflag4_parental_abandonment_syndrome` | ✅ | Cảnh báo đỏ 4: Tâm lý phó mặc và buông xuôi trách nhiệm của chính các bậc cha mẹ. |
| 5-170 | 5 | `5.05#12` | 1 | 9.9 | `t26_a5_16_redflag4_false_promises_consequences` | ✅ | Tin vào những lời hứa hão huyền để trút bỏ gánh nặng đã vô tình tiếp tay cho thảm kịch. |
| 5-171 | 5 | `5.05#13` | 1 | 13.8 | `t26_a5_17_seeking_legitimate_social_support` | ✅ | Luôn chủ động tìm kiếm sự hỗ trợ từ các tổ chức xã hội chính thống thay vì tin kẻ lạ. |
| 5-172 | 5 | `5.05#14` | 1 | 8.5 | `t26_a5_18_primacy_of_child_protection` | ✅ | Quyền được sống và sự an toàn của trẻ em là ưu tiên tối thượng của mọi gia đình và xã hội. |
| 5-173 | 5 | `5.05#15` | 1 | 9.9 | `t26_a5_19_amber_eyes_dossier_closing_tribute` | ✅ | Khép lại tập hồ sơ Miyuki Ishikawa với tấm lòng tri ân và giá trị nhân văn sâu sắc. |
| 5-174 | 5 | `5.05#16` | 1 | 11.8 | `t26_a5_20_call_to_action_community_safety` | ✅ | Lời kêu gọi đồng hành cùng Amber Eyes lan tỏa tri thức vì một cộng đồng an toàn cho trẻ em. |
| 5-175 | 5 | `5.05#17` | 1 | 6.0 | `t26_a5_21_tokyo_cherry_blossom_dawn_peace` | ✅ | Hoa anh đào nở rộ trên đường phố Tokyo đón ánh bình minh, biểu tượng của hòa bình và công lý. |
| 5-176 | 5 | `5.05#18` | 1 | 3.0 | `t26_a5_x04_warm_lit_home_window_quiet_night` | ✅ | Ô cửa sổ ngôi nhà sáng đèn ấm trong đêm yên tĩnh. |
