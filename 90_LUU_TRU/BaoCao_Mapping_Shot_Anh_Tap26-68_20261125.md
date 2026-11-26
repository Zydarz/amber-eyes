# BÁO CÁO RIÊNG: MAPPING SHOT ↔ ẢNH NỀN · TẬP 26–68

> **Ngày:** 25/11/2026 · **Viết cho:** chủ kênh Amber Eyes (người duyệt và sinh ảnh) · **Tóm tắt một dòng:** mapping và prompt đã xong cho 40 tập; việc còn lại chủ yếu là **sinh ảnh** và **dựng thử khi có audio**.
> Số liệu đo trực tiếp từ đĩa lúc lập báo cáo (`py -3 .work/map_shot_anh.py --check`, quét `assets/bg/`). Báo cáo tổng hợp cũ nằm ở `BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md` mục VI–VII.

---

## 1. Tóm tắt nhanh

| Hạng mục | Kết quả |
|---|---|
| Tập có mapping | **40 tập**: 26–63, 65, 67 |
| Tập bị loại (để nguyên) | **64, 66, 68** — kịch bản mới 52 / 61 / 49 câu, chưa mở rộng (H23) |
| Lỗi mapping | **0** ở cả 40 tập (không ảnh lặp, không câu thiếu hay trùng ảnh) |
| Tổng shot đã lập | 6,108 shot (mỗi shot đúng 1 ảnh) |
| Ảnh đã có file | 1,147 / 6,108 |
| **Ảnh còn phải sinh** | **4,961** ảnh, thuộc 33 tập |
| Tập đạt đủ cổng `--check` (mapping + đủ ảnh) | **7 tập**: 26, 27, 28, 29, 30, 36, 40 |

---

## 2. "Mapping shot ↔ ảnh" là gì và dùng thế nào

- Mỗi tập có **một file hướng dẫn**: `02_SAN_XUAT/Ho_So_Toi_Pham/TapXX/Bang_Shot_Anh_TapXX.md`. Mỗi dòng ghi: shot nào · các câu thoại nào · ảnh nào (`assets/bg/<tên>.png`) · ảnh đã có file chưa · mô tả cảnh.
- Bản máy đọc: `.work/shot_map_tapXX.json`.
- **Mapping chỉ làm một lần**, ngay lúc viết prompt: tên ảnh = tên job trong `bg_jobs_tapXX.json`. Sinh ảnh xong, **lưu đúng tên file** là tự khớp shot; không phải ghép lại.
- Sau khi có ảnh chỉ cần: (1) `--check` xem đủ file chưa; (2) soi ảnh bằng mắt; (3) khi có audio thì đo thời lượng thật.
- **Luật dựng (H28 trong `AGENTS.md`):** AI dựng video Tập 26–68 phải đọc file mapping này và dùng đúng ảnh cho đúng câu. Cấm tự chọn ảnh theo chủ đề, cấm lặp ảnh, cấm đổi thứ tự.

### Các lệnh

| Việc | Lệnh |
|---|---|
| Lập hoặc lập lại bảng mapping | `py -3 .work/map_shot_anh.py XX` |
| Cổng trước khi dựng (phải ĐẠT) | `py -3 .work/map_shot_anh.py --check XX` |
| Tạo `shots_tXX.json` cho `build_video3.py` (cần timeline đo thật) | `py -3 .work/map_shot_anh.py --shots XX --lang vi --endcard <tên ảnh thẻ kết>` (`--lang` nhận vi, en hoặc ja) |

---

## 3. Tình trạng từng tập

Cột "Shot dài" = số shot ước **> 15 s / > 30 s** (thời lượng chỉ là **ước lượng** từ số từ; chưa có audio). ✅ = mapping đạt và đủ ảnh · ⏳ = mapping đạt, **thiếu ảnh** · ⛔ = chưa lập.

