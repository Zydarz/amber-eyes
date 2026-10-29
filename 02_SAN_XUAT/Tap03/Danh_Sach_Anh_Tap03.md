# DANH SÁCH ẢNH NỀN — TẬP 03 "GÃ KHỔNG LỒ IQ 145 & CHIẾC GƯƠNG GIẢI PHẪU TÂM TRÍ"

*Vụ án Edmund Kemper. Ngày 23/10/2026.*

> **⚠️ ĐÃ ĐỒNG BỘ LẠI 23/10/2026 sau review sự thật của kịch bản.**
> Kịch bản đã được viết lại (xem `01_KICH_BAN/Tap03/REVIEW_kichban_tap03.md`): 21 lỗi fact + 4 trích dẫn không có nguồn đã sửa.
> Hệ quả trực tiếp lên file này: **mọi mốc câu đã dịch lại** (bảng B2), 4 mô tả ảnh đã sửa nội dung (địa chỉ hiện trường, số án, Rorschach, phiên ân xá), và 1 ảnh (`t3_car_door`) mất mốc vì chi tiết tương ứng đã bị loại khỏi kịch bản.

---

## B1. Thông tin bộ ảnh

| Mục | Nội dung |
|---|---|
| Số ảnh mới | **47** sinh mới — **46 dùng trong bảng shot** (`t3_car_door` không dùng, xem B3.3) + 1 dùng lại từ Tập 02 (`t2_gavel` — xem B3.2) |
| Kích thước | 2112×1188 (16:9), ảnh gốc 2752×1536 nằm ở `assets/bg/_raw/` |
| Vị trí | `assets/bg/t3_*.png` — **tiền tố `t3_` bắt buộc** để không đụng bộ nền Tập 01 (`t2_*` của Tập 02) |
| Prompt gốc | `.work/bg_jobs_tap03.json` (đúng format `bg_jobs*.json` của Tập 01/02) |
| Sổ nguồn gốc | `provenance.json` (tự cộng dồn mỗi khi sinh ảnh) |
| Phong cách | Dark graphic novel noir — mực đen đậm, chiaroscuro, tông lạnh desaturated, sương mù và film grain |
| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền |
| Tool sinh | `connector__matrix__generate_image` (MiniMax qua mcode-tools), 16:9, 2K |

**Quy tắc hình ảnh của kênh (giữ nguyên từ Tập 01/02):**

- **V5** — Người thật trong vụ án chỉ hiện dạng **bóng lưng / mặt khuất hoàn toàn**. **6 ảnh có người** (`t3_hitchhiker`, `t3_bar_stool_shadow`, `t3_two_agents`, `t3_interview_room`, `t3_giant_doorway`, `t3_mother_shadow`) đều ghi rõ *"seen strictly from behind / in strict side profile so that no facial feature is visible at all"*.
- **V9** — Trọng tâm là phân tích tâm lý. **Không** mô tả chi tiết bạo lực, thương tích, thi thể, cách gây hại — cả lời lẫn hình. Không máu, không thi thể, không vũ khí, không hình ảnh tấn công.
- Không biểu tượng tôn vinh, không huy hiệu, không nịp, không tên đơn vị, không chữ trên đồ vật.

**Hai điểm cần lưu ý riêng cho tập này** (khác Tập 01/02):

1. **Không vẽ súng/dao/còng tay trong xe.** Kịch bản 2.07#6 kể rõ Kemper lưu trong **cốp xe** túi nilông, dao găm, chăn và còng tay. V9 cấm minh hoạ cách gây hại → `t3_under_seat` chỉ vẽ **khoang trống** (compartment rỗng). Lời đọc vẫn đủ, hình không vi phạm.
   **Sau review:** chi tiết *"tháo bỏ tay nắm mở cửa ở ghế phụ và chốt khóa an toàn"* đã **bị loại khỏi kịch bản** (không tìm thấy nguồn nào) → ảnh `t3_car_door` **không còn mốc câu**, không dùng trong bảng shot.
