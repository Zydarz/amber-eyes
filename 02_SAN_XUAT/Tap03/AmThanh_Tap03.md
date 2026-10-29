# ÂM THANH TẬP 03 — VỤ EDMUND KEMPER (23/10/2026)

**Vì sao có file này:** Tập 02 đã chuyển sang tiếng **tải thật từ YouTube Audio Library** (đảo ngược quyết định "không dùng tiếng ngoài" ngày 22/10). Tập 03 tiếp tục hướng đó: **10 tiếng mới tải tay**, cộng 12 tiếng dùng lại từ Tập 02. File này ghi nguồn, điều khoản, điểm cắt và bảng đặt âm.

---

## 1. Nguồn & điều khoản

| | |
|---|---|
| Nguồn | **YouTube Audio Library** — YouTube Studio → Thư viện âm thanh → tab **Hiệu ứng âm thanh** (kênh *Amber Eyes*, `UCloOzyxGK3TGtp6ICJpGRBA`) |
| Cách lấy | Tải tay từng track → thu gom vào `02_SAN_XUAT/Tap03/sfx_youtube/` → `.work/import_sfx_tap03.py` rãnh thành wav |
| Định dạng đầu ra | **wav stereo 44 100 Hz 16-bit**, chuẩn hoá đỉnh **−1 dBFS** |
| **Điều khoản** | Miễn phí dùng trong video/nội dung **do chính kênh sáng tạo**. **KHÔNG** được cung cấp, phân phối hay phát hành riêng file âm thanh (không bán, không cho tải pack SFX). An toàn cho video kiếm tiền. |
| Sổ nguồn gốc | `provenance.json` — mỗi file có `track_youtube`, `the_loai_youtube`, `nguon_goc`, `cat_goc`, `dieu_khoan` |

> Bản gốc mp3 giữ lại ở `02_SAN_XUAT/Tap03/sfx_youtube/` để cắt lại bất cứ lúc nào (không cần tải lại).

---

## 2. 10 tiếng mới — bảng chi tiết

| Mã | Track trên YouTube | Thể loại | Nguồn (s) | Cắt | Ra (s) | mean dB |
|---|---|---|---:|---|---:|---:|
| `amb_rain_storm` | Summer Thunder and Rain | — | 572,6 | 0 + 180 | 180,0 | −32,3 |
| `amb_pipe_drain` | Water Drains In Pipe with Pump | — | 162,3 | 0 + 120 | 120,0 | −26,7 |
| `amb_crickets_traffic` | Crickets with Distant Traffic | Không gian xung quanh | 66,7 | 0 + 66 | 66,0 | −17,7 |
| `fx_cassette_motor` | Cassette Tape Motor | Tiếng động thực tế | 42,9 | 0 + 20 | 20,0 | −14,0 |
| `fx_cassette_button` | Cassette Tape Button | Tiếng động thực tế | 23,9 | **4,2 + 3,8** | 3,8 | −38,5 |
| `fx_coin_shuffle` | Coins Shuffling | — | 23,0 | **3,6 + 4,0** | 4,0 | −33,6 |
| `fx_twisting_dial` | Twisting Dial Clicks | — | 12,1 | 0,15 + 5,2 | 5,2 | −33,0 |
| `fx_phone_ring` | Telephone Ring | — | 50,8 | 0,15 + 4,5 | 4,5 | −17,0 |
| `fx_paper_crunch` | Paper Crunching | Tiếng động thực tế | 18,9 | 0,15 + 5,0 | 5,0 | −32,3 |
| `fx_paper_fold` | Paper Folding | Tiếng động thực tế | 7,9 | 0,2 + 6,0 | 6,0 | −34,9 |

### Vì sao phải cắt

File tải về là **cả bài 8–10 phút**. Đặt nguyên sẽ kéo tiếng qua nhiều câu và lộ rõ chỗ lặp. Điểm cắt **không chọn bằng tai** — đo bằng envelope `max_volume` mỗi 0,25 s (`.work/tap03_review/_fine_t3.py`), rồi cắt quanh đỉnh:

