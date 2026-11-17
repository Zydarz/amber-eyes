# BÁO CÁO QC — TRAILER KÊNH CONCEPT A "SỢI CHỈ ĐỎ" (bản VN + bản EN)

*Ngày: 16/11/2026 · Kịch bản: `02_SAN_XUAT/BRAND/Kichban_Trailer_A.md`*
*Thành phẩm: `assets/brand/trailer_kenh_A_vn.mp4` (36,3 MB) · `assets/brand/trailer_kenh_A_en.mp4` (36,6 MB)*
*Nguồn dựng: `.work/trailer_a/` · Bản gốc VN v1 (trước bản vá hiện dòng thẻ): `.work/_cu/trailer_20261116/`*

---

## 0. Bản EN — khác bản VN ở đâu

Cùng timeline 50,0 s, chỉ đổi **3 nhóm**:

| Hạng mục | VN | EN |
|---|---|---|
| Giọng VO | `English_CaptivatingStoryteller` (bộ A) | `English_magnetic_voiced_man` (bộ EN) |
| Lời đọc | 6 câu (bảng §2) | 6 câu EN (`Kichban_Trailer_A.md` §2.1) |
| Tagline end card | "Phân tích tâm lý tội phạm qua những hồ sơ có thật" | "Criminal psychology through real case files" |
| Nhãn vai | DẪN CHUYỆN / ĐIỀU TRA VIÊN / CHUYÊN GIA TÂM LÝ | HOST / INVESTIGATOR / PSYCHOLOGIST |
| Thẻ miễn trừ | "VỀ NỘI DUNG NÀY" (3 dòng tiếng Việt) | "ABOUT THIS VIDEO" (3 dòng tiếng Anh) |
| Dòng số liệu | 29 HỒ SƠ · 5 VAI CHÍNH · 4 NGÔN NGỮ | 29 CASE FILES · 5 CHARACTERS · 4 LANGUAGES |

**Cách chạy lại bản EN:** `AE_LANG=en py -3 .work/make_trailer.py` → `AE_LANG=en py -3 .work/make_trailer_audio.py` → `py -3 .work/_qc_trailer.py --lang en`.
Script dùng `AE_LANG` để tự chọn giọng, tagline, nhãn, thẻ và hậu tố file ⇒ **JA/KO chỉ cần thêm lời đọc vào `vo_manifest.json`**, không phải sửa code.

---

## 1. Thông số thật (đo trên chính file mp4 thành phẩm)

| Mục | Đo được | Ngưỡng | Kết quả |
|---|---|---|---|
| Thời lượng | **50,000 s** (VN) · **49,995 s** (EN) | 50,0 ± 0,05 s | ✅ |
| Kích thước / tần số | 1920×1080 @ 30/1 | 16:9 @30 | ✅ |
| Codec | H.264 (libopenh264 8M) + AAC 192k | H.264 + AAC | ✅ |
| Âm thanh | 44 100 Hz, 2 kênh | stereo | ✅ |
| Loudness (đo lại trên mp4) | **VN −16,14 LUFS · EN −16,20 LUFS** | −16 ± 1 | ✅ |
| True peak | **VN −1,83 dBFS · EN −1,83 dBFS** | ≤ −1,5 dBFS | ✅ |
| LRA | VN 4,5 LU · EN 9,4 LU | — | nghe ổn, không nén méo tiếng |
| Khoảng câm > 0,3 s @ −60 dB | **0** (cả 2 bản) | 0 (V4 / A1) | ✅ |
| Lỗi giải mã | **0** (cả 2 bản) | 0 | ✅ |
| Lệch hình/tiếng | **0,000 s** (VO đặt bằng `adelay` theo mili giây) | ≤ 0,05 s | ✅ |

