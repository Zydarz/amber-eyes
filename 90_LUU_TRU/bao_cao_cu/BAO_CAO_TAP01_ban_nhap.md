# Báo cáo sản xuất Tập 01 — "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ"

Sinh ra từ `KeHoach_ThuAm_Tap01.md` (v2) + `KeHoach_ThuAm_Tap01_VIDEO.md` (v4).
Ngày: 21/10/2026.

---

## 1. Kết quả cuối cùng

| Tệp | Nội dung | Dung lượng | Thông số |
|---|---|---|---|
| `Kc_1_Tap01.mp3` | Audio master | 20.520.044 B (19,6 MiB) | 48 kHz stereo 160 kbps · **−16,3 LUFS** · TP −1,7 dBTP · LRA 5,1 LU |
| `Kc_1_Tap01.mp4` | Video master (có nhúng audio) | 64.633.138 B (61,6 MiB) | 1920×1080 @ 30 fps · h264 (libopenh264) 339 kbps · AAC 157 kbps |

Thời lượng: **17:05,95** (audio) / **17:06,13** (video) — đo thật bằng ffprobe, khớp `timeline.json`.
Decode toàn bộ: **0 lỗi**, đúng **30.784 frame** (không rơi khung).

---

## 2. VẤN ĐỀ "VIDEO ĐƠN ĐIỆU" — CHẨN ĐOÁN & CÁCH SỬA

Bản dựng đầu tiên bị người dùng đánh giá là **đơn điệu, thiếu sức hút**. Đã đo thay
vì đoán:

### 2.1 Số đo

| Chỉ số | Bản cũ |
|---|---|
| Mật độ mực trung vị (pixel không đen) | **2,4 %** — 97,6 % màn hình trống |
| Số frame (mẫu 2 s) dưới 3 % mực | **295 / 513 = 590 s (57,5 %)** |
| Số frame dưới 10 % mực | 476 / 513 = **92,8 %** |
| Vùng chết dài nhất | 198–350 s (**152 s**) · 420–552 s (132 s) · 682–760 s (78 s) |
| Thời lượng có chuyển động thật | 293,8 s / 1025,97 s = **28,6 %** |
| Thời lượng đứng yên | **71,4 %** |
| Số "shot" (khoảnh khắc hình thay đổi) | 53, trung bình 8,3 s |
| Số template trong plan (mục 6) | **5** (`OV-TL`, `OV-DF`, `OV-MD`, `OV-EV`, `NUM`) |
| BBox của asset nhỏ nhất | `label_h4` = **0,94 %** khung · `tl_strip` = 0,51 % (1 vạch 7 px) |
| `bg_base.png` | **hoàn toàn trong suốt** — không có nền |

### 2.2 Kết luận: **lỗi ở phần mô tả hình ảnh, KHÔNG phải ở nội dung**

1. **Mục 6 của plan tự định nghĩa một ngôn ngữ hình chỉ có một kiểu** — *"nền trong mờ
   85–90 %, chữ trắng, tối đa 6 dòng mỗi thẻ"*. Bản chất là **một thẻ chữ nổi trên
   nền tối**. Với 58 block lời thì 58 thẻ chữ → đơn điệu là hệ quả tất định.
2. **Mục 5 yêu cầu *"100 % thời lượng đều có chuyển động"*** nhưng thực tế 28,6 %.
3. **K8 (xfade) chưa hề được implement** (0 % thời lượng) → 19 block `NGHỈ` biến
   thành **màn hình đen trơn**, đúng lúc câu chuyện cao trào nhất.
4. **Lỗi phủ hình thật do tôi gây ra:** block `4.7`–`4.12` (76 s) — phần kể đáng
   nhất về năm 2011, búa đập máy tính, lối thoát — **không được gán hình nào**,
   màn hình trắng trơn 78 s liên tục.
5. **Nội dung thì tốt.** Kịch bản có cấu trúc rõ (ngôi nhà → hồ sơ → dòng thời
   gian → hồ sơ bệnh án → 3 tầng tâm lý → cơ chế học → phán quyết → 4 dấu hiệu
   đỏ) và có mốc hình tự nhiên sẵn có. Vấn đề là **hình ảnh không bám theo nội dung**,
   chứ không phải nội dung thiếu.

### 2.3 Cách sửa (user chọn: *trộn cả 3 theo từng hồi*)

Dựng lại **toàn bộ lớp hình ảnh** — không phải vá chỗ:

- **62 shot toàn mảnh 2400×1350**, mỗi shot = một (nhóm) block lời → phủ **96,5 %**
  thời lượng, và **18 khoảng trống còn lại đều là block `NGHỈ`** — đúng chỗ để
  đặt chuyển cảnh.