| Tập | Số câu | Shot (= ảnh) | Ảnh có file | Ảnh thiếu | Shot dài | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
| 26 | 240 | 176 | 176 | 0 | 53 / 0 | ✅ đạt | ảnh lỗi giữ nguyên: a1_13b; tách 9 ảnh `…b` để sửa lặp ảnh |
| 27 | 240 | 152 | 152 | 0 | 66 / 1 | ✅ đạt | — |
| 28 | 240 | 152 | 152 | 0 | 58 / 0 | ✅ đạt | — |
| 29 | 240 | 152 | 152 | 0 | 60 / 1 | ✅ đạt | — |
| 30 | 240 | 204 | 204 | 0 | 30 / 0 | ✅ đạt | — |
| 31 | 240 | 163 | 0 | 163 | 60 / 0 | ⏳ thiếu ảnh | — |
| 32 | 240 | 143 | 0 | 143 | 90 / 0 | ⏳ thiếu ảnh | — |
| 33 | 240 | 136 | 0 | 136 | 77 / 0 | ⏳ thiếu ảnh | — |
| 34 | 210 | 148 | 0 | 148 | 39 / 0 | ⏳ thiếu ảnh | — |
| 35 | 238 | 150 | 0 | 150 | 70 / 0 | ⏳ thiếu ảnh | — |
| 36 | 237 | 157 | 157 | 0 | 63 / 3 | ✅ đạt | ảnh do phiên khác sinh và sửa chữ; **tôi chưa soi** — nên soi 100 % trước khi dựng |
| 37 | 221 | 122 | 0 | 122 | 71 / 2 | ⏳ thiếu ảnh | — |
| 38 | 218 | 188 | 0 | 188 | 17 / 0 | ⏳ thiếu ảnh | — |
| 39 | 240 | 135 | 0 | 135 | 80 / 0 | ⏳ thiếu ảnh | — |
| 40 | 238 | 154 | 154 | 0 | 63 / 0 | ✅ đạt | ảnh lỗi giữ nguyên: a5_10b, a5_02; tách 5 shot dài, sửa prompt, đã xoá ảnh thừa `a5_27` cũ |
| 41 | 227 | 157 | 0 | 157 | 58 / 0 | ⏳ thiếu ảnh | — |
| 42 | 215 | 143 | 0 | 143 | 68 / 0 | ⏳ thiếu ảnh | — |
| 43 | 240 | 159 | 0 | 159 | 63 / 0 | ⏳ thiếu ảnh | — |
| 44 | 240 | 167 | 0 | 167 | 51 / 0 | ⏳ thiếu ảnh | — |
| 45 | 240 | 143 | 0 | 143 | 81 / 0 | ⏳ thiếu ảnh | — |
| 46 | 241 | 151 | 0 | 151 | 60 / 0 | ⏳ thiếu ảnh | — |
| 47 | 240 | 152 | 0 | 152 | 79 / 1 | ⏳ thiếu ảnh | — |
| 48 | 240 | 135 | 0 | 135 | 80 / 0 | ⏳ thiếu ảnh | — |
| 49 | 243 | 190 | 0 | 190 | 10 / 0 | ⏳ thiếu ảnh | viết lại 190 prompt cho 243 câu (25/11) |
| 50 | 240 | 190 | 0 | 190 | 37 / 0 | ⏳ thiếu ảnh | — |
| 51 | 240 | 133 | 0 | 133 | 103 / 0 | ⏳ thiếu ảnh | — |
| 52 | 221 | 153 | 0 | 153 | 64 / 0 | ⏳ thiếu ảnh | — |
| 53 | 242 | 145 | 0 | 145 | 82 / 0 | ⏳ thiếu ảnh | — |
| 54 | 240 | 158 | 0 | 158 | 72 / 0 | ⏳ thiếu ảnh | — |
| 55 | 242 | 193 | 0 | 193 | 37 / 0 | ⏳ thiếu ảnh | — |
| 56 | 221 | 116 | 0 | 116 | 86 / 0 | ⏳ thiếu ảnh | — |
| 57 | 227 | 150 | 0 | 150 | 68 / 0 | ⏳ thiếu ảnh | — |
| 58 | 240 | 150 | 0 | 150 | 77 / 0 | ⏳ thiếu ảnh | — |
| 59 | 216 | 138 | 0 | 138 | 35 / 0 | ⏳ thiếu ảnh | — |
| 60 | 240 | 169 | 0 | 169 | 47 / 0 | ⏳ thiếu ảnh | — |
| 61 | 240 | 149 | 0 | 149 | 82 / 0 | ⏳ thiếu ảnh | — |
| 62 | 207 | 130 | 0 | 130 | 75 / 0 | ⏳ thiếu ảnh | — |
| 63 | 231 | 144 | 0 | 144 | 63 / 0 | ⏳ thiếu ảnh | — |
| 64 | 52 | — | — | — | — | ⛔ chưa lập | Kịch bản mới 52 câu, chưa mở rộng (H23) — để nguyên theo quyết định |
| 65 | 211 | 134 | 0 | 134 | 59 / 0 | ⏳ thiếu ảnh | — |
| 66 | 61 | — | — | — | — | ⛔ chưa lập | Kịch bản mới 61 câu, chưa mở rộng (H23) — để nguyên theo quyết định |
| 67 | 220 | 127 | 0 | 127 | 75 / 0 | ⏳ thiếu ảnh | — |
| 68 | 49 | — | — | — | — | ⛔ chưa lập | Kịch bản mới 49 câu, chưa mở rộng (H23) — để nguyên theo quyết định |