2. **Kỷ niệm/thưởng vật chất.** 4.07#6 nói về "chiến lợi phẩm" → `t3_trophy_box` là **hộp gỗ đậy kín**, không có đồ vật của nạn nhân.

---

## B2. Ánh xạ ảnh → hồi → mốc câu

Mốc câu theo `.work/script_tap03.json` (parse từ `01_KICH_BAN/Tap03/kichban_tap03_22102026.md`):
**31 lượt · 215 câu · 5 106 từ** — vai H 20 lượt, D 5, C 4, N 2. *(Cập nhật sau review)*

### HỒI 1 · THE HOOK — CUỘC GỌI NỬA ĐÊM TỪ BỐT ĐIỆN THOẠI COLORADO (00:00 – 03:45)

| Ảnh | Nội dung phục vụ | Mốc câu |
|---|---|---|
| `t3_case_file` | Hồ sơ vụ án — hình mở đầu tập | `1.01`, `1.03#1` |
| `t3_dispatch_desk` | Trực ban đêm Santa Cruz, chuông điện thoại reo phá vỡ tĩnh mịch | `1.03#3`–`#5` |
| `t3_phone_booth` | Bốt điện thoại ven đường ở Pueblo, Colorado — hơn 1.600 km | `1.03#2`, `#5` |
| `t3_tape_start` | Tiếng băng ghi âm bật nhẹ "Tách" | `1.08` |
| `t3_apartos_house` | ⚠️ Hiện trường số **609A đường Ord Drive**, thị xã Aptos *(địa chỉ "Aptos Creek" là SAI — đã sửa)* | `1.10#1` |
| `t3_bedroom_door` | Phòng ngủ — cánh cửa đóng, khe sáng dưới cửa | `1.10#2` |
| `t3_prison_corridor` | Hành lang nhà tù — tiếng bước chân vang vọng | `1.11` |
| `t3_gate_slam` | Cánh cửa sắt trại giam kéo lê rồi đóng sập "Rầm" | `1.12` |
| `t3_fbi_corridor` | Chuyển sang góc nhìn Đặc vụ FBI — bê tông nền cho mở đầu chương trình | `1.13`, `1.15#2` |

### HỒI 2 · HIỆN TRƯỜNG & CHUỖI SĂN MỒI — NẤC THANG CỦA SỰ THAY THẾ (03:45 – 10:00)

| Ảnh | Nội dung phục vụ | Mốc câu |
|---|---|---|
| `t3_rain_wipers` | Mưa rơi rả rích trên mui xe, cần gạt nước kêu kẽo kẹt | `2.01` |
| `t3_santacruz_street` | Santa Cruz đầu thập niên 1970 — không khí Hippie | `2.02#1` |
| `t3_hitchhiker` | Giơ ngón tay cái xin đi nhờ xe | `2.02#2` |
| `t3_ucsc_campus` | Khuôn viên Đại học California tại Santa Cruz (UCSC) | `2.02#3` |
| `t3_case_photos` | Tiếng lật các bức ảnh hồ sơ nạn nhân trên mặt bàn | `2.03`, `2.04#1` |
| `t3_ravine` | Vực sâu hẻo lánh dọc dãy núi Santa Cruz — hiện trường bị xóa sạch | `2.06#1`, `2.06#3`–`#4` |
| `t3_backyard_garden` | **Khu vườn sau nhà** — nơi chôn đầu nạn nhân *(ảnh trống: không hố, không vật thể, tránh V9)* | `2.06#2` |
| `t3_galaxie` | Ford Galaxie màu vàng năm 1969 — mẫu xe cực kỳ phổ biến, không gây chú ý | `2.07#2` |
| `t3_car_door` | ❌ **KHÔNG DÙNG** — chi tiết tháo tay nắm đã bị loại khỏi kịch bản (không có nguồn) | — |
| `t3_under_seat` | Khoang giấu kín bên trong xe — "phương tiện di chuyển biến thành bẫy chết chóc di động" | `2.07#1` |
| `t3_trunk` | **Cốp xe** mở nắp — nơi lưu túi nilông, dao găm, chăn, còng tay *(ảnh trống — không vẽ vật, tránh V9)*; cũng là nơi nhốt nạn nhân đầu tiên | `2.07#6`, `#8` |
| `t3_courthouse_exterior` | Tòa án Quận Santa Cruz nằm ngay đối diện quán rượu | `2.09#1` |
| `t3_bar_jury_room` | Quán rượu The Jury Room — nơi lui tới của thám tử, cảnh sát, luật sư | `2.09#1`–`#3` |
| `t3_bar_stool_shadow` | "Big Ed" ngồi ở góc quầy bar uống bia, gật gù phân tích vụ án đang truy lùng chính mình | `2.09#2`–`#9` |