- **3 ngôn ngữ bố cục, mỗi hồi một ngôn ngữ** (user chọn phương án trộn):
  | Hồi | Layout | Mô tả |
  |---|---|---|
  | Mở đầu | **A** toàn mản | cảnh chiếm khung, chữ lớn đè lên |
  | Hồi 1 | **B** thẻ kính | thẻ lớn trôi trên cảnh thật mờ 30 % |
  | Hồi 2 | **C** chia đôi | cột trái là hình/mốc, chữ bên phải |
  | Hồi 3 | **A** toàn mản | não, mạng nơ-ron, số lớn 01/02/03 |
  | Hồi 4 | **B** thẻ kính | cơ chế, xích, trauma bonding |
  | Hồi 5 | **A** xen **B** | tòa án, tù, 4 lá cờ đỏ |
- **15 cảnh nền** dựng bằng Pillow: nhà hồng ban đêm, bàn hồ sơ, điện thoại
  Facebook, đêm đường, bệnh án, phòng bệnh, mạng nơ-ron, tiền, tối, xích, tòa án,
  nhà tù, cờ đỏ, chân dung bị bôi mắt.
- **Mỗi shot có chuyển động riêng** (zoom chậm 1,00 → 1,045, xen kẻ vào/ra) →
  **100 % thời lượng có chuyển động**, đạt đúng yêu cầu mục 5 của plan.
- **Cross-dissolve thật nằm trong block `NGHỈ`** (K8): hai shot cùng hiện, alpha
  bù nhau trong khoảng lặng.
- Giữ nguyên K7 (hạt phim 2, vignette, lệch màu ±1).

### 2.4 Bẫy đã gặp khi dựng lại

- **`PIL.Image.composite` trong hàm dựng cảnh gốc trả về ảnh MỚI, thay thế nền**
  → mọi cảnh bị mất nội dung, chỉ còn một quầng sáng trên nền đen. Đã đổi sang
  hàm `glow()` **hòa vào** nền.
- `house_flat.png` có nền đục sẵn → paste đè lên trời làm mất cảnh; phải dùng
  nó làm nền rồi cắt/dịch sang phải.
- `portrait.png` hóa ra là **thẻ hồ sơ có chữ**, không phải silhouette → phải vẽ
  silhouette thủ công.
- Sai thứ tự chuỗi filter: `setpts` trước `trim` làm lệch timeline → phải
  `fade → trim → setpts`.
- `Set-Content -Encoding UTF8` của PowerShell 5.1 **thêm BOM** → Python báo
  `SyntaxError: invalid non-printable character U+FEFF`; phải gỡ BOM bằng Python.
