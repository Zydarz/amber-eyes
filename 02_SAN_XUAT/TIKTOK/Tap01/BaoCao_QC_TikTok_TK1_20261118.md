# Báo cáo QC clip TikTok TK1 (Tập 01) — 18/11/2026

> 14 cổng QC theo `02_SAN_XUAT/TIKTOK/Tap01/KE_HOACH_CLIP_TAP01.md` §10. **Đo thật trên file mp4 cuối**, không "nói xong".
> Thành phẩm: `02_SAN_XUAT/TIKTOK/Tap01/clip01_TK1.mp4` (media → **không commit**, L10).

---

## 0. Tóm tắt

| Hạng mục | Kết quả |
|---|---|
| **File** | `clip01_TK1.mp4` · 1080×1920 · 30 fps · H.264 + AAC · **28,7 MB** · **66,60 s** |
| **Cổng QC** | **14/14 ĐẠT** |
| **Âm lượng** | I = **−16,0 LUFS** · true peak **−1,6 dBFS** (đo trên mp4 cuối) |
| **Chữ trên hình** | 100 % nguyên văn lời đọc (G6) · hook là trích nguyên văn của `TK1.01#1` (H6) |
| **An toàn TikTok** | mọi chữ nằm trong x 120–780, y 240–1.260 · không watermark nền tảng khác · không mặt người thật |
| **Còn lại** | người dùng nghe duyệt giọng (G10) + bật toggle AIGC khi đăng |

---

## 1. Cổng QC — kết quả đo

| # | Kiểm | Ngưỡng | Đo được | KQ |
|---|---|---|---|:--:|
| 1 | Khung / tỉ lệ | 1080 × 1920, 9:16 | 1080 × 1920 | ✅ |
| 2 | Codec / fps | H.264 + AAC, 30 fps | h264 + aac, 30,0 fps, yuv420p | ✅ |
| 3 | Dung lượng | ≤ 500 MB | 28,67 MB | ✅ |
| 4 | Độ dài | 45–95 s | 66,60 s | ✅ |
| 5 | Âm lượng | −16 ± 1 LUFS | **−16,0 LUFS** | ✅ |
| 5 | True peak | ≤ −1,5 dBFS | **−1,6 dBFS** | ✅ |
| 6 | Khoảng câm | 0 khoảng > 0,3 s @ −60 dB | **0** | ✅ |
| 7 | Lệch hình/tiếng | ≤ 0,05 s | **0,0000 s** | ✅ |
| 8 | Giải mã | 0 lỗi | **0 lỗi** (`ffmpeg -v error -f null -`) | ✅ |
| 9 | Safe zone | mọi chữ trong x 120–780, y 240–1.260 | **0 vi phạm** (đo trên mask chữ thật) | ✅ |
| 10 | Watermark | 0 khung có watermark nền tảng khác | nền AI sinh mới, không có watermark | ✅ |
| 11 | Chữ | 0 chữ rác · 0 chữ trùng · 0 chữ chìm | tương phản thấp nhất **7,11 : 1** (ngưỡng 4,5) | ✅ |
| 12 | Mặt người thật | 0 vi phạm | nền là tranh minh họa AI; nhân vật là ẩn dụ (búp bê trong tay), không phải người thật | ✅ |
| 13 | Từ cấm V9 | 0 từ trong danh sách A9.2 | **0** | ✅ |
| 14 | Hook | 3 giây đầu có chữ hook đọc được ở 100 % khung | mask chữ 24.425 px, hiện đủ ở t = 0,6 / 1,5 / 2,4 s | ✅ |

**G6 (chữ = nguyên văn lời đọc):** 24 chunk phụ đề ghép lại **khớp 12/12 câu** của `timeline_tk1.json` (tự động so từng từ).
**H6 (hook nguyên văn):** chữ hook *"cô ấy bước vào phòng thẩm vấn"* là trích nguyên văn của câu `TK1.01#1` → không vi phạm "chữ không có trong lời đọc".

---

## 2. Bố cục đã dựng (đúng `KE_HOACH_CLIP_TAP01.md` §4)

| Thành phần | Vị trí đã dùng | Cỡ chữ | Ghi chú |
|---|---|---|---|
| **Chữ hook** (0–3 s) | x 120–780, y 300–700 | 76 px Bold (tự co nếu tràn 2 dòng) | màu amber `#FFD68C`, có scrim mềm |
| **Phụ đề burn-in** | x 120–780, y 1.020–1.230 | 52 px Semibold (tự co 52→44 nếu quá 2 dòng) | nền scrim mềm tràn chiều rộng, **nguyên văn** lời đọc |
| **Thẻ overlay** | x 120–780, y 780–980 | 44 px Bold (3 dòng) | card tối 60 %, bo góc 12 px, hiện 2,5 s sau `TK1.01#6` rồi fade 0,4 s |
| **Logo** | x 120–260, y 60–160 | — | logo mắt cú `assets/brand/logo.png` (đã cắt alpha, canh giữa) |
| **Nền** | phủ kín 1080×1920 | — | 8 nền dọc `assets/bg/tk01_*.png`, camera move theo SPEC |

