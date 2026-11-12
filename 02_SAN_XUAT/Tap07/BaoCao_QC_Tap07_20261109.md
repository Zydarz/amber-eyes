# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 07 · 09/11/2026

**Phạm vi lượt này:** đọc kịch bản Tập 07 **viết lại (219 câu)** và **render lại ảnh tĩnh cho 3 ngôn ngữ** (tiếng Việt · tiếng Anh · tiếng Nhật). **KHÔNG tạo video** (theo yêu cầu).

**Sản phẩm:**
- Ảnh tĩnh: `.work/video3_t07/stills/` · `.work/video3_EN_t07/stills/` · `.work/video3_JA_t07/stills/` — **223 ảnh/ngôn ngữ** (1920×1080 PNG).
- Contact sheet để soi: `02_SAN_XUAT/Tap07*/contact_sheet_stills_t07_{vi,en,ja}_p1..p5.png` (5 tờ/ngôn ngữ, 48 ảnh/tờ).
- Hồ sơ: `02_SAN_XUAT/Tap07*/KeHoach_Video_Tap07*.md` (mục 6 = bảng shot 223 dòng).

---

## 1. Số đo thật (không ước lượng)

| Mục | VN | EN | JA | Chuẩn | Kết quả |
|---|---|---|---|---|---|
| Câu trong kịch bản | 219 | 219 | 219 | — | ✅ |
| Element | 50 | 50 | 50 | — | ✅ |
| Shot trong bảng mục 6 | **223** | **223** | **223** | 1 ảnh/shot | ✅ |
| Ảnh tĩnh render | **223** | **223** | **223** | = số shot | ✅ 0 thiếu · 0 thừa |
| Câu được phủ bởi bảng shot | 219/219 | 219/219 | 219/219 | 100% | ✅ |
| Thời lượng timeline | 1843,8 s (30:43) | 1639,59 s (27:19) | 1997,64 s (33:17) | — | ⚠ ước lượng (§6) |
| Shot nội dung > 15 s | **0** (max 13,7 s) | **0** (max 11,3 s) | **0** (max 13,3 s) | H10 | ✅ |
| Shot nội dung < 3 s | 0 | 1 (`1-01` 2,1 s) | 1 (`1-01` 2,7 s) | H10 | ⚠ đã chấp nhận (§6) |
| Đoạn nền lặp dài nhất | 3 shot | 3 shot | 3 shot | ≤ 4 (H10) | ✅ |
| Shot > 8% nét chữ bị "chìm" | **0** (max 6,7%) | **0** (max 6,6%) | **0** (max 7,8%) | H9 | ✅ |
| Thẻ kết `5-37` — pixel sáng | max 249 · TB 65,2 · 25,2% >100 | max 250 · TB 64,9 · 25,0% >100 | max 245 · TB 65,1 · 25,2% >100 | H12 | ✅ |
| Dung lượng 1 ảnh | 2,3–3,4 MB | 2,3–3,4 MB | 2,3–3,4 MB | — | ✅ |
| Thời gian render | 3 ph 21 s | 3 ph 20 s | 2 ph 61 s | — | — |

**Cổng QC dự án `_qc_tap02_shots.py` (AE_EP=07): `TAT CA DA DAT` — cả 3 ngôn ngữ.**
8 cổng đều xanh: phủ câu 219/219 · thứ tự shot khớp kịch bản · cột Vai khớp người nói · nền có file thật (`nền chưa có file: []`) · trích dẫn `“…”` nguyên văn trong câu · **mọi con số trên hình có trong câu** (A9.2) · 0 từ cấm · shot liền kề không hở/chồng.
Ghi chú duy nhất: `5-37` có số `07` — đã ghi nhận là **nhãn cấu trúc** (số tập), không phải dữ kiện bịa.

