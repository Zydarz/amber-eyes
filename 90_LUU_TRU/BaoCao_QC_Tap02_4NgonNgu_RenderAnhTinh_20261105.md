# BÁO CÁO QC & RENDER ẢNH TĨNH · TẬP 02 · 4 NGÔN NGỮ (VN / EN / JA / KO)

**Ngày:** 05/11/2026 · **Phạm vi:** dựng lại bảng shot + QC + render **ảnh tĩnh** (không build video) cho Tập 02 sau khi kịch bản 4 ngôn ngữ được viết lại (bản "10 chỉ dấu tâm lý").

---

## 1. Tóm tắt

Cả 4 ngôn ngữ đã có **bảng shot 161 dòng** phủ **203/203 câu**, **QC 11/11 cổng xanh**, và **161 ảnh tĩnh** + **18 contact sheet** mỗi ngôn ngữ.

| Ngôn ngữ | Hồ sơ bảng shot | Dòng | Câu | Timeline | Ảnh tĩnh | Contact sheet | QC |
|---|---|---|---|---|---|---|---|
| **VN** | `02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md` | 161 | 203/203 | **1.519,08 s** — đo thật (Whisper) | 161 | 18 | ✅ 11/11 |
| **EN** | `02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md` | 161 | 203/203 | 1.548,69 s — **tạm** | 161 | 18 | ✅ 11/11 |
| **JA** | `02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md` | 161 | 203/203 | 2.049,54 s — **tạm** | 161 | 18 | ✅ 11/11 |
| **KO** | `02_SAN_XUAT/Tap02_KO/KeHoach_Video_Tap02_KO.md` | 161 | 203/203 | 1.953,97 s — **tạm** | 161 | 18 | ✅ 11/11 |

Cấu trúc 161 dòng giống nhau: **144 shot có lời + 17 dòng không lời**; mã shot đánh lại tuần tự theo hồi (`1-00 … 5-36`).

---

## 2. Kiến trúc đã dùng (phát hiện quan trọng)

**Bảng shot của EN/JA/KO không viết tay — nó SINH TỰ ĐỘNG từ bảng VN + một "lớp phủ chữ trên hình" riêng:**

```
02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md      ← bảng VN 161 dòng (nguồn sự thật duy nhất)
                    │
                    ├── .work/shots_text_tap02_EN.json  ─┐
                    ├── .work/shots_text_tap02_JA.json  ─┼─→ .work/_build_plan_tap02_{en,ja,ko}.py
                    └── .work/shots_text_tap02_KO.json  ─┘        └→ bảng shot + QC + parse_shots
```

Lớp phủ có dạng `{"mã shot": [chữ trên hình, [cụm beat…], override]}`; script dựng tự kiểm: **cụm beat phải có thật trong câu**, **trích dẫn `“…”` phải nguyên văn**, **mọi số trên hình phải truy được về câu**.

**4 kịch bản song song tuyệt đối:** cùng 63 element, cùng 36 lượt nói, cùng 203 câu, cùng mã câu, cùng số câu mỗi element, cùng vai diễn. Nhờ vậy bảng VN dùng được cho cả 3 bản dịch chỉ bằng cách thay cột chữ.

---

## 3. Lỗi tìm được & đã sửa

### 3.1 Kịch bản EN — 27 dấu nháy cong sai hướng (ảnh hưởng TTS + chữ trên hình)
Markdown EN dùng ASCII `'` cho **cả** dấu nháy kép lẫn dấu nháy trong từ (`don't`, `Williams's`), parser ghép cặp sai và sinh ra `don”t` / `I“m` / `Williams“s` / `: ”`.

* **Đã sửa:** `01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md` + bản trùng trong `01_KICH_BAN/Tap02/kichban_tap02_EN.md` → đổi dấu nháy trong từ sang `’` (typographic). Sao lưu: `.work/_cu/kichban_tap02_EN_pre_quote_fix_20261105.md`.
* **Hệ quả:** 2 dòng chữ trên hình (`3-20`, `4-18`) trước đó hiện `don…t` → nay hiện trích dẫn nguyên văn `don’t`.
* ⚠ **Quan trọng cho TTS:** cần đọc lại TTS sau khi sửa này, nếu không giọng đọc sẽ sai ("Williams s").

### 3.2 Nhãn vai N1/N2 của JA/KO dùng nhầm nhãn chung của Tập 01
JA hiện `証人` (nhân chứng) và KO hiện `증인` cho vai N1 — nhưng vai N1 của Tập 02 là **quan binh căn cứ Trenton**, N2 là **dân Tweed (Mèo)**.

* **Đã sửa:** khai `roles_ja` / `roles_ko` / `sub_tags_ja` / `sub_tags_ko` cho `EPISODES["02"]` trong `.work/edition.py`, và cho `ROLE_NAME` / `SUB_TAG` ưu tiên bản riêng theo ngôn ngữ.
* Nay hiện: JA `トレントン基地関係者` / `ツイード住民` — KO `트렌턴 기지 관계자` / `트위드 주민`.

