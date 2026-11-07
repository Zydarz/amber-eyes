# BÁO CÁO DỰNG LẠI ẢNH TĨNH — TẬP 08 · 06/11/2026

**Lý do dựng lại:** kịch bản Tập 08 được **viết lại toàn bộ** (05/11/2026) — VN / EN / JA đều
đổi từ **47 element · 154–165 câu** lên **53 element · 171 câu**. Bảng shot mục 6 và timeline cũ
vẫn trỏ vào bản kịch bản **trước khi viết lại** ⇒ lớp chữ trên hình không còn khớp lời đọc
⇒ **dựng lại ảnh tĩnh cho 3 ngôn ngữ** (không dựng video).

> **Phạm vi:** chỉ ảnh tĩnh (`build_video3.py --stills all`). **Không** dựng video, **không** dựng lại audio.
> Timeline là **ƯỚC LƯỢNG** (neo theo element + RATE ký tự/s) — audio master cũ đã bị dọn theo A11 §8.

---

## 1. Số đo thật

| Mục | VN | EN | JA | Chuẩn | Kết quả |
|---|---|---|---|---|---|
| Kịch bản | 53 element · **171 câu** | 53 element · **171 câu** | 53 element · **171 câu** | 3 bản đồng nhất | ✅ |
| Timeline (ước lượng) | 1420,4 s (23:40) | 1309,4 s (21:49) | 1571,7 s (26:11) | — | *(số liệu)* |
| Số shot | **108** | **108** | **108** | 3 bản bằng nhau | ✅ |
| Phủ câu | **171/171** đúng thứ tự | 171/171 | 171/171 | 100% | ✅ |
| Ảnh tĩnh render | **108/108** | 108/108 | 108/108 | đủ, không thừa | ✅ |
| ID shot trùng | 0 | 0 | 0 | 0 | ✅ |
| Nền lặp liên tiếp tối đa | 2 shot | 2 shot | 2 shot | ≤ 4 (H10) | ✅ |
| Loại nền dùng | 69 | 69 | 69 | — | *(số liệu)* |
| Mẫu dùng | T1×85 T4×7 T10×4 T8×4 T2×3 T9×2 T3×1 T6×1 T5×1 | (như VN) | (như VN) | — | *(số liệu)* |
| Câu theo vai | H=99 D=37 C=25 N1=5 N2=5 | (như VN) | (như VN) | — | *(số liệu)* |
| Shot > 15 s | 43/108 (TB 13,0 s) | 33/108 (TB 11,9 s) | 49/108 (TB 14,4 s) | 3–15 s | ⚠ mục 5 |
| Dài nhất | `2-12` 42,0 s | `2-12` 32,7 s | `2-12` 38,0 s | ≤ 15 s | ⚠ mục 5 |
| Ngắn nhất | `1-23` 1,8 s | `1-23` 1,8 s | `1-23` 1,8 s | — | ✅ (thẻ chuyển hồi) |
| Cổng QC A9.2 (bảng shot) | 12/12 | 12/12 | 12/12 | 12 | ✅ |
| Chữ trên hình có trong câu (A9.2) | 0 lỗi | 0 lỗi | 0 lỗi | 0 | ✅ |
| Trích dẫn nguyên văn (V3) | 0 lỗi | 0 lỗi | 0 lỗi | 0 | ✅ |
| Từ cấm trên hình | 0 | 0 | 0 | 0 | ✅ |
| Ảnh cũ hơn bảng shot | 0 | 0 | 0 | 0 | ✅ |
| Chữ chìm sau `text_scrim` (H9) | 0 shot | 0 shot | 0 shot | 0 | ✅ (mục 4) |

**Cổng QC dự án `_qc_tap02_shots.py` (AE_EP=08): VN / EN / JA đều `TAT CA DA DAT`.**

---

## 2. Các lỗi đã phát hiện và sửa

### 2.1. Timeline cũ trỏ vào kịch bản cũ (lỗi gốc rễ)

`.work/script_tap08.json` (VN) chỉ có **47 element / 154 câu**, `.work/script_tap08_EN.json` có
**47 element / 165 câu**, `.work/script_tap08_JA.json` cũng lệch — trong khi kịch bản mới có
**53 element / 171 câu**. Timeline cũ neo theo bản cũ ⇒ mốc thời gian và câu đọc lệch.

→ Đã **parse lại cả 3 kịch bản** (`parse_kichban.py` → `script_tap08*.json`, khớp 171 câu / 53 element
/ vai H=99 · D=37 · C=25 · N1=5 · N2=5; N1 là element `1.07`, N2 là element `4.08`).