**Chuẩn hoá (A7):** loudnorm 2 lượt (VN đo vào I = −27,11 LUFS · TP = −7,43 dBFS; EN đo vào I = −20,86 LUFS · TP = −4,81 dBFS) → `alimiter=limit=0.7943:…:latency=1` → AAC. Chuỗi limiter có `latency=1` (bẫy A11 #64: thiếu thì âm lệch ~5 ms).

---

## 2. Cấu trúc thời gian (50,0 s)

| Mốc | Nội dung | Nguồn hình | VO (thời lượng thật) |
|---|---|---|---|
| 0,0–4,6 | Hook: sợi chỉ đỏ vẽ tay → đôi mắt hổ phách bừng sáng | procedural (`make_intro.build_logo_layers`) + `bg/void.png` | — |
| 4,6–10,6 | Bảng ghim hồ sơ, 5 thẻ số 01·07·12·19·29 lần lượt | `bg/pinboard.png` | T-01 · 3,17 s |
| 10,6–16,6 | Bàn podcast · **Cú** · nhãn "DẪN CHUYỆN" | `bg/podcast_desk.png` + `cast/H/P1.png` | T-02 · 2,42 s |
| 16,6–22,6 | Phòng thẩm vấn · **Sói** · nhãn "ĐIỀU TRA VIÊN" | `bg/interrogation.png` + `cast/D/P1.png` | T-03 · 3,10 s |
| 22,6–28,6 | Bàn DSM-5 · **Cáo** · nhãn "CHUYÊN GIA TÂM LÝ" | `bg/brain_desk.png` + `cast/C/P1.png` | T-04 · 2,28 s |
| 28,6–34,6 | Hành lang · cả 3 vai ở 3 góc | `bg/corridor.png` + H/D/C | T-05 · 2,90 s |
| 34,6–38,6 | Thẻ miễn trừ "VỀ NỘI DUNG NÀY" | procedural (`make_intro.card_base`) | — |
| 38,6–46,4 | End card: logo + wordmark + tagline + số liệu | `brand/logo*` + `bg/void.png` | T-06 · 5,02 s |
| 46,4–50,0 | End slate: wordmark + tagline góc trái dưới, mờ dần | procedural | — |

Tổng lời đọc **18,9 s / 50 s** — mọi câu nằm gọn trong nhịp của nó, không chồng nhau.

---

## 3. Giọng đọc

| Mục | Kết quả |
|---|---|
| Giọng | `English_CaptivatingStoryteller` (bộ A, `edition.py`), speed 0,88–0,92, pitch 0, emotion `neutral` |
| Engine | MiniMax TTS qua `connector__matrix__batch_text_to_audio` (mcode-tools) |
| G1 | Không `...`, không `<#s#>` giữa câu ✅ |
| G3 | Chỉ `neutral` ✅ |
| G4 | Lệch speed trong −0,02…+0,02 ✅ |
| G5 | Pitch = 0 ✅ |
| G9/G10 | **Không áp dụng** — trailer chỉ dùng MỘT vai (Host) ⇒ không có rủi ro tách bạch vai, không dính điểm yếu CER 3,1 % của vai Sói |

**Thời lượng VO đo thật**

| Câu | VN | EN |
|---|---|---|
| T-01 | 3,17 s | 2,78 s |
| T-02 | 2,42 s | 2,29 s |
| T-03 | 3,10 s | 2,29 s |
| T-04 | 2,28 s | 2,24 s |
| T-05 | 2,90 s | 3,48 s |
| T-06 | 5,02 s | 4,31 s |
| **Tổng** | **18,9 s** | **17,4 s** |

Mọi câu đều nằm gọn trong nhịp của nó (mốc 5,2 / 11,2 / 17,2 / 23,2 / 29,2 / 39,4 s) — không câu nào chồng lên nhau hay tràn sang nhịp kế.

**Chưa đo lại CER trên máy này** (không cài `whisper`; dự án đo CER trên Kaggle/Mac theo `QUY_TAC_AUDIO_HIGGS_MAC.md`). Cơ sở để tin dùng: đây **đúng giọng + đúng speed** đã đo CER 0,1 % trên 20 câu của Tập 02 (`BaoCao_GiongDoc_Tap02.md` §4) ⇒ không có lý do đổi danh tính. Việc nghe duyệt cuối vẫn cần người dùng.

---

## 4. Tài sản dùng lại (không tốn credit AI)

| Tài sản | Nguồn |
|---|---|
| Logo layers, wordmark, tagline, thẻ giấy | `.work/make_intro.py` + `.work/make_logo.py` (tái dùng nguyên xi) |
| 5 linh thú (bán thân PNG) | `assets/cast/{H,D,C}/P1.png` |
| 6 nền 16:9 | `assets/bg/`: void · pinboard · podcast_desk · interrogation · brain_desk · corridor |
| Nhạc nền | `assets/bgm/bgm_music_box.mp3` + `bgm_sub_drone.mp3` |
| SFX | `assets/sfx/folder_close.wav`, `card_flip.wav` |

**Tổng credit AI phát sinh: 0 ảnh · 0 clip video.** Chỉ 6 câu TTS.

---

## 5. Việc đã sửa trong lúc dựng (bài học)

| # | Vấn đề | Sửa |
|---|---|---|
| 1 | `MI.build_logo_layers()` gọi **mỗi khung hình** (blur 2048 px) ⇒ render 12 phút | cache 1 lần trong `_cache` |
| 2 | `ml.make_mark()` / `MI.wordmark_layer()` cũng dựng lại mỗi khung | cache |
| 3 | `loudnorm print_format=json` in ra **stderr**, không phải stdout ⇒ crash parse | đọc cả stderr |
| 4 | Nhãn vai 34 px, quá nhỏ trên 1920 | lên 46 px + scrim đáy khung |
| 5 | 4 giây cuối đen trống (watermark fade ngược) | end slate giữ tới 50 s, đen ở mức 238/255 |
| 6 | 3 linh thú nhịp 6 bị cắt, bé | to 540/500/540 px, dời lên |
| 7 | Thẻ miễn trừ hiện **cả 3 dòng cùng lúc**: thời gian hiện dòng lấy theo giây tuyệt đối của bumper (4,30 s) trong khi thẻ nằm ở 34,6 s | dùng thời gian **tương đối** (`t − t0 + 4,00`) ⇒ 3 dòng hiện lần lượt |
| 8 | File VO EN ghi đè file VN (cùng mã T-01…T-06) | tách thư mục `vo/` và `vo_en/` theo `--lang` |
| 9 | Script dựng hình viết tiếng Việt cứng | đọc `AE_LANG` → tự chọn giọng/tagline/nhãn/thẻ, hậu tố file `_EN` |

---

## 6. Lớp video động — MiniMax Hailuo-2.3, chế độ first-frame

**Vì sao không phải H3?** H3/H3-Max bị provider từ chối **HTTP 402** ngay lúc gửi: *"the remaining M Plan weekly limit and account credits cannot cover this MiniMax-H3 video generation… legacy Token Plan usage limits cannot be used"*. 402 = **không tạo task nào, không tính phí**. **Hailuo-2.3 vẫn dùng được hạn mức Token Plan** ⇒ chọn H2.3 sau khi hỏi ý kiến người dùng.

| Thông số | Giá trị |
|---|---|
| Model | `MiniMax-Hailuo-2.3` |
| Chế độ | **first-frame** (`input_image` + `reference_type=first_frame`) — không dùng `ratio`, không dùng reference_images/videos/audios (H2.3 không hỗ trợ) |
| Thời lượng / độ phân giải | 6 s / 1080P (1080P của H2.3 chỉ hợp lệ ở 6 s) |
| Âm thanh | **KHÔNG có** (H2.3 silent) ⇒ trailer tiếp tục dùng VO MiniMax TTS + nhạc/SFX sẵn có, đã QC |
| Khung đầu | chính nền của kênh: `void` · `pinboard` · `interrogation` · `corridor` |

**4 task đã gửi (mỗi task 1 lần, không gửi lại):**

| Clip | Task ID | Node ID | Thời lượng | File |
|---|---|---|---|---|
| hook | 463896020181301 | 463898754625778 | 5,88 s | `videos/soi-chi-do-hook.mp4` |
| board | 463897165648154 | 463899136549084 | 5,88 s | `videos/bang-ho-so-chay.mp4` |
| interrogation | 463896082674030 | 463899136549088 | 5,88 s | `videos/phong-tham-van-mo.mp4` |
| corridor | 463897751781579 | 463898797064311 | 5,88 s | `videos/hanh-lang-dem.mp4` |

**Preflight (đo thật trước khi upload):** cả 4 ảnh PNG 2112×1188, tỉ lệ 1,778, 0,38–4,64 MB ⇒ hợp lệ (yêu cầu 256–5760 px, ≤ 30 MB, tỉ lệ 0,4–2,5). Batch 4 ảnh ≤ 12 file.

**QC clip (soi montage 16 khung, `.work/qc_montage/h23_clips.jpg`):**
- **0 chữ AI** — đúng bằng chế độ first-frame (bề mặt giấy trong nền gốc đã trống sẵn, AI không có chỗ để viết chữ).
- Phong cách khớp 100 % với phần còn lại của trailer (vì AI hoạt họng chính nền gốc).
- Chuyển động đúng như yêu cầu: giấy bay + sợi chỉ đỏ đung đưa (board) · bụi trong luồng sáng (interrogation) · sương trườn + camera lùi (corridor) · sương mờ (hook).
- Nhược điểm nhỏ đã ghi nhận: ở `board` có 1–2 mảnh giấy chuyển động bị vẽ thành khối đen ngắn quãng; hình hài không lệch phong cách.

**Cách ghép:** `make_trailer.py` đọc clip đã chuẩn hoá trong `.work/trailer_a/h23_norm/`, trộn vào nền theo trọng số mờ dần ở 2 đầu nhịp (0,55 s) để không giật. Clip **không** có grain/vignette riêng — lớp chung của pipeline áp sau cùng ⇒ hạt phim đồng nhất toàn video.

---

## 7. Việc CHƯA làm / cần người dùng chốt

1. **Nghe duyệt** giọng đọc + nhịp 50 s (cả 2 bản).
2. **Bản JA / KO** — lời đọc **chưa viết**; script đã sẵn sàng chạy đa ngôn ngữ, chỉ cần thêm 6 câu vào `vo_manifest.json` + giọng JA/KO trong `edition.CAST`.
3. **Nâng cấp bằng AI** (cần duyệt credit theo L4): 4 ảnh MiniMax cho bảng hồ sơ / phòng thẩm vấn / bàn tâm lý / hành lang **riêng cho trailer** + 1 clip H3 6–8 s cho hook. Hiện tại trailer dùng nền có sẵn của Tập 01 — dùng được nhưng **nền dùng chung với tập**, khó "riêng" cho video quảng bá.
4. **Thẻ kết / subscribe cue**: end card chưa có lời kêu gọi đăng ký (vì không rõ kênh đăng ở đâu, có chính sách riêng không).

---

## 8. File liên quan

| File | Vai trò |
|---|---|
| `assets/brand/trailer_kenh_A_vn.mp4` | **thành phẩm** (media, không commit — `.gitignore` `*.mp4`) |
| `.work/trailer_a/picture.mp4` | hình chưa ghép tiếng |
| `.work/trailer_a/audio_master.wav` | âm thanh đã chuẩn hoá |
| `.work/trailer_a/vo/*.mp3` | 6 câu VO |
| `.work/trailer_a/vo_manifest.json` | manifest lời đọc (VI + EN) |
| `.work/make_trailer.py` | dựng hình |
| `.work/make_trailer_audio.py` | trộn + loudnorm + đóng gói |
| `.work/make_trailer_tts.py` | đọc giọng |
| `.work/_qc_trailer.py` | QC đo thật + montage |
| `.work/qc_montage/trailer_frames.jpg` | tờ soi 20 khung hình |