---

## 4. Những gì đã làm trong phiên này

1. **Kiểm 43 tập (26–68)**: 39 tập có prompt hợp lệ, Tập 49 trượt, Tập 64/66/68 chưa có prompt.
2. **Tập 26 — sửa lặp ảnh.** Nguyên nhân: 32 job `_x` được chèn vào giữa đoạn câu của job gốc nhưng job gốc không được cắt lại, chỉ còn 2 mã đầu mút (vd `1.04#7,1.06#1`) ⇒ 9 ảnh bị gán 2 vị trí. Không thiếu ảnh, prompt đúng cảnh. Đã viết **9 prompt mới** (job hậu tố `…b`).
3. **Tập 40.** Sửa prompt 4 ảnh thiếu (trong đó `a2_14` cũ **sai nghĩa**: vẽ văn phòng chiến dịch cho câu về đường dây nóng); tách **5 shot ước > 35 s** thành 2 ảnh; sửa lỗi 1 câu bị 2 ảnh cùng nhận (`a5_27` viết lại cho câu `5.05#4`); đã xoá ảnh thừa `a5_27` cũ.
4. **Tập 49.** Viết lại toàn bộ **190 prompt cho 243 câu**. Bản cũ chỉ có 17 prompt khác nhau trên 146 job (bộ "mẫu chung").
5. **Sửa công cụ:** `qc_bg_mapping.py` và `map_shot_anh.py` từng chọn nhầm file kịch bản `…_backup_61cau.md` cho Tập 49 (số đo "61 câu" là sai; thực tế 243). Đã loại file có chữ `backup`.
6. **Viết công cụ** `map_shot_anh.py` (lập bảng, `--check`, `--shots`).
7. **Ghi luật vào `AGENTS.md`:** H28 mới + cập nhật L1, bước 7, bước 9; ghi A11 #194 vào `TIEU_CHUAN_DUNG_VIDEO.md`. `CLAUDE.md` và `GEMINI.md` đã trỏ `@AGENTS.md` nên mọi AI đều đọc.
8. **Nối mapping vào pipeline dựng:** `--shots` tạo `shots_tXX.json` cùng schema với `shots_t10.json`.
9. **Đã commit và push** phần mapping (commit `c2bd681`).
10. **Soi độc lập 19 ảnh mới** của Tập 26/40 (do phiên khác sinh): 16 sạch, 3 còn lỗi — bạn chốt **giữ nguyên**.

---

## 5. Vấn đề còn vướng (xếp theo mức ảnh hưởng)

### 5.1. Chặn việc dựng

