# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 08 · 09/11/2026

**Phạm vi lượt này:** đọc kịch bản Tập 08 **viết lại (218 câu / 53 element)** và **render lại ảnh tĩnh cho 3 ngôn ngữ** (tiếng Việt · tiếng Anh · tiếng Nhật). **KHÔNG tạo video** (theo yêu cầu).

**Sản phẩm:**
- Ảnh tĩnh: `.work/video3_t08/stills/` · `.work/video3_EN_t08/stills/` · `.work/video3_JA_t08/stills/` — **223 ảnh/ngôn ngữ** (1920×1080 PNG).
- Contact sheet để soi: `02_SAN_XUAT/Tap08*/contact_sheet_stills_t08_{vi,en,ja}_p1..p5.png` (5 tờ/ngôn ngữ, 48 ảnh/tờ).
- Hồ sơ: `02_SAN_XUAT/Tap08*/KeHoach_Video_Tap08*.md` (mục 6 = bảng shot 223 dòng).

---

## 1. Số đo thật (không ước lượng)

| Mục | VN | EN | JA | Chuẩn | Kết quả |
|---|---|---|---|---|---|
| Câu trong kịch bản | 218 | 218 | 218 | — | ✅ |
| Element | 53 | 53 | 53 | — | ✅ |
| Shot trong bảng mục 6 | **223** | **223** | **223** | 1 ảnh/shot | ✅ |
| Ảnh tĩnh render | **223** | **223** | **223** | = số shot | ✅ 0 thiếu · 0 thừa |
| Câu được phủ bởi bảng shot | 218/218 | 218/218 | 218/218 | 100% | ✅ |
| Thời lượng timeline | 1957,51 s (32:37) | 1895,91 s (31:35) | 2095,36 s (34:55) | — | ⚠ khớp TỔNG master (§6) |
| Shot nội dung > 15 s | **0** (max 14,0 s) | **0** (max 12,7 s) | **1** (`5-27` 15,3 s) | H10 | ⚠ JA vượt 0,3 s (§7) |
| Shot nội dung < 3 s | 0 | 0 | 0 | H10 | ✅ |
| Đoạn nền lặp dài nhất | 2 shot | 2 shot | 2 shot | ≤ 4 (H10) | ✅ |
| Shot > 8% nét chữ bị "chìm" | **0** (max 7,2%) | **0** (max 7,8%) | **0** (max 7,5%) | H9 | ✅ (43 shot đã bật `text_scrim` — §5) |
| Ảnh nền `t8_*` dùng trong shot | **74** | **74** | **74** | MiniMax | ✅ 74/74 sinh bằng `connector__matrix__generate_image` (§5.1) |
| Ảnh nền có viền trắng/đen | **0** | **0** | **0** | V7 tràn viền | ✅ (1 ảnh đã cắt — §5.1) |
| Thẻ kết `5-41` — pixel sáng | max 172 · TB 62,2 · 24,88% >100 | max 172 · TB 62,5 · 25,08% | max 178 · TB 60,9 · 23,77% | H12 | ✅ đọc rõ |
| Dung lượng 1 ảnh | 2,0–3,5 MB | 2,0–3,5 MB | 2,0–3,5 MB | — | ✅ |
| Thời gian render (lần cuối, 18:12–18:17) | 2 ph 38 s | 3 ph 38 s | 1 ph 49 s | — | — |
| MD5 669 ảnh sau render lại | **0 khác** | **0 khác** | **0 khác** | H15 tất định | ✅ (đo trên nền cũ; code renderer không đổi) |

**Cổng QC dự án `_qc_tap02_shots.py` (AE_EP=08): `TAT CA DA DAT` — 8/8 cổng ở CẢ 3 ngôn ngữ.**

| Cổng | VN | EN | JA |
|---|---|---|---|
| Mọi câu trong timeline có mặt trong bảng shot (thiếu/thừa) | ✅ [] | ✅ [] | ✅ [] |
| Không câu nào thuộc hai shot | ✅ | ✅ | ✅ |
| Câu được phủ | ✅ 218/218 | ✅ 218/218 | ✅ 218/218 |
| Thứ tự shot khớp thứ tự kịch bản | ✅ | ✅ | ✅ |
| Cột Vai khớp người nói | ✅ | ✅ | ✅ |
| Mọi nền dùng trong shot đều có file | ✅ | ✅ | ✅ |
| Chữ trích dẫn nguyên văn (lược bằng …) trong câu — V3 | ✅ 0 lỗi | ✅ 0 lỗi | ✅ 0 lỗi |
| Mọi con số trên hình có trong câu — A9.2 | ✅ 0 lỗi | ✅ 0 lỗi | ✅ 0 lỗi |
| Không từ cấm / không nhắc hành vi tình dục trên hình | ✅ **0 lỗi** | ✅ **0 lỗi** | ✅ 0 lỗi |
| Shot > 15 s có nhịp hoặc bám V2 | ✅ | ✅ | ✅ |
| Các shot liền nhau (không hở/chồng) | ✅ | ✅ | ✅ |