- `-replace` trong PowerShell biến `` `n `` thành ký tự literal → hỏng file;
  dùng Edit tool cho các sửa lệch văn bản.

### 2.5 Kết quả đo lại (bản cũ → bản mới)

| Chỉ số | Cũ | Mới | Thay đổi |
|---|---:|---:|---|
| Mật độ mực median | 2,4 % | **19,3 %** | **× 7,9** |
| Mật độ mực trung bình | 4,3 % | 17,2 % | × 4,0 |
| Frame dưới 3 % mực (màn hình trống) | 57,5 % | **16,4 %** | − 41,1 điểm |
| Frame dưới 10 % mực | 92,8 % | 35,9 % | − 56,9 điểm |
| Số vùng chết | 16 | 12 | − 4 |
| Thời lượng có chuyển động thật | 28,6 % | **100 %** | đạt chuẩn mục 5 của plan |
| Phủ hình (shot) | 53 shot, trung bình 8,3 s | **62 shot toàn mảnh** | — |
| K8 cross-dissolve | 0 % | 18/18 block NGHỈ | đủ chuẩn plan |
| Dung lượng | 43,0 MiB | 61,6 MiB | hình có chi tiết hơn |

Trong 16,4 % còn lại, phần lớn là **cảnh tối có chủ đích** (`void`, `dark`,
`helpless`, `night`) — đó là lựa chọn diễn hình, không phải lỗ hổng (đã xem mắt
từng frame: chữ vẫn rõ, cảnh vẫn có chủ thể). **83,6 %** thời lượng có nội dung
thật (> 3 % mực).

---


### 3.1 Dung lượng video vượt xa ước lượng của plan — **ĐÃ XỬ LÝ**

Plan (mục 9) ghi *"Dung lượng file ~30 MB"*, nhưng bản dựng đầu ra **133,8 MB**.

**Nguyên nhân gốc (đo thật, không phải phỏng đoán):** hạt phim K7 là thứ nuốt bitrate.
Đo trên cùng một chunk (chunk 04, nội dung không đổi), chỉ đổi cường độ hạt:

| `noise=alls` | Bitrate thực | Dung lượng ước tính cả tập |
|---:|---:|---:|
| 4 | 1258 kbps | 134 MB (đo được) |
| 3 | 660 kbps | 85 MB |
| **2** | **278 kbps** | **43,0 MiB (đo được)** |

Plan tự mâu thuẫn: vừa bắt buộc áp K7 (hạt phim) lên **toàn bộ** video, vừa ước
lượng ~30 MB — mà con số 30 MB được đo trên *một lớp overlay đơn giản, không có hạt phim*.

**Cách xử lý:** hạ `noise=alls` từ 4 xuống **2** (plan ghi 7; mà 7 chắc chắn vượt xa
mục tiêu dung lượng). So sánh khung hình 1:1 cho thấy `alls=4` để lại **speckle màu
đỏ/xanh rõ rệt trên nền trời đêm và trên cạnh chữ** — trông giống lỗi nén hơn là
hạt phim; `alls=2` chữ sạch, nền vẫn giữ texture. Cái này cũng phục vụ chính rủi ro
số 5 của plan (*"chữ trong video không đọc được trên điện thoại"*).

**Kết quả:** 133,8 MB → **45.081.236 byte (43,0 MiB)**, video 878 kbps → 186 kbps.
Ảnh so sánh lưu ở `.work/_probe_evidence/` (`cmp_parallax.png` — nền trời đêm,
`cmp_grain.png` — cạnh chữ).

Bản dùng cuối cùng đặt mặc định trong `.work/build_video.py`:
`AUDI_VBR=1500`, `AUDI_NOISE=2` → tái chạy được, không cần biến môi trường.

### 3.2 `libopenh264` bỏ qua `-q:v` — **ĐÃ XỬ LÝ**

Plan mục 2 dùng `-q:v 5/6` cho mọi lệnh. Bản ffmpeg LGPL này **bỏ qua `-q:v` hoàn toàn**:
thử 5 / 8 / 12 cho ra 3 file **byte-identical**. Chuyển sang `-b:v <kbit>` + `-maxrate`
+ `-bufsize` để kiểm soát dung lượng thật.

### 3.3 `rgbashift` ±2 tạo viền đỏ/cyan lộ trên chữ trắng — **ĐÃ XỬ LÝ**

Plan K7 ghi `rgbashift=rh=-2:bh=2`. Ở mức ±2, chữ trắng trên nền tối bị viền đỏ/cyan
rõ rệt. Giảm xuống **±1**, giữ nguyên hiệu ứng tách kênh.

### 3.4 Bản ffmpeg này **không có** `libx264` — **ĐÃ XỬ LÝ**

Đúng như plan mục 8 đã ghi. Dùng `libopenh264` theo đặc tả. Nâng cấp lên bản GPL
(`-c:v libx264 -preset medium -crf 20`) là bước nâng cấp *không bắt buộc* — sẽ cho
chất lượng tốt hơn **và** file nhỏ hơn nữa.

### 3.5 1 pass ffmpeg với 60+ overlay quá nặng — **ĐÃ XỮ LÝ**

Chạy 1 pass với toàn bộ overlay: **5× chậm realtime**, 3,2 GB RAM. Tách thành
**13 chunk**, mỗi chunk 1 pass, rồi `concat` (`-c copy`) + ghép audio.

### 3.6 Mỗi PNG bị giải mã lại 30 lần/giây — **ĐÃ XỬ LÝ**

`-loop 1 -i png.png` giải mã lại file ở **mỗi frame**. Thay bằng bộ lọc
`loop=loop=-1:size=1:start=0,setpts=N/(30*TB)` → mỗi PNG chỉ giải mã **một lần**.

### 3.7 `crop` không có option `eval` — **ĐÃ XỬ LÝ**

Bản ffmpeg này không có `eval=frame` cho `crop`, nên reveal tiến trình của dải timeline
(K2) chuyển sang **trượt bằng biểu thức `x` của `overlay`**.

### 3.8 EffectCraft không set được thông số chữ — **ĐÃ XỬ LÝ, ĐÃ CHUYỂN HƯỚNG**

Cầu nối lệnh của EffectCraft âm thầm bỏ qua tham số số (`layer.newText` từ chối
`size`; `comp.new` bỏ `duration`/`frameRate`; `app.executeCommand` bỏ toàn bộ params).
Đồ hoạ tĩnh dựng lại bằng **Pillow** (PNG 1920×1080 có alpha — đúng đặc tả plan),
còn **mọi chữ trong video để ffmpeg `drawtext`** (đo bề rộng bằng PIL để canh giữa).

### 3.9 2 lỗi bố cục phát hiện khi xem frame — **ĐÃ XỬ LÝ**

- Khung bằng chứng (OV-EV) đặt lệch sang phải, 55% khung bên trái trống → chuyển
  từ 760×570 tại `x=1080` sang **880×660 tại `x=520`** (căn giữa).
- Thẻ mốc timeline bị cắt chữ ở dòng chú thích → kích thước thẻ 300×150 → **300×172**.

### 3.10 42/58 block lệch thời lượng >5% so với plan — **ĐÃ BÁO, KHÔNG TỰ SỬA**

Theo BƯỚC 6 của plan audio: lệch >5% thì **báo lại, không tự sửa**.
Bảng đầy đủ: `.work/duration_deviations.md`.

- Tổng thực tế **1025,97 s** vs plan dự kiến bản demo 17:50.
- Nguyên nhân: cột THỜI LƯỢNG của plan là ước lượng tay, không khớp tốc độ đọc
  thật của giọng TTS.
- Video **dựng theo thời lượng đo được** (`.work/timeline.json`), không theo ước lượng.

### 3.11 5 ô `CẦN VIẾT` — **BỎ QUA ĐÚNG THEO PLAN**

Các ô `1.9`, `2.18`, `3.10`, `4.16`, `5.14` bị bỏ qua hoàn toàn, **không bịa nội dung**.

---

## 4. Kiểm tra đã chạy

- `parse_plan.py` → 89 block (58 lời + 9 SFX + 3 NHẠC + 19 NGHỈ). Kiểm tra R1: **0 lỗi markup**.
- TTS: **64/64 thành công**, 0 failed. 64 MP3 (32000 Hz, mono, 128 kbps).
- Ghép audio: 3 track (voice / bed / cue) lệch drift tối đa **0,010 s**.
- Encode video: 13/13 chunk OK, concat + mux OK.
- Loudness đo lại bằng `loudnorm`: **−16,3 LUFS**, TP **−1,7 dBTP**, LRA 5,1 LU.
- Contact sheet 23 frame tại các mốc chính: `.work/gfx/_final_sheet.png`.
- Mật độ mực + vùng chết so sánh bản cũ / bản mới: `.work/compare_before_after.py`.

---

## 5. Tái chạy được cho tập 2–10

```powershell
cd 'D:\TEST\Gax\Audi'
$env:PYTHONIOENCODING='utf-8'
python .work\parse_plan.py        # -> .work/blocks.json
python .work\make_tts_args.py     # -> .work/tts/batch_01..NN.json
# gọi TTS: mcode-tools connector call connector__matrix__batch_text_to_audio --args-file .work\tts\batch_0N.json
python .work\fetch_audio.py       # -> .work/audio/*.mp3
python .work\build_audio.py       # -> Kc_1_Tap01.mp3 + .work/timeline.json
python .work\build_shots.py       # -> assets/gfx2/shots/*.png (62 shot) + .work/shots.json
$env:AUDI_VBR='1500'; $env:AUDI_NOISE='2'; $env:AUDI_MOVE='zoom'
python .work\build_video2.py      # -> .work/video/chunk_*.mp4 -> Kc_1_Tap01.mp4
python .work\deviation_report.py  # -> .work/duration_deviations.md
python .work\verify.py            # -> .work/gfx/_final_sheet.png
python .work\compare_before_after.py   # so sánh mật độ mực trước/sau
```

**Module dựng hình ảnh (dùng lại cho tập 2–10):**
`.work/shotlib.py` (thư viện) · `.work/scenes.py` (15 cảnh nền) ·
`.work/layouts.py` (3 bố cục A/B/C) · `.work/build_shots.py` (**danh sách shot
+ vòng dựng**) · `.work/build_video2.py` (ffmpeg).

Để làm tập mới: copy `build_shots.py`, thay danh sách `SHOTS` (mỗi block lời →
1 shot với `layout`, `scene`, `label`, `headline`, `sub`), rồi chạy lại
`build_shots.py` + `build_video2.py`. **Cần viết lại phần mô tả hình ảnh cho
từng block** — đó chính là phần quyết định video có hấp dẫn hay không.

**Thả ảnh thật vào `assets/photos/<tên>.jpg`** (vd `portrait.jpg`, `house_flat.jpg`) —
pipeline sẽ **tự ưu tiên ảnh thật** thay cho đồ hoạ phẳng tự dựng, không cần sửa code.
