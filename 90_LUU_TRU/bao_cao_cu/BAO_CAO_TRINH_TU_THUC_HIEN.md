# BÁO CÁO TRÌNH TỰ THỰC HIỆN — TẬP 01 "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ"

**Dự án:** Truyền Thuyết Lĩnh Nam · Văn Lang — 12 Sứ Quân
**Nguồn:** `KeHoach_ThuAm_Tap01.md` (v2) + `KeHoach_ThuAm_Tap01_VIDEO.md` (v4)
**Ngày:** 21/10/2026
**Trạng thái:** Hoàn thành, đã kiểm chứng bằng đo đạc
**Báo cáo tổng quan:** `BAO_CAO_TAP01.md` (tài liệu này là bản **trình tự** chi tiết)

---

## 0. NGUYÊN TẮC SẮP XẾP: AUDIO TRƯỚC, TÍNH FRAME SAU, GHÉP VIDEO CUỐI

Trình tự không phải do thói quen mà do **phụ thuộc dữ liệu**:

```
        ┌─────────────────────────────► THỜI LƯỢNG THẬT ◄─────────────────────────┐
        │                                                                      │
  [A] BÓC PLAN ──► [B] TTS ──► [C] GHÉP 3 TRACK ──► [D] MIX + LOUDNORM ──► [E] ĐO LẠI
        (plan)      (64 MP3)     (voice/bed/cue)      (Kc_1_Tap01.mp3)    (timeline.json)
                                                                                   │
                            ┌──────────────────────────────────────────────────────┘
                            ▼
        [F] TÍNH FRAME ──► [G] DỰNG 62 SHOT ──► [H] CHIA 13 CHUNK ──► [I] RENDER ──► [J] CONCAT + MUX
        (1025,97 s × 30)     (2400×1350 PNG)      (~80 s/chunk)         (13 file)      (Kc_1_Tap01.mp4)
```

**Lý do bắt buộc phải làm audio trước:**

Plan chỉ ghi cột `THỜI LƯỤNG` là **ước lượng** của người viết (plan tính 1055 s, thực tế
933 s — sai 11 %). Nếu dựng video trước rồi ghép audio sau, mọi lần cắt cảnh, mọi chuyển
động sẽ phải làm lại. Ngược lại, nếu đo audio trước thì **thời lượng thật trở thành
nguồn chân lý duy nhất** và toàn bộ video chỉ cần bám theo.

> **Chuẩn dự án (từ R7 của plan video):** *"Chuyển động phải theo thời lượng đo thật
> (`timeline.json`), không dùng ước lượng."* — Trong pipeline này, **không một con số
> thời lượng nào** đến từ cột ước lượng của plan.

---

## GIAI ĐOẠN 0 — CHUẨN BỊ MÔI TRƯỜNG

| Việc | Kết quả |
|---|---|
| Tải ffmpeg n9.0 (bản LGPL có `libopenh264`) | `.work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/` |
| Python + Pillow + numpy | Python 3.14.3 · Pillow 12.2.0 · numpy 2.4.6 |
| Benchmark encoder | `.work/bench/` — thử `h264_qsv`, `libopenh264`, `libvpx-vp9`, `mpeg4` |
| **Kết luận benchmark** | Chọn `libopenh264` (plan yêu cầu). Bản này **không có `libx264`**, và **bỏ qua `-q:v`** → phải ép bằng `-b:v` |

**Biến môi trường bắt buộc trên Windows:**

```powershell
$env:PYTHONIOENCODING='utf-8'   # nếu thiếu, console cp1252 crash khi in tiếng Việt
```

---

## GIAI ĐOẠN A — TẠO AUDIO (6 bước)

### A1 · Bóc plan → cấu trúc dữ liệu

```powershell
python .work\parse_plan.py
```

- **Input:** `KeHoach_ThuAm_Tap01.md` (bảng lời + nhạc + SFX + nghỉ)
- **Output:** `.work/blocks.json` — **89 block**, mỗi block có `ma`, `loại`, `giong`,
  `section`, `start`, `end`, `dur`, `planned`, `text`