Ghi chú: `5-41` có số `08` — đã ghi nhận là **nhãn cấu trúc** (số tập), không phải dữ kiện bịa.

**Cổng QC H10 (`_t08_qc_all.py`): VN ✅ · EN ✅ · JA ⚠ 1 lỗi (`5-27`).**
ID shot duy nhất 223/223 · ảnh tĩnh **mới hơn bảng shot** (ảnh cũ nhất 12:25:18 > bảng shot 12:04:46) · không ảnh rỗng/hỏng.
Log: `.work/qc_final_t08/qc_h10_t08.txt`.

---

## 2. Bảng shot viết lại — 218 câu ⇒ 223 dòng

| Thành phần | Số dòng |
|---|---|
| Shot nội dung | 218 (1 câu = 1 shot) |
| Thẻ chuyển hồi (T10) | 4 (`1-48` · `2-45` · `3-49` · `4-44`) |
| Thẻ kết (T2) | 1 (`5-41`) |
| **Tổng** | **223** |

Mẫu dùng: **T1×202** (chữ nguyên văn) · **T4×12** (thẻ trích dẫn — 12 câu "lời kể") · **T8×4** (4 cờ đỏ) · **T10×4** (chuyển hồi) · **T2×1** (thẻ kết) · 74 loại nền `t8_*`.

**Quyết định lớn:** lớp chữ trên hình = **nguyên văn câu kịch bản của shot** (A7/V3/H6) ⇒ tự đạt quy tắc số trên hình / trích dẫn nguyên văn / từ cấm, và khớp đúng lời đọc.
**Quy tắc 1 câu = 1 shot:** ảnh tĩnh được chụp ở **giữa shot**; shot nhiều đoạn làm đoạn 2 chưa kịp hiện ⇒ mỗi shot chỉ có 1 khối chữ (bài học Tập 07).

---

## 3. Cấu hình tập — `edition.py` (L8: chỉ sửa trong khối `"08"`)

Thêm vào `EPISODES["08"]`:
- `"text_scrim": [42 id]` — H9 đo lại **sau khi đổi nền sang MiniMax**: nền ảnh thật sáng hơn nền texture cũ ⇒ **42 shot** có chữ bị "chìm" (>8% nét chữ). Đã bật lớp tối mềm (`soft_scrim`) cho 42 id đó; đo lại ⇒ **0/223 shot** còn chìm ở cả 3 ngôn ngữ (tệ nhất 7,3% / 7,8% / 7,5%).
- `"intro_card_pos": [490, 250]` · `"intro_card_panel": True` · `"intro_card_hold": 5.8` — thẻ giới thiệu nhân vật đặt cao (không đè chữ T1 ở đáy) và giữ đặc tới giữa shot. Ngưỡng 5,8 s đo từ yêu cầu thực tế ≥ 5,71 s (VN).

Sao lưu trước khi sửa: `.work/_cu/t08_20261109/edition.py.truoc_t08`.

---

## 4. Lỗi còn lại — 7 câu chứa từ cấm A9.2 → **ĐÃ XỬ LÝ (lược từ cấm trên hình)**

Cổng QC dự án báo lỗi ở **VN 6 câu / EN 1 câu / JA 0 câu**:

| Ngôn ngữ | Shot | Từ bị báo | Câu (trích) |
|---|---|---|---|
| VN | `2-28` | "sát hại" | `2.07#5` — gia đình bị sát hại |
| VN | `2-29` | "sát hại" | `2.07#6` |
| VN | `4-24` | "máu" | `4.05#6` |
| VN | `4-38` | "máu" | `4.09#2` |
| VN | `5-13` | "đòn" | `5.04#1` |
| VN | `5-21` | "đòn" | `5.05#2` |
| EN | `4-24` | "blood" | `4.05#6` — "blood-stained" |

Bản JA đã né sạch (dùng "血塗られた手" thay vì chữ Latin ⇒ regex ASCII không khớp).

**Quyết định người dùng 09/11/2026: LƯỢC TỪ CẤM TRÊN HÌNH bằng "…" — KHÔNG sửa kịch bản.**

| | Nội dung |
|---|---|
| Kịch bản (3 ngôn ngữ) | **KHÔNG đổi** — 218 câu, nguyên vẹn |
| Audio master (3 ngôn ngữ) | **KHÔNG đổi** — không lệch 0,000 s |
| Timeline (3 ngôn ngữ) | **KHÔNG đổi** — mốc thời gian giữ nguyên |
| Chỉ lớp "chữ trên hình" | thay từ cấm bằng `…` (theo ranh giới từ, giữ cụm an toàn: "ung thư máu", "bàn tay", "đầu não"…) |

