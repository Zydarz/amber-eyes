# HỒ SƠ SẢN XUẤT TẬP 02 · BẢN TIẾNG ANH · "THE TWO-FACED COLONEL" (PHẦN B)

> **TRẠNG THÁI: XONG (25/10/2026 — Director's Cut)** → xuat_ban/Tap02_EN_master.mp4 (27:54,60 · 1920×1080@30 · H.264+AAC · 595.720.561 byte) · **QC A9.1–A9.4 đạt toàn bộ** (exit 0) · G10 đạt (5/5 vai 1 người).
> Chạy lại bất kỳ bước nào bằng `AE_LANG=en AE_EP=02 py -3 .work/<script>.py`; chạy cả chuỗi: `AE_LANG=en AE_EP=02 py -3 .work/_finish_tap02_en.py`.

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A), giống bản tiếng Việt.
**Kịch bản:** `01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md` · **Chữ cố định:** `CHU_CO_DINH_EN.md` · **Rà soát pháp lý Mỹ:** `REVIEW_EN.md` · **Thành phẩm (sau khi dựng):** `02_SAN_XUAT/Tap02_EN/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md`. File này **sao yên bản gốc** ở các cột Câu, Vai, Mẫu, Nền + bóng, Nhân vật và chuyển cảnh; chỉ thay:
- cột **Chữ** sang tiếng Anh (chữ hiện trên màn hình);
- các cụm `ở "…"` trong cột **Beat** sang cụm tiếng Anh **có thật** trong câu EN tương ứng.

Lời mô tả beat vẫn để tiếng Việt vì renderer dò từ khoá tiếng Việt trong đó (“Dấu”, “giả mạo”, “Thanh tiến trình”, `0/3`, “Cờ 1 tô đầy”…).

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md` — dịch từ `kichban_tap02_22102026.md`, **1 câu EN cho mỗi câu VN, mã câu trùng 100%** (63 phần tử · 215 câu · 36 lượt nói) |
| File parse | `.work/script_tap02_EN.json` |
| N1 / N2 | `1.07` Base personnel (Cừu) / `4.06` Case observer (Mèo) |
| Nền | **Dùng lại 37 ảnh `assets/bg/t2_*`** — không tạo ảnh mới (nền không chứa chữ đọc được) |
| Intro | `assets/brand/intro_kenh_EN_t02.mov` — dựng riêng cho Tập 02 EN (không dùng lại intro của Tập 01): thẻ A "ABOUT THIS DOCUMENTARY" + thẻ B "VIEWER DISCRETION & ADVISORY" theo đúng `CHU_CO_DINH_EN.md` §2, thẻ 1660×780, chữ 40 px, mỗi gạch đầu dòng tự xuống dòng. Đã dựng + soi 2 khung ✅ |
| Bảng shot | 151 dòng, giữ nguyên số hiệu shot; 134 dòng có chữ đã dịch, 17 dòng nghỉ |
| Tên hồi (EN) | Act 1 · The Extreme Contrast Behind a Colonel's Rank · Act 2 · The Scene & Dossier — The 4 Stages of the Abyss · Act 3 · Psychological Autopsy — Inside the Mind of a Two-Faced Predator · Act 4 · The Interrogation Room — Breaking a Military Mind · Act 5 · The Verdict, Red Flags & Closing Thoughts |
| Thumbnail | `THE TWO-FACED` / `COLONEL` |

## B2. Kết quả và việc còn lại

| Hạng mục | Kết quả |
|---|---|
| Kịch bản EN | Đã review theo chính sách YouTube US + pháp lý Mỹ/Canada (`REVIEW_EN.md`): 0 lỗi chính tả trên 3.536 từ; loại bỏ hoàn toàn nội dung tự sát; dùng thuật ngữ pháp lý chuẩn (*sexual assault*); thêm mệnh đề miễn trừ Milkovich ở `3.04#1–2` |
| Bảng shot EN | Xong. Tự kiểm bằng `.work/_build_plan_tap02_en.py`: **151/151 dòng đạt** — cụm beat EN có thật trong câu EN · trích dẫn nguyên văn (lược bằng `…`) · mọi số trên hình truy được về câu (kể cả số viết bằng chữ, tên tháng, nhãn thứ tự) |
| Cấu hình script | `.work/edition.py` → `EPISODES["02"]` có nhánh EN (`AE_LANG=en AE_EP=02`): thư mục `Tap02_EN`, master `Tap02_EN_master`, phụ đề `Tap02_EN.srt`, nhãn vai EN, thẻ cảnh báo EN, mô tả + hotline Mỹ |
| TTS | **215/215 câu EN đã đọc.** Vai D dùng giọng `English_Trustworth_Man` (thay `English_Deep-VoicedGentleman` của Tập 01 EN): đo bằng `.work/_voice_band_test.py` cho thấy **tốc độ đọc không làm đổi danh tính người, chỉ CẢM XÚC mới đổi** — G10 báo vai D "3 người" vì có câu `sad`/`fearful`; giọng mới giữ **SPEAKERS: 1** ở cả 4 cảm xúc. **G10 ĐẠT: cả 5 vai đều "1 người"** (`02_SAN_XUAT/Tap02_EN/thu_giong_kiem_vai/report.md`) |
| Diễn xuất | `.work/acting_tap02_EN.json` — 215 câu · 4 cảm xúc an toàn (neutral/sad/fearful/surprised) · **cao độ luôn = 0** · 6 bậc tốc độ (bậc lớn nhất 29%, không dồn như bản VN 51%) · 9 lời đọc riêng (chỉ thêm `<#0.35#>` sau dấu `:` đứng trước câu trích, **không đổi chữ**) · 70 khoảng lặng / 27,2 s (y hệt bản VN) |
| Âm thanh | **1723,5 s (28:43,47)** · 14 nền SFX + 37 tiếng động · lời đầu 23,0 s · hồi 1: 23,0–306,2 · 2: 308,2–570,1 · 3: 572,1–966,2 · 4: 968,2–1359,4 · 5: 1361,4–1714,5 s |
| Hình | `build_video3.py --workers 6` → 3365 s (56 phút) → `.work/video3_EN_t02/picture.mp4` (51.704 khung 1920×1080@30) |
| QC | **A9.1 · A9.2 · A9.3 · A9.4 — TẤT CẢ ĐẠT** (`EXIT=0`): lệch hình/tiếng **0,017 s** · giải mã mp4 **0 lỗi** · 0 khoảng câm > 0,3 s · loudness **−16,0 LUFS** · lời đầu 23,0 s · 151 khung giữa shot lấy từ chính mp4 thành phẩm → 10 contact sheet (`.work/qc_final_EN_t02/`) · phụ đề 425 cue, không trùng lặp |
| Phụ đề | `Tap02_EN.srt` — 425 cue, cue cuối kết thúc 1714,5 s |
| Gói đăng | `Tap02_EN_master.mp4` (578.017.179 byte) · `Tap02_EN_master.mp3` (41.364.908 byte) · `thumbnail.png` (THE TWO-FACED / COLONEL) · `mo_ta.txt` + `description.txt` (mốc chương 00:00 / 00:20 / 05:06 / 09:30 / 16:06 / 22:39 + hotline RAINN / Domestic Violence / VictimConnect / CRCVC / 911) · `nguon_tham_khao_EN.md` — **khung đã sinh**, cần điền link đã kiểm chứng |
| **Còn lại trước khi đăng** | ① Bạn xem toàn tập · ② Bổ sung nguồn gốc cho các dòng ⚠ trong `nguon_tham_khao_EN.md` · ③ Kiểm tra điều khoản thương mại công cụ AI · ④ Đánh dấu “Altered or synthetic content” khi đăng YouTube |

