# TIÊU CHUẨN DỰNG VIDEO — KÊNH AMBER EYES (PHẦN A)

**Phiên bản 11 · Bản mẫu tiêu chuẩn** · Cập nhật 23/10/2026
**Trạng thái:** đã chạy thật trọn vẹn với Tập 01 (`Tap01_master.mp4`, 18:53) và **Tập 02** (`Tap02_master.mp4`, ~26:45, giọng bộ A). Mọi lệnh, số liệu và lỗi trong file này lấy từ hai lần chạy đó.
**Thay đổi lớn ở bản 11:** giọng bộ A + quy tắc giọng G1–G11 (A4.1–A4.2) · chọn tập bằng `AE_EP` và cấu hình tập trong `edition.py` (A12) · âm thanh stereo có nền môi trường (A4.4, `sfx_tapXX.json`) · ảnh tĩnh mọi shot trước khi dựng · bẫy #17–24 (A11).

## Cách dùng file này

| Tài liệu | Nội dung | Tập mới làm gì |
|---|---|---|
| **File này — `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md`** (Phần A) | Quy tắc, quy trình, lệnh chạy, âm thanh, đồ hoạ, kiểm tra, pháp lý, các bẫy đã gặp | **Giữ nguyên.** Chỉ sửa khi đổi tiêu chuẩn của kênh |
| **Hồ sơ tập — `02_SAN_XUAT/TapXX/KeHoach_Video_TapXX.md`** (Phần B) | Số liệu, ánh xạ riêng, bảng shot, phụ lục của từng tập | Sao chép `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md` làm mẫu, thay nội dung tập mới |

**Cấu trúc thư mục chuẩn:** xem `README.md` ở thư mục gốc.

Người dùng chỉ cần đưa **kịch bản đúng định dạng A2**. AI làm phần còn lại theo A3, dừng lại báo khi gặp vấn đề.

---

# PHẦN A — TIÊU CHUẨN CHUNG

## A0. Chín quy tắc vàng

| # | Quy tắc | Vì sao |
|---|---|---|
| **V1** | **Đơn vị đồng bộ là CÂU.** TTS đọc từng câu thành một file riêng; mọi mốc thời gian đo bằng ffprobe trên file đó | Chia block theo tỉ lệ từng làm hình lệch lời tới 16 s |
| **V2** | **Hình chỉ đổi ở đầu câu.** Cấm chia shot theo tỉ lệ thời gian | Lỗi "vào nội dung rồi hình mới xuất hiện" |
| **V3** | **Chữ trên hình lấy từ chính câu đang đọc.** Không thêm dữ kiện, con số; câu trích phải **nguyên văn** (được lược bằng `…`, không được cắt cụt rồi tự thêm dấu) | Từng tự bịa "19 tuổi"; từng cắt cụt câu trích ở Tập 01 |
| **V4** | **Không có im lặng tuyệt đối quá 0,3 s.** Lớp nền trầm luôn chạy | Từng câm 6 s ở 0:26 |
| **V5** | **Người thật trong vụ án chỉ hiện dạng bóng**, mặt chìm hoàn toàn. **Quan chức, bác sĩ thật không được vẽ** — chỉ hiện tên | Người thật; có thể là trẻ vị thành niên |
| **V6** | **Linh thú là nhân vật minh hoạ**, nhãn *"Nhân vật minh hoạ · giọng đọc AI"* ở lần xuất hiện đầu | Không để người xem hiểu là phỏng vấn thật |
| **V7** | **Nền vụ án luôn toàn màn hình; linh thú ≤ 20% khung**, chỉ ở góc | Bố cục đã chốt |
| **V8** | **Mọi tập mở đầu bằng intro kênh 22,41 s; mọi tài sản có dòng trong `provenance.json`** | Nhận diện kênh; hồ sơ khi bị khiếu nại |
| **V9** | **Trọng tâm là phân tích tâm lý.** Không mô tả chi tiết bạo lực, thương tích, thi thể, cách gây hại — cả lời lẫn hình | Định hướng kênh; giảm rủi ro quảng cáo hạn chế |

## A1. Đầu vào và đầu ra của mỗi tập

**Đầu vào (người dùng):**
- [ ] `01_KICH_BAN/TapXX/kichban_tapXX.md` đúng định dạng A2, **đã giảm bạo lực theo V9** (xem Phụ lục B trong `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md` làm mẫu)
- [ ] Tên tập
- [ ] (tuỳ chọn) ghi chú phong cách, cảnh đặc biệt

**Đầu ra (AI)** — tất cả nằm trong `02_SAN_XUAT/TapXX/xuat_ban/` (riêng `provenance.json` ở thư mục gốc, cộng dồn các tập):

| File | Nội dung |
|---|---|
| `TapXX_master.mp4` | Video chính (H.264 + AAC 192k) |
| `TapXX_master.mp3` | Âm thanh tổng |
| `TapXX.srt` | Phụ đề có tên vai |
| `thumbnail.png` | 1280×720 |
| `mo_ta.txt` | Mô tả YouTube có mốc chương |
| `nguon_tham_khao.md` | Danh sách câu cần nguồn — **người dùng điền link** |
| `provenance.json` | Nguồn gốc mọi tài sản (cộng dồn qua các tập) |

## A2. Định dạng kịch bản bắt buộc

`.work/parse_kichban.py` chỉ hiểu đúng các mẫu sau:

| Dòng | Mẫu chính xác | Ghi chú |
|---|---|---|
| Hồi | `## HỒI N: tên hồi` | N = 1…5; mã phần tử đếm lại từ `N.01` |
| Lượt nói | `**HOST** *(chỉ dẫn)*:` | Tên vai đúng 1 trong 4: `HOST` · `ĐIỀU TRA VIÊN` · `CHUYÊN GIA TÂM LÝ` · `NGƯỜI BÌNH THƯỜNG`. Chỉ dẫn không đọc |
| Hiệu ứng | `**[SFX]:** mô tả` · `**[BGM]:** mô tả` | |
| Nghỉ | `**[Nghỉ X giây – ghi chú]**` | Tối đa 2,5 s khi dựng |
| Gạch đầu dòng | `*   ` hoặc `1.  ` | Mỗi dòng thành một câu riêng |
| Trích dẫn | `'…'` | Hiện `“…”` trên hình; bỏ dấu khi đọc |
| Nhấn mạnh | `**…**` · `*…*` | Bỏ ký hiệu, giữ chữ |

Lượt nói có đoạn văn được bọc trong `"…"` như Tập 01. Câu được cắt tại `. ? ! …` (kể cả `.”`) khi theo sau là chữ hoa. Cue nằm giữa lượt nói cắt lượt thành 2 phần tử cùng vai.

**Hai "Người bình thường" khác nhau** trong cùng tập phải được khai ở `N_ELEMENT` (A12) để có hình và giọng riêng (N1, N2).

### A2b. Bản ngôn ngữ — tiếng Anh, tiếng Hàn, tiếng Nhật

Ngoài bản tiếng Việt (nguồn chuẩn), mỗi tập có thể có các **bản ngôn ngữ**. Bản ngôn ngữ là **bản dịch theo ngôn ngữ**, không phải bản rút gọn: nó phải giữ nguyên cấu trúc để chạy lại đúng pipeline.

| Bản | Thư mục kịch bản | Chuẩn riêng | Lệnh pipeline |
|---|---|---|---|
| EN | `01_KICH_BAN/TapXX_EN/kichban_tapXX_EN.md` | `02_SAN_XUAT/Tap02_EN/CHU_CO_DINH_EN.md` | `$env:AE_LANG='en'; $env:AE_EP='XX'` |
| KO | `01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md` | **`00_TIEU_CHUAN/CHU_CO_DINH_KO.md`** | `$env:AE_LANG='ko'; $env:AE_EP='XX'` |
| JA | `01_KICH_BAN/TapXX_JA/kichban_tapXX_JA.md` | (theo bản JA) | `$env:AE_LANG='ja'; $env:AE_EP='XX'` |

**Bốn điều tuyệt đối không được phá vỡ** khi dịch (chung cho mọi bản ngôn ngữ):

1. **Số hồi** giữ nguyên (`## HỒI N` / `## ACT N` / `## 막 N` / `## 第N幕`) và thứ tự element trong hồi giữ nguyên.
2. **Vai** giữ nguyên — mỗi lượt nói phải là một vai (H/D/C/N), không gộp, không tách.
3. **Số câu** trong mỗi lượt nói giữ nguyên (QC đếm từng câu).
4. **Số giây nghỉ** giữ nguyên.

**Cách đổi nhãn theo ngôn ngữ** (parser chấp nhận cả hai dạng):

| Nhãn VN | Nhãn EN | Nhãn KO | Nhãn JA |
|---|---|---|---|
| `## HỒI N:` | `## ACT N:` | `## 막 N:` | `## 第N幕` |
| `**[Nghỉ X giây]**` | `**[Pause X seconds]**` | `**[정지 X초]**` | `**[休止 X秒]**` |
| `HOST` | `HOST` | `호스트` | `ホスト` |
| `ĐIỀU TRA VIÊN` | `INVESTIGATOR` | `수사관` | `捜査官` |
| `CHUYÊN GIA TÂM LÝ` | `PSYCHOLOGIST` | `심리학자` | `心理学者` |
| `NGƯỜI BÌNH THƯỜNG` | `ORDINARY PERSON` | `일반인` | `一般人` |
| `ĐẶC VỤ FBI` | `FBI AGENT` | `연방수사국` | `FBI特別捜査官` |
| `CẢNH SÁT ĐỊA PHƯƠNG` | `LOCAL POLICE` | `지역경찰` | `地方警察` |

`**[BGM]:**` và `**[SFX]:**` **giữ nguyên tiếng Anh** ở mọi bản — bộ dựng video khớp theo nhãn này.

