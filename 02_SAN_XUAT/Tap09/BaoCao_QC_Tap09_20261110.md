# BÁO CÁO QC — TẬP 09 · RENDER ẢNH TĨNH 3 NGÔN NGỮ (VN / EN / JA)

**Ngày:** 10/11/2026 · **Yêu cầu:** đọc lại kịch bản Tập 09 (bản viết lại) và **render lại ảnh tĩnh cho 3 ngôn ngữ** · **KHÔNG dựng video** (H18: ảnh tĩnh là CỔNG QC, không phải nguyên liệu dựng).

> Mọi số trong báo cáo này lấy từ **script đã chạy** (log lưu trong `.work/_t09/` và `.work/_t09/qc_final_t09/`), không suy đoán.

---

## 1. Phạm vi đã làm

| Hạng mục | Kết quả | Bằng chứng (đo bằng script) |
|---|---|---|
| Kịch bản | **199 câu** đọc · 54 element (35 element có lời) | `.work/script_tap09*.json` khớp `parse_kichban.py` chạy lại trên MD (`SAME=True`) |
| Nền | **65 ảnh** `assets/bg/t9_*.png` sinh lại bằng **MiniMax** (`connector__matrix__generate_image` qua mcode-tools) | `.work/_t09/gen_bg_run.log`, checkpoint `.work/_t09/gen_bg_minimax_t09.jsonl` (65/65) |
| Timeline | VN **đo thật** (1523,19 s) · EN/JA **ước lượng** (1424,63 s / 1931,91 s) | `.work/timeline_s_t09.json` + `timeline_s_EN_t09.json` + `timeline_s_JA_t09.json` |
| Bảng shot | **192 dòng**/ngôn ngữ = 187 shot nội dung + 4 thẻ hồi T10 + 1 thẻ kết T2 | `.work/shots_t09.json` · `shots_EN_t09.json` · `shots_JA_t09.json` |
| Ảnh tĩnh | **576 ảnh** (192 × 3 ngôn ngữ) | `.work/video3_t09/stills` · `video3_EN_t09/stills` · `video3_JA_t09/stills` |
| QC | **TẤT CẢ ĐẠT** | `.work/_t09/qc_final_t09/qc_t09.txt` |

---

## 2. Nền — vì sao phải sinh lại và đã xử lý gì

Nền cũ (23/10/2026) do *"Amber Eyes Noir Graphic Renderer (Pillow & Numpy Procedural Chiaroscuro Pipeline)"* vẽ ⇒ chỉ là gradient tối, **không có nội dung cảnh** ⇒ vi phạm **H19** (đọc tên nền phải ra một cảnh cụ thể). Đã sinh lại toàn bộ bằng MiniMax (đúng cách Tập 08 làm 09/11/2026).

**3 ảnh phải sinh lại lần 2** sau khi soi bằng mắt trên contact sheet (6 tờ, 12 ảnh/tờ):

| Ảnh | Lỗi phát hiện | Xử lý |
|---|---|---|
| `t9_kurt_lewin_three_stages_diagram` | AI **vẽ chữ** "Unfreezing \| Changing \| Refreezing" trên bảng đen ⇒ vi phạm **H5** | Bỏ tên giai đoạn khỏi prompt + `ABSOLUTELY NO WRITING` → sinh lại ⇒ còn **chỉ là sơ đồ hình học** |
| `t9_runaway_teenager_bus_stop` | AI khắc chữ **"LOST" / "FOUND"** trên ghế ⇒ vi phạm **H5** | Ghế gỗ trơn, không khắc → sinh lại |
| `t9_vinyl_record_white_album` | AI tạo **một mảng trắng lơ lửng** (bìa album trắng) ⇒ rác hình | Bỏ bìa, đĩa than đen trơn trên mặt đĩa → sinh lại |

**4 ảnh còn viền trắng** (MiniMax tự vẽ khung) ⇒ **cắt bằng code** (không tốn credit, giữ nguyên nội dung cảnh): `t9_cielo_drive_estate_night` (45/53 px), `t9_cielo_drive_living_room_somber` (11/14 px), `t9_death_valley_barker_ranch_raid` (46/46 px), `t9_spahn_ranch_dilapidated_porch` (31/20 px).

**1 ảnh cũ bị xoá** do đổi tên (A9.2 — bỏ chữ "bloody"): `t9_interlocking_bloody_knots_rope.png` → `t9_interlocking_knots_rope.png`; dòng provenance của file cũ cũng đã xoá (L7).

---

## 3. Bảng shot (mục 6 của 3 file kế hoạch)

