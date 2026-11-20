# HỒ SƠ SẢN XUẤT TẬP 17 · "13 ĐỨA TRẺ TRONG NGỤC TÙ NGOẠI Ô — KIỂM SOÁT CƯỠNG CHẾ & CÚ NHẢY SINH TỒN"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 17: 13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Kiểm Soát Cưỡng Chế & Cú Nhảy Sinh Tồn (Hồ Sơ Gia Đình Turpin)** |
| Vụ án | Thảm kịch giam cầm và bạo hành 13 người con — Biệt thự ngoại ô Perris, California (14/01/2018) |
| Chủ đề | Kiểm soát cưỡng chế (Coercive Control), Hội chứng Điên cuồng đôi (Folie à Deux), Sự ấu trĩ hóa có chủ đích (Deliberate Infantilization) & Bản năng sinh tồn |
| Tổng thời lượng | **2035.0 s (~33 phút 54 giây)** · 5 hồi · **226 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Tổng đài viên 911 Hạt Riverside) · N2 (Đại diện y tế Bệnh viện Riverside) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap17.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.mp3` & `02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2026.0 s, kết thúc audio tại 2035.0 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **121.1 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.6 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **206.5 Hz**
- **Tổng đài viên 911 ($N1$ · Cừu):** F0 trung vị = **180.5 Hz**
- **Đại diện y tế ($N2$ · Mèo):** F0 trung vị = **284.1 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.60\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.24\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `faster-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.77%** (CER trung bình: **10.96%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.57 / 5.0** (Dải điểm: 1.64 – 3.52). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap17/xuat_ban/CanNghe_Tap17_higgs.md`](xuat_ban/CanNghe_Tap17_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.mp3`](xuat_ban/Tap17_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.wav`](xuat_ban/Tap17_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t17.json`](../../.work/timeline_s_t17.json) (2035.0 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap17/xuat_ban/Tap17.srt`](xuat_ban/Tap17.srt) (226 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep17_vi.json`](../../.work/quality_qc_utmos_ep17_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap17/xuat_ban/CanNghe_Tap17_higgs.md`](xuat_ban/CanNghe_Tap17_higgs.md)

---

## B4. Nhật ký dựng hình 19/11/2026 (VI/EN/JA)

- Bảng shot sinh bằng `.work/_gen_shots_t17.py`: 231 dòng, 130/130 nền, 1,7 shot/nền; `qc_bg_usage` + `qc_bg_shared` ĐẠT cả 3 ngôn ngữ. Bản kế hoạch cũ: `.work/_cu/t17_plans_20261119/`.
- **Lệch luật có chủ đích (người dùng chọn "dựng ngay"):** (1) soi 130 nền bằng montage thấy ~13 nền có chữ AI vẽ (kể cả nền thẻ kết "TURPIN DOSSIER"), 4 nền lộ mặt (`folie_a_deux_entwined_shadows`, `gifts_of_fear_protective_instinct`, `district_attorney_indictment_podium`, `redflag2_staged_social_media_facade`), 2 nền nghi V9 (`bathroom_sink_water_punishment`, `stunted_adult_victims_tragedy`) — CHƯA sinh lại; (2) chưa soi mắt ảnh tĩnh theo H20; (3) stems giọng đã bị dọn ⇒ dùng stems GIẢ cắt từ master (`.work/_make_pseudo_stems_t17.py`, có lẫn nhạc nền) chỉ để vẽ sóng badge — `qc_wave_gate` ĐẠT nhưng A14 (`qc_voice_gap`, `qc_voice_sentence`) KHÔNG chạy được; (4) CER VI 10,77% (ngưỡng < 2%) chưa xử lý.
- `edition.py` Tập 17: thêm `mux_af` có `latency=1` (A7). Intro EN/JA Tập 17 là bản COPY từ `intro_kenh_EN.mov` / `intro_kenh_JA_t16.mov` (chưa có intro JA chuẩn).
- Bẫy gặp: `edition.py` trỏ file intro `_t17` chưa tồn tại ⇒ ffmpeg báo lỗi nhưng renderer vẫn chạy tiếp ⇒ phải đọc log, không chỉ chờ `DONE`. `package.py` đọc `.work/audio_master_*_t17.wav` (đã bị dọn) ⇒ phải chép lại từ `xuat_ban/*_master.wav`. `package.py` nhánh EN lỗi `CHU_CO_DINH_EN.md` thiếu trong `Tap17_EN` (sau bước ghép, mo_ta chưa sinh lại).
- Số đo: VI 2026,633 s / EN 1738,867 s / JA 2099,867 s (timeline 2026,64 / 1738,87 / 2099,88); LUFS −16,0; true peak mp4 VI −1,9 / EN −1,8 dBFS.

## 6. DANH SÁCH SHOT — TẬP 17 (VI)