- **Phân loại:** 58 `LỜI` · 9 `SFX` · 3 `NHẠC` · 19 `NGHỈ`
- **Ràng buộc R2:** 5 ô `CẦN VIẾT` (`1.9`, `2.18`, `3.10`, `4.16`, `5.14`) bị loại
  trọn — **không bịa nội dung**
- **Tự kiểm R1 ngay trong lúc bóc:** `**text**` → giữ text bỏ `*`; xoá mọi `*DẪN: ...*`;
  bỏ `` ` ``, `▸`, `[`, `]`, `#`. Kết quả: **0 lỗi markup**

### A2 · Chuẩn bị payload TTS

```powershell
python .work\make_tts_args.py
```

- **Output:** `.work/tts/batch_01..07.json` + `manifest.json`
- **Số request:** **64** = 58 block lời + **6 lần tách** khi gặp dấu `▸` trong `A→B`
  (tại `1.4`, `3.7`, `4.6`, `4.15`, `5.3`, `5.13`)
- **Mỗi lệnh gọi tối đa 10 request** (giới hạn connector) → 7 batch
- **Thông số giọng (R4):** A = `audiobook_male_1`/neutral/0,90 · B = `audiobook_female_1`/sad/0,88
  · pitch 0 · volume 1,0. Block `5.6` có cờ `B ★` = toàn bộ giọng B

### A3 · Sinh & tải audio

```
mcode-tools connector call connector__matrix__batch_text_to_audio --args-file .work\tts\batch_0N.json
```

- **7 lệnh gọi** → `.work/audio/*.mp3` (64 file, **14.993.280 byte**)
- **Kết quả: 64/64 thành công, 0 failed**
- Định dạng đo bằng ffprobe: `mp3 · 32000 Hz · mono · 128 kbps`

### A4 · Ghép 3 track riêng (chưa mix)

```powershell
python .work\build_audio.py
```

Script dựng **3 track WAV riêng biệt** rồi mới mix — để mỗi thành phần kiểm soát
mức độc lập và không lẫn tiếng:

| Track | Số phần | Nội dung | Cách dựng |
|---|---:|---|---|
| `voice_master` | 93 | lời TTS + **im lặng thật** cho `NGHỈ`/`SFX`/`NHẠC` | `anullsrc=r=32000:cl=mono` (R6: tuyệt đối không dùng "...") · khe 0,30 s giữa 2 nửa `A→B` |
| `bed_master` | 108 | BGM theo hồi, loop liền mạch có wrap | −26 dB khi có lời / −14 dB dạo chuyển · mute đúng 4 block "im lặng tuyệt đối" |
| `cue_master` | 81 | 3 cue nhạc, nguồn chồng lấp trong block | `adelay` theo offset · `5.21` có fade-out |

### A5 · Mix + chuẩn hoá loudness

Trong cùng `build_audio.py`:

```
[voice][bed] amix=inputs=2:duration=longest:normalize=0 [m]
[m][cue]    amix=inputs=2:duration=first:normalize=0   [mx]
[mx] loudnorm=I=-16:TP=-1.5:LRA=11 [out]
```

- `normalize=0` là bắt buộc — nếu không, `amix` tự chia sẻ mức và nhạc bị hạ dưới lời
- `duration=first` ở lớp cuối để **độ dài file = độ dài track lời**
- **Output:** `D:\TEST\Gax\Audi\Kc_1_Tap01.mp3` — 20.520.044 B · 1025,95 s · 48 kHz stereo 160 kbps
- **Đo loudness thật:** **−16,3 LUFS** · TP **−1,7 dBTP** · LRA 5,1 LU
- **Kiểm tra drift:** lệch max giữa 3 track = **0,010 s** ⇒ không có đoạn nào lệch tiếng

### A6 · ĐO LẠI TOÀN BỘ → timeline

> **Đây là bước bắt nguồn cho toàn bộ video.**

ffprobe từng file audio đã ghép → `.work/timeline.json`:

- **89 block**, mỗi block có `start` / `end` / `dur` / `planned` (planned = ước lượng
  của plan, dur = thực tế)
- **Tổng thực tế: 1025,973 s**
- So sánh: plan ước lượng **1055 s** vs thực tế **933 s** (theo cột plan) → **sai ~11 %**

### A7 · Báo cáo lệch thời lượng (không tự sửa)

