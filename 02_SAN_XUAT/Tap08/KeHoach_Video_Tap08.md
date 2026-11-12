# HỒ SƠ SẢN XUẤT TẬP 08 · "KHI CÁC THIÊN TÀI BỊ TẨY NÃO"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 08: Khi Các Thiên Tái Bị Tẩy Não** |
| Vụ án | Giáo phái Aum Shinrikyo & Vụ tấn công khí độc tàu điện ngầm Tokyo (Tokyo, Nhật Bản, 1995) |
| Chủ đề | Thao túng tâm lý giáo phái, Sự trống rỗng hiện sinh, Kỹ thuật làm suy kiệt thần kinh, Nghịch lý trí thức tinh hoa |
| Tổng thời lượng | **1957,51 s (32:37)** · 5 hồi · **218 câu thoại** · 53 phần tử kịch bản — timeline **neo master mp3 thật** (`02_SAN_XUAT/Tap08/xuat_ban/Tap08_master.mp3`, dựng 09/11/2026 08:05) · 223 shot (218 nội dung + 4 thẻ chuyển hồi + 1 thẻ kết) |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Hành khách Tokyo) · N2 (Bác sĩ Ikuo Hayashi) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D3_SH.wav`, C: `C2_AB03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap08.json`) |
| Thành phẩm Master | ✅ **ĐÃ DỰNG LẠI 09/11/2026 08:05** — `02_SAN_XUAT/Tap08/xuat_ban/Tap08_master.mp3` (**1957,51 s / 32:37**) cho **218 câu**. Timeline `.work/timeline_s_t08.json` đã neo master này (tổng khớp 0,000 s); mốc từng câu là ước lượng theo ký tự — xem `02_SAN_XUAT/Tap08/BaoCao_QC_Tap08_20261109.md` §6 |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **$-16.2\text{ LUFS}$** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **$-1.6\text{ dBFS}$** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** **$3.3\text{ LU}$**
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **$124.0\text{ Hz}$** ($n=94$)
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **$86.4\text{ Hz}$** ($n=26$)
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **$208.2\text{ Hz}$** ($n=24$)
- **Nhân chứng ($N1$ · Thỏ tuyết):** F0 trung vị = **$180.8\text{ Hz}$** ($n=6$)
- **Lời khai ($N2$ · Gấu trúc):** F0 trung vị = **$278.3\text{ Hz}$** ($n=4$)
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = 12 \log_2(124.0 / 86.4) = \mathbf{6.26\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = 12 \log_2(208.2 / 124.0) = \mathbf{8.97\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **$9.75\%$** (CER trung bình: $10.98\%$, chủ yếu do từ vựng địa danh tiếng Nhật: *Kasumigaseki*, *Chiyoda*, *Marunouchi*, *Hibiya* và các biến thể dấu thanh của Whisper Base trên tiếng Việt).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **$2.56 / 5.0$** (Dải điểm: $1.51 - 3.44$).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap08/xuat_ban/Tap08_master.mp3`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/Tap08_master.mp3) (25.43 MB)
   - WAV: [`.work/audio_master_t08.wav`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/audio_master_t08.wav) (203.40 MB, 48 kHz 24-bit stereo)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t08.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/timeline_s_t08.json) — **1957,51 s (32:37)** · **đã neo master mp3 thật** (`.work/_t08/_t08_build_timeline.py`, tổng khớp 0,000 s); mốc từng câu là ước lượng theo ký tự (mục `_estimated`)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap08/xuat_ban/Tap08.srt`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/Tap08.srt) — ⛔ **CŨ (278 cue, lời bản 154 câu)**; phải sinh lại từ timeline 218 câu khi đóng gói
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep08_vi.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/quality_qc_utmos_ep08_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md)

## 6. DANH SÁCH SHOT — TẬP 08 (viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### HỒI 1 — BUỔI SÁNG ĐỊNH MỆNH DƯỚI LÒNG ĐẤT TOKYO · nền chủ đạo `t8_tokyo_dawn_fog`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.02#1` (9,5 s) | H | T1 | `t8_tokyo_dawn_fog`, `pan` | *Vào sáng thứ Hai, ngày 20 tháng 3 năm 1995, thủ đô Tokyo của Nhật Bản thức dậy trong nhịp sống hối hả thường nhật.* | — | ✦ Cú |  |
| 1-02 | `1.02#2` (6,2 s) | H | T1 | `t8_commuter_crowd_station`, `pull` | *Hàng triệu người dân đổ dồn về hệ thống tàu điện ngầm dưới lòng đất để bắt đầu tuần làm việc mới.* | — | — |  |
| 1-03 | `1.02#3` (10,1 s) | H | T1 | `t8_tokyo_stock_crash_1990`, `still` | *Nước Nhật khi ấy đang chao đảo sau cú sốc sụp đổ của nền kinh tế bong bóng năm 1991, mở ra cái gọi là Thập niên mất mát đầy âu lo.* | — | — |  |
| 1-04 | `1.02#4` (3,7 s) | H | T1 | `t8_subway_tracks_perspective`, `push` | *Đúng tám giờ sáng, giờ cao điểm đông đúc nhất trong ngày.* | — | — |  |
| 1-05 | `1.02#5` (8,3 s) | H | T1 | `t8_subway_tracks_perspective`, `pan` | *Năm chuyến tàu điện ngầm trên ba tuyến huyết mạch Chiyoda, Marunouchi và Hibiya đang cùng lao vun vút về phía nhà ga Kasumigaseki.* | — | — |  |
| 1-06 | `1.02#6` (8,7 s) | H | T1 | `t8_tokyo_stock_crash_1990`, `pull` | *Nơi đây đặt trụ sở của các Bộ ngành trọng yếu và Cơ quan Cảnh sát Quốc gia, được coi là trái tim hành chính quyền lực nhất của đất nước.* | — | — |  |
| 1-07 | `1.02#7` (6,7 s) | H | T1 | `t8_kasumigaseki_facade`, `still` | *Nhật Bản khi ấy vẫn tự hào với “huyền thoại an toàn”, một xã hội có tỷ lệ tội phạm thấp bậc nhất thế giới.* | — | — |  |
| 1-08 | `1.02#8` (7,4 s) | H | T1 | `t8_corporate_salaryman_cogs`, `push` | *Dưới vẻ ngoài hào nhoáng và kỷ luật thép của trật tự công cộng, những vết rạn nứt tâm lý âm ỉ đang chờ dịp bùng nổ.* | — | — |  |
| 1-09 | `1.04#1` (7,8 s) | H | T1 | `t8_chemical_structure_sarin`, `pan` | *Thế nhưng, trên mỗi chuyến tàu ấy, có những người đàn ông mang theo một thứ chất độc thần kinh có sức tàn phá khủng khiếp.* | — | — |  |
| 1-10 | `1.04#2` (6,4 s) | H | T1 | `t8_umbrella_puncture_action`, `pull` | *Họ dùng đầu ô đã mài nhọn đâm thủng các túi ni-lông chứa chất lỏng chết người ngay trên sàn toa xe.* | — | — |  |
| 1-11 | `1.04#3` (9,2 s) | H | T1 | `t8_newspaper_wrapped_package`, `still` | *Năm kẻ khủng bố được trang bị tổng cộng mười một túi chất lỏng chứa sarin, bọc kín bên ngoài bằng các trang báo hàng ngày để ngụy trang hoàn hảo.* | — | — |  |
| 1-12 | `1.04#4` (8,6 s) | H | T1 | `t8_newspaper_wrapped_package`, `push` | *Khi cửa tàu vừa mở tại các nhà ga đông đúc, những kẻ này nhanh chóng bước ra ngoài, để lại luồng hơi độc bốc lên âm thầm giữa đám đông.* | — | — |  |
| 1-13 | `1.04#5` (4,6 s) | H | T1 | `t8_train_doors_closing`, `pan` | *Một cuộc tấn công phối hợp tàn bạo nhắm thẳng vào các công dân vô tội.* | — | — |  |
| 1-14 | `1.06#1` (8,2 s) | H | T1 | `t8_subway_car_mist_vapor`, `pull` | *Chỉ trong vài phút ngắn ngủi, một cơn ác mộng chưa từng có trong lịch sử Nhật Bản thời hậu chiến đã bùng nổ dưới lòng đất Tokyo.* | — | — |  |
| 1-15 | `1.06#2` (8,3 s) | H | T1 | `t8_hospital_triage_corridor`, `still` | *Chất lỏng bay hơi nhanh chóng trong các toa tàu đóng kín cửa, biến không gian di chuyển thường nhật thành một chiếc bẫy nghẹt thở.* | — | — |  |
| 1-16 | `1.06#3` (4,4 s) | H | T1 | `t8_ambulances_tokyo_street`, `push` | *Hãy hình dung những gì một hành khách trên tàu khi ấy phải trải qua.* | — | →N1 |  |
| 1-17 | `1.07#1` (6,5 s) | N1 | T4 lời kể | `t8_dropped_novel_glasses`, `pan` | *Tôi đang đứng đọc sách trên tàu thì ngửi thấy một mùi hắc nhẹ rất lạ, giống như mùi dung môi pha sơn.* | — | ✦ Cừu |  |
| 1-18 | `1.07#2` (6,8 s) | N1 | T4 lời kể | `t8_subway_platform_tunnel_dark`, `pull` | *Đột nhiên, mắt tôi bắt đầu cay xè và mọi thứ xung quanh tối sầm lại như có ai đó vừa tắt toàn bộ bóng đèn.* | — | — |  |
| 1-19 | `1.07#3` (6,5 s) | N1 | T4 lời kể | `t8_dropped_novel_glasses`, `still` | *Tôi thấy ngực mình nghẹt thở, và mọi người xung quanh bắt đầu ho dữ dội rồi hoảng loạn tìm lối thoát.* | — | — |  |
| 1-20 | `1.07#4` (8,6 s) | N1 | T4 lời kể | `t8_subway_stairs_escape`, `push` | *Tôi thấy những nhân viên nhà ga lao vào giúp đỡ hành khách rồi chính họ cũng lảo đảo ngã quỵ vì không hề biết thứ vô hình đang bủa vây.* | — | — |  |
| 1-21 | `1.07#5` (4,9 s) | N1 | T4 lời kể | `t8_commuter_crowd_station`, `pan` | *Không ai hiểu chuyện gì đang xảy ra, và sự kinh hoàng bao trùm khắp sân ga.* | — | — |  |
| 1-22 | `1.07#6` (5,0 s) | N1 | T4 lời kể | `t8_subway_tracks_perspective`, `pull` | *Cảm giác lúc đó cứ như ngày tận thế vừa ập xuống đầu chúng tôi giữa ban ngày.* | — | →H |  |
| 1-23 | `1.09#1` (8,5 s) | H | T1 | `t8_ambulances_tokyo_street`, `still` | *Vụ tấn công hóa học đã cướp đi sinh mạng của mười bốn thường dân vô tội và làm tổn hại sức khỏe của hơn năm nghìn tám trăm người khác.* | — | — |  |
| 1-24 | `1.09#2` (12,1 s) | H | T1 | `t8_hospital_triage_corridor`, `push` | *Hai nhân viên đường sắt quả cảm, ông Kazumasa Takahashi và ông Tsuneo Hishinuma, đã dũng cảm dùng tay không di chuyển các túi chất độc ra khỏi toa xe để bảo vệ hành khách và anh dũng hy sinh.* | — | — |  |
| 1-25 | `1.09#3` (12,2 s) | H | T1 | `t8_hospital_triage_corridor`, `pan` | *Tại Bệnh viện Quốc tế Saint Luke, Bác sĩ Shigeaki Hinohara đã lập tức ra lệnh chuyển đổi toàn bộ sảnh lớn thành trạm cấp cứu dã chiến để tiếp nhận hàng trăm nạn nhân trong tình trạng nguy kịch.* | — | — |  |
| 1-26 | `1.09#4` (6,8 s) | H | T1 | `t8_tokyo_police_hq`, `pull` | *Hàng nghìn người phải chịu đựng những di chứng tâm lý nặng nề và nỗi sợ hãi kéo dài suốt phần đời còn lại.* | — | — |  |
| 1-27 | `1.09#5` (8,7 s) | H | T1 | `t8_incident_board_map`, `still` | *Cơn hoang tưởng tập thể bùng phát khắp thủ đô: người dân Tokyo nín thở khi bước xuống ga ngầm, kiểm tra từng gầm ghế và nghi kỵ lẫn nhau.* | — | — |  |
| 1-28 | `1.09#6` (5,7 s) | H | T1 | `t8_ambulances_tokyo_street`, `push` | *Toàn bộ hệ thống giao thông và y tế của siêu đô thị rơi vào tình trạng tê liệt khẩn cấp.* | — | →D |  |
| 1-29 | `1.11#1` (11,0 s) | D | T1 | `t8_tokyo_police_hq`, `pan` | *Ngay sau khi tiếp nhận thông tin về vụ rải khí độc tại ga Kasumigaseki, Cơ quan Cảnh sát Quốc gia Nhật Bản đã xác định đây là một cuộc tấn công khủng bố phối hợp quy mô lớn.* | — | ✦ Sói |  |
| 1-30 | `1.11#2` (8,9 s) | D | T1 | `t8_incident_board_map`, `pull` | *Mục tiêu của chúng là nhắm thẳng vào các tuyến tàu đi qua khu vực cơ quan đầu não của chính phủ nhằm làm tê liệt bộ máy điều hành đất nước.* | — | — |  |
| 1-31 | `1.11#3` (6,9 s) | D | T1 | `t8_chemical_structure_sarin`, `still` | *Phương thức gây án được tính toán tinh vi với năm kẻ tấn công đồng loạt ra tay vào đúng khung giờ cao điểm.* | — | — |  |
| 1-32 | `1.11#4` (7,2 s) | D | T1 | `t8_aum_shinrikyo_emblem_shadow`, `push` | *Hóa chất được sử dụng là sarin, một loại khí độc thần kinh nhân tạo cực kỳ nguy hiểm và phức tạp trong tổng hợp.* | — | — |  |
| 1-33 | `1.11#5` (9,9 s) | D | T1 | `t8_dossier_elite_scientists`, `pan` | *Sarin là một hợp chất cực độc được các nhà khoa học quân sự Đức tổng hợp từ năm 1938, với độc tính cao gấp hàng trăm lần xyanua.* | — | — |  |
| 1-34 | `1.11#6` (9,6 s) | D | T1 | `t8_chemical_plant_reactor`, `pull` | *Để điều chế được hàng chục lít sarin với độ tinh khiết cao như vậy, kẻ đứng sau bắt buộc phải có một cơ sở công nghiệp và nguồn lực tài chính khổng lồ.* | — | — |  |
| 1-35 | `1.11#7` (7,1 s) | D | T1 | `t8_tokyo_police_hq`, `still` | *Mọi dấu vết tại hiện trường đều nhanh chóng chỉ về một tổ chức tôn giáo bí ẩn mang tên Giáo phái Aum Shinrikyo.* | — | →H |  |
| 1-36 | `1.12#1` (6,0 s) | H | T1 | `t8_dossier_elite_scientists`, `push` | *Nhưng điều khiến toàn bộ thế giới bàng hoàng không chỉ dừng lại ở sự tàn độc của vụ tấn công.* | — | — |  |
| 1-37 | `1.12#2` (8,2 s) | H | T1 | `t8_kasumigaseki_facade`, `pan` | *Khi danh tính thực sự của những kẻ chế tạo và rải chất độc dần lộ diện, một nghịch lý rúng động đã phơi bày trước mắt công chúng.* | — | — |  |
| 1-38 | `1.12#3` (6,5 s) | H | T1 | `t8_broken_hippocratic_oath`, `pull` | *Kẻ thực hiện không phải là một tổ chức quân sự ngoại quốc hay những tên tội phạm đường phố liều lĩnh.* | — | — |  |
| 1-39 | `1.12#4` (6,5 s) | H | T1 | `t8_intellectual_hubris_chess`, `still` | *Đứng sau thảm kịch ấy là những nhà khoa học, bác sĩ và trí thức tinh hoa của chính đất nước Nhật Bản.* | — | — |  |
| 1-40 | `1.12#5` (9,0 s) | H | T1 | `t8_cosmic_physics_observatory`, `push` | *Chính vị thế học thức đỉnh cao ấy đã tạo nên một “Hiệu ứng Hào quang” chết người, che mắt toàn bộ xã hội và cơ quan an ninh suốt nhiều năm dài.* | — | — |  |
| 1-41 | `1.12#6` (8,4 s) | H | T1 | `t8_dossier_elite_scientists`, `pan` | *Một điểm mù xã hội chết người đã hình thành khi niềm tin ngây thơ vào giới tinh hoa che lấp đi những dấu hiệu cảnh báo rõ ràng nhất.* | — | — |  |
| 1-42 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ** | — | ⊘ | ◼ |

