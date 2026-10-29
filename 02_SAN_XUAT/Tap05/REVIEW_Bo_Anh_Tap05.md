# BÁO CÁO THẨM ĐỊNH & REVIEW CHẤT LƯỢNG BỘ ẢNH NỀN TẬP 05
## "CHIẾC ĐĨA MỀM MÀU TÍM & CƠN NGHIỆN ÁI KỶ" (DENNIS RADER — BTK)

*Ngày lập báo cáo: 23/10/2026. Dự án: Podcast Tài liệu Phân tích Tâm lý Tội phạm Amber Eyes.*

---

## I. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

| Tiêu chí | Kết quả thẩm định | Trạng thái | Ghi chú kỹ thuật |
|---|:---:|:---:|---|
| **Số lượng ảnh** | **61 / 61 ảnh** | **ĐẠT (100%)** | Đúng 100% danh sách trong `.work/bg_jobs_tap05.json` |
| **Kích thước & Tỷ lệ** | **2112 × 1188 (16:9 2K)** | **ĐẠT (100%)** | 61/61 ảnh full-bleed, không viền đen letterbox |
| **Kiểm tra viền & Khung vẽ (QC)** | **0 lỗi còn lại** | **ĐẠT (100%)** | Đã tự động crop & chuẩn hóa 3 ảnh có viền khung (`altar`, `archives`, `divide`) |
| **Sổ nguồn gốc (`provenance.json`)** | **61 / 61 bản ghi** | **ĐẠT (100%)** | Đầy đủ metadata prompt, công cụ MiniMax, kích thước gốc |
| **Độ sáng trung bình (Mean Luminance)** | **63.6 / 255** | **ĐẠT CHUẨN NOIR** | Dải chuẩn của kênh: 50.0 – 120.0 |
| **Độ tương phản (Chiaroscuro Std)** | **51.3** | **XUẤT SẮC** | Độ sâu chiaroscuro cao, phân định sáng - tối sắc nét |
| **Tuân thủ quy tắc V5 (Nhân vật thật)** | **100% Bóng lưng / Khuất mặt** | **ĐẠT (100%)** | Tuyệt đối không vẽ mặt thật Dennis Rader, Ken Landwehr |
| **Tuân thủ quy tắc V9 (An toàn nội dung)** | **100% Không bạo lực, máu me** | **ĐẠT (100%)** | Trọng tâm tĩnh vật pháp y, hồ sơ, đĩa mềm, máy móc |
| **Bảng tổng hợp (Contact Sheet)** | **Đã xuất bản** | **HOÀN THÀNH** | `02_SAN_XUAT/Tap05/contact_sheet_t5.png` (1920 × 3198) |

---

## II. PHÂN TÍCH QUANG HỌC & ĐẶC TÍNH THỊ GIÁC

Dữ liệu trích xuất từ phân tích ma trận điểm ảnh toàn bộ 61 file `assets/bg/t5_*.png`:

1. **Phân bổ sắc độ (Luminance Distribution):**
   - **Ảnh tối nhất:** `t5_btk_signature_metaphor.png` (Mean = 32.3, cảnh ẩn dụ cuộn dây thừng và đồng hồ cát trong bóng tối).
   - **Ảnh sáng nhất:** `t5_park_city_suburb.png` (Mean = 119.9, khung cảnh mùa đông băng giá phủ tuyết trắng ngoại ô Park City).
   - **Phân bổ dải trung bình:** 85% số ảnh tập trung ở khoảng $45 - 85$, tạo nên bầu không khí trinh sát ngột ngạt, bí ẩn và u tối đặc trưng của dòng phim tài liệu noir thập niên 80–2000.
2. **Độ tương phản Chiaroscuro:**
   - 100% ảnh có độ lệch chuẩn sắc độ ($Std$) $> 29.0$, giá trị cực đại đạt $83.1$ (`t5_two_faces_silhouette.png`) và $81.3$ (`t5_closing_typewriter_rose.png`).
   - Mọi khung hình đều có sự tương phản mạnh mẽ giữa các mảng đen mực đậm (ink lines) và các vệt sáng vàng hổ phách (amber lamp) hoặc xanh phosphor lạnh (cyan screen).
