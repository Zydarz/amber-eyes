# TRẠNG THÁI SINH ẢNH NỀN TẬP 37/38/39 — đủ 445/445, cổng mapping đạt

> **Ngày:** 25/11/2026 (cập nhật 26/11/2026 ~14:25) · **Nguồn:** Cloudflare Workers AI FLUX.1-schnell (KHÔNG dùng Kaggle — user chốt 25/11)
> **Trạng thái:** **ĐỦ 445/445 ảnh** · `map_shot_anh.py --check` **ĐẠT cả 3 tập** · `qc_bg_mapping.py` **ĐẠT cả 3 tập**.
> 37 ảnh còn chữ AI đã sinh lại ở **vòng 3** (14:12–14:20, 26/11) — **user tự soi mắt kiểm tra**.

---

## 1. Kết quả (cập nhật 26/11)

| Tập | Shot | Ảnh đã có | Ảnh thiếu | Ảnh hỏng | Ảnh thừa | Cổng `--check` | `qc_bg_mapping` |
|---|---|---|---|---|---|---|---|
| 37 | 122 | **122** | 0 | 0 | 0 | **ĐẠT** | **ĐẠT** |
| 38 | 188 | **188** | 0 | 0 | 0 | **ĐẠT** | **ĐẠT** |
| 39 | 135 | **135** | 0 | 0 | 0 | **ĐẠT** | **ĐẠT** |
| **Tổng** | **445** | **445** | **0** | **0** | **0** | | |

- **445 ảnh**: đều hợp lệ (`PIL.verify()`), đúng **2112×1188**, đúng tên job ⇒ tự khớp shot (H25/H28).
- Mapping: **0 lỗi mapping**, bảng shot không cũ/lệch; M1 mã sai 0/122·0/188·0/135; M4 prompt riêng 100 %.
- `provenance.json`: đã gộp đủ 445 dòng t37–39, tổng **6.709 dòng**.

## 2. Ghi chú quota Cloudflare (đã qua)

Cloudflare Workers AI: **10.000 neurons/ngày/tài khoản**, reset lúc **00:00 UTC = 07:00 VN**.
6 tài khoản trong `.work/.cloudflare_accounts` → 60.000 neurons/ngày. 1 ảnh FLUX.1-schnell ≈ **166 neurons**
(≈ 60 ảnh/tài khoản/ngày).

- 25/11: 6/6 tài khoản cạn (HTTP 429 *"you have used up your daily free allocation"*) → dừng, đợi 26/11.
- 26/11 07:41–08:40: vẫn 429 hết (hạn mức cuộn 24h từ lần dùng đầu ~13:30 ngày 25/11, **không** reset 00:00 UTC).
- 26/11 13:34: quota mở lại → sinh nốt 130 ảnh thiếu + 47 ảnh lỗi (vòng 1).
- 26/11 14:12–14:20: quota còn 5/6 account (slot 1 cạn) → sinh lại 37 ảnh lỗi (vòng 3).

## 3. Lệnh chạy lại (nếu cần sinh thêm)

```powershell
# 1 tiến trình, dùng cả 6 account (tự failover khi 429):
py -3 .work/gen_images_cf_resume.py 37 38 39

# 3 tiến trình song song (mỗi tập 1 account khác nhau) — nhanh gấp ~2:
$env:AE_CF_SLOT="2"; py -3 .work/gen_images_cf_resume.py 37   # chạy nền
$env:AE_CF_SLOT="3"; py -3 .work/gen_images_cf_resume.py 38   # chạy nền
$env:AE_CF_SLOT="4"; py -3 .work/gen_images_cf_resume.py 39   # chạy nền
```

Script tự làm 2 việc:
1. **Ảnh thiếu** — job chưa có file hợp lệ ⇒ sinh mới.
2. **Ảnh lỗi QC** (danh sách trong `.work/_qc_flags_t37_39.json`) — sinh lại **cùng tên**.

Sau khi chạy xong: `py -3 .work/merge_prov_shards.py 37 38 39` để gộp provenance, rồi `py -3 .work/map_shot_anh.py --check 37` (38, 39).

## 4. 47 ảnh lỗi QC (AI vẽ chữ / lệch nghĩa)

