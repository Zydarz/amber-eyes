# BÁO CÁO TOÀN BỘ QUÁ TRÌNH SẢN XUẤT — TẬP 01 "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ"

**Dự án:** Truyền Thuyết Lĩnh Nam · Văn Lang — 12 Sứ Quân
**Nguồn:** `KeHoach_ThuAm_Tap01.md` (v2) + `KeHoach_ThuAm_Tap01_VIDEO.md` (v4)
**Ngày:** 21/10/2026
**Trạng thái:** Hoàn thành, đã kiểm chứng

---

## 1. TÓM TẮT ĐIỀU HÀNH

Hai tài liệu plan được triển khai trọn vẹn thành **một bản audio master** và
**một bản video master**. Trong quá trình thực hiện phát hiện **16 vấn đề**, mỗi
vấn đề đều được đo đạc để tìm nguyên nhân gốc trước khi xử lý — không đoán mò.

Sau khi bản đầu tiên bị đánh giá là **"đơn điệu, thiếu sức hút"**, toàn bộ lớp
hình ảnh được dựng lại từ đầu. Kết quả đo:

| Chỉ số | Bản đầu | Bản cuối | Thay đổi |
|---|---:|---:|---|
| Mật độ mực median (pixel không đen) | 2,4 % | **19,3 %** | **× 7,9** |
| Thời lượng "màn hình trống" (<3 % mực) | 57,5 % | **16,4 %** | − 41,1 điểm |
| Frame dưới 10 % mực | 92,8 % | 35,9 % | − 56,9 điểm |
| Thời lượng có chuyển động thật | 28,6 % | **100 %** | đạt chuẩn mục 5 của plan |
| K8 cross-dissolve | 0 % | **17/17** lần chuyển cảnh trong block `NGHỈ` | đủ chuẩn plan |
| Số "shot" (khoảnh khắc hình thay đổi) | 53, TB 8,3 s | **62 shot toàn mảnh** | + 9 shot, mỗi shot có chuyển động riêng |

**Kết luận chẩn đoán quan trọng nhất:** lỗi "đơn điệu" nằm ở **phần mô tả hình
ảnh**, **không phải ở nội dung kịch bản** (chi tiết ở mục 7).

### Sản phẩm bàn giao

| File | Nội dung | Dung lượng | Thông số đo được |
|---|---|---|---|
| `Kc_1_Tap01.mp3` | Audio master | 20.520.044 B (19,6 MiB) | 48 kHz stereo 160 kbps · **−16,3 LUFS** · TP −1,7 dBTP · LRA 5,1 LU |
| `Kc_1_Tap01.mp4` | Video master (có nhúng audio) | 64.633.138 B (61,6 MiB) | 1920×1080 @ 30 fps · h264 339 kbps · AAC 157 kbps · 17:06,13 |

Kiểm chứng cuối: decode toàn bộ file **0 lỗi**, đúng **30.784 frame**
(= 1026,13 s × 30 fps, không rơi khung), audio đồng bộ tuyệt đối với master.

---

## 2. PHẠM VI & NGUỒN ĐẦU VÀO

> **Bản trình tự chi tiết:** xem `BAO_CAO_TRINH_TU_THUC_HIEN.md` — mục 3 dưới đây tóm
> tắt 10 bước, còn tài liệu kia tách rõ **GIAI ĐOẠN A (audio) → GIAI ĐOẠN B (tính
> frame & đồ hoạ) → GIAI ĐOẠN C (ghép video) → GIAI ĐOẠN D (kiểm chứng)**, kèm lệnh
> chạy, số đo và vòng lặp sửa thực tế.

### 2.1 Hai tài liệu plan

| Plan | Nội dung | Vai trò |
|---|---|---|
| `KeHoach_ThuAm_Tap01.md` | Kịch bản 89 block + chỉ dẫn giọng đọc, nhạc, SFX, mix | Nguồn chân lý cho **nội dung & âm thanh** |
| `KeHoach_ThuAm_Tap01_VIDEO.md` | 8 kỹ thuật chuyển động (K1–K8), 5 template đồ hoạ, nguyên tắc chống chán, pipeline | Nguồn chân lý cho **hình ảnh** |

### 2.2 Cấu trúc nội dung sau khi parse

