# BÁO CÁO DỰNG LẠI ẢNH TĨNH — TẬP 07 · 06/11/2026

**Lý do dựng lại:** kịch bản Tập 07 được **viết lại toàn bộ** (05/11/2026 — VN 18:12 · JA 18:23 · EN 18:24).
Bảng shot mục 6 và timeline cũ vẫn trỏ vào bản kịch bản **trước khi viết lại**, nên lớp chữ trên
hình không còn khớp lời đọc ⇒ **dựng lại ảnh tĩnh cho 3 ngôn ngữ** (không dựng video).

> **Phạm vi:** chỉ ảnh tĩnh (`--stills all`). **Không** dựng video, **không** dựng lại audio.
> Timeline là **tạm** (đo theo tỉ lệ từ timeline cũ) — audio master cũ đã upload/dọn.

---

## 1. Số đo thật

| Mục | VN | EN | JA | Chuẩn | Kết quả |
|---|---|---|---|---|---|
| Kịch bản | 50 element · **147 câu** | 50 element · **147 câu** | 50 element · **147 câu** | 3 bản đồng nhất | ✅ |
| Timeline (tạm) | 1299,4 s (21:39) | 1120,9 s (18:40) | 1545,6 s (25:45) | — | *(số liệu)* |
| Số shot | **66** | **66** | **66** | 1 shot / câu-giọng | ✅ |
| Phủ câu | **147/147** đúng thứ tự | 147/147 | 147/147 | 100% | ✅ |
| Ảnh tĩnh render | **66/66** | 66/66 | 66/66 | đủ, không thừa | ✅ |
| ID shot trùng | 0 | 0 | 0 | 0 | ✅ |
| Nền lặp liên tiếp tối đa | 2 shot | 2 shot | 2 shot | ≤ 4 (H10) | ✅ |
| Loại nền dùng | 61 | 61 | 61 | — | *(số liệu)* |
| Mẫu dùng | T1×50 T4×8 T8×4 T2×3 T7×1 | (như VN) | (như VN) | — | *(số liệu)* |
| Shot > 15 s | 46/66 (TB 19,4 s) | 38/66 (TB 16,7 s) | 50/66 (TB 23,1 s) | 3–15 s | ⚠ mục 5 |
| Dài nhất | `4-10` 39,2 s | `1-12` 31,0 s | `1-12` 45,2 s | ≤ 15 s | ⚠ mục 5 |
| Cổng QC A9.2 (bảng shot) | 12/12 | 12/12 | 12/12 | 12 | ✅ |
| Chữ trên hình có trong câu (A9.2) | 0 lỗi | 0 lỗi | 0 lỗi | 0 | ✅ |
| Trích dẫn nguyên văn (V3) | 0 lỗi | 0 lỗi | 0 lỗi | 0 | ✅ |
| Từ cấm trên hình | 0 | 0 | 0 | 0 | ✅ |
| Ảnh cũ hơn bảng shot | 0 | 0 | 0 | 0 | ✅ |
| Ảnh giống hệt bản 11/03 | **0/66** | (mới) | (mới) | 0 | ✅ đã render lại thật |
| Chữ chìm sau `text_scrim` (H9) | 0 shot | 0 shot | 0 shot | 0 | ✅ (mục 4) |

**Cổng QC dự án `_qc_tap02_shots.py` (AE_EP=07): VN / EN / JA đều `TAT CA DA DAT`.**

---

## 2. Các lỗi đã phát hiện và sửa

### 2.1. Timeline cũ trỏ vào kịch bản cũ (lỗi gốc rễ)

`timeline_s_t07.json` (VN) và `timeline_s_EN_t07.json` (EN) được đo từ audio của bản kịch bản
**trước** khi viết lại: **144/147 câu VN** và **143/147 câu EN** có **nội dung khác** so với
kịch bản mới; bản EN còn **164 câu** (thừa `1.06#8` `4.02#4` `5.04#19`, thiếu 3 câu mới).
JA **không có** timeline tập 07.

→ Đã dựng lại cả 3 timeline bằng `.work/_t07/_t07_build_timeline.py` (theo đúng cách
`_t06_build_timeline.py` của Tập 06): neo theo **ID element** (tập 07 giữ nguyên ID 1.01…5.14),
chia lại thời lượng câu theo độ dài câu mới, đặt lại marker BGM/SFX/NGHI/ACT/INTRO.
JA không có timeline cùng tập ⇒ lấy **RATE 5,96 ký tự/s** từ timeline JA Tập 06 (audio thật).

### 2.2. Lớp chữ trong bảng shot cũ không còn khớp lời

