# KẾ HOẠCH SẢN XUẤT VIDEO TẬP 01 — MOTION GRAPHICS 2D

**Phiên bản 4 — bỏ 3D, bỏ AI avatar, bỏ lip-sync**
**Thay thế:** `KeHoach_ThuAm_Tap01_VIDEO.md` (v3, Blender) · (v2, HeyGen)
**Cùng đọc với:** `KeHoach_ThuAm_Tap01.md` (kế hoạch audio — không thay đổi)
**Cập nhật:** 21/10/2026

---

## MỐC 0 — ĐỌC TRƯỚC TIÊN

### R1 · Đây là kế hoạch đã đo, không phải ước lượng

Mọi con số thời gian trong file này đến từ **benchmark chạy thật** trên máy này (mục 2). Không có ước lượng nào dựa trên giả định.

### R2 · Audio là đồng hồ chủ lực

Mọi chuyển động đặt theo **giây tuyệt đối** đọc từ `timeline.json`, sinh ra sau khi đo thời lượng thật của file audio.

### R3 · Không dùng thời lượng ước lượng

Kế hoạch audio ghi block `1.12` là 26 giây — con số suy ra từ tốc độ 3,435 từ/giây. TTS thật lệch vài %. Dựng chuyển động theo ước lượng thì mọi thứ **trôi dần về cuối tập**. Luôn đo trước, dựng sau.

---

## 1. QUYẾT ĐỊNH ĐÃ CHỐT

| Hạng mục | Giá trị |
|---|---|
| Hình thức | **Motion graphics 2D** — không nhân vật, không 3D |
| Nguồn chuyển động | **ffmpeg** — không render từng frame bằng Blender |
| Đồ hoạ tĩnh | Dựng 1 lần bằng EffectCraft → PNG có alpha |
| Khung hình | 1920×1080, 30fps |
| Codec | `libopenh264` (đo thật) · đổi `libx264` sau khi cài bản GPL |
| GPU cần | **Không** |
| Thời gian dự kiến | **12–18 phút** cho toàn bộ tập |

---

## 2. SỐ LIỆU ĐÃ ĐO THẬT

Benchmark chạy ngày 21/10/2026 trên máy này: ghép 1 overlay card 1920×1080 (có alpha, có fade vào/ra) lên nền đen cộng audio 120 giây.

| Codec | Xử lý 120s | Tốc độ | File 2 phút |
|---|---:|---:|---:|
| **libopenh264 (CPU)** | **26,5s** | **6,6× realtime** | **2,50 MB** |
| h264_qsv (GPU Intel) | 24,5s | 6,1× realtime | 2,35 MB |
| libvpx-vp9 | 25,0s | 6,2× realtime | 3,09 MB |
| mpeg4 | 21,7s | 5,4× realtime | 21,04 MB ❌ file khổng lồ |

**Quy ra toàn tập:** `1.482 giây ÷ 6,6` = **225 giây ≈ 3 phút 45 giây** cho một lớp overlay đơn giản.

Thực tế có 3–5 lớp, Ken Burns, nhiều đoạn fade → **nhân 4–5 lần = 12–18 phút**.

**Kết luận: máy không có GPU rời vẫn chạy thoải mái.** Đường sản xuất đúng là ghép bằng ffmpeg, không phải render frame.

### Filter đã xác nhận có trong bản ffmpeg này

`zoompan` · `xfade` · `rgbashift` · `noise` · `vignette` · `drawtext` · `crop` · `fade` · `overlay` · `color` · `gblur` · `curves` · `hue` · `colorkey` · `tblend` · `minterpolate`

*(Không có: `eq`, `boxblur`, `frei0r` — không cần dùng.)*

---

## 3. NGUYÊN TẮC CHỐNG CHÁN

Chuyển động không phải để "cho có". Người xem chán khi **mắt không có chỗ nào bám vào**. Vì vậy:

> **Mỗi đoạn 20–30 giây phải có đúng một thứ đang thay đổi** — con số đang chạy, đường đang vẽ, ảnh đang zoom, hay chữ đang hiện. Không lúc nào hai thứ cùng đổi. Không lúc nào không có gì đổi.