**Vài bẫy riêng khi dịch:**
- Dấu `:` trong tiếng Việt nối hai mệnh đề **trong một câu** — bản dịch phải giữ dấu `:` (đổi thành `.` sẽ sinh thêm câu và làm lệch QC).
- Dấu `…` / `...` giữa câu → dùng ` – ` (sau dấu chấm lửng mà có Hangul, parser sẽ cắt sai câu).
- Trích dẫn nguyên văn (tiếng Anh) giữ **nguyên tiếng Anh** trong `‘…’`, phần giải nghĩa tiếng Hàn đặt **trước** và nối bằng ` – `.
- Tên riêng / địa danh giữ **chữ Latin** (không chuyển sang Hán tự); số viết bằng **chữ số Ả Rập**; lời đọc chỉ dùng **Hangul + Latin + số**, không dùng chữ Hán.
- `tts_sentences.py` chỉ đổi số thành chữ cho bản **tiếng Việt** (G11) — bản EN/KO/JA giữ nguyên chữ số.

**QC bản KO:** `py -3 .work/_qc_ko_parity.py <file_vn.md> <file_ko.md>` — phải in `PASS` (đối chiếu hồi, thứ tự element, vai, số câu, số giây nghỉ, mọi con số, tên riêng, tỉ lệ Hangul). Chạy cả 29 tập: `py -3 .work/_qc_ko_all.py`.

## A3. Quy trình chuẩn — lệnh chạy và thời gian đo được

Chạy từ `D:\TEST\Gax\Audi`, đặt `PYTHONIOENCODING=utf-8`. Connector gọi qua `mcode-tools` (có sẵn tại `C:\Users\ADMIN\.minimax\bin`).

| Bước | Lệnh | Đầu ra | Thời gian Tập 01 |
|---|---|---|---|
| **0. Một lần cho series** | `make_logo.py` · `make_intro.py` · `make_cast_cutouts.py` · `voice_audition.py` | Logo, intro, 5 linh thú, chọn giọng | đã xong |
| **1. Tách kịch bản** | `py -3 .work/parse_kichban.py 01_KICH_BAN/TapXX/kichban_tapXX.md .work/script_tapXX.json` | lượt nói, câu | < 1 s |
| **1b. Diễn xuất** | `py -3 .work/make_acting_tapXX.py` (theo G1–G8 của A4.2) | `.work/acting_tapXX.json` | < 1 s |
| **2. Đọc giọng** | `py -3 .work/tts_sentences.py` (số tự đổi sang chữ — G11) | `.work/audio_s_tXX/*.mp3` | Tập 02: 215 câu / ~12 phút |
| **2b. Nghe theo vai (G10)** | `py -3 .work/voice_role_check.py` — **không đạt thì dừng** | `<EP_DIR>/thu_giong_kiem_vai/report.md` | ~3 phút |
| **3. Âm thanh tổng** | `py -3 .work/build_audio3.py` | `TapXX_master.mp3`, `timeline_s_tXX.json`, `stems_tXX/` | Tập 02 (stereo, nền dài): ~12 phút |
| **4. Kiểm tra âm thanh** | lệnh A9.1 | — | 1 phút |
| **5. Nền mới (nếu cần)** | `py -3 .work/gen_images.py .work/bg_jobs_tapXX.json` | `assets/bg/*.png` | ~1 phút / ảnh |
| **6. Bảng shot** | AI viết mục 6 của hồ sơ tập → `py -3 .work/parse_shots.py` | `.work/shots.json` | < 1 s |
| **7. Kiểm tra chữ** | lệnh A9.2 | — | < 1 s |
| **8. Ảnh tĩnh duyệt — MỌI shot** | `py -3 .work/build_video3.py --stills <giữa mỗi shot>`; ghép 16 ảnh/tờ để soi (A9.3) | `.work/video3_tXX/stills/` | 151 ảnh / ~2 phút |
| **9. Dựng hình** | `py -3 .work/build_video3.py --workers 6` | `.work/video3_tXX/picture.mp4` | Tập 01: 1.133 s / ~22 phút · Tập 02: 1.604 s / **~85 phút** |
| **10. Sửa cục bộ** | `py -3 .work/rerender_part.py K` (K = 0…5) | dựng lại 1/6 tập rồi ghép | ~5 phút / phần |
| **11. Phụ đề** | `py -3 .work/subtitles.py` | `TapXX.srt` | < 1 s |
| **12. Đóng gói** | `py -3 .work/package.py --mux` | `.mp4`, thumbnail, mô tả, nguồn | 1 phút |

**Chọn tập (từ 22/10/2026):** đặt `AE_EP=02` (03…) trước mọi lệnh. Mọi thông số riêng của tập — kịch bản, thư mục, N1/N2, file diễn xuất, bảng âm thanh, mốc nhạc, cảnh ghép, tên hồi, câu cần nguồn — khai **một chỗ** trong `EPISODES` của `.work/edition.py`. File trung gian của tập ≠ 01 có hậu tố `_tXX` nên không ghi đè tập khác. Không có `AE_EP` = Tập 01 như cũ.

**Bản ngôn ngữ khác (từ 22/10/2026):** đặt `AE_LANG=en` trước mọi lệnh trên để chạy bản tiếng Anh.
- Đường dẫn, giọng và chữ giao diện nằm trong `.work/edition.py`. Mọi đầu ra có hậu tố `_EN` hoặc nằm trong `02_SAN_XUAT/TapXX_EN/`.
- Bảng shot EN được sinh từ bảng VN bằng `.work/_build_plan_en.py`: giữ cột Câu, Vai, Mẫu, Nền và lời mô tả beat tiếng Việt (renderer dò từ khoá tiếng Việt); chỉ thay chữ màn hình và cụm `ở "…"`.
- QC giọng toàn tập: `py -3 .work/qc_asr.py`.
- **Diễn xuất từng câu (chống đọc đều đều):** `.work/acting_EN.json`, mỗi câu gồm `[cảm xúc, độ lệch tốc độ, cao độ −12…12, lời đọc riêng]`.
  - Thẻ ngắt `<#0.4#>` được engine hiểu, không đọc thành chữ.
  - Quy tắc tự động: `...` nghỉ 0,45 s · ` — ` nghỉ 0,15 s · `: ` trước chữ hoa nghỉ 0,3 s.
  - Sau câu buồn hoặc căng thẳng nghỉ thêm 0,2 s.
- **SFX theo shot:** `.work/make_sfx2.py` (25 âm tự tổng hợp) cộng `.work/sfx_shots_EN.json` (shot, file, mốc, lệch, dB).
  - Cần chạy 2 lượt: `build_audio3` → `parse_shots` → `build_audio3`.
- Mẫu đầu tiên: `02_SAN_XUAT/Tap01_EN/README.md`.
| **13. Kiểm tra cuối** | lệnh A9.3 + A9.4 | — | ~5 phút |

**Tính phần cần dựng lại (bước 10):** `bước = ceil(tổng_khung / 6)`; khung = `giây × 30`; phần = `khung // bước`. Ví dụ Tập 01: bước 5.668 khung ≈ 188,9 s → giây 829 thuộc **phần 4**. *(Tập 01 từng tính nhầm thành phần 3 — luôn tính bằng công thức.)*

Mọi lệnh đặt `AE_EP=XX` trước (PowerShell: `$env:AE_EP="02"`); Tập 01 không cần.

**Mốc duyệt với người dùng** (người dùng có thể bỏ qua): sau bước 2b (nghe giọng theo vai), sau bước 8 (ảnh tĩnh mọi shot), sau bước 13 (video cuối).

## A4. Âm thanh chuẩn

### A4.1 Năm giọng — BỘ A (chốt 23/10/2026, dùng từ Tập 02)

Ba vai chính phải **khác hẳn nhau** về chất giọng:

| Nhân vật | Chất giọng yêu cầu | `voice_id` | `speed` gốc | F0 đo | **CER đo (T2, 20 câu)** | Kiểm |
|---|---|---|---:|---:|---:|---|
| Cú · Host | **Trầm ấm**, gần, kiểu podcast đêm | `English_CaptivatingStoryteller` | 0,90 | 102,6 Hz | **0,1%** · 0/20 vượt ngưỡng | Hợp vai 9/10 · ổn định 4 cảm xúc → 1 người |
| Sói · Điều tra viên | **Lạnh lùng**, phẳng, chính xác | `Korean_ColdYoungMan` | 0,95 | 140 Hz | **3,1%** · max **28,6%** ⚠ | 8,5/10 · ổn định → 1 người |
| Cáo · Chuyên gia | **Nhấn mạnh**, chín chắn, phân tích (nữ) | `English_AssertiveQueen` | 0,92 | 207,8 Hz | 0,9% | 8,5/10 · ổn định → 1 người |
| Cừu · N1 | Nữ trẻ, hiền | `Vietnamese_kindhearted_girl` | 0,95 | 248,1 Hz | 0,0% | |
| Mèo · N2 | Nữ, tò mò | `English_captivating_female1` | 0,95 | 230,3 Hz | 0,0% | |

- **Ba bộ giọng của kênh.** Bản VN dùng **bộ A** (trên). Bản EN dùng bộ riêng: `English_magnetic_voiced_man` 0,95 · `English_Trustworth_Man` 0,97 · `English_Wiselady` 0,95 · `English_SentimentalLady` 0,95 · `English_captivating_female1` 0,95. **Tập 01 ghim bộ riêng** (`audiobook_male_1` 0,90 · `male-qn-qingse` 0,95 · `audiobook_female_1` 0,92) để dựng lại ra đúng bản đã xuất.
- Khai ở `edition.py`: `CAST` (mặc định bản VN) · `EPISODES["01"]["cast"]` (ghim Tập 01). **Code KHÔNG gọi `get_voice_list`** — `CAST` là hardcode.
- Hồ sơ đầy đủ: `02_SAN_XUAT/Tap02/BaoCao_GiongDoc_Tap02.md` §4. File nghe: `02_SAN_XUAT/Tap02/thu_giong_vai/`.
- **Ba vai chính nghe mù xen kẽ (Tập 07):** gán đúng S1/S2/S3, tách bạch **10/10**.