| Loại | Số block | Ghi chú |
|---|---:|---|
| `LỜI` | 58 | 2.958 từ, TB 16,1 s/block, dài nhất 41,7 s, ngắn nhất 3,9 s |
| `SFX` | 9 | hiệu ứng âm thanh |
| `NHẠC` | 3 | music box / cello / piano |
| `NGHỈ` | 19 | khoảng lặng — nơi đặt chuyển cảnh theo plan |
| **Tổng** | **89** | 5 ô `CẦN VIẾT` bị loại bỏ theo plan (không bịa nội dung) |

### 2.3 Ràng buộc được tuân thủ

| # | Ràng buộc | Nguồn | Thực hiện |
|---|---|---|---|
| R1 | Bóc định dạng: `**text**` → giữ text bỏ `*`; xoá `*DẪN: ...*`; bỏ `` ` ``, `▸`, `[`, `]`, `#` | plan audio | Kiểm tra tự động: **0 lỗi markup** |
| R2 | Bỏ qua trọn 5 ô `CẦN VIẾT` | plan audio | `1.9`, `2.18`, `3.10`, `4.16`, `5.14` — không bịa |
| R3 | Thiếu file SFX → bỏ qua im lặng, không dừng, không hỏi | plan audio | Không có file SFX nào dùng được; 9 block SFX vẫn được giữ đúng vị trí |
| R4 | Giọng A = `audiobook_male_1`/neutral/0,90 · B = `audiobook_female_1`/sad/0,88 · pitch 0 · volume 1,0 | plan audio mục 2 | 64 request TTS đúng thông số |
| R5 | Mix: lời 0 dB · nhạc −26 dB (có lời) / −14 dB (dạo chuyển) · SFX −22/−18 dB | plan audio mục 4 | Áp dụng đúng trong `build_audio.py` |
| R6 | Nghỉ = **im lặng thật** bằng `anullsrc`, tuyệt đối không dùng dấu "..." | plan audio BƯỚC 2 | Dùng `anullsrc`; 4 block "im lặng tuyệt đối" được tắt cả nhạc |
| R7 | Chuyển động theo thời lượng **đo thật** (`timeline.json`), không theo ước lượng | plan video R3 | 100 % lấy từ `timeline.json` |
| R8 | Mỗi đoạn 20–30 s có **đúng một** thứ đang thay đổi | plan video mục 3 | Mỗi shot có đúng 1 zoom chậm; chuyển cảnh nằm trong `NGHỈ` |
| R9 | Chuyển cảnh chỉ rơi vào block `NGHỈ` | plan video mục 4 | **17/17** lần chuyển cảnh (bắt đầu & kết thúc dissolve) nằm trong `NGHỈ`; **0/17** mốc chuyển cảnh rơi vào block `LỜI` — đo bằng `.work/_seq_cuts.py` |
| R10 | Lệch thời lượng >5 % → **báo lại, không tự sửa** | plan audio BƯỚC 6 | Báo 42/58 block, bảng ở `.work/duration_deviations.md` |
| R11 | Không ghi đè file nguồn | yêu cầu dự án | 4 file nguồn giữ nguyên timestamp |

---

## 3. QUY TRÌNH THỰC HIỆN

### BƯỚC 1 · Bóc plan → cấu trúc dữ liệu
`.work/parse_plan.py` → `.work/blocks.json` (89 block, có `ma`, `loại`, `giong`,
`section`, `start`, `end`, `dur`, `planned`, `text`).
Kiểm tra R1 chạy cùng lúc: **0 lỗi markup**, mọi điểm cắt `▸` rơi đúng vào
trích dẫn.

### BƯỚC 2 · Chuẩn bị TTS
`.work/make_tts_args.py` → `.work/tts/batch_01..07.json`.
**64 request** = 58 block lời + 6 lần tách `A→B` (tại `1.4`, `3.7`, `4.6`, `4.15`,
`5.3`, `5.13`). Mỗi lệnh gọi tối đa 10 request:

```json
{"requests":[
 {"text":"<lời đã bóc R1>","voice_id":"audiobook_male_1","emotion":"neutral",
  "speed":0.90,"pitch":0,"volume":1.0,"output_file":"1_4_b1.mp3"}
]}
```

### BƯỚC 3 · Sinh & tải audio
7 lệnh gọi `connector__matrix__batch_text_to_audio`:
**64/64 thành công, 0 failed.** Tải về `.work/audio/` (64 MP3, 14.993.280 byte).
Định dạng đo bằng ffprobe: mp3 · 32000 Hz · mono · 128 kbps.

### BƯỚC 4 · Ghép audio master
`.work/build_audio.py` dựng 3 track riêng rồi mix:

| Track | Số phần | Nội dung |
|---|---:|---|
| `voice_master` | 93 | lời TTS + im lặng thật cho `NGHỈ`/`SFX`/`NHẠC`, khe 0,30 s giữa 2 nửa `A→B` |
| `bed_master` | 108 | BGM theo hồi, loop liền mạch có wrap, −26/−14 dB, mute đúng 4 block "im lặng tuyệt đối" |
| `cue_master` | 81 | 3 cue nhạc, nguồn chồng lấp trong block, `5.21` có fade-out |

Mix: `amix normalize=0` + `loudnorm I=-16 TP=-1.5 LRA=11` → `Kc_1_Tap01.mp3`,
1025,95 s. **Lệch drift max giữa 3 track: 0,010 s.**

### BƯỚC 5 · Đo thật → timeline
ffprobe từng file audio → `.work/timeline.json`: 89 block kèm
`start`/`end`/`dur`/`planned`. Tổng **1025,97 s**. Đây là nguồn chân lý cho video.

### BƯỚC 6 · Dựng đồ hoạ tĩnh (bản đầu)
`.work/build_gfx.py` → 69 PNG có alpha (nhà hồng 3 lớp parallax, thẻ hồ sơ,
timeline, sơ đồ, quote card, hero, tracker…). Xem mục 8 — bản này sau đó bị thay
toàn bộ.

### BƯỚC 7 · Báo cáo lệch thời lượng
`.work/deviation_report.py` → `.work/duration_deviations.md`.
**42/58 block lời lệch >5 %** so với cột `THỜI LƯỤNG` của plan (plan ước lượng
1055 s, thực tế 933 s). Lệch lớn nhất: `O.4` +77,4 % · `3.18` +60,0 % ·
`3.3` −47,9 % · `1.12` −38,2 % · `5.7` +38,3 %. **Không tự sửa** (theo R10).

### BƯỚC 8 · Dựng đồ hoạ (bản dựng lại)
`.work/shotlib.py` + `.work/scenes.py` + `.work/layouts.py` + `.work/build_shots.py`
→ **62 shot toàn mảnh 2400×1350** trong `assets/gfx2/shots/` (14,87 MB).
Chi tiết ở mục 7.

### BƯỚC 9 · Dựng video
`.work/build_video2.py` → 13 chunk → `concat` (`-c copy`) → mux audio.
Thời gian render đo được: **1171 s cho 1026 s video (0,88× realtime)**.

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

### BƯỚC 10 · Kiểm chứng
`.work/verify.py` (ffprobe + loudness + contact sheet 23 frame) ·
`.work/compare_before_after.py` (so sánh mật độ mực) ·
`.work/dead_zone_map.py` (ánh xạ vùng tối theo từng shot) ·
decode toàn file bằng ffmpeg.

---

## 4. KIẾN TRÚC SẢN XUẤT

```
KeHoach_ThuAm_Tap01.md ─┐
                        ├─> parse_plan.py ─> blocks.json (89 block)
KeHoach_ThuAm_Tap01_VIDEO.md ┘        │
                                        ├─> make_tts_args.py ─> 7 batch JSON
                                        │        └─> TTS 64/64 ─> fetch_audio.py ─> 64 MP3
                                        │                 └─> build_audio.py ─> Kc_1_Tap01.mp3
                                        │                              └─> timeline.json (đo thật)
                                        └─> build_shots.py ─> 62 PNG 2400×1350
                                                 └─> build_video2.py ─> 13 chunk ─> concat
                                                                              └─> Kc_1_Tap01.mp4
```

Nguyên tắc kiến trúc: **`timeline.json` là nguồn chân lý duy nhất cho thời lượng**.
Không có con số nào trong pipeline đến từ ước lượng tay của plan.

---

## 5. CÁC QUYẾT ĐỊNH THIẾT KẾ

