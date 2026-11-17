# HỒ SƠ SẢN XUẤT TẬP 11 · "CẶP ĐÔI KEN & BARBIE"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 11: Cặp Đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi & Thỏa Thuận Với Quỷ Dữ (Hồ Sơ Paul Bernardo & Karla Homolka)** |
| Vụ án | Paul Bernardo & Karla Homolka — Vụ án mạng Scarborough Rapist & Ken and Barbie Killers (Ontario, Canada) |
| Chủ đề | Hội chứng Điên cuồng đôi (Folie à Deux), Trung hòa đạo đức (Moral Neutralization), Mặt nạ nạn nhân (Victim Mask), Thỏa thuận với Quỷ dữ & Hệ sinh thái 10 chỉ dấu tâm lý |
| Tổng thời lượng | **2374.2 s (~39 phút 34 giây)** · 5 hồi · **272 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Người hàng xóm Port Dalhousie) · N2 (Công tố viên phụ trách vụ án) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap11.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.mp3` & `02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2365.2 s, kết thúc audio tại 2374.2 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **122.4 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.0 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **207.8 Hz**
- **Người hàng xóm ($N1$ · Cừu):** F0 trung vị = **176.7 Hz**
- **Công tố viên ($N2$ · Mèo):** F0 trung vị = **282.4 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.93\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.16\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.02%** (CER trung bình: **11.05%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.60 / 5.0** (Dải điểm: 1.65 – 3.42). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap11/xuat_ban/CanNghe_Tap11_higgs.md`](xuat_ban/CanNghe_Tap11_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.mp3`](xuat_ban/Tap11_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.wav`](xuat_ban/Tap11_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t11.json`](../../.work/timeline_s_t11.json) (2374.2 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap11/xuat_ban/Tap11.srt`](xuat_ban/Tap11.srt) (272 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep11_vi.json`](../../.work/quality_qc_utmos_ep11_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap11/xuat_ban/CanNghe_Tap11_higgs.md`](xuat_ban/CanNghe_Tap11_higgs.md)

---

## 6. DANH SÁCH SHOT — TẬP 11 (VI) — timeline 272 câu (lập lại 16/11/2026)


### HỒI 1 — VỎ BỌC HOÀN HẢO CỦA CẶP ĐÔI KEN & BARBIE

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.03#1` (13,9 s) | H | T1 | `t11_pink_house_57_bayview`, `pan` | *Vào đầu thập niên 1990, tại thị trấn ven hồ thơ mộng Port Dalhousie thuộc tỉnh Ontario, có một ngôi nhà màu hồng nổi bật tọa lạc tại số 57 Đại lộ Bayview Drive.* | — | ✦ Cú | |
| 1-02 | `1.03#2` (7,0 s) | H | T1 | `t11_pink_house_57_bayview`, `pull` | *Đó là tổ ấm của một cặp vợ chồng trẻ khiến bất kỳ ai đi qua cũng phải ngoái nhìn với ánh mắt ngưỡng mộ.* | — | — | |
| 1-03 | `1.03#3` (11,0 s) | H | T1 | `t11_suburban_admiration_facade`, `still` | *Người chồng là Paul Bernardo, một thanh niên bảnh bao làm việc trong ngành tài chính kế toán, luôn xuất hiện trong những bộ vest hàng hiệu và lái chiếc xe thể thao mui trần cá tính.* | — | — | |
| 1-04 | `1.03#4` (10,2 s) | H | T1 | `t11_paul_bernardo_dashing_car`, `push` | *Người vợ là Karla Homolka, kém hắn sáu tuổi, cô gái tóc vàng xinh đẹp với nụ cười rạng rỡ như thiên thần, đang làm việc tại một phòng khám thú y địa phương.* | — | — | |
| 1-05 | `1.03#5` (7,8 s) | H | T1 | `t11_karla_veterinary_clinic`, `pan` | *Trong mắt cộng đồng dân cư xung quanh, họ chính là hiện thân hoàn mỹ của cặp búp bê “Ken và Barbie” bước ra đời thực.* | — | — | |
| 1-06 | `1.03#6` (12,3 s) | H | T1 | `t11_ken_barbie_golden_illusion`, `pull` | *Họ tổ chức một đám cưới lộng lẫy như truyện cổ tích vào tháng 6 năm 1991 bằng cỗ xe ngựa kéo tại thị trấn cổ kính Niagara-on-the-Lake.* | — | — | |
| 1-07 | `1.05#1` (7,2 s) | H | T1 | `t11_fairytale_wedding_carriage`, `still` | *Đôi vợ chồng trẻ xuất hiện như những thần tượng của giới trung lưu, luôn quấn quýt bên nhau trong mọi sự kiện xã hội.* | — | — | |
| 1-08 | `1.05#2` (9,2 s) | H | T1 | `t11_society_gala_inseparable_couple`, `push` | *Karla say đắm Paul đến mức tôn sùng hắn như một vị hoàng tử hoàn mỹ, sẵn sàng phục tùng mọi yêu sách kỳ quặc để duy trì ảo ảnh hạnh phúc.* | — | — | |
| 1-09 | `1.05#3` (12,0 s) | H | T1 | `t11_blind_adoration_shadow`, `pan` | *Chính vị thế xã hội và vỏ bọc kiểu mẫu ấy đã tạo nên một “Hiệu ứng Hào quang” chết người — một tấm khiên tàng hình ru ngủ hoàn toàn trực giác cảnh giác của cộng đồng suốt nhiều năm ròng.* | — | — | |
| 1-10 | `1.05#4` (7,8 s) | H | T1 | `t11_narcissistic_mirror_vanity`, `pull` | *Người ta chỉ thấy một cặp trai tài gái sắc yêu thương động vật và chăm chút tổ ấm, mà không hề mảy may nghi ngờ bóng tối bên trong.* | — | — | |
| 1-11 | `1.05#5` (7,1 s) | H | T1 | `t11_closed_pink_door_abyss`, `still` | *Để hiểu chiếc mặt nạ ấy hoàn hảo đến mức nào, hãy hình dung cảm nhận của những người từng sống bên cạnh ngôi nhà màu hồng.* | — | →N1 | |
| 1-12 | `1.06#1` (6,2 s) | N1 | T4 lời kể | `t11_lakeside_evening_dog_walk`, `push` | *Trong mắt tất cả chúng tôi tại khu phố ven hồ, Paul và Karla từng là một cặp đôi vàng mẫu mực.* | — | ✦ Cừu | |
| 1-13 | `1.06#2` (6,2 s) | N1 | T4 lời kể | `t11_lakeside_evening_dog_walk`, `pan` | *Họ luôn mỉm cười chào hỏi mọi người, chăm chút cho khu vườn nhỏ và dắt chó đi dạo mỗi buổi chiều tà.* | — | — | |
| 1-14 | `1.06#3` (8,3 s) | N1 | T4 lời kể | `t11_backyard_barbecue_lawn`, `pull` | *Nếu vào thời điểm ấy có ai nói rằng phía sau những khung cửa sổ sơn hồng là một địa ngục kinh hoàng nhất Bắc Mỹ, chắc chắn không một ai tin.* | — | — | |
| 1-15 | `1.06#4` (4,8 s) | N1 | T4 lời kể | `t11_lace_curtain_window_illusion`, `still` | *Chiếc mặt nạ thánh thiện của họ đã khiến cả một khu phố hoàn toàn mù quáng.* | — | →C | |
| 1-16 | `1.07#1` (9,1 s) | C | T1 | `t11_pink_house_winter_dusk`, `pan` | *Dưới lăng kính tâm lý học xã hội, chiếc mặt nạ của ngôi nhà màu hồng số 57 Bayview Drive là một ca nghiên cứu kinh điển về Hiệu ứng Hào quang và Điểm mù Ngoại ô.* | — | ✦ Cáo | |
| 1-17 | `1.07#2` (9,8 s) | C | T1 | `t11_expert_desk_lamp`, `pull` | *Bộ não con người có một xu hướng phán đoán sai lệch bẩm sinh: chúng ta thường mặc định những người trẻ trung, xinh đẹp, có việc làm danh giá và cử chỉ lịch thiệp là những tâm hồn thánh thiện.* | — | — | |
| 1-18 | `1.07#3` (8,5 s) | C | T1 | `t11_ideal_couple_veil_gold`, `push` | *Khi Paul và Karla khoác lên mình hình tượng cặp búp bê Ken và Barbie hoàn hảo, họ đã dựng nên một tấm khiên vô hình ru ngủ hoàn toàn bản năng phòng vệ của cộng đồng.* | — | — | |
| 1-19 | `1.07#4` (10,8 s) | C | T1 | `t11_suburban_admiration_facade`, `still` | *Chúng ta dễ dàng đề phòng một kẻ lôi thôi, khả nghi lẩn khuất trong ngõ tối, nhưng lại hoàn toàn mất cảnh giác trước một cặp vợ chồng trung lưu dắt chó đi dạo và nở nụ cười rạng rỡ bên hàng rào hoa hồng.* | — | →H | |
| 1-20 | `1.08#1` (7,9 s) | H | T1 | `t11_niagara_lakeshore_fog_night`, `pan` | *Và cái giá phải trả cho sự mù quáng ấy là một cơn hoang tưởng tập thể bao trùm khắp miền Nam tỉnh Ontario suốt nửa thập kỷ.* | — | — | |
| 1-21 | `1.08#2` (6,6 s) | H | T1 | `t11_bus_stop_night_desolation`, `pull` | *Những con phố ven hồ vốn yên bình bỗng chốc trở thành nơi rình rập của nỗi kinh hoàng vô hình.* | — | — | |
| 1-22 | `1.08#3` (9,1 s) | H | T1 | `t11_empty_crossroads_searchlight`, `push` | *Các bậc cha mẹ không còn dám để con gái tự bước qua cổng trường; những ánh mắt nhìn nhau đầy ngờ vực xuất hiện ngay tại các bến xe buýt và công viên.* | — | — | |
| 1-23 | `1.08#4` (13,4 s) | H | T1 | `t11_fairytale_wedding_carriage`, `still` | *Sự an toàn quen thuộc của cuộc sống thường nhật sụp đổ hoàn toàn khi người ta bàng hoàng nhận ra: Ác quỷ không mang hình thù dị hợm, mà đang mỉm cười chào họ từ chính cỗ xe ngựa cổ tích giữa ban ngày.* | — | — | |
| 1-24 | `1.10#1` (9,5 s) | H | T1 | `t11_scarborough_nocturnal_shadow`, `push` | *Thế nhưng, đằng sau cánh cửa đóng kín của căn nhà số 57 Bayview Drive là một thực tại tăm tối vượt xa mọi giới hạn tưởng tượng của con người.* | — | — | |
| 1-25 | `1.10#2` (9,5 s) | H | T1 | `t11_scarborough_nocturnal_shadow`, `pan` | *Cùng thời điểm cặp đôi Ken và Barbie đang tận hưởng cuộc sống nhung lụa, một bóng ma kinh hoàng đang bao trùm khắp miền Nam tỉnh Ontario.* | — | — | |
| 1-26 | `1.10#3` (13,4 s) | H | T1 | `t11_scarborough_taskforce_archive`, `pull` | *Từ năm 1987 đến năm 1990, khu vực ngoại ô Scarborough của thành phố Toronto bị rung chuyển bởi một kẻ gây án hàng loạt mang biệt danh “Scarborough Rapist”.* | — | — | |
| 1-27 | `1.10#4` (7,4 s) | H | T1 | `t11_scarborough_taskforce_archive`, `still` | *Hắn rình rập phụ nữ trẻ đi một mình trong đêm tối, tấn công chớp nhoáng rồi biến mất không để lại dấu vết.* | — | — | |
| 1-28 | `1.10#5` (7,5 s) | H | T1 | `t11_bus_stop_night_desolation`, `push` | *Cơn hoang tưởng xã hội và chấn thương tập thể bao trùm khắp các trạm xe buýt và khu dân cư khi màn đêm buông xuống.* | — | →D | |
| 1-29 | `1.12#1` (11,2 s) | D | T1 | `t11_church_parking_lot_ambush`, `pan` | *Cảnh sát Toronto đã lập một nhóm đặc nhiệm quy mô lớn chưa từng có để truy tìm kẻ thủ ác vùng Scarborough, thu thập hàng trăm mẫu dấu vết nhưng hắn vẫn lẩn khuất ngoài vòng pháp luật.* | — | ✦ Sói | |
| 1-30 | `1.12#2` (7,3 s) | D | T1 | `t11_church_parking_lot_ambush`, `pull` | *Nỗi khiếp đảm thực sự bùng nổ khi hành vi phạm tội vượt qua lằn ranh tấn công đơn thuần để bước sang quỹ đạo tước đoạt sinh mạng.* | — | — | |
| 1-31 | `1.12#3` (10,4 s) | D | T1 | `t11_burlington_house_dusk_empty`, `still` | *Tháng 6 năm 1991, nữ sinh 14 tuổi Leslie Mahaffy đột ngột biến mất tại thành phố Burlington sau khi vô tình bị khóa ngoài cửa nhà trong đêm.* | — | — | |
| 1-32 | `1.12#4` (5,1 s) | D | T1 | `t11_lake_gibson_fog_depths`, `push` | *Hai tuần sau, tin tức xác nhận cô bé đã không còn sống làm chấn động toàn bộ dư luận Canada.* | — | — | |
| 1-33 | `1.12#5` (14,1 s) | D | T1 | `t11_lake_gibson_fog_depths`, `pan` | *Chưa đầy một năm sau, vào tháng 4 năm 1992, nữ sinh 15 tuổi Kristen French tiếp tục bị bắt cóc giữa ban ngày ngay tại bãi đỗ xe của một nhà thờ ở thành phố Saint Catharines khi đang trên đường đi học về.* | — | — | |
| 1-34 | `1.12#6` (7,4 s) | D | T1 | `t11_niagara_lakeshore_fog_night`, `pull` | *Hai vụ án chấn động xảy ra ngay trong vùng Niagara, cách ngôi nhà màu hồng của Paul và Karla chỉ vài dặm đường.* | — | →H | |
| 1-35 | `1.13#1` (7,8 s) | H | T1 | `t11_map_proximity_dark_crossroads`, `still` | *Cả đất nước Canada rơi vào trạng thái hoảng loạn và phẫn nộ tột cùng trước sự tàn độc của kẻ săn mồi giấu mặt.* | — | — | |
| 1-36 | `1.13#2` (7,0 s) | H | T1 | `t11_map_proximity_dark_crossroads`, `push` | *Phụ nữ không dám bước ra đường một mình, các bậc phụ huynh nơm nớp lo sợ và đưa đón con cái từng bước chân.* | — | — | |
| 1-37 | `1.13#3` (4,6 s) | H | T1 | `t11_empty_crossroads_searchlight`, `pan` | *Ai là kẻ thủ ác đang gieo rắc nỗi kinh hoàng cho những thiếu nữ ngây thơ?* | — | — | |
| 1-38 | `1.13#4` (8,2 s) | H | T1 | `t11_ideal_couple_veil_gold`, `pull` | *Và làm thế nào một cặp đôi trẻ có vẻ ngoài đẹp như tranh vẽ lại trở thành tâm điểm của một liên minh tội ác kỳ dị nhất lịch sử tư pháp?* | — | — | |
| 1-39 | `1.13#5` (8,8 s) | H | T1 | `t11_pink_house_winter_dusk`, `still` | *Sự thật phía sau chiếc mặt nạ “Ken và Barbie” là một bài học đắt giá về điểm mù xã hội khi con người bị mê hoặc bởi vẻ bề ngoài.* | — | — | |
| 1-40 | `1.13#6` (5,0 s) | H | T1 | `t11_neighbourhood_winter_evening`, `push` | *Chúng ta hãy cùng lắng nghe phân tích chuyên môn về cách thức tội ác đã âm thầm hình thành.* | — | — | |
| 1-41 | `1.15#1` (5,2 s) | H | T1 | `t11_amber_eyes_redflag_intro`, `pan` | *Chào mừng quý vị đến với kênh Amber eyes và hồ sơ phân tích tâm lý học tội phạm hôm nay.* | — | — | |
| 1-42 | `1.15#2` (9,1 s) | H | T1 | `t11_amber_eyes_redflag_intro`, `pull` | *Chúng ta sẽ cùng mở khóa một trong những vụ án gây chấn động và tranh cãi sâu sắc nhất: Hồ sơ Paul Bernardo và Karla Homolka.* | — | — | |
| 1-43 | `1.15#3` (11,0 s) | H | T1 | `t11_closed_dossier_desk`, `still` | *Tập phim này sẽ giải mã hiện tượng “Điên cuồng đôi”, cơ chế đóng vai nạn nhân thao túng lòng trắc ẩn, và bản hợp đồng tư pháp cay đắng mang tên “Thỏa thuận với Quỷ dữ”.* | — | — | |
| 1-44 | `1.15#4` (9,1 s) | H | T1 | `t11_folie_a_deux_resonance`, `push` | *Đồng thời, chúng tôi sẽ phân tích sâu sắc Hệ sinh thái 10 chỉ dấu tâm lý và hành vi để giúp nhận diện những mối quan hệ độc hại trong cuộc sống.* | — | — | |
| 1-45 | `1.15#5` (8,0 s) | H | T1 | `t11_amber_eyes_closing_dossier_bernardo`, `pan` | *Đây không chỉ là câu chuyện về một vụ án trong quá khứ, mà là lời cảnh tỉnh sâu sắc cho sự an toàn của mỗi chúng ta hôm nay.* | — | — | |
| 1-46 | `1.15#6` (5,8 s) | H | T1 | `t11_amber_eyes_closing_dossier_bernardo`, `pull` | *Xin mời quý vị cùng chúng tôi bước vào Hồi thứ hai để giải mã quỹ đạo leo thang của tội ác.* | — | — | |
| 1-47 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 02* · **HIỆN TRƯỜNG & VỰC THẲM LEO THANG — 4 NẤC THANG TỘI ÁC** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & VỰC THẲM LEO THANG — 4 NẤC THANG TỘI ÁC

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (9,0 s) | H | T1 | `t11_marsh_hunting_ground_night`, `still` | *Khi hai thiếu nữ vô tội liên tiếp biến mất tại khu vực Niagara, cơ quan điều tra nhận định họ không chỉ đối mặt với những vụ bắt cóc đơn lẻ.* | — | — | |
| 2-02 | `2.02#2` (8,4 s) | H | T1 | `t11_marsh_hunting_ground_night`, `push` | *Kẻ thủ ác không xuất hiện từ hư không; hắn là một kẻ săn mồi đã tích lũy kinh nghiệm qua nhiều năm rèn giũa kỹ năng trong bóng tối.* | — | — | |
| 2-03 | `2.02#3` (8,8 s) | H | T1 | `t11_destructive_flame_alliance`, `pan` | *Tội ác của Paul Bernardo và Karla Homolka là kết quả của một chu kỳ ảo tưởng và dung nạp kích thích cực kỳ bệnh hoạn.* | — | — | |
| 2-04 | `2.02#4` (9,0 s) | H | T1 | `t11_destructive_flame_alliance`, `pull` | *Giống như một cơn nghiện độc hại, khi những hành vi ban đầu không còn đem lại sự hưng phấn quyền lực, ngưỡng thỏa mãn buộc phải đẩy lên cao hơn.* | — | — | |
| 2-05 | `2.02#5` (7,2 s) | H | T1 | `t11_four_floor_stairwell_shadow`, `still` | *Toàn bộ chuỗi hành vi của cặp đôi này vận hành qua 4 nấc thang leo thang hành vi tàn bạo kéo dài suốt 5 năm.* | — | — | |
| 2-06 | `2.02#6` (5,1 s) | H | T1 | `t11_four_floor_stairwell_shadow`, `push` | *Xin mời Điều tra viên tái hiện lại các giai đoạn phát triển tội ác trong hồ sơ nghiệp vụ.* | — | →D | |
| 2-07 | `2.04#1` (6,6 s) | D | T1 | `t11_investigation_board_four_stages`, `pan` | *Dựa trên dữ liệu điều tra liên ngành, chúng tôi đã tái dựng quỹ đạo tha hóa của Paul Bernardo qua 4 giai đoạn leo thang rõ rệt.* | — | — | |
| 2-08 | `2.04#2` (2,9 s) | D | T1 | `t11_scarborough_night_street_lurking`, `pull` | *Nấc thang thứ nhất: Tấn công đơn lẻ tại ngoại ô.* | — | — | |
| 2-09 | `2.04#3` (12,2 s) | D | T1 | `t11_scarborough_night_street_lurking`, `still` | *Từ tháng 5 năm 1987, Paul Bernardo bắt đầu rình rập và thực hiện ít nhất 14 vụ tấn công phụ nữ trẻ tại vùng Scarborough, hành động đơn độc và tẩu thoát nhanh trong đêm.* | — | — | |
| 2-10 | `2.04#4` (3,7 s) | D | T1 | `t11_christmas_1990_halothane_bottle`, `push` | *Nấc thang thứ hai: Thiết lập liên minh và xâm phạm người thân.* | — | — | |
| 2-11 | `2.04#5` (19,6 s) | D | T1 | `t11_christmas_1990_halothane_bottle`, `pan` | *Tháng 10 năm 1987, hắn gặp Karla Homolka; sự gắn kết lệch lạc đã thúc đẩy chúng nhắm vào chính em gái ruột của Karla là Tammy Homolka vào đêm Giáng sinh năm 1990 bằng thuốc an thần đánh cắp, dẫn đến sự ra đi đau lòng của cô bé.* | — | — | |
| 2-12 | `2.04#6` (3,4 s) | D | T1 | `t11_bayview_basement_concrete`, `pull` | *Nấc thang thứ ba: Bắt cóc giam giữ dài ngày tại tư gia.* | — | — | |
| 2-13 | `2.04#7` (12,8 s) | D | T1 | `t11_bayview_basement_concrete`, `still` | *Tháng 6 năm 1991, sau khi kết hôn, chúng bắt cóc Leslie Mahaffy, đưa về giam cầm và ngược đãi tại căn nhà số 57 Bayview Drive trước khi tước đoạt mạng sống của cô bé.* | — | — | |
| 2-14 | `2.04#8` (3,6 s) | D | T1 | `t11_church_parking_daytime_abduction`, `push` | *Và nấc thang thứ tư: Táo tợn bắt cóc công khai giữa ban ngày.* | — | — | |
| 2-15 | `2.04#9` (11,9 s) | D | T1 | `t11_church_parking_daytime_abduction`, `pan` | *Tháng 4 năm 1992, chúng phục kích bắt giữ Kristen French ngay tại bãi xe nhà thờ đông người ở Saint Catharines, chứng tỏ ảo tưởng quyền lực đã lấn át hoàn toàn nỗi sợ bị phát giác.* | — | — | |
| 2-16 | `2.04#10` (7,2 s) | D | T1 | `t11_lake_gibson_culvert_darkness`, `pull` | *Điểm đáng sợ nhất là sự phối hợp nhịp nhàng giữa hai kẻ thủ ác trong việc giam cầm và tiêu hủy mọi dấu vết sau mỗi vụ án.* | — | — | |
| 2-17 | `2.04#11` (7,2 s) | D | T1 | `t11_lake_gibson_culvert_darkness`, `still` | *Chúng sử dụng xi măng và các công cụ cơ khí để giấu tang vật dưới lòng kênh đào Lake Gibson nhằm đánh lạc hướng cơ quan chức năng.* | — | — | |
| 2-18 | `2.04#12` (5,9 s) | D | T1 | `t11_equal_partner_in_cruelty`, `push` | *Đó là sự biến chất từ một kẻ rình rập đơn độc thành một cặp đôi sát nhân tàn độc có tổ chức.* | — | →H | |
| 2-19 | `2.06#1` (6,2 s) | H | T1 | `t11_silent_christmas_tragedy`, `pan` | *Nhìn vào danh tính của các nạn nhân, chúng ta thấy rõ sự tàn nhẫn của động lực bất đối xứng quyền lực.* | — | — | |
| 2-20 | `2.06#2` (7,2 s) | H | T1 | `t11_silent_christmas_tragedy`, `pull` | *Tammy Homolka là một cô bé 15 tuổi ngây thơ, đặt trọn niềm tin vào người chị gái ruột thịt của mình.* | — | — | |
| 2-21 | `2.06#3` (9,7 s) | H | T1 | `t11_frozen_justice_gavel`, `still` | *Leslie Mahaffy và Kristen French là những nữ sinh trung học tràn đầy ước mơ, bị tước đoạt tương lai chỉ vì lọt vào tầm ngắm của những kẻ săn mồi.* | — | — | |
| 2-22 | `2.06#4` (7,0 s) | H | T1 | `t11_frozen_justice_gavel`, `push` | *Tuy nhiên, sự thật lịch sử phải tôn vinh sự kiên cường và phẩm giá bất khuất của Kristen French.* | — | — | |
| 2-23 | `2.06#5` (7,7 s) | H | T1 | `t11_snowbound_patrol_road`, `pan` | *Trong suốt những ngày bị giam giữ, cô bé 15 tuổi ấy đã kiên quyết không chịu khuất phục và chiến đấu dũng cảm đến hơi thở cuối cùng.* | — | — | |
| 2-24 | `2.06#6` (10,1 s) | H | T1 | `t11_light_of_justice_prevails`, `pan` | *Trong bóng tối ngột ngạt của sự bạo tàn, lịch sử tư pháp Canada mãi mãi khắc ghi tên tuổi của Kristen French như một ngọn hải đăng của lòng dũng cảm.* | — | — | |
| 2-25 | `2.06#7` (4,9 s) | H | T1 | `t11_quiet_window_closing`, `pull` | *Cô bé mười lăm tuổi ấy đã không hề buông xuôi hay van xin trong tuyệt vọng.* | — | — | |
| 2-26 | `2.06#8` (9,2 s) | H | T1 | `t11_empty_chair_black_ribbon`, `push` | *Bằng một ý chí sinh tồn kiên cường phi thường, Kristen đã chiến đấu quyết liệt đến hơi thở cuối cùng để bảo vệ phẩm giá của chính mình.* | — | — | |
| 2-27 | `2.06#9` (13,1 s) | H | T1 | `t11_february_arrest_dna_match`, `still` | *Chính những dấu vết cào cấu mà em để lại trên cơ thể kẻ thủ ác đã trở thành chiếc chìa khóa pháp y vô giá, giữ chặt mẫu ADN của Paul Bernardo để đưa hắn ra trước ánh sáng công lý.* | — | — | |
| 2-28 | `2.06#10` (12,1 s) | H | T1 | `t11_quiet_window_closing`, `pan` | *Sự kiên cường của Kristen nhắc nhở chúng ta rằng: Ngay cả khi thể xác bị giam cầm, phẩm giá và khí phách con người vẫn là thứ mà không một kẻ bạo tàn nào có thể tước đoạt.* | — | →D | |
| 2-29 | `2.07#1` (5,9 s) | D | T1 | `t11_flashlight_shattered_hallway`, `pull` | *Kristen French đã để lại những vết cào cấu quyết liệt trên người Paul Bernardo trong lúc giằng co tự vệ.* | — | — | |
| 2-30 | `2.07#2` (5,6 s) | D | T1 | `t11_flashlight_shattered_hallway`, `still` | *Chính tinh thần phản kháng bất khuất ấy đã giúp lưu giữ những mẫu ADN quan trọng của kẻ thủ ác.* | — | — | |
| 2-31 | `2.07#3` (6,1 s) | D | T1 | `t11_two_dossier_folders_desk`, `push` | *Về mặt nghiệp vụ, chúng tôi phân định rất rõ giữa hai yếu tố: “Thủ đoạn gây án” và “Dấu ấn tâm lý”.* | — | — | |
| 2-32 | `2.07#4` (9,0 s) | D | T1 | `t11_chilling_polaroid_camera`, `pan` | *Thủ đoạn gây án của chúng là sử dụng công cụ đe dọa, cắt đứt liên lạc, dùng thuốc an thần động vật và che giấu chứng cứ nhằm trốn tránh pháp luật.* | — | — | |
| 2-33 | `2.07#5` (4,5 s) | D | T1 | `t11_chilling_polaroid_camera`, `pull` | *Thủ đoạn này liên tục thay đổi và hoàn thiện sau mỗi lần gây án để đối phó với cảnh sát.* | — | — | |
| 2-34 | `2.07#6` (7,2 s) | D | T1 | `t11_handheld_camera_lens`, `still` | *Nhưng “Dấu ấn tâm lý” — thứ không bao giờ thay đổi — chính là nhu cầu bệnh lý về việc ghi hình lại toàn bộ tội ác.* | — | →C | |
| 2-35 | `2.09#1` (6,6 s) | C | T1 | `t11_holding_video_camera_director`, `push` | *Đúng như vậy, việc dùng máy quay cầm tay để ghi lại từng thước phim giam cầm không hề phục vụ cho mục đích tẩu thoát của chúng.* | — | — | |
| 2-36 | `2.09#2` (5,9 s) | C | T1 | `t11_holding_video_camera_director`, `pan` | *Đó là hành vi thuộc về “Signature” — dấu ấn tâm lý thỏa mãn cảm giác thống trị và chiếm hữu tuyệt đối.* | — | — | |
| 2-37 | `2.09#3` (6,4 s) | C | T1 | `t11_tripod_camera_dark_room`, `pull` | *Chúng ép buộc các nạn nhân phải gọi chúng bằng những danh xưng phục tùng, biến nỗi đau của người khác thành những thước phim chiến lợi phẩm.* | — | — | |
| 2-38 | `2.09#4` (6,3 s) | C | T1 | `t11_morbid_thrill_abyss`, `still` | *Đối với Paul Bernardo, các cuộn băng là liều kích thích kích hoạt lại ảo tưởng vĩ cuồng mỗi khi hắn ngồi xem lại một mình.* | — | — | |
| 2-39 | `2.09#5` (6,2 s) | C | T1 | `t11_morbid_thrill_abyss`, `push` | *Còn đối với Karla Homolka, việc cầm máy quay là cách cô ta thể hiện sự gắn kết chặt chẽ với người bạn đời lệch lạc.* | — | — | |
| 2-40 | `2.09#6` (4,6 s) | C | T1 | `t11_videotape_reels_stack`, `pan` | *Những cuộn băng ấy chính là chiếc chìa khóa duy nhất bóc trần bản chất thật của liên minh tội ác này.* | — | — | |
| 2-41 | `2.09#7` (9,0 s) | C | T1 | `t11_handheld_camera_lens`, `pull` | *Về mặt khoa học hành vi, hành vi bắt buộc phải dùng máy quay cầm tay ghi lại toàn bộ quá trình phạm tội chính là một Chữ ký Tâm lý phản ánh sự lệch lạc nhân cách cùng cực.* | — | — | |
| 2-42 | `2.09#8` (6,2 s) | C | T1 | `t11_tripod_camera_dark_room`, `push` | *Đối với Paul Bernardo, chiếc máy quay không đơn thuần là công cụ lưu trữ; nó là một Chiến lợi phẩm Thần kinh.* | — | — | |
| 2-43 | `2.09#9` (10,7 s) | C | T1 | `t11_videotape_reels_stack`, `still` | *Kẻ mang cấu trúc ái kỷ bạo dâm luôn sống trong nỗi sợ hãi vô thức về sự bất lực của bản thân; việc xem lại những thước phim là cách hắn tái kích hoạt ảo tưởng quyền lực toàn năng mỗi khi đối diện với thực tại tầm thường.* | — | — | |
| 2-44 | `2.09#10` (13,7 s) | C | T1 | `t11_lace_curtain_window_illusion`, `pan` | *Còn đối với Karla Homolka, việc chủ động điều khiển góc quay và ra lệnh cho nạn nhân chính là bằng chứng đanh thép bóc trần sự tha hóa: Cô ta tìm thấy khoái cảm quyền lực khi được đứng ngang hàng với kẻ săn mồi để định đoạt số phận đồng loại.* | — | →H | |
| 2-45 | `2.10#1` (8,8 s) | H | T1 | `t11_curtained_window_closed_room`, `pull` | *Thủ đoạn giúp chúng che giấu hành vi suốt nhiều năm ròng rã, nhưng chính dấu ấn tâm lý bệnh hoạn lại trở thành bằng chứng thép kết tội chúng.* | — | — | |
| 2-46 | `2.10#2` (8,0 s) | H | T1 | `t11_curtained_window_closed_room`, `still` | *Nhưng điều gì đã khiến một cô gái trẻ xinh đẹp, có công việc ổn định lại sẵn sàng đồng lõa với những hành vi tàn nhẫn như vậy?* | — | — | |
| 2-47 | `2.10#3` (7,5 s) | H | T1 | `t11_coupled_shadows_mirror`, `push` | *Làm thế nào một mối quan hệ tình cảm lại có thể biến thành một buồng cộng hưởng ác tính thiêu rụi mọi ranh giới lương tri?* | — | — | |
| 2-48 | `2.10#4` (7,2 s) | H | T1 | `t11_coupled_shadows_mirror`, `pan` | *Hãy cùng chúng tôi bước vào Hồi thứ ba để giải phẫu hiện tượng tâm lý học kỳ dị mang tên “Điên cuồng đôi”.* | — | — | |
| 2-49 | `2.10#5` (6,2 s) | H | T1 | `t11_consultation_room_two_chairs`, `pull` | *Xin mời Chuyên gia tâm lý làm sáng tỏ cơ chế bên trong bộ não của cặp đôi Ken và Barbie.* | — | →D | |
| 2-50 | `2.12#1` (7,0 s) | D | T1 | `t11_st_catharines_hospital_night`, `still` | *Trước khi đi vào cơ chế tâm lý, các dữ liệu khám xét tại số 57 Bayview Drive cần được nhìn nhận một cách khách quan.* | — | — | |
| 2-51 | `2.12#2` (7,7 s) | D | T1 | `t11_st_catharines_hospital_night`, `push` | *Ngôi nhà sơn hồng bên ngoài trông vô cùng ấm cúng, nhưng bên trong phòng ngủ và tầng hầm lại được bố trí như những căn phòng biệt lập.* | — | — | |
| 2-52 | `2.12#3` (5,3 s) | D | T1 | `t11_evidence_bags_lab_bench`, `pan` | *Hàng trăm vật dụng cá nhân của các nạn nhân đã được thu giữ và đối chiếu ADN cẩn trọng.* | — | — | |
| 2-53 | `2.12#4` (5,4 s) | D | T1 | `t11_february_arrest_dna_match`, `pull` | *Mỗi món đồ bị lấy đi không mang giá trị vật chất, mà mang ý nghĩa của những chiến lợi phẩm khẳng định quyền lực.* | — | — | |
| 2-54 | `2.12#5` (3,8 s) | D | T1 | `t11_february_arrest_dna_match`, `still` | *Các điều tra viên nhận thấy hung thủ không hành động trong trạng thái hoảng loạn bộc phát.* | — | — | |
| 2-55 | `2.12#6` (5,4 s) | D | T1 | `t11_cold_calculation_desk`, `push` | *Mọi bước đi đều thể hiện sự toan tính lạnh lùng của những bộ óc hoàn toàn làm chủ nhận thức của mình.* | — | →H | |
| 2-56 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 03* · **GIẢI MÃ LIÊN MINH BỆNH HOẠN — ĐIÊN CUỒNG ĐÔI & TRUNG HÒA ĐẠO ĐỨC** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI MÃ LIÊN MINH BỆNH HOẠN — ĐIÊN CUỒNG ĐÔI & TRUNG HÒA ĐẠO ĐỨC

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (8,2 s) | H | T1 | `t11_unanswered_question_corridor`, `pan` | *Đứng trước hồ sơ của Paul Bernardo và Karla Homolka, bất kỳ ai trong chúng ta cũng phải đối mặt với một câu hỏi nhức nhối.* | — | — | |
| 3-02 | `3.02#2` (7,8 s) | H | T1 | `t11_unanswered_question_corridor`, `pull` | *Động lực tâm lý nào đã biến một cặp vợ chồng trẻ trung, có học thức thành những kẻ săn mồi tàn bạo nhất lịch sử Canada?* | — | — | |
| 3-03 | `3.02#3` (7,6 s) | H | T1 | `t11_hostage_puppet_facade`, `still` | *Liệu Karla Homolka chỉ đơn thuần là một nạn nhân bị bạo hành và cưỡng ép như những gì cô ta từng trình bày trước tòa?* | — | — | |
| 3-04 | `3.02#4` (5,6 s) | H | T1 | `t11_hostage_puppet_facade`, `push` | *Hay cô ta chính là một phần không thể tách rời của một cấu trúc tội ác cộng sinh nguy hiểm?* | — | — | |
| 3-05 | `3.02#5` (10,2 s) | H | T1 | `t11_half_truth_dossier_shadow`, `pan` | *Chúng ta cần lưu ý rằng, các phân tích tâm lý dưới đây dựa trên các khung lý thuyết khoa học hành vi và hồ sơ xét xử công khai, không phải là sự quy chụp tùy tiện.* | — | — | |
| 3-06 | `3.02#6` (4,3 s) | H | T1 | `t11_half_truth_dossier_shadow`, `pull` | *Xin mời Chuyên gia tâm lý giải mã hiện tượng tâm lý học đặc biệt này.* | — | →C | |
| 3-07 | `3.04#1` (6,1 s) | C | T1 | `t11_two_shadows_one_wall`, `still` | *Khung lý thuyết kinh điển giúp giải thích trường hợp này là hiện tượng “Điên cuồng đôi”, hay còn gọi là Hội chứng Folie à Deux.* | — | — | |
| 3-08 | `3.04#2` (7,5 s) | C | T1 | `t11_two_shadows_one_wall`, `push` | *Đây là một hiện tượng hiếm gặp khi hai cá nhân có cấu trúc tâm lý lệch lạc gặp gỡ và kết hợp với nhau, tạo ra một buồng cộng hưởng tội ác.* | — | — | |
| 3-09 | `3.04#3` (6,6 s) | C | T1 | `t11_malignant_narcissist_throne`, `pan` | *Trong mối quan hệ này, Paul Bernardo đóng vai trò là kẻ khởi xướng mang tính ái kỷ ác tính và thái nhân cách chống đối xã hội.* | — | — | |
| 3-10 | `3.04#4` (6,4 s) | C | T1 | `t11_malignant_narcissist_throne`, `pull` | *Hắn khao khát quyền lực thống trị tuyệt đối, xem phụ nữ như những công cụ phục vụ cho sự thỏa mãn bản ngã vĩ cuồng của mình.* | — | — | |
| 3-11 | `3.04#5` (5,4 s) | C | T1 | `t11_covert_sociopath_profile`, `still` | *Ở chiều ngược lại, Karla Homolka không hề là một người bình thường bị cuốn vào vòng xoáy một cách thụ động.* | — | — | |
| 3-12 | `3.04#6` (7,6 s) | C | T1 | `t11_covert_sociopath_profile`, `push` | *Các nhà phân tích hành vi chỉ ra rằng Karla mang khiếm khuyết sâu sắc về năng lực thấu cảm, kết hợp với nỗi sợ hãi bệnh lý bị người tình bỏ rơi.* | — | — | |
| 3-13 | `3.04#7` (7,7 s) | C | T1 | `t11_dark_cinema_empty_seats`, `pan` | *Thay vì sợ hãi rút lui khi chứng kiến xu hướng bạo lực của Paul, Karla lại tìm thấy ở hắn một cảm giác kích thích quyền lực và sự lệ thuộc mù quáng.* | — | — | |
| 3-14 | `3.04#8` (4,8 s) | C | T1 | `t11_dark_cinema_empty_seats`, `pull` | *Khi hai cấu trúc tâm lý đó hòa quyện, mọi rào cản đạo đức thông thường đã bị xóa bỏ hoàn toàn.* | — | →H | |
| 3-15 | `3.05#1` (7,4 s) | H | T1 | `t11_unholy_sacrament_altar`, `still` | *Sự cộng sinh độc hại này đã dẫn tới một hiện tượng tâm lý cực kỳ tàn nhẫn: “vật hóa” hoàn toàn nạn nhân.* | — | — | |
| 3-16 | `3.05#2` (6,2 s) | H | T1 | `t11_unholy_sacrament_altar`, `push` | *Trong mắt của cả Paul và Karla, những thiếu nữ ngây thơ kia bị nhìn nhận như thế nào, thưa chuyên gia?* | — | — | |
| 3-17 | `3.05#3` (5,9 s) | H | T1 | `t11_christmas_snow_front_porch`, `pan` | *Tại sao Karla có thể nhẫn tâm đưa chính người em gái ruột thịt của mình vào chiếc bẫy oan nghiệt?* | — | — | |
| 3-18 | `3.05#4` (6,3 s) | H | T1 | `t11_christmas_snow_front_porch`, `pull` | *Đó là câu hỏi khiến hàng triệu người dân Canada đau đớn và phẫn nộ suốt nhiều thập kỷ qua.* | — | — | |
| 3-19 | `3.05#5` (3,3 s) | H | T1 | `t11_expert_desk_lamp`, `still` | *Xin mời chuyên gia phân tích cơ chế nhận thức đen tối này.* | — | →C | |
| 3-20 | `3.06#1` (3,7 s) | C | T1 | `t11_featureless_peg_dolls`, `push` | *Khái niệm cốt lõi ở đây chính là “vật hóa” và “phi nhân hóa” nạn nhân.* | — | — | |
| 3-21 | `3.06#2` (6,1 s) | C | T1 | `t11_featureless_peg_dolls`, `pan` | *Paul Bernardo xem các nạn nhân như những món đồ chơi dùng một lần để thỏa mãn cơn nghiện quyền lực và ảo tưởng tình dục.* | — | — | |
| 3-22 | `3.06#3` (7,6 s) | C | T1 | `t11_empty_chair_black_ribbon`, `pull` | *Còn đối với Karla Homolka, bi kịch nằm ở chỗ cô ta giáng cấp chính em gái mình thành một “vật hiến tế” để củng cố mối liên kết tình cảm với Paul.* | — | — | |
| 3-23 | `3.06#4` (8,6 s) | C | T1 | `t11_grieving_parents_wedding_mask`, `still` | *Karla hoàn toàn thiếu hụt “Thuyết tâm trí” đối với nỗi đau của người khác; tiếng khóc van xin không kích hoạt lòng trắc ẩn mà bị xem như trở ngại cần loại bỏ.* | — | — | |
| 3-24 | `3.06#5` (4,5 s) | C | T1 | `t11_grieving_parents_wedding_mask`, `push` | *Để duy trì cuộc sống thường nhật, Karla áp dụng triệt để cơ chế “Chia ngăn nhận thức”.* | — | — | |
| 3-25 | `3.06#6` (6,6 s) | C | T1 | `t11_divided_room_two_doors`, `pan` | *Cô ta khóa chặt thế giới người vợ hiền yêu thương động vật ở một ngăn, và thế giới đồng lõa săn mồi ở một ngăn hoàn toàn biệt lập.* | — | — | |
| 3-26 | `3.06#7` (6,3 s) | C | T1 | `t11_divided_room_two_doors`, `pull` | *Cuộc hôn nhân màu hồng và đám cưới cổ tích chính là “Lá chắn bình thường hóa” giúp cô ta tự huyễn hoặc về phẩm giá của bản thân.* | — | — | |
| 3-27 | `3.06#8` (7,4 s) | C | T1 | `t11_moral_licence_blank_notes`, `still` | *Cô ta sử dụng các kỹ thuật “Trung hòa đạo đức” để ru ngủ lương tri: tự nhủ rằng mình chỉ làm để làm vui lòng chồng và giữ gìn gia đình.* | — | — | |
| 3-28 | `3.06#9` (11,0 s) | C | T1 | `t11_silent_christmas_tragedy`, `pull` | *Nhiều người không thể hiểu nổi: Làm sao một người chị gái có thể nhẫn tâm đưa chính em ruột của mình vào bẫy, rồi sau đó vẫn có thể thản nhiên dự đám tang và khóc lóc như một người chị chịu tang thương?* | — | — | |
| 3-29 | `3.06#10` (5,7 s) | C | T1 | `t11_consultation_room_two_chairs`, `push` | *Câu trả lời nằm ở cơ chế Chia ngăn Nhận thức Cực đoan kết hợp với Kỹ thuật Trung hòa Đạo đức.* | — | — | |
| 3-30 | `3.06#11` (7,4 s) | C | T1 | `t11_steel_wall_lifeless`, `still` | *Trong não bộ của Karla Homolka, thế giới người vợ hiền yêu gia đình và thế giới đồng lõa săn mồi được ngăn cách bằng một bức tường thép bệnh lý.* | — | — | |
| 3-31 | `3.06#12` (10,4 s) | C | T1 | `t11_composure_in_mirror`, `pan` | *Cô ta tự ru ngủ lương tri bằng lập luận méo mó rằng: Hiến tế em gái Tammy là một hành động hy sinh cần thiết để xoa dịu cơn khát quyền lực của Paul và bảo vệ cuộc hôn nhân màu hồng của mình.* | — | — | |
| 3-32 | `3.06#13` (7,9 s) | C | T1 | `t11_narcissistic_mirror_vanity`, `pull` | *Khi con người đặt sự lệ thuộc ái kỷ lên trên tình máu mủ và các chuẩn mực nhân tính tối thiểu, họ rơi vào một trạng thái Hôn mê Đạo đức hoàn toàn.* | — | — | |
| 3-33 | `3.06#14` (8,4 s) | C | T1 | `t11_cold_calculation_desk`, `push` | *Họ không còn nhìn thấy một sinh mệnh vô tội đang kêu cứu; họ chỉ nhìn thấy một vật cản hoặc một công cụ để phục vụ cho sự sinh tồn ích kỷ của bản ngã độc hại.* | — | →D | |
| 3-34 | `3.08#1` (3,6 s) | D | T1 | `t11_cracked_mirror_hallway`, `push` | *Tuy nhiên, liên minh nào rồi cũng sẽ phải đối mặt với điểm gãy nội tại.* | — | — | |
| 3-35 | `3.08#2` (8,3 s) | D | T1 | `t11_cracked_mirror_hallway`, `pan` | *Và điểm gãy tâm lý của cặp đôi Ken và Barbie xuất hiện vào tháng 1 năm 1993, sau những chuỗi ngày căng thẳng leo thang.* | — | — | |
| 3-36 | `3.08#3` (8,5 s) | D | T1 | `t11_flashlight_beam_floor`, `pull` | *Paul Bernardo bắt đầu bộc lộ sự hung hãn trực tiếp lên chính Karla, ngược đãi cô ta bằng một chiếc đèn pin lớn khiến cô ta phải nhập viện cấp cứu.* | — | — | |
| 3-37 | `3.08#4` (6,6 s) | D | T1 | `t11_escape_to_parents_porch`, `still` | *Trận đòn kinh hoàng đó đã phá vỡ chiếc mặt nạ tình yêu cổ tích, kích hoạt nỗi sợ hãi sinh tồn tột cùng bên trong Karla.* | — | — | |
| 3-38 | `3.08#5` (8,2 s) | D | T1 | `t11_escape_to_parents_porch`, `push` | *Nhận thấy người bạn đời đã trở thành mối đe dọa trực tiếp đến tính mạng của mình, Karla quyết định rời bỏ căn nhà số 57 Bayview Drive.* | — | — | |
| 3-39 | `3.08#6` (7,5 s) | D | T1 | `t11_police_raid_night_house`, `pan` | *Và chỉ một tháng sau đó, vào ngày 17 tháng 2 năm 1993, cảnh sát ập vào bắt giữ Paul Bernardo.* | — | — | |
| 3-40 | `3.08#7` (9,3 s) | D | T1 | `t11_police_raid_night_house`, `pull` | *Kết quả giám định ADN tồn đọng từ nhiều năm trước của Cảnh sát Toronto cuối cùng đã xác nhận Paul Bernardo chính là kẻ gây án hàng loạt vùng Scarborough.* | — | — | |
| 3-41 | `3.08#8` (6,8 s) | D | T1 | `t11_escape_ladder_night`, `still` | *Nhận thấy con thuyền tội ác sắp chìm nghỉm, Karla Homolka lập tức kích hoạt chiến lược sinh tồn tinh vi nhất cuộc đời mình.* | — | →H | |
| 3-42 | `3.09#1` (7,1 s) | H | T1 | `t11_interrogation_bruised_facade`, `push` | *Khi người chồng bị tra tay vào còng số tám, người đàn bà trong ngôi nhà màu hồng không hề lựa chọn việc thú tội chân thành.* | — | — | |
| 3-43 | `3.09#2` (6,6 s) | H | T1 | `t11_interrogation_bruised_facade`, `pan` | *Cô ta chọn cách đóng vai một nạn nhân yếu đuối, bị bạo hành và bị giam cầm trong sự sợ hãi suốt nhiều năm.* | — | — | |
| 3-44 | `3.09#3` (7,4 s) | H | T1 | `t11_pleading_victim_tears`, `pull` | *Một vở kịch thao túng lòng trắc ẩn hoàn hảo bắt đầu được dàn dựng trước mắt các điều tra viên và công tố viên hàng đầu.* | — | — | |
| 3-45 | `3.09#4` (6,0 s) | H | T1 | `t11_weaponized_victim_playing`, `still` | *Và vở kịch ấy đã dẫn tới một quyết định pháp lý gây chấn động bậc nhất thế kỷ 20.* | — | — | |
| 3-46 | `3.09#5` (5,5 s) | H | T1 | `t11_weaponized_victim_playing`, `push` | *Chúng ta hãy cùng bước vào Hồi thứ tư để chứng kiến sự sụp đổ của một ảo tưởng tư pháp.* | — | →C | |
| 3-47 | `3.11#1` (6,5 s) | C | T1 | `t11_victim_playing_camouflage_mirror`, `pan` | *Về mặt hành vi, sự phản bội này không xuất phát từ việc hồi tỉnh lương tri, mà hoàn toàn là một nước cờ bảo toàn bản thân.* | — | — | |
| 3-48 | `3.11#2` (6,6 s) | C | T1 | `t11_victim_playing_camouflage_mirror`, `pull` | *Khi buồng cộng hưởng Folie à Deux bị phá vỡ bởi xung đột lợi ích sinh tử, kẻ tiếp sức sẽ không ngần ngại bán đứng kẻ khởi xướng.* | — | — | |
| 3-49 | `3.11#3` (5,9 s) | C | T1 | `t11_press_scrum_silhouettes`, `still` | *Karla Homolka hiểu rằng ai lên tiếng trước với cơ quan công quyền sẽ là người nắm giữ quyền định đoạt số phận.* | — | — | |
| 3-50 | `3.11#4` (4,6 s) | C | T1 | `t11_press_scrum_silhouettes`, `push` | *Đó là bài học cay đắng nhất về bản chất của những kẻ thái nhân cách khi đối diện với sự trừng phạt.* | — | →H | |
| 3-51 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 04* · **THỎA THUẬN VỚI QUỶ DỮ & SỰ SỤP ĐỔ CỦA MẶT NẠ NẠN NHÂN** | — | ⊘ | ◼ |

### HỒI 4 — THỎA THUẬN VỚI QUỶ DỮ & SỰ SỤP ĐỔ CỦA MẶT NẠ NẠN NHÂN

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (9,7 s) | H | T1 | `t11_prosecution_clock_pressure`, `pan` | *Mùa xuân năm 1993, nền tư pháp tỉnh Ontario đứng trước một áp lực khủng khiếp từ dư luận và truyền thông quốc tế.* | — | — | |
| 4-02 | `4.02#2` (13,2 s) | H | T1 | `t11_prosecution_clock_pressure`, `pull` | *Paul Bernardo đã bị bắt vì các vụ án tại Scarborough, nhưng cảnh sát hoàn toàn bế tắc trong việc tìm kiếm bằng chứng vật chất trực tiếp để buộc tội hắn giết hại Leslie Mahaffy và Kristen French.* | — | — | |
| 4-03 | `4.02#3` (5,3 s) | H | T1 | `t11_silent_interview_corridor`, `still` | *Paul giữ im lặng tuyệt đối, từ chối mọi sự hợp tác và thách thức các điều tra viên.* | — | — | |
| 4-04 | `4.02#4` (7,6 s) | H | T1 | `t11_testimony_figure_shadow`, `push` | *Trong bối cảnh nghẹt thở ấy, Karla Homolka xuất hiện như một tia hy vọng duy nhất để giải mã hai vụ án mạng kinh hoàng.* | — | — | |
| 4-05 | `4.02#5` (7,9 s) | H | T1 | `t11_testimony_figure_shadow`, `pan` | *Được sự hậu thuẫn của các luật sư tài ba, Karla đã vận dụng hoàn hảo chiếc mặt nạ “Hội chứng Người phụ nữ bị Bạo hành”.* | — | — | |
| 4-06 | `4.02#6` (10,1 s) | H | T1 | `t11_folded_coat_empty_chair`, `pull` | *Cô ta trình bày những vết thương trên cơ thể do Paul gây ra, khóc lóc và khẳng định mình chỉ là một nhân chứng bất đắc dĩ bị ép buộc dưới họng súng.* | — | →D | |
| 4-07 | `4.04#1` (10,0 s) | D | T1 | `t11_missing_evidence_dilemma`, `still` | *Các công tố viên hàng đầu của bang Ontario lúc bấy giờ đã mắc phải một cái bẫy tâm lý kinh điển: Đánh giá quá cao lời khai nhân chứng và bị thao túng bởi vẻ ngoài yếu đuối.* | — | — | |
| 4-08 | `4.04#2` (9,3 s) | D | T1 | `t11_missing_evidence_dilemma`, `push` | *Họ tin rằng nếu không có lời khai của Karla, Paul Bernardo có thể sẽ thoát tội giết người cấp độ một và chỉ phải nhận mức án nhẹ cho các vụ án tại Scarborough.* | — | — | |
| 4-09 | `4.04#3` (6,4 s) | D | T1 | `t11_empty_evidence_box`, `pan` | *Mong muốn nhanh chóng đem lại công lý cho gia đình nạn nhân đã khiến cơ quan công tố đánh mất sự cẩn trọng nghề nghiệp cần thiết.* | — | — | |
| 4-10 | `4.04#4` (10,4 s) | D | T1 | `t11_deal_with_the_devil_contract`, `pull` | *Tháng 5 năm 1993, Văn phòng Tổng chưởng lý bang Ontario chính thức ký kết một bản thỏa thuận nhận tội đặc biệt với Karla Homolka.* | — | — | |
| 4-11 | `4.04#5` (8,3 s) | D | T1 | `t11_deal_with_the_devil_contract`, `still` | *Theo thỏa thuận, Karla nhận hai tội danh Ngộ sát với tổng mức án 12 năm tù giam, để đổi lấy lời khai vạch tội chồng mình trước tòa.* | — | — | |
| 4-12 | `4.04#6` (7,3 s) | D | T1 | `t11_sealed_document_folder`, `push` | *Đổi lại, cô ta được miễn trừ truy tố đối với mọi hành vi liên quan đến sự ra đi của em gái Tammy và hai nữ sinh vô tội.* | — | — | |
| 4-13 | `4.04#7` (8,9 s) | D | T1 | `t11_triumphant_smile_deal_with_devil`, `pan` | *Ngay khi thông tin rò rỉ, dư luận và báo chí Canada đã cay đắng gọi bản án ấy bằng một cái tên đầy phẫn uất: “Thỏa thuận với Quỷ dữ”.* | — | — | |
| 4-14 | `4.04#8` (6,4 s) | D | T1 | `t11_triumphant_smile_deal_with_devil`, `pull` | *Karla Homolka bình thản bước vào trại giam với nụ cười kín đáo, tin rằng mình đã chiến thắng hệ thống pháp luật.* | — | →H | |
| 4-15 | `4.06#1` (11,5 s) | H | T1 | `t11_pleading_victim_tears`, `still` | *Tại sao Karla Homolka lại khóc lóc nức nở trước các điều tra viên và tỏ ra ăn năn đến xé lòng khi ký bản thỏa thuận nhận tội năm 1993?* | — | — | |
| 4-16 | `4.06#2`–`#3` (5,8 s) | H | T1 | `t11_silent_interview_corridor`, `pan` | *Điều gì thực sự đã diễn ra bên trong tâm trí người đàn bà này? Tại sao lại hối hận?* | — | — | |
| 4-17 | `4.06#4` (8,0 s) | H | T1 | `t11_victim_playing_camouflage_mirror`, `pull` | *Đó là sự thức tỉnh lương tri của một nạn nhân bị bạo hành, hay là một màn kịch thao túng tâm lý lạnh lùng nhất lịch sử tư pháp?* | — | — | |
| 4-18 | `4.06#5` (3,6 s) | H | T1 | `t11_two_dossier_folders_desk`, `push` | *Bản chất của cơ chế tâm lý ở đây là gì, thưa chuyên gia?* | — | →C | |
| 4-19 | `4.07#1`–`#2` (9,2 s) | C | T1 | `t11_moral_licence_blank_notes`, `still` | *Đây chính là bài toán hóc búa nhất của tâm lý học pháp y. Chúng ta phải phân định rạch ròi giữa hai khái niệm: Hối hận Chân thực và Thao túng Đóng vai Nạn nhân.* | — | — | |
| 4-20 | `4.07#3` (9,6 s) | C | T1 | `t11_folded_coat_empty_chair`, `pan` | *Ở những vụ án khác, người đồng phạm khi thoát khỏi kẻ thao túng thường trải qua Chấn thương Đạo đức – họ suy sụp vì ghê tởm hành vi của chính mình và chấp nhận sự trừng phạt của pháp luật.* | — | — | |
| 4-21 | `4.07#4` (7,5 s) | C | T1 | `t11_blind_adoration_shadow`, `pull` | *Nhưng ở Karla Homolka, các chuyên gia hành vi nhận diện đây là một ca lâm sàng điển hình của Thái nhân cách Nữ giới kết hợp Ái kỷ Ác tính.* | — | — | |
| 4-22 | `4.07#5` (8,1 s) | C | T1 | `t11_contract_table_shadow`, `push` | *Những giọt nước mắt của cô ta tại bàn đàm phán năm 1993 hoàn toàn không phải khóc cho sinh mệnh của Tammy, Leslie hay Kristen.* | — | — | |
| 4-23 | `4.07#6` (9,5 s) | C | T1 | `t11_untitled_letter_desk`, `still` | *Đó là Sự Tự thương hại Bệnh lý – cô ta khóc vì nỗi sợ hãi bản thân phải đối diện với án tù chung thân sau khi trận đòn bằng đèn pin của Paul làm sụp đổ ảo tưởng tình yêu.* | — | — | |
| 4-24 | `4.07#7` (7,0 s) | C | T1 | `t11_sealed_document_folder`, `pan` | *Cô ta nắm bắt rất nhanh điểm yếu của hệ thống tư pháp: Xã hội luôn sẵn lòng bao dung cho một người phụ nữ trẻ đẹp mang vết thương thể xác.* | — | — | |
| 4-25 | `4.07#8` (7,6 s) | C | T1 | `t11_testimony_figure_shadow`, `pull` | *Bằng cách khoác lên mình chiếc áo Hội chứng Người phụ nữ bị Bạo hành, cô ta đã biến toàn bộ hành vi đồng lõa chủ động thành sự cưỡng bức không thể chống cự.* | — | — | |
| 4-26 | `4.07#9` (5,6 s) | C | T1 | `t11_calendar_counting_to_freedom`, `push` | *Sự hối hận của Karla chỉ là một nước cờ toan tính để mua lấy chiếc vé tự do với cái giá mười hai năm tù.* | — | →D | |
| 4-27 | `4.08#1` (6,0 s) | D | T1 | `t11_two_dossier_folders_desk`, `still` | *Và bi kịch tư pháp ấy càng trở nên nghiệt ngã hơn bởi sự giằng xé lương tâm của những người nắm giữ sự thật.* | — | — | |
| 4-28 | `4.08#2` (9,7 s) | D | T1 | `t11_six_tapes_on_floor`, `pan` | *Khi luật sư Ken Murray tìm thấy sáu cuốn băng trên trần nhà vào tháng 5 năm 1993, ông đã rơi vào một chiếc bẫy đạo đức nghề nghiệp khủng khiếp.* | — | — | |
| 4-29 | `4.08#3` (10,0 s) | D | T1 | `t11_silent_interview_corridor`, `pull` | *Một bên là đặc quyền bảo mật giữa luật sư và thân chủ, một bên là lương tri con người khi chứng kiến một kẻ đồng phạm máu lạnh đang dắt mũi toàn bộ cơ quan công tố.* | — | — | |
| 4-30 | `4.08#4` (7,6 s) | D | T1 | `t11_ken_murray_obstruction_charge`, `push` | *Việc ông cất giấu sáu cuốn băng suốt mười bảy tháng trong két sắt đã vô tình tạo điều kiện cho bản Thỏa thuận với Quỷ dữ được đóng dấu phê chuẩn.* | — | — | |
| 4-31 | `4.08#5` (10,9 s) | D | T1 | `t11_closed_dossier_desk`, `still` | *Đó là bài học cay đắng cho thấy: Khi các quy tắc kỹ thuật của luật pháp bị ngắt kết nối khỏi lương tri và sự thật khách quan, công lý sẽ trở thành nạn nhân của chính những kẻ thủ ác.* | — | →H | |
| 4-32 | `4.09#1` (6,1 s) | H | T1 | `t11_gavel_dark_bench`, `still` | *Thỏa thuận đã được tòa án phê chuẩn và bản án 12 năm đã chính thức có hiệu lực pháp lý.* | — | — | |
| 4-33 | `4.09#2` (4,9 s) | H | T1 | `t11_gavel_dark_bench`, `push` | *Karla trở thành nhân chứng vàng của cơ quan công tố trong phiên tòa xét xử người chồng cũ.* | — | — | |
| 4-34 | `4.09#3` (6,5 s) | H | T1 | `t11_six_8mm_tapes_bag`, `pan` | *Thế nhưng, số phận đã sắp đặt một bước ngoặt nghiệt ngã phơi bày toàn bộ sự thật đen tối ra trước ánh sáng.* | — | — | |
| 4-35 | `4.09#4` (13,8 s) | H | T1 | `t11_six_8mm_tapes_bag`, `pull` | *Mùa thu năm 1994, trong khi Paul Bernardo đang bị biệt giam chờ ngày xét xử, luật sư mới của hắn là ông John Rosen đã bàn giao cho cảnh sát một bọc tang vật chấn động.* | — | — | |
| 4-36 | `4.09#5` (6,8 s) | H | T1 | `t11_six_tapes_on_floor`, `still` | *Đó là 6 cuốn băng video ghi hình bí mật được tìm thấy ngay trong ngôi nhà số 57 Bayview Drive.* | — | →D | |
| 4-37 | `4.10#1` (7,0 s) | D | T1 | `t11_bathroom_ceiling_vent_hiding`, `push` | *Sáu cuốn băng định mệnh này trước đó đã được Paul Bernardo giấu kín phía sau chiếc hộp đèn gắn trên trần phòng tắm của ngôi nhà.* | — | — | |
| 4-38 | `4.10#2` (11,6 s) | D | T1 | `t11_bathroom_ceiling_vent_hiding`, `pan` | *Luật sư ban đầu của Paul là Ken Murray đã tìm thấy chúng từ tháng 5 năm 1993 nhưng đã bí mật cất giấu suốt 17 tháng vì lo ngại chúng sẽ hủy hoại thân chủ mình.* | — | — | |
| 4-39 | `4.10#3` (6,1 s) | D | T1 | `t11_ken_murray_obstruction_charge`, `pull` | *Chỉ khi Paul Bernardo quyết định thay đổi luật sư bào chữa, những cuốn băng này mới được giao nộp cho cơ quan điều tra.* | — | — | |
| 4-40 | `4.10#4` (6,6 s) | D | T1 | `t11_ken_murray_obstruction_charge`, `still` | *Khi chiếc máy chiếu được bật lên trong căn phòng họp kín của cơ quan công tố, toàn bộ không gian rơi vào một sự câm lặng kinh hoàng.* | — | — | |
| 4-41 | `4.10#5` (6,1 s) | D | T1 | `t11_dark_screening_room_projector`, `push` | *Những gì hiện lên trên màn hình đã đánh sập hoàn toàn vở kịch dối trá mà Karla Homolka dày công dàn dựng.* | — | — | |
| 4-42 | `4.10#6` (4,1 s) | D | T1 | `t11_dark_screening_room_projector`, `pan` | *Hãy lắng nghe nỗi uất nghẹn của những người từng tin vào sự vô tội của cô ta.* | — | →N2 | |
| 4-43 | `4.11#1` (6,9 s) | N2 | T1 | `t11_investigator_nausea_monitor`, `pull` | *Hãy hình dung cảm giác cay đắng tột cùng của những người làm công tố khi ngồi trong căn phòng tối ngày hôm đó.* | — | ✦ Mèo | |
| 4-44 | `4.11#2` (5,3 s) | N2 | T1 | `t11_investigator_nausea_monitor`, `still` | *Chúng tôi từng tin vào những giọt nước mắt của một người phụ nữ run rẩy nói rằng mình bị ép buộc.* | — | — | |
| 4-45 | `4.11#3` (8,7 s) | N2 | T1 | `t11_spinning_tape_reels`, `push` | *Nhưng những cuốn băng cho thấy Karla tham gia một cách chủ động, thậm chí cười đùa và đưa ra những chỉ dẫn lạnh lùng cho Paul.* | — | — | |
| 4-46 | `4.11#4` (6,2 s) | N2 | T1 | `t11_spinning_tape_reels`, `pan` | *Cô ta không hề bị đe dọa, cô ta là một kẻ đồng lõa tàn nhẫn và say mê với tội ác.* | — | — | |
| 4-47 | `4.11#5` (5,4 s) | N2 | T1 | `t11_contract_table_shadow`, `pull` | *Giây phút ấy, chúng tôi hiểu rằng mình đã ký một bản hợp đồng nhượng bộ với chính quỷ dữ.* | — | →C | |
| 4-48 | `4.13#1` (4,2 s) | C | T1 | `t11_obedient_accomplice_strings`, `still` | *Sáu cuốn băng trên trần nhà chính là sự sụp đổ hoàn toàn của chiếc mặt nạ nạn nhân.* | — | — | |
| 4-49 | `4.13#2` (6,6 s) | C | T1 | `t11_obedient_accomplice_strings`, `push` | *Về mặt tâm lý học hành vi, Karla Homolka đã thực hiện một chiến lược “Thao túng đóng vai nạn nhân” ở cấp độ thượng thừa.* | — | — | |
| 4-50 | `4.13#3` (7,8 s) | C | T1 | `t11_idealised_portrait_dark`, `pan` | *Cô ta hiểu rất rõ điểm mù lớn nhất của lòng trắc ẩn con người: xã hội thường mặc định phụ nữ trẻ đẹp luôn là nạn nhân chứ không thể là kẻ chủ mưu tàn ác.* | — | — | |
| 4-51 | `4.13#4` (8,8 s) | C | T1 | `t11_mockery_of_justice_tears`, `pull` | *Bằng cách lợi dụng vụ việc do Paul gây ra vào tháng 1 năm 1993, cô ta đã khéo léo biến toàn bộ quá khứ của mình thành hệ quả của sự cưỡng ép.* | — | — | |
| 4-52 | `4.13#5` (6,8 s) | C | T1 | `t11_mockery_of_justice_tears`, `still` | *Nhưng những thước phim chân thực đã bóc trần sự thật: cô ta không hề chịu sự tê liệt nhận thức của “Hội chứng Người phụ nữ bị Bạo hành”.* | — | — | |
| 4-53 | `4.13#6` (6,1 s) | C | T1 | `t11_composure_in_mirror`, `push` | *Karla hoàn toàn tỉnh táo, có năng lực phán đoán và thể hiện sự thỏa mãn quyền lực tàn bạo khi chà đạp lên đồng loại.* | — | — | |
| 4-54 | `4.13#7` (5,8 s) | C | T1 | `t11_fragile_beauty_manipulation`, `pan` | *Đó không phải là nỗi sợ hãi, mà là sự tính toán lạnh lùng của một nhân cách thái nhân cách ngụy trang hoàn hảo.* | — | — | |
| 4-55 | `4.13#8` (4,9 s) | C | T1 | `t11_fragile_beauty_manipulation`, `pull` | *Nước mắt của cô ta chỉ là công cụ để mua chuộc lòng thương hại và trốn tránh bản án chung thân.* | — | →H | |
| 4-56 | `4.14#1` (7,4 s) | H | T1 | `t11_outraged_citizens_protest`, `still` | *Một làn sóng thịnh nộ dữ dội chưa từng có bùng nổ khắp đất nước Canada khi thông tin về những cuốn băng bị rò rỉ.* | — | — | |
| 4-57 | `4.14#2` (9,5 s) | H | T1 | `t11_outraged_citizens_protest`, `push` | *Hàng trăm ngàn người dân đã ký tên vào các bản kiến nghị đòi hủy bỏ thỏa thuận nhận tội và truy tố Karla Homolka tội giết người cấp độ một.* | — | — | |
| 4-58 | `4.14#3` (7,0 s) | H | T1 | `t11_constitutional_legal_deadlock`, `pan` | *Thế nhưng, nền tư pháp Canada lúc bấy giờ đã rơi vào một cái bẫy pháp lý bế tắc do chính mình tạo ra.* | — | — | |
| 4-59 | `4.14#4` (12,0 s) | H | T1 | `t11_constitutional_legal_deadlock`, `pull` | *Theo nguyên tắc bảo vệ quyền tố tụng và các điều khoản miễn trừ đã được tòa án đóng dấu, cơ quan công tố không thể đơn phương xé bỏ bản thỏa thuận khi Karla không vi phạm lời khai.* | — | — | |
| 4-60 | `4.14#5` (6,5 s) | H | T1 | `t11_steel_gate_brick_wall`, `still` | *Bản án 12 năm tù của người đàn bà trong ngôi nhà màu hồng vẫn được pháp luật bảo vệ nguyên vẹn.* | — | — | |
| 4-61 | `4.14#6` (8,0 s) | H | T1 | `t11_dangerous_offender_life_sentence`, `push` | *Trong khi đó, ngày 1 tháng 9 năm 1995, Paul Bernardo chính thức nhận phán quyết cuối cùng của công lý.* | — | — | |
| 4-62 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *HỒI 05* · **PHÁN QUYẾT, DI CHỨNG TƯ PHÁP & BÀI HỌC CẢNH BÁO ĐỎ** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT, DI CHỨNG TƯ PHÁP & BÀI HỌC CẢNH BÁO ĐỎ

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (10,6 s) | H | T1 | `t11_dangerous_offender_life_sentence`, `pan` | *Ngày 1 tháng 9 năm 1995, tại Tòa án Cấp cao Ontario, phiên tòa kéo dài làm rúng động dư luận quốc tế đã chính thức đi đến hồi kết.* | — | — | |
| 5-02 | `5.02#2` (11,8 s) | H | T1 | `t11_prison_cell_stone_dark`, `pull` | *Bồi thẩm đoàn chính thức tuyên Paul Bernardo phạm tội Giết người cấp độ một đối với Leslie Mahaffy và Kristen French, cùng hàng loạt tội danh bắt cóc và tấn công nghiêm trọng.* | — | — | |
| 5-03 | `5.02#3` (6,5 s) | H | T1 | `t11_prison_cell_stone_dark`, `still` | *Thẩm phán tuyên phạt Paul Bernardo mức án tù chung thân không ân xá trong ít nhất 25 năm.* | — | — | |
| 5-04 | `5.02#4` (8,1 s) | H | T1 | `t11_thick_concrete_wall`, `push` | *Đặc biệt, tòa án đã gắn cho hắn nhãn “Tội phạm Nguy hiểm” — một chỉ định pháp lý nghiêm khắc bậc nhất của luật hình sự Canada.* | — | — | |
| 5-05 | `5.02#5` (9,1 s) | H | T1 | `t11_thick_concrete_wall`, `pan` | *Chỉ định này đồng nghĩa với việc hắn sẽ bị giam giữ vô thời hạn trong các trại giam an ninh tối đa như Kingston và Millhaven cho đến ngày qua đời.* | — | — | |
| 5-06 | `5.02#6` (5,7 s) | H | T1 | `t11_steel_wall_lifeless`, `pull` | *Hắn bị tước bỏ mọi cơ hội tái hòa nhập cộng đồng và vĩnh viễn sống sau bức tường thép dày đặc.* | — | — | |
| 5-07 | `5.02#7` (8,3 s) | H | T1 | `t11_calendar_counting_to_freedom`, `still` | *Thế nhưng đối với người đàn bà đã đồng lõa tước đoạt sinh mạng của những đứa trẻ, cánh cửa tự do lại hé mở sau đúng một thập kỷ.* | — | — | |
| 5-08 | `5.04#1` (10,2 s) | H | T1 | `t11_christmas_snow_front_porch`, `pan` | *Nhưng ngay cả khi bản hợp đồng tư pháp cay đắng ấy không thể đảo ngược, sức mạnh của tình phụ tử và mẫu tử thiêng liêng đã viết nên một trang sử quật cường.* | — | — | |
| 5-09 | `5.04#2` (7,3 s) | H | T1 | `t11_grieving_parents_wedding_mask`, `pull` | *Ông bà Doug và Donna French – cha mẹ của nữ sinh Kristen French – đã không gục ngã trước nỗi đau xé lòng.* | — | — | |
| 5-10 | `5.04#3` (10,1 s) | H | T1 | `t11_gavel_dark_bench`, `push` | *Họ đã kiên cường đứng lên, biến nỗi mất mát tột cùng thành một cuộc chiến pháp lý bền bỉ để bảo vệ phẩm giá cho con gái mình và tất cả các nạn nhân.* | — | — | |
| 5-11 | `5.04#4` (10,5 s) | H | T1 | `t11_empty_evidence_box`, `still` | *Họ đã đấu tranh đến cùng để niêm phong và tiêu hủy vĩnh viễn những cuốn băng tang vật, kiên quyết không để nỗi đau của các em bị biến thành thứ giải trí tò mò của dư luận.* | — | — | |
| 5-12 | `5.04#5` (12,0 s) | H | T1 | `t11_backyard_barbecue_lawn`, `pan` | *Đồng thời, sự ra đời của Trung tâm Bảo trợ Trẻ em mang tên Kristen French tại vùng Niagara đã trở thành mái ấm chữa lành cho hàng ngàn đứa trẻ tổn thương suốt nhiều thập kỷ qua.* | — | — | |
| 5-13 | `5.04#6` (4,8 s) | H | T1 | `t11_neighbourhood_winter_evening`, `pull` | *Đó là sự chiến thắng vĩ đại của tình yêu thương trước bóng tối của sự hủy diệt.* | — | →D | |
| 5-14 | `5.05#1` (10,4 s) | D | T1 | `t11_joliette_prison_gate_release`, `push` | *Ngày 4 tháng 7 năm 2005, sau khi chấp hành trọn vẹn 12 năm tù giam, Karla Homolka chính thức bước qua cánh cổng nhà tù ở tuổi 35.* | — | — | |
| 5-15 | `5.05#2` (5,8 s) | D | T1 | `t11_joliette_prison_gate_release`, `pan` | *Sự kiện này đã thổi bùng một cơn bão biểu tình và sự phẫn nộ dữ dội trên khắp các đường phố Canada.* | — | — | |
| 5-16 | `5.05#3` (9,4 s) | D | T1 | `t11_blank_photographs_in_hands`, `pull` | *Các bậc phụ huynh và gia đình nạn nhân mang theo di ảnh của Leslie Mahaffy và Kristen French, giăng biểu ngữ phản đối sự bất công của thỏa thuận tư pháp.* | — | — | |
| 5-17 | `5.05#4` (9,8 s) | D | T1 | `t11_haunted_new_identity_shadow`, `still` | *Để có thể tồn tại, Karla Homolka phải đổi tên thành Leanne Bordelais, trốn chạy sang vùng biển Caribbean rồi quay về một thị trấn nhỏ ở tỉnh Quebec.* | — | — | |
| 5-18 | `5.05#5` (7,4 s) | D | T1 | `t11_haunted_new_identity_shadow`, `push` | *Nhưng bất cứ nơi nào dấu vết của cô ta bị phát hiện, làn sóng tẩy chay và phẫn nộ của cộng đồng lại bùng phát mạnh mẽ.* | — | — | |
| 5-19 | `5.05#6` (6,9 s) | D | T1 | `t11_galligan_inquiry_report_reforms`, `pan` | *Về mặt pháp lý, vụ án này đã thúc đẩy chính quyền tỉnh Ontario tiến hành hai cuộc điều tra độc lập mang tính lịch sử.* | — | — | |
| 5-20 | `5.05#7` (8,4 s) | D | T1 | `t11_galligan_inquiry_report_reforms`, `pull` | *Báo cáo của cựu Thẩm phán Patrick Galligan đã mổ xẻ toàn diện quy trình công tố và những thiếu sót chí mạng trong việc ký kết thỏa thuận nhận tội.* | — | — | |
| 5-21 | `5.05#8` (12,9 s) | D | T1 | `t11_police_archive_shelves`, `still` | *Trong khi đó, Báo cáo mang tính bước ngoặt của Thẩm phán Archie Campbell đã chỉ ra sự tắc nghẽn thông tin giữa các sở cảnh sát, dẫn tới cuộc đại cải tổ hệ thống phân tích liên kết tội phạm bạo lực ViCLAS trên toàn quốc.* | — | — | |
| 5-22 | `5.05#9` (5,5 s) | D | T1 | `t11_police_archive_shelves`, `push` | *Đó là những cải cách tư pháp đắt giá được đánh đổi bằng nỗi đau tột cùng của các gia đình nạn nhân.* | — | →C | |
| 5-23 | `5.07#1` (12,9 s) | C | T1 | `t11_steel_gate_brick_wall`, `push` | *Ngày 4 tháng 7 năm 2005, khi Karla Homolka mãn hạn mười hai năm tù và bước ra ngoài ánh sáng, cô ta có thể đã chiến thắng về mặt kỹ thuật pháp lý, nhưng đã vĩnh viễn thua cuộc trước Tòa án Lương tâm của Nhân loại.* | — | — | |
| 5-24 | `5.07#2` (4,1 s) | C | T1 | `t11_outraged_citizens_protest`, `still` | *Hàng ngàn người dân Canada đã xuống đường biểu tình trong sự căm phẫn tột độ.* | — | — | |
| 5-25 | `5.07#3` (5,4 s) | C | T1 | `t11_closed_pink_door_abyss`, `pan` | *Bản án thể xác kết thúc, nhưng bản án cô lập xã hội sẽ theo đuổi cô ta đến tận hơi thở cuối cùng.* | — | — | |
| 5-26 | `5.07#4` (8,5 s) | C | T1 | `t11_haunted_new_identity_shadow`, `pull` | *Dù có đổi tên thành Leanne Bordelais, dù có trốn chạy sang những hòn đảo xa xôi ở Caribbean, cái bóng của tội ác và sự giả trá vẫn luôn đuổi kịp cô ta.* | — | — | |
| 5-27 | `5.07#5` (9,9 s) | C | T1 | `t11_idealised_portrait_dark`, `push` | *Cộng đồng xã hội đã gửi đi một thông điệp đanh thép: Con người có thể bị đánh lừa bởi những giọt nước mắt đóng kịch, nhưng thời gian và sự thật sẽ luôn đòi lại phẩm giá cho những linh hồn vô tội.* | — | — | |
| 5-28 | `5.07#6` (5,8 s) | C | T1 | `t11_empty_auditorium_dust`, `still` | *Lương tri của xã hội không bao giờ tha thứ cho một kẻ đã tước đoạt sinh mệnh của đồng loại nhân danh sự ích kỷ cá nhân.* | — | — | |
| 5-29 | `5.07#7` (9,4 s) | C | T1 | `t11_empty_auditorium_dust`, `pan` | *Xét trên bình diện tâm lý học, bản án thể xác 12 năm của Karla Homolka có thể đã kết thúc, nhưng bản án tâm lý xã hội thì vĩnh viễn không bao giờ xóa bỏ.* | — | — | |
| 5-30 | `5.07#8` (8,5 s) | C | T1 | `t11_empty_auditorium_dust`, `pull` | *Karla không hề biểu lộ sự ăn năn hối cải chân chính; thái độ của cô ta chỉ là sự tự thương hại bệnh lý và nỗ lực bảo vệ quyền lợi cá nhân đến cùng.* | — | — | |
| 5-31 | `5.07#9` (9,2 s) | C | T1 | `t11_untitled_letter_desk`, `still` | *Trong khi đó, Paul Bernardo trong trại giam Millhaven liên tục nộp đơn xin ân xá trong vô vọng, đổ lỗi cho người khác trong một trạng thái sụp đổ cái tôi ái kỷ kéo dài.* | — | — | |
| 5-32 | `5.07#10` (5,6 s) | C | T1 | `t11_disguised_predator_scales`, `push` | *Vụ án này để lại một bài học kinh điển cho nhân loại về việc cảnh giác trước những chiếc mặt nạ đạo đức giả.* | — | — | |
| 5-33 | `5.07#11` (7,4 s) | C | T1 | `t11_disguised_predator_scales`, `pan` | *Chúng ta phải học cách phân định rạch ròi giữa một nạn nhân thực sự chịu tổn thương và một kẻ săn mồi khoác áo nạn nhân để trốn tránh trách nhiệm.* | — | — | |
| 5-34 | `5.07#12` (9,8 s) | C | T1 | `t11_delicate_paper_ornament`, `pull` | *Sự tàn bạo lộ liễu của Paul Bernardo rất dễ nhận diện, nhưng sự nguy hiểm ngụy trang dưới vỏ bọc mong manh của Karla Homolka mới là thứ đánh lừa được cả hệ thống tư pháp tinh vi nhất.* | — | — | |
| 5-35 | `5.07#13` (7,1 s) | C | T1 | `t11_delicate_paper_ornament`, `still` | *Lòng trắc ẩn là phẩm giá cao quý của con người, nhưng lòng trắc ẩn thiếu sự tỉnh táo sẽ trở thành mảnh đất màu mỡ cho tội ác thao túng.* | — | — | |
| 5-36 | `5.07#14` (5,0 s) | C | T1 | `t11_community_shield_circle`, `push` | *Kẻ thủ ác luôn biết cách biến chính lòng tốt của cộng đồng thành tấm khiên che chở cho tội lỗi của chúng.* | — | — | |
| 5-37 | `5.07#15` (5,7 s) | C | T1 | `t11_community_shield_circle`, `pan` | *Để bảo vệ bản thân và những người thân yêu, việc nhận diện các tín hiệu cảnh báo đỏ sinh tồn là vô cùng cấp thiết.* | — | →H | |
| 5-38 | `5.08#1` (9,5 s) | H | T1 | `t11_four_warning_lights`, `pull` | *Để giúp quý vị khán giả có thêm những công cụ bảo vệ thực tế, kênh Amber eyes xin đúc kết 4 tín hiệu cảnh báo đỏ sinh tồn từ hồ sơ lịch sử này.* | — | — | |
| 5-39 | `5.08#2` (4,4 s) | H | T8 cờ | `t11_redflag1_evading_accountability`, `still` | *01* · **CẢNH BÁO ĐỎ THỨ NHẤT: CẢNH GIÁC TRƯỚC KẺ LẠM DỤNG SỰ TỔN THƯƠNG CÁ NHÂN.** | — | — | |
| 5-40 | `5.08#3` (15,2 s) | H | T1 | `t11_redflag1_evading_accountability`, `push` | *Những kẻ thao túng luôn nhắc về những vết thương hay bất hạnh trong quá khứ để biện minh cho hành vi sai trái ở hiện tại; người thực sự có lương tri sẽ nhận trách nhiệm và xót thương nạn nhân, thay vì chỉ chăm chăm đóng vai người bị hại.* | — | — | |
| 5-41 | `5.08#4` (5,3 s) | H | T8 cờ | `t11_redflag2_words_vs_actions_split`, `pan` | *02* · **CẢNH BÁO ĐỎ THỨ HAI: SỰ BẤT NHẤT GIỮA LỜI NÓI ĐẠO ĐỨC VÀ HÀNH VI SAU LƯNG.** | — | — | |
| 5-42 | `5.08#5` (8,7 s) | H | T1 | `t11_redflag2_words_vs_actions_split`, `pull` | *Hãy luôn đánh giá một con người dựa trên chuỗi hành động thực tế, không dựa vào vẻ bề ngoài xinh đẹp hay những lời nói hoa mỹ trước đám đông.* | — | — | |
| 5-43 | `5.08#6` (5,6 s) | H | T8 cờ | `t11_redflag3_guilt_tripping_trap`, `still` | *03* · **CẢNH BÁO ĐỎ THỨ BA: CẢNH GIÁC TRƯỚC SỰ TIẾP CẬN CỦA NHỮNG NGƯỜI CÓ VẺ NGOÀI VÔ HẠI.** | — | — | |
| 5-44 | `5.08#7` (11,2 s) | H | T1 | `t11_redflag3_guilt_tripping_trap`, `push` | *Karla Homolka đã trực tiếp dùng nụ cười thân thiện để hỏi đường và dụ dỗ nạn nhân vào bẫy; sự cảnh giác không được phép lơ là trước bất kỳ ai ở nơi công cộng.* | — | — | |
| 5-45 | `5.08#8` (4,8 s) | H | T8 cờ | `t11_redflag4_toxic_symbiosis_abyss`, `pan` | *04* · **CẢNH BÁO ĐỎ THỨ TƯ: NHẬN DIỆN NHỮNG MỐI QUAN HỆ CỘNG SINH ĐỘC HẠI.** | — | — | |
| 5-46 | `5.08#9` (8,3 s) | H | T1 | `t11_redflag4_toxic_symbiosis_abyss`, `pull` | *Một tình cảm chân chính không bao giờ đòi hỏi bạn phải xâm phạm ranh giới đạo đức hay làm hại người khác để chứng minh sự gắn kết.* | — | — | |
| 5-47 | `5.08#10` (9,4 s) | H | T1 | `t11_noose_shadow_wall`, `still` | *Khi ai đó yêu cầu bạn bước qua lằn ranh lương tâm nhân danh lòng trung thành, đó không phải là tình yêu mà là chiếc thòng lọng dẫn xuống vực thẳm.* | — | — | |
| 5-48 | `5.08#11` (6,3 s) | H | T1 | `t11_light_of_justice_prevails`, `push` | *Hãy luôn lắng nghe trực giác bất an bên trong bạn, bởi trực giác chính là chiếc chuông báo động sớm nhạy bén nhất.* | — | — | |
| 5-49 | `5.08#12` (4,8 s) | H | T1 | `t11_light_of_justice_prevails`, `pan` | *Đừng bao giờ hợp lý hóa hay bỏ qua những bước lấn ranh giới nhỏ nhặt ban đầu.* | — | — | |
| 5-50 | `5.10#1` (9,5 s) | H | T1 | `t11_closing_dossier_stamp`, `pull` | *Hồ sơ Paul Bernardo và Karla Homolka khép lại như một hồi chuông cảnh tỉnh lạnh lùng về những góc khuất khôn lường của tâm trí con người.* | — | — | |
| 5-51 | `5.10#2` (10,6 s) | H | T8 cờ | `t11_closing_dossier_stamp`, `still` | *Chiếc mặt nạ búp bê “Ken và Barbie” lộng lẫy đã vỡ vụn, để lại bài học đau xót về cái giá của sự ngộ nhận và lòng trắc ẩn bị đặt sai chỗ.* | — | — | |
| 5-52 | `5.10#3` (11,3 s) | H | T1 | `t11_hope_candles_dark_room`, `push` | *Dù thỏa thuận tư pháp có những giới hạn của thời đại, nhưng ánh sáng của lương tri lịch sử đã trả lại phẩm giá cho các nạn nhân vô tội và vạch trần chân tướng của tội ác.* | — | — | |
| 5-53 | `5.10#4` (9,0 s) | H | T8 cờ | `t11_hope_candles_dark_room`, `pan` | *Xin hãy luôn nhớ rằng: sự an toàn của chúng ta bắt đầu từ việc biết tôn trọng trực giác và dũng cảm bảo vệ những ranh giới đạo đức sống còn.* | — | — | |
| 5-54 | `5.10#5` (6,1 s) | H | T1 | `t11_empty_stage_spotlight`, `pull` | *Cảm ơn các khách mời chuyên gia đã đồng hành cùng Amber eyes trong ca phẫu thuật tâm lý học đầy kịch tính hôm nay.* | — | — | |
| 5-55 | `5.10#6` (3,8 s) | H | T8 cờ | `t11_empty_stage_spotlight`, `still` | *Cảm ơn quý vị khán giả đã lắng nghe và chia sẻ thông điệp thức tỉnh này.* | — | — | |
| 5-56 | `5.10#7` (4,7 s) | H | T1 | `t11_control_room_dark_monitors`, `push` | *Hãy bấm đăng ký kênh và để lại góc nhìn của bạn ở phần bình luận bên dưới.* | — | — | |
| 5-57 | `5.10#8` (4,1 s) | H | T8 cờ | `t11_control_room_dark_monitors`, `pan` | *Xin chào và hẹn gặp lại quý vị trong những tập hồ sơ tiếp theo.* | — | — | |
| 5-58 | `5.10#9` (4,1 s) | H | T1 | `t11_quiet_window_closing`, `pull` | *Chúc quý vị luôn giữ được sự an yên và sáng suốt trong cuộc sống.* | — | — | |
| 5-59 | hết tập (0,0 s) | — | T2 | `t11_closing_card_dossier`, `still` | **HỒ SƠ TẬP 11 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | — | ⊘ | ◼ |

**Tổng:** 275 dòng · 272 câu · 5 hồi · bảng lập lại 16/11/2026 theo timeline 272 câu (kịch bản 13/11); nền mới 31 mã (`.work/_t11v2/scenes.py`). Nền t11_* dùng chung 100% 3 ngôn ngữ.