**Thực hiện:** vá `_t08_gen_table.py` (thêm `luoc_tam()` — danh sách từ cấm **đúng bằng** danh sách trong cổng dự án `_qc_tap02_shots.py` + cụm EN "blood-stained") → sinh lại bảng shot → ghi lại mục 6 (idempotent) → `parse_shots.py` → render lại ảnh tĩnh.
Sao lưu trước khi vá: `.work/_cu/t08_20261109/_t08_gen_table.py.truoc_luc` + `_t08_table.json.truoc_luc`.

**Kết quả sau khi lược (QC dự án chạy lại):**

| | VN | EN | JA |
|---|---|---|---|
| Cổng từ cấm A9.2 | ✅ **0 lỗi** | ✅ **0 lỗi** | ✅ 0 lỗi |
| Tổng số cổng | ✅ **8/8 TẤT CẢ ĐẠT** | ✅ **8/8 TẤT CẢ ĐẠT** | ✅ **8/8 TẤT CẢ ĐẠT** |

6 dòng VN + 1 dòng EN đã lược (ví dụ `2-28`: *"… đã bị **…** dã man ngay tại nhà riêng…"*; `4-24` EN: *"… believes their **…** hands are performing…"*).

---

## 5. H9 — chữ "chìm" trên nền sáng: **đã bật `text_scrim` cho 42 shot**

Đo bằng `_t08/_t08_scan_contrast.py` (đúng vị trí nét chữ; nền được **dựng lại theo đúng thứ tự renderer** — mỗi element ghép vào nền trước khi đo; ngưỡng: tương phản < 1,6 **hoặc** |Δlum| < 45, cần scrim khi > 8% nét chữ).

**Vì sao phải can thiệp:** nền MiniMax là **ảnh thật, sáng, nhiều vùng sáng** (đèn, kính, giấy) — khác hẳn nền texture tối của lần trước. Chữ trắng chạm vùng sáng ⇒ "chìm".

| | VN | EN | JA |
|---|---|---|---|
| Shot > 8% nét chữ chìm — **trước** khi bật scrim | 30 | 36 | 37 |
| Shot > 8% nét chữ chìm — **sau** khi bật scrim | **0** | **0** | **0** |
| Tệ nhất (sau) | 7,2% (`3-18`) | 7,8% (`3-18`) | 7,5% (`4-40`) |

`text_scrim` của Tập 08 = **hợp 3 ngôn ngữ, 43 id** (ghi trong `edition.py` khối `"08"`): `1-02 · 1-09 · 1-31 · 1-33 · 1-36 · 1-39 · 1-41 · 2-17 · 2-23 · 2-36 · 3-07 · 3-10 · 3-17 · 3-19 · 3-25 · 3-27 · 3-31 · 3-35 · 3-36 · 3-38 · 3-40 · 3-42 · 3-44 · 4-04 · 4-07 · 4-08 · 4-18 · 4-19 · 4-20 · 4-21 · 4-22 · 4-24 · 4-25 · 4-26 · 4-37 · 4-39 · 4-42 · 4-43 · 5-09 · 5-20 · 5-22 · 5-37 · 5-41`.

> `3-07` được thêm sau vòng đo cuối: ảnh nền `t8_matsumoto_court_dossier` đã cắt viền trắng nên sáng hơn một chút ⇒ chữ JA của shot đó chìm 9,1% (> 8%). Bật scrim → đo lại 7,5%.

**Sửa lỗi đo (quan trọng):** lần đo đầu báo `5-41` (thẻ kết T2) là "chìm 19,7%" — **lỗi giả**: thẻ kết là một **tấm giấy đục** (alpha = 255 toàn bộ) nên script cũ tính nhầm mải giấy là "nét chữ", trong khi chữ thật nằm trên nền giấy sáng ⇒ tương phản rất cao. Đã vá scanner: element có > 50% pixel đục ⇒ coi là **NỀN**, ghép vào nền rồi mới đo chữ. Sau khi vá: `5-41` không còn bị báo; soi mắt thẻ kết (3 ngôn ngữ) — chữ đen trên giấy sáng, đọc rõ.

---

## 5.1. Ảnh nền Tập 08 — đã sinh lại bằng **MiniMax** (74/74)

| | Trước | Sau |
|---|---|---|
| Công cụ | `Amber Eyes Noir Graphic Renderer` (Pillow & Numpy procedural — **vẽ bằng code**) | **`connector__matrix__generate_image` (MiniMax qua mcode-tools)** — đúng công cụ Tập 02–07 (402 ảnh) |
| Bản chất | texture trừu tượng, suy ra từ **tên file** ⇒ **vi phạm H3** (ảnh không khớp lời) | ảnh cảnh thật theo prompt từng cảnh ⇒ khớp lời |
| Kích thước | 2112×1188 | 2112×1188 (2752×1536 → crop 16:9) |
| Số lượng | 74 | **74/74**, 0 lỗi |