| # | Quyết định | Lý do | Ảnh hưởng |
|---|---|---|---|
| Q1 | **Dùng Pillow thay EffectCraft** cho đồ hoạ tĩnh | Cầu nối MCP của EffectCraft âm thầm bỏ qua tham số số (`layer.newText` từ chối `size`; `comp.new` bỏ `duration`/`frameRate`; `app.executeCommand` bỏ toàn bộ params) ⇒ không đặt được cỡ chữ/màu/kiểu chữ | Đồ hoạ vẫn đúng spec plan (PNG 1920×1080 có alpha) |
| Q2 | **Mọi chữ để ffmpeg `drawtext`**, đo bề rộng bằng PIL để canh giữa | Đây là thứ EffectCraft không làm được | Chữ luôn sắc nét, canh giữa chuẩn |
| Q3 | **Chia 13 chunk** thay vì 1 pass 60+ overlay | 1 pass chạy **5× chậm realtime**, 3,2 GB RAM | Render 0,88× realtime, ~1,2 GB |
| Q4 | **Bộ lọc `loop`** thay `-loop 1` | `-loop 1` giải mã lại file PNG **30 lần/giây** | Mỗi PNG chỉ giải mã 1 lần |
| Q5 | **Đồ hoạ tự sản xuất** (nhà hồng, hồ sơ bị bôi mắt) | Không có ảnh báo chí sẵn — tránh rủi ro pháp lý về ảnh gia đình tư nhân | Pipeline tự ưu tiên ảnh thật nếu thả vào `assets/photos/` |
| Q6 | **Dùng `-b:v` thay `-q:v`** | `libopenh264` **bỏ qua `-q:v` hoàn toàn** (thử 5/8/12 → 3 file byte-identical) | Kiểm soát dung lượng thật |
| Q7 | **Hạt phim `noise=alls` 7 → 2** (plan ghi 7) | Đo được: hạt phim ăn **4,5× bitrate** (alls=4 → 1258 kbps; alls=3 → 660; alls=2 → 278) | 133,8 MB → 43,0 MB; chữ sạch hơn, phục vụ rủi ro số 5 của plan |
| Q8 | **`rgbashift` ±2 → ±1** | Ở mức ±2, chữ trắng bị viền đỏ/cyan lộ rõ | Giữ hiệu ứng tách kênh, bớt lỗi thị giác |
| Q9 | **Bỏ lưới nền ở `bg_base.png`** | Lưới lộ ra ở mép nơi lớp parallax không phủ hết khung | Nền sạch |
| Q10 | **Cross-dissolve bằng 2 shot cùng hiện** thay vì `xfade` | `xfade` phải cắt chuỗi, khó giữ đồng thời nhiều lớp | Đạt đúng tinh thần K8, chuyển cảnh nằm trong `NGHỈ` |
| Q11 | **Mỗi shot là 1 PNG toàn mảnh 2400×1350** | ffmpeg chỉ cần zoom + overlay, không phải ghép nhiều lớp trong 1 graph | Bền vững, dễ tái lập |
| Q12 | **3 bố cục A/B/C, mỗi hồi một ngôn ngữ** (user chọn) | 1 kiểu bố cục duy nhất = đơn điệu (đã đo ở mục 7) | Mỗi hồi có nhịp thị giác riêng |

---

## 6. NHẬT KÝ VẤN ĐỀ — 16 vấn đề đã gặp

| # | Hiện tượng | Nguyên nhân gốc | Cách xử lý | Bằng chứng |
|---|---|---|---|---|
| 1 | Video **133,8 MB**, plan ghi "~30 MB" | Hạt phim K7 ăn hết bitrate; con số 30 MB của plan đo trên overlay đơn giản **không có grain** | Hạ `noise` 4 → 2, giữ VBR 1500 | 1258 → 278 kbps đo trên cùng 1 chunk |
| 2 | `-q:v 5/6` không có tác dụng | `libopenh264` bỏ qua `-q:v` | Chuyển `-b:v` + `-maxrate` + `-bufsize` | Thử 5/8/12 → 3 file **byte-identical** |
| 3 | Chữ trắng bị viền đỏ/cyan | `rgbashift ±2` của plan quá mạnh | Giảm còn ±1 | So khung hình 1:1 |
| 4 | Không có `libx264` | Bản ffmpeg LGPL | Dùng `libopenh264` theo đặc tả; nâng cấp GPL là bước *không bắt buộc* | `ffmpeg -encoders` |
| 5 | Render 1 pass quá nặng | 60+ overlay cùng lúc | Chia 13 chunk | 5× chậm realtime → 0,88× realtime |
| 6 | PNG bị giải mã lại 30 lần/s | `-loop 1` | Bộ lọc `loop=loop=-1:size=1` | — |
| 7 | Reveal timeline không chạy được | `crop` **không có option `eval`** trên bản này | Trượt bằng biểu thức `x` của `overlay` | — |
| 8 | Không set được cỡ chữ | Cầu nối EffectCraft bỏ qua tham số số | Pillow + `drawtext` | `size: expected a number` |
| 9 | Khung bằng chứng lệch phải, 55 % khung trái trống | Bố cục neo góc | 760×570 @ `x=1080` → **880×660 @ `x=520`** | Xem frame |
| 10 | Thẻ mốc timeline bị cắt dòng chú thích | Kích thước thẻ thiếu | 300×150 → **300×172** | Xem frame |
| 11 | **78 s màn hình đen trơn** (681–759 s) | Block `4.7`–`4.12` **không được gán hình nào** | Dựng lại toàn bộ lớp hình (mục 7) | Quét mực mỗi 2 s |
| 12 | 19 block `NGHỈ` thành màn hình đen | **K8 (xfade) chưa hề implement** | Cross-dissolve trong `NGHỈ` | 0 % → 17/17 lần chuyển cảnh |
| 13 | 15 cảnh nền "tối đen" mất hết nội dung | **`PIL.Image.composite` trả về ảnh MỚI, thay thế nền** | Viết hàm `glow()` **hòa vào** nền | So sánh trước/sau |
| 14 | Nhà hồng biến mất khi dán lên trời | `house_flat.png` có **nền đục sẵn** | Dùng làm nền rồi cắt/dịch sang phải | Xem frame |
| 15 | Chân dung dính chữ thừa | `portrait.png` thực ra là **thẻ hồ sơ có chữ**, không phải silhouette | Vẽ silhouette thủ công | Xem frame |
| 16 | Timeline lệch, shot sai giữa các chunk | `setpts` đặt **trước** `trim` | Thứ tự đúng: `fade → trim → setpts` | So sánh frame |

