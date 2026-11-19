# HỒ SƠ SẢN XUẤT TẬP 16 · "KẺ TƯỚC ĐOẠT MẠNG SỐNG CẢ GIA ĐÌNH ĐỂ 'ĐƯA HỌ LÊN THIÊN ĐÀNG' — JOHN LIST"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 16: Kẻ Tước Đoạt Mạng Sống Cả Gia Đình Để 'Đưa Họ Lên Thiên Đàng' (Hồ Sơ John List)** |
| Vụ án | Thảm kịch gia đình John List — Biệt thự Breeze Knoll, Westfield, New Jersey (09/11/1971) |
| Chủ đề | Rối loạn nhân cách ám ảnh cưỡng chế (OCPD), Bẫy ngụy biện đạo đức, Cuộc trốn chạy 18 năm dưới danh tính Robert Clark & Bức tượng sáp Frank Bender |
| Tổng thời lượng | **2576.1 s (~42 phút 56 giây)** · 5 hồi · **257 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Jean Phillips - Giáo viên kịch) · N2 (Wanda Flanery - Hàng xóm Colorado) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap16.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.mp3` & `02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2567.1 s, kết thúc audio tại 2576.1 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **120.0 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.0 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **205.1 Hz**
- **Jean Phillips ($N1$ · Cừu):** F0 trung vị = **183.2 Hz**
- **Wanda Flanery ($N2$ · Mèo):** F0 trung vị = **282.4 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.56\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.28\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.74%** (CER trung bình: **11.25%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.61 / 5.0** (Dải điểm: 1.65 – 3.48). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap16/xuat_ban/CanNghe_Tap16_higgs.md`](xuat_ban/CanNghe_Tap16_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.mp3`](xuat_ban/Tap16_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.wav`](xuat_ban/Tap16_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t16.json`](../../.work/timeline_s_t16.json) (2576.1 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap16/xuat_ban/Tap16.srt`](xuat_ban/Tap16.srt) (257 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep16_vi.json`](../../.work/quality_qc_utmos_ep16_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap16/xuat_ban/CanNghe_Tap16_higgs.md`](xuat_ban/CanNghe_Tap16_higgs.md)

---

## 6. DANH SÁCH SHOT — TẬP 16 (VI)

Bảng sinh tự động bởi `.work/_gen_shots_t16.py` (cùng mã shot và nền cho cả VI/EN/JA — H17). *Chữ* = nguyên văn câu của shot (H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ⇒ **đậm**.

### INTRO KÊNH · 0,00–22,41 s

Đặt `assets/brand/intro_kenh.mov` tại 0,00 s. Không câu thoại nào thuộc intro.

### HỒI 1

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.02#1` (10,8 s) | H | T1 | `t16_a1_c01_breeze_knoll_victorian_facade`, `pan` | *Vào cuối năm 1971, tại thị trấn giàu có Westfield thuộc bang New Jersey, một sự tĩnh lặng bất thường bao trùm lên căn biệt thự Breeze Knoll.* | — | ✦ Cú |  |
| 1-02 | `1.02#2` (8,1 s) | H | T1 | `t16_a1_c01_breeze_knoll_victorian_facade`, `pull` | *Đó là một dinh thự phong cách Victoria cổ kính gồm mười chín phòng, nơi sinh sống của gia đình người kế toán nghiêm cẩn John List.* | — | — |  |
| 1-03 | `1.02#3` (7,4 s) | H | T1 | `t16_a1_c01_breeze_knoll_victorian_facade`, `still` | *Suốt gần một tháng kể từ ngày 9 tháng 11, toàn bộ hệ thống đèn trong ngôi nhà luôn rực sáng suốt ngày đêm.* | — | — |  |
| 1-04 | `1.02#4` (10,4 s) | H | T1 | `t16_westfield_residential_avenue_spring`, `push` | *Giữa những đêm đông lạnh buốt, từ bên trong căn nhà vắng vọng ra giai điệu thánh ca organ trầm buồn đều đặn, nhưng tuyệt nhiên không một ai thấy bóng dáng các thành viên bước ra ngoài.* | — | — |  |
| 1-05 | `1.02#5` (7,8 s) | H | T1 | `t16_westfield_residential_avenue_spring`, `pan` | *Hàng xóm xung quanh chỉ nhìn thấy thư từ và các số báo giao hàng ngày dần chất đống trước thềm hiên phủ đầy tuyết trắng.* | — | — |  |
| 1-06 | `1.02#6` (7,4 s) | H | T1 | `t16_westfield_residential_avenue_spring`, `pull` | *Ngôi biệt thự uy nghi dường như đã bị đóng băng trong một dòng thời gian tách biệt hoàn toàn với nhịp sống hối hả bên ngoài.* | — | — |  |
| 1-07 | `1.02#7` (9,4 s) | H | T1 | `t16_a1_c07_snow_covered_porch_unread_mail`, `still` | *Sự biến mất kéo dài và kỳ lạ của năm con người trong một gia đình sùng đạo mẫu mực bắt đầu gieo rắc nỗi hoang mang tột độ cho cả thị trấn.* | — | — |  |
| 1-08 | `1.02#8` (9,5 s) | H | T1 | `t16_a1_c07_snow_covered_porch_unread_mail`, `push` | *Một dự cảm chẳng lành len lỏi vào tâm trí những người quen biết, báo hiệu một sự thật kinh hoàng đang chực chờ hé lộ phía sau những cánh cửa khóa kín.* | — | — |  |
| 1-09 | `1.04#1` (7,4 s) | H | T1 | `t16_a1_c07_snow_covered_porch_unread_mail`, `pan` | *Gia đình John List từ lâu đã được cả cộng đồng Westfield tôn vinh như hình mẫu hoàn hảo của tầng lớp trung lưu danh giá.* | — | — |  |
| 1-10 | `1.04#2` (10,9 s) | H | T1 | `t16_breeze_knoll_snowy_porch_mail`, `pull` | *Người chủ gia đình John List bốn mươi sáu tuổi, là cựu quân nhân Thế chiến thứ hai, một kế toán viên mẫn cán và là Phó chủ tịch một ngân hàng lớn tại New Jersey.* | — | — |  |
| 1-11 | `1.04#3` (11,9 s) | H | T1 | `t16_breeze_knoll_snowy_porch_mail`, `still` | *Ông ta luôn xuất hiện trước công chúng trong những bộ âu phục chỉnh tề, thắt cà vạt nghiêm túc và giữ vai trò Trưởng ban tài chính của Hội đồng giáo xứ Nhà thờ Tin Lành Luther.* | — | — |  |
| 1-12 | `1.04#4` (10,2 s) | H | T1 | `t16_breeze_knoll_snowy_porch_mail`, `push` | *Chung sống trong dinh thự mười chín phòng là người vợ Helen bốn mươi lăm tuổi, mẹ ruột Alma tám mươi tư tuổi và ba người con đang tuổi ăn tuổi học.* | — | — |  |
| 1-13 | `1.04#5` (8,0 s) | H | T1 | `t16_a1_c03_breeze_knoll_grand_hall_shadows`, `pan` | *Dưới mắt bạn bè và đồng nghiệp, đó là một tổ ấm kiểu mẫu hội tụ đủ danh vọng, đạo đức và sự kính Chúa mẫu mực.* | — | — |  |
| 1-14 | `1.04#6` (10,4 s) | H | T1 | `t16_a1_c03_breeze_knoll_grand_hall_shadows`, `pull` | *Thế nhưng, chính chiếc mặt nạ đạo mạo ấy đã tạo nên một “Hiệu ứng Hào quang” hoàn hảo, làm mù quáng mọi sự nghi ngờ từ cộng đồng xung quanh suốt một thời gian dài.* | — | — |  |
| 1-15 | `1.04#7` (9,9 s) | H | T1 | `t16_a1_c03_breeze_knoll_grand_hall_shadows`, `still` | *Người ta từ chối tin rằng một người đàn ông chuẩn mực, luôn cúi đầu chào lịch thiệp trước cổng nhà thờ, lại có thể che giấu những vết nứt hủy diệt bên trong tâm trí.* | — | — |  |
| 1-16 | `1.04#8` (8,0 s) | H | T1 | `t16_a1_c02_john_list_conservative_suit_silhouette`, `push` | *Khi những sự bất thường bắt đầu lộ diện, thành kiến bình thường hóa đã khiến xã hội lờ đi những tín hiệu báo động đỏ sớm nhất.* | — | — |  |
| 1-17 | `1.04#9` (11,1 s) | H | T1 | `t16_a1_c02_john_list_conservative_suit_silhouette`, `pan` | *Tại những cộng đồng thượng lưu danh giá như thị trấn Westfield, người ta thường tự ru ngủ mình bằng ảo tưởng rằng danh vọng và sự giàu sang có thể miễn trừ cho con người trước cái ác.* | — | — |  |
| 1-18 | `1.04#10` (12,3 s) | H | T1 | `t16_a1_c06_patricia_theater_script_bedroom`, `pull` | *Vẻ ngoài đạo mạo của những bộ âu phục chỉnh tề và nếp sống sùng đạo đã dệt nên một tấm màn nhung êm ái, nhưng vô tình làm tê liệt hoàn toàn phản xạ cảnh giác tự nhiên của xã hội.* | — | — |  |
| 1-19 | `1.04#11` (10,9 s) | H | T1 | `t16_a1_c06_patricia_theater_script_bedroom`, `still` | *Suốt gần một tháng trời căn biệt thự rực sáng đèn giữa đêm đông và báo chí chất đống trước hiên, hàng xóm xung quanh chỉ nhìn rồi bước qua trong sự im lặng giữ kẽ.* | — | — |  |
| 1-20 | `1.04#12` (8,6 s) | H | T1 | `t16_a1_c06_patricia_theater_script_bedroom`, `push` | *Chính sự thờ ơ tập thể đội lốt tôn trọng quyền riêng tư ấy đã tạo nên một khoảng chân không an toàn cho tội ác đóng băng hiện trường.* | — | — |  |
| 1-21 | `1.06#1` (7,2 s) | H | T1 | `t16_autumn_sunlight_westfield_suburb`, `pan` | *Đằng sau sự hào nhoáng của căn biệt thự Breeze Knoll là một cơn ác mộng tài chính ngày càng vượt khỏi tầm kiểm soát.* | — | — |  |
| 1-22 | `1.06#2` (10,5 s) | H | T1 | `t16_autumn_sunlight_westfield_suburb`, `pull` | *Mùa hè năm 1971, John List bất ngờ bị ngân hàng sa thải, đánh sập nguồn thu nhập duy nhất để gánh vác chi phí vận hành dinh thự khổng lồ.* | — | — |  |
| 1-23 | `1.06#3` (9,2 s) | H | T1 | `t16_autumn_sunlight_westfield_suburb`, `still` | *Thay vì dũng cảm đối diện với thực tại và chia sẻ cùng gia đình, nỗi sợ hãi mất thể diện đã kích hoạt một chuỗi hành vi dối trá bệnh lý.* | — | — |  |
| 1-24 | `1.06#4` (8,9 s) | H | T1 | `t16_a1_c04_unemployment_bank_deficit_letters`, `push` | *Mỗi buổi sáng, ông ta vẫn mặc vest, xách cặp rời nhà đúng giờ như đi làm, rồi ngồi suốt ngày ở bến tàu đọc báo để giết thời gian.* | — | — |  |
| 1-25 | `1.06#5` (8,0 s) | H | T1 | `t16_a1_c04_unemployment_bank_deficit_letters`, `pan` | *Để duy trì cuộc sống giả tạo, List đã lén lút rút cạn hai trăm nghìn đô la từ tài khoản tiết kiệm của người mẹ già Alma.* | — | — |  |
| 1-26 | `1.06#6` (9,0 s) | H | T1 | `t16_a1_c04_unemployment_bank_deficit_letters`, `pull` | *Đến đầu tháng 11 năm 1971, số tiền chiếm đoạt cũng cạn sạch, và ngân hàng bắt đầu gửi thông báo tịch thu căn biệt thự.* | — | — |  |
| 1-27 | `1.06#7` (5,3 s) | H | T1 | `t16_accountant_ledger_red_deficit_ink`, `still` | *Trong bước đường cùng, một kế hoạch tàn độc đã thành hình trong đầu người kế toán cuồng kiểm soát.* | — | — |  |
| 1-28 | `1.07#1` (9,9 s) | N1 | T4 | `t16_accountant_ledger_red_deficit_ink`, `push` | *Hãy hình dung tâm trạng ngột ngạt và nỗi âu lo trĩu nặng của những người quen biết cô bé Patricia List vào những tuần lễ cuối năm 1971.* | — | ✦ Cừu |  |
| 1-29 | `1.07#2` (9,0 s) | N1 | T4 | `t16_accountant_ledger_red_deficit_ink`, `pan` | *Patricia khi ấy mười sáu tuổi, một nữ sinh xinh xắn, thông minh và mang trong mình niềm đam mê cháy bỏng với nghệ thuật kịch nghệ sân khấu.* | — | — |  |
| 1-30 | `1.07#3` (10,5 s) | N1 | T4 | `t16_a1_c05_john_pretending_train_commute`, `pull` | *Trong mắt người cha nghiêm khắc cực đoan, việc con gái bước lên sàn diễn và tiếp cận với văn hóa đương đại bị coi là biểu hiện của sự nổi loạn và tội lỗi không thể dung thứ.* | — | — |  |
| 1-31 | `1.07#4` (8,8 s) | N1 | T4 | `t16_a1_c05_john_pretending_train_commute`, `still` | *Vài tuần trước khi vụ án xảy ra, Patricia đã nhiều lần tâm sự trong nước mắt với tôi rằng em cảm thấy ngột ngạt đến nghẹt thở bên trong căn nhà ấy.* | — | — |  |
| 1-32 | `1.07#5` (6,6 s) | N1 | T4 | `t16_a1_c05_john_pretending_train_commute`, `push` | *Em từng thốt lên một câu nói khiến tôi lạnh sống lưng: “Em sợ bố em sẽ làm điều gì đó kinh khủng với cả gia đình.”* | — | — |  |
| 1-33 | `1.07#6` (10,1 s) | N1 | T4 | `t16_breeze_knoll_attic_staircase_shadows`, `pan` | *Khi cả ba chị em Patricia đột ngột vắng mặt ở trường nhiều tuần liền, nhà trường chỉ nhận được một mẩu giấy xin phép ngắn ngủi với lý do về quê thăm bà ngoại bị ốm.* | — | — |  |
| 1-34 | `1.07#7` (10,1 s) | N1 | T4 | `t16_breeze_knoll_attic_staircase_shadows`, `pull` | *Mỗi lần đi ngang qua biệt thự Breeze Knoll trong đêm đông, nhìn ánh đèn sáng quạnh quẽ và nghe tiếng đàn thánh ca văng vẳng, tôi luôn cảm thấy một linh cảm bất an ghê rợn.* | — | — |  |
| 1-35 | `1.07#8` (8,0 s) | N1 | T4 | `t16_a1_c08_police_flashlight_entering_window`, `still` | *Suốt nhiều năm tháng về sau, câu nói kêu cứu của cô học trò nhỏ vẫn ám ảnh tâm trí tôi như một nỗi day dứt không bao giờ nguôi ngoai.* | — | — |  |
| 1-36 | `1.07#9` (9,6 s) | N1 | T4 | `t16_a1_c08_police_flashlight_entering_window`, `push` | *Mỗi khi nhớ lại ánh mắt thảng thốt của Patricia trong căn phòng tập kịch chiều hôm ấy, tim tôi như bị bóp nghẹt bởi sự bất lực và nỗi ân hận khôn nguôi.* | — | — |  |
| 1-37 | `1.07#10` (9,2 s) | N1 | T4 | `t16_a1_c08_police_flashlight_entering_window`, `pan` | *Con bé đã cảm nhận được hơi thở lạnh lẽo của hiểm họa đang bủa vây quanh mình, em đã dũng cảm cất lên tiếng kêu cứu với người lớn duy nhất mà em tin tưởng.* | — | — |  |
| 1-38 | `1.07#11` (11,8 s) | N1 | T4 | `t16_a1_c09_freezing_corridor_silent_mansion`, `pull` | *Nhưng lúc ấy, tôi đã tự trấn an rằng đó chỉ là những áp lực tâm lý tuổi dậy thì trong một gia đình quá đỗi khắt khe, rằng một người cha mẫu mực như ông List sẽ không bao giờ làm hại con cái.* | — | — |  |
| 1-39 | `1.07#12` (7,0 s) | N1 | T4 | `t16_a1_c09_freezing_corridor_silent_mansion`, `still` | *Sự ngây thơ và do dự của chính tôi đã tước đi cơ hội sống sót cuối cùng của một tâm hồn trẻ thơ vô tội.* | — | — |  |
| 1-40 | `1.09#1` (8,4 s) | H | T1 | `t16_a1_c09_freezing_corridor_silent_mansion`, `push` | *Nỗi bất an của những người xung quanh cuối cùng đã lên đến đỉnh điểm sau gần một tháng không có bất kỳ dấu hiệu sống nào từ ngôi nhà.* | — | — |  |
| 1-41 | `1.09#2` (11,3 s) | H | T1 | `t16_forensic_ballistics_evidence_markers`, `pan` | *Tối ngày 7 tháng 12 năm 1971, cảnh sát thị trấn Westfield quyết định cạy mở một ô cửa sổ tầng hầm để tiến vào bên trong biệt thự.* | — | — |  |
| 1-42 | `1.09#3` (8,2 s) | H | T1 | `t16_forensic_ballistics_evidence_markers`, `pull` | *Một luồng không khí băng giá phả vào mặt các sĩ quan tuần tra, bởi hệ thống lò sưởi đã bị tắt ngấm từ nhiều tuần trước đó.* | — | — |  |
| 1-43 | `1.09#4` (8,4 s) | H | T1 | `t16_forensic_ballistics_evidence_markers`, `still` | *Ngôi biệt thự rộng lớn chìm trong mùi ẩm mốc lạnh lẽo, xen lẫn tiếng nhạc thánh ca organ vẫn đều đặn phát ra từ chiếc máy hát tự động.* | — | — |  |
| 1-44 | `1.09#5` (7,2 s) | H | T1 | `t16_a1_c10_ballroom_sleeping_bags_tiffany_skylight`, `push` | *Khi bước chân vào căn phòng khiêu vũ lớn ở tầng một, lực lượng chức năng sững sờ trước một hiện trường bi thương đến nghẹt thở.* | — | — |  |
| 1-45 | `1.09#6` (8,7 s) | H | T1 | `t16_a1_c10_ballroom_sleeping_bags_tiffany_skylight`, `pan` | *Bốn sinh mạng gồm người vợ Helen và ba người con được xếp nằm ngay ngắn cạnh nhau trên những tấm túi ngủ trải giữa sàn gỗ.* | — | — |  |
| 1-46 | `1.09#7` (8,6 s) | H | T1 | `t16_a1_c10_ballroom_sleeping_bags_tiffany_skylight`, `pull` | *Phía trên đầu họ là mái vòm bằng kính màu nghệ thuật tuyệt mỹ, soi rọi xuống một thảm kịch gia đình chấn động bậc nhất lịch sử nước Mỹ.* | — | — |  |
| 1-47 | `1.10#1` (10,5 s) | D | T1 | `t16_breeze_knoll_grand_ballroom_empty`, `still` | *Kết quả khám nghiệm thực địa cho thấy toàn bộ các nạn nhân đều bị tước đoạt mạng sống vào ngày 9 tháng 11 năm 1971, tức gần một tháng trước thời điểm cảnh sát vào nhà.* | — | ✦ Sói |  |
| 1-48 | `1.10#2` (6,5 s) | D | T1 | `t16_breeze_knoll_grand_ballroom_empty`, `push` | *Hung thủ đã lên kế hoạch tỉ mỉ để lần lượt tiễn đưa từng người thân trong cùng một ngày nhằm tránh sự phản kháng dây chuyền.* | — | — |  |
| 1-49 | `1.10#3` (6,6 s) | D | T1 | `t16_breeze_knoll_grand_ballroom_empty`, `pan` | *Trên căn phòng gác mái ở tầng ba, chúng tôi phát hiện người mẹ già Alma tám mươi tư tuổi cũng đã trút hơi thở cuối cùng.* | — | — |  |
| 1-50 | `1.10#4` (8,3 s) | D | T1 | `t16_a1_c11_confession_letter_five_pages_pastor`, `pull` | *Cách sắp đặt các nạn nhân thẳng hàng và ngay ngắn trong phòng khiêu vũ phản ánh rõ nét tư duy trật tự và màu sắc nghi thức cá nhân của kẻ thủ ác.* | — | — |  |
| 1-51 | `1.10#5` (9,7 s) | D | T1 | `t16_a1_c11_confession_letter_five_pages_pastor`, `still` | *Tại hiện trường, trên bàn làm việc của John List, cảnh sát thu giữ một bức thư dài năm trang gửi cho Mục sư Eugene Rehwinkel thuộc Giáo xứ Redeemer Lutheran.* | — | — |  |
| 1-52 | `1.10#6` (9,7 s) | D | T1 | `t16_a1_c11_confession_letter_five_pages_pastor`, `push` | *Trong bức thư ấy, John List lạnh lùng giãi bày rằng ông ta làm vậy để “đưa linh hồn gia đình lên Thiên đàng” trước khi họ bị hủy hoại bởi cảnh bần cùng và sự tha hóa đạo đức.* | — | — |  |
| 1-53 | `1.10#7` (6,6 s) | D | T1 | `t16_a1_c12_chevrolet_impala_abandoned_airport`, `pan` | *Bức thư kết thúc bằng lời khẳng định rằng bản thân ông ta phải tiếp tục sống để tìm cách xưng tội với Thượng đế trước khi qua đời.* | — | — |  |
| 1-54 | `1.11#1` (8,2 s) | H | T1 | `t16_a1_c12_chevrolet_impala_abandoned_airport`, `pull` | *Bức thư để lại không chỉ là một văn bản thú tội lạnh lùng, mà còn phơi bày sự hoang tưởng bệnh lý đội lốt lòng vị tha méo mó.* | — | — |  |
| 1-55 | `1.11#2` (8,8 s) | H | T1 | `t16_a1_c12_chevrolet_impala_abandoned_airport`, `still` | *Sau khi hủy diệt toàn bộ tổ ấm của chính mình, người đàn ông ấy đã thực hiện một cuộc tẩu thoát được tính toán đến từng chi tiết nhỏ nhất.* | — | — |  |
| 1-56 | `1.11#3` (6,8 s) | H | T1 | `t16_chevrolet_impala_airport_parking_snow`, `push` | *Cảnh sát phát hiện ra rằng hung thủ đã có gần một tháng dẫn trước để xóa sạch mọi dấu vết truy nguyên.* | — | — |  |
| 1-57 | `1.11#4` (5,9 s) | H | T1 | `t16_chevrolet_impala_airport_parking_snow`, `pan` | *Một cuộc săn lùng tội phạm xuyên quốc gia quy mô lớn chính thức được kích hoạt trên toàn lãnh thổ Mỹ.* | — | — |  |
| 1-58 | `1.11#5` (7,6 s) | H | T1 | `t16_chevrolet_impala_airport_parking_snow`, `pull` | *Nhưng không ai có thể ngờ rằng, bóng ma mang tên John List sẽ biến mất không một dấu tích suốt gần hai thập kỷ tiếp theo.* | — | — |  |
| 1-59 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 02* · **VỤ MẤT TÍCH THẾ KỶ VÀ CHIẾC KÉO CẮT MẶT TRONG ALBUM ẢNH** | — | ⊘ | ◼ |

### HỒI 2

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (9,2 s) | H | T1 | `t16_a2_c01_detectives_dusting_empty_frames`, `still` | *Ngay khi vụ án kinh hoàng bị phơi bày, lực lượng điều tra đã lập tức rà soát toàn bộ căn biệt thự mười chín phòng để thu thập hình ảnh nhận dạng nghi phạm.* | — | — |  |
| 2-02 | `2.02#2` (7,0 s) | H | T1 | `t16_a2_c01_detectives_dusting_empty_frames`, `push` | *Tuy nhiên, các thám tử đã gặp phải một cảnh tượng khiến tất cả phải rùng mình kinh hãi trước sự lạnh lùng của hung thủ.* | — | — |  |
| 2-03 | `2.02#3` (7,4 s) | H | T1 | `t16_a2_c01_detectives_dusting_empty_frames`, `pan` | *Mọi cuốn album ảnh gia đình, mọi bức chân dung treo tường và các giấy tờ lưu niệm trong nhà đều bị xới tung.* | — | — |  |
| 2-04 | `2.02#4` (5,9 s) | H | T1 | `t16_a2_c02_family_album_cutout_faces`, `pull` | *Khuôn mặt của John List đã bị cắt bỏ một cách tỉ mỉ và biến mất hoàn toàn khỏi từng bức ảnh.* | — | — |  |
| 2-05 | `2.02#5` (7,0 s) | H | T1 | `t16_a2_c02_family_album_cutout_faces`, `still` | *Hung thủ đã dùng một chiếc kéo sắc để xóa sổ diện mạo của chính mình ra khỏi lịch sử của gia đình Breeze Knoll.* | — | — |  |
| 2-06 | `2.04#1` (9,1 s) | H | T1 | `t16_a2_c02_family_album_cutout_faces`, `push` | *Hành vi cắt bỏ khuôn mặt trong album không đơn thuần là thủ đoạn che giấu nhận dạng, mà còn mang ý nghĩa biểu tượng sâu sắc trong tâm lý học tội phạm.* | — | — |  |
| 2-07 | `2.04#2` (8,1 s) | H | T1 | `t16_carved_family_album_empty_silhouettes`, `pan` | *Đó là hành động chủ động khai tử danh tính cũ của John List để chuẩn bị tái sinh trong một hình hài xã hội hoàn toàn mới.* | — | — |  |
| 2-08 | `2.04#3` (6,2 s) | H | T1 | `t16_carved_family_album_empty_silhouettes`, `pull` | *Trước khi khóa trái cửa rời đi, List đã thực hiện một kịch bản nghi binh vô cùng tinh vi và kín kẽ.* | — | — |  |
| 2-09 | `2.04#4` (6,1 s) | H | T1 | `t16_a2_c03_sharp_scissors_cut_photos_floor`, `still` | *Hắn trực tiếp đến trường gửi đơn xin phép cho ba đứa trẻ nghỉ học dài ngày để về quê thăm người thân.* | — | — |  |
| 2-10 | `2.04#5` (6,9 s) | H | T1 | `t16_a2_c03_sharp_scissors_cut_photos_floor`, `push` | *Hắn liên hệ bưu điện và các đại lý để tạm ngừng dịch vụ giao sữa, giao báo và chuyển phát thư tín.* | — | — |  |
| 2-11 | `2.04#6` (7,9 s) | H | T1 | `t16_a2_c03_sharp_scissors_cut_photos_floor`, `pan` | *Đài phát thanh được hắn điều chỉnh âm lượng vừa phải, phát nhạc tôn giáo liên tục nhằm tạo ảo giác căn nhà vẫn có người sinh hoạt bình thường.* | — | — |  |
| 2-12 | `2.04#7` (7,2 s) | H | T1 | `t16_a2_c04_shredded_birth_certificates_records`, `pull` | *Nhiệt độ của hệ thống lò sưởi được hạ xuống mức thấp nhất để làm chậm quá trình phân hủy tự nhiên của các nạn nhân.* | — | — |  |
| 2-13 | `2.04#8` (11,1 s) | H | T1 | `t16_a2_c04_shredded_birth_certificates_records`, `still` | *Chiếc xe ô tô gia đình sau đó được tìm thấy tại bãi đỗ của Sân bay Quốc tế Kennedy ở thành phố New York, tạo nên một hiện trường giả về một cuộc đào tẩu bằng đường hàng không.* | — | — |  |
| 2-14 | `2.06#1` (5,8 s) | D | T1 | `t16_a2_c04_shredded_birth_certificates_records`, `push` | *Việc phát hiện chiếc xe hơi tại Sân bay Kennedy thoạt nhìn giống như một manh mối đột phá cho cơ quan điều tra.* | — | — |  |
| 2-15 | `2.06#2` (8,6 s) | D | T1 | `t16_a2_c05_erasing_past_identity_metaphor`, `pan` | *Tuy nhiên, sau khi rà soát hàng ngàn danh sách hành khách trên tất cả các chuyến bay nội địa và quốc tế, chúng tôi không tìm thấy bất kỳ dấu vết nào của John List.* | — | — |  |
| 2-16 | `2.06#3` (6,6 s) | D | T1 | `t16_a2_c05_erasing_past_identity_metaphor`, `pull` | *Các đặc vụ FBI nhanh chóng nhận định rằng chiếc xe ở sân bay chỉ là một đòn hỏa mù được tính toán kỹ lưỡng.* | — | — |  |
| 2-17 | `2.06#4` (7,8 s) | D | T1 | `t16_a2_c06_vintage_radio_humming_hymns`, `still` | *Trên thực tế, John List đã bắt một chuyến tàu hỏa rời khỏi New York ngay trong ngày hôm đó để di chuyển sâu vào vùng Trung Tây nước Mỹ.* | — | — |  |
| 2-18 | `2.06#5` (5,6 s) | D | T1 | `t16_a2_c06_vintage_radio_humming_hymns`, `push` | *Khoảng thời gian dẫn trước gần ba mươi ngày đã giúp hung thủ xóa sạch dấu vết di chuyển ban đầu một cách triệt để.* | — | — |  |
| 2-19 | `2.06#6` (7,4 s) | D | T1 | `t16_a2_c06_vintage_radio_humming_hymns`, `pan` | *Lệnh truy nã toàn liên bang được ban hành trên khắp năm mươi tiểu bang, nhưng hồ sơ vụ án nhanh chóng rơi vào trạng thái bế tắc hoàn toàn.* | — | — |  |
| 2-20 | `2.06#7` (6,4 s) | D | T1 | `t16_a2_c07_thermostat_cranked_freezing_cold`, `pull` | *Nghi phạm dường như đã bốc hơi vào không khí, không để lại bất cứ một giao dịch ngân hàng hay tín hiệu liên lạc nào.* | — | — |  |
| 2-21 | `2.08#1` (9,5 s) | H | T1 | `t16_a2_c07_thermostat_cranked_freezing_cold`, `still` | *Những năm tháng sau đó, thảm kịch tại biệt thự Breeze Knoll dần trở thành một truyền thuyết đô thị u tối ám ảnh hạt Union và bang New Jersey.* | — | — |  |
| 2-22 | `2.08#2` (11,8 s) | H | T1 | `t16_a2_c07_thermostat_cranked_freezing_cold`, `push` | *Tháng 8 năm 1972, ngôi biệt thự bỏ hoang bị thiêu rụi hoàn toàn trong một vụ hỏa hoạn bí ẩn, chôn vùi vĩnh viễn mái vòm kính màu Tiffany tuyệt đẹp.* | — | — |  |
| 2-23 | `2.08#3` (10,6 s) | H | T1 | `t16_interstate_bus_terminal_rain_neon`, `pan` | *Cùng với tro tàn của ngôi nhà, những hình ảnh ít ỏi về John List trên các áp phích truy nã của FBI cũng dần trở nên ố vàng và lỗi thời theo năm tháng.* | — | — |  |
| 2-24 | `2.08#4` (8,5 s) | H | T1 | `t16_interstate_bus_terminal_rain_neon`, `pull` | *Lực lượng thực thi pháp luật đã tiếp nhận hàng ngàn cuộc gọi tố giác từ công chúng, nhưng tất cả các đầu mối đều dẫn đến ngõ cụt thất vọng.* | — | — |  |
| 2-25 | `2.08#5` (9,2 s) | H | T1 | `t16_a2_c08_fbi_wanted_poster_hundreds_stamps`, `still` | *Dư luận xã hội rơi vào trạng thái hoài nghi và bất an kéo dài trước câu hỏi liệu công lý có bao giờ chạm tay tới kẻ thủ ác hay không.* | — | — |  |
| 2-26 | `2.08#6` (8,8 s) | H | T1 | `t16_a2_c08_fbi_wanted_poster_hundreds_stamps`, `push` | *Người dân địa phương tự hỏi làm sao một kẻ đoạt mạng năm người thân ruột thịt lại có thể ung dung tồn tại ngoài vòng pháp luật suốt chừng ấy năm.* | — | — |  |
| 2-27 | `2.08#7` (7,8 s) | H | T1 | `t16_a2_c09_mysterious_fire_breeze_knoll_ruins`, `pan` | *Sự im lặng của thời gian như một thách thức nghiệt ngã đối với lương tri và trách nhiệm của những người làm công tác điều tra.* | — | — |  |
| 2-28 | `2.09#1` (7,7 s) | D | T1 | `t16_a2_c09_mysterious_fire_breeze_knoll_ruins`, `pull` | *Suốt mười tám năm ròng rã, hồ sơ mang mã hiệu John Emil List chưa bao giờ bị khép lại trên bàn làm việc của cảnh sát Westfield.* | — | — |  |
| 2-29 | `2.09#2` (6,2 s) | D | T1 | `t16_a2_c09_mysterious_fire_breeze_knoll_ruins`, `still` | *Các thế hệ điều tra viên kỳ cựu đều chia sẻ chung một nhận định nghiệp vụ sâu sắc về bản chất của đối tượng đào tẩu này.* | — | — |  |
| 2-30 | `2.09#3` (7,8 s) | D | T1 | `t16_a2_c10_cold_case_dossier_growing_dust`, `push` | *Chúng tôi tin rằng một người đàn ông có thói quen sống cứng nhắc và bảo thủ như List sẽ không bao giờ có thể thay đổi lối sống bản năng của mình.* | — | — |  |
| 2-31 | `2.09#4` (8,2 s) | D | T1 | `t16_a2_c10_cold_case_dossier_growing_dust`, `pan` | *Hắn nhất định đang ẩn mình dưới một danh tính giả ở một thị trấn bình yên nào đó, tiếp tục làm công việc kế toán sổ sách và đi lễ nhà thờ mỗi chủ nhật.* | — | — |  |
| 2-32 | `2.09#5` (7,0 s) | D | T1 | `t16_a2_c10_cold_case_dossier_growing_dust`, `pull` | *Điểm mấu chốt là tìm ra phương cách để nhận diện một gương mặt đã bị thời gian làm biến đổi sau gần hai thập kỷ lẩn trốn.* | — | — |  |
| 2-33 | `2.09#6` (4,9 s) | D | T1 | `t16_cold_case_dossier_archives_dust`, `still` | *Đó là một bài toán hóc búa vượt quá giới hạn của các kỹ thuật truy nã truyền thống ở thời kỳ đó.* | — | — |  |
| 2-34 | `2.09#7` (11,2 s) | D | T1 | `t16_cold_case_dossier_archives_dust`, `push` | *Để có thể tồn tại suốt mười tám năm ròng rã mà không bị những bóng ma quá khứ quật ngã, bộ não của John List đã vận hành một cơ chế phòng vệ cực hạn mang tên “Sự Chia ngăn Nhận thức”.* | — | — |  |
| 2-35 | `2.09#8` (11,2 s) | D | T1 | `t16_a2_c11_detectives_studying_ocpd_profile`, `pan` | *Hắn đã thành công trong việc đóng băng và niêm phong toàn bộ ký ức về ngày 9 tháng 11 năm 1971 vào một chiếc két sắt tâm lý kiên cố, hoàn toàn cô lập khỏi cuộc sống đời thường.* | — | — |  |
| 2-36 | `2.09#9` (10,4 s) | D | T1 | `t16_a2_c11_detectives_studying_ocpd_profile`, `pull` | *Dưới cái tên Robert Clark, hắn thản nhiên bước vào một cuộc hôn nhân mới, ăn ngon ngủ yên mỗi đêm và tiếp tục duy trì thói quen đi lễ nhà thờ mỗi chủ nhật như một quý ông mẫu mực.* | — | — |  |
| 2-37 | `2.09#10` (14,4 s) | D | T1 | `t16_a2_c12_accountant_ledger_red_ink_cracking`, `still` | *Hắn không hề gặp ác mộng, bởi vì trong thế giới quan méo mó của một kẻ mắc OCPD, bi kịch Breeze Knoll không phải là tội ác tước đoạt mạng sống, mà chỉ là một thủ tục phá sản đau đớn mà hắn đã hoàn tất và đóng sổ sách lại phía sau lưng.* | — | — |  |
| 2-38 | `2.10#1` (12,1 s) | H | T1 | `t16_a2_c13_cognitive_dissonance_moral_trap`, `push` | *Phải chờ đến cuối thập niên 1980, sự giao thoa kỳ diệu giữa nghệ thuật điêu khắc pháp y và sức mạnh của truyền hình đại chúng mới mở ra một lối thoát bất ngờ cho vụ án.* | — | — |  |
| 2-39 | `2.10#2` (8,2 s) | H | T1 | `t16_a2_c13_cognitive_dissonance_moral_trap`, `pan` | *Nhưng trước khi lật mở chiến dịch truy bắt lịch sử ấy, chúng ta cần giải phẫu thế giới nội tâm đen tối và đầy nghịch lý của John List.* | — | — |  |
| 2-40 | `2.10#3` (8,9 s) | H | T1 | `t16_a2_c13_cognitive_dissonance_moral_trap`, `pull` | *Điều gì đã thúc đẩy một người kế toán mẫn cán, một tín đồ sùng đạo chưa từng có tiền án, biến thành kẻ hủy diệt chính tổ ấm của mình?* | — | — |  |
| 2-41 | `2.10#4` (10,4 s) | H | T1 | `t16_a2_c14_psychological_mechanism_rigid_gears`, `still` | *Liệu hành vi tước đoạt mạng sống ấy bắt nguồn từ một cơn loạn thần mất trí, hay là kết quả của một cấu trúc nhân cách bệnh lý bị méo mó bởi niềm tin mù quáng?* | — | — |  |
| 2-42 | `2.10#5` (9,0 s) | H | T1 | `t16_a2_c14_psychological_mechanism_rigid_gears`, `push` | *Các nhà tâm lý học tội phạm hiện đại đã tìm thấy lời giải trong khung lý thuyết về Rối loạn nhân cách ám ảnh cưỡng chế OCPD.* | — | — |  |
| 2-43 | `2.10#6` (7,1 s) | H | T1 | `t16_a2_c15_psychologist_opening_dossier_threshold`, `pan` | *Cùng với đó là chiếc bẫy tư duy ngụy biện mang tên kỹ thuật trung hòa đạo đức vì một mục đích cao cả.* | — | — |  |
| 2-44 | `2.10#7` (9,8 s) | H | T1 | `t16_a2_c15_psychologist_opening_dossier_threshold`, `pull` | *Những cơ chế tâm lý này đã biến tội ác tày trời thành một hành động mà kẻ thủ ác tin rằng mình buộc phải thực hiện để cứu rỗi các nạn nhân.* | — | — |  |
| 2-45 | `2.10#8` (5,9 s) | H | T1 | `t16_a2_c15_psychologist_opening_dossier_threshold`, `still` | *Hãy cùng Chuyên gia tâm lý bóc tách từng lớp mặt nạ nhận thức đằng sau bi kịch Breeze Knoll.* | — | — |  |
| 2-46 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 03* · **GIẢI MÃ TÂM LÝ: RỐI LOẠN NHÂN CÁCH ÁM ẢNH CƯỠNG CHẾ (OCPD) & BẪY NGỤY BIỆN ĐẠO ĐỨC** | — | ⊘ | ◼ |

### HỒI 3

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (7,8 s) | H | T1 | `t16_a3_c01_family_annihilator_shadowy_hall`, `push` | *Trong hệ thống phân loại tội phạm học, John List được xếp vào nhóm hung thủ hủy diệt gia đình mang động cơ “vị tha méo mó”.* | — | — |  |
| 3-02 | `3.02#2` (11,4 s) | H | T1 | `t16_a3_c01_family_annihilator_shadowy_hall`, `pan` | *Thuật ngữ này dùng để chỉ những kẻ tước đoạt sinh mạng người thân không phải vì thù hận bộc phát, mà vì niềm tin bệnh hoạn rằng mình đang cứu họ khỏi một số phận nghiệt ngã hơn.* | — | — |  |
| 3-03 | `3.02#3` (10,6 s) | H | T1 | `t16_a3_c01_family_annihilator_shadowy_hall`, `pull` | *Để thấu hiểu logic lệch lạc này, các nhà phân tích hành vi của FBI đã áp dụng khung bệnh học về Rối loạn nhân cách ám ảnh cưỡng chế, viết tắt là OCPD.* | — | — |  |
| 3-04 | `3.02#4` (11,0 s) | H | T1 | `t16_a3_c02_ocpd_versus_ocd_distorted_mirror`, `still` | *Cần phân biệt rõ OCPD là một rối loạn nhân cách định hình toàn bộ nhân sinh quan của một người, khác hoàn toàn với chứng rối loạn ám ảnh cưỡng chế OCD thường gặp.* | — | — |  |
| 3-05 | `3.02#5` (13,1 s) | H | T1 | `t16_a3_c02_ocpd_versus_ocd_distorted_mirror`, `push` | *Trong khi người mắc OCD luôn đau khổ nhận thức được sự vô lý của các hành vi ám ảnh, thì người mang OCPD lại luôn tin rằng tư duy và hành động của mình là chuẩn mực đạo đức tối thượng.* | — | — |  |
| 3-06 | `3.02#6` (7,2 s) | H | T1 | `t16_a3_c02_ocpd_versus_ocd_distorted_mirror`, `pan` | *Chính niềm tin tuyệt đối vào sự hoàn hảo này đã dẫn dắt John List bước vào một mê cung tâm lý không có lối thoát.* | — | — |  |
| 3-07 | `3.03#1` (11,2 s) | C | T1 | `t16_a3_c03_strict_puritanical_childhood_bible`, `pull` | *Những đặc điểm cốt lõi của Rối loạn nhân cách ám ảnh cưỡng chế OCPD là sự bận tâm quá mức về trật tự, tính quy củ cứng nhắc, chủ nghĩa hoàn hảo và nhu cầu kiểm soát tuyệt đối môi trường xung quanh.* | — | ✦ Cáo |  |
| 3-08 | `3.03#2` (8,4 s) | C | T1 | `t16_a3_c03_strict_puritanical_childhood_bible`, `still` | *Lớn lên dưới sự giáo dưỡng hà khắc của người mẹ Alma trong một môi trường tôn giáo bảo thủ, John List đã hình thành một nhân sinh quan nhị nguyên vô cùng cực đoan.* | — | — |  |
| 3-09 | `3.03#3` (8,8 s) | C | T1 | `t16_a3_c03_strict_puritanical_childhood_bible`, `push` | *Trong thế giới quan của ông ta, mọi sự việc chỉ tồn tại dưới hai thái cực đối lập: hoặc là hoàn hảo theo đúng luật lệ, hoặc là sự suy đồi và sa ngã vĩnh viễn.* | — | — |  |
| 3-10 | `3.03#4` (8,3 s) | C | T1 | `t16_lutheran_cross_austere_study_wall`, `pan` | *Ông ta áp đặt kỷ luật thép kiểu quân đội lên từng bữa ăn, kiểm soát chi tiêu của vợ con đến từng đồng xu lẻ và cấm đoán mọi thú vui giải trí hiện đại.* | — | — |  |
| 3-11 | `3.03#5` (9,0 s) | C | T1 | `t16_lutheran_cross_austere_study_wall`, `pull` | *Đối với một người mắc OCPD, sự thất bại về mặt kinh tế hay mất đi địa vị xã hội không chỉ là khó khăn đơn thuần, mà là sự sụp đổ của toàn bộ bản ngã.* | — | — |  |
| 3-12 | `3.03#6` (7,5 s) | C | T1 | `t16_a3_c04_chasm_between_perfection_ruin`, `still` | *Khi bị mất việc tại ngân hàng và rơi vào cảnh nợ nần chồng chất, cấu trúc trật tự do List dày công xây dựng đã bị đe dọa phá hủy hoàn toàn.* | — | — |  |
| 3-13 | `3.03#7` (6,6 s) | C | T1 | `t16_a3_c04_chasm_between_perfection_ruin`, `push` | *Khoảng cách không thể san lấp giữa ảo tưởng kiểm soát và thực tại bất lực đã đẩy ông ta vào một cơn khủng hoảng nhận thức nghiêm trọng.* | — | — |  |
| 3-14 | `3.03#8` (7,0 s) | C | T1 | `t16_a3_c04_chasm_between_perfection_ruin`, `pan` | *Để bảo vệ chiếc mặt nạ kiêu hãnh của bản ngã ái kỷ, tâm trí của List đã kích hoạt một cơ chế phòng vệ cực đoan nhất có thể hình dung.* | — | — |  |
| 3-15 | `3.03#9` (7,8 s) | C | T1 | `t16_a3_c04_chasm_between_perfection_ruin`, `pull` | *Thay vì chấp nhận thất bại và tìm kiếm sự giúp đỡ từ cộng đồng, ông ta đã biến bi kịch tài chính thành một bài toán đạo đức cần được giải quyết bằng bạo lực.* | — | — |  |
| 3-16 | `3.04#1` (8,0 s) | H | T1 | `t16_john_list_a4_01_mansion`, `still` | *Bên cạnh khủng hoảng kinh tế, những biến động bên trong gia đình cũng trở thành ngòi nổ kích hoạt điểm gãy tâm lý của kẻ cuồng kiểm soát.* | — | — |  |
| 3-17 | `3.04#2` (8,6 s) | H | T1 | `t16_john_list_a4_01_mansion`, `push` | *Người vợ Helen sa sút sức khỏe do bệnh tật kéo dài và dần tìm đến rượu như một lối thoát để quên đi sự lạnh nhạt của chồng.* | — | — |  |
| 3-18 | `3.04#3` (8,6 s) | H | T1 | `t16_john_list_a4_01_mansion`, `pan` | *Cô con gái lớn Patricia bắt đầu công khai phản kháng sự kìm kẹp của cha, bộc lộ khát vọng tự do và theo đuổi đam mê nghệ thuật.* | — | — |  |
| 3-19 | `3.04#4` (9,4 s) | H | T1 | `t16_a3_c05_desperate_embezzlement_mother_fund`, `pull` | *Trong mắt một người mang tư duy OCPD xơ cứng, những biểu hiện bình thường ấy lại bị phóng đại thành dấu hiệu của sự tha hóa và ô uế đạo đức.* | — | — |  |
| 3-20 | `3.04#5` (9,6 s) | H | T1 | `t16_a3_c05_desperate_embezzlement_mother_fund`, `still` | *Nỗi sợ hãi tột cùng trước viễn cảnh gia đình phải nhận trợ cấp xã hội và bị xã hội khinh rẻ đã thúc đẩy List đưa ra một quyết định tàn bạo.* | — | — |  |
| 3-21 | `3.05#1` (9,1 s) | C | T1 | `t16_a3_c05_desperate_embezzlement_mother_fund`, `push` | *Đây chính là thời điểm cơ chế Trung hòa đạo đức vì mục đích cao cả, theo lý thuyết của các nhà xã hội học Sykes và Matza, vận hành toàn diện trong tâm trí hung thủ.* | — | — |  |
| 3-22 | `3.05#2` (7,8 s) | C | T1 | `t16_a3_c06_helen_bedridden_medicine_bottles`, `pan` | *Kỹ thuật trung hòa đạo đức là quá trình tâm lý mà ở đó kẻ phạm tội tự lừa dối bản thân để vô hiệu hóa sự cắn rứt của lương tri trước khi gây án.* | — | — |  |
| 3-23 | `3.05#3` (7,6 s) | C | T1 | `t16_a3_c06_helen_bedridden_medicine_bottles`, `pull` | *John List đã tự thuyết phục mình rằng nếu gia đình rơi vào cảnh bần cùng, các con sẽ mất đi đức tin và linh hồn của họ sẽ bị đày xuống Hỏa ngục.* | — | — |  |
| 3-24 | `3.05#4` (8,6 s) | C | T1 | `t16_a3_c06_helen_bedridden_medicine_bottles`, `still` | *Hắn nại ra một lý lẽ ngụy biện ghê rợn: tước đoạt mạng sống của người thân trong lúc họ còn thuần khiết chính là hành động bác ái cao nhất để đưa họ thẳng lên Thiên đàng.* | — | — |  |
| 3-25 | `3.05#5` (9,9 s) | C | T1 | `t16_a3_c07_moral_disengagement_scales_sin`, `push` | *Đồng thời, hắn vận dụng kỹ thuật đổ lỗi cho nạn nhân và ngoại hóa trách nhiệm, cho rằng hoàn cảnh xã hội suy đồi và căn bệnh của vợ đã ép hắn vào thế không còn lựa chọn nào khác.* | — | — |  |
| 3-26 | `3.05#6` (3,9 s) | C | T1 | `t16_a3_c07_moral_disengagement_scales_sin`, `pan` | *Nhưng tại sao List không tự kết liễu đời mình để cùng gia đình lên cõi vĩnh hằng?* | — | — |  |
| 3-27 | `3.05#7` (9,1 s) | C | T1 | `t16_a3_c07_moral_disengagement_scales_sin`, `pull` | *Câu trả lời bóc trần sự ích kỷ trơ tráo của bản ngã hung thủ: hắn tự biện minh rằng tự tước đoạt sinh mạng của chính mình là trọng tội không thể tha thứ theo giáo lý tôn giáo.* | — | — |  |
| 3-28 | `3.05#8` (8,0 s) | C | T1 | `t16_a3_c07_moral_disengagement_scales_sin`, `still` | *Hắn phải sống sót để tiếp tục làm việc, xưng tội trước lúc lâm chung, với ảo tưởng rằng sau này vẫn sẽ được đoàn tụ cùng những người thân yêu trên Thiên quốc.* | — | — |  |
| 3-29 | `3.05#9` (9,7 s) | C | T1 | `t16_a3_c08_selfish_preservation_masked_piety`, `push` | *Một câu hỏi lớn luôn khiến công chúng đau đáu: Tại sao một người sùng đạo như John List lại không bao giờ biểu lộ một tia ân hận thực sự sau khi tước đoạt sinh mạng của cả gia đình?* | — | — |  |
| 3-30 | `3.05#10` (8,1 s) | C | T1 | `t16_a3_c08_selfish_preservation_masked_piety`, `pan` | *Câu trả lời nằm ở sự khiếm khuyết hoàn toàn về năng lực thấu cảm cảm xúc, kết hợp cùng kỹ thuật trung hòa đạo đức mang tên “Kêu gọi lòng trung thành cao hơn”.* | — | — |  |
| 3-31 | `3.05#11` (13,2 s) | C | T1 | `t16_cognitive_compartmentalization_cabinet`, `pull` | *Bức thư dài năm trang gửi vị mục sư không phải là sự ăn năn, mà là một bản giao dịch tâm lý đầy toan tính: hắn tự thuyết phục mình rằng việc tiễn đưa người thân khi họ còn giữ được đức tin là hành động bác ái để bảo đảm linh hồn họ bước vào Thiên đàng.* | — | — |  |
| 3-32 | `3.05#12` (12,8 s) | C | T1 | `t16_cognitive_compartmentalization_cabinet`, `still` | *Đối với bản ngã ái kỷ bệnh lý, thừa nhận tội lỗi đồng nghĩa với việc chiếc mặt nạ hoàn hảo bị phá hủy hoàn toàn; do đó, tâm trí hắn lựa chọn bám víu vào sự tự huyễn hoặc tôn giáo để vĩnh viễn trốn chạy trách nhiệm lương tâm.* | — | — |  |
| 3-33 | `3.06#1` (8,3 s) | H | T1 | `t16_cognitive_compartmentalization_cabinet`, `push` | *Logic méo mó ấy đã biến một tội ác tàn độc thành một sứ mệnh thiêng liêng mà List tin rằng mình có nghĩa vụ phải hoàn thành.* | — | — |  |
| 3-34 | `3.06#2` (7,2 s) | H | T1 | `t16_a3_c09_cognitive_compartmentalization_cabinet`, `pan` | *Nhưng điều khiến các nhà điều tra kinh ngạc hơn cả chính là khả năng thích nghi và sinh tồn của hung thủ sau khi gây án.* | — | — |  |
| 3-35 | `3.06#3` (7,6 s) | H | T1 | `t16_a3_c09_cognitive_compartmentalization_cabinet`, `pull` | *Trong suốt mười tám năm lẩn trốn, hắn đã vận dụng một cơ chế tâm lý phòng vệ đáng sợ mang tên Sự chia ngăn nhận thức.* | — | — |  |
| 3-36 | `3.06#4` (7,2 s) | H | T1 | `t16_a3_c09_cognitive_compartmentalization_cabinet`, `still` | *Cơ chế này cho phép một con người có thể sống cuộc đời của một công dân lương thiện ngay trên đống tro tàn của quá khứ.* | — | — |  |
| 3-37 | `3.06#5` (10,5 s) | H | T1 | `t16_a3_c10_cross_country_bus_rainy_window`, `push` | *Khi đứng trước vành móng ngựa hai mươi năm sau đó, những giọt nước mắt hiếm hoi mà John List rơi xuống hoàn toàn không dành cho năm người thân đã khuất dưới mái vòm Breeze Knoll.* | — | — |  |
| 3-38 | `3.06#6` (7,0 s) | H | T1 | `t16_a3_c10_cross_country_bus_rainy_window`, `pan` | *Đó là hiện tượng “Sự sụp đổ cái tôi ái kỷ” và “Tự thương hại bệnh lý” kinh điển trong tội phạm học.* | — | — |  |
| 3-39 | `3.06#7` (11,7 s) | H | T1 | `t16_a3_c10_cross_country_bus_rainy_window`, `pull` | *Hắn chỉ khóc cho chính mình: khóc vì danh dự bị vùi dập, khóc vì sự tự do bị tước đoạt, và tiếc nuối cho cuộc đời giả tạo dưới cái tên Robert Clark vừa tan thành mây khói.* | — | — |  |
| 3-40 | `3.06#8` (10,8 s) | H | T1 | `t16_a3_c11_denver_church_choir_hymn_books`, `still` | *Đến tận những ngày cuối đời sau song sắt, hắn vẫn trơ trẽn khẳng định mình là một người cha yêu thương con cái, phơi bày một linh hồn lạnh lẽo không bao giờ có thể cứu rỗi.* | — | — |  |
| 3-41 | `3.07#1` (7,1 s) | C | T1 | `t16_a3_c11_denver_church_choir_hymn_books`, `push` | *Chia ngăn nhận thức là khả năng của bộ não trong việc cô lập hoàn toàn các mảng ký ức và cảm xúc xung đột vào những ngăn chứa độc lập không giao thoa.* | — | — |  |
| 3-42 | `3.07#2` (7,1 s) | C | T1 | `t16_a3_c11_denver_church_choir_hymn_books`, `pan` | *Sau khi khóa cửa rời khỏi New Jersey, John List dường như đã khóa kín chiếc ngăn kéo chứa đựng năm mạng người ở Westfield vào vùng quên lãng.* | — | — |  |
| 3-43 | `3.07#3` (8,2 s) | C | T1 | `t16_a3_c11_denver_church_choir_hymn_books`, `pull` | *Tại tiểu bang Colorado và sau đó là Virginia, hắn tái lập một cuộc đời mới dưới cái tên Robert Clark với trật tự hoàn hảo đến mức khó tin.* | — | — |  |
| 3-44 | `3.07#4` (7,6 s) | C | T1 | `t16_suburban_church_pew_hymnal_solitude`, `still` | *Hắn lại làm kế toán viên cho các công ty uy tín, tham gia hội đồng cờ vua và trở thành một thành viên tích cực tại một nhà thờ Luther địa phương.* | — | — |  |
| 3-45 | `3.07#5` (8,9 s) | C | T1 | `t16_suburban_church_pew_hymnal_solitude`, `push` | *Năm 1985, hắn kết hôn với một người phụ nữ góa bụa tên là Delores Miller, người hoàn toàn không hay biết về quá khứ đen tối của chồng mình.* | — | — |  |
| 3-46 | `3.07#6` (7,0 s) | C | T1 | `t16_suburban_church_pew_hymnal_solitude`, `pan` | *Suốt gần hai thập kỷ, List ngủ ngon giấc mỗi đêm, không gặp ác mộng và sinh hoạt như một quý ông mẫu mực bên cạnh người vợ mới.* | — | — |  |
| 3-47 | `3.07#7` (7,4 s) | C | T1 | `t16_a3_c12_suburban_denver_modest_house`, `pull` | *Sự bình thản phi thường ấy không phải là dấu hiệu của sự bình phục, mà là biểu hiện của khuyết tật thấu cảm và sự phân mảnh tâm trí tột độ.* | — | — |  |
| 3-48 | `3.07#8` (7,6 s) | C | T1 | `t16_a3_c12_suburban_denver_modest_house`, `still` | *Gia đình mới đối với hắn chỉ là một “Lá chắn bình thường hóa” để bảo vệ chiếc mặt nạ danh dự mà bản ngã OCPD luôn khát khao duy trì.* | — | — |  |
| 3-49 | `3.08#1` (8,2 s) | H | T1 | `t16_a3_c12_suburban_denver_modest_house`, `push` | *Hung thủ tự tin rằng ngăn kéo quá khứ đã được khóa kín vĩnh viễn và chiếc mặt nạ Robert Clark sẽ bảo vệ hắn đến cuối đời.* | — | — |  |
| 3-50 | `3.08#2` (8,2 s) | H | T1 | `t16_a3_c13_hand_of_justice_approaching_clock`, `pan` | *Hắn không thể ngờ rằng, chiếc mỏ neo kéo hắn trở lại với công lý lại chính là những thói quen hành vi bất biến của chính mình.* | — | — |  |
| 3-51 | `3.08#3` (10,9 s) | H | T1 | `t16_a3_c13_hand_of_justice_approaching_clock`, `pull` | *Năm 1989, bức màn dối trá kéo dài mười tám năm chính thức bị xé toạc trước ánh sáng của khoa học hành vi và truyền thông đại chúng.* | — | — |  |
| 3-52 | `3.08#4` (8,8 s) | H | T1 | `t16_a3_c13_hand_of_justice_approaching_clock`, `still` | *Một cuộc phối hợp chưa từng có tiền lệ giữa một nhà điêu khắc thiên tài và một chương trình truyền hình đã làm thay đổi hoàn toàn cục diện vụ án.* | — | — |  |
| 3-53 | `3.08#5` (3,6 s) | H | T1 | `t16_a3_c13_hand_of_justice_approaching_clock`, `push` | *Giờ phút đền tội của bóng ma Breeze Knoll cuối cùng đã điểm.* | — | — |  |
| 3-54 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 04* · **BỨC TƯỢNG SÁP CỦA FRANK BENDER VÀ CÚ ĐIỆN THOẠI TỪ AMERICA'S MOST WANTED** | — | ⊘ | ◼ |

### HỒI 4

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (12,0 s) | H | T1 | `t16_a4_c01_yellowed_mugshot_challenge`, `pan` | *Bước ngoặt lịch sử mở ra vào đầu năm 1989, khi nhà sản xuất chương trình truyền hình nổi tiếng America’s Most Wanted quyết định lật lại hồ sơ vụ án John List.* | — | — |  |
| 4-02 | `4.02#2` (7,6 s) | H | T1 | `t16_a4_c01_yellowed_mugshot_challenge`, `pull` | *Thách thức lớn nhất đối với ban biên tập chương trình là họ không có bất kỳ tấm ảnh chân dung nào của List trong suốt mười tám năm qua.* | — | — |  |
| 4-03 | `4.02#3` (8,0 s) | H | T1 | `t16_a4_c01_yellowed_mugshot_challenge`, `still` | *Tấm ảnh duy nhất mà cảnh sát sở hữu là hình chụp từ trước năm 1971, khi đối tượng mới ngoài bốn mươi tuổi.* | — | — |  |
| 4-04 | `4.02#4` (10,6 s) | H | T1 | `t16_a4_c02_frank_bender_sculpting_studio`, `push` | *Để tái hiện diện mạo của nghi phạm ở tuổi sáu mươi ba, chương trình đã tìm đến Frank Bender, một nhà điêu khắc pháp y tài hoa tại thành phố Philadelphia.* | — | — |  |
| 4-05 | `4.02#5` (9,1 s) | H | T1 | `t16_a4_c02_frank_bender_sculpting_studio`, `pan` | *Frank Bender đã bắt tay với Richard Walter, một chuyên gia phân tích tâm lý tội phạm hàng đầu thuộc Hiệp hội Pháp y Vidocq Society.* | — | — |  |
| 4-06 | `4.02#6` (9,0 s) | H | T1 | `t16_a4_c02_frank_bender_sculpting_studio`, `pull` | *Sự kết hợp giữa trực giác nghệ thuật sắc bén và những hiểu biết sâu sắc về tâm thần học đã tạo nên một kỳ tích chưa từng thấy trong lịch sử phá án.* | — | — |  |
| 4-07 | `4.02#7` (8,0 s) | H | T1 | `t16_a4_c02_frank_bender_sculpting_studio`, `still` | *Họ bắt đầu phác thảo chân dung không chỉ dựa trên cấu trúc xương mặt, mà dựa trên chính tính cách và lối sống bảo thủ của nghi phạm.* | — | — |  |
| 4-08 | `4.04#1` (9,6 s) | H | T1 | `t16_frank_bender_sculpting_clay_tools`, `push` | *Dựa trên nghiên cứu về Rối loạn nhân cách ám ảnh cưỡng chế, hai chuyên gia đã dự đoán chuẩn xác những biến đổi sinh học và phong cách cá nhân của John List.* | — | — |  |
| 4-09 | `4.04#2` (10,1 s) | H | T1 | `t16_frank_bender_sculpting_clay_tools`, `pan` | *Walter nhận định rằng một người kế toán cứng nhắc sẽ không bao giờ phẫu thuật thẩm mỹ, mà sẽ tiếp tục duy trì kiểu tóc rẽ ngôi cổ điển và vẻ ngoài chỉn chu.* | — | — |  |
| 4-10 | `4.04#3` (9,5 s) | H | T1 | `t16_frank_bender_sculpting_clay_tools`, `pull` | *Frank Bender đã tỉ mỉ nặn từng nếp nhăn do thời gian, vùng da má chảy xệ và mái tóc thưa dần theo độ tuổi trên khối đất sét chuyên dụng.* | — | — |  |
| 4-11 | `4.04#4` (9,8 s) | H | T1 | `t16_a4_c03_richard_walter_profiler_notes`, `still` | *Điểm nhấn mang tính thiên tài của bức tượng chính là việc Bender quyết định chọn một cặp kính gọng sừng màu nâu cổ điển, dày cộp từ một cửa hàng đồ cũ.* | — | — |  |
| 4-12 | `4.04#5` (8,4 s) | H | T1 | `t16_a4_c03_richard_walter_profiler_notes`, `push` | *Ông tin rằng một người đàn ông bảo thủ sẽ luôn gắn bó với phong cách thị giác đã gắn liền với sự thành đạt trong quá khứ của mình.* | — | — |  |
| 4-13 | `4.04#6` (7,8 s) | H | T1 | `t16_a4_c03_richard_walter_profiler_notes`, `pan` | *Bức tượng bán thân hoàn thành toát lên một ánh nhìn lạnh lùng, xa cách và đầy vẻ nghiêm cẩn của một kẻ cuồng trật tự.* | — | — |  |
| 4-14 | `4.06#1` (11,8 s) | D | T1 | `t16_a4_c04_clay_bust_aging_features_glasses`, `pull` | *Ngày 21 tháng 5 năm 1989, tập phát sóng đặc biệt về hồ sơ John List chính thức lên sóng truyền hình toàn quốc trước sự theo dõi của ước tính hai mươi hai triệu khán giả Mỹ.* | — | — |  |
| 4-15 | `4.06#2` (8,3 s) | D | T1 | `t16_a4_c04_clay_bust_aging_features_glasses`, `still` | *Hình ảnh bức tượng đất sét của Frank Bender với cặp kính gọng sừng đặc trưng được phóng lớn trên màn ảnh cùng lời kêu gọi cung cấp thông tin khẩn cấp.* | — | — |  |
| 4-16 | `4.06#3` (8,3 s) | D | T1 | `t16_a4_c04_clay_bust_aging_features_glasses`, `push` | *Chỉ trong vòng vài giờ sau khi chương trình kết thúc, tổng đài đường dây nóng của America’s Most Wanted đã nhận được hàng trăm cuộc gọi từ khắp nơi trên cả nước.* | — | — |  |
| 4-17 | `4.06#4` (7,6 s) | D | T1 | `t16_a4_c04_clay_bust_aging_features_glasses`, `pan` | *Tuy nhiên, một cuộc điện thoại đặc biệt đến từ thành phố Denver thuộc bang Colorado đã thu hút sự chú ý tối cao của các điều tra viên.* | — | — |  |
| 4-18 | `4.06#5` (5,6 s) | D | T1 | `t16_a4_c05_americas_most_wanted_broadcast_screen`, `pull` | *Một người phụ nữ tên là Wanda Flannery đã gọi điện với giọng nói run rẩy vì kinh ngạc tột độ.* | — | — |  |
| 4-19 | `4.06#6` (9,6 s) | D | T1 | `t16_a4_c05_americas_most_wanted_broadcast_screen`, `still` | *Bà khẳng định rằng bức tượng bán thân trên truyền hình giống hệt một người hàng xóm cũ từng sống cạnh nhà bà nhiều năm trước, một người đàn ông tên là Robert Clark.* | — | — |  |
| 4-20 | `4.06#7` (7,4 s) | D | T1 | `t16_a4_c05_americas_most_wanted_broadcast_screen`, `push` | *Theo lời bà Flannery, người đàn ông này cũng là một kế toán viên sùng đạo và hiện đã cùng vợ chuyển đến sinh sống tại bang Virginia.* | — | — |  |
| 4-21 | `4.08#1` (9,2 s) | H | T1 | `t16_vintage_crt_television_broadcast_amw`, `pan` | *Nhận được thông tin tình báo vô giá từ cuộc gọi của người hàng xóm, Cục Điều tra Liên bang FBI lập tức mở cuộc xác minh tại bang Virginia.* | — | — |  |
| 4-22 | `4.08#2` (6,9 s) | H | T1 | `t16_vintage_crt_television_broadcast_amw`, `pull` | *Các đặc vụ nhanh chóng xác định được Robert Clark đang làm kế toán cho một công ty kế toán nhỏ tại thành phố Richmond.* | — | — |  |
| 4-23 | `4.08#3` (10,8 s) | H | T1 | `t16_vintage_crt_television_broadcast_amw`, `still` | *Ngày 1 tháng 6 năm 1989, chỉ mười một ngày sau buổi phát sóng định mệnh, các đặc vụ FBI đã ập vào văn phòng làm việc của Clark.* | — | — |  |
| 4-24 | `4.08#4` (10,6 s) | H | T1 | `t16_vintage_crt_television_broadcast_amw`, `push` | *Đối diện với lực lượng thực thi pháp luật là một người đàn ông lớn tuổi đang đeo đúng cặp kính gọng sừng cổ điển, toát lên diện mạo giống bức tượng của Frank Bender đến kinh ngạc.* | — | — |  |
| 4-25 | `4.08#5` (8,8 s) | H | T1 | `t16_a4_c06_wanda_flannery_watching_tv_shock`, `pan` | *Người đàn ông này vẫn giữ thái độ điềm tĩnh lạ lùng, kiên quyết phủ nhận cái tên John List và khăng khăng khẳng định mình là Robert Clark.* | — | — |  |
| 4-26 | `4.09#1` (6,6 s) | N2 | T4 | `t16_a4_c06_wanda_flannery_watching_tv_shock`, `pull` | *Hãy hình dung cú sốc tâm lý khủng khiếp của tôi khi ngồi trước màn hình tivi vào đêm chủ nhật hôm ấy.* | — | ✦ Mèo |  |
| 4-27 | `4.09#2` (10,5 s) | N2 | T4 | `t16_a4_c06_wanda_flannery_watching_tv_shock`, `still` | *Khi bức tượng của Frank Bender xuất hiện trên màn ảnh, tôi cảm thấy rợn tóc gáy vì nó giống người hàng xóm Bob Clark của chúng tôi đến từng đường nét.* | — | — |  |
| 4-28 | `4.09#3` (12,9 s) | N2 | T4 | `t16_colorado_neighbor_whispering_telephone`, `push` | *Suốt nhiều năm sống cạnh nhà nhau ở Denver, trong mắt tất cả mọi người, Bob luôn là một người đàn ông lịch thiệp, ít nói, chăm chỉ cắt cỏ và không bao giờ bỏ lỡ một buổi lễ nhà thờ nào.* | — | — |  |
| 4-29 | `4.09#4` (8,4 s) | N2 | T4 | `t16_colorado_neighbor_whispering_telephone`, `pan` | *Người vợ Delores của ông ta là một phụ nữ hiền lành, yêu thương chồng hết mực và hoàn toàn tin tưởng vào vẻ đạo mạo của ông.* | — | — |  |
| 4-30 | `4.09#5` (11,2 s) | N2 | T4 | `t16_colorado_neighbor_whispering_telephone`, `pull` | *Thậm chí trước đó, tôi từng tình cờ đọc được một bài báo cũ về vụ án New Jersey và nửa đùa nửa thật nói với Delores rằng Bob trông giống John List đến kỳ lạ.* | — | — |  |
| 4-31 | `4.09#6` (10,4 s) | N2 | T4 | `t16_colorado_neighbor_whispering_telephone`, `still` | *Nhưng lúc ấy Delores đã cười xòa gạt đi, bởi không một ai có thể tưởng tượng người đàn ông nhã nhặn ấy lại là một kẻ thủ ác bị truy nã gắt gao nhất nước Mỹ.* | — | — |  |
| 4-32 | `4.09#7` (7,6 s) | N2 | T4 | `t16_a4_c07_suburban_richmond_quiet_culdesac`, `push` | *Khoảnh khắc nhìn thấy bức tượng trên truyền hình, trực giác mách bảo tôi rằng đây không thể là một sự trùng hợp ngẫu nhiên.* | — | — |  |
| 4-33 | `4.09#8` (10,0 s) | N2 | T4 | `t16_a4_c07_suburban_richmond_quiet_culdesac`, `pan` | *Tôi hiểu rằng mình phải nhấc máy gọi ngay cho đường dây nóng, bởi nếu im lặng, tôi sẽ đồng lõa với một bóng ma tội ác đang ẩn mình giữa những người vô tội.* | — | — |  |
| 4-34 | `4.09#9` (8,8 s) | N2 | T4 | `t16_a4_c07_suburban_richmond_quiet_culdesac`, `pull` | *Sự thật sau đó đã chứng minh rằng cái ác tinh vi nhất luôn biết cách khoác lên mình chiếc áo choàng của sự bình thường và tử tế.* | — | — |  |
| 4-35 | `4.09#10` (9,0 s) | N2 | T4 | `t16_a4_c08_newspaper_clipping_glance_suspicion`, `still` | *Thú thật rằng suốt nhiều năm trước đó, tôi đã liên tục dập tắt những mối nghi ngờ le lói trong lòng mình vì sợ bị coi là kẻ hoang tưởng tọc mạch.* | — | — |  |
| 4-36 | `4.09#11` (16,8 s) | N2 | T4 | `t16_a4_c08_newspaper_clipping_glance_suspicion`, `push` | *Khi tình cờ đọc được bài báo cũ và nhận thấy vẻ ngoài của Bob Clark giống hệt kẻ đào tẩu John List, tôi đã nửa đùa nửa thật chia sẻ với Delores, nhưng rồi cả hai chúng tôi đều cười xòa bỏ qua vì không muốn phá vỡ cuộc sống bình yên của nhau.* | — | — |  |
| 4-37 | `4.09#12` (10,3 s) | N2 | T4 | `t16_a4_c08_newspaper_clipping_glance_suspicion`, `pan` | *Thế nhưng đêm chủ nhật hôm ấy, khi bức tượng đất sét của Frank Bender xuất hiện trên màn hình truyền hình trước hai mươi hai triệu người, một luồng điện lạnh buốt chạy dọc sống lưng tôi.* | — | — |  |
| 4-38 | `4.09#13` (8,4 s) | N2 | T4 | `t16_a4_c09_telephone_call_hotline_tip`, `pull` | *Tôi nhận ra rằng sự do dự lúc này không còn là sự lịch thiệp, mà là sự đồng lõa hèn nhát với tội ác đang lẩn trốn.* | — | — |  |
| 4-39 | `4.09#14` (10,1 s) | N2 | T4 | `t16_a4_c09_telephone_call_hotline_tip`, `still` | *Lương tâm và trách nhiệm công dân đã thôi thúc tôi nhấc máy gọi cho đường dây nóng, bởi vì một xã hội im lặng trước cái ác là một xã hội đang tự đầu hàng.* | — | — |  |
| 4-40 | `4.10#1` (7,2 s) | D | T1 | `t16_a4_c09_telephone_call_hotline_tip`, `push` | *Dù đối tượng kiên quyết chối bỏ thân phận thực sự suốt nhiều ngày trong phòng thẩm vấn, khoa học hình sự đã đưa ra phán quyết không thể chối cãi.* | — | — |  |
| 4-41 | `4.10#2` (10,7 s) | D | T1 | `t16_a4_c10_fbi_arrest_accounting_office`, `pan` | *Chúng tôi đã tiến hành thu thập dấu vân tay của Robert Clark và gửi đến phòng giám định sinh trắc học của FBI để đối chiếu với hồ sơ quân ngũ thời Thế chiến thứ hai của John Emil List.* | — | — |  |
| 4-42 | `4.10#3` (5,6 s) | D | T1 | `t16_a4_c10_fbi_arrest_accounting_office`, `pull` | *Kết quả đối chiếu dấu vân tay khẳng định sự trùng khớp tuyệt đối ở tất cả các điểm đặc trưng hình thái học.* | — | — |  |
| 4-43 | `4.10#4` (5,0 s) | D | T1 | `t16_a4_c10_fbi_arrest_accounting_office`, `still` | *Trước bằng chứng khoa học đanh thép, bức tường dối trá kéo dài mười tám năm hoàn toàn sụp đổ.* | — | — |  |
| 4-44 | `4.10#5` (8,8 s) | D | T1 | `t16_a4_c10_fbi_arrest_accounting_office`, `push` | *Người đàn ông mang tên Robert Clark cuối cùng đã phải cúi đầu thừa nhận mình chính là John Emil List, kẻ đào tẩu khỏi biệt thự Breeze Knoll năm xưa.* | — | — |  |
| 4-45 | `4.10#6` (6,3 s) | D | T1 | `t16_richmond_accounting_office_desk_arrest`, `pan` | *Hắn bị dẫn độ về bang New Jersey dưới sự bảo vệ nghiêm ngặt để chuẩn bị bước ra trước vành móng ngựa của công lý.* | — | — |  |
| 4-46 | `4.11#1` (7,6 s) | C | T1 | `t16_richmond_accounting_office_desk_arrest`, `pull` | *Thành công phi thường của vụ bắt giữ John List là minh chứng rực rỡ cho sức mạnh của phân tích tâm lý học hành vi kết hợp cùng nghệ thuật tạo hình pháp y.* | — | — |  |
| 4-47 | `4.11#2` (9,3 s) | C | T1 | `t16_richmond_accounting_office_desk_arrest`, `still` | *Frank Bender và Richard Walter đã chiến thắng không chỉ nhờ việc đo đạc tỷ lệ giải phẫu học xương sọ, mà nhờ việc đọc vị chuẩn xác chiếc mỏ neo tâm lý của đối tượng.* | — | — |  |
| 4-48 | `4.11#3` (5,9 s) | C | T1 | `t16_richmond_accounting_office_desk_arrest`, `push` | *Những cá nhân mang rối loạn nhân cách ám ảnh cưỡng chế như List bị cầm tù bởi chính thói quen và sự bảo thủ của mình.* | — | — |  |
| 4-49 | `4.11#4` (7,8 s) | C | T1 | `t16_a4_c11_fingerprint_card_matching_records`, `pan` | *Họ coi phong cách cá nhân là biểu tượng danh dự không thể thay thế, và chính sự bất biến ấy đã trở thành tử huyệt phơi bày thân phận của hắn trước công chúng.* | — | — |  |
| 4-50 | `4.11#5` (6,0 s) | C | T1 | `t16_a4_c11_fingerprint_card_matching_records`, `pull` | *Cặp kính gọng sừng cổ điển trên gương mặt kẻ đào tẩu chính là chiếc chìa khóa định mệnh mở toang cánh cửa dẫn hắn vào trại giam.* | — | — |  |
| 4-51 | `4.11#6` (9,0 s) | C | T1 | `t16_a4_c11_fingerprint_card_matching_records`, `still` | *Hành động dũng cảm của người hàng xóm Wanda Flannery đã kéo sập bức màn dối trá, nhưng đồng thời giáng một đòn chí mạng vào tâm trí người vợ thứ hai là Delores Miller.* | — | — |  |
| 4-52 | `4.11#7` (8,1 s) | C | T1 | `t16_john_list_a4_12_mansion`, `push` | *Delores hoàn toàn vô tội về mặt pháp lý, nhưng lại phải gánh chịu một chấn thương tâm lý tàn khốc mang tên “Sự sụp đổ bản ngã do phản bội niềm tin”.* | — | — |  |
| 4-53 | `4.11#8` (10,8 s) | C | T1 | `t16_john_list_a4_12_mansion`, `pan` | *Bà bàng hoàng nhận ra người đàn ông mà mình đầu ấp tay gối, cùng cầu nguyện và chia sẻ từng bữa ăn suốt nhiều năm qua lại chính là kẻ đã tước đoạt sinh mạng của cả mẹ ruột, vợ và ba người con.* | — | — |  |
| 4-54 | `4.11#9` (12,5 s) | C | T1 | `t16_john_list_a4_12_mansion`, `pull` | *Cảm giác ghê tởm, tội lỗi vì đã vô tình trở thành lá chắn bình thường hóa cho kẻ ác đã đẩy bà vào một cuộc khủng hoảng tinh thần sâu sắc; đó là cái giá quá đắt của sự ngây thơ khi đối diện với chiếc mặt nạ hoàn hảo của tội phạm OCPD.* | — | — |  |
| 4-55 | `4.12#1` (7,4 s) | H | T1 | `t16_a4_c12_courthouse_steps_westfield_return`, `still` | *Cuộc đào tẩu kéo dài mười tám năm, trải qua hai danh tính và hàng ngàn dặm đường cuối cùng đã đi đến hồi kết thúc.* | — | — |  |
| 4-56 | `4.12#2` (11,4 s) | H | T1 | `t16_a4_c12_courthouse_steps_westfield_return`, `push` | *Tháng 4 năm 1990, phiên tòa xét xử John Emil List chính thức diễn ra tại Tòa án Thượng thẩm Hạt Union trong sự theo dõi nghẹt thở của toàn nước Mỹ.* | — | — |  |
| 4-57 | `4.12#3` (6,6 s) | H | T1 | `t16_a4_c12_courthouse_steps_westfield_return`, `pan` | *Đã đến lúc kẻ tự phong mình là đấng cứu thế phải đối diện với phán quyết tối thượng của luật pháp con người.* | — | — |  |
| 4-58 | `4.12#4` (4,2 s) | H | T1 | `t16_a4_c12_courthouse_steps_westfield_return`, `pull` | *Một bản án công lý nghiêm khắc đang chờ đợi hắn tại chính nơi bi kịch bắt đầu.* | — | — |  |
| 4-59 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 05* · **BÀI HỌC ĐẮT GIÁ VỀ SỰ CUỒNG KIỂM SOÁT & 4 CẢNH BÁO ĐỎ** | — | ⊘ | ◼ |

### HỒI 5

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (12,7 s) | H | T1 | `t16_courtroom_gavel_mahogany_verdict`, `still` | *Ngày 12 tháng 4 năm 1990, sau những ngày tranh tụng căng thẳng, bồi thẩm đoàn đã tuyên bố John Emil List phạm đủ năm tội danh Giết người cấp độ một.* | — | — |  |
| 5-02 | `5.02#2` (12,0 s) | H | T1 | `t16_courtroom_gavel_mahogany_verdict`, `push` | *Ngày 1 tháng 5 năm 1990, Thẩm phán William Wertheimer chính thức tuyên phạt bị cáo năm bản án tù chung thân liên tiếp, mức án cao nhất theo luật pháp thời bấy giờ.* | — | — |  |
| 5-03 | `5.02#3` (9,6 s) | H | T1 | `t16_a5_c01_sentencing_five_life_terms`, `pan` | *Trong suốt phiên tòa, trước những lời khai đầy nước mắt của nhân chứng, John List vẫn ngồi bất động với gương mặt lạnh lùng, vô cảm như một pho tượng.* | — | — |  |
| 5-04 | `5.02#4` (10,7 s) | H | T1 | `t16_a5_c01_sentencing_five_life_terms`, `pull` | *Hắn nại ra chứng bệnh trầm cảm và sang chấn tâm lý để xin giảm nhẹ, nhưng tuyệt nhiên không biểu lộ một lời xin lỗi chân thành nào gửi tới hương hồn các nạn nhân.* | — | — |  |
| 5-05 | `5.02#5` (16,4 s) | H | T1 | `t16_a5_c02_unrepentant_cold_stare_defense`, `still` | *Thẩm phán William Wertheimer đã đưa ra lời tuyên án đanh thép đi vào lịch sử tư pháp: “John Emil List không hề có sự ăn năn chân chính, linh hồn của bị cáo đen tối và lạnh lẽo y như ngày 9 tháng 11 năm 1971.”* | — | — |  |
| 5-06 | `5.02#6` (15,8 s) | H | T1 | `t16_state_prison_iron_bars_solitary_cell`, `push` | *Sau phiên tòa, kẻ thủ ác còn trơ trẽn nộp đơn kháng cáo lên các cấp tòa phúc thẩm với lý do bức thư gửi mục sư là tài liệu tôn giáo bí mật không được phép dùng làm bằng chứng, bộc lộ sự tự thương hại bản thân bệnh lý đến phút chót.* | — | — |  |
| 5-07 | `5.03#1` (6,9 s) | D | T1 | `t16_state_prison_iron_bars_solitary_cell`, `pan` | *John List đã trải qua phần đời còn lại trong sự cô độc tuyệt đối tại trại giam bang New Jersey ở thành phố Trenton.* | — | — |  |
| 5-08 | `5.03#2` (12,4 s) | D | T1 | `t16_a5_c03_trenton_prison_cemetery_tombstone`, `pull` | *Ngày 21 tháng 3 năm 2008, hắn trút hơi thở cuối cùng ở tuổi tám mươi hai do biến chứng viêm phổi nặng, khép lại ba mươi bảy năm của một trong những hồ sơ đen tối nhất lịch sử tội phạm học.* | — | — |  |
| 5-09 | `5.03#3` (8,6 s) | D | T1 | `t16_a5_c03_trenton_prison_cemetery_tombstone`, `still` | *Đối với lực lượng thực thi pháp luật, hồ sơ John List là một bài học mẫu mực về sự kiên trì theo đuổi công lý bất chấp khoảng cách thời gian và không gian.* | — | — |  |
| 5-10 | `5.03#4` (9,7 s) | D | T1 | `t16_a5_c04_tyrannical_family_patriarch_throne`, `push` | *Vụ án đã mở ra một kỷ nguyên mới cho ngành khoa học hình sự, khẳng định vai trò sống còn của kỹ thuật phục dựng diện mạo theo độ tuổi và sự hợp tác của cộng đồng quần chúng.* | — | — |  |
| 5-11 | `5.03#5` (7,6 s) | D | T1 | `t16_a5_c04_tyrannical_family_patriarch_throne`, `pan` | *Nó chứng minh rằng không một bức tường dối trá nào có thể tồn tại vĩnh viễn trước ánh sáng của sự thật và khoa học pháp y hiện đại.* | — | — |  |
| 5-12 | `5.03#6` (7,5 s) | D | T1 | `t16_a5_c04_tyrannical_family_patriarch_throne`, `pull` | *Vụ án John List khép lại nhưng để lại lời cảnh tỉnh trường tồn cho công tác điều tra hình sự và an ninh gia đình hiện đại.* | — | — |  |
| 5-13 | `5.03#7` (10,0 s) | D | T1 | `t16_a5_c05_accepting_vulnerability_open_hands`, `still` | *Không một chiếc mặt nạ đạo mạo, không một địa vị xã hội danh giá nào có thể là bảo chứng tuyệt đối cho sự an toàn nếu thiếu vắng sự nhạy cảm và trách nhiệm can thiệp của những người xung quanh.* | — | — |  |
| 5-14 | `5.03#8` (11,1 s) | D | T1 | `t16_a5_c05_accepting_vulnerability_open_hands`, `push` | *Sự an bình thực sự của một cộng đồng không được xây nên từ những cánh cổng đóng kín hay sự giữ kẽ vô cảm, mà phải được gìn giữ bằng lòng dũng cảm bảo vệ những sinh mệnh dễ bị tổn thương nhất.* | — | — |  |
| 5-15 | `5.03#9` (7,7 s) | D | T1 | `t16_four_redflags_overview_banner`, `pan` | *Đó là di sản nhân văn đắt giá nhất được đánh đổi bằng nỗi đau và nước mắt của năm sinh mạng vô tội tại dinh thự Breeze Knoll.* | — | — |  |
| 5-16 | `5.04#1` (9,0 s) | C | T1 | `t16_four_redflags_overview_banner`, `pull` | *Nhìn lại toàn bộ thảm kịch Breeze Knoll dưới lăng kính tâm lý học, chúng ta nhận ra sự nguy hiểm tột cùng của chủ nghĩa hoàn hảo cực đoan khi kết hợp với bản ngã gia trưởng độc đoán.* | — | — |  |
| 5-17 | `5.04#2` (6,2 s) | C | T1 | `t16_a5_c08_transparency_and_shared_honesty`, `still` | *John List đã biến gia đình mình thành một vật phẩm sở hữu để phục vụ cho chiếc mặt nạ danh dự ái kỷ của bản thân.* | — | — |  |
| 5-18 | `5.04#3` (7,7 s) | C | T1 | `t16_a5_c08_transparency_and_shared_honesty`, `push` | *Khi không thể duy trì quyền kiểm soát thực tại, hắn đã chọn cách hủy diệt sinh mệnh của người khác dưới chiêu bài nhân danh đức tin và lòng vị tha méo mó.* | — | — |  |
| 5-19 | `5.04#4` (6,8 s) | C | T1 | `t16_redflag1_rigid_perfectionism_inflexibility`, `pan` | *Tình yêu thương gia đình chân chính luôn đòi hỏi sự thấu cảm, lòng bao dung và sự tôn trọng quyền tự do cá nhân của từng thành viên.* | — | — |  |
| 5-20 | `5.04#5` (8,0 s) | C | T1 | `t16_redflag1_rigid_perfectionism_inflexibility`, `pull` | *Sự trưởng thành thực sự của một con người nằm ở việc dũng cảm thừa nhận thất bại, hạ thấp cái tôi và tìm kiếm sự giúp đỡ khi rơi vào nghịch cảnh cuộc sống.* | — | — |  |
| 5-21 | `5.04#6` (7,3 s) | C | T1 | `t16_redflag3_financial_status_concealment`, `still` | *Tôn giáo và đạo đức không bao giờ là tấm bình phong để biện minh cho sự ích kỷ, sự hèn nhát và hành vi tước đoạt mạng sống của đồng loại.* | — | — |  |
| 5-22 | `5.04#7` (10,4 s) | C | T1 | `t16_redflag3_financial_status_concealment`, `push` | *Nhìn lại thảm kịch Breeze Knoll sau hơn nửa thế kỷ, vết thương dai dẳng nhất không chỉ thuộc về các phòng xử án, mà nằm trong tâm trí của những người từng có cơ hội ngăn chặn cái ác nhưng đã bỏ lỡ.* | — | — |  |
| 5-23 | `5.04#8` (7,6 s) | C | T1 | `t16_redflag2_higher_purpose_neutralization`, `pan` | *Hiện tượng “Chấn thương Đạo đức của Nhân chứng” thể hiện rõ nét qua nỗi day dứt suốt đời của cô giáo Jean Phillips và những người từng tiếp xúc với gia đình List.* | — | — |  |
| 5-24 | `5.04#9` (10,0 s) | C | T1 | `t16_redflag2_higher_purpose_neutralization`, `pull` | *Sự im lặng của xã hội thường không bắt nguồn từ sự tàn nhẫn, mà sinh ra từ nỗi e ngại bị phán xét, sự sợ hãi va chạm và thói quen xem nhẹ linh cảm bất an của những người yếu thế.* | — | — |  |
| 5-25 | `5.04#10` (11,4 s) | C | T1 | `t16_a5_c10_healthy_faith_shield_comfort`, `still` | *Khi một đứa trẻ cất tiếng kêu cứu về sự ngột ngạt trong chính ngôi nhà của mình, đó không bao giờ là câu chuyện riêng tư cần giữ kín, mà là một mệnh lệnh khẩn cấp đòi hỏi cộng đồng phải dũng cảm phá vỡ sự im lặng để hành động.* | — | — |  |
| 5-26 | `5.05#1` (12,4 s) | H | T1 | `t16_a5_c10_healthy_faith_shield_comfort`, `push` | *Thưa quý vị, hồ sơ John List không chỉ là một câu chuyện phá án kinh điển, mà còn để lại những bài học thức tỉnh sâu sắc về việc nhận diện những nguy cơ tiềm ẩn trong các mối quan hệ gia đình.* | — | — |  |
| 5-27 | `5.05#2` (14,6 s) | H | T1 | `t16_redflag4_total_family_isolation`, `pan` | *Dựa trên nguyên lý tâm lý học hành vi và cuốn cẩm nang sinh tồn The Gift of Fear, kênh Amber Eyes xin đúc kết bốn dấu hiệu cảnh báo đỏ để mỗi chúng ta nhận diện và tự bảo vệ mình trước những kẻ cuồng kiểm soát độc hại.* | — | — |  |
| 5-28 | `5.05#3` (7,3 s) | H | T8 cờ | `t16_a5_c06_redflag1_rigid_perfectionism_barracks`, `pull` | *01* · **Dấu hiệu thứ nhất: Chủ nghĩa hoàn hảo cứng nhắc và nhu cầu kiểm soát tuyệt đối mọi khía cạnh cuộc sống của người thân.** | — | ⊘ |  |
| 5-29 | `5.05#4` (10,9 s) | H | T1 | `t16_a5_c06_redflag1_rigid_perfectionism_barracks`, `still` | *Những người này không chấp nhận bất kỳ sự khác biệt nào về sở thích, suy nghĩ hay cá tính của con cái, coi đó là sự nổi loạn chống đối cần phải bị trừng phạt nghiêm khắc.* | — | — |  |
| 5-30 | `5.05#5` (8,4 s) | H | T1 | `t16_redflag4_total_family_isolation`, `push` | *Họ biến ngôi nhà thành một trại lính của những giáo điều xơ cứng, bóp nghẹt quyền tự do và sự phát triển tự nhiên của những người xung quanh.* | — | — |  |
| 5-31 | `5.05#6` (7,3 s) | H | T8 cờ | `t16_a5_c07_redflag2_financial_deceit_vault`, `pan` | *02* · **Dấu hiệu thứ hai: Che giấu khủng hoảng tài chính bằng mọi giá vì nỗi sợ sụp đổ thể diện xã hội.** | — | ⊘ |  |
| 5-32 | `5.05#7` (10,4 s) | H | T1 | `t16_a5_c07_redflag2_financial_deceit_vault`, `pull` | *Một cá nhân từ chối sự minh bạch về kinh tế, âm thầm chiếm đoạt tài sản của người thân và cố duy trì vỏ bọc giàu sang giả tạo chính là một quả bom nổ chậm nguy hiểm.* | — | — |  |
| 5-33 | `5.05#8` (9,3 s) | H | T1 | `t16_vigilance_and_compassion_porch_lantern`, `still` | *Sự minh bạch, sẻ chia và cùng nhau gánh vác khó khăn mới là nền tảng sống còn để bảo vệ sự an toàn và hạnh phúc của một gia đình.* | — | — |  |
| 5-34 | `5.05#9` (9,0 s) | H | T8 cờ | `t16_a5_c09_redflag3_religious_weaponization_altar`, `push` | *03* · **Dấu hiệu thứ ba: Vận dụng giáo lý tôn giáo và chiêu bài nhân danh mục đích cao cả để thao túng tâm lý và ngụy biện cho sự độc tài.** | — | ⊘ |  |
| 5-35 | `5.05#10` (11,0 s) | H | T1 | `t16_a5_c09_redflag3_religious_weaponization_altar`, `pan` | *Kẻ độc hại thường tự phong mình làm quan tòa đạo đức, sử dụng nỗi sợ hãi siêu hình để cô lập người thân khỏi thế giới bên ngoài và bắt họ phải phục tùng tuyệt đối.* | — | — |  |
| 5-36 | `5.05#11` (8,9 s) | H | T1 | `t16_vigilance_and_compassion_porch_lantern`, `pull` | *Hãy luôn tỉnh táo nhận diện rằng tình yêu đích thực không bao giờ đi kèm với sự đe dọa, sự áp đặt tinh thần và sự bạo hành nhận thức.* | — | — |  |
| 5-37 | `5.05#12` (7,9 s) | H | T8 cờ | `t16_a5_c11_redflag4_toxic_isolation_locked_gate`, `still` | *04* · **Dấu hiệu thứ tư: Xu hướng tự cô lập xã hội và phớt lờ những trực giác cảnh báo bất an từ những người xung quanh.** | — | ⊘ |  |
| 5-38 | `5.05#13` (11,4 s) | H | T1 | `t16_a5_c11_redflag4_toxic_isolation_locked_gate`, `push` | *Tiếng kêu cứu nghẹn ngào của cô bé Patricia List trước khi bi kịch xảy ra là một bài học đắt giá về việc xã hội không được phép xem nhẹ linh cảm bất an của trẻ nhỏ.* | — | — |  |
| 5-39 | `5.05#14` (11,5 s) | H | T1 | `t16_a5_c12_listening_to_the_cries_helping_hand`, `pan` | *Khi nhận thấy một người thân quen đột ngột cắt đứt liên lạc, khép kín cực đoan và có những lời cảnh báo rùng mình, cộng đồng và nhà trường cần phải lập tức vào cuộc can thiệp kịp thời.* | — | — |  |
| 5-40 | `5.05#15` (9,1 s) | H | T1 | `t16_a5_c12_listening_to_the_cries_helping_hand`, `pull` | *Lắng nghe trực giác và dũng cảm lên tiếng tìm kiếm sự trợ giúp chính là chiếc phao cứu sinh quý giá nhất để ngăn chặn những bi kịch tàn khốc.* | — | — |  |
| 5-41 | `5.05#16` (9,6 s) | H | T1 | `t16_a5_c12_listening_to_the_cries_helping_hand`, `still` | *Sinh mạng, phẩm giá và sự tự do của mỗi con người luôn là giá trị thiêng liêng nhất cần được tôn trọng và bảo vệ trước mọi áp lực vô hình.* | — | — |  |
| 5-42 | `5.05#17` (9,6 s) | H | T1 | `t16_john_list_a5_09_mansion`, `push` | *Cảm ơn quý vị đã dành thời gian theo dõi trọn vẹn tập hồ sơ giải phẫu tâm lý tội phạm đầy xúc động và bài học nhân văn sâu sắc ngày hôm nay.* | — | — |  |
| 5-43 | `5.05#18` (10,7 s) | H | T1 | `t16_john_list_a5_09_mansion`, `pan` | *Hãy nhấn đăng ký kênh Amber Eyes, bấm chuông thông báo và chia sẻ những suy ngẫm của quý vị ở phần bình luận để lan tỏa thông điệp cảnh giác và yêu thương đích thực.* | — | — |  |
| 5-44 | hết tập (0,0 s) | — | T2 | `t16_amber_eyes_closing_dossier_list`, `still` | **HỒ SƠ TẬP 16 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | — | ⊘ | ◼ |

**Tổng:** 262 dòng · 257 câu · 5 hồi · nền dùng 94 loại (FLUX 2K Colab/Kaggle). Bỏ 31 gradient 24/10 và 22 ảnh phố Westfield lặp (H19).