* **VN**: `02_SAN_XUAT/Tap09/KeHoach_Video_Tap09.md` — **thêm mục 6** (bản cũ đã sao lưu).
* **EN**: `02_SAN_XUAT/Tap09_EN/KeHoach_Video_Tap09_EN.md` — **tạo mới** (trước đó chưa tồn tại).
* **JA**: `02_SAN_XUAT/Tap09_JA/KeHoach_Video_Tap09_JA.md` — **tạo mới** (trước đó chưa tồn tại).

Quy tắc áp dụng:

| Quy tắc | Cách làm |
|---|---|
| A7/V3/H6 — chữ trên hình | **Nguyên văn** câu kịch bản của shot; ≥ 40 ký tự ⇒ *nghiêng*, < 40 ký tự ⇒ **đậm** |
| H10 vế 1 (3–15 s) | Gom **12 câu** ngắn với câu kế trong cùng element (DP tối ưu, ≤ 2 câu/shot, ưu tiên ngôn ngữ đo thật) |
| A7 — shot > 15 s | Câu `2.10#2` (17,9 s VN) **tách chữ trên hình thành 2 đoạn nguyên văn + beat** `ở "<cụm từ>"` (ranh giới shot = ranh giới câu nên không tách được câu) |
| H10 vế 2 (nền lặp ≤ 4) | Xoay vòng 65 nền theo element ⇒ đoạn lặp dài nhất **3 shot** |
| T8 — cảnh báo đỏ | 4 câu `5.07#2/#4/#6/#8` ⇒ mẫu T8 (cờ) `*0N* · **CẢNH BÁO ĐỎ N: …**` |
| T4 — lời kể | Element `1.07` (N1) và `4.05` (N2) |
| A9.2 | Chỉ **lược trên lớp chữ hiển thị** bằng "…" (2 câu VN có "sát hại"); **không sửa kịch bản** ⇒ không lệch audio/timeline |

---

## 4. Kết quả QC đo được

`.work/_t09/_t09_qc_all.py` → `.work/_t09/qc_final_t09/qc_t09.txt`:

| Cổng | VN | EN | JA |
|---|---|---|---|
| Phủ câu | 199/199 | 199/199 | 199/199 |
| ID shot duy nhất | 192 | 192 | 192 |
| H10 vế 1: shot < 3 s | **0** | **0** | **0** |
| Thời lượng | TB 8,0 s · max 18,4 s · > 15 s: **2** | TB 7,5 s · max 15,9 s · > 15 s: **1** | TB 10,2 s · max 30,7 s · > 15 s: **18** |
| H10 vế 2: nền lặp liền | 3 shot | 3 shot | 3 shot |
| A9.2 từ cấm trong chữ | 0 | 0 | 0 |
| Ảnh tĩnh đủ 1 ảnh/shot | 192 ✅ | 192 ✅ | 192 ✅ |
| Ảnh mới hơn bảng shot | ✅ | ✅ | ✅ |
| T25 (số ô bảng markdown) | 192 dòng × 9 ô ✅ | ✅ | ✅ |

### H9 (chữ "chìm") — đo 2 vòng bằng script

| Vòng | VI | EN | JA | Hành động |
|---|---|---|---|---|
| 1 (chưa bật scrim) | 41 shot chìm > 8 % (tệ nhất 52,9 %) | 41 shot (39,0 %) | 42 shot (47,1 %) | **Hợp 52 shot** ⇒ bật `text_scrim` trong `EPISODES["09"]` |
| 2 (sau khi bật) | **0** (tệ nhất 5,0 %) | **0** (4,2 %) | **0** (8,0 %) | ✅ |

Nền MiniMax **sáng hơn nền procedural** của Tập 06/07 ⇒ phải đo lại toàn bộ, không tái dùng kết quả cũ.

### Soi bằng mắt

* 6 tờ contact sheet **nền** (65 ảnh) + 3 tờ **tổng hợp ảnh tĩnh** (192 ảnh/ngôn ngữ) + 3 tờ **zoom** nhóm đặc thù ⇒ `.work/_t09/contact_sheet/` và `.work/_t09/stills_sheet/`.
* Kiểm tra được: nền khớp nội dung câu (H19) ✔ · không còn chữ do AI vẽ ✔ · thẻ giới thiệu vai không đè chữ ✔ · thẻ hồi / thẻ cờ / thẻ kết đúng mẫu ✔ · chữ trên hình đọc được ✔.

---

## 5. Sửa cấu hình tập (chỉ trong `EPISODES["09"]`)