## 6. DANH SÁCH SHOT — TẬP 02 BẢN TIẾNG ANH (cùng cú pháp A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X (hiện badge chờ) · `✦` = lần đầu xuất hiện (thẻ giới thiệu) · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

<!--TABLE-->
## 6. DANH SÁCH SHOT — TẬP 02 (viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### HỒI 1 — SỰ TƯƠNG PHẢN CỰC ĐẠI PHÍA SAU QUÂN HÀM ĐẠI TÁ · nền chủ đạo `t2_base_trenton`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s) | — | T1 | `t2_town_snow` hiện dần từ đen | *ACT 01 · THE EXTREME CONTRAST BEHIND A COLONEL'S RANK* | Tiếng phản lực tụt thành drone; kim đồng hồ | ⊘ | |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t2_base_trenton` | **07 · 2009** · *Canadian Forces Base Trenton — the largest air force base in the Canadian military* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T1 | `t2_oath_hall` | **THE CHANGE-OF-COMMAND CEREMONY** · *Before high-ranking military dignitaries* | — | | |
| 1-03 | `1.03#4` | H | T2 | `t2_oath_hall`, `still` | *ASSUMING SUPREME COMMAND* · **COLONEL DAVID RUSSELL WILLIAMS** · *A service record so spotless* | Dấu mộc ở "spotless" | | |
| 1-04 | `1.04` (nghỉ 1,5 s) | — | — | giữ 1-03 | — | — | | |
| 1-05 | `1.05#1` | H | T5 | `t2_base_trenton` | **46 YEARS OLD** · *Piloted VIP transports for Queen Elizabeth II and the Prime Minister of Canada* | Số đếm | | |
| 1-06 | `1.05#2` | H | T8 | `t2_base_trenton` mờ | *An exemplar of iron discipline · A model husband · Wife: associate director at the Heart and Stroke Foundation of Canada* | Mỗi mục ở cụm từ | | |
| 1-07 | `1.05#3` | H | T1 | `t2_base_trenton`, `pull` | *IMAGINE:* **THOSE WHO SERVED UNDER HIS COMMAND** | — | →N1 | |
| 1-08 | `1.07#1` | N1 | T4 lời kể | `t2_base_trenton` ấm, mờ | “…the living embodiment of perfection.” | — | ✦ Cừu | |
| 1-09 | `1.07#2` | N1 | T8 | `t2_oath_hall` mờ | *Composed · Immaculate down to every crease on his uniform · Never raised his voice* → `#3`: *An authority radiating from pure intellect and precision* | Mỗi mục ở cụm từ | | |
| 1-10 | `1.07#3`–`#4` | N1 | T4 lời kể | `t2_base_trenton` ấm | “We stood beside one of the most dangerous predators alive, bowing our heads in unwavering respect.” | — | 🅑 | |
| 1-11 | `1.08#1` | H | T1 | `t2_town_snow`, `pan` | **THE DEAD OF NIGHT** · *Vanishing into the shadows of quiet suburban towns* | Tiêu đề ở "dead of night" | | |
| 1-12 | `1.08#2`–`#3` | H | T1 | `night_street`, `still` | *The commanding colonel no longer existed* → `#3`: **ONLY A PROWLER** | Tiêu đề ở "a prowler" | ⊘ | |
| 1-13 | `1.09` (nghỉ 2 s) | — | — | giữ 1-12, nhạc tắt, chỉ còn nền trầm | — | — | ⊘ | |
| 1-14 | `1.10#1` | H | T5 ngày | `t2_house_missing` | **28 · 01 · 2010** | Gõ từng ký tự | | ✂ |
| 1-15 | `1.10#2`–`#3` | H | T2 | `t2_house_missing_dawn` | *JESSICA LLOYD · 27 YEARS OLD · BELLEVILLE* · **VANISHED FROM HER HOME** → `#3`: *Ontario Provincial Police opened an investigation · A massive search* | Dấu mộc ở "opened an investigation" | | |
| 1-16 | `1.12#1` | H | T1 | `t2_town_snow` | **NO IMMEDIATE CLUES** | Gió, bước chân (SFX `1.11`) ở đầu | | |
| 1-17 | `1.12#2` | H | T7 | `t2_checkpoint` | **EVENING OF FEBRUARY 4TH** · *Mobile checkpoint · Near the victim's home · All night long* | 2 ghim không nhãn, đường tự vẽ | | |
| 1-18 | `1.12#3`–`#4` | H | T1 | `t2_tire_track`, `still` | *Not there to inspect driver's licenses* → `#4`: **A DISTINCTIVE TIRE TRACK** | Tiêu đề ở "tire track" | | |
| 1-19 | `1.14#1`–`#2` | H | T3 so sánh | `t2_suv_stop` | **NISSAN PATHFINDER** → `#2`: *Rather than the BMW he normally drove* | Gõ kính (SFX `1.13`) ở đầu | | |
| 1-20 | `1.14#3` | H | T1 `hero` | `t2_suv_stop` | **BASE COMMANDER OF CFB TRENTON** | Tiêu đề ở "himself" | ⊘ | |
| 1-21 | `1.14#4`–`#5` | H | T1 | `t2_tire_track` | **STRIKINGLY SIMILAR TO THE TRACKS** → `#5`: *But not enough to detain a man of his standing* | — | | |
| 1-22 | `1.14#6`–`#7` | H | T1 | `t2_checkpoint_dawn` | *Waved through with a polite farewell* → `#7`: **THE NEXT THREE DAYS** · *He remained a free colonel* | — | | |
| 1-23 | `1.14#8` | H | T1 | `t2_interrogation_empty`, `push` | *LISTEN:* **THE INVESTIGATOR RECONSTRUCTS THOSE THREE DAYS** | Cửa sắt "Rầm" (SFX `1.15`) sau câu | →D | |
| 1-24 | `1.17#1` | D | T2 | `t2_tire_track` | *NEAR THE VICTIM'S HOME* · **A RARE ALL-TERRAIN TIRE TREAD PATTERN** · *A large snow boot mark* | Dấu mộc ở "snow boot mark" | ✦ Sói | |
| 1-25 | `1.17#2`–`#3` | D | T1 | `t2_suv_stop` | *A routine traffic stop* → `#3`: **TREAD PATTERN CLOSELY MATCHED THE IMPRESSION** | Vệt sáng đèn pin ở "shone his flashlight" | | |
| 1-26 | `1.17#4` | D | T3 so sánh | `t2_checkpoint` | *Colonel Russell Williams's world* · **INTERSECTED** · *The world of law enforcement* | Cột phải ở "the world of law enforcement" | | |
| 1-27 | `1.17#5`–`#6` | D | T6 | `pinboard` | *Three days · Quietly corroborating the evidence* → `#6`: **SEARCH WARRANTS** · *Ottawa · Tweed* | Mỗi câu một mốc | | |
| 1-28 | `1.17#7` | D | T1 | `t2_phone_call` | *Rather than a formal summons* · **A TELEPHONE INVITATION** | Tiêu đề ở "telephone invitation" | | |
| 1-29 | `1.18#1` | H | T1 | `t2_podcast_desk`, cassette quay | **THE CRIMINAL PSYCHOLOGY CASE FILES** | — | 🅑 | |
| 1-30 | `1.18#2` | H | T2 | `records` | *CASE FILE* · **THE RUSSELL WILLIAMS FILE** | Dấu mộc ở "The Russell Williams File" | | |
| 1-31 | `1.18#3` | H | T9 → T10 | `t2_two_masks` | **BEHAVIORAL ESCALATION** · **COMPARTMENTALIZATION** → *EPISODE 02 · THE TWO-FACED COLONEL* | Mỗi thuật ngữ ở cụm từ; tên tập cuối câu | | |
| 1-32 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 02* · **THE 4 STAGES OF THE ABYSS** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ TỘI ÁC · nền chủ đạo `t2_folder_tree`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` | H | T1 | `t2_cottage_search` | **THE SEARCH** · *Ottawa · Tweed* | — | | |
| 2-02 | `2.02#2` | H | T1 | `t2_cottage_search`, `push` | **EXCEEDED THE DARKEST IMAGINATIONS** | — | | |
| 2-03 | `2.04#1` | H | T1 | `t2_house_missing_dawn` | **HARD DRIVES HIDDEN IN THE BASEMENT CEILING** | Lật hồ sơ (SFX `2.03`) ở đầu | | |
| 2-04 | `2.04#2` | H | T1 | `t2_escalation_stairs` | *Thousands of photos and videos · Date-and-time stamps · Complex folder structures · Logs of every intrusion* | — | | |
| 2-05 | `2.04#3` | H | T1 | `t2_escalation_stairs` | **NOT A PREDATOR OVERNIGHT** → `#4`: *The visible tip of an iceberg* · **FOUR STAGES OF BEHAVIORAL ESCALATION** | — | | |
| 2-06 | `2.04#4` | H | T1 | `pinboard` mờ, `push` | *LISTEN:* **THE INVESTIGATOR BREAKS DOWN THE MODUS OPERANDI** | — | →D | |
| 2-07 | `2.05#1` | D | T2 | `pinboard` | **FOUR STAGES OF ESCALATION** · *Digital evidence and recovered logs* | Bộ đếm `0/4`, 4 thẻ trống ghim lên | | |
| 2-08 | `2.05#2`–`#3` | D | T3 `1/4` | `t2_open_window` | *STAGE 01* · **VOYEURISM** → `#3`: *Prowling quiet residential neighborhoods at night* | — | | |
| 2-09 | `2.05#4`–`#6` | D | T3 `2/4` | `t2_drawer_dark` | *STAGE 02* · **BURGLARY AND THEFT OF INTIMATE ITEMS** → `#6`: *The earliest break-ins traced by investigators: 2006* | — | | |
| 2-10 | `2.05#7` | D | T5 | `t2_open_window` mờ | *09 · 2007 – 11 · 2009* · **82** · *Burglaries and attempted burglaries* | Số đếm 0 → 82 | | |
| 2-11 | `2.05#8`–`#9` | D | T8 gạch bỏ | `records` | *Cash · Jewelry* → `#9`: **WOMEN'S PERSONAL BELONGINGS** | Gạch ở "took neither" | | |
| 2-12 | `2.05#10` | D | T8 | `t2_logbook` | *THE RITUAL REPEATED IDENTICALLY* · *Photograph the scene · Take the items · Log every detail* | Mỗi mục ở cụm từ | | |
| 2-13 | `2.05#11`–`#13` | D | T3 `3/4` | `t2_escalation_stairs` | *STAGE 03* · **HOME INVASION WITH OCCUPANTS PRESENT** → `#12`: *09 · 2009 · The threshold kept growing duller* → `#13`: *Two women · Around the town of Tweed* | — | ⊘ ở `#13` | |
| 2-14 | `2.05#14`–`#16` | D | T3 `4/4` | `fog`, tối dần | *STAGE 04* · **MURDER** → `#15`: *Late November 2009 · Marie-France Comeau · Corporal · 37 years old · 437 Transport Squadron* → `#16`: *Two months later · Jessica Lloyd* | Chỉ chữ, không hình người | ⊘ | |
| 2-15 | `2.06` (nghỉ 1,5 s) | — | — | giữ 2-14, tối dần | — | — | ⊘ | |
| 2-16 | `2.07#1`–`#2` | H | T3 so sánh | `t2_two_masks` | *An unsettling predatory instinct* → `#2`: *The rigid discipline of an officer* · **AS THOUGH FILING A FORMAL MILITARY BRIEFING** | Cột phải ở `#2` | | ✂ |
| 2-17 | `2.07#3` | H | T9 | `t2_logbook` | **BEHAVIORAL SIGNATURE** · *The one thing he could never part with* | — | | |
| 2-18 | `2.07#4` | H | T1 | `pinboard`, `push` | *LISTEN:* **THE INVESTIGATOR EXPLAINS** | — | →D | |
| 2-19 | `2.08#1`–`#2` | D | T9 | `records` | *Conventional offenders: destroy every trace* → `#2`: **TROPHIES** · *What he needed, not merely wanted* | Thuật ngữ ở `#2` | | |
| 2-20 | `2.08#3`–`#4` | D | T1 | `t2_drawer_dark` | **RELIVING THE SENSATION OF CONTROL** | Tiêu đề ở "relive" | 🅑 | |
| 2-21 | `2.08#5` | D | T1 | `t2_boot_evidence` | *AN ENDURING RECORD OF HIS DOMINION* · **PHOTOGRAPHING AND CATALOGING** | — | | |
| 2-22 | `2.08#6` | D | T1 | `t2_suv_stop` | *TIRE TREAD AND BOOT IMPRESSIONS* · **TRACKS IN THE SNOW** | — | | |
| 2-23 | `2.08#7` | D | T1 | `t2_house_missing_dawn` | *THE SINGLE KEY* · **THE SECRET EVIDENCE VAULT** | — | | |
| 2-24 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 03* · **INSIDE THE MIND OF A TWO-FACED PREDATOR** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI PHẪU TÂM LÝ · nền chủ đạo `t2_brain_neural`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T1 | `t2_command_chair` | **A DEEPLY UNSETTLING RIDDLE** | — | | |
| 3-02 | `3.02#2` | H | T8 | `t2_command_chair` tối | *A man who seemingly possessed everything* → `#2`: **WHY GAMBLE IT ALL AWAY?** | Mỗi mục ở cụm từ; tiêu đề ở "gamble it all away" | | |
| 3-03 | `3.03` (nghỉ 2 s) | — | — | giữ 3-02 | — | — | | |
| 3-04 | `3.04#1` | H | T2 | `records` | *BEFORE THE ANALYSIS* · **NO PUBLICLY KNOWN CLINICAL DIAGNOSIS** · *Of Russell Williams* | — | 🅑 | |
| 3-05 | `3.04#2` | H | T1 | `t2_brain_neural` mờ | **HELPING US ASK THE RIGHT QUESTIONS** · *Not a clinical finding endorsed by any authority* | — | | |
| 3-06 | `3.04#3` | H | T1 | `t2_brain_neural`, `push` | *LISTEN:* **THE PSYCHOLOGIST** → *Three layers of cognitive mechanisms* | — | →C | |
| 3-07 | `3.05#1`–`#3` | C | T9 | `t2_brain_neural` + sơ đồ 3 vòng (dùng lại `brain3` Tập 01) | *Not someone detached from reality or psychotic* → `#2`: **FULLY LUCID** → `#3`: **THREE LAYERS OF PSYCHOLOGICAL MECHANISMS** | 3 vòng sáng ở `#3` | ✦ Cáo | |
| 3-08 | `3.05#4` | C | T9 | `t2_escalation_stairs` | *LAYER 01* · **THE LAW OF BEHAVIORAL ESCALATION** · *And dopamine desensitization* | — | | |
| 3-09 | `3.05#5` | C | T1 | `t2_escalation_stairs`, `pan` | **ORIGINATING IN SMALLER, TRANSGRESSIVE IMPULSES** | Tiêu đề ở "transgressive impulses" (thuật ngữ y khoa chỉ đọc, không hiện) | | |
| 3-10 | `3.05#6`–`#7` | C | T9 | `t2_brain_neural` + đường nhịp tăng vọt (Pillow) | **DOPAMINE** · *Reward and anticipation* → `#7`: *In this framework, an intense neurochemical rush* | Nhịp nhấp nháy ở `#7` | | |
| 3-11 | `3.05#8`–`#9` | C | T9 | `t2_brain_neural`, đường nhịp phẳng dần | **TOLERANCE** → `#9`: *Much like an addict requiring ever-larger doses* | — | 🅑 | |
| 3-12 | `3.05#10` | C | T8 | `t2_escalation_stairs`, `pan` | *Unoccupied houses · Confronting victims · Restraining them · Deciding between life and death* | Mỗi bậc ở cụm từ, camera leo dần | | |
| 3-13 | `3.05#11` | C | T1 `hero` | `t2_stairs_dark`, tối dần | **THE THRESHOLD OF SATISFACTION DRIFTED FARTHER** · *A bottomless downward spiral* | Tiêu đề ở "bottomless downward spiral" | ⊘ | |
| 3-14 | `3.06` (nghỉ 1,5 s) | — | — | giữ 3-13 | — | — | | |
| 3-15 | `3.07#1` | H | T1 | `t2_drawer_dark` | **HOW HE CONCEALED IT** | — | | ✂ |
| 3-16 | `3.07#2` | H | T3 so sánh | `t2_two_masks` | *BY DAY* · *Chaired military briefings · Shook hands with officials · Dinner with his wife* → *BY MIDNIGHT* · **SOMEONE ENTIRELY UNRECOGNIZABLE** | Cột phải ở "midnight" | | |
| 3-17 | `3.07#3` | H | T1 | `t2_two_masks`, `push` | **HOW COULD A HUMAN MIND SUSTAIN THIS?** | — | →C | |
| 3-18 | `3.08#1`–`#2` | C | T9 | `t2_two_drawers` | *LAYER 02* · **ABSOLUTE PSYCHOLOGICAL COMPARTMENTALIZATION** → `#2`: *A defense mechanism · Separate cognitive drawers* | Thuật ngữ Anh ở `#2` | | |
| 3-19 | `3.08#3`–`#5` | C | T3 so sánh | `t2_two_drawers` | *COMPARTMENT 01* · **COLONEL WILLIAMS** · *Order · Discipline · Duty* → `#5`: *COMPARTMENT 02* · **THE NOCTURNAL PREDATOR** · *Discarding every social constraint* | Cột phải ở `#5` | | |
| 3-20 | `3.08#6`–`#8` | C | T1 | `t2_drawer_dark` | **WHEN INHABITING ONE COMPARTMENT, HE SEALED THE DOOR TO THE OTHER** | Ngăn kéo đóng ở "sealed the door" | | |
| 3-21 | `3.08#9`–`#10` | C | T4 `hero` | `t2_interrogation_empty` | *INCAPABLE OF EXPLAINING HIS ACTIONS* → `#10`: “Yes, but I don’t know the answers, and I’m pretty sure the answers don’t matter.” | Câu trích từng dòng từ dấu `:` | ⊘ | |
| 3-22 | `3.08#11`–`#12` | C | T1 | `t2_interrogation_empty` | **THE MOST CANDID RESPONSE** → `#12`: *Re-examine our entire analytical lens* | — | 🅑 | |
| 3-23 | `3.09` (nghỉ 2 s) | — | — | giữ 3-22 | — | — | | |
| 3-24 | `3.10#1` | H | T1 | `t2_command_chair`, `push` | *THE THIRD PSYCHOLOGICAL LAYER* · **THE FOUNDATIONAL MOTIVE?** | — | →C | |
| 3-25 | `3.11#1` | C | T9 | `t2_command_chair` | *LAYER 03* · **MALIGNANT NARCISSISM** · **GOD COMPLEX** | Thuật ngữ 2 ở "god complex" | | |
| 3-26 | `3.11#2`–`#3` | C | T3 | `t2_base_trenton` | **MILITARY AUTHORITY** · *Thousands who had to obey* → `#3`: *Bound by institutional rules and law* | — | | |
| 3-27 | `3.11#4` | C | T1 | `bedroom_door` tối | **ABSOLUTE POWER WITHOUT RESTRAINT** | Tiêu đề ở "unconstrained authority" | ⊘ | |
| 3-28 | `3.11#5` | C | T4 | `t2_command_chair` tối | *Tangible trophies feeding his grandiosity* → “I stand above everyone… none of you can touch me.” | Câu trích ở "I stand above" (lời độc thoại tưởng tượng — dấu “” màu tím `violet` của Cáo, không phải lời thật) | | |
| 3-29 | `3.11#6`–`#8` | C | T1 | `t2_oath_hall` | **HIS EGO WAS NEVER CRUSHED BY SHAME** → `#8`: *Still the man on the podium* | Gọi lại hình lễ nhậm chức Hồi 1 | 🅑 | |
| 3-30 | `3.11#9`–`#11` | C | T3 so sánh | `void` | **AN IMPULSIVE FRENZY** · *Burns itself out* → `#11`: **HERE** · *Each transgression rewarded him* | Cột phải ở `#11` | | |
| 3-31 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 04* · **BREAKING A MILITARY MIND** | — | ⊘ | ◼ |

