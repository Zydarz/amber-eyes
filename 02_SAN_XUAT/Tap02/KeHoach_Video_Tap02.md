# HỒ SƠ SẢN XUẤT TẬP 02 · "ĐẠI TÁ HAI MẶT" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A) — các mã A0…A13 trong file này trỏ về đó.
**Kịch bản:** `01_KICH_BAN/Tap02/kichban_tap02_22102026.md` · **Thành phẩm:** `02_SAN_XUAT/Tap02/xuat_ban/`
**Mẫu gốc:** `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md`. Lập ngày 22/10/2026, **chưa chạy** — mọi số đo thời gian ở đây là ước tính, sẽ thay bằng số đo thật sau bước 3.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap02/kichban_tap02_22102026.md` — đã sửa theo đánh giá và đối chiếu nguồn (`REVIEW_kichban_tap02.md`, lần 1 + lần 2). Bản trước khi sửa: `_truoc_review.md` |
| Lượt nói / câu / từ | 36 / **203** / 4.547 — Bản Director's Cut (25/10/2026): nâng cấp kịch tính, dời ổ cứng sang Hồi 4, bỏ giáo điều Hồi 5 |
| **Giọng (bộ A)** | Host `English_CaptivatingStoryteller` (trầm ấm) · Điều tra viên `Korean_ColdYoungMan` (lạnh lùng) · Chuyên gia `English_AssertiveQueen` (nhấn mạnh, nữ) · N1 `Vietnamese_kindhearted_girl` · N2 `English_captivating_female1`. Cao độ luôn 0, chỉ 4 cảm xúc an toàn (A4.2 G5, G8) |
| N1 / N2 | `1.07` Người từng phục vụ dưới quyền (Cừu) / `4.06` Người dân Tweed (Mèo) |
| Thời lượng | **25:19** (1.519,08 s) — bản 10 chỉ dấu tâm lý (khớp 100% audio master Tap02_master.mp3) |
| Mốc hồi (đo) | Hồi 1 · 00:23 · Hồi 2 · 05:44 · Hồi 3 · 09:53 · Hồi 4 · 14:44 · Hồi 5 · 19:52 |
| Bảng shot | **161 dòng** — 100% QC đạt (H13 khớp 3 chiều ảnh - chữ - lời thoại, P0 thẻ kết đã sửa hoàn chỉnh) |
| Nền dùng | 36/37 nền `t2_*` (chỉ bỏ `t2_cell_medical`) + 9 nền Tập 01. `t2_two_chairs`, `t2_hidden_drive`, `t2_tape_recorder` đã **tạo lại 23/10** (dịch vụ ảnh chạy lại) và dùng lại theo bảng shot gốc |
| Phân loại YouTube | Giáo dục · Không dành cho trẻ em · "Nội dung bị thay đổi hoặc tổng hợp" · tự đánh giá quảng cáo: chủ đề gây tranh cãi, có nhắc tội phạm tình dục ở mức khái quát (A10) |

## B2. Trạng thái và việc phải làm

| Hạng mục | Trạng thái |
|---|---|
| Kịch bản | ✅ Đã sửa, đã đối chiếu nguồn, parse đạt (215 câu, không còn từ cấm A9.2) |
| Ảnh nền | ✅ 37 nền `t2_*`; 3 nền tạo lại 23/10 (`t2_two_chairs`, `t2_hidden_drive`, `t2_tape_recorder`); duyệt ảnh tĩnh đủ 151 shot. **QC lại 23/10: 37/37 đạt** (đủ 2112×1188, không viền, không ảnh thừa) — `py -3 .work/qc_bg.py t2 --sheet` |
| Cấu hình script | ✅ Đã làm 22/10 — mục B3 nằm trong `EPISODES["02"]` của `.work/edition.py`; chạy mọi lệnh với `AE_EP=02`. Tập 01 kiểm hồi quy đạt |
| TTS, âm thanh, hình, đóng gói | ✅ **Bản hoàn thiện — dựng lại 05/11/2026** (khớp master audio Tap02_master.mp3 1.519,08 s) · 203/203 câu · âm thanh 1.519,05 s, −16,3 LUFS, max volume −2,0 dB, 0 khoảng câm > 0,3 s · 161 shot video render 6 worker → picture.mp4 1.519,07 s · **Tap02_master.mp4 525,7 MB — 1.519,07 s, 1920×1080@30, 45.572 khung, H.264 + AAC 194 kbps stereo, lệch hình/tiếng 0,017 s (17,2 ms)**. Decode check: 0 lỗi. Thẻ kết shot 5-36 hoàn chỉnh đầy đủ logo, tên kênh, khẩu hiệu. |
| Nguồn | ⚠ `xuat_ban/nguon_tham_khao.md` đã sinh (35 câu) — **người dùng điền link**; gợi ý ở mục "LẦN 2" của `01_KICH_BAN/Tap02/REVIEW_kichban_tap02.md` |
| **Sổ nguồn gốc** | ✅ `provenance.json` **587 dòng** — bổ sung 23/10: **9 file nhạc nền `assets/bgm/`** (trước đó thiếu hẳn — A10 dựa vào sổ này để kháng nghị khi bị Content ID nhận nhầm), 15 linh thú (`P0`/`full`/mascot), 41 ảnh gốc `_raw/t2_*`, 37 SFX tự tổng hợp, 15 ảnh người dùng cung cấp, 5 file nhận diện kênh. **92/92 tài sản Tập 02 đã có dòng.** Sao cũ: `.work/provenance.backup_23102026.json` |
| **Trước khi đăng** | ① Điền nguồn · ② Kiểm tra điều khoản thương mại (`provenance.json` — xem cột `kiem_tra_thuong_mai`; **9 file nhạc nền MiniMax còn "chưa"**, phải kiểm tra điều khoản MiniMax trước khi bật kiếm tiền; **ảnh linh thú + ảnh người dùng cung cấp còn "chưa"** — cần người dùng xác nhận công cụ đã dùng) · ③ Người dùng nghe toàn tập |
| **Thành phẩm** | xuat_ban/ — Tap02_master.mp4 (525,7 MB) · Tap02_master.mp3 (34,8 MB) · Tap02.srt (408 cue) · 	humbnail.png (1280×720) · mo_ta.txt (có mốc chương 00:20 / 05:44 / 09:53 / 14:44 / 19:52) |

### Quy tắc hình riêng của tập này (bổ sung V5, V9)

- **Không vẽ nạn nhân**, kể cả dạng bóng: Jessica Lloyd, Marie-France Comeau và hai người phụ nữ ở Tweed chỉ xuất hiện bằng **tên trên chữ**, hoặc không xuất hiện. Lý do: nạn nhân bị xâm hại tình dục và bị giết, một bóng người cũng dễ bị hiểu là minh hoạ hành vi.
- **Williams và Smyth** chỉ là bóng người có sẵn trong nền, mặt chìm hoàn toàn (`t2_two_chairs`, `t2_head_down`, `t2_suv_stop`). Không ghép tên lên bóng người.
- **Thẩm phán Robert Scott, người phát ngôn Hubert Genest**: chỉ tên (V5).
- **Không có chữ nào trên hình** nhắc tới đồ lót hay hành vi tình dục. Riêng thuật ngữ "rối loạn ái vật" ở `3.05#5` vẫn được đọc nhưng không hiện chữ.
- Tắt bán thân `⊘` ở 4 khoảnh khắc nặng nhất: `2.05#13`–`#16` (nấc 3–4), `3.11#4`, `4.10#9` ("Có bản đồ không?") và `4.12#2`–`#3`.

### B2.1 QC tự động — chạy lại 23/10/2026

| Lệnh | Kiểm | Kết quả |
|---|---|---|
| `py -3 .work/_qc_tap02_shots.py` | A9.2 — bảng shot vs kịch bản | **Đạt toàn bộ**: 215/215 câu thuộc đúng một shot và đúng thứ tự · cột Vai khớp timeline · mọi nền có file · chữ trích dẫn nguyên văn (lược bằng `…`) · mọi con số trên hình đều truy được về câu · 0 từ cấm / không nhắc hành vi tình dục · các shot liền nhau |
| `py -3 .work/qc_bg.py t2 --sheet` | ảnh nền | 37/37 đạt (2112×1188, không viền, không ảnh thừa) |
| `py -3 .work/_check_shots_sync.py` | bảng shot có khớp kế hoạch | **IDENTICAL** — `parse_shots.py` parse lại từ mục 6 cho ra đúng bảng đang dựng |
| `py -3 .work/_qc_tap02_frames.py` | A9.3 — 1 khung giữa mỗi shot **lấy từ chính mp4 thành phẩm** → contact sheet 16 ảnh/tờ | xem `.work/qc_tap02/sheet_*.png` |

**Ghi nhận (không phải lỗi nội dung):** Ở 4 shot T1 dài > 15 s (`1-11`, `1-18`, `1-25`, `1-31`), kế hoạch ghi beat neo theo cụm từ (`Tiêu đề ở "đêm khuya"`) nhưng renderer T1 chỉ đặt khối chữ ở **đầu câu** → cứu vãn bằng V2 ("hình chỉ đổi ở đầu câu"), nên tiêu đề hiện sớm hơn câu thoại khoảng 1–3 s. Mẫu T8 thì ngược lại: renderer tự neo từng mục danh sách vào cụm từ đầu của mục (`build_video3.py:626`) nên vẫn hiện dần đúng nhịp.

### B2.2 REVIEW CHUYÊN GIA VIDEO/ÂM THANH — 25/10/2026 (Mavis, độc lập)

Báo cáo đầy đủ: `02_SAN_XUAT/Tap02/Review_Video_Audio_Tap02.md`. Số đo thật trên `xuat_ban/Tap02_master.mp4`.

**⚠ P0 — THẺ KẾT TẬP ĐANG TRẮNG TRƠN, VIDEO KẾT BẰNG 2,7 S MÀN ĐEN.**
`shots_t02.json` (sửa 24/10 09:22) **đã có** chữ cho shot `5-29` (`HỒ SƠ TẬP 02 · ĐÃ ĐÓNG` + `AMBER EYES` + khẩu hiệu), nhưng `Tap02_master.mp4` dựng lúc 23/10 19:43 — tức dựng từ `shots_t02.json.bak` (23/10 18:09) mà bản đó có `"segments": []`. Đối chiếu 151 shot giữa hai bản: **chỉ khác đúng `5-29`**.
→ Đo trên mp4: 1598–1601 s là tờ giấy trắng **không chữ**; 1603,5–1605,7 s là đen tuyệt đối.
→ **Cần dựng lại riêng đoạn cuối** (`build_video3.py --stills 5-29` → `rerender_part.py` → `package.py --mux`), không cần dựng lại 92 phút. Chưa tự làm vì ghi đè lên thành phẩm — chờ người dùng duyệt.

**Các vấn đề còn lại (chưa sửa, xếp theo mức độ):**