- **Prompt:** `.work/bg_jobs_tap08.json` (74 prompt thô) + `STYLE`/`NEG` **giống hệt** `gen_images.py` của dự án (`aspect_ratio 16:9`, `resolution 2K`).
- **Runner riêng** `.work/_t08/_t08_gen_bg_minimax.py` — **không sửa `gen_images.py`** (script dùng chung, L9). Runner ghi `provenance.json` bằng **splice văn bản** (giữ `indent=1` + CRLF + không BOM) và có **checkpoint JSONL** ⇒ chạy lại không tốn thêm credit.
- **Sao lưu 74 nền cũ:** `.work/_cu/t08_bg_20261109/` (L5).

**Sinh lại 2 ảnh vì AI vẽ chữ đọc được (H5):** soi 74 nền bằng contact sheet riêng (`.work/qc_final_t08/contact_sheet_bg_t08_p1..p7.png`) ⇒ 2 nền có chữ/số **đọc được**:
`t8_dossier_elite_scientists` (sách in *"UNIVERSITY REGISTRY"*, *"TECHNICAL SCIENCE JOURNALS"*) và `t8_sarin_synthesis_laboratory` (màn hình hiện số `2.0`/`88`).
Đã sinh lại 2 ảnh này bằng **negative mạnh hơn** (cấm mọi chữ/số trên sách, giấy, nhãn, màn hình) → ảnh mới sạch chữ, đã soi lại bằng mắt. Các nền còn lại chỉ có nét chữ **không đọc được** (giấy viết tay, bảng đen, báo) — không vi phạm.

**Hệ quả đo được:** nền sáng hơn ⇒ **43 shot** cần lớp `text_scrim` (mục 5). Không có thay đổi nào đối với **kịch bản / audio master / timeline** — chỉ tài sản hình ảnh.

**Viền trắng còn sót (V7):** 1/74 ảnh (`t8_matsumoto_court_dossier`) bị MiniMax để lại khung trắng ~45 px ⇒ **cắt bằng code** (không tốn credit), ghi lại trong `provenance.json` (`hau_xu_ly`). Đo lại: **0/74 ảnh còn viền trắng/đen**.

---

## 5.2. Rà H3 — 3 shot có nền KHÔNG khớp lời (đã sửa)

Rà toàn bộ 74 nền (soi mắt bằng contact sheet riêng + đối chiếu mã câu trong bảng shot) ⇒ phát hiện **3 dòng bảng shot dùng nền không khớp câu thoại**, trong khi ảnh đúng cảnh đã có sẵn trong bộ nền (một ảnh bị bỏ trống hoàn toàn):

| Shot | Câu | Nền cũ (lệch) | Nền mới (khớp) |
|---|---|---|---|
| `1-10` | 1.04#2 *"Họ dùng đầu ô đã mài nhọn đâm thủng các túi ni-lông…"* | `t8_chemical_structure_sarin` | **`t8_umbrella_puncture_action`** |
| `1-25` | 1.09#3 *"…chuyển đổi toàn bộ sảnh lớn thành trạm cấp cứu dã chiến"* | `t8_subway_exit_sunlight` | **`t8_hospital_triage_corridor`** |
| `2-25` | 2.07#2 *"…khởi đầu từ một phòng tập yoga nhỏ và những màn biểu diễn bay bổng"* | `t8_sarin_synthesis_laboratory` | **`t8_yoga_meditation_incense`** |

Đã vá **đồng bộ cả 3 hồ sơ** (VN/EN/JA) → `parse_shots.py` (223 shot, không thiếu nền) → render lại 669 ảnh tĩnh → QC lại toàn bộ.
Sao lưu: `.work/_cu/t08_20261109/KeHoach_Video_Tap08*.md.truoc_fix_bg_match`.

**Ảnh nền không còn dùng:** `t8_subway_exit_sunlight` (giữ lại làm tài sản dự phòng — không mất credit đã sinh). 73/74 nền đang được dùng.

---

## 5.3. Mô tả video (`mo_ta.txt`) — mốc chương đã sửa

`mo_ta.txt` (VN/EN/JA) viết ngày 05/11 cho bản kịch bản cũ ⇒ **5 mốc chương trỏ sai nội dung**. Đã sửa theo timeline 218 câu thật (`shots_t08*.json`):

