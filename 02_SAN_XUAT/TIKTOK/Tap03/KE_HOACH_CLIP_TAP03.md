# KẾ HOẠCH CLIP TIKTOK — TẬP 03 · "GÃ KHỔNG LỒ IQ 145 & CHIẾC GƯƠNG GIẢI PHẪU TÂM TRÍ"

*Ngày: 20/11/2026 · Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*
*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap03/SPEC_AUDIO_CLIP_TAP03.json`*
*Nguồn duy nhất của mọi dữ kiện: `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md` · `.work/script_tap03.json` (220 câu) · `02_SAN_XUAT/Tap03/nguon_tham_khao.md`*
*Sinh tự động bởi `.work/_build_tk_tap03.py` — sửa kịch bản thì sửa file script rồi chạy lại, không sửa tay.*

---

## 0. Tóm tắt chốt

| Hạng mục | Giá trị |
|---|---|
| Số clip | **5 clip** (TK1–TK4 chính + TK5 clip kết / bài học sinh tồn) |
| Tổng câu | **51 câu** đọc giọng |
| Độ dài | Ước lượng 64.8–75.1 s/clip (mục tiêu 65–90 s · cổng QC 45–95 s) |
| Chủ đề | Mỗi clip = **1–2 chỉ dấu tâm lý cốt lõi** của Tập 03 (K10) |
| Ngôn ngữ | Tiếng Việt · vai Host (H), Điều tra viên (D), Chuyên gia (C), Trực ban (N1), Cảnh sát (N2) |
| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (đúng giọng Tập 03) |
| Hình | Nền dọc 9:16 crop/pad từ 28 nền 16:9 gốc của Tập 03 |
| Chi phí | **0 đồng** (Kaggle GPU có sẵn) |
| Việc cần người dùng | Tạo **51 file WAV** theo `SPEC_AUDIO_CLIP_TAP03.json` · điền link YouTube Tập 03 |

---

## 1. Năm clip và chỉ dấu tâm lý tương ứng (K10)

| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng |
|---|---|---|---|---|
| **TK1** | #4 · #6 | Sự sụp đổ của ảo tưởng quyền lực + Điểm gãy tâm lý (Precipitating Trigger) | *"Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa."* | 73.4 s · 10 câu |
| **TK2** | #9 · #1 | Hiệu ứng hào quang trí tuệ + Điểm mù xã hội (Halo Effect & Blind Spots) | *"Uống bia cùng cảnh sát. Và bàn về chính vụ án của mình."* | 75.1 s · 10 câu |
| **TK3** | #2 · #3 | Chấn thương mẫu hệ độc hại + Cơ chế Phóng chiếu (Projection & Proxy Victims) | *"Tám tuổi. Bị nhốt dưới tầng hầm có cửa sập dưới bàn ăn."* | 73.4 s · 11 câu |
| **TK4** | #7 · #8 | Vòng lặp ảo tưởng & Dấu ấn Signature vs Thủ đoạn MO (FBI Behavioral Science Unit) | *"IQ một trăm bốn mươi lăm. Bộ não thay đổi vĩnh viễn FBI."* | 73.7 s · 11 câu |
| **TK5** | #10 | Nạn nhân học & 4 dấu hiệu cảnh báo đỏ sinh tồn (Macdonald Triad & Red Flags) | *"Bốn chỉ dấu cảnh báo sớm. Để không ai phải trở thành nạn nhân."* | 64.8 s · 9 câu |

**Thứ tự đăng đề xuất:** TK2 → TK1 → TK4 → TK3 → TK5 (TK2 có hook nghịch lý quán rượu mạnh nhất để viral; TK5 là clip đọng lại giá trị chia sẻ/lưu trữ).

---

## 2. Diễn xuất từng clip (lời đọc + hình + âm)

> Quy ước vai: **H** = Host (Cú) · **D** = Điều tra viên (Sói) · **C** = Chuyên gia tâm lý (Cáo) · **N1** = Trực ban · **N2** = Cảnh sát
> `pause_after` = thời gian im lặng chèn giữa hai câu (0.2–1.2 s — luật G2). Emotion an toàn (G3). Tốc độ offset trong [-0.06, +0.02] (G4). Cao độ = 0 (G5).
> Mỗi câu có mã `TKx.01#z` khớp với `SPEC_AUDIO_CLIP_TAP03.json`.

### 2.1 CLIP TK1 — "Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa"

