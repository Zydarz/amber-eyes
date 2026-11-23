# HỒ SƠ SẢN XUẤT TẬP 25 · "SÁT NHÂN ÁO MƯA & CƠN CUỒNG NỘ THÙ HẬN XÃ HỘI" — VI EDITION

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 25: Sát Nhân Áo Mưa & Cơn Cuồng Nộ Thù Hận Xã Hội — Vỏ Bọc Tự Ti & Tội Ác Đội Lốt Phán Xét (Hồ Sơ Yoo Young-chul)** |
| Vụ án | Hồ sơ chuỗi án mạng Seoul của Yoo Young-chul (Seoul, Hàn Quốc, 2003–2004) |
| Chủ đề tâm lý | Mặc cảm tự ti chuyển hóa thành thù hận xã hội (*Sociopathic Resentment*) · Tổn thương ái kỷ (*Narcissistic Injury*) · Hung hăng dịch chuyển (*Displaced Aggression*) · Ảo tưởng phán xét đạo đức (*Moral Vigilante Delusion*) · Kỹ thuật trung hòa đạo đức (*Moral Neutralization*) · Cơ chế ăn năn chân chính vs Tự thương hại bệnh lý |
| Định dạng | Podcast Tài liệu Phân tích Tâm lý Tội phạm (Host-Driven Documentary) — 5 Hồi chuẩn A2/K10 |
| Cấu trúc phân vai | 4 Giọng đọc: **Host** (Cú vọ - 95 câu) · **Điều tra viên** (Chó săn - 28 câu) · **Chuyên gia Tâm lý** (Cáo bạc - 27 câu) · **Người bình thường** (N1 Chủ cơ sở massage: 7 câu & N2 Đại diện gia đình nạn nhân: 8 câu) |
| Quy mô kịch bản gốc | **165 câu thoại** · 51 phần tử (Elements) · 32 lượt thoại |
| Quy mô nghiên cứu bổ sung | Bản nghiên cứu & bổ sung 10 chỉ dấu tâm lý hành vi (`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/NghienCuu_TamLy_BoSung_KichBan_Tap25.md`) ngày 15/11/2026 cho 3 ngôn ngữ (VN / EN / JA) |
| Tiêu chuẩn an toàn | **Tuân thủ tuyệt đối Quy tắc V9 (YouTube Safe)**: 0% mô tả bạo lực gore, máu me hay xâm hại thân thể; 100% tập trung phân tích khoa học hành vi và 4 cảnh báo đỏ nhận diện nguy cơ |
| Tài nguyên hình ảnh | **60 ảnh nền chuẩn 2112×1188 (16:9 2K)** tiền tố `t25_` tại `assets/bg/` · Phong cách Dark Graphic Novel Noir |
| Bộ nhạc nền (BGM) | Cello u buồn $\rightarrow$ Deep Ambient lạnh lẽo $\rightarrow$ Minimalist Piano học thuật $\rightarrow$ Violin trầm hùng tòa án $\rightarrow$ Warm Piano đúc kết nhân văn |

---

## B2. Kế hoạch Triển khai & Đồng bộ Đa ngôn ngữ (Pipeline Roadmap)

### 1. Đồng bộ Hồ sơ & Tư liệu Tham khảo (Đã hoàn tất)
- [x] Thẩm tra dữ kiện lịch sử & pháp lý đạt độ chính xác 100% qua hồ sơ SMPA, Tòa án Tối cao Hàn Quốc và tư liệu Profiler Kwon Il-yong (`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/REVIEW_kichban_tap25.md`).
- [x] Hoàn thiện bản nghiên cứu chuyên sâu 5 chủ thể (Kẻ thủ ác, Đồng phạm vô thức/Nạn nhân, Nhân chứng quả cảm, Gia đình nạn nhân, Người dân đô thị) và khung lời thoại bổ sung 3 ngôn ngữ (`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/NghienCuu_TamLy_BoSung_KichBan_Tap25.md`).
- [x] Cập nhật bộ mô tả video YouTube (`mo_ta.txt`, `description.txt`) và nguồn đối chiếu kiểm chứng (`nguon_tham_khao.md`) cho 3 ngôn ngữ VN / EN / JA.