| | VN | EN | JA |
|---|---|---|---|
| Hồi 1 | 00:22 | 00:22 | 00:22 |
| Hồi 2 | 06:08 | 06:07 | 06:39 |
| Hồi 3 | 12:05 | 11:51 | 13:03 |
| Hồi 4 | 19:15 | 18:49 | 20:47 |
| Hồi 5 | 26:33 | 25:52 | 28:27 |
| **Tổng** | **32:37** | **31:35** | **34:55** |

Nội dung mô tả + 19 nguồn **không đổi** (kịch bản không đổi). Script: `.work/_t08/_t08_fix_chapters.py` (idempotent).

**Hai hồ sơ ảnh nền cũng được dựng lại** từ dữ liệu thật: `Danh_Sach_Anh_Tap08.md` (bảng ảnh → hồi → mốc câu, công cụ, quang học) và `REVIEW_Bo_Anh_Tap08.md` (số đo mới: mean TB **61,0** (30,9–138,5) · std TB **50,7** (max 82,9) · **std > 25: 74/74** — bộ procedural cũ chỉ 11/74).

---

## 6. Timeline — neo master mp3 thật (T20)

`_t08_build_timeline.py` tái tạo **đúng bố cục `build_audio3.py`** (FIRST_VOICE 23,0 · GAP_SENT 0,35 · GAP_Q 0,60 · GAP_SPEAKER 0,70 · GAP_ACT 2,0 · NGHI ≤ 2,5 · `_pause_after` từ `acting_tap08*.json` · +0,2 s cho EN sad/fearful · outro 9,0 s), ước lượng thời lượng lời theo ký tự rồi **hiệu chỉnh tổng cho khớp master 0,000 s**:

| | VN | EN | JA |
|---|---|---|---|
| Master mp3 | 1957,51 s | 1895,91 s | 2095,36 s |
| Timeline | 1957,51 s | 1895,91 s | 2095,36 s |
| **Lệch tổng** | **0,000 s** | **0,000 s** | **0,000 s** |
| Tỉ lệ đọc | 16,06 ký tự/s | 17,68 ký tự/s | 5,93 ký tự/s |
| Câu ngắn nhất / dài nhất | 3,55 s / 13,32 s | 3,68 s / 12,05 s | 3,88 s / 14,68 s |

**Cảnh báo (L3 — nói rõ giới hạn):** trường `_estimated` trong 3 file timeline ghi rõ thời lượng **từng câu là ước lượng theo ký tự**; chỉ **tổng** được neo vào master.

**Đo kiểm chứng bằng ASR (Whisper `small`, toàn bộ master):** xem §6.1 — timeline ước lượng lệch **trung vị 1,7 s, TB |lệch| 7,1 s (VN) / 3,9 s (EN)** so với lời đọc thật, và lệch **tích luỹ dần** theo thời gian (âm ở đầu, dương ở giữa) ⇒ **khi ghép video phải dùng timeline đo bằng ASR** (`.work/timeline_asr_{lang}_t08.json`), không dùng timeline ước lượng.

### 6.1. Timeline đo thật bằng ASR (Whisper `small`)

Kỹ thuật (`_t08_asr_full.py` + `_t08_align_asr.py`): cắt master thành chunk 180 s (overlap 4 s) → Whisper với word timestamps → ghép transcript → **căn chỉnh tuần tự 218 câu** bằng *voting 9 mẫu k-gram (k=7)* trên chuỗi đã bỏ dấu thanh điệu (Whisper hay nghe sai thanh điệu tiếng Việt: "vào" → "giaosáng") → điểm đánh giá = tỉ lệ khớp chuỗi thật (difflib).

| | VN | EN | JA |
|---|---|---|---|
| Câu khớp ≥ 50% | **217/218** | **218/218** | **212/218** |
| Điểm khớp trung bình | 0,748 | 0,930 | 0,662 |
| Lệch mốc — trung vị \|lệch\| | 6,16 s | — | 6,42 s |
| Lệch mốc — TB \|lệch\| | **7,05 s** | **3,91 s** | **7,33 s** |
| Lệch mốc — max | 18,96 s | 10,43 s | 17,93 s |
| Lệch trong ±1 s | 11/218 | — | — |
| Lệch trong ±3 s | 43/218 | — | — |

**Kết luận quan trọng:** tổng thời lượng khớp master 0,000 s **không bảo đảm** mốc từng câu khớp — sai số tích luỹ tới ±19 s giữa tập. Ảnh tĩnh không bị ảnh hưởng (chữ = nguyên văn câu của shot, ảnh không gắn mốc thời gian), nhưng **video ghép sau này sẽ lệch chữ** nếu dùng timeline ước lượng.

**Sản phẩm:** `.work/timeline_asr_vi_t08.json` · `.work/timeline_asr_EN_t08.json` · `.work/timeline_asr_JA_t08.json` (mỗi file 218 câu, kèm `tl_start`/`tl_end`/`asr_start`/`asr_end`/`match`/`offset`). Checkpoint Whisper: `.work/_t08/asr_full_{vi,en,ja}.jsonl`.

