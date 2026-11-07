# HỒ SƠ SẢN XUẤT TẬP 08 · "KHI CÁC THIÊN TÀI BỊ TẨY NÃO"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 08: Khi Các Thiên Tái Bị Tẩy Não** |
| Vụ án | Giáo phái Aum Shinrikyo & Vụ tấn công khí độc tàu điện ngầm Tokyo (Tokyo, Nhật Bản, 1995) |
| Chủ đề | Thao túng tâm lý giáo phái, Sự trống rỗng hiện sinh, Kỹ thuật làm suy kiệt thần kinh, Nghịch lý trí thức tinh hoa |
| Tổng thời lượng | **ƯỚC LƯỢNG 23 phút 40,4 giây** (1420,4 s) · 5 hồi · 171 câu thoại · 53 phần tử kịch bản |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Hành khách Tokyo) · N2 (Bác sĩ Ikuo Hayashi) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D3_SH.wav`, C: `C2_AB03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap08.json`) |
| Thành phẩm Master | ⛔ **ĐÃ BỊ DỌN (A11 §8)** — `Tap08_master.mp3` & `.work/audio_master_t08.wav` không còn. Số đo B2 bên dưới là **kết quả của master cũ** (bản kịch bản 154 câu), chỉ để tham khảo. Cần dựng lại TTS + `build_audio3.py` cho 171 câu mới. |

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
   - Timeline: [`.work/timeline_s_t08.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/timeline_s_t08.json) — **1420,4 s (23:40) · bản ƯỚC LƯỢNG** (`.work/_build_timeline_t08.py`); sẽ bị ghi đè bởi `build_audio3.py` sau khi dựng lại TTS
   - Phụ đề SRT: [`02_SAN_XUAT/Tap08/xuat_ban/Tap08.srt`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/Tap08.srt) — ⛔ **CŨ (278 cue, lời bản 154 câu)**; phải sinh lại từ timeline mới (171 câu)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep08_vi.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/quality_qc_utmos_ep08_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md)

## 6. DANH SÁCH SHOT — TẬP 08 (viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.