### 2.2. Dựng lại timeline theo đúng cách Tập 07

Dùng `.work/_build_timeline_t08.py` (viết lại theo `.work/_t07/_t07_build_timeline.py`): neo theo
**ID element** + **RATE ký tự/s** đo được, bố trí đúng công thức `build_audio3.py`
(FIRST_VOICE 23,0 · GAP_SENT 0,35 · GAP_Q 0,60 · GAP_SPEAKER 0,70 · GAP_ACT 2,0).

| | VN | EN | JA |
|---|---|---|---|
| RATE (ký tự/s) | 15,66 | 17,88 | 5,96 (lấy từ timeline JA Tập 07) |
| Neo element | 27 | 27 | 27 |
| Marker | 25 | 25 | 25 |

Mỗi file có khối `_estimated` ghi rõ là ước lượng (audio master Tập 08 đã bị dọn).

### 2.3. Bảng shot Tập 08 chưa tồn tại trong lịch sử git

⇒ **dựng mới 108 dòng × 3 ngôn ngữ** từ **một nguồn dữ liệu chung** (`.work/_t08_rows_a1.py` …
`_t08_rows_a5.py`, 11 trường/dòng) qua generator idempotent `.work/_gen_plan_t08.py` — bảo đảm
parity 1:1 về số shot, mẫu, nền, vai; chỉ khác cột *Chữ* + tiêu đề mục 6.

Cột **"Mẫu"** giữ nguyên tiếng Việt ở cả 3 bản (bắt buộc — `parse_shots.py` dò "cờ"/"lời kể"/
"ngày"/"so sánh" để suy `variant`).

### 2.4. Bốn caption VN dính từ cấm

| Shot | Cũ | Mới |
|---|---|---|
| `4-12` | *…vấy máu…* | *…đôi tay mình đã làm việc thiện cứu rỗi nạn nhân…* (viết lại cả câu) |
| `4-17` | *…một biến cố đẫm máu khác…* | *…một biến cố bạo lực khác…* |
| `5-06` | *…đòn chí mạng…* | *…một cú sốc chí mạng…* |
| `5-09` | *…đòn thao túng…* | *…những thủ đoạn thao túng tâm lý tinh vi…* |

Đồng thời bỏ `bloodstained` (EN) / `血塗られた` (JA) ở các caption tương ứng.

### 2.5. Lỗi số trên hình ở bản EN (`2-09`)

Câu đọc viết `March 22,` (có dấu phẩy) ⇒ regex token `\d[\d.,]*` của cổng A9.2 nuốt cả dấu phẩy
thành `"22,"` ⇒ không khớp câu. Đã sửa thành `March 22 —` ⇒ token = `"22"`, khớp.

### 2.6. Header B1/B3 còn số liệu của bản cũ

| File | Sửa |
|---|---|
| `KeHoach_Video_Tap08.md` | 1452,0 s → **1420,4 s (23:40)**; timeline 1110,8 s → 1420,4 s (ghi rõ là ước lượng); SRT 278 cue → ghi rõ là **CŨ**; dòng "Thành phẩm Master" → ghi rõ **đã bị dọn** |
| `KeHoach_Video_Tap08_EN.md` | 47 element/165 câu → **53/171**; Master Output 1181,9 s → ghi rõ **đã bị dọn + timeline ước lượng 1309,4 s**; CER/MOS ghi chú "số đo của master cũ"; Date 04/11 → **06/11** |
| `KeHoach_Video_Tap08_JA.md` | 1564,9 s (26:05) → **1571,7 s (26:11)**; 107 shot → **108** |

### 2.7. Thẻ kết EN lệch H12 của chính bản kế hoạch

Mục B2 của bản EN quy định thẻ kết = `DOSSIER EPISODE 08 · CLOSED`, nhưng dòng `5-22` lại ghi
`CASE FILE 08 · CLOSED`. Đã sửa về đúng **H12 của bản kế hoạch** và render lại.

Bản JA cũng lệch quy ước chuỗn (Tập 02/03/06/07 dùng `事件ファイル 第NN話 · 終結` + tagline
`実際の事件記録から読み解く犯罪心理学`) ⇒ đã chuẩn hoá `5-22` JA.

### 2.8. Nhãn hồi 4 còn "đẫm máu" trong `act_titles`