### 2. Các bước Sản xuất Tiếp theo (Cổng kiểm theo `AGENTS.md`)
1. **Bước 1 (Duyệt kịch bản):** Người dùng duyệt nội dung bổ sung chiều sâu tâm lý; tích hợp vào kịch bản chính thức `kichban_tap25_23102026.md` và các bản dịch `EN`, `JA`.
2. **Bước 2 (Tách kịch bản):** Biên dịch kịch bản sang `.work/script_tap25.json`, `.work/script_tap25_EN.json`, `.work/script_tap25_JA.json`.
3. **Bước 3 (Diễn xuất & Nhịp nghỉ):** Tạo file diễn xuất `acting_tap25.json` (đo khoảng câm và nhịp nghỉ theo cổng `qc_pause_gate.py`).
4. **Bước 4 (Tổng hợp giọng đọc TTS):** Chạy đọc giọng 4 vai qua Higgs Audio v3 / MiniMax theo cấu hình `CAST` của `edition.py`.
5. **Bước 5 (Kiểm định giọng theo vai):** Chạy `voice_role_check.py` đảm bảo 1 vai 1 chất giọng đồng nhất.
6. **Bước 6 (Master Audio):** Trộn 3 lớp âm thanh (Voice + SFX + BGM) đạt chuẩn EBUR128 (-16 LUFS, TP $\le -1.5$ dBFS).
7. **Bước 7 (Bảng shot):** Khớp 100% câu thoại với 60 ảnh nền dùng chung `t25_*` qua `parse_shots.py`.
8. **Bước 8 (Dựng hình & Đóng gói):** Render video bằng `build_video3.py` và đóng gói phụ đề srt qua `package.py --mux`.

---

## B3. Cấu trúc 5 Hồi Chi tiết & Danh mục Ảnh Nền Liên kết

Bộ ảnh nền 60 ảnh (`assets/bg/t25_*.png`) được phân bổ chặt chẽ theo nhịp kịch bản 5 hồi:

### HỒI 1: CƠN ÁC MỘNG ÁO MƯA VÀNG & NHỮNG BÓNG MA SAU CÁNH CỬA BIỆT THỰ SEOUL (12 ảnh)
- `t25_yoo_young_chul_a1_01_mapo_police`: Toàn cảnh Seoul đầu thập niên 2000 & Đồn cảnh sát Mapo trong đêm mưa.
- `t25_yoo_young_chul_a1_02_bongwon_temple`: Cổng chùa Bongwon tĩnh mịch trong sương mù.
- `t25_yoo_young_chul_a1_03_sociopathic_resentment`: Bóng dáng kẻ đột nhập áo mưa vàng trước cổng biệt thự Sinsa-dong.
- `t25_yoo_young_chul_a1_04_narcissistic_injury`: Khu biệt thự Gugi-dong và Samsung-dong dưới ánh đèn đường hiu hắt.
- `t25_yoo_young_chul_a1_05_displaced_aggression`: Phòng khách biệt thự vắng bóng người, tài sản nguyên vẹn.
- `t25_yoo_young_chul_a1_06_moral_vigilante_delusion`: Xe tuần tra cảnh sát tuần tra dày đặc các ngõ ngách Seoul.
- `t25_yoo_young_chul_a1_07_moral_neutralization`: Con phố Sinchon sầm uất với ánh đèn neon mờ ảo trong mưa.
- `t25_yoo_young_chul_a1_08_sinchon_massage_seoul`: Căn phòng dịch vụ massage tại gia ấm cúng nhưng đơn sơ.
- `t25_yoo_young_chul_a1_09_officetel_mapo_seoul`: Bàn làm việc của chủ cơ sở massage rà soát lại sổ nhật ký cuộc gọi.
- `t25_yoo_young_chul_a1_10_kwon_il_yong_profiler`: Màn hình điện thoại hiển thị cùng một dãy số gọi đến nhiều lần.
- `t25_yoo_young_chul_a1_11_seoul_mansion_crime_scene`: Lối ra ga Sinchon lúc nửa đêm, nhóm nhân chứng mật phục cùng cảnh sát.
- `t25_yoo_young_chul_a1_12_escape_police_station_rain`: Khoảnh khắc khống chế kẻ mặc áo mưa vàng trong đêm mưa 15/07/2004.