```powershell
python .work\deviation_report.py
```

- **42/58 block lời lệch >5 %** so với cột `THỜI LƯỤNG` của plan
- Lệch lớn nhất: `O.4` **+77,4 %** · `3.18` +60,0 % · `3.3` −47,9 % · `1.12` −38,2 % · `5.7` +38,3 %
- **Không tự sửa** (theo R10 của plan audio) — báo lại để người duyệt quyết định
- Bảng đầy đủ: `.work/duration_deviations.md`

> **Điểm mấu chốt:** video sau đó dựng theo `timeline.json` (**đo thật**), không theo
> cột ước lượng. Người xem nghe thấy đúng những gì màn hình đang diễn ra.

---

## GIAI ĐOẠN B — TÍNH FRAME & DỰNG ĐỒ HOẠ (4 bước)

### B1 · Ngân sách frame tổng

```
Tổng thời lượng đo thật = 1025,973 s
FPS = 30
Tổng frame = 1025,973 × 30 = 30.779 frame
```

Sau khi cắt chunk và mux, file cuối đo được:

| Stream | Thời lượng | Số frame/gói |
|---|---:|---|
| Video | 1026,1333 s | **30.784 frame** |
| Audio (AAC) | 1025,9462 s | 48.093 gói |
| Container | 1026,1333 s | — |

Chênh **+0,16 s / +5 frame** là do sai số cắt chunk và padding AAC — **không rơi frame**:
decode toàn file cho **exit 0, 0 lỗi, đúng 30.784 frame**.

### B2 · Frame riêng cho từng shot + tốc độ zoom

```python
frames = max(2, int(dur * FPS))          # dur = thời lượng shot (s)
step   = (ZOOMMAX - 1.0) / frames        # ZOOMMAX = 1.045
```

Ý nghĩa: **shot dài ⇒ zoom chậm hơn**, để mọi shot đều có biên độ chuyển động như
nhau trong thời gian của nó.

| Chỉ số | Giá trị |
|---|---|
| Shot ngắn nhất | **123 frame** |
| Shot dài nhất | **1.368 frame** |
| Shot trung bình | 497 frame |

Biểu thức zoom **xen kẽ vào/ra** để tránh cảm giác máy móc:

```
shot chẵn : z = min(1 + step*on, 1.045)      # zoom vào
shot lẻ   : z = max(1.045 - step*on, 1.000)  # zoom ra
x = 'iw/2-(iw/zoom/2)'   y = 'ih/2-(ih/zoom/2)'   s = 1920x1080   fps = 30
```

> Ví dụ thật từ `.work/_fg2_05.txt`:
> `zoompan=z='max(1.045-0.00012397*on,1.0)'` — shot 12,100 s ⇒ 363 frame ⇒ step 0,000124.

### B3 · Ánh xạ block → shot (62 shot)

```powershell
python .work\build_shots.py
```

- **Input:** `.work/timeline.json` + danh sách `SHOTS` trong `build_shots.py`
- **Output:** `assets/gfx2/shots/*.png` — **63 file** (62 shot + `bg_solid.png`), mỗi file
  **2400×1350 toàn mảnh** + `.work/shots.json`
- **Bộ dựng:** `.work/shotlib.py` (hiệu ứng) + `.work/scenes.py` (**15 cảnh nền**) +
  `.work/layouts.py` (**3 bố cục A/B/C**)

| Bố cục | Số shot | Dùng ở hồi |
|---|---:|---|
| **A** — toàn mản (chữ lớn đè lên cảnh) | 36 | h3, h5, mở đầu |
| **B** — thẻ kính (thẻ 280–1700, cảnh lộ bên phải) | 17 | h1, h4 |
| **C** — chia đôi (anchor trái + panel chữ phải) | 9 | h2 |

**Độ phủ đo được:**

| Chỉ số | Giá trị |
|---|---|
| Tổng thời lượng có hình | **989,96 s / 1025,97 s = 96,5 %** |
| Số khoảng trống còn lại | **17 khoảng** >0,05 s (tổng 33,01 s) + 3 khoảng ≤0,05 s |
| Khoảng trống nằm trong block `NGHỈ` | **17/17** ✅ |

### B4 · Kiểm chứng "không cắt vạch giữa lời"