**Vì sao bỏ bộ cũ** (phản hồi người dùng về Tập 02: "Host nghe như 3 người", "giọng nam giống hệt nhau"):
- `audiobook_male_1` **đổi danh tính** mỗi khi đổi cảm xúc hoặc cao độ: 7 thiết lập → 6 "người".
- Hai giọng nam cùng baritone miền Nam, chỉ cách nhau ~2 nửa cung.

**Giọng đã thử và loại:**
- Điểm hợp vai cao nhưng **không ổn định**: `English_Deep-VoicedGentleman` (4 người), `English_ReservedYoungMan` (3), `English_MatureBoss` (2), `Korean_IntellectualMan` (2).
- Đổi người giữa 2 câu neutral: `English_ConfidentWoman`, `English_Wiselady`.
- Sai thanh điệu: `Chinese (Mandarin)_News_Anchor`.

**Kho giọng chỉ có MỘT giọng tiếng Việt gốc** (`Vietnamese_kindhearted_girl`, nữ) — chỉ đọc cho vai N1, chiếm **2% số câu**. 3 vai chính đọc tiếng Việt bằng giọng `English_`/`Korean_`: **giọng hệ thống MiniMax đa ngôn ngữ** — tiền tố là ngôn ngữ *gốc* của giọng, KHÔNG giới hạn ngôn ngữ đầu vào (endpoint TTS không có tham số `language`; engine tự nhận diện ngôn ngữ từ văn bản). Đổi giọng ở tập sau thì phải qua đủ **G8–G10 + G12**.

### A4.1b ĐO CHẤT LƯỢNG PHÁT ÂM TIẾNG VIỆT — CER (đo 27/10/2026, Tập 02)

**Vì sao phải có mục này:** G8–G10 đo **danh tính** và **tách bạch** của giọng, nhưng **không đo giọng đọc tiếng Việt có đúng không**. Đo 27/10 mới phát hiện `Korean_ColdYoungMan` (vai Điều tra viên) đọc tiếng Việt **sai thanh điệu nặng**: *"Thứ hắn lấy đi"* → nghe ra *"Thương hiệu Han Lady"* (3 lượt ASR khác nhau, đều sai) → CER 28%.

### Cách đo (tái lập được)

| Bước | Cách làm |
|---|---|
| Mẫu | 20 câu của **đúng vai đó**, dùng **đúng `emotion` + `speed` của production** (đọc từ `tts_manifest_t02.json`) |
| Chuẩn | Trường `text` của manifest — đúng thứ đã gửi cho engine |
| ASR | `connector__matrix__listen_audio` + hàm `cer()` sẵn có trong `.work/voice_audition.py` |
| ⚠ Chuẩn hoá | **Áp `vi_numbers()` cho CẢ HAI Vế.** Chuẩn là CHỮ (`"tám mươi tám"`), ASR trả SỐ (`"88"`) — không chuẩn hoá thì CER phình to giả (một câu đúng bị tính **21%**, một câu **300%**) |
| ⚠ Lọc lỗi | Câu bị **bộ lọc Gemini chặn** (nội dung nhạy cảm) → `transcription` dính đuôi *"This request was blocked…"* mà `code` vẫn `0`. Cắt đuôi + **loại câu khỏi mẫu** |
| Mẫu nhỏ | Câu < 12 từ → 1 lỗi = 20%+ CER. Tách riêng khi báo cáo |
| Lặp lại | ASR **không tất định**: 3/9 câu vượt ngưỡng đổi kết quả giữa 2 lượt ⇒ **≥ 2 lượt** cho mọi kết luận về 1 câu |
| Tiết kiệm | Nếu audio TTS **đã xuất** → đo thẳng trên file thành phẩm, **không cần tổng hợp lại** |

### Kết quả — 3 vai, cùng 20 câu, audio thành phẩm Tập 02

| Vai | `voice_id` | CER tb | median | max | >2% | F0 | cách Host |
|---|---|---:|---:|---:|---:|---:|---:|
| Host | `English_CaptivatingStoryteller` | **0,1%** | 0,0% | 2,0% | **0/20** | 103 Hz | — |
| **Điều tra viên** | **`Korean_ColdYoungMan`** | **3,1%** | 0,0% | **28,6%** | 4/20 | 140 Hz | +5,4 nc |
| Chuyên gia | `English_AssertiveQueen` | 0,9% | 0,0% | 5,4% | 4/20 | 203 Hz | +9,4 nc |

### Kết quả — 5 ứng viên thay vai Điều tra viên (cùng 20 câu)

| `voice_id` | CER tb | max | F0 | cách Host | dao động F0 | G8 | G9 | trong catalog |
|---|---:|---:|---:|---:|---:|---|---|---|
| **`English_Diligent_Man`** | **0,6%** | 6,0% | 158 Hz | **+7,7 nc** | 55 Hz | ✅ 1 | 9/10 | ✅ |
| `male-qn-qingse` | 0,6% | 9,5% | 137 Hz | +5,0 nc | 44 Hz | ✅ 1 | **10/10** | ❌ *nhưng còn sống* |
| `English_DecentYoungMan` | 0,6% | 4,0% | 128 Hz | **+3,8 nc ✗** | 75 Hz | ✅ 1 | **10/10** | ✅ |
| `Korean_CockyGuy` | 1,6% | 20,0% | 152 Hz | +6,8 nc | 76 Hz | ✅ 1 | 9/10 | ✅ |
| `Korean_ColdYoungMan` *(đang dùng)* | 3,1% | 28,6% | 140 Hz | +5,4 nc | **17 Hz** | — | 8–9/10 | ✅ |

- **G8/G9 đo bằng `audios_understand` mù** (đúng cách `voice_role_check.py`): G8 = gộp 12 câu của 1 giọng → "SPEAKERS: n" (đạt = 1). G9 = xen kẽ Host · D · C (12 câu) → "SPEAKERS: n" + rating tách bạch 1–10.
- **Giọng đang dùng bị chấm thấp nhất về tách bạch (8–9/10)**: *"cả ba chia sẻ cùng một nhịp đọc tin không cảm xúc"*. Cả 3 vai đều là giọng Hàn Quốc/English.
- **`audiobook_male_1`** loại: F0 116 Hz chỉ cách Host **+2,0 nc** (G9 fail) + đã biết đổi danh tính khi đổi cảm xúc.
- **`English_DecentYoungMan`** loại: F0 128 Hz → chỉ **+3,8 nc** (< 4 của G9).
- **Kiểm tra sống của giọng legacy** (không có trong danh mục 332): `male-qn-qingse` ✅ · `audiobook_male_1` ✅ (27/10/2026, gọi TTS thật). **Vắng mặt trong danh mục ≠ chết.**
- **Phạm vi áp dụng**: Tập 03–07 đã có master (đã xuất) · **Tập 08–29 chưa có master** → đổi giọng vai D từ Tập 08 **không tốn dựng lại video nào đã xuất**.

Báo cáo đầy đủ: `90_LUU_TRU/BaoCao_SangLocGiongDieuTraVien_20261027.md` · đo bộ A: `90_LUU_TRU/BaoCao_CER_GiongBoA_Tap02_20261027.md`.

### A4.2 Diễn xuất từng câu — BẮT BUỘC từ Tập 02

**Vì sao:** khán giả Tập 01 phản hồi "mọi giọng đều đều, không điểm nhấn, nghe buồn ngủ". Đo lại Tập 01: Sói và Cáo đọc 100% câu `neutral`, cao độ giữa các câu chỉ lệch ~0,85 nửa cung, 3,5–3,8 âm tiết/giây. Nguyên nhân: cảm xúc chỉ đổi theo **cả lượt nói** (bảng từ khoá A4.2b), mọi câu trong lượt đọc y hệt nhau.

**Cách làm:** mỗi tập có `.work/make_acting_tapXX.py` → `.work/acting_tapXX.json`, khai ở `EPISODES[..]["acting"]` trong `edition.py`. Mỗi câu: `[cảm xúc, lệch tốc độ, cao độ, lời đọc riêng | null]`, cộng `_pause_after` (giây nghỉ thêm **sau** câu). `tts_sentences.py` đọc file này; `build_audio3.py` cộng `_pause_after` vào khoảng nghỉ.

**Quy tắc (rút từ 3 vòng thử, 74 bản đọc, 23/10/2026 — `02_SAN_XUAT/Tap02/AmThanh_Tap02.md` §2.4):**