### HỒI 2: CUỘC ĐÀO TẨU CHỚP NHOÁNG & SỰ TRƠ TRÁO SAU CHIẾC MẶT NẠ PHÁN XÉT (12 ảnh)
- `t25_yoo_young_chul_a2_01_handcuff_interrogation`: Phòng hỏi cung đồn cảnh sát Mapo rạng sáng 16/07/2004.
- `t25_yoo_young_chul_a2_02_glass_door_broken`: Cánh cửa kính đồn cảnh sát bị tông vỡ trong cuộc đào tẩu chớp nhoáng.
- `t25_yoo_young_chul_a2_03_seoul_red_alert_grid`: Cảnh sát Seoul giăng lưới báo động đỏ phong tỏa các nhà ga và bến xe.
- `t25_yoo_young_chul_a2_04_yeongdeungpo_station_overpass`: Cầu vượt ga Yeongdeungpo nơi kẻ đào tẩu bị khống chế trở lại.
- `t25_yoo_young_chul_a2_05_narcissistic_smirk_confession`: Nụ cười ngạo mạn lạnh lùng trong phòng thẩm vấn đặc biệt.
- `t25_yoo_young_chul_a2_06_bongwon_mountain_map`: Tờ giấy vẽ sơ đồ các điểm chôn cất trên sườn núi chùa Bongwon.
- `t25_yoo_young_chul_a2_07_rainy_digging_hillside`: Cuộc khai quật quy mô lớn trên sườn đồi Bongwon dưới trời mưa tầm tã.
- `t25_yoo_young_chul_a2_08_eleven_victims_marked`: Dây phong tỏa hiện trường vàng chăng ngang cánh rừng tĩnh mịch.
- `t25_yoo_young_chul_a2_09_officetel_crime_lab`: Căn phòng officetel nhỏ hẹp ở Mapo ngổn ngang công cụ pháp y.
- `t25_yoo_young_chul_a2_10_reconstruction_stride`: Yoo Young-chul bước đi điềm tĩnh chỉ dẫn thực nghiệm hiện trường.
- `t25_yoo_young_chul_a2_11_media_frenzy_cap_mask`: Rừng ống kính phóng viên và ánh đèn flash bủa vây kẻ sát nhân.
- `t25_yoo_young_chul_a2_12_raincoat_killer_myth`: Chiếc áo khoác mưa màu vàng, mũ bóng chày xanh và tuyên ngôn trơ trẽn trước truyền thông.