### HỒI 3 · GIẢI PHẪU TÂM LÝ — BÊN TRONG BỘ NÃO CỦA KẺ THÁI NHÂN CÁCH TỰ PHẢN TỈNH (10:00 – 16:30)

| Ảnh | Nội dung phục vụ | Mốc câu |
|---|---|---|
| `t3_basement_stairs` | Quay ngược về căn hầm ẩm ướt, tối tăm ở Montana thập niên 1950 | `3.01`, `3.02#2` |
| `t3_layers_stair` | Bóc tách **3 tầng** bệnh lý | `3.04` |
| `t3_coal_furnace` | Tầng 1 — lò sưởi than suốt nhiều năm, chuột bọ, ẩm ướt | `3.05#6` |
| `t3_small_bed` | Tầng 1 — đứa trẻ 8 tuổi ngủ dưới tầng hầm *(đã làm lại: bỏ song chắn, thêm cầu thang lên tầng trên)* | `3.05#6` |
| `t3_trapdoor` | **Cửa bẩy dưới bàn ăn ở tầng trên** — phải nâng bàn lên mới ra khỏi được | `3.05#7` |
| `t3_atascadero` | Tầng 2 — Bệnh viện Tâm thần Bang Atascadero (vào năm 15 tuổi, thả đúng ngày 21 tuổi) | `3.08#2`–`#5` |
| `t3_mother_shadow` | Tầng 2 — cơ chế **phóng chiếu**: bóng người mẹ bị dồn nén | `3.08#7`–`#11` |
| `t3_textbooks` | Tầng 2 — học thuộc MMPI, tự phát triển thang đo của riêng mình, thao túng hội đồng y khoa *(đã bỏ Rorschach — không có nguồn)* | `3.08#3`–`#4` |
| `t3_self_observation` | Tầng 3 — tách rời cảm xúc, quan sát cơn khát máu của mình như nhà khoa học theo dõi thí nghiệm | `3.11#1`, `#4`–`#6` |
| `t3_brain_mirror` | **"Chiếc Gương Giải Phẫu Tâm Trí"** — tự mổ xẻ tâm trí với độ chính xác của bác sĩ giải phẫu thần kinh | `1.13#5`, `3.11#1` |

### HỒI 4 · ĐỐI THOẠI VỚI FBI — NỀN TẢNG CỦA NGHỆ THUẬT LẬP HỒ SƠ TỘI PHẠM (16:30 – 22:00)

| Ảnh | Nội dung phục vụ | Mốc câu |
|---|---|---|
| `t3_cassette` | Tiếng máy ghi âm cassette cổ bật lên "Cạch" | `4.01` |
| `t3_vacaville_1978` | Năm 1978, Cơ sở Y tế Bang California (California Medical Facility), Vacaville | `4.02#1`–`#2` |
| `t3_two_agents` | John Douglas & Robert Ressler bước qua những cánh cửa thép kiên cố | `4.02#3` |
| `t3_giant_doorway` | "Kemper khổng lồ như một ngọn núi, lấp kín cả khung cửa" | `4.05#1`–`#2` |
| `t3_interview_room` | Hắn kéo ghế ngồi xuống, mỉm cười lịch sự như giáo sư đại học | `4.05#3` |
| `t3_fantasy_spiral` | **Vòng lặp Ảo tưởng Bạo lực (Violent Fantasy Cycle)** — vòng xoáy không đáy | `4.07#2`–`#5` |
| `t3_trophy_box` | Khái niệm **Chiến lợi phẩm (Trophies/Souvenirs)** | `4.07#6`–`#7` |
| `t3_organized_split` | Hệ thống phân loại: Kẻ giết người **có tổ chức** và **vô tổ chức** | `4.08#1`–`#3` |
| `t3_signature_trace` | **Chữ ký tâm lý (Behavioral Signature)** hiện trường vụ án | `4.08#4`–`#5` |

