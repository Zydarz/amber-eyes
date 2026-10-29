# DANH SÁCH SFX CẦN TẠO — TẬP 03 → TẬP 29

**AMBER EYES** · rút từ toàn bộ cue `[SFX]:` / `[BGM]:` / `[Nghỉ …]` trong `01_KICH_BAN/Tap03/ … Tap29/` · ngày 23/10/2026

---

## 1. Tóm tắt

| Hạng mục | Số lượng |
|---|---:|
| Tập khảo sát | 27 (Tập 03 – Tập 29) |
| Tổng cue `[SFX]` đọc được | 221 |
| Tổng cue `[BGM]` / nền | 246 |
| Tổng cue `[Nghỉ …]` có mô tả âm thanh | 19 |
| Dòng dải nền đã tách từ cue `[BGM]` / `[Nghỉ]` | 71 dòng |
| **File SFX mới phải tạo (unique)** | **169** |
| Lượt file mới tính theo tập (tính cả file dùng chung) | 254 |
| File đã có trong thư viện, tái dùng được | 37 |
| Kịch bản tiếng Anh (`Tap03_EN` … `Tap29_EN`) | 27 bản — số cue khớp 100% ⇒ **dùng chung bảng SFX này** |
| Nhạc nền (BGM) dùng lại từ `assets/bgm/` | 9 track |
| Nhạc nền tải thêm | 2 — ✅ đã tải **và đã gắn vào bed** (25/10/2026): `bgm_guitar_acoustic_60s` (guitar T09 H1) · `bgm_church_organ` (organ T16 H1) |
| **Trạng thái tạo file SFX (24/10/2026)** | ✅ **169/169** file đã tải từ YouTube Audio Library + nhập vào `assets/sfx/` · QC 179/179 đạt · **12 mã đã đổi sang track đúng nghĩa hơn** (sigh ×3, máy in ×2, thư viện, phòng thiết, luật sư, báo chí, sốc điện, quán ăn) → xem mục 4.2 |
| **Ứng viên Freesound CC0 (24/10/2026)** | 🟡 **57 ứng viên / 19 mã đang dùng track thay thế** đã tải về `.work/freesound/` — **chưa nhập, chờ nghe duyệt** → xem mục 4.3 |

### Cách đọc ký hiệu

| Ký hiệu | Ý nghĩa |
|---|---|
| 🔴 **TẠO MỚI** | Chưa có trong `assets/sfx/` — phải tải từ YouTube Audio Library, Freesound hoặc tổng hợp bằng `make_sfx3.py` |
| 🟢 **TÁI DÙNG** | Đã có sẵn trong `assets/sfx/` (`/` = gốc, `t2/` = Tập 02, `t3/` = Tập 03) — chỉ cần trỏ file |
| 🎵 **NHẠC NỀN** | Nhạc nền / dải nền, không phải tiếng động một lần |

> **Cột “mã cue”** là mã element theo đúng logic `parse_kichban.py` (`1.02` = phần tử thứ 2 của Hồi 1) — dùng được ngay để ghi vào `.work/sfx_tapXX.json`.
> Mỗi tập có **2 bảng**: tiếng động trong cue `[SFX]`, và **dải nền trong cue `[BGM]` / `[Nghỉ …]`** — bảng thứ 2 hay bị bỏ sót vì nằm lẫn trong mô tả nhạc.
> Có một số cue trong kịch bản gộp 2–3 âm thanh vào một dòng (ví dụ `1.05` của Tập 12) — bảng này đã tách sẵn thành từng file.

---

## 2. Tổng nhanh theo tập