**Cổng QC H10 (`_t07_qc_all.py`): `✓ TẤT CẢ ĐẠT` — cả 3 ngôn ngữ.**
ID shot duy nhất 223/223 · ảnh tĩnh **mới hơn bảng shot** (ảnh cũ nhất 10:09:29 > bảng shot 09:41:56) · không ảnh rỗng/hỏng.
Log: `.work/qc_final_t07/qc_h10_t07.txt`.

---

## 2. Bảng shot viết lại — 219 câu ⇒ 223 dòng

| Thành phần | Số dòng |
|---|---|
| Shot nội dung | 218 (217 shot 1 câu + 1 shot 2 câu `5.04#17`+`#18`) |
| Thẻ chuyển hồi (T10) | 4 (`1-48` Hồi 2 · `2-45` Hồi 3 · `3-49` Hồi 4 · `4-44` Hồi 5) |
| Thẻ kết | 1 (`5-37`) |
| **Tổng** | **223** |

Mẫu dùng: **T1×209** (chữ nguyên văn) · **T4×5** (thẻ trích dẫn) · **T10×4** (chuyển hồi) · **T8×4** (4 cờ đỏ) · **T7×1** (tuyến đường Plainville ↔ Mattapoisett) · 62 loại nền (61 `t7_*` + `void`).

**Quyết định lớn:** lớp chữ trên hình = **nguyên văn câu kịch bản của shot** (A7/V3/H6) thay vì viết tay ⇒ tự đạt quy tắc số trên hình / trích dẫn nguyên văn / từ cấm, và khớp đúng lời đọc.
**Quy tắc 1 câu = 1 shot:** ảnh tĩnh được chụp ở **giữa shot**; shot nhiều đoạn làm đoạn 2 chưa kịp hiện (đo được 3/6 shot lỗi trước khi sửa) ⇒ mỗi shot chỉ có 1 khối chữ.

---

## 3. Lỗi kịch bản đã sửa (4 chỗ, có kiểm chứng)

| File | Vị trí | Lỗi | Đã sửa |
|---|---|---|---|
| `01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md` | dòng 215 | còn sót **tiêu đề vai tiếng Việt** `**CHUYÊN GIA TÂM LÝ**` ⇒ `parse_kichban` nhận nhầm bản VN ⇒ dấu `'` trong *"Achilles' heel"* bị ghép sai ⇒ sinh `Achilles“ heel` | `**PSYCHOLOGIST** *(exposing the mechanism of Cognitive Compartmentalization & Dehumanization of the Victim)*` |
| `01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md` | `1.02#3` | từ cấm EN `struggle` | `no physical trace of a fight at the scene` |
| `01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md` | `1.06#2` | từ cấm EN `struggle` | `internal conflict` |
| `01_KICH_BAN/Tap07/kichban_tap07_23102026.md` | `2.06#2` | từ cấm VN `đòn roi` | `không sử dụng bạo lực thể xác` (khớp EN/JA) |

Bản JA **không đổi nội dung** (4 câu có khoảng trắng đầu dòng là artifact của parser, xử lý khi dựng bảng, không sửa parser dùng chung).
Sau khi sửa: 3 script JSON parse lại → **219 câu, id khớp, text khớp 100%**; quét từ cấm: **0** (VN/EN), JA 0. Line ending CRLF giữ nguyên (348 dòng/file, không BOM).

---

## 4. H9 — chữ "chìm" trên nền sáng: 65 shot được thêm lớp tối mềm

Đo bằng `_t07/_t07_scan_contrast.py` (đúng vị trí nét chữ, nền = `bg_frame` + lớp phủ toàn khung theo đúng thứ tự renderer; ngưỡng: tương phản < 1,6 **hoặc** |Δlum| < 45, cần scrim khi > 8% nét chữ).

| | VN | EN | JA |
|---|---|---|---|
| Shot > 8% **trước** | 50 | 52 | 61 |
| Shot tệ nhất **trước** | 53,2% (`1-01`) | 42,6% | 44,0% |
| **Hợp 3 ngôn ngữ** | **65 shot** (`text_scrim` trong `edition.py`) | | |
| Shot > 8% **sau** | **0** | **0** | **0** |
| Tệ nhất **sau** | 6,7% | 6,6% | 7,8% |