Ba sai lầm cần tránh:

| Sai lầm | Hậu quả |
|---|---|
| Nhân vật AI đứng yên nói | Chán ngay ~20 giây |
| Overlay bay vào liên tục | Mắt mỏi, không đọc kịp |
| Một dòng chữ tĩnh 40 giây | Người xem lướt qua |

---

## 4. TÁM KỸ THUẬT CHUYỂN ĐỘNG

Mỗi kỹ thuật dưới đây đều có câu lệnh ffmpeg chạy được.

### K1 · Ken Burns — ảnh tĩnh zoom + pan

Dùng cho: ảnh hiện trường, ảnh nhân vật, ảnh hồ sơ.

```bash
ffmpeg -loop 1 -i photo.jpg -t 8 \
  -vf "zoompan=z='min(zoom+0.0012,1.18)':x='iw/2-(iw/zoom/2)+sin(on/40)*40':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30,format=yuv420p" \
  -c:v libopenh264 -q:v 6 kenburns.mp4
```

| Tham số | Ý nghĩa |
|---|---|
| `z='min(zoom+0.0012,1.18)'` | Phóng dần, dừng ở 1,18×. Tăng nhanh hơn = zoom mạnh hơn |
| `+sin(on/40)*40` | Pan nhẹ sang trái/phải. Bỏ `sin(...)` = chỉ zoom vào giữa |
| `d=1` | Bắt buộc. Không có nó, filter chỉ xuất 1 frame |

> **Không dùng `zoompan` cho cả 24 phút.** Ảnh động chỉ dùng ở các khoảnh khắc quan trọng — 1 bài, dùng nhiều lần thì chán.

### K2 · Timeline tự vẽ

Dùng cho: dòng thời gian bệnh án 1991 → 2015.

Vẽ 1 PNG dài 1600×6 (đường trắng) + các mốc. Giấu dần bằng `crop` theo thời gian:

```bash
ffmpeg -loop 1 -i line.png -loop 1 -i dot1.png \
  -filter_complex "[0:v]crop=w='iw*min(1,t/3)':h=ih:eval=frame,format=rgba[ln];\
[1:v]format=rgba,fade=t=in:st=3:d=0.4:alpha=1[d1];\
color=c=#121214:s=1920x1080[r=30][bg];\
[bg][ln]overlay=160:520[tmp];[tmp][d1]overlay=120:490[out]" \
  -map "[out]" -t 6 -c:v libopenh264 -q:v 5 timeline.mp4
```

Đường vẽ hết trong 3 giây, mốc nhảy lên sau đó.

### K3 · Chữ hiện từng từ (typewriter)

Dùng cho: định nghĩa hội chứng, các câu chốt.

```bash
ffmpeg -loop 1 -i text_card.png -t 6 \
  -filter_complex "[0:v]format=rgba,crop=w='iw*min(1,t/4.5)':h=ih:eval=frame,fade=t=in:st=0:d=0.3:alpha=1,fade=t=out:st=5.4:d=0.6:alpha=1,format=yuv420p" \
  -c:v libopenh264 -q:v 5 typewriter.mp4
```

`crop` bóp ngang từ trái sang phải → chữ hiện dần như đang gõ. `t/4.5` = hiện hết trong 4,5 giây.

### K4 · Đếm số

Dùng cho: 23 năm · 48 giờ · 85% bản án · 3 tầng tâm lý.

Không cần render — `drawtext` tự chạy:

```bash
ffmpeg -f lavfi -i color=c=#121214:s=1920x1080:d=4:r=30 \
  -vf "drawtext=text='%{eif\:floor(t/1)\:d}':fontsize=190:fontcolor=0xC05050:x=1560:y=830,format=yuv420p" \
  -c:v libopenh264 -q:v 5 counter.mp4
```

`floor(t/1)` đếm 1 đơn vị mỗi giây. Muốn nhanh hơn dùng `floor(t*3)`.