Bảng sinh tự động bởi `.work/_gen_shots_t17.py` (cùng mã shot và nền cho cả VI/EN/JA — H17). *Chữ* = nguyên văn câu của shot (H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ⇒ **đậm**.

### INTRO KÊNH · 0,00–22,41 s

Đặt `assets/brand/intro_kenh.mov` tại 0,00 s. Không câu thoại nào thuộc intro.

### HỒI 1

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.02#1` (9,8 s) | H | T1 | `t17_perris_suburban_mist_dawn`, `pan` | *Rạng sáng ngày 14 tháng 1 năm 2018, thành phố Perris thuộc hạt Riverside, bang California vẫn đang chìm trong màn sương lạnh giá.* | — | ✦ Cú |  |
| 1-02 | `1.02#2` (6,6 s) | H | T1 | `t17_perris_suburban_mist_dawn`, `pull` | *Tại một ngôi nhà trên đường Muir Woods Road, một cánh cửa sổ hé mở trong sự tĩnh lặng tuyệt đối.* | — | — |  |
| 1-03 | `1.02#3` (7,0 s) | H | T1 | `t17_window_escape_sill_shadow`, `still` | *Một thiếu nữ gầy gò, nhỏ bé đến mức trông như một đứa trẻ, trèo qua bậu cửa và bước ra ngoài.* | — | — |  |
| 1-04 | `1.02#4` (5,0 s) | H | T1 | `t17_window_escape_sill_shadow`, `push` | *Trong lồng ngực cô gái trẻ là nỗi sợ hãi tột cùng nếu bị cha mẹ phát hiện.* | — | — |  |
| 1-05 | `1.02#5` (4,6 s) | H | T1 | `t17_deactivated_cellphone_clutched_hand`, `pan` | *Trong tay cô là một chiếc điện thoại di động cũ đã bị ngắt dịch vụ mạng.* | — | — |  |
| 1-06 | `1.02#6` (6,7 s) | H | T1 | `t17_deactivated_cellphone_clutched_hand`, `pull` | *Cô không biết địa chỉ chính xác của ngôi nhà mình, vì gần như chưa bao giờ được tự do bước ra thế giới bên ngoài.* | — | — |  |
| 1-07 | `1.02#7` (7,6 s) | H | T1 | `t17_new_a1_01_frosted_window_pane`, `still` | *Sự cô lập nghiệt ngã suốt nhiều năm đã biến khu phố ngoại ô quen thuộc thành một mê cung đầy bất trắc đối với cô.* | — | — |  |
| 1-08 | `1.04#1` (4,9 s) | H | T1 | `t17_two_year_escape_plan_secret_corner`, `push` | *Thiếu nữ quả cảm ấy tên là Jordan Turpin, khi đó mười bảy tuổi.* | — | — |  |
| 1-09 | `1.04#2` (8,4 s) | H | T1 | `t17_two_year_escape_plan_secret_corner`, `pan` | *Theo cơ quan công tố, Jordan cùng một người em đã âm thầm lên kế hoạch tìm đường thoát thân suốt khoảng hai năm ròng rã.* | — | — |  |
| 1-10 | `1.04#3` (7,0 s) | H | T1 | `t17_new_a1_02_deserted_suburban_asphalt`, `pull` | *Cô biết rằng nếu kế hoạch thất bại, cái giá phải trả sẽ là những hình phạt vô cùng tàn khốc từ cha mẹ.* | — | — |  |
| 1-11 | `1.04#4` (7,6 s) | H | T1 | `t17_emergency_911_connection_signal`, `still` | *May mắn thay, tại Mỹ, một chiếc điện thoại đã ngắt dịch vụ vẫn có thể kết nối đến tổng đài khẩn cấp 911.* | — | — |  |
| 1-12 | `1.04#5` (7,7 s) | H | T1 | `t17_emergency_911_connection_signal`, `push` | *Khi đầu dây bên kia cất tiếng trả lời, Jordan cất lên một giọng nói non nớt, đứt quãng nhưng chứa đựng sự thật kinh hoàng.* | — | — |  |
| 1-13 | `1.04#6` (7,1 s) | H | T1 | `t17_dark_house_twelve_siblings_void`, `pan` | *Cô cho nhân viên trực ban biết mình có mười hai anh chị em và cha mẹ đang giam giữ họ trong ngôi nhà tăm tối.* | — | — |  |
| 1-14 | `1.04#7` (6,1 s) | H | T1 | `t17_dark_house_twelve_siblings_void`, `pull` | *Cuộc gọi định mệnh ấy đã kích hoạt một chiến dịch giải cứu làm chấn động toàn bộ xã hội Mỹ.* | — | — |  |
| 1-15 | `1.06#1` (8,3 s) | H | T1 | `t17_dispatch_audio_waveform_console`, `still` | *Trong suốt cuộc trò chuyện kéo dài hai mươi phút, nhân viên điều phối nhận ra những câu trả lời ngây thơ đến kỳ lạ của cô gái mười bảy tuổi.* | — | — |  |
| 1-16 | `1.06#2` (10,0 s) | H | T1 | `t17_dispatch_audio_waveform_console`, `push` | *Giữa một khu đô thị hiện đại của thế kỷ hai mươi mốt, sự thiếu hụt kiến thức cơ bản của cô gái là dấu hiệu rúng động của một quá trình bị cách ly nhận thức triệt để.* | — | — |  |
| 1-17 | `1.06#3` (7,8 s) | H | T1 | `t17_new_a1_03_broken_screen_cellphone_back`, `pan` | *Jordan không biết rõ địa chỉ nơi mình sinh sống và hoàn toàn xa lạ với nhiều khái niệm thông thường như thuốc men hay bác sĩ.* | — | — |  |
| 1-18 | `1.06#4` (6,4 s) | H | T1 | `t17_iron_chains_and_bedpost_shadows`, `pull` | *Cô kể rằng căn nhà vô cùng bẩn thỉu và các anh chị em của mình đã rất lâu không được tắm rửa.* | — | — |  |
| 1-19 | `1.06#5` (7,2 s) | H | T1 | `t17_iron_chains_and_bedpost_shadows`, `still` | *Nghiêm trọng hơn, cô tiết lộ một số người em đang bị xích chặt vào khung giường bằng những sợi dây xích sắt nặng nề.* | — | — |  |
| 1-20 | `1.06#6` (5,4 s) | H | T1 | `t17_evidence_photos_polaroid_clutch`, `push` | *Cô còn mang theo những bức ảnh chụp trong nhà, về sau trở thành những bằng chứng pháp lý then chốt.* | — | — |  |
| 1-21 | `1.06#7` (6,4 s) | H | T1 | `t17_evidence_photos_polaroid_clutch`, `pan` | *Lực lượng tuần tra của Văn phòng Cảnh sát trưởng Hạt Riverside ngay lập tức được điều động khẩn cấp đến hiện trường.* | — | — |  |
| 1-22 | `1.06#8` (7,8 s) | H | T1 | `t17_new_a1_04_hidden_nook_floorboards`, `pull` | *Một cuộc chạy đua nghẹt thở với thời gian bắt đầu nhằm bảo vệ an toàn cho thiếu nữ đang đứng đơn độc giữa trời đông lạnh giá.* | — | — |  |
| 1-23 | `1.07#1` (5,6 s) | N1 | T4 | `t17_dispatcher_headset_trembling_desk`, `still` | *Hãy hình dung cảm giác của một nhân viên tổng đài khẩn cấp khi tiếp nhận cuộc gọi vào rạng sáng hôm đó.* | — | ✦ Cừu |  |
| 1-24 | `1.07#2` (6,8 s) | N1 | T4 | `t17_dispatcher_headset_trembling_desk`, `push` | *Giọng nói ở đầu dây nghe non nớt và run rẩy như của một đứa trẻ lên mười, dù người gọi đã mười bảy tuổi.* | — | — |  |
| 1-25 | `1.07#3` (6,6 s) | N1 | T4 | `t17_new_a1_05_dim_ceiling_lightbulb_dust`, `pan` | *Cô gái nói chuyện rất khó khăn, nhiều từ ngữ giao tiếp thông dụng dường như hoàn toàn xa lạ với nhận thức của cô.* | — | — |  |
| 1-26 | `1.07#4` (8,0 s) | N1 | T4 | `t17_dispatcher_lifeline_monitor_night`, `pull` | *Khi nghe cô gái kể rằng các em mình đang bị khóa bằng xích sắt vào giường trong bóng tối, người trực ban cảm thấy lạnh toát sống lưng.* | — | — |  |
| 1-27 | `1.07#5` (10,8 s) | N1 | T4 | `t17_dispatcher_lifeline_monitor_night`, `still` | *Trực giác nghề nghiệp thôi thúc người trực ban phải giữ chặt đường dây, bởi trực giác ấy cảnh báo rằng chỉ một khoảnh khắc ngắt kết nối cũng có thể khiến một sinh mạng biến mất mãi mãi.* | — | — |  |
| 1-28 | `1.07#6` (7,0 s) | N1 | T4 | `t17_new_a1_06_rusty_metal_chain_links`, `push` | *Mỗi giây trôi qua trong cuộc gọi là một sự lo âu nghẹt thở cho sự an toàn tính mạng của cô gái ngoài góc phố.* | — | — |  |
| 1-29 | `1.07#7` (6,2 s) | N1 | T4 | `t17_new_a1_06_rusty_metal_chain_links`, `pan` | *Đó là kiểu cuộc gọi khẩn cấp đau đớn mà người làm nghề trực tổng đài không bao giờ có thể quên trong suốt cuộc đời.* | — | — |  |
| 1-30 | `1.09#1` (7,3 s) | H | T1 | `t17_deputy_campos_cruiser_fog_arrival`, `pull` | *Phó Cảnh sát trưởng Manuel Campos là một trong những sĩ quan đầu tiên tiếp cận vị trí của Jordan Turpin.* | — | — |  |
| 1-31 | `1.09#2` (8,4 s) | H | T1 | `t17_deputy_campos_cruiser_fog_arrival`, `still` | *Các cảnh sát sững sờ khi nhìn thấy một thiếu nữ mười bảy tuổi gầy gò, suy kiệt và nhỏ bé như một đứa trẻ tiểu học.* | — | — |  |
| 1-32 | `1.09#3` (8,8 s) | H | T1 | `t17_new_a1_07_blurred_cruiser_flashing_beacon`, `push` | *Sau khi xem xét những bức ảnh bằng chứng mà Jordan mang theo, lực lượng tuần tra lập tức ập đến ngôi nhà trên đường Muir Woods Road.* | — | — |  |
| 1-33 | `1.09#4` (8,8 s) | H | T1 | `t17_muir_woods_front_door_breach`, `pan` | *Người cha David Turpin và người mẹ Louise Turpin tỏ ra bối rối và kinh ngạc khi thấy cảnh sát xuất hiện trước cửa.* | — | — |  |
| 1-34 | `1.09#5` (8,0 s) | H | T1 | `t17_muir_woods_front_door_breach`, `pull` | *Bước chân qua cánh cửa, các điều tra viên đối diện với một không gian tối tăm, nồng nặc mùi hôi thối và ngập tràn rác rưởi.* | — | — |  |
| 1-35 | `1.09#6` (6,5 s) | H | T1 | `t17_new_a1_08_worn_carpet_stained_footsteps`, `still` | *Mười hai người con còn lại trong gia đình đang lặng lẽ chờ đợi sự giải thoát sau những năm tháng bị đày đọa.* | — | — |  |
| 1-36 | `1.10#1` (7,2 s) | D | T1 | `t17_house_of_horrors_dark_hallway`, `push` | *Theo biên bản của cơ quan chức năng, cảnh tượng bên trong ngôi nhà vượt xa mọi sức tưởng tượng của các sĩ quan tuần tra giàu kinh nghiệm.* | — | ✦ Sói |  |
| 1-37 | `1.10#2` (6,4 s) | D | T1 | `t17_house_of_horrors_dark_hallway`, `pan` | *Toàn bộ căn nhà tối đen như mực, không khí ngột ngạt và nồng nặc mùi chất thải, dù ngoài trời đã sáng rõ.* | — | — |  |
| 1-38 | `1.10#3` (4,4 s) | D | T1 | `t17_new_a1_09_radio_microphone_intercom_cord`, `pull` | *Một số nạn nhân đang bị khóa chặt vào khung giường bằng xích sắt và ổ khóa kiên cố.* | — | — |  |
| 1-39 | `1.10#4` (7,1 s) | D | T1 | `t17_stunted_adult_victims_tragedy`, `still` | *Ban đầu, các sĩ quan đều nghĩ rằng tất cả nạn nhân đều là trẻ em vì thể trạng của họ vô cùng nhỏ bé và suy kiệt.* | — | — |  |
| 1-40 | `1.10#5` (7,4 s) | D | T1 | `t17_stunted_adult_victims_tragedy`, `push` | *Nhưng sau đó, họ bàng hoàng phát hiện rằng bảy người trong số đó thực chất đã là người trưởng thành từ mười tám đến hai mươi chín tuổi.* | — | — |  |
| 1-41 | `1.11#1` (8,6 s) | H | T1 | `t17_suburban_facade_curtain_drawn`, `pan` | *Làm thế nào mà một ngục tù gia đình tàn nhẫn như vậy có thể tồn tại suốt nhiều năm giữa một khu dân cư ngoại ô yên bình?* | — | — |  |
| 1-42 | `1.11#2` (7,6 s) | H | T1 | `t17_suburban_facade_curtain_drawn`, `pull` | *Điều gì đã giúp cặp vợ chồng David và Louise Turpin che đậy tội ác trước hàng xóm và các cơ quan quản lý xã hội?* | — | — |  |
| 1-43 | `1.11#3` (8,0 s) | H | T1 | `t17_suburban_facade_curtain_drawn`, `still` | *Bức màn bí mật bắt đầu được vén lên, để lộ một vỏ bọc gia đình kiểu mẫu được dàn dựng công phu nhằm đánh lừa dư luận.* | — | — |  |
| 1-44 | `1.11#4` (8,9 s) | H | T1 | `t17_new_a1_10_suburban_storm_drain_curb`, `push` | *Chào mừng quý vị đến với kênh Amber Eyes, nơi chúng ta cùng giải phẫu tâm lý tội phạm và bóc tách những góc tối ẩn giấu sau cánh cửa gia đình.* | — | — |  |
| 1-45 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 02* · **NGỤC TÙ NGOẠI Ô VÀ VỎ BỌC HOÀN HẢO** | — | ⊘ | ◼ |

### HỒI 2

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (9,6 s) | H | T1 | `t17_computer_engineer_desk_blueprints`, `pan` | *Người cha David Allen Turpin khi bị bắt giữ năm mươi sáu tuổi, là một kỹ sư máy tính từng làm việc cho các tập đoàn quốc phòng danh tiếng.* | — | — |  |
| 2-02 | `2.02#2` (7,6 s) | H | T1 | `t17_computer_engineer_desk_blueprints`, `pull` | *Người mẹ Louise Anna Turpin bốn mươi chín tuổi, đảm nhận vai trò nội trợ và quản lý toàn bộ sinh hoạt gia đình.* | — | — |  |
| 2-03 | `2.02#3` (8,8 s) | H | T1 | `t17_new_a2_01_silicon_circuit_magnifier`, `still` | *Gia đình Turpin từng sinh sống tại bang Texas nhiều năm trước khi chuyển đến California và định cư tại Perris vào năm 2014.* | — | — |  |
| 2-04 | `2.02#4` (7,4 s) | H | T1 | `t17_financial_collapse_bankruptcy_notices`, `push` | *Bề ngoài, họ thể hiện hình ảnh một cặp vợ chồng có học thức, sùng đạo và luôn gìn giữ lối sống gia đình nề nếp.* | — | — |  |
| 2-05 | `2.02#5` (6,4 s) | H | T1 | `t17_financial_collapse_bankruptcy_notices`, `pan` | *David Turpin từng nhận mức thu nhập hàng trăm nghìn đô la mỗi năm từ công việc kỹ sư kỹ thuật cao.* | — | — |  |
| 2-06 | `2.02#6` (7,6 s) | H | T1 | `t17_financial_collapse_bankruptcy_notices`, `pull` | *Thế nhưng, phía sau nguồn thu nhập đáng mơ ước ấy là những khoản nợ tín dụng khổng lồ và hai lần nộp đơn xin phá sản.* | — | — |  |
| 2-07 | `2.02#7` (9,3 s) | H | T1 | `t17_new_a2_02_stamped_legal_envelope_stack`, `still` | *Sự khủng hoảng tài chính kết hợp áp lực nuôi dưỡng mười ba người con đã trở thành ngòi nổ làm sụp đổ hoàn toàn cơ chế tự chủ của cặp vợ chồng.* | — | — |  |
| 2-08 | `2.04#1` (10,5 s) | H | T1 | `t17_sandcastle_day_school_sign_closed`, `push` | *Để qua mặt cơ quan quản lý giáo dục địa phương, David Turpin đã đăng ký căn nhà của mình thành một trường tư thục tại gia mang tên Sandcastle Day School.* | — | — |  |
| 2-09 | `2.04#2` (8,3 s) | H | T1 | `t17_sandcastle_day_school_sign_closed`, `pan` | *Với tư cách là hiệu trưởng kiêm người hướng dẫn, David hợp thức hóa việc giữ tất cả các con trong nhà thay vì cho đến trường công lập.* | — | — |  |
| 2-10 | `2.04#3` (7,8 s) | H | T1 | `t17_disneyland_identical_shirts_facade`, `pull` | *Trên mạng xã hội, cặp vợ chồng này liên tục đăng tải những bức ảnh gia đình rạng rỡ trong những chuyến đi chơi xa hoa.* | — | — |  |
| 2-11 | `2.04#4` (8,3 s) | H | T1 | `t17_disneyland_identical_shirts_facade`, `still` | *Họ từng đưa các con đến công viên Disneyland và ba lần tổ chức các buổi lễ làm mới lời thề hôn nhân tại Las Vegas.* | — | — |  |
| 2-12 | `2.04#5` (7,7 s) | H | T1 | `t17_disneyland_identical_shirts_facade`, `push` | *Trong những bức ảnh đó, các con luôn mặc trang phục giống hệt nhau theo từng nhóm tuổi và xếp hàng ngay ngắn trước ống kính máy ảnh.* | — | — |  |
| 2-13 | `2.04#6` (7,9 s) | H | T1 | `t17_las_vegas_vow_renewal_glitz_shadow`, `pan` | *“Hiệu ứng Hào quang” của một gia đình đông con ngoan ngoãn và hạnh phúc đã tạo nên một điểm mù nhận thức hoàn hảo che mắt cộng đồng.* | — | — |  |
| 2-14 | `2.04#7` (7,7 s) | H | T1 | `t17_las_vegas_vow_renewal_glitz_shadow`, `pull` | *Người ngoài nhìn vào chỉ thấy một gia đình mẫu mực, mà không hề biết nỗi kinh hoàng đang diễn ra phía sau những nụ cười gượng gạo.* | — | — |  |
| 2-15 | `2.04#8` (8,7 s) | H | T1 | `t17_new_a2_03_row_of_identical_hangers`, `still` | *Thói quen đóng kín cửa và tôn trọng quyền riêng tư thái quá của xã hội hiện đại đã vô tình tạo nên một bức tường vô hình che chắn cho tội ác.* | — | — |  |
| 2-16 | `2.06#1` (7,7 s) | D | T1 | `t17_escalation_ropes_to_iron_chains`, `push` | *Dưới góc nhìn hồ sơ điều tra, quá trình ngược đãi và kiểm soát nạn nhân đã leo thang dần qua nhiều năm theo một chu kỳ tàn nhẫn.* | — | — |  |
| 2-17 | `2.06#2` (7,2 s) | D | T1 | `t17_escalation_ropes_to_iron_chains`, `pan` | *Ban đầu, khi còn ở bang Texas, các hình phạt chỉ dừng lại ở việc mắng mỏ, bắt đứng úp mặt vào tường và nhốt trong phòng kín.* | — | — |  |
| 2-18 | `2.06#3` (6,5 s) | D | T1 | `t17_escalation_ropes_to_iron_chains`, `pull` | *Khi sự thỏa mãn quyền lực cũ bị lờn, cặp vợ chồng bắt đầu dùng dây thừng để cố định các con vào giường nhằm trừng phạt.* | — | — |  |
| 2-19 | `2.06#4` (7,5 s) | D | T1 | `t17_new_a2_04_neon_flicker_motel_curtain`, `still` | *Đến khi một người con tìm cách tự cởi dây thoát ra, thủ đoạn gây án lập tức leo thang sang việc sử dụng xích sắt và ổ khóa kiên cố.* | — | — |  |
| 2-20 | `2.06#5` (7,2 s) | D | T1 | `t17_bathroom_sink_water_punishment`, `push` | *Lý do cho những hình phạt hà khắc này vô cùng phi lý, như việc các con lỡ rửa tay quá phần cổ tay hoặc chạm vào đồ chơi.* | — | — |  |
| 2-21 | `2.06#6` (6,3 s) | D | T1 | `t17_bathroom_sink_water_punishment`, `pan` | *Theo công tố viên, các nạn nhân hầu như không được tắm rửa, nhiều người chỉ được phép tắm một lần duy nhất trong suốt cả năm.* | — | — |  |
| 2-22 | `2.06#7` (6,6 s) | D | T1 | `t17_new_a2_05_heavy_padlock_hasp_closed`, `pull` | *Cả gia đình bị cưỡng ép sinh hoạt đảo lộn hoàn toàn, ban ngày phải ngủ trong phòng tối và chỉ được thức dậy vào ban đêm.* | — | — |  |
| 2-23 | `2.08#1` (7,2 s) | H | T1 | `t17_taunting_kitchen_pies_counter`, `still` | *Một trong những thủ đoạn bạo hành tinh thần tàn nhẫn nhất được cơ quan công tố nêu ra là sự tra tấn thông qua thức ăn.* | — | — |  |
| 2-24 | `2.08#2` (6,3 s) | H | T1 | `t17_taunting_kitchen_pies_counter`, `push` | *Mười ba người con bị kìm hãm dinh dưỡng nghiêm trọng và chỉ được phép ăn một bữa đạm bạc mỗi ngày.* | — | — |  |
| 2-25 | `2.08#3` (7,7 s) | H | T1 | `t17_taunting_kitchen_pies_counter`, `pan` | *Trong khi đó, cha mẹ mua về rất nhiều bánh ngọt, bánh táo thơm phức và đồ ăn nhanh để ngay trên bàn bếp trước mặt các con.* | — | — |  |
| 2-26 | `2.08#4` (7,3 s) | H | T1 | `t17_new_a2_06_kitchen_table_untouched_plate`, `pull` | *Họ đặt ra quy định nghiêm ngặt cấm các con chạm vào thức ăn, và ai vi phạm sẽ phải chịu những đòn trừng phạt khủng khiếp.* | — | — |  |
| 2-27 | `2.08#5` (9,3 s) | H | T1 | `t17_hoarded_unopened_toys_boxes`, `still` | *David Turpin vận hành gia đình như một hệ thống lập trình máy tính lạnh lùng, nơi sự sống của các con bị chia nhỏ thành từng định mức để toàn quyền định đoạt.* | — | — |  |
| 2-28 | `2.08#6` (7,8 s) | H | T1 | `t17_hoarded_unopened_toys_boxes`, `push` | *Cặp vợ chồng thậm chí còn mua nhiều đồ chơi mới về xếp đầy trong nhà nhưng cấm các con mở bao bì để chơi đùa.* | — | — |  |
| 2-29 | `2.08#7` (8,1 s) | H | T1 | `t17_new_a2_07_unopened_cardboard_toy_towers`, `pan` | *Hành vi biến thức ăn và đồ chơi thành đạo cụ tra tấn tâm lý bộc lộ sự tha hóa tột cùng trong nhân cách của hai kẻ bạo hành.* | — | — |  |
| 2-30 | `2.08#8` (11,5 s) | H | T1 | `t17_luxury_shopping_hoarding_compulsion`, `pull` | *Trong khi đó, người mẹ Louise Turpin chìm đắm trong cơn nghiện mua sắm tích trữ để bù đắp sự trống rỗng, biến những món hàng xa xỉ thành công cụ khoét sâu thêm sự đày đọa con cái.* | — | — |  |
| 2-31 | `2.08#9` (7,2 s) | H | T1 | `t17_luxury_shopping_hoarding_compulsion`, `still` | *Tình trạng thiếu hụt dinh dưỡng kéo dài nhiều năm đã kìm hãm nặng nề sự phát triển thể chất và não bộ của những người con.* | — | — |  |
| 2-32 | `2.09#1` (6,2 s) | D | T1 | `t17_medical_records_stunted_growth_charts`, `push` | *Kết quả kiểm tra y tế toàn diện tại bệnh viện đã khiến các bác sĩ và điều tra viên phải bàng hoàng và rơi nước mắt.* | — | — |  |
| 2-33 | `2.09#2` (5,0 s) | D | T1 | `t17_medical_records_stunted_growth_charts`, `pan` | *Người chị cả hai mươi chín tuổi khi được giải cứu chỉ có cân nặng khoảng ba mươi bảy kilôgam.* | — | — |  |
| 2-34 | `2.09#3` (7,0 s) | D | T1 | `t17_medical_records_stunted_growth_charts`, `pull` | *Theo lời Công tố viên Michael Hestrin, một nạn nhân mười hai tuổi chỉ có thể trạng tương đương một đứa trẻ bảy tuổi bình thường.* | — | — |  |
| 2-35 | `2.09#4` (7,8 s) | D | T1 | `t17_new_a2_08_stacked_luxury_shoe_boxes`, `still` | *Hầu hết các nạn nhân đều bị teo cơ nghiêm trọng, suy giảm nhận thức và mang nhiều tổn thương thần kinh vĩnh viễn do thiếu dưỡng chất.* | — | — |  |
| 2-36 | `2.09#5` (6,2 s) | D | T1 | `t17_complete_social_blindspot_concept`, `push` | *Sự cô lập xã hội triệt để khiến họ không có những hiểu biết cơ bản nhất về thế giới thực tại bên ngoài cánh cửa.* | — | — |  |
| 2-37 | `2.09#6` (6,4 s) | D | T1 | `t17_complete_social_blindspot_concept`, `pan` | *Khi các điều tra viên hỏi về cảnh sát, nhiều người con hoàn toàn ngơ ngác và không biết cảnh sát là ai hay làm công việc gì.* | — | — |  |
| 2-38 | `2.09#7` (7,0 s) | D | T1 | `t17_new_a2_09_measuring_tape_height_marks`, `pull` | *Thậm chí những khái niệm sinh hoạt thiết yếu nhất như thuốc chữa bệnh hay bàn chải đánh răng cũng hoàn toàn xa lạ với họ.* | — | — |  |
| 2-39 | `2.10#1` (8,8 s) | H | T1 | `t17_perris_house_crime_scene_tape`, `still` | *Vụ án gia đình Turpin đã làm rúng động truyền thông toàn cầu, và ngôi nhà tại Perris bị gọi là “Ngôi nhà của những nỗi kinh hoàng”.* | — | — |  |
| 2-40 | `2.10#2` (8,5 s) | H | T1 | `t17_perris_house_crime_scene_tape`, `push` | *David và Louise Turpin lập tức bị bắt giữ và đối mặt với hàng chục tội danh nghiêm trọng về bạo hành và giam giữ người trái phép.* | — | — |  |
| 2-41 | `2.10#3` (10,1 s) | H | T1 | `t17_new_a2_10_abandoned_front_lawn_tricycle`, `pan` | *Dư luận xã hội bàng hoàng đặt ra câu hỏi tại sao một tội ác quy mô lớn như vậy có thể tồn tại suốt hàng thập kỷ mà không bị phát hiện.* | — | — |  |
| 2-42 | `2.10#4` (7,4 s) | H | T1 | `t17_jordan_turpin_spark_of_survival`, `pull` | *Điều gì đã thôi thúc hai bậc cha mẹ có học thức đối xử với chính những đứa con ruột thịt của mình như những tù nhân?* | — | — |  |
| 2-43 | `2.10#5` (8,6 s) | H | T1 | `t17_jordan_turpin_spark_of_survival`, `still` | *Và làm thế nào mà một cô gái nhỏ bé như Jordan Turpin lại có thể duy trì được ngọn lửa sinh tồn để phá vỡ xiềng xích nô dịch?* | — | — |  |
| 2-44 | `2.10#6` (7,9 s) | H | T1 | `t17_psychological_profiling_dossier_open`, `push` | *Để giải mã những câu hỏi nhức nhối ấy, chúng ta cần đi sâu vào cấu trúc tâm lý học hành vi của những kẻ kiểm soát cưỡng chế.* | — | — |  |
| 2-45 | `2.10#7` (6,9 s) | H | T1 | `t17_psychological_profiling_dossier_open`, `pan` | *Sau đây, Chuyên gia tâm lý sẽ bóc tách các cơ chế tâm bệnh học đã biến một gia đình thành một địa ngục khép kín.* | — | — |  |
| 2-46 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 03* · **GIẢI MÃ KIỂM SOÁT CƯỠNG CHẾ & FOLIE À DEUX** | — | ⊘ | ◼ |

### HỒI 3

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (8,3 s) | H | T1 | `t17_coercive_control_matrix_diagram`, `pull` | *Dưới góc độ tâm lý học tội phạm, hồ sơ Nhà Turpin là một trường hợp kinh điển về sự lạm dụng quyền lực gia đình ở mức độ cực đoan.* | — | — |  |
| 3-02 | `3.02#2` (6,8 s) | H | T1 | `t17_coercive_control_matrix_diagram`, `still` | *Đây không đơn thuần là sự bộc phát của cơn giận dữ hay sự vô trách nhiệm trong việc nuôi dạy con cái của cha mẹ.* | — | — |  |
| 3-03 | `3.02#3` (9,0 s) | H | T1 | `t17_coercive_control_matrix_diagram`, `push` | *Đó là một hệ thống kiểm soát cưỡng chế toàn diện được xây dựng tinh vi nhằm tước đoạt hoàn toàn căn tính và ý chí tự do của nạn nhân.* | — | — |  |
| 3-04 | `3.02#4` (11,4 s) | H | T1 | `t17_infantilization_concept_baby_crib_shadow`, `pan` | *Để mổ xẻ hiện tượng tâm lý phức tạp này, chúng ta cần phân tích ba khái niệm cốt lõi: Kiểm soát cưỡng chế, Hội chứng điên cuồng đôi và Sự ấu trĩ hóa có chủ đích.* | — | — |  |
| 3-05 | `3.02#5` (5,7 s) | H | T1 | `t17_infantilization_concept_baby_crib_shadow`, `pull` | *Xin mời Chuyên gia tâm lý phân tích chi tiết cơ chế vận hành của chiếc bẫy tâm lý tàn độc này.* | — | — |  |
| 3-06 | `3.03#1` (9,6 s) | C | T1 | `t17_dehumanization_living_props_shelf`, `still` | *Khái niệm Kiểm soát cưỡng chế, hay Coercive Control, chỉ một mô hình hành vi thống trị liên tục thông qua sự đe dọa, cô lập và trừng phạt nhằm làm suy yếu quyền tự chủ của nạn nhân.* | — | ✦ Cáo |  |
| 3-07 | `3.03#2` (7,9 s) | C | T1 | `t17_dehumanization_living_props_shelf`, `push` | *David và Louise Turpin đã cắt đứt hoàn toàn mọi sợi dây liên hệ giữa các con với thế giới bên ngoài nhằm tạo ra một ốc đảo tâm lý biệt lập.* | — | — |  |
| 3-08 | `3.03#3` (7,4 s) | C | T1 | `t17_new_a3_01_spiderweb_in_doorframe_corner`, `pan` | *Khi nạn nhân bị tước đoạt mọi tương tác xã hội, thế giới quan của họ bị thu hẹp hoàn toàn vào hệ thống quy tắc lệch lạc do kẻ thống trị áp đặt.* | — | — |  |
| 3-09 | `3.03#4` (6,3 s) | C | T1 | `t17_malignant_narcissism_mirror_crack`, `pull` | *Về góc nhìn đối với nạn nhân, hai kẻ thủ ác đã thực hiện cơ chế Phi nhân hóa và Vật hóa nạn nhân ở cấp độ triệt để.* | — | — |  |
| 3-10 | `3.03#5` (7,5 s) | C | T1 | `t17_malignant_narcissism_mirror_crack`, `still` | *Các con không được nhìn nhận như những con người có cảm xúc và nhân phẩm, mà bị giáng cấp thành những “đạo cụ sống” phục vụ ảo tưởng quyền lực của cha mẹ.* | — | — |  |
| 3-11 | `3.03#6` (5,2 s) | C | T1 | `t17_new_a3_02_porcelain_doll_shadow_profile`, `push` | *Lý do gốc rễ nằm ở sự khuyết tật thấu cảm trầm trọng và ảo tưởng ái kỷ ác tính của cặp vợ chồng.* | — | — |  |
| 3-12 | `3.03#7` (7,8 s) | C | T1 | `t17_moral_disengagement_scriptures_desk`, `pan` | *Tiếng khóc van xin hay sự đau đớn của các con không hề kích hoạt lòng trắc ẩn, mà trái lại còn củng cố cảm giác kiểm soát toàn năng của kẻ săn mồi.* | — | — |  |
| 3-13 | `3.03#8` (8,3 s) | C | T1 | `t17_moral_disengagement_scriptures_desk`, `pull` | *Để biện minh cho hành vi tàn bạo, họ sử dụng kỹ thuật Trung hòa đạo đức, tự thuyết phục rằng việc giam giữ là để bảo vệ các con khỏi sự cám dỗ của xã hội.* | — | — |  |
| 3-14 | `3.04#1` (9,6 s) | H | T1 | `t17_folie_a_deux_entwined_shadows`, `still` | *Một câu hỏi lớn đặt ra là tại sao cả hai vợ chồng lại có thể cùng nhau duy trì một tội ác kéo dài suốt nhiều năm mà không ai thức tỉnh lương tri.* | — | — |  |
| 3-15 | `3.04#2` (6,2 s) | H | T1 | `t17_folie_a_deux_entwined_shadows`, `push` | *Điều gì đã tạo nên sự đồng lõa mù quáng giữa một người cha kỹ sư và một người mẹ nội trợ?* | — | — |  |
| 3-16 | `3.04#3` (8,0 s) | H | T1 | `t17_new_a3_03_tarnished_silver_hand_mirror`, `pan` | *Dưới lăng kính tâm thần học, giới phân tích thường nhắc đến hiện tượng rối loạn tâm thần chia sẻ, hay Hội chứng Điên cuồng đôi.* | — | — |  |
| 3-17 | `3.04#4` (7,5 s) | H | T1 | `t17_compartmentalization_two_drawers_void`, `pull` | *Cơ chế này kết hợp cùng sự phân mảnh tâm trí đã tạo nên một bức tường nhận thức vững chắc ngăn cách hai thế giới đối lập.* | — | — |  |
| 3-18 | `3.04#5` (4,2 s) | H | T1 | `t17_compartmentalization_two_drawers_void`, `still` | *Xin Chuyên gia tâm lý làm rõ hơn về sự cộng hưởng bệnh lý này.* | — | — |  |
| 3-19 | `3.05#1` (9,2 s) | C | T1 | `t17_shared_delusional_echo_chamber`, `push` | *Hội chứng Điên cuồng đôi, hay Folie à Deux, là một khung lý thuyết mô tả tình trạng hai cá nhân gắn bó sâu sắc cùng chia sẻ và củng cố một hệ thống niềm tin lệch lạc.* | — | — |  |
| 3-20 | `3.05#2` (7,5 s) | C | T1 | `t17_shared_delusional_echo_chamber`, `pan` | *Đây là một góc nhìn phân tích hành vi giúp giải thích hiện tượng xã hội, không phải là một chẩn đoán y khoa chính thức được tòa án công nhận cho hai bị cáo.* | — | — |  |
| 3-21 | `3.05#3` (8,8 s) | C | T1 | `t17_new_a3_04_leather_bound_book_clasps`, `pull` | *Khi hai cái tôi bệnh lý kết hợp với nhau, họ tạo ra một vòng lặp tự xác thực khép kín, nơi sự tàn nhẫn được bình thường hóa và cảm giác tội lỗi bị triệt tiêu hoàn toàn.* | — | — |  |
| 3-22 | `3.05#4` (8,8 s) | C | T1 | `t17_learned_helplessness_open_cage`, `still` | *Bên cạnh đó là cơ chế Chia ngăn nhận thức cực đoan: họ tách biệt rạch ròi giữa “ngăn kéo gia đình mẫu mực trên mạng xã hội” và “ngăn kéo ngục tù sau cánh cửa”.* | — | — |  |
| 3-23 | `3.05#5` (8,4 s) | C | T1 | `t17_learned_helplessness_open_cage`, `push` | *Trong thế giới khép kín ấy, người vợ từng bước trượt từ vị thế một thiếu nữ bị phụ thuộc sang vai trò kẻ đồng lõa bạo hành để củng cố quyền lực tối thượng cùng chồng.* | — | — |  |
| 3-24 | `3.05#6` (5,7 s) | C | T1 | `t17_new_a3_05_two_intertwined_wax_candles`, `pan` | *Để duy trì sự quy phục tuyệt đối, cặp vợ chồng đã áp dụng chiến lược Ấu trĩ hóa nạn nhân một cách có hệ thống.* | — | — |  |
| 3-25 | `3.05#7` (6,7 s) | C | T1 | `t17_physical_atrophy_empty_shoes`, `pull` | *Tình trạng kìm hãm dinh dưỡng kéo dài khiến cơ thể những người con trưởng thành không thể phát triển bình thường, kẹt lại trong hình hài trẻ thơ.* | — | — |  |
| 3-26 | `3.05#8` (9,2 s) | C | T1 | `t17_physical_atrophy_empty_shoes`, `still` | *Khi cơ thể suy kiệt và nhận thức bị cô lập, các nạn nhân rơi vào trạng thái Bất lực tập nhiễm, tin rằng bản thân hoàn toàn bất lực và không thể tồn tại nếu thiếu cha mẹ.* | — | — |  |
| 3-27 | `3.05#9` (8,5 s) | C | T1 | `t17_new_a3_06_wooden_cabinet_divided_cubbies`, `push` | *Tuy nhiên, dù sự đày đọa có khốc liệt đến đâu, bản năng sinh tồn và khát vọng tự do của con người vẫn là một ngọn lửa không bao giờ có thể bị dập tắt hoàn toàn.* | — | — |  |
| 3-28 | `3.06#1` (7,2 s) | H | T1 | `t17_clandestine_wifi_glow_wardrobe`, `pan` | *Và ngọn lửa sinh tồn kỳ diệu ấy đã âm thầm bùng cháy mãnh liệt bên trong tâm hồn của cô con gái Jordan Turpin.* | — | — |  |
| 3-29 | `3.06#2` (7,8 s) | H | T1 | `t17_clandestine_wifi_glow_wardrobe`, `pull` | *Sống trong một ngục tù thiếu thốn ánh sáng và thức ăn, điều gì đã nuôi dưỡng ý chí tự do của một thiếu nữ mười bảy tuổi?* | — | — |  |
| 3-30 | `3.06#3` (7,2 s) | H | T1 | `t17_new_a3_07_hanging_iron_birdcage_door_ajar`, `still` | *Làm thế nào cô gái ấy có thể vượt qua nỗi sợ hãi tê liệt tích tụ suốt cả đời để đưa ra một quyết định sinh tử?* | — | — |  |
| 3-31 | `3.06#4` (7,6 s) | H | T1 | `t17_outside_world_music_video_screen`, `push` | *Đó là câu chuyện phi thường về sức mạnh của nhận thức và tình mẫu tử, tình anh em vượt lên nghịch cảnh tăm tối.* | — | — |  |
| 3-32 | `3.06#5` (4,6 s) | H | T1 | `t17_outside_world_music_video_screen`, `pan` | *Chúng ta hãy cùng lắng nghe phân tích về bước ngoặt giải phóng tâm lý của Jordan.* | — | — |  |
| 3-33 | `3.07#1` (8,2 s) | C | T1 | `t17_gift_of_fear_protective_instinct`, `pull` | *Trong những lời chia sẻ sau này, Jordan Turpin kể lại rằng một chiếc điện thoại thông minh cũ bị vứt xó đã trở thành chiếc chìa khóa mở ra thế giới nhận thức của cô.* | — | — |  |
| 3-34 | `3.07#2` (8,4 s) | C | T1 | `t17_gift_of_fear_protective_instinct`, `still` | *Bằng cách kết nối mạng không dây lén lút, cô đã âm thầm xem các video ca nhạc và các đoạn phim về cuộc sống đời thường của những người cùng trang lứa trên thế giới.* | — | — |  |
| 3-35 | `3.07#3` (6,7 s) | C | T1 | `t17_new_a3_08_blue_led_router_glow_dark`, `push` | *Những hình ảnh về sự tự do, nụ cười hồn nhiên và tình yêu thương đã tạo nên một cú sốc nhận thức tích cực trong tâm trí Jordan.* | — | — |  |
| 3-36 | `3.07#4` (7,5 s) | C | T1 | `t17_new_a3_08_blue_led_router_glow_dark`, `pan` | *Cô nhận ra rằng những quy tắc hà khắc của cha mẹ không phải là chân lý, và một thế giới nhân ái tươi đẹp thực sự đang tồn tại bên ngoài cánh cửa.* | — | — |  |
| 3-37 | `3.07#5` (9,4 s) | C | T1 | `t17_imminent_relocation_cardboard_threat`, `pull` | *Nguyên lý Quà tặng của Nỗi sợ hãi, hay The Gift of Fear, đã kích hoạt bản năng sinh tồn mạnh mẽ khi Jordan nhận thấy các em nhỏ đang ngày càng kiệt sức.* | — | — |  |
| 3-38 | `3.07#6` (6,7 s) | C | T1 | `t17_imminent_relocation_cardboard_threat`, `still` | *Khi tình yêu thương và trách nhiệm bảo vệ các em vượt lên trên nỗi sợ hãi trừng phạt, cô đã tìm thấy lòng dũng cảm phi thường để hành động.* | — | — |  |
| 3-39 | `3.07#7` (8,4 s) | C | T1 | `t17_new_a3_09_folded_blanket_foot_of_bed`, `push` | *Khi đối diện với nguy cơ các em nhỏ có thể không qua khỏi trong đợt chuyển nhà sắp tới, bản năng bảo vệ giống loài đã đè bẹp hoàn toàn sự bất lực tập nhiễm bấy lâu.* | — | — |  |
| 3-40 | `3.07#8` (7,0 s) | C | T1 | `t17_unbreakable_human_dignity_dawn`, `pan` | *Quyết định trèo qua bậu cửa sổ rạng sáng hôm đó là một minh chứng rực rỡ cho sự bất khuất của phẩm giá con người trước sự áp chế tàn bạo.* | — | — |  |
| 3-41 | `3.07#9` (6,2 s) | C | T1 | `t17_unbreakable_human_dignity_dawn`, `pull` | *Đó là khoảnh khắc nhận thức của con người bừng tỉnh, biến nỗi sợ hãi tê liệt thành ngọn lửa hành động quyết định sự sống còn.* | — | — |  |
| 3-42 | `3.08#1` (8,3 s) | H | T1 | `t17_courthouse_steps_shadow_justice`, `still` | *Cú nhảy sinh tồn của Jordan không chỉ tự cứu lấy cuộc đời mình, mà còn mở toang cánh cửa địa ngục để giải thoát cho mười hai anh chị em.* | — | — |  |
| 3-43 | `3.08#2` (8,4 s) | H | T1 | `t17_courthouse_steps_shadow_justice`, `push` | *Bức màn giả tạo bao trùm ngôi nhà số 160 đường Muir Woods Road chính thức sụp đổ trước ánh sáng của công lý.* | — | — |  |
| 3-44 | `3.08#3` (7,7 s) | H | T1 | `t17_courthouse_steps_shadow_justice`, `pan` | *Giờ là lúc hai kẻ bạo hành phải bước ra trước vành móng ngựa để đối diện với bản cáo trạng nghiêm khắc của pháp luật.* | — | — |  |
| 3-45 | `3.08#4` (6,8 s) | H | T1 | `t17_new_a3_10_cardboard_packing_tape_roll`, `pull` | *Hồi 4 sẽ đưa chúng ta đến với phiên tòa công lý và sự sụp đổ cái tôi của những kẻ thống trị bạo tàn.* | — | — |  |
| 3-46 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 04* · **BẢN ÁN CÔNG LÝ & SỰ SỤP ĐỔ CÁI TÔI** | — | ⊘ | ◼ |

### HỒI 4

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (11,2 s) | H | T1 | `t17_district_attorney_indictment_press`, `still` | *Ngày 18 tháng 1 năm 2018, Văn phòng Biện lý Hạt Riverside chính thức công bố bản cáo trạng rúng động dư luận đối với David và Louise Turpin.* | — | — |  |
| 4-02 | `4.02#2` (10,0 s) | H | T1 | `t17_district_attorney_indictment_press`, `push` | *Cặp vợ chồng bị truy tố hàng chục tội danh nghiêm trọng, bao gồm tra tấn, lạm dụng trẻ em, giam giữ người trái phép và ngược đãi người phụ thuộc.* | — | — |  |
| 4-03 | `4.02#3` (9,2 s) | H | T1 | `t17_new_a4_01_microphones_podium_silhouette`, `pan` | *Công tố viên Michael Hestrin khẳng định trước các cơ quan báo chí rằng đây là một trong những vụ án đày đọa gia đình tàn nhẫn nhất trong lịch sử tư pháp hạt.* | — | — |  |
| 4-04 | `4.02#4` (8,9 s) | H | T1 | `t17_fourteen_felony_guilty_plea_docs`, `pull` | *Trước những bằng chứng vật chất đanh thép từ các bức ảnh của Jordan và hồ sơ y tế không thể chối cãi, hai bị cáo không còn đường chối tội.* | — | — |  |
| 4-05 | `4.02#5` (11,0 s) | H | T1 | `t17_fourteen_felony_guilty_plea_docs`, `still` | *Ngày 22 tháng 2 năm 2019, cả David và Louise Turpin đã chính thức ký thỏa thuận nhận tội đối với mười bốn tội danh hình sự đặc biệt nghiêm trọng.* | — | — |  |
| 4-06 | `4.02#6` (8,8 s) | H | T1 | `t17_new_a4_02_courtroom_bench_empty_chairs`, `push` | *Quyết định nhận tội này giúp các nạn nhân tránh được nỗi đau tái chấn thương tâm lý khi không phải trực tiếp đối chất trong một phiên tòa xét xử kéo dài.* | — | — |  |
| 4-07 | `4.04#1` (9,6 s) | H | T1 | `t17_riverside_superior_courtroom_bench`, `pan` | *Ngày 19 tháng 4 năm 2019, phiên tòa tuyên án diễn ra tại Tòa Thượng thẩm Hạt Riverside dưới sự chủ tọa của Thẩm phán Bernard Schwartz.* | — | — |  |
| 4-08 | `4.04#2` (7,1 s) | H | T1 | `t17_riverside_superior_courtroom_bench`, `pull` | *Khán phòng xét xử chật kín các phóng viên truyền thông quốc tế, đại diện tổ chức bảo vệ trẻ em và những người dân quan tâm.* | — | — |  |
| 4-09 | `4.04#3` (7,4 s) | H | T1 | `t17_narcissistic_collapse_tears_dock`, `still` | *Đứng trước vành móng ngựa, cả David và Louise Turpin đều cúi đầu rơi nước mắt và đọc những lời xin lỗi run rẩy.* | — | — |  |
| 4-10 | `4.04#4` (11,3 s) | H | T1 | `t17_narcissistic_collapse_tears_dock`, `push` | *Liệu những giọt nước mắt lăn dài trước vành móng ngựa là biểu hiện của một lương tâm thức tỉnh muộn màng, hay chỉ là sự sụp đổ của một ảo tưởng ái kỷ khi quyền lực đã tan biến?* | — | — |  |
| 4-11 | `4.04#5` (7,7 s) | H | T1 | `t17_victim_impact_statement_podium`, `pan` | *Thế nhưng, tâm điểm xúc động và thiêng liêng nhất của phiên tòa lại thuộc về những lời phát biểu dũng cảm từ chính những người con.* | — | — |  |
| 4-12 | `4.04#6` (8,1 s) | H | T1 | `t17_victim_impact_statement_podium`, `pull` | *Những nạn nhân từng bị coi là bất lực đã ngẩng cao đầu bước lên bục nhân chứng để đòi lại tiếng nói và phẩm giá cho chính mình.* | — | — |  |
| 4-13 | `4.06#1` (6,9 s) | D | T1 | `t17_reclaiming_my_life_courtroom_light`, `still` | *Theo ghi nhận tại phiên tòa, một số người con đã dũng cảm trực tiếp đứng trước hội đồng xét xử để cất lên tiếng nói của sự thật.* | — | — |  |
| 4-14 | `4.06#2` (8,2 s) | D | T1 | `t17_reclaiming_my_life_courtroom_light`, `push` | *Một người con gái nghẹn ngào phát biểu trước tòa rằng cha mẹ đã lấy đi cả tuổi thơ của cô, nhưng giờ đây cô đang từng bước lấy lại cuộc đời tự do của mình.* | — | — |  |
| 4-15 | `4.06#3` (9,8 s) | D | T1 | `t17_forgiveness_as_liberation_concept`, `pan` | *Một người con trai chia sẻ một thông điệp vị tha sâu sắc, nói rằng anh vẫn giữ tình yêu thương và chọn tha thứ cho cha mẹ, dù không bao giờ có thể quên những nỗi đau đã qua.* | — | — |  |
| 4-16 | `4.06#4` (9,0 s) | D | T1 | `t17_forgiveness_as_liberation_concept`, `pull` | *Lời tha thứ từ người con không đồng nghĩa với việc xóa bỏ tội lỗi, mà là một hành vi giải phóng tâm lý đanh thép, tước bỏ quyền năng làm tổn thương của cha mẹ mãi mãi.* | — | — |  |
| 4-17 | `4.06#5` (6,2 s) | D | T1 | `t17_inverted_day_night_clock_blinds`, `still` | *Những lời phát biểu đầy nhân văn và kiên cường ấy đã khiến cả phòng xử án lặng đi trong niềm xúc động nghẹn ngào.* | — | — |  |
| 4-18 | `4.06#6` (8,4 s) | D | T1 | `t17_new_a4_03_heavy_steel_handcuffs_table`, `push` | *Các nạn nhân không còn xuất hiện như những cái bóng sợ hãi trong bóng tối, mà đã hóa thân thành những con người mạnh mẽ đang khẳng định quyền làm chủ số phận.* | — | — |  |
| 4-19 | `4.06#7` (6,6 s) | D | T1 | `t17_new_a4_03_heavy_steel_handcuffs_table`, `pan` | *Hình ảnh ấy đối lập hoàn toàn với sự bạc nhược và co ro của hai kẻ từng tự xưng là đấng toàn năng trong gia đình.* | — | — |  |
| 4-20 | `4.08#1` (7,9 s) | H | T1 | `t17_judge_schwartz_gavel_verdict`, `pull` | *Thẩm phán Bernard Schwartz đã dành những lời phán quyết đanh thép và nghiêm khắc nhất gửi tới hai kẻ phạm tội trước khi tuyên án.* | — | — |  |
| 4-21 | `4.08#2` (9,9 s) | H | T1 | `t17_judge_schwartz_gavel_verdict`, `still` | *Ông khẳng định rằng cách đối xử tàn bạo của hai bị cáo đối với chính con cái của mình là hành vi ích kỷ, nhẫn tâm và hoàn toàn phi nhân tính.* | — | — |  |
| 4-22 | `4.08#3` (6,7 s) | H | T1 | `t17_life_sentence_prison_doors_closing`, `push` | *Bản án được tuyên phạt là hai mươi lăm năm tù đến chung thân dành cho cả David và Louise Turpin.* | — | — |  |
| 4-23 | `4.08#4` (8,2 s) | H | T1 | `t17_life_sentence_prison_doors_closing`, `pan` | *Đây là mức án phạt nghiêm khắc nhất theo quy định pháp luật của bang California cho các tội danh lạm dụng và tra tấn người phụ thuộc.* | — | — |  |
| 4-24 | `4.08#5` (9,4 s) | H | T1 | `t17_life_sentence_prison_doors_closing`, `pull` | *Hai bị cáo bị áp giải đến hai trại giam an ninh tối đa khác nhau và chỉ có thể được xem xét ân xá khi đã chấp hành đủ hai mươi lăm năm thụ án.* | — | — |  |
| 4-25 | `4.09#1` (9,0 s) | N2 | T4 | `t17_hospital_warm_meal_healing_bed`, `still` | *Hãy hình dung cảm xúc vỡ òa của các y bác sĩ tại Trung tâm Y tế Đại học Riverside khi lần đầu tiên tiếp nhận mười ba anh chị em nhà Turpin.* | — | ✦ Mèo |  |
| 4-26 | `4.09#2` (8,4 s) | N2 | T4 | `t17_hospital_warm_meal_healing_bed`, `push` | *Trong những ngày đầu, các nạn nhân co rúm người lại trước ánh sáng đèn phòng bệnh và giật mình hoảng sợ trước mọi tiếng động nhỏ nhất xung quanh.* | — | — |  |
| 4-27 | `4.09#3` (10,2 s) | N2 | T4 | `t17_new_a4_04_court_witness_microphone_stand`, `pan` | *Những điều bình dị của đời sống như một bữa cơm nóng hổi, một chiếc giường êm ái hay một lần tắm nước ấm đối với họ đều là những phép màu chưa từng thấy.* | — | — |  |
| 4-28 | `4.09#4` (10,1 s) | N2 | T4 | `t17_pediatric_care_gentle_stethoscope`, `pull` | *Quy trình hồi phục thể chất cho những bệnh nhân suy kiệt dinh dưỡng lâu năm đòi hỏi sự theo dõi y khoa vô cùng tỉ mỉ để tránh hội chứng nuôi ăn lại nguy hiểm.* | — | — |  |
| 4-29 | `4.09#5` (10,0 s) | N2 | T4 | `t17_pediatric_care_gentle_stethoscope`, `still` | *Nhưng điều khiến tất cả đội ngũ y tế xúc động sâu sắc nhất chính là tình yêu thương và sự gắn kết bảo bọc lẫn nhau đến kỳ diệu giữa các anh chị em.* | — | — |  |
| 4-30 | `4.09#6` (8,6 s) | N2 | T4 | `t17_new_a4_05_polished_wood_sound_block_gavel`, `push` | *Sự hồi sinh từng ngày của họ là một bài học vô giá về sức sống mãnh liệt và phẩm giá kiên cường của con người sau nghịch cảnh.* | — | — |  |
| 4-31 | `4.10#1` (7,1 s) | D | T1 | `t17_new_a4_05_polished_wood_sound_block_gavel`, `pan` | *Dưới góc độ tư pháp, bản án hai mươi lăm năm đến chung thân đã khép lại một chương đen tối và thiết lập sự nghiêm minh của luật pháp.* | — | — |  |
| 4-32 | `4.10#2` (9,5 s) | D | T1 | `t17_spiritual_bypass_delusion_shattered`, `pull` | *Phản ứng khóc lóc của hai bị cáo tại tòa thể hiện sự sụp đổ cái tôi ái kỷ khi toàn bộ quyền lực thống trị bị tước bỏ, hoàn toàn không phải sự ăn năn thực tâm.* | — | — |  |
| 4-33 | `4.10#3` (11,4 s) | D | T1 | `t17_spiritual_bypass_delusion_shattered`, `still` | *Lời phân trần của người mẹ rằng Chúa có một kế hoạch đặc biệt thực chất là cơ chế ngắt kết nối đạo đức và ngụy biện tâm linh, nhằm trốn tránh trách nhiệm cá nhân đối với tội ác do chính tay mình tạo ra.* | — | — |  |
| 4-34 | `4.10#4` (9,3 s) | D | T1 | `t17_new_a4_06_steel_cell_door_crossbars`, `push` | *Hai kẻ thủ ác chỉ thực sự đau đớn khi nhận ra chiếc ngai vàng gia đình đã sụp đổ và họ phải đối diện với sự cô độc trong bốn bức tường giam cầm suốt phần đời còn lại.* | — | — |  |
| 4-35 | `4.10#5` (7,5 s) | D | T1 | `t17_legislative_hearing_homeschool_reform`, `pan` | *Vụ án Turpin đã gióng lên một hồi chuông cảnh tỉnh sâu sắc về những lỗ hổng pháp lý trong việc giám sát giáo dục tại gia ở bang California.* | — | — |  |
| 4-36 | `4.10#6` (7,6 s) | D | T1 | `t17_legislative_hearing_homeschool_reform`, `pull` | *Sự việc đã thúc đẩy các nhà lập pháp tiến hành các phiên điều trần nhằm tăng cường kiểm tra phúc lợi đối với các trường học tại nhà.* | — | — |  |
| 4-37 | `4.10#7` (7,9 s) | D | T1 | `t17_new_a4_07_hospital_bedside_pitcher_glass`, `still` | *Di sản lớn nhất của vụ án chính là tấm gương dũng cảm phi thường của Jordan Turpin trong việc đấu tranh bảo vệ quyền sống cho bản thân và người thân.* | — | — |  |
| 4-38 | `4.11#1` (6,4 s) | C | T1 | `t17_post_traumatic_growth_sprout_brick`, `push` | *Quá trình hồi phục kỳ diệu của mười ba người con là một minh chứng tiêu biểu cho khái niệm Tăng trưởng sau sang chấn trong tâm lý học.* | — | — |  |
| 4-39 | `4.11#2` (6,8 s) | C | T1 | `t17_post_traumatic_growth_sprout_brick`, `pan` | *Dù mang trên mình những tổn thương thể chất và ký ức đau buồn, sự nâng đỡ của cộng đồng đã giúp họ từng bước tái hòa nhập xã hội.* | — | — |  |
| 4-40 | `4.11#3` (6,6 s) | C | T1 | `t17_new_a4_08_medical_stethoscope_chart_clipboard`, `pull` | *Họ đã chuyển hóa nỗi đau trong quá khứ thành động lực mạnh mẽ để xây dựng cuộc sống tự lập và theo đuổi con đường học tập.* | — | — |  |
| 4-41 | `4.11#4` (7,6 s) | C | T1 | `t17_sibling_hands_reunited_sunlight`, `still` | *Khả năng phục hồi của các nạn nhân khẳng định rằng bóng tối của sự kiểm soát bạo tàn không thể tiêu diệt được bản ngã và khát vọng yêu thương của con người.* | — | — |  |
| 4-42 | `4.11#5` (9,2 s) | C | T1 | `t17_sibling_hands_reunited_sunlight`, `push` | *Bằng cách từ chối sự giam cầm của thù hận, các nạn nhân đã thực hiện một bước nhảy nhận thức vĩ đại, chứng minh rằng sự thấu cảm và tính thiện luôn mạnh hơn bạo lực độc đoán.* | — | — |  |
| 4-43 | `4.11#6` (6,7 s) | C | T1 | `t17_new_a4_09_small_green_leaf_stone_crack`, `pan` | *Tình cảm ruột thịt chân thành chính là chiếc phao cứu sinh vững chắc nhất đưa họ vượt qua giông bão để tìm lại ánh sáng cuộc đời.* | — | — |  |
| 4-44 | `4.12#1` (8,6 s) | H | T1 | `t17_prison_perimeter_fence_sunset`, `pull` | *Cánh cửa nhà tù đã vĩnh viễn khép lại phía sau David và Louise Turpin, kết thúc chuỗi ngày đen tối của ngôi nhà ngục tù ngoại ô.* | — | — |  |
| 4-45 | `4.12#2` (5,8 s) | H | T1 | `t17_prison_perimeter_fence_sunset`, `still` | *Những người con dũng cảm giờ đây đã được tự do hít thở bầu không khí của độc lập và yêu thương.* | — | — |  |
| 4-46 | `4.12#3` (7,2 s) | H | T1 | `t17_prison_perimeter_fence_sunset`, `push` | *Thế nhưng, bi kịch này để lại cho toàn xã hội những bài học cảnh giác đắt giá không bao giờ được phép lãng quên.* | — | — |  |
| 4-47 | `4.12#4` (8,9 s) | H | T1 | `t17_new_a4_10_hands_joined_together_sunbeam`, `pan` | *Hồi 5 sẽ tổng kết hành trình tái sinh và đúc kết bốn dấu hiệu cảnh báo đỏ sinh tồn giúp chúng ta nhận diện bạo hành gia đình khép kín.* | — | — |  |
| 4-48 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 05* · **TÁI SINH & BỐN CẢNH BÁO ĐỎ SINH TỒN** | — | ⊘ | ◼ |

### HỒI 5

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (7,3 s) | H | T1 | `t17_university_campus_steps_independence`, `pull` | *Nhiều năm sau ngày được giải thoát, các anh chị em nhà Turpin đã từng bước nỗ lực tái thiết lại toàn bộ cuộc đời của mình.* | — | — |  |
| 5-02 | `5.02#2` (9,9 s) | H | T1 | `t17_university_campus_steps_independence`, `still` | *Những đứa trẻ còi cọc ngày nào giờ đây đã trưởng thành, theo học tại các trường đại học, có việc làm ổn định và hòa nhập tích cực vào xã hội.* | — | — |  |
| 5-03 | `5.02#3` (10,4 s) | H | T1 | `t17_new_a5_01_opened_notebook_fountain_pen`, `push` | *Cuối năm 2021, Jordan và Jennifer Turpin đã lần đầu tiên xuất hiện công khai trong một cuộc phỏng vấn truyền cảm hứng trên đài truyền hình quốc gia.* | — | — |  |
| 5-04 | `5.02#4` (9,5 s) | H | T1 | `t17_broadcast_interview_studio_hope`, `pan` | *Sự tự tin, rạng rỡ và tinh thần lạc quan của hai chị em đã truyền đi một thông điệp mạnh mẽ về nghị lực vươn lên từ tro tàn nghịch cảnh.* | — | — |  |
| 5-05 | `5.02#5` (8,3 s) | H | T1 | `t17_broadcast_interview_studio_hope`, `pull` | *Họ trở thành nguồn cảm hứng sống cho hàng triệu người trên khắp thế giới đang phải chiến đấu với những tổn thương tinh thần trong quá khứ.* | — | — |  |
| 5-06 | `5.02#6` (8,6 s) | H | T1 | `t17_new_a5_02_studio_camera_lens_reflection`, `still` | *Hành trình tái sinh ấy khẳng định một chân lý sâu sắc rằng không có ngục tù nào có thể giam cầm được một tâm hồn luôn hướng về tự do.* | — | — |  |
| 5-07 | `5.03#1` (8,1 s) | D | T1 | `t17_suburban_neighbor_porch_vigilance`, `push` | *Hồ sơ gia đình Turpin là một lời nhắc nhở nghiêm khắc đối với toàn thể xã hội về tinh thần cảnh giác và trách nhiệm cộng đồng của mỗi công dân.* | — | — |  |
| 5-08 | `5.03#2` (6,3 s) | D | T1 | `t17_suburban_neighbor_porch_vigilance`, `pan` | *Chúng ta tuyệt đối không bao giờ được phép thờ ơ trước những dấu hiệu bất thường từ những ngôi nhà hàng xóm kín cổng cao tường xung quanh.* | — | — |  |
| 5-09 | `5.03#3` (7,2 s) | D | T1 | `t17_new_a5_03_wooden_picket_fence_sunlight`, `pull` | *Đừng để “Hiệu ứng Hào quang” hay vẻ bề ngoài lịch thiệp, thành đạt của ai đó tạo nên điểm mù che giấu những hành vi nguy hiểm bên trong.* | — | — |  |
| 5-10 | `5.03#4` (7,5 s) | D | T1 | `t17_break_bystander_effect_lifeline`, `still` | *Một sự quan sát nhạy bén, một thái độ quan tâm chân thành và một cuộc gọi thông báo kịp thời có thể giải cứu những sinh mạng vô tội.* | — | — |  |
| 5-11 | `5.03#5` (9,2 s) | D | T1 | `t17_break_bystander_effect_lifeline`, `push` | *Mỗi công dân cần chủ động phá vỡ hiệu ứng người ngoài cuộc, bởi sự chần chừ và im lặng trước những điều bất thường chính là cơ hội để bạo hành gia đình tiếp tục hoành hành.* | — | — |  |
| 5-12 | `5.03#6` (7,0 s) | D | T1 | `t17_new_a5_04_vintage_brass_desk_bell`, `pan` | *Sự an toàn của trẻ em và những người phụ thuộc phải luôn là ưu tiên cao nhất của toàn bộ hệ thống thực thi pháp luật và xã hội.* | — | — |  |
| 5-13 | `5.04#1` (7,3 s) | C | T1 | `t17_child_dignity_open_park_swing`, `pull` | *Dưới góc độ bảo vệ quyền con người, bài học sâu sắc nhất từ thảm kịch này là sự tôn trọng tuyệt đối quyền độc lập và phẩm giá của trẻ em.* | — | — |  |
| 5-14 | `5.04#2` (6,8 s) | C | T1 | `t17_child_dignity_open_park_swing`, `still` | *Con cái không phải là tài sản sở hữu riêng của cha mẹ để phục vụ cho các ảo tưởng bệnh lý hay nhu cầu kiểm soát quyền lực độc đoán.* | — | — |  |
| 5-15 | `5.04#3` (6,6 s) | C | T1 | `t17_new_a5_05_empty_park_bench_dappled_light`, `push` | *Tình yêu thương gia đình chân chính phải được xây dựng trên sự nâng đỡ, tôn trọng và tạo điều kiện cho các thành viên phát triển tự do.* | — | — |  |
| 5-16 | `5.04#4` (6,4 s) | C | T1 | `t17_new_a5_05_empty_park_bench_dappled_light`, `pan` | *Kiểm soát cưỡng chế là một dạng thức bạo hành vô hình cực kỳ nguy hiểm cần phải được nhận diện và xử lý nghiêm minh trước pháp luật.* | — | — |  |
| 5-17 | `5.04#5` (7,6 s) | C | T1 | `t17_intuition_compassion_inner_light`, `pull` | *Chúng ta cần lắng nghe và tin tưởng vào trực giác bất an của chính mình, bởi đó là cơ chế cảnh báo tự nhiên giúp con người tự vệ trước mối nguy hiểm.* | — | — |  |
| 5-18 | `5.04#6` (7,6 s) | C | T1 | `t17_intuition_compassion_inner_light`, `still` | *Sự hỗ trợ tâm lý dài hạn và sự đồng hành của cộng đồng là nhân tố quyết định giúp các nạn nhân của kiểm soát cưỡng chế tìm lại căn tính bản thân.* | — | — |  |
| 5-19 | `5.04#7` (9,2 s) | C | T1 | `t17_new_a5_06_corkboard_pinned_blank_cards`, `push` | *Khái niệm Tăng trưởng sau sang chấn khẳng định rằng những vết thương tinh thần sâu sắc nhất hoàn toàn có thể trở thành nền tảng cho sự thức tỉnh nội tâm và lòng trắc ẩn cứu rỗi tha nhân.* | — | — |  |
| 5-20 | `5.04#8` (7,1 s) | C | T1 | `t17_new_a5_06_corkboard_pinned_blank_cards`, `pan` | *Hãy luôn dũng cảm lên tiếng khi phát hiện những dấu hiệu lạm dụng quyền lực, bởi sự im lặng vô cảm đôi khi chính là sự đồng lõa với tội ác.* | — | — |  |
| 5-21 | `5.05#1` (10,5 s) | H | T1 | `t17_four_redflags_overview_banner`, `pull` | *Để giúp mỗi chúng ta nâng cao cảnh giác và kịp thời bảo vệ những người xung quanh, kênh Amber Eyes xin đúc kết bốn dấu hiệu cảnh báo đỏ về bạo hành gia đình khép kín.* | — | — |  |
| 5-22 | `5.05#2` (7,2 s) | H | T1 | `t17_redflag1_total_physical_isolation`, `still` | *Dấu hiệu cảnh báo đỏ thứ nhất là sự cô lập xã hội tuyệt đối và chủ động né tránh mọi tương tác cộng đồng bình thường.* | — | — |  |
| 5-23 | `5.05#3` (10,9 s) | H | T1 | `t17_redflag1_total_physical_isolation`, `push` | *Khi một gia đình hoàn toàn không bao giờ mở cửa giao tiếp với hàng xóm láng giềng, kiên quyết cấm đoán con cái tham gia các hoạt động xã hội, đó là một tín hiệu bất thường rõ rệt.* | — | — |  |
| 5-24 | `5.05#4` (9,3 s) | H | T1 | `t17_new_a5_07_closed_tall_wrought_iron_gate`, `pan` | *Kẻ bạo hành luôn tìm cách cắt đứt mọi mối quan hệ bạn bè và người thân của nạn nhân nhằm triệt tiêu hoàn toàn các điểm tựa hỗ trợ bên ngoài.* | — | — |  |
| 5-25 | `5.05#5` (7,4 s) | H | T1 | `t17_new_a5_07_closed_tall_wrought_iron_gate`, `pull` | *Sự khép kín cực đoan phía sau những bức tường kiên cố thường là tấm bình phong che đậy những hành vi kiểm soát cưỡng chế độc hại.* | — | — |  |
| 5-26 | `5.05#6` (8,3 s) | H | T1 | `t17_redflag2_staged_social_media_contrast`, `still` | *Dấu hiệu cảnh báo đỏ thứ hai là sự tương phản phi lý giữa hình ảnh hào nhoáng trên mạng xã hội với thực tế sinh hoạt đời thường.* | — | — |  |
| 5-27 | `5.05#7` (9,6 s) | H | T1 | `t17_redflag2_staged_social_media_contrast`, `push` | *Những kẻ thống trị bệnh lý thường dàn dựng những bức ảnh gia đình hoàn hảo quá mức, ép các thành viên mặc đồ đồng bộ và tạo dáng cứng nhắc trước ống kính.* | — | — |  |
| 5-28 | `5.05#8` (8,0 s) | H | T1 | `t17_new_a5_08_empty_dining_table_chairs_morning`, `pan` | *Hãy luôn quan sát kỹ ánh mắt lo âu, nụ cười gượng gạo và sự căng thẳng ngấm ngầm của các thành viên trong gia đình.* | — | — |  |
| 5-29 | `5.05#9` (8,2 s) | H | T1 | `t17_new_a5_08_empty_dining_table_chairs_morning`, `pull` | *Chiếc mặt nạ hạnh phúc được phô trương rực rỡ có thể chính là lá chắn bình thường hóa nhằm ru ngủ sự nghi ngờ của dư luận xã hội.* | — | — |  |
| 5-30 | `5.05#10` (9,5 s) | H | T1 | `t17_redflag3_severe_malnutrition_evidence`, `still` | *Dấu hiệu cảnh báo đỏ thứ ba là những biểu hiện suy kiệt dinh dưỡng, thể trạng còi cọc và sự chậm phát triển thể chất nghiêm trọng không rõ nguyên nhân.* | — | — |  |
| 5-31 | `5.05#11` (10,2 s) | H | T1 | `t17_redflag3_severe_malnutrition_evidence`, `push` | *Việc những đứa trẻ hoặc thanh thiếu niên có vóc dáng nhỏ bé bất thường so với lứa tuổi, da dẻ xanh xao và sợ hãi ánh sáng tự nhiên là hồi chuông báo động cấp tính.* | — | — |  |
| 5-32 | `5.05#12` (9,6 s) | H | T1 | `t17_new_a5_09_wildflower_field_gentle_breeze`, `pan` | *Kẻ lạm dụng thường dùng thức ăn và điều kiện vệ sinh thiết yếu như một công cụ trừng phạt nhằm làm suy giảm năng lực phản kháng của nạn nhân.* | — | — |  |
| 5-33 | `5.05#13` (9,6 s) | H | T1 | `t17_new_a5_09_wildflower_field_gentle_breeze`, `pull` | *Khi bắt gặp những dấu hiệu suy kiệt bất thường như vậy, chúng ta đừng ngần ngại liên hệ ngay với các cơ quan bảo trợ xã hội để yêu cầu kiểm tra phúc lợi.* | — | — |  |
| 5-34 | `5.05#14` (8,8 s) | H | T1 | `t17_redflag4_nocturnal_routine_punishment`, `still` | *Dấu hiệu cảnh báo đỏ thứ tư là lối sống đảo lộn ngày đêm kỳ lạ kết hợp cùng những quy tắc kỷ luật mang tính chất trừng phạt khắt khe.* | — | — |  |
| 5-35 | `5.05#15` (10,8 s) | H | T1 | `t17_redflag4_nocturnal_routine_punishment`, `push` | *Những ngôi nhà luôn đóng kín rèm cửa suốt ban ngày, các thành viên chỉ ra ngoài vào những khung giờ khuya vắng và có biểu hiện sợ sệt người lạ là điều cần đặc biệt chú ý.* | — | — |  |
| 5-36 | `5.05#16` (8,5 s) | H | T1 | `t17_new_a5_10_amber_feather_on_leather_dossier`, `pan` | *Trong những môi trường độc hại ấy, mọi lỗi lầm nhỏ nhặt nhất đều bị thổi phồng thành những sai phạm nghiêm trọng để áp đặt các hình phạt hà khắc.* | — | — |  |
| 5-37 | `5.05#17` (9,3 s) | H | T1 | `t17_new_a5_10_amber_feather_on_leather_dossier`, `pull` | *Sự tuân phục mù quáng được thiết lập bằng nỗi sợ hãi kéo dài sẽ từng bước bóp nghẹt ý chí tự do và hủy hoại tâm lý của những người phụ thuộc.* | — | — |  |
| 5-38 | `5.05#18` (10,1 s) | H | T1 | `t17_no_child_deserves_fear_warmth`, `still` | *Không một đứa trẻ nào sinh ra trên đời đáng phải sống trong sự sợ hãi, bẩn thỉu và bị tước đoạt quyền được ăn no, được học hành và được yêu thương.* | — | — |  |
| 5-39 | `5.05#19` (10,0 s) | H | T1 | `t17_no_child_deserves_fear_warmth`, `push` | *Sự thấu cảm và trách nhiệm xã hội chính là ánh sáng duy nhất có thể xua tan bóng tối của những ngục tù vô hình ẩn giấu sau những bức tường khép kín.* | — | — |  |
| 5-40 | `5.05#20` (10,4 s) | H | T1 | `t17_community_vigilance_neighborhood_dawn`, `pan` | *Lòng dũng cảm và sự tinh tế trong quan sát của mỗi chúng ta hôm nay chính là chìa khóa mở toang cánh cửa tự do cho những số phận đang tuyệt vọng chờ đợi sự giúp đỡ.* | — | — |  |
| 5-41 | `5.05#21` (9,0 s) | H | T1 | `t17_community_vigilance_neighborhood_dawn`, `pull` | *Hãy lan tỏa thông điệp này để cùng nhau xây dựng một cộng đồng an toàn, nơi mọi mái nhà thực sự là một tổ ấm bình yên của tình thương yêu trọn vẹn.* | — | — |  |
| 5-42 | `5.05#22` (9,7 s) | H | T1 | `t17_rebirth_sunlight_blooming_meadow`, `still` | *Chân thành cảm ơn quý vị đã dành thời gian theo dõi trọn vẹn hồ sơ phân tích tâm lý học tội phạm đầy xúc động ngày hôm nay trên kênh Amber Eyes.* | — | — |  |
| 5-43 | `5.05#23` (8,7 s) | H | T1 | `t17_amber_eyes_closing_dossier_turpin`, `push` | *Xin quý vị hãy nhấn nút đăng ký kênh, bật chuông thông báo và để lại những bình luận chia sẻ góc nhìn sâu sắc của mình dưới video này.* | — | — |  |
| 5-44 | `5.05#24` (8,8 s) | H | T1 | `t17_amber_eyes_closing_dossier_turpin`, `pan` | *Sự đồng hành quý báu của quý vị chính là nguồn động lực lớn lao giúp chúng tôi tiếp tục hành trình giải mã những bí ẩn tâm lý của nhân loại.* | — | — |  |
| 5-45 | `5.05#25` (4,7 s) | H | T1 | `t17_endcard_investigative_archive_wall`, `pull` | *Xin kính chào tạm biệt và hẹn gặp lại quý vị trong những tập hồ sơ tiếp theo.* | — | — |  |
| 5-46 | hết tập (0,0 s) | — | T2 | `t17_amber_eyes_closing_dossier_turpin`, `still` | **HỒ SƠ TẬP 17 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | — | ⊘ | ◼ |

**Tổng:** 231 dòng · 226 câu · 5 hồi · nền dùng 131 loại (FLUX 2K Kaggle).