*Ước lượng 73.4 s (10 câu) · BGM `bgm_sub_drone.mp3` (Hồi 1 — bed tập: bgm_sub_drone.mp3) · SFX: amb_winter_wind.wav (nền) · fx_coin_drop.wav · fx_phone_dial.wav · fx_tension_tick.wav · fx_stinger.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK1.01#1` | H | neutral | -0.02 | 0.5 | Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa. | 1.10#10 · 1.10#11 |
| `TK1.01#2` | H | neutral | -0.02 | 0.6 | Bốn giờ sáng ngày hai mươi tư tháng tư năm 1973, chuông điện thoại tại trụ sở Cảnh sát Santa Cruz reo vang. | 1.03#1 · 1.03#3 |
| `TK1.01#3` | H | neutral | -0.02 | 0.6 | Đầu dây bên kia là Edmund Kemper, gọi từ một bốt điện thoại ven đường ở Pueblo, Colorado, cách đó hơn một nghìn sáu trăm cây số. | 1.03#2 · 1.03#3 · 1.03#5 |
| `TK1.01#4` | H | neutral | -0.02 | 0.6 | Giọng nói điềm đạm, rành mạch: <#0.35#> Tôi đã giết mẹ tôi và người bạn của bà. Và tôi đã giết mấy cô nữ sinh đó. Sáu người. | 1.05#4 · 1.05#5 · 1.05#6 |
| `TK1.01#5` | N1 | neutral | -0.02 | 0.6 | Ban đầu phía trực ban tưởng hắn say rượu trêu đùa và bảo gọi lại sau. | 1.09#1 · 1.09#3 |
| `TK1.01#6` | H | neutral | -0.02 | 0.7 | Hai tiếng sau hắn gọi lại, và lời cảnh báo thật sự khiến người nghe đông cứng: <#0.35#> Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa. | 1.09#4 · 1.10#10 · 1.10#11 |
| `TK1.01#7` | H | neutral | -0.02 | 0.6 | Hắn không gọi để khoe khoang chiến tích. Hắn gọi vì sợ chính mình sẽ không dừng lại được. | 1.10#12 · 1.10#13 |
| `TK1.01#8` | D | neutral | -0.03 | 0.7 | Khi xe tuần tra tới nơi, gã khổng lồ hai mét không sáu ngồi yên trong bốt điện thoại đầu thú, cùng ba khẩu súng và hàng trăm viên đạn trong xe. | 1.03#6 · 1.07#4 · 1.09#5 · 1.09#6 |
| `TK1.01#9` | C | neutral | -0.02 | 0.7 | Khi mục tiêu tối thượng là người mẹ bị sát hại, toàn bộ ảo tưởng quyền lực sụp đổ hoàn toàn. Cảm xúc trống rỗng tột độ đã đẩy hắn vào điểm gãy tâm lý. | 1.10#8 · 1.10#9 · 4.07#8 · 4.07#9 |
| `TK1.01#10` | H | neutral | -0.02 | 0.0 | Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK1.01#1` | `tk03_phone_booth` | still | 3.6 s |
| `TK1.01#2` | `tk03_dispatch_desk` | pull | 8.7 s |
| `TK1.01#3` | `tk03_phone_booth` | pan | 8.1 s |
| `TK1.01#4` | `tk03_phone_booth` | push | 8.1 s |
| `TK1.01#5` | `tk03_dispatch_desk` | still | 4.4 s |
| `TK1.01#6` | `tk03_phone_booth` | push | 8.7 s |
| `TK1.01#7` | `tk03_phone_booth` | still | 5.7 s |
| `TK1.01#8` | `tk03_apartos_house` | pan | 8.1 s |
| `TK1.01#9` | `tk03_brain_mirror` | pull | 8.4 s |
| `TK1.01#10` | `tk03_closing_desk` | still | 4.2 s |

**Thẻ chữ trên hình (overlay card):**
- `TK1.01#1` → *"BỐT ĐIỆN THOẠI PUEBLO · 4 GIỜ SÁNG 24/4/1973"* (3.0 s)
- `TK1.01#4` → *"“TÔI ĐÃ GIẾT MẸ TÔI... VÀ SÁU NỮ SINH”"* (2.5 s)
- `TK1.01#6` → *"“TÔI SẮP LÀM ĐIỀU ĐÓ THÊM MỘT LẦN NỮA”"* (2.5 s)
- `TK1.01#8` → *"3 KHẨU SÚNG · HÀNG TRĂM VIÊN ĐẠN · ĐẦU THÚ"* (2.5 s)
- `TK1.01#9` → *"ĐIỂM GÃY TÂM LÝ: ẢO TƯỞNG SỤP ĐỔ"* (3.0 s)