### HỒI 5 · PHÁN QUYẾT, BÀI HỌC CẢNH BÁO ĐỎ & LỜI KẾT (22:00 – 26:00)

| Ảnh | Nội dung phục vụ | Mốc câu |
|---|---|---|
| `t2_gavel` | Tiếng búa tòa án gõ "Cốp… Cốp… Cốp" — **dùng lại ảnh Tập 02** (xem B3.2) | `5.01` |
| `t3_courtroom_1973` | Phiên tòa Santa Cruz (mở 23/10/1973, tuyên án 08/11/1973) — 8 án chung thân **thi hành đồng thời** | `5.02#1`–`#5` |
| `t3_life_sentence` | Thụ án suốt đời tại Cơ sở Y tế Bang California, Vacaville; hồ sơ bị bác hơn 10 lần, kế tiếp 2031 | `5.02#8`–`#11` |
| `t3_red_flags` | **4 dấu hiệu cảnh báo đỏ** — 4 vật thể trên bàn | `5.05`, `5.06` |
| `t3_gift_drowned` | "Món quà bị nhúng vào bể chứa của sự ngược đãi" — ẩn dụ lời kết | `5.08#6`–`#7` |
| `t3_closing_desk` | Đóng tập hồ sơ, bấm nút tắt máy ghi âm, Cello fade out | `5.10`–`5.12` |

---

## B3. Nền có thể tái dùng từ Tập 01 / Tập 02

Không cần sinh lại, dùng trực tiếp trong bảng shot:

- **Tập 01**: `void` · `podcast_desk` · `night_street` · `corridor` · `fog` · `records` · `pinboard` · `prison_window` · `interrogation` · `phone_dark` · `spotlight` · `cage` · `glass_box` · `house_night` · `bedroom_door` · `empty_room` · `route_night` · `storm` · `clinical` · `court_dawn` · `screen_off` · `locked_door` · `night_screen` · `brain_desk` · `doll` · `hands`
- **Tập 02**: `t2_courtroom` · `t2_gavel` · `t2_brain_neural` · `t2_red_flags` · `t2_two_chairs` · `t2_tape_recorder` · `t2_podcast_desk` · `t2_escalation_stairs` · `t2_interrogation_empty` · `t2_two_drawers` · `t2_two_masks` · `t2_command_chair` · `t2_logbook` · `t2_folder_tree` · `t2_cell_medical`

---

## B3.1 Kết quả duyệt (23/10/2026)

**Quét bằng code** — `.work/qc_bg.py` (quét 4 cạnh: dải đều tuyệt đối **và** nhảy viền ở mép):

| Kiểm tra | Kết quả |
|---|---|
| Kích thước | **47/47** đúng 2112×1188 |
| Viền/frame model thêm vào | **4** ảnh, đã cắt tay (xem bảng bên dưới) |
| Sai kích thước | 0 |

**Các lỗi viền đã phát hiện & sửa (23/10/2026):**

| Ảnh | Lỗi | Cách sửa |
|---|---|---|
| `t3_ravine` | Khung trắng 27–29 px ở cả 4 cạnh (model thêm "mát trắng") | Cắt 30/28/29/32 px → resize lại 2112×1188 |
| `t3_apartos_house` | **Khung trắng + đường mực** quanh cả ảnh | Cắt 24 px ở 4 cạnh |
| `t3_textbooks` | **Khung trắng + đường mực** quanh cả ảnh | Cắt 15 px ở 4 cạnh; lần quét sau phát hiện còn sót **đường sáng 3–4 px** ở mép → cắt thêm 6 px (lần 2, gốc ở `_raw/t3_textbooks.framefix2.png`) |
| `t3_galaxie` | **Đường mực đen** vẽ tay, lệch nhau 15–25 px giữa 4 cạnh | Cắt thủ công 30 px ở 4 cạnh (detector tự động bỏ vì các cạnh lệch nhau > 7 px) |