Bảng shot cũ dùng caption **cắt cụt bằng `...`** (vd `*…ánh sáng xanh lạnh buốt hắt lên ...*`),
viết cho lời cũ. Đã **viết lại toàn bộ 66 dòng chữ** cho 3 ngôn ngữ theo lời mới:
câu trích dẫn bám sát ý, **trích dẫn `“…”` nguyên văn** trong câu, **mọi con số trên hình
đều có trong câu** (vd đổi `1.04#3` → `1.04#2`–`#3` để có “Ford F-250” trong ngữ cảnh;
4 thẻ cờ đỏ dịch “thứ nhất…thứ tư” đúng câu để số 01–04 có cơ sở).

### 2.3. Bốn thẻ cờ đỏ lệch ngữ cảnh (H3 — ảnh phải khớp lời)

Bảng cũ đặt thẻ cờ 1 ở shot `5-04` (ngữ cảnh là phần luật “Đạo luật Conrad”), còn câu tuyên bố
cảnh báo đỏ 1 nằm ở `5.04#4`. Đã **dời ranh giới shot**:
`5-04` = `5.04#1`–`#3` (luật) · `5-05` = thẻ cờ 1 · `5-06` = `5.04#5`–`#7` (thẻ cờ 2) ·
`5-07` = `5.04#8`–`#10` (thẻ cờ 3) · `5-08` = `5.04#11`–`#13` (thẻ cờ 4).
Kết quả: **4 thẻ cờ đánh số 01→02→03→04 đúng thứ tự** trên hình, và mỗi thẻ có đúng câu
tuyên bố cảnh báo tương ứng trong ngữ cảnh của nó.

### 2.4. Badge vai EN/JA ghi sai hồ sơ khác