**Nguồn dữ liệu:** 1.03#1-#8 · 1.05#1-#7 · 1.07#1-#4 · 1.09#1-#6 · 1.10#8-#13 · nguon_tham_khao.md (Inside Detective 1973 · TPG Online Daily)

### 2.2 CLIP TK2 — "Uống bia cùng cảnh sát và bàn về kẻ sát nhân"

*Ước lượng 75.1 s (10 câu) · BGM `bgm_jazz_noir.mp3` (Hồi 2 — bed tập: bgm_jazz_noir.mp3) · SFX: amb_bar.wav (nền) · fx_beer_pour.wav · fx_glass_clink.wav · fx_car_drive.wav · fx_stinger.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK2.01#1` | H | neutral | -0.02 | 0.5 | Uống bia cùng cảnh sát. Và bàn về chính vụ án của mình. | 1.03#7 · 2.09#8 · 2.09#9 |
| `TK2.01#2` | N2 | neutral | -0.02 | 0.6 | Quán rượu The Jury Room nằm đối diện ngay Tòa án Quận Santa Cruz, là nơi thám tử và cảnh sát thường ghé uống bia sau giờ tuần tra. | 2.09#1 |
| `TK2.01#3` | N2 | neutral | -0.02 | 0.6 | Big Ed luôn ngồi ở góc quầy quen thuộc. Cao hai mét không sáu, đeo kính cận, ăn nói nhỏ nhẹ và hiểu biết sâu sắc về luật pháp. | 1.03#6 · 2.07#12 · 2.09#2 · 2.09#3 |
| `TK2.01#4` | D | neutral | -0.03 | 0.6 | Ban ngày, hắn lái chiếc Ford Galaxie màu vàng năm một nghìn chín trăm sáu mươi chín, dán nhãn bãi đỗ xe nhân viên đại học trên cản trước. | 2.07#2 · 2.07#3 · 2.07#4 |
| `TK2.01#5` | D | neutral | -0.03 | 0.6 | Chính tấm nhãn trường cùng vẻ ngoài trí thức, lịch thiệp đã khiến các cô nữ sinh tin rằng chiếc xe tuyệt đối an toàn. | 2.07#5 · 2.07#10 · 2.07#12 |
| `TK2.01#6` | N2 | sad | -0.04 | 0.8 | Có những đêm cảnh sát ngồi uống bia cùng Ed, chia sẻ những bế tắc trong cuộc săn lùng hung thủ Co-ed Killer. | 2.09#6 |
| `TK2.01#7` | N2 | sad | -0.04 | 0.8 | Ed vừa uống bia vừa phân tích, thậm chí gợi ý những giả thuyết tâm lý sắc bén về kẻ thủ ác. | 2.09#7 |
| `TK2.01#8` | N2 | sad | -0.04 | 0.7 | Nghĩ lại khoảnh khắc đó, lưng chúng tôi lạnh toát: Kẻ cả thành phố đang ráo riết truy tìm lại ngồi cười đùa cùng chính những người đi săn. | 2.09#8 · 2.09#9 |
| `TK2.01#9` | C | neutral | -0.02 | 0.7 | Hiệu ứng hào quang: trí thông minh vượt trội và sự hòa nhã giả tạo đã tạo nên điểm mù tuyệt đối trước mắt lực lượng thực thi pháp luật. | 2.07#10 · 5.06#3 · 5.06#4 |
| `TK2.01#10` | H | neutral | -0.02 | 0.0 | Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK2.01#1` | `tk03_bar_stool_shadow` | still | 3.9 s |
| `TK2.01#2` | `tk03_bar_jury_room` | pull | 8.9 s |
| `TK2.01#3` | `tk03_bar_stool_shadow` | pan | 8.9 s |
| `TK2.01#4` | `tk03_galaxie` | still | 7.3 s |
| `TK2.01#5` | `tk03_hitchhiker` | push | 6.3 s |
| `TK2.01#6` | `tk03_bar_jury_room` | still | 7.0 s |
| `TK2.01#7` | `tk03_bar_stool_shadow` | push | 6.7 s |
| `TK2.01#8` | `tk03_bar_stool_shadow` | pull | 8.9 s |
| `TK2.01#9` | `tk03_brain_mirror` | still | 7.2 s |
| `TK2.01#10` | `tk03_closing_desk` | still | 4.2 s |