---

## 7. Sai sót H10 ở bản Nhật — 1 shot

`5-27` (câu `5.06#3`) dài **15,3 s** — vượt H10 (≤ 15 s) **0,3 s**.
Nguyên nhân đo được: lời đọc Nhật của câu này thật sự dài, và timeline neo master nên không rút được.
Cổng QC dự án ghi nhận là **GHI** (không phải lỗi nội dung): tiêu đề hiện ở đầu câu (đúng V2) nên nhịp vẫn đúng; beat trong kế hoạch chưa được renderer T1 dùng.
Cách xử lý nếu muốn sạch tuyệt đối: gom câu (vi phạm quy tắc "1 câu = 1 shot") hoặc rút `OUTRO` (lệch T20 3,00 s) — **chưa làm, ghi nhận để người dùng quyết**.

---

## 8. H12 — thẻ kết `5-41`

Đo bằng `_t08_measure_endcard.py`:

| | VN | EN | JA |
|---|---|---|---|
| Pixel sáng tối đa | 172 | 172 | 178 |
| Trung bình | 46,4 | 46,7 | 44,0 |
| % pixel > 100 | 22,75% | 22,94% | 20,48% |

Soi mắt: thẻ hồ sơ giấy **"HỒ SƠ TẬP 08 · ĐÃ ĐÓNG"** (JA: **"事件ファイル 第08話・終結"**) + **AMBER EYES** + khẩu hiệu + clip đồ sáng — đọc rõ ở cả 3 ngôn ngữ.

**Lưu ý:** shot cuối dài 10,2 s ⇒ `build_video3.py` mờ shot cuối sang đen từ `start + 4,0 s` trong 3,0 s ⇒ ảnh tĩnh chụp ở giữa shot bị phủ ~30% đen. Vẫn đọc rõ (đã đo ở trên). Nếu muốn sáng hơn thì đổi `OUTRO 9,0 → 6,0` (tiền lệ Tập 07) — **chưa làm vì lệch T20 3,00 s**.

---

## 9. Việc còn lại / cần người dùng quyết

| # | Nội dung | Trạng thái |
|---|---|---|
| 1 | **7 câu chứa từ cấm A9.2** (VN 6 / EN 1 / JA 0) | ✅ **ĐÃ XỬ LÝ** — lược từ cấm trên hình bằng "…", không đụng kịch bản / audio / timeline (§4) |
| 2 | **74 ảnh nền `t8_*` là texture trừu tượng vẽ bằng CODE** (vi phạm H3) | ✅ **ĐÃ XỬ LÝ** — đã sinh lại **74/74 bằng MiniMax** (`connector__matrix__generate_image`, đúng công cụ Tập 02–07), 2112×1188, 0 lỗi; riêng 2 nền có chữ AI đọc được đã sinh lại với negative mạnh hơn. Sao lưu nền cũ: `.work/_cu/t08_bg_20261109/` (§5.1) |
| 3 | Shot JA `5-27` 15,3 s (vượt H10 0,3 s) | Ghi nhận (§7) |
| 4 | Mốc thời gian từng câu trong timeline là ước lượng — **đã dựng thêm timeline đo thật bằng ASR** (`.work/timeline_asr_{vi,en,ja}_t08.json`), lệch TB |lệch| 7,05 s (VN) / 3,91 s (EN) / 7,33 s (JA) | Xong (§6.1) — **dùng file ASR khi ghép video** |
| 5 | `02_SAN_XUAT/Tap08/nguon_tham_khao.md` và `mo_ta.txt` viết cho bản kịch bản cũ (147 câu) | ✅ **ĐÃ XỬ LÝ** — mốc chương trong 3 file `mo_ta.txt` (VN/EN/JA) đã sửa theo timeline 218 câu thật; 19 nguồn không đổi (§5.3) |
| 6 | Tooling T8 nằm ở `.work/_t08/` mà `.gitignore` loại `.work/*` ⇒ **0 file trong `.work/_t08` được git track** | Muốn commit code phải thêm `!.work/_t08/*.py` |
| 7 | **Chưa commit gì** (repo có sẵn file đổi từ phiên khác) | Theo L10 (cấm commit media/artifact QC) và người dùng chưa yêu cầu |
| 8 | **Một lần render nhầm Tập 01** (thiếu `AE_EP=08`) đã ghi 7 ảnh vào `.work/video3/stills/` | Đã xử lý: hash MD5 `1-01` = `89D124DE…` và `3-17` = `1D0DE279…` **khớp đúng** giá trị đã ghi nhận trong báo cáo Tập 07 ⇒ nội dung không đổi; 6 ảnh dư đã xoá (Recycle Bin). Đã render lại Tập 08 đúng `AE_EP=08` và **hash 669 ảnh (223 × 3) y hệt 100%** ⇒ xác nhận renderer tất định (H15) |