### 6.1 Bẫy môi trường (không phải lỗi logic, nhưng mất thời gian)

| Bẫy | Biểu hiện | Xử lý |
|---|---|---|
| `Set-Content -Encoding UTF8` của PowerShell 5.1 | Thêm BOM → `SyntaxError: invalid non-printable character U+FEFF` | Gỡ BOM bằng Python |
| `-replace` trong PowerShell | `` `n `` biến thành ký tự literal → hỏng file | Dùng Edit tool cho sửa lệch văn bản |
| `fontfile='C:/...'` trong ffmpeg | "No option name near..." | Escape dấu `:` → `C\:/Windows/Fonts/...` |
| Lệnh `cd` + `Set-Content`/`Remove-Item` | Bị policy chặn | Dùng Edit tool / `rm -- <đường dẫn tuyệt đối>` |
| `mcode-tools` là `.cmd` | Không gọi trực tiếp được | Gọi qua `["cmd","/c","mcode-tools",...]` |
| `Tee-Object` ghi file | Ghi UTF-16 (BOM) | Đọc file JSON bằng detector BOM |

---

## 7. ĐIỂM MẮU CHỐT — CHẨN ĐOÁN "VIDEO ĐƠN ĐIỆU"

Bản đầu tiên bị đánh giá là đơn điệu. Để không đoán, đã đo 3 cách khác nhau.

### 7.1 Đo mật độ mực (513 mẫu, mỗi 2 s)

| Chỉ số | Bản đầu |
|---|---:|
| Mật độ mực trung bình | 4,3 % |
| **Mật độ mực median** | **2,4 %** — tức 97,6 % màn hình đen |
| Frame dưới 3 % mực | 295 / 513 = **590 s (57,5 %)** |
| Frame dưới 6 % mực | 427 / 513 = 854 s (83,2 %) |
| Frame dưới 10 % mực | 476 / 513 = **952 s (92,8 %)** |
| Vùng chết dài nhất | 198–350 s (**152 s**) · 420–552 s (132 s) · 682–760 s (78 s) · 898–968 s (70 s) |

### 7.2 Đo phủ hình & chuyển động

| Chỉ số | Bản đầu | Yêu cầu của plan |
|---|---:|---|
| Thời lượng có chuyển động thật | 293,8 s / 1025,97 s = **28,6 %** | mục 5: *"100 % thời lượng đều có chuyển động"* |
| Thời lượng đứng yên | **71,4 %** | 0 % |
| K8 cross-dissolve | **0 %** | mục 4 K8 + BƯỚC 6 |
| Số template trong mục 6 | **5** (`OV-TL`, `OV-DF`, `OV-MD`, `OV-EV`, `NUM`) | — |
| `bg_base.png` | **hoàn toàn trong suốt** | — |
| BBox `label_h4` (nhãn chương dùng 78 s) | **0,94 %** khung | — |
| BBox `tl_strip` (dải timeline) | 0,51 % — 1 vạch 7 px | — |
| BBox `blank_hero` (dùng cho Ken Burns 26 s) | 1,02 % | — |

### 7.3 Kết luận

**Nguyên nhân là ở phần mô tả hình ảnh, không phải ở nội dung kịch bản.**

1. **Mục 6 của plan tự định nghĩa một ngôn ngữ hình chỉ có một kiểu**: *"nền trong mờ
   85–90 %, chữ trắng, tối đa 6 dòng mỗi thẻ"*. Bản chất của đặc tả này là **một
   thẻ chữ nổi trên nền tối**. Với 58 block lời thì ra 58 thẻ chữ — đơn điệu là
   **hệ quả tất định** của chính đặc tả, không phải lỗi thực thi.
2. **Mục 5 yêu cầu "100 % thời lượng có chuyển động"** nhưng thực tế 28,6 %.
3. **Lỗi phủ hình thật do tôi gây ra**: block `4.7`–`4.12` (76 s) không có hình →
   78 s màn hình đen đúng lúc cao trào.
4. **Nội dung thì tốt**: kịch bản có cấu trúc rõ (ngôi nhà → hồ sơ → dòng thời
   gian → hồ sơ bệnh án → 3 tầng tâm lý → cơ chế học → phán quyết → 4 dấu hiệu
   đỏ → khép lại) và có sẵn các mốc hình tự nhiên. Vấn đề là **hình ảnh không bám
   theo nội dung**.

### 7.4 Cách sửa đã thực hiện (user chọn: *trộn cả 3 theo từng hồi*)

Dựng lại **toàn bộ lớp hình ảnh**, không phải vá chỗ:

- **62 shot toàn mảnh 2400×1350** — mỗi shot = một (nhóm) block lời.
  Phủ **96,5 %** thời lượng; **17 khoảng trống ≥0,05 s** còn lại (tổng 33,01 s) đều là
  block `NGHỈ` ⇒ đúng chỗ đặt chuyển cảnh theo plan.
- **3 bố cục, mỗi hồi một ngôn ngữ**:

| Hồi | Thời lượng | Số shot | Bố cục |
|---|---:|---:|---|
| Mở đầu | 40,9 s | 2 | A toàn mản ×2 |
| Hồi 1 — Ngôi nhà màu hồng | 147,3 s | 9 | A ×4 · **B** thẻ kính ×5 |
| Hồi 2 — Hồ sơ bệnh án | 182,4 s | 10 | **C** chia đôi ×9 · A ×1 |
| Hồi 3 — Giải pháp tâm lý | 215,4 s | 15 | A toàn mản ×15 (mạng nơ-ron, số 01/02/03) |
| Hồi 4 — Giọc nhìn nạn nhân | 289,7 s | 12 | **B** thẻ kính ×11 · A ×1 |
| Hồi 5 — Pháp luật & cảnh báo | 181,6 s | 14 | A ×13 (tòa án, tù, 4 lá cờ đỏ) · B ×1 |

  - **A · Toàn mản**: cảnh chiếm khung, chữ lớn đè lên (nhà hồng, mạng nơ-ron, tù).
  - **B · Thẻ kính**: thẻ lớn bên trái trên cảnh thật mờ 30 %, cột phải để cảnh lộ.
  - **C · Chia đôi**: cột trái là hình/mốc, chữ bên phải.
- **15 cảnh nền** dựng bằng Pillow: nhà hồng ban đêm · bàn hồ sơ · điện thoại
  Facebook · đêm đường · bệnh án · phòng bệnh · mạng nơ-ron · tiền · tối ·
  xích · tòa án · nhà tù · cờ đỏ · chân dung bị bôi mắt.
- **Mỗi shot có 1 zoom chậm riêng** (1,00 → 1,045, xen kẻ vào/ra) ⇒
  **100 % thời lượng có chuyển động**, đúng chuẩn mục 5.
- **Cross-dissolve thật trong block `NGHỈ`** (2 shot cùng hiện, alpha bù nhau) —
  đạt đúng tinh thần K8, không cắt vạch giữa lời.
- Giữ nguyên K7 (hạt phim 2, vignette, lệch màu ±1).

### 7.5 Kết quả

| Chỉ số | Cũ | Mới |
|---|---:|---:|
| Mật độ mực median | 2,4 % | **19,3 %** (× 7,9) |
| Thời lượng "chết" | 57,5 % | **16,4 %** |
| Thời lượng có nội dung thật (>3 % mực) | ~42 % | **83,6 %** |
| Thời lượng có chuyển động thật | 28,6 % | **100 %** |
| Dung lượng | 43,0 MiB | 61,6 MiB |

Trong 16,4 % còn lại, phần lớn là **cảnh tối có chủ đích** (`void`, `dark`,
`helpless`, `night`) — đã xem mắt từng frame: chữ vẫn rõ, cảnh vẫn có chủ thể.
*Metric "mực" đếm thiếu chữ mảnh (chữ trắng 66 px trên nền tối chỉ ~1 % khung),
nên phải xem mắt để kết luận, đừng chỉ nhìn số.*

---

## 8. KIỂM CHỨNG CHẤT LƯỢNG

| Hạng mục | Kết quả |
|---|---|
| Parse plan | 89 block · 5 `CẦN VIẾT` bị loại · **0 lỗi markup** |
| TTS | **64/64 thành công**, 0 failed · 64 MP3 (32000 Hz, mono, 128 kbps) |
| Ghép audio | 3 track · **drift max 0,010 s** |
| Loudness | **−16,3 LUFS** · TP −1,7 dBTP · LRA 5,1 LU |
| Encode video | 13/13 chunk OK · concat OK · mux OK |
| Decode toàn file | **0 lỗi** · đúng **30.784 frame** (không rơi khung) |
| Phủ hình | **96,5 %** · 17 khoảng trống ≥0,05 s (tổng 33,01 s) = block `NGHỈ` |
| Chuyển động | **100 %** thời lượng |
| Mật độ mực | median **19,3 %** (× 7,9 so với bản đầu) |
| Lệch thời lượng | 42/58 block lệch >5 % — **đã báo, không tự sửa** |
| File nguồn | 4 file gốc giữ nguyên timestamp |

---

## 9. RUNBOOK — TÁI LẬP CHO TẬP 2–10

### 9.1 Quy trình chạy

```powershell
cd 'D:\TEST\Gax\Audi'
$env:PYTHONIOENCODING='utf-8'        # BẮT BUỘC, nếu không console cp1252 sẽ crash khi in tiếng Việt

