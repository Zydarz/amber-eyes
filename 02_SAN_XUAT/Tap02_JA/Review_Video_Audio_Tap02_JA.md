# REVIEW CHUYẾN GIA VIDEO / ÂM THANH — TẬP 02 "二重生活の大佐" · BẢN TIẾNG NHẬT

*Ngày: 02/11/2026. Đối tượng: `02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp4`.*
*Người thực hiện: Mavis (AI). Mọi số đo dưới đây lấy **trực tiếp trên file thành phẩm**, không trích lại từ hồ sơ.*

---

## 0. Tóm tắt kết quả

| Hạng mục | Kết quả |
|---|---|
| Thời lượng file mp4 | ✅ 1791,83 s (timeline 1791,85 s — lệch 0,02 s) |
| Giải mã toàn bộ | ✅ 0 lỗi |
| Âm lượng tổng | ✅ LUFS −16,0 (chuẩn −16 ± 1) · đỉnh −2,3 dBFS (trần ≤ −1,5) |
| Khoảng lặng > 0,3 s | ✅ 0 |
| Bảng shot / câu phủ kịch bản | ✅ 151 shot · 203/203 câu · 0 thiếu · 0 trùng · 0 sai thứ tự |
| Khớp vai nói ↔ shot ↔ câu | ✅ 0 sai lệch trên 134 shot có lời |
| Phụ đề `.srt` | ✅ 219 cue · 0 khối lỗi · 0 dòng trống · **219/219 câu khớp lời đọc thật** |
| Font tiếng Nhật | ✅ YuGothB / YuGothM thiếu **0 ký tự** (647 ký tự Nhật) |
| Thẻ kết cuối tập | ✅ Có — trích khung 1784,85 s thấy thẻ `AMBER EYES` |
| Ảnh tĩnh soi bằng mắt | ✅ 151/151 shot, 5 trang contact sheet |
| **Chữ trên hình còn lệch lời đọc** | ⚠️ **21 phần tử** (15 beat + 6 trích dẫn) — xem mục 3 |

**Kết luận:** Video dựng xong, khớp thời lượng, đạt chuẩn âm thanh, hình ảnh sạch, phụ đề khớp 100 % lời đọc. Phần còn lại là **21 dòng chữ trên hình** vẫn mang văn bản của bản dịch cũ (25/10) trong khi giọng đọc đã đổi sang bản dịch 31/10 — mục 3 nêu chi tiết và cách sửa đã chuẩn bị.

---

## 1. Những gì đã dựng lại (vì sao không dùng được bản cũ)

Bản `picture.mp4` cũ (25/10) dài **1917,62 s** trong khi audio master hiện tại dài **1791,85 s** — lệch 125,77 s. Bảng shot và file `.srt` cũ cũng được sinh từ timeline cũ. Nếu mux thẳng, toàn bộ hình sẽ lệch tiếng từ giây thứ 23.

Đã chạy lại đúng thứ tự chuẩn:

1. `parse_shots.py` (AE_LANG=ja, AE_EP=02) → `shots_JA_t02.json` mới — 151 shot, phủ 203/203 câu
2. `subtitles.py` → `Tap02_JA.srt`
3. `build_video3.py --stills all` → 151 ảnh tĩnh, soi bằng mắt từng hồi
4. `build_video3.py --workers 6` → `picture.mp4` (80,8 phút)
5. `package.py --mux` → `Tap02_JA_master.mp4`

---

## 2. Lỗi đã phát hiện và sửa trong quá trình dựng

### P0 — Chữ Nhật ra ô vuông (tofu) ở 3 shot

`F_NUM` trong `build_video3.py` dùng **Bahnschrift** (font chỉ có Latin) cho mẫu T5 "con số lớn". Mọi ký tự Nhật trong mẫu này ra ô vuông:

| Shot | Trước | Sau |
|---|---|---|
| `1-05` | `46□` | ✅ `46歳` |
| `5-04` | `25□` | ✅ `25年間` |
| `5-05` | `25□` | ✅ `25年間` |