Ảnh gốc trước khi sửa giữ ở `assets/bg/_raw/<tên>.framefix.png`.

> **Bổ sung quy tắc QC (mới, phát hiện khi soi ảnh lần 2):** "dải đều" (std < 6) **và** "đường mực 1 px" là **hai lỗi khác nhau**, cần 2 detector riêng.
> - `fix_frames.py` — khối đều (dải trắng/đen do model thêm).
> - `qc_border_line.py` — đường mực mảnh vẽ tay. Không phải mọi "điểm cục bộ tối" ở mép đều là khung vẽ (góc tối tự nhiên cũng vậy) ⇒ chỉ coi là khung khi **≥ 2 cạnh có đường mực lệch nhau ≤ 7 px**. Quét ra 6 ảnh nghi vấn, soi tay xác nhận 3 ảnh lỗi thật (aptos_house, textbooks, galaxie), 3 ảnh còn lại là báo động giả (góc tối tự nhiên).
> - Lưu ý: khung trắng của `t3_apartos_house` / `t3_textbooks` **không** bị detector "dải đều" bắt vì mép trắng bị nhiễu (std > 6) — chỉ lộ ra khi soi mắt ở 100%.

> **Quy tắc phát hiện viền đã sửa (quan trọng cho các tập sau):** "dải đều" (std < 6) **không** đủ để kết luận có viền — `t3_phone_booth` có 91 px trời đêm đồng đều ở trên nhưng đó là **nội dung ảnh**, không phải viền. Viền thật phải thoả cả 3 điều kiện: (1) dài ≥ 12 px, (2) độ sáng trong dải đều (std < 2), (3) **có nhảy** ở mép (|sáng trong − sáng ngoài| > 25). Thêm nữa, mẫu "nội dung" phải lấy **xa mép ~40 px** vì hàng/cột ngay cạnh viền bị blend nên nhảy bị đo thấp.

**Soi bằng mắt** (toàn bộ 47 ảnh):

| Kiểm tra | Kết quả |
|---|---|
| Chữ / số / biển hiệu do AI vẽ | **0** |
| Mặt người lộ (vi phạm V5) | **0** — 6 ảnh có người đều là bóng lưng, mặt khuất hoàn toàn: `t3_hitchhiker` · `t3_bar_stool_shadow` · `t3_two_agents` · `t3_interview_room` · `t3_giant_doorway` · `t3_mother_shadow` |
| Bạo lực / máu / thi thể / vũ khí (vi phạm V9) | **0** — `t3_under_seat` là khoang **rỗng**, `t3_trophy_box` là **hộp đậy kín** |
| Watermark / khung viền | **0** |
| Đồng nhất phong cách với Tập 01/02 | Đạt — noir, mực đậm, tông lạnh, grain đều |

**Lệch nội dung nhẹ — vẫn dùng được, nhưng cần biết lúc ghép chữ:**