### HỒI 2 — KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ · nền chủ đạo `t8_mount_fuji_dawn_somber`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (8,7 s) | H | T1 | `t8_mount_fuji_dawn_somber`, `pull` | *Sáng sớm ngày 22 tháng 3 năm 1995, đúng hai ngày sau vụ tấn công kinh hoàng dưới lòng đất Tokyo.* | — | — |  |
| 2-02 | `2.02#2` (5,6 s) | H | T1 | `t8_hazmat_officers_formation`, `still` | *Hơn một nghìn sĩ quan cảnh sát và đặc nhiệm phòng hóa Nhật Bản đã đồng loạt xuất kích.* | — | — |  |
| 2-03 | `2.02#3` (3,9 s) | H | T1 | `t8_police_convoy_kamikuishiki`, `push` | *Họ trang bị mặt nạ phòng độc và bình dưỡng khí chuyên dụng.* | — | — |  |
| 2-04 | `2.02#4` (7,5 s) | H | T1 | `t8_police_convoy_kamikuishiki`, `pan` | *Đoàn xe tiến thẳng vào khu căn cứ khổng lồ của giáo phái Aum tại làng Kamikuishiki, nằm biệt lập dưới chân núi Phú Sĩ.* | — | — |  |
| 2-05 | `2.02#5` (8,5 s) | H | T1 | `t8_asahara_empty_dock`, `pull` | *Sự u ám, hoang tàn của những dãy nhà xưởng biệt lập này tạo nên một sự tương phản rùng mình với vẻ đẹp thanh bình của ngọn núi thiêng.* | — | — |  |
| 2-06 | `2.02#6` (6,2 s) | H | T1 | `t8_satyam_compound_aerial`, `still` | *Một cuộc khám xét quy mô chưa từng có trong lịch sử thực thi pháp luật của đất nước mặt trời mọc.* | — | →D |  |
| 2-07 | `2.04#1` (9,6 s) | D | T1 | `t8_satyam_compound_aerial`, `push` | *Khu liên hợp của giáo phái mang tên Satyam là một quần thể gồm hàng chục tòa nhà bê tông xám xịt được canh phòng cẩn mật bằng hệ thống camera giám sát.* | — | — |  |
| 2-08 | `2.04#2` (6,2 s) | D | T1 | `t8_satyam_7_exterior`, `pan` | *Bề ngoài khu căn cứ mang danh nghĩa là tu viện thiền định và xưởng sản xuất nông sản thanh tịnh.* | — | — |  |
| 2-09 | `2.04#3` (8,8 s) | D | T1 | `t8_satyam_7_exterior`, `pull` | *Nhưng khi cảnh sát tiến vào tòa nhà mang mã số Satyam số 7, tất cả các chuyên gia đều phải lạnh người trước những gì tận mắt chứng kiến.* | — | — |  |
| 2-10 | `2.04#4` (8,2 s) | D | T1 | `t8_chemical_precursor_drums`, `still` | *Bên trong không hề có tượng Phật hay không gian thờ tự, mà là một nhà máy sản xuất vũ khí hóa học quy mô công nghiệp hoàn chỉnh.* | — | — |  |
| 2-11 | `2.04#5` (10,3 s) | D | T1 | `t8_mi17_helicopter_hangar`, `push` | *Khu phức hợp hóa học này có giá trị ước tính lên tới hơn ba mươi triệu đô la Mỹ, được vận hành với hệ thống lọc khí áp suất âm hệt như một nhà máy vũ khí quân sự.* | — | — |  |
| 2-12 | `2.04#6` (7,6 s) | D | T1 | `t8_chemical_plant_reactor`, `pan` | *Cảnh sát thu giữ hàng chục tấn hóa chất tiền chất cùng dàn máy móc tổng hợp hữu cơ tối tân trị giá hàng triệu đô la Mỹ.* | — | — |  |
| 2-13 | `2.04#7` (8,3 s) | D | T1 | `t8_mi17_helicopter_hangar`, `pull` | *Thậm chí, giáo phái còn bí mật nhập khẩu một chiếc trực thăng quân sự Mi-17 từ nước ngoài và nuôi cấy cả vi khuẩn bệnh than.* | — | — |  |
| 2-14 | `2.04#8` (9,1 s) | D | T1 | `t8_tsukuba_chemistry_lab`, `still` | *Tài liệu thu giữ còn tiết lộ kế hoạch điên rồ mua trang trại rộng hàng trăm nghìn héc-ta tại Úc để thử nghiệm vũ khí và tìm kiếm quặng uranium.* | — | →H |  |
| 2-15 | `2.05#1` (8,7 s) | H | T1 | `t8_newspaper_wrapped_package`, `push` | *Về mặt nghiệp vụ, vụ tấn công ngày 20 tháng 3 đã phơi bày sự tách bạch rõ rệt giữa Thủ đoạn gây án và Chữ ký tâm lý của giáo phái.* | — | — |  |
| 2-16 | `2.05#2` (9,8 s) | H | T1 | `t8_aum_shinrikyo_emblem_shadow`, `pan` | *Thủ đoạn thực hiện được chuẩn bị kỹ lưỡng: dùng túi ni-lông hai lớp bọc giấy báo, dùi thủng bằng đầu ô và bố trí tài xế đợi sẵn trước cửa ga để tẩu thoát.* | — | — |  |
| 2-17 | `2.05#3` (8,3 s) | H | T1 | `t8_apocalypse_prophecy_scroll`, `pull` | *Thế nhưng, ngòi nổ tâm lý kích hoạt cuộc tấn công vào đúng thời điểm đó lại xuất phát từ một cơn hoảng loạn tột độ của kẻ cầm đầu.* | — | — |  |
| 2-18 | `2.05#4` (11,0 s) | H | T1 | `t8_iron_gate_closing`, `still` | *Giáo chủ Aum nhận được tin mật báo rằng cảnh sát sẽ tiến hành đại lục soát khu căn cứ Kamikuishiki vào ngày 22 tháng 3 vì vụ bắt cóc một công chứng viên tại Tokyo.* | — | — |  |
| 2-19 | `2.05#5` (10,4 s) | H | T1 | `t8_moral_rationalization_books`, `push` | *Nạn nhân bị giáo phái thủ tiêu trước đó là ông Kiyoshi Kariya, một công chứng viên dũng cảm đã kiên quyết bảo vệ em gái mình khỏi sự cưỡng đoạt tài sản của tổ chức.* | — | — |  |
| 2-20 | `2.05#6` (11,4 s) | H | T1 | `t8_police_convoy_kamikuishiki`, `pan` | *Để đối phó với nguy cơ bị vạch trần, giáo chủ đã ra lệnh phát động cuộc tấn công sarin chỉ trong vòng 48 giờ nhằm đánh lạc hướng điều tra và làm tê liệt đầu não cảnh sát.* | — | — |  |
| 2-21 | `2.05#7` (7,5 s) | H | T1 | `t8_newspaper_wrapped_package`, `pull` | *Còn Chữ ký tâm lý bất biến của hắn chính là nhu cầu cưỡng chế hiện thực hóa kịch bản ngày tận thế mà hắn đã tiên tri.* | — | — |  |
| 2-22 | `2.05#8` (8,6 s) | H | T1 | `t8_aum_shinrikyo_emblem_shadow`, `still` | *Ảo tưởng cứu thế và nỗi sợ hãi thực tại bị phơi bày đã hòa làm một, biến cuộc thảm sát thành công cụ tự vệ tuyệt vọng của kẻ cuồng tín.* | — | — |  |
| 2-23 | `2.05#9` (7,4 s) | H | T1 | `t8_apocalypse_prophecy_scroll`, `push` | *Hắn khao khát chứng minh cho các đệ tử thấy rằng dự ngôn chiến tranh thế giới thứ ba của mình đang thực sự diễn ra.* | — | →D |  |
| 2-24 | `2.07#1` (6,6 s) | D | T1 | `t8_matsumoto_night_1994`, `pan` | *Quá trình điều tra sau đó đã vạch trần quỹ đạo leo thang tội ác kéo dài suốt nhiều năm của tổ chức này:* | — | — |  |
| 2-25 | `2.07#2` (7,9 s) | D | T1 | `t8_yoga_meditation_incense`, `pull` | *Nấc thang thứ nhất: Khởi đầu từ một phòng tập yoga nhỏ và những màn biểu diễn bay bổng trên không để thu hút tín đồ nhẹ dạ.* | — | — |  |
| 2-26 | `2.07#3` (9,3 s) | D | T1 | `t8_sakamoto_lawyer_desk`, `still` | *Nấc thang thứ hai: Cưỡng đoạt toàn bộ tài sản, giam giữ các thành viên có ý định bỏ trốn và thủ tiêu những người bất đồng chính kiến trong nội bộ.* | — | — |  |
| 2-27 | `2.07#4` (10,3 s) | D | T1 | `t8_mountain_grave_memorial`, `push` | *Nấc thang thứ ba: Tàn sát cả gia đình Luật sư Tsutsumi Sakamoto vào năm 1989 khi ông đứng ra bảo vệ các gia đình nạn nhân bị lừa gạt.* | — | — |  |
| 2-28 | `2.07#5` (11,8 s) | D | T1 | `t8_mountain_grave_memorial`, `pan` | *Gia đình nạn nhân gồm người vợ Satoko và đứa con trai nhỏ Tatsuhiko mới mười bốn tháng tuổi đã bị … dã man ngay tại nhà riêng chỉ vì dám lên tiếng vạch trần bộ mặt thật của tổ chức.* | — | — |  |
| 2-29 | `2.07#6` (12,9 s) | D | T1 | `t8_police_convoy_kamikuishiki`, `pull` | *Nấc thang thứ tư: Vụ phát tán khí độc tại thành phố Matsumoto vào mùa hè năm 1994 khiến tám người thiệt mạng nhằm … các thẩm phán đang thụ lý vụ kiện chống lại giáo phái.* | — | — |  |
| 2-30 | `2.07#7` (10,5 s) | D | T1 | `t8_matsumoto_court_dossier`, `still` | *Tại Matsumoto, giáo phái đã sử dụng một xe tải cải tiến gắn quạt gió để phát tán khí độc vào ban đêm, tạo thành một vụ tập dượt quy mô lớn trước khi tấn công thủ đô.* | — | — |  |
| 2-31 | `2.07#8` (7,2 s) | D | T1 | `t8_matsumoto_night_1994`, `push` | *Chuỗi hành vi cho thấy mức độ bạo lực liên tục tăng tiến khi giáo phái ngày càng lún sâu vào ảo tưởng quyền lực.* | — | — |  |
| 2-32 | `2.07#9` (6,3 s) | D | T1 | `t8_sarin_synthesis_laboratory`, `pan` | *Và thảm kịch tàu điện ngầm Tokyo chính là điểm bùng nổ cuối cùng của quỹ đạo leo thang tàn bạo đó.* | — | — |  |
| 2-33 | `2.07#10` (7,9 s) | D | T1 | `t8_sakamoto_lawyer_desk`, `pull` | *Mỗi nấc thang tội ác bị bỏ lọt đã tiếp thêm sự ngạo mạn cho giáo phái, biến chúng thành một thực thể thách thức cả quốc gia.* | — | →H |  |
| 2-34 | `2.08#1` (7,0 s) | H | T1 | `t8_aum_shinrikyo_emblem_shadow`, `still` | *Một tổ chức tôn giáo tự xưng là mang lại sự giác ngộ tâm linh lại sở hữu cả một kho vũ khí hủy diệt hàng loạt.* | — | — |  |
| 2-35 | `2.08#2` (9,5 s) | H | T1 | `t8_moral_rationalization_books`, `push` | *Cơ chế dung nạp kích thích đã khiến ngưỡng thỏa mãn của giáo phái liên tục bị đẩy xa hơn, từ những trò lừa bịp nhỏ cho đến hành vi khủng bố tàn khốc.* | — | — |  |
| 2-36 | `2.08#3` (11,8 s) | H | T1 | `t8_weapons_of_mass_destruction`, `pan` | *Sự chậm trễ và lúng túng của chính quyền bắt nguồn từ việc luật pháp thời kỳ đó trao quyền tự do tôn giáo gần như tuyệt đối, tạo nên một tấm khiên bất khả xâm phạm cho các hoạt động ngầm.* | — | — |  |
| 2-37 | `2.08#4` (9,0 s) | H | T1 | `t8_devotion_altar_kneeling`, `pull` | *Làm thế nào một kẻ mù lòa từng bán thuốc giả lại có thể tập hợp và thao túng cả một đội ngũ trí thức xuất chúng để chế tạo cỗ máy tử thần ấy?* | — | — |  |
| 2-38 | `2.08#5` (6,7 s) | H | T1 | `t8_buddhist_mandala_distortion`, `still` | *Đằng sau bức màn thần thánh ấy là một mê cung thao túng tâm lý được tính toán đến từng chi tiết nhỏ nhất.* | — | — |  |
| 2-39 | `2.08#6` (5,1 s) | H | T1 | `t8_aum_shinrikyo_emblem_shadow`, `push` | *Câu trả lời nằm sâu trong những góc khuất tăm tối nhất của tâm lý học hành vi.* | — | — |  |
| 2-40 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC** | — | ⊘ | ◼ |