| File | Vì sao cắt chỗ đó |
|---|---|
| `fx_cassette_button` | Nguồn có **4,5 s im lặng** ở đầu; cú bấm nút rõ nằm ở 4,5 s (nguồn) → sau cắt rơi đúng vào **0,25 s** đầu file, tức đủ để ghép thẳng vào mốc `1.08` / `5.11` |
| `fx_coin_shuffle` | Đồng xu leng keng vang nhất ở 4,0 s → cắt bắt đầu 3,6 s để **tiếng leng keng rơi vào đầu file** |
| `fx_twisting_dial` | 5 cú quay số rõ ở 0,25 / 0,50 / 1,75 / 2,50 / 3,75 s; đoạn 7–8 s trống → cắt trước chỗ trống |
| `fx_phone_ring` | Chuông kêu 0,25–2,0 s rồi tắt dần → cắt 4,5 s giữ trọn chuông + vang |
| `fx_paper_crunch` / `fx_paper_fold` | Tiếng giấy dồn ngay 0,15–2,0 s → cắt từ đầu |
| `amb_rain_storm` | 0–4 s có **sấm** rõ (−3 dB), sau đó mới là mưa đều → giữ nguyên 0–180 s vì sấm làm nền xe đêm mưa thêm sức |
| `amb_crickets_traffic` | 1,06 phút nguyên bản — đủ làm nền một đoạn, không cắt |

### Dùng lại từ Tập 02 (không tải lại)

| File | Track YouTube | Dùng cho Tập 03 |
|---|---|---|
| `t2/amb_winter_wind` | Wind In Pine Trees | nền gió đêm Hồi 1 |
| `t2/amb_road_night` | Distant Highway | nền đường đêm |
| `t2/amb_interrogation` | Room Tone Wind Blowing Long | room tone phòng thẩm vấn 1978 (Hồi 4) |
| `t2/amb_courtroom` | *(tổng hợp bằng code)* | nền phòng tòa án (Hồi 5) |
| `t2/fx_door_metal_slam` | Dumpster Door Slam | cửa sắt trại giam `1.12` |
| `t2/fx_gavel_triple` | Wooden Bead Hitting Series | búa tòa `5.01` |
| `t2/fx_phone_ring` | Telephone Ring | (t3 đã có bản tốt hơn — dùng bản t3) |
| `t2/fx_paper_folder` | *(tổng hợp bằng code)* | (t3 đã có bản tốt hơn — dùng bản t3) |
| `t2/fx_stinger` · `t2/fx_sub_drop` · `t2/fx_chair_scrape` · `t2/fx_tire_snow` | — | nhấn kịch tính, ghế kéo, xe chạy tới |

Các file trong `assets/sfx/` (không có tiền tố thư mục) là bộ tổng hợp bằng code của Tập 01: `footsteps.wav` (bước chân hành lang nhà tù), `door_creak.wav` (cửa sắt kéo lê).

---

## 3. Bảng đặt âm — `.work/sfx_tap03.json`

Cùng format với `.work/sfx_tap02.json`: `ambience` (nền chạy liên tục) · `cues` (tiếng động gắn mốc) · `music_drop` (tắt nhạc ở câu hé lộ).

### 3.1 Nền môi trường (10 đoạn)

| Từ câu | Đến câu | File | dB so với RMS lời | Cảnh |
|---|---|---|---:|---|
| `1.01` | `1.10` | `t2/amb_winter_wind.wav` | −30 | đêm ở Pueblo, gió qua khe cửa sắt |
| `2.01` | `2.06` | `t3/amb_rain_storm.wav` | −25 | mưa trên mui xe, cần gạt nước |
| `2.06#2` | `2.08#3` | `t3/amb_crickets_traffic.wav` | −27 | vườn sau nhà & rừng ban đêm |
| `2.09` | `2.09` | `t2/amb_office_night.wav` | −33 | quán rượu The Jury Room |
| `3.01` | `3.11` | `t3/amb_pipe_drain.wav` | −28 | căn hầm ẩm ướt — nước nhỏ giọt |
| `4.01` | `4.08` | `t2/amb_interrogation.wav` | −31 | phòng thẩm vấn Vacaville 1978 |
| `4.01` | `4.08` | `t3/fx_cassette_motor.wav` | −33 | **rè băng từ quay chậm** (đúng như cue `4.01`) |
| `5.01` | `5.03` | `t2/amb_courtroom.wav` | −27 | phiên tòa |
| `5.04` | `5.09` | `t2/amb_office_night.wav` | −33 | phần chuyên gia phân tích |
| `5.10` | `5.12` | `t2/amb_courtroom.wav` | −30 | lời kết |

### 3.2 Tiếng động (20 mốc)