Đây là ràng buộc khó nhất của plan video (R8/R9). Đo bằng script
`.work/_seq_cuts.py` — dựng lại đúng công thức cửa sổ chuyển cảnh của
`build_video2.gaps_and_windows()` rồi tra block `NGHỈ`/`LỜI` tại đúng thời điểm đó:

```
gap giữa 2 shot:  e = shot[i].end ,  g = shot[i+1].start − e
cửa sổ dissolve:  bắt đầu tại ws = e + g×0,1 ,  kéo dài d = min(2,0 , g×0,8)
```

| Kết quả | Số liệu |
|---|---|
| Ranh giới shot nằm trong block `LỜI` | **0 / 17** ✅ |
| **Bắt đầu** cross-dissolve nằm trong block `LỜI` | **0 / 17** ✅ |
| **Kết thúc** cross-dissolve nằm trong block `LỜI` | **0 / 17** ✅ |

> **Ghi chú công bằng:** 7 khoảng trống *khoảng thời gian* có chạm vào đuôi một block
> `LỜI` (ví dụ gap 02: 121,92 → 124,42 s, chạm `1.5`). Nhưng **thời điểm chuyển cảnh
> thật** (lúc dissolve bắt đầu, 122,17 s) đã nằm sau khi block `1.5` kết thúc — tức
> **hình ảnh vẫn thay đổi trong im lặng**, không cắt vạch giữa lời. Đây là điểm cần
> nói rõ vì báo cáo tổng quan ghi "18 khoảng" — số đo đúng sau khi kiểm lại là
> **17 khoảng ≥0,05 s**.

---

## GIAI ĐOẠN C — GHÉP VIDEO (5 bước)

```powershell
$env:AUDI_VBR='1500'; $env:AUDI_NOISE='2'; $env:AUDI_MOVE='zoom'
python .work\build_video2.py
```

### C1 · Chia 13 chunk (~80 s/chunk, cắt đúng ranh giới shot)

```python
target = 80.0
acc += SHOTS[i]["end"] - SHOTS[i]["start"]
if acc >= target: bounds.append(SHOTS[i]["end"]); acc = 0
```

> **Không cắt vạch giữa shot** — ranh giới chunk luôn trùng ranh giới shot, nên
> không có lần cắt nào chẻ ngang một chuyển động đang chạy.

### C2 · Sinh filtergraph cho từng chunk

Mỗi chunk ghi ra `.work/_fg2_NN.txt` (UTF-8 **không BOM**) rồi gọi ffmpeg bằng
`-/filter_complex <file>` — né giới hạn 32 KB của dòng lệnh Windows.

Thứ tự filter trong mỗi lớp shot (bắt buộc):

```
loop=loop=-1:size=1:start=0 , setpts=N/(30*TB) , trim=duration=… ,
zoompan=… , format=rgba ,
fade=t=in , fade=t=out
```

> **BẪY ĐÃ GẶP:** thứ tự phải là **`fade → trim → setpts`**. Nếu `setpts` đặt trước
> `trim` thì timeline lệch → video lệch tiếng. Đồng thời dùng bộ lọc `loop` thay cho
> `-loop 1` (vì `-loop 1` giải mã lại file PNG **30 lần/giây**).

### C3 · Render 13 chunk

| Chunk | Khoảng thời gian | Dài | Render | Dung lượng |
|---|---|---:|---:|---:|
| 00 | 0 – 82,54 | 82,54 s | 88,2 s | 3.395.048 B |
| 01 | 82,54 – 176,59 | 94,05 s | 112,2 s | 3.422.822 B |
| 02 | 176,59 – 276,36 | 99,78 s | 114,6 s | 3.978.789 B |
| 03 | 276,36 – 383,05 | 106,69 s | 119,6 s | 3.289.187 B |
| 04 | 383,05 – 468,69 | 85,63 s | 109,7 s | 3.203.377 B |
| 05 | 468,69 – 566,03 | 97,35 s | 112,2 s | 5.305.116 B |
| 06 | 566,03 – 652,26 | 86,23 s | 97,5 s | 3.422.885 B |
| 07 | 652,26 – 706,95 | 54,69 s | 59,2 s | 2.856.830 B |
| 08 | 706,95 – 756,92 | 49,97 s | 55,0 s | 2.682.727 B |
| 09 | 756,92 – 842,16 | 85,24 s | 100,6 s | 3.264.953 B |
| 10 | 842,16 – 932,09 | 89,93 s | 99,2 s | 3.892.643 B |
| 11 | 932,09 – 1017,97 | 85,88 s | 95,0 s | 3.627.342 B |
| 12 | 1017,97 – 1025,97 | 8,00 s | 9,2 s | 1.314.219 B |

