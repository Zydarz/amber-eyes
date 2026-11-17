# KỊCH BẢN TRAILER KÊNH — CONCEPT A "SỢI CHỈ ĐỎ" (bản VN)

*Ngày: 16/11/2026 · Thời lượng: 50,0 s · 1920×1080@30 · H.264+AAC*
*Vai giọng: **H (Cú / Host)** — `English_CaptivatingStoryteller`, speed base 0,90 (bộ A, `edition.py`)*
*Toàn bộ chữ trên màn hình do **Pillow vẽ**, AI KHÔNG vẽ chữ (bẫy A11 #87).*

> **Trạng thái 16/11/2026:** đã dựng **bản VN** (`assets/brand/trailer_kenh_A_vn.mp4`) và **bản EN** (`assets/brand/trailer_kenh_A_en.mp4`).
> Bản EN dùng cùng timeline, đổi 3 thứ: lời đọc + giọng (`English_magnetic_voiced_man` 0,95) · tagline EN · nhãn vai EN (HOST / INVESTIGATOR / PSYCHOLOGIST) · thẻ miễn trừ EN ("ABOUT THIS VIDEO").
> Chạy lại: `AE_LANG=en py -3 .work/make_trailer.py` → `AE_LANG=en py -3 .work/make_trailer_audio.py`.

> **Lớp video động (thêm 16/11/2026):** 4 đoạn nền tĩnh đã được **AI hoạt họng** bằng MiniMax **Hailuo-2.3** ở chế độ **first-frame** — lấy chính nền gốc làm khung đầu nên chất đồ hoạ khớp 100 % và **không có chữ AI**.
> Nguồn clip: `videos/soi-chi-do-hook.mp4` · `videos/bang-ho-so-chay.mp4` · `videos/phong-tham-van-mo.mp4` · `videos/hanh-lang-dem.mp4` (mỗi clip 5,88 s, 1080P, **không có tiếng**).
> Bản chuẩn hoá cho pipeline: `.work/trailer_a/h23_norm/<tên>.mp4`. Muốn quay lại bản ảnh tĩnh: xoá thư mục `h23_norm` rồi chạy lại `make_trailer.py`.

---

## 1. Timeline 50,0 s

| # | Mốc | Hình | VO (mã câu) | Nguồn hình |
|---|---|---|---|---|
| 1 | 0,0–4,6 | Nền tối có sương. Sợi chỉ đỏ vẽ tay (0–1,4 s) → đôi mắt hổ phách bừng sáng (1,35–1,5 s) → logo tan dần (4,0–4,6 s). | — | `assets/bg/void.png` + **procedural** (tái dùng `make_intro.build_logo_layers()`) |
| 2 | 4,6–10,6 | Bảng ghim đầy giấy, có sợi chỉ đỏ. 5 thẻ giấy "HỒ SƠ" lần lượt xuất hiện (5,6 / 6,6 / 7,6 / 8,6 / 9,6 s) — số 01 · 07 · 12 · 19 · 29. | **T-01** 5,2 | `assets/bg/pinboard.png` |
| 3 | 10,6–16,6 | Bàn podcast đèn ấm. Cú (H) bán thân lớn góc phải, nhãn "DẪN CHUYỆN". | **T-02** 11,2 | `assets/bg/podcast_desk.png` + `assets/cast/H/P1.png` |
| 4 | 16,6–22,6 | Phòng thẩm vấn, đèn lạnh. Sói (D) bán thân góc phải, nhãn "ĐIỀU TRA VIÊN". | **T-03** 17,2 | `assets/bg/interrogation.png` + `assets/cast/D/P1.png` |
| 5 | 22,6–28,6 | Bàn DSM-5, tông tím. Cáo (C) bán thân góc phải, nhãn "CHUYÊN GIA TÂM LÝ". | **T-04** 23,2 | `assets/bg/brain_desk.png` + `assets/cast/C/P1.png` |
| 6 | 28,6–34,6 | Hành lang tối. Cả 3 vai nhỏ ở 3 góc (Cú · Sói · Cáo). | **T-05** 29,2 | `assets/bg/corridor.png` + H/D/C |
| 7 | 34,6–38,6 | Thẻ giấy "VỀ NỘI DUNG NÀY" (3 dòng miễn trừ, đúng bản trong bumper). | — | **procedural** (`make_intro.card_base`) |
| 8 | 38,6–46,4 | End card: logo + wordmark "AMBER EYES" + tagline + dòng số liệu. | **T-06** 39,4 | `assets/bg/void.png` + `assets/brand/*` |
| 9 | 46,4–50,0 | Fade đen, logo nhỏ + watermark ở góc. | — | procedural |

---

## 2. Lời dẫn (VN) — 6 câu, **một vai duy nhất** (Host)

> Luật G1: KHÔNG `...`, KHÔNG thẻ `<#s#>` giữa câu · G3: chỉ `neutral|sad|fearful|surprised` · G5: pitch = 0 · G4: speed lệch base trong −0,06…+0,02

| Mã | Lời đọc | Emotion | Speed | Ghi chú |
|---|---|---|---|---|
| T-01 | Mỗi vụ án bắt đầu bằng một câu hỏi đơn giản. | neutral | 0,90 | base |
| T-02 | Nhưng câu trả lời không nằm ở hiện trường. | neutral | 0,88 | trầm xuống |
| T-03 | Nó nằm ở cách kẻ gây án nhìn nạn nhân. | neutral | 0,92 | dứt khoát hơn |
| T-04 | Và ở cách hắn biện minh cho chính mình. | neutral | 0,90 | base |
| T-05 | Hồ sơ có thật. Phân tích có căn cứ. | neutral | 0,88 | chắc, chậm |
| T-06 | Amber Eyes. Phân tích tâm lý tội phạm qua những hồ sơ có thật. | neutral | 0,90 | base |

**Chỉ dùng 1 vai ⇒ không có rủi ro G9/G10 (tách bạch vai) và không dính điểm yếu CER 3,1 % của vai Sói.**

### 2.1 Bản EN (dựng sau, cùng timeline, chỉ đổi lời + giọng `English_magnetic_voiced_man` 0,95)

| Mã | EN | Speed |
|---|---|---|
| T-01 | Every case begins with a simple question. | 0,95 |
| T-02 | But the answer is not at the scene. | 0,93 |
| T-03 | It is in how the killer sees the victim. | 0,97 |
| T-04 | And in how he justifies himself. | 0,95 |
| T-05 | Real case files. Grounded analysis. | 0,93 |
| T-06 | Amber Eyes. Criminal psychology through real case files. | 0,95 |

---

## 3. Âm thanh

| Lớp | Nguồn | Cách dùng |
|---|---|---|
| VO | MiniMax TTS (`connector__matrix__batch_text_to_audio`), giọng Host | 6 câu, đặt đúng mốc bảng 1 |
| Nhạc | `assets/bgm/bgm_music_box.mp3` (22,4 s) lặp 3 lần, crossfade 1,2 s | −17 dB so với VO |
| Nền | `assets/bgm/bgm_sub_drone.mp3` (30,5 s) lặp 2 lần | −21 dB, fade 0→3 s và 46→50 s |
| SFX | `folder_close.wav` @4,5 s · `card_flip.wav` @10,5 / 16,5 / 22,5 s | −14 dB, đánh dấu chuyển cảnh |
| Chuẩn hoá | `loudnorm I=-16 TP=-1,5 LRA=11`, 2 lượt, `latency=1`, `alimiter` trước khi mã hoá | Đo lại LUFS/peak trên mp4 cuối |

**V4:** không đoạn nào câm tuyệt đối > 0,3 s (nhạc + drone phủ liên tục).

---

## 4. Chữ trên màn hình (đều do Pillow vẽ)

| Vị trí | Nội dung | Font | Vì sao an toàn |
|---|---|---|---|
| End card | `AMBER EYES` | Georgia | **không dấu** → Georgia đủ 92 ký tự còn thiếu |
| End card | Tagline VN | Segoe UI (qua `make_logo.tagline`) | Georgia thiếu ký tự tiếng Việt |
| End card | `29 HỒ SƠ · 5 VAI CHÍNH · 4 NGÔN NGỮ` | Segoe UI Semibold, letterspace | số liệu đúng theo repo |
| Góc trái các beat 3–6 | `DẪN CHUYỆN` / `ĐIỀU TRA VIÊN` / `CHUYÊN GIA TÂM LÝ` | Segoe UI Semibold 34 px | có lớp tối mờ (scrim) ⇒ tương phản H9 đạt |
| Thẻ giấy beat 2 | `01` `07` `12` `19` `29` | Consolas / Bahnschrift | giấy sáng + chữ tối ⇒ tương phản tự đạt |

---

## 5. Cổng QC phải đạt trước khi giao

| Cổng | Ngưỡng | Cách đo |
|---|---|---|
| Thời lượng | 50,0 s ± 0,05 s | `ffprobe` trên master mp4 |
| Lệch hình/tiếng | ≤ 0,05 s | so mốc VO với `timeline` |
| Âm lượng | −16 LUFS ± 1, TP ≤ −1,5 dBFS | `ffmpeg` loudnorm print_format=json |
| Khoảng câm | 0 đoạn > 0,3 s @ −60 dB | `qc_pause_gate.py` |
| Chữ chìm (H9) | 0 shot chữ chìm | đo tương phản từng vùng chữ trên nền thật |
| Lỗi giải mã | 0 | `ffmpeg -v error -i master.mp4 -f null -` |
| Provenance | mọi tài sản AI có dòng | `provenance.json` |

> Vì bản này **không sinh ảnh/video AI mới**, không phát sinh dòng provenance mới; nếu sau này nâng cấp bằng MiniMax/H3 thì bắt buộc ghi.