| Tập | Hồ sơ | File mới | Tái dùng | Tổng cue SFX |
|---|---|---:|---:|---:|
| 03 | Gã Khổng Lồ IQ 145 & Chiếc Gương Giải Phẫu Tâm Trí — Hồ Sơ | 1 | 10 | 11 |
| 04 | Thiên Thần Tử Thần & Phức Cảm Chúa Trời — Bí Mật Sau 16 Nă | 10 | 7 | 18 |
| 05 | Chiếc Đĩa Mềm Màu Tím & Cơn Nghiện Ái Kỷ — Sự Sụp Đổ Của V | 5 | 14 | 19 |
| 06 | Nụ Cười Chú Hề & 29 Bí Mật Dưới Sàn Nhà — Hồ Sơ John Wayne | 4 | 8 | 11 |
| 07 | Bản Án Giết Người Bằng Tin Nhắn — Hồ Sơ Michelle Carter &  | 7 | 4 | 12 |
| 08 | Khi Các Thiên Tài Bị Tẩy Não — Hồ Sơ Aum Shinrikyo & Vụ Tấ | 7 | 3 | 11 |
| 09 | Nghệ Thuật Xóa Bỏ Bản Ngã — Hồ Sơ Charles Manson & Thảm Kị | 9 | 4 | 13 |
| 10 | Chiếc Hộp Gỗ Dưới Gầm Giường — Sự Bất Lực Tập Nhiễm & Bóng | 7 | 4 | 12 |
| 11 | Cặp Đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi (Paul Bern | 6 | 4 | 10 |
| 12 | Thảm Kịch Jonestown — Khi 918 Con Người Cùng Bước Vào Chỗ  | 11 | 7 | 18 |
| 13 | Vỏ Bọc 'Con Nhà Người Ta' & Lời Nói Dối 10 Năm — Hồ Sơ Jen | 14 | 3 | 18 |
| 14 | Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới Tội Ác — Hồ Sơ | 15 | 4 | 19 |
| 15 | Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới — Hồ Sơ Jodi A | 12 | 7 | 20 |
| 16 | Kẻ Sát Hại Cả Gia Đình Để 'Đưa Họ Lên Thiên Đàng' — Hồ Sơ  | 11 | 6 | 19 |
| 17 | 13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Hồ Sơ Gia Đình Turpin | 9 | 9 | 19 |
| 18 | Lời Tiên Tri Ngày Tận Thế & Ảo Tưởng Ma Quỷ — Hồ Sơ Lori V | 12 | 5 | 20 |
| 19 | Hồ Sơ Nicholas Cruz — Màn Kịch 'Con Quỷ Trong Đầu' & Sự Th | 12 | 6 | 20 |
| 20 | Hồ Sơ Stephen McDaniel — Khoảnh Khắc Sụp Đổ Trước Ống Kính | 10 | 8 | 21 |
| 21 | Hồ Sơ Andrea Yates — Bi Kịch Của Cơn Loạn Thần Sau Sinh | 9 | 10 | 20 |
| 22 | Hồ Sơ Dalia Dippolito — Nước Mắt Cá Sấu Của Kẻ Thuê Sát Th | 12 | 7 | 19 |
| 23 | Hồ Sơ Richard Ramirez — Ám Ảnh 'Night Stalker' & Hội Chứng | 12 | 7 | 20 |
| 24 | Hồ Sơ Lee Choon-jae — Ký Ức Kẻ Sát Nhân Hwaseong & 33 Năm  | 7 | 12 | 21 |
| 25 | Hồ Sơ Yoo Young-chul — Sát Nhân Áo Mưa & Cơn Cuồng Nộ Thù  | 11 | 7 | 22 |
| 26 | Hồ Sơ Miyuki Ishikawa — Nữ Hộ Sinh Kotobuki & Tội Ác Dưới  | 10 | 8 | 22 |
| 27 | Hồ Sơ Nguyễn Hải Dương — Tổn Thương Ái Kỷ & Thao Túng Đồng | 9 | 10 | 22 |
| 28 | Hồ Sơ Lê Văn Luyện — Cơn Cuồng Loạn Trong Đêm Mưa Bão & Bi | 15 | 6 | 23 |
| 29 | Hồ Sơ Jeffrey Dahmer — Sát Nhân Từ Nỗi Sợ Bị Bỏ Rơi Bệnh L | 8 | 7 | 15 |

---

## 3. Chi tiết theo từng tập

### Tập 03 — Gã Khổng Lồ IQ 145 & Chiếc Gương Giải Phẫu Tâm Trí — Hồ Sơ Edmund Kemper

`01_KICH_BAN/Tap03/kichban_tap03_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 gió rít + tiếng dây điện thoại 1970 → `t2/amb_winter_wind` · H2 mưa + cần gạt → `t3/amb_rain_storm` · H3 nước nhỏ giọt hầm → `t3/amb_pipe_drain` · H4 máy ghi âm cassette → `t2/amb_interrogation` + `t3/fx_cassette_motor` · H5 tòa án → `t2/amb_courtroom` + `bgm_cello_sad_v2`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.02` | Thả đồng xu vào khe bốt điện thoại + quay số | 🟢 TÁI DÙNG | `t3/fx_coin_shuffle.wav` |  |
| `1.08` | Băng ghi âm bật nhẹ 'Tách' | 🟢 TÁI DÙNG | `t3/fx_cassette_button.wav` |  |
| `1.12` | Cửa sắt trại giam kéo lê rồi đóng sập | 🟢 TÁI DÙNG | `t2/fx_door_metal_slam.wav` |  |
| `2.03` | Lật ảnh hồ sơ nạn nhân trên bàn | 🟢 TÁI DÙNG | `card_flip.wav` |  |
| `4.06` | Lật trang ghi chép nhanh lách cách | 🟢 TÁI DÙNG | `t3/fx_paper_crunch.wav` |  |
| `5.11` | Đóng tập hồ sơ giấy + tắt máy ghi âm cassette | 🟢 TÁI DÙNG | `folder_close.wav`<br>`t3/fx_cassette_button.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Gió rít lùa qua khe cửa sắt lạnh giữa đêm vắng | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 1.01` | Rè kim loại cổ điển của đường dây điện thoại đường dài 1970 | 🔴 **TẠO MỚI** | `fx_phone_line_hiss_1970.wav` | tuỳ chọn — bảng chuẩn sfx_tap03.json đã bỏ qua, dùng amb_winter_wind cho cả Hồi 1 |
| `BGM 2.01` | Mưa rơi rả rích trên mui xe hơi | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 2 |
| `BGM 2.01` | Tiếng cần gạt nước kính chắn gió kêu kẽo kẹt | 🟢 TÁI DÙNG | ⚠️ *không có track tương ứng* | KHÔNG CÓ track 'wiper' trong thư viện — bảng chuẩn sfx_tap03.json đã bỏ qua |
| `NGHI 1.11` | Chỉ còn tiếng bước chân vang vọng trong hành lang nhà tù | 🟢 TÁI DÙNG | `footsteps.wav` | đoạn nghỉ Hồi 1 |

### Tập 04 — Thiên Thần Tử Thần & Phức Cảm Chúa Trời — Bí Mật Sau 16 Năm Lặng Câm Của 9 Bệnh Viện

`01_KICH_BAN/Tap04/kichban_tap04_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 máy thở cơ học + monitor → `amb_hospital_ventilator` (MỚI) · H2 piano tối giản + gõ bàn phím đêm → `bgm_piano_minimal_v2` + `keyboard_night` · H3 sub-bass + nhịp tim → `bgm_sub_drone` + `fx_heartbeat_slow` · H4 synth dồn dập → `bgm_ambient_deep` · H5 gavel + piano → `t2/fx_gavel_triple` + `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.02` | Còi xe cứu thương xa + bánh đẩy cáng lăn trên sàn gạch | 🔴 **TẠO MỚI** | `fx_ambulance_siren_distant.wav`<br>`fx_stretcher_wheels.wav` |  |
| `1.06` | Băng ghi âm bật nhẹ 'Tách' | 🟢 TÁI DÙNG | `t3/fx_cassette_button.wav` |  |
| `1.09` | Máy khử rung tim nạp điện + tiếng sốc điện | 🔴 **TẠO MỚI** | `fx_defib_charge_shock.wav` |  |
| `1.13` | Mở tập hồ sơ vụ án + lật giấy tờ dồn dập | 🟢 TÁI DÙNG | `t2/fx_paper_folder.wav`<br>`paper_rustle.wav` |  |
| `2.05` | Quẹt thẻ 'Tít' + ngăn kéo tủ thuốc bật mở | 🔴 **TẠO MỚI** | `fx_card_swipe.wav` |  |
| `2.09` | Đóng dấu mộc lên giấy tờ 'Cộp... Cộp' | 🔴 **TẠO MỚI** | `fx_stamp_wood.wav` | dùng chung T26 |
| `3.03` | Lật các trang bệnh án tâm thần | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.03` | Bước chân vội vã hành lang + mở cửa phòng trà bệnh viện | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `4.03` | (phần) Mở cửa phòng trà bệnh viện 'Cạch' | 🔴 **TẠO MỚI** | `fx_hospital_door_open.wav` |  |
| `4.05` | Băng ghi âm bật nhẹ 'Tách' | 🟢 TÁI DÙNG | `t3/fx_cassette_button.wav` |  |
| `4.07` | Đĩa thìa va chạm + ồn ào nhỏ quán ăn nhanh | 🔴 **TẠO MỚI** | `fx_spoon_clink.wav`<br>`amb_fastfood_cafeteria.wav` |  |
| `4.10` | Cửa sắt phòng hỏi cung kéo lê rồi sập lại | 🟢 TÁI DÙNG | `t2/fx_door_metal_slam.wav` |  |
| `5.11` | Đóng nắp máy đo điện tim 'Tách' | 🔴 **TẠO MỚI** | `fx_monitor_case_close.wav` |  |
| `5.11` | (phần) Gấp tập hồ sơ giấy 'Bụp' | 🟢 TÁI DÙNG | `folder_close.wav` |  |
| `BG H1` | Máy thở cơ học rít + tiếng bíp theo dõi sinh hiệu | 🔴 **TẠO MỚI** | `amb_hospital_ventilator.wav` | nền Hồi 1 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Máy thở cơ học rít nhẹ đều đặn + tiếng bíp theo dõi sinh hiệu | 🔴 **TẠO MỚI** | `amb_hospital_ventilator.wav` | nền Hồi 1 |
| `NGHI 1.11` | Chỉ còn tiếng giọt nước nhỏ chậm rãi | 🟢 TÁI DÙNG | `t3/amb_pipe_drain.wav` | đoạn nghỉ Hồi 1 |
| `NGHI 4.09` | Chuyển sang tiếng bước chân nặng nề trong phòng giam | 🟢 TÁI DÙNG | `footsteps.wav` | đoạn nghỉ Hồi 4 |

### Tập 05 — Chiếc Đĩa Mềm Màu Tím & Cơn Nghiện Ái Kỷ — Sự Sụp Đổ Của Vỏ Bọc 30 Năm

`01_KICH_BAN/Tap05/kichban_tap05_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 máy đánh chữ cơ + gió đông → `typewriter` + `t2/amb_winter_wind` · H2 nhịp tim + cuộn băng từ → `fx_heartbeat_slow` + `t3/fx_cassette_motor` · H3 cello + sub-bass → `bgm_cello_sad` + `bgm_sub_drone` · H4 synth + quạt server → `bgm_ambient_deep` + `amb_server_fan` (MỚI) · H5 gavel → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.02` | Xé phong bì thư giấy 'Soạt' + lật giấy tài liệu gấp nếp | 🔴 **TẠO MỚI** | `fx_envelope_tear.wav` | dùng chung T23 |
| `1.08` | Băng ghi âm bật nhẹ 'Tách' | 🟢 TÁI DÙNG | `t3/fx_cassette_button.wav` |  |
| `1.13` | Mở ngăn kéo kim loại hồ sơ + đặt tập tài liệu lên bàn | 🟢 TÁI DÙNG | `t2/fx_drawer_open.wav`<br>`stamp_thud.wav` |  |
| `2.03` | Lật ảnh chụp hiện trường trên bàn gỗ | 🟢 TÁI DÙNG | `card_flip.wav` |  |
| `4.03` | Lật giở trang báo giấy sột soạt | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | Nạp đĩa mềm vào ổ đĩa 'Cạch... Rè... Rè' | 🔴 **TẠO MỚI** | `fx_floppy_disk_insert.wav` |  |
| `4.09` | Còi xe cảnh sát xa + phanh xe dồn dập | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `4.09` | (phần) Phanh xe trên đường nhựa | 🔴 **TẠO MỚI** | `fx_car_brake_screech.wav` |  |
| `4.11` | Cửa sắt phòng thẩm vấn đóng sầm | 🟢 TÁI DÙNG | `t2/fx_door_metal_slam.wav` |  |
| `4.13` | Thở dài nghẹn ngào của một người phụ nữ | 🔴 **TẠO MỚI** | `fx_sigh_female.wav` |  |
| `5.11` | Đóng tập hồ sơ giấy + gõ máy đánh chữ 'Cạch' | 🟢 TÁI DÙNG | `folder_close.wav`<br>`typewriter.wav` |  |
| `BG H4` | Quạt tản nhiệt máy chủ vo ve trong phòng kỹ thuật số | 🔴 **TẠO MỚI** | `amb_server_fan.wav` | nền Hồi 4 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Máy đánh chữ cơ học lách cách gõ từng nhịp chậm rãi | 🟢 TÁI DÙNG | `typewriter.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng gió đông rít từng hồi lạnh lẽo | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng nhịp tim đập chậm | 🟢 TÁI DÙNG | `t2/fx_heartbeat_slow.wav` | nền Hồi 2 |
| `BGM 2.01` | Tiếng rè rè của cuộn băng từ phát lại bản ghi âm | 🟢 TÁI DÙNG | `t3/fx_cassette_motor.wav` | nền Hồi 2 |
| `BGM 4.01` | Tiếng gõ phím vi tính trong phòng kỹ thuật số | 🟢 TÁI DÙNG | `keyboard_night.wav` | nền Hồi 4 |
| `BGM 4.01` | Âm thanh quạt tản nhiệt máy chủ kêu vo ve | 🔴 **TẠO MỚI** | `amb_server_fan.wav` | nền Hồi 4 |
| `NGHI 1.11` | Chỉ còn tiếng tích tắc khô khốc của đồng hồ | 🟢 TÁI DÙNG | `clock_tick.wav` | đoạn nghỉ Hồi 1 |

### Tập 06 — Nụ Cười Chú Hề & 29 Bí Mật Dưới Sàn Nhà — Hồ Sơ John Wayne Gacy

`01_KICH_BAN/Tap06/kichban_tap06_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dương cầm → `bgm_piano_minimal` · H2 dark ambient dồn dập → `bgm_ambient_deep` · H3 sub-drone → `bgm_sub_drone` · H4 vĩ cầm → `bgm_cello_sad` · H5 piano sâu lắng → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Máy ảnh chớp nháy lách tách | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `1.03` | (phần) Vỗ tay tán thưởng vang xa xăm | 🔴 **TẠO MỚI** | `amb_crowd_applause_distant.wav` |  |
| `1.07` | Đóng cửa xe cọt kẹt + bước chân vội vã trên tuyết | 🟢 TÁI DÙNG | `door_creak.wav`<br>`t2/fx_footsteps_snow.wav` |  |
| `1.10` | Chuông điện thoại đồn cảnh sát reo dồn dập | 🟢 TÁI DÙNG | `t2/fx_phone_ring.wav` |  |
| `2.05` | Lật mở hồ sơ + bước chân kiểm tra hiện trường | 🟢 TÁI DÙNG | `paper_rustle.wav`<br>`footsteps.wav` |  |
| `3.04` | Bước chân nặng trên sàn gỗ + mở nắp hầm kỹ thuật | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `3.04` | (phần) Cọt kẹt mở nắp hầm kỹ thuật | 🔴 **TẠO MỚI** | `fx_hatch_lid_open.wav` |  |
| `3.08` | Xẻng cắm sâu vào đất ẩm + thở dốc điều tra viên | 🔴 **TẠO MỚI** | `fx_shovel_dirt.wav` |  |
| `4.11` | Búa gõ phán quyết của thẩm phán | 🟢 TÁI DÙNG | `gavel.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `NGHI 2.12` | Tiếng còi xe cảnh sát xa xăm | 🟢 TÁI DÙNG | `police_siren_distant.wav` | đoạn nghỉ Hồi 2 |
| `NGHI 5.05` | Tiếng thở dài trầm lặng | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | đoạn nghỉ Hồi 5 |

### Tập 07 — Bản Án Giết Người Bằng Tin Nhắn — Hồ Sơ Michelle Carter & Conrad Roy

`01_KICH_BAN/Tap07/kichban_tap07_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 piano tối giản + synth → `bgm_piano_minimal_v2` · H2 pulse số → `bgm_ambient_deep` · H3 cello u uất → `bgm_cello_sad` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Gõ phím cảm ứng lách tách dồn dập | 🔴 **TẠO MỚI** | `fx_phone_typing_swipe.wav` |  |
| `1.03` | (phần) Chuông thông báo tin nhắn | 🟢 TÁI DÙNG | `notif_ping.wav` |  |
| `1.05` | Bước chân sột soạt trên nhựa đường | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `1.05` | (phần) Gõ cửa kính xe | 🔴 **TẠO MỚI** | `fx_car_window_knock.wav` |  |
| `1.08` | Còi xe cảnh sát xa xăm | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.08` | (phần) Mở khóa túi đựng vật chứng | 🔴 **TẠO MỚI** | `fx_zipper_bag.wav` |  |
| `2.05` | Chuông báo tin nhắn gửi đi liên hồi | 🟢 TÁI DÙNG | `notif_ping.wav` |  |
| `2.05` | (phần) Rung điện thoại khô khốc | 🔴 **TẠO MỚI** | `fx_phone_vibrate.wav` | dùng chung T13 |
| `4.04` | In tài liệu điện tử | 🔴 **TẠO MỚI** | `fx_printer_thermal.wav` | dùng chung T23 |
| `4.04` | (phần) Đóng dấu hồ sơ khởi tố | 🔴 **TẠO MỚI** | `fx_stamp_wood.wav` | dùng chung T04, T26 |
| `4.09` | Búa gõ phán quyết của thẩm phán | 🟢 TÁI DÙNG | `gavel.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `NGHI 2.11` | Tiếng thở dài buốt giá giữa đêm | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | đoạn nghỉ Hồi 2 |

### Tập 08 — Khi Các Thiên Tài Bị Tẩy Não — Hồ Sơ Aum Shinrikyo & Vụ Tấn Công Tàu Điện Ngầm

`01_KICH_BAN/Tap08/kichban_tap08_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dương cầm + heartbeat → `bgm_piano_minimal` + `fx_heartbeat_slow` · H2 dark ambient → `bgm_ambient_deep` · H3 piano u ám → `bgm_piano_minimal_v2` · H4 vĩ cầm → `bgm_cello_sad` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Còi tàu điện ngầm + thông báo ga tiếng Nhật | 🔴 **TẠO MỚI** | `amb_subway_station_jp.wav` |  |
| `1.03` | (phần) Bước chân hối hả | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `1.05` | Mũi ô cắm thủng màng nylon | 🔴 **TẠO MỚI** | `fx_umbrella_puncture_nylon.wav` |  |
| `1.05` | (phần) Chất lỏng rỉ ra sàn tàu | 🔴 **TẠO MỚI** | `fx_liquid_pour_splat.wav` |  |
| `1.05` | (phần) Cửa toa xe đóng sập lại | 🔴 **TẠO MỚI** | `fx_train_door_slam.wav` |  |
| `1.08` | Còi xe cứu thương dồn dập | 🔴 **TẠO MỚI** | `fx_ambulance_siren_close.wav` | dùng chung T22, T25, T28 |
| `1.08` | (phần) Còi hú cảnh sát náo loạn | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `2.03` | Bước chân rầm rộ của lực lượng đặc nhiệm | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `2.03` | (phần) Loa phát thanh yêu cầu đầu hàng | 🔴 **TẠO MỚI** | `amb_megaphone_loudspeaker.wav` |  |
| `4.09` | Gõ búa đanh thép của Tòa án Tokyo | 🟢 TÁI DÙNG | `gavel.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `NGHI 2.10` | Tiếng còi báo động xa xăm | 🔴 **TẠO MỚI** | `amb_alarm_siren_distant.wav` | đoạn nghỉ Hồi 2 — dùng chung T12, T25 |

### Tập 09 — Nghệ Thuật Xóa Bỏ Bản Ngã — Hồ Sơ Charles Manson & Thảm Kịch Gia Đình Manson

`01_KICH_BAN/Tap09/kichban_tap09_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 guitar acoustic 60s → `bgm_guitar_acoustic_60s` (đã tải + đã gắn vào bed 25/10/2026) · H2 dark ambient + gió sa mạc → `bgm_ambient_deep` + `amb_wind_pines` (MỚI) · H3 piano tối giản → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Đàn hát du ca xa xăm | 🔴 **TẠO MỚI** | `amb_female_humming_far.wav` |  |
| `1.03` | (phần) Sóng biển rì rào | 🔴 **TẠO MỚI** | `amb_ocean_waves_soft.wav` | dùng chung T18 |
| `1.03` | (phần) Còi xe cảnh sát rít xé màn đêm | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.05` | Gió rít qua rặng thông trên đồi cao | 🔴 **TẠO MỚI** | `amb_wind_pines.wav` |  |
| `1.05` | (phần) Bước chân lén lút trên sỏi đá | 🔴 **TẠO MỚI** | `fx_footsteps_gravel_stealth.wav` |  |
| `1.08` | Lên đạn lách cách | 🔴 **TẠO MỚI** | `fx_rifle_shell_load.wav` |  |
| `1.08` | (phần) Khóa cửa sắt dồn dập | 🟢 TÁI DÙNG | `chains.wav` |  |
| `2.03` | Cửa gỗ cọt kẹt đu đưa trong gió | 🟢 TÁI DÙNG | `door_creak.wav` |  |
| `2.03` | (phần) Vó ngựa xa xăm trên nền đất khô | 🔴 **TẠO MỚI** | `amb_horse_hooves_distant.wav` |  |
| `4.06` | Máy ảnh chớp nháy lách tách | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `4.06` | (phần) Xôn xao bàn tán của đám đông | 🔴 **TẠO MỚI** | `amb_crowd_murmur_press.wav` | dùng chung T20–T22, T28 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 2.01` | Tiếng gió sa mạc khô khốc (Spahn Ranch, Mojave) | 🔴 **TẠO MỚI** | `amb_desert_wind_dry.wav` | nền Hồi 2 — KHÁC amb_wind_pines của Hồi 1 |
| `NGHI 2.12` | Tiếng guitar bass rền rĩ u uất | 🔴 **TẠO MỚI** | ⚠️ *không có track tương ứng* | dùng track guitar acoustic đang cần tải cho BGM (chưa có trong assets/bgm/) |

### Tập 10 — Chiếc Hộp Gỗ Dưới Gầm Giường — Sự Bất Lực Tập Nhiễm & Bóng Ma 'The Company' (Colleen Stan)

`01_KICH_BAN/Tap10/kichban_tap10_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello u buồn → `bgm_cello_sad` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Xe cộ lao vút trên đường cao tốc + gió rít bên cửa kính | 🔴 **TẠO MỚI** | `amb_highway_speed_car.wav` |  |
| `1.05` | Lốp xe rít phanh chầm chậm tấp vào lề | 🔴 **TẠO MỚI** | `fx_car_tire_screech_stop.wav` | dùng chung T22 |
| `1.05` | (phần) Động cơ nổ trầm đục | 🔴 **TẠO MỚI** | `amb_car_engine_idle.wav` | dùng chung T22, T26 |
| `1.08` | Còi cảnh sát vang vọng xa xăm | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.08` | (phần) Lật giấy tờ hồ sơ vội vã | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.03` | Nắp gỗ nặng nề sập xuống + then cài sắt khóa rít | 🔴 **TẠO MỚI** | `fx_wooden_lid_slam_latch.wav` |  |
| `3.03` | Chuông cửa ngân vang | 🔴 **TẠO MỚI** | `fx_doorbell_chime.wav` |  |
| `3.03` | (phần) Then cài mở khóa gấp gáp | 🔴 **TẠO MỚI** | `fx_latch_unlock.wav` |  |
| `4.06` | Động cơ xe nổ gấp gáp | 🔴 **TẠO MỚI** | `amb_car_engine_idle.wav` | dùng chung T22, T26 |
| `4.06` | (phần) Bánh xe nghiến trên sỏi đá | 🔴 **TẠO MỚI** | `fx_gravel_car_drive.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít hiu hắt trên xa lộ hoang vắng | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng kim đồng hồ tích tắc chậm rãi | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 2 |

### Tập 11 — Cặp Đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi (Paul Bernardo & Karla Homolka)

`01_KICH_BAN/Tap11/kichban_tap11_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + gió → `bgm_cello_sad` + `t2/amb_winter_wind` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Ly rượu chạm nhau lách cách | 🔴 **TẠO MỚI** | `fx_glasses_clink.wav` | dùng chung T14 |
| `1.03` | (phần) Cười đùa rộn rã bữa tiệc ngoài trời | 🔴 **TẠO MỚI** | `amb_party_crowd_outdoor.wav` | dùng chung T14 |
| `1.06` | Còi xe cảnh sát rít xé màn đêm | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.06` | (phần) Lật giở hồ sơ điều tra dồn dập | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.03` | Đổ vỡ đồ đạc loảng xoảng | 🔴 **TẠO MỚI** | `fx_objects_smash_break.wav` |  |
| `2.03` | (phần) Còi xe cấp cứu inh ỏi | 🔴 **TẠO MỚI** | `fx_ambulance_siren_close.wav` | dùng chung T08, T25, T28 |
| `4.06` | Máy chiếu phim rè rè trong phòng tối | 🔴 **TẠO MỚI** | `amb_projector_room.wav` |  |
| `4.06` | (phần) Đập bàn phẫn nộ | 🔴 **TẠO MỚI** | `fx_table_slap_anger.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít hiu hắt bên bờ hồ Ontario | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng kim đồng hồ tích tắc chậm rãi | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 2 |

### Tập 12 — Thảm Kịch Jonestown — Khi 918 Con Người Cùng Bước Vào Chỗ Chết

`01_KICH_BAN/Tap12/kichban_tap12_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + côn trùng nhiệt đới → `bgm_cello_sad` + `t3/amb_crickets_traffic` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Lật giở trang tài liệu lưu trữ FBI | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `1.03` | (phần) Quạt trần quay kẽo kẹt | 🔴 **TẠO MỚI** | `amb_ceiling_fan.wav` | dùng chung T20 |
| `1.05` | Máy bay trực thăng bay lượn + động cơ rền xa | 🔴 **TẠO MỚI** | `amb_helicopter_far.wav` | dùng chung T14 |
| `1.08` | Loa phóng thanh rè rè vọng lại giữa rừng sâu | 🔴 **TẠO MỚI** | `amb_loudspeaker_jungle_echo.wav` |  |
| `1.08` | (phần) Gió rít từng hồi | 🔴 **TẠO MỚI** | `amb_wind_tropical.wav` |  |
| `2.03` | Vỗ tay rộn rã + đàn guitar + hát tập thể | 🔴 **TẠO MỚI** | `amb_crowd_singing_acoustic.wav` |  |
| `2.05` | Giấy sột soạt gấp vội | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.05` | (phần) Bước chân lén lút trong bóng tối | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `2.08` | Động cơ máy bay nhỏ gầm rú chuẩn bị cất cánh | 🔴 **TẠO MỚI** | `amb_small_plane_engine.wav` |  |
| `2.10` | Máy kéo ầm ĩ tiến lại gần | 🔴 **TẠO MỚI** | `amb_tractor_engine.wav` |  |
| `2.10` | (phần) Loạt đạn súng trường và súng hoa cải | 🔴 **TẠO MỚI** | `fx_gunshots_rifle_shotgun.wav` |  |
| `2.12` | Còi báo động khẩn cấp rú lên vang dội | 🔴 **TẠO MỚI** | `amb_alarm_siren_distant.wav` |  |
| `4.03` | Rè rè băng từ cassette + bấm nút Play | 🟢 TÁI DÙNG | `t3/fx_cassette_motor.wav`<br>`t3/fx_cassette_button.wav` |  |
| `4.03` | (phần) Thở dồn dập trong không gian kín | 🔴 **TẠO MỚI** | `fx_breathing_tense_close.wav` | dùng chung T13, T17, T19, T20, T22 |
| `4.05` | Đám đông xì xào tranh cãi | 🔴 **TẠO MỚI** | `amb_crowd_arguing_indoor.wav` |  |
| `4.05` | (phần) Bước chân tiến lại gần micro | 🟢 TÁI DÙNG | `footsteps.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít hiu hắt + âm thanh côn trùng nhiệt đới | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav`<br>`t3/amb_crickets_traffic.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng kim đồng hồ tích tắc giữa đêm rừng | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 2 |

### Tập 13 — Vỏ Bọc 'Con Nhà Người Ta' & Lời Nói Dối 10 Năm — Hồ Sơ Jennifer Pan

`01_KICH_BAN/Tap13/kichban_tap13_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + đồng hồ treo tường → `bgm_cello_sad` + `clock_tick` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Đàn piano cổ điển gấp gáp, căng thẳng | 🎵 NHẠC NỀN | `bgm_piano_minimal_v2.mp3` | nhạc nền |
| `1.05` | Lưỡi dao cạo giấy + tẩy xóa | 🔴 **TẠO MỚI** | `fx_sandpaper_scrape_eraser.wav` |  |
| `1.05` | (phần) Máy in màu chạy rè rè | 🔴 **TẠO MỚI** | `fx_inkjet_printer_run.wav` | dùng chung T18 |
| `1.08` | Lật sách thì thầm trong thư viện công cộng | 🔴 **TẠO MỚI** | `amb_library_quiet.wav` |  |
| `1.08` | (phần) Còi xe buýt xa xa | 🔴 **TẠO MỚI** | `amb_bus_distant.wav` |  |
| `2.03` | Tin nhắn điện thoại rung dồn dập | 🔴 **TẠO MỚI** | `fx_phone_vibrate.wav` | dùng chung T07 |
| `2.03` | (phần) Gõ phím lén lút | 🔴 **TẠO MỚI** | `fx_keyboard_typing_soft.wav` |  |
| `2.05` | Then cài cửa mở lách cách | 🟢 TÁI DÙNG | `lock_door.wav` |  |
| `2.05` | (phần) Bước chân nặng trên nền nhà gỗ | 🔴 **TẠO MỚI** | `fx_footsteps_wood_heavy.wav` | dùng chung T23 |
| `2.07` | Súng nổ liên tiếp dưới tầng hầm | 🔴 **TẠO MỚI** | `fx_gunshots_pistol_inside.wav` |  |
| `2.07` | (phần) La hét đau đớn vang vọng | 🔴 **TẠO MỚI** | `fx_scream_distant.wav` |  |
| `2.09` | Bấm số 911 dồn dập (touch-tone) | 🔴 **TẠO MỚI** | `fx_dtmf_touch_tone_beep.wav` | dùng chung T17 — KHÔNG dùng mỏ quay rotary |
| `2.09` | (phần) Jennifer la hét khóc lóc qua đường dây | 🔴 **TẠO MỚI** | `fx_crying_female_phone.wav` |  |
| `4.04` | Máy đo nhịp tim bệnh viện bíp chậm rãi | 🔴 **TẠO MỚI** | `amb_hospital_monitor_heartbeat.wav` | dùng chung T21, T23 |
| `4.04` | (phần) Thở dồn dập qua ống thở oxy | 🔴 **TẠO MỚI** | `fx_oxygen_breathing.wav` |  |
| `4.07` | Đẩy cánh cửa kim loại phòng thẩm vấn | 🔴 **TẠO MỚI** | `fx_metal_door_push_open.wav` |  |
| `4.07` | (phần) Đặt tập hồ sơ dày cộp xuống mặt bàn | 🟢 TÁI DÙNG | `stamp_thud.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng tích tắc đều đặn của chiếc đồng hồ treo tường | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng kim đồng hồ đếm từng giây vô vọng | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 2 |

### Tập 14 — Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới Tội Ác — Hồ Sơ Betty Broderick

`01_KICH_BAN/Tap14/kichban_tap14_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + sóng biển → `bgm_cello_sad` + `amb_ocean_waves_soft` (MỚI) · H2 dark ambient + búa tòa → `bgm_ambient_deep` + `gavel` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Lật sách giáo trình y khoa dày cộp | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `1.03` | (phần) Trẻ thơ khóc đêm | 🔴 **TẠO MỚI** | `fx_baby_crying_night.wav` |  |
| `1.03` | (phần) Máy may lách cách | 🔴 **TẠO MỚI** | `fx_sewing_machine.wav` |  |
| `1.05` | Ly rượu chạm nhau lách cách | 🔴 **TẠO MỚI** | `fx_glasses_clink.wav` | dùng chung T11 |
| `1.05` | (phần) Cười nói rộn rã giới thượng lưu | 🔴 **TẠO MỚI** | `amb_party_crowd_outdoor.wav` | dùng chung T11 |
| `1.08` | Kim đồng hồ tích tắc dồn dập | 🟢 TÁI DÙNG | `clock_tick.wav` |  |
| `1.08` | (phần) Điện thoại bàn đổ chuông không người nhấc máy | 🔴 **TẠO MỚI** | `fx_landline_ring_office.wav` | dùng chung T25 |
| `2.03` | Máy bay trực thăng tuần tra | 🔴 **TẠO MỚI** | `amb_helicopter_far.wav` | dùng chung T12 |
| `2.03` | (phần) Còi xe cảnh sát réo rắt từ xa | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `2.05` | Máy ghi âm điện thoại phát lại lời mắng chửi + gác máy | 🔴 **TẠO MỚI** | `fx_phone_hangup_click.wav` |  |
| `2.07` | Kim loại va chạm kinh hoàng | 🔴 **TẠO MỚI** | `fx_vehicle_impact_metal.wav` |  |
| `2.07` | (phần) Kính vỡ vụn khi xe tải đâm sầm | 🔴 **TẠO MỚI** | `fx_glass_smash_vehicle_crash.wav` | dùng chung T25 |
| `4.03` | Tra chìa khóa vào ổ mở cửa | 🔴 **TẠO MỚI** | `fx_key_in_lock.wav` | dùng chung T27 |
| `4.03` | (phần) Bước chân trần rón rén trên cầu thang gỗ | 🔴 **TẠO MỚI** | `fx_footsteps_barefoot_stairs.wav` |  |
| `4.05` | Súng lục nổ liên tiếp năm phát | 🔴 **TẠO MỚI** | `fx_gunshots_revolver_5.wav` |  |
| `4.05` | (phần) Vỏ đạn rơi lách cách | 🔴 **TẠO MỚI** | `fx_shell_casing_drop.wav` |  |
| `4.07` | Búa tòa án gõ vang dội | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.07` | (phần) Xì xào tranh cãi nảy lửa của đám đông | 🔴 **TẠO MỚI** | `amb_crowd_murmur_courtroom.wav` | dùng chung T17–T28 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng sóng biển vỗ rì rào xa xa bên bờ biển La Jolla | 🔴 **TẠO MỚI** | `amb_ocean_waves_soft.wav` | nền Hồi 1 — dùng chung T09, T18 |

### Tập 15 — Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới — Hồ Sơ Jodi Arias

`01_KICH_BAN/Tap15/kichban_tap15_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dark ambient + nước nhỏ giọt → `bgm_ambient_deep` + `t3/amb_pipe_drain` · H2 điện tử dồn dập → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin căng thẳng → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Còi xe cảnh sát từ xa | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.03` | (phần) Bộ đàm Sở Cảnh sát xì xèo | 🟢 TÁI DÙNG | `radio_chatter.wav` |  |
| `1.05` | Chuông điện thoại đổ dồn dập trong đêm | 🔴 **TẠO MỚI** | `fx_phone_ring_landline_night.wav` | dùng chung T18 |
| `1.05` | (phần) Gõ bàn phím máy tính gấp gáp | 🟢 TÁI DÙNG | `keyboard_night.wav` |  |
| `1.08` | Kéo dải băng niêm phong hiện trường ro ro | 🔴 **TẠO MỚI** | `fx_crime_scene_tape_pull.wav` |  |
| `1.08` | (phần) Bước chân mang bọc giày chuyên dụng lạo xạo | 🔴 **TẠO MỚI** | `fx_footsteps_shoes_scuff.wav` |  |
| `2.03` | Nhấp chuột máy tính liên thanh | 🔴 **TẠO MỚI** | `fx_mouse_click_rapid.wav` | dùng chung T22 |
| `2.03` | (phần) Bíp bíp phục hồi tập tin hình ảnh | 🔴 **TẠO MỚI** | `fx_computer_beep_restore.wav` |  |
| `2.05` | Gõ bàn phím cơ dồn dập | 🔴 **TẠO MỚI** | `fx_mechanical_keyboard.wav` |  |
| `2.05` | (phần) Máy in hóa đơn chạy rè rè | 🔴 **TẠO MỚI** | `fx_printer_thermal.wav` | dùng chung T07, T23 |
| `2.07` | Lật mở hồ sơ giấy tờ dày cộp | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.07` | (phần) Cửa sắt phòng lưu trữ chứng cứ | 🔴 **TẠO MỚI** | `fx_evidence_room_door.wav` |  |
| `4.03` | Gõ bàn thẩm vấn cộc cộc | 🔴 **TẠO MỚI** | `fx_knock_table.wav` | dùng chung T26 |
| `4.03` | (phần) Lật giấy biên bản hỏi cung rột roạt | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | Đèn flash máy ảnh chớp nháy lia lịa | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `4.05` | (phần) Máy quay truyền hình rè rè | 🔴 **TẠO MỚI** | `amb_tv_camera_operator.wav` | dùng chung T22 |
| `4.07` | Micro truyền hình ù nhẹ | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T17–T29 (13 tập) |
| `4.07` | (phần) Xì xào tranh cãi tại phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_murmur_courtroom.wav` | dùng chung T14, T17–T28 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng nước nhỏ giọt đều đặn | 🟢 TÁI DÙNG | `t3/amb_pipe_drain.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng gió rít qua khe cửa sổ | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |

### Tập 16 — Kẻ Sát Hại Cả Gia Đình Để 'Đưa Họ Lên Thiên Đàng' — Hồ Sơ John List

`01_KICH_BAN/Tap16/kichban_tap16_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 organ nhà thờ → `bgm_church_organ` (đã tải + đã gắn vào bed 25/10/2026) + `t2/amb_winter_wind` · H2 điện tử + máy bay → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Còi xe tuần tra từ xa | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.03` | (phần) Bước chân vội vã trên lớp tuyết mỏng | 🟢 TÁI DÙNG | `t2/fx_footsteps_snow.wav` |  |
| `1.05` | Chuông trường học tan học | 🔴 **TẠO MỚI** | `fx_school_bell_dismissal.wav` |  |
| `1.05` | (phần) Mở khóa cửa kim loại lách cách | 🔴 **TẠO MỚI** | `fx_metal_lock_open.wav` |  |
| `1.08` | Cảnh sát phá khóa cửa sổ tầng hầm kêu rắc | 🔴 **TẠO MỚI** | `fx_window_pry_break.wav` | dùng chung T23 |
| `1.08` | (phần) Bước chân cẩn trọng trên sàn gỗ bụi bặm | 🔴 **TẠO MỚI** | `fx_footsteps_dusty_wood_slow.wav` |  |
| `2.03` | Kéo cắt giấy lách cách sắc ngọt | 🔴 **TẠO MỚI** | `fx_scissors_cut_paper.wav` |  |
| `2.03` | (phần) Lật trang album ảnh sột soạt | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.05` | Còi tàu hỏa hú dài trong đêm | 🔴 **TẠO MỚI** | `amb_train_horn_distant_night.wav` |  |
| `2.05` | (phần) Bước chân vội vã trên sân ga | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `2.07` | Lật hồ sơ vụ án tồn đọng dày cộp | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.07` | (phần) Gõ máy chữ của cơ quan điều tra | 🟢 TÁI DÙNG | `typewriter.wav` |  |
| `4.03` | Gõ búa điêu khắc trên đất sét | 🔴 **TẠO MỚI** | `fx_chisel_hammer_clay.wav` |  |
| `4.03` | (phần) Thở dài tập trung của nghệ sĩ pháp y | 🔴 **TẠO MỚI** | `fx_breathing_focused_artist.wav` |  |
| `4.05` | Tách trà rơi vỡ tan tành trên sàn | 🔴 **TẠO MỚI** | `fx_cup_shatter_tea.wav` |  |
| `4.05` | (phần) Chuông điện thoại đường dây nóng đổ dồn dập | 🔴 **TẠO MỚI** | `fx_phone_ring_landline_night.wav` | dùng chung T15, T18 |
| `4.07` | Còi xe đặc vụ FBI rú lên inh ỏi | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `4.07` | (phần) Đạp cửa phòng làm việc dứt khoát | 🔴 **TẠO MỚI** | `fx_door_kick_boot.wav` | dùng chung T27 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít qua khe cửa sổ của tòa biệt thự cổ | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |

### Tập 17 — 13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Hồ Sơ Gia Đình Turpin

`01_KICH_BAN/Tap17/kichban_tap17_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dark ambient + gió → `bgm_ambient_deep` + `t2/amb_winter_wind` · H2 dark ambient + công viên giải trí → `bgm_ambient_deep` + `amb_carnival_ride_music_far` (MỚI) · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Bấm phím số điện thoại khẩn cấp tút tút (touch-tone) | 🔴 **TẠO MỚI** | `fx_dtmf_touch_tone_beep.wav` | dùng chung T13 — KHÔNG dùng mỏ quay rotary |
| `1.03` | (phần) Thở dốc nghẹn ngào | 🔴 **TẠO MỚI** | `fx_breathing_tense_close.wav` | dùng chung T12, T13, T19, T20, T22 |
| `1.05` | Ghi âm cuộc gọi 911 rào rào | 🔴 **TẠO MỚI** | `fx_911_call_recording_radio.wav` |  |
| `1.05` | (phần) Gõ bàn phím định vị tọa độ khẩn cấp | 🟢 TÁI DÙNG | `keyboard_night.wav` |  |
| `1.08` | Gõ cửa dồn dập của cảnh sát | 🟢 TÁI DÙNG | `door_knock.wav` |  |
| `1.08` | (phần) Then cài cửa sắt lạch cạch mở ra | 🟢 TÁI DÙNG | `lock_door.wav` |  |
| `2.03` | Máy ảnh chụp flash lách cách | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `2.03` | (phần) Nhạc vui nhộn tại công viên giải trí | 🔴 **TẠO MỚI** | `amb_carnival_ride_music_far.wav` |  |
| `2.05` | Dây xích sắt cọ xát vào thành giường kim loại | 🟢 TÁI DÙNG | `chains.wav` |  |
| `2.05` | (phần) Bước chân lạnh lùng dậm mạnh | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `2.07` | Mở bao bì bánh ngọt sột soạt | 🔴 **TẠO MỚI** | `fx_candy_wrapper_open.wav` | dùng chung T19 |
| `2.07` | (phần) Khóa tủ lạnh lách cách đánh cạch | 🔴 **TẠO MỚI** | `fx_fridge_door_open.wav` |  |
| `4.03` | Xì xào của đám đông tại phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_murmur_courtroom.wav` | dùng chung T14, T18–T28 |
| `4.03` | (phần) Micro phát biểu rung nhẹ | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.05` | Thở dài xúc động | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | dùng chung T18, T19, T21, T23, T24, T25, T27 |
| `4.05` | (phần) Lật trang giấy phát biểu run rẩy | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.07` | Búa tòa án gõ ba tiếng vang dội | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít rợn người giữa đêm lạnh | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng thở gấp gáp trong bóng tối | 🔴 **TẠO MỚI** | `fx_breathing_tense_close.wav` | nền Hồi 1 — dùng chung T12, T13, T19, T20, T22 |

### Tập 18 — Lời Tiên Tri Ngày Tận Thế & Ảo Tưởng Ma Quỷ — Hồ Sơ Lori Vallow & Chad Daybell

`01_KICH_BAN/Tap18/kichban_tap18_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dark ambient + gió biển + chuông gió → `bgm_ambient_deep` + `amb_ocean_waves_soft` (MỚI) · H2 điện tử dồn dập → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Chuông điện thoại đổ dồn dập không người nhấc máy | 🔴 **TẠO MỚI** | `fx_phone_ring_landline_night.wav` | dùng chung T15, T16 |
| `1.03` | (phần) Sóng biển rì rào xa xa | 🔴 **TẠO MỚI** | `amb_ocean_waves_soft.wav` | dùng chung T09 |
| `1.05` | Gõ cửa căn hộ cộc cộc | 🟢 TÁI DÙNG | `door_knock.wav` |  |
| `1.05` | (phần) Radio đàm thoại của cảnh sát tuần tra | 🟢 TÁI DÙNG | `radio_chatter.wav` |  |
| `1.08` | Lật mở hồ sơ truy nã khẩn cấp | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `1.08` | (phần) Máy in lệnh bắt giữ rột roạt | 🔴 **TẠO MỚI** | `fx_inkjet_printer_run.wav` | dùng chung T13 |
| `2.03` | Cuốc xẻng đào đất chạm vào vật cứng | 🔴 **TẠO MỚI** | `fx_shovel_pick_dirt_stone.wav` | dùng chung T25 |
| `2.03` | (phần) Chó nghiệp vụ sủa báo hiệu | 🔴 **TẠO MỚI** | `fx_dog_bark_working.wav` |  |
| `2.05` | Còng số tám tra vào tay đánh cạch | 🔴 **TẠO MỚI** | `fx_handcuff_snap.wav` | dùng chung T23, T25, T28 |
| `2.05` | (phần) Mở tủ hồ sơ chứng cứ pháp y | 🔴 **TẠO MỚI** | `fx_evidence_cabinet_open.wav` |  |
| `2.07` | Lật hồ sơ bảo hiểm nhân thọ | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.07` | (phần) Xét nghiệm mẫu bệnh phẩm pháp y | 🔴 **TẠO MỚI** | `fx_lab_test_kit.wav` |  |
| `4.03` | Búa tòa án gõ vang dội | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.03` | (phần) Xì xào phẫn nộ của khán giả | 🔴 **TẠO MỚI** | `amb_crowd_angry_jeers.wav` | dùng chung T25 |
| `4.05` | Micro phát biểu rung nhẹ | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.05` | (phần) Thở dài xúc động của bồi thẩm viên | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | dùng chung T17, T19, T21, T23, T24, T25, T27 |
| `4.07` | Búa tòa án gõ ba tiếng dứt khoát | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |
| `4.07` | (phần) Xì xào chấn động của phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_angry_jeers.wav` | dùng chung T25 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió biển Hawaii | 🔴 **TẠO MỚI** | `amb_ocean_waves_soft.wav` | nền Hồi 1 — dùng chung T09, T14 |
| `BGM 1.01` | Tiếng chuông gió lạnh lẽo | 🔴 **TẠO MỚI** | `amb_wind_chime.wav` | nền Hồi 1 — chuông gió là nốt nhạc nền, không phải tiếng động |

### Tập 19 — Hồ Sơ Nicholas Cruz — Màn Kịch 'Con Quỷ Trong Đầu' & Sự Thật Trước Máy Quay

`01_KICH_BAN/Tap19/kichban_tap19_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 drone + đồng hồ → `bgm_sub_drone` + `clock_tick` · H2 dark ambient → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Cùm tay sắt va chạm trên mặt bàn kim loại | 🔴 **TẠO MỚI** | `fx_handcuffs_chain_on_metal_table.wav` |  |
| `1.03` | (phần) Thở dốc run rẩy | 🔴 **TẠO MỚI** | `fx_breathing_tense_close.wav` | dùng chung T12, T13, T17, T20, T22 |
| `1.05` | Còi xe cứu thương từ xa | 🔴 **TẠO MỚI** | `fx_ambulance_siren_distant.wav` | dùng chung T04 |
| `1.05` | (phần) Tiếng người hoảng loạn hỗn loạn ngoài sân trường | 🔴 **TẠO MỚI** | `amb_panic_crowd_schoolyard.wav` |  |
| `1.08` | Lật mở tập hồ sơ vụ án trên bàn | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `1.08` | (phần) Bút bi gõ nhịp xuống mặt bàn | 🟢 TÁI DÙNG | `pen_strike.wav` |  |
| `2.03` | Đóng cửa đánh cạch | 🔴 **TẠO MỚI** | `fx_door_slam_indoor.wav` |  |
| `2.03` | (phần) Mở bao bì bánh mì sột soạt | 🔴 **TẠO MỚI** | `fx_bread_bag_open.wav` |  |
| `2.05` | Bấm mở khóa màn hình điện thoại | 🔴 **TẠO MỚI** | `fx_phone_unlock_click.wav` |  |
| `2.05` | (phần) Rè rè của đoạn video tự quay | 🔴 **TẠO MỚI** | `fx_video_playback_static.wav` | dùng chung T22 |
| `2.07` | Lật hồ sơ chứng cứ pháp lý | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.07` | (phần) Gõ phím máy tính lưu trữ bằng chứng | 🟢 TÁI DÙNG | `keyboard_night.wav` |  |
| `4.03` | Búa tòa án gõ ba tiếng | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |
| `4.03` | (phần) Xì xào căng thẳng của phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_murmur_courtroom.wav` | dùng chung T14, T17, T18, T20–T28 |
| `4.05` | Thở dài nghẹn ngào | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | dùng chung T17, T18, T21, T23, T24, T25, T27 |
| `4.05` | (phần) Micro phát biểu của các phụ huynh | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | Búa tòa án vang lên đanh thép | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.07` | (phần) Thở phào nhẹ nhõm lẫn nghẹn ngào từ hàng ghế | 🔴 **TẠO MỚI** | `fx_crowd_relief_sigh.wav` | dùng chung T21, T24 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng kim đồng hồ tích tắc nặng nề trong phòng thẩm vấn kín | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng tích tắc đồng hồ lạnh lẽo và sắc lạnh | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 2 |

### Tập 20 — Hồ Sơ Stephen McDaniel — Khoảnh Khắc Sụp Đổ Trước Ống Kính

`01_KICH_BAN/Tap20/kichban_tap20_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dark ambient + nhịp tim + đồng hồ → `bgm_ambient_deep` + `fx_heartbeat_slow` + `clock_tick` · H2 minimal ambient → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Máy quay ghi hình rè nhẹ | 🔴 **TẠO MỚI** | `amb_camera_crew_press.wav` |  |
| `1.03` | (phần) Xì xào của đám đông phóng viên | 🔴 **TẠO MỚI** | `amb_crowd_murmur_press.wav` | dùng chung T09, T21, T22, T28 |
| `1.05` | Còi cảnh sát hú gấp từ xa | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.05` | (phần) Bộ đàm rè rè ngắt quãng | 🟢 TÁI DÙNG | `radio_chatter.wav` |  |
| `1.08` | Thở dốc nghẹn ngào | 🔴 **TẠO MỚI** | `fx_breathing_tense_close.wav` | dùng chung T12, T13, T17, T19, T22 |
| `1.08` | (phần) Micro thu âm tiếng thở run rẩy | 🔴 **TẠO MỚI** | `fx_lav_mic_breathing.wav` |  |
| `2.03` | Quạt trần quay đều đều đơn điệu | 🔴 **TẠO MỚI** | `amb_ceiling_fan.wav` | dùng chung T12 |
| `2.03` | (phần) Thở nặng nề trong phòng kín | 🔴 **TẠO MỚI** | `fx_breathing_tense_close.wav` | dùng chung T12, T13, T17, T19, T22 |
| `2.05` | Lật mở tập hồ sơ khám xét | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.05` | (phần) Đặt chùm chìa khóa kim loại xuống bàn | 🔴 **TẠO MỚI** | `fx_keys_drop_on_table.wav` |  |
| `2.07` | Cạy mở ngăn kéo | 🟢 TÁI DÙNG | `t2/fx_drawer_open.wav` |  |
| `2.07` | (phần) Mở bao bì cưa sắt sột soạt | 🔴 **TẠO MỚI** | `fx_saw_blade_packaging.wav` |  |
| `4.03` | Lật mở tập thỏa thuận nhận tội | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.03` | (phần) Bút ký sột soạt | 🔴 **TẠO MỚI** | `fx_pen_signing_scroll.wav` | dùng chung T23 |
| `4.05` | Thì thầm phẫn nộ trong khán phòng | 🔴 **TẠO MỚI** | `amb_crowd_angry_whisper.wav` |  |
| `4.05` | (phần) Búa tòa án gõ giữ trật tự | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.07` | Gõ búa tòa án dứt khoát ba tiếng | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |
| `4.07` | (phần) Micro phát biểu của nhân chứng | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng nhịp tim đập chậm | 🟢 TÁI DÙNG | `t2/fx_heartbeat_slow.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng tích tắc đồng hồ kim loại ngột ngạt | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng kim đồng hồ điện tử khô khốc và đều đặn | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 2 |

### Tập 21 — Hồ Sơ Andrea Yates — Bi Kịch Của Cơn Loạn Thần Sau Sinh

`01_KICH_BAN/Tap21/kichban_tap21_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + nhịp tim + mưa → `bgm_cello_sad` + `fx_heartbeat_slow` + `t3/amb_rain_storm` · H2 ambient trầm đục → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Còi xe cảnh sát từ xa vọng lại | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.03` | (phần) Bước chân vội vã trên sàn nhà | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `1.05` | Máy ảnh chớp nháy của phóng viên | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `1.05` | (phần) Xôn xao bàng hoàng của đám đông | 🔴 **TẠO MỚI** | `amb_crowd_murmur_press.wav` | dùng chung T09, T20, T22, T28 |
| `1.08` | Đóng cửa xe cảnh sát đánh cạch | 🔴 **TẠO MỚI** | `fx_car_door_close.wav` | dùng chung T22 |
| `1.08` | (phần) Mở cuốn sổ ghi chép điều tra | 🔴 **TẠO MỚI** | `fx_notebook_open_pages.wav` |  |
| `2.03` | Lật từng trang hồ sơ bệnh án y khoa | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.03` | (phần) Thở dài nặng nhọc | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | dùng chung T17, T18, T19, T23, T24, T25, T27 |
| `2.05` | Máy đo nhịp tim trong bệnh viện | 🔴 **TẠO MỚI** | `amb_hospital_monitor_heartbeat.wav` | dùng chung T13, T23 |
| `2.05` | (phần) Gõ bàn phím lưu trữ bệnh án | 🟢 TÁI DÙNG | `keyboard_night.wav` |  |
| `2.07` | Tích tắc đồng hồ chạy gấp gáp | 🟢 TÁI DÙNG | `clock_tick.wav` |  |
| `2.07` | (phần) Xe ô tô rời khỏi gara | 🔴 **TẠO MỚI** | `amb_car_start_leave_garage.wav` |  |
| `4.03` | Búa tòa án gõ mạnh | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.03` | (phần) Lật phán quyết hủy án của Tòa Phúc thẩm | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | Xì xào thảo luận của các luật sư | 🔴 **TẠO MỚI** | `amb_lawyers_discussion.wav` |  |
| `4.05` | (phần) Micro phát biểu của điều tra viên | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | Gõ búa tòa án dứt khoát ba tiếng | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |
| `4.07` | (phần) Thở phào nhẹ nhõm từ hàng ghế | 🔴 **TẠO MỚI** | `fx_crowd_relief_sigh.wav` | dùng chung T19, T24 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng nhịp tim trầm đục | 🟢 TÁI DÙNG | `t2/fx_heartbeat_slow.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng mưa rơi rả rích | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 1 |

### Tập 22 — Hồ Sơ Dalia Dippolito — Nước Mắt Cá Sấu Của Kẻ Thuê Sát Thủ Giết Chồng

`01_KICH_BAN/Tap22/kichban_tap22_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dark ambient + còi xe → `bgm_ambient_deep` + `police_siren_distant` · H2 electronic pulse → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Phanh xe gấp | 🔴 **TẠO MỚI** | `fx_car_tire_screech_stop.wav` | dùng chung T10 |
| `1.03` | (phần) Dải băng phong tỏa bay phần phật trong gió | 🔴 **TẠO MỚI** | `fx_police_tape_flutter.wav` |  |
| `1.05` | Máy quay phim truyền hình rè nhẹ | 🔴 **TẠO MỚI** | `amb_tv_camera_operator.wav` | dùng chung T15 |
| `1.05` | (phần) Xì xào bàn tán của đám đông | 🔴 **TẠO MỚI** | `amb_crowd_murmur_press.wav` | dùng chung T09, T20, T21, T28 |
| `1.08` | Đóng cửa xe đặc chủng đánh cạch | 🔴 **TẠO MỚI** | `fx_car_door_close.wav` | dùng chung T21 |
| `1.08` | (phần) Động cơ xe cảnh sát chuyển bánh | 🔴 **TẠO MỚI** | `amb_car_engine_idle.wav` | dùng chung T10, T26 |
| `2.03` | Ghế kim loại bị kéo mạnh lách cách | 🟢 TÁI DÙNG | `t2/fx_chair_scrape.wav` |  |
| `2.03` | (phần) Bước chân lùi lại dứt khoát | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `2.05` | Nhấn chuột mở tệp video | 🔴 **TẠO MỚI** | `fx_mouse_click_rapid.wav` | dùng chung T15 |
| `2.05` | (phần) Rè rè của camera giấu kín trên xe ô tô | 🔴 **TẠO MỚI** | `fx_video_playback_static.wav` | dùng chung T19 |
| `2.07` | Gõ bàn phím lưu trữ vật chứng | 🟢 TÁI DÙNG | `keyboard_night.wav` |  |
| `2.07` | (phần) Thở dốc bối rối | 🔴 **TẠO MỚI** | `fx_breathing_tense_close.wav` | dùng chung T12, T13, T17, T19, T20 |
| `4.03` | Búa tòa án gõ mạnh | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.03` | (phần) Lật mở hồ sơ cáo trạng của công tố viên | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | Xì xào căng thẳng trong phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_murmur_courtroom.wav` | dùng chung T14, T17–T28 |
| `4.05` | (phần) Micro phát biểu của điều tra viên | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | Gõ búa tòa án dứt khoát ba tiếng | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |
| `4.07` | (phần) Khán phòng im lặng tuyệt đối | 🔴 **TẠO MỚI** | `fx_courtroom_dead_silence.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 2.01` | Tiếng tích tắc đồng hồ lạnh lẽo và sắc lạnh | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 2 |

### Tập 23 — Hồ Sơ Richard Ramirez — Ám Ảnh 'Night Stalker' & Hội Chứng Say Mê Tội Phạm

`01_KICH_BAN/Tap23/kichban_tap23_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H2 heavy bass → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Cọt kẹt cửa sổ bị cạy mở trong đêm | 🔴 **TẠO MỚI** | `fx_window_pry_break.wav` | dùng chung T16 |
| `1.03` | (phần) Bước chân lén lút trên sàn gỗ | 🔴 **TẠO MỚI** | `fx_footsteps_stealth_wood.wav` |  |
| `1.05` | Máy in báo chạy rầm rộ | 🔴 **TẠO MỚI** | `fx_printer_thermal.wav` | dùng chung T07, T15 |
| `1.05` | (phần) Còi xe cảnh sát hú dồn dập | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.08` | Còng số tám khóa chặt lách cách | 🔴 **TẠO MỚI** | `fx_handcuff_snap.wav` | dùng chung T18, T25, T28 |
| `1.08` | (phần) Hò reo của đám đông bên ngoài | 🔴 **TẠO MỚI** | `amb_crowd_cheer_outdoor.wav` |  |
| `2.03` | Máy ảnh bấm liên thanh tách tách | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `2.03` | (phần) Xì xào phấn khích của các cô gái | 🔴 **TẠO MỚI** | `amb_crowd_excited_girls.wav` |  |
| `2.05` | Gõ búa tòa án giữ trật tự | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `2.05` | (phần) Thở dài phẫn nộ của thân nhân nạn nhân | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | dùng chung T17, T18, T19, T21, T24, T25, T27 |
| `2.07` | Xé phong bì thư sột soạt | 🔴 **TẠO MỚI** | `fx_envelope_tear.wav` | dùng chung T05 |
| `2.07` | (phần) Bước chân giám thị trong trại giam | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `4.03` | Khóa cửa buồng giam lách cách | 🟢 TÁI DÙNG | `lock_door.wav` |  |
| `4.03` | (phần) Thở dốc mệt mỏi | 🔴 **TẠO MỚI** | `fx_breathing_tired.wav` |  |
| `4.05` | Lật mở hồ sơ lưu trữ điều tra | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | (phần) Bút ký xác nhận kết thúc vụ án | 🔴 **TẠO MỚI** | `fx_pen_signing_scroll.wav` | dùng chung T20 |
| `4.07` | Máy monitor tim đập chậm dần rồi tắt hẳn | 🔴 **TẠO MỚI** | `amb_hospital_monitor_heartbeat.wav` | dùng chung T13, T21 |
| `4.07` | (phần) Còi xe cấp cứu chuyển thi thể | 🔴 **TẠO MỚI** | `fx_ambulance_siren_close.wav` | dùng chung T08, T11, T25, T28 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng kim đồng hồ tích tắc nặng nề | 🟢 TÁI DÙNG | `clock_tick.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng còi xe cảnh sát rền rĩ trong đêm hè oi ả | 🟢 TÁI DÙNG | `police_siren_distant.wav` | nền Hồi 1 |

### Tập 24 — Hồ Sơ Lee Choon-jae — Ký Ức Kẻ Sát Nhân Hwaseong & 33 Năm Dưới Sương Mù

`01_KICH_BAN/Tap24/kichban_tap24_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 minimal ambient + bước chân hành lang → `bgm_sub_drone` + `footsteps` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Còi xe tuần tra rền rĩ trong mưa đêm | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.03` | (phần) Bước chân chạy loạn xạ trên đường đất | 🔴 **TẠO MỚI** | `fx_footsteps_run_gravel.wav` | dùng chung T28 |
| `1.05` | Đồng hồ tích tắc nặng nề | 🟢 TÁI DÙNG | `clock_tick.wav` |  |
| `1.05` | (phần) Lật mở các trang tài liệu lưu trữ cũ kỹ | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `1.08` | Máy phân tích ADN trong phòng thí nghiệm | 🔴 **TẠO MỚI** | `amb_lab_equipment.wav` |  |
| `1.08` | (phần) Bàn phím máy tính gõ dồn dập | 🟢 TÁI DÙNG | `keyboard_night.wav` |  |
| `2.03` | Kéo ghế kim loại trong phòng hỏi cung | 🟢 TÁI DÙNG | `t2/fx_chair_scrape.wav` |  |
| `2.03` | (phần) Rót nước trà ấm | 🔴 **TẠO MỚI** | `fx_tea_pour_cup.wav` |  |
| `2.05` | Đặt tách cà phê xuống bàn | 🟢 TÁI DÙNG | `t2/fx_cup_down.wav` |  |
| `2.05` | (phần) Mở nắp bút bi sột soạt | 🔴 **TẠO MỚI** | `fx_pen_cap_open.wav` |  |
| `2.07` | Lật mở hồ sơ nhân chứng năm xưa | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.07` | (phần) Thở dài cay đắng của điều tra viên | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | dùng chung T17, T18, T19, T21, T23, T25, T27 |
| `4.03` | Búa tòa án gõ dứt khoát ba tiếng | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |
| `4.03` | (phần) Thở phào nhẹ nhõm từ hàng ghế | 🔴 **TẠO MỚI** | `fx_crowd_relief_sigh.wav` | dùng chung T19, T21 |
| `4.05` | Máy ảnh chớp nháy liên hồi | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `4.05` | (phần) Vỗ tay vang dội phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_applause_court.wav` |  |
| `4.07` | Khóa cửa sắt nhà tù đóng sập nặng nề | 🟢 TÁI DÙNG | `t2/fx_door_metal_slam.wav` |  |
| `4.07` | (phần) Bước chân giám thị | 🟢 TÁI DÙNG | `footsteps.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió thổi rít qua cánh đồng hoang vắng | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng mưa rơi rả rích | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng bước chân vang vọng trong hành lang nhà tù bê tông | 🟢 TÁI DÙNG | `footsteps.wav` | nền Hồi 2 |

### Tập 25 — Hồ Sơ Yoo Young-chul — Sát Nhân Áo Mưa & Cơn Cuồng Nộ Thù Hận Xã Hội

`01_KICH_BAN/Tap25/kichban_tap25_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass + hú báo động → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Mưa rơi rả rích trên mái tôn | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` |  |
| `1.03` | (phần) Búa tạ kim loại gõ xuống nền bê tông | 🔴 **TẠO MỚI** | `fx_sledgehammer_impact_concrete.wav` |  |
| `1.05` | Chuông điện thoại bàn reo dồn dập | 🔴 **TẠO MỚI** | `fx_landline_ring_office.wav` | dùng chung T14 |
| `1.05` | (phần) Còi xe tuần tra rền rĩ | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.08` | Giằng co dồn dập trên mặt đường ướt | 🔴 **TẠO MỚI** | `fx_handcuffs_struggle_chain.wav` |  |
| `1.08` | (phần) Còng số tám bập lại đanh thép | 🔴 **TẠO MỚI** | `fx_handcuff_snap.wav` | dùng chung T18, T23, T28 |
| `2.03` | Cánh cửa kính vỡ loảng xoảng | 🔴 **TẠO MỚI** | `fx_glass_smash_vehicle_crash.wav` | dùng chung T14 |
| `2.03` | (phần) Còi xe tuần tra dồn dập | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `2.05` | Cánh cửa sắt phòng thẩm vấn đóng sập | 🟢 TÁI DÙNG | `t2/fx_door_metal_slam.wav` |  |
| `2.05` | (phần) Lật mở biên bản hỏi cung dồn dập | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.07` | Máy ảnh chớp nháy dồn dập | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `2.07` | (phần) Xẻng đào bới đất đá trong đêm mưa | 🔴 **TẠO MỚI** | `fx_shovel_pick_dirt_stone.wav` | dùng chung T18 |
| `4.03` | Ồn ào phẫn nộ từ phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_angry_jeers.wav` | dùng chung T18 |
| `4.03` | (phần) Gõ búa giữ trật tự nghiêm khắc | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.05` | Lật mở tập hồ sơ giám định ADN dày đặc | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | (phần) Micro của công tố viên | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | Micro của đại diện gia đình nạn nhân | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | (phần) Nấc nghẹn ngào từ hàng ghế khán phòng | 🔴 **TẠO MỚI** | `fx_sobbing_crowd_row.wav` | dùng chung T26, T27 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng mưa rơi dồn dập trong đêm tối | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng còi hú báo động | 🔴 **TẠO MỚI** | `amb_alarm_siren_distant.wav` | nền Hồi 2 — dùng chung T08, T12 |
| `BGM 2.01` | Tiếng bước chân chạy gấp gáp trên nền bê tông | 🔴 **TẠO MỚI** | `fx_footsteps_run_gravel.wav` | nền Hồi 2 — dùng chung T24, T28 |

### Tập 26 — Hồ Sơ Miyuki Ishikawa — Nữ Hộ Sinh Kotobuki & Tội Ác Dưới Lớp Vỏ Bọc Từ Thiện

`01_KICH_BAN/Tap26/kichban_tap26_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + gió + tuyết → `bgm_cello_sad` + `t2/amb_winter_wind` · H2 deep ambient → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Bánh xe gỗ kẽo kẹt lăn trên đường đá vụn | 🔴 **TẠO MỚI** | `amb_wooden_cart_stone_road.wav` |  |
| `1.03` | (phần) Gió mùa đông gầm rú lạnh buốt | 🔴 **TẠO MỚI** | `amb_winter_wind_hollow.wav` |  |
| `1.05` | Gõ bàn thẩm vấn dồn dập | 🔴 **TẠO MỚI** | `fx_knock_table.wav` | dùng chung T15 |
| `1.05` | (phần) Lật giở giấy tờ kiểm tra hộ khẩu | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `1.08` | Động cơ xe tuần tra nổ máy dồn dập | 🔴 **TẠO MỚI** | `amb_car_engine_idle.wav` | dùng chung T10, T22 |
| `1.08` | (phần) Bước chân cảnh sát rầm rập bao vây tòa nhà | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `2.03` | Đếm tiền giấy sột soạt | 🔴 **TẠO MỚI** | `fx_counting_cash.wav` |  |
| `2.03` | (phần) Đóng dấu mộc trên văn bản hành chính | 🔴 **TẠO MỚI** | `fx_stamp_wood.wav` | dùng chung T04, T07 |
| `2.05` | Cánh cửa sắt phòng thẩm vấn đóng sập | 🟢 TÁI DÙNG | `t2/fx_door_metal_slam.wav` |  |
| `2.05` | (phần) Lật mở các tập hóa đơn tài chính | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.07` | Máy ảnh chớp nháy của các phóng viên | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `2.07` | (phần) Xì xào phẫn nộ của dư luận ngoài cổng tòa án | 🔴 **TẠO MỚI** | `amb_crowd_outside_press_anger.wav` |  |
| `4.03` | Ồn ào xôn xao từ phòng xử án | 🔴 **TẠO MỚI** | `amb_crowd_murmur_courtroom.wav` | dùng chung T14, T17–T28 |
| `4.03` | (phần) Gõ búa giữ trật tự nghiêm khắc | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.05` | Lật mở hồ sơ bằng chứng dày đặc | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | (phần) Micro của vị công tố viên | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | Micro nghẹn ngào của nhân chứng đại diện thân nhân | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | (phần) Nấc khóc xót xa từ hàng ghế khán phòng | 🔴 **TẠO MỚI** | `fx_sobbing_crowd_row.wav` | dùng chung T25, T27 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít qua những khu phố đổ nát | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng mưa tuyết rơi lạnh lẽo | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 1 — lớp mưa; gió lạnh dùng amb_winter_wind_hollow ở cue 1.03 |
| `BGM 2.01` | Tiếng máy đánh chữ lọc cọc | 🟢 TÁI DÙNG | `typewriter.wav` | nền Hồi 2 |
| `BGM 2.01` | Tiếng bước chân trong hành lang ẩm mốc | 🟢 TÁI DÙNG | `footsteps.wav` | nền Hồi 2 |

### Tập 27 — Hồ Sơ Nguyễn Hải Dương — Tổn Thương Ái Kỷ & Thao Túng Đồng Phạm

`01_KICH_BAN/Tap27/kichban_tap27_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Xe máy dừng gấp trước cổng sắt | 🔴 **TẠO MỚI** | `fx_motorbike_stop_engine.wav` |  |
| `1.03` | (phần) Chìa khóa tra vào ổ khóa kẽo kẹt | 🔴 **TẠO MỚI** | `fx_key_in_lock.wav` | dùng chung T14 |
| `1.05` | Còi xe cảnh sát hú dồn dập | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `1.05` | (phần) Bước chân phong tỏa hiện trường | 🟢 TÁI DÙNG | `footsteps.wav` |  |
| `1.08` | Chụp ảnh hiện trường chớp nháy liên tục | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `1.08` | (phần) Đo đạc dấu vết cơ học | 🔴 **TẠO MỚI** | `fx_evidence_measure_tape.wav` | dùng chung T28 |
| `2.03` | Chuông điện thoại trích xuất dữ liệu | 🔴 **TẠO MỚI** | `fx_modem_dialup_data.wav` |  |
| `2.03` | (phần) Lật giở bảng kê cuộc gọi viễn thông | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `2.05` | Cánh cửa sắt phòng hỏi cung đóng sập | 🟢 TÁI DÙNG | `t2/fx_door_metal_slam.wav` |  |
| `2.05` | (phần) Đặt tập hồ sơ dày cộp lên mặt bàn | 🟢 TÁI DÙNG | `stamp_thud.wav` |  |
| `2.07` | Còi xe hú dồn dập | 🟢 TÁI DÙNG | `police_siren_distant.wav` |  |
| `2.07` | (phần) Đạp cửa bắt giữ đối tượng trong đêm mưa | 🔴 **TẠO MỚI** | `fx_door_kick_boot.wav` | dùng chung T16 |
| `4.03` | Ồn ào căm phẫn của hàng nghìn người dân | 🔴 **TẠO MỚI** | `amb_crowd_mourning_outdoor.wav` | dùng chung T28 |
| `4.03` | (phần) Búa tòa án gõ mạnh mẽ | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.05` | Lật mở các tập hồ sơ tài liệu chứng cứ | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | (phần) Micro của vị đại diện Viện Kiểm sát | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | Nấc nghẹn ngào từ hàng ghế đại diện gia đình nạn nhân | 🔴 **TẠO MỚI** | `fx_sobbing_crowd_row.wav` | dùng chung T25, T26 |
| `4.07` | (phần) Thở dài xót xa của người dân | 🔴 **TẠO MỚI** | `fx_sigh_emotional.wav` | dùng chung T17, T18, T19, T21, T23, T24, T25 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng gió rít qua cánh rừng cao su bạt ngàn | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng mưa rả rích đầu mùa | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng gõ bàn phím máy tính phân tích dữ liệu viễn thông | 🟢 TÁI DÙNG | `keyboard_night.wav` | nền Hồi 2 |
| `BGM 2.01` | Tiếng bước chân trinh sát | 🟢 TÁI DÙNG | `footsteps.wav` | nền Hồi 2 |

### Tập 28 — Hồ Sơ Lê Văn Luyện — Cơn Cuồng Loạn Trong Đêm Mưa Bão & Bi Kịch Vị Thành Niên

`01_KICH_BAN/Tap28/kichban_tap28_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + sấm + bão → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass + động cơ xe → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Bước chân chạy vội vã trên vỉa hè ướt mưa | 🔴 **TẠO MỚI** | `fx_footsteps_run_wet_pavement.wav` | dùng chung T29 |
| `1.03` | (phần) Đập cửa cuốn sắt thình thình | 🔴 **TẠO MỚI** | `fx_roller_shutter_slam.wav` |  |
| `1.05` | Còi hụ cấp cứu dồn dập | 🔴 **TẠO MỚI** | `fx_ambulance_siren_close.wav` | dùng chung T08, T11, T23, T25 |
| `1.05` | (phần) Rào chắn kim loại của cảnh sát phong tỏa | 🔴 **TẠO MỚI** | `fx_metal_barrier_drop.wav` |  |
| `1.08` | Máy ảnh chớp nháy dồn dập | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `1.08` | (phần) Đo đạc kích thước dấu chân trên sàn nhà | 🔴 **TẠO MỚI** | `fx_evidence_measure_tape.wav` | dùng chung T27 |
| `2.03` | Gió thổi ào ào qua hẻm núi biên giới | 🔴 **TẠO MỚI** | `amb_wind_mountain_pass.wav` |  |
| `2.03` | (phần) Máy bộ đàm liên lạc dồn dập | 🟢 TÁI DÙNG | `radio_chatter.wav` |  |
| `2.05` | Còng số tám bập lại đanh thép | 🔴 **TẠO MỚI** | `fx_handcuff_snap.wav` | dùng chung T18, T23, T25 |
| `2.05` | (phần) Bước chân áp giải đối tượng qua đường rừng | 🔴 **TẠO MỚI** | `fx_footsteps_chase_forest.wav` |  |
| `2.07` | Máy ảnh chớp nháy của hàng chục phóng viên | 🟢 TÁI DÙNG | `t2/fx_camera_shutter.wav` |  |
| `2.07` | (phần) Xôn xao của dư luận khi đối tượng được di lý | 🔴 **TẠO MỚI** | `amb_crowd_murmur_press.wav` | dùng chung T09, T20, T21, T22 |
| `4.03` | Ồn ào căm phẫn từ hội trường xử án | 🔴 **TẠO MỚI** | `amb_crowd_murmur_hall_1000.wav` |  |
| `4.03` | (phần) Búa tòa án gõ giữ trật tự | 🟢 TÁI DÙNG | `gavel.wav` |  |
| `4.05` | Lật giở các tập hồ sơ pháp lý | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.05` | (phần) Micro của vị chủ tọa phiên tòa | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.07` | Khóc nức nở của đại diện gia đình bị hại | 🔴 **TẠO MỚI** | `fx_crying_family_representative.wav` |  |
| `4.07` | (phần) Xôn xao từ hàng ghế khán phòng | 🔴 **TẠO MỚI** | `amb_crowd_murmur_courtroom.wav` | dùng chung T14, T17–T27 |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng sấm rền từ xa | 🔴 **TẠO MỚI** | `amb_thunder_distant.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng gió bão rít qua những mái nhà tôn | 🟢 TÁI DÙNG | `t2/amb_winter_wind.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng mưa như trút nước giữa đêm tối | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng động cơ xe tuần tra gầm rú | 🔴 **TẠO MỚI** | `amb_car_engine_idle.wav` | nền Hồi 2 — dùng chung T10, T22, T26 |
| `BGM 2.01` | Tiếng bước chân hành quân gấp gáp trong rừng sâu | 🔴 **TẠO MỚI** | `fx_footsteps_chase_forest.wav` | nền Hồi 2 |

### Tập 29 — Hồ Sơ Jeffrey Dahmer — Sát Nhân Từ Nỗi Sợ Bị Bỏ Rơi Bệnh Lý

`01_KICH_BAN/Tap29/kichban_tap29_*.md`

**Nhạc nền / dải nền theo hồi:**

H1 cello + bass + mưa + còi tuần tra → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 cello + gõ nhịp kim loại + quạt → `bgm_cello_sad_v2` + `amb_ceiling_fan` (MỚI) · H3 piano tối giản → `bgm_piano_minimal` · H4 violin + búa tòa → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `1.03` | Bước chân chạy thục mạng trên vỉa hè | 🔴 **TẠO MỚI** | `fx_footsteps_run_wet_pavement.wav` | dùng chung T28 |
| `1.03` | (phần) Xích còng sắt va chạm lách cách | 🟢 TÁI DÙNG | `chains.wav` |  |
| `1.05` | Cửa khóa trái khô khốc | 🔴 **TẠO MỚI** | `fx_lock_turning_dry.wav` |  |
| `1.05` | (phần) Rì rầm ma quái từ màn hình tivi | 🔴 **TẠO MỚI** | `amb_tv_static_eerie.wav` |  |
| `1.08` | Gõ cửa dồn dập | 🟢 TÁI DÙNG | `door_knock.wav` |  |
| `1.08` | (phần) Bản lề cửa gỗ rít lên khi hé mở | 🔴 **TẠO MỚI** | `fx_wooden_hinge_creak_open.wav` |  |
| `2.03` | Rót nước nóng vào ly giấy | 🔴 **TẠO MỚI** | `fx_pour_hot_water_paper_cup.wav` |  |
| `2.03` | (phần) Bật lửa châm thuốc lá lách tách | 🔴 **TẠO MỚI** | `fx_lighter_flick_flame.wav` |  |
| `4.03` | Micro rè rè | 🔴 **TẠO MỚI** | `fx_mic_hum_feedback.wav` | dùng chung T15–T29 |
| `4.03` | (phần) Lật giở hồ sơ bệnh án dày cộp của các luật sư | 🟢 TÁI DÙNG | `paper_rustle.wav` |  |
| `4.08` | Gõ búa tòa án vang lên ba tiếng | 🟢 TÁI DÙNG | `t2/fx_gavel_triple.wav` |  |

**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:

| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |
|---|---|---|---|---|
| `BGM 1.01` | Tiếng mưa đêm rả rích | 🟢 TÁI DÙNG | `t3/amb_rain_storm.wav` | nền Hồi 1 |
| `BGM 1.01` | Tiếng còi tuần tra xa xăm của cảnh sát | 🟢 TÁI DÙNG | `police_siren_distant.wav` | nền Hồi 1 |
| `BGM 2.01` | Tiếng gõ nhịp kim loại lạnh lẽo | 🟢 TÁI DÙNG | `t2/fx_tension_tick.wav` | nền Hồi 2 |
| `BGM 2.01` | Tiếng quạt thông gió trong phòng hỏi cung | 🔴 **TẠO MỚI** | `amb_ceiling_fan.wav` | nền Hồi 2 — dùng chung T12, T20 |

---

## 4. Danh mục 169 file mới — đặt ở đâu, dùng cho tập nào

**Quy tắc đặt file:** dùng ≥ 2 tập → `assets/sfx/<file>` (gốc, dùng chung toàn series) · chỉ 1 tập → `assets/sfx/tXX/<file>`.

| # | File | Loại | Dùng cho tập | Đặt tại |
|---:|---|---|---|---|
| 1 | `fx_mic_hum_feedback.wav` | tiếng động | T15, T17, T18, T19, T20, T21, T22, T25, T26, T27, T28, T29 | `assets/sfx/fx_mic_hum_feedback.wav` |
| 2 | `fx_sigh_emotional.wav` | tiếng động | T06, T07, T17, T18, T19, T21, T23, T24, T27 | `assets/sfx/fx_sigh_emotional.wav` |
| 3 | `amb_crowd_murmur_courtroom.wav` | nền môi trường | T14, T15, T17, T19, T22, T26, T28 | `assets/sfx/amb_crowd_murmur_courtroom.wav` |
| 4 | `amb_crowd_murmur_press.wav` | nền môi trường | T09, T20, T21, T22, T28 | `assets/sfx/amb_crowd_murmur_press.wav` |
| 5 | `fx_breathing_tense_close.wav` | tiếng động | T12, T17, T19, T20, T22 | `assets/sfx/fx_breathing_tense_close.wav` |
| 6 | `amb_car_engine_idle.wav` | nền môi trường | T10, T22, T26, T28 | `assets/sfx/amb_car_engine_idle.wav` |
| 7 | `fx_ambulance_siren_close.wav` | tiếng động | T08, T11, T23, T28 | `assets/sfx/fx_ambulance_siren_close.wav` |
| 8 | `fx_handcuff_snap.wav` | tiếng động | T18, T23, T25, T28 | `assets/sfx/fx_handcuff_snap.wav` |
| 9 | `amb_alarm_siren_distant.wav` | nền môi trường | T08, T12, T25 | `assets/sfx/amb_alarm_siren_distant.wav` |
| 10 | `amb_ceiling_fan.wav` | nền môi trường | T12, T20, T29 | `assets/sfx/amb_ceiling_fan.wav` |
| 11 | `amb_hospital_monitor_heartbeat.wav` | nền môi trường | T13, T21, T23 | `assets/sfx/amb_hospital_monitor_heartbeat.wav` |
| 12 | `amb_ocean_waves_soft.wav` | nền môi trường | T09, T14, T18 | `assets/sfx/amb_ocean_waves_soft.wav` |
| 13 | `fx_crowd_relief_sigh.wav` | tiếng động | T19, T21, T24 | `assets/sfx/fx_crowd_relief_sigh.wav` |
| 14 | `fx_phone_ring_landline_night.wav` | tiếng động | T15, T16, T18 | `assets/sfx/fx_phone_ring_landline_night.wav` |
| 15 | `fx_printer_thermal.wav` | tiếng động | T07, T15, T23 | `assets/sfx/fx_printer_thermal.wav` |
| 16 | `fx_sobbing_crowd_row.wav` | tiếng động | T25, T26, T27 | `assets/sfx/fx_sobbing_crowd_row.wav` |
| 17 | `fx_stamp_wood.wav` | tiếng động | T04, T07, T26 | `assets/sfx/fx_stamp_wood.wav` |
| 18 | `amb_crowd_angry_jeers.wav` | nền môi trường | T18, T25 | `assets/sfx/amb_crowd_angry_jeers.wav` |
| 19 | `amb_helicopter_far.wav` | nền môi trường | T12, T14 | `assets/sfx/amb_helicopter_far.wav` |
| 20 | `amb_party_crowd_outdoor.wav` | nền môi trường | T11, T14 | `assets/sfx/amb_party_crowd_outdoor.wav` |
| 21 | `amb_tv_camera_operator.wav` | nền môi trường | T15, T22 | `assets/sfx/amb_tv_camera_operator.wav` |
| 22 | `fx_ambulance_siren_distant.wav` | tiếng động | T04, T19 | `assets/sfx/fx_ambulance_siren_distant.wav` |
| 23 | `fx_car_door_close.wav` | tiếng động | T21, T22 | `assets/sfx/fx_car_door_close.wav` |
| 24 | `fx_car_tire_screech_stop.wav` | tiếng động | T10, T22 | `assets/sfx/fx_car_tire_screech_stop.wav` |
| 25 | `fx_door_kick_boot.wav` | tiếng động | T16, T27 | `assets/sfx/fx_door_kick_boot.wav` |
| 26 | `fx_dtmf_touch_tone_beep.wav` | tiếng động | T13, T17 | `assets/sfx/fx_dtmf_touch_tone_beep.wav` |
| 27 | `fx_envelope_tear.wav` | tiếng động | T05, T23 | `assets/sfx/fx_envelope_tear.wav` |
| 28 | `fx_evidence_measure_tape.wav` | tiếng động | T27, T28 | `assets/sfx/fx_evidence_measure_tape.wav` |
| 29 | `fx_footsteps_run_gravel.wav` | tiếng động | T24, T25 | `assets/sfx/fx_footsteps_run_gravel.wav` |
| 30 | `fx_footsteps_run_wet_pavement.wav` | tiếng động | T28, T29 | `assets/sfx/fx_footsteps_run_wet_pavement.wav` |
| 31 | `fx_glass_smash_vehicle_crash.wav` | tiếng động | T14, T25 | `assets/sfx/fx_glass_smash_vehicle_crash.wav` |
| 32 | `fx_glasses_clink.wav` | tiếng động | T11, T14 | `assets/sfx/fx_glasses_clink.wav` |
| 33 | `fx_inkjet_printer_run.wav` | tiếng động | T13, T18 | `assets/sfx/fx_inkjet_printer_run.wav` |
| 34 | `fx_key_in_lock.wav` | tiếng động | T14, T27 | `assets/sfx/fx_key_in_lock.wav` |
| 35 | `fx_knock_table.wav` | tiếng động | T15, T26 | `assets/sfx/fx_knock_table.wav` |
| 36 | `fx_landline_ring_office.wav` | tiếng động | T14, T25 | `assets/sfx/fx_landline_ring_office.wav` |
| 37 | `fx_mouse_click_rapid.wav` | tiếng động | T15, T22 | `assets/sfx/fx_mouse_click_rapid.wav` |
| 38 | `fx_pen_signing_scroll.wav` | tiếng động | T20, T23 | `assets/sfx/fx_pen_signing_scroll.wav` |
| 39 | `fx_phone_vibrate.wav` | tiếng động | T07, T13 | `assets/sfx/fx_phone_vibrate.wav` |
| 40 | `fx_shovel_pick_dirt_stone.wav` | tiếng động | T18, T25 | `assets/sfx/fx_shovel_pick_dirt_stone.wav` |
| 41 | `fx_video_playback_static.wav` | tiếng động | T19, T22 | `assets/sfx/fx_video_playback_static.wav` |
| 42 | `fx_window_pry_break.wav` | tiếng động | T16, T23 | `assets/sfx/fx_window_pry_break.wav` |
| 43 | `amb_bus_distant.wav` | nền môi trường | T13 | `assets/sfx/t13/amb_bus_distant.wav` |
| 44 | `amb_camera_crew_press.wav` | nền môi trường | T20 | `assets/sfx/t20/amb_camera_crew_press.wav` |
| 45 | `amb_car_start_leave_garage.wav` | nền môi trường | T21 | `assets/sfx/t21/amb_car_start_leave_garage.wav` |
| 46 | `amb_carnival_ride_music_far.wav` | nền môi trường | T17 | `assets/sfx/t17/amb_carnival_ride_music_far.wav` |
| 47 | `amb_crowd_angry_whisper.wav` | nền môi trường | T20 | `assets/sfx/t20/amb_crowd_angry_whisper.wav` |
| 48 | `amb_crowd_applause_court.wav` | nền môi trường | T24 | `assets/sfx/t24/amb_crowd_applause_court.wav` |
| 49 | `amb_crowd_applause_distant.wav` | nền môi trường | T06 | `assets/sfx/t06/amb_crowd_applause_distant.wav` |
| 50 | `amb_crowd_arguing_indoor.wav` | nền môi trường | T12 | `assets/sfx/t12/amb_crowd_arguing_indoor.wav` |
| 51 | `amb_crowd_cheer_outdoor.wav` | nền môi trường | T23 | `assets/sfx/t23/amb_crowd_cheer_outdoor.wav` |
| 52 | `amb_crowd_excited_girls.wav` | nền môi trường | T23 | `assets/sfx/t23/amb_crowd_excited_girls.wav` |
| 53 | `amb_crowd_mourning_outdoor.wav` | nền môi trường | T27 | `assets/sfx/t27/amb_crowd_mourning_outdoor.wav` |
| 54 | `amb_crowd_murmur_hall_1000.wav` | nền môi trường | T28 | `assets/sfx/t28/amb_crowd_murmur_hall_1000.wav` |
| 55 | `amb_crowd_outside_press_anger.wav` | nền môi trường | T26 | `assets/sfx/t26/amb_crowd_outside_press_anger.wav` |
| 56 | `amb_crowd_singing_acoustic.wav` | nền môi trường | T12 | `assets/sfx/t12/amb_crowd_singing_acoustic.wav` |
| 57 | `amb_desert_wind_dry.wav` | nền môi trường | T09 | `assets/sfx/t09/amb_desert_wind_dry.wav` |
| 58 | `amb_fastfood_cafeteria.wav` | nền môi trường | T04 | `assets/sfx/t04/amb_fastfood_cafeteria.wav` |
| 59 | `amb_female_humming_far.wav` | nền môi trường | T09 | `assets/sfx/t09/amb_female_humming_far.wav` |
| 60 | `amb_highway_speed_car.wav` | nền môi trường | T10 | `assets/sfx/t10/amb_highway_speed_car.wav` |
| 61 | `amb_horse_hooves_distant.wav` | nền môi trường | T09 | `assets/sfx/t09/amb_horse_hooves_distant.wav` |
| 62 | `amb_hospital_ventilator.wav` | nền môi trường | T04 | `assets/sfx/t04/amb_hospital_ventilator.wav` |
| 63 | `amb_lab_equipment.wav` | nền môi trường | T24 | `assets/sfx/t24/amb_lab_equipment.wav` |
| 64 | `amb_lawyers_discussion.wav` | nền môi trường | T21 | `assets/sfx/t21/amb_lawyers_discussion.wav` |
| 65 | `amb_library_quiet.wav` | nền môi trường | T13 | `assets/sfx/t13/amb_library_quiet.wav` |
| 66 | `amb_loudspeaker_jungle_echo.wav` | nền môi trường | T12 | `assets/sfx/t12/amb_loudspeaker_jungle_echo.wav` |
| 67 | `amb_megaphone_loudspeaker.wav` | nền môi trường | T08 | `assets/sfx/t08/amb_megaphone_loudspeaker.wav` |
| 68 | `amb_panic_crowd_schoolyard.wav` | nền môi trường | T19 | `assets/sfx/t19/amb_panic_crowd_schoolyard.wav` |
| 69 | `amb_projector_room.wav` | nền môi trường | T11 | `assets/sfx/t11/amb_projector_room.wav` |
| 70 | `amb_server_fan.wav` | nền môi trường | T05 | `assets/sfx/t05/amb_server_fan.wav` |
| 71 | `amb_small_plane_engine.wav` | nền môi trường | T12 | `assets/sfx/t12/amb_small_plane_engine.wav` |
| 72 | `amb_subway_station_jp.wav` | nền môi trường | T08 | `assets/sfx/t08/amb_subway_station_jp.wav` |
| 73 | `amb_thunder_distant.wav` | nền môi trường | T28 | `assets/sfx/t28/amb_thunder_distant.wav` |
| 74 | `amb_tractor_engine.wav` | nền môi trường | T12 | `assets/sfx/t12/amb_tractor_engine.wav` |
| 75 | `amb_train_horn_distant_night.wav` | nền môi trường | T16 | `assets/sfx/t16/amb_train_horn_distant_night.wav` |
| 76 | `amb_tv_static_eerie.wav` | nền môi trường | T29 | `assets/sfx/t29/amb_tv_static_eerie.wav` |
| 77 | `amb_wind_chime.wav` | nền môi trường | T18 | `assets/sfx/t18/amb_wind_chime.wav` |
| 78 | `amb_wind_mountain_pass.wav` | nền môi trường | T28 | `assets/sfx/t28/amb_wind_mountain_pass.wav` |
| 79 | `amb_wind_pines.wav` | nền môi trường | T09 | `assets/sfx/t09/amb_wind_pines.wav` |
| 80 | `amb_wind_tropical.wav` | nền môi trường | T12 | `assets/sfx/t12/amb_wind_tropical.wav` |
| 81 | `amb_winter_wind_hollow.wav` | nền môi trường | T26 | `assets/sfx/t26/amb_winter_wind_hollow.wav` |
| 82 | `amb_wooden_cart_stone_road.wav` | nền môi trường | T26 | `assets/sfx/t26/amb_wooden_cart_stone_road.wav` |
| 83 | `fx_911_call_recording_radio.wav` | tiếng động | T17 | `assets/sfx/t17/fx_911_call_recording_radio.wav` |
| 84 | `fx_baby_crying_night.wav` | tiếng động | T14 | `assets/sfx/t14/fx_baby_crying_night.wav` |
| 85 | `fx_bread_bag_open.wav` | tiếng động | T19 | `assets/sfx/t19/fx_bread_bag_open.wav` |
| 86 | `fx_breathing_focused_artist.wav` | tiếng động | T16 | `assets/sfx/t16/fx_breathing_focused_artist.wav` |
| 87 | `fx_breathing_tired.wav` | tiếng động | T23 | `assets/sfx/t23/fx_breathing_tired.wav` |
| 88 | `fx_candy_wrapper_open.wav` | tiếng động | T17 | `assets/sfx/t17/fx_candy_wrapper_open.wav` |
| 89 | `fx_car_brake_screech.wav` | tiếng động | T05 | `assets/sfx/t05/fx_car_brake_screech.wav` |
| 90 | `fx_car_window_knock.wav` | tiếng động | T07 | `assets/sfx/t07/fx_car_window_knock.wav` |
| 91 | `fx_card_swipe.wav` | tiếng động | T04 | `assets/sfx/t04/fx_card_swipe.wav` |
| 92 | `fx_chisel_hammer_clay.wav` | tiếng động | T16 | `assets/sfx/t16/fx_chisel_hammer_clay.wav` |
| 93 | `fx_computer_beep_restore.wav` | tiếng động | T15 | `assets/sfx/t15/fx_computer_beep_restore.wav` |
| 94 | `fx_counting_cash.wav` | tiếng động | T26 | `assets/sfx/t26/fx_counting_cash.wav` |
| 95 | `fx_courtroom_dead_silence.wav` | tiếng động | T22 | `assets/sfx/t22/fx_courtroom_dead_silence.wav` |
| 96 | `fx_crime_scene_tape_pull.wav` | tiếng động | T15 | `assets/sfx/t15/fx_crime_scene_tape_pull.wav` |
| 97 | `fx_crying_family_representative.wav` | tiếng động | T28 | `assets/sfx/t28/fx_crying_family_representative.wav` |
| 98 | `fx_crying_female_phone.wav` | tiếng động | T13 | `assets/sfx/t13/fx_crying_female_phone.wav` |
| 99 | `fx_cup_shatter_tea.wav` | tiếng động | T16 | `assets/sfx/t16/fx_cup_shatter_tea.wav` |
| 100 | `fx_defib_charge_shock.wav` | tiếng động | T04 | `assets/sfx/t04/fx_defib_charge_shock.wav` |
| 101 | `fx_dog_bark_working.wav` | tiếng động | T18 | `assets/sfx/t18/fx_dog_bark_working.wav` |
| 102 | `fx_door_slam_indoor.wav` | tiếng động | T19 | `assets/sfx/t19/fx_door_slam_indoor.wav` |
| 103 | `fx_doorbell_chime.wav` | tiếng động | T10 | `assets/sfx/t10/fx_doorbell_chime.wav` |
| 104 | `fx_evidence_cabinet_open.wav` | tiếng động | T18 | `assets/sfx/t18/fx_evidence_cabinet_open.wav` |
| 105 | `fx_evidence_room_door.wav` | tiếng động | T15 | `assets/sfx/t15/fx_evidence_room_door.wav` |
| 106 | `fx_floppy_disk_insert.wav` | tiếng động | T05 | `assets/sfx/t05/fx_floppy_disk_insert.wav` |
| 107 | `fx_footsteps_barefoot_stairs.wav` | tiếng động | T14 | `assets/sfx/t14/fx_footsteps_barefoot_stairs.wav` |
| 108 | `fx_footsteps_chase_forest.wav` | tiếng động | T28 | `assets/sfx/t28/fx_footsteps_chase_forest.wav` |
| 109 | `fx_footsteps_dusty_wood_slow.wav` | tiếng động | T16 | `assets/sfx/t16/fx_footsteps_dusty_wood_slow.wav` |
| 110 | `fx_footsteps_gravel_stealth.wav` | tiếng động | T09 | `assets/sfx/t09/fx_footsteps_gravel_stealth.wav` |
| 111 | `fx_footsteps_shoes_scuff.wav` | tiếng động | T15 | `assets/sfx/t15/fx_footsteps_shoes_scuff.wav` |
| 112 | `fx_footsteps_stealth_wood.wav` | tiếng động | T23 | `assets/sfx/t23/fx_footsteps_stealth_wood.wav` |
| 113 | `fx_footsteps_wood_heavy.wav` | tiếng động | T13 | `assets/sfx/t13/fx_footsteps_wood_heavy.wav` |
| 114 | `fx_fridge_door_open.wav` | tiếng động | T17 | `assets/sfx/t17/fx_fridge_door_open.wav` |
| 115 | `fx_gravel_car_drive.wav` | tiếng động | T10 | `assets/sfx/t10/fx_gravel_car_drive.wav` |
| 116 | `fx_gunshots_pistol_inside.wav` | tiếng động | T13 | `assets/sfx/t13/fx_gunshots_pistol_inside.wav` |
| 117 | `fx_gunshots_revolver_5.wav` | tiếng động | T14 | `assets/sfx/t14/fx_gunshots_revolver_5.wav` |
| 118 | `fx_gunshots_rifle_shotgun.wav` | tiếng động | T12 | `assets/sfx/t12/fx_gunshots_rifle_shotgun.wav` |
| 119 | `fx_handcuffs_chain_on_metal_table.wav` | tiếng động | T19 | `assets/sfx/t19/fx_handcuffs_chain_on_metal_table.wav` |
| 120 | `fx_handcuffs_struggle_chain.wav` | tiếng động | T25 | `assets/sfx/t25/fx_handcuffs_struggle_chain.wav` |
| 121 | `fx_hatch_lid_open.wav` | tiếng động | T06 | `assets/sfx/t06/fx_hatch_lid_open.wav` |
| 122 | `fx_hospital_door_open.wav` | tiếng động | T04 | `assets/sfx/t04/fx_hospital_door_open.wav` |
| 123 | `fx_keyboard_typing_soft.wav` | tiếng động | T13 | `assets/sfx/t13/fx_keyboard_typing_soft.wav` |
| 124 | `fx_keys_drop_on_table.wav` | tiếng động | T20 | `assets/sfx/t20/fx_keys_drop_on_table.wav` |
| 125 | `fx_lab_test_kit.wav` | tiếng động | T18 | `assets/sfx/t18/fx_lab_test_kit.wav` |
| 126 | `fx_latch_unlock.wav` | tiếng động | T10 | `assets/sfx/t10/fx_latch_unlock.wav` |
| 127 | `fx_lav_mic_breathing.wav` | tiếng động | T20 | `assets/sfx/t20/fx_lav_mic_breathing.wav` |
| 128 | `fx_lighter_flick_flame.wav` | tiếng động | T29 | `assets/sfx/t29/fx_lighter_flick_flame.wav` |
| 129 | `fx_liquid_pour_splat.wav` | tiếng động | T08 | `assets/sfx/t08/fx_liquid_pour_splat.wav` |
| 130 | `fx_lock_turning_dry.wav` | tiếng động | T29 | `assets/sfx/t29/fx_lock_turning_dry.wav` |
| 131 | `fx_mechanical_keyboard.wav` | tiếng động | T15 | `assets/sfx/t15/fx_mechanical_keyboard.wav` |
| 132 | `fx_metal_barrier_drop.wav` | tiếng động | T28 | `assets/sfx/t28/fx_metal_barrier_drop.wav` |
| 133 | `fx_metal_door_push_open.wav` | tiếng động | T13 | `assets/sfx/t13/fx_metal_door_push_open.wav` |
| 134 | `fx_metal_lock_open.wav` | tiếng động | T16 | `assets/sfx/t16/fx_metal_lock_open.wav` |
| 135 | `fx_modem_dialup_data.wav` | tiếng động | T27 | `assets/sfx/t27/fx_modem_dialup_data.wav` |
| 136 | `fx_monitor_case_close.wav` | tiếng động | T04 | `assets/sfx/t04/fx_monitor_case_close.wav` |
| 137 | `fx_motorbike_stop_engine.wav` | tiếng động | T27 | `assets/sfx/t27/fx_motorbike_stop_engine.wav` |
| 138 | `fx_notebook_open_pages.wav` | tiếng động | T21 | `assets/sfx/t21/fx_notebook_open_pages.wav` |
| 139 | `fx_objects_smash_break.wav` | tiếng động | T11 | `assets/sfx/t11/fx_objects_smash_break.wav` |
| 140 | `fx_oxygen_breathing.wav` | tiếng động | T13 | `assets/sfx/t13/fx_oxygen_breathing.wav` |
| 141 | `fx_pen_cap_open.wav` | tiếng động | T24 | `assets/sfx/t24/fx_pen_cap_open.wav` |
| 142 | `fx_phone_hangup_click.wav` | tiếng động | T14 | `assets/sfx/t14/fx_phone_hangup_click.wav` |
| 143 | `fx_phone_line_hiss_1970.wav` | tiếng động | T03 | `assets/sfx/t03/fx_phone_line_hiss_1970.wav` |
| 144 | `fx_phone_typing_swipe.wav` | tiếng động | T07 | `assets/sfx/t07/fx_phone_typing_swipe.wav` |
| 145 | `fx_phone_unlock_click.wav` | tiếng động | T19 | `assets/sfx/t19/fx_phone_unlock_click.wav` |
| 146 | `fx_police_tape_flutter.wav` | tiếng động | T22 | `assets/sfx/t22/fx_police_tape_flutter.wav` |
| 147 | `fx_pour_hot_water_paper_cup.wav` | tiếng động | T29 | `assets/sfx/t29/fx_pour_hot_water_paper_cup.wav` |
| 148 | `fx_rifle_shell_load.wav` | tiếng động | T09 | `assets/sfx/t09/fx_rifle_shell_load.wav` |
| 149 | `fx_roller_shutter_slam.wav` | tiếng động | T28 | `assets/sfx/t28/fx_roller_shutter_slam.wav` |
| 150 | `fx_sandpaper_scrape_eraser.wav` | tiếng động | T13 | `assets/sfx/t13/fx_sandpaper_scrape_eraser.wav` |
| 151 | `fx_saw_blade_packaging.wav` | tiếng động | T20 | `assets/sfx/t20/fx_saw_blade_packaging.wav` |
| 152 | `fx_school_bell_dismissal.wav` | tiếng động | T16 | `assets/sfx/t16/fx_school_bell_dismissal.wav` |
| 153 | `fx_scissors_cut_paper.wav` | tiếng động | T16 | `assets/sfx/t16/fx_scissors_cut_paper.wav` |
| 154 | `fx_scream_distant.wav` | tiếng động | T13 | `assets/sfx/t13/fx_scream_distant.wav` |
| 155 | `fx_sewing_machine.wav` | tiếng động | T14 | `assets/sfx/t14/fx_sewing_machine.wav` |
| 156 | `fx_shell_casing_drop.wav` | tiếng động | T14 | `assets/sfx/t14/fx_shell_casing_drop.wav` |
| 157 | `fx_shovel_dirt.wav` | tiếng động | T06 | `assets/sfx/t06/fx_shovel_dirt.wav` |
| 158 | `fx_sigh_female.wav` | tiếng động | T05 | `assets/sfx/t05/fx_sigh_female.wav` |
| 159 | `fx_sledgehammer_impact_concrete.wav` | tiếng động | T25 | `assets/sfx/t25/fx_sledgehammer_impact_concrete.wav` |
| 160 | `fx_spoon_clink.wav` | tiếng động | T04 | `assets/sfx/t04/fx_spoon_clink.wav` |
| 161 | `fx_stretcher_wheels.wav` | tiếng động | T04 | `assets/sfx/t04/fx_stretcher_wheels.wav` |
| 162 | `fx_table_slap_anger.wav` | tiếng động | T11 | `assets/sfx/t11/fx_table_slap_anger.wav` |
| 163 | `fx_tea_pour_cup.wav` | tiếng động | T24 | `assets/sfx/t24/fx_tea_pour_cup.wav` |
| 164 | `fx_train_door_slam.wav` | tiếng động | T08 | `assets/sfx/t08/fx_train_door_slam.wav` |
| 165 | `fx_umbrella_puncture_nylon.wav` | tiếng động | T08 | `assets/sfx/t08/fx_umbrella_puncture_nylon.wav` |
| 166 | `fx_vehicle_impact_metal.wav` | tiếng động | T14 | `assets/sfx/t14/fx_vehicle_impact_metal.wav` |
| 167 | `fx_wooden_hinge_creak_open.wav` | tiếng động | T29 | `assets/sfx/t29/fx_wooden_hinge_creak_open.wav` |
| 168 | `fx_wooden_lid_slam_latch.wav` | tiếng động | T10 | `assets/sfx/t10/fx_wooden_lid_slam_latch.wav` |
| 169 | `fx_zipper_bag.wav` | tiếng động | T07 | `assets/sfx/t07/fx_zipper_bag.wav` |

**Tóm tắt:** 169 file mới — 42 file dùng chung (≥2 tập) đặt ở `assets/sfx/`, 127 file riêng một tập đặt trong `assets/sfx/tXX/`.

### 4.1. 12 file dùng chung nhiều tập nhất — ưu tiên làm trước

| File | Số tập dùng | Các tập |
|---|---:|---|
| `fx_mic_hum_feedback.wav` | 12 | T15, T17, T18, T19, T20, T21, T22, T25, T26, T27, T28, T29 |
| `fx_sigh_emotional.wav` | 9 | T06, T07, T17, T18, T19, T21, T23, T24, T27 |
| `amb_crowd_murmur_courtroom.wav` | 7 | T14, T15, T17, T19, T22, T26, T28 |
| `amb_crowd_murmur_press.wav` | 5 | T09, T20, T21, T22, T28 |
| `fx_breathing_tense_close.wav` | 5 | T12, T17, T19, T20, T22 |
| `amb_car_engine_idle.wav` | 4 | T10, T22, T26, T28 |
| `fx_ambulance_siren_close.wav` | 4 | T08, T11, T23, T28 |
| `fx_handcuff_snap.wav` | 4 | T18, T23, T25, T28 |
| `amb_alarm_siren_distant.wav` | 3 | T08, T12, T25 |
| `amb_ceiling_fan.wav` | 3 | T12, T20, T29 |
| `amb_hospital_monitor_heartbeat.wav` | 3 | T13, T21, T23 |
| `amb_ocean_waves_soft.wav` | 3 | T09, T14, T18 |

---

### 4.2. Nguồn YouTube Audio Library của từng mã — 169/169 đã tải & nhập xong

> Nguồn: YouTube Studio → Thư viện âm thanh (YouTube Audio Library). Tải tay, cắt 2 pass, chuẩn hoá đỉnh −1 dBFS, đưa vào `assets/sfx/` theo cột “Đặt tại” của mục 4. Sổ nguồn đầy đủ: `provenance.json` (mục `track_youtube`, `the_loai_youtube`).

Cột **Ghi chú** đánh dấu các mã dùng **track thay thế** (thư viện không có track đúng nghĩa) — cần duyệt khi dựng bản trộn.

| # | Mã cue | Tập | Track YouTube | Thể loại | File đích | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | `amb_alarm_siren_distant` | nền môi trường | Emergency Siren Approaching | Báo động khẩn cấp | `assets/sfx/amb_alarm_siren_distant.wav` |  |
| 2 | `amb_bus_distant` | nền môi trường | Engine Bus | Phương tiện giao thông | `assets/sfx/t13/amb_bus_distant.wav` |  |
| 3 | `amb_camera_crew_press` | nền môi trường | Transporting A Camera | Công cụ | `assets/sfx/t20/amb_camera_crew_press.wav` |  |
| 4 | `amb_car_engine_idle` | nền môi trường | Engine Rev Continuous | Phương tiện giao thông | `assets/sfx/amb_car_engine_idle.wav` |  |
| 5 | `amb_car_start_leave_garage` | nền môi trường | Muscle Car Start Idle and Drive Away | Phương tiện giao thông | `assets/sfx/t21/amb_car_start_leave_garage.wav` |  |
| 6 | `amb_carnival_ride_music_far` | nền môi trường | Carnival Atmosphere | Không gian xung quanh | `assets/sfx/t17/amb_carnival_ride_music_far.wav` |  |
| 7 | `amb_ceiling_fan` | nền môi trường | Sewing Machine Industrial | Công cụ | `assets/sfx/amb_ceiling_fan.wav` |  |
| 8 | `amb_crowd_angry_jeers` | nền môi trường | Crowd Yelling Series | Đám đông | `assets/sfx/amb_crowd_angry_jeers.wav` |  |
| 9 | `amb_crowd_angry_whisper` | nền môi trường | Murmuring And Talking Men | Đám đông | `assets/sfx/t20/amb_crowd_angry_whisper.wav` |  |
| 10 | `amb_crowd_applause_court` | nền môi trường | Female Crowd Celebration | Đám đông | `assets/sfx/t24/amb_crowd_applause_court.wav` |  |
| 11 | `amb_crowd_applause_distant` | nền môi trường | Battle Crowd Celebrate Stutter | Đám đông | `assets/sfx/t06/amb_crowd_applause_distant.wav` |  |
| 12 | `amb_crowd_arguing_indoor` | nền môi trường | Voices Angry | Đám đông | `assets/sfx/t12/amb_crowd_arguing_indoor.wav` |  |
| 13 | `amb_crowd_cheer_outdoor` | nền môi trường | Battle Crowd Celebration | Đám đông | `assets/sfx/t23/amb_crowd_cheer_outdoor.wav` |  |
| 14 | `amb_crowd_excited_girls` | nền môi trường | Battle Crowd Celebrate Stutter | Đám đông | `assets/sfx/t23/amb_crowd_excited_girls.wav` |  |
| 15 | `amb_crowd_mourning_outdoor` | nền môi trường | Human Group Cry Out | Đám đông | `assets/sfx/t27/amb_crowd_mourning_outdoor.wav` |  |
| 16 | `amb_crowd_murmur_courtroom` | nền môi trường | Crowd Talking | Đám đông | `assets/sfx/amb_crowd_murmur_courtroom.wav` |  |
| 17 | `amb_crowd_murmur_hall_1000` | nền môi trường | Convention Hall Ambience Noise | Không gian xung quanh | `assets/sfx/t28/amb_crowd_murmur_hall_1000.wav` |  |
| 18 | `amb_crowd_murmur_press` | nền môi trường | Small Outdoor Marketplace | Không gian xung quanh | `assets/sfx/amb_crowd_murmur_press.wav` |  |
| 19 | `amb_crowd_outside_press_anger` | nền môi trường | Voices Angry | Đám đông | `assets/sfx/t26/amb_crowd_outside_press_anger.wav` | thay thế - `Voices Murmur` (hoán đổi nguồn với `amb_lawyers_discussion`) |
| 20 | `amb_crowd_singing_acoustic` | nền môi trường | Children Group Ambience | Không gian xung quanh | `assets/sfx/t12/amb_crowd_singing_acoustic.wav` | không có track hát tập thể — dùng tiếng nhóm trẻ (`Children Group Ambience`) |
| 21 | `amb_desert_wind_dry` | nền môi trường | Desert Howling Wind | Thời tiết | `assets/sfx/t09/amb_desert_wind_dry.wav` |  |
| 22 | `amb_fastfood_cafeteria` | nền môi trường | Ladle Food into Carton | Tiếng động thực tế | `assets/sfx/t04/amb_fastfood_cafeteria.wav` | thay thế - `Summer Beach Ambience` (tiếng múc đồ ăn vào hộp) |
| 23 | `amb_female_humming_far` | nền môi trường | Voices On Street Accent | Đám đông | `assets/sfx/t09/amb_female_humming_far.wav` | không có tiếng đàn/humming — dùng `Voices On Street Accent` |
| 24 | `amb_helicopter_far` | nền môi trường | Helicopter Background Noise | Phương tiện giao thông | `assets/sfx/amb_helicopter_far.wav` |  |
| 25 | `amb_highway_speed_car` | nền môi trường | Muscle Car Speeding Highway | Phương tiện giao thông | `assets/sfx/t10/amb_highway_speed_car.wav` |  |
| 26 | `amb_horse_hooves_distant` | nền môi trường | Horse Farm Actions | Phương tiện giao thông | `assets/sfx/t09/amb_horse_hooves_distant.wav` |  |
| 27 | `amb_hospital_monitor_heartbeat` | nền môi trường | Metal Machine Hum | Công cụ | `assets/sfx/amb_hospital_monitor_heartbeat.wav` | không có tiếng monitor tim — dùng tiếng máy ồn (`Metal Machine Hum`) |
| 28 | `amb_hospital_ventilator` | nền môi trường | Machine Sounds Halt Slowly | Tiếng động thực tế | `assets/sfx/t04/amb_hospital_ventilator.wav` |  |
| 29 | `amb_lab_equipment` | nền môi trường | Machine Sewing | Phương tiện giao thông | `assets/sfx/t24/amb_lab_equipment.wav` |  |
| 30 | `amb_lawyers_discussion` | nền môi trường | Voices Murmur | Đám đông | `assets/sfx/t21/amb_lawyers_discussion.wav` | thay thế - `Voices Angry` bản 0:36 → nay dùng tiếng xì xào `Voices Murmur` |
| 31 | `amb_library_quiet` | nền môi trường | Flipping Newspaper Pages | Tiếng động thực tế | `assets/sfx/t13/amb_library_quiet.wav` | thay thế - `Bowling Alley Room Tone` (tiếng lật trang giấy trong thư viện) |
| 32 | `amb_loudspeaker_jungle_echo` | nền môi trường | Subway NYC Announcement | Phương tiện giao thông | `assets/sfx/t12/amb_loudspeaker_jungle_echo.wav` |  |
| 33 | `amb_megaphone_loudspeaker` | nền môi trường | PA Announcement - Close | Giọng của con người | `assets/sfx/t08/amb_megaphone_loudspeaker.wav` |  |
| 34 | `amb_ocean_waves_soft` | nền môi trường | Water Lapping Wind | Nước | `assets/sfx/amb_ocean_waves_soft.wav` |  |
| 35 | `amb_panic_crowd_schoolyard` | nền môi trường | Wild Battle Crowd Approach | Đám đông | `assets/sfx/t19/amb_panic_crowd_schoolyard.wav` |  |
| 36 | `amb_party_crowd_outdoor` | nền môi trường | Small Outdoor Gathering | Không gian xung quanh | `assets/sfx/amb_party_crowd_outdoor.wav` |  |
| 37 | `amb_projector_room` | nền môi trường | Projector Screen Slow Pull | Tiếng động trong nhà | `assets/sfx/t11/amb_projector_room.wav` |  |
| 38 | `amb_server_fan` | nền môi trường | Sewing Machine Series | Công cụ | `assets/sfx/t05/amb_server_fan.wav` |  |
| 39 | `amb_small_plane_engine` | nền môi trường | Motor Aircraft Approaching | Phương tiện giao thông | `assets/sfx/t12/amb_small_plane_engine.wav` |  |
| 40 | `amb_subway_station_jp` | nền môi trường | Subway Station NYC | Không gian xung quanh | `assets/sfx/t08/amb_subway_station_jp.wav` |  |
| 41 | `amb_thunder_distant` | nền môi trường | Distant Thunder | Thời tiết | `assets/sfx/t28/amb_thunder_distant.wav` |  |
| 42 | `amb_tractor_engine` | nền môi trường | Motor Running Loudly | Phương tiện giao thông | `assets/sfx/t12/amb_tractor_engine.wav` |  |
| 43 | `amb_train_horn_distant_night` | nền môi trường | Air Horn in Close Hall - Series | Phương tiện giao thông | `assets/sfx/t16/amb_train_horn_distant_night.wav` |  |
| 44 | `amb_tv_camera_operator` | nền môi trường | Play And Stop On A Camera | Công cụ | `assets/sfx/amb_tv_camera_operator.wav` |  |
| 45 | `amb_tv_static_eerie` | nền môi trường | Radio Static | Tiếng động thực tế | `assets/sfx/t29/amb_tv_static_eerie.wav` |  |
| 46 | `amb_wind_chime` | nền môi trường | Windchime Drone | Khoa học viễn tưởng | `assets/sfx/t18/amb_wind_chime.wav` |  |
| 47 | `amb_wind_mountain_pass` | nền môi trường | Room Tone Wind Blowing Long | Thời tiết | `assets/sfx/t28/amb_wind_mountain_pass.wav` |  |
| 48 | `amb_wind_pines` | nền môi trường | Lake Wind Ambience | Không gian xung quanh | `assets/sfx/t09/amb_wind_pines.wav` |  |
| 49 | `amb_wind_tropical` | nền môi trường | Room Tone Wind Blowing Short | Thời tiết | `assets/sfx/t12/amb_wind_tropical.wav` |  |
| 50 | `amb_winter_wind_hollow` | nền môi trường | Wind through window | Thời tiết | `assets/sfx/t26/amb_winter_wind_hollow.wav` |  |
| 51 | `amb_wooden_cart_stone_road` | nền môi trường | Horse and Carriage | Phương tiện giao thông | `assets/sfx/t26/amb_wooden_cart_stone_road.wav` |  |
| 52 | `fx_911_call_recording_radio` | tiếng động | Voice On Radio Accent | Phương tiện giao thông | `assets/sfx/t17/fx_911_call_recording_radio.wav` |  |
| 53 | `fx_ambulance_siren_close` | tiếng động | Emergency Siren Close Long | Báo động khẩn cấp | `assets/sfx/fx_ambulance_siren_close.wav` |  |
| 54 | `fx_ambulance_siren_distant` | tiếng động | Ambulance Siren Distant | Báo động khẩn cấp | `assets/sfx/fx_ambulance_siren_distant.wav` |  |
| 55 | `fx_baby_crying_night` | tiếng động | Baby Cry Long | Giọng của con người | `assets/sfx/t14/fx_baby_crying_night.wav` |  |
| 56 | `fx_bread_bag_open` | tiếng động | Paper Bag Opening | Tiếng động thực tế | `assets/sfx/t19/fx_bread_bag_open.wav` |  |
| 57 | `fx_breathing_focused_artist` | tiếng động | Human Breathing Nose | Giọng của con người | `assets/sfx/t16/fx_breathing_focused_artist.wav` |  |
| 58 | `fx_breathing_tense_close` | tiếng động | Human Breathing | Giọng của con người | `assets/sfx/fx_breathing_tense_close.wav` |  |
| 59 | `fx_breathing_tired` | tiếng động | Male Sick Breathing | Giọng của con người | `assets/sfx/t23/fx_breathing_tired.wav` |  |
| 60 | `fx_candy_wrapper_open` | tiếng động | Plastic Crumpling | Tiếng động trong nhà | `assets/sfx/t17/fx_candy_wrapper_open.wav` |  |
| 61 | `fx_car_brake_screech` | tiếng động | Muscle Car Highway Skid | Phương tiện giao thông | `assets/sfx/t05/fx_car_brake_screech.wav` |  |
| 62 | `fx_car_door_close` | tiếng động | Car Door Closing | Phương tiện giao thông | `assets/sfx/fx_car_door_close.wav` |  |
| 63 | `fx_car_tire_screech_stop` | tiếng động | Tires Rolling On Gravel No Engine | Phương tiện giao thông | `assets/sfx/fx_car_tire_screech_stop.wav` |  |
| 64 | `fx_car_window_knock` | tiếng động |  |  | `assets/sfx/t07/fx_car_window_knock.wav` |  |
| 65 | `fx_card_swipe` | tiếng động | Credit Card Swipe | Phương tiện giao thông | `assets/sfx/t04/fx_card_swipe.wav` |  |
| 66 | `fx_chisel_hammer_clay` | tiếng động | Hammering into Wood | Công cụ | `assets/sfx/t16/fx_chisel_hammer_clay.wav` |  |
| 67 | `fx_computer_beep_restore` | tiếng động | Beeps bowling computer | Thể thao | `assets/sfx/t15/fx_computer_beep_restore.wav` | thay thế - `Beep Short` (bản gốc chỉ 0,1 s) |
| 68 | `fx_counting_cash` | tiếng động | Coins Shuffling | Tiếng động thực tế | `assets/sfx/t26/fx_counting_cash.wav` |  |
| 69 | `fx_courtroom_dead_silence` | tiếng động | Sheet Flap In Large Hall | Tiếng động trong nhà | `assets/sfx/t22/fx_courtroom_dead_silence.wav` | thay thế - `Ambient Hum Air Conditioner` (tiếng tờ giấy vẫy trong phòng xử án rộng) |
| 70 | `fx_crime_scene_tape_pull` | tiếng động | Cassette Tape Rewind | Tiếng động thực tế | `assets/sfx/t15/fx_crime_scene_tape_pull.wav` |  |
| 71 | `fx_crowd_relief_sigh` | tiếng động | Voices Moaning | Đám đông | `assets/sfx/fx_crowd_relief_sigh.wav` | thay thế - `Breathing Echo space` (tiếng rên rỉ từ hàng ghế khán phòng) |
| 72 | `fx_crying_family_representative` | tiếng động | Male Dramatic Crying | Giọng của con người | `assets/sfx/t28/fx_crying_family_representative.wav` |  |
| 73 | `fx_crying_female_phone` | tiếng động | Male Crying | Giọng của con người | `assets/sfx/t13/fx_crying_female_phone.wav` | ⚠️ **SAI GIỚI TÍNH** — thư viện KHÔNG có tiếng khóc nữ (chỉ có `Male Crying`, `Male Dramatic Crying`, `Babies Cry`, `Baby Cry*`); giữ `Male Crying` vì đúng nhịp khóc nén người lớn hơn tiếng trẻ khóc |
| 74 | `fx_cup_shatter_tea` | tiếng động | Porcelain Bowl Drop Short Series | Tiếng động trong nhà | `assets/sfx/t16/fx_cup_shatter_tea.wav` |  |
| 75 | `fx_defib_charge_shock` | tiếng động | Tweeter Electric Static | Tiếng động thực tế | `assets/sfx/t04/fx_defib_charge_shock.wav` | thay thế - `Power Tool Electrical Buzz` (tiếng điện tĩnh/ran) |
| 76 | `fx_dog_bark_working` | tiếng động | Outdoor Ambience Dog Barking | Không gian xung quanh | `assets/sfx/t18/fx_dog_bark_working.wav` |  |
| 77 | `fx_door_kick_boot` | tiếng động | Dumpster Door Slam | Phương tiện giao thông | `assets/sfx/fx_door_kick_boot.wav` |  |
| 78 | `fx_door_slam_indoor` | tiếng động | Sliding Glass Door Aggressive | Cửa ra vào | `assets/sfx/t19/fx_door_slam_indoor.wav` | thay thế - `Dumpster Door Slam` |
| 79 | `fx_doorbell_chime` | tiếng động | Medium Bell Ringing Near | Chuông báo | `assets/sfx/t10/fx_doorbell_chime.wav` |  |
| 80 | `fx_dtmf_touch_tone_beep` | tiếng động | Phone Alerts And Rings | Chuông báo | `assets/sfx/fx_dtmf_touch_tone_beep.wav` |  |
| 81 | `fx_envelope_tear` | tiếng động | Paper Towel Rip | Tiếng động trong nhà | `assets/sfx/fx_envelope_tear.wav` |  |
| 82 | `fx_evidence_cabinet_open` | tiếng động | Sliding Closet Door Series | Cửa ra vào | `assets/sfx/t18/fx_evidence_cabinet_open.wav` |  |
| 83 | `fx_evidence_measure_tape` | tiếng động | Cassette Tape Play | Tiếng động thực tế | `assets/sfx/fx_evidence_measure_tape.wav` | thay thế - `Cassette Tape Rewind` |
| 84 | `fx_evidence_room_door` | tiếng động | Wood Door Close and Rattle | Cửa ra vào | `assets/sfx/t15/fx_evidence_room_door.wav` |  |
| 85 | `fx_floppy_disk_insert` | tiếng động | Disk Drive Insert and Spinning | Công cụ | `assets/sfx/t05/fx_floppy_disk_insert.wav` |  |
| 86 | `fx_footsteps_barefoot_stairs` | tiếng động | Bare Feet Scuff Wood | Tiếng động thực tế | `assets/sfx/t14/fx_footsteps_barefoot_stairs.wav` |  |
| 87 | `fx_footsteps_chase_forest` | tiếng động | Footsteps on fallen leaves | Giọng của con người | `assets/sfx/t28/fx_footsteps_chase_forest.wav` |  |
| 88 | `fx_footsteps_dusty_wood_slow` | tiếng động | Distant Footsteps On Wood | Tiếng động thực tế | `assets/sfx/t16/fx_footsteps_dusty_wood_slow.wav` |  |
| 89 | `fx_footsteps_gravel_stealth` | tiếng động | Footsteps gravel | Tiếng động thực tế | `assets/sfx/t09/fx_footsteps_gravel_stealth.wav` |  |
| 90 | `fx_footsteps_run_gravel` | tiếng động | Footsteps grit | Tiếng động thực tế | `assets/sfx/fx_footsteps_run_gravel.wav` |  |
| 91 | `fx_footsteps_run_wet_pavement` | tiếng động |  |  | `assets/sfx/fx_footsteps_run_wet_pavement.wav` |  |
| 92 | `fx_footsteps_shoes_scuff` | tiếng động | Shoe Scuffing on Concrete | Tiếng động thực tế | `assets/sfx/t15/fx_footsteps_shoes_scuff.wav` |  |
| 93 | `fx_footsteps_stealth_wood` | tiếng động | Shoe scuff hollow wood | Tiếng động thực tế | `assets/sfx/t23/fx_footsteps_stealth_wood.wav` |  |
| 94 | `fx_footsteps_wood_heavy` | tiếng động | Footsteps solid wood | Tiếng động thực tế | `assets/sfx/t13/fx_footsteps_wood_heavy.wav` |  |
| 95 | `fx_fridge_door_open` | tiếng động | Washing Machine Door | Tiếng động trong nhà | `assets/sfx/t17/fx_fridge_door_open.wav` |  |
| 96 | `fx_glass_smash_vehicle_crash` | tiếng động | Wine Glass Shatter | Va chạm | `assets/sfx/fx_glass_smash_vehicle_crash.wav` |  |
| 97 | `fx_glasses_clink` | tiếng động | Wineglass On Wood Soft | Tiếng động trong nhà | `assets/sfx/fx_glasses_clink.wav` |  |
| 98 | `fx_gravel_car_drive` | tiếng động | Car Drive By | Phương tiện giao thông | `assets/sfx/t10/fx_gravel_car_drive.wav` |  |
| 99 | `fx_gunshots_pistol_inside` | tiếng động | Gunfire And Voices | Vũ khí | `assets/sfx/t13/fx_gunshots_pistol_inside.wav` |  |
| 100 | `fx_gunshots_revolver_5` | tiếng động | Gunfire Long Distance | Vũ khí | `assets/sfx/t14/fx_gunshots_revolver_5.wav` |  |
| 101 | `fx_gunshots_rifle_shotgun` | tiếng động | Vulcan Machine Gun Series | Vũ khí | `assets/sfx/t12/fx_gunshots_rifle_shotgun.wav` |  |
| 102 | `fx_handcuff_snap` | tiếng động | Metal Hand Cuff | Tiếng động thực tế | `assets/sfx/fx_handcuff_snap.wav` |  |
| 103 | `fx_handcuffs_chain_on_metal_table` | tiếng động | Chain On Metal Post | Tiếng động thực tế | `assets/sfx/t19/fx_handcuffs_chain_on_metal_table.wav` |  |
| 104 | `fx_handcuffs_struggle_chain` | tiếng động | Chain Jingle | Va chạm | `assets/sfx/t25/fx_handcuffs_struggle_chain.wav` |  |
| 105 | `fx_hatch_lid_open` | tiếng động | Sliding Glass Door Opening | Cửa ra vào | `assets/sfx/t06/fx_hatch_lid_open.wav` |  |
| 106 | `fx_hospital_door_open` | tiếng động | Wood Door Open and Close Series | Cửa ra vào | `assets/sfx/t04/fx_hospital_door_open.wav` |  |
| 107 | `fx_inkjet_printer_run` | tiếng động | Paper Stacking | Tiếng động thực tế | `assets/sfx/fx_inkjet_printer_run.wav` | thay thế - `Handheld Motor Running` (tiếng giấy nạp/rút liên tục) |
| 108 | `fx_key_in_lock` | tiếng động | Key In Lock | Cửa ra vào | `assets/sfx/fx_key_in_lock.wav` |  |
| 109 | `fx_keyboard_typing_soft` | tiếng động | Typing Keyboard | Tiếng động trong nhà | `assets/sfx/t13/fx_keyboard_typing_soft.wav` |  |
| 110 | `fx_keys_drop_on_table` | tiếng động | Change Drop on Wood | Tiếng động thực tế | `assets/sfx/t20/fx_keys_drop_on_table.wav` |  |
| 111 | `fx_knock_table` | tiếng động | Knock On Door | Cửa ra vào | `assets/sfx/fx_knock_table.wav` |  |
| 112 | `fx_lab_test_kit` | tiếng động | Water Pour Into Surgical Tray | Nước | `assets/sfx/t18/fx_lab_test_kit.wav` | không có tiếng xét nghiệm — dùng tiếng rót chất lỏng vào khay phẫu thuật |
| 113 | `fx_landline_ring_office` | tiếng động | Phone Ringing Untraditional | Tiếng động trong nhà | `assets/sfx/fx_landline_ring_office.wav` |  |
| 114 | `fx_latch_unlock` | tiếng động | Sewing Machine Treadle | Công cụ | `assets/sfx/t10/fx_latch_unlock.wav` |  |
| 115 | `fx_lav_mic_breathing` | tiếng động | Human Breathing | Giọng của con người | `assets/sfx/t20/fx_lav_mic_breathing.wav` |  |
| 116 | `fx_lighter_flick_flame` | tiếng động | Lighter Flick | Tiếng động thực tế | `assets/sfx/t29/fx_lighter_flick_flame.wav` |  |
| 117 | `fx_liquid_pour_splat` | tiếng động | Water Pour Into Half Full Sink | Nước | `assets/sfx/t08/fx_liquid_pour_splat.wav` |  |
| 118 | `fx_lock_turning_dry` | tiếng động | Opening door with Key | Cửa ra vào | `assets/sfx/t29/fx_lock_turning_dry.wav` |  |
| 119 | `fx_mechanical_keyboard` | tiếng động | Keyboard Typing Fast Close | Văn phòng | `assets/sfx/t15/fx_mechanical_keyboard.wav` |  |
| 120 | `fx_metal_barrier_drop` | tiếng động | Metallic drops and echo | Vũ khí | `assets/sfx/t28/fx_metal_barrier_drop.wav` |  |
| 121 | `fx_metal_door_push_open` | tiếng động | Push Bar Door Series | Cửa ra vào | `assets/sfx/t13/fx_metal_door_push_open.wav` |  |
| 122 | `fx_metal_lock_open` | tiếng động | Key In Lock | Cửa ra vào | `assets/sfx/t16/fx_metal_lock_open.wav` | thay thế - `Deadbolt Lock` (bản gốc chỉ 0,1 s) |
| 123 | `fx_mic_hum_feedback` | tiếng động | Ambient Hum Pitched | Phim kinh dị | `assets/sfx/fx_mic_hum_feedback.wav` |  |
| 124 | `fx_modem_dialup_data` | tiếng động | Dial Turning | Tiếng động thực tế | `assets/sfx/t27/fx_modem_dialup_data.wav` |  |
| 125 | `fx_monitor_case_close` | tiếng động | Opening Plastic Storage Container | Tiếng động trong nhà | `assets/sfx/t04/fx_monitor_case_close.wav` | thay thế - `Washing Machine Door` |
| 126 | `fx_motorbike_stop_engine` | tiếng động | Bicycle Pedaling Old Chain | Thể thao | `assets/sfx/t27/fx_motorbike_stop_engine.wav` |  |
| 127 | `fx_mouse_click_rapid` | tiếng động | Click Continuous | Văn phòng | `assets/sfx/fx_mouse_click_rapid.wav` |  |
| 128 | `fx_notebook_open_pages` | tiếng động | Scraping On Paper | Tiếng động thực tế | `assets/sfx/t21/fx_notebook_open_pages.wav` |  |
| 129 | `fx_objects_smash_break` | tiếng động | Glass Drop and Roll | Va chạm | `assets/sfx/t11/fx_objects_smash_break.wav` |  |
| 130 | `fx_oxygen_breathing` | tiếng động | Breathing Running | Giọng của con người | `assets/sfx/t13/fx_oxygen_breathing.wav` |  |
| 131 | `fx_pen_cap_open` | tiếng động | Pen Clicking | Tiếng động thực tế | `assets/sfx/t24/fx_pen_cap_open.wav` | `Pen Clicking` chỉ 0,3 s → đã đệm 0,6 s |
| 132 | `fx_pen_signing_scroll` | tiếng động | drawing on paper with marker | Tiếng động thực tế | `assets/sfx/fx_pen_signing_scroll.wav` |  |
| 133 | `fx_phone_hangup_click` | tiếng động | Phone Ringing | Tiếng động trong nhà | `assets/sfx/t14/fx_phone_hangup_click.wav` |  |
| 134 | `fx_phone_line_hiss_1970` | tiếng động | Phone Alerts And Rings | Chuông báo | `assets/sfx/t03/fx_phone_line_hiss_1970.wav` |  |
| 135 | `fx_phone_ring_landline_night` | tiếng động | Telephone Ring | Tiếng động trong nhà | `assets/sfx/fx_phone_ring_landline_night.wav` |  |
| 136 | `fx_phone_typing_swipe` | tiếng động | Phone Ringing | Tiếng động trong nhà | `assets/sfx/t07/fx_phone_typing_swipe.wav` |  |
| 137 | `fx_phone_unlock_click` | tiếng động | Revolver Cylinder Click Series | Vũ khí | `assets/sfx/t19/fx_phone_unlock_click.wav` | thay thế - `Phone Ringing` |
| 138 | `fx_phone_vibrate` | tiếng động | Cell Phone Vibrate | Giọng của con người | `assets/sfx/fx_phone_vibrate.wav` |  |
| 139 | `fx_police_tape_flutter` | tiếng động | Cassette Tape | Tiếng động thực tế | `assets/sfx/t22/fx_police_tape_flutter.wav` |  |
| 140 | `fx_pour_hot_water_paper_cup` | tiếng động | Pour Boiling Water Into Cup | Tiếng động trong nhà | `assets/sfx/t29/fx_pour_hot_water_paper_cup.wav` |  |
| 141 | `fx_printer_thermal` | tiếng động | Quiet Whirring | Phương tiện giao thông | `assets/sfx/fx_printer_thermal.wav` | thay thế - `Motor Running Muffled` (tiếng máy chạy è è) |
| 142 | `fx_rifle_shell_load` | tiếng động | Handgun Magazine Loading | Vũ khí | `assets/sfx/t09/fx_rifle_shell_load.wav` |  |
| 143 | `fx_roller_shutter_slam` | tiếng động | Cartoon Metal Thunk | Hoạt hình | `assets/sfx/t28/fx_roller_shutter_slam.wav` |  |
| 144 | `fx_sandpaper_scrape_eraser` | tiếng động | Scratching Sandpaper | Hoạt hình | `assets/sfx/t13/fx_sandpaper_scrape_eraser.wav` |  |
| 145 | `fx_saw_blade_packaging` | tiếng động | Small Reciprocating Saw Burst | Công cụ | `assets/sfx/t20/fx_saw_blade_packaging.wav` |  |
| 146 | `fx_school_bell_dismissal` | tiếng động | Xylophone Tip Toe Scale Up | Hoạt hình | `assets/sfx/t16/fx_school_bell_dismissal.wav` |  |
| 147 | `fx_scissors_cut_paper` | tiếng động | Paper Scraps Cut | Tiếng động thực tế | `assets/sfx/t16/fx_scissors_cut_paper.wav` |  |
| 148 | `fx_scream_distant` | tiếng động | Battle Cry - High Pitch | Đám đông | `assets/sfx/t13/fx_scream_distant.wav` |  |
| 149 | `fx_sewing_machine` | tiếng động | Sewing Machine Squeal | Công cụ | `assets/sfx/t14/fx_sewing_machine.wav` |  |
| 150 | `fx_shell_casing_drop` | tiếng động | Shell Casings Handgun | Vũ khí | `assets/sfx/t14/fx_shell_casing_drop.wav` |  |
| 151 | `fx_shovel_dirt` | tiếng động | Shovel Into Dirt | Công cụ | `assets/sfx/t06/fx_shovel_dirt.wav` |  |
| 152 | `fx_shovel_pick_dirt_stone` | tiếng động | Shovel Digging Dirt | Công cụ | `assets/sfx/fx_shovel_pick_dirt_stone.wav` |  |
| 153 | `fx_sigh_emotional` | tiếng động | Battle Agony Moans | Đám đông | `assets/sfx/fx_sigh_emotional.wav` | thay thế - `Quiet Breathing` (thư viện không có tiếng sigh; dùng tiếng rên đau của đám đông) |
| 154 | `fx_sigh_female` | tiếng động | Death Rattle Breath | Giọng của con người | `assets/sfx/t05/fx_sigh_female.wav` | thay thế - `Human Breathing Mouth` (thở nghẹn ngào, đúng tâm lý thở dài nghẹn ngào) |
| 155 | `fx_sledgehammer_impact_concrete` | tiếng động | Sledgehammer Handle Cement | Công cụ | `assets/sfx/t25/fx_sledgehammer_impact_concrete.wav` |  |
| 156 | `fx_sobbing_crowd_row` | tiếng động | Human Group Cry Out | Đám đông | `assets/sfx/fx_sobbing_crowd_row.wav` |  |
| 157 | `fx_spoon_clink` | tiếng động | Spoon on Bowl | Tiếng động trong nhà | `assets/sfx/t04/fx_spoon_clink.wav` |  |
| 158 | `fx_stamp_wood` | tiếng động | Stomach Thumps | Hoạt hình | `assets/sfx/fx_stamp_wood.wav` |  |
| 159 | `fx_stretcher_wheels` | tiếng động | Wheeling A Cart | Tiếng động trong nhà | `assets/sfx/t04/fx_stretcher_wheels.wav` |  |
| 160 | `fx_table_slap_anger` | tiếng động | Knock On Wooden Door | Cửa ra vào | `assets/sfx/t11/fx_table_slap_anger.wav` |  |
| 161 | `fx_tea_pour_cup` | tiếng động | Water Pouring from Jug | Nước | `assets/sfx/t24/fx_tea_pour_cup.wav` |  |
| 162 | `fx_train_door_slam` | tiếng động | Door Opening Closing | Cửa ra vào | `assets/sfx/t08/fx_train_door_slam.wav` |  |
| 163 | `fx_umbrella_puncture_nylon` | tiếng động | Plastic Grovery Bag Movement | Tiếng động thực tế | `assets/sfx/t08/fx_umbrella_puncture_nylon.wav` |  |
| 164 | `fx_vehicle_impact_metal` | tiếng động | Smashing Car Windshield Series | Va chạm | `assets/sfx/t14/fx_vehicle_impact_metal.wav` |  |
| 165 | `fx_video_playback_static` | tiếng động | Radio Static | Tiếng động thực tế | `assets/sfx/fx_video_playback_static.wav` |  |
| 166 | `fx_window_pry_break` | tiếng động | Sliding Glass Door Aggressive | Cửa ra vào | `assets/sfx/fx_window_pry_break.wav` |  |
| 167 | `fx_wooden_hinge_creak_open` | tiếng động | Sliding Closet Door Series | Cửa ra vào | `assets/sfx/t29/fx_wooden_hinge_creak_open.wav` | thay thế - `Wood Door Open and Close Series` |
| 168 | `fx_wooden_lid_slam_latch` | tiếng động | Sliding Glass Door Latching | Cửa ra vào | `assets/sfx/t10/fx_wooden_lid_slam_latch.wav` | thay thế - `Wood Door Close and Rattle` |
| 169 | `fx_zipper_bag` | tiếng động | Zipper | Tiếng động thực tế | `assets/sfx/t07/fx_zipper_bag.wav` |  |

### 4.3. Ứng viên thay thế từ Freesound (CC0) — 24/10/2026, CHỜ NGHE DUYỆT

**Vì sao:** 19 mã ở bảng 4.2 đang dùng **track thay thế** (không đúng nghĩa). Freesound là nguồn thứ 2 — mục 6 của file này đã ghi *"Nguồn: YouTube Audio Library (ưu tiên), **Freesound (CC0)**"*.

**Đã tải:** 57 ứng viên / 19 mã, **100% CC0**, 38 tác giả khác nhau.
Bảng đầy đủ (có link Freesound, thời lượng, mức dBFS, cảnh báo): `.work/freesound_candidates.md` · máy: `.work/freesound_candidates.json` · file tạm: `.work/freesound/<mã>/*.mp3`.

**Giới hạn:** Token auth chỉ lấy được **preview hq mp3 160 kbps stereo**, KHÔNG phải file gốc (endpoint `download/` là OAuth2-required). Nếu cần file gốc → phải làm OAuth2 `authorization_code` (cần đăng nhập trình duyệt).

**Trạng thái:** ⛔ **Chưa file nào được nhập vào `assets/sfx/` hay đưa vào video.** Theo A3 phải nghe kiểm trước. Sổ provenance tạm: `.work/freesound_provenance.json` (57 dòng, trạng thái "CHUA nghe duyet"). Chỉ gộp vào `provenance.json` sau khi người dùng duyệt.

**Rủi ro đã thấy trong tên:** `fx_monitor_case_close` → 3 ứng viên là "Plastic Handle Unlock" / "Switch Flip" (không phải đóng vỏ); `fx_phone_unlock_click` → ứng viên là cửa/hàm (đúng "unlock" nhưng không phải điện thoại); `amb_lawyers_discussion` → cả 3 là cùng một bản ghi "guided tour" của một tác giả. Những mã này **cần từ khóa khác hoặc tự tổng hợp**.

## 5. Nhạc nền (BGM)

### 5.0. Bản tiếng Anh dùng CHUNG bảng SFX này

Có **27 kịch bản tiếng Anh** (`01_KICH_BAN/Tap03_EN/ … Tap29_EN/`) và số cue SFX/BGM **khớp 100%** với bản tiếng Việt ở cả 27 tập (kiểm bằng script `.work/_audit_sfx.py`, mục A).

⇒ **Một bảng SFX, dùng cho cả bản VN lẫn bản EN** — không phải làm hai lần. Các cue trong bản EN là bản dịch 1–1 của cue tiếng Việt, nên file âm thanh và mức dB giữ nguyên.

### 5.1. Thư viện nhạc nền

Thư viện hiện có (`assets/bgm/`, **11 track**): `bgm_ambient_deep` · `bgm_cello_sad` · `bgm_cello_sad_v2` · `bgm_music_box` · `bgm_piano_minimal` · `bgm_piano_minimal_v2` · `bgm_piano_warm` · `bgm_sub_drone` · `bgm_violin_heart` (9 track tự sinh MiniMax) **+ `bgm_guitar_acoustic_60s` · `bgm_church_organ` (2 track tải tay từ YouTube Audio Library — đã gắn vào bed T09/T16 ngày 25/10/2026)**

### 5.2. Cấu trúc 5 hồi theo tập

| Tập | Cấu trúc 5 hồi & file nhạc dùng | Dải nền mới phải tạo |
|---|---|---|
| 03 | H1 gió rít + tiếng dây điện thoại 1970 → `t2/amb_winter_wind` · H2 mưa + cần gạt → `t3/amb_rain_storm` · H3 nước nhỏ giọt hầm → `t3/amb_pipe_drain` · H4 máy ghi âm cassette → `t2/amb_interrogation` + `t3/fx_cassette_motor` · H5 tòa án → `t2/amb_courtroom` + `bgm_cello_sad_v2` | — |
| 04 | H1 máy thở cơ học + monitor → `amb_hospital_ventilator` (MỚI) · H2 piano tối giản + gõ bàn phím đêm → `bgm_piano_minimal_v2` + `keyboard_night` · H3 sub-bass + nhịp tim → `bgm_sub_drone` + `fx_heartbeat_slow` · H4 synth dồn dập → `bgm_ambient_deep` · H5 gavel + piano → `t2/fx_gavel_triple` + `bgm_piano_warm` | `amb_fastfood_cafeteria.wav`, `amb_hospital_ventilator.wav` |
| 05 | H1 máy đánh chữ cơ + gió đông → `typewriter` + `t2/amb_winter_wind` · H2 nhịp tim + cuộn băng từ → `fx_heartbeat_slow` + `t3/fx_cassette_motor` · H3 cello + sub-bass → `bgm_cello_sad` + `bgm_sub_drone` · H4 synth + quạt server → `bgm_ambient_deep` + `amb_server_fan` (MỚI) · H5 gavel → `bgm_piano_warm` | `amb_server_fan.wav` |
| 06 | H1 dương cầm → `bgm_piano_minimal` · H2 dark ambient dồn dập → `bgm_ambient_deep` · H3 sub-drone → `bgm_sub_drone` · H4 vĩ cầm → `bgm_cello_sad` · H5 piano sâu lắng → `bgm_piano_warm` | `amb_crowd_applause_distant.wav` |
| 07 | H1 piano tối giản + synth → `bgm_piano_minimal_v2` · H2 pulse số → `bgm_ambient_deep` · H3 cello u uất → `bgm_cello_sad` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm` | — |
| 08 | H1 dương cầm + heartbeat → `bgm_piano_minimal` + `fx_heartbeat_slow` · H2 dark ambient → `bgm_ambient_deep` · H3 piano u ám → `bgm_piano_minimal_v2` · H4 vĩ cầm → `bgm_cello_sad` · H5 piano ấm → `bgm_piano_warm` | `amb_alarm_siren_distant.wav`, `amb_megaphone_loudspeaker.wav`, `amb_subway_station_jp.wav` |
| 09 | H1 guitar acoustic 60s → `bgm_guitar_acoustic_60s` (đã tải + đã gắn vào bed 25/10/2026) · H2 dark ambient + gió sa mạc → `bgm_ambient_deep` + `amb_wind_pines` (MỚI) · H3 piano tối giản → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_murmur_press.wav`, `amb_desert_wind_dry.wav`, `amb_female_humming_far.wav`, `amb_horse_hooves_distant.wav`, `amb_ocean_waves_soft.wav`, `amb_wind_pines.wav` |
| 10 | H1 cello u buồn → `bgm_cello_sad` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm` | `amb_car_engine_idle.wav`, `amb_highway_speed_car.wav` |
| 11 | H1 cello + gió → `bgm_cello_sad` + `t2/amb_winter_wind` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm` | `amb_party_crowd_outdoor.wav`, `amb_projector_room.wav` |
| 12 | H1 cello + côn trùng nhiệt đới → `bgm_cello_sad` + `t3/amb_crickets_traffic` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm` | `amb_alarm_siren_distant.wav`, `amb_ceiling_fan.wav`, `amb_crowd_arguing_indoor.wav`, `amb_crowd_singing_acoustic.wav`, `amb_helicopter_far.wav`, `amb_loudspeaker_jungle_echo.wav`, `amb_small_plane_engine.wav`, `amb_tractor_engine.wav`, `amb_wind_tropical.wav` |
| 13 | H1 cello + đồng hồ treo tường → `bgm_cello_sad` + `clock_tick` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm` | `amb_bus_distant.wav`, `amb_hospital_monitor_heartbeat.wav`, `amb_library_quiet.wav` |
| 14 | H1 cello + sóng biển → `bgm_cello_sad` + `amb_ocean_waves_soft` (MỚI) · H2 dark ambient + búa tòa → `bgm_ambient_deep` + `gavel` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_murmur_courtroom.wav`, `amb_helicopter_far.wav`, `amb_ocean_waves_soft.wav`, `amb_party_crowd_outdoor.wav` |
| 15 | H1 dark ambient + nước nhỏ giọt → `bgm_ambient_deep` + `t3/amb_pipe_drain` · H2 điện tử dồn dập → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin căng thẳng → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_murmur_courtroom.wav`, `amb_tv_camera_operator.wav` |
| 16 | H1 organ nhà thờ → `bgm_church_organ` (đã tải + đã gắn vào bed 25/10/2026) + `t2/amb_winter_wind` · H2 điện tử + máy bay → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_train_horn_distant_night.wav` |
| 17 | H1 dark ambient + gió → `bgm_ambient_deep` + `t2/amb_winter_wind` · H2 dark ambient + công viên giải trí → `bgm_ambient_deep` + `amb_carnival_ride_music_far` (MỚI) · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_carnival_ride_music_far.wav`, `amb_crowd_murmur_courtroom.wav` |
| 18 | H1 dark ambient + gió biển + chuông gió → `bgm_ambient_deep` + `amb_ocean_waves_soft` (MỚI) · H2 điện tử dồn dập → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_angry_jeers.wav`, `amb_ocean_waves_soft.wav`, `amb_wind_chime.wav` |
| 19 | H1 drone + đồng hồ → `bgm_sub_drone` + `clock_tick` · H2 dark ambient → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_murmur_courtroom.wav`, `amb_panic_crowd_schoolyard.wav` |
| 20 | H1 dark ambient + nhịp tim + đồng hồ → `bgm_ambient_deep` + `fx_heartbeat_slow` + `clock_tick` · H2 minimal ambient → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_camera_crew_press.wav`, `amb_ceiling_fan.wav`, `amb_crowd_angry_whisper.wav`, `amb_crowd_murmur_press.wav` |
| 21 | H1 cello + nhịp tim + mưa → `bgm_cello_sad` + `fx_heartbeat_slow` + `t3/amb_rain_storm` · H2 ambient trầm đục → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_car_start_leave_garage.wav`, `amb_crowd_murmur_press.wav`, `amb_hospital_monitor_heartbeat.wav`, `amb_lawyers_discussion.wav` |
| 22 | H1 dark ambient + còi xe → `bgm_ambient_deep` + `police_siren_distant` · H2 electronic pulse → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_car_engine_idle.wav`, `amb_crowd_murmur_courtroom.wav`, `amb_crowd_murmur_press.wav`, `amb_tv_camera_operator.wav` |
| 23 | H1 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H2 heavy bass → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_cheer_outdoor.wav`, `amb_crowd_excited_girls.wav`, `amb_hospital_monitor_heartbeat.wav` |
| 24 | H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 minimal ambient + bước chân hành lang → `bgm_sub_drone` + `footsteps` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_applause_court.wav`, `amb_lab_equipment.wav` |
| 25 | H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass + hú báo động → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_alarm_siren_distant.wav`, `amb_crowd_angry_jeers.wav` |
| 26 | H1 cello + gió + tuyết → `bgm_cello_sad` + `t2/amb_winter_wind` · H2 deep ambient → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_car_engine_idle.wav`, `amb_crowd_murmur_courtroom.wav`, `amb_crowd_outside_press_anger.wav`, `amb_winter_wind_hollow.wav`, `amb_wooden_cart_stone_road.wav` |
| 27 | H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_crowd_mourning_outdoor.wav` |
| 28 | H1 cello + sấm + bão → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass + động cơ xe → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_car_engine_idle.wav`, `amb_crowd_murmur_courtroom.wav`, `amb_crowd_murmur_hall_1000.wav`, `amb_crowd_murmur_press.wav`, `amb_thunder_distant.wav`, `amb_wind_mountain_pass.wav` |
| 29 | H1 cello + bass + mưa + còi tuần tra → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 cello + gõ nhịp kim loại + quạt → `bgm_cello_sad_v2` + `amb_ceiling_fan` (MỚI) · H3 piano tối giản → `bgm_piano_minimal` · H4 violin + búa tòa → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm` | `amb_ceiling_fan.wav`, `amb_tv_static_eerie.wav` |

> **Chuẩn BGM 5 hồi** áp dụng cho Tập 15–29 (nhóm kịch bản viết cùng đợt): Hồi 1 Dark Ambient/cello u buồn → Hồi 2 Dark Ambient điện tử dồn dập → Hồi 3 Minimalist Piano triết học → Hồi 4 Violin căng thẳng → Hồi 5 Warm Piano suy tư.
> Tập 03–14 có nhịp riêng, xem cột “Nhạc nền / dải nền theo hồi” ở mục 3.

**Cần tải thêm 2 track BGM (chưa có trong thư viện):**

| Tập | Track cần | Ghi chú |
|---|---|---|
| 09 | Guitar acoustic mộc mạc thập niên 60, biến dạng dần sang u tối | ✅ **ĐÃ TẢI** — `Jewelry Box` (Tim Bluhm, đồng quê) → `assets/bgm/bgm_guitar_acoustic_60s.mp3` · xử lý thêm để u tối |
| 16 | Organ nhà thờ trầm buồn, u tối | ✅ **ĐÃ TẢI** — `Sinister Cathedral` (Asher Fulero, ambient) → `assets/bgm/bgm_church_organ.mp3` |

---

## 6. Quy trình tạo & đưa vào bảng âm thanh

1. **Tải/tổng hợp file mới** theo bảng mục 4. Nguồn: YouTube Audio Library (ưu tiên — đã dùng cho Tập 03), Freesound (CC0), hoặc tổng hợp bằng `.work/make_sfx3.py` (bản `_code/` là bản dự phòng tự tổng hợp).
2. **Đặt file** vào `assets/sfx/` (dùng chung) hoặc `assets/sfx/tXX/` (riêng tập) — đúng cột “Đặt tại” ở mục 4.
3. **Ghi `.work/sfx_tapXX.json`** theo đúng format `sfx_tap03.json`:
   - `ambience`: `[mã câu đầu, mã câu cuối, file, dB]` — **hai mốc đều là mã câu** (`2.06#1`), không phải mã element.
   - `cues`: `[mốc, 'start'|'end', lệch (s), file, dB]` — mốc được **mã câu HOẶC mã element SFX/BGM/NGHI**.
   - `music_drop.ranges`: `[mã câu, mã câu]` — tắt nhạc có giai điệu ở các câu hé lộ.
   - ⚠️ `ambience` / `music_drop` phải dùng **mã câu**; nếu trỏ mã element thì cue bị **bỏ qua im lặng, không báo lỗi**.
4. **Ghi `provenance.json`** cho từng file mới (nguồn tải, giấy phép, ngày tải) — file không có dòng sổ là mất lớp bảo vệ đầu tiên khi bị Content ID nhận nhầm.
5. **Dựng thử** `AE_EP=XX py -3 .work/build_audio3.py` rồi nghe lại trên bản trộn để chỉnh dB (mức dB trong bảng chỉ là điểm khởi đầu, tính theo RMS lời).

---

## 7. Nhật ký review — những gì đã sửa sau lần soát đầu tiên

Bản đầu tiên chỉ rút cue `[SFX]`. Khi soát lại toàn bộ kịch bản, đã phát hiện và sửa 5 lỗi sau:

| # | Lỗi | Mức độ | Cách sửa |
|---|---|---|---|
| 1 | **Bỏ sót dải nền trong cue `[BGM]` và `[Nghỉ]`** — 82 cue có âm thanh môi trường cụ thể (gió, mưa, đồng hồ, tiếng tim, sóng biển…) nhưng bảng per-episode chỉ liệt kê cue `[SFX]` | Nghiêm trọng | Thêm bảng **“Dải nền / âm thanh môi trường”** riêng cho từng tập, gồm cả dải nền còn thiếu như `clock_tick`, `t2/amb_winter_wind`, `fx_heartbeat_slow`, `t3/amb_rain_storm` |
| 2 | **Gán nhầm âm thanh: mỏ quay (rotary dial) cho cú bấm touch-tone** — Tập 13 (`2.09` “Bấm số 911”) và Tập 17 (`1.03` “Bấm phím khẩn cấp tút tút”) đều trỏ `t3/fx_twisting_dial.wav`. Kịch bản EN ghi rõ *“Frantic touch-tone dialing”* / *“distinct electronic tones of emergency dialing”* | Trung bình | Tạo mới `fx_dtmf_touch_tone_beep.wav` cho cả 2 tập, bỏ mỏ quay |
| 3 | **Gió sa mạc bị gộp nhầm với gió rặng thông** — Tập 9 Hồi 2 là Mojave Desert (Spahn Ranch), khác Hồi 1 là gió rặng thông | Thấp | Tách thành 2 file: `amb_wind_pines.wav` (Hồi 1) + `amb_desert_wind_dry.wav` (Hồi 2) |
| 4 | **Thiếu 2 âm thanh nền có trong cue BGM** — chuông gió lạnh lẽo (Tập 18) và sấm rền từ xa (Tập 28) | Thấp | Thêm `amb_wind_chime.wav` + `amb_thunder_distant.wav` |
| 5 | **Cột “Nền dùng chung” của bảng BGM in sai** (luôn ra `assets/sfx/`) | Vặt | Sửa lại thành cột “Dải nền mới phải tạo” |

Ngoài ra đã **thêm mục 5.0**: 27 kịch bản tiếng Anh có số cue khớp 100% ⇒ một bảng SFX dùng chung cho cả hai bản.

---

## 8. Bẫy đã gặp (rút từ Tập 02–03)

| Bẫy | Hậu quả | Cách tránh |
|---|---|---|
| Trỏ `ambience` bằng mã element thay vì mã câu | Cue **bị bỏ qua im lặng**, không báo lỗi, tập thiếu nền mà QC vẫn xanh | Luôn kiểm tra mã đầu/cuối là mã câu dạng `X.YY#Z` |
| Dùng `ambience`/`music_drop` trỏ element SFX/BGM cũ | Bỏ qua im lặng, không báo lỗi | Đối chiếu mã câu theo **nội dung câu**, không đánh số tay |
| Xoá mp3 cũ rồi đọc lại khi hết số dư gói | API trả **402 “plan balance has run out”** → mất file, không retry được | Luôn lưu `node_id` của từng file TTS (`res_*.json`) để khôi phục |
| Ghép mp4 cũ với audio mới | Lệch **1,77 s**, mọi cổng QC vẫn xanh vì mỗi file “hợp lệ” riêng lẻ | So `duration` mp4 với `.work/audio_master_tXX.wav` trước khi giao (lệch > 0,05 s = dựng lại) |
| Tài sản tạo ngoài `gen_images.py` không có dòng sổ | Mất lớp bảo vệ bản quyền | Backfill bằng `.work/_prov_backfill.py` |
| **Ngưỡng cắt lặng cố định −45 dB khi import SFX** | Nguồn nhỏ (hơi thở, tiếng máy vặn, tiếng ngân xa, tiếng sột soạt) bị xoá sạch ⇒ file ra **0 giây**, import im lặng bỏ qua | Tính ngưỡng **tương đối**: đỉnh của chính đoạn cắt − 18 dB (`thr_for()` trong `import_sfx_series.py`); nguồn < 2 s thì **không cắt lặng**; file < 0,5 s thì `apad=whole_dur=0.6` |
| **Dùng chung 1 track cho 2 mã** | 2 file `.wav` **trùng MD5** ⇒ nghe ra y hệt nhau ở 2 cảnh khác nhau | Rà **MD5** (`.work/_check_dup.py`) **và** track nguồn (`.work/_check_src_dup.py`) — 1 mã 1 track |
| Collector bỏ qua mã đã `used` khi tải lại | File tải về nằm lại trong `Downloads`, dính `REJECT` vì không còn dòng manifest chờ | `py -3 .work\_map_fix.py --unuse <ma>` **trước** khi bấm tải lại |
| Chrome tự thêm hậu tố khi trùng tên (`Voices Angry 1.mp3`) | Collector khớp tên không được ⇒ file bị bỏ lại | Regex bỏ hậu tố đã vá: `re.sub(r"\s*(?:\(\d+\)\|\d+)$", "", stem)` |
| **Tìm trong Thư viện âm thanh là so khớp CHUỖI CON trong TÊN track, không phải từ khóa** | "sing" khớp `Tossing`/`Clo**sing**`, "hum" khớp `Hu**m**an`, "ink" khớp `S**ink**`; từ khóa `print`/`sigh`/`book`/`woman`/`office`/`science`/`gasp` ⇒ **0 kết quả** dù ý nghĩa có thể tồn tại | Tìm bằng **gốc từ độc trùng**: `moan`→`Battle Agony Moans`/`Voices Moaning`, `paper`→`Flipping Newspaper Pages`/`Paper Stacking`, `hall`→`Sheet Flap In Large Hall`, `quiet`→`Quiet Whirring`, `electric`→`Tweeter Electric Static`, `food`→`Ladle Food into Carton` |
| **Nút "Tải xuống" của hàng ngoài viewport chưa được render** | Click bằng selector báo lỗi *Element not found* dù track có thật | `hover` vào hàng trước, rồi click `ytmus-library-row:has([aria-label*="TÊN TRACK"]) button[aria-label="Tải xuống"]` — dùng **tên track** thay vì số thứ tự hàng |
| **Bấm Enter trong ô "Giá trị" của bộ lọc ⇒ panel đóng, ô mới đổi `data-backend-node-id`** | Gõ từ khóa thứ hai vào ref cũ ⇒ thao tác rác / im lặng | Click lại chip để mở panel, `query kind=editable` lấy ref mới **mỗi lần**; 2 tab (Âm nhạc / Hiệu ứng âm thanh) có chip filter riêng |
| **Đổi nguồn cho mã đã có** | Collector đưa file mới vào `_conflict/<mã>_<tên>.mp3`, file cũ vẫn chiếm `<mã>.mp3` ⇒ import vẫn dùng nguồn cũ | `py -3 .work\_map_fix.py --unuse <mã>` **trước khi tải** → collector → `py -3 .work\_swap_named.py <mã>` (file mới vào đúng tên mã, file cũ → `_conflict/<mã>_old.mp3`) → `py -3 .work\import_sfx_series.py <mã>` |
| **Hoán đổi nguồn giữa 2 mã** (đổi chỗ file mp3 trong inbox) | Sửa mã trong manifest là không đủ — file mp3 trong `02_SAN_XUAT/sfx_youtube/` vẫn là nguồn cũ | `py -3 .work\_swap_pair.py <mãA> <mãB>` (đổi chỗ 2 file mp3) **rồi mới** import 2 mã đó |
| **Thư viện không có track đúng nghĩa cho một số cue** (khóc nữ, máy in, hát tập thể, monitor tim, xét nghiệm, quán ăn, phòng thiết) | Chọn đại trà tiếng gần giống → sai tâm trạng cảnh (vd bãi biển trong quán ăn nhanh) | Ghi rõ lý do vào cột **Ghi chú** mục 4.2, giữ luật "1 mã = 1 track"; rà lại bằng `_check_dup.py` + `_check_src_dup.py` sau khi đổi |

---

## 9. Phụ lục — câu lệnh kiểm tra nhanh

```powershell
# Trích xuất lại toàn bộ cue SFX từ kịch bản (đã chạy, cập nhật 23/10/2026)
py -3 .work/_extract_sfx_cues.py

# SOÁT LẠI: parity kịch bản VN vs EN + rà dải nền trong cue BGM/[Nghỉ]
py -3 .work/_audit_sfx.py

# In bảng cue của một tập bất kỳ (ví dụ Tập 17)
py -3 .work/_dump_sfx_cues.py 17 17

# Chạy lại phân tích + xuất bảng thống kê + sinh lại tài liệu
py -3 .work/_sfx_analysis.py
py -3 .work/_gen_sfx_doc.py
```

**Nguồn:** 27 file kịch bản trong `01_KICH_BAN/Tap03/ … Tap29/` · thư viện hiện có: `assets/sfx/` (36 file gốc) + `t2/` + `t3/` · `assets/bgm/` (**11** track: 9 cũ + `bgm_guitar_acoustic_60s` + `bgm_church_organ`).

**Đã tạo 24/10/2026:** 169/169 file SFX mới từ YouTube Studio → Thư viện âm thanh (mục 4.2) · 169/169 file trong `assets/sfx/` đúng cột “Đặt tại” · QC 179/179 đạt (định dạng, thời lượng ≥ 0,5 s, đỉnh ≤ −0,5 dBFS) · không còn 2 file trùng MD5 nào ngoài cặp `fx_lav_mic_breathing` ↔ `fx_breathing_tense_close` (dùng chung có chủ ý) · sổ nguồn: `provenance.json` (2 102 mục).

**Đổi nguồn lần 2 (24/10/2026, sau khi quét thêm từ khóa trong thư viện):** 12 mã chuyển sang track đúng nghĩa hơn — `fx_sigh_female` → `Death Rattle Breath`, `fx_sigh_emotional` → `Battle Agony Moans`, `fx_crowd_relief_sigh` → `Voices Moaning`, `fx_printer_thermal` → `Quiet Whirring`, `fx_inkjet_printer_run` → `Paper Stacking`, `amb_library_quiet` → `Flipping Newspaper Pages`, `fx_courtroom_dead_silence` → `Sheet Flap In Large Hall`, `fx_defib_charge_shock` → `Tweeter Electric Static`, `amb_camera_crew_press` → `Transporting A Camera`, `amb_fastfood_cafeteria` → `Ladle Food into Carton`, `amb_lawyers_discussion` → `Voices Murmur`, `amb_crowd_outside_press_anger` → `Voices Angry` (hai mã cuối **hoán đổi nguồn**). Thư viện **không có** track cho: khóc nữ, máy in/giấy in, hát tập thể, monitor tim, xét nghiệm, quán ăn, phòng thiết tuyệt đối — xem cột *Ghi chú* mục 4.2.
