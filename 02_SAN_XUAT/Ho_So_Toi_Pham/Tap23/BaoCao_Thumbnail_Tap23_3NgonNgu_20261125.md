# Báo cáo dựng ảnh thumbnail Tập 23 — 3 ngôn ngữ (VI / EN / JA)

**Ngày:** 25/11/2026 · **Người thực hiện:** AI (MCode) · **Tập:** 23 — Hồ Sơ Richard Ramirez ('Night Stalker')

---

## 1. Yêu cầu

Đọc kịch bản Tập 23 + video đã dựng, tạo ảnh thumbnail (`thumbnail.png`, 1280×720) cho 3 ngôn ngữ.

## 2. Nguồn đã đọc

| Nguồn | Dùng để |
|---|---|
| `01_KICH_BAN/Ho_So_Toi_Pham/Tap23/kichban_tap23_23102026.md` | nội dung Hồi 1 (ngôi sao 5 cánh ngược tại hiện trường), Hồi 2 (cơn sốt Hybristophilia), tiêu đề tập |
| `01_KICH_BAN/Ho_So_Toi_Pham/Tap23_EN/kichban_tap23_EN.md` | bản EN — cụm "Night Stalker" + "Hybristophilia" |
| `01_KICH_BAN/Ho_So_Toi_Pham/Tap23_JA/kichban_tap23_JA.md` | bản JA — cụm 「ナイト・ストーカー」+「犯罪者愛好症」 |
| `02_SAN_XUAT/Ho_So_Toi_Pham/Tap23*/mo_ta.txt` | tiêu đề đã xuất bản (đối chiếu chữ thumbnail với tiêu đề thật) |
| `02_SAN_XUAT/Ho_So_Toi_Pham/Tap23/xuat_ban/Tap23_master.mp4` | soi khung hình thật (60 s, 300 s) để chọn nền đúng tông của tập |
| `assets/bg/t23_*.png` (213 ảnh) | chọn nền — đã soi montage + zoom full-res |

## 3. Quyết định

### 3.1 Nền thumbnail (H11 — nền và chữ của đúng tập)

**Chọn:** `assets/bg/t23_a2_19_psychological_signature_pentagram_wall.png`

Lý do: ngôi sao năm cánh ngược là **DẤU ẤN (signature)** thật của Richard Ramirez — hắn để lại tại hiện trường (kịch bản Hồi 1) và trong tư thế ở tòa (Hồi 2). Nền do Cloudflare Workers AI FLUX.1-schnell sinh ngày 20/11/2026, đã có dòng provenance riêng.

**Loại** (không dùng): `t23_a1_03_shadowy_figure_prowling_alley` (có chữ biển "LOS ANGELES"), `t23_a1_06_newspaper_headline_night_stalker` (chữ báo), `t23_a2_03_rockstar_aura_sunglasses_defense_table` (tháp Eiffel — sai bối cảnh LA).

### 3.2 Chữ trên thumbnail (A11 #148 — mỗi ngôn ngữ một cặp chữ riêng)

Trước khi sửa, `EPISODES["23"]["thumb"]` chỉ có **một** cặp chữ tiếng Việt ⇒ bản EN/JA sẽ in chữ "SAY MÊ KẺ ÁC" (đúng lỗi Tập 07/08 đã ghi ở TIEU_CHUAN #148).

| Ngôn ngữ | Dòng 1 | Dòng 2 |
|---|---|---|
| VI | `NIGHT STALKER` | `SAY MÊ KẺ ÁC` |
| EN | `NIGHT STALKER` | `HYBRISTOPHILIA` |
| JA | `ナイト・ストーカー` | `犯罪者愛好症` |

EN/JA lấy đúng 2 cụm từ nổi bật trong tiêu đề đã xuất bản của tập ("The 'Night Stalker' Terror & The Enigma of Hybristophilia" / 「ナイト・ストーカーの悪夢と犯罪者愛好症の深淵」).

### 3.3 Sửa mã

- `.work/edition.py` → `EPISODES["23"]`: thêm khoá `"thumb_bg"`, rẽ nhánh `thumb` theo `EN` / `JA` / mặc định VI.
- Bản sao lưu: `.work/_cu/edition.py.bak_t23_thumb_20261125_144136`
- Script dựng: `.work/_gen_thumb_t23.py` (chỉ gọi `package.thumbnail()`, **không** gọi `--mux` ⇒ không đụng mp4/mô tả tập đã xuất)

## 4. Kết quả

| Bản | File | Dung lượng | Kích thước |
|---|---|---|---|
| VI | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap23/xuat_ban/thumbnail.png` | 1 408 360 B | 1280×720 RGB |
| EN | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap23_EN/xuat_ban/thumbnail.png` | 1 420 583 B | 1280×720 RGB |
| JA | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap23_JA/xuat_ban/thumbnail.png` | 1 435 157 B | 1280×720 RGB |

Font: VI/EN = `segoeuib.ttf` (86 px), JA = `YuGothB.ttc` (70 px) — cùng font/cỡ với Tập 20–22.

## 5. Kiểm tra đã chạy

| # | Kiểm tra | Kết quả |
|---|---|---|
| 1 | `py_compile .work/edition.py` | **PASS** |
| 2 | Hồi quy Tập 01 (L9): `thumb`/`thumb_bg`/`OUT_DIR` không đổi | **PASS** |
| 3 | Tập 20/21/22/24/25 không đổi | **PASS** |
| 4 | Nền sạch chữ (H2/H26) — soi full-res | **PASS** |
| 5 | Đọc chữ ở kích thước hiển thị thật 320×180 | **PASS** |
| 6 | `provenance.json` hợp lệ, +3 dòng, 0 dòng cũ bị đổi/xoá | **PASS** |
| 7 | Không đụng mp4/mp3/wav/srt/mo_ta của Tap 23 (mtime không đổi) | **PASS** |
| 8 | `thumbnail.png` nằm trong `.gitignore` (L10 — không commit media) | **PASS** |

## 6. Provenance

3 dòng mới cho `thumbnail.png` (VI/EN/JA) trong `provenance.json` — nền dùng chung, đã có dòng riêng từ 20/11/2026.

## 7. Việc còn lại cho người dùng

1. **Bản KO chưa có thumbnail.** `01_KICH_BAN/.../Tap23_KO/kichban_tap23_KO.md` đã có kịch bản, nhưng `Tap23_KO/xuat_ban/` **chưa có** video (`Tap23_KO_master.mp4`) ⇒ chưa dựng thumbnail KO. Khi video KO dựng xong, thêm khoá `"thumb"` nhánh KO vào `EPISODES["23"]` rồi chạy lại `.work/_gen_thumb_t23.py` (thêm cặp `ko`).
2. **Nghe duyệt chữ trên thumbnail** trước khi đăng — đặc biệt cặp JA 「ナイト・ストーカー / 犯罪者愛好症」 (chữ do Pillow vẽ, không phải AI vẽ ⇒ H26 (f) đạt).
3. Chưa commit — `provenance.json` + `.work/edition.py` đang là thay đổi chờ duyệt; `thumbnail.png` bị `.gitignore` loại (L10).
