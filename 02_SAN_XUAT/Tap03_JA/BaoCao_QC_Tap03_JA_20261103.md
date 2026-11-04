# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 03 (BẢN TIẾNG NHẬT) · 03/11/2026

**Thẩm phẩm:** `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4`
**Nguồn:** audio master `Tap03_JA_master.mp3` (1927.910 s) → wav `audio_master_JA_t03.wav` (1927,910 s)
**Căn cứ:** `timeline_s_JA_t03.json` (`total` = 1927.91 s) · `shots_JA_t03.json` (110 shot) · kịch bản `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md` (218 câu)
**Nguyên nhân dựng:** chưa có bản mp4 nào cho Tập 03 JA. Dựng **100 % hình** từ timeline JA + bảng shot JA ⇒ H14 thỏa đáng vì mốc thời gian lấy **chỉ từ timeline JA**.

---

## 1. Số đo thật (đo trên chính file thành phẩm)

| Mục | Giá trị | Chuẩn | Kết quả |
|---|---|---|---|
| Thời lượng mp4 cuối | **1927.900 s** (0:32:07) | — | *(số liệu)* |
| `timeline.total` | 1927.91 s | khớp ±0,05 s | ✅ lệch **0.010 s** |
| Audio master (mp3) | 1927.910 s | khớp ±0,05 s | ✅ lệch 0.000 s |
| LUFS — mp4 cuối | **-16.3 LUFS** | −16 ± 1 | ✅ |
| True peak — mp4 cuối | **-3.3 dBFS** | ≤ −1,5 | ✅ |
| LRA — mp4 cuối | 4.5 LU | — | *(số liệu)* |
| LUFS / true peak — master wav | -16.2 LUFS / -1.6 dBFS | — | *(số liệu)* |
| Số khung | **57,837** khung | `int(1927.91 × 30)` = 57,837 | ✅ |
| Video | h264 · 1920×1080 · 30/1 | H.264 1080p30 | ✅ |
| Audio | aac · 48000 Hz · 2 kênh · 197 kbps | AAC | ✅ |
| Dung lượng | **650.3 MB** (650,283,118 byte) | — | *(số liệu)* |
| Bitrate tổng | 2.70 Mbps | — | *(số liệu)* |
| **Lệch âm thanh – hình** | **0.0 ms** (4 cửa sổ, r = 0.9986–1.0000) | ≤ 20 ms | ✅ (A11 #64) |
| Giải mã toàn file | **0 lỗi** | 0 | ✅ |
| Phụ đề | **238 cue** · cue cuối ≤ `timeline.total` | phủ 100 % lời thoại | ✅ |
| Thẻ kết | có chữ ở giữa shot cuối | H12 | ✅ |
| Số shot | **110** (TB 17.3 s · dài nhất 56.4 s `3-14` · ngắn nhất 0.8 s `1-10`) | 3–15 s | ⚠ 64/110 shot ngoài 3–15 s (mục 5) |
| Nền lặp liên tiếp | tối đa **3** shot | ≤ 4 shot | ✅ H10 |
| Ảnh tĩnh | **110/110** render + soi 5 hồi bằng mắt | H9 | ✅ |
| **Ảnh tĩnh ↔ khung hình thật trong mp4** | **110/110 khớp (MAE TB 3.86 / lớn nhất 5.51, số vượt 15: 0/110)** | MAE < 15 | ✅ |
| Handoff badge | **9** shot có handoff | A11 #88 | ✅ |
| `⊘` (tắt bán thân) | **37** shot | H10 | ✅ |
| `mo_ta.txt` / `description.txt` | **2,658 ký tự** · **24 link nguồn ✅** | ≤ 5.000 ký tự | ✅ |
| Thumbnail | nền `t3_brain_mirror` + chữ JA | H11 | ✅ |
| Mốc chương trong mô tả | 00:00 / 00:23 / 06:33 / 12:24 / 19:33 / 26:01 | đo từ timeline | ✅ T11 |

**Kết luận cổng QC: 32/32 cổng đạt — 0 lỗi** (mục 5 là cảnh báo, không phải lỗi).

---

## 2. Bảng cổng QC đầu ra

| Cổng | Kết quả |
|---|---|
| G0 | ✅ shots.total == timeline.total  shots=1927.91 timeline=1927.91 |
| G0 | ✅ master mp3 == timeline.total (±0,05s)  mp3=1927.910 |
| G0 | ✅ wav master == timeline.total (±0,05s)  wav=1927.910 |
| G1 | ✅ picture.mp4 == timeline.total (±0,05s)  picture=1927.900 timeline=1927.910 lech=0.010 |
| G2 | ✅ đủ 1 video + 1 audio  v=1 a=1 |
| G2 | ✅ video 1920x1080 @30fps h264  h264 1920x1080 @30/1 |
| G2 | ✅ audio 48kHz stereo aac  aac 48000Hz 2ch |
| G2 | ✅ dung lượng > 100 MB  650.3 MB |
| G2 | ✅ faststart (moov trước mdat)  moov@36 mdat@1664207 |
| G4 | ✅ mp4 cuối == timeline.total (±0,05s)  mp4=1927.900 timeline=1927.910 lech=0.010 |
| G5 | ✅ số khung == int(total*30)  thuc=57837 mong doi=57837 |
| G3 | ✅ giải mã toàn file: 0 lỗi  0 dòng lỗi |
| G6 | ✅ LUFS mp4 trong −16±1  LUFS=-16.3 |
| G6 | ✅ true peak mp4 ≤ −1,5 dBFS (A7)  peak=-3.3 dBFS |
| G6 | ✅ 0 khoảng lặng > 0,3 s @ −60 dB  0 [] |
| G6 | ✅ 0 khoảng lặng ≥ 2,5 s @ −35 dB  0 [] |
| G6 | ✅ lời đầu tiên > 20,5 s (sau intro)  lời đầu=23.00s |
| G7 | ✅ phủ câu 218/218, 0 thiếu/thừa/trùng  phu=218/218 thieu=0 thua=0 trung=0 |
| G7 | ✅ thứ tự câu khớp timeline |
| G8 | ✅ SRT khối hợp lệ, không dòng rỗng  238 cue · khoi loi=0 · dong rong=0 |
| G8 | ✅ cue cuối ≤ timeline.total  het 1915.75s |
| G8 | ✅ 0 cue chồng nhau  0 chồng |
| G9 | ✅ font YuGothB.ttc phủ hết ký tự  0 thiếu [] |
| G9 | ✅ font YuGothM.ttc phủ hết ký tự  0 thiếu [] |
| G10 | ✅ 0 ký tự tiếng Việt trong chữ trên hình + SRT  0 nơi [] |
| G11 | ✅ thẻ kết có chữ (không đen)  t=1920.9s pixel sang>140 = 4.67%  -> endcard_ja_t03.png |
| G12 | ✅ nền lặp liên tiếp ≤ 4 shot  max=3 |
| G12 | ✅ shot cuối là thẻ kết (5-21) không gắn câu  5-21 |
| G13 | ✅ mô tả ≤ 5.000 ký tự (T15)  2658 ký tự · 24 link |
| G13 | ✅ không còn [PENDING |
| G13 | ✅ description.txt == mo_ta.txt  2658 vs 2658 |
| G13 | ✅ thumbnail 1280x720  (1280, 720) |

---

## 3. Lỗi thật đã tìm ra và sửa

| # | Lỗi | Mức độ | Cách sửa |
|---|---|---|---|
| 1 | **Chuỗi limiter khi ghép của bản JA thiếu `latency=1` và để trần quá cao.** `edition.py` EP03 khai `mux_af` theo nhánh `if EN else …` ⇒ bản **JA** rơi vào `alimiter=limit=0.7943:attack=5:release=50:level=disabled` (**không** có `latency=1`). Đo được: master wav JA có **đỉnh mẫu −1,903 dBFS** ⇒ trần −2,0 dBFS chỉ bóp đúng **1 mẫu** ⇒ AAC dựng lại vọn true peak lên ~+1,8 dB (đúng như bản EN đã ghi nhận: −2,5 dBFS → −0,7 dBFS) ⇒ **vượt trần A7 −1,5 dBFS**. Đồng thời thiếu `latency=1` ⇒ lệch A/V ~4,98 ms | Âm thanh vượt chuẩn + lệch hình | Dùng **đúng chuỗi đã chứng minh cho bản EN**: `alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1` (trần −4 dBFS ⇒ bóp 14.529 mẫu = **0,0157 %** tổng thời lượng, không gây pumping; `latency=1` bù trễ ⇒ lệch A/V ≈ 0 ms). Sửa **riêng nhánh JA** trong `edition.py`, **không** đụng chuỗi của EN/KO/VN |
| 2 | **Bản timeline đọc lúc 22:24 khác bản 22:40.** Lần đọc đầu cho `total` = 1936,71 s; file bị ghi đè lúc 22:40:06 (cùng lúc `build_video3.py` / `edition.py` / `package.py`) ⇒ `total` = 1927.91 s | Timeline stale ⇒ lệch 8,8 s toàn video | Đối chiếu **22 mốc** bằng ASR (`connector__matrix__listen_audio`) giữa audio master và timeline mới ⇒ lệch trung bình −0,50 s, max +0,10 / min −1,36 (sai số timestamp ASR) ⇒ **timeline mới khớp tuyệt đối**, bản 1936,71 là file stale. Mọi mốc thời gian lấy **chỉ từ `timeline_s_JA_t03.json`** (H14) |
| 3 | **`intro_kenh.mov` là bản tiếng Việt** — không dùng cho bản JA | Ảnh sai | Sinh intro riêng `make_intro.py` (`AE_LANG=ja AE_EP=03`) → `assets/brand/intro_kenh_JA_t03.mov` (22,40 s). **Đo parity**: profile độ sáng 10 mốc thời gian khớp intro chuẩn `intro_kenh.mov` trong sai số **0,45 điểm %** ⇒ đúng thiết kế (fade-in đen 0–1,5 s là cố ý) |
| 4 | **Chưa có bản stems JA** ⇒ renderer vỡ `FileNotFoundError` khi vẽ badge sóng âm | Render hỏng | Dựng lại `stems_JA_t03` (5 vai H/D/C/N1/N2) **từ master mp3 theo mốc timeline** (16 kHz mono, 1928,91 s) |
| 5 | **12 tiêu đề quá dài** trong bảng chữ JA (nguy cơ orphan ≤ 3 ký tự và cắt giữa từ Latin) | Chữ trên hình | Rút gọn 12 tiêu đề (`1-02`, `1-18`, `1-24`, `3-11`, `3-16`, `3-20`, `4-05`, `4-06`, `4-17`, `5-08`, `5-10`, `5-12`) — giữ nguyên mọi tên riêng tiếng Anh (The Jury Room, Big Ed, The Co-ed Killer, Criminal Personality Research Project, VICAP, The Lust Murderer, The Silence of the Lambs, Mindhunter) |
| 6 | **12 lỗi cấu trúc chữ** (mất tiều tố "01 ·", tiêu đề hồi, `3-03`/`4-05`/`5-12`/`3-17`/`3-05`/`4-09`) | Chữ trên hình | Sửa ở `.work/shots_text_tap03_JA.json` + mục 6 của `KeHoach_Video_Tap03_JA.md`, chạy lại `parse_shots.py` ⇒ **cùng số segment, cùng chuỗi bold/ital/quote, cùng số mục T8** so với bản VN (QC hình học PASS 110/110) |

**Thêm 2 lỗi trong chính bộ QC** (đã sửa để cổng đo đúng):

| Lỗi | Sửa |
|---|---|
| Cổng "intro không đen" báo FAIL ở t = 1 s | Đo lại: t = 1 s đen là **fade-in cố ý** (profile khớp intro chuẩn VN/EN). Đổi cổng sang **parity với `intro_kenh.mov`** |
| Cổng hồi quy `mux_af` báo "không khác biệt" dù đã sửa | `EPISODES` dùng khoá **2 chữ số** (`"03"`), mã so sánh dùng `str(ep)` = `"3"` ⇒ **mọi lần tra đều trượt**, trả `None` cho cả hai bản. Sửa: `"%02d" % ep` ⇒ kết quả đúng: **chỉ (03, ja) khác biệt** |

---

## 4. Quy trình dựng

| Bước | Nội dung |
|---|---|
| 1 | `parse_shots.py` (`AE_LANG=ja AE_EP=03`) → `shots_JA_t03.json` (110 shot) · `subtitles.py` → `Tap03_JA.srt` (238 cue, phủ 218/218 câu, 0 thừa/0 trùng/0 đảo thứ tự) |
| 2 | `make_intro.py` → `assets/brand/intro_kenh_JA_t03.mov` · `_build_stems_ja_t03.py` → `.work/stems_JA_t03/` |
| 3 | `build_video3.py --stills all` → 110 ảnh tĩnh → 5 contact sheet → **soi bằng mắt toàn bộ** (H9) |
| 4 | `build_video3.py --workers 6` → 6 part × ~9.640 khung → concat `-c copy` → `picture.mp4` |
| 5 | `package.py --mux` → `Tap03_JA_master.mp4` (+ `thumbnail.png` + `description.txt`/`mo_ta.txt`) |
| 6 | QC: 13 cổng đầu ra + lệch A/V (FFT + self-test) + ảnh tĩnh ↔ khung hình thật |

---

## 5. Cảnh báo (không phải lỗi)

| Cảnh báo | Giải thích |
|---|---|
| **64/110 shot ngoài khoảng 3–15 s** (TB 17.3 s; dài nhất 56.4 s `3-14`; ngắn nhất 0.8 s `1-10`) | H10 ghi "3–15 s" nhưng **không có cổng QC nào đo**; đây là quy ước của dự án (Tập 06: 42/73 shot > 15 s · Tập 07: 40/66 shot). Tập 03 JA dài hơn bản EN/VN vì **tiếng Nhật đọc chậm hơn** (> 15 s = 64 shot JA vs 52 EN vs 58 VN). Ghi nhận, không sửa (sửa = dựng lại ~55 phút) |
| **Nhãn vai N1/N2 trên hình là nhãn chung của bản JA** (`証人` = chứng nhân, `視聴者` = người xem), trong khi bản EN dùng nhãn riêng theo tập (`SANTA CRUZ DESK OFFICER` / `BAR COLLEAGUE OFFICER`) và bản VN dùng `EP["n1"]/EP["n2"]` | `edition.py` chưa có khối `roles_ja` ⇒ nhánh JA rơi về bộ nhãn dùng chung cho **mọi** tập JA. Với Tập 03, N2 đúng là người kể (Big Ed, đồng nghiệp tại The Jury Room) nên nhãn `視聴者` **chung chung, không sai tập**. Dữ liệu nhãn riêng đã có sẵn trong `edition.py` (`n1`/`n2` của EP03). **Không tự sửa** vì sửa = đổi badge + `.srt` + **dựng lại toàn bộ ~55 phút**, và sẽ làm Tập 03 JA lệch với các tập JA khác. Đã ghi vào mục 8 |
| **Khung 3 s cuối file mờ dần đen** | Renderer mờ dần 3 s cuối (dùng chung T01–T03) ⇒ đã kiểm thẻ kết ở **giữa shot cuối**, có chữ ✅ |

---

## 6. Nguồn tham khảo (A10)

`02_SAN_XUAT/Tap03_JA/nguon_tham_khao_JA.md` — **24 nguồn công khai** đánh dấu ✅ (hồ sơ tòa án, FBI Law Enforcement Bulletin, OJP, báo chí, Wikipedia). Khối nguồn đã được **chèn vào mô tả YouTube** (24/24 link, kiểm bằng script gọi `verified_links()` của `package.py`). File nguồn **không** bị ghi đè khi sinh mô tả (chỉ đọc).

---

## 7. Sao lưu (L5)

| Bản cũ | Đường dẫn |
|---|---|
| `edition.py` (trước khi sửa `mux_af` cho JA) | `.work/_cu/ja_t03_fix_20261103/edition.py.bak_muxaf` |

---

## 8. Việc còn lại của người dùng

1. **Nghe duyệt** — nghe `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4` (hoặc master mp3) và đối chiếu với `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md`.
2. **Quyết định về nhãn vai riêng cho bản JA** — có sẵn `n1`/`n2` cho EP03 trong `edition.py`; nếu muốn badge + phụ đề ghi đúng vai (`サンタクルーズ警察当直` / `酒場の同僚警察官`) thì cần thêm khối `roles_ja`/`sub_tags_ja` cho EP03 ⇒ **dựng lại toàn bộ (~55 phút)** và Tập 03 JA sẽ khác các tập JA khác (hiện chúng dùng nhãn chung).
3. **Đăng thì nhớ dọn đĩa theo `AGENTS.md` §11** — xoá `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4`, `Tap03_JA_master.mp3`, `thumbnail.png`, `.work/video3_JA_t03/`, `.work/stems_JA_t03/`, `.work/audio_master_JA_t03.wav`, `assets/brand/intro_kenh_JA_t03.mov` (**giữ** `intro_kenh.mov` + `intro_kenh_EN.mov` và mọi file text).

---

## 9. Script QC đã chạy (tái lập được)

| Script | Cổng | Kết quả |
|---|---|---|
| `.work/_qc_preflight_ja_t03.py` | intro parity · 110 ảnh tĩnh · 5 stems · 46 nền | ✅ |
| `.work/_measure_audio_ja_t03.py` | LUFS / LRA / true peak / khoảng lặng của master wav | ✅ |
| `.work/_qc_limiter_impact_ja_t03.py` | mức bóp đỉnh của limiter (1 mẫu vs 14.529 mẫu) | ✅ |
| `.work/_qc_regress_muxaf_ja_t03.py` | hồi quy `mux_af` 29 tập × 4 ngôn ngữ (L9) | ✅ chỉ (03, ja) đổi |
| `.work/_qc_final_ja_t03.py` | **13 cổng đầu ra** | **32/32 đạt** ✅ |
| `.work/_qc_sync_ja_t03.py` | lệch A/V (FFT + self-test chống chỉ số sai) | **0.0 ms** ✅ |
| `.work/_check_stills_vs_video_ja_t03.py` | ảnh tĩnh ↔ khung hình thật | **110/110 khớp (MAE TB 3.86 / lớn nhất 5.51, số vượt 15: 0/110)** ✅ |
| `.work/_qc_shape_ja_t03.py` | hình học chữ JA vs VN | PASS 110/110 ✅ |

---

## 10. Bài học đã ghi nhận (L6)

| Nơi | Nội dung |
|---|---|
| `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` | Cần thêm mục cho: **chuỗi limiter của bản JA EP03 thiếu `latency=1`** (A11) · **tra khoá `EPISODES` bằng `str(ep)` thay vì `"%02d" % ep`** làm cổng hồi quy hỏng âm thầm · **cổng "không đen" phải là parity với intro chuẩn**, không phải ngưỡng tuyệt đối |
| `AGENTS.md` | Giữ nguyên nguyên tắc: mọi thay đổi `edition.py` phải kèm hồi quy L9 theo **tập × ngôn ngữ**, và **không** đụng chuỗi của các bản đã xuất |

---

## 11. Bối cảnh âm thanh (đã QC trước, không thuộc lượt này)

`.work/quality_qc_utmos_ep03_ja.json` — ASR + CER + UT-MOS cho **218/218 câu**:
CER trung bình **0,136** (median 0,107); UT-MOS trung bình **2,98**.
Các câu CER cao (> 0,3) đều là **từ mượn tiếng Anh trong tiếng Nhật** (ví dụ `3.05#3` "Psychological Castration" → ASR ghi "サイコロジカルカストレーション") ⇒ là **sai số chuyển âm của ASR**, không phải lỗi master. Master wav đo được: LUFS -16.2, true peak -1.6 dBFS, **0 khoảng lặng > 0,3 s @ −60 dB**, **0 khoảng lặng ≥ 2,5 s @ −35 dB**.

### Mức bóp của limiter khi ghép (đo trên master wav)

```
wav: 92539679 frames · 2 ch · 16 bit · 48000 Hz · 1927.910 s
đỉnh mẫu (max|stereo|) = -1.903 dBFS
  trần -2.0 dBFS (0.7943 (mặc định)): 1 mẫu = 0.000 s · 0.0000% · 1 đoạn liên tiếp
  trần -3.0 dBFS (0.708): 1582 mẫu = 0.033 s · 0.0017% · 640 đoạn liên tiếp
  trần -4.0 dBFS (0.63 (đã sửa)): 14529 mẫu = 0.303 s · 0.0157% · 3239 đoạn liên tiếp
  chỉ 1 đỉnh vượt -2 dBFS (dưới ngưỡng thống kê)
```

**Kết luận:** trần −4 dBFS bóp **14.529 mẫu = 0,0157 %** (0,303 s rải rác 3.239 đoạn rất ngắn) ⇒ không gây pumping; trần −2 dBFS mặc định chỉ bóp **1 mẫu** ⇒ không đủ chắn để giữ true peak dưới −1,5 dBFS sau khi AAC dựng lại.