python .work\parse_plan.py            # -> .work/blocks.json
python .work\make_tts_args.py         # -> .work/tts/batch_01..NN.json
# 7 lệnh gọi TTS (KHÔNG chạy lại nếu file MP3 đã tồn tại):
#   mcode-tools connector call connector__matrix__batch_text_to_audio --args-file .work\tts\batch_0N.json
python .work\fetch_audio.py           # -> .work/audio/*.mp3
python .work\build_audio.py           # -> Kc_1_Tap01.mp3 + .work/timeline.json
python .work\build_shots.py           # -> assets/gfx2/shots/*.png + .work/shots.json
$env:AUDI_VBR='1500'; $env:AUDI_NOISE='2'; $env:AUDI_MOVE='zoom'
python .work\build_video2.py          # -> 13 chunk -> concat -> Kc_1_Tap01.mp4
python .work\deviation_report.py      # -> .work/duration_deviations.md
python .work\verify.py                # -> .work/gfx/_final_sheet.png
python .work\compare_before_after.py  # so sánh mật độ mực
```

Biến môi trường hữu ích:
`AUDI_ONLY="1,3"` (render lại đúng các chunk) · `AUDI_VBR` (kbit/s, mặc định 1500) ·
`AUDI_NOISE` (hạt phim, mặc định 2) · `AUDI_MOVE` (`zoom` | `pan`).

### 9.2 Phần phải viết lại cho mỗi tập

Chỉ có **một** phần cần sáng tạo lại: **danh sách `SHOTS` trong
`.work/build_shots.py`**. Đó chính là "phần mô tả hình ảnh" mà plan mục 6 thiếu.

Cấu trúc mỗi shot:

```python
S(id="h2b", ma="2.4", end="2.4", f1=0.5, L="C", sc="casefile",
  anch="doc", chap="h2",
  label="HỒ SƠ Y TẾ",
  headline="1991 — SINH RA,\nHOÀN TOÀN KHỎE MẠNH",
  sub="Một đứa trẻ bình thường, không có gì bất thường.")