Kiểm chứng bằng mắt trên ảnh thật: `3-01` (trước 52,8% chìm) → dải chữ nằm trên lớp tối mềm, chữ đọc rõ.

---

## 5. H12 — thẻ kết bị mờ đen: đã sửa ở gốc

**Triệu chứng:** ảnh tĩnh `shot_5-37.png` (thẻ "HỒ SƠ TẬP 07 · ĐÃ ĐÓNG") gần như **đen** — VN max 97 / TB 24,2 / 0% pixel > 100; EN & JA max 95 / TB 24,8.

**Nguyên nhân (đo được, không đoán):** `build_video3.py` làm mờ **shot cuối** sang đen từ `start + 4,0 s` trong 3,0 s (`render()`), còn ảnh tĩnh được chụp ở **giữa shot**. Với `OUTRO = 10 s` ⇒ thẻ kết dài 11,5 s ⇒ giữa shot = +5,75 s ⇒ ảnh bị phủ **62% đen**.

**Sửa (ở dữ liệu, không đụng renderer dùng chung):** `OUTRO 10,0 → 6,0` (`_t07_build_timeline.py`) ⇒ thẻ kết dài **7,5 s** ⇒ giữa shot = +3,75 s ⇒ hệ số mờ = 0.
Kết quả đo lại: **VN max 249 · TB 65,2 · 25,21% pixel > 100** · **EN max 250 · 25,04%** · **JA max 245 · 25,17%** ⇒ thẻ kết đọc rõ ở cả 3 ngôn ngữ (soi mắt: "HỒ SƠ TẬP 07 · ĐÃ ĐÓNG" + "AMBER EYES · …" + khẩu hiệu).

---

## 6. Lỗi chữ đè nhau ở thẻ giới thiệu nhân vật — đã sửa, có hồi quy Tập 01

**Triệu chứng:** ở shot lần đầu của mỗi vai, thẻ giới thiệu nhân vật (tên vai + vai trò + "Nhân vật minh họa · giọng đọc AI") được vẽ ở `(490, H-250)` — **trùng khung chữ T1 ở đáy** ⇒ chữ "HOST" đè lên câu đầu. Lỗi ở **3 shot/ngôn ngữ** (`1-01`, `1-22`, `1-32`; EN thêm `4-07`).

**Sửa:** thêm 3 khoá **tuỳ chọn theo tập** trong `build_video3.py` (mặc định giữ nguyên hành vi cũ):
`intro_card_pos` (đặt thẻ lên cao 490,250) · `intro_card_panel` (nền tối + viền màu vai cho thẻ) · `intro_card_hold` (giữ thẻ đặc tới 5,8 s thay vì mờ từ 3,6 s — tính từ số đo thật: giữa shot nằm ở +0,82 … +5,67 s so với lượt đầu của vai).

**Hồi quy Tập 01 (L9):** render lại `shot_1-01` + `shot_3-17` của Tập 01 trước và sau khi sửa ⇒ **hash MD5 giống hệt** (`89D124DEAE942B70EE84EC0FE8B77286`, `1D0DE2793A349D87917341D37FD6FF5E`) ⇒ các tập khác không bị ảnh hưởng.

---

## 7. Cảnh báo (không phải lỗi) & việc còn lại