**Thẻ chữ trên hình (overlay card):**
- `TK2.01#1` → *"QUÁN THE JURY ROOM · ĐỐI DIỆN TÒA ÁN SANTA CRUZ"* (3.0 s)
- `TK2.01#3` → *"2M06 · 127 KG · KÍNH CẬN · GIỌNG NHỎ NHẸ"* (2.5 s)
- `TK2.01#5` → *"NHÃN ĐỖ XE ĐẠI HỌC TRÊN CHIẾC FORD GALAXIE"* (2.5 s)
- `TK2.01#7` → *"PHÂN TÍCH TÂM LÝ HUNG THỦ CHO ĐIỀU TRA VIÊN"* (3.0 s)
- `TK2.01#9` → *"HIỆU ỨNG HÀO QUANG TRÍ TUỆ (HALO EFFECT)"* (2.5 s)

**Nguồn dữ liệu:** 1.03#6-#7 · 2.07#1-#5 · 2.07#10-#14 · 2.09#1-#9 · nguon_tham_khao.md (Front Page Detective 1974 · Peter Vronsky)

### 2.3 CLIP TK3 — "Căn hầm tuổi thơ và căn ngục dưới bàn ăn"

*Ước lượng 73.4 s (11 câu) · BGM `bgm_cello_sad_v2.mp3` (Hồi 3 — bed tập: bgm_cello_sad_v2.mp3) · SFX: amb_basement.wav (nền) · fx_water_drip.wav · fx_trapdoor_creak.wav · fx_sub_drop.wav · fx_stinger.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK3.01#1` | H | neutral | -0.02 | 0.5 | Tám tuổi. Bị nhốt dưới tầng hầm có cửa sập dưới bàn ăn. | 3.05#6 · 3.05#7 |
| `TK3.01#2` | C | neutral | -0.02 | 0.6 | Mẹ của Kemper, bà Clarnell, nhìn thấy ở con trai hình bóng người chồng cũ mà bà căm ghét. | 3.05#4 · 3.05#5 |
| `TK3.01#3` | C | neutral | -0.02 | 0.7 | Từ năm tám tuổi, Ed bị tống xuống ngủ dưới tầng hầm ẩm ướt cạnh lò sưởi than, với chiếc cửa sập nằm ngay dưới bàn ăn ở tầng trên. | 3.05#6 · 3.05#7 |
| `TK3.01#4` | C | neutral | -0.02 | 0.6 | Muốn ra ngoài phải nâng chiếc bàn ăn lên. Sự giam cầm kéo dài cho đến khi người cha can thiệp đe dọa báo cảnh sát. | 3.05#7 · 3.05#8 |
| `TK3.01#5` | C | sad | -0.04 | 0.7 | Mỗi ngày, bà dùng những lời lẽ cay độc nhất để sỉ nhục ngoại hình và triệt tiêu lòng tự trọng của con trai. | 3.05#9 · 3.05#12 |
| `TK3.01#6` | C | neutral | -0.02 | 0.7 | Trong tiềm thức đứa trẻ, người mẹ biến thành một tượng đài quyền lực áp chế khổng lồ mà hắn vừa căm thù vừa khiếp sợ. | 3.08#6 |
| `TK3.01#7` | C | neutral | -0.02 | 0.7 | Không thể phản kháng trực diện người mẹ, bộ não của Kemper kích hoạt cơ chế phóng chiếu: tìm kiếm những nạn nhân thay thế. | 3.08#1 · 3.08#7 · 3.08#11 |
| `TK3.01#8` | C | neutral | -0.02 | 0.7 | Những nữ sinh trẻ trung, xinh đẹp bên vệ đường chính là hiện thân của sự tự do mà hắn thèm khát nhưng tin rằng sẽ luôn khinh miệt hắn. | 3.08#10 · 3.08#11 |
| `TK3.01#9` | H | neutral | -0.02 | 0.6 | Những nạn nhân vô tội đã phải gánh chịu cơn thịnh nộ thay thế cho người mẹ ruột của kẻ thủ ác. | 3.08#11 · 3.08#13 |
| `TK3.01#10` | H | neutral | -0.02 | 0.6 | Trước khi phân tích: các chuyên gia tâm thần từng đưa ra nhiều chẩn đoán trái ngược nhau. Đây là khung giải thích tâm lý, không phải phán xét đạo đức. | 3.04#1 · 3.08#3 · 3.11#6 |
| `TK3.01#11` | H | neutral | -0.02 | 0.0 | Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK3.01#1` | `tk03_basement_stairs` | still | 3.9 s |
| `TK3.01#2` | `tk03_coal_furnace` | push | 4.5 s |
| `TK3.01#3` | `tk03_small_bed` | still | 7.2 s |
| `TK3.01#4` | `tk03_trapdoor` | pull | 6.2 s |
| `TK3.01#5` | `tk03_basement_stairs` | pan | 5.7 s |
| `TK3.01#6` | `tk03_mother_shadow` | still | 6.2 s |
| `TK3.01#7` | `tk03_ucsc_campus` | push | 6.0 s |
| `TK3.01#8` | `tk03_hitchhiker` | pull | 7.2 s |
| `TK3.01#9` | `tk03_apartos_house` | pan | 6.6 s |
| `TK3.01#10` | `tk03_brain_mirror` | still | 9.3 s |
| `TK3.01#11` | `tk03_closing_desk` | still | 4.2 s |