Danh sách đầy đủ + lý do: `.work/_qc_flags_t37_39.json`

**Tập 37 (10):** a1_19 (chữ trên sách mở) · a2_05 (biển đèn CITY/GOLF) · a2_07 (thẻ giấy có chữ) ·
a2_22 (áp phích "PO") · a2_25 (biển số xe) · a3_25 (chữ AMBULANCE) · a4_09 (chữ trên biên bản) ·
a4_14 (chữ trên giấy A4) · a4_19 (chữ PROVINCIAL COURT) · a5_05 (chữ COURT trên vòm)

**Tập 38 (17):** a1_02 (DINER) · a1_05 (bảng thông báo) · a1_08 (biển số) · a1_10 (FOX SCREP) ·
a1_13 (chữ trên bản đồ) · a2_10 (HOTEL MOTEL) · a2_22 (tường hồ sơ) · a2_33 (MOTEL) · a2_36 (MOTEL lớn) ·
a3_08 (bảng hồ sơ) · a3_10 (chữ trên bản đồ) · a3_13/a3_14/a3_15 (biển PAWN SHOP, nặng) ·
a3_21 (MOTEL/VACANCY) · a3_31 (CONT… POLIC) · a3_33 (…ROAD FACING)

**Tập 39 (20):** a1_12 (chữ viết tay) · a1_19/a1_20 (biển tiếng Trung) · a1_22 (lệch nghĩa: 2 người ngồi) ·
a1_26 (SATE) · a2_02 (biển Hán tự lớn) · a2_08/a2_12/a2_14 (biển Hán tự) · a2_20 (chữ POLICE trên áo) ·
a2_23 (lệch nghĩa: mặt nạ) · a3_04 (nhiều biển Hán tự) · a3_13 (màn hình có chữ) ·
a4_01/a4_03/a5_03 (chữ Hán tự) · a4_15 (EXIT) · a4_16 (chữ trên giấy) · a4_17 (HARDWARE) · a5_10 (biển neon)

> **Ghi chú:** Tập 39 bối cảnh Trung Quốc nên FLUX hay vẽ chữ Hán tự lên biển hiệu dù negative đã cấm.
> Nếu sinh lại vẫn còn chữ → cân nhắc đổi prompt sang cảnh **không có biển hiệu** (chỉ đèn lồng, đèn neon
> trơn) thay vì chỉ thêm negative.

## 4b. Đã viết lại prompt 47 ảnh lỗi (26/11/2026, chưa tốn quota)

Thêm câu cấm chữ vào prompt KHÔNG hiệu quả với FLUX (nó vẫn vẽ chữ). Nguyên tắc mới:
**bỏ hẳn cơ hội để vẽ chữ** —
· cửa hệ / đèn neon → plain blank facade, closed shutters, no signboard
· chữ Hán tự (Tập 39) → paper lanterns without writing, plain cloth awnings, unmarked walls
· biển số xe → lank unreadable plate
· giấy tờ / bảng tin → completely blank unmarked surface
· thẻ tiền → plain notes with no printing

Đã ghi đè g_jobs_tap37/38/39.json (backup: .work/_cu/bg_jobs_tapXX_20261126_0845.json).
Mapping sau khi sửa: **vẫn 0 lỗi**, bảng shot không lệch (tên ảnh không đổi).

Script: .work/_rewrite_prompts_flags.py

## 4c. Vòng 2 & vòng 3 — xử lý 47 ảnh AI vẽ chữ (26/11/2026)

### Bài học rút ra (quan trọng, áp dụng cho các đợt sau)

| Cách thử | Kết quả |
|---|---|
| Thêm câu cấm chữ vào prompt (`no text, no lettering, no characters…`) | **Vô hiệu** — FLUX.1-schnell không tuân thủ negation, vẫn ra chữ (có khi còn nặng hơn vì "signage/no signage" kích hoạt đúng vật thể cần biển) |
| Vòng 1 (26/11 07:40): gỡ chữ khỏi prompt + thêm negative | 47 → **37 ảnh còn chữ** |
| Vòng 2 (26/11 13:40): đổi bối cảnh / crop sát, vẫn giữ câu negative | 37 ảnh → **~37 ảnh vẫn còn chữ** (cải thiện rất ít) |
| **Vòng 3 (26/11 14:12): bỏ hẳn mọi từ kích hoạt chữ + bỏ hẳn negation** | 37/37 sinh lại thành công — **chờ user tự soi mắt** |

