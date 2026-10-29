# HỒ SƠ SẢN XUẤT TẬP 02 · "ĐẠI TÁ HAI MẶT" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A) — các mã A0…A13 trong file này trỏ về đó.
**Kịch bản:** `01_KICH_BAN/Tap02/kichban_tap02_22102026.md` · **Thành phẩm:** `02_SAN_XUAT/Tap02/xuat_ban/`
**Mẫu gốc:** `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md`. Lập ngày 22/10/2026, **chưa chạy** — mọi số đo thời gian ở đây là ước tính, sẽ thay bằng số đo thật sau bước 3.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap02/kichban_tap02_22102026.md` — đã sửa theo đánh giá và đối chiếu nguồn (`REVIEW_kichban_tap02.md`, lần 1 + lần 2). Bản trước khi sửa: `_truoc_review.md` |
| Lượt nói / câu / từ | 36 / **215** / 4.721 — Host 48% · Chuyên gia 25% · Điều tra viên 23% · Người bình thường 4% |
| **Giọng (bộ A)** | Host `English_CaptivatingStoryteller` (trầm ấm) · Điều tra viên `Korean_ColdYoungMan` (lạnh lùng) · Chuyên gia `English_AssertiveQueen` (nhấn mạnh, nữ) · N1 `Vietnamese_kindhearted_girl` · N2 `English_captivating_female1`. Cao độ luôn 0, chỉ 4 cảm xúc an toàn (A4.2 G5, G8) |
| N1 / N2 | `1.07` Người từng phục vụ dưới quyền (Cừu) / `4.06` Người theo dõi vụ án (Mèo) |
| Thời lượng | **26:45** (1.605,7 s) — bản giọng bộ A + số đọc bằng chữ (ước tính ban đầu 25–26 phút) |
| Mốc hồi (đo) | Hồi 1 · 00:20 · Hồi 2 · 05:25 · Hồi 3 · 09:32 · Hồi 4 · 15:18 · Hồi 5 · 20:58 |
| Bảng shot | **151 dòng** = 134 shot có lời + 17 dòng không lời (mục 6) |
| Nền dùng | 36/37 nền `t2_*` (chỉ bỏ `t2_cell_medical`) + 9 nền Tập 01. `t2_two_chairs`, `t2_hidden_drive`, `t2_tape_recorder` đã **tạo lại 23/10** (dịch vụ ảnh chạy lại) và dùng lại theo bảng shot gốc |
| Phân loại YouTube | Giáo dục · Không dành cho trẻ em · "Nội dung bị thay đổi hoặc tổng hợp" · tự đánh giá quảng cáo: chủ đề gây tranh cãi, có nhắc tội phạm tình dục ở mức khái quát (A10) |

## B2. Trạng thái và việc phải làm

| Hạng mục | Trạng thái |
|---|---|
| Kịch bản | ✅ Đã sửa, đã đối chiếu nguồn, parse đạt (215 câu, không còn từ cấm A9.2) |
| Ảnh nền | ✅ 37 nền `t2_*`; 3 nền tạo lại 23/10 (`t2_two_chairs`, `t2_hidden_drive`, `t2_tape_recorder`); duyệt ảnh tĩnh đủ 151 shot. **QC lại 23/10: 37/37 đạt** (đủ 2112×1188, không viền, không ảnh thừa) — `py -3 .work/qc_bg.py t2 --sheet` |
| Cấu hình script | ✅ Đã làm 22/10 — mục B3 nằm trong `EPISODES["02"]` của `.work/edition.py`; chạy mọi lệnh với `AE_EP=02`. Tập 01 kiểm hồi quy đạt |
| TTS, âm thanh, hình, đóng gói | ✅ **Bản 4 — dựng lại 23/10/2026, 18:09–19:43** (giọng bộ A + số đọc bằng chữ) · 215/215 câu · G10 đạt (mỗi vai 1 người, 3 vai tách bạch 10/10) · âm thanh 1.605,7 s, −15,9 LUFS, đỉnh −1,5 dBFS, 0 khoảng câm · 14 đoạn nền + 37 tiếng động · hình dựng lại 6 worker 92 phút → `picture.mp4` 1.605,70 s · **`Tap02_master.mp4` 552,8 MB — 1.605,70 s, 1920×1080@30, 48.171 khung, H.264 + AAC 192 kbps stereo, lệch hình/tiếng 0,002 s**. Lịch sử: bản 1 (11:14, giọng cũ — Host đổi danh tính) → bản 2 (15:07, bộ A — đọc "1.400" thành "một phẩy bốn trăm") → bản 3 (18:08, audio) → **bản 4 (19:43, video + đóng gói)**. *Bản 3 dựng lúc 15:05 bị lệch 1,77 s với audio bản 3 → đã dựng lại toàn bộ.* |
| Nguồn | ⚠ `xuat_ban/nguon_tham_khao.md` đã sinh (35 câu) — **người dùng điền link**; gợi ý ở mục "LẦN 2" của `01_KICH_BAN/Tap02/REVIEW_kichban_tap02.md` |
| **Sổ nguồn gốc** | ✅ `provenance.json` **587 dòng** — bổ sung 23/10: **9 file nhạc nền `assets/bgm/`** (trước đó thiếu hẳn — A10 dựa vào sổ này để kháng nghị khi bị Content ID nhận nhầm), 15 linh thú (`P0`/`full`/mascot), 41 ảnh gốc `_raw/t2_*`, 37 SFX tự tổng hợp, 15 ảnh người dùng cung cấp, 5 file nhận diện kênh. **92/92 tài sản Tập 02 đã có dòng.** Sao cũ: `.work/provenance.backup_23102026.json` |
| **Trước khi đăng** | ① Điền nguồn · ② Kiểm tra điều khoản thương mại (`provenance.json` — xem cột `kiem_tra_thuong_mai`; **9 file nhạc nền MiniMax còn "chưa"**, phải kiểm tra điều khoản MiniMax trước khi bật kiếm tiền; **ảnh linh thú + ảnh người dùng cung cấp còn "chưa"** — cần người dùng xác nhận công cụ đã dùng) · ③ Người dùng nghe toàn tập |
| **Thành phẩm** | `xuat_ban/` — `Tap02_master.mp4` (552,8 MB) · `Tap02_master.mp3` (38,5 MB) · `Tap02.srt` (391 cue, có tên vai) · `thumbnail.png` (1280×720) · `mo_ta.txt` (có mốc chương 00:20 / 05:25 / 09:32 / 15:18 / 20:58) · `nguon_tham_khao.md` (35 câu) |

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
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t2_base_trenton` | **07 · 2009** · *Căn cứ Không quân Trenton — căn cứ không quân lớn nhất của quân đội Canada* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T1 | `t2_oath_hall` | **LỄ NHẬM CHỨC** · *Trước các quan chức cấp cao trong quân đội* | — | | |
| 1-03 | `1.03#4` | H | T2 | `t2_oath_hall`, `still` | *NHẬN QUYỀN CHỈ HUY TỐI CAO* · **ĐẠI TÁ DAVID RUSSELL WILLIAMS** · *Một bản lý lịch hoàn hảo* | Dấu mộc ở "hoàn hảo" | | |
| 1-04 | `1.04` (nghỉ 1,5 s) | — | — | giữ 1-03 | — | — | | |
| 1-05 | `1.05#1` | H | T5 | `t2_base_trenton` | **46 TUỔI** · *Lái chuyên cơ đưa đón Nữ hoàng Anh Elizabeth II và Thủ tướng Canada* | Số đếm | | |
| 1-06 | `1.05#2` | H | T8 | `t2_base_trenton` mờ | *Biểu tượng của kỷ luật thép · Một người chồng gương mẫu · Vợ: lãnh đạo tại Quỹ Tim mạch và Đột quỵ Canada* | Mỗi mục ở cụm từ | | |
| 1-07 | `1.05#3` | H | T1 | `t2_base_trenton`, `pull` | *HÃY HÌNH DUNG:* **NHỮNG NGƯỜI TỪNG PHỤC VỤ DƯỚI QUYỀN ÔNG** | — | →N1 | |
| 1-08 | `1.07#1` | N1 | T4 lời kể | `t2_base_trenton` ấm, mờ | “…hình mẫu lý tưởng về sự hoàn hảo.” | — | ✦ Cừu | |
| 1-09 | `1.07#2`–`#3` | N1 | T8 | `t2_oath_hall` mờ | *Điềm tĩnh · Chuẩn mực đến từng nếp gấp quân phục · Không bao giờ to tiếng* → `#3`: *Uy quyền toát ra từ trí tuệ và sự chuẩn xác* | Mỗi mục ở cụm từ | | |
| 1-10 | `1.07#4` | N1 | T4 lời kể | `t2_base_trenton` ấm | “Chúng tôi sẵn sàng theo ông ấy đến bất cứ đâu mà không một chút hoài nghi.” | — | 🅑 | |
| 1-11 | `1.08#1` | H | T1 | `t2_town_snow`, `pan` | **NHỮNG ĐÊM KHUYA THANH VẮNG** · *Biến mất vào bóng tối của những thị trấn ngoại ô* | Tiêu đề ở "đêm khuya" | | |
| 1-12 | `1.08#2`–`#3` | H | T1 | `night_street`, `still` | *Không còn một vị đại tá oai phong* → `#3`: **CHỈ CÒN MỘT KẺ RÌNH RẬP** | Tiêu đề ở "kẻ rình rập" | ⊘ | |
| 1-13 | `1.09` (nghỉ 2 s) | — | — | giữ 1-12, nhạc tắt, chỉ còn nền trầm | — | — | ⊘ | |
| 1-14 | `1.10#1` | H | T5 ngày | `t2_house_missing` | **28 · 01 · 2010** | Gõ từng ký tự | | ✂ |
| 1-15 | `1.10#2`–`#3` | H | T2 | `t2_house_missing_dawn` | *JESSICA LLOYD · 27 TUỔI · BELLEVILLE* · **BIẾN MẤT KHỎI NHÀ RIÊNG** → `#3`: *Cảnh sát tỉnh Ontario mở hồ sơ điều tra · Một cuộc tìm kiếm quy mô lớn* | Dấu mộc ở "mở hồ sơ" | | |
| 1-16 | `1.12#1` | H | T1 | `t2_town_snow` | **KHÔNG TÌM RA MANH MỐI NÀO** | Gió, bước chân (SFX `1.11`) ở đầu | | |
| 1-17 | `1.12#2` | H | T7 | `t2_checkpoint` | **TỐI 4 THÁNG 2** · *Trạm kiểm soát lưu động · Gần nhà nạn nhân · Suốt đêm* | 2 ghim không nhãn, đường tự vẽ | | |
| 1-18 | `1.12#3`–`#4` | H | T1 | `t2_tire_track`, `still` | *Không phải kiểm tra giấy tờ* → `#4`: **MỘT VỆT VÂN LỐP XE ĐỘC ĐÁO** | Tiêu đề ở "vân lốp" | | |
| 1-19 | `1.14#1`–`#2` | H | T3 so sánh | `t2_suv_stop` | **NISSAN PATHFINDER** → `#2`: *Thay vì chiếc BMW mà ông ta vẫn thường đi* | Gõ kính (SFX `1.13`) ở đầu | | |
| 1-20 | `1.14#3` | H | T1 `hero` | `t2_suv_stop` | **CHỈ HUY TRƯỞNG CĂN CỨ KHÔNG QUÂN TRENTON** | Tiêu đề ở "chính là" | ⊘ | |
| 1-21 | `1.14#4`–`#5` | H | T1 | `t2_tire_track` | **RẤT GIỐNG DẤU VẾT TRÊN TUYẾT** → `#5`: *Nhưng chưa đủ để giữ một người như ông ta lại* | — | | |
| 1-22 | `1.14#6`–`#7` | H | T1 | `t2_checkpoint_dawn` | *Được cho đi với lời chào lịch sự* → `#7`: **BA NGÀY TIẾP THEO** · *Vẫn là một vị đại tá tự do* | — | | |
| 1-23 | `1.14#8` | H | T1 | `t2_interrogation_empty`, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN TÁI HIỆN BA NGÀY ĐÓ** | Cửa sắt "Rầm" (SFX `1.15`) sau câu | →D | |
| 1-24 | `1.17#1` | D | T2 | `t2_tire_track` | *GẦN NHÀ NẠN NHÂN* · **VỆT GAI LỐP XE ĐỊA HÌNH KHÁ HIẾM GẶP** · *Một dấu giày đi tuyết cỡ lớn* | Dấu mộc ở "dấu giày" | ✦ Sói | |
| 1-25 | `1.17#2`–`#3` | D | T1 | `t2_suv_stop` | *Một cuộc dừng xe thủ tục* → `#3`: **HOA VĂN LỐP RẤT GIỐNG DẤU VẾT TẠI HIỆN TRƯỜNG** | Vệt sáng đèn pin ở "rọi đèn pin" | | |
| 1-26 | `1.17#4` | D | T3 so sánh | `t2_checkpoint` | *Thế giới của Đại tá Russell Williams* · **CHẠM VÀO** · *Thế giới của cảnh sát* | Cột phải ở "thế giới của cảnh sát" | | |
| 1-27 | `1.17#5`–`#6` | D | T6 | `pinboard` | *Ba ngày · Lặng lẽ đối chiếu dấu vết* → `#6`: **LỆNH KHÁM XÉT** · *Ottawa · Tweed* | Mỗi câu một mốc | | |
| 1-28 | `1.17#7` | D | T1 | `t2_phone_call` | *Thay vì lệnh triệu tập* · **MỘT LỜI MỜI BẰNG ĐIỆN THOẠI** | Tiêu đề ở "lời mời" | | |
| 1-29 | `1.18#1` | H | T1 | `t2_podcast_desk`, cassette quay | **HỒ SƠ PHÂN TÍCH TÂM LÝ HỌC TỘI PHẠM** | — | 🅑 | |
| 1-30 | `1.18#2` | H | T2 | `records` | *HỒ SƠ* · **ĐẠI TÁ RUSSELL WILLIAMS** | Dấu mộc ở "Hồ sơ Đại tá" | | |
| 1-31 | `1.18#3` | H | T9 → T10 | `t2_two_masks` | **QUY LUẬT LEO THANG HÀNH VI** · **SỰ PHÂN MẢNH TÂM TRÍ** → *TẬP 02 · ĐẠI TÁ HAI MẶT* | Mỗi thuật ngữ ở cụm từ; tên tập cuối câu | | |
| 1-32 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **4 BẬC THANG CỦA VỰC THẲM** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ TỘI ÁC · nền chủ đạo `t2_folder_tree`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` | H | T1 | `t2_cottage_search` | **KHÁM XÉT** · *Ottawa · Tweed* | — | | |
| 2-02 | `2.02#2` | H | T1 | `t2_cottage_search`, `push` | **VƯỢT QUA MỌI TRÍ TƯỞNG TƯỢNG** | — | | |
| 2-03 | `2.04#1` | H | T1 | `t2_hidden_drive` | **Ổ CỨNG GIẤU TRONG TRẦN TẦNG HẦM** | Lật hồ sơ (SFX `2.03`) ở đầu | | |
| 2-04 | `2.04#2` | H | T8 | `t2_folder_tree`, `pan` | *Hàng nghìn bức ảnh và video · Đóng dấu ngày giờ · Hệ thống thư mục phức tạp · Ghi chép về từng lần phạm tội* | Mỗi mục ở cụm từ | | |
| 2-05 | `2.04#3`–`#4` | H | T1 | `t2_escalation_stairs` | **KHÔNG PHẢI MỘT KẺ BỘC PHÁT TRONG MỘT ĐÊM** → `#4`: *Đỉnh chóp của một tảng băng chìm* · **4 NẤC THANG LEO THANG HÀNH VI** | — | | |
| 2-06 | `2.04#5` | H | T1 | `pinboard` mờ, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN PHÂN TÍCH PHƯƠNG THỨC HOẠT ĐỘNG** | — | →D | |
| 2-07 | `2.05#1` | D | T2 | `pinboard` | **4 GIAI ĐOẠN LEO THANG** · *Dữ liệu số và chứng cứ thu giữ* | Bộ đếm `0/4`, 4 thẻ trống ghim lên | | |
| 2-08 | `2.05#2`–`#3` | D | T3 `1/4` | `t2_open_window` | *NẤC 01* · **NHÌN TRỘM** → `#3`: *Lảng vảng ban đêm trong các khu dân cư vắng* | — | | |
| 2-09 | `2.05#4`–`#6` | D | T3 `2/4` | `t2_drawer_dark` | *NẤC 02* · **ĐỘT NHẬP LẤY ĐỒ RIÊNG TƯ** → `#6`: *Những vụ trộm đầu tiên cảnh sát lần ra: 2006* | — | | |
| 2-10 | `2.05#7` | D | T5 | `t2_open_window` mờ | *09 · 2007 – 11 · 2009* · **82** · *Vụ đột nhập và đột nhập bất thành* | Số đếm 0 → 82 | | |
| 2-11 | `2.05#8`–`#9` | D | T8 gạch bỏ | `records` | *Tiền bạc · Trang sức* → `#9`: **ĐỒ RIÊNG TƯ CỦA PHỤ NỮ** | Gạch ở "không lấy" | | |
| 2-12 | `2.05#10` | D | T8 | `t2_logbook` | *NGHI THỨC LẶP LẠI Y HỆT* · *Chụp ảnh · Lấy đồ · Ghi chép lại* | Mỗi mục ở cụm từ | | |
| 2-13 | `2.05#11`–`#13` | D | T3 `3/4` | `t2_escalation_stairs` | *NẤC 03* · **XÂM NHẬP KHI CÓ NGƯỜI Ở NHÀ** → `#12`: *09 · 2009 · Ngưỡng kích thích tiếp tục bị lờn* → `#13`: *Hai người phụ nữ · Quanh thị trấn Tweed* | — | ⊘ ở `#13` | |
| 2-14 | `2.05#14`–`#16` | D | T3 `4/4` | `fog`, tối dần | *NẤC 04* · **CÁI CHẾT** → `#15`: *Cuối tháng 11 · 2009 · Marie-France Comeau · Hạ sĩ · 37 tuổi · Phi đoàn 437* → `#16`: *Hai tháng sau · Jessica Lloyd* | Chỉ chữ, không hình người | ⊘ | |
| 2-15 | `2.06` (nghỉ 1,5 s) | — | — | giữ 2-14, tối dần | — | — | ⊘ | |
| 2-16 | `2.07#1`–`#2` | H | T3 so sánh | `t2_two_masks` | *Bản năng săn mồi lệch lạc* → `#2`: *Tính kỷ luật, tỉ mỉ của một sĩ quan* · **NHƯ MỘT BẢN BÁO CÁO QUÂN SỰ** | Cột phải ở `#2` | | ✂ |
| 2-17 | `2.07#3` | H | T9 | `t2_logbook` | **CHỮ KÝ TÂM LÝ** *(Signature)* · *Thứ không thể từ bỏ* | — | | |
| 2-18 | `2.07#4` | H | T1 | `pinboard`, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN LÀM RÕ** | — | →D | |
| 2-19 | `2.08#1`–`#2` | D | T9 | `records` | *Kẻ phạm tội thông thường: xóa dấu vết* → `#2`: **CHIẾN LỢI PHẨM** *(Trophies)* · *Thứ hắn cần, chứ không chỉ là thứ hắn muốn* | Thuật ngữ ở `#2` | | |
| 2-20 | `2.08#3`–`#4` | D | T1 | `t2_drawer_dark` | **SỐNG LẠI CẢM GIÁC KIỂM SOÁT** | Tiêu đề ở "sống lại" | 🅑 | |
| 2-21 | `2.08#5`–`#6` | D | T3 so sánh | `t2_boot_evidence` | **VÂN LỐP VÀ DẤU GIÀY** · *Dẫn cảnh sát tới cửa nhà* → `#6`: **MỘT KHO BẰNG CHỨNG** | Cột phải ở `#6` | | |
| 2-22 | `2.08#7` | D | T5 | `t2_folder_tree` | **82** · *Vụ đột nhập* → *Khoảng 1.400 món đồ bị lấy đi* | Số đếm; dòng phụ ở "1.400" | | |
| 2-23 | `2.08#8`–`#9` | D | T1 | `t2_house_missing_dawn` | *THỊ TRẤN TWEED* · **KHÔNG MỘT VỤ NÀO TỪNG ĐƯỢC TRÌNH BÁO** → `#9`: *Cho đến khi cảnh sát gõ cửa* | — | | |
| 2-24 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **BÊN TRONG BỘ NÃO CỦA SÁT NHÂN HAI MẶT** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI PHẪU TÂM LÝ · nền chủ đạo `t2_brain_neural`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T1 | `t2_command_chair` | **MỘT CÂU HỎI HÓC BÚA ĐẾN RỢN NGƯỜI** | — | | |
| 3-02 | `3.02#2` | H | T8 | `t2_command_chair` tối | *Địa vị · Danh vọng · Một người vợ tài năng · Sự kính trọng của cả một quốc gia* → **TẠI SAO ĐÁNH CƯỢC TẤT CẢ?** | Mỗi mục ở cụm từ; tiêu đề ở "đánh cược" | | |
| 3-03 | `3.03` (nghỉ 2 s) | — | — | giữ 3-02 | — | — | | |
| 3-04 | `3.04#1` | H | T2 | `records` | *TRƯỚC KHI PHÂN TÍCH* · **KHÔNG TỒN TẠI MỘT CHẨN ĐOÁN LÂM SÀNG CÔNG KHAI NÀO** · *Về Russell Williams* | — | 🅑 | |
| 3-05 | `3.04#2` | H | T1 | `t2_brain_neural` mờ | **GIÚP TA ĐẶT CÂU HỎI ĐÚNG** · *Không phải một sự phán xét đã được cơ quan chuyên môn xác nhận* | — | | |
| 3-06 | `3.04#3` | H | T1 | `t2_brain_neural`, `push` | *LẮNG NGHE:* **CHUYÊN GIA TÂM LÝ** → *3 tầng cơ chế* | — | →C | |
| 3-07 | `3.05#1`–`#3` | C | T9 | `t2_brain_neural` + sơ đồ 3 vòng (dùng lại `brain3` Tập 01) | *Không phải một kẻ loạn thần mất trí* → `#2`: **HOÀN TOÀN TỈNH TÁO** → `#3`: **3 TẦNG CƠ CHẾ TÂM LÝ** | 3 vòng sáng ở `#3` | ✦ Cáo | |
| 3-08 | `3.05#4` | C | T9 | `t2_escalation_stairs` | *TẦNG 01* · **QUY LUẬT LEO THANG HÀNH VI** · *Và sự lờn Dopamine* | — | | |
| 3-09 | `3.05#5` | C | T1 | `t2_escalation_stairs`, `pan` | **BẮT ĐẦU TỪ NHỮNG XUNG LỰC RẤT NHỎ** | Tiêu đề ở "xung lực" (thuật ngữ y khoa chỉ đọc, không hiện) | | |
| 3-10 | `3.05#6`–`#7` | C | T9 | `t2_brain_neural` + đường nhịp tăng vọt (Pillow) | **DOPAMINE** · *Phấn khích và phần thưởng* → `#7`: *Theo mô hình đó: một cơn hưng phấn dị thường* | Nhịp nhấp nháy ở `#7` | | |
| 3-11 | `3.05#8`–`#9` | C | T9 | `t2_brain_neural`, đường nhịp phẳng dần | **CƠ CHẾ DUNG NẠP** → `#9`: *Như người nghiện cần liều lượng ngày càng cao* | — | 🅑 | |
| 3-12 | `3.05#10` | C | T8 | `t2_escalation_stairs`, `pan` | *Nhà trống · Đối diện với nạn nhân · Khống chế nạn nhân · Quyền sinh tử* | Mỗi bậc ở cụm từ, camera leo dần | | |
| 3-13 | `3.05#11` | C | T1 `hero` | `t2_stairs_dark`, tối dần | **MỘT CHIẾC DỐC KHÔNG ĐÁY** | Tiêu đề ở "dốc không đáy" | ⊘ | |
| 3-14 | `3.06` (nghỉ 1,5 s) | — | — | giữ 3-13 | — | — | | |
| 3-15 | `3.07#1` | H | T1 | `t2_drawer_dark` | **CÁCH HẮN CHE GIẤU NÓ** | — | | ✂ |
| 3-16 | `3.07#2` | H | T3 so sánh | `t2_two_masks` | *BAN NGÀY* · *Điều hành các cuộc họp · Bắt tay các quan chức · Ăn tối cùng vợ* → *NỬA ĐÊM* · **MỘT KẺ KHÁC HOÀN TOÀN** | Cột phải ở "nửa đêm" | | |
| 3-17 | `3.07#3` | H | T1 | `t2_two_masks`, `push` | **LÀM THẾ NÀO MÀ KHÔNG BỊ PHÁT ĐIÊN?** | — | →C | |
| 3-18 | `3.08#1`–`#2` | C | T9 | `t2_two_drawers` | *TẦNG 02* · **SỰ PHÂN MẢNH TÂM TRÍ TUYỆT ĐỐI** → `#2`: *(Compartmentalization)* · *Một cơ chế phòng vệ · Những ngăn kéo riêng biệt* | Thuật ngữ Anh ở `#2` | | |
| 3-19 | `3.08#3`–`#5` | C | T3 so sánh | `t2_two_drawers` | *Ngăn kéo 01* · **ĐẠI TÁ WILLIAMS** · *Trật tự · Kỷ cương · Đạo đức* → `#5`: *Ngăn kéo 02* · **KẺ SĂN MỒI BÓNG ĐÊM** · *Trút bỏ mọi quy chuẩn xã hội* | Cột phải ở `#5` | | |
| 3-20 | `3.08#6`–`#8` | C | T1 | `t2_drawer_dark` | **ĐÓNG CHẶT CÁNH CỬA CỦA NGĂN KÉO KIA** → `#8`: *Không bị giằng xé nội tâm* | Ngăn kéo đóng ở "đóng chặt" | | |
| 3-21 | `3.08#9`–`#10` | C | T4 `hero` | `t2_interrogation_empty` | *KHÔNG THỂ TỰ GIẢI THÍCH* → `#10`: “Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng.” | Câu trích từng dòng từ dấu `:` | ⊘ | |
| 3-22 | `3.08#11`–`#12` | C | T1 | `t2_interrogation_empty` | **CÂU TRẢ LỜI TRUNG THỰC NHẤT** → `#12`: *Đặt lại toàn bộ khung phân tích* | — | 🅑 | |
| 3-23 | `3.09` (nghỉ 2 s) | — | — | giữ 3-22 | — | — | | |
| 3-24 | `3.10#1` | H | T1 | `t2_command_chair`, `push` | *TẦNG TÂM LÝ THỨ BA* · **ĐỘNG CƠ CỐT LÕI?** | — | →C | |
| 3-25 | `3.11#1` | C | T9 | `t2_command_chair` | *TẦNG 03* · **ÁI KỶ ÁC TÍNH** *(Malignant Narcissism)* · **PHỨC CẢM CHÚA TRỜI** *(God Complex)* | Thuật ngữ 2 ở "Phức cảm" | | |
| 3-26 | `3.11#2`–`#3` | C | T3 | `t2_base_trenton` | **QUYỀN LỰC QUÂN SỰ** · *Hàng nghìn người phải phục tùng* → `#3`: *Bị ràng buộc bởi luật pháp và hệ thống* | — | | |
| 3-27 | `3.11#4` | C | T1 | `bedroom_door` tối | **MỘT THỨ QUYỀN LỰC KHÔNG BỊ RÀNG BUỘC** · *Định đoạt số phận · Tước đoạt nhân phẩm* | Tiêu đề ở "quyền lực không" | ⊘ | |
| 3-28 | `3.11#5` | C | T4 | `t2_command_chair` tối | *Bằng chứng nuôi dưỡng cái tôi ái kỷ* → “Ta là kẻ đứng trên tất cả… không một ai trong các ngươi có thể chạm tới ta.” | Câu trích ở "Ta là kẻ" (lời độc thoại tưởng tượng — dấu “” màu tím `violet` của Cáo, không phải lời thật) | | |
| 3-29 | `3.11#6`–`#8` | C | T1 | `t2_oath_hall` | **KHÔNG BỊ ĐÈ BẸP BỞI SỰ XẤU HỔ** → `#8`: *Vẫn là người đàn ông ở bục nhậm chức* | Gọi lại hình lễ nhậm chức Hồi 1 | 🅑 | |
| 3-30 | `3.11#9`–`#11` | C | T3 so sánh | `void` | **MỘT CƠN CUỒNG** · *Sẽ tự tắt* → `#11`: **Ở ĐÂY** · *Mỗi lần vi phạm lại được thưởng* | Cột phải ở `#11` | | |
| 3-31 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **NGHỆ THUẬT BẺ GÃY BỘ ÓC QUÂN SỰ** | — | ⊘ | ◼ |