### HỒI 3 — NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC · nền chủ đạo `t8_asahara_shadow_profile`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (6,9 s) | H | T1 | `t8_asahara_shadow_profile`, `pan` | *Đứng đầu giáo phái Aum Shinrikyo là một người đàn ông mang tên Shoko Asahara, tên thật là Chizuo Matsumoto.* | — | — |  |
| 3-02 | `3.02#2` (9,0 s) | H | T1 | `t8_todai_red_gate_shadow`, `pull` | *Hắn sinh ra trong một gia đình nghèo đông con tại tỉnh Kumamoto, bị mù một mắt và mắt còn lại suy giảm thị lực nghiêm trọng do bệnh bẩm sinh.* | — | — |  |
| 3-03 | `3.02#3` (9,6 s) | H | T1 | `t8_chinese_herbal_apothecary`, `still` | *Bị gia đình gửi vào trường nội trú dành cho người mù từ khi còn nhỏ, Matsumoto lớn lên trong sự thiếu thốn tình thương và nỗi uất ức bị cô lập sâu sắc.* | — | — |  |
| 3-04 | `3.02#4` (5,8 s) | H | T1 | `t8_todai_red_gate_shadow`, `push` | *Thời trẻ, Matsumoto từng nhiều lần thi trượt kỳ thi tuyển sinh vào Đại học Tokyo danh giá.* | — | — |  |
| 3-05 | `3.02#5` (5,3 s) | H | T1 | `t8_chinese_herbal_apothecary`, `pan` | *Hắn từng mở phòng khám châm cứu và phải nhận án phạt vì buôn bán thuốc đông y giả.* | — | — |  |
| 3-06 | `3.02#6` (10,1 s) | H | T1 | `t8_devotion_altar_kneeling`, `pull` | *Mặc cảm tự ti về thể xác và thất bại học vấn đã kích hoạt cơ chế bù trừ tâm lý cực đoan, nung nấu trong hắn một khao khát điên cuồng về sự thống trị tuyệt đối.* | — | — |  |
| 3-07 | `3.02#7` (6,3 s) | H | T1 | `t8_matsumoto_court_dossier`, `still` | *Một kẻ có trình độ học vấn chắp vá, ngoại hình luộm thuộm và nhân cách mang đậm nét ái kỷ bệnh lý.* | — | — |  |
| 3-08 | `3.02#8` (6,9 s) | H | T1 | `t8_yoga_meditation_incense`, `push` | *Thế nhưng, quỳ gối dưới chân người đàn ông mù lòa ấy lại là những trí thức ưu tú nhất của đất nước Nhật Bản.* | — | — |  |
| 3-09 | `3.02#9` (6,9 s) | H | T1 | `t8_asahara_shadow_profile`, `pan` | *Họ sẵn sàng dâng hiến toàn bộ tài sản, lý trí và lương tâm của mình cho một kẻ từng bị xã hội khinh thường.* | — | →D |  |
| 3-10 | `3.03#1` (7,7 s) | D | T1 | `t8_dossier_elite_scientists`, `pull` | *Hồ sơ của ban lãnh đạo giáo phái Aum khiến bất kỳ ai cũng phải ngỡ ngàng trước hàm lượng chất xám mà tổ chức này sở hữu.* | — | — |  |
| 3-11 | `3.03#2` (7,9 s) | D | T1 | `t8_cosmic_physics_observatory`, `still` | *Người phụ trách Bộ Hóa học của giáo phái là Masami Tsuchiya, thạc sĩ hóa học hữu cơ xuất sắc của Đại học Tsukuba danh tiếng.* | — | — |  |
| 3-12 | `3.03#3` (8,2 s) | D | T1 | `t8_cosmic_physics_observatory`, `push` | *Người đứng đầu Bộ Khoa học và Công nghệ là Hideo Murai, một nhà vật lý tài ba của Đại học Osaka từng nghiên cứu về bức xạ vũ trụ.* | — | — |  |
| 3-13 | `3.03#4` (7,4 s) | D | T1 | `t8_virology_electron_microscope`, `pan` | *Người phụ trách mảng y tế và vũ khí sinh học là Seiichi Endo, người từng theo học ngành virus học tại Đại học Kyoto.* | — | — |  |
| 3-14 | `3.03#5` (5,4 s) | D | T1 | `t8_virology_electron_microscope`, `pull` | *Một thành viên cốt cán khác là Bác sĩ Tomomasa Nakagawa, tốt nghiệp đại học y khoa.* | — | — |  |
| 3-15 | `3.03#6` (12,2 s) | D | T1 | `t8_cardiac_surgery_theatre`, `still` | *Và đặc biệt hơn cả, phụ trách hệ thống bệnh viện của giáo phái là Bác sĩ Ikuo Hayashi, chuyên gia tim mạch tốt nghiệp Đại học Keio danh giá và từng là bác sĩ trưởng khoa tại bệnh viện quốc gia.* | — | — |  |
| 3-16 | `3.03#7` (10,2 s) | D | T1 | `t8_tsukuba_chemistry_lab`, `push` | *Những cá nhân này đều từng là thủ khoa hoặc nghiên cứu sinh xuất sắc, được nhà nước đầu tư nguồn học bổng lớn và nắm giữ tương lai xán lạn trong giới học thuật.* | — | — |  |
| 3-17 | `3.03#8` (8,7 s) | D | T1 | `t8_dossier_elite_scientists`, `pan` | *Sự quy tụ của một đội ngũ trí thức tầm cỡ quốc gia dưới trướng một kẻ mù chữ về khoa học là một hiện tượng điều tra chưa từng có tiền lệ.* | — | →H |  |
| 3-18 | `3.04#1` (8,3 s) | H | T1 | `t8_stethoscope_abandoned_drain`, `pull` | *Một bác sĩ tim mạch từng dành cả cuộc đời để giành giật sự sống cho người bệnh, những nhà khoa học với tương lai học thuật rực rỡ.* | — | — |  |
| 3-19 | `3.04#2` (6,1 s) | H | T1 | `t8_intellectual_hubris_chess`, `still` | *Tại sao họ lại từ bỏ đỉnh cao danh vọng để rồi chế tạo vũ khí hủy diệt chính đồng bào của mình?* | — | — |  |
| 3-20 | `3.04#3` (6,1 s) | H | T1 | `t8_broken_hippocratic_oath`, `push` | *Điều gì đã đánh sập toàn bộ hệ thống phòng thủ lý trí của những bộ óc thông minh nhất đất nước?* | — | — |  |
| 3-21 | `3.04#4` (7,4 s) | H | T1 | `t8_frontal_lobe_brain_scan`, `pan` | *Làm thế nào mà tư duy duy lý khoa học lại có thể đầu hàng hoàn toàn trước những điều hoang đường và vô căn cứ nhất?* | — | →C |  |
| 3-22 | `3.05#1` (6,4 s) | C | T1 | `t8_tokyo_stock_crash_1990`, `pull` | *Câu trả lời bắt nguồn từ một hiện tượng tâm lý học xã hội sâu sắc mang tên Sự trống rỗng hiện sinh.* | — | ✦ Cáo |  |
| 3-23 | `3.05#2` (6,1 s) | C | T1 | `t8_corporate_salaryman_cogs`, `still` | *Vào đầu thập niên 90, nước Nhật trải qua sự sụp đổ kinh hoàng của nền kinh tế bong bóng.* | — | — |  |
| 3-24 | `3.05#3` (9,7 s) | C | T1 | `t8_yoga_meditation_incense`, `push` | *Xã hội Nhật Bản lúc bấy giờ vận hành như một cỗ máy áp lực khổng lồ, nơi mỗi cá nhân bị ép phải trở thành những bánh răng vô danh trong các tập đoàn lớn.* | — | — |  |
| 3-25 | `3.05#4` (9,5 s) | C | T1 | `t8_moral_rationalization_books`, `pan` | *Nhiều thanh niên trí thức đạt điểm số tuyệt đối trong học tập nhưng tâm hồn lại hoàn toàn trống rỗng về ý nghĩa cuộc đời và mất phương hướng giá trị.* | — | — |  |
| 3-26 | `3.05#5` (9,4 s) | C | T1 | `t8_fragile_boundary_mirror`, `pull` | *Họ có câu trả lời hoàn hảo cho câu hỏi “Làm thế nào” bằng khoa học thực nghiệm, nhưng lại hoàn toàn bế tắc trước câu hỏi hiện sinh “Ta sống để làm gì”.* | — | — |  |
| 3-27 | `3.05#6` (9,5 s) | C | T1 | `t8_apocalypse_prophecy_scroll`, `still` | *Chính vào lúc những bộ óc xuất sắc ấy cảm thấy cô đơn và lạc lõng nhất, Shoko Asahara đã xuất hiện với một chiếc bẫy ngôn từ được ngụy trang hoàn hảo.* | — | — |  |
| 3-28 | `3.05#7` (8,9 s) | C | T1 | `t8_tokyo_stock_crash_1990`, `push` | *Hắn khéo léo lồng ghép các khái niệm tâm linh phương Đông với các thuật ngữ khoa học như cơ học lượng tử, trường năng lượng và tận thế luận.* | — | — |  |
| 3-29 | `3.05#8` (7,2 s) | C | T1 | `t8_corporate_salaryman_cogs`, `pan` | *Cách tiếp cận ngụy khoa học này đã đánh trúng cơn khát tìm kiếm ý nghĩa siêu nghiệm của giới sinh viên tinh hoa.* | — | — |  |
| 3-30 | `3.05#9` (9,1 s) | C | T1 | `t8_yoga_meditation_incense`, `pull` | *Asahara không trao cho họ tri thức mới, mà hắn trao cho họ một cảm giác thuộc về và một sứ mệnh vĩ đại giả tạo để khỏa lấp nỗi cô đơn cùng cực.* | — | →H |  |
| 3-31 | `3.06#1` (5,9 s) | H | T1 | `t8_intellectual_hubris_chess`, `still` | *Những người có học thức cao thường có một điểm yếu tâm lý chí mạng: Cái tôi trí tuệ quá lớn.* | — | — |  |
| 3-32 | `3.06#2` (6,4 s) | H | T1 | `t8_moral_rationalization_books`, `push` | *Họ luôn tin rằng bản thân quá thông minh và duy lý để có thể bị một kẻ khác thao túng hoặc lừa gạt.* | — | — |  |
| 3-33 | `3.06#3` (11,5 s) | H | T1 | `t8_frontal_lobe_brain_scan`, `pan` | *Hiện tượng kiêu ngạo trí thức khiến họ tin rằng việc gia nhập một giáo phái bí mật không phải là sự mê muội, mà là một trải nghiệm khai sáng vượt lên trên sự tầm thường của đám đông.* | — | — |  |
| 3-34 | `3.06#4` (8,6 s) | H | T1 | `t8_buddhist_mandala_distortion`, `pull` | *Khi Asahara trao cho họ cảm giác được trở thành những người được chọn nắm giữ chân lý cứu rỗi vũ trụ, chiếc bẫy kiêu ngạo đã sập xuống.* | — | — |  |
| 3-35 | `3.06#5` (9,4 s) | H | T1 | `t8_intellectual_hubris_chess`, `still` | *Trí thông minh phi thường của họ không hề bảo vệ được họ, mà ngược lại trở thành công cụ đắc lực để họ tự hợp lý hóa cho những hành vi tàn bạo nhất.* | — | →C |  |
| 3-36 | `3.07#1` (7,2 s) | C | T1 | `t8_devotion_altar_kneeling`, `push` | *Để duy trì cuộc sống hai mặt, các đệ tử trí thức đã vận dụng triệt để cơ chế tâm lý mang tên Chia ngăn nhận thức.* | — | — |  |
| 3-37 | `3.07#2` (10,0 s) | C | T1 | `t8_bio_incubator_pathogens`, `pan` | *Họ khóa chặt thế giới đời thường gồm gia đình, bạn bè và đạo đức xã hội vào một ngăn riêng biệt, và cách ly hoàn toàn với thế giới bí mật trong căn cứ Satyam.* | — | — |  |
| 3-38 | `3.07#3` (12,0 s) | C | T1 | `t8_psi_headgear_electrodes`, `pull` | *Trong phòng thí nghiệm, họ vẫn là những nhà khoa học làm việc tỉ mỉ với phương pháp luận chuẩn xác, nhưng mục đích tối hậu của công việc đó lại bị phong tỏa hoàn toàn khỏi phán xét đạo đức.* | — | — |  |
| 3-39 | `3.07#4` (5,1 s) | C | T1 | `t8_mountain_grave_memorial`, `still` | *Đồng thời, giáo chủ nhồi sọ họ bằng kỹ thuật Vật hóa và phi nhân hóa nạn nhân.* | — | — |  |
| 3-40 | `3.07#5` (12,4 s) | C | T1 | `t8_moral_rationalization_books`, `push` | *Trong mắt các nhà khoa học Aum, những người bình thường ngoài xã hội không còn là những sinh linh có cha mẹ và con cái, mà bị coi là những cá nhân mang nghiệp chướng nặng nề cản trở kỷ nguyên mới.* | — | — |  |
| 3-41 | `3.07#6` (7,5 s) | C | T1 | `t8_concrete_cell_isolation`, `pan` | *Tiếng khóc van xin hay sinh mạng của người vô tội bị giáng cấp thành những dữ liệu thí nghiệm vô cảm trong phòng lab.* | — | — |  |
| 3-42 | `3.07#7` (9,0 s) | C | T1 | `t8_devotion_altar_kneeling`, `pull` | *Sự tha hóa này minh chứng cho việc một khi nhân tính bị tước bỏ khỏi nhận thức, năng lực trí tuệ càng cao thì mức độ hủy diệt sẽ càng tàn bạo.* | — | — |  |
| 3-43 | `3.07#8` (5,9 s) | C | T1 | `t8_bio_incubator_pathogens`, `still` | *Và bi kịch tàn khốc không kém đã đổ ập xuống gia đình của chính những trí thức tinh hoa ấy.* | — | — |  |
| 3-44 | `3.07#9` (8,9 s) | C | T1 | `t8_psi_headgear_electrodes`, `push` | *Cha mẹ của họ, những người từng tự hào về những đứa con đỗ thủ khoa, đã hoàn toàn sụp đổ danh tính khi biết con mình trở thành kẻ khủng bố.* | — | — |  |
| 3-45 | `3.07#10` (8,0 s) | C | T1 | `t8_mountain_grave_memorial`, `pan` | *Nhiều bậc phụ huynh phải từ bỏ công việc, quỳ gối xin lỗi trước công chúng trong nỗi cay đắng tột cùng suốt phần đời còn lại.* | — | →H |  |
| 3-46 | `3.08#1` (6,1 s) | H | T1 | `t8_broken_hippocratic_oath`, `pull` | *Trí tuệ khi bị ngắt kết nối khỏi lòng trắc ẩn sẽ trở thành thứ vũ khí nguy hiểm nhất trên đời.* | — | — |  |
| 3-47 | `3.08#2` (9,5 s) | H | T1 | `t8_psi_headgear_electrodes`, `still` | *Sự phân mảnh tâm trí đã cho phép những con người từng được xã hội tôn kính trở thành những kẻ gieo rắc tử thần mà không hề cảm thấy cắn rứt lương tâm.* | — | — |  |
| 3-48 | `3.08#3` (6,7 s) | H | T1 | `t8_frontal_lobe_brain_scan`, `push` | *Đó là sự kết hợp chết người giữa một bộ óc lạnh lùng không có trái tim và một tâm hồn cuồng tín mù quáng.* | — | — |  |
| 3-49 | `3.08#4` (10,1 s) | H | T1 | `t8_fragile_boundary_mirror`, `pan` | *Thế nhưng, để biến sự mê muội ấy thành hành động tàn sát thực tế, giáo phái còn sử dụng những công nghệ kiểm soát tâm trí tinh vi và tàn bạo hơn thế rất nhiều.* | — | — |  |
| 3-50 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **MA THUẬT TẨY NÃO & KHÁI NIỆM POA** | — | ⊘ | ◼ |