⇒ **Quy tắc vàng cho FLUX**: không dựa vào negation; phải **loại bỏ khỏi khung hình mọi bề mặt có thể mang chữ** (biển, bảng, biển số, giấy tờ, màn hình, tiền, nhãn) và mô tả vật thể trơn (*blank / unmarked / plain / bare / featureless*). Tốt nhất là **chỉ giữ vật thể, bỏ hẳn ngữ cảnh có bảng hiệu**.

### Vòng 3 — 37 ảnh, kỹ thuật dùng

- Script viết prompt: `.work/_rewrite_prompts_r3.py` (backup job json: `.work/_cu/bg_jobs_tapXX_20261126_1412_r3.json`)
- Xoá `extra_negative` trong `.work/_qc_flags_t37_39.json` (để trống) — vì negation vô hiệu.
- Chạy 3 tiến trình song song, mỗi tập 1 account: `AE_CF_SLOT=2` (T37), `=3` (T38), `=4` (T39).
- Kết quả: **T37 7/7 · T38 11/11 · T39 19/19, 0 lỗi**, tổng 4.6 phút.
- Tờ soi mắt cho 37 ảnh vòng 3: `.work/qc_montage/regen_00.jpg` · `regen_01.jpg` · `regen_02.jpg` (đã build lại 14:2x).

---

## 5. File liên quan

| Việc | Đường dẫn |
|---|---|
| Script sinh (chạy tiếp) | `.work/gen_images_cf_resume.py` |
| Client Cloudflare FLUX (dùng chung) | `.work/flux_client.py` |
| Danh sách ảnh lỗi QC | `.work/_qc_flags_t37_39.json` |
| Job sinh ảnh (nguồn chuẩn) | `.work/bg_jobs_tap37.json` · `tap38` · `tap39` |
| Bảng shot | `02_SAN_XuAT/Ho_So_Toi_Pham/TapXX/Bang_Shot_Anh_TapXX.md` |
| Ảnh nền | `assets/bg/t37_*.png` (122) · `t38_*.png` (188) · `t39_*.png` (135) |
| Tờ soi mắt (đã soi 100 % vòng 1) | `.work/qc_montage/sheet_t37_00..03.jpg` · `sheet_t38_00..03` · `sheet_t39_00..04` |
| Tờ soi mắt vòng 3 (37 ảnh, chờ user soi) | `.work/qc_montage/regen_00.jpg` · `regen_01.jpg` · `regen_02.jpg` |
| Script viết prompt vòng 3 | `.work/_rewrite_prompts_r3.py` |
| Log sinh | `.work/_gen_cf_t37.log` · `_gen_cf_t38.log` · `_gen_cf_t39.log` + `_gen_cf_t37b/t38b.log` |
| Gộp provenance | `.work/merge_prov_shards.py` |

## 6. Việc đã dọn

- 2 kernel Kaggle đã push (`amber-eyes-flux2-t37-r1`, `-t38-r1`) đã **xoá**; watcher đã dừng.
  **Không có ảnh nào của Kaggle lọt vào `assets/bg/`** — toàn bộ 445 ảnh đều do Cloudflare sinh.
- 1 file PNG bị cắt cụt (do dừng tiến trình giữa chừng) đã được phát hiện và sẽ tự sinh lại
  (script skip có `PIL.verify()`).
- `provenance.json` vẫn còn các dòng cũ trỏ tới file đã xoá (T37: 148 dòng klein cũ; T38: 146; T39: 152) —
  giữ làm lịch sử theo báo cáo 25/11, **chưa dọn**.

## 7. Rủi ro còn lại

- Thời lượng shot trong bảng vẫn là **ước lượng** (chưa có audio) ⇒ chưa tách shot dài.
- Tập 64/66/68 chưa lập mapping (kịch bản chưa mở rộng) — không liên quan đợt này.