### HỒI 4 — ĐẤU TRÍ PHÒNG THẨM VẤN · nền chủ đạo `t2_two_chairs`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.03#1`–`#2` | H | T5 ngày | `t2_interrogation_empty` | **07 · 02 · 2010** · *Sunday · Ottawa Police headquarters · 3:00 PM* | Gõ từng ký tự; đèn huỳnh quang (SFX `4.01`) | | |
| 4-02 | `4.03#3`–`#4` | H | T3 so sánh | `t2_two_chairs` | *One side of the table* · **COLONEL RUSSELL WILLIAMS** · *Civilian clothes* → `#4`: *Facing him* · **DETECTIVE SERGEANT JIM SMYTH** · *Behavioral science investigator · Ontario Provincial Police* | Cột phải ở `#4`; chỉ tên, không gắn lên bóng (V5) | | |
| 4-03 | `4.03#5`–`#6` | H | T2 | `t2_interrogation_empty` | **CAME ENTIRELY VOLUNTARILY** · *Following a simple telephone request* → `#6`: *Read his rights and cautions — yet remained relaxed* | — | | |
| 4-04 | `4.04` (nghỉ 2 s) | — | — | giữ 4-03 | — | — | | |
| 4-05 | `4.05#1` | H | T1 | `t2_tape_recorder`, `push` | *ONE OF THE MOST CELEBRATED INTERROGATIONS* · *LISTEN:* **THE MEMORIES OF RESIDENTS** | — | →N2 | |
| 4-06 | `4.06#1`–`#2` | N2 | T4 lời kể | `t2_house_missing_dawn` | “…our small town of Tweed lived under an intangible sense of dread…” | — | ✦ Mèo | |
| 4-07 | `4.06#3` | N2 | T4 lời kể | `t2_bedroom_intruder` | “…the realization was far more terrifying than any nightmare.” | — | ✦ Mèo | |
| 4-08 | `4.06#4` | N2 | T4 lời kể | `t2_bedroom_intruder` | “…a man disguised in an officer's uniform was standing right there in the dark, watching you.” | — | 🅑 | |
| 4-09 | `4.07#1`–`#3` | H | T1 | `t2_two_chairs`, `pull` | **PSYCHOLOGICAL INTERROGATION** · *Detective Sergeant Jim Smyth* → `#3`: *LISTEN:* **THE BATTLE OF MINDS** | — | →D | |
| 4-10 | `4.08#1`–`#2` | D | T9 | `t2_two_chairs` | **THE ART OF RAPPORT BUILDING** · *The trap of overconfidence* | — | | |
| 4-11 | `4.08#3`–`#4` | D | T1 | `t2_two_chairs` | *WILLING TO PROVIDE* · **DNA · FINGERPRINTS · FOOTWEAR IMPRESSIONS** | — | | |
| 4-12 | `4.08#5` | D | T3 so sánh | `t2_siren_wall` | **THE TRAP OF OVERCONFIDENCE** · *Search warrants at Ottawa & Tweed* | Đèn xanh đỏ | | |
| 4-13 | `4.08#6` | D | T3 so sánh | `t2_boot_evidence`, `still` | *Footprint from the crime scene* · *Williams's own boots* → “They are identical.” | Câu trích ở "stating plainly" | | ✂ |
| 4-14 | `4.08#7` | D | T1 | `t2_head_down` | **THE COLONEL PAUSED NOTICEABLY** | — | | |
| 4-15 | `4.08#8`–`#9` | D | T4 | `t2_two_chairs` | *A REVEALING REQUEST* → “Just call me Russ.” | Trượt ảnh "Xoẹt" ở đầu | | |
| 4-16 | `4.10#1` | D | T1 | `t2_hidden_drive` | **HARD DRIVES IN THE BASEMENT CEILING** · *Thousands of classified photographs & meticulous logs* | — | ⊘ | |
| 4-17 | `4.10#2`–`#3` | D | T4 `hero` | `t2_siren_wall` | **THE DECISIVE MOVE** → `#3`: “Your wife now knows what’s going on.” | Câu trích ở "decisive move" | ⊘ | |
| 4-18 | `4.10#4`–`#6` | D | T4 | `t2_head_down` | *Did not break immediately* → `#7`: “I don’t know what to say.” | — | | |
| 4-19 | `4.10#7` | D | T4 | `t2_interrogation_empty`, `still` | *Roughly four hours and forty minutes into the interview* → “So, where is she?” | Câu trích ở "asked softly" | | |
| 4-20 | `4.10#8` | D | T4 `hero` | `t2_forest_map` | “Got a map?” | — | ⊘ | ✂ |
| 4-21 | `4.10#9` | D | T1 | `t2_interrogation_early` | *Over the next six hours* · **ONE BY ONE** | — | | |
| 4-22 | `4.11#1`–`#3` | C | T1 | `t2_two_drawers` | **THE MOMENT OF PSYCHOLOGICAL COLLAPSE** → `#3`: *The barrier between two drawers · Shattered* | Hai ngăn kéo bật mở ở `#3` | 🅑 | |
| 4-23 | `4.11#4` | C | T4 | `t2_interrogation_empty` | *HIS ONLY REMAINING VULNERABILITY* · **HIS WIFE** → `#5`: “I want to minimize the impact on my wife.” | — | | |
| 4-24 | `4.11#5` | C | T1 | `t2_two_chairs` | *The only path forward began with the truth* → `#7`: **ABOUT HALF AN HOUR LATER** | — | | |
| 4-25 | `4.11#6`–`#7` | C | T3 so sánh | `void` | *THE ANXIETIES HE VOICED* · *His wife · The fallout on the airbase* → `#9`: *NOT ONCE* · **THE WOMEN HE HAD BRUTALIZED** | — | ⊘ | |
| 4-26 | `4.11#8` | C | T1 | `void` | **NOT REMORSE** → `#11`: **IT WAS TERROR** · *Fear of losing his persona* | — | | |
| 4-27 | `4.11#9` | C | T1 | `t2_head_down` | **A SINGLE INDIVIDUAL** · *Having to face everything he had done* | — | 🅑 | |
| 4-28 | `4.12#1` | H | T1 `hero` | `t2_head_down` | **HE BOWED HIS HEAD** | — | ⊘ | |
| 4-29 | `4.12#2` | H | T1 | `t2_head_down` | *Only on a map* → `#3`: **DAWN THE NEXT MORNING** · *Police reached the location* | — | | |
| 4-30 | `4.12#3` | H | T8 | `records` | *ADMITTED* · *The murder of Corporal Marie-France Comeau · Two sexual assaults in Tweed* | Mỗi mục ở cụm từ | | |
| 4-31 | `4.12#4` | H | T1 | `t2_folder_tree` | *After roughly ten hours in that room* · **THE SPOTLESS FACADE DISINTEGRATED** | — | | |
| 4-32 | `4.12#5` | H | T5 | `pinboard` | **THE INVESTIGATION DID NOT CONCLUDE** → `#7`: *His own cataloged photographs and logs* | Số đếm 0 → 88 | | |
| 4-33 | `4.12#6` | H | T1 | `t2_head_down` | **THE PRISTINE DISGUISE DISSOLVED INTO ASH** | — | | |
| 4-34 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 05* · **THE VERDICT, RED FLAGS & CLOSING THOUGHTS** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT, BÀI HỌC CẢNH BÁO ĐỎ & LỜI KẾT · nền chủ đạo `t2_courtroom`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#2` | H | T5 ngày | `t2_courtroom` | **10 · 2010** · *Ontario Superior Court of Justice in Belleville · Justice Robert Scott* | Búa gõ ba lần (SFX `5.01`) trước câu | | |
| 5-02 | `5.02#3` | H | T5 | `t2_courtroom` | *October 18th* · **88** · *Guilty pleas to all charges* | Số đếm | | |
| 5-03 | `5.02#4` | H | T8 | `t2_gavel` | *OCTOBER 21ST · THE SENTENCE* · *Two concurrent life sentences · Ten years for each sexual assault · Ten years for each forcible confinement · One year for each of the 82 burglaries* | Mỗi mục ở cụm từ (câu dài ~20 s → 5 beat) | | |
| 5-04 | `5.02#5`–`#6` | H | T5 | `t2_gavel` | **25 YEARS** · *No eligibility for parole* → `#6`: *The mandatory minimum under Canadian criminal law* | Số đếm 0 → 25 | | |
| 5-05 | `5.03` (nghỉ 2 s) | — | — | giữ 5-04 | — | — | | |
| 5-06 | `5.04#1` | H | T1 | `t2_oath_hall` tối | **THE TOTAL ANNIHILATION OF HIS PUBLIC PERSONA** | Gọi lại hình lễ nhậm chức, nay tối | | |
| 5-07 | `5.04#2`–`#4` | H | T8 gạch bỏ | `t2_medals_cut` | *Commission · Decorations · Commission scroll · Official biography on the National Defence website* | Mỗi câu gạch mục tương ứng | | |
| 5-08 | `5.04#5` | H | T1 | `t2_uniform_fire` | **BURNING HIS UNIFORMS** · *CFB Trenton · A document disposal facility* | Lửa bùng ở "burning his uniforms" | | |
| 5-09 | `5.04#6`–`#7` | H | T2 | `t2_uniform_fire` mờ | *Hubert Genest · Military spokesperson* · *No formal ceremony · No photography* → `#7`: **THE FIRST TIME IN 25 YEARS** | Tiêu đề ở `#7` | | |
| 5-10 | `5.04#8` | H | T4 | `t2_uniform_fire` tối | “When you put a period at the end of a sentence, the period is small, but it carries immense meaning.” | Câu trích ở "punctuation mark" | ⊘ | |
| 5-11 | `5.04#9` | H | T1 | `t2_checkpoint_dawn` | **THE SUV WAS CRUSHED** · *Hundreds of stolen items destroyed* | — | | |
| 5-12 | `5.05` (nghỉ 2 s) | — | — | giữ 5-11 | — | — | | |
| 5-13 | `5.06#1` | H | T1 | `t2_red_flags` | **SPOTTING PREDATORS EARLY** · *Hidden behind perfect facades* | — | | |
| 5-14 | `5.06#2` | H | T1 | `t2_red_flags`, `pull` | **FOUR CRITICAL RED FLAGS** · *Psychologist & Investigator* | — | →C+D | |
| 5-15 | `5.07#1`–`#3` | C | T1 | `void` | **THE ILLUSION OF RESPECTABILITY** · *Lowering our defensive guard* | — | | |
| 5-16 | `5.07#4`–`#6` | C | T1 | `t2_bedroom_intruder` | **MINOR BOUNDARY VIOLATIONS** · *The threshold for satisfaction drifts perpetually farther* | — | | |
| 5-17 | `5.08#1` | D | T1 | `t2_folder_tree` | *MILITARY PRECISION & RECORD-KEEPING* · **DRAFTING HIS OWN CONVICTION** | — | | |
| 5-18 | `5.08#2` | D | T1 | `void` | **A NARCISSIST’S ARROGANCE INVARIABLY LEAVES A TRAIL** | — | | |
| 5-19 | `5.08#3` | D | T1 | `t2_suv_stop` | *Perfectionism on its own is not an indicator of criminality* → `#7`: *Worth noting when it comes with extreme secrecy and a deficit of empathy* | — | | |
| 5-20 | `5.09` (nghỉ 2 s) | — | — | giữ 5-19 | — | — | ⊘ | |
| 5-21 | `5.10#1`–`#3` | H | T1 | `t2_podcast_desk`, đèn ấm dần | *The unfathomable depths of the human psyche* → `#2`: **MERELY EXTERNAL COATS** → `#3`: *Never a guarantee of moral integrity* | — | | |
| 5-22 | `5.10#4`–`#5` | H | T1 `hero` | `t2_escalation_stairs` | *Evil rarely begins with a gunshot or a blade* → `#5`: **FROM A SINGLE STEP ACROSS A MORAL BOUNDARY** | Câu dài → beat ở "step by agonizing step" | | |
| 5-23 | `5.10#6`–`#9` | H | T8 | `t2_folder_tree` | **THE ONLY ONE GUARDING THE SECRET** → `#7`: *Photographs cataloged with surgical precision* → `#8`: *Stolen items hidden with obsessive care* → `#9`: *An interrogation lasting roughly ten hours* | Mỗi câu một mục | | |
| 5-24 | `5.10#10`–`#11` | H | T1 `hero` | `t2_oath_hall` | **AN ELITE INTELLECT PROTECTS NO ONE** → `#11`: *It only delays the collapse, and makes it worse* | Tiêu đề ở "protects no one" | ⊘ | |
| 5-25 | `5.11` (nghỉ 1,5 s) | — | — | giữ 5-24 | — | — | | |
| 5-26 | `5.12#1`–`#2` | H | T1 | `t2_podcast_desk` | **THANK YOU TO OUR EXPERT GUESTS** · *Fictional characters · AI voices* | 5 ảnh P0 sáng lần lượt | dàn khách mời | |
| 5-27 | `5.12#3` | H | T1 | `t2_podcast_desk` | **KEEP A SHARP EYE OPEN** · *Trust your instincts · Respect protective boundaries* | — | | |
| 5-28 | `5.12#4` | H | T10 | `t2_podcast_desk` mờ | **SEE YOU IN THE NEXT EPISODE** · *Leave your perspective in the comments* | — | 🅑 | |
| 5-29 | `5.13`–`5.14` | — | T2 | `t2_podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | *DOSSIER EPISODE 02 · CLOSED* · **AMBER EYES** · *Criminal Psychology Analysis* · *Through Real Case Files* | Thẻ hồ sơ hiện sau tiếng "Cạch"; mờ ra đen | ⊘ | ◼ |

**Tổng: 151 dòng = 134 shot có lời + 17 dòng không lời.** Phủ 215/215 câu, đúng thứ tự, cột Vai khớp người nói, mọi nền có file, mọi câu trích nguyên văn (kiểm tra bằng script ngày 22/10/2026). Các số `01`–`04`, `02` trên hình là nhãn thứ tự (giống *TẦNG 01*, cờ *01* của Tập 01), không phải dữ kiện.