| # | Vấn đề | Cần làm |
|---|---|---|
| 1 | **Chưa có ảnh cho 33 tập (4,961 ảnh).** Chi tiết từng tập ở mục 3. | Bạn sinh ảnh (Kaggle FLUX, H21), lưu **đúng tên** `assets/bg/<tên job>.png` |
| 2 | **Chưa có audio / `timeline_s` thật** cho tập nào từ 26 trở lên. Lệnh `--shots` mới chỉ chạy thử với timeline giả (Tập 27). | Làm bước 2–6 của quy trình (giọng, trộn âm thanh) |

### 5.2. Rủi ro khi dựng (chưa kiểm được)

| # | Rủi ro | Ghi chú |
|---|---|---|
| 3 | **Chưa render thật** bằng `build_video3.py` với shot `template`/`role` rỗng (theo H26: khung chỉ có ảnh + số). | Chạy ảnh tĩnh (bước 8) ngay khi có audio đầu tiên |
| 4 | **Thời lượng shot chỉ là ước lượng.** Khoảng 35–100 shot mỗi tập ước dài hơn 15 s (H10); 8 shot ước hơn 30 s, mức vượt nhỏ. | Đo lại bằng `timeline_s`, chỉ tách khi thật sự > 30 s |
| 5 | **3 ảnh lỗi giữ nguyên** (quyết định của bạn): `t40_a5_10b` và `t26_a1_13b` có viền giấy kem + chữ giả; `t40_a5_02` có biển nhỏ nghi chữ. | Soi 3 shot này khi dựng; lộ viền/chữ thì cắt mép hoặc sinh lại cùng tên. Đã ghi ⚠ trong bảng mapping |
| 6 | **Thẻ kết chưa có ảnh riêng**; không truyền `--endcard` thì mượn ảnh shot cuối (H22: nên có ảnh riêng). | Chỉ định ảnh thẻ kết khi chạy `--shots` |
| 7 | **`edition.py` chỉ hỗ trợ EN/JA/KO tới Tập 29** ⇒ từ Tập 30 chỉ dựng được bản tiếng Việt. | Mở rộng nếu cần bản đa ngôn ngữ |

### 5.3. Tồn đọng nhỏ