3. **Không có hiện tượng bệt đen hoặc cháy sáng:**
   - Số ảnh có $Mean < 30.0$: **0 ảnh**.
   - Số ảnh có $Mean > 180.0$: **0 ảnh**.
   - Số ảnh thiếu tương phản ($Std < 25.0$): **0 ảnh**.

---

## III. ĐÁNH GIÁ MẠCH KỂ THỊ GIÁC (VISUAL STORYTELLING) THEO 5 HỒI

### 1. Hồi 1: The Hook — Bức thư tái xuất sau 13 năm (14 ảnh)
- **Điểm sáng:** Bắt đầu bằng không gian lạnh giá của thành phố Wichita (`t5_wichita_skyline_dusk`), dẫn nhập vào tòa soạn báo đêm (`t5_eagle_newsroom_night`), cận cảnh phong bì màu vàng và tấm bằng lái cũ (`t5_manila_envelope_polaroids`).
- **Khắc họa cái tôi ái kỷ:** Hình ảnh chiếc máy đánh chữ cổ (`t5_vintage_typewriter_desk`), kho án nguội phủ bụi 13 năm (`t5_cold_case_archives`) và chiếc gương nứt vỡ (`t5_narcissist_mirror_shadow`) tạo điểm tựa thị giác hoàn hảo cho lập luận về sự tổn thương lòng tự tôn ái kỷ của hung thủ trước cuốn sách của Robert Beattie.
- **Tuân thủ V5:** Cảnh viên chức đo bãi cỏ (`t5_compliance_truck_street`) và hai thám tử trước bảng tác chiến (`t5_detective_war_room`) đều nhìn từ sau lưng, giữ khoảng cách khách quan.

### 2. Hồi 2: Hiện trường & Hồ sơ — Chữ ký tâm lý con thú hai mặt (13 ảnh)
- **Hình tượng hóa tâm lý học hành vi:** Cảnh đường dây điện thoại bị cắt (`t5_darkened_house_exterior`) và chiếc hộp cất giấu chiến lợi phẩm (`t5_trophy_lockbox`) khắc họa chính xác khái niệm "Chiến lợi phẩm cảm xúc" (Emotional Souvenirs) của FBI.
- **Sự phân đôi rợn người:** Tái hiện trung thực vỏ bọc xã hội đáng kính của Rader qua góc kỷ niệm Không quân (`t5_air_force_service_era`), Nhà thờ Lutheran Chúa Kitô (`t5_lutheran_church_exterior`, `t5_church_council_altar`), lửa trại hướng đạo sinh (`t5_scout_camp_campfire`) đối lập với chiếc thước dây đo cỏ khắc nghiệt (`t5_compliance_measuring_tape`).
- **Khép lại ấn tượng:** `t5_two_faces_silhouette` tạo nên cú ngắt hình thị giác mạnh mẽ trước khi bước vào phần giải phẫu tâm thần.

### 3. Hồi 3: Giải phẫu tâm lý — Bộ não ái kỷ ác tính (9 ảnh)
- **Ẩn dụ hóa các khái niệm trừu tượng:**
  - *Sự phân mảnh tâm trí:* Chiếc tủ thuốc cổ điển nhiều ngăn kéo khóa kín (`t5_compartmentalization_cabinet`) và bức tường bê tông chia cắt căn phòng (`t5_concrete_wall_divide`).
  - *Ảo tưởng Nhân tố X (Factor X):* Chiếc ghế đơn độc với bóng ma đen trườn trên tường (`t5_factor_x_shadow`).
  - *Cơ chế Phóng chiếu:* Chiếc mặt nạ sứ trắng bên gương vỡ (`t5_projection_mask`).
  - *Cơn nghiện chú ý:* Chiếc ngai vàng da bành dưới ánh đèn spotlight (`t5_narcissistic_throne`) và cuốn sổ lưu niệm dán báo vụ án (`t5_secret_scrapbook`).

