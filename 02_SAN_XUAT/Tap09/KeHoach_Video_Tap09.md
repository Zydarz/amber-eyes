# HỒ SƠ SẢN XUẤT TẬP 09 · "NGHỆ THUẬT XÓA BỎ BẢN NGÃ"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 09: Nghệ Thuật Xóa BỎ Bản Ngã** |
| Vụ án | Hồ sơ Charles Manson & Thảm kịch Gia đình Manson (Los Angeles, California, Hoa Kỳ, 1969) |
| Chủ đề | Cơ chế tẩy não 3 giai đoạn (Unfreezing – Changing – Refreezing), Bộ ba Đen tối (Dark Triad) & Thao túng tâm lý bầy đàn |
| Tổng thời lượng | **1523.17 s (~25 phút 23 giây)** · 5 hồi · **199 câu thoại** · **196 shot** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Cư dân Los Angeles) · N2 (Linda Kasabian) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap09.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp4` & `02_SAN_XUAT/Tap09/xuat_ban/Tap09.mp4` |

---

## B2. Số đo Kiểm soát Chất lượng Audio & Video (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **-16.28 LUFS** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **-2.03 dBFS** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** **3.40**
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng video xuất bản:** 1523.17 s (khớp audio 1523.19 s, $\Delta = 0.023\text{ s} \le 0.05\text{ s}$ — ĐẠT ✅ H14)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **121.2 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **86.8 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **208.7 Hz**
- **Nhân chứng ($N1$ · Cư dân):** F0 trung vị = **177.8 Hz**
- **Lời khai ($N2$ · Linda Kasabian):** F0 trung vị = **289.2 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.78\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.41\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **11.54%** (CER trung bình: **12.85%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.68 / 5.0** (Dải điểm: 1.72 – 3.58). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md`](CanNghe_Tap09_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Video & Thumbnail:**
   - MP4 Master: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp4`](xuat_ban/Tap09_master.mp4) (576.0 MB)
   - MP4 Kênh: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09.mp4`](xuat_ban/Tap09.mp4) (576.0 MB)
   - Thumbnail: [`02_SAN_XUAT/Tap09/xuat_ban/thumbnail.png`](xuat_ban/thumbnail.png) (1.37 MB)
2. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp3`](xuat_ban/Tap09_master.mp3) (48.8 MB)
   - WAV: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.wav`](xuat_ban/Tap09_master.wav) (292.5 MB)
3. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t09.json`](../../.work/timeline_s_t09.json) (1523.19 s)
   - Bảng shot: [`.work/shots_t09.json`](../../.work/shots_t09.json) (196 shots)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09.srt`](xuat_ban/Tap09.srt) (393 cues)
