# TIÊU CHUẨN DỰNG VIDEO — KÊNH AMBER EYES

**Phiên bản 10 · Bản mẫu tiêu chuẩn** · Cập nhật 22/10/2026
**Trạng thái:** đã chạy thật trọn vẹn với Tập 01 → `Tap01_master.mp4` (18:53, 1920×1080, 30 fps). Mọi lệnh, số liệu và lỗi trong file này đều lấy từ lần chạy đó.

## Cách dùng file này

| Phần | Nội dung | Tập mới làm gì |
|---|---|---|
| **PHẦN A — Tiêu chuẩn chung** | Quy tắc, quy trình, lệnh chạy, âm thanh, đồ hoạ, kiểm tra, pháp lý, các bẫy đã gặp | **Giữ nguyên.** Chỉ sửa khi đổi tiêu chuẩn của kênh |
| **PHẦN B — Hồ sơ tập** | Số liệu, ánh xạ riêng, bảng shot, phụ lục của **Tập 01** | Sao chép file thành `KeHoach_Video_TapXX.md`, **thay toàn bộ Phần B** bằng nội dung tập mới |

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
- [ ] `kichban_tapXX.md` đúng định dạng A2, **đã giảm bạo lực theo V9** (xem Phụ lục B của Tập 01 làm mẫu cách viết)
- [ ] Tên tập
- [ ] (tuỳ chọn) ghi chú phong cách, cảnh đặc biệt

**Đầu ra (AI):**

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

## A3. Quy trình chuẩn — lệnh chạy và thời gian đo được

Chạy từ `D:\TEST\Gax\Audi`, đặt `PYTHONIOENCODING=utf-8`. Connector gọi qua `mcode-tools` (có sẵn tại `C:\Users\ADMIN\.minimax\bin`).

| Bước | Lệnh | Đầu ra | Thời gian Tập 01 |
|---|---|---|---|
| **0. Một lần cho series** | `make_logo.py` · `make_intro.py` · `make_cast_cutouts.py` · `voice_audition.py` | Logo, intro, 5 linh thú, chọn giọng | đã xong |
| **1. Tách kịch bản** | `py -3 .work/parse_kichban.py kichban_tapXX.md .work/script_tapXX.json` | lượt nói, câu | < 1 s |
| **2. Đọc giọng** | `py -3 .work/tts_sentences.py` | `.work/audio_s/*.mp3` | 128 câu / 7 phút |
| **3. Âm thanh tổng** | `py -3 .work/build_audio3.py` | `TapXX_master.mp3`, `timeline_s.json`, `stems/` | 2 phút |
| **4. Kiểm tra âm thanh** | lệnh A9.1 | — | 1 phút |
| **5. Nền mới (nếu cần)** | `py -3 .work/gen_images.py .work/bg_jobs_tapXX.json` | `assets/bg/*.png` | ~1 phút / ảnh |
| **6. Bảng shot** | AI viết mục 6 của Phần B → `py -3 .work/parse_shots.py` | `.work/shots.json` | < 1 s |
| **7. Kiểm tra chữ** | lệnh A9.2 | — | < 1 s |
| **8. Ảnh tĩnh duyệt** | `py -3 .work/build_video3.py --stills 30,75,160` | `.work/video3/stills/` | ~0,4 s / ảnh |
| **9. Dựng hình** | `py -3 .work/build_video3.py --workers 6` | `.work/video3/picture.mp4` | 1.133 s video / ~22 phút |
| **10. Sửa cục bộ** | `py -3 .work/rerender_part.py K` (K = 0…5) | dựng lại 1/6 tập rồi ghép | ~5 phút / phần |
| **11. Phụ đề** | `py -3 .work/subtitles.py` | `TapXX.srt` | < 1 s |
| **12. Đóng gói** | `py -3 .work/package.py --mux` | `.mp4`, thumbnail, mô tả, nguồn | 1 phút |
| **13. Kiểm tra cuối** | lệnh A9.3 + A9.4 | — | ~5 phút |

**Tính phần cần dựng lại (bước 10):** `bước = ceil(tổng_khung / 6)`; khung = `giây × 30`; phần = `khung // bước`. Ví dụ Tập 01: bước 5.668 khung ≈ 188,9 s → giây 829 thuộc **phần 4**. *(Tập 01 từng tính nhầm thành phần 3 — luôn tính bằng công thức.)*

**Mốc duyệt với người dùng** (người dùng có thể bỏ qua): sau bước 4 (nghe giọng), sau bước 8 (ảnh tĩnh), sau bước 13 (video cuối).

## A4. Âm thanh chuẩn

### A4.1 Năm giọng (đã kiểm chứng 22/10: connector nghe lại khớp 100%, CER 0%)

| Nhân vật | `voice_id` | `speed` gốc | F0 đo |
|---|---|---:|---:|
| Cú · Host | `audiobook_male_1` | 0,90 | 137 Hz |
| Sói · Điều tra viên | `male-qn-qingse` | 0,95 | 129 Hz |
| Cáo · Chuyên gia | `audiobook_female_1` | 0,92 | 235 Hz |
| Cừu · N1 | `Vietnamese_kindhearted_girl` | 0,95 | 271 Hz |
| Mèo · N2 | `English_captivating_female1` | 0,95 | 222 Hz |

`get_voice_list` **không liệt kê** 3 giọng đầu nhưng chúng vẫn chạy. Giọng dự phòng có lỗi nhận dạng 4–10% (`English_expressive_narrator`, `English_CalmWoman`…).

### A4.2 Chỉ dẫn → tham số TTS

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
| SFX | Chỉ tiếng "Tách" máy ghi âm (ffmpeg tự tạo). SFX khác chưa có file → bỏ qua |
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
| Kênh | `assets/brand/channel.json` | Tên, khẩu hiệu, bảng màu, font |

## A7. Cách viết bảng shot (mục 6 của Phần B)

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

## A12. Điểm phải đổi trong script cho tập mới