### 4. Hồi 4: Đấu trí thẩm vấn & Bẫy công nghệ đĩa mềm (15 ảnh)
- **Tái hiện chính xác hiện trường điều tra thực tế:**
  - Bãi đỗ xe Home Depot Wichita mùa đông (`t5_winter_home_depot`).
  - Hộp ngũ cốc Kellogg's trên thùng xe bán tải (`t5_cereal_box_pickup`).
  - Dòng tin nhắn mật trên mục rao vặt 494 ("Rex, it will be OK") (`t5_newspaper_classified_494`).
  - Đĩa mềm Memorex 1.44MB màu tím (`t5_purple_floppy_disk`).
- **Đột phá kỹ thuật số:**
  - Phòng pháp y EnCase (`t5_digital_forensics_lab`) và màn hình trích xuất Metadata "Dennis / Christ Lutheran Church" (`t5_metadata_screen`).
  - Mẫu ADN phết tế bào y tế Pap smear của Kerri Rawson (`t5_dna_pap_smear_vial`).
- **Đỉnh cao kịch tính & Nhân văn:**
  - Cảnh bắt giữ trên xa lộ trưa 25/02/2005 (`t5_highway_takedown_arrest`).
  - Cuộc đối chất Ken Landwehr — Dennis Rader qua bàn thẩm vấn (`t5_interrogation_confrontation`).
  - Nỗi đau sụp đổ tuổi thơ của người con gái Kerri Rawson (`t5_kerri_rawson_tears`).

### 5. Hồi 5: Phán quyết, 4 Cảnh báo đỏ & Lời kết (10 ảnh)
- **Tính nghiêm minh của pháp luật:** Phòng xét xử Quận Sedgwick (`t5_sedgwick_courtroom`), tiếng búa tuyên phạt 10 án chung thân liên tiếp (`t5_judge_gavel_verdict`), nhà tù El Dorado (`t5_el_dorado_prison`) và buồng biệt giam vĩnh viễn (`t5_solitary_confinement_cell`).
- **Trực quan hóa 4 Cờ đỏ (Red Flags):** 4 ảnh tĩnh vật hình học (`t5_redflag_rule_control`, `t5_redflag_shallow_affect`, `t5_redflag_secret_trophies`, `t5_redflag_narcissistic_hubris`) hỗ trợ trực quan đắc lực cho lời thoại đúc kết của Chuyên gia tâm lý và Điều tra viên.
- **Cái kết nhân văn:** Chiếc đĩa mềm đón ánh bình minh (`t5_justice_dawn_sunlight`) và chiếc máy đánh chữ nằm im bên đóa hoa hồng trắng (`t5_closing_typewriter_rose`) tạo cảm giác thanh thản, giải thoát và trang trọng.

---

## IV. BẢO TRÌ VÀ KHUYẾN NGHỊ DỰNG VIDEO

1. **Tương thích Pipeline dựng:**
   - Bộ ảnh hoàn toàn sẵn sàng cho script dựng hình `build_video3.py` khi cấu hình `AE_EP=05`.
   - Độ phân giải dư 10% (2112×1188 so với khung hình xuất bản 1920×1080) cho phép các hiệu ứng lia máy, zoom chậm (Ken Burns effect) mà không bị vỡ hạt hay lộ mép đen.
2. **Đã xử lý dứt điểm các lỗi biên:**
   - Các file có viền trắng do mô hình sinh ảnh vẽ thêm đều đã được cắt xén chính xác và nội suy LANCZOS về kích thước chuẩn.
3. **Đánh giá chung:**
   - Bộ ảnh đạt chất lượng nghệ thuật cao nhất trong các tập từ trước đến nay, bám sát từng chi tiết của hồ sơ lịch sử Cảnh sát Wichita và FBI BSU.