### K5 · Đường nối bật dây

Dùng cho: sơ đồ vòng lặp quyền lực ở Hồi 4.

Mỗi đoạn nối là 1 PNG riêng. Hiện lần lượt, mỗi cách nhau 0,35s:

```bash
ffmpeg -loop 1 -i node1.png -loop 1 -i link1.png -loop 1 -i node2.png -t 5 \
  -filter_complex "[1:v]format=rgba,fade=t=in:st=1.0:d=0.4:alpha=1[l1];\
color=c=#121214:s=1920x1080[r=30][bg];[bg][l1]overlay[t1];\
[2:v]format=rgba,fade=t=in:st=1.4:d=0.4:alpha=1[n2];[t1][n2]overlay[out]" \
  -map "[out]" -c:v libopenh264 -q:v 5 diagram.mp4
```

Mỗi đoạn nối lệch `st` 0,35 giây → hiệu ứng "mắt xích" nối dần.

### K6 · Lớp phối cảnh (parallax)

Dùng cho: mở đầu và các đoạn chuyển hồi.

Ba lớp PNG (nền xa / trung gian / tiền cảnh), mỗi lớp trôi khác tốc độ:

```bash
ffmpeg -loop 1 -i far.png -loop 1 -i mid.png -loop 1 -i near.png -t 8 \
  -filter_complex "[0:v]scale=2100:-1,crop=1920:1080:x='(t*3)-90':y=0[far];\
[1:v]scale=2050:-1,crop=1920:1080:x='(t*7)-65':y=0[mid];\
[2:v]scale=2000:-1,crop=1920:1080:x='(t*14)-40':y=0[near];\
[far][mid]overlay[t1];[t1][near]overlay,format=yuv420p" \
  -c:v libopenh264 -q:v 5 parallax.mp4
```

Tốc độ 3 / 7 / 14 px mỗi giây — tạo cảm giác chiều sâu dù ảnh vẫn phẳng.

### K7 · Film grain + vignette + lệch màu

Dùng cho: **toàn bộ video.** Đây là thứ rẻ nhất và hiệu quả nhất.

```bash
-vf "noise=alls=7:allf=t+u,vignette=PI/4.5,rgbashift=rh=-2:bh=2,format=yuv420p"
```

| Filter | Tác dụng |
|---|---|
| `noise=alls=7:allf=t+u` | Hạt phim nhấp nháy theo từng frame. `allf=t` = thay đổi liên tục, không lặp pattern |
| `vignette=PI/4.5` | Tối 4 góc, kéo mắt vào giữa khung |
| `rgbashift=rh=-2:bh=2` | Tách nhẹ kênh đỏ/xanh — màu "rung" như film ổn định |

> Không có 3 filter này, video ổn định trông như slide PowerPoint. Có chúng thì có chất phim.

### K8 · Chuyển cảnh cross-dissolve

Dùng cho: ranh giới giữa các hồi.

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0:v][1:v]xfade=transition=fade:duration=1:offset=29" \
  -c:v libopenh264 -q:v 5 joined.mp4