**Trạng thái 06/11/2026:** kịch bản viết lại 05/11/2026 (53 phần tử · 171 câu) ⇒ bảng shot dựng lại **108 shot**. Master audio cũ đã bị dọn theo A11 §8 ⇒ `timeline_s_t08.json` là **bản ước lượng** (`.work/_build_timeline_t08.py`), chỉ dùng cho ảnh tĩnh; khi dựng video phải chạy lại TTS + `build_audio3.py` (sẽ ghi đè đúng file timeline này).

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### HỒI 1 — BUỔI SÁNG ĐỊNH MỆNH DƯỚI LÒNG ĐẤT TOKYO · nền chủ đạo `t8_tokyo_dawn_fog`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s) | — | T1 | `t8_tokyo_dawn_fog` hiện dần từ đen | *HỒI 01 · BUỔI SÁNG ĐỊNH MỆNH DƯỚI LÒNG ĐẤT TOKYO* | — | ⊘ |  |
| 1-01 | `1.02#1`–`#2` | H | T1 | `t8_tokyo_dawn_fog`, `pull` | *Sáng thứ Hai, ngày 20 tháng 3 năm 1995, thủ đô Tokyo thức dậy trong nhịp sống hối hả thường nhật. Hàng triệu người dân đổ dồn về hệ thống tàu điện ngầm dưới lòng đất.* | — | ✦ Cú |  |
| 1-02 | `1.02#3` | H | T1 | `t8_commuter_crowd_station`, `still` | *Đúng tám giờ sáng — giờ cao điểm đông đúc nhất trong ngày.* | — | — |  |
| 1-03 | `1.02#4` | H | T1 | `t8_subway_tracks_perspective`, `pull` | *Năm chuyến tàu điện ngầm trên ba tuyến huyết mạch Chiyoda, Marunouchi và Hibiya đang cùng lao vun vút về phía nhà ga Kasumigaseki.* | — | — |  |
| 1-04 | `1.02#5`–`#6` | H | T1 | `t8_kasumigaseki_facade`, `pan` | *Nơi đây đặt trụ sở của các Bộ ngành trọng yếu và Cơ quan Cảnh sát Quốc gia. Nhật Bản khi ấy vẫn tự hào với “huyền thoại an toàn” — một xã hội có tỷ lệ tội phạm thấp bậc nhất thế giới.* | — | — |  |
| 1-05 | `1.04#1` | H | T1 | `t8_chemical_structure_sarin`, `still` | *Thế nhưng, trên mỗi chuyến tàu ấy, có những người đàn ông mang theo một thứ chất độc thần kinh có sức tàn phá khủng khiếp.* | — | — |  |
| 1-06 | `1.04#2` | H | T1 | `t8_umbrella_puncture_action`, `pull` | *Họ dùng đầu ô đã mài nhọn đâm thủng các túi ni-lông chứa chất lỏng chết người ngay trên sàn toa xe.* | — | — |  |
| 1-07 | `1.04#3` | H | T1 | `t8_train_doors_closing`, `pan` | *Khi cửa tàu vừa mở tại các nhà ga đông đúc, những kẻ này nhanh chóng bước ra ngoài, để lại luồng hơi độc bốc lên âm thầm giữa đám đông.* | — | — |  |
| 1-08 | `1.04#4` | H | T4 trích dẫn | `t8_newspaper_wrapped_package`, `still` | *Một cuộc tấn công phối hợp tàn bạo nhắm thẳng vào các công dân vô tội.* | — | — |  |
| 1-09 | `1.06#1`–`#2` | H | T1 | `t8_subway_car_mist_vapor`, `pull` | *Chỉ trong vài phút ngắn ngủi, một cơn ác mộng chưa từng có trong lịch sử Nhật Bản thời hậu chiến đã bùng nổ dưới lòng đất Tokyo. Hãy hình dung điều một hành khách khi ấy phải trải qua.* | — | →N1 |  |
| 1-10 | `1.07#1`–`#2` | N1 | T4 lời kể | `t8_subway_platform_tunnel_dark`, `still` | *Tôi đang đứng đọc sách trên tàu thì ngửi thấy một mùi hắc nhẹ rất lạ, giống như mùi dung môi pha sơn. Đột nhiên, mắt tôi cay xè và mọi thứ xung quanh tối sầm lại.* | — | ✦ Cừu |  |
| 1-11 | `1.07#3` | N1 | T1 | `t8_dropped_novel_glasses`, `pull` | *Tôi thấy ngực mình nghẹt thở, và mọi người xung quanh bắt đầu ho dữ dội rồi hoảng loạn tìm lối thoát.* | — | — |  |
| 1-12 | `1.07#4`–`#5` | N1 | T1 | `t8_subway_stairs_escape`, `pan` | *Không ai hiểu chuyện gì đang xảy ra, và sự kinh hoàng bao trùm khắp sân ga. Cảm giác ấy cứ như ngày tận thế vừa ập xuống đầu chúng tôi giữa ban ngày.* | — | — |  |
| 1-13 | `1.09#1` | H | T1 | `t8_ambulances_tokyo_street`, `still` | *Vụ tấn công hóa học đã cướp đi sinh mạng của mười bốn thường dân vô tội và làm tổn hại sức khỏe của hơn năm nghìn tám trăm người khác.* | — | →H |  |
| 1-14 | `1.09#2` | H | T1 | `t8_hospital_triage_corridor`, `pull` | *Hai nhân viên đường sắt quả cảm, ông Kazumasa Takahashi và ông Tsuneo Hishinuma, đã dũng cảm dùng tay không di chuyển các túi chất độc ra khỏi toa xe để bảo vệ hành khách và anh dũng hy sinh.* | — | — |  |
| 1-15 | `1.09#3`–`#4` | H | T1 | `t8_subway_platform_tunnel_dark`, `still` | *Hàng nghìn người phải chịu đựng những di chứng tâm lý nặng nề và nỗi sợ hãi kéo dài suốt phần đời còn lại. Cơn hoang tưởng tập thể bùng phát khắp thủ đô: người dân Tokyo nín thở khi bước xuống ga ngầm.* | — | — |  |
| 1-16 | `1.09#5` | H | T1 | `t8_subway_exit_sunlight`, `pull` | *Toàn bộ hệ thống giao thông và y tế của siêu đô thị rơi vào tình trạng tê liệt khẩn cấp.* | — | — |  |
| 1-17 | `1.11#1` | D | T1 | `t8_tokyo_police_hq`, `pan` | *Ngay sau khi tiếp nhận thông tin về vụ rải khí độc tại ga Kasumigaseki, Cơ quan Cảnh sát Quốc gia Nhật Bản đã xác định đây là một cuộc tấn công khủng bố phối hợp quy mô lớn.* | — | ✦ Sói |  |
| 1-18 | `1.11#2` | D | T1 | `t8_incident_board_map`, `still` | *Mục tiêu của chúng là nhắm thẳng vào các tuyến tàu đi qua khu vực cơ quan đầu não của chính phủ nhằm làm tê liệt bộ máy điều hành đất nước.* | — | — |  |
| 1-19 | `1.11#3`–`#4` | D | T1 | `t8_chemical_structure_sarin`, `pull` | *Phương thức gây án được tính toán tinh vi với năm kẻ tấn công đồng loạt ra tay vào đúng khung giờ cao điểm. Hóa chất được sử dụng là sarin, một loại khí độc thần kinh nhân tạo cực kỳ nguy hiểm và phức tạp trong tổng hợp.* | — | — |  |
| 1-20 | `1.11#5` | D | T2 thẻ hồ sơ | `t8_aum_shinrikyo_emblem_shadow`, `still` | *Mọi dấu vết tại hiện trường đều nhanh chóng chỉ về một tổ chức tôn giáo bí ẩn mang tên Giáo phái Aum Shinrikyo.* | — | — |  |
| 1-21 | `1.12#1`–`#3` | H | T1 | `t8_dossier_elite_scientists`, `pull` | *Điều khiến toàn bộ thế giới bàng hoàng không chỉ dừng lại ở sự tàn độc của vụ tấn công. Kẻ thực hiện không phải là một tổ chức quân sự ngoại quốc hay những tên tội phạm đường phố liều lĩnh.* | — | →C |  |
| 1-22 | `1.12#4`–`#5` | H | T1 | `t8_kasumigaseki_facade`, `pan` | *Đứng sau thảm kịch ấy là những nhà khoa học, bác sĩ và trí thức tinh hoa của chính đất nước Nhật Bản. Chính vị thế học thức đỉnh cao ấy đã tạo nên một “Hiệu ứng Hào quang” chết người, che mắt toàn bộ xã hội và cơ quan an ninh suốt nhiều năm dài.* | — | — |  |
| 1-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ** | — | ⊘ | ◼ |