| Mốc | Lệch (s) | File | dB | Hành động |
|---|---:|---|---:|---|
| `1.02` | −0,6 | `t3/fx_coin_shuffle.wav` | −12 | đồng xu leng keng trong khe bốt |
| `1.02` | +0,5 | `t3/fx_twisting_dial.wav` | −14 | quay số xoay tròn |
| `1.03#3` | −0,2 | `t3/fx_phone_ring.wav` | −16 | chuông trực ban Santa Cruz reo |
| `1.05#3` | 0 | `t2/fx_stinger.wav` | −16 | mở lời khai trong *Inside Detective* |
| `1.10#10` | 0 | `t2/fx_sub_drop.wav` | −12 | "Ngăn tôi lại" |
| `1.11` | 0 | `footsteps.wav` | −20 | bước chân hành lang nhà tù (cue trong `NGHI`) |
| `1.12` | −0,6 | `door_creak.wav` | −12 | cánh cửa sắt kéo lê |
| `1.12` | +0,2 | `t2/fx_door_metal_slam.wav` | −4 | đóng sập "Rầm" |
| `2.03` | 0 | `t3/fx_paper_fold.wav` | −12 | lật ảnh hồ sơ |
| `2.03` | +0,3 | `t3/fx_paper_crunch.wav` | −14 | giấy nhăn trên bàn |
| `2.04#3` | −0,4 | `t2/fx_tire_snow.wav` | −18 | xe lăn tới đón |
| `3.05` | 0 | `t2/fx_sub_drop.wav` | −14 | bước sang tầng 1 — cơ chế "thiến hoạn" |
| `4.01` | 0 | `t3/fx_cassette_button.wav` | −8 | máy ghi âm cassette "Cạch" |
| `4.05#3` | +0,1 | `t2/fx_chair_scrape.wav` | −12 | hắn kéo ghế ngồi xuống |
| `4.06` | 0 | `t3/fx_paper_crunch.wav` | −12 | lật trang ghi chép lách cách |
| `5.01` | −2,0 | `t2/fx_gavel_triple.wav` | 0 | búa tòa "Cốp… Cốp… Cốp" |
| `5.02#7` | 0 | `t2/fx_stinger.wav` | −14 | yêu cầu tuyên án tử hình bằng tra tấn |
| `5.08#3` | 0 | `t2/fx_sub_drop.wav` | −14 | lá thư của viên cảnh sát Bruce Colomy |
| `5.11` | 0 | `t3/fx_paper_fold.wav` | −10 | đóng tập hồ sơ "Bụp" |
| `5.11` | +0,7 | `t3/fx_cassette_button.wav` | −8 | bấm nút tắt máy ghi âm "Cạch" |

### 3.3 Tắt nhạc ở câu hé lộ (6 đoạn)

`1.05#3`–`1.05#7` · `1.10#10`–`1.10#11` · `1.11` · `4.05#1`–`4.05#3` · `5.02#6`–`5.02#7` · `5.11`

> Mức dB ở trên là **điểm khởi đầu**, phải nghe lại trên bản trộn thật. Đặc biệt `fx_cassette_motor` có mean −14 dB (nghe to hơn hẳn phần còn lại của bộ) nên đặt ở −33 dB trong bảng — nếu nghe chói thì hạ thêm.

**Đã kiểm bằng script** (`.work/tap03_review/_check_sfx_sheet.py`) — theo **đúng quy tắc** của `build_audio3.py::place_sheet()`:
- `ambience` và `music_drop` bắt buộc dùng **mã câu** (`2.06#2`), không dùng mã element (mã element sẽ bị bỏ qua **im lặng** — không báo lỗi).
- `cues` chấp nhận cả hai: mã câu **hoặc** mã element SFX/BGM/NGHI.
- 22 file được tham chiếu đều tồn tại · mọi mốc đều resolve · cả 10 file `t3/` đều được dùng. **0 lỗi.**

---

### 3.4 Diễn xuất TTS — `.work/acting_tap03.json`

Sinh bởi `.work/make_acting_tap03.py` (bản riêng cho Tập 03, không sửa bản Tập 02):

| | Tập 02 | Tập 03 |
|---|---:|---:|
| Số câu | 215 | 215 |
| Mốc then chốt được soạn tay | ~60 | **162** |
| Cảm xúc (neutral / sad / fearful / surprised) | 160 / 28 / 14 / 13 | 139 / **49** / 19 / 8 |
| Khoảng lặng thêm giữa câu | 70 chỗ · 27,2 s | 60 chỗ · **29,3 s** |
| Lời đọc riêng (chỉ thêm ngắt nghỉ) | có | 6 câu |