---

## 10. Sao lưu (L5)

| Bản cũ | Đường dẫn |
|---|---|
| Timeline + bảng shot cũ (171 câu) + 3 hồ sơ + `edition.py` (trước khi vá Tập 08) | `.work/_cu/t08_20261109/` |
| 3 hồ sơ (trước khi cập nhật metadata 171→218 câu) | `.work/_cu/t08_20261109/*.truoc_meta` |
| Bản 171 câu (kịch bản + bảng shot + tooling) | `.work/_cu/t08_171cau_20261107/` |
| Bản 218 câu trước khi dựng master | `.work/_cu/t08_218_20261107/` |
| `provenance.json` (trước khi thêm dòng Tập 08) | `.work/_cu/t08_20261109/provenance.json.truoc_t08` |
| `edition.py` (trước khi bật `text_scrim` 42 shot) | `.work/_cu/t08_20261109/edition.py.truoc_scrim_minimax` |
| `provenance.json` (trước khi gỡ dòng ảnh thử) | `.work/_cu/t08_20261109/provenance.json.truoc_xoa_test` |
| **74 ảnh nền procedural cũ** (trước khi sinh lại bằng MiniMax) | `.work/_cu/t08_bg_20261109/` |

---

## 11. Truy vết tài sản (L7)

`provenance.json`: **2271 mục** (trước: 2231) — thêm **40 dòng** cho lượt 09/11/2026: 3 hồ sơ · 3 bảng shot máy · 3 timeline · 3 thư mục ảnh tĩnh · 3 contact sheet · 3 timeline đo ASR · 3 `mo_ta.txt` · 2 hồ sơ ảnh nền · 7 contact sheet nền · 10 script tooling · cập nhật dòng `edition.py` (thêm thay đổi Tập 08).
**Cập nhật 74 dòng ảnh nền `t8_*`**: công cụ đổi từ *"Amber Eyes Noir Graphic Renderer (Pillow & Numpy Procedural Chiaroscuro Pipeline)"* ⇒ **`connector__matrix__generate_image` (MiniMax qua mcode-tools)**, ngày 2026-11-09, kèm prompt đầy đủ (STYLE + prompt cảnh + NEG); 2 ảnh sinh lại lần 2 có NEG mạnh hơn (ghi trong prompt ⇒ truy vết đúng); 1 ảnh ghi thêm `hau_xu_ly` (cắt viền trắng). Dòng ảnh thử `t8TEST_preview.png` đã **gỡ** (file cũng đã xoá) ⇒ không còn dòng cho tài sản không tồn tại.

File giữ nguyên định dạng: **CRLF**, **`indent=1`** (đúng chuẩn dự án — mục 30 bảng lỗi), **không BOM**, JSON hợp lệ (đã kiểm parse sau khi ghi).

---

## 12. Công cụ dùng lượt này (`.work/_t08/`)

`_t08_check_scripts.py` · `_t08_dump_script.py` · `_t08_dump_table.py` · `_t08_scan_special.py` · `_t08_build_timeline.py` · `_t08_gen_table.py` · `_t08_build_table.py` · `_t08_patch_edition.py` · `_t08_intro_hold_need.py` · `_t08_render_all.ps1` · `_t08_scan_contrast.py` (H9) · `_t08_qc_all.py` (H10) · `_t08_update_text_scrim.py` (hợp, không xoá) · `_t08_contact_sheet.py` · `_t08_bg_sheet.py` (contact sheet 74 nền) · `_t08_measure_endcard.py` (H12) · `_t08_update_plan_meta.py` (metadata hồ sơ) · `_t08_verify_sec6_unchanged.py` · `_t08_asr_check.py` · `_t08_asr_check2.py` · `_t08_asr_full.py` (Whisper toàn bộ master) · `_t08_align_asr.py` (căn chỉnh 218 câu) · `_t08_patch_kichban.py` (dry-run) · `_t08_add_provenance.py` · `_t08_add_prov_asr.py` · `_t08_update_prov_edition.py` · **`_t08_gen_bg_minimax.py`** (sinh 74 nền MiniMax, checkpoint + splice provenance) · **`_t08_prov_bump.py`** (bù provenance cho ảnh đã sinh) · **`_t08_remove_test_prov.py`** (gỡ dòng ảnh thử) · **`_t08_bg_stats.py`** (đo quang học + viền 74 nền) · **`_t08_fix_white_border.py`** (cắt viền trắng MiniMax) · **`_t08_fix_chapters.py`** (sửa mốc chương mo_ta.txt ×3) · **`_t08_fix_bg_match.py`** (vá 3 dòng bảng shot lệch cảnh) · **`_t08_regen_danh_sach.py`** · **`_t08_regen_review.py`** · **`_t08_prov_final.py`**.

