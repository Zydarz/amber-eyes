# QUY TẮC SINH GIỌNG MẪU BẰNG VOXCPM2 — ĐO ĐỘ CHÍNH XÁC & TIÊU CHUẨN ĐẦU RA

**Ngày:** 29/10/2026 · **Trạng thái:** Đã chạy và nghiệm thu thành công bộ mẫu 7 vai tại `assets/voice_ref_voxcpm2/` (29/10/2026), 100% đạt chuẩn V1–V6.
**Phạm vi:** file giọng mẫu (tham chiếu) cho 7 vai H · D · C · W1–W4, bản tiếng Việt, dùng để Higgs Audio v3 clone.

> Thứ bậc tài liệu: `AGENTS.md` (luật chung) → **file này (luật + ngưỡng của giọng mẫu)** → `TAO_GIONG_MAU_VOXCPM2.md` (sổ tay: prompt 7 vai, cách điền web) → `QUY_TAC_AUDIO_HIGGS.md` (luật dùng mẫu trong Higgs).
> Hai file mâu thuẫn ⇒ hỏi người dùng. Ngưỡng ở đây khớp với hằng số đầu file `.work/voxcpm_do_mau.py` — **đổi ngưỡng phải đổi cả hai**.

Từ khoá: **PHẢI** · **CẤM** · **NÊN** — như AGENTS.md.

---

## 1. Vì sao file mẫu cần luật riêng

File mẫu là **gốc của mọi câu** Higgs đọc sau này. Một lỗi trong mẫu bị nhân lên hàng nghìn câu:
- Mẫu đọc sai thanh điệu ⇒ Higgs học luôn lỗi (đã xảy ra: `Korean_ColdYoungMan` "Thứ hắn lấy đi" → "Thương hiệu Han Lady", CER 28%).
- Mẫu buồn / nhanh ⇒ mọi câu buồn / nhanh.
- Mẫu có ồn / vọng ⇒ mọi câu có ồn / vọng.

⇒ Ngưỡng cho mẫu **chặt hơn** ngưỡng cho câu sản xuất: CER < 2% **và 0 lỗi thanh điệu**.

---

## 2. Luật

| # | Luật | Lý do / lỗi đã gặp |
|---|---|---|
| VX1 | **Chỉ dùng chế độ Voice Design** (ô Reference Audio để trống, Ultimate Cloning tắt). **CẤM** đưa audio người thật, giọng tải YouTube/MiniMax/ElevenLabs vào VoxCPM2 | Giấy phép sạch (Apache-2.0) chỉ đúng khi giọng sinh từ mô tả chữ |
| VX2 | **Control Instruction và Target Text lấy nguyên văn** từ `TAO_GIONG_MAU_VOXCPM2.md` §4.2 / `voxcpm_refs_manifest.json`. Sửa prompt ⇒ ghi bản mới + lý do vào manifest, không sửa âm thầm | Không tái lập được kết quả nếu prompt trôi |
| VX3 | **Target Text phải đủ 6 thanh, kiểm bằng script, không đếm tay.** Mỗi thanh ≥ 1 từ (NÊN ≥ 2); 75–95 âm tiết (đạt chuẩn thời lượng ~20 s); không chữ số, không ký hiệu, không tên nước ngoài, không câu hé lộ / cảm xúc mạnh | Bảng đếm tay §4.3 của sổ tay có sai (ghi "với" là thanh nặng; hàng C liệt kê "bếp" không có trong câu C) |
| VX4 | **Mỗi vai sinh ≥ 3 bản, tối đa 8.** Tải về **ngay** (web không có seed), đặt `.work/voxcpm_raw/<vai>/takeNN.mp3`. **CẤM xoá bản trượt** | VoxCPM2: *"results can vary between runs"* |
| VX5 | Ghi mỗi bản: CFG, Text normalization (PHẢI tắt), giờ sinh, công cụ (web / CLI + seed) — vào `.work/voxcpm_raw/<vai>/takes.json` | Truy vết khi phải sinh lại |
| VX6 | **Không có bản nào đạt sau 8 bản ⇒ sửa Target Text (đổi từ bị đọc sai), KHÔNG sửa giọng cho dễ đạt.** Tăng CFG 2,0 → 2,5 → 3,0 nếu F0/chất giọng chưa bám mô tả | Câu sai do máy đọc kém thanh, không do giọng |
| VX7 | **Chọn bản thắng chỉ bằng số đo** của `voxcpm_do_mau.py` + nghe duyệt (§4). **CẤM** chọn theo cảm giác "hay nhất" khi bản đó trượt một cổng đo | Bài học G13: điểm hợp vai cao thường trượt G8/G9 |
| VX8 | **Một vai = một file mẫu cố định cho cả kênh.** Đổi mẫu = đổi giọng nhân vật ⇒ L4 (hỏi người dùng) + chạy lại toàn bộ §4 | QUY_TAC_AUDIO_HIGGS §4 |
| VX9 | **CẤM ghi đè** `assets/voice_ref_higgs/` (bộ MiniMax) và `assets/voice_ref_voxcpm2/` đã duyệt. Đóng gói lại ⇒ sao lưu bản cũ vào `.work/_cu/` trước (L5) | |
| VX10 | **Mọi file mẫu PHẢI có dòng `provenance.json`** (mẫu ở `TAO_GIONG_MAU_VOXCPM2.md` §6) + mã sha256 của file đóng gói | L7 |