- **Tổng thời gian render: 1171 s cho 1026 s video = 0,88× realtime**
- Vì sao chia chunk: 1 pass chứa 60+ overlay chạy **5× chậm realtime** và ngốn **3,2 GB RAM**

### C4 · Ghép chunk + hạt phim phim cuối

```
ffmpeg -f concat -safe 0 -i .work/video/concat.txt -c copy .work/video/video_only2.mp4
```

> `-c copy` (không encode lại) nên **không mất chất lượng** và nhanh.

### C5 · Mux audio + xuất bản cuối

```
ffmpeg -i .work/video/video_only2.mp4 -i Kc_1_Tap01.mp3 \
       -map 0:v -map 1:a -c:v copy -c:a aac -b:a 160k -movflags +faststart \
       Kc_1_Tap01.mp4
```

- `-c:v copy` giữ nguyên dòng video · `-movflags +faststart` để stream được chơi ngay
- **Output:** `D:\TEST\Gax\Audi\Kc_1_Tap01.mp4` — 64.633.138 B (61,6 MiB) ·
  1920×1080@30 yuv420p · video 339 kbps · audio 157 kbps

---

## GIAI ĐOẠN D — KIỂM CHỨNG (5 bước)

| Bước | Lệnh | Kết quả đo |
|---|---|---|
| D1 | `python .work\verify.py` | duration/size/codec/bitrate + loudness đều đạt · contact sheet 23 frame → `.work/gfx/_final_sheet.png` |
| D2 | `ffmpeg -i Kc_1_Tap01.mp4 -f null -` | **exit 0, 0 lỗi, đúng 30.784 frame** (không rơi khung) |
| D3 | `python .work\compare_before_after.py` | median mực **2,4 % → 19,3 % (×7,9)** · thời lượng chết **57,5 % → 16,4 %** |
| D4 | `python .work\dead_zone_map.py` | **83,6 %** thời lượng có nội dung thật; 16,2 % còn lại là cảnh tối có chủ đích (đã xem mắt, chữ vẫn rõ) |
| D5 | Kiểm file nguồn | 4 file nguồn giữ nguyên timestamp — **không ghi đè** |

---

## VÒNG LẶP SỬA — TRÌNH TỰ THỰC TẾ TRONG PHIÊN LÀM VIỆC

Trình tự trên là trình tự **đúng**. Nhưng trong thực tế đã có **một vòng dựng lại toàn bộ
lớp hình ảnh**, và đây là phần quan trọng nhất của báo cáo:

| Lượt | Việc | Kết quả |
|---|---|---|
| 1 | Chạy trọn GIAI ĐOẠN 0 → A → B → C với `build_gfx.py` (69 PNG lớp) + `build_video.py` | Ra video **43,0 MiB** — bị đánh giá **"đơn điệu, thiếu sức hút"** |
| 2 | **Đo thay vì đoán**: `ink_profile.py` (513 mẫu, mỗi 2 s) + `diagnose_monotony.py` + `bbox_report.py` | median mực **2,4 %** · 57,5 % thời lượng chết · chuyển động thật chỉ **28,6 %** · K8 xfade = 0 % · `bg_base.png` trong suốt hoàn toàn |
| 3 | Kết luận + 3 prototype (`A_toan_man` / `B_the_kinh` / `C_chia_doi`) | Lỗi ở **MÔ TẢ HÌNH ẢNH**, không phải nội dung. User chọn **trộn cả 3 theo từng hồi** |
| 4 | Dựng lại **GIAI ĐOẠN B** (15 cảnh + 3 layout + 62 shot) | phủ hình 96,5 %, 17 khoảng trống đều trong `NGHỈ` |
| 5 | Dựng lại **GIAI ĐOẠN C** (13 chunk) + render lại 4 chunk dùng cảnh `casefile` | median mực **×7,9** · chuyển động **100 %** · 61,6 MiB |