### HỒI 2 — KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ VÀ PHÒNG THÍ NGHIỆM TỬ THẦN · nền chủ đạo `t8_mount_fuji_dawn_somber`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `t8_mount_fuji_dawn_somber`, `pull` | *Sáng sớm ngày 22 tháng 3 năm 1995, đúng hai ngày sau vụ tấn công kinh hoàng dưới lòng đất Tokyo. Hơn một nghìn sĩ quan cảnh sát và đặc nhiệm phòng hóa Nhật Bản đã đồng loạt xuất kích.* | — | — |  |
| 2-02 | `2.02#3` | H | T1 | `t8_hazmat_officers_formation`, `still` | *Họ trang bị mặt nạ phòng độc và bình dưỡng khí chuyên dụng.* | — | — |  |
| 2-03 | `2.02#4`–`#5` | H | T1 | `t8_police_convoy_kamikuishiki`, `pan` | *Đoàn xe tiến thẳng vào khu căn cứ khổng lồ của giáo phái Aum tại làng Kamikuishiki, nằm biệt lập dưới chân núi Phú Sĩ. Một cuộc khám xét quy mô chưa từng có trong lịch sử thực thi pháp luật của đất nước mặt trời mọc.* | — | →D |  |
| 2-04 | `2.04#1`–`#2` | D | T1 | `t8_satyam_compound_aerial`, `still` | *Khu liên hợp của giáo phái mang tên Satyam là một quần thể gồm hàng chục tòa nhà bê tông xám xịt được canh phòng cẩn mật bằng hệ thống camera giám sát. Bề ngoài, nó mang danh nghĩa là tu viện thiền định và xưởng sản xuất nông sản thanh tịnh.* | — | ✦ Sói |  |
| 2-05 | `2.04#3`–`#4` | D | T1 | `t8_satyam_7_exterior`, `pull` | *Khi cảnh sát tiến vào tòa nhà mang mã số Satyam số 7, tất cả các chuyên gia đều phải lạnh người trước những gì tận mắt chứng kiến. Bên trong không hề có tượng Phật hay không gian thờ tự, mà là một nhà máy sản xuất vũ khí hóa học quy mô công nghiệp hoàn chỉnh.* | — | — |  |
| 2-06 | `2.04#5` | D | T1 | `t8_chemical_precursor_drums`, `still` | *Cảnh sát thu giữ hàng chục tấn hóa chất tiền chất cùng dàn máy móc tổng hợp hữu cơ tối tân trị giá hàng triệu đô la Mỹ.* | — | — |  |
| 2-07 | `2.04#6` | D | T1 | `t8_mi17_helicopter_hangar`, `pan` | *Thậm chí, giáo phái còn bí mật nhập khẩu một chiếc trực thăng quân sự Mi-17 từ nước ngoài và nuôi cấy cả vi khuẩn bệnh than.* | — | — |  |
| 2-08 | `2.05#1`–`#2` | H | T3 so sánh | `t8_newspaper_wrapped_package`, `still` | *THỦ ĐOẠN* **Túi ni-lông, đầu ô, xe chờ sẵn** → *CHỮ KÝ TÂM LÝ* **Hiện thực hóa ngày tận thế** | — | — |  |
| 2-09 | `2.05#3`–`#5` | H | T1 | `t8_aum_shinrikyo_emblem_shadow`, `pull` | *Thế nhưng, ngòi nổ tâm lý kích hoạt cuộc tấn công vào đúng thời điểm đó lại xuất phát từ một cơn hoảng loạn tột độ của kẻ cầm đầu. Giáo chủ Aum nhận được tin mật báo cảnh sát sẽ đại lục soát khu căn cứ Kamikuishiki vào ngày 22 tháng 3 — và ra lệnh phát động cuộc tấn công sarin chỉ trong vòng 48 giờ.* | — | — |  |
| 2-10 | `2.05#6`–`#7` | H | T1 | `t8_weapons_of_mass_destruction`, `still` | *Còn Chữ ký tâm lý bất biến của hắn chính là nhu cầu cưỡng chế hiện thực hóa kịch bản ngày tận thế mà hắn đã tiên tri. Hắn khao khát chứng minh cho các đệ tử thấy rằng dự ngôn chiến tranh thế giới thứ ba của mình đang thực sự diễn ra.* | — | — |  |
| 2-11 | `2.07#1` | D | T1 | `t8_matsumoto_night_1994`, `pan` | *Quá trình điều tra sau đó đã vạch trần quỹ đạo leo thang tội ác kéo dài suốt nhiều năm của tổ chức này.* | — | — |  |
| 2-12 | `2.07#2`–`#5` | D | T6 dòng thời gian | `t8_sarin_synthesis_laboratory`, `still` | *Nấc thứ nhất · Yoga và bay bổng* → *Nấc thứ hai · Cưỡng đoạt và giam giữ* → *Nấc thứ ba · Ám sát năm 1989* → *Nấc thứ tư · Matsumoto năm 1994* | — | — |  |
| 2-13 | `2.07#6`–`#7` | D | T1 | `t8_sakamoto_lawyer_desk`, `pull` | *Chuỗi hành vi cho thấy mức độ bạo lực liên tục tăng tiến khi giáo phái ngày càng lún sâu vào ảo tưởng quyền lực. Và thảm kịch tàu điện ngầm Tokyo chính là điểm bùng nổ cuối cùng của quỹ đạo leo thang tàn bạo đó.* | — | — |  |
| 2-14 | `2.08#1`–`#2` | H | T1 | `t8_mountain_grave_memorial`, `still` | *Một tổ chức tôn giáo tự xưng là mang lại sự giác ngộ tâm linh lại sở hữu cả một kho vũ khí hủy diệt hàng loạt. Cơ chế dung nạp kích thích đã khiến ngưỡng thỏa mãn của giáo phái liên tục bị đẩy xa hơn, từ những trò lừa bịp nhỏ cho đến hành vi khủng bố tàn khốc.* | — | — |  |
| 2-15 | `2.08#3`–`#4` | H | T1 | `t8_asahara_shadow_profile`, `pull` | *Làm thế nào một kẻ mù lòa từng bán thuốc giả lại có thể tập hợp và thao túng cả một đội ngũ trí thức xuất chúng để chế tạo cỗ máy tử thần ấy? Câu trả lời nằm sâu trong những góc khuất tăm tối nhất của tâm lý học hành vi.* | — | — |  |
| 2-16 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC** | — | ⊘ | ◼ |