### 3.3 Timeline tạm của 3 bản dịch — 3 lỗi kỹ thuật
| Lỗi | Hậu quả | Cách sửa |
|---|---|---|
| Marker `ACT` / `NGHI` giữ mốc thời gian của timeline cũ | Shot "chuyển hồi" **90–160 s**, shot "nghỉ" lệch, **11 shot có thời lượng ÂM** | Tính lại `ACT`/`NGHI`/`acts` từ mốc câu mới; thứ tự element lấy theo **mã element** (= thứ tự đọc), không theo mốc thời gian cũ |
| 15 câu mới chưa có trong timeline gốc bị gán vai mặc định `"H"` và `act=1` | QC "Cột vai" đỏ 5 shot; renderer crash `KeyError: 'N'` | Vai lấy từ kịch bản + ánh xạ `N → N1/N2` theo `EPISODES["02"]["n_element"]`; hồi lấy từ mã element |
| Mất đoạn outro cuối tập | Thẻ kết `5-36` có 0 giây | Thêm outro chuẩn 9,0 s (đo trên cả 3 timeline gốc) |

### 3.4 Renderer — 2 thay đổi bổ sung (không đụng nhánh VN/EN/JA)
* `.work/build_video3.py`: thêm nhánh font **Hàn** (`malgunbd.ttf` / `malgun.ttf`) — trước đó chữ Hàn sẽ ra ô vuông tofu; thêm fallback khi thiếu stem giọng (badge bỏ sóng âm thanh thay vì crash).
* Kiểm hồi quy: **render lại ảnh VN** sau khi sửa và đối chiếu bằng mắt → chữ tiếng Việt, sóng âm thanh, nhân vật đều đúng.

### 3.5 Dọn
Ảnh JA thừa `shot_3-31.png` từ lần render cũ (mã shot đã đánh lại) → chuyển sang `.work/_cu/shot_3-31_stale_20261105.png`.

---

## 4. ⚠ Vấn đề nội dung CẦN BẠN QUYẾT

### 4.1 JA và KO **thiếu hẳn** lớp nội dung "Vật hóa nạn nhân (Objectification)"

| Element | VN / EN | JA / KO |
|---|---|---|
| `3.11` | **Tầng 3 · Vật hóa nạn nhân + Ái kỷ ác tính** (`3.11#1`: "Trong vật hóa nạn nhân, kẻ phạm tội biến nạn nhân thành **đạo cụ sống**…"; `3.11#4`: "…**ái kỷ ác tính**…") | **Tiếp của Tầng 2 (compartmentalization / hai thế giới ngày–đêm)**, nội dung Objectification chỉ lóe ở câu cuối |

Đã quét toàn bộ 203 câu của từng bản: cụm "vật hóa / đạo cụ sống / objectification / living props / 対象化 / 살아있는 소품" **có ở VN + EN, không có ở JA + KO**.

⇒ 4 bản đang kể **hai phiên bản khác nhau của hồi 3**. Ảnh tĩnh JA/KO vẫn **tự nhất quán** (chữ trên hình đã bám đúng câu JA/KO), nhưng **câu chuyện không khớp giữa các bản**.

**Cần bạn chọn:** (a) viết bổ sung lớp Objectification vào kịch bản JA/KO, hay (b) sửa lại `3.11` của VN/EN cho khớp JA/KO. Tôi **không tự sửa** vì đây là quyết định biên tập nội dung.

### 4.2 Vi phạm H10 (shot 3–15 s) — hệ quả tự nhiên của tiếng Nhật/Hàn
| Ngôn ngữ | Shot > 15 s | Shot dài nhất |
|---|---|---|
| VN | 23 | 22,9 s (`1-18`) |
| EN | 23 | 29,0 s (`3-15`) |
| JA | **50** | **40,6 s** (`3-30`) |
| KO | **46** | **34,0 s** (`3-18`) |

Tiếng Nhật/Hàn đọc chậm hơn tiếng Anh ~30–35% nên cùng một bảng shot cho ra shot dài hơn. Các shot dài đều **có nhịp** (đổi mẫu/nhịp beat theo khoảnh khắc), nhưng nếu bạn muốn siết H10 cho JA/KO thì phải **tách shot thêm** (tăng số dòng bảng shot) — cần bạn quyết.

---

## 5. Việc còn lại theo từng ngôn ngữ

### VN — gần xong
- [x] Bảng shot 161 dòng, QC xanh, ảnh tĩnh theo timeline **đo thật**
- [ ] Sinh lại `.srt` từ timeline mới (timeline đổi lúc 15:29 ⇒ `.srt` cũ đã lệch)
- [ ] Ghép video + đối chiếu A/V