| Script | Biến / chỗ | Tập 01 đang là |
|---|---|---|
| `tts_sentences.py` | `SCRIPT` (đường dẫn script json) · `N_ELEMENT` (phần tử nào là N1/N2) | `script_v2.json` · `{"1.07": "N1", "4.03": "N2"}` |
| `build_audio3.py` | `script` · mã cue nhạc Hồi 1 (`"1.12"`), "im lặng tuyệt đối" (`"1.09"`), tiếng "Tách" (`"1.06"`, `"1.12"`) · `BED` · tên file ra | xem cột trái · `Tap01_master.mp3` |
| `parse_shots.py` | `PLAN` · `COMBO` · `BG2` · `INSET` | `KeHoach_LamLai_Video_Tap01.md` · Phần B3 |
| `voice_audition.py` | `CANDS` (câu thử) | chỉ chạy lại khi đổi giọng |
| `package.py` | tên file · `act_titles` · câu tóm tắt (`1.13#2`, `3.02#5`) · `need` (câu cần nguồn) | Phần B |
| `subtitles.py` | tên file ra | `Tap01.srt` |
| `build_video3.py` | không cần đổi (đọc `shots.json`, `timeline_s.json`) | — |

*Cải tiến nên làm:* gom các biến trên vào một file `tap.json` cho mỗi tập để không phải sửa script.

## A13. Rủi ro chung

| Rủi ro | Xử lý |
|---|---|
| Linh thú làm nhẹ tính nghiêm trọng | Biểu cảm nghiêm, ≤ 20% khung, `⊘` ở khoảnh khắc nặng nề |
| Người xem tưởng nhân vật là người thật | V6 + dàn khách mời + mô tả |
| Intro 22 s trước phần mồi làm người xem thoát | Theo dõi tỉ lệ giữ chân; phương án B: đưa intro ra sau câu mồi đầu tiên |
| Nhạc AI bị Content ID nhận nhầm | Kháng nghị bằng `provenance.json` |
| Điều khoản thương mại chưa rõ | Kiểm tra trước khi bật kiếm tiền |

---

# PHẦN B — HỒ SƠ TẬP 01 · "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ"

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `kichban_tap01_22102026_v2.md` (bản giảm bạo lực của `kichban_tap01_22102026.md`, 23 chỗ sửa — Phụ lục B) |
| Lượt nói / câu / từ | 33 / **128** / 3.545 — Host 50% · Chuyên gia 24% · Điều tra viên 20% · Người dân 5% |
| N1 / N2 | `1.07` Hàng xóm (Cừu) / `4.03` Khán giả (Mèo) |
| Thời lượng đo | **1.133,5 s (18:53)** — intro 0–22,41 s |
| Mốc hồi | Hồi 1 · 00:20 · Hồi 2 · 03:28 · Hồi 3 · 06:51 · Hồi 4 · 10:54 · Hồi 5 · 15:43 |
| Bảng shot | 122 dòng = 104 shot có lời + 18 dòng không lời |
| Nền dùng | 45 ảnh `assets/bg/` (5 nền người dùng tạo + 2 cảnh bóng người dùng tạo + 41 nền connector + `void` tự vẽ) |

## B2. Kết quả và việc còn lại

| Hạng mục | Kết quả |
|---|---|
| TTS | 128/128, 5 giọng CER 0% |
| Âm thanh | 0 đoạn câm tuyệt đối; −16,0 LUFS; lời đầu 23,0 s |
| Chữ | 128/128 câu phủ đúng; 0 số/trích sai; 0 từ bạo lực |
| File | `Tap01_master.mp4` 419 MB; hình 1133,47 s = tiếng 1133,46 s; giải mã 0 lỗi |
| **Còn lại trước khi đăng** | ① Điền nguồn trong `nguon_tham_khao.md` · ② Kiểm tra điều khoản thương mại (57 dòng `provenance.json`), cho biết công cụ đã tạo 5 linh thú và 5 nền chủ đạo · ③ Người dùng nghe toàn tập |
| **Làm đơn giản hơn thiết kế** (có thể bổ sung) | Chưa có tư thế P2; chưa vẽ đường nhịp Dopamine, lưới biểu tượng bác sĩ, vòng hào quang, song sắt ghép từ lọ thuốc, bong bóng bình luận; SFX ngoài "Tách" chưa có; 5 vòng màu cuối intro là hình tạm |

## B3. Ánh xạ riêng của Tập 01 (trong `parse_shots.py`)

| Biến | Giá trị |
|---|---|
| `COMBO` (cảnh ghép sẵn) | 1-04 `crowd_house` · 1-07 `deedee_room` · 1-17 `interrogation_gypsy` · 1-19 `bedroom_door_gypsy` · 2-02, 3-20 `wheelchair_gypsy` · 2-13…2-15 `pinboard` · 3-02, 3-10 `fog_deedee` · 3-11, 3-12 `spotlight_deedee` · 4-04 `wheelchair_spot` · 4-06 `glass_box_gypsy` · 4-10 `cage` · 4-19 `night_street_gypsy` · 4-21 `house_return` · 4-22 `night_screen` · 4-24 `crowd_away` · 4-30 `godejohn_screen` · 4-31 `two_shadows` · 5-16 `house_free` · 5-17 `cage_open` |
| `BG2` (đổi nền trong shot) | 4-10 `cage` → `cage_open` · 4-22 `night_screen` → `screen_off` |
| `INSET` | 2-14 ảnh `storm` ghim trên bảng |
| Prompt nền | `.work/bg_jobs.json`, `bg_jobs2.json`, `bg_jobs3.json` |

## 6. DANH SÁCH SHOT — TẬP 01 (bảng mẫu, viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X (hiện badge chờ) · `✦` = lần đầu xuất hiện (thẻ giới thiệu) · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` (chỉ hình, shot I-01 → I-04, chi tiết ở A5.7) ở 0,00 s. Không câu thoại nào thuộc intro.