> **Bài học:** GIAI ĐOẠN A (audio) **được giữ nguyên 100 %** — không phải làm lại lần
> nào. Toàn bộ thời gian sửa nằm ở GIAI ĐOẠN B và C. Đây chính là giá trị của việc
> **đo trước, dựng sau**: chỉ phần hình ảnh phải làm lại, phần âm thanh không đụng tới.

---

## BẢNG TỔNG HỢP THỜI GIAN & DUNG LƯỢNG

| Hạng mục | Giá trị |
|---|---|
| Số lệnh/script tạo ra | 24 file `.py` trong `.work/` |
| Tổng MP3 TTS | 64 file · 14.993.280 B |
| Audio master | 20.520.044 B (19,6 MiB) · 1025,95 s |
| Đồ hoạ | 63 PNG 2400×1350 · 14,87 MB |
| Render video | 13 chunk · 1171 s · 0,88× realtime |
| Video master | 64.633.138 B (61,6 MiB) · 1026,13 s |
| Báo cáo tổng quan | `BAO_CAO_TAP01.md` · 28.225 B |
| Báo cáo trình tự (tài liệu này) | `BAO_CAO_TRINH_TU_THUC_HIEN.md` |

---

## RUNBOOK — TÁI LẬP CHO TẬP 2–10

### Thứ tự chạy (giữ nguyên)

```powershell
cd 'D:\TEST\Gax\Audi'
$env:PYTHONIOENCODING='utf-8'

# GIAI ĐOẠN A — AUDIO
python .work\parse_plan.py
python .work\make_tts_args.py
# 7 lệnh TTS (KHÔNG chạy lại nếu MP3 đã có)
python .work\fetch_audio.py
python .work\build_audio.py
python .work\deviation_report.py

# GIAI ĐOẠN B — TÍNH FRAME + ĐỒ HOẠ
python .work\build_shots.py

# GIAI ĐOẠN C — GHÉP VIDEO
$env:AUDI_VBR='1500'; $env:AUDI_NOISE='2'; $env:AUDI_MOVE='zoom'
python .work\build_video2.py

# GIAI ĐOẠN D — KIỂM CHỨNG
python .work\verify.py
```

### Biến môi trường

| Biến | Mặc định | Ý nghĩa |
|---|---|---|
| `AUDI_ONLY` | (trống) | Render lại đúng chunk, ví dụ `AUDI_ONLY="1,2,3,7"` — **dùng để sửa cục bộ** |
| `AUDI_VBR` | 1500 | Bitrate video (kbps). `libopenh264` **bỏ qua `-q:v`** nên đây là đòn bẩy duy nhất |
| `AUDI_NOISE` | 2 | Hạt phim `noise=alls`. Đo được: 4 → 1258 kbps, 3 → 660, **2 → 278** |
| `AUDI_MOVE` | `zoom` | `zoom` hoặc `pan` (camera trượt ngang) |

### Thay đổi cho tập mới

Chỉ cần sửa **3 chỗ**:

1. `KeHoach_ThuAm_TapXX.md` — nội dung mới (bóc tự động)
2. Danh sách `SHOTS` trong `.work/build_shots.py` — mỗi shot là 1 block lời
3. `SCENES` trong `.work/scenes.py` nếu cần cảnh nền mới

Cấu trúc một shot:

```python
S(id="h2b", ma="2.4", end="2.4", f1=0.5, L="C", sc="casefile",
  anch="doc", chap="h2",
  label="HỒ SƠ Y TẾ",
  headline="1991 — SINH RA,\nHOÀN TOÀN KHỎE MẠNH",
  sub="Một đứa trẻ bình thường, không có gì bất thường.")
```