`edition.py` (`EPISODES["08"]["act_titles"]`) VN ghi *"Hồi 4 · Ma thuật tẩy não & khái niệm Poa
đẫm máu"*; EN/JA mới thêm trong lượt này còn dịch tương ứng (*Bloodied Poa Doctrine* /
*血に塗られた「ポア」*). `act_titles` **không** được vẽ lên ảnh (`build_video3.py` không đọc khoá này)
nhưng lại đi vào **mốc chương YouTube** (`package.py`) và mô tả (`generate_all_descriptions.py`).
Đã gỡ tham chiếu máu ở cả 3 ngôn ngữ, khớp đúng chữ trên thẻ chương T10.

> Lưu ý: **lời đọc** của kịch bản vẫn giữ nguyên (VD `4.09#2` *"một biến cố đẫm máu khác…"*) —
> cấm là cấm **chữ trên hình**, không cấm lời.

---

## 3. File đã tạo / sửa

| File | Việc |
|---|---|
| `02_SAN_XUAT/Tap08/KeHoach_Video_Tap08.md` | **mục 6 viết lại** (108 dòng) + B1/B3 cập nhật + dòng trạng thái |
| `02_SAN_XUAT/Tap08_EN/KeHoach_Video_Tap08_EN.md` | **mục 6 viết lại** (108 dòng) + B1 cập nhật + dòng trạng thái |
| `02_SAN_XUAT/Tap08_JA/KeHoach_Video_Tap08_JA.md` | **tạo mới** (header + mục 6, 108 dòng) |
| `02_SAN_XUAT/Tap08/BaoCao_QC_Tap08_20261106.md` | **file này** |
| `.work/script_t08.json` / `_EN_` / `_JA_` | parse lại từ kịch bản mới (53 element / 171 câu) |
| `.work/timeline_s_t08.json` / `_EN_` / `_JA_` | dựng lại (171 câu · 25 marker · 27 neo) |
| `.work/shots_t08.json` / `_EN_` / `_JA_` | sinh lại từ bảng shot mới |
| `.work/edition.py` | thêm nhánh **EN/JA** cho `act_titles` tập 08 + gỡ tham chiếu máu ở hồi 4 (3 ngôn ngữ) |
| `.work/video3_t08/stills/` | **108 ảnh render lại** |
| `.work/video3_EN_t08/stills/` | **108 ảnh render lại** |
| `.work/video3_JA_t08/stills/` | **108 ảnh render lại** |
| `.work/video3*/qc/qc_stills_{vi,en,ja}_01..09.png` | 27 contact sheet (9 tab/ngôn ngữ × 12 ảnh) |
| `.work/_t08_rows_a1..a5.py` | dữ liệu bảng shot (nguồn chung 3 ngôn ngữ) |
| `.work/_gen_plan_t08.py` | generator bảng shot (idempotent) |
| `.work/_build_timeline_t08.py` | dựng timeline ước lượng |
| `.work/_dump_sents_t08.py` + `_t08_sents.txt` | trích câu 3 ngôn ngữ để đối chiếu |
| `.work/_qc_words_t08.py` / `_qc_contrast_t08.py` / `_qc_stats_t08.py` / `_qc_contact_stills_t08.py` | bộ QC |
| `.work/_render_t08_stills.ps1` | script render 3 ngôn ngữ (tách tiến trình) |

**Bản sao lưu (L5):** `.work/_cu/script_tap08_before_reparse_20261106.json`,
`script_tap08_EN_before_reparse_20261106.json`, `script_tap08_JA_before_reparse_20261106.json`,
`timeline_s_t08_before_rebuild_20261106.json`, `timeline_s_EN_t08_before_rebuild_20261106.json`,
`KeHoach_Video_Tap08_before_shots_20261106.md`, `KeHoach_Video_Tap08_EN_before_shots_20261106.md`,
`edition.py.bak_20261106_t08_acttitles`.

---

## 4. Độ tương phản chữ (H9 `text_scrim`)

Đo bằng `.work/_qc_contrast_t08.py`: lấy đúng vị trí **nét chữ** (theo màu vai của shot),
nền = trung vị pixel quanh đó (loại nét chữ), tính tỉ lệ tương phản WCAG.
Ngưỡng: `ratio < 1.6` hoặc `|Δlum| < 45` ⇒ chữ chìm; `ratio < 3.0` ⇒ chữ nhạt.

| | ảnh có chữ chìm | ảnh chữ nhạt | ratio thấp nhất | ratio trung vị | ratio cao nhất |
|---|---|---|---|---|---|
| VN | 0 | 0 | 5,01 (`4-16`) | 9,61 | 10,69 |
| EN | 0 | 0 | 5,01 (`4-16`) | 9,53 | 10,69 |
| JA | 0 | 0 | 5,01 (`4-16`) | 9,53 | 10,69 |