Đã sửa tối thiểu: phần con số vẫn vẽ bằng Bahnschrift (giữ nguyên kiểu chữ của bản VN/EN), phần hậu tố Nhật vẽ bằng `YuGothB.ttc` nối liền. Các shot T5 thuần số (`82`, `88`) **không đổi** một pixel nào. Đã xác nhận lại trong file mp4 thành phẩm.

### P0 — Phụ đề lệch lời đọc ở 154/203 câu

Nguyên nhân gốc: kịch bản JA được **hiệu đính lại ngày 31/10** (bản dịch mới) và audio Higgs được dựng lại từ bản dịch đó. Nhưng `build_audio3.py` lấy trường `display` cho timeline từ `tts_manifest_JA_t02.json` — file **25/10, cũ hơn**, nên phụ đề vẫn mang bản dịch cũ.

| | Ví dụ |
|---|---|
| Lời đọc thật (audio) | `オンタリオ州ベルヴィル市に住む27歳の女性会社員、ジェシカ・ロイドが自宅から姿を消しました` |
| Phụ đề (cũ) | `ベルヴィルに勤める27歳の女性社員Jessica Lloydは、自邸から行方不明になりました` |

Đã sửa bằng cách gán lại `text` của timeline từ **payload Higgs thật** (`higgs_payload_JA_t02.json`, 203 câu) — thời lượng giữ nguyên nên hình không phải dựng lại. Sau khi sửa: **219/219 cue khớp lời đọc thật**.

### P0 — Một khối phụ đề lỗi (dòng trống)

`subtitles.py` nhánh JA (`two_lines`) khi điểm cắt rơi vào cuối câu sẽ trả về chuỗi kết thúc bằng `\n` → cue sinh ra 1 dòng trống, khối SRT bị lệch. Đã sửa trong `subtitles.py` và kiểm hồi quy:

| Tập | Kết quả |
|---|---|
| JA Tap 01 | ✅ sửa đúng 1 khối lỗi (dòng trống), còn lại **byte-identical** |
| JA Tap 02 | ✅ sửa đúng 1 khối lỗi (dòng trống) |
| VN Tap 01 / Tap 02, EN Tap 02 | ✅ **byte-identical**, không đổi |

> Tệp `02_SAN_XUAT/Tap01/xuat_ban/Tap01.srt` (bản VN) đã được **khôi phục nguyên trạng** sau khi sinh lại: bản commit cũ dùng định dạng cue 1 dòng (tiền đệm 42 ký tự) trong khi `subtitles.py` hiện tại dùng cue 2 dòng (84 ký tự) — khác định dạng, không phải lỗi.

---

## 3. Còn lại: 21 phần tử chữ trên hình mang văn bản bản dịch cũ (25/10)

Bảng shot (`KeHoach_Video_Tap02_JA.md`) được sinh ngày 25/10 từ bản dịch cũ. Kịch bản đổi 31/10 thì bảng shot **chưa được dịch lại** (bảng shot bản VN đã được cập nhật, bản JA thì không).

| Loại | Số | Ví dụ (trên hình → lời đọc thật) |
|---|---:|---|
| Beat (nhãn + mốc thời gian) | 15 | `文末に置く点こそ小さいけれど` → `文末にピリオドを打つとき` |
| Trích dẫn (`“…”`) | 6 | `文末に置く点こそ小さいけれど、その点には実に多くの意味が込められています` → `文末にピリオドを打つとき、その点は小さくとも、計り知れないほど大きな意味を持つのです` |

**Vì sao chưa sửa:** sửa cột **Chữ** của bảng shot = đổi nội dung khung hình → phải dựng lại toàn bộ video (~2 giờ). Đã chuẩn bị sẵn: bảng sửa đủ 22 mục trong `_sync_plan_text_ja_t02.py`, và validator sẵn có (`_build_plan_tap02_ja.py`) sẽ tự chặn nếu beat/trích dẫn không còn nằm trong câu nói.