### HỒI 3 — NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC · nền chủ đạo `t8_asahara_shadow_profile`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1`–`#2` | H | T1 | `t8_asahara_shadow_profile`, `pull` | *Đứng đầu giáo phái Aum Shinrikyo là một người đàn ông mang tên Shoko Asahara, tên thật là Chizuo Matsumoto. Hắn sinh ra trong một gia đình nghèo đông con tại tỉnh Kumamoto, bị mù một mắt và mắt còn lại suy giảm thị lực nghiêm trọng do bệnh bẩm sinh.* | — | — |  |
| 3-02 | `3.02#3` | H | T1 | `t8_todai_red_gate_shadow`, `still` | *Thời trẻ, Matsumoto từng nhiều lần thi trượt kỳ thi tuyển sinh vào Đại học Tokyo danh giá.* | — | — |  |
| 3-03 | `3.02#4` | H | T1 | `t8_chinese_herbal_apothecary`, `pull` | *Hắn từng mở phòng khám châm cứu và phải nhận án phạt vì buôn bán thuốc đông y giả.* | — | — |  |
| 3-04 | `3.02#5` | H | T4 trích dẫn | `t8_asahara_shadow_profile`, `still` | *Một kẻ có trình độ học vấn chắp vá, ngoại hình luộm thuộm và nhân cách mang đậm nét ái kỷ bệnh lý.* | — | — |  |
| 3-05 | `3.02#6`–`#7` | H | T1 | `t8_devotion_altar_kneeling`, `pan` | *Thế nhưng, quỳ gối dưới chân người đàn ông mù lòa ấy lại là những trí thức ưu tú nhất của đất nước Nhật Bản. Họ sẵn sàng dâng hiến toàn bộ tài sản, lý trí và lương tâm của mình cho một kẻ từng bị xã hội khinh thường.* | — | — |  |
| 3-06 | `3.03#1`–`#2` | D | T2 thẻ hồ sơ | `t8_dossier_elite_scientists`, `still` | *Hồ sơ của ban lãnh đạo giáo phái Aum khiến bất kỳ ai cũng phải ngỡ ngàng trước hàm lượng chất xám mà tổ chức này sở hữu. Người phụ trách Bộ Hóa học của giáo phái là Masami Tsuchiya, thạc sĩ hóa học hữu cơ xuất sắc của Đại học Tsukuba danh tiếng.* | — | — |  |
| 3-07 | `3.03#3` | D | T1 | `t8_cosmic_physics_observatory`, `pull` | *Người đứng đầu Bộ Khoa học và Công nghệ là Hideo Murai, một nhà vật lý tài ba của Đại học Osaka từng nghiên cứu về bức xạ vũ trụ.* | — | — |  |
| 3-08 | `3.03#4` | D | T1 | `t8_virology_electron_microscope`, `still` | *Người phụ trách mảng y tế và vũ khí sinh học là Seiichi Endo, người từng theo học ngành virus học tại Đại học Kyoto.* | — | — |  |
| 3-09 | `3.03#5`–`#6` | D | T1 | `t8_cardiac_surgery_theatre`, `pan` | *Một thành viên cốt cán khác là Bác sĩ Tomomasa Nakagawa, tốt nghiệp đại học y khoa. Và đặc biệt hơn cả, phụ trách hệ thống bệnh viện của giáo phái là Bác sĩ Ikuo Hayashi, chuyên gia tim mạch tốt nghiệp Đại học Keio danh giá và từng là bác sĩ trưởng khoa tại bệnh viện quốc gia.* | — | — |  |
| 3-10 | `3.04#1` | H | T4 trích dẫn | `t8_stethoscope_abandoned_drain`, `still` | *Một bác sĩ tim mạch từng dành cả cuộc đời để giành giật sự sống cho người bệnh, những nhà khoa học với tương lai học thuật rực rỡ.* | — | — |  |
| 3-11 | `3.04#2`–`#3` | H | T1 | `t8_intellectual_hubris_chess`, `pull` | *Tại sao họ lại từ bỏ đỉnh cao danh vọng để rồi chế tạo vũ khí hủy diệt chính đồng bào của mình? Điều gì đã đánh sập toàn bộ hệ thống phòng thủ lý trí của những bộ óc thông minh nhất đất nước?* | — | — |  |
| 3-12 | `3.05#1` | C | T9 thuật ngữ | `t8_tokyo_stock_crash_1990`, `still` | **Sự trống rỗng hiện sinh** *(Existential Vacuum)* | — | ✦ Cáo |  |
| 3-13 | `3.05#2`–`#3` | C | T1 | `t8_corporate_salaryman_cogs`, `pull` | *Vào đầu thập niên 90, nước Nhật trải qua sự sụp đổ kinh hoàng của nền kinh tế bong bóng. Xã hội Nhật Bản lúc bấy giờ vận hành như một cỗ máy áp lực khổng lồ, nơi mỗi cá nhân bị ép phải trở thành những bánh răng vô danh trong các tập đoàn lớn.* | — | — |  |
| 3-14 | `3.05#4` | C | T1 | `t8_yoga_meditation_incense`, `still` | *Nhiều thanh niên trí thức đạt điểm số tuyệt đối trong học tập nhưng tâm hồn lại hoàn toàn trống rỗng về ý nghĩa cuộc đời và mất phương hướng giá trị.* | — | — |  |
| 3-15 | `3.05#5`–`#6` | C | T1 | `t8_asahara_shadow_profile`, `pan` | *Chính vào lúc những bộ óc xuất sắc ấy cảm thấy cô đơn và lạc lõng nhất, Shoko Asahara đã xuất hiện với một chiếc bẫy ngôn từ được ngụy trang hoàn hảo. Hắn khéo léo lồng ghép các khái niệm tâm linh phương Đông với các thuật ngữ khoa học như cơ học lượng tử, trường năng lượng và tận thế luận.* | — | — |  |
| 3-16 | `3.05#7` | C | T1 | `t8_moral_rationalization_books`, `still` | *Cách tiếp cận ngụy khoa học này đã đánh trúng cơn khát tìm kiếm ý nghĩa siêu nghiệm của giới sinh viên tinh hoa.* | — | — |  |
| 3-17 | `3.06#1`–`#2` | H | T1 | `t8_intellectual_hubris_chess`, `pull` | *Những người có học thức cao thường có một điểm yếu tâm lý chí mạng: Cái tôi trí tuệ quá lớn. Họ luôn tin rằng bản thân quá thông minh và duy lý để có thể bị một kẻ khác thao túng hoặc lừa gạt.* | — | — |  |
| 3-18 | `3.06#3`–`#4` | H | T1 | `t8_moral_rationalization_books`, `still` | *Khi Asahara trao cho họ cảm giác được trở thành những người được chọn nắm giữ chân lý cứu rỗi vũ trụ, chiếc bẫy kiêu ngạo đã sập xuống. Trí thông minh phi thường của họ không hề bảo vệ được họ, mà ngược lại trở thành công cụ đắc lực để họ tự hợp lý hóa cho những hành vi tàn bạo nhất.* | — | — |  |
| 3-19 | `3.07#1`–`#2` | C | T1 | `t8_yoga_meditation_incense`, `pull` | *Để duy trì cuộc sống hai mặt, các đệ tử trí thức đã vận dụng triệt để cơ chế tâm lý mang tên Chia ngăn nhận thức. Họ khóa chặt thế giới đời thường gồm gia đình, bạn bè và đạo đức xã hội vào một ngăn riêng biệt, và cách ly hoàn toàn với thế giới bí mật trong căn cứ Satyam.* | — | — |  |
| 3-20 | `3.07#3`–`#5` | C | T1 | `t8_devotion_altar_kneeling`, `pan` | *Đồng thời, giáo chủ nhồi sọ họ bằng kỹ thuật Vật hóa và phi nhân hóa nạn nhân. Trong mắt các nhà khoa học Aum, những người bình thường ngoài xã hội không còn là những sinh linh có cha mẹ và con cái, mà bị coi là những cá nhân mang nghiệp chướng nặng nề cản trở kỷ nguyên mới. Tiếng khóc van xin hay sinh mạng của người vô tội bị giáng cấp thành những dữ liệu thí nghiệm vô cảm trong phòng lab.* | — | — |  |
| 3-21 | `3.07#6`–`#8` | C | T1 | `t8_bio_incubator_pathogens`, `still` | *Và bi kịch tàn khốc không kém đã đổ ập xuống gia đình của chính những trí thức tinh hoa ấy. Cha mẹ của họ, những người từng tự hào về những đứa con đỗ thủ khoa, đã hoàn toàn sụp đổ danh tính khi biết con mình trở thành kẻ khủng bố. Nhiều bậc phụ huynh phải từ bỏ công việc, quỳ gối xin lỗi trước công chúng trong nỗi cay đắng tột cùng suốt phần đời còn lại.* | — | — |  |
| 3-22 | `3.08#1`–`#3` | H | T1 | `t8_broken_hippocratic_oath`, `pan` | *Trí tuệ khi bị ngắt kết nối khỏi lòng trắc ẩn sẽ trở thành thứ vũ khí nguy hiểm nhất trên đời. Sự phân mảnh tâm trí đã cho phép những con người từng được xã hội tôn kính trở thành những kẻ gieo rắc tử thần mà không hề cảm thấy cắn rứt lương tâm. Thế nhưng, để biến sự mê muội ấy thành hành động tàn sát thực tế, giáo phái còn sử dụng những công nghệ kiểm soát tâm trí tinh vi và tàn bạo hơn thế rất nhiều.* | — | — |  |
| 3-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **MA THUẬT TẨY NÃO & KHÁI NIỆM POA** | — | ⊘ | ◼ |