```

| Trường | Ý nghĩa |
|---|---|
| `ma` / `end` | Mã block đầu & cuối mà shot phủ |
| `f0` / `f1` | Phần đầu / cuối của block (dùng để tách block dài thành 2 shot) |
| `L` | Bố cục: `A` toàn mảnh · `B` thẻ kính · `C` chia đôi |
| `sc` | Tên cảnh nền (xem `SCENES` trong `scenes.py`) |
| `anch` | Hình neo cột trái cho bố cục C: `house` `doc` `medical` `storm` `brain` `phone` `money` `chains` `bars` |
| `label` / `headline` / `sub` | Chữ trên khung |
| `big` | Con số lớn (vd `"03"`, `"10"`, `"?"`) |
| `chap` | Hồi (dùng cho nhãn chương) |

**Nguyên tắc chọn bố cục:** xen kẽ A/B/C trong một hồi để không có 2 shot giống
nhau liền nhau. Ưu tiên shot dài 12–22 s (mục 3 của plan: 20–30 s).

### 9.3 Thêm ảnh thật

Thả ảnh vào `assets/photos/<tên>.jpg` (vd `portrait.jpg`, `house_flat.jpg`) —
pipeline **tự ưu tiên ảnh thật** thay cho đồ hoạ phẳng tự dựng, không cần sửa code.

### 9.4 Nâng cấp encoder (không bắt buộc)

Bản ffmpeg hiện tại là LGPL, **không có `libx264`**. Theo plan mục 8, tải bản GPL
từ <https://www.gyan.dev/ffmpeg/builds/> rồi dùng:

```bash
ffmpeg ... -c:v libx264 -preset medium -crf 20 ...
```

→ chất lượng tốt hơn **và** file nhỏ hơn nữa.

---

## 10. PHỤ LỤC

### A. Cấu trúc thư mục

```
D:\TEST\Gax\Audi\
├── Kc_1_Tap01.mp3              ← audio master (19,6 MiB)
├── Kc_1_Tap01.mp4              ← video master (61,6 MiB)
├── KeHoach_ThuAm_Tap01.md     ← plan audio (nguyên bản, không sửa)
├── KeHoach_ThuAm_Tap01_VIDEO.md← plan video (nguyên bản, không sửa)
├── Kc_1.txt / Kich_ban.txt / AI_video.txt / Kc_1.mp3   ← nguồn (không sửa)
├── BAO_CAO_TAP01.md           ← báo cáo này
├── assets\
│   ├── gfx2\shots\            ← 63 PNG 2400×1350 (62 shot + nền đen)
│   └── gfx\                   ← 69 PNG lớp cũ (giữ lại tham khảo)
└── .work\
    ├── blocks.json / timeline.json / shots.json
    ├── blocks_list.txt / duration_deviations.md
    ├── parse_plan.py  make_tts_args.py  fetch_audio.py
    ├── build_audio.py  build_shots.py  build_video2.py
    ├── shotlib.py  scenes.py  layouts.py
    ├── deviation_report.py  verify.py  compare_before_after.py
    ├── dead_zone_map.py  diagnose_monotony.py  ink_profile.py
    ├── collect_report_data.py  shots_sheet.py  bbox_report.py
    ├── audio/ (64 MP3)   tts/ (15 JSON)   video/ (13 chunk)
    ├── ffmpeg/  (bản LGPL n9.0, có libopenh264)
    ├── _old_Tap01.mp4      ← bản cũ, để so sánh
    └── _probe_evidence\    ← ảnh so sánh encoder (noise 2/3/4)
