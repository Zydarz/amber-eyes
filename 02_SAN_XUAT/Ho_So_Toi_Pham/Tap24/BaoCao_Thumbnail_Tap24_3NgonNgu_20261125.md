# Báo cáo dựng ảnh thumbnail Tập 24 — 3 ngôn ngữ (VI / EN / JA)

**Ngày:** 25/11/2026 · **Người thực hiện:** AI (MCode) · **Tập:** 24 — Hồ Sơ Lee Choon-jae (Hwaseong, Gyeonggi, Hàn Quốc)

---

## 1. Yêu cầu

Dựng `thumbnail.png` (1280×720) cho 3 bản Tập 24, mỗi ngôn ngữ một cặp chữ riêng, nền đúng chủ đề tập (H11), không dùng lại nền của tập khác.

## 2. Nguồn đã đọc

| Nguồn | Dùng để |
|---|---|
| `assets/bg/t24_*.png` (155 ảnh) | chọn nền — soi full-res |
| `02_SAN_XUAT/Ho_So_Toi_Pham/Tap24*/mo_ta.txt` | tiêu đề đã xuất bản (đối chiếu chữ thumbnail) |
| `01_KICH_BAN/Ho_So_Toi_Pham/Tap24*/kichban_tap24*.md` | nội dung 5 hồi, cụm từ nổi bật |

## 3. Quyết định

### 3.1 Nền thumbnail (H11)

**Chọn:** `assets/bg/t24_a1_30_prison_cell_embroidery_desk_30.png`

Lý do: **bàn thêu hoa trong buồng giam Busan** là dấu vật "ký ức" của hồ sơ Lee Choon-jae — người tù thêu ren 25 năm và câu chuyện được giải mã từ chiếc áo màu đỏ (Hồi 1) tới thư phòng tù (Hồi 3–4). Nền tối, trung tâm trống cho chữ, **không có chữ AI** (đã soi full-res), do Cloudflare Workers AI FLUX sinh ngày 21/11/2026 (có dòng provenance riêng).

**Loại** (không dùng): `t24_a4_28_hall_of_justice_m Marble_corridor_28` (biển `CALIFORNIA` — sai bối cảnh Hàn Quốc), `t24_a3_01_forensic_investigation_desk_01` (chữ AI đọc được), `t24_a1_05_police_patrol_rural_search_05` (biển POLICE).

### 3.2 Chữ trên thumbnail (A11 #148)

Trước khi sửa, `EPISODES["24"]["thumb"]` chỉ có **một** cặp chữ tiếng Việt ⇒ bản EN/JA sẽ in chữ tiếng Việt (đúng lỗi Tập 07/08 đã ghi ở TIEU_CHUAN #148).

| Ngôn ngữ | Dòng 1 | Dòng 2 |
|---|---|---|
| VI | `KÝ ỨC` | `HWASEONG` |
| EN | `MEMORIES` | `HWASEONG` |
| JA | `記憶` | `ファセオン` |

EN lấy từ tiêu đề đã xuất bản ("**Memories** of the Hwaseong Serial Killer"); JA lấy từ tiêu đề đã xuất bản (「ファセオンの殺人者」).

### 3.3 Sửa mã

- `.work/edition.py` → `EPISODES["24"]`: thêm khoá `"thumb_bg"`, rẽ nhánh `thumb` theo `EN`/`JA`/mặc định VI, khai `roles_en` + `roles_ja` (bản EN mặc định ghi *"Blanchard case file"* — thuộc tập khác).
- Bản sao lưu: `.work/_cu/plan_t24_20261125/` (3 file plan) — `edition.py` có bản sao trong `.work/_cu/`.
- Script dựng: `.work/_package_t24.py` (mux + thumbnail + thay mốc chương; **không** gọi `package.description()` vì lý do ở báo cáo hồ sơ §7).

## 4. Kết quả

| Bản | File | Dung lượng | Kích thước |
|---|---|---:|---|
| VI | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap24/xuat_ban/thumbnail.png` | 1 330 830 B | 1280×720 RGB |
| EN | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap24_EN/xuat_ban/thumbnail.png` | 1 330 496 B | 1280×720 RGB |
| JA | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap24_JA/xuat_ban/thumbnail.png` | 1 341 610 B | 1280×720 RGB |

Font: VI/EN = `segoeuib.ttf` (86 px) · JA = `YuGothB.ttc` (70 px) — cùng font/cỡ với Tập 20–23.

## 5. Kiểm tra đã chạy

| # | Kiểm tra | Kết quả |
|---|---|---|
| 1 | Nền sạch chữ (H2/H26) — soi full-res | **PASS** |
| 2 | Nền là của Tập 24, đúng chủ đề (H11) | **PASS** |
| 3 | 3 bản có 3 cặp chữ riêng, không trộn ngôn ngữ (A11 #148) | **PASS** |
| 4 | Font tiếng Nhật render đúng kanji (YuGothB.ttc) | **PASS** |
| 5 | Chữ đọc được ở cỡ hiển thị thật 320×180 | **PASS** |
| 6 | `provenance.json` +3 dòng, 0 dòng cũ bị đổi/xoá | **PASS** (6623 → 6626) |
| 7 | `thumbnail.png` nằm trong `.gitignore` (L10 — không commit media) | **PASS** |

## 6. Provenance

3 dòng mới cho `thumbnail.png` (VI/EN/JA) trong `provenance.json` — nền dùng chung `t24_a1_30_…` đã có dòng riêng từ 21/11/2026. Bản sao lưu trước khi ghi: `.work/_cu/provenance_t24_20261125/provenance.json`.

## 7. Việc còn lại cho người dùng

1. **Nghe duyệt chữ trên thumbnail** trước khi đăng — đặc biệt cặp JA 「記憶 / ファセオン」 (chữ do Pillow vẽ, không phải AI vẽ ⇒ H26 (f) đạt).
2. **Bản KO chưa có thumbnail** — Tập 24 không có bản KO trong phạm vi lần này.
3. Chưa commit (L10): `thumbnail.png` bị `.gitignore` loại; các file JSON/MD đang chờ duyệt.