| # | Quy tắc | Giá trị | Bằng chứng |
|---|---|---|---|
| G1 | **Không đặt `...` hay thẻ ngắt `<#s#>` giữa câu.** Tiếng Việt có thanh điệu: ngắt giữa câu làm ngữ điệu vụn, "như robot" | Duy nhất: **một** thẻ `<#0.35#>` sau dấu `:` đứng trước câu trích “…” | Có ngắt giữa câu: nhịp 3–4/10, thắng 2/7 câu. Không ngắt: nhịp 5–6/10, thắng 7/7 |
| G2 | **Kịch tính đặt GIỮA các câu**, không trong câu | `_pause_after` 0,2–1,2 s sau câu hé lộ, câu "đóng đinh", cuối nấc thang | Tập 02: 70 chỗ, 27 s |
| G3 | **Cảm xúc đổi theo nhịp truyện**, không theo lượt — **chỉ trong bộ cảm xúc an toàn của giọng (G8)** | Dẫn chuyện `neutral` → căng `fearful` → hé lộ `surprised` → lắng `sad`; câu hỏi `surprised`. Bộ A: chỉ `neutral · sad · fearful · surprised` | Tập 02 (bản sửa): neutral 160 · sad 28 · fearful 14 · surprised 13 |
| G4 | **Tốc độ chỉ chậm vừa** | Lệch so với tốc độ gốc của vai trong **−0,06 … +0,02** | `sad`/`fearful` tự làm máy đọc chậm; cộng thêm −0,1 làm câu dài gấp đôi |
| G5 | **Cao độ = 0** (sửa 23/10; bản cũ −4…+3 gây lỗi "Host thành 3 người") | Không dùng tham số `pitch`. Biểu cảm lấy từ cảm xúc an toàn, tốc độ, khoảng lặng, nhạc, tiếng động | `audiobook_male_1`: cao độ +1 → F0 +4,5 nửa cung **và đổi người**; −1/−2 → đổi sang giọng miền Bắc khàn |
| G6 | **Lời đọc riêng chỉ để sửa cách đọc, không đổi chữ** | Phụ đề và chữ trên hình luôn lấy câu gốc; lời đọc riêng dựng lại từ câu gốc, giữ nguyên dấu câu | Kiểm bằng script: so từng chữ (bỏ dấu câu và thẻ) với câu gốc |
| G7 | **Không để giọng Việt đọc tiếng Anh dài** | Bỏ chú thích tiếng Anh trong ngoặc khỏi lời đọc khi không cần (vd. `(Signature)`); câu trích tiếng Anh dịch sang tiếng Việt | |
| G8 | **Mỗi giọng có bộ tham số an toàn** — chỉ dùng thiết lập mà giọng vẫn là CÙNG MỘT NGƯỜI | Thử: cùng một câu × mọi cảm xúc/cao độ định dùng; ghép vào một file, hỏi `audios_understand` "mấy người?" → phải ra **1** | Bộ A: 4 cảm xúc → 1 người. Bị loại: Deep-VoicedGentleman 4 người, ReservedYoungMan 3… |
| G9 | **Các vai phải khác hẳn nhau** | Hai giọng cùng giới cách nhau **≥ 4 nửa cung** F0 trung vị và khác rõ chất giọng; file xen kẽ 3 vai × 2 câu, nghe mù phải gán **đúng 100%** | Bộ A: 6/6, tách bạch 9/10; nam–nam cách ~6 nửa cung |
| G10 | **Nghe liền theo vai trước khi dựng** | Sau khi đọc toàn tập: mỗi vai ghép 10–12 câu rải đều → nghe mù phải ra **1 người**; đạt mới chạy `build_audio3` | Lỗi Tập 02 lọt qua vì chỉ so các bản của CÙNG MỘT CÂU |
| G11 | **Số đọc bằng chữ tiếng Việt** (tự động) | `tts_sentences.vi_numbers()` đổi mọi chữ số trong LỜI ĐỌC sang chữ: "1.400" → "một nghìn bốn trăm" (dấu chấm giữa nhóm 3 số = dấu nghìn), "2009" → "hai nghìn không trăm lẻ chín", "21" → "hai mươi mốt", "Elizabeth II" → "Elizabeth Đệ nhị". Phụ đề và chữ trên hình giữ chữ số | Tập 02: giọng đa ngôn ngữ đọc "1.400" thành "một phẩy bốn trăm" (người dùng phát hiện) |

**Trước khi đọc toàn tập:** chạy `.work/voice_act_test_tapXX.py` cho 5–7 câu then chốt: bản cũ, bản diễn xuất, bản với giọng thay thế. Kiểm ba thứ:
- **CER** bằng `listen_audio`.
- **Thẻ ngắt có bị đọc thành tiếng không.**
- **Chấm so sánh** bằng `audios_understand`: ghép các bản của **cùng một câu** vào một file, hỏi về biểu cảm, nhịp, thanh điệu, độ hợp phim tài liệu.

Người dùng nghe file so sánh để chốt.

**Lưu ý khi đọc số đo:**
- CER "13%" thường do bộ nhận dạng viết số ("4 tiếng 40 phút"); kết quả "290%" là do bộ lọc của dịch vụ nhận dạng chặn. Phải đọc bản chép lại trước khi kết luận giọng sai.
- Dải cao độ **trong** câu tiếng Việt luôn rộng (11–15 nửa cung, do thanh điệu). Chỉ số "đều đều" thật là cao độ và tốc độ **giữa** các câu.

### A4.2b Chỉ dẫn → tham số TTS (cách cũ, chỉ dùng khi tập không có file diễn xuất)

`emotion` chỉ nhận `happy · sad · angry · fearful · disgusted · surprised · neutral`.

| Chỉ dẫn chứa | `emotion` | `speed` cộng thêm |
|---|---|---:|
| "xúc động" | `sad` | 0 |
| "Đẩy nhanh" | `neutral` | +0,04 |
| "sắc lạnh" · "đanh thép" | `neutral` | +0,02 |
| "trầm lắng" · "trăn trở" | `sad` | −0,02 |
| "Hạ giọng trầm, chậm rãi" | `neutral` | −0,04 |
| "trầm ấm" · "chậm, trầm" | `neutral` | −0,02 |
| (khác / không ghi) | `neutral` | 0 |

Lượt không có chỉ dẫn kế thừa lượt trước cùng vai, cùng hồi.

### A4.3 Khoảng ngắt

| Vị trí | Độ dài |
|---|---:|
| Giữa 2 câu cùng lượt | 0,35 s |
| Sau câu hỏi | 0,60 s |
| Đổi người nói | 0,70 s |
| `[Nghỉ X giây]` | X, tối đa 2,5 s (khoảng nghỉ thay cho khoảng ngắt) |
| Ranh giới hồi | 2,0 s |

### A4.4 Nhạc và lớp nền