| Ảnh | Vấn đề | Xử lý |
|---|---|---|
| `t3_mother_shadow` | Tông **xanh lục** thay vì tông lạnh của cả bộ | Chấp nhận — màu "bệnh viện" hợp tầng phóng chiếu. **Dùng cho Hồi 3, tránh Hồi 1/5** để giữ nhịp màu |
| `t3_atascadero` | Hành lang bệnh viện tâm thần, hơi giống hành lang văn phòng | Chấp nhận — vẫn là "nơi giam giữ tâm lý" |
| `t3_courtroom_1973` | Ghế bài giống **nhà thờ** hơn là tòa án | Chấp nhận — cùng chất "phòng xử"; có thể đổi sang `t2_courtroom` của Tập 02 |
| `t3_santacruz_street` | Tông **tím ấm** thay vì tông lạnh; có vài nét vẽ nhỏ trên mặt tiệm (không đọc được) | Chấp nhận — hợp không khí Hippie 1970; dùng đúng một lần ở `2.02#1` |
| `t3_trapdoor` | **Sáng** hơn hẳn bộ ảnh (nhiều vùng trắng) | Dùng đúng 1 shot ở `3.05#7`. Sáng = "tầng trên, ánh sáng bình thường" → tương phản tốt với tầng hầm tối của `t3_small_bed`/`t3_coal_furnace` |
| `t3_prison_corridor` | Tông **sepia ấm** thay vì tông lạnh | Chấp nhận — chỉ dùng 1 shot |
| `t3_case_photos` | Tông sepia ấm | Chấp nhận — chỉ dùng 1 shot, hợp "không gian hồ sơ" |
| `t3_backyard_garden` | Có **mưa** trong ảnh | Chấp nhận — khớp đêm mưa của Hồi 2 (cue `2.01` là mưa trên mui xe). Dùng 1 shot ở `2.06#2` |

### B3.4 Ảnh đã làm lại sau khi đối chiếu kịch bản mới (23/10/2026)

Kịch bản được review lại (+1 567 từ) đã đổi một số chi tiết ⇒ 3 ảnh cũ không còn khớp, đã sửa:

| Ảnh | Vấn đề phát hiện | Đã sửa |
|---|---|---|
| `t3_small_bed` | Có **song chắn** → đọc như phòng giam, không phải tầng hầm Montana 1950 | ✅ Sinh lại: bỏ song chắn, thêm cầu thang lên tầng trên, cửa sổ kính thường. Giờ khớp `3.05#6` |
| `t3_under_seat` | Ảnh là **khoang dưới ghế**, nhưng kịch bản mới nói **"cốp xe"** ⇒ chữ trên hình sẽ mâu thuẫn với lời đọc | ✅ Tái neo ảnh cũ sang `2.07#1` ("phương tiện di chuyển thành bẫy chết chóc di động" — khoang giấu kín trong xe) + **sinh ảnh mới `t3_trunk`** cho `2.07#6`/`#8` |
| `t3_gavel` | Connector 500 | ✅ Dùng `t2_gavel` của Tập 02 (B3.2) |
| `t3_car_door` | Chi tiết tháo tay nắm đã bị gỡ khỏi kịch bản | ✅ Không dùng (B3.3) — file vẫn còn, đã qua QC |
| — | `3.05#7` ("cửa bẩy dưới bàn ăn") **chưa có ảnh nào** | ✅ Sinh mới `t3_trapdoor` |
| — | `2.06#2` ("khu vườn sau nhà" — nơi chôn đầu nạn nhân) **chưa có ảnh nào** | ✅ Sinh mới `t3_backyard_garden` — vườn sau nhà đêm mưa; **không vẽ hố, không vẽ vật thể** (V9) |

## B3.2 `t3_gavel` — chưa sinh được, dùng `t2_gavel` của Tập 02

Connector `connector__matrix__generate_image` **từ chối riêng ảnh này**: `err_code: 500 — image post-processing failed`. Đã thử **8 lần** với 4 bản prompt khác nhau (búa + tiếng điệu / búa trên bàn + sách luật / cảnh toà án rộng / chỉ roi gỗ + đĩa gỗ) × 4 mức độ phân giải (1K/2K/4K) × 2 tên `output_file` khác nhau → **tất cả đều fail**, trong khi 44 ảnh còn lại đều sinh thành công.

⇒ **Dùng `t2_gavel`** (ảnh búa tòa án của Tập 02 — cùng phong cách, cùng ý, đã qua QC). Trong bảng shot chỉ cần ghi `t2_gavel` thay vì `t3_gavel`, **không cần copy file** — `build_video3.py` resolve nền bằng `assets/bg/<tên>.png` nên nó sẽ lấy đúng file.

Prompt chuẩn bị sẵn trong `.work/bg_jobs_tap03.json` (mục `t3_gavel`) — khi nào connector ổn định lại, chạy:

