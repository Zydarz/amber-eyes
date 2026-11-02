# CHUẨN TIÊU ĐỀ SERIES — AMBER EYES
**Cập nhật:** 02/11/2026 · **Áp dụng:** Tập 01–07 (EN / VN / JA / KO) — Tập 08+ chuyển khi đóng gói

---

## 1. KHUÔN TIÊU ĐỀ

```
<MARKER TẬP> <HOOK> | <The Psychology of SUBJECT> (<MECHANISM>)
```

| Thành phần | Quy tắc |
|---|---|
| **MARKER TẬP** | EN `Ep. NN:` · VN `Tập NN:` · JA `第NN話 ·` · KO `NN화 ·` — **dùng đúng marker đã burn trên hình video** (JA card ghi `第01話 · 母の愛という名の毒薬`, KO card ghi `01화 · …`) |
| **HOOK** | Cụm từ ngắn, dễ nhớ, ưu tiên lấy từ **thumbnail** của tập (VD `THE PURPLE FLOPPY DISK`) |
| **SUBJECT** | Tên nhân vật/vụ án — dùng đúng cách viết trong script của từng ngôn ngữ |
| **MECHANISM** | Trục tâm lý của tập (theo `01_KICH_BAN/KHO_Y_TUONG_28_HO_SO.md`) — có thể viết tắt (`FDIA`, `ASPD`) hoặc viết đầy (`Behavioral Escalation`) |
| **Hậu tố** | ❌ Không dùng `| Amber eyes` nữa — kênh đã có tên ở tên kênh YouTube |

> **Lưu ý SEO:** tiêu đề EN nên ≤ 100 ký tự để không bị YouTube cắt. Ep. 01 dài 89 ký tự ✓. **Ep. 02 dài 106 ký tự → vượt ngưỡng, sẽ bị cắt.** Bản rút gọn nếu bạn muốn: `Ep. 02: A Predator Disguised as Honor | The Psychology of R. Williams (Behavioral Escalation)` (96 ký tự).

---

## 2. BẢNG TIÊU ĐỀ ĐÃ CHỐT

### Tiếng Anh

| Ep. | Tiêu đề | Ký tự |
|---|---|---|
| 01 | `Ep. 01: Poison Disguised as Mother's Love \| The Psychology of Gypsy Rose Blanchard (FDIA)` | 89 |
| 02 | `Ep. 02: A Predator Disguised as Honor \| The Psychology of Colonel Russell Williams (Behavioral Escalation)` | **106** ⚠ |
| 03 | `Ep. 03: The IQ 145 Giant \| The Psychology of Edmund Kemper (Psychopathy)` | 72 |
| 04 | `Ep. 04: The Angel of Death \| The Psychology of Charles Cullen (God Complex)` | 75 |
| 05 | `Ep. 05: The Purple Floppy Disk \| The Psychology of BTK Dennis Rader (Compartmentalization)` | 90 |
| 06 | `Ep. 06: The Clown Beneath the Floorboards \| The Psychology of John Wayne Gacy (ASPD)` | 84 |
| 07 | `Ep. 07: Murder by Text Message \| The Psychology of Michelle Carter (Histrionic Personality)` | 91 |

### Tiếng Việt

| Ep. | Tiêu đề |
|---|---|
| 01 | `Tập 01: Độc Dược Nhân Danh Tình Mẹ \| Tâm lý học tội phạm: Gypsy Rose Blanchard (FDIA)` |
| 02 | `Tập 02: Kẻ Săn Mồi Ẩn Sau Danh Dựng \| Tâm lý học tội phạm: Đại tá Russell Williams (Quy luật leo thang hành vi)` |
| 03 | `Tập 03: Gã Khổng Lồ IQ 145 \| Tâm lý học tội phạm: Edmund Kemper (Thái nhân cách)` |
| 04 | `Tập 04: Thiên Thần Tử Thần \| Tâm lý học tội phạm: Charles Cullen (Phức cảm Chúa trời)` |
| 05 | `Tập 05: Chiếc Đĩa Mềm Màu Tím \| Tâm lý học tội phạm: BTK Dennis Rader (Sự phân mảnh tâm trí)` |
| 06 | `Tập 06: Nụ Cười Chú Hề \| Tâm lý học tội phạm: John Wayne Gacy (ASPD)` |
| 07 | `Tập 07: Bản Án Giết Người Bằng Tin Nhắn \| Tâm lý học tội phạm: Michelle Carter (Nhân cách kịch tính)` |