| Lớp | Quy tắc |
|---|---|
| Intro | `bgm_music_box.mp3` trọn 22,41 s, đặt ở t = 0 trong master, thấp hơn lời 4 dB |
| Drone nối Hồi 1 | `bgm_sub_drone` vào từ 19,5 s, −40 → −26 dB, tắt dần khi nhạc Hồi 1 vào |
| Lời đầu tiên | 23,0 s |
| Nhạc theo hồi | 1 cello · 2 piano_minimal + _v2 · 3 ambient (đoạn đã cắt) · 4 violin · 5 piano_warm. **Bắt đầu tại ranh giới hồi** (2 s trước lời đầu hồi) để thẻ chương có nhạc |
| Mức nhạc | −26 dB khi có lời, −14 dB ở khoảng nghỉ (tự hạ theo hoạt động giọng) |
| Nền trầm (V4) | `bgm_ambient_deep.mp3` **chỉ đoạn 0,5–13,4 s** (file gốc có 3 khoảng câm), lặp xuyên tập ở −34 dB |
| "Im lặng tuyệt đối" trong kịch bản | Tắt nhạc có giai điệu, giữ nền trầm |
| SFX | Tiếng "Tách" máy ghi âm (tổng hợp bằng code trong `build_audio3.py`) + **11 file SFX trong `assets/sfx/`** (tự tổng hợp bằng `.work/make_sfx.py`, không tải file ngoài). Đặt theo bảng `SFX_CUES` trong `build_audio3.py`: `offset` âm = đặt trước mốc để nối vào câu thoại kế tiếp. Mức tính theo RMS lời, hiệu chuẩn bằng cách nghe thật trong bản thành phẩm, neo theo tiếng "Tách" (−6 dB): dấu câu to (búa tòa +1, gấp hồ sơ −8, khóa cửa −2), sự kiện (−2…−8), nền (−12…−18). Thiếu file → bỏ qua, không làm hỏng cả tập |
| **Nền môi trường** (từ Tập 02) | Bảng `sfx_tapXX.json` → `ambience`: [từ câu, đến câu, file, dB]. Chạy **liên tục** dưới lời theo cảnh (gió tuyết, phòng thẩm vấn, tầng hầm…), −27…−38 dB so với lời, hạ thêm 4 dB khi có lời, mờ vào/ra 1,5 s, nối vòng hoà chồng 1 s. **Mọi đoạn nhạc bị tắt phải có nền bên dưới** (nếu không sẽ vi phạm V4 — Tập 02 từng câm 0,6 s ở lời kết) |
| **Tiếng động theo câu** (từ Tập 02) | `sfx_tapXX.json` → `cues`: [mốc câu/SFX, start\|end, lệch, file, dB]. Tập 02: 37 tiếng (gấp 2,6 lần Tập 01/phút). Tiếng tải về phải **cắt đúng đoạn** và nghe kiểm trước khi nhập (bẫy #20) |
| **Tắt nhạc ở câu hé lộ** | `sfx_tapXX.json` → `music_drop`: tắt nhạc có giai điệu, giữ nền môi trường + nền trầm |
| **Stereo** | Lớp nền/tiếng động trộn stereo (tiếng có vị trí trái/phải và vang theo không gian); lời và nhạc giữa |
| Kết | Piano_warm 6 s mờ dần, 3 s cuối |
| Chuẩn hoá | `loudnorm I=-16:TP=-1.5:LRA=11` **2 lượt, `linear=true`** |

## A5. Hệ thống đồ hoạ chuẩn

### A5.1 Phong cách
Graphic Novel Noir: nét mực đậm, chiaroscuro, viền sáng màu vai, hạt phim. Hai tầng nhân vật: **linh thú dẫn chuyện ở góc** / **người trong vụ án dạng bóng trong cảnh**.

### A5.2 Bảng màu

| Token | Hex | | Token | Hex |
|---|---|---|---|---|
| `ink` | `#0E0E11` | | `amber` · Cú | `#E2B467` |
| `night` | `#151A2A` | | `cold` · Sói | `#86A9CC` |
| `slate` (badge) | `#1C1F2B` | | `violet` · Cáo | `#A99BD6` |
| `paper` / `paper_ink` | `#E6DED0` / `#1C1B1F` | | `sand` · Cừu | `#D9B99B` |
| `text` / `muted` | `#F2EFE9` / `#9C988F` | | `cyan` · Mèo | `#6E8CA0` |
| `pink` / `pink_deep` (**chỉ vụ án**) | `#E8A0BF` / `#A85273` | | `red` (gạch bỏ, cờ, dấu mộc) | `#C8423A` |

### A5.3 Font — **đã đo độ phủ tiếng Việt**

| Vai trò | Font | Ghi chú |
|---|---|---|
| Tiêu đề, nhãn, phụ | Segoe UI Bold / Semibold / Regular | đủ 100% |
| Trích dẫn, lời kể | **Cambria Italic** `cambriai.ttf` | đủ 100% |
| Tiêu đề chương, thẻ hồ sơ | **Cambria** / **Cambria Bold** | đủ 100% |
| Hồ sơ, dữ liệu (Sói) | Consolas | đủ 100% |
| Con số lớn | Bahnschrift | **thiếu "ỷ" và "−"** → chỉ dùng cho chữ số, dấu trừ viết "-" |
| Logo "AMBER EYES" | Georgia | **Georgia thiếu 92 ký tự tiếng Việt — cấm dùng cho chữ có dấu** |

Kiểm tra font mới: script đo ký tự thiếu ở A9.2. Chữ ≥ 24 px; ≤ 3 khối chữ/khung; mọi chữ do Pillow vẽ, không để AI vẽ chữ.

### A5.4 Bố cục khung 1920×1080

- Nền 2112×1188 (dư 10% cho camera). Lề 96 px trái/phải, 72 px trên/dưới; tránh 140 px đáy.
- **Badge người nói:** góc trên-trái (64, 56), 470×124, P0 88 px + tên + chức danh + sóng âm thật (từ `stems/`). Hiện suốt mọi lượt của cả 5 vai; trượt vào 0,3 s.
- **Bán thân:** góc dưới-trái, 420×500, thở 1,000↔1,006 (4 s), viền sáng nhấp ở đầu câu. Hiện ở câu đầu mỗi lượt (3–6 s) và các shot `🅑`. Lần đầu mỗi vai có thẻ giới thiệu (tên · chức danh · *Nhân vật minh hoạ · giọng đọc AI*) 4 s.
- **Vùng cấm chữ khi có bán thân:** `x < 560`, `y > 560` → mẫu T1 / T5-ngày / T6 tự dời khối chữ sang phải.
- **Lời mời (→X):** badge mờ của người sắp nói ở góc trên-phải, chữ *TIẾP THEO*.
- **Hai badge:** đoạn hai vai cùng bàn (Cáo trái, Sói phải; người đang nói sáng).
- **Dàn khách mời:** 5 biểu tượng 150 px cách nhau 250 px ở `y = 300`, tên 18 px.
- **Watermark:** logo 96 px, 35%, góc dưới-phải; ẩn trong intro và thẻ chương ở khoảng nghỉ.

### A5.5 Mười một mẫu khung (đã cài trong `build_video3.py`)

| Mẫu | Tên | Bố cục chuẩn |
|---|---|---|
| T1 | Toàn cảnh | Lớp tối 45% đáy; khối chữ đáy `y = 900`, `x = 96` (hoặc 560) |
| T2 | Thẻ hồ sơ | Giấy rộng 860, **cao theo chữ** (≥ 340), xoay −1,5°, tại `x = 960`; nhãn Consolas đỏ, tiêu đề Cambria Bold, dòng Consolas; **dấu mộc đặt ngay dưới dòng chữ cuối** |
| T3 | Chia đôi / so sánh | Vạch màu vai `x = 920`, chữ phải `x = 970`; biến thể so sánh phủ tối cả khung, cột phải hiện ở câu 2 |
| T4 | Trích dẫn / lời kể | Phủ tối 70%; dấu “ màu vai; Cambria Italic 46–54 px tại `x = 600`, rộng 1180 |
| T5 | Con số | Bahnschrift 250 px đếm lên 1,2 s tại `x = 760`; biến thể ngày gõ từng ký tự |
| T6 | Dòng thời gian | Trục `y = 520`; mốc chấm hồng + nhãn so le trên/dưới; mỗi câu một mốc |
| T7 | Tuyến đường | 2 ghim + đường đứt nét cong tự vẽ 1,5 s |
| T8 | Danh sách | Mục ở `x = 980`, hàng 88 px; biến thể **gạch bỏ** (mỗi câu gạch một mục) và **cờ đỏ** (4 cờ, tô dần) |
| T9 | Thuật ngữ | Vạch màu vai + tên Việt 70 px + tên Anh Consolas 32 px tại `x = 760` |
| T10 | Thẻ chương | Nền `void`; `HỒI 0X` Consolas + tên hồi Cambria 70 px |
| T11 | Bài đăng mạng xã hội | Thẻ trung tính có nhãn MINH HOẠ, không logo, dòng nội dung mờ không đọc được |

### A5.6 Chuyển động và hoàn thiện
- Camera: `push` 1,00→1,05 (mặc định) · `pull` · `pan` · `hero` 1,00→1,10 · `still`.
- Phần tử: mờ dần + nhích 24 px, 0,35 s. Dòng **giữ hình** hiện sẵn mọi thứ (không hiện lại).
- Chuyển cảnh: hoà tan 0,35 s · ✂ cắt · ◼ tối đen 0,6 + 0,6 s.
- Hạt phim + vignette + lệch kênh đỏ 1 px **chỉ trên nền**; chữ, badge, bán thân vẽ sau, sạch.
- Encoder: `libopenh264 -b:v 3000k -maxrate 5000k`; 6 phần ghép bằng `concat -c copy`.

### A5.7 Intro kênh (dùng chung, đã dựng)

`assets/brand/intro_kenh.mov` — chỉ hình, 22,41 s:

| Thời gian | Nội dung |
|---|---|
| 0–4 s | Sợi chỉ đỏ tự vẽ; đôi mắt hổ phách bừng sáng ở 1,5 s; **AMBER EYES** gõ từng chữ; khẩu hiệu *Phân tích tâm lý tội phạm qua những hồ sơ có thật* |
| 4–12,25 s | **Thẻ A — VỀ NỘI DUNG NÀY:** *Nội dung giáo dục, phân tích tâm lý học tội phạm. / Dựa trên tư liệu công khai, nguồn ở phần mô tả. / Không nhằm kết tội hay bôi nhọ bất kỳ ai.* |
| 12,25–20,5 s | **Thẻ B — LƯU Ý TRƯỚC KHI XEM:** *Nội dung không phù hợp cho trẻ em. / Âm thanh và hình ảnh chỉ mang tính minh hoạ. / Không thay thế tư vấn y khoa, tâm lý hay pháp lý.* — 5 vòng màu vai sáng từ 18 s |
| 20,5–22,41 s | Mờ về đen; nền đầu Hồi 1 của từng tập hiện chồng lên |

Nội dung hai thẻ **đã được người dùng chốt** — không tự sửa. Lời miễn trừ không thay được bảo vệ pháp lý thật (A10).

## A6. Tài sản dùng chung (đã có, tập sau dùng lại)

| Nhóm | Đường dẫn | Ghi chú |
|---|---|---|
| Logo, avatar, watermark | `assets/brand/` | Vẽ bằng code (`make_logo.py`), kênh sở hữu trọn vẹn |
| Intro | `assets/brand/intro_kenh.mov` | `make_intro.py`; đổi 5 vòng màu thành biểu tượng linh thú khi cần |
| 5 linh thú | `assets/cast/{H,D,C,N1,N2}/` — `full.png`, `P1.png` (840×1000), `P0.png` (256 tròn) | Tách nền BiRefNet; chưa có P2 |
| 45 nền 16:9 | `assets/bg/*.png` (2112×1188) | Xem danh sách ở Phần B; nhiều cảnh dùng lại được (nhà hồng, bảng ghim, phòng xử, `void`…) |
| Nhạc | `assets/bgm/` (9 file MiniMax) | Lưu ý khoảng câm của `ambient_deep` |
| Hiệu ứng âm thanh | `assets/sfx/` (11 file WAV tự tổng hợp) | `make_sfx.py` — không tải file ngoài nên không vướng bản quyền; dùng lại được cho tập sau |
| Kênh | `assets/brand/channel.json` | Tên, khẩu hiệu, bảng màu, font |
| Ý tưởng các tập sau | `01_KICH_BAN/KHO_Y_TUONG_28_HO_SO.md` | Kho 28 hồ sơ |

## A7. Cách viết bảng shot (mục 6 của hồ sơ tập)

`parse_shots.py` đọc trực tiếp bảng này. Tiêu đề mục phải bắt đầu bằng `## 6. DANH SÁCH SHOT`; bảng kết thúc trước dòng bắt đầu bằng `**Tổng:`.

**Cột:** `Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | chuyển cảnh`

| Cột | Cú pháp |
|---|---|
| Shot | `H-NN` (H = số hồi) |
| Câu | `` `1.11#3`–`#4` `` (khoảng câu trong một phần tử) · `` `1.04` (nghỉ 2 s) `` · `nghỉ chuyển hồi (2 s)` · `` `1.01`–`1.02` `` (mở đầu) |
| Vai | `H` · `D` · `C` · `N1` · `N2` · `—` (không lời) |
| Mẫu | `T1`…`T11`, thêm chữ: `ngày`, `gạch bỏ`, `cờ`, `lời kể`, `so sánh`, `hero` |
| Nền + bóng | Tên nền trong backtick, phải có file `assets/bg/<tên>.png`; camera `` `pull` `` `` `pan` `` `` `still` `` |
| Chữ | `**tiêu đề**` · `*nhãn / dòng phụ*` · `“trích nguyên văn”` · ` → ` tách đoạn hiện sau · `` `#k`: `` đoạn hiện ở câu k · mục danh sách cách nhau ` · ` |
| Beat | `ở "cụm từ trong câu"` → thời điểm theo vị trí cụm từ |
| Nhân vật | `✦` lần đầu · `🅑` thêm bán thân · `⊘` tắt bán thân · `→D` / `→C+D` lời mời · `hai badge` · `dàn khách mời` |
| Chuyển cảnh | trống = hoà tan · `✂` · `◼` |

**Dòng không có câu và không có mẫu** (ví dụ `` `1.04` (nghỉ) `` với mẫu `—`) là **dòng giữ hình**: kế thừa nền và chữ của shot trước. Shot không ghi nền dùng lại nền shot trước.

**Cảnh ghép "nền + bóng người"** (ví dụ phòng thẩm vấn + Gypsy đứng) được tạo sẵn thành một ảnh và khai trong `COMBO` của `parse_shots.py` (A12). Nền đổi trong shot khai trong `BG2`; ảnh nhỏ ghim lên bảng khai trong `INSET`.

**Nguyên tắc biên kịch hình:** mỗi shot 3–15 s; câu > 15 s cần beat mỗi ≤ 7 s; tắt bán thân `⊘` ở khoảnh khắc nặng nề nhất; vai nào nói thì đồ hoạ theo "ngôn ngữ" của vai đó (Sói: hồ sơ, bảng ghim, dòng thời gian · Cáo: thuật ngữ, sơ đồ, so sánh · Người dân: lời kể · Host: cảnh toàn khung).

## A8. Tạo ảnh nền mới

- Công cụ: `connector__matrix__generate_image`, 16:9, 2K, 4 ảnh/lần (~1 phút/ảnh). Ảnh cùng bối cảnh tạo bằng **ảnh tham chiếu** (`"ref"` → script tự `upload-temp-url`).
- Prompt = phong cách chung + mô tả + phần cấm (đã cài sẵn trong `gen_images.py`): `no text, no letters, no numbers, no signs, no labels, no logos, no watermark, no frame, no letterbox bars`.
- Người trong vụ án: `seen from behind`, `face completely hidden in deep shadow, no facial features`; nạn nhân viết là `slender young woman`, không phải trẻ em.
- Không đưa địa chỉ, tên đường vào prompt (AI sẽ vẽ biển tên).
- Script tự cắt viền đen; **viền sáng (trắng, be) phải cắt tay** như Tập 01 (`empty_room`, `fog`).
- **Duyệt bằng mắt mọi ảnh:** chữ lạ, mặt người lộ nét, viền khung, watermark.

## A9. Kiểm tra (chạy và đạt hết trước khi giao)

### A9.1 Âm thanh
```bash
F=.work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe
$F -i .work/audio_master.wav -af silencedetect=n=-60dB:d=0.3 -f null -   # 0 đoạn
$F -i .work/audio_master.wav -af silencedetect=n=-35dB:d=2.5 -f null -   # chỉ được là đoạn "im lặng tuyệt đối" có chủ đích
$F -i .work/audio_master.wav -af ebur128=peak=true -f null -             # -16 ± 1 LUFS
```
Lời đầu tiên 22,8–23,5 s; mỗi câu đúng giọng vai (`tts_manifest.json`).

### A9.2 Chữ và font
- Phủ câu: 100% câu thuộc đúng một shot, đúng thứ tự, cột Vai khớp người nói.
- Mọi con số trên hình có trong câu của shot; mọi câu trích có nguyên văn trong kịch bản.
- Không còn từ bạo lực (danh sách: máu ngoài "ung thư máu", thi thể, sát hại, đòn, trói, bầm, đập, đầu độc, diệt cỏ, bỏ đói, móc áo…).
- Font: đo ký tự tiếng Việt thiếu (`getmask` so với ký tự `\uffff`) — 0 với mọi font chứa chữ có dấu.

### A9.3 Hình
- Ảnh ghép 1 khung giữa mỗi shot → AI xem từng ô: hình đúng câu? biết ai đang nói? chữ đè nhau? mặt người lộ? chữ lạ do AI?
- Sửa → dựng lại đúng phần (công thức A3) → ghép lại.

### A9.4 File cuối
- Hình và tiếng cùng thời lượng (±0,05 s); `ffmpeg -v error -i TapXX_master.mp4 -f null -` không lỗi.

## A10. Đóng gói, pháp lý, kiếm tiền

- **Mô tả:** mẫu trong `package.py` (mốc chương tự tính từ `timeline_s.json`; lưu ý; nguồn; Tổng đài 111). **Không có email liên hệ.**
- **Nguồn:** `nguon_tham_khao.md` liệt kê câu nói về người thật cần link — **người dùng điền, AI không bịa**.
- **Hồ sơ nguồn gốc:** mọi file tạo ra ghi vào `provenance.json` (công cụ, prompt, ngày, điều khoản). Trước khi đăng phải kiểm tra điều khoản thương mại của MiniMax và công cụ tạo ảnh của người dùng.
- **YouTube:** bật "Nội dung bị thay đổi hoặc tổng hợp" · chọn "Không dành cho trẻ em" · không tự bật 18+ · danh mục Giáo dục · tự đánh giá quảng cáo trung thực ("chủ đề gây tranh cãi — thảo luận, không mô tả chi tiết").
- Lời miễn trừ không ngăn được khiếu nại; bảo vệ thật là tài sản có giấy phép + nguồn cho từng dữ kiện.

## A11. Bẫy đã gặp — đừng lặp lại

| # | Bẫy | Cách làm đúng |
|---|---|---|
| 1 | `output_file` có dấu chấm (`1.03_01`) → server coi là đuôi file, mọi câu trùng tên `1.mp3` | Tên không dấu chấm: `s1_03_01` |
| 2 | `--args '<json>'` chứa URL có `&` bị `cmd` cắt | Luôn dùng `--args-file` |
| 3 | `mcode-tools` thỉnh thoảng báo "Network request failed" | Tự thử lại 4 lần, giãn 10/20/30 s (đã cài trong script) |
| 4 | `listen_audio` trả trường `transcription` | Đọc đúng tên trường |
| 5 | Georgia thiếu 92 ký tự tiếng Việt; Bahnschrift thiếu "ỷ", "−" | Cambria / Segoe; đo font trước khi dùng |
| 6 | `bgm_ambient_deep` có khoảng câm bên trong → lặp ra khoảng câm | Chỉ lặp đoạn liên tục |
| 7 | Nhạc hồi mới vào sau thẻ chương → ranh giới hồi hụt tiếng | Nhạc hồi bắt đầu tại ranh giới |
| 8 | Ảnh AI: viền đen, viền trắng, chữ (biển tên, "FEEDING TUBE", "DSM-5"), lộ mặt | Prompt cấm + tự cắt viền + inpaint chữ + duyệt mắt |
| 9 | Tách nền bằng khoá độ sáng làm quần áo tối trong suốt | BiRefNet + lấp lỗ **chỉ khi lỗ có màu** (lỗ đen tuyền là nền) |
| 10 | Giải mã cả intro vào RAM (~4 GB × 6 tiến trình) | Đọc intro tuần tự từng khung |
| 11 | Dòng giữ hình làm chữ, thẻ hiện lại từ đầu | Dòng giữ hình hiện sẵn mọi phần tử |
| 12 | Dấu mộc đặt theo đáy thẻ → đè chữ khi thẻ dài | Đặt theo dòng chữ cuối |
| 13 | Câu trích bị cắt cụt rồi thêm "?" | Kiểm tra nguyên văn (A9.2) |
| 14 | Tính nhầm phần cần dựng lại | Dùng công thức A3 |
| 15 | Ảnh concept từ Pollinations có watermark | Tạo lại không watermark, không tự xoá |
| 16 | Kịch bản ghi 25–27 phút nhưng thực đọc ~19 phút | Ước tính 3,1–3,2 từ/giây; muốn dài hơn phải thêm lời |
| 17 | Giọng đều đều — cảm xúc đặt theo lượt, Sói/Cáo 100% `neutral` (phản hồi khán giả Tập 01) | Diễn xuất từng câu theo A4.2 |
| 18 | Ngắt `...` / `<#s#>` giữa câu làm giọng Việt vụn như robot | Chỉ ngắt GIỮA các câu (`_pause_after`); trong câu chỉ một thẻ trước câu trích (G1) |
| 19 | Dịch vụ TTS lỗi "audio post-processing failed" nhiều giờ (22–23/10); vòng chờ báo nhầm là đã chạy lại | Chỉ coi là chạy lại khi phản hồi có `node_id`; script đã có bộ đệm, chạy lại chỉ đọc câu còn thiếu |
| 20 | Tiếng động tải về là cả bài 14–59 s, hoặc sai nội dung (búa tòa thành tiếng lắc bình xịt, có giọng radio lẫn vào) | Nghe từng file bằng `audios_understand` trước khi nhập; cắt đúng đoạn (`CUTS`), file sai giữ bản code (`KEEP_CODE`) trong `import_sfx_video.py` |
| 21 | Renderer viết theo bảng shot Tập 01: T3 "so sánh" chỉ hiểu một đoạn có ≥ 2 tiêu đề đậm; T8 chỉ đọc đoạn đầu; T7 có nhãn ghim "SPRINGFIELD/WISCONSIN" viết cứng; T7 vẽ mọi đoạn cùng một chỗ (Tập 02: lỗi `IndexError`, chữ bị mất, sai địa danh, đè chữ) | Đã sửa 23/10: T3 nhận `trái → phải` và giữ thứ tự nhãn/tiêu đề, hiện câu trích; T8 đọc mọi đoạn, dòng đậm không đánh số; T7 xếp chồng đoạn, nhãn ghim khai ở `EPISODES[..]["route_pins"]`. **Luôn chạy ảnh tĩnh cho MỌI shot (A9.3) trước khi dựng cả tập** — một shot lỗi làm hỏng cả lượt dựng 30 phút |
| 22 | **T5 (con số) chỉ hiện MỘT số/tiêu đề lớn** — đoạn thứ hai có chữ đậm đè lên ("B8ẾN 01 · 2010", "82" chồng "88") | Ở T5 chỉ một `**…**`; thông tin thêm viết nghiêng, hoặc tách sang shot kế |
| 23 | "Host nghe như 3 người", "giọng nam giống hệt nhau" (Tập 02): tham số cao độ/cảm xúc làm `audiobook_male_1` đổi danh tính; 2 giọng nam cùng vùng giọng; buổi thử chỉ so các bản của cùng một câu | Bộ A + G8–G10; cao độ luôn 0 |
| 24 | Giọng đa ngôn ngữ đọc số kiểu tiếng Anh: "1.400" → "một phẩy bốn trăm"; số La Mã "II" đọc thành chữ cái | G11 — đổi số sang chữ trong lời đọc. Khi soạn kịch bản: đơn vị, ký hiệu (%, km, $) nên viết bằng chữ |
| 25 | Shot cuối (bìa hồ sơ gập, mẫu T2) để cột Chữ là "—" → video kết thúc bằng **tờ giấy trống** (Tập 01, Tập 02; người dùng phát hiện) | Cột Chữ shot cuối: `*HỒ SƠ TẬP XX · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật*`. Hai dòng khẩu hiệu viết thành hai mục nghiêng riêng (mỗi dòng ≤ 48 ký tự, tránh tiền tố "—") |
| 26 | **Freesound API: mọi từ trong `query` đều BẮT BUỘC** → truy vấn 3–4 từ luôn trả 0 kết quả (7/19 mã SFX rỗng lần đầu) | Từ khóa chỉ **1–2 từ**: "library ambience" ✓, "library quiet room tone" ✗. Client đã có `fallback` tự bỏ dần từ |
| 27 | **Freesound không hỗ trợ `grant_type=client_credentials`** (trả 400 `unauthorized_client`) | Dùng **Token auth**: cột "Client secret/Api key" làm API key, header `Authorization: Token <key>`. Chỉ khi cần **file gốc** mới làm OAuth2 `authorization_code` (cần đăng nhập trình duyệt) |
| 28 | Freesound endpoint `download/` (file gốc) là **OAuth2-required** → Token auth trả 401 | Token auth chỉ lấy được **preview hq mp3 160 kbps stereo** qua CDN — đủ dùng cho mix video |
| 29 | Hạn mức Freesound: **60 req/phút · 2000 req/ngày**, tính theo USER (mọi client cùng tài khoản dùng chung hạn mức) | Client throttle ≥ 1,1 s/lần (~54 req/phút); `GET /apiv2/usage/` để xem đã dùng bao nhiêu (endpoint này không bị throttle) |
| 30 | Ghi `provenance.json` bằng `indent=2` làm file phình 1,83 MB → 1,89 MB, không mất dòng nào nhưng **đổi định dạng toàn file** | `provenance.json` dùng **`indent=1`** — giữ nguyên khi ghi |
| 31 | Ghi provenance cho ứng viên Freesound vào sổ chính bị **skip hết** vì `file` trùng đường dẫn đích đã có dòng từ YouTube Audio Library | Ứng viên **chưa duyệt** ghi vào sổ tạm `.work/freesound_provenance.json`; chỉ `--merge` vào `provenance.json` sau khi người dùng nghe duyệt |
| 32 | **Lệch pha ngữ nghĩa giữa câu thoại và hình ảnh/chữ trên hình (Tập 06: người dùng phát hiện đang nói mức lương 5$ thì hình đã chuyển sang tủ áo khoác mỏng)**: Phân bổ ranh giới câu thoại vào shot bị vội, cắt shot ở giữa hai câu cùng chủ đề hoặc đặt shot hiển thị trước khi câu thoại bắt đầu | **Rà soát đồng bộ ngữ nghĩa 100% trước khi dựng**: Mỗi khi câu thoại chuyển sang đối tượng/vật chứng/địa điểm mới thì ảnh và chữ mới chuyển theo; các câu cùng một nội dung cốt lõi (như 2 câu về mức lương 5$) phải gom trọn vẹn trong cùng 1 shot; chữ hiển thị phải lấy đúng từ câu đang đọc trong shot đó (H3, V3) |
| 33 | **Lệch chữ trên hình, ảnh nền và vai nhân vật (Tập 04)**: Chữ trên hình tự tóm tắt ý niệm hoặc trích dẫn bịa không có trong câu thoại (vi phạm H6/V3); nền chuyển trước khi câu thoại đề cập (nền kho dịch truyền hiện khi đang nói về hủy lệnh bỏ túi áo); gán nhầm vai Host cho câu của Điều tra viên (vi phạm G9/H3) | **Quy tắc đối soát 3 lớp trước khi render**: 1) Script quét chữ trên hình đối chiếu 100% với lời đọc; 2) Mỗi shot chỉ dùng ảnh nền tương ứng với ngữ cảnh câu đang đọc; 3) Kiểm tra khớp vai và avatar bán thân 100% với kịch bản gốc. |
| 34 | **Tắc nghẽn CPU khi tính đường bao ducking trên mảng mẫu lớn (Tập 03 EN)**: `np.convolve` trực tiếp trên ~85 triệu mẫu (32 phút) tốn ~5 phút CPU 100% | Thay bằng trung bình trượt tích lũy `np.cumsum` chạy trong **0,05 giây**, kết quả toán học đồng nhất |
| 35 | **Khoảng câm > 0,3 s ở đoạn kết video dài > 30 phút (Tập 03 EN)**: Sàn môi trường đặt −34 dB bị hụt dưới −60 dBFS khi nhạc nền fade out | Đặt sàn môi trường −31 dB và kéo dài đuôi piano ấm 7,8 s với fade out mượt giúp video không bao giờ câm > 0,3 s |
| 36 | **Lỗi `IntroReader` văng `AttributeError` khi worker render seek vượt đuôi video intro (Tập 04 EN)**: Worker bắt đầu từ frame $\ge$ thời lượng của `intro_kenh_*.mov` hoặc shot `1-00` gọi blend khi $t \ge 20.5 + 1.9$ s khiến FFmpeg hết frame (`self.last` là `None`) | Trong `IntroReader.get`: nếu `self.last is None` trả ảnh đen RGBA; trong `render()` chỉ blend intro ở shot `1-00` khi $t < 20.5 + 1.9$ s |
| 37 | **Sửa bảng shot xong nhưng KHÔNG dựng lại video → thành phẩm vẫn còn lỗi cũ** (Tập 02, phát hiện 25/10/2026): `shots_t02.json` sửa lúc 24/10 09:22 (thêm chữ cho thẻ kết `5-29`) nhưng `Tap02_master.mp4` dựng lúc 23/10 19:43 → **video kết bằng tờ giấy trắng trơn + 2,7 s màn đen**, đúng bẫy #25 đã ghi là "đã sửa" | **Trước khi giao bất kỳ tập nào: so `mtime` bảng shot (`shots_tXX.json`) với `mtime` file mp4 thành phẩm — bảng shot phải CŨ HƠN video.** Luôn trích **khung tại giữa shot cuối** từ mp4 (không dùng ảnh tĩnh) và đảm bảo khung đó có chữ, không phải nền trắng/đen trơn. Nếu chỉ sửa 1 shot cuối thì `build_video3.py --stills` + `rerender_part.py` + `package.py --mux`, **không cần dựng lại toàn bộ** |
| 38 | **Đo đỉnh âm lượng trên WAV trung gian → tưởng là đạt, nhưng file mp4 vượt trần** (Tập 02): WAV đo −1,5 dBFS nhưng AAC trong mp4 đo **−0,9 dBTP** (vượt trần −1,5 của chính dự án) vì bộ mã hoá đẩy đỉnh lên ~0,6 dB | **Luôn đo `ebur128` trên chính file mp4 cuối**, không đo WAV trung gian. Khi đóng gói, áp giới hạn trước khi mã hoá: `-af "loudnorm=I=-16:TP=-1.8:LRA=11"` rồi đo lại trên mp4 |
| 39 | **Copy pattern `bed` của tập khác cho tập mới → nhạc nền không khớp kịch bản** (phát hiện 25/10/2026): 20/29 tập dùng chung 1 pattern; T09/T16 kịch bản đòi guitar/organ nhưng bed trỏ piano/cello; 2 track tải về (220 s + 196 s) nằm không ai dùng | **Bed mỗi hồi = mood thẻ `[BGM]` ĐẦU TIÊN của hồi đó** trong `01_KICH_BAN/TapXX/` (Hồi 1 lấy tại mốc `act1_cue`). Kiểm bằng `.work/_qc_bgm_bed_start.py` (đối chiếu 145 slot hồi) trước khi dựng. **Cấm** copy y hồi sẵn tập khác |
| 40 | **Vá `edition.py` bằng script → mất dấu nháy → `py_compile` vẫn PASS nhưng file hỏng khi chạy** (25/10/2026): dựng lại literal `"bed"` bằng `", ".join(...)` làm mất `"` → `1: bgm_cello_sad.mp3` thành **biểu thức thuộc tính** (NameError lúc chạy), và làm hỏng cả các giá trị tuple cũ | Vá **chỉ giá trị của đúng hồi** trong literal gốc (regex `(\d+): ("[^"]*"\|\([^()]*\))`), không dựng lại cả khối. Sau khi vá **phải `import edition` thật** để bắt lỗi tên biến — `py_compile` chỉ kiểm cú pháp. Có bản sao lưu ở `.work/_cu/` để quay lại |
| 41 | **`package.py --mux` crash `KeyError: '1.01#1'` vì `EPISODES[*]["summary"]` trỏ vào element không có câu thoại** (Tập 07, 08 — 25/10/2026): element `1.01` của 2 tập này là thẻ `[BGM]` (không có câu), nên mã câu `1.01#1` không tồn tại trong script hiện tại (script đã được sửa sau lúc dựng). Mp4 đã ghép xong nhưng **mô tả + thumbnail không được tạo** | Kiểm `summary` của cả 29 tập trước khi đóng gói: `.work/_patch_summary_t07.py` (in ra tập nào hỏng và tự sửa về câu thoại đầu hồi 1). Sau khi sửa kịch bản phải cập nhật lại `summary` |
| 42 | **`audio_master.wav` là 48 kHz, không phải 44,1 kHz** (25/10/2026): `loudnorm` trong `build_audio3.py` dùng `aresample=48000`. Đo/cắt bằng hằng số 44100 lệch mốc thời gian **8,8 %** → kết luận sai là "các hồi không sửa cũng thay đổi" | Khi phân tích file âm thanh, **đọc `framerate` từ header WAV** (`wave.getframerate()`), không hard-code. Bài học còn lại: khi đo "phần nào thay đổi", so bằng **tương quan với file nguồn** (`.work/_qc_bgm_pause.py`) chứ không chỉ so trước/sau |
| 43 | **`batch_text_to_audio` chỉ nhận tối đa 10 request/lượt** (27/10/2026): gửi 51 request trong 1 lượt → lỗi `connector_tool_error: Connector tool execution failed (latency_ms=0)` — **không có thông báo nào nói nguyên nhân là vượt giới hạn**, trông như server chết | Chia chunk **10 request/lượt**; đọc `success_items[]`/`failed_items[]` của **từng** batch thay vì tin exit code. Cùng lỗi này đã làm 4 ứng viên TTS "hỏng" trong 1 lượt chạy |
| 44 | **Đo CER bằng ASR mà không chuẩn hoá số ở CẢ HAI VẾ** (27/10/2026): `ref` = lời đọc trong manifest (đã qua `vi_numbers()` → chữ: "tám mươi tám") nhưng `hyp` = ASR trả về **dạng số** ("88") → 1 câu hoàn toàn đúng bị tính **CER 21,4 %**, câu khác **300 %** | Áp `vi_numbers()` cho **cả `ref` lẫn `hyp`** trước khi tính CER. Sau khi sửa, toàn bộ "lỗi nặng" biến mất |
| 45 | **Bộ lọc nội dung Gemini chặn câu TTS nhưng mã lỗi vẫn `code = 0`** (27/10/2026): `listen_audio` trả `{"code":0,"message":"ok","transcription":"This request was blocked by Gemini's filters..."}` → tưởng đó là lỗi phát âm của giọng | **Đọc nội dung `transcription` chứ không chỉ `code`**; cắt đuôi lỗi bằng regex rồi chạy lại câu đó. Câu bị chặn là **mẫu hỏng** → loại khỏi mẫu đo (2/20 câu), không tính là lỗi giọng |
| 46 | **Vắng mặt trong `get_voice_list` ≠ giọng đã chết** (27/10/2026): `audiobook_male_1`, `male-qn-qingse`, `audiobook_female_1` không có trong danh mục live 332 giọng, nhưng `male-qn-qingse` lại là **default** của schema TTS | MiniMax có 2 lớp: *voice library* (danh mục) và **system voice cũ** không được liệt kê nhưng API vẫn nhận. Chỉ kết luận "giọng chết" sau **1 lần gọi TTS thật**; không kết luận từ tên |
| 47 | **`pitch` của connector KHÔNG phải chỉnh cao độ (F0)**: `pitch` = `voice_setting.pitch` = đổi **âm sắc (timbre)**, 0 = giữ nguyên âm sắc gốc | Muốn đổi F0 thì đổi `voice_id` và **đo lại F0**, không dùng `pitch`. Cũng **không có tham số `language`** — ngôn ngữ đến từ **văn bản**, chất giọng đến từ `voice_id` (synthesis, không phải dịch) |
| 48 | **ASR không tất định — cùng 1 file, 2 lượt cho kết luận khác nhau** (27/10/2026): 3/9 câu vượt ngưỡng đổi kết quả giữa 2 lượt (28 %→18 %, 4,3 %→1,1 %) | Mỗi kết luận về **từng câu** phải chạy **≥ 2 lượt**; câu vượt ngưỡng thì chạy thêm lượt nữa (rẻ, ~10 lượt). Với `audios_understand`, cùng 1 file bed đổi verdict **10/45 file** ⇒ verdict AI chỉ là **tín hiệu mềm**, không dùng làm gate cứng |
| 49 | **Đoán giới tính giọng từ tên** → sai (`"female"` chứa `"male"`, `"woman"` chứa `"man"`) | Không đoán từ tên — **đo F0 thật**. Và chỉ đo trên **file TTS rời**: đo trên master (đã có nhạc + SFX) sinh 164 nhóm nhiễu và ra kết luận sai |
| 50 | **Bảng kiểm 6 thanh của câu mẫu VoxCPM2 đếm bằng tay → sai** (29/10/2026): ghi "với" là thanh nặng, liệt kê từ không có trong câu. Script đóng gói `higgs_make_refs_voxcpm.py` viết cứng `ROOT = D:\TEST\Gax\Audi` (sai repo) | Đếm thanh bằng `tone_coverage` của `.work/voxcpm_do_mau.py`; đường dẫn tính từ `__file__`. Luật: `QUY_TAC_GIONG_MAU_VOXCPM2.md` |
| 51 | **Chú thích vai N1/N2 trong kịch bản không ghi giới/tuổi** (29/10/2026: 27/58 vị trí thiếu, 3 tập T21·T22·T25 hai vai trùng một giọng) → không ghép được giọng mẫu W1–W4 nếu không đoán | Chú thích vai PHẢI ghi **giới + tuổi** (nữ/nam × trẻ·thanh niên·trung niên·lớn tuổi); hai N cùng tập khác giọng. Đổi tuổi chỉ ở nhân vật minh hoạ, **kiểm lời thoại không mâu thuẫn** (T25 N2 nhắc "cha mẹ già" nên không đổi được). Bảng ghép: `TAO_GIONG_MAU_VOXCPM2.md` §3.1 |