**Chuyển động** (đúng cột `chuyen_dong` của SPEC): `still` #1 · `pull` #2 · `push` #3 · `still` #4 · `pan` #5 · `pull` #6 · `push` #7 · `pan` #8 · `still` #9 · `pull` #10 · `push` #11 · `still` #12. Zoom 1,00→1,05 (push), 1,05→1,00 (pull), pan 1,03.

**Phụ đề chia theo nhịp đọc:** mỗi câu dài được chia thành chunk ~2,6 s (24 chunk cho 12 câu), mỗi chunk tối đa 2 dòng, hiển thị đúng khoảng thời gian tương ứng với câu đó — đọc theo mà không nhảy chữ.

---

## 3. Âm thanh

| Thành phần | Nguồn | Mức |
|---|---|---|
| Giọng | `TK1_master_audio.wav` (master người dùng tạo) | giữ nguyên |
| BGM | `assets/bgm/bgm_sub_drone.mp3` (MiniMax Music — **được phép TikTok**) | −26 dB khi có lời · −14 dB ở đoạn nghỉ, ducking attack 0,12 s / release 0,40 s |
| SFX | **tự tổng hợp** (room tone + tiếng máy ghi âm "Tách") | −38 dB / −34 dB so với giọng |
| Nền môi trường | luôn có lớp nền ⇒ **0 khoảng câm** (A1/V4) | — |

> **Không dùng** 2 BGM + 211 SFX của YouTube Audio Library (không có license cho TikTok).
> Chuẩn hoá 2 lượt `loudnorm` → **I = −16,0 LUFS, true peak = −1,7 dBFS** trên wav; sau khi mã hoá AAC 256 kbps đo lại trên mp4: **−16,0 LUFS / −1,6 dBFS** (A7 đo trên mp4 cuối).

---

## 4. Điểm cần người dùng nghe (không đo được bằng máy)

| Việc | Ghi chú |
|---|---|
| **G10 — nghe mù** | Ghép 12 câu theo vai (H / D / C) thành 3 file nghe: phải ra đúng **1 người** mỗi vai, 3 vai tách bạch |
| **G8 — bộ tham số** | So câu `TK1.01#11` (emotion `sad`, vai C) với `#8`/`#9` (neutral): cùng một người, không đổi giới/tim |
| **Chất lượng phát âm** | Audio dùng nguyên bản như báo cáo QC TK1: **6 câu có lỗi phát âm thật** (`#4 #5 #7 #9 #10 #12`) — nghe để quyết định có sinh lại hay chấp nhận |
| **Đăng** | Bật toggle **"AI-generated content"** + kèm dòng: *"Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự."* |

---

## 5. File liên quan

| File | Vai trò |
|---|---|
| `02_SAN_XUAT/TIKTOK/Tap01/clip01_TK1.mp4` | **thành phẩm** (media, không commit) |
| `02_SAN_XUAT/TIKTOK/Tap01/Caption_TK1.txt` | caption + hashtag + ghi chú đăng AIGC |
| `02_SAN_XUAT/TIKTOK/Tap01/timeline_tk1.json` | 12 câu · vai · mốc thời gian (nguồn của phụ đề) |
| `02_SAN_XUAT/TIKTOK/Tap01/SPEC_AUDIO_CLIP_TAP01.json` | đặc tả nền / chuyển động / thẻ overlay |
| `02_SAN_XUAT/TIKTOK/Tap01/BaoCao_QC_TK1_Audio_20261118.md` | QC audio (G12 CER + G9 F0) — đọc kèm |
| `.work/_build_tk01_audio.py` | mix giọng + BGM ducking + SFX + loudnorm |
| `.work/_build_tk01_video.py` | dựng khung + chữ + camera move + encode |
| `.work/_qc_tk01_clip.py` | 14 cổng QC (đo trên mp4 cuối) |
| `.work/_qc_tk01_clip.json` · `.work/_tk1_build_manifest.json` | dữ liệu đo dạng máy đọc được |

**Tái lập:**

```powershell
py -3 .work\_build_tk01_audio.py     # audio mix -> .work/_tk1_mix_norm.wav
py -3 .work\_build_tk01_video.py     # render -> .work/_tk1_video_nosound.mp4 (~20 phút)
py -3 .work\_qc_tk01_clip.py         # 14 cổng QC
```

> **Lưu ý kỹ thuật:** bản FFmpeg đi kèm repo **không có `libx264`** (`--disable-libx264`) ⇒ phải dùng **`libopenh264`** (đúng như `build_video3.py` của dự án). `libx264` sẽ báo *"Unknown encoder"* và làm hỏng tiến trình.