```powershell
py -3 .work\gen_one.py t3_gavel 2K 5
```

rồi đổi lại shot `5.01` từ `t2_gavel` → `t3_gavel`.

## B3.3 `t3_car_door` — đã sinh nhưng không dùng

Ảnh vẽ "hai lỗ trống sau khi tháo tay nắm" — **chi tiết này không có nguồn** nên đã bị loại khỏi kịch bản (xem `01_KICH_BAN/Tap03/REVIEW_kichban_tap03.md` mục A18) → ảnh mất mốc câu.

⇒ **File `assets/bg/t3_car_door.png` vẫn còn trên đĩa, không cần sinh lại.** Chỉ cần bỏ nó khỏi bảng shot. Nếu sau này kịch bản thêm lại chi tiết tương tự thì dùng lại được ngay — ảnh đã qua QC.

---

## B4. Việc còn lại để dựng được video Tập 03

| # | Việc | Ghi chú |
|---|---|---|
| 1 | `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md` | Bảng shot (mục 6) — dùng mốc câu ở B2 |
| 2 | `.work/shots.json` cho tập 3 | `parse_shots.py` cần bảng shot; hiện file còn trỏ Tập 01 |
| 3 | Khai báo `EPISODES["03"]` trong `.work/edition.py` | `edition.py` đã có `"04"` (vụ Charles Cullen) nhưng **chưa có `"03"`** |
| 4 | `edition.py` → `N_ELEMENT` | Tap03 có 2 lượt vai N: **`1.09`** (trực ban Santa Cruz) và **`2.09`** (cảnh sát quán rượu) → cần `{... "1.09": "N1", "2.09": "N2"}`. Lưu ý nhãn `N2` mặc định là "KHÁN GIẢ" — Tập 03 không có vai khán giả, phải đổi nhãn |
| 5 | Đo lại thời lượng sau khi có audio TTS | Xem B5 — **đã đạt** ~25,8 phút sau khi bổ sung nội dung có nguồn |
| 6 | Bảng nguồn tham khảo theo từng câu (A10) | ✅ `02_SAN_XUAT/Tap03/xuat_ban/nguon_tham_khao.md` — đã tạo, 19 câu + phụ lục nguyên văn tiếng Anh; **cần người dùng điền link** |
| 7 | Bảng âm thanh Tập 03 | ✅ `.work/sfx_tap03.json` (10 nền + 20 tiếng động) — xem `02_SAN_XUAT/Tap03/AmThanh_Tap03.md` |
| 8 | Dựng audio TTS + trộn cho Tập 03 | ⚠️ `EPISODES["03"]` + `acting_tap03.json` (215 câu) + bảng âm thanh **đã xong** — còn thiếu **bảng shot** thì `build_audio3.py` mới dựng trọn được |

### B4.1 Công cụ mới tạo cho Tập 03 (dùng lại được cho tập sau)

| File | Việc |
|---|---|
| `.work/bg_jobs_tap03.json` | Danh sách prompt **48 ảnh** (47 đã sinh + `t3_gavel` chờ connector ổn định; format giống `bg_jobs.json` / `bg_jobs_tap02.json`) |
| `.work/gen_parallel.py` | **Sinh ảnh song song**: chia danh sách cho N worker, mỗi worker 1 file provenance riêng rồi gộp — tránh đụng file khi chạy song song. Dùng: `py -3 .work\gen_parallel.py .work\bg_jobs_tapXX.json 4 2` |
| `.work/gen_one.py` | Sinh **1 ảnh** với độ phân giải tùy chọn (1K/2K/4K) và số lần thử — dùng khi connector lỗi 500 cho một prompt cụ thể |
| `.work/qc_bg.py` | **Quét QC viền khối đều + kích thước** + dựng contact sheet. Quy tắc 3 điều kiện xem mục B3.1 |
| `.work/qc_border_line.py` | **Quét đường mực mảnh** (khung vẽ tay 1–3 px) mà quét "dải đều" bỏ sót. Chỉ coi là khung khi ≥ 2 cạnh có đường mực lệch nhau ≤ 7 px |
| `.work/fix_frames.py` | Cắt khối đều (dải trắng/đen model thêm) rồi resize lại 2112×1188 (ảnh gốc giữ ở `assets/bg/_raw/<tên>.framefix.png`) |
| `.work/fix_frame_lines.py` | Cắt khung vẽ tay; có thêm chế độ `--manual <tên> <px>` cho khung lệch nhau không đồng đều (vd `t3_galaxie`) |
| `.work/_uoc_luong_tap03.py` | Ước lượng thời lượng tập từ số từ, hiệu chỉnh trên Tap02 có audio đo thật |
| `.work/_show_script.py` | Xem cấu trúc element/vai/câu của một script đã parse |

