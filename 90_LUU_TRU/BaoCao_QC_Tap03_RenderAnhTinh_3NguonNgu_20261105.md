# BÁO CÁO QC · TẬP 03 · RENDER LẠI ẢNH TĨNH 3 NGÔN NGỮ (VN / EN / JA)

**Ngày:** 05/11/2026 (lượt 2, sau phiên render đầu 14:40–16:11) · **Kênh:** Amber Eyes
**Hồ sơ:** `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md` (+ `_EN`, `_JA`)
**Lệnh dựng:** `py -3 .work/build_video3.py --stills all` (AE_EP=03, AE_LANG=vi|en|ja)

> Báo cáo này bổ sung cho `BaoCao_QC_Tap03_RenderAnhTinh_20261105.md` (lượt 1 trong ngày).

---

## 1. KẾT LUẬN

| Bản | Ảnh tĩnh | Contact sheet | 11 cổng QC bảng shot | Ảnh hỏng | H15 tất định |
|:---|---:|:---:|:---:|---:|:---:|
| **VN** | **110 / 110** | 13 tờ + 5 tờ/hồi | **11 OK / 0 lỗi** | 0 | ✔ |
| **EN** | **110 / 110** | 13 tờ + 5 tờ/hồi | **11 OK / 0 lỗi** | 0 | ✔ 110/110 byte giống nhau giữa 2 lượt |
| **JA** | **110 / 110** | 13 tờ + 5 tờ/hồi | **11 OK / 0 lỗi** | 0 | ✔ |

**Sửa trong lượt này (2 lỗi thật, đều là chữ trên hình — KHÔNG đụng lời đọc):**

| # | Bản | Shot | Trước | Sau | Lý do |
|:--|:---|:---|:---|:---|:---|
| 1 | EN | `5-02` | **8 CONCURRENT LIFE TERMS** | **EIGHT CONCURRENT LIFE TERMS** | Quy tắc kênh "câu đọc viết số bằng chữ ⇒ hình cũng viết bằng chữ". Câu `5.02#4` đọc *"eight concurrent life terms"* → số `8` trên hình là lệch (cùng loại với 13 shot EN đã sửa lượt 1) |
| 2 | VN | `5-21` | **AMBER EYES** · *Đón xem tập tiếp theo* | **HỒ SƠ TẬP 03 · ĐÃ ĐÓNG** · **AMBER EYES** · *Phân tích tâm lý tội phạm qua những hồ sơ có thật* · *Đón xem tập tiếp theo* | **H12** — thẻ kết thiếu nhãn + khẩu hiệu |
| 3 | JA | `5-21` | **AMBER EYES** · *次回のエピソードをお楽しみに* | **事件ファイル 第03話 · 終結** · **AMBER EYES** · *実際の事件記録から読み解く犯罪心理学* · *次回のエピソードをお楽しみに* | **H12** — thẻ kết thiếu nhãn + khẩu hiệu |

> Bản EN đã có đủ 3 thành phần H12 từ đầu (`CASE FILE 03 · CLOSED` / `AMBER EYES` / `Criminal psychology through real case files`) ⇒ **chỉ VN + JA là thiếu**. Dòng *"Đón xem tập tiếp theo"* / *"次回のエピソードをお楽しみに"* **giữ nguyên**, không xoá gì.

---

## 2. KỊCH BẢN MỚI ĐỔI GÌ? — ĐO ĐẾM, KHÔNG ĐOÁN

Phiên bản 4 (sửa 05/11/2026) là **tái cấu trúc**, **không phải viết lại lời**. Đo bằng `.work/_verify_t03_script.py` (parse lại `.md` rồi so từng câu với `timeline_s_*.json` — tức âm thanh đã thu):

| Chỉ số | VN | EN | JA |
|:---|---:|---:|---:|
| Element | 55 | 55 | 55 |
| Câu | 218 | 218 | 218 |
| Câu phủ được trong timeline (âm thanh đã thu) | **218/218** | **218/218** | **218/218** |
| Câu khớp chữ với timeline (đã chuẩn hoá dấu nháy) | **218/218** | **218/218** | **218/218** |

⇒ **Âm thanh đã thu (31/10–03/11) vẫn khớp 100% — KHÔNG cần thu lại.**
Phần "bổ sung thêm nhiều yếu tố" là: tái cấu trúc bảng metadata theo khung *Hệ sinh thái 10 chỉ dấu tâm lý* (A2c/K10) · viết lại hướng dẫn diễn · đổi format 1 câu = 1 dòng · đổi quy ước trích dẫn `'…'`.