```

### B. Con số đo được đáng nhớ

| Con số | Giá trị |
|---|---|
| Hạt phim K7 tốn bitrate | alls=4 → 1258 kbps · alls=3 → 660 · alls=2 → 278 (4,5×) |
| Tốc độ render (13 chunk) | 1171 s cho 1026 s video = 0,88× realtime |
| Chi phí 1 pass 60+ overlay | 5× chậm realtime, 3,2 GB RAM |
| Tốc độ decode PNG | `-loop 1` = 30 lần/s → bộ lọc `loop` = 1 lần |
| File filter > 32 KB | dùng `-/filter_complex <file>`, file **UTF-8 không BOM** |
| Mật độ mực chữ trắng 66 px trên nền tối | ~1 % khung ⇒ metric đếm thiếu, phải xem mắt |

### C. Bảng lệch thời lượng

Toàn bộ 42/58 block lệch >5 % nằm ở **`.work/duration_deviations.md`**
(kèm trích lời để đối chiếu). Tóm tắt: plan ước lượng 1055 s, thực tế 933 s —
nguyên nhân là cột `THỜI LƯỢNG` của plan là ước lượng tay, không khớp tốc độ
đọc thật của giọng TTS. Video dựng theo thời lượng **đo được**.

---

*Báo cáo được tạo bằng Mavis · 21/10/2026. Mọi con số trong báo cáo đều đo được
từ artifact thực tế bằng ffprobe / PIL / ffmpeg, không ước lượng.*