| Field | Ý nghĩa |
|---|---|
| `ma` / `end` | Block đầu – block cuối trong timeline |
| `f0` / `f1` | Tách block dài thành 2 shot (tỉ lệ 0–1) |
| `L` | Bố cục: `A` / `B` / `C` |
| `sc` | Tên scene trong `scenes.py` (15 cảnh) |
| `anch` | Chủ thể: `house` / `doc` / `medical` / `storm` / `brain` / `phone` / `money` / `chains` / `bars` |
| `label` / `headline` / `sub` | Nội dung chữ (đo bề rộng bằng PIL để canh giữa) |
| `big` | Chữ số lớn: `"03"` / `"10"` / `"?"` |
| `chap` | Hồi (dùng để bố trí xen kẽ A/B/C) |

---

## PHỤ LỤC — CÁC BẪY ĐÃ GẶP (ĐỪNG THỬ LẠI)

| # | Bẫy | Hệ quả | Cách xử lý |
|---|---|---|---|
| 1 | `Image.composite(color, black, mask)` của Pillow **trả ảnh MỚI, thay thế toàn bộ nền** | 15 cảnh nền ra "tối đen" trơn, mất nội dung | Viết hàm `glow(base, ...)` **hòa sáng vào** nền |
| 2 | `house_flat.png` có **nền đục sẵn** | Paste đè lên trời làm mất cảnh | Dùng làm nền rồi cắt/dịch sang phải (`_house(shift=400, zoom=1.35)`) |
| 3 | `portrait.png` thực ra là **thẻ hồ sơ có chữ**, không phải silhouette | Không dùng được làm chân dung | Vẽ tay trong `sc_portrait()` |
| 4 | Cầu nối MCP của EffectCraft **âm thầm bỏ tham số số** (`layer.newText` từ chối `size`; `comp.new` bỏ `duration`/`frameRate`; `app.executeCommand` bỏ toàn bộ params) | Không đặt được cỡ chữ/màu/kiểu chữ | **Dùng Pillow** cho đồ hoạ + **ffmpeg `drawtext`** cho mọi chữ |
| 5 | `libopenh264` **bỏ qua `-q:v`** (thử 5/8/12 → 3 file byte-identical) | Không kiểm soát được dung lượng | Ép bằng `-b:v <kbit> -maxrate -bufsize` |
| 6 | Hạt phim `noise=alls` ăn **4,5× bitrate** | 133,8 MB nếu giữ mức 4 | `AUDI_NOISE=2` → 43,0 MB, chữ sạch hơn |
| 7 | `rgbashift ±2` tạo viền đỏ/cyan lộ trên chữ trắng | Lỗi thị giác rõ | Hạ xuống `±1` |
| 8 | `crop` của ffmpeg **không có option `eval`** | Biểu thức không animate được | Trượt bằng biểu thức `x` của `overlay` |
| 9 | `fontfile` trên Windows **phải escape dấu `:`** | "No option name near …" | `fontfile='C\:/Windows/Fonts/segoeuib.ttf'` |
| 10 | File filter > 32 KB | Vượt giới hạn dòng lệnh Windows | `-/filter_complex <file>`, file **UTF-8 không BOM** |
| 11 | `Set-Content -Encoding UTF8` (PowerShell 5.1) **thêm BOM** | `SyntaxError: invalid non-printable character U+FEFF` | Gỡ BOM bằng Python |
| 12 | `-replace` trong PowerShell biến `` `n `` thành ký tự literal | Hỏng file | Dùng Edit tool |
| 13 | `Tee-Object` ghi UTF-16 (BOM) | JSON đọc hỏng | Đọc JSON bằng detector BOM |
| 14 | `mcode-tools` là `.cmd` | Gọi trực tiếp trong PowerShell lỗi | Gọi qua `["cmd","/c","mcode-tools",…]` |
| 15 | `shade()` cần gradient rộng = `im.width` | `IndexError` khi tạo gradient 1 px | Luôn dùng `Image.new("L",(im.width, h))` |
| 16 | Layout C dùng key `anchor`, shot list dùng `anch` | KeyError | Hỗ trợ **cả hai** |
| 17 | Thứ tự filter phải là `fade → trim → setpts` | Lệch timeline ⇒ lệch tiếng | Cố định thứ tự này |
| 18 | **Metric mực đếm thiếu chữ mảnh** (chữ trắng 66 px trên nền tối chỉ ~1 % khung) | Số liệu có vẻ đẹp nhưng hình vẫn đơn | **Phải xem mắt từng frame**, không chỉ nhìn số |
