# REVIEW CHUYÊN GIA VIDEO / ÂM THANH — TẬP 02 "ĐẠI TÁ HAI MẶT"

*Ngày: 25/10/2026. Đối tượng: `02_SAN_XUAT/Tap02/xuat_ban/Tap02_master.mp4`.*
*Người thực hiện: Mavis (AI). Mọi con số dưới đây là **số đo thật** trên file thành phẩm, không phải trích lại từ hồ sơ.*

---

## 0. Tóm tắt chấm điểm

| Hạng mục | Kết quả |
|---|---|
| Âm thanh nền tảng (độ lớn, khoảng câm) | ✅ Đạt |
| Giọng đọc 3 vai chính | ✅ Đạt — nghe mù tách bạch 10/10 |
| Phụ đề (nội dung + đồng bộ) | ✅ Đạt hoàn hảo — lệch 0,000 s |
| Bảng shot / chữ trên hình (A9.2) | ✅ Đạt |
| **Thẻ kết cuối tập** | ❌ **Hỏng — video kết bằng tờ giấy trống** |
| **Đỉnh âm lượng trong file mp4** | ❌ Vượt trần −0,9 dBTP (chuẩn ≤ −1,5) |
| **Độ rộng stereo** | ❌ Gần như mono (side thấp hơn mid 34,7 dB) |
| Tách giọng nữ (Chuyên gia / N1 / N2) | ⚠ Ba giọng nữ chồng lên nhau |
| Độ tương phản chữ trên nền sáng (mẫu T1) | ⚠ Một số shot chữ gần như không đọc được |
| Mức âm lượng 3 phút cuối | ⚠ Thấp hơn trung vị 4,5 LU |

**Kết luận:** Chất lượng âm thanh và phụ đề của Tập 02 đã đạt chuẩn xuất bản — đây là một trong những bản dựng chắc tay nhất của kênh. Phần hình ảnh và bảng shot cũng sạch. **Nhưng bản thành phẩm đang bị 1 lỗi chặn (P0): 9 giây cuối video không có chữ kết tập** — và nguyên nhân không nằm ở renderer mà nằm ở việc **bảng shot đã sửa sau khi dựng video**.

---

## 1. Phương pháp (đã làm gì, chưa làm gì)

**Đã kiểm bằng số đo trên file mp4 thành phẩm:**
`ffprobe` (stream/bitrate/duration) · giải mã toàn bộ (`-f null -`) · `ebur128` (LUFS/LRA/true peak) · `silencedetect` (−60 dB, 0,3 s) · `volumedetect` theo đoạn · hồ sơ loudness 20 s/cửa sổ · đo rộng stereo bằng mid/side + tương quan L/R · `blackdetect` · `freezedetect` · phân tích phụ đề (phủ câu, đồng bộ, đối chiếu nguyên văn) · trích **151 khung giữa mỗi shot từ chính mp4** → 10 tờ contact sheet, soi bằng mắt · phóng to 18 khữ nghi ngờ · đo F0 từng vai (tự tương quan) · **nghe mù bằng mô hình** trên 6 file cắt từ mp4 thành phẩm.

**Chưa kiểm được (cần người dùng):** cảm giác thực tế khi xem trên điện thoại/tai nghe; cảm giác "cuốn hút" của giọng Host; tác giả hoá cảm xúc khi nghe (TTS không có cảm xúc thật); mức độ hấp dẫn thuật lý.

---

## 2. LỖI CẦN SỬA (theo thứ tự ưu tiên)

### P0 — Thẻ kết cuối tập trắng trơn, video kết bằng 4 giây đen

**Bằng chứng (đo trên mp4):**

| Mốc | Độ sáng khung hình (mean 0–255) | Nhìn thấy |
|---|---:|---|
| 1596,70 s | 3,4 | cảnh cũ đang dissolve |
| 1598–1601 s | ~50 | **tờ giấy trắng — KHÔNG CÓ CHỮ** |
| 1602 s | 31 | bắt đầu mờ đi |
| 1603 s | 6,8 | gần như đen |
| 1603,5–1605,7 s | **0,18** | **đen tuyệt đối (~2,7 s)** |

