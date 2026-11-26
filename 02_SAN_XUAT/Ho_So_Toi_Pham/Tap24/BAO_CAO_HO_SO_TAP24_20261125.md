# BÁO CÁO HỒ SƠ SẢN XUẤT TẬP 24 — "KÝ ỨC KẺ SÁT NHÂN HWASEONG"

**Ngày:** 25/11/2026 · **Người thực hiện:** AI (MCode) · **Tập:** 24 — Hồ sơ Lee Choon-jae (Hwaseong, Gyeonggi, Hàn Quốc) & kỳ án oan Yoon Sung-yeo
**Ngôn ngữ:** Tiếng Việt / Tiếng Anh / Tiếng Nhật (3 bản dùng chung 1 bảng shot · 1 bộ ảnh nền)

---

## 1. Quyết định của người dùng (chốt 25–26/11/2026)

| # | Quyết định | Hệ quả kỹ thuật |
|---|---|---|
| 1 | **Giữ nguyên 155 ảnh nền hiện có**, không sinh lại ảnh nào (kể cả nhóm A/B/C trong báo cáo QC) | Chấp nhận ngoại lệ H26 (81/155 ảnh có chữ AI/pseudo-text/lộ mặt) và ngoại lệ M4 của `qc_bg_mapping.py` (chỉ 22/155 prompt khác nhau) |
| 2 | **Chỉ thực hiện từ mục 2** trong danh sách 6 việc đã đề xuất | Không đụng tới bước 1 (duyệt lại kịch bản) và không sinh lại ảnh |
| 3 | **Chấp nhận lỗi tiêu đề đỏ ở intro JA** (8 ô vuông thiếu glyph) — lỗi có sẵn ở Tập 16/17/18 | Không sửa video; ghi nhận ngoại lệ trong hồ sơ. Nội dung intro tiếng Nhật hiển thị đúng |
| 4 | **Dựng lại cả 3 video, chạy tuần tự từng video** (26/11/2026) — bắt buộc có dải sóng giọng nói | Dùng `make_pseudo_stems.py` (chuẩn #186) → cổng H24 ĐẠT → dựng lại 6 lô/ngôn ngữ → đóng gói lại. **0 credit**, không đổi giọng, không sửa `build_video3.py`. Xem §9.2 |

---

## 2. Việc đã thực hiện (mục 2 → 6)

| Mục | Việc | Công cụ | Kết quả |
|---|---|---|---|
| 2 | Bảng shot EN + JA từ bảng VN (A8.1(c)) | `.work/_make_plan_t24_multilang.py` | `KeHoach_Video_Tap24_EN.md` (350 dòng) · `KeHoach_Video_Tap24_JA.md` (350 dòng) — chỉ đổi **cột Chữ + tên linh thú + thời lượng thật**, giữ nguyên mã shot / nền / mẫu T / camera |
| 3 | Dựng lại timeline 3 ngôn ngữ | `.work/_rebuild_t24.py` | `timeline_s_t24.json` (2203,30 s) · `timeline_s_EN_t24.json` (2137,38 s) · `timeline_s_JA_t24.json` (2444,66 s) |
| 4 | Bảng diễn xuất + âm thanh | `.work/_make_acting_sfx_t24.py` | `acting_tap24[_EN\|_JA].json` (246 câu) · `sfx_tap24[_EN\|_JA].json` (5 nền + 18 điểm) |
| 5 | Intro JA | copy `assets/brand/intro_kenh_JA_t18.mov` → `intro_kenh_JA_t24.mov` (md5 `edac63c63f0f`, trùng t16/t17/t18) | sửa `EPISODES["24"]["intro"]` trỏ đúng file — nếu không, 20,5 s đầu video JA sẽ là màn đen |
| 6 | REVIEW + báo cáo hồ sơ | `.work/_make_review_t24.py` | `REVIEW_Bo_Anh_Tap24.md` (viết lại, 467 dòng) + báo cáo này |

**Sửa thêm trong `EPISODES["24"]` (`.work/edition.py`)** — có bản sao lưu tại `.work/_cu/`:

- `thumb_bg` = `t24_a1_30_prison_cell_embroidery_desk_30` (bàn thêu hoa trong buồng giam Busan — dấu vật "ký ức" của hồ sơ, nền sạch chữ, tối).
- `thumb` rẽ nhánh theo ngôn ngữ (A11 #148): VI `KÝ ỨC · HWASEONG` · EN `MEMORIES · HWASEONG` · JA `記憶 · ファセオン`.
- `roles_en` / `roles_ja`: bản EN mặc định ghi *"Blanchard case file"* (tập khác) và bản JA mặc định không có nhãn riêng cho 2 vai nhân chứng ⇒ đã khai đủ 5 vai cho EN và JA.

---

## 3. Kiểm chứng timeline (H14)

| Ngôn ngữ | Thời lượng master audio | `timeline.total` | Sai lệch | Số cue SRT |
|---|---:|---:|---:|---:|
| VI | 2203,299979 s | 2203,30 s | **0,000 s** | 566 |
| EN | 2137,379979 s | 2137,38 s | **0,000 s** | 607 |
| JA | 2444,659979 s | 2444,66 s | **0,000 s** | 508 |

**Round-trip kiểm chứng** (`.work/_verify_t24.py`): chạy lại `subtitles.py` từ timeline mới rồi so với SRT gốc đã xuất bản → **nội dung cue 100 % giống**, sai lệch thời gian tối đa **3 / 4 / 2 ms** (ngưỡng 50 ms).

Sau khi chạy lại `subtitles.py` ở bước đóng gói, so với bản gốc (`.work/_cu/srt_t24_20261125/`): **nội dung khác 0 cue**, lệch tối đa 3 / 4 / 2 ms.

**Cổng `qc_pause_gate.py` — ĐẠT cả 3 ngôn ngữ:**

```
vi: 246 câu · trung vị nghỉ 0,95 s (≥ 0,6) · < 0,4 s: 0/241 = 0% (≤ 25%) · timeline.total = master ±0,00 → ĐẠT
en: 246 câu · trung vị nghỉ 0,95 s · < 0,4 s: 0/241 = 0% · ±0,00 → ĐẠT
ja: 246 câu · trung vị nghỉ 0,95 s · < 0,4 s: 0/241 = 0% · ±0,00 → ĐẠT
```

---

## 4. Bảng shot 3 ngôn ngữ

| Ngôn ngữ | File | Số shot | Số nền | Shot/nền |
|---|---|---:|---:|---:|
| VI | `KeHoach_Video_Tap24.md` (mục 6) | 246 | 155 | 1,6 |
| EN | `KeHoach_Video_Tap24_EN.md` | 246 | 155 | 1,6 |
| JA | `KeHoach_Video_Tap24_JA.md` | 246 | 155 | 1,6 |

- Mã câu `1.02#1` … `5.05#18` trùng khớp **100 %** giữa 3 ngôn ngữ ⇒ **1 bảng shot phục vụ cả 3 bản** (H25 · A8.1(c)), không cần ảnh riêng cho EN/JA.
- **Sửa 1 vi phạm H22 của bản VN**: `t24_a1_01` bị 2 shot / 31,6 s (> 30 s) ⇒ đổi shot `1-01` sang `t24_a1_23_rural_village_lane_fog_23` và đưa nền ruộng lúa về `1-02` (khớp ngữ nghĩa H3). Thay đổi này áp dụng chung cho cả 3 ngôn ngữ.

---

## 5. Bảng diễn xuất & âm thanh (mục 4)

| File | Nội dung | Cổng `--pre` |
|---|---|---|
| `acting_tap24.json` | 246 câu · `_pause_after` 135 mục (55 %) | **ĐẠT** (0 mã lạ · 0 ngoài 0,2–1,2 s) |
| `acting_tap24_EN.json` | 246 câu · `_pause_after` 146 mục (59 %) | **ĐẠT** |
| `acting_tap24_JA.json` | 246 câu · `_pause_after` 129 mục (52 %) | **ĐẠT** |
| `sfx_tap24[_EN\|_JA].json` | 5 nền môi trường + 18 điểm âm thanh | đọc bởi `build_audio3.py::place_sheet()` |

- Cảm xúc lấy từ **chú dẫn diễn xuất** của từng element trong kịch bản, chỉ dùng 4 cảm xúc an toàn (G3: neutral · sad · fearful · surprised); lệch tốc độ trong −0,06…+0,02 (G4); cao độ luôn 0 (G5).
- `_pause_after` **đo từ timeline thật của từng ngôn ngữ** (A13: mỗi ngôn ngữ một file riêng).

---

## 6. Ảnh nền & QC (H22 / H26)

| Kiểm tra | Kết quả |
|---|---|
| Số file `assets/bg/t24_*.png` | **155** · tất cả 2112×1188 · 0 file hỏng · 0 ảnh trùng nội dung |
| `provenance.json` | **155/155 dòng** `t24_*` (Cloudflare Workers AI FLUX) |
| `qc_bg_usage.py` (VI / EN / JA) | **ĐẠT** — 0 ảnh thừa · 0 shot mượn nền · 0 nền thiếu file · 0 nền vượt 3 shot / 30 s |
| Ảnh tĩnh | 246 shot × 3 ngôn ngữ = **738 ảnh tĩnh**, đủ mã, đúng 1920×1080 |
| QC nội dung ảnh (H2/H19/H26) | **81/155 ảnh (52 %) có chữ AI / pseudo-text / lộ mặt / sai bối cảnh** → **người dùng chốt giữ nguyên** |

Chi tiết 81 ảnh: [`BAO_CAO_QC_ANH_NEN_TAP24_H26_20261125.md`](BAO_CAO_QC_ANH_NEN_TAP24_H26_20261125.md).

---

## 7. Dựng hình & đóng gói

> **Bản dựng lại 26/11/2026 (có dải sóng giọng thật):** mỗi ngôn ngữ chia **6 lô** (`.work/_render_t24.py --part K --of 6`, rồi `--concat --of 6`), chạy **tuần tự từng video** theo yêu cầu người dùng.
>
> **Hiệu năng (đo thật trên máy này):** lần đầu dùng **8 worker ⇒ máy tràn RAM** (mỗi worker ~500 MB private + ffmpeg mở 30 thread; RAM trống rơi về 0,6 GB ⇒ phân trang đĩa) → tổng tốc độ chỉ **6,7 fps** và lệnh nền bị giết khi hết 3600 s. Đo mở rộng CPU cho thấy máy **vỡ ở ≥8 tiến trình** (39 M vòng lặp/s ở 6 tiến trình → 6,8 M ở 8). Chuyển sang **4–6 worker** ⇒ ổn định, ~7–11 fps tổng. Encode libopenh264 không phải nút thắt (124 fps đo riêng).
>
> Thời gian dựng lại: VN ~2 h 15 ph · EN ~2 h 05 ph · JA ~2 h 25 ph (6 lô/ngôn ngữ).

Dựng hình chia nhiều lô vì 1 lệnh dựng trọn vượt giới hạn 3600 s của tiến trình nền.

| Ngôn ngữ | `picture.mp4` | MP4 thành phẩm | Thời lượng mp4 (ffprobe) | Lệch vs `timeline.total` | Dung lượng |
|---|---:|---|---:|---:|---:|
| VI | 2203,300000 s | `Tap24/xuat_ban/Tap24_master.mp4` | 2203,299979 s | **−0,000 s** | 871,5 MB |
| EN | 2137,367000 s | `Tap24_EN/xuat_ban/Tap24_EN_master.mp4` | 2137,366667 s | **−0,013 s** | 845,2 MB |
| JA | 2444,633000 s | `Tap24_JA/xuat_ban/Tap24_JA_master.mp4` | 2444,633333 s | **−0,027 s** | 968,3 MB |

> Dung lượng tính theo quy ước của `.work/_verify_final_t24.py`: 1 MB = 1 000 000 byte (tương đương 831,12 / 806,09 / 923,47 MiB).

Cả 3 bản đều lệch ≤ 0,03 s so với `timeline.total` ⇒ **đạt H14** (ngưỡng dự án ± 0,05 s; lệch do làm tròn khung hình 30 fps, tối đa 1/30 s = 0,033 s).

Thông số chung: 1920×1080 · 30 fps · H.264 (libopenh264, 3000 k) + AAC 192 k 48 kHz stereo · `-alimiter=limit=0.7943` (A7) · `+faststart`.

**Thumbnail** (`.work/package.py thumbnail()`): 1280×720 RGB · nền `t24_a1_30_prison_cell_embroidery_desk_30` + logo kênh + Sói/Cáo · chữ Pillow (`segoeuib.ttf` 86 px VI/EN · `YuGothB.ttc` 70 px JA).
Dung lượng: VI 1,33 MB · EN 1,33 MB · JA 1,34 MB. Chữ: VI `KÝ ỨC / HWASEONG` · EN `MEMORIES / HWASEONG` · JA `記憶 / ファセオン`.

**Mô tả YouTube**: giữ nguyên toàn bộ nội dung mô tả đã xuất bản, **chỉ thay mốc chương** bằng mốc đo thật:

| Ngôn ngữ | Mốc chương cũ (ước lượng) | Mốc chương mới (đo thật) |
|---|---|---|
| VI | 00:23 / 05:00 / 10:00 / 15:30 / 21:00 | 00:23 / **09:23 / 16:11 / 23:03 / 30:58** |
| EN | 00:23 / 05:00 / 10:00 / 15:30 / 21:00 | 00:23 / **08:38 / 15:14 / 22:27 / 30:18** |
| JA | 00:23 / 05:00 / 10:00 / 15:30 / 21:00 | 00:23 / **09:51 / 17:16 / 25:40 / 34:46** |

> Vì sao không dùng `package.py --mux` cho cả 3 bản: VN `description()` sinh mô tả rút gọn (mất khối "10 chỉ dấu"); EN `description_en()` đọc `CHU_CO_DINH_EN.md` — Tập 24 **không có** file này ⇒ crash; JA `description_ja()` lấy `EPISODES["24"]["title"]` là tiếng Việt ⇒ in tiếng Việt. Vì vậy dùng `.work/_package_t24.py`: **mux + thumbnail + thay mốc chương**, giữ nguyên mô tả gốc.

---

## 8. Bảng cổng QC

| Cổng | VI | EN | JA | Ghi chú |
|---|:---:|:---:|:---:|---|
| `qc_pause_gate.py` (A13) | ✅ ĐẠT | ✅ ĐẠT | ✅ ĐẠT | trung vị nghỉ 0,95 s · 0 % < 0,4 s · timeline = master ±0,00 s |
| `qc_bg_usage.py` (H22) | ✅ ĐẠT | ✅ ĐẠT | ✅ ĐẠT | 0 ảnh thừa / 0 mượn nền / 0 vượt 3 shot-30 s |
| `qc_pause_gate.py --pre` (A13) | ✅ ĐẠT | ✅ ĐẠT | ✅ ĐẠT | file diễn xuất: 0 mã lạ, 0 giá trị ngoài 0,2–1,2 s |
| `qc_bg_mapping.py 24` (H27) | ❌ TRƯỢT | ❌ TRƯỢT | — | xem §9.1 |
| `qc_wave_gate.py` (H24) | ✅ ĐẠT | ✅ ĐẠT | ✅ ĐẠT | sau khi tạo pseudo-stem (§9.2) — chạm trần 1,5–3,2 %, lệch chuẩn 0,25–0,28, p95 0,90 |
| `qc_master_voice_presence.py` (**cổng thay thế A14**) | ✅ ĐẠT | ✅ ĐẠT | ✅ ĐẠT | 0 câu mất giọng · 0 đoạn lặng > 1 s · 0 khoảng lặng > 3,5 s |
| `qc_bg.py` (chất lượng ảnh) | ⚠ 147/155 | ⚠ 147/155 | ⚠ 147/155 | 8 ảnh có dải tối — đã soi: thuộc nội dung cảnh, không phải letterbox |
| Kiểm tra cuối `_verify_final_t24.py` | ✅ ĐẠT | ✅ ĐẠT | ✅ ĐẠT | timeline/mp4/SRT/mốc chương/thumbnail/provenance khớp |

---

## 9. Ngoại lệ cần người dùng biết

### 9.1 `qc_bg_mapping.py 24` — TRƯỢT 2 luật

```
Tập 24: TRƯỢT · M1 mã sai 91/155 · M2 trùng — · M5 câu chưa phủ 182/246
         · M4 prompt riêng 22/155 MẪU CHUNG · M3(cảnh báo) tên ['lee','choon','jae'] có trong job
```

- **M1 + M5 (91/155 và 182/246): giới hạn của cổng, KHÔNG phải lỗi dữ liệu.** Cổng tách mã câu bằng `re.split(r"[,;\s]+", …)` — không tách được dấu `–`, nên `bg_jobs_tap24.json` ghi dải mã kiểu `1.02#1–1.02#2` bị coi là 1 mã lạ. **Cùng trạng thái này xảy ra ở Tập 18/19/20/21/22/23** (cùng định dạng dải mã); chỉ Tập 25 (định dạng phân tách bằng dấu phẩy) là ĐẠT cả 4 luật. Bảng shot thực tế phủ đúng 246/246 câu (đã kiểm bằng `qc_bg_usage.py`).
- **M4 (22/155 prompt riêng): vi phạm THẬT của Tập 24** — cần ≥ 140 prompt khác nhau. Bộ ảnh dùng **17 prompt mẫu chung** lặp lại ⇒ **hệ quả trực tiếp của quyết định giữ nguyên 155 ảnh**. Muốn đóng được M4 thì phải sinh lại ảnh — việc người dùng đã chốt không làm.

### 9.2 Badge sóng giọng (H24) — ĐÃ SỬA xong bằng pseudo-stem + dựng lại video

**Phát hiện 26/11/2026 (sau khi bản xuất bản đầu đã hoàn tất):** dải sóng trên badge vai bị **thẳng ngang** — 26 vạch cao đều 3 px ở mọi khung hình, ở cả 3 ngôn ngữ.

**Nguyên nhân gốc:** `build_video3.py::_env_for()` (dòng 1856–1868) đọc envelope từ `ED.w("stems")/{H,D,C,N1,N2}.wav`; **Tập 24 không có thư mục stem nào** ⇒ `ENV` rỗng ⇒ `v = 0` ⇒ `hh = 3 + int(30*v) = 3 px` mọi vạch. Master audio Tập 24 được dựng trên **máy khác** (Higgs Audio v3, 22/11/2026) nên chỉ có file trộn sẵn, không kèm stem giọng tách vai.

> **Đính chính báo cáo cũ (sai):** báo cáo 25/11 ghi "`qc_wave_gate.py` không chạy được" và "chấp nhận badge không sóng". Cả hai đều **không đúng**: cổng H24 **chạy được** và báo **TRƯỢT 5/5 vai × 3 ngôn ngữ** khi thiếu stem (exit 1) — tức lỗi này bị cổng bắt được nhưng đã bị bỏ qua; và H24 quy định rõ *"vạch phẳng (không có stem)" là trạng thái **TRƯỢT***, không phải ngoại lệ được chấp nhận.

**Cách sửa đã áp dụng (theo đúng lối thoát chuẩn của dự án — `TIEU_CHUAN_DUNG_VIDEO.md` mục #186):**

1. `.work/make_pseudo_stems.py` — cắt master mp3 theo **cửa sổ câu của từng vai** (ngoài cửa sổ = 0), ghi `_PSEUDO.txt` trong thư mục stem. Cùng cơ chế đã dùng cho **Tập 11** và có script riêng cho **T13–T18**.
   - Nguồn: `Tap24_master.mp3` (VN 2203,30 s · EN 2137,38 s · JA 2444,66 s — khớp timeline tuyệt đối).
   - Timeline đủ vai cho 246 câu: **H 130 · C 53 · D 42 · N1 8 · N2 13**.
   - Output: `.work/stems_t24/`, `.work/stems_EN_t24/`, `.work/stems_JA_t24/` (5 file wav/ngôn ngữ + `_PSEUDO.txt`).
   - **0 credit**, không đổi giọng, **không sửa `build_video3.py`** (giữ nguyên renderer dùng chung).
2. Cổng `qc_wave_gate.py` (H24) sau khi có pseudo-stem → **ĐẠT cả 3 ngôn ngữ**:

   | Ngôn ngữ | Chạm trần (≤10 %) | Lệch chuẩn (≥0,15) | p95 (0,6–1,0) | Vai có lời |
   |---|---|---|---|---|
   | VI | 1,6 – 2,9 % | 0,25 – 0,27 | 0,90 | H/C/D/N1/N2 ✓ |
   | EN | 1,9 – 3,0 % | 0,25 – 0,27 | 0,90 | H/C/D/N1/N2 ✓ |
   | JA | 1,5 – 3,2 % | 0,25 – 0,28 | 0,90 | H/C/D/N1/N2 ✓ |

3. **Dựng lại toàn bộ 3 video** (6 lô/ngôn ngữ, 4–6 worker) rồi đóng gói lại (mux + thumbnail + mốc chương).
   - Hoàn tất: VN 11:21 · EN 13:32 · JA 15:29 (26/11/2026). Tổng ~7 giờ dựng máy.
   - `picture.mp4` mới: VN 2203,300 s · EN 2137,367 s · JA 2444,633 s — khớp `timeline.total`.
   - Master mp4 mới: 871,5 / 845,2 / 968,3 MB · 1920×1080 @ 30 fps · H.264 + AAC 192 k.
4. **Kiểm chứng hậu dựng (H24):** trích **3 khung liên tiếp** trong 1 câu thoại từ chính `*_master.mp4` (VN @ 1:00 · EN @ 1:00 · JA @ 5:00) ⇒ **dải sóng đổi hình giữa các khung** (ảnh lưu tại `.work/scratch/wave_chk/{vn_new,en_new,ja_new}/`).
5. **Kiểm tra cuối** `_verify_final_t24.py` ⇒ **ĐẠT cả 3 ngôn ngữ**; `qc_wave_gate.py` chạy lại ⇒ **ĐẠT cả 3 ngôn ngữ**.

**Giới hạn của pseudo-stem (ghi rõ trong hồ sơ):** trong cửa sổ câu, master còn lẫn nhạc nền/SFX ⇒ dải sóng phản ánh **giọng + nhạc lẫn trong cửa sổ câu** (đúng như Tập 11). Vì vậy:
- Chỉ dùng cho **sóng badge + cổng H24**; **KHÔNG** thay thế A14.
- A14 vẫn kiểm bằng cổng thay thế `qc_master_voice_presence.py` → **ĐẠT cả 3 ngôn ngữ** (0 câu mất giọng · 0 đoạn lặng > 1 s · 0 khoảng lặng > 3,5 s) — ghi rõ là **kiểm thay thế**.


### 9.3 H10 — shot vượt 15 s

VN 4/246 shot · EN 2/246 · JA 4/246 (dài nhất 21,1 s). Nguyên nhân: câu thoại dài + audio cố định; `parse_shots.py` gán thời lượng theo mã câu nên không tách được 1 câu thành 2 shot. (Tập 18 — mẫu H25 — chỉ 1 shot vượt 15 s.)

### 9.4 Intro JA — tiêu đề đỏ ở góc trên-trái hiển thị 8 ô vuông (thiếu glyph)

`assets/brand/intro_kenh_JA_t24.mov` là **bản copy nguyên vẹn** của `intro_kenh_JA_t18.mov` (md5 `edac63c63f0f`, dùng chung với Tập 16/17/18).

- **Phần nội dung intro bằng tiếng Nhật hiển thị đúng** (đã trích frame kiểm tra) — 20,5 s đầu video JA không bị đen.
- **Lỗi có sẵn trong file nguồn**: dòng tiêu đề đỏ ở góc trên-trái hiển thị **8 ô vuông thay cho chữ** ⇒ font trong file .mov không khớp glyph (thiếu phông trong hệ thống dựng).
- **Không sửa được bằng script**: file `.mov` không kèm dự án nguồn (không có .prproj/.aep) để thay font; mã hóa lại bằng ffmpeg không khôi phục được glyph đã mất.
- **Không đoán chữ thương hiệu**: nội dung là dòng tiêu đề kênh/series, không suy đoán.
- ⇒ **Đã chốt (25/11/2026, người dùng): (a) chấp nhận lỗi có sẵn** ở Tập 16/17/18, không cần file intro gốc mới. Ghi nhận ngoại lệ trong hồ sơ, **không sửa video**.

---

## 10. Bản lưu (L5)

| Nội dung | Đường dẫn bản lưu |
|---|---|
| 3 file SRT gốc (trước khi chạy lại `subtitles.py`) | `.work/_cu/srt_t24_20261125/` |
| 3 file plan (trước khi sinh lại) | `.work/_cu/plan_t24_20261125/` |
| `provenance.json` (trước khi thêm dòng thumbnail) | `.work/_cu/provenance_t24_20261125/provenance.json` |
| **3 master mp4 + 3 thumbnail bản 25/11 (dải sóng thẳng ngang)** — trước khi dựng lại 26/11 | `.work/_cu/t24_wavefix_20261126/` (2,56 GB) |

---

## 11. Việc còn lại cho người dùng

1. **Nghe duyệt lại 3 bản video** — đặc biệt: dải sóng badge (đã sửa, xem §9.2), intro JA (file copy từ t16–t18, đã chốt chấp nhận lỗi tiêu đề §9.4), mốc chương trong mô tả, và 81 ảnh nền có chữ AI (§6).
2. **Kiểm tra nguồn** trước khi đăng: `nguon_tham_khao*.md` / `nguon_mo_ta*.txt` (chưa tự điền link).
3. **Điều khoản YouTube / nhãn nội dung** theo chính sách kênh.
4. **Chưa commit** (L10): mp4/wav/thumbnail là media ⇒ không commit; các file JSON/MD thay đổi đang chờ duyệt.

> Đã chốt: (1) 25/11 — giữ nguyên 155 ảnh, chỉ làm từ mục 2; (2) 25/11 — chấp nhận lỗi tiêu đề đỏ intro JA (§9.4); (3) 26/11 — **dựng lại cả 3 video, tuần tự từng video, bắt buộc có dải sóng giọng nói** (§9.2, đã xong).