| Khoá | Giá trị | Vì sao |
|---|---|---|
| `intro_card_pos` | `[960, 90]` | Vị trí cũ (490, 250) của Tập 07/08 **che dòng chữ đầu tiên của mẫu T4 "lời kể"** ⇒ đặt sang góc trên phải (không đè T1 ở đáy, không đè T4 ở giữa-trái) |
| `intro_card_panel` | `True` | Nền tối cho thẻ vai (đọc được trên nền sáng) |
| `intro_card_hold` | `5.8` | Giữ thẻ đủ lâu cho ảnh tĩnh chụp giữa shot |
| `text_scrim` | 52 mã shot | H9 — xem bảng ở §4 |

> **Lưu ý (không phải hồi quy):** Tập 08 vẫn còn lỗi thẻ vai che chữ T4 (ảnh `video3_t08/stills/shot_1-17.png`). Chưa sửa vì `intro_card_pos` của Tập 08 là cấu hình riêng và việc sửa sẽ đụng vào tập đã dựng — đã ghi vào bảng bài học.

---

## 6. Hạn chế còn lại (đã đo, đã ghi nhận)

1. **Timeline EN/JA là ước lượng**, chưa có audio ⇒ **18 shot JA vượt 15 s** là hệ quả của tốc độ đọc tiếng Nhật (hệ số `K_ja = 2,6767` neo từ Tập 08, sai số kiểm chứng **0,000 %**). Khi có audio thật phải **dựng lại timeline rồi render lại ảnh** (T20/H14).
2. **`t9_vinyl_record_white_album`** nay là **đĩa than đen trơn** (không còn bìa trắng) — hình ảnh không còn ám chỉ "White Album" một cách chính xác, nhưng là hình học sạch, không chữ, không rác.
3. **Thẻ kết JA** hiển thị "第0 / 9話 · 終結" (xuống dòng giữa số) — **lỗi có sẵn ở Tập 08** (`video3_JA_t08/stills/shot_5-41.png`), do mẫu T2 wrap theo độ rộng thẻ; **không sửa** để không đụng tập đã dựng.
4. **Chưa có `Tap09_master.mp3`** ⇒ không thể dựng video (đúng yêu cầu: chỉ ảnh tĩnh).

---

## 7. Sao lưu (L5)

| Bản sao | Nội dung |
|---|---|
| `.work/_cu/t09_bg_20261110/` | 65 ảnh nền procedural cũ (trước khi sinh lại) |
| `.work/_cu/t09_bg_jobs_20261110.json` | bộ prompt gốc trước khi vá H5 (lần 1 và lần 2) |
| `.work/_cu/t09_plan_20261110/` | 3 file kế hoạch trước khi ghi mục 6 |
| `.work/_cu/t09_timeline_roles_20261110/` | 3 file timeline trước khi sửa vai N → N1/N2 |
| `.work/_cu/edition_t09_truoc_scrim_20261110.py` | `edition.py` trước khi bật `text_scrim` |
| `.work/_cu/provenance_truoc_dondep_t09_20261110.json` | `provenance.json` trước khi dọn |
| `.work/_cu/TIEU_CHUAN_DUNG_VIDEO_truoc_t09_20261110.md` | tài liệu chuẩn trước khi thêm mục #141–#144 |

---

## 8. Bài học đã ghi vào tài liệu (L6)

`00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` — thêm **#141–#144** (bằng script, số liên tục, không trùng):

* **#141** — Nền MiniMax vẫn vẽ chữ dù prompt đã cấm ⇒ **phải soi bằng mắt**, grep prompt không đủ.
* **#142** — `intro_card_pos` phải kiệm theo **mẫu** của shot đầu vai (T1/T4/T8/T2), không chỉ T1.
* **#143** — Timeline ước lượng phải ép vai `N` → `N1`/`N2` theo `edition.py` (nếu không `build_video3` crash `KeyError: 'N'`).
* **#144** — Gom câu H10 bằng DP: giới hạn ≤ 2 câu/shot, tính chi phí theo **mức độ** vi phạm, ưu tiên ngôn ngữ đo thật; shot > 15 s tách **chữ trên hình** + beat.

---

## 9. Bước tiếp theo (khi có audio thật)

1. Thu âm EN/JA (Higgs Audio v3) → `Tap09_EN_master.mp3` / `Tap09_JA_master.mp3`.
2. Dựng lại `timeline_s_EN_t09.json` / `timeline_s_JA_t09.json` **từ mp3 thật** (T20: tổng khớp master ≤ 0,05 s).
3. Chạy lại `_t09_gen_table.py` → `_t09_write_plans.py` → `parse_shots.py` → `build_video3.py --stills all` cho EN/JA.
4. Chạy lại `_t09_scan_contrast.py` (H9) + `_t09_qc_all.py`.