### HỒI 3: GIẢI MÃ TÂM LÝ: THÙ HẬN XÃ HỘI (SOCIOPATHIC RESENTMENT) & CƠ CHẾ ĐỔ LỖI NGOẠI HÓA (12 ảnh)
- `t25_yoo_young_chul_a3_01_profiler_dialogue`: Bàn đối thoại tâm lý học tội phạm giữa Profiler Kwon Il-yong và Yoo Young-chul.
- `t25_yoo_young_chul_a3_02_childhood_poverty_jeolla`: Căn nhà mái tôn nghèo khó tại vùng quê tỉnh Jeolla những năm 1970.
- `t25_yoo_young_chul_a3_03_colorblind_art_dream`: Hộp màu vẽ dở dang và giấc mơ trường nghệ thuật tan vỡ vì chứng mù màu.
- `t25_yoo_young_chul_a3_04_fourteen_convictions_record`: Tập hồ sơ tiền án dày đặc mười bốn lần ra vào trại giam.
- `t25_yoo_young_chul_a3_05_prison_divorce_papers`: Lá đơn ly hôn và cánh cửa trại giam khép lại năm 2002.
- `t25_yoo_young_chul_a3_06_rejection_rage_mirror`: Tấm gương vỡ phản chiếu sự tự ti và cơn thịnh nộ ái kỷ bị tổn thương.
- `t25_yoo_young_chul_a3_07_displaced_aggression_diagram`: Sơ đồ giải phẫu cơ chế Hung hăng dịch chuyển (Displaced Aggression).
- `t25_yoo_young_chul_a3_08_class_resentment_divide`: Bức tường phân cách giữa những tòa nhà chọc trời hào nhoáng và khu ổ chuột.
- `t25_yoo_young_chul_a3_09_dehumanization_mask`: Chiếc mặt nạ vô cảm biến tha nhân thành công cụ phục vụ ảo tưởng quyền lực.
- `t25_yoo_young_chul_a3_10_moral_neutralization_scales`: Cán cân công lý bị bóp méo bởi ảo tưởng trừng phạt ngầm.
- `t25_yoo_young_chul_a3_11_god_complex_arrogance`: Ảo tưởng toàn năng và sự ngộ nhận về vị thế "đấng phán xét tối cao".
- `t25_yoo_young_chul_a3_12_pathological_self_pity`: Bóc trần sự đối lập giữa Ăn năn chân chính và Tự thương hại bệnh lý.

### HỒI 4: BẢN ÁN TỬ HÌNH & PHÁN QUYẾT NGHIÊM MINH CỦA CÔNG LÝ (12 ảnh)
- `t25_yoo_young_chul_a4_01_seoul_central_court`: Toàn cảnh Tòa án Quận Trung tâm Seoul mùa thu năm 2004.
- `t25_yoo_young_chul_a4_02_tight_security_perimeter`: Vành đai an ninh nghiêm ngặt bao quanh phòng xét xử trước đám đông phẫn nộ.
- `t25_yoo_young_chul_a4_03_dock_defiance`: Yoo Young-chul ngồi trước vành móng ngựa với thái độ lạnh lùng thách thức.
- `t25_yoo_young_chul_a4_04_prosecutor_forensic_binder`: Bàn công tố viên trưng bày các tập hồ sơ giám định ADN dày đặc.
- `t25_yoo_young_chul_a4_05_cell_tower_records`: Bản đồ dữ liệu định vị các cột sóng viễn thông và lịch sử cuộc gọi.
- `t25_yoo_young_chul_a4_06_unshakable_evidence`: Các bản ảnh hiện trường và vật chứng khoa học không thể chối cãi.
- `t25_yoo_young_chul_a4_07_grieving_families_tears`: Hàng ghế thân nhân nạn nhân nghẹn ngào trong nỗi đau đớn tột cùng.
- `t25_yoo_young_chul_a4_08_victim_representative_voice`: Đại diện gia đình nạn nhân đứng lên cất tiếng nói đòi lại phẩm giá cho người đã khuất.
- `t25_yoo_young_chul_a4_09_judge_gavel_verdict`: Búa tòa gỗ gõ dứt khoát trên bàn chủ tọa phòng xét xử.
- `t25_yoo_young_chul_a4_10_death_penalty_pronouncement`: Phán quyết tử hình lịch sử ngày 13/12/2004 vang vọng phòng xử án.
- `t25_yoo_young_chul_a4_11_seoul_detention_center`: Trại giam Seoul nơi kẻ tử tù đang bị giam giữ biệt lập.
- `t25_yoo_young_chul_a4_12_justice_restored`: Ánh bình minh le lói trên mái tòa án, khép lại chương tăm tối tư pháp.

### HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ NHẬN DIỆN NHÂN CÁCH THÙ HẬN XÃ HỘI (12 ảnh)
- `t25_yoo_young_chul_a5_01_modern_seoul_skyline`: Seoul hiện đại ngày nay với hệ thống an ninh thông minh và phố xá rực sáng.
- `t25_yoo_young_chul_a5_02_community_vigilance_cooperation`: Tinh thần cảnh giác và sự chủ động phối hợp giữa người dân và cảnh sát.
- `t25_yoo_young_chul_a5_03_gradual_escalation_pyramid`: Kim tự tháp phân tích sự hình thành và tích tụ nhân cách thù hận xã hội.
- `t25_yoo_young_chul_a5_04_red_flag_1_external_blame`: Biểu đồ nhận diện Cảnh báo đỏ 1 — Thói quen đổ lỗi và hằn học xã hội.
- `t25_yoo_young_chul_a5_05_red_flag_2_misogyny_bullying`: Biểu đồ nhận diện Cảnh báo đỏ 2 — Kỳ thị, coi thường và bắt nạt người yếu thế.
- `t25_yoo_young_chul_a5_06_red_flag_3_isolated_locations`: Biểu đồ nhận diện Cảnh báo đỏ 3 — Nhận việc tại không gian kín đáo thiếu bảo trợ.
- `t25_yoo_young_chul_a5_07_red_flag_4_moral_threats`: Biểu đồ nhận diện Cảnh báo đỏ 4 — Ảo tưởng phán xét và đe dọa thanh trừng người khác.
- `t25_yoo_young_chul_a5_08_safety_protocol_freelancers`: Hướng dẫn an toàn thực tế: Chia sẻ vị trí trực tiếp và từ chối điểm hẹn đáng ngờ.
- `t25_yoo_young_chul_a5_09_community_empathy_healing`: Sự gắn kết thấu cảm và trách nhiệm tương trợ trong cộng đồng đô thị.
- `t25_yoo_young_chul_a5_10_amber_eyes_philosophy`: Biểu tượng kênh Amber Eyes trên nền ấm áp, lan tỏa tri thức tự bảo vệ.
- `t25_yoo_young_chul_a5_11_candlelight_tribute`: Ngọn nến lung linh tưởng niệm phẩm giá của hai mươi nạn nhân vô tội.
- `t25_yoo_young_chul_a5_12_outtro_subscribe_card`: Khung thẻ kết Outtro kênh Amber Eyes kêu gọi đăng ký và bảo vệ cộng đồng.

---

## B4. Danh mục Tệp Thành phẩm & Tài liệu Sản xuất

| Tệp tin | Thư mục lưu trữ | Trạng thái |
|---|---|:---:|
| `KeHoach_Video_Tap25.md` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25/` | ✅ Mới lập & Chuẩn hóa |
| `KeHoach_Video_Tap25_EN.md` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25_EN/` | ✅ Đã lập (Bản Anh) |
| `KeHoach_Video_Tap25_JA.md` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25_JA/` | ✅ Đã lập (Bản Nhật) |
| `mo_ta.txt` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25/` & `xuat_ban/` | ✅ Đã cập nhật chuẩn hóa |
| `description.txt` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25_EN/` & `Tap25_JA/` | ✅ Đã cập nhật chuẩn hóa |
| `nguon_tham_khao.md` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25/` & các bản `_EN`, `_JA` | ✅ Đã cập nhật đối chiếu |
| `Danh_Sach_Anh_Tap25.md` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25/` | ✅ Đầy đủ 60 ảnh 2K |
| `REVIEW_Bo_Anh_Tap25.md` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25/` | ✅ 100% Đạt QC |
| `contact_sheet_t25.png` | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25/` | ✅ Contact sheet tổng quan |