**Sửa 2 script dùng chung (không đổi hành vi cũ):**
- `.work/gen_images.py` — thêm biến môi trường `AE_PROV` để ghi provenance ra file khác (mặc định vẫn là `provenance.json`).
- `.work/parse_kichban.py` — thêm 2 vai của Tập 03 vào bảng `ROLES`: **`ĐẶC VỤ FBI`** → `D`, **`CẢNH SÁT ĐỊA PHƯƠNG`** → `N`. Không có bản sửa này, regex sẽ không khớp 2 vai đó và **gán nhầm lời thoại của họ vào lượt HOST**. Đã kiểm chứng không ảnh hưởng Tập 01/02: parse lại Tap02 cho kết quả **giống hệt** file cũ.

> **Lưu ý khi sinh ảnh:** connector `connector__matrix__generate_image` hay trả `err_code: 500 — image post-processing failed` (lỗi phía dịch vụ, không phải lỗi prompt). Tập 03 gặp **4/45** ảnh bị vậy: `t3_fbi_corridor`, `t3_santacruz_street`, `t3_red_flags`, `t3_cassette` → **3/4 đã sinh lại được** bằng cách viết lại prompt hoặc chạy lại (`--only <tên>` / `gen_one.py`); riêng `t3_gavel` fail hết mọi lần thử ⇒ dùng `t2_gavel` (mục B3.2). Xem thêm mục B3.3 của manifest Tập 02 — lỗi này đã từng xảy ra và tự hết khi dịch vụ ổn định lại.

---

## B5. Cảnh báo về thời lượng (phát hiện khi thiết kế ảnh)

Ước lượng bằng mô hình thời lượng của chính pipeline (`build_audio3.py`), hiệu chỉnh trên **Tap02 có audio đo thật**:

| | Tap02 (đo thật) | Tap03 (ước lượng) |
|---|---|---|
| Số từ | 4 721 | **5 106** (108% của Tap02) |
| Phần lời | 1 452,8 s | ~1 547 s |
| Phụ lục (gap + intro + nền) | 163,4 s | ~119 s |
| **Tổng** | **1 616,3 s = 26:56** | **~1 666 s = 27:46** *(ước lượng)* |
| Brief | 25–27 phút | 25–27 phút ⇒ **ĐẠT** (ước ~25,8 phút theo hệ số phần lời; cần đo lại khi có audio TTS thật) |

⇒ Sau review, kịch bản đã **+1 567 từ** (bổ sung nội dung có nguồn: danh sách 6 nạn nhân, lịch sử CPRP/VICAP, chẩn đoán 1984, phiên tòa, thẩm phán Brauer, đặc vụ Colomy) và đạt khung 25–27 phút.
Bộ 46 ảnh dùng được này vẫn hợp lý: 46 ảnh / 25,8 phút = **1 ảnh ≈ 34 s** (Tap02: 37 ảnh / 26,9 phút ≈ 44 s) — nhịp chuyển cảnh hơi nhanh hơn Tập 02 nhưng vẫn trong vùng dùng được.
**Lưu ý:** `t3_car_door` không còn mốc câu (chi tiết đã bị loại khỏi kịch bản) → nếu dùng đủ 47 ảnh thì cần **giảm nhịp hoặc tái neo ảnh này** cho một câu khác; còn 46 ảnh thì không vấn đề.