**Bảng shot cũng không cần sửa cấu trúc:** parse lại `KeHoach_Video_Tap03{,_EN,_JA}.md` cho ra `shots_*.json` **y hệt** bản đang dùng (110 shot, cùng `total`, cùng mọi trường) — trừ 3 dòng chữ trên hình đã sửa ở mục 1.

---

## 3. QUY TẮC SỐ TRÊN HÌNH — SOI TỪNG NGÔN NGỮ (phát hiện lỗi ở EN)

Quy tắc kênh: **câu đọc viết số bằng chữ ⇒ chữ trên hình cũng viết bằng chữ** (xem báo cáo Tập 02, shot `5-09`). Script `.work/_check_t03_numstyle.py` quét **chỉ chữ thực sự được vẽ** (`segments[*].elems`) — không tính `beat_text` (đó là chỉ dẫn đặt nhịp, không vẽ lên hình).

| Bản | Số trên hình ↔ câu đọc | Kết luận |
|:---|:---|:---|
| VN | shot `5-02` — số `8` trên hình ↔ câu đọc có **"tám"** | ⚠ nghi vấn → kiểm lại: câu `5.02#4` viết **"8 bản án tù chung"** (dạng số) ⇒ hình viết `8` là **đúng** ✔ |
| EN | shot `5-02` — số `8` trên hình ↔ câu đọc có **"eight"** | ✗ **LỖI THẬT** → đã sửa (mục 1) |
| JA | kịch bản JA viết số bằng **chữ số** ngay trong lời đọc (`5年間` / `3つ` / `10回` / `8件`) | ✔ khớp 100 %, quy tắc "viết bằng chữ" **không áp cho JA** |

> Bản JA dùng chữ số trong lời đọc là chuẩn riêng của bản Nhật (đúng với `CHU_CO_DINH_JA.md`), nên **không** sửa gì ở JA.

---

## 4. THẺ KẾT (H12) — ĐỐI CHIẾU 9 THẺ KẾT TRONG REPO

| Tập | Nhãn hồ sơ | AMBER EYES | Khẩu hiệu |
|:---|:---|:---:|:---:|
| Tap01 VN | ✗ | ✗ | ✗ |
| Tap01 JA | *事件記録 第01話 · 完結* | ✔ | ✔ |
| **Tap02 VN** | *HỒ SƠ TẬP 02 · ĐÃ ĐÓNG* | ✔ | ✔ (2 dòng) |
| **Tap02 EN** | *DOSSIER EPISODE 02 · CLOSED* | ✔ | ✔ (2 dòng) |
| **Tap02 JA** | *事件ファイル 第02話 · 終結* | ✔ | ✔ |
| **Tap03 EN** | *CASE FILE 03 · CLOSED* | ✔ | ✔ |
| **Tap04 VN** | *HỒ SƠ TẬP 04 · ĐÃ ĐÓNG* | ✔ | ✔ (2 dòng) |
| **Tap04 JA** | *事件記録 第04話 · 終了* | ✔ | ✔ |
| **Tap05 VN** | *HỒ SƠ TẬP 05 · ĐÃ ĐÓNG* | ✔ | ✔ (1 dòng) |
| **Tap03 VN** (trước) | ✗ | ✔ | ✗ → **đã sửa** |
| **Tap03 JA** (trước) | ✗ | ✔ | ✗ → **đã sửa** |

⇒ 7/9 thẻ kết trong repo theo đúng H12; **Tap03 VN + JA là hai ngoại lệ** (cùng tập, bản EN thì đúng) ⇒ coi là thiếu sót khi soạn bảng shot, đã vá.

---

## 5. ĐO TẤT ĐỊNH (H15) + ĐỐI CHIẾU HASH

* **Tất định:** render EN 2 lượt độc lập → **110/110 ảnh giống byte-for-byte** (`stills_manifest_afterA.json` vs `afterB.json`).
* **So với bản ảnh trước lượt này** (manifest `before` lúc 18:05):

| Bản | Ảnh đổi byte | Ảnh giữ nguyên |
|:---|---:|---:|
| VN | 92 | 18 |
| EN | 92 | 18 |
| JA | 93 | 17 |