**Bộ tham số an toàn (giữ nguyên từ Tập 02):** cao độ **luôn = 0**; cảm xúc chỉ trong
`neutral · sad · fearful · surprised` — bộ giọng đã thử ở Tập 02 chỉ được kiểm ở cao độ 0.
Lệch tốc độ kẹp trong `[-0,06 · +0,02]`, phân bố 5 bậc (Tập 03 có **độ tương phản tốt hơn**
Tập 02: không bậc nào chiếm quá 32 %, Tập 02 dồn 51 % vào một bậc).

**Quy tắc bất biến:** lời đọc riêng chỉ được **thêm ngắt nghỉ**, tuyệt đối **không đổi chữ** —
phụ đề và chữ trên hình giữ nguyên kịch bản. Đã kiểm tự động: bỏ hết thẻ `<#..#>` rồi so
với câu gốc, **215/215 câu giống hệt**, không còn dấu nháy kép trong lời đọc.

## 4. Giới hạn thật — đọc trước khi dựng

- **Không có tiếng cần gạt nước.** Đã tìm `wiper` và `windshield` trong Thư viện âm thanh → **0 kết quả**. Cue `2.01` ("tiếng cần gạt nước kính chắn gió kêu kẽo kẹt đều đặn") dùng `t3/amb_rain_storm` làm nền, **bỏ nhánh cần gạt**. Nếu bắt buộc phải có thì phải tự tổng hợp bằng code.
- **Không có track tòa án mới** → dùng lại `t2/amb_courtroom.wav` (bản tổng hợp bằng code của Tập 02, chưa phải tiếng thật).
- **Tiếng động có sẵn tiếng nền riêng** (mưa, gió, đường xa) → khi dựng phải **hạ tiếng nền của file dưới lời** hoặc chấp nhận chúng thành một phần của nền.
- **Chưa nghe thử.** Toàn bộ mức dB và điểm cắt mới **đo bằng số**, không nghe bằng tai ⇒ bắt buộc nghe lại trước khi chốt bản trộn.
- **Chưa có bản demo** (Tập 02 có `02_SAN_XUAT/Tap02/thu_am/demo_sfx_tap02.mp3`). Nên làm một bản demo tương tự: 3 cảnh — đêm ở bốt điện thoại · vườn sau nhà đêm mưa · phòng thẩm vấn 1978.

---

## 5. Việc còn lại để dựng được âm thanh Tập 03

| # | Việc | Trạng thái |
|---|---|---|
| 1 | `.work/edition.py` → khai báo `EPISODES["03"]` | ✅ **Đã làm 23/10** — thêm khối `"03"` (đặt trước `"04"`), `AE_EP=03` chạy được. Ba mốc đã sửa theo docstring của builder: `act1_cue` = `1.14` (mốc nhạc), `silence_cue` = `1.11` (NGHI), `click_cues` = `("1.08",)` (SFX băng ghi âm) |
| 2 | `.work/edition.py` → `N_ELEMENT` cho Tap03 | ✅ **Đã làm 23/10** — `{"1.09": "N1", "2.09": "N2"}`; nhãn `N1` = "TRỰC BAN CẢNH SÁT SANTA CRUZ", `N2` = **"CẢNH SÁT QUÁN RƯỢU"** (đã đổi, không còn "KHÁNH GIẢ") |
| 3 | Chạy `build_audio3.py` cho tập 3 | **Chưa** — khối `EPISODES["03"]` + `acting_tap03.json` + bảng âm thanh đã xong; còn cần bảng shot để dựng hình |
| 4 | Diễn xuất từng câu cho TTS | ✅ **Đã làm 23/10** — `.work/make_acting_tap03.py` → `.work/acting_tap03.json`: 215 câu, 162 mốc then chốt, 60 khoảng lặng thêm (29,3 s — cùng mức Tập 02: 27,2 s), bộ tham số an toàn (cảm xúc neutral·sad·fearful·surprised, cao độ luôn 0) |
| 5 | Bảng shot + `.work/shots.json` cho tập 3 | **Chưa** — `parse_shots.py` hiện còn trỏ Tập 01; `KeHoach_Video_Tap03.md` chưa có |
| 6 | Dải âm (ducking) khi lời đọc lên | Theo bản Tập 02 |
| 7 | Bản demo SFX (không lời) | **Chưa** |