## A12. Cấu hình tập mới — một mục trong `.work/edition.py`

Từ 23/10/2026 **không sửa script** cho tập mới. Thêm mục `"XX"` vào `EPISODES` của `edition.py` và chạy mọi lệnh với `AE_EP=XX`. File trung gian của tập ≠ 01 có hậu tố `_tXX`, nên các tập không ghi đè nhau.

| Khoá | Ý nghĩa | Tập 02 |
|---|---|---|
| `script` · `dir` · `plan` · `master` · `srt` | đường dẫn kịch bản json, thư mục tập, hồ sơ, tên file ra | `script_tap02.json` · `Tap02` · `KeHoach_Video_Tap02.md` · `Tap02_master` · `Tap02.srt` |
| `n_element` | phần tử nào là N1/N2 | `{"1.07": "N1", "4.06": "N2"}` |
| `acting` | file diễn xuất từng câu (A4.2) | `acting_tap02.json` |
| `sfx_sheet` | bảng âm thanh stereo (nền · tiếng động · tắt nhạc) | `sfx_tap02.json` |
| `act1_cue` · `silence_cue` · `click_cues` | mốc nhạc Hồi 1 vào · "nhạc dừng đột ngột" · tiếng "Tách" | `"1.16"` · `"1.09"` · `("1.06",)` |
| `bed` | nhạc nền theo hồi | cello · piano · cello_v2 · sub_drone · piano_warm |
| `sfx_cues` | SFX kiểu cũ (Tập 01) | `[]` |
| `combo` · `inset` · `bg2` | cảnh ghép, ảnh ghim, đổi nền trong shot (theo **mã shot của tập đó**) | `{}` |
| `flag_hold_shots` · `route_pins` | dòng giữ hình vẽ cờ · nhãn 2 ghim T7 | `()` · `{}` (ghim không nhãn) |
| `thumb` · `thumb_bg` · `title` · `act_titles` · `summary` · `need` | chữ và nền thumbnail, tiêu đề mô tả, tên 5 hồi, câu tóm tắt, câu cần nguồn | "ĐẠI TÁ / HAI MẶT" · `t2_two_chairs` · … |
| `case` · `n1` · `n2` | tên vụ trên badge Điều tra viên, nhãn N1/N2 | `Williams` · "BINH SĨ CĂN CỨ TRENTON" · "KHÁN GIẢ" |
| `cast` | **chỉ khai khi đổi giọng** (đã qua G8–G10); để `None` = dùng bộ A | `None` — Tập 01 ghim bộ giọng cũ |

**Kiểm tra hồi quy khi sửa script dùng chung:** chạy lại `tts_sentences.plan_items()` và `parse_shots.py` của Tập 01, so với bản cũ — phải giống hệt (đã làm 22/10: 122 shot giống hệt, âm thanh lệch 1 mẫu / 50 triệu do thứ tự cộng số thực).

## A13. Rủi ro chung

| Rủi ro | Xử lý |
|---|---|
| Linh thú làm nhẹ tính nghiêm trọng | Biểu cảm nghiêm, ≤ 20% khung, `⊘` ở khoảnh khắc nặng nề |
| Người xem tưởng nhân vật là người thật | V6 + dàn khách mời + mô tả |
| Intro 22 s trước phần mồi làm người xem thoát | Theo dõi tỉ lệ giữ chân; phương án B: đưa intro ra sau câu mồi đầu tiên |
| Nhạc AI bị Content ID nhận nhầm | Kháng nghị bằng `provenance.json` |
| Điều khoản thương mại chưa rõ | Kiểm tra trước khi bật kiếm tiền |

---

*Tách từ bản v10 gộp ngày 22/10/2026 (lưu ở `90_LUU_TRU/ke_hoach_cu/`).*