| # | Việc | Ghi chú |
|---|---|---|
| 8 | **Tập 64, 66, 68** chưa có prompt/mapping. | Chờ mở rộng kịch bản (≈ 240 câu, K1–K10) |
| 9 | `provenance.json` còn **2 dòng tên cũ** của Tập 40 (`t40_a2_14_political…`, `t40_a5_27_final…`). | Giữ làm lịch sử hoặc dọn |
| 10 | `.work/_staging_bg_jobs/` là **bản cũ** (chưa có job mới Tập 26/40/49). | Không chạy `_sync_bg_jobs.py` khi chưa cập nhật |
| 11 | **Mục V của `BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md`** vẫn ghi sai "đã có ảnh Tập 01–32…" (đã đính chính ở mục VI.6, chưa sửa chữ gốc). | Muốn thì sửa |
| 12 | Cổng `qc_bg_mapping.py` **chưa bắt được** lỗi "mã câu rời rạc" (nguyên nhân lỗi Tập 26). | Nên vá cổng trước khi dùng cho tập mới |
| 13 | Kịch bản Tập 49 nhắc "kim tiêm" (câu `3.04#6`) và thuốc gây mê (câu `2.06#3`). | Prompt ảnh đã né; nội dung kịch bản cần rà K4/V9 khi duyệt |
| 14 | Lỗi ô thừa ở các bảng cũ trong tiêu chuẩn (A11 #190–191, `AGENTS.md` dòng 853–854), có từ trước. | Dọn khi tiện |

### 5.4. Git và làm việc song song

- Có **nhiều phiên cùng chạy trong repo này** (phiên sinh ảnh Tập 36 đã sửa `bg_jobs_tap36.json`, `provenance.json`, thêm nhiều script `_*`; ảnh Tập 36 chưa được soi mắt ở phiên này). Tôi **không đụng** phần đó.
- Chưa commit: phần của tôi (`map_shot_anh.py` bản có `KNOWN`, bảng mapping Tập 26/40/36, báo cáo) lẫn với thay đổi của phiên khác.

---

## 6. Quy trình từ đây (checklist cho mỗi tập)

1. Sinh đủ ảnh theo `Bang_Shot_Anh_TapXX.md` (lưu đúng tên) → `py -3 .work/map_shot_anh.py --check XX` ĐẠT.
2. Soi 100 % ảnh mới (chữ AI vẽ, viền, lộ mặt — H2/H19/H20/H26); ảnh hỏng sinh lại **cùng tên**.
3. Làm giọng + âm thanh theo quy trình → có `timeline_s_tXX.json` đo thật, `timeline.total` khớp master (T20).
4. `py -3 .work/map_shot_anh.py --shots XX --endcard <ảnh thẻ kết>` → sinh `shots_tXX.json`.
5. Ảnh tĩnh mọi shot (bước 8), soi các shot có ⚠ → dựng hình (bước 9) → đóng gói.
6. Sửa kịch bản / `bg_jobs` / audio ⇒ chạy lại `map_shot_anh.py XX` rồi `--check`.

---

## 7. File liên quan

| Loại | Đường dẫn |
|---|---|
| Bảng mapping từng tập | `02_SAN_XUAT/Ho_So_Toi_Pham/TapXX/Bang_Shot_Anh_TapXX.md` |
| Bản máy đọc | `.work/shot_map_tapXX.json` |
| Prompt sinh ảnh | `.work/bg_jobs_tapXX.json` |
| Công cụ | `.work/map_shot_anh.py` · `.work/qc_bg_mapping.py` · `.work/scan_bg_content.py` |
| Luật | `AGENTS.md` (H27, H28) · `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` A11 #193–194 |
| Báo cáo liên quan | `BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md` mục VI–VII · `90_LUU_TRU/BaoCao_TaoAnh_Tap26_Tap40_20261125.md` |
| Sao lưu trước khi sửa | `.work/_cu/` (bg_jobs T26/T40/T49, AGENTS, TIEU_CHUAN, công cụ, ảnh `a5_27` cũ) |

## 8. Vì sao có tập "đã có ảnh" mà báo cáo ghi 0, và việc dọn ảnh cũ (25/11/2026)

**Nguyên nhân.** Ảnh Tập 31, 32, 34, 35, 37, 38, 39 (≈ 1.061 ảnh) được sinh **trước** đợt xáo thứ tự tập ngày 24/11. Ngày 24/11 đợt xử lý mapping chuyển chúng vào `.work/_cu/bg_old_20261124/tXX/` (bài học H27) và **viết lại toàn bộ `bg_jobs` với tên ảnh mới**. Mapping khớp theo tên file nên 0 tên khớp ⇒ cổng đo ra 0 ảnh. Cùng lúc `provenance.json` vẫn ghi ảnh cũ và mục V của báo cáo thống kê chưa được cập nhật ⇒ nhìn vào sổ vẫn tưởng "có ảnh".

**Đối chiếu tên job cũ với kịch bản hiện tại (chỉ qua tên file, không mở ảnh):** ảnh cũ của Tập 31 (Shanann/Watts), 34 (Northwestern 1978, chuyến bay 444/Kaczynski) và 38 (đường cao tốc, lán gỗ, gương ký ức) **có vẻ đúng vụ án hiện tại**; ảnh cũ Tập 32, 35, 37, 39 và `t30` (nhà Watts) thuộc vụ án khác. Người dùng quyết định **không tái dùng, sinh lại toàn bộ bằng prompt mới** để tránh nhầm lẫn.

**Đã xoá (25/11/2026, theo yêu cầu người dùng; vào Thùng rác, khôi phục được tới khi dọn):**
| Nơi | Nội dung | Ghi chú |
|---|---|---|
| `.work/_cu/bg_old_20261124/t31, t32, t34, t35, t37, t38, t39/` | 7 thư mục ảnh cũ, 1.061 ảnh ≈ 5,1 GB | giữ lại các file `bg_jobs_*.json` cũ |
| `.work/_backup_before_shuffle/assets_bg/` | 851 ảnh `t29–t34` ≈ 4,1 GB (170 ảnh `t30` cũ không còn trong `assets/bg`; 37 ảnh `t29` là bản cũ; 115 ảnh giống hệt `assets/bg`) | giữ `01_KICH_BAN/`, `02_SAN_XUAT/`, `provenance.json` của bản backup |
| `.work/kaggle_flux/out_t37_k1`, `out_t37_k2` | kết quả sinh cũ Tập 37 (148 ảnh + zip + log), 0/122 tên khớp job hiện tại | |

**Giữ nguyên:** `assets/bg/` (mọi ảnh đang dùng, kể cả Tập 36 và Tập 40); các thư mục `*_replaced`, `t40_v9`, `t41_replaced`; mọi file `bg_jobs_*.json` cũ trong `.work/_cu/`.

**Kiểm sau xoá:** Tập 31–39 (trừ 36) không còn ảnh `tNN_*` ở bất kỳ nơi nào trên đĩa; `--check` vẫn **ĐẠT** cho Tập 26, 27, 28, 29, 30, 36, 40.

**Còn lại cần biết:** `provenance.json` vẫn còn các dòng ghi ảnh cũ (≈ 170/152/145/148/148/146/152 dòng cho Tập 31–39) trỏ tới file **không còn tồn tại** — để làm lịch sử, chưa dọn. Khi sinh ảnh mới, tên mới sẽ có dòng riêng. Ổ D: còn trống ≈ 43 GB trong Thùng rác chưa dọn; muốn giải phóng thật phải dọn Recycle Bin (mục 11 `AGENTS.md`).

## 9. Soi lại ảnh lần cuối (25/11/2026)

Phạm vi: 7 tập đã có đủ ảnh (26, 27, 28, 29, 30, 36, 40).

**Cổng máy**
- `map_shot_anh.py --check` ĐẠT cả 7 tập: 0 lỗi mapping, bảng không cũ, 0 ảnh thiếu file.
- `qc_bg_mapping.py` ĐẠT cả 7 tập: M1 0 mã sai, M5 0 câu chưa phủ, M4 mọi prompt riêng.
- Số ảnh trên đĩa khớp số shot: 26 = 176, 27 = 152, 28 = 152, 29 = 152, 30 = 204, 36 = 157, 40 = 154.
- `qc_bg_usage.py` không chạy được cho tập 26+: nó đọc `shots_tXX.json`, file này chỉ có sau khi có audio (H28).

**Soi mắt**
- Máy dò chữ `_detect_text_bg.py` xếp hạng các ảnh nghi chữ nhất của tập 26, 36, 40; tôi ghép 28 ảnh vào 3 tờ montage và mở zoom hai ảnh nghi nhất.
- Tập 27, 28, 29, 30 chưa soi mắt lần này.
- Tập 36 sạch: 12 ảnh nghi nhất không có chữ.

| Ảnh | Lỗi | Xử lý |
|---|---|---|
| `t26_a4_23_public_outcry_tokyo_streets` | Chữ AI "RELAEL PASSEN" trên đầu tàu điện, thêm biển phản đối (H26) | **MỚI, chờ quyết định sinh lại** |
| `t40_a1_18_fleeing_taillights_in_the_rain` | Biển số xe có chữ AI "T9Y 110" (H2/H26) | **MỚI, chờ quyết định sinh lại** |
| `t26_a1_13b_…`, `t40_a5_10b_…`, `t40_a5_02_…` | Đã biết từ trước | Giữ nguyên theo quyết định 25/11 |

Hai ảnh MỚI đã ghi cảnh báo ⚠ vào `Bang_Shot_Anh_Tap26.md` và `Bang_Shot_Anh_Tap40.md` (khai ở `KNOWN` của `map_shot_anh.py`). Nếu sinh lại thì giữ nguyên tên file, thêm mệnh đề "no tram destination text, no placards" và "blank unreadable plate".