| # | Nội dung | Xử lý |
|---|---|---|
| 1 | **Timeline là ước lượng** — RATE 15,50 (VN) · 18,10 (EN) · 5,96 (JA) ký tự/s, neo được 28 element (VN/EN), JA neo 0 (lấy RATE từ timeline JA Tập 06) | Chưa có audio master 219 câu ⇒ thời lượng shot trong bảng là **số tạm**; phải đo lại khi dựng audio |
| 2 | 2 shot < 3 s: `1-01` EN 2,1 s · JA 2,7 s | Đã chấp nhận (ghép sẽ vượt 15 s ở VN = 15,24 s); cùng tính chất thẻ mốc Tập 06 |
| 3 | 9 thẻ mốc ngắn theo thiết kế: T10 ×4 (1,8 s) · T8 ×4 (2,3–5,0 s) · thẻ kết 7,5 s | Không tính vào H10 vế 1 (giống Tập 06) |
| 4 | `02_SAN_XUAT/Tap07/nguon_tham_khao.md` (56 dữ kiện × 54 nguồn) và `mo_ta.txt` viết cho bản **147 câu** | Phải rà lại khi đóng gói — **ngoài phạm vi lượt này** |
| 5 | `assets/brand/intro_kenh_EN_t07.mov` **thiếu** | Không ảnh hưởng ảnh tĩnh (mọi still nằm sau 22,41 s) |
| 6 | Tooling T7 nằm ở `.work/_t07/` mà `.gitignore` loại `.work/*` ⇒ **0 file trong `.work/_t07` được git track** | Muốn commit code phải thêm `!.work/_t07/*.py` hoặc chuyển script lên `.work/` |
| 7 | **Chưa commit gì** (repo có sẵn 30 file đổi từ phiên khác) | Theo L10 (cấm commit media/artifact QC) và vì người dùng chưa yêu cầu |

---

## 8. Sao lưu (L5)

| Bản cũ | Đường dẫn |
|---|---|
| Kịch bản + 3 hồ sơ + `edition.py` (trước khi sửa chữ & `need`) | `.work/_cu/t07_fix_20261109/` |
| Bản 147 câu (kịch bản + bảng shot + tooling `_t07/`) | `.work/_cu/t07_cu_20261107/` |
| `_t07_build_timeline.py` (trước khi đổi `OUTRO`) | `.work/_cu/_t07_build_timeline_20261109.py.bak` |
| `_t07_gen_table.py` (trước khi đổi dòng thẻ kết) | `.work/_cu/_t07_gen_table_20261109.py.bak` |
| `edition.py` (trước khi ghi `text_scrim`) | `.work/_cu/edition_20261109.truoc_scrim.py.bak` |
| `build_video3.py` (trước khi thêm khoá `intro_card_*`) | `.work/_cu/build_video3_20261109.truoc_introcard.py.bak` |
| `provenance.json` (trước khi thêm dòng Tập 07) | `.work/_cu/provenance.backup_20261109_t06ja_thumb.json` |

---

## 9. Truy vết tài sản (L7)

`provenance.json`: **2231 mục** (trước: 2215) — thêm **16 dòng** cho lượt 09/11/2026: 3 kịch bản · 3 hồ sơ · 3 bảng shot máy · 3 timeline · `build_video3.py` · `edition.py` · 3 thư mục ảnh tĩnh.
File giữ nguyên định dạng: **CRLF**, `indent=2`, **không BOM**, JSON hợp lệ (đã kiểm parse sau khi ghi).

---

## 10. Công cụ dùng lượt này (`.work/_t07/`)

`_t07_build_timeline.py` (timeline ước lượng) · `_t07_group.py` (1 câu = 1 shot, H10) · `_t07_gen_table.py` (bảng shot 223 dòng) · `_t07_build_table.py` (ghi mục 6 vào 3 hồ sơ, idempotent) · `_t07_preflight.py` · `_t07_scan_contrast.py` (H9) · `_t07_update_text_scrim.py` · `_t07_qc_all.py` (H10) · `_t07_measure_endcard.py` (H12) · `_t07_contact_sheet.py` · `_t07_add_provenance.py` · `_t07_update_plan_meta.py` · `_t07_update_plan_durations.py` · `_t07_update_plan_note.py` · `_t07_fix_script_text.py` · `_t07_fix_eol.py` · `_t07_intro_affect.py` · `_t07_intro_hold_need.py` · `_t07_fix_provenance.py`.