**Thẻ chữ trên hình (overlay card):**
- `TK3.01#1` → *"TẦNG HẦM MONTANA · THẬP NIÊN 1950"* (3.0 s)
- `TK3.01#3` → *"CỬA SẬP DƯỚI BÀN ĂN · PHẢI NHẤC BÀN MỚI RA ĐƯỢC"* (2.5 s)
- `TK3.01#5` → *"NGƯỢC ĐÃI TINH THẦN CÓ HỆ THỐNG"* (2.5 s)
- `TK3.01#7` → *"CƠ CHẾ PHÓNG CHIẾU (PROJECTION)"* (3.0 s)
- `TK3.01#8` → *"NẠN NHÂN THAY THẾ (PROXY VICTIMS)"* (2.5 s)
- `TK3.01#10` → *"KHUNG PHÂN TÍCH TÂM LÝ · KHÔNG PHÁN XÉT LÂM SÀNG"* (2.5 s)

**Nguồn dữ liệu:** 3.02#1-#2 · 3.04#1 · 3.05#1-#12 · 3.08#1-#13 · nguon_tham_khao.md (Front Page Detective 1974 · Peter Vronsky)

### 2.4 CLIP TK4 — "Gã khổng lồ IQ 145 mở toang tâm trí với FBI"

*Ước lượng 73.7 s (11 câu) · BGM `bgm_ambient_deep.mp3` (Hồi 4 — bed tập: bgm_ambient_deep.mp3) · SFX: amb_prison.wav (nền) · fx_iron_door.wav · fx_tape_click.wav · fx_tension_tick.wav · fx_sub_drop.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK4.01#1` | H | neutral | -0.02 | 0.5 | IQ một trăm bốn mươi lăm. Bộ não thay đổi vĩnh viễn FBI. | 1.13#2 · 4.02#4 · 4.08#1 |
| `TK4.01#2` | D | neutral | -0.03 | 0.6 | Năm một nghìn chín trăm bảy mươi tám, hai đặc vụ FBI Robert Ressler và John Douglas bước vào buồng giam tại Vacaville. | 4.02#1 · 4.02#4 · 4.02#8 |
| `TK4.01#3` | D | neutral | -0.03 | 0.6 | Kemper lấp kín khung cửa như một ngọn núi, nhưng hắn mỉm cười lịch thiệp và nói chuyện bằng phong thái của một giáo sư. | 4.05#1 · 4.05#2 · 4.05#3 |
| `TK4.01#4` | D | neutral | -0.03 | 0.6 | Hắn sở hữu IQ một trăm bốn mươi lăm, không đòi giảm án, không cần luật sư, và tự mổ xẻ nội tâm mình với độ chính xác lạnh lùng. | 1.13#2 · 1.13#5 · 4.05#4 · 4.05#13 · 4.05#14 |
| `TK4.01#5` | D | neutral | -0.03 | 0.7 | Kemper giải thích cho FBI khái niệm mang tính cách mạng: Vòng lặp ảo tưởng bạo lực. | 4.07#1 · 4.07#2 |
| `TK4.01#6` | D | neutral | -0.03 | 0.7 | Tội ác không bắt đầu khi rút vũ khí ra, mà bắt đầu từ hàng trăm lần tập dượt trong tâm tưởng suốt nhiều năm trước đó. | 4.07#3 · 4.07#4 · 4.07#5 |
| `TK4.01#7` | D | neutral | -0.03 | 0.6 | Hắn giải thích vì sao giữ chiến lợi phẩm: để tái trải nghiệm cảm giác quyền lực khi cơn hưng phấn sau vụ án tan biến. | 4.07#6 · 4.07#7 |
| `TK4.01#8` | H | neutral | -0.02 | 0.7 | Từ cuộc đối thoại với Kemper cùng ba mươi lăm can phạm khác, FBI đã xây dựng hệ thống phân loại kẻ sát nhân có tổ chức và mạng lưới VICAP toàn quốc. | 1.13#6 · 1.13#7 · 4.08#1 · 4.08#2 · 4.08#3 |
| `TK4.01#9` | C | neutral | -0.02 | 0.7 | Hiện trường không chỉ để lại dấu vết vật lý, mà để lại chữ ký tâm lý độc nhất của kẻ thủ ác. | 4.08#4 |
| `TK4.01#10` | H | neutral | -0.02 | 0.6 | Hồ sơ này trở thành nguồn cảm hứng kinh điển cho các công trình phân tích hành vi và loạt phim Mindhunter. | 4.08#6 · 4.08#7 |
| `TK4.01#11` | H | neutral | -0.02 | 0.0 | Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK4.01#1` | `tk03_vacaville_1978` | still | 3.9 s |
| `TK4.01#2` | `tk03_two_agents` | pull | 5.8 s |
| `TK4.01#3` | `tk03_giant_doorway` | still | 6.3 s |
| `TK4.01#4` | `tk03_interview_room` | push | 7.6 s |
| `TK4.01#5` | `tk03_cassette` | pan | 4.3 s |
| `TK4.01#6` | `tk03_fantasy_spiral` | push | 6.8 s |
| `TK4.01#7` | `tk03_trophy_box` | still | 6.6 s |
| `TK4.01#8` | `tk03_organized_split` | pull | 9.9 s |
| `TK4.01#9` | `tk03_self_observation` | still | 5.5 s |
| `TK4.01#10` | `tk03_case_photos` | push | 6.6 s |
| `TK4.01#11` | `tk03_closing_desk` | still | 4.2 s |