### HỒI 4 — MA THUẬT TẨY NÃO & KHÁI NIỆM POA · nền chủ đạo `t8_concrete_cell_isolation`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (6,7 s) | H | T1 | `t8_concrete_cell_isolation`, `pull` | *Bên trong các khu trại khép kín của giáo phái Aum, các tín đồ bị cô lập hoàn toàn với thế giới bên ngoài.* | — | — |  |
| 4-02 | `4.02#2` (8,0 s) | H | T1 | `t8_malnutrition_solitary_bowl`, `still` | *Họ bị tịch thu toàn bộ giấy tờ tùy thân, cắt đứt liên lạc với cha mẹ và không được tiếp cận bất kỳ nguồn tin tức độc lập nào.* | — | — |  |
| 4-03 | `4.02#3` (6,9 s) | H | T1 | `t8_frontal_lobe_brain_scan`, `push` | *Nhưng thủ đoạn tàn độc nhất nhằm triệt tiêu ý chí tự do chính là kỹ thuật làm suy kiệt thể xác có hệ thống.* | — | — |  |
| 4-04 | `4.02#4` (8,2 s) | H | T1 | `t8_hidden_ceiling_hideout`, `pan` | *Các thành viên chỉ được phép ngủ hai đến ba tiếng mỗi ngày và phải duy trì chế độ ăn uống vô cùng kham khổ thiếu chất dinh dưỡng.* | — | — |  |
| 4-05 | `4.02#5` (9,9 s) | H | T1 | `t8_yoga_meditation_incense`, `pull` | *Tín đồ bị buộc phải ngồi thiền liên tục suốt hai mươi tiếng trong những căn phòng tối chật hẹp và bị trừng phạt tàn bạo nếu có bất kỳ biểu hiện ngủ gật nào.* | — | — |  |
| 4-06 | `4.02#6` (11,8 s) | H | T1 | `t8_concrete_cell_isolation`, `still` | *Khi cơ thể rơi vào trạng thái kiệt quệ kéo dài, vùng vỏ não trước trán phụ trách tư duy phản biện và phán đoán logic sẽ suy giảm nghiêm trọng, khiến con người trở nên phục tùng tuyệt đối.* | — | →D |  |
| 4-07 | `4.03#1` (6,8 s) | D | T1 | `t8_psi_headgear_electrodes`, `push` | *Hồ sơ điều tra đã làm sáng tỏ những thiết bị kỳ dị mà giáo phái sử dụng để thao túng não bộ của các đệ tử.* | — | — |  |
| 4-08 | `4.03#2` (7,2 s) | D | T1 | `t8_psi_headgear_electrodes`, `pan` | *Chúng phát minh ra một chiếc mũ gắn đầy điện cực mang tên PSI và bắt các tín đồ phải đội liên tục nhiều giờ liền.* | — | — |  |
| 4-09 | `4.03#3` (10,3 s) | D | T1 | `t8_hallucinogen_ritual_hall`, `pull` | *Giáo phái rêu rao rằng thiết bị này sẽ đồng bộ hóa sóng não của người đội với tần số sóng não của giáo chủ, và thu phí hàng nghìn đô la mỗi tháng cho mỗi chiếc mũ.* | — | — |  |
| 4-10 | `4.03#4` (9,7 s) | D | T1 | `t8_bio_incubator_pathogens`, `still` | *Hàng trăm tín đồ đã chi trả những khoản tiền khổng lồ để đội chiếc mũ này mỗi ngày, tin rằng họ đang tiếp nhận trực tiếp trí tuệ siêu phàm của giáo chủ.* | — | — |  |
| 4-11 | `4.03#5` (10,0 s) | D | T1 | `t8_hallucinogen_ritual_hall`, `push` | *Ngoài ra, cảnh sát còn phát hiện giáo phái bí mật sử dụng các loại chất gây ảo giác cực mạnh như LSD và thuốc hướng thần trong các nghi lễ kín trong bóng tối.* | — | — |  |
| 4-12 | `4.03#6` (9,8 s) | D | T1 | `t8_chemical_precursor_drums`, `pan` | *Cảnh sát còn tìm thấy nhiều kho hóa chất gây mê thiopental sodium được sử dụng để tra khảo lòng trung thành và xóa sạch ký ức của các thành viên nghi ngờ.* | — | — |  |
| 4-13 | `4.03#7` (10,7 s) | D | T1 | `t8_virology_electron_microscope`, `pull` | *Dưới tác động của hóa chất và sự suy kiệt thần kinh, các trí thức trẻ thực sự tin rằng họ đã nhìn thấy hào quang của đấng cứu thế và hoàn toàn mất đi khả năng hoài nghi.* | — | →H |  |
| 4-14 | `4.04#1` (10,6 s) | H | T1 | `t8_poa_twisted_doctrine`, `still` | *Thế nhưng, vũ khí tâm lý mang tính hủy diệt nhất mà Asahara sử dụng để xóa sạch lời thề nghề nghiệp của các bác sĩ và nhà khoa học chính là việc bóp méo khái niệm Poa.* | — | — |  |
| 4-15 | `4.04#2` (7,4 s) | H | T1 | `t8_buddhist_mandala_distortion`, `push` | *Trong truyền thống Phật giáo Tây Tạng, Poa là một pháp môn thiền định thanh tịnh giúp chuyển di tâm thức khi cận tử.* | — | — |  |
| 4-16 | `4.04#3` (8,3 s) | H | T1 | `t8_broken_hippocratic_oath`, `pan` | *Thế nhưng Asahara đã đánh tráo khái niệm thiêng liêng ấy thành một học thuyết biện minh cho hành vi tước đoạt mạng sống con người.* | — | — |  |
| 4-17 | `4.04#4` (7,6 s) | H | T1 | `t8_yoga_meditation_incense`, `pull` | *Bằng cách bẻ cong một triết lý cổ xưa, hắn tự ban cho mình quyền năng tối thượng được quyết định sinh tử của muôn loài.* | — | — |  |
| 4-18 | `4.04#5` (6,5 s) | H | T1 | `t8_devotion_altar_kneeling`, `still` | *Hắn biến một tội ác giết người man rợ thành một hành động được ngụy trang dưới vỏ bọc đạo đức cao cả.* | — | →C |  |
| 4-19 | `4.05#1` (7,8 s) | C | T1 | `t8_apocalypse_prophecy_scroll`, `push` | *Asahara rao giảng rằng thế giới thực tại đã bị ô uế và sắp sửa bước vào cuộc chiến tranh hạt nhân hủy diệt toàn nhân loại.* | — | — |  |
| 4-20 | `4.05#2` (8,2 s) | C | T1 | `t8_devotion_altar_kneeling`, `pan` | *Hắn tuyên bố rằng những người bình thường nếu tiếp tục sống sẽ chỉ tích tụ thêm ác nghiệp và chắc chắn phải đọa vào cõi địa ngục.* | — | — |  |
| 4-21 | `4.05#3` (9,7 s) | C | T1 | `t8_moral_rationalization_books`, `pull` | *Do đó, việc chấm dứt sinh mạng của họ trước khi họ kịp phạm thêm tội lỗi không phải là giết chóc, mà là một hành vi đại từ bi để giải thoát linh hồn họ.* | — | — |  |
| 4-22 | `4.05#4` (8,7 s) | C | T1 | `t8_weapons_of_mass_destruction`, `still` | *Học thuyết ngụy tạo này biến kẻ sát nhân thành một đấng cứu độ từ bi và biến hành vi giết chóc thành một nghĩa cử giải thoát cao thượng.* | — | — |  |
| 4-23 | `4.05#5` (5,1 s) | C | T1 | `t8_buddhist_mandala_distortion`, `push` | *Đây chính là đỉnh cao của Kỹ thuật Trung hòa đạo đức và Ngắt kết nối lương tâm.* | — | — |  |
| 4-24 | `4.05#6` (8,1 s) | C | T1 | `t8_apocalypse_prophecy_scroll`, `pan` | *Bằng cách đảo ngược hoàn toàn chuẩn mực thiện ác, hung thủ tin rằng bàn tay mình vấy … là để làm việc thiện cứu rỗi nạn nhân.* | — | — |  |
| 4-25 | `4.05#7` (8,2 s) | C | T1 | `t8_devotion_altar_kneeling`, `pull` | *Đồng thời, cơ chế ngoại hóa trách nhiệm khiến họ tin rằng mọi hành động của mình chỉ là công cụ thực thi ý chí của Đấng tối cao.* | — | — |  |
| 4-26 | `4.05#8` (8,3 s) | C | T1 | `t8_moral_rationalization_books`, `still` | *Sự chuyển dịch nhận thức ma quỷ này đã tháo gỡ hoàn toàn mọi rào cản đạo đức tự nhiên trong tâm trí của những trí thức ưu tú nhất.* | — | →H |  |
| 4-27 | `4.06#1` (8,5 s) | H | T1 | `t8_dr_hayashi_umbrella_subway`, `push` | *Chính sự ngụy biện ma quỷ ấy đã làm tê liệt hoàn toàn lương tâm của Bác sĩ Ikuo Hayashi, người từng đứng đầu một khoa tim mạch uy tín.* | — | — |  |
| 4-28 | `4.06#2` (8,0 s) | H | T1 | `t8_cardiac_surgery_theatre`, `pan` | *Đôi bàn tay từng thực hiện hàng trăm ca phẫu thuật tim cứu người giờ đây lại trở thành công cụ thực thi một tội ác kinh hoàng.* | — | — |  |
| 4-29 | `4.06#3` (9,7 s) | H | T1 | `t8_dr_hayashi_umbrella_subway`, `pull` | *Vào buổi sáng ngày 20 tháng 3, chính đôi bàn tay từng cứu sống hàng nghìn bệnh nhân đã dùng đầu ô chọc thủng hai túi sarin trên tuyến tàu Chiyoda.* | — | — |  |
| 4-30 | `4.06#4` (5,7 s) | H | T1 | `t8_tokyo_court_witness_stand`, `still` | *Hãy lắng nghe khoảnh khắc người đàn ông ấy đối diện với chính mình trước vành móng ngựa.* | — | →N2 |  |
| 4-31 | `4.08#1` (4,7 s) | N2 | T4 lời kể | `t8_grand_courtroom_proceedings`, `push` | *Trước tòa án, tôi không tìm kiếm bất kỳ sự tha thứ nào cho bản thân mình.* | — | ✦ Mèo |  |
| 4-32 | `4.08#2` (4,7 s) | N2 | T4 lời kể | `t8_tokyo_court_witness_stand`, `pan` | *Tôi từng là một bác sĩ với lời thề bảo vệ sự sống con người bằng mọi giá.* | — | — |  |
| 4-33 | `4.08#3` (7,0 s) | N2 | T4 lời kể | `t8_broken_hippocratic_oath`, `pull` | *Tôi đã phản bội lời thề Hippocrates thiêng liêng mà tôi từng khắc ghi trong tim suốt những năm tháng tuổi trẻ.* | — | — |  |
| 4-34 | `4.08#4` (8,2 s) | N2 | T4 lời kể | `t8_stethoscope_abandoned_drain`, `still` | *Vậy mà tôi đã để cho giáo lý mù quáng làm tê liệt lý trí, để rồi gây ra nỗi đau đớn không thể cứu vãn cho những đồng bào vô tội.* | — | — |  |
| 4-35 | `4.08#5` (9,9 s) | N2 | T4 lời kể | `t8_grand_courtroom_proceedings`, `push` | *Khi nhìn vào mắt của thân nhân các nạn nhân, tôi hiểu rằng không có sự cứu rỗi nào dành cho tội lỗi của mình ngoài việc thành khẩn khai báo toàn bộ sự thật.* | — | — |  |
| 4-36 | `4.08#6` (4,7 s) | N2 | T4 lời kể | `t8_tokyo_court_witness_stand`, `pan` | *Tôi quỳ xuống xin nhận mọi sự trừng phạt nghiêm khắc nhất của pháp luật.* | — | →H |  |
| 4-37 | `4.09#1` (10,1 s) | H | T1 | `t8_murai_assassination_cameras`, `pull` | *Lời khai thành khẩn và chi tiết của Bác sĩ Hayashi đã trở thành chìa khóa quyết định giúp cơ quan điều tra bóc trần toàn bộ cơ cấu vận hành ngầm của giáo phái.* | — | — |  |
| 4-38 | `4.09#2` (4,7 s) | H | T1 | `t8_police_convoy_kamikuishiki`, `still` | *Thế nhưng, một biến cố đẫm … khác đã xảy ra ngay trước mắt công chúng.* | — | — |  |
| 4-39 | `4.09#3` (13,5 s) | H | T1 | `t8_murai_assassination_cameras`, `push` | *Ngày 23 tháng 4 năm 1995, nhà vật lý Hideo Murai, nhân vật số hai của Aum, đã bị ám sát ngay trước ống kính truyền hình bên ngoài trụ sở Tokyo nhằm bịt đầu mối bí mật vũ khí.* | — | — |  |
| 4-40 | `4.09#4` (9,4 s) | H | T1 | `t8_hidden_ceiling_hideout`, `pan` | *Vụ thanh trừng Murai ngay giữa ban ngày phơi bày sự tàn khốc của một tổ chức sẵn sàng tiêu diệt cả những bộ óc trung thành nhất để xóa sạch dấu vết.* | — | — |  |
| 4-41 | `4.09#5` (5,2 s) | H | T1 | `t8_asahara_shadow_profile`, `pull` | *Mặc dù vậy, vòng vây pháp lý vẫn siết chặt không ngừng quanh kẻ chủ mưu tối cao.* | — | — |  |
| 4-42 | `4.09#6` (10,7 s) | H | T1 | `t8_hidden_ceiling_hideout`, `still` | *Ngày 16 tháng 5 năm 1995, cảnh sát đã phát hiện Shoko Asahara đang ẩn nấp trong một hốc trần nhà chật hẹp tại tòa nhà Satyam số 6.* | — | — |  |
| 4-43 | `4.09#7` (10,0 s) | H | T1 | `t8_hidden_ceiling_hideout`, `push` | *Kẻ từng tự phong mình là Đấng cứu thế của nhân loại ngồi co ro trong bóng tối, run rẩy bên cạnh một bọc tiền mặt trị giá gần mười triệu yên và các thỏi vàng.* | — | — |  |
| 4-44 | `4.09#8` (8,6 s) | H | T1 | `t8_iron_gate_closing`, `pan` | *Không một lời kinh kệ nào vang lên trong khoảnh khắc đó, chỉ còn lại sự run rẩy bẽ bàng của một kẻ lừa đảo bị lột trần trước pháp luật.* | — | — |  |
| 4-45 | `4.09#9` (8,4 s) | H | T1 | `t8_concrete_cell_isolation`, `pull` | *Chiếc mặt nạ thần thánh rơi xuống, phơi bày sự trơ trọi và nỗi sợ hãi hèn hạ của một kẻ lừa đảo khi bản ngã ái kỷ sụp đổ hoàn toàn.* | — | →D |  |
| 4-46 | `4.11#1` (7,0 s) | D | T1 | `t8_tokyo_court_gavel_strike`, `still` | *Sự sụp đổ của Shoko Asahara trong hốc trần nhà đã vạch trần bản chất thật sự của kẻ cầm đầu giáo phái độc hại.* | — | — |  |
| 4-47 | `4.11#2` (6,9 s) | D | T1 | `t8_asahara_shadow_profile`, `push` | *Không hề có phép màu bay bổng, không có hào quang tâm linh nào cứu giúp hắn trước sự truy lùng của công lý.* | — | — |  |
| 4-48 | `4.11#3` (10,2 s) | D | T1 | `t8_concrete_cell_isolation`, `pan` | *Những cuộc thẩm vấn sau đó cho thấy hắn hoàn toàn mất đi sự kiểm soát cảm xúc, liên tục chối bỏ mọi trách nhiệm và đùn đẩy tội lỗi cho chính các đệ tử của mình.* | — | — |  |
| 4-49 | `4.11#4` (7,6 s) | D | T1 | `t8_matsumoto_court_dossier`, `pull` | *Hắn chỉ là một kẻ thao túng tàn nhẫn, sẵn sàng hy sinh toàn bộ tín đồ để bảo toàn sự an toàn và lòng tham của bản thân.* | — | — |  |
| 4-50 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT LỊCH SỬ & BÀI HỌC TỰ DO TƯ TƯỞNG** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT LỊCH SỬ & BÀI HỌC TỰ DO TƯ TƯỞNG · nền chủ đạo `t8_grand_courtroom_proceedings`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (10,6 s) | H | T1 | `t8_grand_courtroom_proceedings`, `still` | *Các phiên tòa xét xử giáo phái Aum Shinrikyo kéo dài suốt hơn hai thập kỷ, trở thành một trong những trang hồ sơ tư pháp đồ sộ và phức tạp nhất trong lịch sử Nhật Bản.* | — | — |  |
| 5-02 | `5.02#2` (8,2 s) | H | T1 | `t8_tokyo_court_gavel_strike`, `push` | *Trước tòa án, Shoko Asahara liên tục giả điên, lẩm bẩm những câu vô nghĩa và từ chối giao tiếp với cả luật sư lẫn các thẩm phán.* | — | — |  |
| 5-03 | `5.02#3` (5,6 s) | H | T1 | `t8_fragile_boundary_mirror`, `pan` | *Đó chính là phản ứng điển hình của Sự sụp đổ cái tôi ái kỷ và Sự tự thương hại bệnh lý.* | — | — |  |
| 5-04 | `5.02#4` (8,0 s) | H | T1 | `t8_concrete_cell_isolation`, `pull` | *Bản chất của kẻ ái kỷ suy đồi là không bao giờ chấp nhận vị thế của một kẻ bại trận trước những người mà hắn từng coi thường.* | — | — |  |
| 5-05 | `5.02#5` (8,6 s) | H | T1 | `t8_grand_courtroom_proceedings`, `still` | *Kẻ từng quen đứng trên đỉnh cao quyền lực tuyệt đối đã không thể đối diện với sự trần trụi của chính mình khi bị tước bỏ mọi đặc quyền.* | — | — |  |
| 5-06 | `5.02#6` (6,9 s) | H | T1 | `t8_tokyo_court_gavel_strike`, `push` | *Hắn thà chọn cách thu mình vào vỏ bọc câm lặng hơn là thừa nhận sự thất bại thảm hại của ảo tưởng vĩ cuồng.* | — | →D |  |
| 5-07 | `5.03#1` (11,3 s) | D | T1 | `t8_thirteen_death_verdicts`, `pan` | *Sau quá trình xét xử nghiêm minh và thận trọng, Tòa án Tối cao Nhật Bản đã tuyên phạt mức án cao nhất: Án tử hình đối với Shoko Asahara và mười hai đệ tử then chốt của giáo phái.* | — | — |  |
| 5-08 | `5.03#2` (10,3 s) | D | T1 | `t8_thirteen_death_verdicts`, `pull` | *Trong số những kẻ phải đền tội có nhà hóa học Masami Tsuchiya, chuyên gia virus học Seiichi Endo, nhà mua sắm vũ khí Kiyohide Hayakawa và bác sĩ Tomomasa Nakagawa.* | — | — |  |
| 5-09 | `5.03#3` (9,1 s) | D | T1 | `t8_dossier_elite_scientists`, `still` | *Riêng Bác sĩ Ikuo Hayashi, nhờ sự thức tỉnh, thái độ ăn năn chân thành và lời khai hợp tác toàn diện giúp phá án, đã nhận mức án tù chung thân.* | — | — |  |
| 5-10 | `5.03#4` (10,5 s) | D | T1 | `t8_tokyo_court_gavel_strike`, `push` | *Hệ thống tư pháp Nhật Bản đã thể hiện sự kiên định và tôn trọng chuẩn mực tố tụng tuyệt đối khi dành hơn hai thập kỷ để làm sáng tỏ từng chi tiết nhỏ nhất của vụ án.* | — | — |  |
| 5-11 | `5.03#5` (11,2 s) | D | T1 | `t8_iron_gate_closing`, `pan` | *Vào tháng 7 năm 2018, bản án tử hình bằng hình thức treo cổ đã chính thức được thi hành đối với Shoko Asahara và toàn bộ mười hai đồng phạm then chốt.* | — | — |  |
| 5-12 | `5.03#6` (8,3 s) | D | T1 | `t8_matsumoto_court_dossier`, `pull` | *Sự trừng phạt nghiêm khắc của pháp luật đã khép lại một chương đen tối kéo dài hơn hai mươi ba năm trong tâm thức xã hội Nhật Bản.* | — | →H |  |
| 5-13 | `5.04#1` (7,1 s) | H | T1 | `t8_tokyo_detention_house_dawn`, `still` | *Vụ án đã giáng một … chí mạng vào niềm tin xã hội và thúc đẩy cuộc đại cải tổ thể chế pháp luật chưa từng có.* | — | — |  |
| 5-14 | `5.04#2` (9,8 s) | H | T1 | `t8_murakami_underground_book`, `push` | *Nhật Bản đã sửa đổi toàn diện Đạo luật Tổ chức Tôn giáo và ban hành các đạo luật đặc biệt nhằm kiểm soát chặt chẽ các tổ chức có nguy cơ khủng bố tập thể.* | — | — |  |
| 5-15 | `5.04#3` (10,6 s) | H | T1 | `t8_murakami_underground_book`, `pan` | *Trong cuốn sách tư liệu nổi tiếng mang tên “Ngầm”, nhà văn Haruki Murakami đã dành nhiều tháng phỏng vấn hàng chục nạn nhân và cả những cựu thành viên của giáo phái Aum.* | — | — |  |
| 5-16 | `5.04#4` (7,5 s) | H | T1 | `t8_tokyo_dawn_restored_peace`, `pull` | *Ông nhận ra rằng: Ranh giới giữa một con người bình thường và một kẻ cuồng tín mỏng manh hơn chúng ta tưởng rất nhiều.* | — | — |  |
| 5-17 | `5.04#5` (7,8 s) | H | T1 | `t8_fragile_boundary_mirror`, `still` | *Khi xã hội quá áp lực và vô cảm, bất kỳ tâm hồn cô đơn nào cũng có thể tìm đến một chiếc phao cứu sinh độc hại để bấu víu.* | — | — |  |
| 5-18 | `5.04#6` (9,4 s) | H | T1 | `t8_buddhist_mandala_distortion`, `push` | *Một xã hội hiện đại thịnh vượng về vật chất nhưng nghèo nàn về sự kết nối cảm xúc chính là mảnh đất màu mỡ nhất cho những mầm mống tà giáo sinh sôi.* | — | — |  |
| 5-19 | `5.04#7` (9,3 s) | H | T1 | `t8_tokyo_detention_house_dawn`, `pan` | *Và cái ác thực sự không phải là những con quái vật từ bên ngoài, mà nảy sinh ngay từ sự thiếu thốn kết nối nhân văn trong lòng cuộc sống hiện đại.* | — | →C |  |
| 5-20 | `5.05#1` (7,0 s) | C | T1 | `t8_tokyo_dawn_restored_peace`, `pull` | *Hồ sơ Aum Shinrikyo để lại một bài học cảnh tỉnh sâu sắc cho toàn nhân loại về giới hạn của trí tuệ con người.* | — | — |  |
| 5-21 | `5.05#2` (8,5 s) | C | T1 | `t8_corporate_salaryman_cogs`, `still` | *Bằng cấp học thuật cao và chỉ số thông minh logic không bao giờ là tấm khiên bảo vệ chúng ta trước những … thao túng tâm lý tinh vi.* | — | — |  |
| 5-22 | `5.05#3` (9,4 s) | C | T1 | `t8_moral_rationalization_books`, `push` | *Ngược lại, khi những bộ óc xuất chúng nhất bị mất phương hướng về mặt giá trị sống, họ có thể trở thành công cụ hủy diệt nguy hiểm nhất của cái ác.* | — | — |  |
| 5-23 | `5.05#4` (9,4 s) | C | T1 | `t8_fragile_boundary_mirror`, `pan` | *Khi tư duy phản biện bị đánh đổi để lấy cảm giác an toàn giả tạo, con người sẽ tự nguyện trao quyền kiểm soát cuộc đời mình cho những kẻ thao túng.* | — | — |  |
| 5-24 | `5.05#5` (8,1 s) | C | T1 | `t8_tokyo_dawn_restored_peace`, `pull` | *Sự cuồng tín luôn bắt đầu từ những lời hứa hẹn ngọt ngào về một chân lý tuyệt đối đứng trên mọi quy chuẩn đạo đức thông thường.* | — | →H |  |
| 5-25 | `5.06#1` (10,8 s) | H | T1 | `t8_redflag1_social_isolation`, `still` | *Để bảo vệ bản thân và những người thân yêu trước các tổ chức thao túng tâm trí độc hại, kênh Amber Eyes xin đúc kết bốn tín hiệu cảnh báo đỏ sinh tồn từ hồ sơ lịch sử này:* | — | — |  |
| 5-26 | `5.06#2` (5,3 s) | H | T8 cờ | `t8_redflag1_social_isolation`, `push` | *01* · **CẢNH BÁO ĐỎ THỨ NHẤT: CHIẾN THUẬT CÔ LẬP XÃ HỘI VÀ CẮT ĐỨT CÁC MỐI QUAN HỆ HỖ TRỢ.** | — | — |  |
| 5-27 | `5.06#3` (11,7 s) | H | T1 | `t8_redflag2_physical_exhaustion`, `pan` | *Bất kỳ tổ chức lành mạnh nào cũng tôn trọng gia đình và các mối liên kết xã hội của bạn, nếu một nhóm tìm cách tách bạn khỏi người thân và kiểm soát nguồn thông tin, hãy lập tức rời đi.* | — | — |  |
| 5-28 | `5.06#4` (5,5 s) | H | T8 cờ | `t8_redflag2_physical_exhaustion`, `pull` | *02* · **CẢNH BÁO ĐỎ THỨ HAI: KỸ THUẬT LÀM SUY KIỆT THỂ CHẤT NHẰM TRIỆT TIÊU TƯ DUY PHẢN BIỆN.** | — | — |  |
| 5-29 | `5.06#5` (9,5 s) | H | T1 | `t8_redflag3_cult_of_personality`, `still` | *Hãy cảnh giác cao độ với những nơi ép buộc bạn phải thức khuya liên tục, nhịn ăn khắc nghiệt hoặc lao động quá sức dưới danh nghĩa thanh lọc tâm hồn.* | — | — |  |
| 5-30 | `5.06#6` (8,1 s) | H | T1 | `t8_redflag4_moral_inversion`, `push` | *Một tinh thần minh mẫn không bao giờ có thể tồn tại trong một cơ thể bị bóc lột và kiệt quệ đến mức mất đi quyền tự chủ cơ bản.* | — | — |  |
| 5-31 | `5.06#7` (5,7 s) | H | T8 cờ | `t8_redflag3_cult_of_personality`, `pan` | *03* · **CẢNH BÁO ĐỎ THỨ BA: SỰ SÙNG BÁI CÁ NHÂN TUYỆT ĐỐI VÀ CẤM ĐOÁN VIỆC ĐẶT CÂU HỎI HOÀI NGHI.** | — | — |  |
| 5-32 | `5.06#8` (12,3 s) | H | T1 | `t8_malnutrition_solitary_bowl`, `pull` | *Một người thầy chân chính luôn khuyến khích học trò tự do suy nghĩ và kiểm chứng sự thật, chỉ có những kẻ thao túng mới coi lời nói của mình đứng trên luật pháp và quy kết sự nghi ngờ là tội lỗi.* | — | — |  |
| 5-33 | `5.06#9` (4,9 s) | H | T8 cờ | `t8_redflag4_moral_inversion`, `still` | *04* · **CẢNH BÁO ĐỎ THỨ TƯ: NGỤY BIỆN ĐẢO NGƯỢC ĐẠO ĐỨC VÀ KÍCH ĐỘNG THÙ HẬN XÃ HỘI.** | — | — |  |
| 5-34 | `5.06#10` (8,2 s) | H | T1 | `t8_fragile_boundary_mirror`, `push` | *Hãy kiên quyết từ chối bất kỳ giáo lý nào rao giảng rằng việc gây tổn hại cho người khác là một hành vi từ bi vì mục đích cao cả.* | — | — |  |
| 5-35 | `5.06#11` (7,2 s) | H | T1 | `t8_concrete_cell_isolation`, `pan` | *Hãy luôn nhớ rằng không một mục đích cao cả nào có thể biện minh cho những phương tiện tàn nhẫn và phi nhân tính.* | — | — |  |
| 5-36 | `5.06#12` (6,1 s) | H | T1 | `t8_redflag1_social_isolation`, `pull` | *Chân lý đích thực không bao giờ được xây dựng trên sự lừa dối, sợ hãi và nỗi đau của đồng loại.* | — | — |  |
| 5-37 | `5.08#1` (7,2 s) | H | T1 | `t8_tokyo_dawn_restored_peace`, `still` | *Ánh sáng của tri thức chỉ thực sự có giá trị khi nó được soi đường bởi lòng trắc ẩn và sự tỉnh táo của lương tri.* | — | — |  |
| 5-38 | `5.08#2` (5,7 s) | H | T1 | `t8_tokyo_dawn_fog`, `push` | *Cảm ơn quý vị đã đồng hành cùng Amber Eyes trong tập hồ sơ giải phẫu tâm lý ngày hôm nay.* | — | — |  |
| 5-39 | `5.08#3` (5,7 s) | H | T1 | `t8_corporate_salaryman_cogs`, `pan` | *Hãy bấm đăng ký kênh, chia sẻ video và để lại góc nhìn của bạn ở phần bình luận bên dưới.* | — | — |  |
| 5-40 | `5.08#4` (4,1 s) | H | T1 | `t8_tokyo_dawn_restored_peace`, `pull` | *Xin chào và hẹn gặp lại quý vị trong những tập hồ sơ tiếp theo.* | — | — |  |
| 5-41 | hết tập (9,0 s) | — | T2 thẻ hồ sơ | `t8_tokyo_dawn_restored_peace`, `pull` | **HỒ SƠ TẬP 08 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | — | ⊘ | ◼ |