**Nguyên nhân 92–93 ảnh đổi: KHÔNG phải lỗi nội dung — là mất file `stems` (mục 6).** Mọi ảnh đổi đều là shot **có badge vai**; mọi ảnh giữ nguyên đều là shot **không có vai** (thẻ chương / giữ / lời kết).

---

## 6. ⚠ PHÁT HIỆN NGOÀI PHẠM VI: SESSION KHÁC ĐÃ XOÁ `stems` + MASTER CỦA TẬP 03

Trong lúc render, **một session khác đang chạy song song trong cùng workspace đã dọn đĩa** (AGENTS.md §11 · T17). Thiệt hại:

| Mất | Hậu quả |
|:---|:---|
| `.work/stems_t03/` · `stems_EN_t03/` · `stems_JA_t03/` | Badge vai **không còn sóng âm** → vẽ thành **đường gạch ngang phẳng** thay vì thanh sóng. Đây là lý do 92–93 ảnh đổi byte |
| `02_SAN_XUAT/Tap03*/xuat_ban/*_master.mp3` và `Tap03_JA_master.mp4` | **Không còn master âm thanh** ⇒ không dựng lại được `stems` (script `_build_stems_t02.py` cần master) |

* Bằng chứng renderer cũ **bắt buộc** có `stems` mới chạy được: hàm `_env_for()` trước commit `5bf1d5f` (05/11 17:15) gọi `wave.open()` trực tiếp ⇒ **thiếu file là crash**. Lượt render 14:40–16:11 (còn `stems`) chạy được ⇒ `stems` còn tồn tại lúc đó; hiện đã mất.
* Renderer mới (`5bf1d5f`, 17:15) **không crash** nữa mà trả về mảng rỗng ⇒ badge vẽ 26 thanh cao đều 3 px = **gạch ngang phẳng** (đã soi bằng mắt, ảnh `.work/_qc_t03_20261105/badge_zoom.png`).
* **Chỉ ảnh trên bị ảnh hưởng** — nền, chữ trên hình, thẻ kết, mốc thời gian, badge vai đều đúng.
* **Cách khôi phục** (1 lệnh, khi master âm thanh còn trong repo hoặc được dựng lại):
  1. dựng lại master Tập 03 (VN/EN/JA) → `02_SAN_XUAT/Tap03*/xuat_ban/*_master.mp3`
  2. `py -3 .work/_build_stems_t02.py` (đổi đường dẫn + `TL_PATH` + `OUT_DIR` cho từng bản) → sinh `stems_t03/`, `stems_EN_t03/`, `stems_JA_t03/`
  3. `py -3 .work/build_video3.py --stills all` lại cho 3 bản ⇒ badge có sóng âm trở lại
* **Không tự bịa sóng âm giả**: hiện chưa có master ⇒ không dựng được envelope thật; không dùng sóng tổng hợp vì sẽ lệch với video khi dựng lại.

---

## 7. SỐ ĐO QC

### 7.1 Cổng QC bảng shot (`.work/_qc_tap02_shots.py`, dùng chung) — **3/3 bản 11/11 OK**

| Cổng | VN | EN | JA |
|:---|:---:|:---:|:---:|
| Câu trong timeline có trong bảng shot (thiếu/thừa) | ✔ 0/0 | ✔ 0/0 | ✔ 0/0 |
| Câu thuộc hai shot | ✔ | ✔ | ✔ |
| Phủ câu | ✔ 218/218 | ✔ 218/218 | ✔ 218/218 |
| Thứ tự shot khớp kịch bản | ✔ | ✔ | ✔ |
| Cột Vai khớp người nói | ✔ | ✔ | ✔ |
| Nền có file thật | ✔ | ✔ | ✔ |
| Chữ trích dẫn nguyên văn (V3) | ✔ 0 lỗi | ✔ 0 lỗi | ✔ 0 lỗi |
| **Số trên hình có trong câu (A9.2)** | ✔ 0 lỗi | ✔ 0 lỗi | ✔ 0 lỗi |
| Từ cấm / hành vi tình dục | ✔ 0 lỗi | ✔ 0 lỗi | ✔ 0 lỗi |
| Shot > 15 s có nhịp hoặc bám V2 | ✔ | ✔ | ✔ |
| Shot liền nhau (không hở/chồng) | ✔ | ✔ | ✔ |

### 7.2 Cổng ảnh (`.work/_qc_t03_stills_final.py`)