### EN
- [x] Bảng shot 161 dòng, QC xanh, ảnh tĩnh (timeline **tạm**)
- [ ] **Đọc lại TTS** (Higgs/Kaggle) → `audio_master_EN_t02.wav` — *cần GPU Kaggle*
- [ ] Dựng lại timeline bằng Whisper → dựng lại ảnh
- [ ] Sinh `.srt` + `stems_EN_t02/{H,D,C,N1,N2}.wav` (hiện badge **chưa có sóng âm thanh**)
- [ ] `assets/brand/intro_kenh_EN_t02.mov` — hồ sơ nhắc tới nhưng **file chưa có**

### JA
- [x] Bảng shot 161 dòng, QC xanh, ảnh tĩnh (timeline **tạm**)
- [ ] **Đọc lại TTS** → `audio_master_JA_t02.wav` (bản 11/4 cũ ứng với kịch bản cũ) — *cần GPU Kaggle*
- [ ] Dựng lại timeline bằng Whisper → dựng lại ảnh
- [ ] Sinh `.srt` mới (`.srt` cũ ứng với timeline cũ)
- [ ] Stems: có `stems_JA_t02/` nhưng ứng với audio cũ → sinh lại

### KO — dựng mới gần như từ đầu
- [x] Bảng shot 161 dòng (dựng mới), QC xanh, ảnh tĩnh (timeline **tạm**, font Hàn đã thêm)
- [ ] **Đọc lại TTS** (chưa có audio master KO nào) — *cần GPU Kaggle*
- [ ] Dựng timeline Whisper → dựng lại ảnh
- [ ] `stems_KO_t02/` (badge hiện chưa có sóng âm thanh)
- [ ] `.srt` KO, `acting_tap02_KO.json`, `intro_kenh_KO_t02.mov`, thumbnail, mô tả + hotline Hàn

---

## 6. File bàn giao

### Hồ sơ (đã cập nhật)
```
02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md        161 dòng (nguồn sự thật)
02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md  161 dòng
02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md  161 dòng
02_SAN_XUAT/Tap02_KO/KeHoach_Video_Tap02_KO.md  161 dòng  (mới)
01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md        đã sửa 27 dấu nháy
01_KICH_BAN/Tap02/kichban_tap02_EN.md           đã sửa 27 dấu nháy (bản trùng)
```

### Ảnh tĩnh (161 ảnh / ngôn ngữ)
```
.work/video3_t02/stills/shot_<mã>.png
.work/video3_EN_t02/stills/shot_<mã>.png
.work/video3_JA_t02/stills/shot_<mã>.png
.work/video3_KO_t02/stills/shot_<mã>.png
```

### Contact sheet (18 trang / ngôn ngữ)
```
.work/qc_t02_20261105/contact_sheet/sheet_01..18.png         VN
.work/qc_t02_en_20261105/contact_sheet/sheet_01..18.png      EN
.work/qc_t02_ja_20261105/contact_sheet/sheet_01..18.png      JA
.work/qc_t02_ko_20261105/contact_sheet/sheet_01..18.png      KO
```

### Script dùng lại được
```
.work/_build_timeline_langs_t02.py   dựng timeline EN/JA/KO (tạm) — chạy lại được, idempotent
.work/_qc_tap02_langs.py              QC 11 cổng, đa ngôn ngữ  (AE_LANG=vi|en|ja|ko)
.work/_pipeline_stills_t02.py         parse_shots → QC → render ảnh → contact sheet
.work/_mk_contact_langs.py            dựng contact sheet
.work/_build_plan_tap02_{en,ja,ko}.py sinh bảng shot + kiểm lớp phủ
```

### Sao lưu (L5)
`.work/_cu/` — bảng shot & timeline cũ, lớp phủ EN/JA cũ, kịch bản EN trước khi sửa nháy, ảnh JA thừa.

---

## 7. Ghi chú kỹ thuật

* **Timeline EN/JA/KO là TẠM.** Cách dựng: giữ **mốc element** đo được từ audio master cũ (nhịp phim, khoảng lặng, vị trí SFX), chỉ **chia lại thời lượng từng câu** theo độ dài câu mới. 15 câu mới được đặt vào đúng element theo thứ tự đọc. KO chưa có audio nào ⇒ dùng khung nhịp của timeline VN + tốc độ đọc ước tính theo tiếng Nhật (cùng hệ âm tiết CJK).
* **Ảnh tĩnh render tại GIỮA shot** ⇒ chữ hiện đúng khoảnh khắc; dòng "nghỉ" dùng mẫu kế thừa từ shot trước.
* **Chỉ dựng ảnh, không build video** (theo yêu cầu) ⇒ không đụng tới `package.py` / mux / kiểm A-V.
* Lệnh tái lập:
  ```powershell
  $env:PYTHONIOENCODING='utf-8'; py -3 .work/_build_timeline_langs_t02.py --apply
  $env:AE_LANG='ko'; $env:AE_EP='02'; py -3 .work/_pipeline_stills_t02.py ko
  ```