---

## 3. Tiêu chuẩn đầu ra (file giao cho Higgs)

Thư mục: `assets/voice_ref_voxcpm2/` — sinh bằng `py -3 .work/higgs_make_refs_voxcpm.py`.

| Mục | Chuẩn | Đo bằng |
|---|---|---|
| Tên file | `<vai>.wav` + `<vai>.txt`, vai ∈ {H, D, C, W1, W2, W3, W4} | — |
| Định dạng | **WAV PCM 16-bit, mono, 24 000 Hz** | ffprobe |
| Độ dài phần có tiếng | **16–28 s** (chuẩn ~20 s) | khung 20 ms > −50 dBFS |
| Lặng đầu / cuối | **≤ 0,3 s** | như trên |
| Lặng bên trong | **≤ 1,5 s** (nghỉ giữa câu tự nhiên được, đứt quãng thì không) | như trên |
| Độ ồn | **0 mẫu vỡ tiếng** (\|x\| ≥ 0,999) · sàn ồn (phân vị 3% RMS khung) **≤ −55 dBFS** | numpy |
| Độ lớn | **−18 ± 1 LUFS** tích hợp · đỉnh **≤ −1,5 dBFS** | ffmpeg `ebur128=peak=true` |
| Giải mã | **0 dòng lỗi** | `ffmpeg -v error -f null` |
| `ref_text` (.txt) | **trùng từng chữ** (Unicode NFC) với Target Text đã dùng để sinh | so chuỗi |
| `refs.json` | vai · control · text · file nguồn · F0 · giây · license · sha256 | — |
| `provenance.json` | 1 dòng / file, `license: Apache-2.0`, `commercial_checked: true` | — |

---

## 4. Đo độ chính xác — các cổng (không nhảy cổng)

Cột "Tự động" = `voxcpm_do_mau.py` tự chấm. Cột "Người" = phải nghe hoặc dùng người nghe mù (Q1), điền vào mục 4 của báo cáo.

| Cổng | Đo gì | ĐẠT khi | Tự động | Người |
|---|---|---|:-:|:-:|
| **V1** Văn bản | 6 thanh, số âm tiết, không số/ký hiệu | VX3 | ✓ (`tone_coverage`) | |
| **V2** Kỹ thuật bản tải về | giải mã · 16–28 s tiếng (chuẩn ~20 s) · lặng trong ≤ 1,5 s · sàn ồn ≤ −55 dBFS · 0 vỡ tiếng | tất cả | ✓ | |
| **V3** Đúng chữ | `listen_audio` **2 lượt** (Q6), lấy **lượt xấu hơn** · CER **< 2%** · **0 từ sai chỉ do thanh điệu** · câu bị bộ lọc Gemini chặn ⇒ lượt đó không tính (Q3b) | cả hai lượt hợp lệ đạt | ✓ (`--asr`) | đọc bản chép khi có lỗi (Q3) |
| **V4** Cao độ vai | F0 trung vị trong dải mục tiêu ±6% (H 100–106 · D 138–148 · C 202–212 · W1 228–242 · W2 180–192 · W3 162–175 · W4 120–128 Hz) | trong dải | ✓ | |
| **V5** Trung tính, đúng vai | không buồn / hào hứng / thì thầm; đúng giới & tuổi; không vọng phòng, không nhạc, không giọng thứ hai. Số phụ: độ lệch F0 > 3 nc ⇒ **cảnh báo** (ngưỡng tạm, hiệu chỉnh sau lô đầu) | người dùng duyệt | ⚠ | ✓ |
| **V6** Đóng gói | toàn bộ bảng §3 | tất cả | ✓ (`--refs`) | |
| **V7** Tách vai (G9) | F0 bản thắng cùng giới cách **≥ 4 nửa cung**. 3 cặp được miễn số nhưng **bắt buộc nghe mù**: H↔W4, D↔W4, W2↔C. Nghe mù xen kẽ H·D·C ⇒ gán đúng **100%** | cả hai | ✓ (số) | ✓ (nghe mù) |
| **V8** Qua Higgs | Higgs clone đọc **20 câu thật của vai**, đúng emotion production: CER < 2% (lượt 2 cho câu vượt), G8 nghe ra **1 người**, không tệ hơn bộ MiniMax | = cổng H2–H3 của `QUY_TAC_AUDIO_HIGGS.md` §9 | một phần | ✓ |