### HỒI 4 — ĐẤU TRÍ PHÒNG THẨM VẤN · nền chủ đạo `t2_two_chairs`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.03#1`–`#2` | H | T5 ngày | `t2_interrogation_empty` | **07 · 02 · 2010** · *Chủ nhật · Trụ sở cảnh sát tại Ottawa · 3 giờ chiều* | Gõ từng ký tự; đèn huỳnh quang (SFX `4.01`) | | |
| 4-02 | `4.03#3`–`#4` | H | T3 so sánh | `t2_two_chairs` | *Một bên bàn* · **ĐẠI TÁ RUSSELL WILLIAMS** · *Quần áo dân sự* → `#4`: *Đối diện* · **THÁM TỬ JIM SMYTH** · *Chuyên gia khoa học hành vi · Cảnh sát tỉnh Ontario* | Cột phải ở `#4`; chỉ tên, không gắn lên bóng (V5) | | |
| 4-03 | `4.03#5`–`#6` | H | T2 | `t2_interrogation_empty` | **TỰ NGUYỆN ĐẾN ĐÂY** · *Sau một cuộc điện thoại mời* → `#6`: *Được đọc quyền và cảnh báo pháp lý — vẫn bình thản ngồi lại* | — | | |
| 4-04 | `4.04` (nghỉ 2 s) | — | — | giữ 4-03 | — | — | | |
| 4-05 | `4.05#1`–`#2` | H | T1 | `t2_tape_recorder`, `push` | **MỘT TRONG NHỮNG CUỘC THẨM VẤN KINH ĐIỂN NHẤT** → `#2`: *LẮNG NGHE:* **MỘT NGƯỜI THEO DÕI VỤ ÁN** | — | →N2 | |
| 4-06 | `4.06#1` | N2 | T4 lời kể | `t2_interrogation_empty` | “…một sĩ quan cấp cao như Đại tá Williams hẳn phải biết rõ quyền của mình.” | — | ✦ Mèo | |
| 4-07 | `4.06#2` | N2 | T8 | `t2_boot_evidence` | *CẢNH SÁT LÚC ĐÓ MỚI CHỈ CÓ* · *Dấu vết lốp xe · Dấu giày trên nền tuyết* → *Toàn quyền giữ im lặng hoặc yêu cầu luật sư* | Mỗi mục ở cụm từ | | |
| 4-08 | `4.06#3` | N2 | T4 lời kể | `t2_two_chairs` | “Vậy bằng cách nào… lại tự miệng thú nhận toàn bộ chỉ sau vài tiếng đồng hồ?” | — | 🅑 | |
| 4-09 | `4.07#1`–`#2` | H | T1 | `t2_two_chairs`, `pull` | **KỸ THUẬT THẨM VẤN TÂM LÝ** · *Thám tử Jim Smyth* → `#2`: *LẮNG NGHE:* **TỪNG NƯỚC CỜ** | — | →D | |
| 4-10 | `4.08#1` | D | T9 | `t2_two_chairs` | **NGHỆ THUẬT XÂY DỰNG SỰ KẾT NỐI** *(Rapport Building)* · *Chiếc bẫy hạ nhiệt cảm xúc* | — | | |
| 4-11 | `4.08#2`–`#4` | D | T8 | `t2_interrogation_empty` | *Giọng đều đặn và dễ chịu* → `#3`: **SẴN SÀNG ĐƯA RA NHỮNG GÌ?** → `#4`: *Mẫu ADN · Dấu vân tay · Dấu giày* | Mỗi mục ở cụm từ | | |
| 4-12 | `4.08#5`–`#6` | D | T3 so sánh | `t2_siren_wall` | **CÁI BẪY CỦA SỰ TỰ TIN** → `#6`: *Cùng lúc: lệnh khám đang được thi hành · Tweed · Ottawa* | Đèn xanh đỏ ở `#6` | | |
| 4-13 | `4.08#7` | D | T3 so sánh | `t2_boot_evidence`, `still` | *Dấu giày gần nhà nạn nhân* · *Dấu giày của chính Williams* → “Chúng giống hệt nhau.” | Câu trích ở "và nói" | | ✂ |
| 4-14 | `4.08#8`–`#9` | D | T1 | `t2_tire_track` | *Vân lốp Nissan Pathfinder có vẻ trùng với vết bánh xe gần nhà Jessica Lloyd* → `#9`: **MỌI CHUYỆN ĐÃ KẾT THÚC** | — | | |
| 4-15 | `4.10#1` | D | T4 | `t2_two_chairs` | *MỘT ĐỀ NGHỊ KỲ LẠ* → “Cứ gọi tôi là Russ.” | Trượt ảnh "Xoẹt" (SFX `4.09`) ở đầu | | |
| 4-16 | `4.10#2`–`#3` | D | T4 `hero` | `t2_siren_wall` | **NƯỚC CỜ QUYẾT ĐỊNH** → `#3`: “Vợ ông giờ đã biết chuyện gì đang xảy ra.” | Câu trích ở "nói thêm" | ⊘ | |
| 4-17 | `4.10#4`–`#5` | D | T1 | `bedroom_door` | **CÁNH CỬA ĐÃ BỊ MỞ** → `#5`: *Hình tượng · Danh dự · Gia đình* | Khe sáng mở rộng ở "bị mở" | | |
| 4-18 | `4.10#6`–`#7` | D | T4 | `t2_head_down` | *Không thú nhận ngay* → `#7`: “Tôi không biết phải nói gì.” | — | | |
| 4-19 | `4.10#8` | D | T4 | `t2_interrogation_empty`, `still` | *Khoảng bốn tiếng bốn mươi phút sau* → “Vậy, cô ấy ở đâu?” | Câu trích ở "hỏi khẽ" | | |
| 4-20 | `4.10#9` | D | T4 `hero` | `t2_forest_map` | “Có bản đồ không?” | — | ⊘ | ✂ |
| 4-21 | `4.10#10` | D | T1 | `t2_interrogation_early` | *Gần sáu tiếng tiếp theo* · **TỪNG VỤ MỘT** | — | | |
| 4-22 | `4.11#1`–`#3` | C | T1 | `t2_two_drawers` | **KHOẢNH KHẮC TÂM LÝ SỤP ĐỔ** → `#3`: *Bức tường giữa hai ngăn kéo tâm trí · Vỡ vụn* | Hai ngăn kéo bật mở ở `#3` | 🅑 | |
| 4-23 | `4.11#4`–`#5` | C | T4 | `t2_interrogation_empty` | *ĐIỂM YẾU DUY NHẤT CÒN LẠI* · **NGƯỜI VỢ** → `#5`: “Tôi muốn giảm thiểu ảnh hưởng lên vợ tôi.” | — | | |
| 4-24 | `4.11#6`–`#7` | C | T1 | `t2_two_chairs` | *Cách duy nhất là bắt đầu bằng sự thật* → `#7`: **KHOẢNG NỬA GIỜ SAU** | — | | |
| 4-25 | `4.11#8`–`#9` | C | T3 so sánh | `void` | *NHỮNG NỖI LO HẮN NÓI RA* · *Vợ mình · Tác động lên căn cứ* → `#9`: *KHÔNG PHẢI* · **NHỮNG NGƯỜI PHỤ NỮ ĐÃ BỊ HẮN LÀM HẠI** | Cột phải ở `#9` | ⊘ | |
| 4-26 | `4.11#10`–`#11` | C | T3 so sánh | `void` | **KHÔNG PHẢI SỰ HỐI HẬN** → `#11`: **LÀ SỰ SỢ HÃI** · *Sợ mất đi hình tượng* | Cột phải ở `#11` | | |
| 4-27 | `4.11#12` | C | T1 | `t2_head_down` | **MỘT NGƯỜI ĐÀN ÔNG DUY NHẤT** · *Phải đối diện với tất cả những gì mình đã làm* | — | 🅑 | |
| 4-28 | `4.12#1` | H | T1 `hero` | `t2_head_down` | **CÚI GỤC ĐẦU** | — | ⊘ | |
| 4-29 | `4.12#2`–`#3` | H | T7 | `t2_forest_map` | *Chỉ trên bản đồ* → `#3`: **RẠNG SÁNG HÔM SAU** · *Cảnh sát đến được nơi đó* | 2 ghim không nhãn, đường đứt nét tự vẽ | ⊘ | |
| 4-30 | `4.12#4` | H | T8 | `records` | *THỪA NHẬN* · *Vụ việc với nữ hạ sĩ Marie-France Comeau · Hai vụ tấn công tình dục ở Tweed* | — | | |
| 4-31 | `4.12#5` | H | T1 | `t2_interrogation_early` | *Sau khoảng mười tiếng đồng hồ* · **VỎ BỌC HOÀN HẢO ĐÃ SỤP ĐỔ** | — | | |
| 4-32 | `4.12#6`–`#7` | H | T1 | `t2_folder_tree` | **CÂU CHUYỆN CHƯA KẾT THÚC** → `#7`: *Kho ảnh và ghi chép hắn tự lưu giữ* | — | | |
| 4-33 | `4.12#8` | H | T5 | `pinboard` | **88** · *82 cáo buộc đột nhập · Tổng cộng 88 cáo buộc · Một người đàn ông duy nhất* | Số đếm 0 → 88 (T5 chỉ hiện một số lớn) | | |
| 4-34 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT, CẢNH BÁO ĐỎ & LỜI KẾT** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT, BÀI HỌC CẢNH BÁO ĐỎ & LỜI KẾT · nền chủ đạo `t2_courtroom`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#2` | H | T5 ngày | `t2_courtroom` | **10 · 2010** · *Tòa án Cấp cao Ontario · Thẩm phán Robert Scott · Belleville* (chỉ chữ, V5) | Búa gõ ba lần (SFX `5.01`) trước câu | | |
| 5-02 | `5.02#3` | H | T5 | `t2_courtroom` | *Ngày 18 tháng 10* · **88** · *Nhận tội trước toàn bộ cáo buộc* | Số đếm | | |
| 5-03 | `5.02#4` | H | T8 | `t2_gavel` | *NGÀY 21 · THẨM PHÁN TUYÊN PHẠT* · *Hai mức tù chung thân chạy song song · 10 năm cho mỗi tội tấn công tình dục · 10 năm cho mỗi tội giam giữ trái phép · 1 năm cho mỗi trong 82 vụ đột nhập* | Mỗi mục ở cụm từ (câu dài ~20 s → 5 beat) | | |
| 5-04 | `5.02#5`–`#6` | H | T5 | `t2_gavel` | **25 NĂM** · *Không được xét ân xá* → `#6`: *Mức án tối thiểu luật hình sự Canada bắt buộc* | Số đếm 0 → 25 | | |
| 5-05 | `5.03` (nghỉ 2 s) | — | — | giữ 5-04 | — | — | | |
| 5-06 | `5.04#1` | H | T1 | `t2_oath_hall` tối | **SỰ SỤP ĐỔ HOÀN TOÀN VỀ DANH DỰ** | Gọi lại hình lễ nhậm chức, nay tối | | |
| 5-07 | `5.04#2`–`#4` | H | T8 gạch bỏ | `t2_medals_cut` | *Quân hàm · Huân chương · Sắc lệnh phong cấp · Tiểu sử trên trang Bộ Quốc phòng* | Mỗi câu gạch mục tương ứng | | |
| 5-08 | `5.04#5` | H | T1 | `t2_uniform_fire` | **ĐỐT QUÂN PHỤC** · *Căn cứ Trenton · Một cơ sở vốn dùng để tiêu hủy tài liệu* | Lửa bùng ở "đốt quân phục" | | |
| 5-09 | `5.04#6`–`#7` | H | T2 | `t2_uniform_fire` mờ | *Hubert Genest · Người phát ngôn quân đội* · *Không có nghi lễ chính thức · Không có ảnh chụp* → `#7`: **LẦN ĐẦU TIÊN TRONG 25 NĂM** | Tiêu đề ở `#7` | | |
| 5-10 | `5.04#8` | H | T4 | `t2_uniform_fire` tối | “Khi đặt dấu chấm cuối câu, dấu chấm ấy nhỏ thôi, nhưng nó mang rất nhiều ý nghĩa.” | Câu trích ở "câu văn" | ⊘ | |
| 5-11 | `5.04#9` | H | T1 | `t2_checkpoint_dawn` | **CHIẾC SUV BỊ ĐÈ NÁT** · *Hàng trăm món đồ bị đem đốt* | — | | |
| 5-12 | `5.05` (nghỉ 2 s) | — | — | giữ 5-11 | — | — | | |
| 5-13 | `5.06#1` | H | T1 | `t2_red_flags` | **NHẬN DIỆN SỚM NHỮNG KẺ SĂN MỒI** · *Ẩn mình sau những vỏ bọc hoàn hảo* | — | | |
| 5-14 | `5.06#2` | H | T1 | `t2_red_flags`, `pull` | **4 DẤU HIỆU CẢNH BÁO ĐỎ** · *Chuyên gia tâm lý & Điều tra viên* | — | →C+D | |
| 5-15 | `5.07#1`–`#3` | C | T8 cờ | `void` đỏ sẫm, 4 ô cờ | *01* · **KHÔNG XEM NHẸ CÁC HÀNH VI LỆCH LẠC RANH GIỚI BAN ĐẦU** → `#2`: *Nhìn trộm · Theo dõi qua mạng · Lục lọi đồ riêng tư* | Cờ 1 tô đầy | hai badge | |
| 5-16 | `5.07#4`–`#6` | C | T8 cờ | cờ 2 | *02* · **SỰ TÁCH RỜI CẢM XÚC BẤT THƯỜNG** → `#6`: *Lo cho vợ và cho căn cứ — không phải cho những người đã bị hắn làm hại* | — | hai badge | |
| 5-17 | `5.08#1`–`#3` | D | T8 cờ | cờ 3 | *03* · **BÍ MẬT CỰC ĐOAN · THÓI QUEN GIỮ KỶ VẬT** → `#3`: *Một hệ thống ghi chép · Một kho ảnh phân cấp · Những món đồ được cất giấu* | — | hai badge · Sói sáng | |
| 5-18 | `5.08#4`–`#5` | D | T8 cờ | cờ 4 | *04* · **VỎ BỌC ĐẠO ĐỨC QUÁ HOÀN MỸ** | — | hai badge | |
| 5-19 | `5.08#6`–`#7` | D | T8 cờ | đủ 4 cờ | *Sự cầu toàn không phải là dấu hiệu tội phạm* → `#7`: *Đáng chú ý khi đi kèm sự bí mật cực đoan và sự thiếu đồng cảm* | Cờ 4 viền mảnh lại ở `#6` (cân bằng, tránh định kiến) | hai badge | |
| 5-20 | `5.09` (nghỉ 2 s) | — | — | giữ 5-19 | — | — | ⊘ | |
| 5-21 | `5.10#1`–`#3` | H | T1 | `t2_podcast_desk`, đèn ấm dần | *Vực thẳm sâu hoắm của tâm trí con người* → `#2`: **CHỈ LÀ LỚP ÁO KHOÁC BÊN NGOÀI** → `#3`: *Không phải tấm khiên bảo chứng cho đạo đức* | — | | |
| 5-22 | `5.10#4`–`#5` | H | T1 `hero` | `t2_escalation_stairs` | *Hiếm khi bắt đầu bằng một phát súng hay một nhát dao* → `#5`: **TỪ MỘT BƯỚC CHÂN VƯỢT QUA LẰN RANH** | Câu dài → beat ở "từng bước" | | |
| 5-23 | `5.10#6`–`#9` | H | T8 | `t2_folder_tree` | **NGƯỜI DUY NHẤT GIỮ BÍ MẬT** → `#7`: *Những tập ảnh được sắp xếp tỉ mỉ* → `#8`: *Những món đồ được cất giấu cẩn thận* → `#9`: *Một cuộc đấu trí khoảng mười tiếng đồng hồ* | Mỗi câu một mục | | |
| 5-24 | `5.10#10`–`#11` | H | T1 `hero` | `t2_oath_hall` | **BỘ ÓC TINH HOA KHÔNG BẢO VỆ ĐƯỢC AI CẢ** → `#11`: *Chỉ làm cho lần sụp đổ ấy đến muộn hơn, và nặng hơn* | Tiêu đề ở "không bảo vệ" | ⊘ | |
| 5-25 | `5.11` (nghỉ 1,5 s) | — | — | giữ 5-24 | — | — | | |
| 5-26 | `5.12#1`–`#2` | H | T1 | `t2_podcast_desk` | **CẢM ƠN CÁC KHÁCH MỜI** · *Nhân vật minh hoạ · giọng đọc AI* | 5 ảnh P0 sáng lần lượt | dàn khách mời | |
| 5-27 | `5.12#3` | H | T1 | `t2_podcast_desk` | **GIỮ MỘT CÁI NHÌN TỈNH TÁO** · *Lắng nghe trực giác · Trân trọng những ranh giới an toàn* | — | | |
| 5-28 | `5.12#4` | H | T10 | `t2_podcast_desk` mờ | **HẸN GẶP LẠI Ở TẬP TIẾP THEO** · *Để lại góc nhìn của bạn ở phần bình luận* | — | 🅑 | |
| 5-29 | `5.13`–`5.14` | — | T2 | `t2_podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | *HỒ SƠ TẬP 02 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật* | Thẻ hồ sơ hiện sau tiếng "Cạch"; mờ ra đen | ⊘ | ◼ |

**Tổng: 151 dòng = 134 shot có lời + 17 dòng không lời.** Phủ 215/215 câu, đúng thứ tự, cột Vai khớp người nói, mọi nền có file, mọi câu trích nguyên văn (kiểm tra bằng script ngày 22/10/2026). Các số `01`–`04`, `02` trên hình là nhãn thứ tự (giống *TẦNG 01*, cờ *01* của Tập 01), không phải dữ kiện.


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