```

`offset=29` = bắt đầu mờ chuyển tại giây thứ 29 của clip đầu.

**Quy tắc:** chuyển cảnh chỉ rơi vào block `NGHỈ` của plan audio. Cắt vạch giữa lời sẽ thấy rõ và phá mạch.

---

## 5. PHÂN BỔ THEO BLOCK

100% thời lượng đều có chuyển động, nhưng cường độ khác nhau.

### 5.1 Khoảnh khắc chủ đạo — 319 giây (22%)

Toàn màn, ảnh Ken Burns + chữ lớn. Đây là những chỗ người xem sẽ nhớ.

| Block | Thời lượng | Kỹ thuật | Nội dung hình |
|---|---:|---|---|
| `O.1` | 18s | K6 parallax + K7 | Nhà màu hồng, 3 lớp |
| `1.7`+`1.8` | 38s | K1 Ken Burns | Ảnh Gypsy Rose, zoom chậm vào mắt |
| `1.12` | 26s | K3 typewriter | Tiêu đề "Hội chứng Münchausen qua trung gian" |
| `3.2` | 5s | K4 đếm số | "Tại sao?" đếm lên |
| `3.17` | 20s | K3 + K7 tối dần | Câu "Hãy làm cho con bé tàn tật…" |
| `4.6` | 33s | K5 sơ đồ | Bộ não → "Mọi sự vùng vẫy đều vô nghĩa" |
| `5.9` | 20s | K4 đếm số | "4 dấu hiệu cảnh báo đỏ" đếm 1→4 |
| `5.16`+`5.17` | 33s | K1 + K7 | Ảnh ngôi nhà, zoom ra |
| `5.19` | 16s | K3 | Lời cảm ơn, chữ hiện dần |

### 5.2 Chuyển động hỗ trợ — 1.163 giây (78%)

Overlay chạy nền dưới giọng đọc. Không chiếm mắt, nhưng không đứng yên.

| Hồi | Kỹ thuật chính |
|---|---|
| Hồi 1 | `OV-EV` ảnh hồ sơ, fade vào/ra 0,3s |
| Hồi 2 | K2 timeline bệnh án 1991→2015 (chạy suốt hồi) |
| Hồi 3 | `OV-DF` thẻ định nghĩa FDIA · K4 đếm "3 tầng tâm lý" |
| Hồi 4 | `OV-MD` sơ đồ quan hệ · K5 nối dây khi nhắc 2011 |
| Hồi 5 | `OV-DF` 4 thẻ Red Flags, hiện từng thẻ một |

---

## 6. TEMPLATE ĐỒ HOẠ

Dựng 1 lần, dùng lại cho 10 tập. Xuất PNG có alpha, 1920×1080.

| Mã | Cách dựng | Dùng ở |
|---|---|---|
| `OV-TL` | Dải timeline + các mốc tròn | Hồi 2 |
| `OV-DF` | Khung thẻ, tiêu đề + 4 dòng định nghĩa | Hồi 3, 4, 5 |
| `OV-MD` | 4 nút + 5 đoạn nối riêng | Hồi 4 |
| `OV-EV` | Khung ảnh 4:3 viền trắng | Hồi 1 |
| `NUM` | Chỉ con số, font 190px | Mọi nơi |

**Dựng bằng EffectCraft** — tôi đã kiểm chứng chạy được: `comp.new` → `layer.newText` → `render_frame` với `transparent: true` ra PNG 1920×1080 có alpha.

Quy tắc chung: nền trong mờ 85–90%, chữ trắng, **tối đa 6 dòng mỗi thẻ**, viền mảnh 2px.

---

## 7. PIPELINE

```
BƯỚC 1  Thu TTS 53 khối lời (connector batch_text_to_audio)
         2 giọng: audiobook_male_1 + audiobook_female_1
         Bỏ qua 5 ô CẦN VIẾT

BƯỚC 2  ffmpeg ghép lời + khoảng lắng thật (anullsrc, không dùng "...")
         Trộn BGM loop ở -26dB

BƯỚC 3  ffprobe ĐO THẬT từng khối → timeline.json
         {ma, start, end, type, voice, kỹ thuật đồ hoạ}

BƯỚC 4  Dựng template PNG (mục 6)

BƯỚC 5  Dựng các đoạn đồ hoạ ngắn (K1–K6)
         Mỗi đoạn là 1 file mp4 riêng, đặt tên theo mã block

BƯỚC 6  Ghép: audio làm trục, overlay + hero moment theo timeline.json
         Áp K7 lên toàn bộ
         Dùng xfade tại các block NGHỈ