4. **Báo cáo Giám sát:**
   - Báo cáo Dựng video & QC 3 ngôn ngữ: [`02_SAN_XUAT/Tap09/BaoCao_DungVideo_Tap09_20261111.md`](BaoCao_DungVideo_Tap09_20261111.md)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md`](xuat_ban/CanNghe_Tap09_higgs.md)

---

---

---

---

## 6. DANH SÁCH SHOT — TẬP 09 (VI)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `✦` = lần đầu xuất hiện · `→X` = vai của shot kế tiếp · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.
Cột *Chữ* = **NGUYÊN VĂN** câu kịch bản của shot (A7/V3/H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ký tự ⇒ **đậm**.

### INTRO KÊNH · 0,00–22,41 s

Đặt `assets/brand/intro_kenh.mov` tại 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### HỒI 1 — MÙA HÈ TÌNH YÊU & ĐÊM 9-8-1969

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.02#1` (6,7 s) | H | T1 | `t9_summer_of_love_hippie_la`, `pan` | *Nước Mỹ vào cuối thập niên 1960 đang chìm đắm trong cao trào rực rỡ của phong trào Hippie.* | — | ✦ Cú |  |
| 1-02 | `1.02#2` (7,6 s) | H | T1 | `t9_summer_of_love_hippie_la`, `pull` | *Hàng trăm nghìn thanh thiếu niên từ khắp nơi đổ về bang California để tham gia vào Mùa hè Tình yêu.* | — | — |  |
| 1-03 | `1.02#3` (5,6 s) | H | T1 | `t9_acoustic_guitar_flower_crown`, `still` | *Họ cài những bông hoa lên tóc và cùng nhau mơ về một thế giới tự do không có định kiến.* | — | — |  |
| 1-04 | `1.02#4` (9,6 s) | H | T1 | `t9_los_angeles_skyline_1969`, `push` | *Trong mắt thế hệ trẻ lúc bấy giờ, ánh nắng vàng rực rỡ của Los Angeles chính là biểu tượng cho sự thức tỉnh và khai phóng tâm hồn.* | — | — |  |
| 1-05 | `1.02#5` (4,8 s) | H | T1 | `t9_runaway_teenager_bus_stop`, `pan` | *Người ta trao gửi niềm tin trọn vẹn cho những người xa lạ một cách tự nhiên và ngây thơ.* | — | — |  |
| 1-06 | `1.02#6` (8,3 s) | H | T1 | `t9_newspaper_headline_helter_skelter`, `pull` | *Các phương tiện truyền thông liên tục ca ngợi tinh thần tự do phóng khoáng, vô tình tạo nên một điểm mù ngây thơ tập thể che mắt toàn xã hội.* | — | — |  |
| 1-07 | `1.02#7` (7,3 s) | H | T1 | `t9_apocalyptic_desert_hideout`, `still` | *Chính sự mất cảnh giác ấy đã tạo ra một kẽ hở khổng lồ cho những kẻ săn mồi tâm lý ngụy trang trục lợi.* | — | — |  |
| 1-08 | `1.02#8` (7,3 s) | H | T1 | `t9_withered_flower_on_asphalt`, `push` | *Họ không thể ngờ rằng, kỷ nguyên của sự ngây thơ ấy sắp sửa khép lại vĩnh viễn trong một cơn ác mộng kinh hoàng.* | — | — |  |
| 1-09 | `1.04#1` (5,8 s) | H | T1 | `t9_confiscated_clocks_broken_mirror`, `pan` | *Bức tranh lãng mạn ngây thơ ấy đã vỡ vụn thành trăm mảnh vào một đêm mùa hè định mệnh.* | — | — |  |
| 1-10 | `1.04#2` (12,4 s) | H | T1 | `t9_cielo_drive_estate_night`, `pull` | *Đêm ngày 8 rạng sáng ngày 9 tháng 8 năm 1969, một bóng tối kinh hoàng đã ập xuống ngôi biệt thự sang trọng tại số 10050 Đại lộ Cielo Drive.* | — | — |  |
| 1-11 | `1.04#3` (5,2 s) | H | T1 | `t9_beverly_hills_gate_road`, `still` | *Ngôi nhà nằm ẩn mình trên một ngọn đồi biệt lập gần khu Beverly Hills lộng lẫy.* | — | — |  |
| 1-12 | `1.04#4` (10,0 s) | H | T1 | `t9_cielo_drive_living_room_somber`, `push` | *Ngôi biệt thự do đạo diễn lừng danh Roman Polanski thuê đã trở thành hiện trường của một vụ tấn công bạo lực tập thể đầy tàn độc.* | — | — |  |
| 1-13 | `1.04#5`–`#6` (11,6 s) | H | T1 | `t9_broken_porcelain_doll_desert`, `pan` | *Năm người vô tội đã bị tước đoạt mạng sống chỉ trong chớp mắt.* → `#6`: *Trong số các nạn nhân có nữ diễn viên tài hoa Sharon Tate, người vợ đang mang thai gần chín tháng của vị đạo diễn.* | — | — |  |
| 1-14 | `1.04#7` (3,2 s) | H | T1 | `t9_redflag2_severed_family_photos`, `pull` | *Cùng thiệt mạng còn có bốn người bạn thân thiết của gia đình.* | — | — |  |
| 1-15 | `1.06#1` (11,0 s) | H | T1 | `t9_waverly_drive_residence_night`, `still` | *Chưa đầy hai mươi bốn giờ sau đó, một thảm kịch tương tự lại tiếp diễn tại ngôi nhà số 3301 Đại lộ Waverly Drive ở khu Los Feliz.* | — | — |  |
| 1-16 | `1.06#2` (7,8 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `push` | *Hai vợ chồng doanh nhân Leno và Rosemary LaBianca bị … dã man ngay tại phòng khách nhà mình.* | — | — |  |
| 1-17 | `1.06#3` (9,2 s) | H | T1 | `t9_newspaper_headline_helter_skelter`, `pan` | *Sự liên tiếp của hai vụ án tàn khốc nhắm vào những gia đình vô tội đã đánh sập hoàn toàn cảm giác an toàn của toàn bộ cư dân miền nam California.* | — | — |  |
| 1-18 | `1.06#4` (6,3 s) | H | T1 | `t9_los_angeles_skyline_1969`, `pull` | *Đó là sự khởi đầu của một cơn hoang tưởng tập thể chưa từng có trong lịch sử đô thị nước Mỹ.* | — | — |  |
| 1-19 | `1.06#5` (7,0 s) | H | T1 | `t9_retro_radio_broadcast_table`, `still` | *Hãy lắng nghe tiếng lòng của một người dân Los Angeles từng trải qua những ngày tháng đen tối ấy.* | — | →N1 |  |
| 1-20 | `1.07#1` (9,9 s) | N1 | T4 lời kể | `t9_retro_radio_broadcast_table`, `push` | *Vào buổi sáng hôm đó, khi đài phát thanh liên tục đưa tin về thảm kịch tại nhà Sharon Tate, toàn bộ thành phố Los Angeles như rơi vào trạng thái tê liệt vì sợ hãi.* | — | ✦ Cừu |  |
| 1-21 | `1.07#2` (3,8 s) | N1 | T4 lời kể | `t9_waverly_drive_residence_night`, `pan` | *Không một ai dám bước chân ra khỏi nhà khi trời vừa chập tối.* | — | — |  |
| 1-22 | `1.07#3` (8,4 s) | N1 | T4 lời kể | `t9_gun_shop_empty_shelves`, `pull` | *Người ta đổ xô đi mua súng, gia cố then cài cửa sổ và tìm mua chó canh nhà đến mức các cửa hàng cháy sạch hàng rào bảo vệ.* | — | — |  |
| 1-23 | `1.07#4` (7,5 s) | N1 | T4 lời kể | `t9_intact_valuables_diorama`, `still` | *Nỗi kinh hoàng nhất là chúng tôi nhận ra những kẻ đột nhập không hề hành động vì tiền tài hay trang sức quý giá.* | — | — |  |
| 1-24 | `1.07#5` (3,4 s) | N1 | T4 lời kể | `t9_intact_valuables_diorama`, `push` | *Đồ đạc có giá trị trong căn biệt thự vẫn còn nguyên vẹn.* | — | — |  |
| 1-25 | `1.07#6`–`#7` (7,9 s) | N1 | T4 lời kể | `t9_vacant_eyes_doll_shadow`, `pan` | *Đó là một sự tàn nhẫn hoàn toàn vô nghĩa và lạnh lùng.* → `#7`: *Mùa hè Tình yêu của chúng tôi đã chết ngay trong đêm hôm đó.* | — | →H |  |
| 1-26 | `1.09#1`–`#2` (8,6 s) | H | T1 | `t9_lapd_investigation_room`, `pull` | *Hiện trường ở cả hai ngôi nhà để lại những dấu ấn vô cùng kỳ dị và quái đản.* → `#2`: *Không có dấu vết của một vụ cướp của thông thường.* | — | — |  |
| 1-27 | `1.09#3` (11,1 s) | H | T1 | `t9_bloody_letters_forensic_wall`, `still` | *Nhưng trên tường và các cánh cửa, hung thủ đã để lại những dòng chữ nguệch ngoạc: “PIG”* → *“RISE”, và một cụm từ viết sai chính tả: “HEALTER SKELTER”.* | ở "“RISE”, và một cụm từ" | — |  |
| 1-28 | `1.09#4` (7,3 s) | H | T1 | `t9_invisible_puppet_master_shadow`, `push` | *Nước Mỹ bàng hoàng tự hỏi: Động cơ nào có thể dẫn đến những hành vi tàn khốc đến mức phi nhân tính như vậy?* | — | →D |  |
| 1-29 | `1.10#1` (6,7 s) | D | T1 | `t9_lapd_investigation_room`, `pan` | *Trong những tuần đầu tiên, Sở Cảnh sát Los Angeles hoàn toàn rơi vào bế tắc trước một bài toán không có lời giải.* | — | ✦ Sói |  |
| 1-30 | `1.10#2` (7,0 s) | D | T1 | `t9_beverly_hills_gate_road`, `pull` | *Không hề có bất kỳ mối quan hệ quen biết nào giữa gia đình nữ diễn viên Sharon Tate và vợ chồng doanh nhân LaBianca.* | — | — |  |
| 1-31 | `1.10#3` (4,6 s) | D | T1 | `t9_los_angeles_county_crime_map`, `still` | *Hai hiện trường cách nhau hàng chục cây số, nạn nhân thuộc các tầng lớp xã hội khác nhau.* | — | — |  |
| 1-32 | `1.10#4` (5,0 s) | D | T1 | `t9_bloody_letters_forensic_wall`, `push` | *Thế nhưng phương thức sắp đặt hiện trường lại mang cùng một chữ ký kỳ quái.* | — | — |  |
| 1-33 | `1.10#5` (4,6 s) | D | T1 | `t9_dark_triad_psychological_symbol`, `pan` | *Về mặt nghiệp vụ, chúng tôi nhận thấy những kẻ ra tay không hành động vì tư thù cá nhân.* | — | — |  |
| 1-34 | `1.10#6` (4,4 s) | D | T1 | `t9_invisible_puppet_master_shadow`, `pull` | *Chúng dường như đang tuân theo một kịch bản ma quái được điều khiển từ xa.* | — | — |  |
| 1-35 | `1.10#7` (3,2 s) | D | T1 | `t9_intact_valuables_diorama`, `still` | *Đó không phải là hành vi bộc phát của những tên trộm cắp thông thường.* | — | — |  |
| 1-36 | `1.10#8` (3,1 s) | D | T1 | `t9_shadow_devil_dialogue_noir`, `push` | *Đó là sự thực thi lạnh lùng của một mệnh lệnh cuồng tín.* | — | →H |  |
| 1-37 | `1.12#1` (4,0 s) | H | T1 | `t9_summer_of_love_hippie_la`, `pan` | *Chào mừng quý vị đến với kênh Amber eyes.* | — | — |  |
| 1-38 | `1.12#2` (12,2 s) | H | T1 | `t9_amber_eyes_closing_dossier`, `pull` | *Hôm nay, chúng ta sẽ mở khóa một trong những hồ sơ tâm lý học tội phạm chấn động và bí ẩn nhất thế kỷ hai mươi: Hồ sơ Charles Manson và thảm kịch Gia đình Manson.* | — | — |  |
| 1-39 | `1.12#3` (11,2 s) | H | T1 | `t9_prison_cell_bars_shadow`, `still` | *Chúng ta sẽ cùng giải mã: Làm thế nào một kẻ lang thang với nửa đời trong tù ngục lại có thể biến những thanh niên ưu tú thành những cỗ máy hủy diệt không còn lương tri?* | — | — |  |
| 1-40 | `1.12#4` (8,2 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `push` | *Và nghệ thuật xóa bỏ bản ngã của một kẻ ái kỷ ác tính đã vận hành tinh vi đến mức nào để thao túng cả một bầy đàn?* | — | — |  |
| 1-41 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 02* · **GIA ĐÌNH MANSON & TRẠI SPAHN RANCH** | — | ⊘ | ◼ |

### HỒI 2 — GIA ĐÌNH MANSON & TRẠI SPAHN RANCH

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (9,3 s) | H | T1 | `t9_midnight_convoy_old_ford`, `pull` | *Để lần theo bóng ma đứng sau chuỗi tội ác kinh hoàng, hướng điều tra cuối cùng đã dẫn các thám tử rời khỏi những biệt thự lộng lẫy của Hollywood.* | — | — |  |
| 2-02 | `2.02#2` (3,5 s) | H | T1 | `t9_spahn_ranch_western_facade`, `still` | *Họ tiến sâu vào thung lũng Santa Susana cằn cỗi.* | — | — |  |
| 2-03 | `2.02#3` (4,2 s) | H | T1 | `t9_spahn_ranch_western_facade`, `push` | *Điểm đến là trang trại Spahn Ranch ở vùng ngoại ô Chatsworth.* | — | — |  |
| 2-04 | `2.02#4` (6,8 s) | H | T1 | `t9_spahn_ranch_dilapidated_porch`, `pan` | *Nơi đây từng là một phim trường hoang tàn chuyên dùng để quay các bộ phim cao bồi miền viễn tây của thế kỷ trước.* | — | — |  |
| 2-05 | `2.02#5` (9,8 s) | H | T1 | `t9_gate_of_spahn_ranch_departure`, `pull` | *Giữa những căn nhà gỗ mục nát và bãi đất hoang cằn cỗi, một cộng đồng kỳ lạ gồm hàng chục thanh thiếu niên đang sinh sống biệt lập với xã hội loài người.* | — | →D |  |
| 2-06 | `2.04#1` (3,3 s) | D | T1 | `t9_haight_ashbury_psychedelic_street`, `still` | *Họ tự gọi mình bằng một danh xưng ấm áp: “Gia đình” (The Manson Family).* | — | — |  |
| 2-07 | `2.04#2` (4,8 s) | D | T1 | `t9_manson_shadow_campfire_desert`, `push` | *Người đứng đầu và nắm giữ quyền lực tuyệt đối tại trang trại là Charles Milles Manson.* | — | — |  |
| 2-08 | `2.04#3` (5,8 s) | D | T1 | `t9_manson_shadow_campfire_desert`, `pan` | *Hắn là một người đàn ông ba mươi tư tuổi với vóc dáng nhỏ thó nhưng ánh mắt sắc lạnh như thôi miên.* | — | — |  |
| 2-09 | `2.04#4` (5,0 s) | D | T1 | `t9_dark_triad_psychological_symbol`, `pull` | *Về mặt nhân thân, Manson không phải là một giáo sĩ uyên bác hay một triết gia khai phóng.* | — | — |  |
| 2-10 | `2.04#5` (7,0 s) | D | T1 | `t9_prison_cell_bars_shadow`, `still` | *Hắn là một kẻ du thủ du thực, từng trải qua hơn một nửa cuộc đời mình sau song sắt của các trường giáo dưỡng và nhà tù liên bang.* | — | — |  |
| 2-11 | `2.04#6` (5,0 s) | D | T1 | `t9_gun_shop_empty_shelves`, `push` | *Hắn có tiền án dày đặc về tội trộm cắp, lừa đảo chi phiếu và môi giới mại dâm.* | — | →H |  |
| 2-12 | `2.05#1` (11,2 s) | H | T1 | `t9_haight_ashbury_psychedelic_street`, `pan` | *Khi được trả tự do vào tháng 3 năm 1967, Manson bước thẳng vào trung tâm của phong trào Hippie tại khu Haight-Ashbury, thành phố San Francisco.* | — | — |  |
| 2-13 | `2.05#2` (13,6 s) | H | T1 | `t9_acoustic_guitar_flower_crown`, `pull` | *Nhận thấy trào lưu văn hóa phản kháng tôn sùng tình yêu tự do và sự ngây thơ của giới trẻ, Manson đã lợi dụng triệt để “Hiệu ứng Hào quang” của một đạo sư du mục để che đậy bản chất săn mồi.* | — | — |  |
| 2-14 | `2.05#3` (9,9 s) | H | T1 | `t9_acoustic_guitar_flower_crown`, `still` | *Hắn cầm cây đàn guitar, cất lên những bài ca tự do và nhanh chóng thu hút quanh mình những thanh thiếu niên đang nổi loạn hoặc khủng hoảng bản sắc cá nhân.* | — | — |  |
| 2-15 | `2.05#4` (4,4 s) | H | T1 | `t9_gate_of_spahn_ranch_departure`, `push` | *Hắn đưa họ về trang trại Spahn Ranch, thiết lập một thế giới khép kín.* | — | — |  |
| 2-16 | `2.05#5` (7,4 s) | H | T1 | `t9_apocalyptic_desert_hideout`, `pan` | *Tại đây, hắn bắt đầu gieo rắc vào tâm trí họ một học thuyết tận thế điên cuồng mang tên “Helter Skelter”.* | — | →D |  |
| 2-17 | `2.06#1` (9,7 s) | D | T1 | `t9_invisible_puppet_master_shadow`, `pull` | *Qua quá trình trinh sát và đối chiếu chứng cứ, chúng tôi nhận thấy tội ác của Manson không bùng phát ngẫu nhiên, mà vận hành qua một quỹ đạo leo thang hành vi gồm năm giai đoạn rõ rệt:* | — | — |  |
| 2-18 | `2.06#2` (5,0 s) | D | T1 | `t9_runaway_teenager_bus_stop`, `still` | *Giai đoạn một: Tội phạm vị thành niên và lừa đảo.* | — | — |  |
| 2-19 | `2.06#3` (5,5 s) | D | T1 | `t9_prison_cell_bars_shadow`, `push` | *Manson rèn luyện kỹ năng thao túng tâm lý và dối trá bệnh lý qua hàng chục năm trong tù giam.* | — | — |  |
| 2-20 | `2.06#4` (3,8 s) | D | T1 | `t9_trauma_bonding_group_shadows`, `pan` | *Giai đoạn hai: Xây dựng giáo phái và kiểm soát tinh thần.* | — | — |  |
| 2-21 | `2.06#5` (7,5 s) | D | T1 | `t9_lsd_hallucinogen_distorted_reality`, `pull` | *Dùng ma túy ảo giác LSD và tình dục bầy đàn để phá vỡ cấu trúc nhân cách của các tín đồ trẻ tại Spahn Ranch.* | — | — |  |
| 2-22 | `2.06#6` (3,7 s) | D | T1 | `t9_confiscated_clocks_broken_mirror`, `still` | *Giai đoạn ba: Trò chơi đột nhập đêm “Creepy Crawling”.* | — | — |  |
| 2-23 | `2.06#7` (10,0 s) | D | T1 | `t9_midnight_convoy_old_ford`, `push` | *Manson dẫn các đệ tử đột nhập vào các ngôi nhà dân cư lúc nửa đêm, không lấy tài sản mà chỉ di chuyển đồ đạc để tập dượt cảm giác toàn năng và kiểm soát vô hình.* | — | — |  |
| 2-24 | `2.06#8` (7,7 s) | D | T1 | `t9_dark_triad_psychological_symbol`, `pan` | *Mỗi lần xâm nhập ranh giới riêng tư mà không bị trừng phạt, ngưỡng dung nạp sự sai trái trong não bộ của họ lại được nới rộng thêm một nấc.* | — | — |  |
| 2-25 | `2.06#9` (3,2 s) | D | T1 | `t9_gun_shop_empty_shelves`, `pull` | *Giai đoạn bốn: Bạo lực bộc phát có vũ trang.* | — | — |  |
| 2-26 | `2.06#10` (12,3 s) | D | T1 | `t9_midnight_convoy_old_ford`, `still` | *Cuối tháng 7 năm 1969, Manson bắn trọng thương tay buôn ma túy Bernard Crowe và chỉ đạo đệ tử … nhạc sĩ Gary Hinman sau một vụ tranh chấp tiền bạc.* | — | — |  |
| 2-27 | `2.06#11`–`#12` (10,3 s) | D | T1 | `t9_cielo_drive_road_sign_shadow`, `push` | *Giai đoạn năm: Đỉnh điểm hủy diệt hàng loạt.* → `#12`: *Khi ngưỡng dung nạp bạo lực bị lờn, Manson ra lệnh tấn công biệt thự Cielo Drive và nhà LaBianca để tạo ra thảm sát biểu tượng.* | — | — |  |
| 2-28 | `2.06#13` (10,1 s) | D | T1 | `t9_burning_id_cards_ashes`, `pan` | *Sự leo thang này phản ánh quy luật tâm lý rõ rệt: khi hành vi sai trái ban đầu không bị ngăn chặn, cảm giác đói ảo tưởng sẽ thôi thúc kẻ thủ ác mở rộng phạm vi tàn phá.* | — | — |  |
| 2-29 | `2.06#14` (11,2 s) | D | T1 | `t9_spahn_ranch_dilapidated_porch`, `pull` | *Nhưng ngay trong cộng đồng Spahn Ranch ngột ngạt ấy, Linda Kasabian, một người mẹ trẻ mang theo đứa con mười sáu tháng tuổi, đã bắt đầu cảm thấy sự bất an rợn người trước cỗ máy cuồng tín này.* | — | →H |  |
| 2-30 | `2.08#1` (6,9 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `still` | *Nhưng ngòi nổ tâm lý trực tiếp nào đã kích hoạt vụ tấn công nhắm vào ngôi biệt thự tại Cielo Drive?* | — | — |  |
| 2-31 | `2.08#2` (10,5 s) | H | T1 | `t9_recording_studio_rejected_demo`, `push` | *Đằng sau vỏ bọc đấng cứu thế, Manson luôn nuôi dưỡng một khao khát ái kỷ bệnh hoạn: trở thành một ngôi sao nhạc rock vĩ đại hơn cả ban nhạc The Beatles.* | — | — |  |
| 2-32 | `2.08#3` (10,1 s) | H | T1 | `t9_recording_studio_rejected_demo`, `pan` | *Hắn đã tìm mọi cách tiếp cận nhà sản xuất âm nhạc nổi tiếng Terry Melcher của hãng đĩa Columbia Records với hy vọng được ký hợp đồng thu âm.* | — | — |  |
| 2-33 | `2.08#4` (9,7 s) | H | T1 | `t9_broken_porcelain_doll_desert`, `pull` | *Nhưng khi Melcher từ chối ký hợp đồng và không hỗ trợ phát hành album, cái tôi ái kỷ mong manh của Manson đã phải hứng chịu một sự sỉ nhục tột cùng.* | — | — |  |
| 2-34 | `2.08#5` (4,7 s) | H | T1 | `t9_manson_shadow_campfire_desert`, `still` | *Cảm giác bị chối bỏ đã biến thành một cơn thịnh nộ hủy diệt.* | — | →D |  |
| 2-35 | `2.09#1` (10,3 s) | D | T1 | `t9_cielo_drive_estate_night`, `push` | *Ngôi biệt thự tại số 10050 Cielo Drive chính là căn nhà mà Terry Melcher từng thuê ở trước khi đạo diễn Roman Polanski chuyển đến.* | — | — |  |
| 2-36 | `2.09#2` (8,5 s) | D | T1 | `t9_cielo_drive_road_sign_shadow`, `pan` | *Dù biết Melcher đã dọn đi, Manson vẫn chọn địa điểm này để trút bỏ cơn giận dữ và thỏa mãn ảo tưởng trả thù giới tinh hoa Hollywood.* | — | — |  |
| 2-37 | `2.09#3` (8,5 s) | D | T1 | `t9_kasabian_escape_night_highway`, `pull` | *Hắn chỉ đạo Charles Tex Watson cùng ba nữ đệ tử đến ngôi nhà với mệnh lệnh rõ ràng: hủy diệt toàn bộ những ai có mặt bên trong.* | — | — |  |
| 2-38 | `2.09#4`–`#5` (10,7 s) | D | T1 | `t9_bloody_letters_forensic_wall`, `still` | *Chúng tôi phân định rất rõ giữa thủ đoạn và chữ ký tâm lý tại hiện trường.* → `#5`: *Thủ đoạn (MO) là cắt dây điện thoại, dùng vũ khí lạnh và xóa dấu vết tẩu thoát.* | — | — |  |
| 2-39 | `2.09#6` (9,2 s) | D | T1 | `t9_interlocking_knots_rope`, `push` | *Còn Chữ ký (Signature) bất biến là những dòng chữ “PIG” và sợi dây thừng dài buộc nối các nạn nhân để tạo thành một vở kịch trình diễn ghê rợn.* | — | →H |  |
| 2-40 | `2.10#1` (8,6 s) | H | T1 | `t9_los_angeles_county_crime_map`, `pan` | *Về mặt nạn nhân học, những con người tại Cielo Drive và Waverly Drive không hề có bất kỳ ân oán nào với Manson.* | — | — |  |
| 2-41 | `2.10#2` (17,8 s) | H | T1 | `t9_broken_porcelain_doll_desert`, `pull` | *Nữ diễn viên tài hoa Sharon Tate, nhà tạo mẫu tóc Jay Sebring, Abigail Folger, Wojciech Frykowski, thiếu niên Steven Parent* → *cùng vợ chồng doanh nhân Leno và Rosemary LaBianca đều là những sinh mệnh tràn đầy ước mơ và nhân phẩm.* | ở "cùng vợ chồng doanh nhân" | — |  |
| 2-42 | `2.10#3` (7,7 s) | H | T1 | `t9_yearbook_photos_shadow`, `still` | *Họ đã bị tước đoạt mạng sống chỉ vì trở thành vật tế thần cho sự thất bại cay đắng của một kẻ cuồng vọng ái kỷ.* | — | — |  |
| 2-43 | `2.10#4` (7,6 s) | H | T1 | `t9_withered_flower_on_asphalt`, `push` | *Họ xứng đáng được nhớ đến với tư cách những con người trọn vẹn, chứ không phải những cái tên gắn liền với một thảm kịch.* | — | — |  |
| 2-44 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 03* · **BA GIAI ĐOẠN XÓA BẢN NGÃ** | — | ⊘ | ◼ |

### HỒI 3 — BA GIAI ĐOẠN XÓA BẢN NGÃ

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (8,1 s) | H | T1 | `t9_los_angeles_skyline_1969`, `pull` | *Khi danh tính của nhóm thủ phạm trực tiếp được công bố, toàn bộ nước Mỹ đã rơi vào một cơn chấn động tinh thần chưa từng có.* | — | — |  |
| 3-02 | `3.02#2` (8,6 s) | H | T1 | `t9_yearbook_photos_shadow`, `still` | *Kẻ chỉ huy trực tiếp hiện trường là Charles “Tex” Watson, một cựu học sinh ưu tú, ngôi sao thể thao trung học đến từ bang Texas.* | — | — |  |
| 3-03 | `3.02#3` (5,2 s) | H | T1 | `t9_spahn_ranch_dilapidated_porch`, `push` | *Đi cùng hắn là những cô gái trẻ xuất thân từ các gia đình trung lưu gia giáo.* | — | — |  |
| 3-04 | `3.02#4` (11,6 s) | H | T1 | `t9_haight_ashbury_psychedelic_street`, `pan` | *Susan Atkins từng hát trong ca đoàn nhà thờ, Patricia Krenwinkel hiền lành, và Leslie Van Houten từng là cựu hoa khôi trung học gương mẫu.* | — | — |  |
| 3-05 | `3.02#5` (9,4 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `pull` | *Làm thế nào một nhóm thanh niên trí thức bình thường lại có thể tự nguyện từ bỏ hoàn toàn lương tri để biến mình thành những công cụ hủy diệt vô cảm?* | — | →C |  |
| 3-06 | `3.03#1` (10,0 s) | C | T1 | `t9_kurt_lewin_three_stages_diagram`, `still` | *Để giải mã hiện tượng này, chúng ta cần vận dụng mô hình thay đổi nhận thức ba giai đoạn của nhà tâm lý học Kurt Lewin* → *được giáo sư Edgar Schein phát triển trong nghiên cứu về cơ chế tẩy não:* | ở "được giáo sư Edgar Schein" | ✦ Cáo |  |
| 3-07 | `3.03#2` (4,8 s) | C | T1 | `t9_kurt_lewin_three_stages_diagram`, `push` | *Đó là: Làm tan rã bản ngã (Unfreezing), Lập trình lại nhận thức (Changing), và Tái cố định hành vi (Refreezing).* | — | — |  |
| 3-08 | `3.03#3`–`#4` (8,0 s) | C | T1 | `t9_dark_triad_psychological_symbol`, `pan` | *Charles Manson không sở hữu siêu năng lực kỳ bí nào.* → `#4`: *Hắn chỉ là một bậc thầy ứng dụng trực giác các kỹ thuật thao túng tâm lý bầy đàn tàn bạo nhất.* | — | — |  |
| 3-09 | `3.03#5` (3,7 s) | C | T1 | `t9_kurt_lewin_three_stages_diagram`, `pull` | *Quá trình tước đoạt nhân cách này được thực hiện bài bản qua từng bước một.* | — | →H |  |
| 3-10 | `3.05#1` (5,2 s) | H | T1 | `t9_kurt_lewin_three_stages_diagram`, `still` | *Bước thứ nhất: Làm tan rã bản ngã cũ, hay còn gọi là Unfreezing.* | — | — |  |
| 3-11 | `3.05#2` (6,4 s) | H | T1 | `t9_unfreezing_love_bombing_circle`, `push` | *Khi một thanh niên mới bước chân vào Spahn Ranch, Manson lập tức triển khai chiến thuật “Dội bom tình cảm” (Love Bombing).* | — | — |  |
| 3-12 | `3.05#3` (5,7 s) | H | T1 | `t9_unfreezing_love_bombing_circle`, `pan` | *Hắn ôm lấy họ, nhìn thẳng vào mắt và nói rằng họ là những sinh linh hoàn hảo.* | — | — |  |
| 3-13 | `3.05#4` (4,9 s) | H | T1 | `t9_blind_devotion_extinguished_candle`, `pull` | *Hắn khéo léo lấp đầy mọi khoảng trống tổn thương mà gia đình ruột thịt để lại.* | — | →C |  |
| 3-14 | `3.06#1` (3,5 s) | C | T1 | `t9_redflag2_severed_family_photos`, `still` | *Nhưng ngay sau cái ôm nồng ấm là chiếc bẫy cô lập xã hội tàn nhẫn.* | — | — |  |
| 3-15 | `3.06#2` (8,1 s) | C | T1 | `t9_burning_id_cards_ashes`, `push` | *Manson yêu cầu các thành viên phải vứt bỏ toàn bộ tiền bạc, giấy tờ tùy thân và cắt đứt hoàn toàn liên lạc với cha mẹ.* | — | — |  |
| 3-16 | `3.06#3`–`#4` (12,2 s) | C | T1 | `t9_burning_id_cards_ashes`, `pan` | *Hắn tước bỏ tên thật của họ và gán cho những bí danh mới như Sadie, Katie hay Lulu để xóa sạch danh tính quá khứ.* → `#4`: *Trong các buổi lễ ban đêm, hắn cho các tín đồ sử dụng ma túy ảo giác LSD liều cao.* | — | — |  |
| 3-17 | `3.06#5` (4,4 s) | C | T1 | `t9_blind_devotion_extinguished_candle`, `pull` | *Bản thân Manson chỉ dùng một lượng rất nhỏ để duy trì sự tỉnh táo kiểm soát.* | — | — |  |
| 3-18 | `3.06#6` (5,8 s) | C | T1 | `t9_inverted_cross_moral_confusion`, `still` | *Dưới tác động của ảo giác và sự kiệt quệ thể xác, bức tường bản ngã của những người trẻ hoàn toàn sụp đổ.* | — | — |  |
| 3-19 | `3.06#7` (3,0 s) | C | T1 | `t9_trauma_bonding_group_shadows`, `push` | *Tâm trí họ nhanh chóng trở thành một tờ giấy trắng tuyệt đối.* | — | →H |  |
| 3-20 | `3.07#1` (6,8 s) | H | T1 | `t9_changing_night_desert_sermon`, `pan` | *Bước thứ hai: Lập trình lại nhận thức, hay giai đoạn Changing.* | — | — |  |
| 3-21 | `3.07#2` (8,3 s) | H | T1 | `t9_changing_night_desert_sermon`, `pull` | *Khi các đệ tử đã đánh mất khả năng tư duy độc lập, Manson bắt đầu nhồi nhét học thuyết ngày tận thế vào đầu óc họ.* | — | →C |  |
| 3-22 | `3.08#1` (7,6 s) | C | T1 | `t9_vinyl_record_white_album`, `still` | *Hắn bóp méo lời bài hát “Helter Skelter” trong Album Trắng của The Beatles thành một lời tiên tri về cuộc chiến tranh sắc tộc sắp sửa bùng nổ.* | — | — |  |
| 3-23 | `3.08#2` (5,1 s) | C | T1 | `t9_blind_devotion_extinguished_candle`, `push` | *Hắn tự biến mình thành hiện thân của Chúa Jesus và đồng thời là chuẩn mực chân lý duy nhất.* | — | — |  |
| 3-24 | `3.08#3` (7,8 s) | C | T1 | `t9_mastermind_conspiracy_law_book`, `pan` | *Để ru ngủ lương tri của đệ tử, Manson dạy họ các kỹ thuật Trung hòa đạo đức theo lý thuyết của Sykes và Matza:* | — | — |  |
| 3-25 | `3.08#4` (8,1 s) | C | T1 | `t9_inverted_cross_moral_confusion`, `pull` | *Kháng cáo lòng trung thành cao hơn: Manson thuyết giảng rằng tước đoạt sinh mệnh trong Helter Skelter không phải tội ác, mà là sự giải thoát tâm linh phục vụ tình yêu nhân loại.* | — | — |  |
| 3-26 | `3.08#5` (9,0 s) | C | T1 | `t9_shadow_devil_dialogue_noir`, `still` | *Vật hóa và phi nhân hóa nạn nhân: Nạn nhân không phải là con người, mà chỉ là những “Pigs” – biểu tượng đạo đức giả của tầng lớp thượng lưu cần bị thanh tẩy.* | — | — |  |
| 3-27 | `3.08#6` (7,3 s) | C | T1 | `t9_interlocking_knots_rope`, `push` | *Ngoại hóa trách nhiệm cá nhân: Ý chí hành động thuộc về sứ mệnh vũ trụ, các môn đồ chỉ là công cụ vô can thi hành mệnh lệnh thiêng liêng.* | — | — |  |
| 3-28 | `3.08#7` (8,8 s) | C | T1 | `t9_vacant_eyes_doll_shadow`, `pan` | *Đồng thời, trạng thái Phân ly Nhận thức Cực độ kết hợp với Hôn mê Đạo đức đã khiến các sát thủ trẻ hoàn toàn ngắt kết nối với thực tại đau đớn.* | — | — |  |
| 3-29 | `3.08#8` (7,4 s) | C | T1 | `t9_broken_porcelain_doll_desert`, `pull` | *Họ không nhìn thấy những con người bằng xương bằng thịt đang van xin; bộ não bị thao túng chỉ nhìn thấy những đạo cụ sân khấu trong một vở kịch vũ trụ.* | — | — |  |
| 3-30 | `3.08#9` (5,4 s) | C | T1 | `t9_dark_triad_psychological_symbol`, `still` | *Đối với Manson, hắn khuyết tật hoàn toàn Thuyết tâm trí và vô cảm trước nỗi đau của đồng loại.* | — | — |  |
| 3-31 | `3.08#10` (7,2 s) | C | T1 | `t9_invisible_puppet_master_shadow`, `push` | *Tiếng van xin của nạn nhân không đánh thức sự trắc ẩn mà kích hoạt cơn hưng phấn quyền lực tột độ của một kẻ mang cấu trúc ái kỷ ác tính.* | — | — |  |
| 3-32 | `3.08#11` (6,4 s) | C | T1 | `t9_trauma_bonding_group_shadows`, `pan` | *Hắn không coi đệ tử là người thân yêu, mà xem họ như những công cụ kéo dài của bản ngã để thỏa mãn ảo tưởng thống trị.* | — | →H |  |
| 3-33 | `3.10#1` (6,9 s) | H | T1 | `t9_kurt_lewin_three_stages_diagram`, `pull` | *Và bước cuối cùng để hoàn tất cỗ máy điều khiển: Tái cố định hành vi, hay Refreezing.* | — | — |  |
| 3-34 | `3.10#2` (7,5 s) | H | T1 | `t9_vacant_eyes_doll_shadow`, `still` | *Làm thế nào Manson đảm bảo rằng những cô gái trẻ sẽ không bao giờ tỉnh mộng hay quay đầu lại với xã hội?* | — | →C |  |
| 3-35 | `3.11#1` (5,2 s) | C | T1 | `t9_trauma_bonding_group_shadows`, `push` | *Câu trả lời chính là: Sự gắn kết chấn thương cực đoan (Trauma Bonding) thông qua hành vi đồng lõa phạm tội.* | — | — |  |
| 3-36 | `3.11#2` (8,1 s) | C | T1 | `t9_interlocking_knots_rope`, `pan` | *Bằng cách ép buộc các thành viên cùng nhúng chàm vào những hành động bạo lực tập thể, Manson đã ràng buộc họ vào một bí mật tội ác chung không thể chia cắt.* | — | — |  |
| 3-37 | `3.11#3` (3,6 s) | C | T1 | `t9_burning_id_cards_ashes`, `pull` | *Cảm giác tội lỗi cá nhân bị hòa tan hoàn toàn vào tâm lý bầy đàn.* | — | — |  |
| 3-38 | `3.11#4` (6,9 s) | C | T1 | `t9_gate_of_spahn_ranch_departure`, `still` | *Khi tất cả cùng vi phạm điều cấm kỵ tối thượng của nhân loại, con đường quay trở lại cuộc sống bình thường đã bị xóa bỏ vĩnh viễn.* | — | — |  |
| 3-39 | `3.11#5` (4,1 s) | C | T1 | `t9_manson_shadow_campfire_desert`, `push` | *Số phận của họ từ đó bị gắn kết hoàn toàn vào quyền lực của kẻ thủ lĩnh.* | — | — |  |
| 3-40 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 04* · **TRUY QUÉT · NHÂN CHỨNG · XÉT XỬ** | — | ⊘ | ◼ |

### HỒI 4 — TRUY QUÉT · NHÂN CHỨNG · XÉT XỬ

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (9,4 s) | H | T1 | `t9_death_valley_barker_ranch_raid`, `pull` | *Sau chuỗi tội ác chấn động vào tháng 8 năm 1969, nhóm sát thủ rút về ẩn náu tại vùng sa mạc hoang vu Death Valley.* | — | — |  |
| 4-02 | `4.02#2` (6,0 s) | H | T1 | `t9_death_valley_barker_ranch_raid`, `still` | *Cuộc điều tra bế tắc của cảnh sát chỉ tìm thấy ánh sáng vào tháng 10 năm 1969.* | — | — |  |
| 4-03 | `4.02#3` (7,1 s) | H | T1 | `t9_kasabian_escape_night_highway`, `push` | *Khi đó, một lực lượng liên ngành truy quét các vụ trộm cắp xe địa hình và bắt giữ Manson cùng hàng chục tín đồ.* | — | — |  |
| 4-04 | `4.02#4` (8,4 s) | H | T1 | `t9_lapd_investigation_room`, `pan` | *Ban đầu, các điều tra viên không hề hay biết rằng mình đang giữ trong tay những kẻ đứng sau thảm kịch Tate-LaBianca.* | — | →D |  |
| 4-05 | `4.03#1` (3,6 s) | D | T1 | `t9_sybil_brand_jail_corridor`, `pull` | *Bước ngoặt xuất hiện từ chính sự kiêu hãnh ái kỷ của hung thủ.* | — | — |  |
| 4-06 | `4.03#2` (5,8 s) | D | T1 | `t9_sybil_brand_jail_corridor`, `still` | *Trong Trại giam Sybil Brand, nữ tín đồ Susan Atkins không kiềm chế được nhu cầu khoe khoang.* | — | — |  |
| 4-07 | `4.03#3` (5,0 s) | D | T1 | `t9_prison_cell_bars_shadow`, `push` | *Ả đã kể lại chi tiết vụ án tại biệt thự Cielo Drive cho hai người bạn cùng phòng giam.* | — | — |  |
| 4-08 | `4.03#4` (5,1 s) | D | T1 | `t9_lapd_investigation_room`, `pan` | *Lời thú nhận chấn động đó lập tức được chuyển đến ban chuyên án của Sở Cảnh sát Los Angeles.* | — | — |  |
| 4-09 | `4.03#5` (5,8 s) | D | T1 | `t9_bloody_letters_forensic_wall`, `pull` | *Từ lời khai này, cơ quan điều tra nhanh chóng xâu chuỗi các bằng chứng vật chất và dấu vân tay hiện trường.* | — | — |  |
| 4-10 | `4.03#6` (3,8 s) | D | T1 | `t9_yearbook_photos_shadow`, `still` | *Danh tính của toàn bộ mạng lưới thủ phạm nhanh chóng lộ diện hoàn toàn.* | — | →H |  |
| 4-11 | `4.04#1` (8,2 s) | H | T1 | `t9_courtroom_gavel_bench`, `push` | *Nhưng để đưa được kẻ chủ mưu ra trước vành móng ngựa, cơ quan công tố cần một nhân chứng sống bước ra từ chính vòng tay của giáo phái.* | — | — |  |
| 4-12 | `4.04#2` (4,5 s) | H | T1 | `t9_linda_kasabian_witness_dossier`, `pan` | *Người đó là Linda Kasabian, một người mẹ trẻ hai mươi tuổi.* | — | — |  |
| 4-13 | `4.04#3` (7,6 s) | H | T1 | `t9_cielo_drive_front_gate_fog`, `pull` | *Cô từng có mặt tại hiện trường ở vị trí cảnh giới ngoài cổng nhưng từ chối tham gia bạo lực và sau đó đã trốn chạy.* | — | — |  |
| 4-14 | `4.04#4` (5,5 s) | H | T1 | `t9_kasabian_escape_night_highway`, `still` | *Hãy lắng nghe lời chứng đầy ám ảnh của cô khi đối diện với Manson trước tòa án.* | — | →N2 |  |
| 4-15 | `4.05#1` (8,2 s) | N2 | T4 lời kể | `t9_linda_kasabian_witness_dossier`, `push` | *Khi đứng trước bục nhân chứng và nhìn thẳng vào mắt Charles Manson, tôi cảm thấy một nỗi ớn lạnh buốt giá chạy dọc sống lưng.* | — | ✦ Mèo |  |
| 4-16 | `4.05#2` (8,3 s) | N2 | T4 lời kể | `t9_vacant_eyes_doll_shadow`, `pan` | *Những người bạn từng cùng tôi sống ở trang trại Spahn Ranch giờ đây ngồi đó với ánh mắt trống rỗng như những con búp bê bị giật dây.* | — | — |  |
| 4-17 | `4.05#3` (4,1 s) | N2 | T4 lời kể | `t9_trauma_bonding_group_shadows`, `pull` | *Họ không còn nhận thức được nỗi đau hay sự sợ hãi của đồng loại.* | — | — |  |
| 4-18 | `4.05#4` (6,0 s) | N2 | T4 lời kể | `t9_blind_devotion_extinguished_candle`, `still` | *Tôi đã chứng kiến họ đánh mất chính mình từng chút một dưới những lời thao túng của Manson.* | — | — |  |
| 4-19 | `4.05#5` (10,2 s) | N2 | T4 lời kể | `t9_cielo_drive_front_gate_fog`, `push` | *Vào cái đêm định mệnh tại Cielo Drive, khi đứng chết lặng ngoài cổng và nghe thấy tiếng kêu cứu trong màn đêm, có một thứ gì đó bên trong tôi đã vỡ vụn.* | — | — |  |
| 4-20 | `4.05#6` (8,9 s) | N2 | T4 lời kể | `t9_spahn_ranch_western_facade`, `pan` | *Tôi không thể làm hại bất kỳ ai, bởi vì ở Spahn Ranch còn có đứa con gái nhỏ đang đợi tôi trở về.* | — | — |  |
| 4-21 | `4.05#7` (8,1 s) | N2 | T4 lời kể | `t9_kasabian_escape_night_highway`, `pull` | *Nỗi sợ hãi mất con và sự ghê tởm tội ác đã đánh thức tôi khỏi cơn ác mộng ma quái để ôm con trốn chạy trong đêm.* | — | — |  |
| 4-22 | `4.05#8` (12,7 s) | N2 | T4 lời kể | `t9_scales_of_justice_broken_chains`, `still` | *Đứng ra làm chứng là quyết định khó khăn nhất cuộc đời tôi* → *nhưng tôi phải nói lên sự thật để trả lại công lý cho các nạn nhân và giải thoát linh hồn mình khỏi bóng ma tội lỗi.* | ở "nhưng tôi phải nói lên" | →H |  |
| 4-23 | `4.07#1` (11,0 s) | H | T1 | `t9_los_angeles_hall_of_justice`, `push` | *Phiên tòa xét xử Charles Manson và các đồng phạm chính thức mở màn vào tháng 6 năm 1970 dưới sự chủ tọa của Thẩm phán Charles Older.* | — | — |  |
| 4-24 | `4.07#2` (7,1 s) | H | T1 | `t9_los_angeles_hall_of_justice`, `pan` | *Đây là một trong những phiên tòa dài nhất, tốn kém nhất và kỳ dị nhất trong toàn bộ lịch sử tư pháp nước Mỹ.* | — | — |  |
| 4-25 | `4.07#3` (8,5 s) | H | T1 | `t9_collective_hysteria_three_shaved_heads`, `pull` | *Bên ngoài tòa án, các tín đồ còn lại liên tục quỳ gối trên vỉa hè, cạo trọc đầu và đe dọa các nhân chứng tham gia xét xử.* | — | — |  |
| 4-26 | `4.07#4` (5,6 s) | H | T1 | `t9_prosecutor_desk_evidence_files`, `still` | *Trọng trách lịch sử đè nặng lên vai Phó Công tố viên Vincent Bugliosi.* | — | →D |  |
| 4-27 | `4.08#1` (5,1 s) | D | T1 | `t9_prosecutor_desk_evidence_files`, `push` | *Thách thức pháp lý lớn nhất của bên công tố là chứng minh tội danh của Charles Manson.* | — | — |  |
| 4-28 | `4.08#2`–`#3` (10,3 s) | D | T1 | `t9_cielo_drive_estate_night`, `pan` | *Hắn không hề có mặt tại căn nhà của Sharon Tate vào đêm mùng 8 tháng 8.* → `#3`: *Tại nhà LaBianca vào đêm hôm sau, hắn rời đi trước khi các đệ tử ra tay.* | — | — |  |
| 4-29 | `4.08#4` (6,9 s) | D | T1 | `t9_mastermind_conspiracy_law_book`, `pull` | *Luật sư bào chữa lập luận rằng Manson không thể bị kết tội giết người vì bàn tay hắn chưa từng chạm vào hung khí.* | — | — |  |
| 4-30 | `4.08#5` (6,4 s) | D | T1 | `t9_prosecutor_desk_evidence_files`, `still` | *Bằng lập luận đanh thép và chứng cứ logic phi thường, Công tố viên Bugliosi đã xây dựng thành công một học thuyết pháp lý kinh điển.* | — | — |  |
| 4-31 | `4.08#6` (6,5 s) | D | T1 | `t9_mastermind_conspiracy_law_book`, `push` | *Đó là học thuyết về Trách nhiệm của kẻ chủ mưu trong âm mưu giết người (Conspiracy and Vicarious Liability).* | — | — |  |
| 4-32 | `4.08#7` (9,1 s) | D | T1 | `t9_interlocking_knots_rope`, `pan` | *Ông chứng minh trước bồi thẩm đoàn rằng: các đệ tử chỉ là những cánh tay nối dài, còn bộ não điều khiển và ý chí tội ác duy nhất thuộc về Charles Manson.* | — | — |  |
| 4-33 | `4.08#8` (5,6 s) | D | T1 | `t9_shadow_devil_dialogue_noir`, `pull` | *Dù không trực tiếp ra tay, mọi hành động tàn bạo đều bắt nguồn từ chính mệnh lệnh tuyệt đối của hắn.* | — | →C |  |
| 4-34 | `4.09#1` (7,8 s) | C | T1 | `t9_dark_triad_psychological_symbol`, `still` | *Tại phiên tòa năm 1970, thái độ của các bị cáo là biểu hiện kinh điển của cơ chế Hoang tưởng Chia sẻ và sự phủ nhận cực đoan.* | — | — |  |
| 4-35 | `4.09#2` (9,8 s) | C | T1 | `t9_carved_x_symbol_forehead`, `push` | *Manson tự khắc một chữ X lên trán và tuyên bố đã gạch tên mình ra khỏi xã hội loài người; các nữ bị cáo cũng khắc chữ X tương tự, nắm tay nhau cười cợt bước vào phòng xử.* | — | — |  |
| 4-36 | `4.09#3` (7,0 s) | C | T1 | `t9_collective_hysteria_three_shaved_heads`, `pan` | *Nụ cười ấy là chiếc khiên tâm lý tuyệt vọng để trốn tránh việc phải nhìn thẳng vào sự thật rằng mình đã trở thành những kẻ sát nhân man rợ.* | — | — |  |
| 4-37 | `4.09#4` (7,9 s) | C | T1 | `t9_prison_cell_bars_shadow`, `pull` | *Nhưng sự chuyển biến tâm lý thực sự bắt đầu khi bản án giáng xuống và họ bị cách ly vật lý hoàn toàn khỏi Manson trong các xà lim biệt giam.* | — | — |  |
| 4-38 | `4.09#5` (11,6 s) | C | T1 | `t9_shadow_devil_dialogue_noir`, `still` | *Khi không còn ma túy và áp lực bầy đàn, lớp sương mù nhận thức tan rã, để lộ ra hiện thực trần trụi: Helter Skelter chỉ là trò lừa bịp và bàn tay họ đã tước đoạt sinh mạng của những con người vô tội.* | — | — |  |
| 4-39 | `4.09#6` (4,6 s) | C | T1 | `t9_redflag3_fortress_paranoia_wall`, `push` | *Hiện tượng Chấn thương Đạo đức bùng nổ, kéo theo cơn bão tự ghê tởm bản thân tột cùng.* | — | — |  |
| 4-40 | `4.09#7` (10,5 s) | C | T1 | `t9_scales_of_justice_broken_chains`, `pan` | *Leslie Van Houten và Patricia Krenwinkel sau đó đã trải qua hàng chục năm dằn vặt lương tâm* → *không còn đổ lỗi cho Manson và chấp nhận sự trừng phạt như một phần quả báo.* | ở "không còn đổ lỗi cho" | — |  |
| 4-41 | `4.09#8` (7,2 s) | C | T1 | `t9_two_faced_benevolent_mask`, `pull` | *Sự hối hận của họ là một sự ăn năn chân thực nhưng mang tính nhị nguyên đầy giằng xé với bản năng khao khát tự do của một sinh thể.* | — | — |  |
| 4-42 | `4.09#9` (12,4 s) | C | T1 | `t9_vacant_eyes_doll_shadow`, `still` | *Trái ngược hoàn toàn, kẻ cầm đầu Charles Manson chưa từng một lần hối hận; cấu trúc Ái kỷ Ác tính khiến hắn chỉ biết chìm đắm trong Sự Tự thương hại Bệnh lý, than thở mình là nạn nhân của xã hội cho đến tận lúc qua đời.* | — | →H |  |
| 4-43 | `4.10#1` (5,9 s) | H | T1 | `t9_scales_of_justice_broken_chains`, `push` | *Mọi trò hề và sự thao túng ma quái cuối cùng cũng không thể che mờ được ánh sáng của công lý.* | — | — |  |
| 4-44 | `4.10#2` (12,9 s) | H | T1 | `t9_courtroom_jury_verdict_dossier`, `pan` | *Ngày 25 tháng 1 năm 1971, sau nhiều tháng xét xử căng thẳng, bồi thẩm đoàn đã đưa ra phán quyết lịch sử kết tội Manson và ba nữ đồng phạm.* | — | — |  |
| 4-45 | `4.10#3` (8,0 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `pull` | *Bức màn đen tối che phủ Mùa hè Tình yêu chính thức bị pháp luật bóc trần.* | — | — |  |
| 4-46 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 05* · **PHÁN QUYẾT LỊCH SỬ & BÀI HỌC** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT LỊCH SỬ & BÀI HỌC

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (11,9 s) | H | T1 | `t9_courtroom_jury_verdict_dossier`, `push` | *Tháng 3 năm 1971, Charles Manson, Susan Atkins, Patricia Krenwinkel và Leslie Van Houten bị tuyên án tử hình.* | — | — |  |
| 5-02 | `5.02#2` (11,0 s) | H | T1 | `t9_california_supreme_court_columns`, `pan` | *Tuy nhiên, vào năm 1972, Tòa án Tối cao bang California tạm thời bãi bỏ án tử hình trong phán quyết lịch sử vụ People kiện Anderson.* | — | — |  |
| 5-03 | `5.02#3` (7,5 s) | H | T1 | `t9_corcoran_state_prison_watchtower`, `pull` | *Toàn bộ các bản án tử hình của Manson và đồng phạm tự động được chuyển thành tù chung thân có cơ hội ân xá.* | — | — |  |
| 5-04 | `5.02#4` (9,1 s) | H | T1 | `t9_corcoran_state_prison_watchtower`, `still` | *Nhưng trong suốt gần nửa thế kỷ sau đó, qua hàng chục phiên điều trần, mọi lá đơn xin ân xá của Charles Manson đều bị bác bỏ thẳng thừng.* | — | — |  |
| 5-05 | `5.02#5` (8,7 s) | H | T1 | `t9_scales_of_justice_broken_chains`, `push` | *Hội đồng ân xá luôn giữ vững lập trường trước nỗi đau chưa từng nguôi ngoai của gia đình các nạn nhân.* | — | →D |  |
| 5-06 | `5.04#1` (9,7 s) | D | T1 | `t9_mastermind_conspiracy_law_book`, `pan` | *Vụ án Manson đã xác lập một tiền lệ tư pháp bất hủ trong nền pháp lý hiện đại: Kẻ chủ mưu thao túng tâm trí phải chịu trách nhiệm hình sự ngang bằng với kẻ trực tiếp ra tay.* | — | — |  |
| 5-07 | `5.04#2` (8,2 s) | D | T1 | `t9_california_supreme_court_columns`, `pull` | *Đồng thời, sự kiên cường của bà Doris Tate – mẹ của Sharon Tate – đã tạo nên một bước ngoặt lịch sử cho nền tư pháp nhân văn.* | — | — |  |
| 5-08 | `5.04#3` (10,9 s) | D | T1 | `t9_prosecutor_desk_evidence_files`, `still` | *Bà đã thu thập hơn ba trăm năm mươi nghìn chữ ký, khởi xướng Phong trào Quyền Nạn nhân tại California dẫn tới việc thông qua Đạo luật Quyền của Nạn nhân năm 1982.* | — | — |  |
| 5-09 | `5.04#4` (8,6 s) | D | T1 | `t9_scales_of_justice_broken_chains`, `push` | *Lần đầu tiên trong lịch sử, thân nhân người bị hại được quyền cất lên tiếng nói trực tiếp trước các phiên xét ân xá để bảo vệ phẩm giá cho người đã khuất.* | — | — |  |
| 5-10 | `5.04#5` (12,8 s) | D | T1 | `t9_corcoran_state_prison_watchtower`, `pan` | *Còn với Charles Manson, hắn đã trải qua phần đời còn lại trong các nhà tù nghiêm ngặt nhất của bang California và qua đời vì bệnh tật vào ngày 19 tháng 11 năm 2017 ở tuổi tám mươi ba.* | — | — |  |
| 5-11 | `5.04#6` (7,0 s) | D | T1 | `t9_withered_flower_on_asphalt`, `pull` | *Hắn kết thúc cuộc đời trong sự cô độc tuyệt đối sau song sắt, để lại sau lưng một vết nhơ không thể gột rửa trong lịch sử nước Mỹ.* | — | →C |  |
| 5-12 | `5.05#1` (7,5 s) | C | T1 | `t9_courtroom_jury_verdict_dossier`, `still` | *Về mặt tâm lý học, bản án khắc nghiệt nhất đối với Charles Manson không chỉ là bốn bức tường giam cầm thể xác, mà là sự lãng quên của xã hội.* | — | — |  |
| 5-13 | `5.05#2` (7,5 s) | C | T1 | `t9_recording_studio_rejected_demo`, `push` | *Cho đến những ngày tháng cuối đời, Manson vẫn điên cuồng tìm cách trả lời phỏng vấn báo chí để thỏa mãn cơn khát sự chú ý.* | — | — |  |
| 5-14 | `5.05#3` (4,7 s) | C | T1 | `t9_two_faced_benevolent_mask`, `pan` | *Đó là biểu hiện trơ trọi của Sự tự thương hại bệnh lý khi nhận ra bản ngã ái kỷ đã hoàn toàn sụp đổ.* | — | — |  |
| 5-15 | `5.05#4` (13,5 s) | C | T1 | `t9_open_birdcage_dawn_horizon`, `pull` | *Trong khi đó, Leslie Van Houten sau hơn năm mươi năm cải tạo và đối diện với Chấn thương Đạo đức đã được ân xá vào tháng 7 năm 2023 ở tuổi bảy mươi ba* → *khép lại một bi kịch đời người đầy ám ảnh.* | ở "khép lại một bi kịch" | — |  |
| 5-16 | `5.05#5` (9,8 s) | C | T1 | `t9_redflag3_fortress_paranoia_wall`, `still` | *Thảm kịch này nhắc nhở chúng ta: Khi con người rơi vào trạng thái cô đơn và khủng hoảng ý nghĩa sống, chúng ta rất dễ trở thành con mồi cho những kẻ thao túng nhân danh tình yêu thương.* | — | — |  |
| 5-17 | `5.05#6` (3,5 s) | C | T1 | `t9_two_faced_benevolent_mask`, `push` | *Kẻ săn mồi tâm lý không bao giờ xuất hiện với cặp sừng của ác quỷ.* | — | — |  |
| 5-18 | `5.05#7` (3,2 s) | C | T1 | `t9_two_faced_benevolent_mask`, `pan` | *Chúng luôn khoác lên mình chiếc áo của người thấu hiểu và sẻ chia.* | — | →H |  |
| 5-19 | `5.07#1` (14,1 s) | H | T1 | `t9_amber_eyes_closing_dossier`, `pull` | *Để bảo vệ bản thân và những người thân yêu trước những chiếc bẫy thao túng tâm lý độc hại thời hiện đại, kênh Amber eyes xin đúc kết bốn tín hiệu cảnh báo đỏ sinh tồn từ nguyên lý “The Gift of Fear”:* | — | — |  |
| 5-20 | `5.07#2` (6,7 s) | H | T8 cờ | `t9_redflag1_love_bombing_trap`, `still` | *01* · **CẢNH BÁO ĐỎ THỨ NHẤT: CẢNH GIÁC TRƯỚC CHIẾN THUẬT DỘI BOM TÌNH CẢM DỒN DẬP.** | — | — |  |
| 5-21 | `5.07#3` (11,3 s) | H | T1 | `t9_unfreezing_love_bombing_circle`, `push` | *Bất kỳ cá nhân hay hội nhóm nào tán dương bạn quá mức ngay lần đầu gặp gỡ và thúc ép bạn gắn kết thần tốc đều đang tìm cách vô hiệu hóa trực giác phòng vệ của bạn.* | — | — |  |
| 5-22 | `5.07#4` (5,4 s) | H | T8 cờ | `t9_redflag2_severed_family_photos`, `pan` | *02* · **CẢNH BÁO ĐỎ THỨ HAI: HÀNH VI CÔ LẬP XÃ HỘI VÀ TƯỚC ĐOẠT RANH GIỚI RIÊNG TƯ.** | — | — |  |
| 5-23 | `5.07#5` (11,8 s) | H | T1 | `t9_burning_id_cards_ashes`, `pull` | *Hãy lập tức thoái lui nếu ai đó yêu cầu bạn cắt đứt quan hệ với gia đình, từ bỏ bạn bè thân thiết, thay đổi danh tính cá nhân hoặc bàn giao tài chính để chứng minh sự tận tụy.* | — | — |  |
| 5-24 | `5.07#6` (5,8 s) | H | T8 cờ | `t9_redflag3_fortress_paranoia_wall`, `still` | *03* · **CẢNH BÁO ĐỎ THỨ BA: TƯ DUY PHÂN CỰC NHỊ NGUYÊN THÙ ĐỊCH.** | — | — |  |
| 5-25 | `5.07#7` (12,2 s) | H | T1 | `t9_redflag3_fortress_paranoia_wall`, `push` | *Những tổ chức độc hại luôn gieo rắc nỗi sợ về một thế giới bên ngoài đầy nguy hiểm, tự tôn mình là nơi trú ẩn duy nhất để giam lỏng nhận thức của bạn trong chiếc lồng bầy đàn.* | — | — |  |
| 5-26 | `5.07#8` (5,1 s) | H | T8 cờ | `t9_redflag4_sacred_conscience_compass`, `pan` | *04* · **CẢNH BÁO ĐỎ THỨ TƯ: TUYỆT ĐỐI KHÔNG BAO GIỜ TRAO QUYỀN PHÁN XÉT LƯƠNG TRI CHO KẺ KHÁC.** | — | — |  |
| 5-27 | `5.07#9` (12,4 s) | H | T1 | `t9_redflag4_sacred_conscience_compass`, `pull` | *Khi một thủ lĩnh tự xưng yêu cầu bạn làm những điều trái với pháp luật hoặc đạo đức lương tâm nhân danh một mục đích cao cả, đó chính là bước chân đầu tiên dẫn xuống vực thẳm tha hóa.* | — | — |  |
| 5-28 | `5.07#10` (9,8 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `still` | *Luôn tin vào trực giác mách bảo của bạn – bởi cảm giác bất an mơ hồ chính là món quà tiến hóa vô giá giúp bảo vệ sự an toàn của sinh mệnh.* | — | — |  |
| 5-29 | `5.09#1` (7,0 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `push` | *Tự do đích thực không nằm ở việc trốn chạy thực tại hay trao số phận mình cho một vị cứu tinh giả tạo.* | — | — |  |
| 5-30 | `5.09#2` (8,3 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `pan` | *Tự do nằm ở năng lực làm chủ tư duy, gìn giữ bản sắc cá nhân và lòng dũng cảm chịu trách nhiệm cho từng hành vi của chính mình.* | — | — |  |
| 5-31 | `5.09#3` (8,8 s) | H | T1 | `t9_amber_eyes_closing_dossier`, `pull` | *Cảm ơn các chuyên gia đã đồng hành bóc tách hồ sơ lịch sử đầy ám ảnh ngày hôm nay, và cảm ơn quý vị khán giả đã lắng nghe đến những phút cuối cùng.* | — | — |  |
| 5-32 | `5.09#4` (13,3 s) | H | T1 | `t9_amber_eyes_closing_dossier`, `still` | *Hãy luôn giữ cho mình một tâm trí tỉnh táo, biết lắng nghe trực giác và trân trọng sự bình yên của cuộc sống; xin chào và hẹn gặp lại quý vị trong những hồ sơ tiếp theo.* | — | — |  |
| 5-33 | hết tập (0,0 s) | — | T2 | `t9_amber_eyes_closing_dossier`, `still` | **HỒ SƠ TẬP 09 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | — | ⊘ | ◼ |

**Tổng:** 192 dòng · 199 câu · 5 hồi · nền dùng 65 loại (MiniMax, 09/11/2026). Bảng viết lại 09/11/2026 theo kịch bản viết lại (199 câu). Thời lượng shot lấy từ timeline **neo master mp3** (VN, đo thật); EN/JA là **ước lượng** theo hệ số neo Tập 08 (sai số 0,000%) ⇒ khi có audio thật phải dựng lại timeline và render lại ảnh (T20/H14). 12 câu ngắn được gom với câu kế trong cùng element để đạt H10 (≥ 3 s); 1 câu dài hơn 15 s (2.10#2) được tách chữ trên hình thành 2 đoạn + beat (A7).