| Chỉ số | VN | EN | JA |
|:---|---:|---:|---:|
| Ảnh / shot | 110/110 | 110/110 | 110/110 |
| Ảnh thừa / thiếu | 0 / 0 | 0 / 0 | 0 / 0 |
| Ảnh hỏng (< 20 KB hoặc không mở được) | 0 | 0 | 0 |
| Thời lượng shot (min–max) | 0,8–48,97 s | 0,8–40,37 s | 0,8–56,37 s |
| Shot ngoài 3–15 s | 74 | 68 | 80 |
| **Chuỗi nền lặp liền > 4 shot** | **0** | **0** | **0** |
| Thẻ kết có nhãn + tên kênh + khẩu hiệu | ✔ | ✔ | ✔ |

> Shot ngoài 3–15 s là **thuộc thiết kế bảng shot cũ** (shot "giữ" + beat theo cụm từ) và đã được cổng "Shot > 15 s có nhịp hoặc bám V2" chấp nhận — **không phải hồi quy do lượt render này** (bảng shot không đổi cấu trúc).

### 7.3 Kiểm bằng mắt (H2)

* `shot_1-02` (VN): phóng to 1920×1080 — chữ "lạ" nhìn thấy ở contact sheet thực ra là **dòng phụ đề của chính kênh** (màu vàng) nằm trên thiết bị; **không có chữ AI vẽ**, không mặt, không watermark ✔
* `shot_5-21` (VN/EN/JA): thẻ kết 4 dòng, không chồng chữ, tương phản tốt ✔
* `shot_5-02` (EN): "EIGHT CONCURRENT LIFE TERMS" hiển thị đúng, không tràn khung ✔

---

## 8. VIỆC CÒN LẠI / CẦN NGƯỜI DÙNG QUYẾT

| # | Việc | Trạng thái |
|:--|:---|:---|
| 1 | **Ảnh tĩnh VN / EN / JA** | ✅ **Xong** — 110 ảnh mỗi bản, 11/11 cổng QC, 0 lỗi |
| 2 | **Dựng video Tập 03** | ❌ **KHÔNG làm** — người dùng chỉ yêu cầu ảnh tĩnh (giống lượt 1) |
| 3 | **Ghép audio + xuất bản** | ❌ Không làm. `package.py --mux` chỉ chạy khi có yêu cầu rõ ràng |
| 4 | **Bản KO** | ⛔ Không tạo (quyết định 05/11) — giữ nguyên |
| 5 | **Sóng âm trên badge vai** | ⚠ **Cần master âm thanh Tập 03 đã bị xoá** → xem mục 6. Khi có master: dựng `stems` → render lại 3 bản (mỗi bản ~2 phút) |
| 6 | **Video đã xuất bản của Tập 03** | ⚠ Master mp3/mp4 bị session dọn đĩa xoá ⇒ nếu muốn xuất bản lại cần dựng lại master |

---

## 9. FILE ĐÃ TẠO / SỬA

| File | Trạng thái |
|:---|:---|
| `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md` | sửa — 2 dòng: `5-02` không đổi · `5-21` thêm nhãn + khẩu hiệu (H12) |
| `02_SAN_XUAT/Tap03_EN/KeHoach_Video_Tap03_EN.md` | sửa — 2 dòng: `5-02` "8"→"EIGHT" · `5-21` giữ nguyên |
| `02_SAN_XUAT/Tap03_JA/KeHoach_Video_Tap03_JA.md` | sửa — 1 dòng: `5-21` thêm nhãn + khẩu hiệu (H12) |
| `.work/shots_t03.json` · `shots_EN_t03.json` · `shots_JA_t03.json` | sinh lại (110 shot mỗi bản) |
| `.work/video3_t03/stills/` · `video3_EN_t03/stills/` · `video3_JA_t03/stills/` | 110 ảnh mới mỗi bản |
| `02_SAN_XUAT/Tap03*/contact_sheet_*.png` | contact sheet 3 bản (13 tờ + 5 tờ/hồi) |
| `.work/_cu/t03_20261105_1800/` | **sao lưu trước khi ghi** (L5): 3 bảng shot + 3 timeline + script + 3 hồ sơ + 4 manifest hash |
| `.work/_verify_t03_script.py` · `_parse_shots_t03_langs.py` · `_check_t03_numstyle.py` · `_qc_t03_gates.py` · `_qc_t03_stills_final.py` · `_render_stills_t03.py` · `_manifest_t03_stills.py` · `_diff_stills_t03.py` | script kiểm dùng chung cho lượt này |