Lời thoại cuối kết thúc lúc 1596,70 s. Nghĩa là người xem nhìn **3 s tờ giấy trắng không chữ + 2,7 s màn đen**, trong khi âm thanh vẫn còn đuôi nhạc (12 s cuối: mean −29,2 dB).

**Nguyên nhân gốc — đã xác định chính xác:**

| File | Mtime | Nội dung shot `5-29` (thẻ kết) |
|---|---|---|
| `.work/shots_t02.json.bak` | 23/10 **18:09** | `"segments": []` ← **bản dùng để dựng** |
| `.work/shots_t02.json` | 24/10 **09:22** | `"segments": [["ital","HỒ SƠ TẬP 02 · ĐÃ ĐÓNG"],["bold","AMBER EYES"],["ital","Phân tích tâm lý tội phạm"],["ital","qua những hồ sơ có thật"]]` |
| `Tap02_master.mp4` | 23/10 **19:43** | dựng lúc 19:43 — **trước lần sửa 24/10** |

Đối chiếu 151 shot giữa hai bản: **chỉ khác đúng shot `5-29`**. Tức là bản sửa bẫy #25 (A11: "video kết thúc bằng tờ giấy trống") đã được viết đúng vào bảng shot, **nhưng video chưa được dựng lại**. Mẫu T2 trong renderer (`build_video3.py:691 t2_card`, nhánh `closing` ở dòng 713) vẫn còn nguyên và vẽ đúng 4 dòng chữ nếu `segments` có dữ liệu.

**Cách sửa (không cần dựng lại 92 phút):**
1. `py -3 .work/build_video3.py --stills 5-29` → xác nhận ảnh tĩnh có chữ.
2. Render lại **riêng đoạn cuối** bằng `.work/rerender_part.py`, rồi `py -3 .work/package.py --mux` (AE_EP=02).
3. Kiểm lại: trích khung tại `t = 1598 s` → phải thấy "HỒ SƠ TẬP 02 · ĐÃ ĐÓNG / AMBER EYES".