**Thẻ chữ trên hình (overlay card):**
- `TK4.01#1` → *"NHÀ TÙ VACAVILLE · 1978 · ĐẶC VỤ FBI"* (3.0 s)
- `TK4.01#3` → *"IQ 145 · TOP 0,13% BỘ ÓC THÔNG MINH NHẤT"* (2.5 s)
- `TK4.01#5` → *"VÒNG LẶP ẢO TƯỞNG (FANTASY CYCLE)"* (2.5 s)
- `TK4.01#7` → *"CHIẾN LỢI PHẨM: TÁI TẠO CẢM GIÁC QUYỀN LỰC"* (2.5 s)
- `TK4.01#9` → *"CHỮ KÝ SIGNATURE vs THỦ ĐOẠN MO"* (3.0 s)
- `TK4.01#10` → *"NGUỒN CẢM HỨNG CHO MINDHUNTER"* (2.5 s)

**Nguồn dữ liệu:** 1.13#1-#9 · 4.02#1-#8 · 4.05#1-#19 · 4.07#1-#10 · 4.08#1-#7 · nguon_tham_khao.md (FBI Law Enforcement Bulletin 1985 · VICAP 1985)

### 2.5 CLIP TK5 — "Bộ ba Macdonald và bốn hồi chuông cảnh báo"