---

## 4. Những gì đã đo (chi tiết)

### Âm thanh (đo trên `audio_master_JA_t02.wav` và trên mp4 thành phẩm)

| Chỉ số | Yêu cầu | Kết quả |
|---|---|---|
| Khoảng lặng > 0,3 s (ngưỡng −60 dB) | 0 | ✅ 0 |
| Loudness tích hợp | −16 ± 1 LUFS | ✅ −16,0 LUFS |
| Đỉnh thật | ≤ −1,5 dBFS | ✅ −2,3 dBFS |
| Thời lượng mp3 master | = timeline | ✅ 1791,85 s |

### Hình ảnh

| Chỉ số | Kết quả |
|---|---|
| Độ phân giải / fps | 1920×1080, 30 fps, yuv420p |
| Video bitrate | 2629 kb/s · Audio 195 kb/s AAC 48 kHz stereo |
| Số khung hình | 53755 (1791,83 × 30) |
| Giải mã `-f null -` | ✅ 0 lỗi |
| Nền lặp tối đa | 4 shot liền (chuẩn ≤ 4) ✅ |
| Shot < 1 s | 0 ✅ |
| Shot cuối có chữ | ✅ `5-29` → thẻ `AMBER EYES` |

### Ba chiều: (ảnh) — (chữ) — (lời thoại)

| Kiểm tra | Kết quả |
|---|---|
| Câu trong shot có trong timeline | ✅ 203/203, 0 thiếu, 0 thừa, 0 trùng |
| Thứ tự câu trong shot | ✅ 0 shot đảo thứ tự |
| Mốc bắt đầu shot khớp câu | ✅ 0 lệch > 0,02 s |
| Shot liền nhau liên tục | ✅ 0 khoảng hở |
| Vai nói (cột Vai) khớp vai trong timeline | ✅ 0 sai lệch |
| Tỉ lệ vai | H 69/134 (51 %) · D 33 (25 %) · C 26 (19 %) · N1+N2 6 (4 %) ✅ |
| Phủ đề trùng ứng dụng | ✅ 100 % nền có file |
| Chữ trên hình lấy từ câu đang đọc | ✅ 100 % sau khi đồng bộ phụ đề |

### Font

| Font | Ký tự Nhật thiếu |
|---|---|
| `YuGothB.ttc` | ✅ 0 / 647 |
| `YuGothM.ttc` | ✅ 0 / 647 |

---

## 5. Việc đã làm thêm

- **`provenance.json`**: thêm 11 dòng cho tài sản JA Tap 02 (intro `intro_kenh_JA_t02.mov`, bộ giọng mẫu VoxCPM2 `voice_ref_voxcpm2_ja3`, audio Higgs `.work/audio_s_higgs_JA_t02`, master mp3/mp4, phụ đề). Từ 2148 → 2159 dòng. Sao lưu: `.work/_cu/provenance_pre_ja_t02_20261102.json`.
- **Sao lưu trước khi ghi đè**: `.work/_cu/ja_t02_20261102/` (shots cũ, SRT cũ, shots_text cũ), `.work/_cu/timeline_s_JA_t02_pre_text_fix.json`, `.work/_cu/subtitles_fix_20261102/`.
- **Contact sheet**: `contact_sheet_ja_t02_act1..5.png` + `contact_sheet_stills_ja_t02.png` trong `02_SAN_XUAT/Tap02_JA/`.

---

## 6. Việc cần người dùng làm

1. **Nghe thử bằng tai nghe** — kiểm tra cảm giác thực tế, độ đồng đều âm thanh, và cảm giác "cuộn nói" của giọng AI.
2. **Điền link nguồn** trong `02_SAN_XUAT/Tap02_JA/nguon_tham_khao_JA.md` (mới có 2/38 dòng có link) — phần AI không được bịa nguồn.
3. **Quyết định về 21 phần tử chữ trên hình** (mục 3): dựng lại video ~2 giờ để khớp tuyệt đối, hay giữ bản hiện tại.