| # | Vấn đề | Số đo | Đề xuất |
|---|---|---|---|
| P1 | Đỉnh âm thanh trong mp4 vượt trần −1,5 | WAV −1,5 dBFS → **AAC trong mp4 −0,9 dBTP** | Giới hạn lúc đóng gói (`loudnorm TP=-1.8`), đo lại trên mp4 — bẫy #38 A11 |
| P1 | Âm thanh gần như mono | side thấp hơn mid **34,74 dB**, tương quan L–R **0,999329** | Pan nền/SFX theo vị trí khung hình; mục tiêu side 12–18 dB |
| P1 | 3 giọng nữ chồng nhau | F0: Chuyên gia 206,1 · N2 233,5 (+2,16) · N1 254,3 (+1,48) Hz — thấp hơn ngưỡng G9 (≥4 nửa cung) và ngưỡng ≥3 nửa cung ghi trong hồ sơ | Đổi cao độ/giọng N1 hoặc N2 (chỉ 7 câu) — chờ người dùng nghe phương án |
| P2 | Chữ T1 mất tương phản trên nền sáng | shot `1-25`: "HOA VĂN LỐP RẤT GIỐNG DẤU VẾT…" chìm vào thân xe | `gradient_bottom(frac=0.45, alpha=180)` chỉ phủ 45% dưới khung → nâng `frac`/`alpha` hoặc thêm đệm tối dưới khối chữ |
| P2 | Hồi 5 nhỏ hơn phần còn lại | loudness 20 s: median −16,35 · min **−20,8** @1500 s; 12 s cuối mean −29,2 dB | Nâng nhạc outro ~2–3 dB, giữ đuôi piano ấm không fade hẳn (bẫy #35) |
| P3 | Encoder phần mềm, file lớn | Constrained Baseline (libopenh264) · 2,55 Mbps · 552,8 MB | Có GPU thì chuyển `h264_nvenc`/`qsv`; đã kiểm **không có lèn màu** (168–191 mức xám ở nền tối) |

**Đã kiểm và ĐẠT:** giải mã 0 lỗi · faststart · 0 khoảng câm > 0,3 s @ −60 dB · −15,9 LUFS · lời đầu 23,0 s · phụ đề **215/215 câu, lệch 0,000 s, văn bản nguyên văn 0 sai lệch** · QC A9.2 đạt toàn bộ · 0 freeze frame · không lộ mặt, không chữ lạ do AI vẽ · nghe mù: mỗi vai 1 người (10/10), H+D+C tách bạch 10/10.


## B3. Cấu hình riêng của Tập 02 (A12) — làm trước khi chạy

### B3.1 `.work/edition.py`

Đổi cấu hình bản tiếng Việt sang Tập 02. Bản EN giữ Tập 01:

| Biến | Tập 01 | **Tập 02** |
|---|---|---|
| `SCRIPT_JSON` | `script_v2.json` | `script_tap02.json` |
| `EP_DIR` | `02_SAN_XUAT/Tap01` | `02_SAN_XUAT/Tap02` |
| `PLAN` | `KeHoach_Video_Tap01.md` | `KeHoach_Video_Tap02.md` |
| `MASTER` / `SRT` | `Tap01_master` / `Tap01.srt` | `Tap02_master` / `Tap02.srt` |

**Đề nghị:** thêm biến môi trường `AE_EP=02` thay vì sửa cứng, để Tập 01 vẫn dựng lại được (đây chính là cải tiến "tap.json" ghi ở A12). Các file trung gian dùng chung tên (`audio_s/`, `timeline_s.json`, `shots.json`, `video3/`) sẽ bị **ghi đè** — sao lưu của Tập 01 trước khi chạy (B5 bước 0).

### B3.2 `.work/tts_sentences.py`

`N_ELEMENT = {"1.07": "N1", "4.06": "N2"}` (Tập 01 là `"4.03"`).

### B3.3 `.work/build_audio3.py`

| Chỗ | Tập 01 | **Tập 02** | Ghi chú |
|---|---|---|---|
| Mốc nhạc Hồi 1 (`cue_112`) | `"1.12"` | **`"1.16"`** | Ở Tập 02, `1.12` là lượt lời của Host, không phải mốc → script sẽ lỗi `StopIteration` nếu giữ nguyên |
| "Im lặng tuyệt đối" | `"1.09"` | `"1.09"` | Trùng mã — vẫn là chỗ "Nhạc nền dừng đột ngột" |
| Tiếng "Tách" | `("1.06", "1.12")` | **`("1.06",)`** | Tập 02 chỉ có một tiếng "Tách" ở mở đầu; tiếng tắt máy cuối tập vẫn đặt theo `end_voice` |
| `BED` | 1 cello · 2 piano · 3 ambient · 4 violin · 5 piano_warm | 1 `bgm_cello_sad` · 2 `bgm_piano_minimal` + `_v2` · 3 `bgm_cello_sad_v2` · 4 `bgm_sub_drone` + `bgm_ambient_deep` · 5 `bgm_piano_warm` | Theo `[BGM]` trong kịch bản |
| `SFX_CUES` | 11 dòng Tập 01 | bảng B4 | |
| Tên file ra | `Tap01_master.mp3` | `Tap02_master.mp3` | theo `edition.py` |

### B3.4 `.work/parse_shots.py`

- **`COMBO = {}` · `INSET = {}` · `BG2 = {}`**: ba bảng này đang khoá theo mã shot của Tập 01, nên sẽ gán nhầm cảnh Gypsy vào shot cùng mã của Tập 02. Tập 02 không cần cảnh ghép vì bóng người đã có sẵn trong nền.
- Dòng `elif sid == "5-21":` (shot cuối, từ hết lời tới hết tập) phải đổi thành **"dòng cuối của bảng"**. Shot cuối của Tập 02 là `5-29`.

### B3.5 `.work/package.py`

- `act_titles`:
  1. Hồi 1 · Sự tương phản phía sau quân hàm đại tá
  2. Hồi 2 · 4 bậc thang của vực thẳm
  3. Hồi 3 · Bên trong bộ não của sát nhân hai mặt
  4. Hồi 4 · Nghệ thuật bẻ gãy bộ óc quân sự
  5. Hồi 5 · Phán quyết, cảnh báo đỏ & lời kết
- Câu tóm tắt: `1.18#3` + `3.04#1` (giới thiệu hai cơ chế + câu "không có chẩn đoán công khai").
- `need`: danh sách B3.6.
- Mô tả: giữ mẫu A10 (không email, có Tổng đài 111).

### B3.6 Câu cần nguồn (`need` → `nguon_tham_khao.md`)

`1.03#4` · `1.05#1` · `1.05#2` · `1.10#2` · `1.12#2` · `1.14#2` · `1.17#3` · `2.04#1` · `2.04#2` · `2.05#6` · `2.05#7` · `2.05#13` · `2.05#15` · `2.08#7` · `2.08#8` · `3.08#10` · `4.03#6` · `4.08#3` · `4.08#7` · `4.10#1` · `4.10#3` · `4.10#7` · `4.10#8` · `4.10#9` · `4.11#5` · `4.11#8` · `4.12#2` · `5.02#4` · `5.04#2` · `5.04#3` · `5.04#5` · `5.04#6` · `5.04#7` · `5.04#8` · `5.04#9`

Link gợi ý cho từng nhóm: mục "LẦN 2" trong `01_KICH_BAN/Tap02/REVIEW_kichban_tap02.md`.

## B4. Âm thanh — SFX theo mốc

Dùng lại file có sẵn trong `assets/sfx/` khi đủ nghĩa. Bốn âm chưa có thì thêm vào `make_sfx.py` (tự tổng hợp, không tải file ngoài). Mức âm theo quy ước A4.4, neo tiếng "Tách" ở −6 dB; con số trong bảng là **mức khởi điểm**, phải nghe lại trên bản thành phẩm.

| File | Mốc | Offset | Mức | Mô tả trong kịch bản | Có sẵn? |
|---|---|---:|---:|---|---|
| `clock_tick.wav` | `1.01` | −2,5 s | −14 dB | Kim đồng hồ tích tắc khô khốc | ✅ |
| `tire_snow.wav` | `1.02` | −2,0 s | −8 dB | Lốp xe nghiến trên tuyết | ❌ tạo mới |
| `wind_snow.wav` + `footsteps.wav` | `1.11` | −2,2 s | −10 / −8 dB | Gió rít, bước chân trên tuyết | ❌ / ✅ |
| `door_knock.wav` | `1.13` | −0,9 s | −6 dB | Gõ cửa kính xe "Cốc… cốc…" (nhẹ hơn gõ cửa nhà) | ✅ |
| `impact.wav` + `lock_door.wav` | `1.15` | −1,0 s | −2 dB | Cửa sắt đóng "Rầm" | ✅ |
| `keyboard_night.wav` | `2.01` | −4,0 s | −14 dB | Gõ bàn phím chậm trong đêm | ✅ |
| `paper_rustle.wav` + `pop.wav` | `2.03` | −1,0 s | −8 / −16 dB | Lật hồ sơ + click chuột | ✅ |
| `fluoro_hum.wav` | `4.01` | −4,0 s | −20 dB | Đèn huỳnh quang vo ve | ❌ tạo mới |
| `chair_scrape.wav` + `hit_soft.wav` | `4.02` | −1,6 s | −6 / −4 dB | Kéo ghế kim loại, đặt cốc "Cộp" | ❌ / ✅ |
| `card_flip.wav` + `whoosh.wav` | `4.09` | −0,8 s | −6 / −12 dB | Mở tập ảnh, trượt ảnh "Xoẹt" | ✅ |
| `gavel.wav` ×3 | `5.01` | −2,4 / −1,7 / −1,0 s | +1 dB | Búa tòa "Cốp… Cốp… Cốp" | ✅ |
| `folder_close.wav` | `5.13` | −0,5 s | −8 dB | Đóng tập hồ sơ "Cạch" (tiếng tắt máy do `build_audio3` tổng hợp) | ✅ |

## 5. TRÌNH TỰ THỰC HIỆN (theo A3)

Chạy từ `D:\TEST\Gax\Audi`, đặt `PYTHONIOENCODING=utf-8`. Thời gian ước theo tỉ lệ Tập 01 (215 câu so với 128 câu; 25,5 phút so với 18,9 phút).

| Bước | Việc | Lệnh / cách làm | Ước tính | Đạt khi |
|---|---|---|---|---|
| 0 | Chọn tập | `set AE_EP=02` (PowerShell: `$env:AE_EP="02"`) — file trung gian có hậu tố `_t02`, **không cần sao lưu** Tập 01 | — | |
| 0b | Âm thanh | `py -3 .work/make_sfx3.py` (đã chạy) · `py -3 .work/make_acting_tap02.py` (đã chạy) · tuỳ chọn `make_sfx_h3.py` | — | `assets/sfx/t2/` đủ 32 file |
| 1 | Tách kịch bản | `py -3 .work/parse_kichban.py 01_KICH_BAN/Tap02/kichban_tap02_22102026.md .work/script_tap02.json` | < 1 s | Khớp đúng Phụ lục A (62 phần tử, 215 câu) |
| 2 | Đọc giọng | `py -3 .work/tts_sentences.py` | ~12 phút | 215 file; `qc_asr.py` CER ≈ 0 |
| 3 | Âm thanh tổng | `py -3 .work/build_audio3.py` | ~3 phút | `Tap02_master.mp3`, `timeline_s.json` |
| 4 | Kiểm tra âm thanh | A9.1 | 1 phút | 0 khoảng câm > 0,3 s; −16 ± 1 LUFS; lời đầu 22,8–23,5 s. **Mốc duyệt 1: người dùng nghe** — chú ý cách đọc "Pathfinder", "Smyth", "Comeau", "Genest", "Tweed", "ADN" |
| 5 | Nền mới | Không cần, trừ khi duyệt mắt loại `t2_house_missing` | — | |
| 6 | Bảng shot | `py -3 .work/parse_shots.py` | < 1 s | 151 shot; "nền chưa có file: []" |
| 7 | Kiểm tra chữ | A9.2 + kiểm tra riêng B6 | < 1 s | 215/215 câu phủ đúng; mọi số trên hình có trong câu |
| 8 | Ảnh tĩnh | `py -3 .work/build_video3.py --stills 40,330,640,980,1290` | 5 s | **Mốc duyệt 2** |
| 9 | Dựng hình | `py -3 .work/build_video3.py --workers 6` | ~30 phút | `picture.mp4` |
| 10 | Sửa cục bộ | `py -3 .work/rerender_part.py K` — K tính theo công thức A3 | ~6 phút/phần | |
| 11 | Phụ đề | `py -3 .work/subtitles.py` | < 1 s | `Tap02.srt` |
| 12 | Đóng gói | `py -3 .work/package.py --mux` | 1 phút | mp4, thumbnail, mô tả, nguồn |
| 13 | Kiểm tra cuối | A9.3 + A9.4 | ~7 phút | **Mốc duyệt 3** |

## 6. DANH SÁCH SHOT — TẬP 02 (viết theo A7)



**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### HỒI 1 — SỰ TƯƠNG PHẢN CỰC ĐẠI PHÍA SAU QUÂN HÀM ĐẠI TÁ · nền chủ đạo `t2_base_trenton`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s) | — | T1 | `t2_town_snow` hiện dần từ đen | *HỒI 01 · SỰ TƯƠNG PHẢN CỰC ĐẠI PHÍA SAU QUÂN HÀM ĐẠI TÁ* | Tiếng phản lực tụt thành drone; kim đồng hồ | ⊘ | |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t2_base_trenton` | **07 · 2009** · *Căn cứ Không quân Trenton — căn cứ không quân lớn nhất của quân đội Canada* | Gõ từng ký tự | ✦ Cú |  |
| 1-02 | `1.03#3` | H | T1 | `t2_oath_hall` | **LỄ NHẬM CHỨC** · *Trước các quan chức cấp cao trong quân đội* | — |  |  |
| 1-03 | `1.03#4` | H | T2 | `t2_oath_hall`, `still` | *NHẬN QUYỀN CHỈ HUY TỐI CAO* · **ĐẠI TÁ DAVID RUSSELL WILLIAMS** · *Một bản lý lịch hoàn hảo* | Dấu mộc ở "hoàn hảo" |  |  |
| 1-04 | `1.04` (nghỉ 1,5 s) | — | — | giữ 1-03 | — | — |  |  |
| 1-05 | `1.05#1` | H | T5 | `t2_base_trenton` | **46 TUỔI** · *Lái chuyên cơ đưa đón Nữ hoàng Anh Elizabeth II, Hoàng thân Philip và các Thủ tướng Canada* | Số đếm |  |  |
| 1-06 | `1.05#2` | H | T8 | `t2_base_trenton` mờ | *Biểu tượng của kỷ luật thép · Một người chồng mẫu mực · Vợ: lãnh đạo tại Quỹ Tim mạch và Đột quỵ Canada ở Ottawa* | Mỗi mục ở cụm từ |  |  |
| 1-07 | `1.05#3` | H | T2 | `t2_oath_hall` | *CON LỘ ANH HÙNG* · **NƠI ĐÓN LINH CỮU LIỆT SĨ** · *Từ chiến trường Afghanistan về* | Dấu mộc ở "linh cữu" |  |  |
| 1-08 | `1.05#4` | H | T1 | `t2_siren_wall` | **NGƯỜI ĐỨNG ĐẦU NGHI LỄ THIÊNG LIÊNG** · *Chính là Williams* | Tiêu đề ở "thiêng liêng" |  |  |
| 1-09 | `1.05#5` | H | T1 | `t2_base_trenton`, `pull` | *HÃY HÌNH DUNG:* **NHỮNG NGƯỜI TỪNG PHỤC VỤ DƯỚI QUYỀN ÔNG** | — | →N1 |  |
| 1-10 | `1.07#1` | N1 | T4 lời kể | `t2_base_trenton` ấm, mờ | “…hiện thân của sự chuẩn mực tuyệt đối.” | — | ✦ Cừu |  |
| 1-11 | `1.07#2` | N1 | T8 | `t2_oath_hall` mờ | *Điềm tĩnh · Chuẩn mực đến từng nếp gấp quân phục · Chưa từng to tiếng* | Mỗi mục ở cụm từ |  |  |
| 1-12 | `1.07#3`–`#4` | N1 | T4 lời kể | `t2_base_trenton` ấm | “…một người đàn ông mà ban đêm lại là một kẻ săn mồi nguy hiểm nhất.” | — | 🅑 |  |
| 1-13 | `1.08#1` | H | T1 | `t2_town_snow`, `pan` | **NHỮNG ĐÊM KHUYA THANH VẮNG** · *Biến mất vào bóng tối của những thị trấn ngoại ô* | Tiêu đề ở "đêm khuya" |  |  |
| 1-14 | `1.08#2`–`#3` | H | T1 | `night_street`, `still` | *Không còn một vị đại tá oai phong* → `#3`: **CHỈ CÒN MỘT BÓNG ĐEN RÌNH RẬP** | Tiêu đề ở "bóng đen" | ⊘ |  |
| 1-15 | `1.08#4` | H | T1 | `t2_base_trenton`, `push` | **HIỆU ỨNG HÀO QUANG** · *Một tấm khiên vô hình khiến cả xã hội lẫn cơ quan thực thi pháp luật bị che mắt suốt nhiều năm ròng* | Tiêu đề ở "Hào quang" |  |  |
| 1-16 | `1.09` (nghỉ 2 s) | — | — | giữ 1-12, nhạc tắt, chỉ còn nền trầm | — | — | ⊘ |  |
| 1-17 | `1.10#1` | H | T5 ngày | `t2_house_missing` | **28 · 01 · 2010** | Gõ từng ký tự |  | ✂ |
| 1-18 | `1.10#2`–`#3` | H | T2 | `t2_house_missing_dawn` | *JESSICA LLOYD · 27 TUỔI · BELLEVILLE* · **BIẾN MẤT KHỎI NHÀ RIÊNG** → `#3`: *Cảnh sát tỉnh Ontario mở hồ sơ điều tra · Một cuộc tìm kiếm quy mô lớn* | Dấu mộc ở "mở hồ sơ" |  |  |
| 1-19 | `1.12#1` | H | T1 | `t2_town_snow` | **KHÔNG TÌM RA MANH MỐI NÀO** · *Cảnh sát trong những ngày đầu tiên* | Gió, bước chân (SFX `1.11`) ở đầu |  |  |
| 1-20 | `1.12#2` | H | T7 | `t2_checkpoint` | **TỐI 4 THÁNG 2** · *Trạm kiểm soát lưu động · Gần nhà nạn nhân · Suốt đêm* | 2 ghim không nhãn, đường tự vẽ |  |  |
| 1-21 | `1.12#3` | H | T1 | `t2_tire_track`, `still` | *Mục tiêu duy nhất của trạm* → `#3`: **MỘT VỆT VÂN LỐP XE ĐỊA HÌNH HIẾM GẶP** | Tiêu đề ở "vân lốp" |  |  |
| 1-22 | `1.14#1`–`#2` | H | T3 so sánh | `t2_suv_stop` | **NISSAN PATHFINDER** → `#2`: *Thay vì chiếc BMW mà ông ta vẫn thường đi* | Gõ kính (SFX `1.13`) ở đầu |  |  |
| 1-23 | `1.14#3` | H | T1 `hero` | `t2_suv_stop` | **CHỈ HUY TRƯỞNG CĂN CỨ KHÔNG QUÂN TRENTON** | Tiêu đề ở "chính là" | ⊘ |  |
| 1-24 | `1.14#4`–`#5` | H | T1 | `t2_tire_track` | **VÂN LỐP RẤT GIỐNG DẤU VẾT TRÊN TUYẾT** → `#5`: *Không giữ được một sĩ quan cấp cao đĩnh đạc* | — |  |  |
| 1-25 | `1.14#6` | H | T1 | `t2_checkpoint_dawn` | **VẪN LÀ MỘT VỊ ĐẠI TÁ TỰ DO** · *Trong ba ngày tiếp theo* | — |  |  |
| 1-26 | `1.14#7` | H | T1 | `t2_interrogation_empty`, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN TÁI HIỆN BA NGÀY ĐÓ** | Cửa sắt "Rầm" (SFX `1.15`) sau câu | →D |  |
| 1-27 | `1.17#1` | D | T2 | `t2_tire_track` | *GẦN NHÀ NẠN NHÂN* · **HOA VĂN LỐP XE ĐỊA HÌNH KUMHO** · *Một dấu giày đi tuyết cỡ lớn* | Dấu mộc ở "dấu giày" | ✦ Sói |  |
| 1-28 | `1.17#2`–`#3` | D | T1 | `t2_suv_stop` | *Một cuộc dừng xe ngẫu nhiên* → `#3`: **SỰ TƯƠNG ĐỒNG ĐẾN KINH NGẠC** | Vệt sáng đèn pin ở "rọi xuống bánh xe" |  |  |
| 1-29 | `1.17#4` | D | T3 so sánh | `t2_checkpoint` | *Thế giới ngầm của Đại tá Russell Williams* · **CHẠM VÀO** · *Thế giới của cơ quan điều tra* | Cột phải ở "cơ quan điều tra" |  |  |
| 1-30 | `1.17#5` | D | T6 | `pinboard` | *Ba ngày đêm · Đối chiếu dấu lốp · Rà soát lịch trình di chuyển* → **LỆNH KHÁM XÉT KHẨN CẤP** · *Ottawa · Tweed* | Mỗi cụm từ một mốc |  |  |
| 1-31 | `1.17#6` | D | T1 | `t2_phone_call` | *Thay vì tung quân vây bắt ồn ào* · **MỘT CUỘC GỌI LỊCH SỰ** · *Mời đến trụ sở cảnh sát tỉnh* | Tiêu đề ở "cuộc gọi" |  |  |
| 1-32 | `1.18#1` | H | T1 | `t2_podcast_desk`, cassette quay | **HỒ SƠ PHÂN TÍCH TÂM LÝ HỌC TỘI PHẠM** | — | 🅑 |  |
| 1-33 | `1.18#2` | H | T2 | `records` | *HỒ SƠ* · **ĐẠI TÁ RUSSELL WILLIAMS** | Dấu mộc ở "Hồ sơ Đại tá" |  |  |
| 1-34 | `1.18#3` | H | T9 → T10 | `t2_two_masks` | **QUY LUẬT LEO THANG HÀNH VI** · **SỰ PHÂN MẢNH TÂM TRÍ** → *TẬP 02 · ĐẠI TÁ HAI MẶT* | Mỗi thuật ngữ ở cụm từ; tên tập cuối câu |  |  |
| 1-35 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **4 BẬC THANG CỦA VỰC THẲM** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ TỘI ÁC · nền chủ đạo `t2_folder_tree`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` | H | T1 | `t2_cottage_search` | **MỘT VỤ ÁN ĐƠN LẺ** · *Cảnh sát tỉnh Ontario đối mặt với vụ biến mất* | — |  |  |
| 2-02 | `2.02#2` | H | T1 | `t2_cottage_search`, `push` | **MỘT BỨC TRANH GHÊ RỢN LỘ DIỆN** · *Tweed · Belleville* | — |  |  |
| 2-03 | `2.04#1` | H | T1 | `t2_house_missing_dawn` | **KẺ BẮT CÓC KHÔNG XUẤT HIỆN TỪ HƯ KHÔNG** | Lật hồ sơ (SFX `2.03`) ở đầu |  |  |
| 2-04 | `2.04#2` | H | T1 | `t2_escalation_stairs` | *Âm thầm hoàn thiện kỹ năng săn mồi* · **BÓNG MA TRONG BÓNG TỐI** | — |  |  |
| 2-05 | `2.04#3` | H | T1 | `t2_escalation_stairs` | *Đỉnh chóp của một tảng băng chìm* · **4 NẤC THANG LEO THANG HÀNH VI** | — |  |  |
| 2-06 | `2.04#4` | H | T1 | `pinboard` mờ, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN PHÂN TÍCH PHƯƠNG THỨC HOẠT ĐỘNG** | — | →D |  |
| 2-07 | `2.05#1` | D | T2 | `pinboard` | **4 GIAI ĐOẠN LEO THANG** · *Dữ liệu số và chứng cứ thu giữ* | Bộ đếm `0/4`, 4 thẻ trống ghim lên |  |  |
| 2-08 | `2.05#2`–`#3` | D | T3 `1/4` | `t2_open_window` | *NẤC 01* · **NHÌN TRỘM** → `#3`: *Lảng vảng ban đêm trong các khu dân cư vắng* | — |  |  |
| 2-09 | `2.05#4`–`#6` | D | T3 `2/4` | `t2_drawer_dark` | *NẤC 02* · **ĐỘT NHẬP LẤY ĐỒ RIÊNG TƯ** → `#6`: *Những vụ trộm đầu tiên cảnh sát lần ra: 2006* | — |  |  |
| 2-10 | `2.05#7` | D | T5 | `t2_open_window` mờ | *09 · 2007 – 11 · 2009* · **82** · *Vụ đột nhập và đột nhập bất thành* | Số đếm 0 → 82 |  |  |
| 2-11 | `2.05#8`–`#9` | D | T8 gạch bỏ | `records` | *Tiền bạc · Trang sức* → `#9`: **ĐỒ RIÊNG TƯ CỦA PHỤ NỮ** | Gạch ở "không lấy" |  |  |
| 2-12 | `2.05#10` | D | T8 | `t2_logbook` | *NGHI THỨC LẶP LẠI Y HỆT* · *Chụp ảnh · Lấy đồ · Ghi chép lại* | Mỗi mục ở cụm từ |  |  |
| 2-13 | `2.05#11`–`#13` | D | T3 `3/4` | `t2_escalation_stairs` | *NẤC 03* · **XÂM NHẬP KHI CÓ NGƯỜI Ở NHÀ** → `#12`: *09 · 2009 · Ngưỡng kích thích tiếp tục bị lờn* → `#13`: *Hai người phụ nữ · Quanh thị trấn Tweed* | — | ⊘ ở `#13` |  |
| 2-14 | `2.05#14`–`#16` | D | T3 `4/4` | `fog`, tối dần | *NẤC 04* · **CÁI CHẾT** → `#15`: *Cuối tháng 11 · 2009 · Marie-France Comeau · Hạ sĩ · 37 tuổi · Phi đoàn 437* → `#16`: *Hai tháng sau · Jessica Lloyd* | Chỉ chữ, không hình người | ⊘ |  |
| 2-15 | `2.06` (nghỉ 1,5 s) | — | — | giữ 2-14, tối dần | — | — | ⊘ |  |
| 2-16 | `2.07#1` | H | T1 | `t2_two_masks` | **ĐỘNG LỰC BẤT ĐỐI XỨNG** · *Quyền lực tàn nhẫn của kẻ săn mồi* | — |  |  |
| 2-17 | `2.07#2`–`#3` | H | T3 so sánh | `t2_two_masks` | *Hạ sĩ Marie-France Comeau · Cấp dưới phục vụ trong căn cứ* → `#3`: *Jessica Lloyd · Cô gái trẻ độc thân sống trong căn nhà riêng* | Cột phải ở "Jessica Lloyd" |  |  |
| 2-18 | `2.07#4`–`#6` | H | T1 | `t2_drawer_dark` | *Cả hai đều bị tước đoạt mạng sống* → `#5`: **BẢN NĂNG SĂN MỒI LỆCH LẠC + KỶ LUẬT QUÂN SỰ** → `#6`: *Chụp ảnh mọi thứ, ghi chép lại từng lần đột nhập* | — |  |  |
| 2-19 | `2.07#7` | H | T1 | `pinboard`, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN LÀM RÕ** | — | →D |  |
| 2-20 | `2.08#1`–`#3` | D | T9 | `records` | *Hai khái niệm phải phân biệt* → `#2`: **THỦ ĐOẠN GÂY ÁN** *(Modus Operandi)* → `#3`: *Điều chỉnh liên tục qua 82 vụ đột nhập* | Thuật ngữ ở `#2` |  |  |
| 2-21 | `2.08#4` | D | T9 | `t2_drawer_dark` | *TÂM LÝ HỌC* · **DẤU ẤN TÂM LÝ** *(Signature)* | Thuật ngữ ở `#4` |  |  |
| 2-22 | `2.08#5`–`#7` | D | T1 | `t2_boot_evidence` | **HẮN KHÔNG LẤY ĐỒ ĐỂ BÁN** → `#6`: *Mặc đồ nạn nhân · Chụp ảnh tự sướng trước gương* → `#7`: *Thứ hắn cần để duy trì hưng phấn tâm lý* | — |  |  |
| 2-23 | `2.08#8` | D | T1 | `t2_tire_track` | **DẤU VẾT LỐP XE DẪN CẢNH SÁT TỚI HẮN** | — |  |  |
| 2-24 | `2.08#9` | D | T1 | `t2_hidden_drive` | **CHIẾC CHÌA KHÓA DUY NHẤT** · *Kho dữ liệu bí mật bóc trần hoàn toàn bề mặt thật của vị đại tá* | — |  |  |
| 2-25 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **BÊN TRONG BỘ NÃO CỦA SÁT NHÂN HAI MẶT** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI PHẪU TÂM LÝ · nền chủ đạo `t2_brain_neural`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T1 | `t2_command_chair` | **MỘT CÂU HỎI HÓC BÚA ĐẾN RỢN NGƯỜI** | — |  |  |
| 3-02 | `3.02#2` | H | T8 | `t2_command_chair` tối | *Địa vị · Danh vọng · Một người vợ tài năng · Sự kính trọng của cả một quốc gia* → **TẠI SAO ĐÁNH CƯỢC TẤT CẢ?** | Mỗi mục ở cụm từ; tiêu đề ở "đánh cược" |  |  |
| 3-03 | `3.03` (nghỉ 2 s) | — | — | giữ 3-02 | — | — |  |  |
| 3-04 | `3.04#1` | H | T2 | `records` | *TRƯỚC KHI PHÂN TÍCH* · **KHÔNG TỒN TẠI MỘT CHẨN ĐOÁN LÂM SÀNG CÔNG KHAI NÀO** · *Về Russell Williams* | — | 🅑 |  |
| 3-05 | `3.04#2` | H | T1 | `t2_brain_neural` mờ | **GIÚP TA ĐẶT CÂU HỎI ĐÚNG** · *Không phải một sự phán xét đã được cơ quan chuyên môn xác nhận* | — |  |  |
| 3-06 | `3.04#3` | H | T1 | `t2_brain_neural`, `push` | *LẮNG NGHE:* **CHUYÊN GIA TÂM LÝ** → *Các tầng cơ chế vận hành bên trong bộ não* | — | →C |  |
| 3-07 | `3.05#1`–`#3` | C | T9 | `t2_brain_neural` + sơ đồ 3 vòng (dùng lại `brain3` Tập 01) | *Không phải một kẻ loạn thần mất trí* → `#2`: **HOÀN TOÀN TỈNH TÁO** → `#3`: **3 TẦNG CƠ CHẾ TÂM LÝ** | 3 vòng sáng ở `#3` | ✦ Cáo |  |
| 3-08 | `3.05#4` | C | T9 | `t2_escalation_stairs` | *TẦNG 01* · **CHU KỲ ẢO TƯỞNG** · *Sự lờn Dopamine · Ngòi nổ điểm gãy* | — |  |  |
| 3-09 | `3.05#5` | C | T1 | `t2_escalation_stairs`, `pan` | **ĐẶC ĐIỂM THƯỜNG THẤY** · *Hành vi ban đầu của hắn* | Tiêu đề ở "đặc điểm thường thấy" |  |  |
| 3-10 | `3.05#6` | C | T9 | `t2_brain_neural` + đường nhịp tăng vọt (Pillow) | **DOPAMINE** · *Phấn khích và phần thưởng* → `#6`: *Cảm giác hưng phấn quyền lực tột độ* | Nhịp nhấp nháy ở `#6` |  |  |
| 3-11 | `3.05#7` | C | T1 | `t2_brain_neural`, đường nhịp phẳng dần | **CƠ CHẾ DUNG NẠP KÍCH THÍCH** · *Não bộ con người có cơ chế này* | — |  |  |
| 3-12 | `3.05#8`–`#9` | C | T1 | `t2_brain_neural`, đường nhịp phẳng dần | **HÀNH VI CŨ TRỞ NÊN QUEN THUỘC** → `#9`: *Phải tăng liều lượng rủi ro để tìm lại khoái cảm ban đầu* | — | 🅑 |  |
| 3-13 | `3.05#10` | C | T1 `hero` | `t2_stairs_dark`, tối dần | *NGÒI NỔ TÂM LÝ* *(Precipitating Trigger)* · *Tháng 7 năm 2009 · Thăng cấp chỉ huy trưởng căn cứ Trenton* | Tiêu đề ở "Ngòi nổ" | ⊘ |  |
| 3-14 | `3.06` (nghỉ 1,5 s) | — | — | giữ 3-13 | — | — |  |  |
| 3-15 | `3.07#1` | H | T3 so sánh | `t2_two_masks` | *BAN NGÀY* · *Điều hành hàng ngàn binh sĩ · Sống bên cạnh người vợ tài năng* → `#1`: *BAN ĐÊM* · **MỘT KẺ KHÁC HOÀN TOÀN** · *Không hề phát điên hay cắn rứt lương tâm* | Cột phải ở "ban đêm" | →C |  |
| 3-16 | `3.08#1`–`#2` | C | T9 | `t2_two_drawers` | *TẦNG 02* · **SỰ PHÂN MẢNH TÂM TRÍ TUYỆT ĐỐI** → `#2`: *(Compartmentalization)* · *Hệ thống tự bào chữa · Hai ngăn kéo hoàn toàn biệt lập* | Thuật ngữ Anh ở `#2` |  |  |
| 3-17 | `3.08#3`–`#5` | C | T3 so sánh | `t2_two_drawers` | *Ngăn kéo 01* · **ĐẠI TÁ WILLIAMS** · *Mẫu mực · Chu đáo · Chuẩn mực đạo đức tại Ottawa* → `#5`: *Ngăn kéo 02* · **KẺ SĂN MỒI BÓNG ĐÊM** · *Giải phóng xung lực tàn bạo tại Tweed* | Cột phải ở `#5` |  |  |
| 3-18 | `3.08#6`–`#8` | C | T1 | `t2_drawer_dark` | **ĐÓNG CHẶT CÁNH CỬA CỦA NGĂN KÉO KIA** → `#7`: *Lá chắn bình thường hóa · Tự ru ngủ mình là người đàn ông danh giá* → `#8`: *Trung hòa đạo đức · 82 vụ trộm đầu tiên* | Ngăn kéo đóng ở "đóng chặt" |  |  |
| 3-19 | `3.08#9`–`#10` | C | T1 | `t2_interrogation_empty` | *Tự biện minh: nạn nhân đã thấy mặt mình* → `#10`: **HẮN KHÔNG THỂ TỰ GIẢI THÍCH** | — | ⊘ |  |
| 3-20 | `3.08#11` | C | T4 `hero` | `t2_interrogation_empty` | “Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng.” | Câu trích từng dòng từ dấu `:` | ⊘ |  |
| 3-21 | `3.08#12`–`#13` | C | T1 | `t2_interrogation_empty` | **CÂU TRẢ LỜI TRƠ TRẼN NHẤT** → `#13`: *Cơ chế tự bào chữa đã ăn sâu vào tiềm thức của hắn* | — | 🅑 |  |
| 3-22 | `3.09` (nghỉ 2 s) | — | — | giữ 3-22 | — | — |  |  |
| 3-23 | `3.10#1`–`#2` | H | T1 | `t2_command_chair`, `push` | **GÓC NHÌN CỦA HẮN VỚI NHỮNG NGƯỜI PHỤ NỮ** · *Tại sao lạnh lùng với chính cấp dưới?* | — | →C |  |
| 3-24 | `3.11#1` | C | T9 | `t2_command_chair` | *TẦNG 03* · **SỰ VẬT HÓA NẠN NHÂN** *(Objectification)* → *Ái kỷ ác tính* | Thuật ngữ ở "vật hóa" |  |  |
| 3-25 | `3.11#2` | C | T9 | `t2_brain_neural` | *TÂM LÝ HỌC* · **THUYẾT TÂM TRÍ** *(Theory of Mind)* · *Thiếu hụt năng lực thấu cảm cảm xúc* | — |  |  |
| 3-26 | `3.11#3` | C | T1 | `t2_base_trenton` | **KHÔNG PHẢI NHỮNG CON NGƯỜI** · *Không có sinh mệnh, ước mơ hay nỗi đau* | — |  |  |
| 3-27 | `3.11#4` | C | T1 | `t2_two_masks` | **BỊ GIÁNG CẤP THÀNH ĐẠO CỤ SỐNG** | Tiêu đề ở "giáng cấp" |  |  |
| 3-28 | `3.11#5` | C | T1 | `t2_command_chair` tối | **HƯNG PHẤN QUYỀN LỰC** · *Ảo tưởng tối thượng · Quyền sinh tử như một vị Chúa trời* | — |  |  |
| 3-29 | `3.11#6` | C | T4 `hero` | `t2_command_chair` tối | “Ta kiểm soát các ngươi, và không ai có thể chạm tới ta.” | Câu trích ở "Ta kiểm soát" (lời độc thoại tưởng tượng — dấu “” màu tím `violet` của Cáo, không phải lời thật) | 🅑 |  |
| 3-30 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **NGHỆ THUẬT BẺ GÃY BỘ ÓC QUÂN SỰ** | — | ⊘ | ◼ |

### HỒI 4 — ĐẤU TRÍ PHÒNG THẨM VẤN · nền chủ đạo `t2_two_chairs`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.03#1`–`#2` | H | T5 ngày | `t2_interrogation_empty` | **07 · 02 · 2010** · *Chủ nhật · Trụ sở cảnh sát tại Ottawa · 3 giờ chiều* | Gõ từng ký tự; đèn huỳnh quang (SFX `4.01`) |  |  |
| 4-02 | `4.03#3`–`#4` | H | T3 so sánh | `t2_two_chairs` | *Một bên bàn* · **ĐẠI TÁ RUSSELL WILLIAMS** · *Quần áo dân sự* → `#4`: *Đối diện* · **THÁM TỬ JIM SMYTH** · *Chuyên gia khoa học hành vi · Cảnh sát tỉnh Ontario* | Cột phải ở `#4`; chỉ tên, không gắn lên bóng (V5) |  |  |
| 4-03 | `4.03#5`–`#6` | H | T2 | `t2_interrogation_empty` | **TỰ NGUYỆN ĐẾN ĐÂY** · *Sau một cuộc gọi mời trao đổi* → `#6`: *Bình thản ngồi lại · Từ chối luật sư* | — |  |  |
| 4-04 | `4.04` (nghỉ 2 s) | — | — | giữ 4-03 | — | — |  |  |
| 4-05 | `4.05#1` | H | T1 | `t2_tape_recorder`, `push` | *LẮNG NGHE:* **KÝ ỨC CỦA NGƯỜI DÂN** · *Tiếng lòng của những người từng sống trong bóng tối của Williams* | — | →N2 |  |
| 4-06 | `4.06#1`–`#2` | N2 | T4 lời kể | `t2_house_missing_dawn` | “…thị trấn nhỏ Tweed của chúng tôi sống trong một nỗi bất an mơ hồ…” | — | ✦ Mèo |  |
| 4-07 | `4.06#3` | N2 | T4 lời kể | `bedroom_door` | “…Chúng tôi tưởng mình đang hoang tưởng… cho đến khi sự thật vỡ lở.” | — | ✦ Mèo |  |
| 4-08 | `4.06#4` | N2 | T4 lời kể | `bedroom_door` | “…một kẻ đội lốt sĩ quan cấp cao đã đứng ngay trong phòng ngủ, nhìn chằm chằm vào bạn trong bóng tối.” | — | 🅑 |  |
| 4-09 | `4.07#1`–`#3` | H | T1 | `t2_two_chairs`, `pull` | **KỸ THUẬT THẨM VẤN TÂM LÝ** · *Thám tử Jim Smyth* → `#3`: *LẮNG NGHE:* **TỪNG NƯỚC CỜ** | — | →D |  |
| 4-10 | `4.08#1`–`#2` | D | T9 | `t2_two_chairs` | **NGHỆ THUẬT XÂY DỰNG SỰ KẾT NỐI** *(Rapport Building)* → `#2`: *Giọng điệu phẳng lặng, tôn trọng · Dẫn dắt vào chiếc bẫy của sự tự phụ* | — |  |  |
| 4-11 | `4.08#3`–`#4` | D | T1 | `t2_two_chairs` | *SẴN SÀNG CUNG CẤP NHỮNG GÌ?* → `#4`: **ADN · VÂN TAY · DẤU GIÀY** | — |  |  |
| 4-12 | `4.08#5` | D | T3 so sánh | `t2_tape_recorder` | *Trong lúc hai người đối thoại* · **MŨI TRINH SÁT THỰC ĐỊA** · *Lệnh khám xét tại Ottawa và Tweed* | Đèn xanh đỏ |  |  |
| 4-13 | `4.08#6` | D | T3 so sánh | `t2_boot_evidence`, `still` | *Dấu giày tuyết tại hiện trường* · *Dấu giày của chính Williams* → “Chúng giống hệt nhau.” | Câu trích ở "và nói" |  |  |
| 4-14 | `4.08#7` | D | T1 | `t2_head_down` | *MỘT ĐỀ NGHỊ KỲ LẠI* → “Cứ gọi tôi là Russ.” | — |  |  |
| 4-15 | `4.08#8` | D | T4 | `t2_two_chairs` | **CHIẾC THÒNG LỌNG VÔ HÌNH BẮT ĐẦU SIẾT CHẶT** | Trượt ảnh "Xoẹt" ở đầu |  |  |
| 4-16 | `4.10#1` | D | T1 | `t2_hidden_drive` | **Ổ CỨNG TRÊN TRẦN TẦNG HẦM** · *Hàng nghìn bức ảnh và ghi chép chi tiết* | — | ⊘ |  |
| 4-17 | `4.10#2`–`#3` | D | T4 `hero` | `t2_siren_wall` | *Smyth nhìn thẳng vào mắt Williams* → `#3`: “Vợ ông giờ đã biết chuyện gì đang xảy ra.” | Câu trích ở "nói thêm" | ⊘ |  |
| 4-18 | `4.10#4`–`#6` | D | T4 | `t2_head_down` | *Toàn bộ thế giới danh dự đã hoàn toàn sụp đổ* → `#6`: “Tôi không biết phải nói gì.” | — |  |  |
| 4-19 | `4.10#7` | D | T4 | `t2_interrogation_empty`, `still` | *4 giờ 40 phút sau* → “Vậy, cô ấy ở đâu?” | Câu trích ở "hỏi khẽ" |  |  |
| 4-20 | `4.10#8` | D | T4 `hero` | `t2_forest_map` | “Có bản đồ không?” | — | ⊘ | ✂ |
| 4-21 | `4.10#9` | D | T1 | `t2_interrogation_early` | *Gần 6 tiếng tiếp theo* · **TỪNG VỤ MỘT** | — |  |  |
| 4-22 | `4.11#1`–`#3` | C | T1 | `t2_two_drawers` | **KHOẢNH KHẮC TÂM LÝ SỤP ĐỔ** → `#3`: *Bức tường giữa hai ngăn kéo tâm trí · Vỡ vụn* | Hai ngăn kéo bật mở ở `#3` | 🅑 |  |
| 4-23 | `4.11#4` | C | T4 | `t2_interrogation_empty` | *Theo bản ghi thẩm vấn* · **NGƯỜI VỢ** → “Tôi muốn giảm thiểu ảnh hưởng lên vợ tôi.” | — |  |  |
| 4-24 | `4.11#5` | C | T1 | `t2_two_chairs` | *Smyth đáp rằng ông cũng muốn vậy* · **CON ĐƯỜNG DUY NHẤT LÀ SỰ THẬT** | — |  |  |
| 4-25 | `4.11#6`–`#7` | C | T3 so sánh | `void` | *NỖI LO VỢ MÌNH VÀ CĂN CỨ* → *KHÔNG PHẢI NỖI ĐAU CỦA NẠN NHÂN* | — | ⊘ |  |
| 4-26 | `4.11#8` | C | T1 | `void` | **KHÔNG PHẢI SỰ ĂN NĂN HỐI LỖI** | — |  |  |
| 4-27 | `4.11#9` | C | T1 | `t2_head_down` | **MẶT NẠ DANH DỰ VỠ VỤN** · *Sự thương hại bản thân tột độ · Trước người thân và xã hội* | — | 🅑 |  |
| 4-28 | `4.12#1` | H | T1 `hero` | `t2_head_down` | **CHÍNH THỨC GỤC NGÃ** · *Trước sức ép của sự thật khách quan* | — | ⊘ |  |
| 4-29 | `4.12#2` | H | T1 | `t2_head_down` | **JESSICA LLOYD** · *Đánh dấu trên bản đồ nơi hắn phi tang* | — |  |  |
| 4-30 | `4.12#3` | H | T8 | `records` | *THỪA NHẬN* · *Nữ hạ sĩ Marie-France Comeau · Hai vụ tấn công tại Tweed* | Mỗi mục ở cụm từ |  |  |
| 4-31 | `4.12#4` | H | T1 | `t2_folder_tree` | *Kho dữ liệu trong ổ cứng* · **82 VỤ ĐỘT NHẬP BÍ MẬT** | — |  |  |
| 4-32 | `4.12#5` | H | T5 | `pinboard` | **88** · *88 Cáo buộc hình sự · Một người đàn ông duy nhất* | Số đếm 0 → 88 |  |  |
| 4-33 | `4.12#6` | H | T1 | `t2_head_down` | **VỎ BỌC HÀO NHOÁNG TAN THÀNH MÂY KHÓI** | — |  |  |
| 4-34 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT, CẢNH BÁO ĐỎ & LỜI KẾT** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT, BÀI HỌC CẢNH BÁO ĐỎ & LỜI KẾT · nền chủ đạo `t2_courtroom`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#2` | H | T5 ngày | `t2_courtroom` | **10 · 2010** · *Tòa án Cấp cao Ontario · Thẩm phán Robert Scott · Belleville* (chỉ chữ, V5) | Búa gõ ba lần (SFX `5.01`) trước câu |  |  |
| 5-02 | `5.02#3` | H | T5 | `t2_courtroom` | *Ngày 18 tháng 10* · **88** · *Nhận tội trước toàn bộ cáo buộc* | Số đếm |  |  |
| 5-03 | `5.02#4` | H | T8 | `t2_gavel` | *NGÀY 21 · THẨM PHÁN TUYÊN PHẠT* · *Hai mức tù chung thân chạy song song · 10 năm cho mỗi tội tấn công tình dục · 10 năm cho mỗi tội giam giữ trái phép · 1 năm cho mỗi trong 82 vụ đột nhập* | Mỗi mục ở cụm từ (câu dài ~20 s → 5 beat) |  |  |
| 5-04 | `5.02#5`–`#6` | H | T5 | `t2_gavel` | **25 NĂM** · *Không được xét ân xá* → `#6`: *Mức án tối thiểu luật hình sự Canada bắt buộc* | Số đếm 0 → 25 |  |  |
| 5-05 | `5.03` (nghỉ 2 s) | — | — | giữ 5-04 | — | — |  |  |
| 5-06 | `5.04#1` | H | T1 | `t2_oath_hall` tối | **SỰ SỤP ĐỔ HOÀN TOÀN VỀ DANH DỰ** | Gọi lại hình lễ nhậm chức, nay tối |  |  |
| 5-07 | `5.04#2`–`#4` | H | T8 gạch bỏ | `t2_medals_cut` | *Quân hàm · Huân chương · Sắc lệnh phong cấp · Tiểu sử trên trang Bộ Quốc phòng* | Mỗi câu gạch mục tương ứng |  |  |
| 5-08 | `5.04#5` | H | T1 | `t2_uniform_fire` | **ĐỐT QUÂN PHỤC** · *Căn cứ Trenton · Một cơ sở vốn dùng để tiêu hủy tài liệu* | Lửa bùng ở "đốt quân phục" |  |  |
| 5-09 | `5.04#6`–`#7` | H | T2 | `t2_uniform_fire` mờ | *Hubert Genest · Người phát ngôn quân đội* · *Không có nghi lễ chính thức · Không có ảnh chụp* → `#7`: **LẦN ĐẦU TIÊN TRONG HAI MƯƠI LĂM NĂM PHỤC VỤ** | Tiêu đề ở `#7` |  |  |
| 5-10 | `5.04#8` | H | T4 | `t2_uniform_fire` tối | “Khi đặt dấu chấm cuối câu, dấu chấm ấy nhỏ thôi, nhưng nó mang rất nhiều ý nghĩa.” | Câu trích ở "câu văn" | ⊘ |  |
| 5-11 | `5.04#9` | H | T1 | `t2_checkpoint_dawn` | **CHIẾC SUV BỊ ĐÈ NÁT** · *Hàng trăm món đồ bị đem đốt* | — |  |  |
| 5-12 | `5.05` (nghỉ 2 s) | — | — | giữ 5-11 | — | — |  |  |
| 5-13 | `5.06#1` | H | T1 | `t2_red_flags` | **THÁI ĐỘ TÂM LÝ TRƯỚC BẢN ÁN** · *Câu hỏi dành cho chuyên gia tâm lý* | — |  |  |
| 5-14 | `5.06#2` | H | T1 | `t2_courtroom` | **MỘT LỜI XIN LỖI KHÔ KHỐC** · *Máy móc như một cỗ máy trả bài* | — |  |  |
| 5-15 | `5.06#3` | H | T1 | `t2_cell_medical` | **KINGSTON PENITENTIARY** · *Đặc quyền bị tước sạch · Thành kẻ bị khinh bỉ nhất* | — |  |  |
| 5-16 | `5.06#4` | H | T9 | `t2_red_flags` | *TÂM LÝ HỌC* · **SỰ SỤP ĐỔ CÁI TÔI ÁI KỶ** *(Narcissistic Collapse)* → `#4`: *Chỉ còn lại sự tự thương hại bản thân* | — | →C |  |
| 5-17 | `5.07#1`–`#2` | C | T1 | `void` | **MỘT CHẤN THƯƠNG SÂU SẮC** · *Quân đội Canada phải cải tổ toàn diện quy trình kiểm tra an ninh* | — |  |  |
| 5-18 | `5.07#3` | C | T1 | `t2_red_flags` | **ĐỪNG ĐỂ HIỆU ỨNG HÀO QUANG RU NGỦ TRỰC GIÁC** | — |  |  |
| 5-19 | `5.07#4`–`#6` | C | T1 | `t2_escalation_stairs` | *Địa vị, bằng cấp, quân hàm chỉ là lớp áo khoác xã hội* → `#6`: **TỘI ÁC LUÔN BẮT ĐẦU TỪ NHỮNG BƯỚC RẤT NHỎ** · *Một cái nhìn trộm · Một lần lục lọi đồ riêng tư* | — |  |  |
| 5-20 | `5.07#7` | C | T1 | `t2_stairs_dark`, `push` | **NGƯỠNG THỎA MÃN BỊ ĐẨY XA HƠN** · *Cho đến khi nuốt chửng cả nạn nhân lẫn kẻ thủ ác* | — |  |  |
| 5-21 | `5.08#1` | D | T1 | `t2_folder_tree` | *TÍNH KỶ LUẬT VÀ GHI CHÉP* · **TỰ VIẾT BẢN ÁN CHO CHÍNH MÌNH** | — |  |  |
| 5-22 | `5.08#2` | D | T1 | `void` | **SỰ KIÊU HÃNH CỦA KẺ ÁI KỶ LUÔN ĐỂ LẠI DẤU VẾT** | — |  |  |
| 5-23 | `5.08#3` | D | T1 | `t2_red_flags` | **HÃY LUÔN TIN VÀO TRỰC GIÁC CỦA BẠN** | — |  |  |
| 5-24 | `5.08#4`–`#5` | D | T1 | `t2_head_down` | *Sự bất an mơ hồ · Ranh giới riêng tư bị xâm phạm* → `#5`: **TRỰC GIÁC LÀ HỆ THỐNG CẢNH BÁO SỚM** | — |  |  |
| 5-25 | `5.09` (nghỉ 2 s) | — | — | giữ 5-19 | — | — | ⊘ |  |
| 5-26 | `5.10#1` | H | T1 | `t2_podcast_desk`, đèn ấm dần | *Vực thẳm khôn lường của tâm trí con người* | — |  |  |
| 5-27 | `5.10#2`–`#3` | H | T1 | `t2_podcast_desk` | **BỘ ÓC TINH HOA KHÔNG BẢO VỆ ĐƯỢC AI CẢ** → `#3`: *Chỉ làm cho lần sụp đổ ấy đến muộn hơn, và tàn khốc hơn* | — |  |  |
| 5-28 | `5.10#4` | H | T1 | `t2_podcast_desk` | **NGƯỜI DUY NHẤT GIỮ BÍ MẬT** · *Chính người đàn ông ấy* | — |  |  |
| 5-29 | `5.10#5`–`#6` | H | T8 | `t2_folder_tree` | **CHIẾN LỢI PHẨM CỦA HẮN** → `#5`: *Những tập ảnh được sắp xếp tỉ mỉ* → `#6`: *Những món đồ được cất giấu cẩn thận* | Mỗi câu một mục |  |  |
| 5-30 | `5.10#7` | H | T1 | `t2_escalation_stairs` | **MỘT CUỘC ĐẤU TRÍ KÉO DÀI MƯỜI TIẾNG** · *Chiếc mặt nạ danh dự không thể hàn gắn* | — |  |  |
| 5-31 | `5.10#8` | H | T1 `hero` | `t2_oath_hall` | **BÀI HỌC LỚN NHẤT KHÔNG PHẢI LÀ SỢ HÃI** · *Mà là sự tỉnh thức để nhận diện và bảo vệ ranh giới an toàn* | Tiêu đề ở "tỉnh thức" | ⊘ |  |
| 5-32 | `5.11` (nghỉ 1,5 s) | — | — | giữ 5-24 | — | — |  |  |
| 5-33 | `5.12#1`–`#2` | H | T1 | `t2_podcast_desk` | **CẢM ƠN CÁC KHÁCH MỜI** · *Nhân vật minh hoạ · giọng đọc AI* | 5 ảnh P0 sáng lần lượt | dàn khách mời |  |
| 5-34 | `5.12#3` | H | T1 | `t2_podcast_desk` | **GIỮ MỘT CÁI NHÌN TỈNH TÁO** · *Lắng nghe trực giác · Trân trọng sự bình yên của cuộc sống* | — |  |  |
| 5-35 | `5.12#4` | H | T10 | `t2_podcast_desk` mờ | **HẸN GẶP LẠI Ở TẬP TIẾP THEO** · *Để lại góc nhìn của bạn ở phần bình luận* | — | 🅑 |  |
| 5-36 | `5.13`–`5.14` | — | T2 | `t2_podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | *HỒ SƠ TẬP 02 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật* | Thẻ hồ sơ hiện sau tiếng "Cạch"; mờ ra đen | ⊘ | ◼ |

**Tổng: 161 dòng = 144 shot có lời + 17 dòng không lời.** Phủ 203/203 câu, đúng thứ tự, cột Vai khớp người nói, mọi nền có file, mọi câu trích nguyên văn (kiểm bằng `.work/_qc_tap02_shots.py`, 05/11/2026). Các số `01`–`04`, `02` trên hình là nhãn thứ tự (giống *TẦNG 01*, cờ *01* của Tập 01), không phải dữ kiện.


**Xuất hiện của linh thú (ước tính):**

| Nhân vật | Lượt nói | Bán thân (câu đầu lượt + `🅑`) | Lần được mời (`→`) |
|---|---:|---:|---:|
| Cú · Host | 23 | ~25 | — |
| Sói · Điều tra viên | 6 | ~7 | 4 + 1 (`→C+D`) |
| Cáo · Chuyên gia | 5 | ~10 | 3 + 1 (`→C+D`) |
| Cừu · N1 | 1 | 2 | 1 |
| Mèo · N2 | 1 | 2 | 1 |

## B6. Kiểm tra riêng của Tập 02 (thêm vào A9.2)

| Kiểm tra | Cách | Đạt khi |
|---|---|---|
| Không chữ nhạy cảm trên hình | Tìm trong cột Chữ: "đồ lót", "tình dục", "ái vật", "thi thể", "xác" | Chỉ còn "Hai vụ tấn công tình dục ở Tweed" (4-30, tên tội danh — giữ có chủ đích, như "giết người cấp độ hai" ở Tập 01) |
| Không vẽ nạn nhân | Duyệt mắt mọi khung có tên Lloyd / Comeau | Chỉ có chữ |
| Câu trích tiếng Việt khớp kịch bản | So từng “…” trong cột Chữ với kịch bản | 100% nguyên văn (được lược bằng `…`) |
| Số trên hình | Mọi chữ số trong cột Chữ có trong câu của shot | 0 vi phạm. Đã cố ý viết chữ ("bốn tiếng bốn mươi phút", "Hai mức tù chung thân") ở những chỗ câu đọc bằng chữ |
| Tên riêng đọc đúng | Nghe các câu có Pathfinder, Smyth, Comeau, Genest, Tweed, Belleville, Trenton, ADN | Không đọc sai đến mức khó hiểu; nếu sai, viết phiên âm trong kịch bản (ví dụ "Xmít") và chạy lại câu đó |

---

## PHỤ LỤC A (Tập 02) — CẤU TRÚC KỊCH BẢN (`parse_kichban.py`, 22/10/2026)

Bước 1 phải sinh ra **đúng bảng này**; khác là dừng và báo.

| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |
|---|---|---:|---:|---|
| `1.01` | *BGM* | — | — | Tiếng động cơ phản lực gầm rú vang rền từ xa, sau đó bị kéo tuột xuống thành một nốt Sub-bass trầm đục, nghẹt  |
| `1.02` | *SFX* | — | — | Tiếng lốp xe nghiến chậm rãi trên mặt đường phủ đầy băng tuyết giữa đêm đông lạnh giá. |
| `1.03` | Cú · Host | 4 | 77 | Giọng đọc chậm, trầm, giữ khoảng cách khách quan |
| `1.04` | *Nghỉ 1,5 s* | — | — |  |
| `1.05` | Cú · Host | 3 | 80 | Giọng đọc chậm, trầm, giữ khoảng cách khách quan |
| `1.06` | *SFX* | — | — | Tiếng băng ghi âm bật nhẹ "Tách". |
| `1.07` | **Cừu · N1** | 4 | 91 | Giọng xúc động, chân thật |
| `1.08` | Cú · Host | 3 | 74 | Giọng trầm lắng |
| `1.09` | *Nghỉ 2,0 s* | — | — | Nhạc nền dừng đột ngột |
| `1.10` | Cú · Host | 3 | 51 | Giọng trầm lắng |
| `1.11` | *SFX* | — | — | Tiếng gió rít gào, tiếng bước chân trên tuyết giòn rụm. |
| `1.12` | Cú · Host | 4 | 89 | Giọng trầm lắng |
| `1.13` | *SFX* | — | — | Tiếng gõ cửa kính xe "Cốc... cốc...". |
| `1.14` | Cú · Host | 8 | 121 | Giọng trầm lắng |
| `1.15` | *SFX* | — | — | Tiếng đóng cửa sắt nặng nề vang lên "Rầm". |
| `1.16` | *BGM* | — | — | Đoạn nhạc Cello u ám trỗi dậy, hòa vào tiếng Sub-bass dồn dập. |
| `1.17` | **Sói · Điều tra viên** | 7 | 189 | Giọng sắc lạnh, dứt khoát và chuẩn xác |
| `1.18` | Cú · Host | 3 | 104 | Giọng đọc chậm, trầm, dẫn dắt mạch truyện |
| `2.01` | *BGM* | — | — | Nhạc Minimalist Piano rải những nốt lạnh lẽo, xen lẫn âm thanh gõ bàn phím máy tính chậm rãi trong đêm vắng. |
| `2.02` | Cú · Host | 2 | 69 | Giọng đọc chậm, trầm, dẫn dắt mạch truyện |
| `2.03` | *SFX* | — | — | Tiếng lật mở hồ sơ giấy và tiếng click chuột lách cách. |
| `2.04` | Cú · Host | 5 | 122 | Giọng đọc chậm, trầm, dẫn dắt mạch truyện |
| `2.05` | **Sói · Điều tra viên** | 16 | 282 | Giọng đanh thép, lạnh lùng, nhấn mạnh từng tình tiết chứng cứ |
| `2.06` | *Nghỉ 1,5 s* | — | — |  |
| `2.07` | Cú · Host | 4 | 105 | Giọng trầm tư |
| `2.08` | **Sói · Điều tra viên** | 9 | 188 | Tiếp lời, giọng đều đặn |
| `3.01` | *BGM* | — | — | Tiếng đàn Cello rải những nốt trầm ai oán, hòa cùng tiếng Sub-bass rền rĩ, tạo không gian u tối mang tính chất |
| `3.02` | Cú · Host | 2 | 79 | Giọng đọc chậm, trầm, dẫn dắt mạch truyện |
| `3.03` | *Nghỉ 2,0 s* | — | — |  |
| `3.04` | Cú · Host | 3 | 95 | Giọng đọc chậm, trầm, dẫn dắt mạch truyện |
| `3.05` | **Cáo · Chuyên gia** | 11 | 268 | Giọng học thuật, khúc chiết, phân tích mạch lạc và sâu sắc |
| `3.06` | *Nghỉ 1,5 s* | — | — |  |
| `3.07` | Cú · Host | 3 | 77 | Giọng trăn trở |
| `3.08` | **Cáo · Chuyên gia** | 12 | 271 | Hạ giọng trầm, chậm rãi hơn |
| `3.09` | *Nghỉ 2,0 s* | — | — |  |
| `3.10` | Cú · Host | 1 | 28 | Giọng đọc chậm, trầm, dẫn dắt mạch truyện |
| `3.11` | **Cáo · Chuyên gia** | 11 | 259 | Giọng đều đặn, phân tích sắc bén |
| `4.01` | *BGM* | — | — | Không gian âm thanh chuyển sang tiếng vo ve của đèn huỳnh quang phòng thẩm vấn. Một tiếng Bass drone đơn độc,  |
| `4.02` | *SFX* | — | — | Tiếng kéo ghế kim loại rít trên nền gạch, tiếng đặt cốc cà phê xuống mặt bàn gỗ vang lên một tiếng "Cộp". |
| `4.03` | Cú · Host | 6 | 122 | Hạ giọng trầm, chậm rãi hơn |
| `4.04` | *Nghỉ 2,0 s* | — | — |  |
| `4.05` | Cú · Host | 2 | 33 | Hạ giọng trầm, chậm rãi hơn |
| `4.06` | **Mèo · N2** | 3 | 79 | Giọng băn khoăn, đầy ngạc nhiên |
| `4.07` | Cú · Host | 2 | 38 | Hạ giọng trầm, chậm rãi hơn |
| `4.08` | **Sói · Điều tra viên** | 9 | 185 | Giọng hồi tưởng, đầy thán phục |
| `4.09` | *SFX* | — | — | Tiếng mở tập hồ sơ ảnh, tiếng trượt tấm ảnh trên mặt bàn "Xoẹt". |
| `4.10` | **Sói · Điều tra viên** | 10 | 152 | Giọng hồi tưởng, đầy thán phục |
| `4.11` | **Cáo · Chuyên gia** | 12 | 234 | Giọng học thuật, khúc chiết |
| `4.12` | Cú · Host | 8 | 157 | Giọng trầm lắng, xúc động |
| `5.01` | *BGM* | — | — | Tiếng búa tòa án gõ "Cốp... Cốp... Cốp" vang vọng trong không gian giáo đường tĩnh lặng. Tiếp sau đó là tiếng  |
| `5.02` | Cú · Host | 6 | 128 | Giọng đọc đĩnh đạc, đanh thép nhưng đầy suy tư |
| `5.03` | *Nghỉ 2,0 s* | — | — |  |
| `5.04` | Cú · Host | 9 | 206 | Giọng đọc đĩnh đạc, đanh thép nhưng đầy suy tư |
| `5.05` | *Nghỉ 2,0 s* | — | — |  |
| `5.06` | Cú · Host | 2 | 74 | Giọng đọc đĩnh đạc, đanh thép nhưng đầy suy tư |
| `5.07` | **Cáo · Chuyên gia** | 6 | 143 | Nhấn mạnh từng luận điểm |
| `5.08` | **Sói · Điều tra viên** | 7 | 157 | Tiếp lời dưới góc độ an toàn thực tế |
| `5.09` | *Nghỉ 2,0 s* | — | — | Nhạc nền Piano dâng lên nhẹ nhàng, ấm áp |
| `5.10` | Cú · Host | 11 | 218 | Giọng đọc trầm ấm, truyền cảm, khép lại tập Podcast |
| `5.11` | *Nghỉ 1,5 s* | — | — |  |
| `5.12` | Cú · Host | 4 | 76 | Giọng đọc trầm ấm, truyền cảm, khép lại tập Podcast |
| `5.13` | *SFX* | — | — | Tiếng đóng tập hồ sơ vụ án vang lên tiếng "Cạch" dứt khoát, theo sau là tiếng tắt máy ghi âm. |
| `5.14` | *BGM* | — | — | Nhạc Piano trầm buồn vang lên 5 giây rồi từ từ nhỏ dần và tắt hẳn (Fade out). |
| | **Tổng** | **215** | **4.721** | |

---

## PHỤ LỤC B (Tập 02) — THAY ĐỔI KỊCH BẢN

Khác Tập 01 (chỉ giảm bạo lực), kịch bản Tập 02 được sửa cả về **dữ kiện** sau khi đối chiếu nguồn. Toàn bộ danh sách thay đổi, lý do và link nguồn nằm trong `01_KICH_BAN/Tap02/REVIEW_kichban_tap02.md`.

- **An toàn nội dung (V9, chính sách trẻ em):** bỏ cụm "các cô bé vị thành niên", bỏ chi tiết tự chụp ảnh mặc đồ lót, bỏ chi tiết tự hại trong trại giam.
- **Dữ kiện, sửa theo nguồn:** "Call me Russ" đặt đúng thời điểm; "Got a map?" thay cho "OK"; Comeau 37 tuổi, thuộc Phi đoàn 437; Toàn quyền Canada thu hồi quân hàm; lời ông Genest; bỏ "quốc lộ 37" và "chân dung bị gỡ".
- **Phân tích tâm lý:** không khẳng định chẩn đoán; Dopamine là mô hình giải thích; thống nhất ẩn dụ "hai ngăn kéo".

---

*Lập từ mẫu `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md` ngày 22/10/2026. Chưa sửa file script nào — các thay đổi ở B3 chờ người dùng đồng ý.*
---

## PHỤ LỤC C (Tập 02) — QUYẾT ĐỊNH GIỌNG HIGGS (31/10/2026, người dùng chốt)

| Vai | Giọng mẫu (dataset Kaggle `amber-eyes-voice-ref-voxcpm2`) | Nguồn |
|---|---|---|
| Host | `H.wav` (giữ) | VoxCPM2 bộ gốc |
| Điều tra viên | **`D3_SH.wav`** | `assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02` (seed 7) |
| Chuyên gia | **`C2_AB03.wav`** | `assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03` (seed 77) |
| N1 / N2 | `W6_LOW.wav` / `W5_HIGH.wav` (giữ) | |

- **Bỏ mọi thẻ `<|emotion:…|>`** khi gửi câu vào Higgs (giữ `<|prosody:pause|>`). Cấu hình: `.work/g9_role_map.json` khoá `_emotion_tags: false`, `build_spec.py` đọc khoá này.
- Lý do: bản sản xuất trước D ← `M_HIGH` ra ~193 Hz, cách C 1,03 nc → người nghe nhầm D với C; thẻ `sadness`/`surprise` làm Host vọt 203–228 Hz. Pilot v10: D3_SH cách Host 5,85 nc, cách C 15,1 nc.
- Bản sản xuất cũ sao lưu: `.work/_cu/prod_t02_20261031/` (output Kaggle, audio cài, master, timeline, stems).
- Số đo: `90_LUU_TRU/BaoCao_DoGiongMau_DC_20261030.md`.

### C.1 Lượt sản xuất lần 2 (31/10/2026) — số đo

Kernel `amber-eyes-higgs-prod-t02-kaggle-gpu` v2: 416/416 file, 0 lỗi, 0 thẻ cảm xúc trong văn bản gửi Higgs.

| Đo | Kết quả | Cổng |
|---|---|---|
| F0 câu neutral (AC/YIN) | H 122/128 · D 88/88 · C 207/209 · N1 178 · N2 287–290 Hz | |
| G9 | H-D 5,69 · H-C 8,54 · D-C 14,82 · C-N2 5,66 · H-N1 5,75 nc | ✅ (C-N1 2,56: không liền kề, chấp nhận như trước) |
| Câu cảm xúc | Host `sad` 125 Hz (lần 1: 213 Hz) · D `surprised` 88 Hz | ✅ hết vọt |
| File lệch ≥ 4 nc so với neutral của vai | 4/416 → loại khỏi lựa chọn (`.work/higgs_exclude_f0_t02.json`) | ✅ 0 bản đã chọn bị lệch |
| CER bản đã chọn > 2% (lượt ASR xấu hơn) | 29/203 câu: 8 ASR dao động · ~6 mất chữ đầu · tên riêng (Tweed, Lloyd, Smyth, Genest) · ~7 nghi đọc sai âm đầu ("Vợ"→"Mợ", "Đó"→"nó", "Ban đầu"→"thăng dầu"…) | ⚠ cần vòng 2 (§7) |
| Master `xuat_ban/Tap02_master.mp3` | 1412,0 s · −16,2 LUFS · đỉnh −1,7 dBFS · 0 khoảng câm > 0,3 s @ −60 dB · lời đầu 23,0 s | ✅ |

Bản sản xuất lần 1 + master cũ: `.work/_cu/prod_t02_20261031/`.

### C.2 Vòng 2 §7 (31/10/2026)

29 câu (28 CER > 2% + 5.02#6 có bản tốt duy nhất bị lệch cao độ) × 2 bản = 58 file, kernel `amber-eyes-higgs-prod-t02-r2-kaggle-gpu`, 0 lỗi, không thẻ cảm xúc (`build_spec_r2.py` đọc `_emotion_tags`, thêm `--exclude`). Gộp bằng `.work/merge_r2.py` (manifest trước vòng 2: `higgs_manifest.before_r2.json`).

- Câu CER > 2%: **29 → 12**. 5 câu đọc sai rõ (4.10#3 "Vợ", 4.11#8 "Đó", 2.05#3 "Ban đầu", 5.10#2 "Quân hàm", 5.02#6 "Và đó là") → **0,0%**. 21/203 câu dùng bản vòng 2.
- 12 câu còn lại: tên riêng (Smyth, Genest) · ASR dao động (2.02#2, 4.08#2 có lượt 0%) · mất/sai âm đầu câu (1.07#1 "Trong", 2.05#15 "Cuối", 3.05#4 "Tầng", 4.11#3 "Và", 5.10#10 "Chúng") · 2.05#9 "Thứ hắn lấy đi" → "nhãn lady" (19,6%, giống hệt lỗi G12 của giọng MiniMax `Korean_ColdYoungMan` ⇒ nghi ASR).
- Master: 1411,9 s · −16,2 LUFS · đỉnh −1,7 dBFS · 0 khoảng câm > 0,3 s · lời đầu 23,0 s · 0 bản chọn bị lệch cao độ.

---

## PHỤ LỤC D (Tập 02) — ĐÓNG GÓI LẠI THEO AUDIO HIGGS (31/10/2026)

> Yêu cầu: "dựng lại phụ đề và đóng gói video theo audio mới".
> Kết quả: **không chỉ lệch ~1 s** — video cũ lệch tiếng **142,46 s** và phải dựng lại toàn bộ hình.

### D.1 Phát hiện: video cũ không khớp audio (lỗi có sẵn từ trước, chưa ai phát hiện)

| Đo | Số liệu |
|---|---|
| Audio master hiện tại `xuat_ban/Tap02_master.mp3` (31/10 11:23, vòng 2 §7) | **1411,87 s** |
| `picture.mp4` cũ (dựng 25/10 17:23) | **1554,33 s** → dài hơn audio **142,46 s** |
| Bảng shot cũ `shots_t02.json` (25/10 16:14) | 151 shot, kéo tới 1554,34 s |
| Lệch bảng shot so với timeline mới | shot `1-01` lệch −0,2 s → shot `5-28` lệch **+141,5 s** (lệch dần theo thời gian) |
| Vị trí thẻ kết trong video cũ | **1545,34–1554,34 s** ⇒ ghép `-shortest` sẽ **cắt mất thẻ kết** |
| Khung tại 1410 s của video cũ | vẫn là shot `5-16` — "NHỮNG BƯỚC LẪN RANH GIỚI RẤT NHỎ" (giữa hồi 5), **không** phải thẻ kết |

**Lịch sử thời lượng audio master (đo bằng ffprobe):**

| Mốc | Master | Thời lượng |
|---|---|---|
| 23/10 18:09 | MiniMax, bản `.bak_bgm` | 1605,70 s |
| 31/10 08:37 | Higgs lượt 1 (`.work/_cu/prod_t02_20261031/`) | 1476,27 s |
| 31/10 11:23 | Higgs lượt 2 — bản đang dùng | **1411,87 s** |
| 25/10 17:23 | **video dựng** (từ timeline lúc đó, tổng 1554,34 s) | picture 1554,33 s |

⇒ Hình **chưa bao giờ** được dựng lại sau mỗi lần audio đổi; độ lệch tích luỹ dần.

**Nguyên nhân:** `parse_shots.py` lấy mốc thời gian **chỉ từ `timeline_s.json`** (đo từ audio). Đổi audio ⇒ timeline đổi ⇒ bảng shot và hình phải sinh lại. `mtime` bảng shot vẫn **CŨ HƠN** mp4 nên bẫy A11 #37 không bắt được — phải so **thời lượng** (`picture.mp4` ↔ `timeline.total`), không so mtime.

### D.2 Cách làm (đúng quy trình A3, mọi lệnh có `AE_EP=02`)

| Bước | Lệnh | Kết quả |
|---|---|---|
| 0 | Sao lưu (L5) | `.work/_cu/repack_t02_20261031/` — `shots_t02.json`, `picture.mp4`, `Tap02.srt`, `Tap02_master.mp3`, `thumbnail.png`, `mo_ta.txt`, `nguon_tham_khao.md`, `package.py` |
| 1 | `py -3 .work/parse_shots.py` | 151 shot · **0 khác biệt nội dung** so với bản cũ (chỉ `start`/`end`) ⇒ **ảnh tĩnh không cần duyệt lại** · tổng 1411,87 s · 0 nền thiếu file |
| 2 | `py -3 .work/build_video3.py --workers 6` | **37 phút 41 s** (30 fps tổng ≈ 5 fps/worker) → `picture.mp4` **1411,87 s** · 475,2 MB |
| 3 | `py -3 .work/subtitles.py` | **380 cue** (không đổi số cue, lệch −142,47 s) |
| 4 | `py -3 .work/package.py --mux` | `Tap02_master.mp4` **510,6 MB** + thumbnail + `mo_ta.txt` + `nguon_tham_khao.md` |

### D.3 Số đo thành phẩm (đo trên CHÍNH file mp4 cuối — A11 #38)

| Đo | Kết quả | Cổng |
|---|---|---|
| Thời lượng mp4 | **1411,867 s** (khớp `timeline.total` 1411,87 s) | ±0,05 s ✅ |
| Video / tiếng | 1411,867 s / 1411,861 s · h264 1920×1080 @30 · AAC 48 kHz 2ch · 2,89 Mbps | ✅ |
| Giải mã toàn tệp | **0 dòng lỗi** | ✅ |
| Loudness (ebur128 trên mp4) | **−16,0 LUFS** | −16 ± 1 ✅ |
| Đỉnh true peak (trên mp4) | lần ghép đầu **−1,4 dBTP** → sau vá **−1,9 dBTP** | ≤ −1,5 ✅ |
| Câu thoại nằm trọn trong shot của nó | **203/203 câu** | ✅ |
| Shot liền kề (không hở) | 0 chỗ hở | ✅ |
| Phụ đề | 380 cue · 0 cue > 6 s · 0 overlap · cue cuối 1402,87 s | ✅ |
| Phụ đề vs kịch bản (G6) | **203/203 câu khớp nguyên văn**; phụ đề (bỏ tag vai) == lời đọc | ✅ |
| Thẻ kết | shot `5-29` ở 1402,87–1411,87 s; khung trích từ mp4 có đủ "HỒ SƠ TẬP 02 · ĐÃ ĐÓNG / AMBER EYES / Phân tích tâm lý tội phạm / qua những hồ sơ có thật" | ✅ |
| Mốc chương trong mô tả | 00:00 · 00:20 Hồi 1 · 05:03 Hồi 2 · 08:39 Hồi 3 · 13:32 Hồi 4 · 18:32 Hồi 5 | ✅ |

### D.4 Vá `package.py` — giới hạn đỉnh trước khi mã hoá AAC

Lần ghép đầu: WAV đã ở đúng trần (sample peak −1,5 dBFS) nhưng **AAC dựng lại true peak thành −1,4 dBTP** → vượt trần của dự án (A11 #38). Vá trong `mux()`:

```
-af "alimiter=limit=0.7943:attack=5:release=50:level=disabled"
```

`limit` = sample peak −2 dBFS; `level=disabled` để không đổi loudness tổng. Đo lại trên mp4: **đỉnh −1,9 dBTP · −16,0 LUFS**. Vá áp dụng cho **mọi tập** (không riêng Tập 02) và không đụng danh sách câu / mốc thời gian / bảng shot ⇒ không cần hồi quy Tập 01. Bản gốc: `.work/_cu/repack_t02_20261031/package.py.bak`.

### D.5 Bài học đã ghi vào tài liệu

- Tiêu chuẩn A11 **#55**: đổi audio ⇒ phải chạy lại `parse_shots.py` + dựng lại hình. Cổng trước khi đóng gói: so thời lượng `picture.mp4` với `timeline.total` (±0,05 s) + trích khung `timeline.total − 2 s` xem thẻ kết có thật không.
- `AGENTS.md` mục 2 (bước 9–10) + mục 6 **H14**.

### D.6 Việc còn lại của người dùng

- Bổ sung nguồn công khai vào `xuat_ban/nguon_tham_khao.md` (34 dòng còn trống link) trước khi đăng.
- Nghe duyệt lại tập 02 bản tiếng Việt (giọng Higgs mới, hình dựng lại).
- Bản EN / JA của Tập 02 dùng audio riêng (25/10, không đổi) ⇒ không bị ảnh hưởng.

---

## PHỤ LỤC E (Tập 02) — RÀ MÔ TẢ (`mo_ta.txt`) VỚI VIDEO THẬT (02/11/2026)

**Cách làm:** trích frame từ CHÍNH `xuat_ban/Tap02_master.mp4` (1920×1080 @30 · 1411,867 s) bằng OpenCV, dò độ sáng để tìm thẻ hồi, đọc chữ trên thẻ, đối chiếu từng dòng của `mo_ta.txt`. Không tin bảng shot trong hồ sơ — đo lại từ file xuất.

### E.1 Số đo trên chính file mp4

| Mốc trong `mo_ta.txt` | Thực tế trong mp4 (đo) | Kết luận |
|---|---|---|
| 00:00 Intro | intro 0 → 22,41 s; thẻ "LƯU Ý TRƯỚC KHI XEM" ~19–21 s | ✅ |
| 00:20 Hồi 1 | thẻ **HỒI 01** hiện **22,0 s**; lời đầu 23,0 s | ⚠ lệch 2 s → đổi 00:22 |
| 05:03 Hồi 2 | thẻ ở **303,2 s** (timeline ACT 2 = 303,640 s) | ✅ |
| 08:39 Hồi 3 | thẻ ở **519,5 s** (timeline ACT 3 = 519,590 s) | ✅ |
| 13:32 Hồi 4 | thẻ ở **~812–813 s** (timeline ACT 4 = 812,090 s) | ✅ |
| 18:32 Hồi 5 | thẻ ở **1112,5 s** (timeline ACT 5 = 1112,640 s) | ✅ |

Ngoài ra: câu *"không tồn tại một chẩn đoán lâm sàng công khai nào về Russell Williams"* có thật trong video (lúc 09:11) · thẻ kết ở 1402,9–1411,9 s có đủ "HỒ SƠ TẬP 02 · ĐÃ ĐÓNG / AMBER EYES / Phân tích tâm lý tội phạm qua những hồ sơ có thật" · thumbnail đúng tập.

### E.2 Ba lệch đã sửa (lượt 02/11/2026)

| # | Lệch | Sửa ở đâu |
|---|---|---|
| 1 | Tên Hồi 1 thiếu "cực đại" (thẻ ghi "SỰ TƯƠNG PHẢN **CỰC ĐẠI** PHÍA SAU QUÂN HÀM ĐẠI TÁ") | `.work/edition.py` → `EPISODES["02"]["act_titles"][1]` |
| 2 | Mốc Hồi 1 lệch 2 s | `.work/package.py` → `starts = {1: TL.get("intro", 20.5)}` (mọi timeline VN đều `intro = 22,41` s) |
| 3 | Disclaimer ghi vai "Người dân", nhưng phụ đề tập 02 dùng nhãn **[BINH SĨ]** (cue 14) và **[KHÁN GIẢ]** (cue 237) — không có "Người dân" | `.work/edition.py` → khoá mới `EPISODES["02"]["roles_line"]`; `.work/package.py` đọc khoá này, **mặc định giữ nguyên** câu cũ cho tập khác |

### E.3 Vì sao sửa ở generator chứ không sửa tay `mo_ta.txt`

`mo_ta.txt` do `package.py description()` **sinh ra** mỗi lần chạy ⇒ sửa tay file thành phẩm sẽ bị ghi đè. Đã sửa đúng 3 tầng: `edition.py` (cấu hình tập) → `package.py` (template) → sinh lại bằng `AE_EP=02 python .work/package.py` (**không** `--mux` ⇒ không ghép lại video).

**Kết quả:** `mo_ta.txt` diff đúng **3 dòng**, `nguon_tham_khao.md` **không đổi** (sha256 giống nhau), `thumbnail.png` **không đổi** (sha256 giống nhau).

### E.4 Kiểm hồi quy Tập 01 (L9)

Sinh thử trong bộ nhớ (chặn `Path.write_text` ⇒ **không** đụng file Tập 01) rồi diff với file trên đĩa:

- **Tập 01:** đúng **1 dòng đổi** — `00:20 Hồi 1` → `00:22 Hồi 1`. Tên 5 hồi, câu disclaimer và phần còn lại giữ nguyên. `nguon_tham_khao.md` Tập 01 **giống hệt** file sinh ra ⇒ không mất link nào.
- **Tập 02:** **0 dòng đổi** ⇒ file trên đĩa = đúng output của pipeline (chạy lại `package.py` không làm lệch thêm).

Cơ sở của việc đổi Tập 01: `timeline_s.json` (T01) cũng có `intro = 22,41 s`, hồ sơ Tập 01 mục "INTRO KÊNH · 0,00–22,41 s" và shot 1-00 (thẻ HỒI 01) chồng lên phần đen cuối intro — **cùng thiết kế** với Tập 02.

### E.5 Bài học đã ghi

- Tiêu chuẩn A11 **#70** (file mô tả là file sinh — sửa generator + config, không sửa tay) và **#71** (mốc chương phải đo từ mp4; `starts` hardcode 20,5 s lệch 2 s).
- `AGENTS.md` mục 8 **T10** (file mô tả là file sinh) và **T11** (mốc chương phải đo, không đoán).

### E.6 Việc còn lại của người dùng

- **34 dòng nguồn trong `nguon_tham_khao.md` vẫn trống link** ⇒ chặn đăng (bản EN cũng 0/37).
- Dòng tổng đài **111 (bảo vệ trẻ em)** không liên quan nội dung tập này (cả hai nạn nhân đều là người lớn: Jessica Lloyd 27 tuổi, Marie-France Comeau 37 tuổi). Bản EN dùng đường dây nóng tấn công tình dục + nạn nhân Canada. **Cần người dùng chốt** số điện thoại — AI không tự bịa.
- Bản EN (`Tap02_EN/xuat_ban/mo_ta.txt`) vẫn dùng mốc `00:20 Act 1` và `package.py` vẫn hardcode `20.5` ở nhánh EN/JA/KO ⇒ cùng lệch 2 s, **chưa sửa** (ngoài phạm vi lượt này).

---

## PHỤ LỤC F (Tập 02) — HASHTAG CHO MÔ TẢ TIẾNG VIỆT (02/11/2026)

**Quyết định của người dùng (02/11/2026):** hashtag = **bộ tag EN của tập + 3 tag tiếng Việt không dấu** `#TamLyToiPham #PhamVan #HoiTo`; áp dụng cho **toàn bộ tập tiếng Việt** (01, 03–07 cùng Tập 02).

### F.1 Vì sao phải sửa ở generator

`mo_ta.txt` do `package.py description()` sinh ra ⇒ sửa tay sẽ mất. Đã vá 2 tầng:

- `.work/edition.py`: thêm khoá `"hashtags"` vào `EPISODES["01".."07"]` (mỗi tập một bộ tag riêng).
- `.work/package.py` (nhánh VN): `hashtags = ED.EP.get("hashtags", "")` → `tag_line = ("\n\n" + hashtags) if hashtags else ""`, chèn ở cuối mô tả (sau dòng tổng đài 111). **Bản EN/JA/KO không đọc khoá này** — EN lấy tag từ `CHU_CO_DINH_EN.md`.

### F.2 Bộ tag đã đặt

| Tập | Tag EN (nguồn) | Tag bản VN |
|---|---|---|
| 01 Blanchard | tự đặt theo vụ án (EN chưa có dòng tag) | + `#TamLyToiPham #PhamVan #HoiTo` |
| 02 Williams | `CHU_CO_DINH_EN.md` | + 3 tag VN |
| 03 Kemper | `CHU_CO_DINH_EN.md` | + 3 tag VN |
| 04 Cullen | `CHU_CO_DINH_EN.md` | + 3 tag VN |
| 05 BTK | `CHU_CO_DINH_EN.md` | + 3 tag VN |
| 06 Gacy | tự đặt theo vụ án (chưa có bản EN) | + 3 tag VN |
| 07 Carter–Roy | tự đặt theo vụ án (chưa có bản EN) | + 3 tag VN |

### F.3 Cách sinh lại (không đụng thumbnail)

Gọi `description()` **trực tiếp** cho từng tập — **không** chạy CLI `package.py` vì CLI còn gọi `thumbnail()` ⇒ sẽ **ghi đè thumbnail đã xuất** của các tập cũ (Tập 01, 03–07 có thumbnail từ 22/10–01/11).

**Đo sau khi sinh:** `thumbnail.png` của cả 7 tập **không đổi** (sha256 giống bản trên đĩa) · `nguon_tham_khao.md` 6/7 tập không đổi · **Tập 03 đổi 6 dòng** vì file nguồn cũ sinh trước khi kịch bản viết lại (trích dẫn trong bảng lấy từ câu hiện tại) ⇒ **không mất link nào**, chỉ cập nhật đoạn trích. `mo_ta.txt` mỗi tập **+1 dòng hashtag**; Tập 03 thêm dòng `voice_credit` (Higgs) vì file cũ sinh trước khi có khoá này; Tập 04/05 mất 1 dòng trống thừa do template credit cũ.

### F.4 Ghi chú

- Tập 08–29 trong `EPISODES` **chưa có mô tả** ⇒ chưa đặt tag; khi dựng tập mới, khai `"hashtags"` theo cùng khuôn (tag EN/vụ án + 3 tag VN).
- `#PhamVan` hơi "lệch" với Tập 01 (Münchausen — không có phần thẩm vấn) nhưng giữ **đồng nhất 3 tag VN cho mọi tập** theo quyết định của người dùng.
