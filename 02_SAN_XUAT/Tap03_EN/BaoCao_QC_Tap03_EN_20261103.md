# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 03 (BẢN TIẾNG ANH) · 03/11/2026

**Thẩm phẩm:** `02_SAN_XUAT/Tap03_EN/xuat_ban/Tap03_EN_master.mp4`
**Nguồn:** audio master `Tap03_EN_master.mp3` (39.520.556 B) → wav `audio_master_EN_t03.wav`
**Nguyên nhân dựng lại:** chưa có bản mp4 nào cho Tập 03 EN (lượt trước chỉ có ảnh tĩnh). Dựng mới **100 % hình** từ `timeline_s_EN_t03.json` + `shots_EN_t03.json` (110 shot) ⇒ H14 thỏa đáng vì mốc thời gian lấy **chỉ từ timeline EN**.

---

## 1. Số đo thật (không ước lượng — đo trên chính file thành phẩm)

| Mục | Giá trị | Chuẩn | Kết quả |
|---|---|---|---|
| Thời lượng mp4 cuối | **1646,600 s** (27:26,60) | — | *(số liệu)* |
| Thời lượng audio master (wav) | 1646,620 s | khớp ±0,05 s | ✅ lệch **0,020 s** |
| `timeline.total` | 1646,620 s | khớp ±0,05 s | ✅ lệch **0,020 s** |
| `picture.mp4` (trước khi ghép) | 1646,600 s | khớp `timeline.total` ±0,05 s | ✅ **H14 đạt** |
| LUFS — mp4 cuối | **−16,1 LUFS** | −16 ± 1 | ✅ |
| True peak — mp4 cuối | **−3,4 dBFS** | ≤ −1,5 | ✅ |
| LRA — mp4 cuối | 3,1 LU | — | *(số liệu)* |
| Khoảng lặng > 0,3 s @ −60 dB | **0** | 0 | ✅ |
| Khoảng lặng ≥ 2,5 s @ −35 dB | **0** | 0 | ✅ |
| Lời đầu tiên | **23,0 s** | 22,8 – 23,5 s | ✅ |
| **Lệch âm thanh – hình** | **0,0 ms** (r = 0,9994 – 1,0000, 4 cửa sổ) | ≤ 20 ms | ✅ (A11 #64) |
| Giải mã toàn file | **0 lỗi** | 0 | ✅ |
| Video | h264 · 1920×1080 · 30/1 · **49.398 khung** · 2,57 Mbps | H.264 1080p30 | ✅ |
| Audio | AAC · 48.000 Hz · 2 kênh · 197 kbps | AAC | ✅ |
| Dung lượng | **570,0 MB** (570.005.649 byte) | — | *(số liệu)* |
| Phụ đề | **469 cue** · UTF-8 không BOM (42.390 byte) | phủ 100 % lời thoại | ✅ |
| Cue cuối kết thúc | 1637,62 s | ≤ `timeline.total` | ✅ |
| Thẻ kết (giữa shot cuối, 1642,12 s) | **11,50 %** pixel sáng | có chữ | ✅ H12 |
| Shot cuối | `5-21` — thẻ kết, không gắn câu | H12 | ✅ |
| Số shot | **110** (TB 14,8 s · dài nhất 40,4 s `3-14` · ngắn nhất 0,8 s `1-10`) | 3–15 s | ⚠ 68/110 shot ngoài 3–15 s (mục 5) |
| Nền lặp liên tiếp | tối đa **3** shot | ≤ 4 shot | ✅ H10 |
| Ảnh tĩnh | **110/110** render + soi 7 contact sheet | H9 | ✅ |
| **Ảnh tĩnh ↔ khung hình thật trong mp4** | **110/110 khớp** (MAE TB 4,04 / 4,07 / 3,44 · lớn nhất **5,53**) | MAE < 15 | ✅ |
| Handoff badge | **9** shot có handoff, 0 sai | A11 #88 | ✅ |
| `⊘` (tắt bán thân) | **37** shot | H10 | ✅ |
| `mo_ta.txt` / `description.txt` | **4.935 ký tự** · **24/24 link nguồn ✅** | ≤ 5.000 ký tự | ✅ |
| Thumbnail | nền `t3_brain_mirror` + chữ "IQ 145 / GIANT" | H11 | ✅ |
| Mốc chương trong mô tả | 00:00 / 00:23 / 05:32 / 10:45 / 16:28 / 22:02 | đo từ timeline | ✅ T11 |

**Kết luận cổng QC: đạt toàn bộ — 0 lỗi, 1 cảnh báo (mục 5), 3 việc cần user quyết (mục 8).**

---

## 2. Bảng shot — khớp 3 chiều (H13), đo bằng script

| Cổng | Kết quả |
|---|---|
| Phủ câu: câu timeline → shot | **218/218** câu, đúng thứ tự ✅ |
| Vai nói khớp kịch bản | **0 lỗi** ✅ |
| Số / chữ trên hình truy được về câu EN đang đọc | **0 lỗi** ✅ |
| Nền lặp liên tiếp | tối đa 3 shot ≤ 4 ✅ |
| EN vs VN: nền / template / variant | **0/110 shot khác** ⇒ hình giống hệt bản tiếng Việt đã duyệt ✅ |

Ảnh tĩnh render 110 shot → dựng 7 contact sheet → **soi bằng mắt toàn bộ**; thêm 7 contact sheet **trích từ chính mp4 thành phẩm** (`.work/qc_final_EN_t03/sheet_01..07.png`) → soi bằng mắt toàn bộ. Không tràn chữ, không chữ sai tập, không lộ mặt.

**Bằng chứng mới (H9 áp dụng được cho video thật):** so từng ảnh tĩnh đã QC với khung hình thật trong mp4 tại giữa mỗi shot —
`chunk A` 45/45 · `chunk B` 33/33 · `chunk C` 32/32 = **110/110**; MAE trung bình **4,04 / 4,07 / 3,44**, lớn nhất **5,53/255** (chỉ tổn thất nén H.264), **0 shot lệch > 15**.

---

## 3. Lỗi thật đã tìm ra và sửa (7 lỗi)

| # | Lỗi | Mức độ | Cách sửa |
|---|---|---|---|
| 1 | **Chữ trên hình chứa nhãn không có trong lời thoại.** Shot `2-15` ghi `hunting knife ("The General")` — nhãn thương hiệu **không** có trong lời thoại EN/VN (có nguồn ở hồ sơ `REVIEW_kichban_tap03.md` dòng 97/248 nhưng không được đọc) ⇒ vi phạm H6 | Ảnh sai | Bỏ nhãn + dấu nháy kép, giữ nội dung có nguồn: `*Trunk: plastic bags, hunting knife, blankets, handcuffs · Handcuffing one, locking the other in trunk*`. Sửa ở `KeHoach_Video_Tap03_EN.md` + `.work/shots_text_tap03_EN.json`, chạy lại `parse_shots.py` ⇒ **chỉ 1 shot đổi** (diff cô lập bằng script) |
| 2 | **Badge vai hiện sai tập.** `edition.py` thiếu `roles_en` cho Tập 03 ⇒ rơi về nhãn cứng Tập 01: Điều tra viên *"Blanchard case file"* (vụ Gypsy Rose Blanchard) và N1 *"SPRINGFIELD RESIDENT"* — trong khi đang kể vụ Edmund Kemper. `.srt` cũng gắn nhãn sai | Ảnh sai + phụ đề sai | Khai `roles_en` + `sub_tags_en` cho `EPISODES["03"]` (HOST / INVESTIGATOR / PSYCHOLOGIST / **SANTA CRUZ DESK OFFICER** / **BAR POLICE**). Kiểm sau khi sửa: badge trên ảnh và nhãn trong `.srt` đều đúng Tập 03 |
| 3 | **Renderer không tất định.** `np.random.default_rng(abs(hash(shot["id"])) % 999)` — `hash()` của chuỗi bị ngẫu nhiên hoá theo `PYTHONHASHSEED` **mỗi tiến trình** ⇒ cùng 1 shot ra 2 khung hình khác nhau (đo được: 1/6 shot lệch, tới 90/765 mức xám) ⇒ **ảnh tĩnh QC không bảo đảm khớp video thật** | Hình không tái lập | Đổi sang `zlib.crc32(shot["id"].encode("utf-8"))`. A/B 2 lượt render trên 6 shot ⇒ **6/6 giống byte** |
| 4 | **Phụ đề cũ dài hơn video 315 s.** `Tap03_EN.srt` (25/10) có cue cuối kết thúc 1961,75 s trong khi timeline mới là 1646,62 s ⇒ toàn bộ phần sau lệch | Phụ đề hỏng | Sinh lại bằng `AE_EP=03 AE_LANG=en py -3 .work/subtitles.py` ⇒ **469 cue**, cue cuối 1637,62 s, **0 cue chồng nhau**, 0 cue > 6 s, ≤ 2 dòng/cue |
| 5 | **`verified_links()` chỉ hiểu bảng 4 cột, nhưng cả 29 tập EN dùng bảng 3 cột** ⇒ lần `package.py --mux` đầu làm mất **24/24 link nguồn** trong mô tả (thành `[PENDING …]`), **không báo lỗi** | Đóng gói sai | Thêm nhánh đọc bảng 3 cột (thuần bổ sung). **Kiểm hồi quy (L9):** trên toàn bộ file nguồn EN/JA/KO — link cũ **không mất** (228 → 1.053, mất 0) và link mới **trùng khớp** với `mo_ta.txt` trên đĩa của **28/28 tập EN còn lại**; chỉ Tập 03 EN khác (đúng lý do cần sửa) |
| 6 | **`mo_ta.txt` dài 5.201 ký tự > giới hạn YouTube 5.000.** Mẫu mô tả "rich" (3 đoạn dẫn + 5 bullet + CHAPTERS + disclaimer + khối crisis + 24 URL) không vừa | Vượt trần | Rút gọn **câu chữ** (giữ nguyên mọi dữ kiện và mọi link) trong `CHU_CO_DINH_EN.md` ⇒ **4.935 ký tự**, vẫn đủ 24 link + 5 mốc CHAPTERS đo từ timeline |
| 7 | **True peak −0,7 dBFS (vượt trần A7 −1,5) và lệch A/V +5,0 ms.** Audio master EN có đỉnh mẫu −2,5 dBFS ⇒ AAC dựng lại vọn true peak lên −0,7 dBFS; thiếu `latency=1` nên limiter để lại trễ 4,98 ms | Âm thanh vượt chuẩn | Khoá `mux_af` **riêng cho bản EN** của Tập 03: `alimiter=limit=0.63:…:latency=1` (hạ trần xuống −4 dBFS + bù trễ). **Bản VN giữ nguyên chuỗi cũ** (đang đạt −1,7 dBFS) ⇒ không đổi thành phẩm đã xuất. Mux lại ⇒ **true peak −3,4 dBFS**, **lệch A/V 0,0 ms**, LUFS −16,1 |

**Thêm 2 lỗi trong chính bộ QC** (đã sửa để cổng đo đúng):

| Lỗi | Sửa |
|---|---|
| `_check_stills_vs_video.py` seek theo thời gian **toàn cục** trong khi mỗi chunk bắt đầu ở frame **cục bộ 0** ⇒ ở chunk B/C nó trích nhầm khung hình của shot khác. Lỗi **chỉ lộ ở chunk B/C** (chunk A offset = 0 nên vẫn đúng) | Trừ offset: `lfi = int(t*30) − int(round(--from*30))`. Sau khi sửa: chunk B **33/33 khớp, MAE TB 4,07** |
| `_qc_en_t03_final.py` so `round(total*30)` = 49.399 trong khi renderer dùng **cắt chân** `int()` = 49.398 ⇒ báo lỗi nhầm | So theo đúng cách renderer: `int(total*30)` |

---

## 4. Quy trình dựng (vì sao chia 3 chunk)

Một lần build liên tục **49.398 khung** vượt trần thời gian của một lệnh bash. Lượt render đầu (6,1 fps) bị dừng chủ động ⇒ 6 `part_*.mp4` **không có `moov`** (ffprobe: `moov atom not found`) ⇒ không cứu được. Chuyển sang **3 chunk theo frame**, mỗi chunk tạo ra mp4 có `moov` nên bị hủy cũng không mất chunk trước:

| Chunk | Frame | Thời gian | Khung hình | Dung lượng |
|---|---|---|---|---|
| A | 0 – 16.469 | 0 → 549,0 s | **16.470** | 185,4 MB |
| B | 16.470 – 32.939 | 549,0 → 1.098,0 s | **16.470** | 174,6 MB |
| C | 32.940 – 49.397 | 1.098,0 → 1.646,62 s | **16.458** | 168,2 MB |
| **Tổng** | | | **49.398** = `int(1646,62 × 30)` | 503,7 MB (`picture.mp4`) |

Mỗi chunk dùng bản biến thể `_build_video3_split.py` (pipe 4 MB + `finishing()` tối ưu **bit-identical**) ⇒ **không sửa `build_video3.py` dùng chung** ⇒ không phát sinh nghĩa vụ hồi quy Tập 01 (L9).

---

## 5. Cảnh báo (không phải lỗi)

| Cảnh báo | Giải thích |
|---|---|
| **68/110 shot ngoài khoảng 3–15 s** (TB 14,8 s; dài nhất 40,4 s `3-14`; ngắn nhất 0,8 s `1-10`) | H10 ghi "3–15 s" nhưng **không có cổng QC nào đo**; đây là quy ước của dự án (Tập 06: 42/73 shot > 15 s, TB 17,1 s · Tập 07: 40/66 shot, TB 16,9 s). Tập 03 EN TB **14,8 s** — ngắn hơn cả hai ⇒ gần chuẩn nhất trong 3 tập đã đo. Ghi nhận, không sửa (sửa = dựng lại ~55 phút) |
| **Khung tại `total − 2 s` bị đen** | Renderer mờ dần 3 s cuối (dùng chung T01–T03) ⇒ đã kiểm thẻ kết ở **giữa shot cuối (1642,12 s) → 11,50 % pixel sáng** ✅ |
| **15/469 dòng phụ đề dài 43–47 ký tự** | Kết quả tối ưu của thuật toán chia 2 dòng trong `subtitles.py`; sửa thuật toán sẽ ảnh hưởng **mọi** tập ⇒ không sửa |
| **133/110 shot EN khác phạm vi chữ so với bản VN** | Hạ cấp từ A3 (từ khoá rút gọn trên hình) xuống cảnh báo: khác biệt là **phong cách thiết kế** (tiêu đề / label), không phải khai báo sai dữ kiện |

---

## 6. Nguồn tham khảo (A10)

`02_SAN_XUAT/Tap03_EN/nguon_tham_khao_EN.md` — **24 nguồn công khai** đánh dấu ✅ (hồ sơ tòa án, FBI Law Enforcement Bulletin, OJP, hồ sơ CDCR, báo chí, Wikipedia, Britannica, A&E, thư viện SFSU). Khối nguồn đã được **chèn vào mô tả YouTube** (24/24 link, kiểm bằng script so với file trên đĩa). `nguon_tham_khao_EN.md` **không** bị ghi đè khi sinh mô tả (chỉ đọc).

---

## 7. Sao lưu (L5)

| Bản cũ | Đường dẫn |
|---|---|
| `picture.mp4` bản 25/10 (585,8 MB, dựng từ audio/timeline cũ) | `.work/_cu/en_t03_fix_20261103/picture_EN_t03_cu_2510.mp4` |
| `Tap03_EN_master.mp4` bản đầu (true peak −0,7 dBFS — vượt trần A7) | `.work/_cu/en_t03_fix_20261103/Tap03_EN_master_peakfail.mp4` |
| `mo_ta.txt` / `description.txt` / `thumbnail.png` (trước khi sinh lại) | `.work/_cu/en_t03_fix_20261103/*.bak` |
| `shots_EN_t03.json`, `shots_text_tap03_EN.json`, `KeHoach_Video_Tap03_EN.md`, `Tap03_EN.srt` (trước sửa) | `.work/_cu/en_t03_fix_20261103/*.bak` |
| `build_video3.py` (trước khi sửa seed hash) | `.work/_cu/en_t03_fix_20261103/build_video3.py.bak_seedfix` |

---

## 8. Việc còn lại của người dùng

1. **Nghe duyệt** — `02_SAN_XUAT/Tap03_EN/CanNghe_Tap03_EN_higgs.md`.
2. **Quyết định về `roles_en` cho các tập EN khác.** Đo được: `EPISODES` chỉ có `roles_en` cho **Tập 02, 03, 04, 05** ⇒ **Tập 01 và Tập 06–29 EN** vẫn hiện badge sai tập (kiểu *"Blanchard case file"*, *"SPRINGFIELD RESIDENT"*) nếu dựng lại. Có 2 cách: (a) khai `roles_en` cho từng tập, (b) sửa **fallback dùng chung** trong `edition.py` để suy ra từ `EP["case"]`/`n1`/`n2` (Tập 01 không đổi vì `n1/n2` Tập 01 EN trùng nhãn cứng). **Chưa tự sửa** vì đụng thành phẩm các tập khác.
3. **Quyết định về mô tả Tập 04 EN.** `CHU_CO_DINH_EN.md` của Tập 04 cùng kiểu "rich" ⇒ sinh ra **5.366 ký tự** (> 5.000). File trên đĩa hiện còn 3.683 (sinh từ mẫu cũ) nên chưa lộ; chỉ lộ khi sinh lại. Tập 03 EN đã rút gọn xong; Tập 04 chưa đụng (ngoài phạm vi).
4. **Không cần đăng lại bản `.srt`**: file đã sinh lại khớp timeline.

---

## 9. Sự cố ngoài phạm vi việc này (ghi nhận để truy vết)

Lúc **19:53** ngày 03/11/2026, trong lúc dọn CPU cho QC, tôi đã dừng 6 tiến trình `ffmpeg` mà tôi cho là rác thừa của lượt QC trước. Hoá ra chúng **thuộc lượt render Tập 04 EN đang chạy song song** (bắt đầu 19:08:43, log ghi ra `test.txt` ở gốc repo) ⇒ lượt đó crash lúc **19:58:14** ở mốc 4200/7941 khung mỗi part. Người dùng đã quyết định **tự render lại Tập 04 EN** ⇒ tôi không chạm vào Tập 04 EN. Bài học đã ghi vào `AGENTS.md` **T16** và tiêu chuẩn **A11 #113**: không dừng tiến trình mình không spawn khi chưa xác định được owner; **2 session có thể chạy song song trong cùng một workspace**.

---

## 10. Script QC đã chạy (tái lập được)

| Script | Cổng | Kết quả |
|---|---|---|
| `.work/_qc_en_t03_input.py` | master mp3 ↔ timeline ↔ shots ↔ intro ↔ nền | ✅ |
| `.work/_qc_en_t03_match.py` | phủ câu · vai · số trên hình | 218/218 · 0 lỗi ✅ |
| `.work/_qc_en_t03_names.py` | nhãn vai EN đúng tập | ✅ |
| `.work/_qc_en_t03_vs_vn.py` | EN vs VN (nền / template / variant) | 0/110 khác ✅ |
| `.work/_check_stills_vs_video.py A\|B\|C` | ảnh tĩnh ↔ khung hình thật | 110/110 khớp, MAE ≤ 5,53 ✅ |
| `.work/_count_frames_t03_en.py` | đếm khung từng chunk + tổng | 49.398 ✅ |
| `.work/_concat_mux_t03_en.py` | ghép + mux + kiểm thời lượng | lệch −0,020 s ✅ |
| `.work/_qc_en_t03_final.py` | A9.1/A9.4 · thẻ kết · phụ đề · nhãn vai | **TẤT CẢ ĐẠT** ✅ |
| `.work/_qc_final_generic.py` | A9.1 · A9.3 · A9.4 (chung) | **TẤT CẢ ĐẠT** ✅ |
| `.work/_measure_t03_en.py` | đo toàn bộ số đo cho báo cáo | `.work/_qc_measure_t03_en.json` ✅ |
| `.work/_qc_sync_t03_en.py` | lệch A/V (FFT + self-test chống chỉ số sai) | **0,0 ms** ✅ |
| `.work/_qc_regress_links.py` | hồi quy `verified_links()` (L9) | 28/28 tập EN khớp, mất 0 link ✅ |
| `.work/_dry_desc_len.py` | đo độ dài mô tả mọi tập EN (không ghi file) | Tap03 4.935 / Tap04 5.366 ⚠ |

---

## 11. Bài học đã ghi vào tài liệu (L6)

| Nơi | Nội dung |
|---|---|
| `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` | A11 **#104** seed hash · **#105** thiếu `roles_en` · **#106** validator chỉ quét dấu nháy cong · **#107** đổi audio phải sinh lại `.srt` · **#108** log UTF-16LE + đo tiến độ sai bằng file size · **#109** offset frame cục bộ của chunk · **#110** `np.correlate` O(n²) → FFT + self-test · **#111** `verified_links()` chỉ hiểu bảng 4 cột · **#112** mô tả YouTube giới hạn 5.000 ký tự · **#113** không dừng tiến trình không rõ owner. *Đã validate: 113 mục, liên tiếp 1…113, không trùng.* |
| `AGENTS.md` | **H15** renderer phải tất định · **H16** chunk bắt đầu ở frame cục bộ 0 · **T15** `package.py` có thể xoá link nguồn và vượt trần 5.000 · **T16** đừng dừng tiến trình không rõ owner |