**Ngoài ra, nên thêm chốt chặn trong quy trình:** trước khi giao, luôn so `mtime` của bảng shot với `mtime` file mp4; và luôn trích **khung tại giữa shot cuối** để đảm bảo nó khác nền đen/trắng trơn (bài học #37 đã thêm vào A11).

---

### P1 — Đỉnh âm lượng trong file mp4 vượt chuẩn

| Nguồn | Integrated | True peak |
|---|---:|---:|
| `audio_master_t02.wav` (file nguồn) | −15,9 LUFS | **−1,5 dBFS** |
| **AAC trong `Tap02_master.mp4`** (thành phẩm) | −15,9 LUFS | **−0,9 dBTP** ❌ |
| `Tap02_master.mp3` | −16,2 LUFS | −1,3 dBTP |

Tiêu chuẩn A7/A9.1 yêu cầu đỉnh ≤ −1,5 dBFS. Hồ sơ tập ghi "đỉnh −1,5 dBFS" — con số đó đo trên **WAV trước khi encode**. Bộ mã hoá AAC đẩy đỉnh lên **+0,6 dB**, nên file thành phẩm thật sự vi phạm trần của chính dự án.

**Cách sửa:** khi đóng gói, áp limiter/encoder trực tiếp lên stream âm thanh: `-af "loudnorm=I=-16:TP=-1.8:LRA=11"` (hoặc `alimiter=limit=0.841` ≈ −1,5 dBFS) trước khi mã hoá AAC, rồi đo lại trên chính mp4. Nên đổi luôn QC để **đo trên file mp4 cuối**, không đo trên WAV trung gian — đó là lý do lỗi này lọt qua.

> *Tham chiếu chéo:* Tập 01 đang có đỉnh −4,5 dBFS (rất dè). Hai tập lệch nhau ~3,6 dB về đỉnh — khi đăng cùng playlist thì cảm giác "chặt" sẽ không đồng đều.

---

### P1 — Âm thanh gần như đơn kênh (mono)

Đo trên 60 s giữa tập (800–860 s), giải mã stereo 48 kHz:

| Chỉ số | Giá trị | Nghĩa |
|---|---:|---|
| RMS kênh L / R | −17,75 / −17,75 dB | hai kênh bằng nhau tuyệt đối |
| Tương quan L–R | **0,999329** | gần như cùng một tín hiệu |
| Side (L−R) so với Mid (L+R) | **−34,74 dB** (side chỉ còn 4,3% công suất) | **không có ảnh stereo** |

Tiêu chuẩn A2 yêu cầu "trộn stereo" (nền môi trường · tiếng động · nhạc). Thực tế file thành phẩm là **dual-mono**: nền tiếng và tiếng động không hề tách bên trái/phải. Người xem tai nghe sẽ thấy "phẳng", thiếu không gian; loa TV càng không nhận ra.

**Cách sửa (rẻ, không cần đọc lại TTS):** trong `build_audio3.py`, pan nhạc nền và SFX theo vị trí trong khung hình (nền bên trái → L, bên phải → R), hoặc áp `stereotools`/`haas` nhẹ để tạo chiều rộng. Mục tiêu đo được: **side thấp hơn mid 12–18 dB** (hiện tại là 34,7 dB — tức gần như không có side).

---

### P1 — Ba giọng nữ trong bộ 5 vai chồng lên nhau

**Nghe mù** (file cắt từ chính mp4 thành phẩm, không nói trước đáp án):

| File thử | Kết quả mô hình nghe ra | Chấm |
|---|---|---|
| 12 câu Host | **1 người**, không đổi giọng | 10/10 ổn định |
| 12 câu Điều tra viên | **1 người** | 10/10 |
| 12 câu Chuyên gia | **1 người** | 10/10 |
| H + D + C xen kẽ (27 câu) | **3 người** (2 nam 1 nữ), tách bạch rõ | **10/10** |
| N1 + N2 (7 câu) | **2 người** | 9/10 |
| **Cả 5 vai xen kẽ (19 câu)** | **4 người** (2 nam + 2 nữ) | 8,5/10 · cặp nữ dễ nhầm **7/10** |

**Đo F0** (trung vị, trên file TTS rời không lẫn nhạc):

| Vai | F0 trung vị | Dải p5–p95 | Cách nhau so với vai trước | G9 (cần ≥ 4 nửa cung) |
|---|---:|---|---:|---|
| Host | 102,4 Hz | 78,9–162,2 | — | — |
| Điều tra viên | 141,6 Hz | 113,0–388,6 | **+5,61** | ✅ |
| Chuyên gia | 206,1 Hz | 167,2–275,7 | **+6,50** | ✅ |
| N2 | 233,5 Hz | 172,8–363,9 | **+2,16** | ❌ |
| N1 | 254,3 Hz | 211,0–335,4 | **+1,48** | ❌ |

Ba giọng nữ nằm trong **48 Hz** — cách nhau chỉ 2,2 và 1,5 nửa cung, thấp hơn cả ngưỡng ≥ 3 nửa cung mà hồ sơ tập tự ghi ("Cách Chuyên gia ≥ 3 nửa cung"). Đây là lý do người nghe mù gộp 3 giọng nữ thành 2.

**Đánh giá:** N1 và N2 nghe riêng vẫn tách được (9/10), nên chỉ cần tách **Chuyên gia ↔ N1/N2**. Vì N1/N2 chỉ có 7 câu trong cả tập, cách rẻ nhất là **đổi giọng N1/N2 sang vùng xa Chuyên gia** (ví dụ N1 xuống ~170 Hz hoặc N2 lên ~290 Hz) — chỉ cần đọc lại 7 câu, không phải dựng lại toàn bộ.

> *Lưu ý giới hạn của phép thử:* trong file 5 vai, các câu của Chuyên gia rơi thành một khối liên tiếp (4 câu), nên "4 người thay vì 5" là **dấu hiệu**, chưa phải phán quyết tuyệt đối. Nhưng phép đo F0 độc lập cũng cho kết luận trùng khớp, nên vấn đề là thật.

---

### P2 — Chữ trên nền sáng ở mẫu T1: đọc gần như không được

Shot `1-25` (4:14,74) — tiêu đề `HOA VĂN LỐP RẤT GIỐNG DẤU VẾT TẠI HIỆN TRƯỜNG` nằm trên thân xe SUV trắng và tuyết sáng. Phóng to 2,34× cho thấy chữ là **trắng mờ ~40% không có nền tối**, chữ "DẤU VẾT" **chìm hẳn vào thân xe**; dòng nhỏ "MỐT CUỘC DÙNG XE THUÊ TỤC" cũng mờ tương tự.

**Nguyên nhân trong mã:** mẫu T1 chỉ dùng `gradient_bottom(frac=0.45, alpha=180)` (`build_video3.py:471`) — lớp tối chỉ phủ **45% dưới cùng** khung hình (từ y≈594 trở xuống), và ở vùng này alpha mới chỉ ~40–70. Trong khi T2/T4/T9/T11 có `DARK70` (alpha 178 toàn khung) hoặc `shade` riêng. Tiêu đề T1 đặt ở khoảng y≈700–800 → nằm đúng chỗ lớp tối yếu nhất.

**Cách sửa:** nâng `frac` lên ~0,6 và/hoặc tăng `alpha`; tốt hơn là thêm một lớp đệm tối cục bộ ngay dưới khối chữ. 60/151 shot dùng mẫu T1 nên sửa ở renderer là sửa được cả kênh.

---

### P2 — 3 phút cuối tập nhỏ hơn phần còn lại

Hồ sơ loudness 20 s/cửa sổ trên mp4: trung vị **−16,35 LUFS**, cao nhất **−11,8** (tại 980 s), thấp nhất **−20,8** (tại 1500 s). Riêng 12 s cuối: mean **−29,2 dB**. Hồi 5 vì thế "chìm" hơn các hồi trước ~4,5 LU — người xem dễ cảm thấy video bị cắt dần thay vì kết.

**Cách sửa:** nâng nhạc nền/nhạc outro ở Hồi 5 lên ~2–3 dB và giữ đuôi piano ấm không fade hẳn xuống (bẫy #35 của A11 đã nói đúng hướng này cho Tập 03 EN).

---

### P3 — Bộ mã hoá hình: đang dùng encoder phần mềm, dung lượng lớn

| Chỉ số | Giá trị |
|---|---|
| Profile | **Constrained Baseline** (không CABAC, không B-frame) |
| Encoder | **libopenh264** (phần mềm, không phải NVENC/QSV) |
| Bitrate video | 2,55 Mbps ở 1920×1080@30 |
| Dung lượng | 552,8 MB (527,2 MiB) |
| Bản mã hoá âm thanh | AAC-LC 48 kHz stereo 194,7 kbps |

H.264 Constrained Baseline bằng encoder phần mềm là lựa chọn **an toàn cho tính tương thích** nhưng tốn bitrate. Kiểm chứng chất lượng thực tế: vùng nền tối còn **168–191 mức xám** → **không có hiện tượng lèn màu (posterization) đáng kể**. Vậy nền tảng hình ảnh là tốt; vấn đề chỉ là **kích thước file và thời gian dựng** (92 phút).

**Cách sửa (tùy máy có GPU NVIDIA/Intel):** dùng `h264_nvenc`/`h264_qsv` với `-profile:v high -preset p5`, cho file nhỏ hơn ~40% và dựng nhanh hơn nhiều lần. Cần kiểm tra bằng cách render 1 shot thử và so ảnh.

---

## 3. NHỮNG THỨ ĐÃ ĐƯỢC KIỂM VÀ **KHÔNG** CÓ LỖI

Ghi lại để không tốn công dựng lại những chỗ tôi nghi ngờ rồi kiểm chứng là sai:

| Nghi ngờ | Kết quả kiểm chứng |
|---|---|
| Phụ đề cắt giữa từ ("sự chứng" \| "kiến của") | ❌ Không. Đối chiếu nguyên văn 215/215 câu: **0 sai lệch**, 0 lỗi mất dấu cách |
| Phụ đề lệch tiếng | ❌ Không. Cue đầu mỗi câu lệch **0,000 s** (min = max = 0,0), phủ 99,68% lời thoại |
| Phụ đề bị đè lên nhau / hụt câu | ❌ Không. 391 cue, 215/215 câu có phụ đề, 0 cue trùng |
| Gạch ngang ở "01 Tiền bạc" (shot 2-11) | ❌ Có chủ đích — `variant: "strike"`, gạch đúng nhịp lời thoại |
| Chữ tiếng Anh lạ ("Art to cutting so") | ❌ Đọc nhầm khi xem thumbnail. Nguồn: "Ăn tối cùng vợ" |
| Sai chính tả "LỚP" | ❌ Nguồn và hình đều đúng "LỐP" |
| Đường gạch đỏ lạ trên nền | ❌ Là route-pin của mẫu T7, đúng thiết kế |
| Lộ mặt người thật / chữ do AI vẽ | ❌ Không. 151 khung soi bằng mắt: không lộ mặt, không có chữ lạ, nạn nhân chỉ xuất hiện bằng tên (đúng V5) |
| Lềch hình/tiếng | ❌ Không. Video 1605,700 s · audio 1605,696 s (lệch 4 ms) |
| Đóng băng hình | ❌ Không. `freezedetect` = 0 đoạn |
| Khoảng câm | ❌ Không. 0 đoạn > 0,3 s ở −60 dB (đạt V4) |
| Lền màu trên nền tối | ❌ Không. 168–191 mức xám còn lại trong vùng tối |
| Đen bất thường giữa tập | ❌ Hợp lý — 4 mốc chuyển hồi (05:25 / 09:32 / 15:18 / 20:58) + mở đầu + đuôi |

---

## 4. Bảng số đo đầy đủ

**File:** `Tap02_master.mp4` · 552.807.855 byte (552,8 MB / 527,2 MiB) · 1605,700 s (26:45,70) · 1920×1080@30 · 48.171 khung · H.264 Constrained Baseline (libopenh264) · AAC-LC 48 kHz stereo 194,7 kbps · **faststart (moov trước mdat)** · 2 stream.

**Âm thanh**

| Chỉ số | Giá trị | Chuẩn | Kết quả |
|---|---:|---|---|
| Integrated loudness (AAC trong mp4) | −15,9 LUFS | −16 ± 1 | ✅ |
| Loudness Range | 8,0 LU | — | ✅ |
| True peak (AAC trong mp4) | **−0,9 dBTP** | ≤ −1,5 | ❌ |
| True peak (WAV nguồn) | −1,5 dBFS | ≤ −1,5 | ✅ |
| Khoảng câm > 0,3 s @ −60 dB | 0 | 0 | ✅ |
| Loudness ngắn hạn (20 s) | median −16,35 · max −11,8 @ 980 s · min −20,8 @ 1500 s | — | ⚠ |
| 12 s cuối | mean −29,2 dB · max −4,6 dB | — | ⚠ |
| Side / Mid | −34,74 dB (4,3%) | mục tiêu 12–18 dB | ❌ |
| Tương quan L–R | 0,999329 | < 0,98 | ❌ |
| Lời đầu tiên | 23,0 s | 22,8–23,5 | ✅ |
| Giải mã | 0 lỗi | 0 | ✅ |

**Phụ đề** (`Tap02.srt`)

| Chỉ số | Giá trị |
|---|---|
| Số cue / dòng | 391 / 687 |
| Câu có phụ đề | 215 / 215 |
| Lệch cue đầu so với câu (min/max) | 0,000 s / 0,000 s |
| Phủ lời thoại | 99,68% |
| Sai lệch văn bản so với câu gốc | 0 |
| Cue trùng nhau / hụt | 0 / 0 |
| Khoảng trống > 1 s | 26 (lớn nhất 2,63 s) |
| Cue có nhãn vai | 36 — đủ cả 5 vai (HOST 23 · ĐTV 6 · CÁO 5 · BINH SĨ 1 · KHÁNG GIẢ 1) |

**Hình**

| Chỉ số | Giá trị |
|---|---|
| Shot / câu | 151 / 215 |
| Mẫu dùng | T1×60 · T8×20 · T3×18 · T4×13 · T5×11 · T2×11 · T9×10 · T10×5 · T7×2 · T6×1 |
| Câu theo vai | H 98 · D 58 · C 52 · N1 4 · N2 3 |
| QC A9.2 (script của dự án) | Đạt toàn bộ |
| Freeze frame | 0 |
| Đoạn đen | 0–0,77 s · 325,8 · 572,3 · 917,6 · 1258,2 · 1491,1–1492,6 s (mở đầu + 4 mốc hồi + đuôi) |
| Mức xám còn lại ở nền tối | 168–191 / 255 |

**Giọng (nghe mù trên file cắt từ mp4 thành phẩm)**

| File thử | Người nghe ra | Chấm |
|---|---|---|
| 12 câu Host | 1 | 10/10 |
| 12 câu Điều tra viên | 1 | 10/10 |
| 12 câu Chuyên gia | 1 | 10/10 |
| H+D+C (27 câu) | 3 | 10/10 |
| N1+N2 (7 câu) | 2 | 9/10 |
| Cả 5 vai (19 câu) | 4 | 8,5/10 (cặp nữ 7/10) |

---

## 5. Việc người dùng cần làm / quyết định

1. **Duyệt để dựng lại đoạn cuối** (P0). Chỉ cần render lại shot `5-29` + `package --mux` (vài phút), không cần dựng lại 92 phút. Tôi chưa tự làm vì đây là ghi đè lên thành phẩm.
2. **Quyết định hướng sửa đỉnh âm lượng** (P1): hạ 0,6 dB khi mã hoá AAC, hay giữ nguyên và nới trần trong tiêu chuẩn cho khớp thực tế. Tôi đề xuất hạ đỉnh và sửa QC để đo trên mp4.
3. **Quyết định có mở rộng stereo không** (P1): nếu không, cần ghi rõ vào tiêu chuẩn rằng kênh đang chủ động làm mono (đơn giản hơn nhiều so với pan SFX).
4. **Chọn hướng tách 3 giọng nữ** (P1): đổi cao độ/giọng của N1 hoặc N2 (chỉ 7 câu, rẻ) — cần bạn nghe 2–3 phương án trước khi đọc lại.
5. **Nghe toàn tập** (bắt buộc trước khi đăng): các số đo không bắt được cảm giác "đều đều" hay "cuốn hút". Bản tôi nghe mù đạt, nhưng tai bạn là tiêu chí cuối.
6. **Điền nguồn** (`xuat_ban/nguon_tham_khao.md` — 35 câu) và **chốt điều khoản thương mại**: 9 file nhạc nền MiniMax + ảnh linh thú + ảnh bạn cung cấp vẫn đang ở trạng thái "chưa" trong `provenance.json`.
7. **Ghi chú kỹ thuật**: file mp4 có faststart, 0 lỗi giải mã, 0 freeze, phụ đề sạch — những phần này không cần làm lại.

---

*Tài liệu này do AI tạo trong lượt review độc lập; mọi số đo đều tái lập được bằng các script trong `.work/_review_tap02_*.py` và `.work/_qc_tap02_*.py`.*
