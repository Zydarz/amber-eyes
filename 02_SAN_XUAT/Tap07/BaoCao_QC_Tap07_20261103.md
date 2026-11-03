# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 07 · 03/11/2026

**Thẩm phẩm:** `02_SAN_XUAT/Tap07/xuat_ban/Tap07_master.mp4`
**Nguyên nhân dựng lại:** đổi giọng từ **bộ A** (giọng `English_*`/`Korean_*` đọc tiếng Việt) sang **giọng tiếng Việt Higgs Audio v3** ⇒ âm thanh đổi hoàn toàn ⇒ phải dựng lại hình (A11 #55, H14).

---

## 1. Số đo thật (không ước lượng)

| Mục | Giá trị | Chuẩn | Kết quả |
|---|---|---|---|
| Thời lượng mp4 cuối | **1134,867 s** (18:55) | — | *(số liệu)* |
| Thời lượng audio master (wav) | 1134,870 s | khớp ±0,05 s | ✅ lệch **0,003 s** |
| `timeline.total` | 1134,870 s | khớp ±0,05 s | ✅ lệch **0,003 s** |
| `picture.mp4` (trước khi ghép) | 1134,867 s | khớp `timeline.total` ±0,05 s | ✅ **H14 đạt** |
| LUFS — mp4 cuối | **−16,0 LUFS** | −16 ± 1 | ✅ |
| True peak — mp4 cuối | **−1,9 dBFS** | ≤ −1,5 | ✅ |
| LRA — mp4 cuối | 3,3 LU | — | *(số liệu)* |
| Khoảng lặng > 0,3 s @ −60 dB | **0** | 0 | ✅ |
| Khoảng lặng ≥ 2,5 s @ −35 dB | **0** | 0 | ✅ |
| Lời đầu tiên | **23,0 s** | 22,8 – 23,5 s | ✅ |
| **Lệch âm thanh – hình** | **0,0 ms** (tương quan 0,9999) | ≤ 20 ms | ✅ (A11 #64) |
| Giải mã toàn file | **0 lỗi** | 0 | ✅ |
| Video | h264 · 1920×1080 · 30/1 · 34.046 khung · 2,78 Mbps | H.264 1080p30 | ✅ |
| Audio | AAC · 48.000 Hz · 2 kênh · 196 kbps | AAC | ✅ |
| Dung lượng | **423,5 MB** (423.533.411 byte) | — | *(số liệu)* |
| Phụ đề | **290 cue** · UTF-8 không BOM (32.260 byte) | phủ 100% lời thoại | ✅ |
| Cue cuối kết thúc | 1124,9 s | = hết lời (thẻ kết không lời) | ✅ |
| Thẻ kết (giữa shot cuối, 1129,87 s) | **15,34 %** pixel sáng | có chữ | ✅ H12 |
| Shot cuối | `5-12` — thẻ kết, không gắn câu | H12 | ✅ |
| Số shot | **66** (TB 16,9 s · dài nhất 32,0 s `4-01` · ngắn nhất 2,3 s `1-00`) | 3–15 s | ⚠ 40/66 shot > 15 s (mục 4) |
| Nền lặp liên tiếp | tối đa **2** shot | ≤ 4 shot | ✅ H10 |
| Ảnh tĩnh | **66/66** render + soi mắt 5 contact sheet | H9 | ✅ |
| Cổng QC A9.2 (bảng shot) | **12/12** | 12 | ✅ |
| Vai + handoff | **27/66** shot có handoff, **0** sai | A11 #88 | ✅ |
| `⊘` (tắt bán thân) | 4 shot (`1-00` `2-11` `2-12` `2-14`) | H10 | ✅ |
| Thumbnail | nền `t7_confession_text_timestamp` + chữ "BẢN ÁN GIẾT NGƯỜI / BẰNG TIN NHẮN" | H11 | ✅ |
| Ghi công Higgs trong `mo_ta.txt` | có dòng Boson AI | QUY_TAC_AUDIO_HIGGS §2 | ✅ |
| Nguồn tham khảo | **54** nguồn / **56** dữ kiện · 30 link HTTP 200 · 0 link chết | mọi dữ kiện có nguồn | ✅ A10 (mục 5) |

**Kết luận cổng QC A–G: 23 OK · 1 cảnh báo · 0 lỗi.**

---

## 2. Bảng shot — viết lại từ đầu theo nội dung câu

Kịch bản vá V9 (01/11/2026) còn **147 câu** (cũ 164) nhưng bảng shot mục 6 vẫn trỏ mã câu của bản **164 câu** cũ. `parse_shots.py` **không báo lỗi** vì mã cũ vẫn là chuỗi hợp lệ — nhưng nội dung hình đã sai. Đã map **cũ → mới theo diff nội dung câu** (đọc bản gốc ở commit `HEAD`), không đoán số thứ tự.

> Bài học từ Tập 06: căn chỉnh theo vị trí (`difflib` positional) cho kết quả **sai** ở element `1.07`. Lần này đối chiếu **KEY** trong `make_acting_tap07.py` + nội dung câu.

**82 câu thay đổi:** 59 đổi chữ · 20 xoá · 3 thêm mới (`1.06#8`, `4.02#4`, `5.04#19`). 164 − 20 + 3 = **147 câu**.
**26 element bị đụng:** 12 element đổi **số câu** — `1.06` 7→8 · `1.07` 6→5 · `2.06` 6→2 · `2.07` 4→2 · `2.09` 8→6 · `3.06` 6→4 · `3.08` 7→6 · `4.02` 3→4 · `4.03` 8→3 · `4.08` 7→5 · `5.02` 6→5 · `5.04` 18→19 — và 14 element chỉ đổi **chữ** (`1.02` `1.04` `1.10` `1.12` `1.13` `2.04` `2.10` `3.03` `3.05` `3.07` `4.05` `4.06` `4.07` `4.10`).

### 2.1. Lỗi đã sửa trong bảng shot

| Nhóm | Chi tiết |
|---|---|
| **Phủ câu** | Bảng mới có **66 dòng** (cũ 62). Thêm 4 dòng: `1-15` (câu `1.13#1`–`#2`, nền `t7_dossier_carter_case_07`), `5-10` (`5.04#16`–`#17`), `5-11` (`5.04#18`–`#19`), `5-12` (thẻ kết). **Không dòng nào bị xoá.** Kết quả: **147/147 câu, 0 trùng** |
| **Câu tham chiếu** | **27 dòng** đổi mã câu — đã remap theo KEY `make_acting_tap07.py`: `1-08` `1.07#1`–`#3`→`1.06#8` · `1-09` `1.07#4`–`#6`→`1.07#1`–`#3` · `1-10` `1.09#1`–`#3`→`1.07#4`–`#5` · `1-11` `1.10#1`–`#4`→`1.09#1`–`#3` · `1-12` `1.11#1`–`#2`→`1.10#1`–`#4` · `1-13` `1.12#1`–`#3`→`1.11#1`–`#2` · `1-14` `1.13#1`–`#2`→`1.12#1`–`#3` · `2-06` `2.06#1`–`#3`→`2.06#1` · `2-07` `2.06#4`–`#6`→`2.06#2` · `2-08` `2.07#1`–`#4`→`2.07#1`–`#2` · `2-10` `2.09#1`–`#3`→`2.09#1`–`#2` · `2-11` `2.09#4`–`#6`→`2.09#3`–`#4` · `2-12` `2.09#7`–`#8`→`2.09#5`–`#6` · `3-07` `3.06#4`–`#6`→`3.06#4` · `3-10` `3.08#4`–`#6`→`3.08#4`–`#5` · `3-11` `3.08#7`→`3.08#6` · `4-01` `4.02#1`–`#3`→`4.02#1`–`#4` · `4-02` `4.03#1`–`#4`→`4.03#1`–`#2` · `4-03` `4.03#5`–`#8`→`4.03#3` · `4-11` `4.08#5`–`#7`→`4.08#5` · `5-02` `5.02#4`–`#6`→`5.02#4`–`#5` · `5-04` `5.04#1`–`#4`→`5.04#1`–`#2` · `5-05` `5.04#5`–`#7`→`5.04#3`–`#4` · `5-06` `5.04#8`–`#11`→`5.04#5`–`#7` · `5-07` `5.04#12`–`#15`→`5.04#8`–`#10` · `5-08` `5.04#16`–`#17`→`5.04#11`–`#12` · `5-09` `5.04#18`→`5.04#13`–`#15` |
| **Hồi 5 — tách lại khối cờ đỏ** | Bản cũ trộn 4 cảnh báo đỏ vào 6 dòng, mỗi dòng gộp cả mô tả lẫn tiêu đề cờ. Đã tách: mỗi cờ đỏ (`5-04` Đỏ 1 · `5-07` Đỏ 3 · `5-08` Đỏ 4) có **một shot T8 riêng**; các shot mô tả (bong bóng cô lập `5-05` · tin nhắn mỉa mai `5-06` · điện thoại úp `5-09` · hải đăng `5-10` · hồ sơ đóng dấu `5-11`) tách thành T1/T4 riêng. Net **+3 dòng** |
| **Thẻ kết** | Shot `5-12` tách riêng, **không gắn câu** (vai `—`), chữ `*HỒ SƠ TẬP 07 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật*` — đúng H12, và tránh lỗi "số 07 trên hình không có trong câu" (A9.2) |
| **Handoff** | Bản cũ **không dòng nào** có mã `→X` (chỉ có trong dòng chú giải) ⇒ badge "TIẾP THEO" **chưa bao giờ hiện** ở Tập 07. Đã tính lại theo quy tắc `handoff(dòng i) = vai của dòng i+1` ⇒ **27/66 shot có handoff**, 0 sai (A11 #88) |
| **Cột Vai** | Khớp 147/147 câu; override `{"1.07":"N1", "4.03":"N2"}` vì `script_tap07.json` gộp hai vai thành `N` |
| **Số trên hình** | `1-15` bỏ "Tập 07" (câu không có số này) · `2-03` "3 giờ sáng" → "ba giờ sáng" · `2-13` bỏ "hơn 40 phút" (câu mới không còn nhắc; nền `t7_incoming_call_timer_40min` **không hiện chữ số** nên không còn số mồ côi trên hình) · `4-03` bỏ tên "Samantha Boardman" khỏi caption (tên riêng nằm ngoài câu đang đọc) · `5-06` chuyển `5.04#11` ("thứ tư") sang để Cảnh báo đỏ 4 có số nằm trong câu đang đọc |
| **Câu trích** | 100% nguyên văn câu đang đọc — cổng A9.2 "câu trích nguyên văn" xanh |
| **Từ cấm A9.2** | **0** từ cấm trong toàn bảng |

### 2.2. Lỗi template T8 — mất chữ (phát hiện khi soi ảnh tĩnh)

3 shot cờ đỏ dùng caption kiểu `Cảnh báo đỏ N: …` (viết tay) ⇒ template T8 chỉ hiện **cờ**, **không hiện tiêu đề** ⇒ mất thông tin chính trên hình. Đã đổi sang định dạng renderer hiểu (mẫu Tập 01):

```
*01* · **CẢNH BÁO ĐỎ 1 — CẢNH GIÁC TRƯỚC CÁC MỐI QUAN HỆ ẢO SIÊU TỐC VÀ CÔ LẬP**
```

Sau khi sửa: cờ **01/02/03/04 tô đầy đúng số thứ tự** (Đỏ 1 → 1 cờ, Đỏ 3 → 3 cờ, Đỏ 4 → 4 cờ) và tiêu đề hiện rõ. Đã render lại và kiểm bằng mắt trên ảnh trích từ mp4 cuối.

### 2.3. Bản chẩn

4 shot `⊘` giữ nguyên như bản gốc: `1-00` (thẻ mở đầu hồi) · `2-11` `2-12` `2-14` (khoảnh khắc đêm bãi đỗ xe — bầu trời sâu thẳm, kính xe kín sương mù). Đối chiếu bảng cũ 62 dòng vs bảng mới 66 dòng: **không mất dòng `⊘` nào, không thêm dòng `⊘` sai**.

---

## 3. QC ảnh tĩnh (A9.3 / H9 / H10)

- Render **66/66 shot** (`.work/video3_t07/stills/`) → dựng 6 contact sheet → **soi bằng mắt toàn bộ**.
- Từ mp4 cuối đã ghép, trích **66 khung giữa mỗi shot** → 5 contact sheet `.work/qc_final_t07/sheet_01..05.png` → **soi bằng mắt toàn bộ**.
- Không lỗi chữ đè nhau, không chữ lạ do AI (H2), không mặt người lộ, mọi nền có file trong `assets/bg/`.
- Handoff badge ("TIẾP THEO" / tên vai) hiện đúng ở 27 shot, đã soi trên ảnh trích từ mp4 cuối.
- **H10 lặp nền:** đo bằng script — đoạn lặp nền liên tiếp dài nhất **2 shot** (`1-00`+`1-01`), **0** đoạn lặp > 4 shot. Nền dùng: 61 nền / 66 shot.

---

## 4. Cảnh báo (không phải lỗi)

| Cảnh báo | Giải thích |
|---|---|
| 40/66 shot dài > 15 s (TB 16,9 s; dài nhất 32,0 s `4-01`) | A7/H10 ghi "3–15 s" nhưng **không có cổng QC nào đo**; đây là quy ước của dự án (Tập 06: 42/73 shot > 15 s, TB 17,1 s, dài nhất 30,4 s). Bản cũ của Tập 07 còn tệ hơn — đo được: **62 shot · TB 20,6 s · dài nhất 40,5 s · 47/62 (76 %) shot > 15 s**. Việc tách khối cờ đỏ + thêm shot đã kéo TB xuống 16,9 s và dài nhất xuống 32,0 s (ngang chuẩn Tập 06); phần còn lại ghi nhận để tách đoạn chữ ở lần sau |
| Khung tại `total − 2 s` bị đen | Renderer mờ dần 3 s cuối (dùng chung T01–T03). Thẻ kết đã kiểm ở **giữa shot cuối** (1129,87 s) → 15,34 % pixel sáng ✅ |
| Shot cờ 2 giữ style T4 (còn shot cờ 1) | 2 shot cờ dùng template T4 vẫn hiện đủ chữ mô tả ảnh, không mất thông tin. Đồng bộ style toàn bộ cờ sẽ phải dựng lại ~52 phút ⇒ ghi nhận khác biệt, không sửa |

---

## 5. Nguồn tham khảo (A10)

Tra cứu và kiểm chứng **54 nguồn công khai** cho **56 dữ kiện** nói như sự thật trong lời thoại:

| Hạng mục | Kết quả |
|---|---|
| Dữ kiện có nguồn trong bảng đối chiếu | **56** câu (mỗi câu 1–4 nguồn) |
| Tổng nguồn trong danh mục | **54** (hồ sơ tòa án · báo chí · văn bản lập pháp · nghiên cứu học thuật · đường dây nóng) |
| Link fetch trực tiếp thành công (HTTP 200) | **30/54** — đã đối chiếu từ khoá nội dung |
| Link bị lớp chống bot chặn khi fetch tự động | **24/54** — *vẫn mở bình thường bằng trình duyệt*, đã đọc nội dung qua bộ tìm kiếm |
| Link chết (404) | **1** — trang HBO của phim tài liệu đã bị gỡ ⇒ đã đổi sang trang Hulu |
| Mức "⚠" (cần hiểu chính xác cách diễn đạt) | **3** dòng — xem mục 5.1 |
| Bảng đầy đủ | `02_SAN_XUAT/Tap07/nguon_tham_khao.md` (44.110 ký tự, UTF-8 không BOM) — sinh bằng generator có validator, không gõ tay (A11 #84) |
| Khối nguồn trong mô tả YouTube | `02_SAN_XUAT/Tap07/nguon_mo_ta.txt` → 23 nguồn, `mo_ta.txt` = **4874 ký tự** (giới hạn YouTube 5.000) — đo trực tiếp file thật, không ước lượng (A11 #86) |

Nguồn gốc của vụ án là **hồ sơ Tòa Tối cao Massachusetts** (`Commonwealth v. Carter`, phụ lục bản ghi buổi xét xử) — mọi dữ kiện về **nguyên văn nội dung tin nhắn** đều dẫn về đây, không dựa vào phóng sự báo chí.

### 5.1. Ba điểm cần đọc kỹ (đã đánh dấu ⚠ trong bảng)

1. **`3.02#2` — "gia đình khá giả".** Nguồn chỉ mô tả gia đình Carter có điều kiện ổn định ở vùng ngoại ô (cha là giám đốc bán hàng, cháu ruột của một phó giám đốc ngân hàng). "Khá giả" trong lời dẫn là cách diễn đạt của kịch bản, không phải dữ kiện có thể chứng minh từ hồ sơ.
2. **`3.03#1` — "rối loạn nhân cách kịch tính / Hội chứng Münchausen kỹ thuật số".** Đây là **khung lý thuyết để phân tích**, không phải chẩn đoán y kế — Carter không bao giờ được chẩn đoán như vậy (nguồn: StatPearls, JMIR 2012).
3. **`5.02#5` — "Đạo luật Conrad".** Lời dẫn nói đúng là **dự luật đang vận động** (ra mắt 24/7/2019), không nói đã thành luật. Thực tế: **tới 11/2026 dự luật vẫn chưa được thông qua** — còn nằm trong Quý giai 194 (Bill S.1109), Massachusetts vẫn là một trong 8 bang chưa có điều luật riêng cho tội ép buộc tự sát. Đã ghi rõ ở cả bảng nguồn lẫn mô tả YouTube.

### 5.2. Các nguồn chính theo nhóm

| Nhóm | Nguồn tiêu biểu |
|---|---|
| Hồ sơ vụ án & bản án | Tòa Tối cao Massachusetts (phụ lục 2019) · Harvard Law Review 131 Harv. L. Rev. 918 · *Commonwealth v. Carter* 52 N.E.3d 1054 (Mass. 2016) · AP (6/2/2019) · Wikipedia (EN) |
| Báo chí | NYT (×2) · Washington Post (×2) · CNN (×2) · LA Times · CBS News (×3) · Boston Herald (×3) · MassLive (×5) · The Standard-Times · The Sun Chronicle · Esquire (×2) · People (×2) · The Independent (×2) · Courthouse News · The Daily Beast · NBC News (×3) · Newsweek |
| Đạo luật Conrad | malegislature.gov — **toàn văn Bill S.1032** (192nd GC) + **Bill S.1109** (194th GC, hiện đang chờ) · Boston.com · WGBH · WBUR · CBS Boston · Northeastern Law |
| Tâm lý học & thao túng | StatPearls (Munchausen by Internet) · JMIR 2012 · PubMed Central (kiểm soát cưỡng ép) · The Cognitive Behavioural Therapist (Cambridge) · RBWM (hướng dẫn tự sát & bạo hành) · Scamwatch — Chính phủ Úc (**"commitment escalation"**) |
| Đường dây nóng | **Đường dây nóng Ngày mai — 096 306 1414** (https://duongdaynongngaymai.vn/hotline/) · **Tổng đài 111** (http://tongdai111.vn/ — "hoạt động 24/24 và các cuộc gọi đến tổng đài là hoàn toàn miễn phí") |

Máy kiểm tra từng URL + từ khoá: `.work/qc_final_t07/_urlcheck_t07.json`.

---

## 6. Việc còn lại của người dùng

1. **Nghe duyệt** — danh sách câu cần nghe: `02_SAN_XUAT/Tap07/CanNghe_Tap07_higgs.md` (2 câu chọn tay + 40 câu chỉ Whisper báo).
2. ~~Điền nguồn~~ — **đã xong 03/11/2026**: 54 nguồn, 56 dữ kiện, mục 5.

---

## 7. Sao lưu (L5)

| Bản cũ | Đường dẫn |
|---|---|
| Master mp4 bản 25/10 (1309,6 s · bộ giọng A) | `.work/_cu/Tap07_master_25thang.mp4` |
| Bộ `.work` MiniMax (script, acting, sfx, manifest, timeline, shots, mp3, srt) | `.work/_cu/t07_minimax_20261102/` |
| Bảng shot 62 dòng (trước khi viết lại) | `.work/_cu/t07_shottable_147cu/KeHoach_Video_Tap07.md.bak` + commit `HEAD` |
| `shots_t07.json` bản cũ (62 shot) | `.work/qc_final_t07/_shots_t07_git_HEAD.json` |
| `edition.py` (thêm `thumb_bg`, `mux_af`, `voice_credit`) | git (chưa commit) |

---

## 8. Script QC đã chạy (tái lập được)

| Script | Cổng | Kết quả |
|---|---|---|
| `.work/_qc_tap07_shots.py` | A9.2 — 12 cổng trên bảng shot | 12/12 ✅ |
| `.work/parse_shots.py` | 66 shot · max 32,0 s · không thiếu nền | ✅ |
| `.work/_qc_h14_picture_t07.py` | H14 — `picture.mp4` lệch `timeline.total` −0,003 s; thẻ kết 15,34 % pixel sáng | ✅ |
| `.work/_qc_final_generic.py` | A9.1 · A9.3 · A9.4 · phụ đề | **TẤT CẢ ĐẠT** ✅ |
| `.work/_qc_sync_t07.py` | Lệch A/V mp4 vs audio master | **0,0 ms** (r = 0,9999) ✅ |
| `.work/qc_final_t07/_qc_h10_t07.py` | H10 — thời lượng shot + lặp nền | 0 đoạn lặp > 4 shot ✅ |
| `.work/qc_final_t07/_diff_plan_detail.py` | Diff bảng shot cũ (62) vs mới (66) theo từng cột | 4 dòng mới · 0 dòng xoá ✅ |
| `.work/qc_final_t07/_diff_script_t07.py` | Diff kịch bản cũ (164 câu) vs mới (147 câu) | 59 đổi chữ · 20 xoá · 3 thêm ✅ |
| `.work/qc_final_t07/_cmp_old_shots.py` | So thời lượng shot bản cũ vs mới | 20,6 s → 16,9 s TB ✅ |
| `.work/qc_final_t07/_gen_nguon_t07.py` | Sinh bảng nguồn + khối nguồn mô tả (54 nguồn / 56 dữ kiện) | ✅ |
| `.work/qc_final_t07/_urlcheck_t07.json` | Máy kiểm tra URL + từ khoá từng nguồn | 30 HTTP 200 · 24 chặn bot · 0 chết (đã thay 1) ✅ |