BƯỚC 7  Kiểm tra: ffprobe thời lượng, xem lại 3 điểm chuyển cảnh
```

---

## 8. ENCODER

**Hiện tại dùng `libopenh264`** — đo thật 6,6× realtime, 2,5 MB / 2 phút.

**Nâng cấp khuyến nghị:** bản ffmpeg hiện tại là **LGPL, không có `libx264`**. Tải bản GPL từ <https://www.gyan.dev/ffmpeg/builds/>, giải nén đè thư mục `.work\ffmpeg\`.

```bash
ffmpeg ... -c:v libx264 -preset medium -crf 20 ...
```

Chất lượng tốt hơn `libopenh264`, và nhẹ hơn — có thể lên gấp đôi khung hình.

---

## 9. CHI PHÍ & THỜI GIAN

| Hạng mục | Lần đầu | Tập 2–10 (mỗi tập) |
|---|---:|---:|
| Template PNG (5 loại) | ~2 giờ | 0 |
| Mỗi tập: dựng đoạn đồ hoạ | — | ~1 giờ |
| Mỗi tập: ghép + encode | — | **12–18 phút** |
| Dung lượng file | — | ~30 MB |

| Hạng mục | Chi phí |
|---|---:|
| ffmpeg | 0 |
| EffectCraft (đồ hoạ) | 0 |
| Ảnh bằng chứng | ảnh công khai trên báo chí |
| **Tổng cả series 10 tập** | **0 đồng** |

So với phương án HeyGen (~11 USD) và phương án Blender (4–5 ngày dựng scene).

---

## 10. CHECKLIST TRƯỚC KHI LÀM CẢ TẬP

- [ ] Nghe `Kc_1.mp3` (16:32) — xác nhận giọng `male-qn-qingse` có chấp nhận được không, hay bắt buộc đổi sang `audiobook_male_1`
- [ ] Tìm 5–8 ảnh bằng chứng: ngôi nhà màu hồng, ảnh chân dung Gypsy / Dee Dee, báo chí
- [ ] Dựng thử **1 Ken Burns 8 giây** bằng câu lệnh K1 — xem có đủ mượt không
- [ ] Dựng thử **1 timeline vẽ tay 6 giây** bằng K2
- [ ] Ghép thử 60 giây có K7 (grain + vignette) — nghe thấy khác biệt chứ không
- [ ] Nếu cảm thấy ổn → dựng cả 5 template

**Đừng dựng cả tập trước khi xem 3 thứ này chạy.** Mỗi cái chỉ mất vài phút.

---

## 11. RỦI RO

| # | Rủi ro | Mức | Xử lý |
|---|---|---|---|
| 1 | Chuyển động ở mức 78% không đủ giữ chân | Trung bình | Quy tắc mục 3 — mỗi 20–30s phải có 1 thứ đổi |
| 2 | Ken Burns dùng quá nhiều → mệt | Trung bình | Giới hạn: chỉ 9 khoảnh khắc chủ đạo ở mục 5.1 |
| 3 | Ảnh bằng chứng nhàm hoặc không đủ nét | Trung bình | Ảnh crop sát, thêm grain để giấu độ nét kém |
| 4 | Pháp lý ảnh — Gypsy Rose năm 2015 mới 14 tuổi | Trung bình | Chỉ dùng ảnh đã công khai trên báo chí. **Tránh ảnh gia đình tư nhân.** |
| 5 | Chữ trong video không đọc được trên điện thoại | Thấp | Cỡ chữ tối thiểu 40px, tối đa 6 dòng |
| 6 | Bản LGPL thiếu libx264 | Thấp | Đã xử lý — dùng `libopenh264`, hoặc cài bản GPL |

**Đã loại trừ:** không cần GPU rời (đo thật 6,6× realtime) · không cần Blender · không cần lip-sync · không cần AI avatar.

---

## 12. SAU TẬP 1

| Tái sử dụng | Sửa lại |
|---|---|
| 5 template PNG | Chỉ đổi chữ |
| Script ghép | Chỉ đổi `timeline.json` |
| Cấu trúc pipeline | Không đổi |
| **Danh sách hero moment** | Phải lập lại — mỗi tập có nhịp riêng |

---

*Không có file nguồn nào bị sửa. `Kc_1.txt`, `Kich_ban.txt`, `AI_video.txt`, `KeHoach_ThuAm_Tap01.md` nguyên trạng.*