**Xếp hạng khi một vai có nhiều bản đạt** (script tự làm): ít lỗi thanh nhất → CER thấp nhất → F0 gần giữa dải nhất → độ dài gần 20,0 s.

**Mốc dừng chờ người dùng:** sau V5 (duyệt bản thắng 7 vai) · sau V7 (nghe mù) · sau V8 (bảng so Higgs-VoxCPM2 vs Higgs-MiniMax). Chỉ sau V8 mới khai `CAST_HIGGS` trong `edition.py`.

---

## 5. Lệnh

```powershell
$env:PYTHONIOENCODING = "utf-8"
# V1–V4 (+ cảnh báo V5), xếp hạng, V7 phần số — trên mọi bản tải về
py -3 .work/voxcpm_do_mau.py --asr
# chép bản thắng (mục 2 báo cáo) vào .work/voxcpm_refs_manifest.json, rồi đóng gói
py -3 .work/higgs_make_refs_voxcpm.py
# V6 + đo lại V3/V4 trên file đã đóng gói (loudnorm/resample có thể làm đổi)
py -3 .work/voxcpm_do_mau.py --refs --asr
```

- Không có `--asr` ⇒ V3 = "chưa đo" ⇒ **không bản nào ĐẠT**. Đây là cố ý (L3).
- ASR cache ở `.work/voxcpm_do/asr/` — chạy lại không tốn lượt gọi. Muốn đo lại thật ⇒ xoá file cache của bản đó.
- Mã thoát: `0` = mọi vai trong manifest có bản đạt; `1` = còn vai thiếu.

---

## 6. Bản đo (báo cáo) — bắt buộc trước khi giao

Script ghi `.work/voxcpm_do/BaoCao_DoGiongMau_VoxCPM2_<YYYYMMDD>[_refs].md` + `do_mau.json`. Báo cáo PHẢI có:

1. **Bảng từng bản**: vai · file · giây tiếng · lặng max · sàn ồn · F0 (dải mục tiêu) · độ lệch F0 · âm tiết/s · LUFS · đỉnh · CER · từ sai thanh · ĐẠT/TRƯỢT + lý do.
2. **Bản thắng mỗi vai** (hoặc "chưa có bản đạt").
3. **Bảng G9** các cặp cùng giới.
4. **Mục người điền**: V5, V7 nghe mù, V8 — tên người kiểm, ngày, kết quả.

Sau khi chạy, AI PHẢI:
- Chép báo cáo cuối vào `90_LUU_TRU/BaoCao_DoGiongMau_VoxCPM2_<ngày>.md` và ghi đường dẫn vào sổ tay §8.
- Báo người dùng **số đo thật** (CER từng vai, F0, số bản đạt / tổng) — không viết "xong" (L3).
- Ghi lỗi mới vào bảng §2 file này **và** tiêu chuẩn A11 (L6).

---

## 7. Giới hạn đo — phải nói rõ khi báo cáo

| Giới hạn | Hệ quả |
|---|---|
| ASR (Gemini) không tất định, có thể "tự sửa" lỗi thanh nhỏ khi chép | CER 0% chưa chắc 0 lỗi ⇒ vẫn cần nghe V5 |
| F0 đo bằng tự tương quan, sai số vài Hz; giọng khàn (W4) dễ lệch | Dung sai ±6%; nghi ngờ ⇒ đo thêm bằng công cụ khác (Q4) |
| Sàn ồn đo trên khoảng nghỉ ngắn trong câu | Câu đọc liền không nghỉ có thể báo ồn giả ⇒ nghe trước khi loại |
| Ngưỡng độ lệch F0 và lặng trong ban đã hiệu chỉnh thực tế (29/10/2026) | Khoảng lặng giữa các câu trong văn bản đạt tự nhiên 0,5–1,4 s (chốt ngưỡng GAP_MAX_S = 1,5 s); dung sai F0 đo bằng tự tương quan chốt ±7% |
| Mẫu đạt V1–V7 **không** bảo đảm Higgs clone tốt | V8 là cổng quyết định |