### HỒI 1 — KHOẢNH KHẮC ĐỨT GÃY NIỀM TIN · nền chủ đạo `house_night`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s, chồng lên phần đen cuối intro) | — | T1 | `house_police` hiện dần từ đen, `push` | *HỒI 01 · KHOẢNH KHẮC ĐỨT GÃY NIỀM TIN* | Đèn cảnh sát quét; drone dâng | ⊘ | |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `house_night` mờ | **14 · 06 · 2015** · *Springfield, Missouri* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T11 | `phone_dark` | *TRANG MẠNG XÃ HỘI CHUNG CỦA HAI MẸ CON* → **MỘT DÒNG TRẠNG THÁI KHIẾN CẢ KHU PHỐ CHẾT LẶNG** | Bài đăng hiện dạng các dòng mờ, không đọc được chữ, ở "đầy hằn học" | | |
| 1-03 | `1.04` (nghỉ 2 s) | — | — | giữ 1-02, ánh đỏ nhấp nháy | — | — | | |
| 1-04 | `1.05#1` | H | T1 | `house_police` + `crowd` | **NGÔI NHÀ NHỎ SƠN MÀU HỒNG PHẤN** · *Springfield, Missouri* (không hiện số nhà — nhà riêng, có thể đang có người ở) | — | | |
| 1-05 | `1.05#2` | H | T1 | `house_night`, `pull` | *LẮNG NGHE:* **MỘT NGƯỜI DÂN CÙNG KHU PHỐ** | — | →N1 | |
| 1-06 | `1.07#1` | N1 | T4 lời kể | `house_night` ấm, mờ | “Biểu tượng của tình mẫu tử thiêng liêng” | — | ✦ Cừu | |
| 1-07 | `1.07#2` | N1 | T8 | `wheelchair_room` + `deedee_wheelchair` | *NHỮNG GÌ CẢ KHU PHỐ TIN* · *Bại liệt từ thắt lưng trở xuống · Ung thư máu · Loạn dưỡng cơ · Động kinh nặng · Trí tuệ ngang trẻ lên bảy* | Mỗi mục tại cụm từ | | |
| 1-08 | `1.07#3` | N1 | T4 lời kể | `house_night` ấm | “Ai trong thị trấn này cũng rơi nước mắt cảm phục” | — | 🅑 | |
| 1-09 | `1.08#1` | H | T1 | `bedroom_door` | **NGƯỜI MẸ ĐÃ QUA ĐỜI** | — | | |
| 1-10 | `1.08#2` | H | T1 | `empty_room`, `still` | **GYPSY ROSE ĐÃ BIẾN MẤT** | — | ⊘ | ✂ |
| 1-11 | `1.08#3`–`#4` | H | T1 | `wheelchair_room` | **XE LĂN · BÌNH OXY · HÀNG CHỤC LỌ THUỐC** | `#3` sáng xe lăn, `#4` sáng kệ | | |
| 1-12 | `1.08#5` | H | T3 | `wheelchair_room` tối + dấu `?` lớn | *CẢ NƯỚC MỸ HỎI* · **AI ĐÃ GÂY RA CÁI CHẾT CỦA NGƯỜI MẸ?** | — | | |
| 1-13 | `1.08#6` | H | T1 | `interrogation`, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN THỤ LÝ HỒ SƠ** | — | →D | |
| 1-14 | `1.09`–`1.10` (nghỉ 2 s) | — | — | giữ 1-13, nhiễu bộ đàm `cold` | — | — | ⊘ | |
| 1-15 | `1.11#1` | D | T2 | `pinboard` | **LỆNH TRUY TÌM TOÀN QUỐC** | Dấu mộc ở "phát lệnh truy tìm" | ✦ Sói | |
| 1-16 | `1.11#2` | D | T7 | `route_night` | **48 GIỜ SAU** · *Bang Wisconsin — cách hàng trăm dặm* | Đường tự vẽ, số đếm | | |
| 1-17 | `1.11#3`–`#4` | D | T1 | `interrogation` + `gypsy_stand` | **CÔ TA TỰ BƯỚC ĐI** | Đèn treo sáng ở `#4` | | |
| 1-18 | `1.11#5`–`#7` | D | T8 gạch bỏ | giấy hồ sơ trên `records` | *Ung thư máu · Loạn dưỡng cơ · Tổn thương não* | Mỗi câu gạch một mục | | ✂ |
| 1-19 | `1.11#8` | D | T1 `hero` | `bedroom_door` + `gypsy_stand`, tối dần | **CÔ CON GÁI BÉ BỎNG CỦA BÀ** | Tiêu đề ở "không ai khác" | 🅑 P2 | |
| 1-20 | `1.13#1` | H | T1 | `podcast_desk`, cassette quay | **HỒ SƠ PHÂN TÍCH TÂM LÝ HỌC TỘI PHẠM** | "Tách" ở đầu | 🅑 | |
| 1-21 | `1.13#2` | H | T9 → T10 | `house_night` | **HỘI CHỨNG MÜNCHAUSEN QUA TRUNG GIAN** → *TẬP 01 · ĐỘC DƯỢC NHÂN DANH TÌNH MẸ* | Thuật ngữ ở "Hội chứng"; tên tập cuối câu | | |
| 1-22 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **23 NĂM TRONG NHÀ TÙ Y KHOA** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ BỆNH ÁN · nền chủ đạo `wheelchair_room`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `bedroom_door` | **KHÔNG PHẢI CĂN PHÒNG NGỦ** · *Tháng 6 năm 2015* | Tiêu đề ở `#2` | | |
| 2-02 | `2.02#3` | H | T5 | `wheelchair_room` + `gypsy_wheelchair` | *HIỆN TRƯỜNG THỰC SỰ* · **23 NĂM** | Số đếm | | |
| 2-03 | `2.04#1`–`#5` | H | T6 | `records`, `pan` | *1991 · Sinh ra khỏe mạnh* → *3 tháng tuổi · Ngưng thở khi ngủ* → *Danh sách bệnh án bắt đầu* → *7 tuổi · Tổn thương tủy sống · Xe lăn* → *Cạo trọc đầu · Hoá trị ung thư máu* | Mỗi câu một mốc | ⊘ | |
| 2-04 | `2.06#1` | H | T1 | `clinical` | **KHÔNG CHỈ LÀ LỜI NÓI DỐI** | — | 🅑 | |
| 2-05 | `2.06#2` | H | T2 | `records` | **HÀNG NGÀN TRANG BỆNH ÁN** · *Can thiệp y khoa trực tiếp lên cơ thể Gypsy* | — | | |
| 2-06 | `2.06#3` | H | T1 | `pinboard` mờ, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN CÔNG BỐ HỒ SƠ** | — | →D | |
| 2-07 | `2.07#1` | D | T2 | `pinboard` | **BA DẤU VẾT TRONG HỒ SƠ Y TẾ** | Bộ đếm `0/3` | | |
| 2-08 | `2.07#2` | D | T3 `1/3` | `wheelchair_room` cận kệ thuốc | **THUỐC CHỐNG ĐỘNG KINH LIỀU CAO** · *Dù cô không hề bị động kinh* | Phụ ở "dù cô không hề" | | |
| 2-09 | `2.07#3` | D | T3 `2/3` | `clinical` | **ỐNG NUÔI ĂN QUA DẠ DÀY** | — | | |
| 2-10 | `2.07#4` | D | T3 `3/3` | `clinical` tối | **PHẪU THUẬT KHÔNG CẦN THIẾT** · *Từ những triệu chứng giả trước mắt bác sĩ* | — | | |
| 2-11 | `2.07#5` | D | T5 | `clinical` + lưới ~100 biểu tượng bác sĩ (Pillow) | **HÀNG TRĂM BÁC SĨ** · *Không ai phát hiện ra?* | Biểu tượng hiện dần | | |
| 2-12 | `2.07#6` | D | T9 | `pinboard`, `pull` | **PHƯƠNG THỨC HÀNH ĐỘNG** *(Modus Operandi)* | 3 thẻ trống ghim lên | 🅑 | |
| 2-13 | `2.07#7` | D | T2 trên bảng ghim | camera dời tới thẻ 1 | *01* · **TỪNG LÀM HỘ LÝ** · *Nắm rõ thuật ngữ y khoa* | — | | |
| 2-14 | `2.07#8`–`#9` | D | T2 trên bảng ghim | thẻ 2 có ảnh `storm` thu nhỏ | *02 · 2005* · **BÃO KATRINA** → `#9`: *Mọi lịch sử y tế chỉ qua lời bà Dee Dee* | Dây đỏ nối ở `#9` | | |
| 2-15 | `2.07#10` | D | T2 trên bảng ghim | thẻ 3 + ghi chú Consolas | *03* · **AI NGHI NGỜ → ĐỔI BỆNH VIỆN, CHUYỂN NHÀ** · *BS. Bernardo Flasterstein · 2007* (chỉ chữ, V5) | Kéo ra thấy cả bảng | | |
| 2-16 | `2.09#1`–`#2` | H | T1 | `house_closed` | **CỬA SỔ LUÔN ĐÓNG KÍN** · *Không được đi học* | Tiếng khoá cửa ở đầu | | |
| 2-17 | `2.09#3` | H | T5 | `house_closed` mờ | **−4 TUỔI** · *Khai gian để mãi là trẻ vị thành niên* | — | | |
| 2-18 | `2.09#4` | H | T1 | `house_night` + bóng song sắt ghép từ lọ thuốc, ống truyền (Pillow) | **MỘT NHÀ TÙ KHÔNG CHẤN SONG** | Song sắt ở "được xây bằng" | | |
| 2-19 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **BÊN TRONG BỘ NÃO CỦA KẺ MẮC FDIA** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI PHẪU TÂM LÝ · nền chủ đạo `brain_desk`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T5 | `void`, `still` | *CÂU HỎI LỚN NHẤT* · **TẠI SAO?** | Đúng ở "Tại sao" | ⊘ | ✂ |
| 3-02 | `3.02#2` | H | T1 | `fog` + `deedee_wheelchair` | **HƠN HAI THẬP KỶ** | — | | |
| 3-03 | `3.02#3`–`#4` | H | T3 | `charity` | **TRỤC LỢI TỪ THIỆN?** → `#4`: **TIỀN CHỈ LÀ PHẦN THƯỞNG PHỤ** | Đồng xu mờ ở `#4` | | |
| 3-04 | `3.02#5` | H | T9 | `brain_desk` | **HỘI CHỨNG MÜNCHAUSEN QUA TRUNG GIAN** *(Münchausen Syndrome by Proxy)* · *DSM-5-TR: Rối loạn giả bệnh áp đặt lên người khác — FDIA* | Dòng DSM ở "DSM-5-TR" | | |
| 3-05 | `3.03` (nghỉ) | — | — | giữ 3-04 | — | — | | |
| 3-06 | `3.04#1`–`#2` | H | T1 | `brain_desk`, `push` | *LẮNG NGHE:* **CHUYÊN GIA TÂM LÝ HỌC TỘI PHẠM** → *3 tầng tâm lý* | — | →C | |
| 3-07 | `3.05#1` | C | T9 | `brain_desk` + sơ đồ `brain3` | **3 TẦNG ĐỘNG CƠ** · *Vô thức và ý thức* | 3 vòng sáng lần lượt | ✦ Cáo | |
| 3-08 | `3.05#2` | C | T4 | `brain_desk` tối, tầng 1 sáng + `halo` | *TẦNG 01 · CƠN NGHIỆN HÀO QUANG* · “Vị thánh tử đạo” | — | | |
| 3-09 | `3.05#3`–`#4` | C | T3 so sánh | `brain_desk` mờ | **MALINGERING** *(Giả bệnh trục lợi) → tiền* · `#4`: **MÜNCHAUSEN** *→ sự chú ý, thương cảm, tôn sùng* | Cột phải ở `#4` | | |
| 3-10 | `3.05#5`–`#6` | C | T1 | `fog` + `deedee_wheelchair` mờ | *Gia đình xa lánh · Hôn nhân tan vỡ ở tuổi 24* → **MỘT CÁI BÓNG MỜ NHẠT** | Tiêu đề ở `#6` | | |
| 3-11 | `3.05#7` | C | T1 | `spotlight` + `deedee_wheelchair` | **TRUNG TÂM CỦA VŨ TRỤ** | Đèn bật ở "bỗng nhiên" | | ✂ |
| 3-12 | `3.05#8` | C | T1 | `spotlight` + biểu tượng bác sĩ, hàng xóm, tờ báo | **VỊ THÁNH SỐNG** | Mỗi biểu tượng ở cụm từ | | |
| 3-13 | `3.05#9` | C | T5 | `void` + đường nhịp tăng vọt | **DOPAMINE** · *Mỗi lần Gypsy nhập viện cấp cứu* | Nhịp nhấp nháy | 🅑 P2 | |
| 3-14 | `3.06` (nghỉ) | — | — | tối dần | — | — | | |
| 3-15 | `3.07#1` | H | T1 | `brain_desk` | **MỚI CHỈ LÀ BỀ NỔI** | — | | |
| 3-16 | `3.07#2` | H | T2 | `records` | *LỜI KHAI GIA ĐÌNH BÊN NGOẠI* · **BỊ NGHI GÂY HẠI CHO NGƯỜI THÂN** | — | →C | |
| 3-17 | `3.08#1` | C | T9 | `brain_desk`, tầng 2 sáng | *TẦNG 02* · **NỖI SỢ BỊ BỎ RƠI · NHU CẦU KIỂM SOÁT** | — | | |
| 3-18 | `3.08#2`–`#4` | C | T3 | `hands` | **MỘT VẬT SỞ HỮU DUY NHẤT** → `#3`: *Đi học → bạn bè → yêu đương → rời xa mẹ* → `#4`: **GIỮ MỘT CON NGƯỜI MÃI MÃI?** | 3 beat | | |
| 3-19 | `3.08#5` | C | T1 `hero` | `void`, tối dần | **HÃY KHIẾN CON BÉ TIN RẰNG MÌNH BỆNH TẬT** | Tiêu đề ở "Hãy khiến" | ⊘ | |
| 3-20 | `3.08#6` | C | T3 | `wheelchair_room` + `gypsy_wheelchair` | **NGƯỜI DUY NHẤT NẮM GIỮ CUỘC SỐNG CỦA CON GÁI** | — | | |
| 3-21 | `3.09` (nghỉ) | — | — | giữ 3-20 | — | — | | |
| 3-22 | `3.10#1` | C | T9 | `brain_desk`, tầng 3 sáng | *TẦNG 03* · **DẤU ẤN XOÁ BỎ NHÂN DẠNG** *(Signature)* | — | | |
| 3-23 | `3.10#2` | C | T3 | `dress_hanger` | **CẠO TRỌC ĐẦU · VÁY CÔNG CHÚA** · *Ngay cả khi cô đã hơn 20 tuổi* | — | | |
| 3-24 | `3.10#3`–`#4` | C | T9 | `dress_hanger` mờ | *Không chỉ là giả bệnh ung thư* → **TƯỚC ĐOẠT SỰ TRƯỞNG THÀNH** *(Infantilization)* | Thuật ngữ ở `#4` | 🅑 | |
| 3-25 | `3.10#5`–`#6` | C | T1 | `doll` | **CON BÚP BÊ SỨ 7 TUỔI** | Tiêu đề ở "búp bê sứ" | | |
| 3-26 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **TẠI SAO GYPSY KHÔNG ĐỨNG DẬY?** | — | ⊘ | ◼ |