**Tổng:** 223 dòng · 218 câu · 5 hồi · nền dùng 74 loại. Bảng dựng lại 09/11/2026 theo kịch bản viết lại 07/11/2026 (218 câu). Thời lượng shot lấy từ timeline **neo master mp3** (T20: tổng khớp master 0,000 s) — thời lượng LỜI từng câu vẫn là ước lượng theo số ký tự.


## Dựng video 10/11/2026 (AI)
- Master dùng: mp3 ngày 09/11 08:05 (VN 1957,51 s · EN 1895,91 s · JA 2095,36 s). Timeline `.work/timeline_s*_t08.json` đo lại từ chính mp3 (khoá `_measured`); bản cũ ở `.work/_cu/t08_20261110/`.
- Ghép tiếng thủ công (limiter `latency=1`), không dùng `package.py --mux` (wav cũ). Không sinh lại `mo_ta.txt`.
- Số đo VN/EN/JA: hình−tiếng lệch 0,01/0,01/0,03 s · giải mã 0 lỗi · −16,2/−16,3/−16,3 LUFS · TP −1,9/−1,8/−2,0 dBFS · 0 câm > 0,3 s · 16/16 khung khớp ảnh tĩnh (MAE ≤ 5,9) · thẻ kết đạt.
- Thumbnail: nền `t8_frontal_lobe_brain_scan`; chữ EN/JA do AI dịch — chờ người dùng duyệt. Loại `t8_psi_headgear_electrodes` (lộ nửa mặt, H1).
- Tồn: thẻ kết JA ngắt dòng "第0 / 8話" (thẩm mỹ).