### HỒI 4 — MA THUẬT TẨY NÃO & KHÁI NIỆM POA ĐẪM MÁU · nền chủ đạo `t8_poa_twisted_doctrine`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1`–`#2` | H | T1 | `t8_concrete_cell_isolation`, `pull` | *Bên trong các khu trại khép kín của giáo phái Aum, các tín đồ bị cô lập hoàn toàn với thế giới bên ngoài. Họ bị tịch thu toàn bộ giấy tờ tùy thân, cắt đứt liên lạc với cha mẹ và không được tiếp cận bất kỳ nguồn tin tức độc lập nào.* | — | — |  |
| 4-02 | `4.02#3`–`#4` | H | T1 | `t8_malnutrition_solitary_bowl`, `still` | *Nhưng thủ đoạn tàn độc nhất nhằm triệt tiêu ý chí tự do chính là kỹ thuật làm suy kiệt thể xác có hệ thống. Các thành viên chỉ được phép ngủ hai đến ba tiếng mỗi ngày và phải duy trì chế độ ăn uống vô cùng kham khổ thiếu chất dinh dưỡng.* | — | — |  |
| 4-03 | `4.02#5` | H | T1 | `t8_frontal_lobe_brain_scan`, `pan` | *Khi cơ thể rơi vào trạng thái kiệt quệ kéo dài, vùng vỏ não trước trán phụ trách tư duy phản biện và phán đoán logic sẽ suy giảm nghiêm trọng, khiến con người trở nên phục tùng tuyệt đối.* | — | — |  |
| 4-04 | `4.03#1`–`#2` | D | T1 | `t8_psi_headgear_electrodes`, `still` | *Hồ sơ điều tra đã làm sáng tỏ những thiết bị kỳ dị mà giáo phái sử dụng để thao túng não bộ của các đệ tử. Chúng phát minh ra một chiếc mũ gắn đầy điện cực mang tên PSI và bắt các tín đồ phải đội liên tục nhiều giờ liền.* | — | ✦ Sói |  |
| 4-05 | `4.03#3`–`#4` | D | T1 | `t8_hallucinogen_ritual_hall`, `pull` | *Giáo phái rêu rao rằng thiết bị này sẽ đồng bộ hóa sóng não của người đội với tần số sóng não của giáo chủ, và thu phí hàng nghìn đô la mỗi tháng cho mỗi chiếc mũ. Ngoài ra, cảnh sát còn phát hiện giáo phái bí mật sử dụng các loại chất gây ảo giác cực mạnh như LSD và thuốc hướng thần trong các nghi lễ kín trong bóng tối.* | — | — |  |
| 4-06 | `4.03#5` | D | T1 | `t8_bio_incubator_pathogens`, `still` | *Dưới tác động của hóa chất và sự suy kiệt thần kinh, các trí thức trẻ thực sự tin rằng họ đã nhìn thấy hào quang của đấng cứu thế và hoàn toàn mất đi khả năng hoài nghi.* | — | — |  |
| 4-07 | `4.04#1` | H | T9 thuật ngữ | `t8_poa_twisted_doctrine`, `still` | **Poa** *(Tibetan Phowa — Chuyển di tâm thức)* | — | — |  |
| 4-08 | `4.04#2` | H | T1 | `t8_buddhist_mandala_distortion`, `pull` | *Trong truyền thống Phật giáo Tây Tạng, Poa là một pháp môn thiền định thanh tịnh giúp chuyển di tâm thức khi cận tử.* | — | — |  |
| 4-09 | `4.04#3`–`#4` | H | T4 trích dẫn | `t8_broken_hippocratic_oath`, `still` | *Thế nhưng Asahara đã đánh tráo khái niệm thiêng liêng ấy thành một học thuyết biện minh cho hành vi tước đoạt mạng sống con người. Hắn biến một tội ác tàn bạo thành một hành động được ngụy trang dưới vỏ bọc đạo đức cao cả.* | — | — |  |
| 4-10 | `4.05#1`–`#2` | C | T1 | `t8_apocalypse_prophecy_scroll`, `pull` | *Asahara rao giảng rằng thế giới thực tại đã bị ô uế và sắp sửa bước vào cuộc chiến tranh hạt nhân hủy diệt toàn nhân loại. Hắn tuyên bố rằng những người bình thường nếu tiếp tục sống sẽ chỉ tích tụ thêm ác nghiệp và chắc chắn phải đọa vào cõi địa ngục.* | — | ✦ Cáo |  |
| 4-11 | `4.05#3`–`#4` | C | T1 | `t8_devotion_altar_kneeling`, `still` | *Do đó, việc chấm dứt sinh mạng của họ trước khi họ kịp phạm thêm tội lỗi không phải là một tội ác, mà là một hành vi đại từ bi để giải thoát linh hồn họ. Đây chính là đỉnh cao của Kỹ thuật Trung hòa đạo đức và Ngắt kết nối lương tâm.* | — | — |  |
| 4-12 | `4.05#5`–`#6` | C | T1 | `t8_moral_rationalization_books`, `pan` | *Bằng cách đảo ngược hoàn toàn chuẩn mực thiện ác, hung thủ tin rằng đôi tay mình đã làm việc thiện cứu rỗi nạn nhân. Đồng thời, cơ chế ngoại hóa trách nhiệm khiến họ tin rằng mọi hành động của mình chỉ là công cụ thực thi ý chí của Đấng tối cao.* | — | — |  |
| 4-13 | `4.06#1`–`#2` | H | T1 | `t8_dr_hayashi_umbrella_subway`, `still` | *Chính sự ngụy biện ma quỷ ấy đã làm tê liệt hoàn toàn lương tâm của Bác sĩ Ikuo Hayashi, người từng đứng đầu một khoa tim mạch uy tín. Vào buổi sáng ngày 20 tháng 3, chính đôi bàn tay từng cứu sống hàng nghìn bệnh nhân đã dùng đầu ô chọc thủng hai túi sarin trên tuyến tàu Chiyoda.* | — | — |  |
| 4-14 | `4.06#3` | H | T4 trích dẫn | `t8_tokyo_court_witness_stand`, `pull` | *Hãy lắng nghe khoảnh khắc người đàn ông ấy đối diện với chính mình trước vành móng ngựa.* | — | →N2 |  |
| 4-15 | `4.08#1`–`#2` | N2 | T4 lời kể | `t8_grand_courtroom_proceedings`, `still` | *Trước tòa án, tôi không tìm kiếm bất kỳ sự tha thứ nào cho bản thân mình. Tôi từng là một bác sĩ với lời thề bảo vệ sự sống con người bằng mọi giá.* | — | ✦ Mèo |  |
| 4-16 | `4.08#3`–`#5` | N2 | T1 | `t8_tokyo_court_witness_stand`, `pull` | *Vậy mà tôi đã để cho giáo lý mù quáng làm tê liệt lý trí, để rồi gây ra nỗi đau đớn không thể cứu vãn cho những đồng bào vô tội. Khi nhìn vào mắt của thân nhân các nạn nhân, tôi hiểu rằng không có sự cứu rỗi nào dành cho tội lỗi của mình ngoài việc thành khẩn khai báo toàn bộ sự thật. Tôi quỳ xuống xin nhận mọi sự trừng phạt nghiêm khắc nhất của pháp luật.* | — | — |  |
| 4-17 | `4.09#1`–`#2` | H | T1 | `t8_tokyo_court_gavel_strike`, `still` | *Lời khai thành khẩn và chi tiết của Bác sĩ Hayashi đã trở thành chìa khóa quyết định giúp cơ quan điều tra bóc trần toàn bộ cơ cấu vận hành ngầm của giáo phái. Thế nhưng, một biến cố bạo lực khác đã xảy ra ngay trước mắt công chúng.* | — | — |  |
| 4-18 | `4.09#3` | H | T1 | `t8_murai_assassination_cameras`, `pan` | *Ngày 23 tháng 4 năm 1995, nhà vật lý Hideo Murai, nhân vật số hai của Aum, đã bị ám sát ngay trước ống kính truyền hình bên ngoài trụ sở Tokyo nhằm bịt đầu mối bí mật vũ khí.* | — | — |  |
| 4-19 | `4.09#4` | H | T1 | `t8_police_convoy_kamikuishiki`, `still` | *Mặc dù vậy, vòng vây pháp lý vẫn siết chặt không ngừng quanh kẻ chủ mưu tối cao.* | — | — |  |
| 4-20 | `4.09#5` | H | T5 ngày | `t8_hidden_ceiling_hideout`, `still` | *NGÀY PHÁT HIỆN* · **16 · 05 · 1995** | — | — |  |
| 4-21 | `4.09#6`–`#7` | H | T1 | `t8_asahara_shadow_profile`, `pan` | *Kẻ từng tự phong mình là Đấng cứu thế của nhân loại ngồi co ro trong bóng tối, run rẩy bên cạnh một bọc tiền mặt trị giá gần mười triệu yên và các thỏi vàng. Chiếc mặt nạ thần thánh rơi xuống, phơi bày sự trơ trọi và nỗi sợ hãi hèn hạ của một kẻ lừa đảo khi bản ngã ái kỷ sụp đổ hoàn toàn.* | — | — |  |
| 4-22 | `4.11#1`–`#3` | D | T1 | `t8_tokyo_court_gavel_strike`, `still` | *Sự sụp đổ của Shoko Asahara trong hốc trần nhà đã vạch trần bản chất thật sự của kẻ cầm đầu giáo phái độc hại. Không hề có phép màu bay bổng, không có hào quang tâm linh nào cứu giúp hắn trước sự truy lùng của công lý. Hắn chỉ là một kẻ thao túng tàn nhẫn, sẵn sàng hy sinh toàn bộ tín đồ để bảo toàn sự an toàn và lòng tham của bản thân.* | — | — |  |
| 4-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT LỊCH SỬ & BÀI HỌC** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT LỊCH SỬ & BÀI HỌC VỀ SỰ TỰ DO TƯ TƯỞNG · nền chủ đạo `t8_tokyo_dawn_restored_peace`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#2` | H | T1 | `t8_grand_courtroom_proceedings`, `pull` | *Các phiên tòa xét xử giáo phái Aum Shinrikyo kéo dài suốt hơn hai thập kỷ, trở thành một trong những trang hồ sơ tư pháp đồ sộ và phức tạp nhất trong lịch sử Nhật Bản. Trước tòa án, Shoko Asahara liên tục giả điên, lẩm bẩm những câu vô nghĩa và từ chối giao tiếp với cả luật sư lẫn các thẩm phán.* | — | — |  |
| 5-02 | `5.02#3`–`#5` | H | T1 | `t8_tokyo_court_gavel_strike`, `still` | *Đó chính là phản ứng điển hình của Sự sụp đổ cái tôi ái kỷ và Sự tự thương hại bệnh lý. Kẻ từng quen đứng trên đỉnh cao quyền lực tuyệt đối đã không thể đối diện với sự trần trụi của chính mình khi bị tước bỏ mọi đặc quyền. Hắn thà chọn cách thu mình vào vỏ bọc câm lặng hơn là thừa nhận sự thất bại thảm hại của ảo tưởng vĩ cuồng.* | — | — |  |
| 5-03 | `5.03#1` | D | T1 | `t8_thirteen_death_verdicts`, `pan` | *Sau quá trình xét xử nghiêm minh và thận trọng, Tòa án Tối cao Nhật Bản đã tuyên phạt mức án cao nhất: án tử hình đối với Shoko Asahara và mười hai đệ tử then chốt của giáo phái.* | — | ✦ Sói |  |
| 5-04 | `5.03#2` | D | T2 thẻ hồ sơ | `t8_dossier_elite_scientists`, `still` | *Trong số những kẻ phải đền tội có nhà hóa học Masami Tsuchiya, chuyên gia virus học Seiichi Endo, nhà mua sắm vũ khí Kiyohide Hayakawa và bác sĩ Tomomasa Nakagawa.* | — | — |  |
| 5-05 | `5.03#3`–`#5` | D | T1 | `t8_tokyo_court_gavel_strike`, `pull` | *Riêng Bác sĩ Ikuo Hayashi, nhờ sự thức tỉnh, thái độ ăn năn chân thành và lời khai hợp tác toàn diện giúp phá án, đã nhận mức án tù chung thân. Vào tháng 7 năm 2018, bản án tử hình bằng hình thức treo cổ đã chính thức được thi hành đối với Shoko Asahara và toàn bộ mười hai đồng phạm then chốt. Sự trừng phạt nghiêm khắc của pháp luật đã khép lại một chương đen tối kéo dài hơn hai mươi ba năm trong tâm thức xã hội Nhật Bản.* | — | — |  |
| 5-06 | `5.04#1`–`#2` | H | T1 | `t8_tokyo_detention_house_dawn`, `still` | *Vụ án đã giáng một cú sốc chí mạng vào niềm tin xã hội và thúc đẩy cuộc đại cải tổ thể chế pháp luật chưa từng có. Nhật Bản đã sửa đổi toàn diện Đạo luật Tổ chức Tôn giáo và ban hành các đạo luật đặc biệt nhằm kiểm soát chặt chẽ các tổ chức có nguy cơ khủng bố tập thể.* | — | — |  |
| 5-07 | `5.04#3` | H | T1 | `t8_murakami_underground_book`, `pull` | *Trong cuốn sách tư liệu nổi tiếng mang tên “Ngầm”, nhà văn Haruki Murakami đã dành nhiều tháng phỏng vấn hàng chục nạn nhân và cả những cựu thành viên của giáo phái Aum.* | — | — |  |
| 5-08 | `5.04#4`–`#6` | H | T1 | `t8_fragile_boundary_mirror`, `pan` | *Ông nhận ra rằng: ranh giới giữa một con người bình thường và một kẻ cuồng tín mỏng manh hơn chúng ta tưởng rất nhiều. Khi xã hội quá áp lực và vô cảm, bất kỳ tâm hồn cô đơn nào cũng có thể tìm đến một chiếc phao cứu sinh độc hại để bấu víu. Và cái ác thực sự không phải là những con quái vật từ bên ngoài, mà nảy sinh ngay từ sự thiếu thốn kết nối nhân văn trong lòng cuộc sống hiện đại.* | — | — |  |
| 5-09 | `5.05#1`–`#2` | C | T1 | `t8_tokyo_dawn_restored_peace`, `still` | *Hồ sơ Aum Shinrikyo để lại một bài học cảnh tỉnh sâu sắc cho toàn nhân loại về giới hạn của trí tuệ con người. Bằng cấp học thuật cao và chỉ số thông minh logic không bao giờ là tấm khiên bảo vệ chúng ta trước những thủ đoạn thao túng tâm lý tinh vi.* | — | ✦ Cáo |  |
| 5-10 | `5.05#3`–`#4` | C | T1 | `t8_tokyo_dawn_fog`, `pull` | *Ngược lại, khi những bộ óc xuất chúng nhất bị mất phương hướng về mặt giá trị sống, họ có thể trở thành công cụ hủy diệt nguy hiểm nhất của cái ác. Sự cuồng tín luôn bắt đầu từ những lời hứa hẹn ngọt ngào về một chân lý tuyệt đối đứng trên mọi quy chuẩn đạo đức thông thường.* | — | — |  |
| 5-11 | `5.06#1` | H | T1 | `t8_mountain_grave_memorial`, `still` | *Để bảo vệ bản thân và những người thân yêu trước các tổ chức thao túng tâm trí độc hại, kênh Amber Eyes xin đúc kết bốn tín hiệu cảnh báo đỏ sinh tồn từ hồ sơ lịch sử này.* | — | — |  |
| 5-12 | `5.06#2` | H | T8 cờ | `t8_redflag1_social_isolation`, `still` | *01* · **CẢNH BÁO ĐỎ 1 — CÔ LẬP XÃ HỘI & CẮT ĐỨT MỐI QUAN HỆ HỖ TRỢ** | — | — |  |
| 5-13 | `5.06#3` | H | T1 | `t8_corporate_salaryman_cogs`, `pull` | *Bất kỳ tổ chức lành mạnh nào cũng tôn trọng gia đình và các mối liên kết xã hội của bạn; nếu một nhóm tìm cách tách bạn khỏi người thân và kiểm soát nguồn thông tin, hãy lập tức rời đi.* | — | — |  |
| 5-14 | `5.06#4` | H | T8 cờ | `t8_redflag2_physical_exhaustion`, `still` | *02* · **CẢNH BÁO ĐỎ 2 — KỸ THUẬT LÀM SUY KIỆT THỂ CHẤT & TRIỆT TIÊU TƯ DUY PHẢN BIỆN** | — | — |  |
| 5-15 | `5.06#5` | H | T1 | `t8_malnutrition_solitary_bowl`, `pull` | *Hãy cảnh giác cao độ với những nơi ép buộc bạn phải thức khuya liên tục, nhịn ăn khắc nghiệt hoặc lao động quá sức dưới danh nghĩa thanh lọc tâm hồn.* | — | — |  |
| 5-16 | `5.06#6` | H | T8 cờ | `t8_redflag3_cult_of_personality`, `still` | *03* · **CẢNH BÁO ĐỎ 3 — SÙNG BÁI CÁ NHÂN TUYỆT ĐỐI & CẤM ĐOÁN** | — | — |  |
| 5-17 | `5.06#7` | H | T1 | `t8_devotion_altar_kneeling`, `pull` | *Một người thầy chân chính luôn khuyến khích học trò tự do suy nghĩ và kiểm chứng sự thật; chỉ có những kẻ thao túng mới coi lời nói của mình đứng trên luật pháp và quy kết sự nghi ngờ là tội lỗi.* | — | — |  |
| 5-18 | `5.06#8` | H | T8 cờ | `t8_redflag4_moral_inversion`, `still` | *04* · **CẢNH BÁO ĐỎ 4 — NGỤY BIỆN ĐẢO NGƯỢC ĐẠO ĐỨC & KÍCH ĐỘNG THÙ HẬN** | — | — |  |
| 5-19 | `5.06#9`–`#10` | H | T1 | `t8_fragile_boundary_mirror`, `pan` | *Hãy kiên quyết từ chối bất kỳ giáo lý nào rao giảng rằng việc gây tổn hại cho người khác là một hành vi từ bi vì mục đích cao cả. Chân lý đích thực không bao giờ được xây dựng trên sự lừa dối, sợ hãi và nỗi đau của đồng loại.* | — | — |  |
| 5-20 | `5.08#1` | H | T1 | `t8_tokyo_dawn_restored_peace`, `still` | *Ánh sáng của tri thức chỉ thực sự có giá trị khi nó được soi đường bởi lòng trắc ẩn và sự tỉnh táo của lương tri.* | — | — |  |
| 5-21 | `5.08#2`–`#4` | H | T1 | `t8_tokyo_dawn_fog`, `pan` | *Cảm ơn quý vị đã đồng hành cùng Amber Eyes trong tập hồ sơ giải phẫu tâm lý ngày hôm nay. Hãy bấm đăng ký kênh, chia sẻ video và để lại góc nhìn của bạn ở phần bình luận bên dưới. Xin chào và hẹn gặp lại quý vị trong những tập hồ sơ tiếp theo.* | — | — |  |
| 5-22 | — | — | T1 | `t8_tokyo_dawn_restored_peace` | *HỒ SƠ TẬP 08 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật* | — | ⊘ |  |

**Tổng:** 108 shot · 171 câu · 33 element lời (5 hồi) · nền dùng 70 loại. Bảng dựng lại 06/11/2026 theo kịch bản viết lại 05/11/2026 (53 phần tử · 171 câu).