`edition.py` mặc định lấy nhãn vai của **Tập 01** ⇒ bản EN hiện “INVESTIGATOR / **Blanchard
case file**”, bản JA hiện “捜査官 / **事件記録 Blanchard**”. Đã khai riêng cho tập 07
(`roles_en` / `roles_ja` / `sub_tags_en` / `sub_tags_ja`): Carter Case File · 事件記録 Carter ·
LYNN ROY (Victim's Mother) · SAMANTHA BOARDMAN (Witness Testimony).

### 2.5. Tuyến đường không có nhãn địa điểm

`route_pins` rỗng ⇒ template T7 (shot `2-02`) chỉ vẽ cung đường không có tên. Đã thêm
`{"2-02": ("Plainville", "Fairhaven")}` — khớp lời “chỉ cách … ba mươi lăm dặm”.

---

## 3. File đã tạo / sửa

| File | Việc |
|---|---|
| `02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md` | mục 6 viết lại (66 dòng, chữ mới) + ghi chú dựng lại |
| `02_SAN_XUAT/Tap07_EN/KeHoach_Video_Tap07_EN.md` | **thêm mục 6** (chưa có) + số câu 164→147 + ghi chú dựng lại |
| `02_SAN_XUAT/Tap07_JA/KeHoach_Video_Tap07_JA.md` | **tạo mới** (Part B + mục 6) |
| `.work/edition.py` | `roles_en` `roles_ja` `sub_tags_en` `sub_tags_ja` `route_pins` `text_scrim` cho tập 07 |
| `.work/timeline_s_t07.json` / `_EN_` / `_JA_` | dựng lại (147 câu) |
| `.work/shots_t07.json` / `_EN_` / `_JA_` | sinh lại từ bảng shot mới |
| `.work/video3_t07/stills` | **66 ảnh render lại** |
| `.work/video3_EN_t07/stills` | **66 ảnh mới** (thư mục chưa tồn tại) |
| `.work/video3_JA_t07/stills` | **66 ảnh mới** (thư mục chưa tồn tại) |
| `02_SAN_XUAT/Tap07/contact_sheet_stills_t07_vi.png` | contact sheet 66 shot (review 1 lượt) |
| `02_SAN_XUAT/Tap07_EN/contact_sheet_stills_t07_en.png` | contact sheet 66 shot EN |
| `02_SAN_XUAT/Tap07_JA/contact_sheet_stills_t07_ja.png` | contact sheet 66 shot JA |
| `.work/_t07/` | script dựng (timeline, bảng shot, QC tương phản, QC ảnh, contact sheet, backup) |

**Bản sao lưu (L5):** `.work/_cu/t07_20261106/` — bảng shot VN/EN cũ, timeline cũ VN/EN,
`shots_t07.json` cũ, 66 ảnh VN cũ (`stills` + `stills_final`), `edition.py` cũ.

---

## 4. Độ tương phản chữ (H9 `text_scrim`)

Đo bằng `.work/_t07/_t07_scan_contrast.py` (đúng cách `_t06_scan_contrast.py` của Tập 06):
lấy vị trí nét chữ (alpha = 255), nền = `bg_frame` + lớp phủ toàn khung, ngưỡng **> 8 % nét chữ bị chìm**.

**Lần 1 — 13 shot bị chìm** (VN 77,7 % ở `2-07`; EN 81,7 %; JA 81,4 %) ⇒ đã bật
`text_scrim` cho 12 shot: `1-11 1-14 2-03 2-07 2-09 3-01 3-02 3-05 3-11 4-02 4-10 4-13`.

**Lần 2 — vẫn còn `2-07` 43,8 % / `2-03` 11,1 %:** nhánh scrim của template **T5** phủ
`y 360–800` nhưng nhãn T5 được vẽ ở `y ≈ 330` ⇒ scrim không phủ đúng chữ.
→ Đổi mẫu `2-03` và `2-07` từ **T5 ngày** sang **T1** (48/66 shot còn lại vốn là T1, chữ nằm
đáy khung và dùng đúng nhánh scrim đã chứng minh chạy tốt). **Không sửa `build_video3.py`**
để không ảnh hưởng Tập 04/06 (đang dùng chung nhánh scrim T5).

**Lần 3 (cuối):** VN / EN / JA — **0 shot cần scrim**, chỉ còn `4-04` bị báo (47 %) — đây là
**báo nhầm**: template T2 vẽ một tấm thẻ sáng, phần đo lấy màu tấm thẻ chứ không phải màu chữ;
soi mắt xác nhận chữ đỏ trên nền kem **đọc rõ**. Renderer cũng không có nhánh scrim cho T2.

---

## 5. Cảnh báo còn lại (không sửa trong lượt này)

1. **Shot dài:** 38–50/66 shot vượt 15 s (chuẩn H10). Đây là **đặc tính có sẵn** của bảng shot
   tập 07 từ 03/11 (40/66 shot > 15 s, dài nhất 32 s) — kịch bản viết lại chỉ làm tập **dài hơn**
   (VN 1134,9 s → 1299,4 s). Muốn đạt H10 phải **tách shot** (66 → ~110 shot) — việc thiết kế lại
   toàn bộ kế hoạch hình, **nằm ngoài phạm vi “render lại ảnh”**. Cổng QC chỉ ghi nhận, không báo lỗi.
2. **Sóng âm trên badge vai là đường gạch phẳng** (không có stem): `.work/stems_t07*/` đã bị dọn
   cùng audio master, và audio master của bản kịch bản cũ không còn khớp với lời mới.
   Không bịa envelope để làm đẹp — cần dựng lại audio rồi mới có stem (bài học Tập 03).
3. **`intro_kenh_EN_t07.mov` / `intro_kenh_JA_t07.mov` không tồn tại** (`assets/brand/` chỉ có
   bản `t02`–`t06` + bản chung). Chỉ ảnh hưởng **video** (lớp intro 0–22,41 s), **không ảnh hưởng ảnh tĩnh**.
4. **Lỗi chính tả trong kịch bản EN** (không sửa, thuộc bản kịch bản của bạn): `2.03#2` dùng
   dấu nháy kép làm dấu nháy đơn — `Conrad“s home`, `an hour”s drive`.
5. **Audio master của bản kịch bản cũ** (164 câu EN) không còn khớp lời mới (147 câu) ⇒ khi dựng
   video phải **dựng lại audio** cho cả 3 ngôn ngữ.

---

## 6. Cách chạy lại

```powershell
# 1. timeline (nếu kịch bản đổi tiếp)
py -3 .work/_t07/_t07_build_timeline.py vi|en|ja

# 2. bảng shot 3 ngôn ngữ (idempotent — chạy lại nhiều lần cho kết quả giống hệt)
py -3 .work/_t07/_t07_preflight.py          # kiểm trước khi ghi
py -3 .work/_t07/_t07_build_table.py vi|en|ja

# 3. parse + cổng QC dự án
$env:AE_EP="07"; $env:AE_LANG="vi|en|ja"; py -3 .work/parse_shots.py
$env:AE_EP="07"; $env:AE_LANG="vi|en|ja"; py -3 .work/_qc_tap02_shots.py

# 4. render ảnh tĩnh (tách tiến trình, tuần tự 3 ngôn ngữ)
powershell -File .work/_t07/_render_t07.ps1

# 5. QC sau render
py -3 .work/_t07/_t07_qc_stills.py
py -3 .work/_t07/_t07_scan_contrast.py vi|en|ja

# 6. contact sheet (tuỳ chọn — để review 66 shot trong 1 ảnh)
py -3 .work/_t07/_t07_contact_sheet.py all
```