*Ước lượng 64.8 s (9 câu) · BGM `bgm_piano_minimal.mp3` (Hồi 5 — bed tập: bgm_piano_minimal.mp3) · SFX: amb_wind_soft.wav (nền) · fx_clock_tick.wav · fx_stinger.wav · fx_sub_drop.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK5.01#1` | H | neutral | -0.02 | 0.5 | Bốn chỉ dấu cảnh báo sớm. Để không ai phải trở thành nạn nhân. | 5.04#1 · 5.08#11 |
| `TK5.01#2` | C | neutral | -0.02 | 0.6 | Chỉ dấu thứ nhất: Bộ ba Macdonald thời thơ ấu. Hành vi hành hạ động vật có chủ đích lặp đi lặp lại từ năm mười tuổi. | 5.05#1 · 5.05#2 · 5.05#4 · 5.05#6 |
| `TK5.01#3` | C | neutral | -0.02 | 0.6 | Đó là dấu hiệu sớm của sự vô cảm tột cùng và xu hướng bạo lực leo thang mà gia đình đã bỏ qua. | 5.05#6 |
| `TK5.01#4` | C | neutral | -0.02 | 0.6 | Chỉ dấu thứ hai: Bạo lực tinh thần gia đình cực đoan. Việc cô lập đứa trẻ trong không gian kín và sỉ nhục nhân phẩm kéo dài. | 5.05#7 · 5.05#8 |
| `TK5.01#5` | D | neutral | -0.03 | 0.6 | Chỉ dấu thứ ba: Chìm đắm trong thế giới ảo tưởng bạo lực tách rời thực tại, khao khát quyền lực kiểm soát. | 5.06#1 · 5.06#2 |
| `TK5.01#6` | D | neutral | -0.03 | 0.7 | Và chỉ dấu thứ tư: Trí tuệ cao kết hợp với sự lạnh lùng cảm xúc, dùng sự thông minh để thao túng và che giấu. | 5.06#3 · 5.06#4 |
| `TK5.01#7` | H | neutral | -0.02 | 0.7 | Edmund Kemper sinh ra với bộ não thiên tài và thể lực vượt trội, nhưng khi bị nhúng vào sự ngược đãi, nó đã biến thành vũ khí hủy diệt. | 5.08#8 · 5.08#9 |
| `TK5.01#8` | H | neutral | -0.02 | 0.8 | Giam giữ cái ác sau song sắt là trách nhiệm của pháp luật. Nhưng nhận diện và chữa lành vết thương tâm hồn của con trẻ chính là cách duy nhất để ngăn cái ác sinh sôi. | 5.08#10 · 5.08#11 |
| `TK5.01#9` | H | neutral | -0.02 | 0.0 | Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK5.01#1` | `tk03_red_flags` | still | 4.2 s |
| `TK5.01#2` | `tk03_gift_drowned` | push | 6.5 s |
| `TK5.01#3` | `tk03_gift_drowned` | pull | 5.7 s |
| `TK5.01#4` | `tk03_coal_furnace` | pan | 6.7 s |
| `TK5.01#5` | `tk03_fantasy_spiral` | still | 5.8 s |
| `TK5.01#6` | `tk03_self_observation` | push | 6.6 s |
| `TK5.01#7` | `tk03_life_sentence` | pull | 9.0 s |
| `TK5.01#8` | `tk03_closing_desk` | still | 11.1 s |
| `TK5.01#9` | `tk03_closing_desk` | still | 4.2 s |

**Thẻ chữ trên hình (overlay card):**
- `TK5.01#1` → *"4 HỒI CHUÔNG CẢNH BÁO SỚM TRONG TÂM LÝ HỌC"* (3.0 s)
- `TK5.01#2` → *"CHỈ DẤU 1: BỘ BA MACDONALD THỜI THƠ ẤU"* (2.5 s)
- `TK5.01#4` → *"CHỈ DẤU 2: BẠO LỰC TINH THẦN CỰC ĐOAN"* (2.5 s)
- `TK5.01#5` → *"CHỈ DẤU 3: CHÌM ĐẮM TRONG ẢO TƯỞNG QUYỀN LỰC"* (2.5 s)
- `TK5.01#6` → *"CHỈ DẤU 4: TRÍ TUỆ CAO KÈM SỰ LẠNH LÙNG CẢM XÚC"* (3.0 s)
- `TK5.01#8` → *"BẢO BỌC VÀ CHỮA LÀNH CON TRẺ TỪ GIA ĐÌNH"* (3.0 s)

**Nguồn dữ liệu:** 5.04#1 · 5.05#1-#8 · 5.06#1-#4 · 5.08#6-#11 · nguon_tham_khao.md (Peter Vronsky · Sue Coletta)

---

## 3. Tự kiểm kịch bản (QC Checklist)