---

## 13. Bài học rút ra từ lượt này (L6)

1. **Tổng thời lượng khớp master 0,000 s KHÔNG bảo đảm mốc từng câu khớp.** Timeline ước lượng theo ký tự lệch **tích luỹ dần** tới ±19 s giữa tập (đo bằng ASR). Khi ghép video phải dùng timeline đo thật.
2. **Whisper nghe sai thanh điệu tiếng Việt** ("vào" → "giaosáng") ⇒ khi căn chỉnh transcript phải **bỏ dấu thanh điệu** cả hai vế (Unicode NFD + bỏ combining marks).
3. **Manifest có 2 trường**: `text` (số viết bằng chữ — "hai mươi tháng ba") và `display` (số dạng chữ số — "20 tháng 3"). Whisper nghe số dạng chữ số ⇒ **phải căn chỉnh bằng `display`**, dùng `text` sẽ không khớp câu nào.
4. **Voting nhiều mẫu k-gram** (9 mẫu rải đều, k=7) chịu được lỗi nghe cục bộ của Whisper: 1–2 ký tự sai chỉ làm mất 1–2 mẫu, các mẫu còn lại vẫn chỉ đúng ứng viên. Một mẫu đơn lẻ thì không.
5. **Điểm đánh giá phải là tỉ lệ khớp chuỗi thật (difflib)**, không phải tỉ lệ phiếu — tỉ lệ phiếu đánh giá sai vị trí.
6. **`pyav` bản cũ lỗi `metadata_errors`** khiến `faster-whisper` không đọc được file ⇒ đọc wav thủ công bằng `wave` + numpy rồi truyền mảng float32 vào `transcribe()`.
7. **Render nhầm tập khác vì thiếu `AE_EP`** — luôn kiểm `AE_EP`/`AE_LANG` trước khi gọi `build_video3.py`. Đã kiểm chứng không thiệt hại bằng MD5.
8. **Nền AI sáng ⇒ H9 không còn "miễn nhiễm"**: 42/223 shot có chữ chìm khi đổi nền sang ảnh thật. Phải **đo lại H9 sau khi đổi nền**, không dùng kết quả đo của nền cũ.
9. **Script đo H9 phải dựng nền theo đúng thứ tự renderer** — nếu không, tấm giấy đục của thẻ kết bị tính nhầm là "nét chữ" ⇒ báo lỗi giả 19,7% (đã vá: element > 50% pixel đục ⇒ coi là nền).
10. **Lần đo sau khi bật scrim sẽ cho danh sách RỖNG** ⇒ script cập nhật `text_scrim` phải **HỢP** với danh sách đang có, không được thay thế (đã vá `_t08_update_text_scrim.py`).
11. **AI vẽ chữ đọc được trong ảnh nền** (sách "UNIVERSITY REGISTRY", màn hình hiện số) — negative "no text" **không đủ**; phải mô tả rõ "mọi bề mặt trắng trơn, số lẫn chữ đều không có" rồi **soi lại bằng mắt**.
12. **`provenance.json` dùng `indent=1`, không phải `indent=2`** (đúng chuẩn dự án, mục 30 bảng lỗi) — và nên ghi bằng **splice văn bản** để không đổi định dạng cả file.
13. **Runner sinh ảnh phải có checkpoint** — nếu không, một lần crash là mất credit cho cả lô; và logic "đã sinh" phải dựa trên **checkpoint**, không dựa trên "file đã tồn tại" (nền cũ cũng tồn tại).
14. **Trên Windows, xoá file bằng `rm "<đường dẫn>"`** (runtime chuyển sang Recycle Bin); dạng `rm -- "<path>"` bị policy chặn.
15. **Viền trắng do MiniMax để lại phải kiểm bằng TỶ LỆ pixel trắng trên khung viền**, không phải "có pixel sáng hay không" — nhiều ảnh tối có vùng sáng chạm mép (nội dung) nhưng không phải khung. Ở đây 1/74 ảnh có khung thật (~45 px, 99,8% khung viền là trắng) ⇒ cắt bằng code, không tốn credit.
16. **Rà H3 bằng cách đối chiếu "ảnh nào KHÔNG dùng ở đâu"** — ảnh bị bỏ trống là dấu hiệu bảng shot còn dùng nhầm nền (3 lỗi H3 ở Tập 08, tất cả đều có ảnh đúng sẵn trong bộ nền).
17. **Mốc chương trong `mo_ta.txt` phải lấy từ bảng shot**, không viết tay — bản cũ dùng mốc của script 147 câu ⇒ trỏ sai nội dung trên YouTube.