`4-16` là shot lời khai của N2 (màu chữ cyan 110,140,160 trên nền tối 32,22,15) — thấp nhất nhưng
vẫn ổn ⇒ **không cần bật `text_scrim`** cho Tập 08 (nền của bộ ảnh `t8_*` là noir tối).

---

## 5. Cảnh báo còn lại (không sửa trong lượt này)

1. **Timeline là bản ƯỚC LƯỢNG** — audio master Tập 08 đã bị dọn (A11 §8). Mọi mốc thời gian trên
   ảnh tĩnh là số ước lượng. **Muốn dựng video bắt buộc phải chạy lại TTS** (Higgs Audio v3 chỉ chạy
   được trên Kaggle GPU — máy này không có GPU/kaggle CLI) → `build_audio3.py` sẽ ghi đè đúng các
   file `timeline_s_*_t08.json` này → **parse_shots.py + render lại ảnh** (bẫy: ảnh cũ hơn timeline
   ⇒ hình lệch tiếng).
2. **`Tap08.srt` (278 cue) và `Tap08_EN.srt` (333 cue) là CŨ** — lấy từ bản 154/165 câu, lời đọc
   khác. Phải sinh lại từ timeline 171 câu (`subtitles.py`).
3. **`tts_manifest_t08.json` (154 câu) và `tts_manifest_EN_t08.json` (165 câu) là CŨ** ⇒ phải
   sinh lại trước khi chạy TTS. **Bản JA chưa có manifest** ⇒ cần tạo mới.
4. **Sóng âm trên badge vai là đường gạch phẳng** (không có stem): `.work/stems_t08*/` đã bị dọn
   cùng audio master. Không bịa envelope để làm đẹp — cần dựng lại audio rồi mới có stem.
5. **Shot dài:** 33–49/108 shot vượt 15 s (chuẩn H10), dài nhất `2-12` 42,0 s (VN). Thấp hơn Tập 07
   (TB 16,9–19,4 s) nhưng vẫn trên ngưỡng. Muốn đạt H10 phải **tách shot** (108 → ~160 shot) —
   việc thiết kế lại toàn bộ kế hoạch hình, **nằm ngoài phạm vi "render lại ảnh"**. Cổng QC chỉ ghi
   nhận, không báo lỗi.
6. **Bộ ảnh nền `assets/bg/t8_*.png` (74 file) là noir trừu tượng** (gần đen, gradient/tia sáng),
   không phải cảnh diễn minh hoạa. Đây là bộ asset có sẵn của dự án, không phải lỗi render — nhưng
   nếu muốn hình minh hoạa tình huống thì phải sinh lại ảnh nền (A8).
7. **Chưa commit git.** Working tree còn nhiều thay đổi của các session trước (Tập 03/04/06/07) —
   cần chốt phạm vi trước khi commit. Theo L10, **không commit media/artifact QC** (contact sheet,
   ảnh tĩnh), chỉ commit tài liệu + code + config.

---

## 6. Cách chạy lại

```powershell
# 1. parse kịch bản (nếu kịch bản đổi tiếp)
py -3 .work/parse_kichban.py '01_KICH_BAN/Tap08/kichban_tap08_23102026.md' '.work/script_tap08.json'
py -3 .work/parse_kichban.py '01_KICH_BAN/Tap08_EN/kichban_tap08_EN.md' '.work/script_tap08_EN.json'
py -3 .work/parse_kichban.py '01_KICH_BAN/Tap08_JA/kichban_tap08_JA.md' '.work/script_tap08_JA.json'

# 2. timeline (3 ngôn ngữ) — AE_EP=08 + AE_LANG
$env:AE_EP='08'; foreach ($l in @('vi','en','ja')) { $env:AE_LANG=$l; py -3 .work/_build_timeline_t08.py $l }

# 3. bảng shot 3 ngôn ngữ (idempotent)
py -3 .work/_gen_plan_t08.py

# 4. parse + cổng QC dự án
foreach ($l in @('vi','en','ja')) { $env:AE_LANG=$l; py -3 .work/parse_shots.py; py -3 .work/_qc_tap02_shots.py }

# 5. render ảnh tĩnh (tách tiến trình, tuần tự 3 ngôn ngữ)
powershell -File .work/_render_t08_stills.ps1

# 6. QC sau render
py -3 .work/_qc_words_t08.py
py -3 .work/_qc_contrast_t08.py
py -3 .work/_qc_stats_t08.py

# 7. contact sheet (9 tab/ngôn ngữ)
foreach ($l in @('vi','en','ja')) { py -3 .work/_qc_contact_stills_t08.py $l }
```