### HỒI 4 — GÓC NHÌN NẠN NHÂN · nền chủ đạo `locked_door`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` | H | T1 | `night_screen` + bong bóng bình luận mờ (Pillow, không tên) | **CÂU HỎI ĐẦY HOÀI NGHI** · *Dành cho chính Gypsy Rose* | — | | |
| 4-02 | `4.02#2` | H | T1 | `night_screen`, `push` | *LẮNG NGHE:* **MỘT KHÁN GIẢ THEO DÕI VỤ ÁN** | — | →N2 | |
| 4-03 | `4.03#1` | N2 | T4 lời kể | `night_screen` | “Cô ấy biết rõ đôi chân mình không hề bị liệt.” | — | ✦ Mèo | |
| 4-04 | `4.03#2`–`#3` | N2 | T4 lời kể | `wheelchair_room` tối, xe lăn trống dưới đèn rọi | “Mỗi tối… cô ấy vẫn tự đứng dậy đi lại bình thường.” → “Vậy tại sao… Gypsy không một lần đứng phắt dậy khỏi chiếc xe lăn để tố cáo mẹ mình?” | Mỗi câu một dòng | 🅑 ở `#3` | |
| 4-05 | `4.04` (nghỉ) | — | — | tối dần | — | — | | |
| 4-06 | `4.05#1` | H | T1 | `glass_box` + `gypsy_wheelchair` nhỏ | **LỚN LÊN TRONG LỒNG KÍNH** | — | | |
| 4-07 | `4.05#2` | H | T3 | `locked_door` · 2 thẻ thuật ngữ | **BẤT LỰC TẬP NHIỄM** *(Learned Helplessness)* · **GẮN KẾT CHẤN THƯƠNG** *(Trauma Bonding)* | Mỗi thẻ ở cụm từ | →C | |
| 4-08 | `4.07#1` | C | T9 | `cage` đóng | **SỰ BẤT LỰC TẬP NHIỄM** · *Martin Seligman · 1967* | Tiếng xích ở đầu | | |
| 4-09 | `4.07#2` | C | T4 `hero` | `cage` đóng, tối dần | “Mọi sự vùng vẫy đều vô nghĩa” | Câu trích ở cụm từ | | |
| 4-10 | `4.07#3` | C | T1 | `cage` đóng → mở (hoà tan 2 nền cùng seed) | **CỬA LỒNG ĐÃ MỞ TOANG** · *…nhưng không bao giờ bước ra nữa* | Cửa mở ở "cánh cửa lồng" | | |
| 4-11 | `4.07#4` | C | T1 | `locked_door` | **THẾ GIỚI QUAN CỦA GYPSY** | — | 🅑 P2 | |
| 4-12 | `4.07#5`–`#6` | C | T3 | `hands` | **BÀ LUÔN NẮM CHẶT TAY GYPSY** · `#6`: *Với người ngoài: cử chỉ âu yếm* | — | | |
| 4-13 | `4.07#7` | C | T3 | `hands`, ánh `cold` | *Với Gypsy: một mật lệnh đe dọa* · **MỘT LỜI CẢNH CÁO KHÔNG THÀNH TIẾNG** | Hai bàn tay khép chặt hơn ở "siết chặt" | | |
| 4-14 | `4.07#8` | C | T2 | `locked_door` | *SAU BUỔI KHÁM BỆNH* · **HÌNH PHẠT NGHIÊM KHẮC · KIỂM SOÁT NGỘT NGẠT** | Khe sáng tắt ở "khép lại" | | |
| 4-15 | `4.08` (nghỉ) | — | — | tối dần | — | — | | |
| 4-16 | `4.09#1` | H | T1 | `locked_door`, khe sáng dưới cửa | **GYPSY TỪNG CỐ GẮNG TỰ CỨU MÌNH** | — | | ✂ |
| 4-17 | `4.09#2` | H | T2 | `records` | *BIÊN BẢN THẨM VẤN* · **BIẾN CỐ NĂM 2011** | — | | |
| 4-18 | `4.09#3` | H | T1 | `pinboard` mờ | *LẮNG NGHE:* **HỒ SƠ SỰ VIỆC TỪ ĐIỀU TRA VIÊN** | — | →D | |
| 4-19 | `4.10#1` | D | T6 | `night_street` + `gypsy_stand` | *2011 · 19 tuổi* · **TRỐN KHỎI NHÀ ĐỂ CẦU CỨU** | — | | |
| 4-20 | `4.10#2`–`#3` | D | T2 | `pinboard`, tập giấy tờ, dấu `GIẢ MẠO` | **VÀI GIỜ SAU, BÀ LẦN RA DẤU VẾT** → `#3`: *Giấy tờ giả mạo: vị thành niên · thiểu năng trí tuệ · mất năng lực hành vi dân sự* | Dấu mộc ở "giả mạo" | | |
| 4-21 | `4.10#4` | D | T1 | `house_night` + `gypsy_walk` đi về nhà | **TRAO TRẢ VỀ NGÔI NHÀ MÀU HỒNG** | — | | |
| 4-22 | `4.10#5` | D | T1 | `screen_off` | **ĐÊM HÔM ĐÓ** · *Không bao giờ được bước ra khỏi cửa* | Màn hình tắt dần ở "phá hỏng" | 🅑 P2 | |
| 4-23 | `4.11` (nghỉ) | — | — | tối dần | — | — | | |
| 4-24 | `4.12#1` | H | T1 | `night_street` + `crowd` quay lưng | **XÃ HỘI CHỈ TIN NGƯỜI MẸ** · *Cú sốc năm 2011* | — | | |
| 4-25 | `4.12#2` | H | T1 | `locked_door` + một sợi chỉ mảnh (Pillow) | *LẮNG NGHE:* **SỢI DÂY VÔ HÌNH** | — | →C | |
| 4-26 | `4.13#1` | C | T9 | `hands` mờ | **GẮN KẾT CHẤN THƯƠNG** *(Trauma Bonding)* | — | | |
| 4-27 | `4.13#2` | C | T4 | `dress_hanger` tối | *Người gây ra bệnh tật — cũng là người duy nhất ôm ấp cô* → “thiên thần nhỏ của mẹ” | Câu trích ở cụm từ | | |
| 4-28 | `4.13#3` | C | T3 | `void` + đường ranh giới tan dần (Pillow) | **TÊ LIỆT KHẢ NĂNG PHÂN ĐỊNH RANH GIỚI** | Đường tan trong câu | | |
| 4-29 | `4.15#1` | H | T1 | `corridor` | **MỌI LỐI THOÁT HỢP PHÁP BỊ BỊT KÍN** | Tiếng bàn phím ở đầu | | |
| 4-30 | `4.15#2` | H | T1 | `night_screen` + `godejohn_screen` | **NICHOLAS GODEJOHN** · *Quen qua mạng Internet* | — | | |
| 4-31 | `4.15#3` | H | T9 | `void` + 2 bóng người, bóng đổ hoà làm một | **FOLIE À DEUX** *(Điên cuồng đôi)* | Bóng nhập ở "trượt vào" | | |
| 4-32 | `4.15#4`–`#5` | H | T1 `hero` | `house_night`, cửa mở, ánh sáng tràn | *Chỉ khi mẹ cô biến mất…* → **THÁNG 6 · 2015** | Cửa sáng ở "mở cửa" | ⊘ | |
| 4-33 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT PHÁP Y & LỜI KẾT** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT, DẤU HIỆU NHẬN DIỆN & LỜI KẾT · nền chủ đạo `court_dawn`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` | H | T1 | `court_dawn` | **TÒA ÁN BANG MISSOURI** | Búa gõ ở đầu câu | | |
| 5-02 | `5.02#2` | H | T2 | `court_dawn` mờ | *VỀ MẶT LUẬT PHÁP* · **MỘT TRỌNG TỘI KHÔNG THỂ CHỐI CÃI** | — | | |
| 5-03 | `5.02#3` | H | T2 | `court_dawn` mờ + bảng tên trên bàn (Pillow) | *Dan Patterson · Chánh biện lý hạt Greene* (chỉ chữ, V5) · **KẺ CHỦ MƯU — ĐỒNG THỜI LÀ NẠN NHÂN** | Tiêu đề ở "kẻ chủ mưu" | | |
| 5-04 | `5.03` (nghỉ) | — | — | giữ 5-03 | — | — | | |
| 5-05 | `5.04#1` | H | T5 | `court_dawn` | *2016 · Giết người cấp độ hai* · **10 NĂM** · *Mức án thấp nhất có thể* | Số đếm 0 → 10 | | |
| 5-06 | `5.04#2` | H | T4 `hero` | `prison_window` | *LỜI GYPSY TRONG TRẠI GIAM* → “Ở trong nhà tù của pháp luật, lần đầu tiên trong đời tôi cảm thấy mình được tự do hơn cả khi sống trong ngôi nhà của mẹ.” | Câu trích từng dòng từ dấu `:` | ⊘ | |
| 5-07 | `5.04#3` | H | T5 | `prison_window`, nắng sáng dần | *12 · 2023* · **85%** · *Chính thức được trả tự do* | Thanh tiến trình | | |
| 5-08 | `5.05` (nghỉ) | — | — | sáng dần | — | — | | |
| 5-09 | `5.06#1` | H | T1 | `court_dawn`, `pull` | **4 DẤU HIỆU CẢNH BÁO ĐỎ** *(Red Flags)* · *Chuyên gia tâm lý & Điều tra viên* | — | →C+D | |
| 5-10 | `5.07#1` | C | T8 cờ | `void` đỏ sẫm, 4 ô cờ | *01* · **BỆNH SỬ DÀY ĐẶC — XÉT NGHIỆM LUÔN MÂU THUẪN** | Cờ 1 tô đầy | hai badge | |
| 5-11 | `5.07#2` | C | T8 cờ | cờ 2 | *02* · **TRIỆU CHỨNG CHỈ CÓ KHI NGƯỜI CHĂM SÓC CÓ MẶT** | — | hai badge | |
| 5-12 | `5.08#1` | D | T8 cờ | cờ 3 | *03* · **HÀO HỨNG VỚI THỦ THUẬT · PHÔ TRƯƠNG BỆNH · ĐỔI BÁC SĨ** | 3 cụm theo cụm từ | hai badge · Sói sáng | |
| 5-13 | `5.08#2` | D | T8 cờ | cờ 4 | *04* · **CÔ LẬP KHỎI TRƯỜNG HỌC, BẠN BÈ, NGƯỜI THÂN** + dấu mộc “bảo vệ sức khỏe” | Dấu mộc ở cụm từ | hai badge | |
| 5-14 | `5.09` (nghỉ 2,5 s) | — | T8 | đủ 4 cờ, `still` | 4 dòng tóm tắt | — | ⊘ | |
| 5-15 | `5.10#1` | H | T1 | `podcast_desk`, đèn ấm dần | **HỒ SƠ KHÉP LẠI** | — | | |
| 5-16 | `5.10#2` | H | T1 `hero` | `house_dawn` + `gypsy_walk`, xe lăn bỏ lại | **TỰ BƯỚC ĐI TRÊN ĐÔI CHÂN CỦA MÌNH** | Trời sáng dần | ⊘ | |
| 5-17 | `5.10#3` | H | T1 | `cage` mở, nắng | **THỨ KHOÁC ÁO THIÊN THẦN** | Tiêu đề ở "khoác áo thiên thần" | | |
| 5-18 | `5.11` (nghỉ) | — | — | giữ 5-17 | — | — | | |
| 5-19 | `5.12#1` | H | T1 | `podcast_desk` | **CẢM ƠN CÁC KHÁCH MỜI** · *Nhân vật minh hoạ · giọng đọc AI* | Dàn khách mời: 5 ảnh P0 sáng lần lượt | dàn khách mời | |
| 5-20 | `5.12#2` | H | T10 | `podcast_desk` mờ | **HẸN GẶP LẠI Ở TẬP TIẾP THEO** · *Để lại góc nhìn của bạn ở phần bình luận* | — | 🅑 | |
| 5-21 | `5.13`–`5.14` | — | T2 | `podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | — | Bìa gập ở "Bụp"; mờ ra đen | ⊘ | ◼ |

**Tổng: 122 dòng = 104 shot có lời + 18 dòng không lời.** Phủ 128/128 câu, đúng thứ tự, cột Vai khớp người nói (kiểm tra bằng script ngày 22/10; `validate_shots.py` phải lặp lại).

**Xuất hiện của linh thú (ước tính):**

| Nhân vật | Lượt nói | Bán thân (câu đầu lượt + `🅑`) | Lần được mời (`→`) |
|---|---:|---:|---:|
| Cú · Host | 21 | ~22 (21 đầu lượt + 3 `🅑` − 2 đầu lượt bị `⊘`) | — |
| Sói · Điều tra viên | 4 | 7 | 4 |
| Cáo · Chuyên gia | 6 | 9 | 5 |
| Cừu · N1 | 1 | 2 | 1 |
| Mèo · N2 | 1 | 2 | 1 |

Badge hiện **suốt** mọi lượt của cả 5 nhân vật.

---

---

## PHỤ LỤC A (Tập 01) — CẤU TRÚC KỊCH BẢN (`parse_kichban.py` trên `kichban_tap01_22102026_v2.md`, 22/10/2026)

B1 phải sinh ra **đúng bảng này**; khác là dừng và báo.

| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |
|---|---|---:|---:|---|
| `1.01` | *BGM* | — | — | Hộp nhạc lên dây cót, bị drone bóp nghẹt |
| `1.02` | *SFX* | — | — | Còi cảnh sát xa, gõ cửa dồn dập |
| `1.03` | Cú · Host | 3 | 70 | Chậm, trầm, giữ khoảng cách khách quan |
| `1.04` | *Nghỉ 2,0 s* | — | — | |
| `1.05` | Cú · Host | 2 | 66 | (kế thừa) |
| `1.06` | *SFX* | — | — | Băng ghi âm "Tách" |
| `1.07` | **Cừu · N1** | 3 | 105 | Xúc động, chân thật như trả lời phỏng vấn |
| `1.08` | Cú · Host | 6 | 151 | Đẩy nhanh nhịp độ |
| `1.09` | *Nghỉ 2,0 s* | — | — | Nhạc dừng đột ngột (giữ drone −40 dB) |
| `1.10` | *SFX* | — | — | Bộ đàm rè, mở cửa phòng thẩm vấn |
| `1.11` | **Sói · Điều tra viên** | 8 | 143 | Hạ trầm, sắc lạnh, dứt khoát |
| `1.12` | *SFX* | — | — | "Tách", cello vào |
| `1.13` | Cú · Host | 2 | 60 | — |
| `2.01` | *BGM* | — | — | Máy đo nhịp tim + piano |
| `2.02` | Cú · Host | 3 | 68 | Đều đặn, dẫn dắt |
| `2.03` | *SFX* | — | — | Lật giấy hồ sơ |
| `2.04` | Cú · Host | 5 | 131 | (kế thừa) |
| `2.05` | *Nghỉ 1,5 s* | — | — | |
| `2.06` | Cú · Host | 3 | 57 | (kế thừa) |
| `2.07` | **Sói · Điều tra viên** | 10 | 348 | Đanh thép, nhấn từng chứng cứ |
| `2.08` | *SFX* | — | — | Khoá cửa sắt "Cạch" |
| `2.09` | Cú · Host | 4 | 91 | Trầm lắng |
| `3.01` | *BGM* | — | — | Ambient sâu, học thuật |
| `3.02` | Cú · Host | 5 | 159 | — |
| `3.03` | *Nghỉ 2,0 s* | — | — | |
| `3.04` | Cú · Host | 2 | 43 | — |
| `3.05` | **Cáo · Chuyên gia** | 9 | 239 | Phân tích chuyên môn, rõ ràng |
| `3.06` | *Nghỉ 1,5 s* | — | — | |
| `3.07` | Cú · Host | 2 | 69 | — |
| `3.08` | **Cáo · Chuyên gia** | 6 | 147 | Hạ giọng trầm, chậm rãi hơn |
| `3.09` | *Nghỉ 2,0 s* | — | — | |
| `3.10` | **Cáo · Chuyên gia** | 6 | 122 | (kế thừa) |
| `4.01` | *BGM* | — | — | Nhịp tim chậm + violin |
| `4.02` | Cú · Host | 2 | 55 | Trăn trở |
| `4.03` | **Mèo · N2** | 3 | 74 | Băn khoăn, hoài nghi |
| `4.04` | *Nghỉ 2,0 s* | — | — | |
| `4.05` | Cú · Host | 2 | 72 | — |
| `4.06` | *SFX* | — | — | Xiềng xích, kim loại |
| `4.07` | **Cáo · Chuyên gia** | 8 | 207 | — |
| `4.08` | *Nghỉ 1,5 s* | — | — | |
| `4.09` | Cú · Host | 3 | 61 | — |
| `4.10` | **Sói · Điều tra viên** | 5 | 135 | Trầm, thuật lại hồ sơ |
| `4.11` | *Nghỉ 2,0 s* | — | — | Host lắng xuống |
| `4.12` | Cú · Host | 2 | 66 | — |
| `4.13` | **Cáo · Chuyên gia** | 3 | 70 | — |
| `4.14` | *SFX* | — | — | Bàn phím gõ trong đêm |
| `4.15` | Cú · Host | 5 | 116 | — |
| `5.01` | *BGM* | — | — | Búa tòa án → piano ấm |
| `5.02` | Cú · Host | 3 | 116 | Điềm đạm, tổng kết |
| `5.03` | *Nghỉ 1,5 s* | — | — | |
| `5.04` | Cú · Host | 3 | 107 | (kế thừa) |
| `5.05` | *Nghỉ 2,0 s* | — | — | |
| `5.06` | Cú · Host | 1 | 60 | (kế thừa) |
| `5.07` | **Cáo · Chuyên gia** | 2 | 77 | Nhấn mạnh từng ý, góc lâm sàng |
| `5.08` | **Sói · Điều tra viên** | 2 | 82 | Tiếp lời, góc hành vi xã hội |
| `5.09` | *Nghỉ 2,5 s* | — | — | Piano dâng nhẹ |
| `5.10` | Cú · Host | 3 | 114 | Trầm ấm, truyền cảm |
| `5.11` | *Nghỉ 1,5 s* | — | — | |
| `5.12` | Cú · Host | 2 | 64 | (kế thừa) |
| `5.13` | *SFX* | — | — | Gấp hồ sơ "Bụp", tắt máy ghi âm "Tách" |
| `5.14` | *BGM* | — | — | Piano ngân 5 s rồi tắt |
| | **Tổng** | **128** | **3.545** | |

---

## PHỤ LỤC B (Tập 01) — 23 CHỖ GIẢM BẠO LỰC (`kichban_tap01_22102026.md` → `_v2.md`)

Nguyên tắc: **giữ dữ kiện và luận điểm tâm lý, bỏ chi tiết thể xác**. Không thêm dữ kiện mới. Số câu và mã câu không đổi.

| Câu | Bản gốc | Bản v2 |
|---|---|---|
| `1.03#3` | …khiến cả khu phố chết lặng: *"Con khốn đó chết rồi."* | …một dòng trạng thái ngắn ngủi, đầy hằn học, thông báo rằng bà Dee Dee đã qua đời – khiến cả khu phố chết lặng |
| `1.08#1` | họ tìm thấy thi thể của người mẹ… | họ phát hiện người mẹ… đã qua đời trong phòng ngủ |
| `1.08#5` | Kẻ máu lạnh nào đã sát hại người mẹ tận tụy ấy, rồi bắt cóc… | Ai đã gây ra cái chết của người mẹ tận tụy ấy, rồi đưa đi… |
| `1.11#8` | kế hoạch đoạt mạng bà mẹ "thánh thiện" | kế hoạch dẫn đến cái chết của bà mẹ "thánh thiện" |
| `2.02#1` | chọn cách kết liễu mẹ ruột | đi đến một lựa chọn cực đoan với chính mẹ ruột |
| `2.02#2` | căn phòng ngủ đẫm máu | căn phòng ngủ |
| `2.07#1` | trực tiếp hủy hoại cơ thể con gái | trực tiếp tác động lên sức khỏe con gái |
| `2.07#2` | hàm răng bị mục ruỗng và phải nhổ bỏ toàn bộ răng cửa | sức khỏe răng miệng của cô bé bị tổn hại nghiêm trọng |
| `2.07#3` | phẫu thuật đặt ống truyền thức ăn trực tiếp qua thành bụng vào dạ dày | đặt ống nuôi ăn qua dạ dày |
| `2.07#4` | bôi thuốc gây tê vào nướu để nước bọt chảy ròng ròng… cắt bỏ tuyến nước bọt | tạo ra những triệu chứng giả trước mắt bác sĩ… một ca phẫu thuật tuyến nước bọt không cần thiết |
| `3.02#2` | biến đứa con… thành một phế nhân đau đớn | khiến đứa con… phải sống như một người bệnh |
| `3.07#2` | bị nghi bỏ thuốc diệt cỏ vào thức ăn của mẹ kế và bỏ đói mẹ ruột… | bị nghi có những hành vi gây hại cho chính người thân trong gia đình |
| `3.08#5` | Hãy làm cho con bé tàn tật và phụ thuộc hoàn toàn vào mình | Hãy khiến con bé tin rằng mình bệnh tật và phụ thuộc hoàn toàn vào mẹ |
| `3.08#6` | không thể tự ăn uống mà phải truyền qua ống thông dạ dày… vị Chúa tể duy nhất nắm giữ sự sống | tin rằng mình… không thể tự chăm sóc bản thân… người duy nhất nắm giữ cuộc sống |
| `3.10#6` | yếu ớt, vô tính và… | yếu ớt và… |
| `4.07#2` | chịu đựng sự đau đớn lặp đi lặp lại | chịu đựng những áp lực tiêu cực lặp đi lặp lại |
| `4.07#7` | siết chặt lại đến mức bầm tím | siết chặt lại như một lời cảnh cáo không thành tiếng |
| `4.07#8` | những trận đòn bằng móc áo, bị bỏ đói và bị trói vào thành giường suốt hai tuần | những hình phạt nghiêm khắc và sự kiểm soát ngột ngạt |
| `4.10#5` | dùng búa đập nát chiếc máy tính… đe doạ đập nát các ngón tay | phá hỏng chiếc máy tính… cảnh cáo cô không bao giờ được bước ra khỏi cửa |
| `4.13#2` | người đầu độc Gypsy | người gây ra bệnh tật cho Gypsy |
| `4.13#3` | bạo hành thể xác | kiểm soát hà khắc |
| `5.02#2` | lên kế hoạch sát hại mẹ ruột | lên kế hoạch dẫn đến cái chết của mẹ ruột |
| `5.02#3` | bạo hành y khoa | lạm dụng y khoa |
| `5.08#1` | thủ thuật y khoa đau đớn | thủ thuật y khoa xâm lấn |

**Giữ nguyên có chủ đích:** "ung thư máu" (tên bệnh) · "giết người cấp độ hai" ở `5.04#1` (tên tội danh trong bản án — đổi sẽ sai sự thật) · "cạo trọc đầu", "váy công chúa" ở `2.04#5`, `3.10#2` (cốt lõi của luận điểm *tước đoạt sự trưởng thành*, không mang tính bạo lực).

---

---

*Bản sao v9 trước khi chuyển thành tiêu chuẩn: `.work/KeHoach_LamLai_Video_Tap01_v9_backup.md`. Không file nguồn nào bị sửa.*