### Tiếng Nhật

| Ep. | Tiêu đề |
|---|---|
| 01 | `第01話 · 母の愛という名の毒薬 \| Gypsy Rose Blanchardの心理学 (FDIA)` |
| 02 | `第02話 · 二重生活の大佐 \| ラッセル・ウィリアムズ大佐の心理学 (行動のエスカレーション)` |

### Tiếng Hàn

| Ep. | Tiêu đề |
|---|---|
| 01 | `01화 · 엄마의 사랑이라는 이름의 독약 \| Gypsy Rose Blanchard의 심리학 (FDIA)` |

> Tương lai: Tập 03+ JA/KO sẽ theo đúng khuôn này — marker `第NN話 ·` / `NN화 ·`, hook lấy từ thumbnail, subject + cơ chế tâm lý.

---

## 3. NGUỒN SỰ THẬT

| Nội dung | File nguồn | Ghi chú |
|---|---|---|
| Tiêu đề (VN/EN/JA/KO) | `.work/edition.py` → `EPISODES["NN"]["title"]` | nhiều ngôn ngữ dùng biểu thức điều kiện `if EN else …` |
| Tiêu đề EN trong mô tả | `02_SAN_XUAT/TapNN_EN/CHU_CO_DINH_EN.md` (khối ```text có `CHAPTERS`) | `package.py` đọc từ đây, **không** đọc `edition.py` cho EN |
| Sinh file mô tả | `.work/package.py` | `description()` VN · `description_en()` · `description_ko()` · `description_ja()` |

⚠ **Sửa 1 chỗ là chưa đủ** — phải sửa cả `edition.py` + file mô tả đã đóng gói + (nếu có) `CHU_CO_DINH_*.md`. Nếu không, lần `package.py` chạy lại sẽ ghi đè.

---

## 4. LUẬT MỐC CHƯƠNG (ĐÃ SỬA 02/11/2026)

**Mốc hồi = câu thoại ĐẦU TIÊN của hồi đó** (`timeline.items` → `act` + `start`), **làm tròn** giây.

⛔ **Không dùng marker `ACT` trong timeline.** Marker là *thời điểm KẾT THÚC hồi trước*, nên chapter rơi vào khoảng đen chuyển hồi hoặc card của hồi trước:

| Tập | Mốc cũ (marker) | Mốc mới | Frame thật ở mốc cũ | Frame thật ở mốc mới |
|---|---|---|---|---|
| Tap02 EN hồi 2 | 04:40 (280,40 s) | **04:42** (282,40 s) | ⬛ màn hình đen | `ACT 02 — THE 4 STAGES OF THE ABYSS` |
| Tap02 EN hồi 1 | 00:20 (20,5 s) | **00:23** (23,00 s) | thẻ `VIEWER DISCRETION & ADVISORY` | `ACT 01 — THE EXTREME CONTRAST…` |
| Tap05 EN hồi 2 | 05:09 (309 s) | **05:11** (311 s) | `ACT 01 — THE PURPLE FLOPPY DISK…` | `ACT 02 — THE CRIME SCENE & PSYCHOLOGICAL SIGNATURE…` |

Đã áp dụng cho **22 file mô tả** của Tập 01–07 (EN/VN/JA/KO) — mọi mốc cũ đều lệch 2–3 s.

Code đã sửa trong `.work/package.py`:
- `act_start_times(tl)` — lấy cue đầu tiên mỗi hồi (fallback marker).
- `mmss(t)` — làm tròn thay vì cắt cụt (cắt cụt làm chapter lọt vào khoảng đen).
- `with_brand(title)` — không nối `| Amber eyes` khi tiêu đề đã ở khuôn mới; Tập 08+ giữ hành vi cũ.

---

## 5. VIỆC CÒN LẠI

1. **📚 SOURCES của Tập 02 EN** đang là `[PENDING]` — 30/30 dòng trong `nguon_tham_khao_EN.md` chưa có nguồn. Không đăng được.
2. Bật nhãn **"Altered or synthetic content"** khi đăng YouTube.
3. Rà điều khoản thương mại Higgs Audio v3 (đã ghi công trong mô tả).
4. **Tập 08+**: khi đóng gói, đặt tiêu đề theo khuôn §1 và dùng `with_brand()` (tự bỏ `| Amber eyes`).