| # | Kiểm tra | Kết quả |
|---|---|---|
| 1 | Thời lượng ước lượng 45–95 s (mục tiêu 65–90 s) | ✅ 5/5 đạt: TK1 73.4s, TK2 75.1s, TK3 73.4s, TK4 73.7s, TK5 64.8s |
| 2 | Hook 3 giây đầu (câu 1 ≤ 4.5 s) | ✅ 5/5 đạt: TK1 3.6s, TK2 3.9s, TK3 3.9s, TK4 3.9s, TK5 4.2s |
| 3 | Độ dài caption ≤ 2.200 ký tự (chuẩn TikTok API) | ✅ 5/5 đạt: TK1 1299kt, TK2 1294kt, TK3 1295kt, TK4 1304kt, TK5 1304kt |
| 4 | G1 — CẤM dấu ba chấm trong lời đọc | ✅ 0 lỗi |
| 5 | G3 — Emotion chỉ dùng safe list | ✅ 53/53 câu hợp lệ |
| 6 | G4 — Tốc độ offset trong [-0.06, +0.02] | ✅ 53/53 câu trong ngưỡng |
| 7 | V9 — không từ cấm bạo lực / tình dục nhạy cảm | ✅ 0 lỗi từ cấm |
| 8 | Nguồn 16:9 của 28 nền dùng trong clip có trong assets/bg/_raw/ | ✅ 28/28 nền có file raw |
| 9 | K10 — mỗi clip ≥ 1 chỉ dấu tâm lý | ✅ 5/5 đạt — bao phủ chỉ dấu: #1, #2, #3, #4, #6, #7, #8, #9, #10 |
| 10 | K5 — có câu cảnh báo chẩn đoán tâm lý / khung giải thích lý thuyết | ✅ có ở TK3 |
| 11 | K2 — 2 câu trích được đóng gói chuẩn <#0.35#> | ✅ 2/2 câu trích hợp lệ |
| 12 | Mô tả ngắn & dài — đồng bộ dòng 1, độ dài chuẩn, hashtag đầy đủ | ✅ 5/5 đạt |

---

## 4. Hướng dẫn bước tiếp theo

1. **Duyệt kịch bản:** Người dùng xem xét nội dung 5 clip trên.
2. **Sinh giọng WAV:** Đưa `02_SAN_XUAT/TIKTOK/Tap03/SPEC_AUDIO_CLIP_TAP03.json` lên Kaggle GPU chạy với engine Higgs Audio v3.
3. **Xử lý nền dọc:** Render nền 9:16 từ các file raw `t3_*` tương ứng.
4. **Dựng video & ghép phụ đề:** Dùng script dựng tự động xuất video hoàn chỉnh.

---

## 5. Ảnh nền dọc — đã dựng 20/11/2026

*Chi tiết đo thật + bẫy gặp được: `02_SAN_XUAT/TIKTOK/Tap03/BAO_CAO_ANH_NEN_DOC_TAP03.md`*

| Hạng mục | Số đo |
|---|---|
| Số nền dọc | **28/28** · 1080×1920 đúng 28/28 · phủ **51/51 shot** (TK1 10 · TK2 10 · TK3 11 · TK4 11 · TK5 9) |
| Nguồn | **12 AI thật** (MiniMax `generate_image`, 9:16, 2K) + **16 dự phòng** crop từ ảnh 16:9 gốc (`t3_*`) — allowance hết ở lô 3 (lỗi 402) |
| Vùng chữ | hook mean **45,1** (≤ 58) · sub mean **53,4** (≤ 72) · **0** vệt sáng ngang |
| provenance.json | **28** dòng (12 có `prompt` · 16 `prompt: null` = dự phòng) |
| QC mắt | Soi **100 %** 28 nền + 2 tờ zoom 1:1 → đúng phong cách graphic-noir, **0 mặt lộ**, **0 chữ lạ** |

Cột **Nền** ở mục 2.1–2.5 và trường `bg` trong `SPEC_AUDIO_CLIP_TAP03.json` (VN/EN/JA) trỏ tới **`tk03_*`** — đúng ảnh dọc 9:16 trong `assets/bg/`. Ánh xạ sang ảnh gốc 16:9 nằm trong `NEN_SRC` của `.work/_build_tk_tap03.py` (`tk03_x` → `t3_x`).

Cần nâng 16 nền dự phòng thành AI thật → bật **Settings → Usage & model → Credits → credit auto-consumption** rồi chạy `.work/_tk_gen_bg_extra_t03.py` → `_tk_download_imgs_t03.py` → `_tk_postprocess_t03.py`.
