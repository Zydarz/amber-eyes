# Báo cáo H2 — Higgs Audio v3 · pilot 96 bản · Tập 02

**Ngày:** 30/10/2026 · **Cổng:** H2 (so sánh với MiniMax) — **trạng thái: ĐẠT có điều kiện**
**Tài liệu chuẩn:** `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` §5–§9 · `AGENTS.md` G8–G13, Q1–Q6
**Số đo thô:** `.work/kaggle_higgs/cer_pilot_rows.json` (96 dòng, có 2 bản chép ASR/câu)
`.work/kaggle_higgs/cer_pilot_rows_fixed.json` (CER sau khi chuẩn hóa 2 vế)

---

## 1. Môi trường (đo thật trên Kaggle, kernel v3)

| Mục | Giá trị đo được |
|---|---|
| Model | `bosonai/higgs-tts-3-4b` (trọng số gốc) + 2 file loader từ `multimodalart/higgs-audio-v3-tts-4b-transformers` + `auto_map` tự thêm |
| transformers / torch | 5.22.0 / 2.11.0+cu128 |
| GPU | Tesla T4 15,6 GB (sm_75) · **bf16 có** (`torch.cuda.is_bf16_supported()` = True) |
| Lớp model | `HiggsMultimodalQwen3ForConditionalGeneration` |
| `num_codebooks` | 8 |
| Frame-rate bộ giải mã | **25,02 Hz** → `max_new_tokens = int(47,5 × 25,02) + 8 = 1196` |
| VRAM đỉnh | 9,94 GB |
| RTF | trung bình **2,15** (max 2,98) |
| Kết quả sinh | **96/96 OK**, 0 lỗi · tổng 1522,6 s sinh |
| Xuất | WAV 24 kHz mono PCM16, fade 30 ms, **không** chuẩn hóa loudness, **không** mp3 |

**H1 §5 (thẻ `<|…|>`): ĐẠT.** Đo bằng `listen_audio` trên `plain_vi_emotiontag.wav` vs `plain_vi_neutral.wav` —
bản chép **không** chứa từ khóa thẻ (`emotion`/`sadness`/`fear`/`prosody`/`pause`). Cảnh báo "emotion" trong
script đầu là false-positive do **tên file**.

**Phát hiện phụ (quan trọng):** không truyền `reference_audio` → đọc sai thanh điệu nặng
("Trở lại đan" thay vì "Trò tôi đan"). ⇒ **bắt buộc clone** (đúng cảnh báo §4).

---

## 2. LỖI PHÉP ĐO ĐÃ TÌM RA VÀ SỬA (Q3a)

Lần đo đầu cho CER rất cao (H t=0,7 → 12,38%; D t=0,7 → 4,98%). Nguyên nhân **không phải TTS** —
mà là **lỗi chuẩn hóa 1 vế**, đúng bẫy đã ghi ở `AGENTS.md` Q3(a):

* `tts_sentences.py:105` gửi **số → chữ** cho TTS ⇒ TTS nói *"hai nghìn không trăm lẻ chín"*.
* ASR (`listen_audio`) trả **chữ số** ⇒ *"2009"*.
* Script đo chỉ áp `vi_numbers()` cho **một** vế ⇒ mọi câu có số bị phình lỗi giả.

Hai lỗi kèm theo:

1. `vi_numbers()` bản rút gọn trong script đo chia nhóm 3 chữ số sai ⇒ `"2009"` → *"two nine"*.
   Đã thay bằng **đúng** `vi_number()` của `tts_sentences.py` (xử lý nghìn/triệu/tỷ, "mốt"/"tư"/"lăm").
2. Số đo **MiniMax** cũng bị phình theo đúng lỗi này ⇒ phải tính lại MiniMax mới so sánh công bằng.

> **Cùng một lỗi đo đã làm cho cả hai hệ thống "trông tệ" giống nhau.** Chỉ sau khi sửa cả hai vế
> mới biết ai thực sự tốt hơn.

---

## 3. CER — Higgs (96 bản, 2 lượt ASR/câu, lấy lượt **xấu hơn**)

| Vai | Clip | Temp | n | CER tb | CER max | >2% | F0 (AC gốc) | F0 (pp2) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **H** | H.wav | 0,6 | 8 | 1,29% | 7,14% | 2/8 | 128 Hz | 124 Hz |
| **H** | H.wav | 0,7 | 8 | 2,48% | 7,46% | 3/8 | 130 Hz | 123 Hz |
| **H** | H.wav | **0,8** | 8 | **0,00%** | **0,00%** | **0/8** | 131 Hz | 127 Hz |
| **D** | D.wav | 0,6 | 8 | 3,29% | 9,38% | 5/8 | 120 Hz | 123 Hz |
| **D** | D.wav | 0,7 | 8 | **0,99%** | 5,21% | 1/8 | 123 Hz | 127 Hz |
| **D** | D.wav | **0,8** | 8 | 2,27% | 9,38% | 3/8 | 118 Hz | 122 Hz |
| **C** | C.wav | 0,6 | 8 | 1,01% | 8,06% | 1/8 | 203 Hz | 193 Hz |
| **C** | C.wav | 0,7 | 8 | 0,88% | 4,84% | 1/8 | 207 Hz | 197 Hz |
| **C** | C.wav | **0,8** | 8 | **0,00%** | **0,00%** | **0/8** | 205 Hz | 192 Hz |
| N1 | W1.wav | 0,7 | 4 | **1,08%** | 3,23% | 1/4 | 245 Hz | 229 Hz |
| N1 | W2.wav | 0,7 | 4 | 2,86% | 6,59% | 2/4 | 197 Hz | 190 Hz |
| N1 | W3.wav | 0,7 | 4 | 4,25% | 7,53% | 3/4 | 158 Hz | 150 Hz |
| **N2** | **W1.wav** | 0,7 | 4 | **0,63%** | 2,53% | 1/4 | 276 Hz | 256 Hz |
| N2 | W2.wav | 0,7 | 4 | 1,27% | 5,06% | 1/4 | 207 Hz | 194 Hz |
| N2 | W3.wav | 0,7 | 4 | 1,58% | 6,33% | 1/4 | 165 Hz | 156 Hz |

*"pp2" = phương pháp F0 thứ 2 (AC chuẩn hóa + nội suy parabol + sửa lỗi octave) dùng để kiểm chéo.*

### 3.1 MiniMax — TÍNH LẠI cùng chuẩn hóa (32 câu pilot)

| Vai | n | CER tb | CER max | >2% |
|---|---:|---:|---:|---:|
| C | 8 | 0,00% | 0,00% | 0/8 |
| D | 8 | 1,72% | 5,69% | 3/8 |
| H | 8 | 0,89% | 7,14% | 1/8 |
| N1 | 4 | 0,00% | 0,00% | 0/4 |
| N2 | 4 | 0,00% | 0,00% | 0/4 |

*(Trước khi sửa Q3a, MiniMax bị ghi nhầm là H 10,79% / D 5,60%.)*

### 3.2 So sánh từng câu (cấu hình đề xuất)

| Vai | Cấu hình | Higgs | MiniMax | H2 |
|---|---|---:|---:|---|
| H | H.wav, t=0,8 | **0,00%** | 0,89% | **ĐẠT** |
| C | C.wav, t=0,8 | **0,00%** | 0,00% | **ĐẠT** |
| D | D.wav, t=0,8 | 2,27% | 1,72% | trượt (xử lý bằng đa bản §7) |
| N1 | W1.wav, t=0,7 | 1,08% | 0,00% | trượt (nhẹ) |
| N2 | W1.wav, t=0,7 | 0,63% | 0,00% | trượt (nhẹ) |

Câu lỗi còn lại ở cấu hình đề xuất: `D 2.05#15` 3,79% · `D 2.05#16` 3,39% · `D 1.17#5` 9,38%
(bản MiniMax cùng câu: 5,69% / 3,39% / 0,00%) · `C 3.05#3` ASR bị chặn 1 lượt.

---

## 4. G9 — tách bạch giọng (F0 trung vị của **audio đã clone**, không phải clip gốc)

| Cặp | Higgs (đã clone) | MiniMax (cũ) | Ngưỡng | Kết luận Higgs |
|---|---:|---:|---:|---|
| **H ↔ D** | **0,23 nửa cung** (124,3 vs 122,6 Hz) | 5,54 nc | ≥ 4 nc | ❌ **TRƯỢT** |
| C ↔ N1 (W1) | 2,98 nc | 3,07 nc | ≥ 4 nc | ❌ trượt |
| C ↔ N1 (W2) | 0,19 nc | — | ≥ 4 nc | ❌ trượt |
| C ↔ N1 (W3) | 4,34 nc | — | ≥ 4 nc | ✅ đạt *(nhưng CER 4,25%)* |
| **C ↔ N2 (W1)** | **4,97 nc** | 1,78 nc | ≥ 4 nc | ✅ **đạt** |
| C ↔ N2 (W2) | 0,11 nc | — | ≥ 4 nc | ❌ trượt |
| C ↔ N2 (W3) | 3,63 nc | — | ≥ 4 nc | ❌ trượt |
| H/D ↔ N1/N2 | 7,36–7,92 nc | — | ≥ 4 nc | ✅ đạt |

**Kiểm chéo 2 thuật toán:** `f0_median` (AC thô, `voice_audition.py`) và AC chuẩn hóa + sửa octave cho
H↔D lần lượt **1,12** và **0,23** nửa cung ⇒ **H và D gần như trùng nhau là thật**, không phải lỗi đo.

### 4.1 Cơ chế: Higgs **không** giữ F0 của clip tham chiếu

| Vai | F0 clip gốc | F0 audio clone (pp2) | Lệch |
|---|---:|---:|---:|
| H | 107 Hz | 124 Hz | **+16%** |
| D | 132 Hz | 123 Hz | **−7%** |
| C | 200 Hz | 192 Hz | −4% |
| N1 ← W1 | 235 Hz | 229 Hz | −3% |

H và D **trôi ngược chiều vào cùng một vùng ~123 Hz** ⇒ tự chúng không tách được, dù clip gốc cách nhau 25 Hz.

**Kết luận:** với 7 clip VoxCPM2 VI hiện có, **không thể đạt G9 cho H↔D**:
đổi sang clip có F0 cao nhất (W3, 162 Hz) thì audio clone chỉ về ~150 Hz ⇒ H↔D ≈ 3,3 nc, **vẫn dưới 4**.
Cần một clip tham chiếu **mới** có F0 thấp hơn (cho H) hoặc cao hơn (cho D).

---

## 5. Kiểm file theo §8

| Mục | Kết quả | Yêu cầu | Kết luận |
|---|---:|---:|---|
| Số file sinh | 96/96 OK | 100% | ✅ |
| Thời lượng > 47 s | **2** (`2.05#14` t0,6 · `2.05#15` t0,7 — cả hai 47,56 s) | 0 | ❌ cần xử lý |
| Thời lượng < 0,5 s | 0 | 0 | ✅ |
| Đỉnh > −1,5 dBFS | 33/96 | — | ⚠ loudnorm 2-pass ở bước mix sẽ xử lý |
| Câu lỗi > 2% | xem §3 | 0 ở H4 | ⚠ cần đa bản §7 |

---

## 6. Kết luận H2

### Chốt được (bằng số đo thật)

1. **temperature = 0,8 cho H và C** — CER **0,00%**, 8/8 câu sạch ở cả hai vai.
2. **temperature = 0,8 cho D** (không dùng 0,7): 0,7 cho CER tb thấp hơn (0,99%) nhưng sinh **runaway**
   (`2.05#15` = 47,56 s) và `2.05#16` = 32,6 s (âm tiết/s 0,40 ⇒ thoái dạng); 0,8 cho thời lượng ổn định.
   D còn 3 câu > 2% ⇒ dùng **3 bản/câu** theo §7 để chọn bản tốt nhất.
3. **N2 ← W1** — CER 0,63% **và** G9 4,97 nc ⇒ **lựa chọn duy nhất đạt cả hai**.
4. **Higgs tốt hơn MiniMax rõ rệt ở vai H** (0,00% vs 0,89%; câu `1.03#1` 0,00% vs 7,14%).

### Chưa chốt — cần quyết định của người dùng

| # | Vấn đề | Số đo | Lựa chọn |
|---|---|---|---|
| **1** | **G9 H↔D** | 0,23 nc (cần ≥ 4) | (a) tạo clip VoxCPM2 VI mới: nam rất trầm ~80 Hz cho H, **hoặc** nam ~170 Hz cho D · (b) dùng clip MiniMax làm tham chiếu (cần xác nhận điều khoản) · (c) ghi nhận vi phạm G9 |
| **2** | **G9 N1** | W1: CER ✅ 1,08% nhưng G9 2,98 nc ❌ · W3: G9 ✅ 4,34 nc nhưng CER 4,25% ❌ | (a) tạo clip nữ mới F0 ~270 Hz · (b) chấp nhận N1 ở 2,98 nc (bằng MiniMax hiện tại) · (c) đổi N1 ← W3 (sai giới tính — không khuyến nghị) |
| **3** | **Ghi công Boson** (H0) | Creator Use Grant II-A cho phép thương mại | Xác nhận chấp nhận ghi "This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio" trong mô tả mọi tập |

### Đang chạy

**Pilot v4** (kernel `chiduong2026/amber-eyes-higgs-v4-tts-kaggle-gpu`, dataset v3) — 104 bản, **chỉ đo, không gán vai** (L4):

* **A)** F0 thật của audio clone khi đổi clip tham chiếu H/D sang **W3** và **W4** ⇒ trả lời dứt điểm vấn đề #1 bằng đo thay vì suy đoán.
* **B)** 3 biến thể seed cho **D** (t=0,7 và t=0,8), **N1**, **N2** theo §7 ⇒ kiểm chọn-bản-tốt-nhất có kéo D/N1/N2 về CER < 2% không.

---

## 7. Lỗi hệ thống khác đã phát hiện (đã sửa & commit)

* **~273 file** trong repo hardcode `D:\TEST\Gax\Audi` (thư mục không tồn tại) ⇒ **toàn bộ pipeline Tập 02 crash ngay dòng đầu**.
  Đã sửa bằng `Path(__file__).resolve().parents[N]`. Verify: 801/801 file `.py` compile sạch, 12/12 script import OK.
  Commit: `1e79241`, `1b3cba4`.
* Bài học: `Path(x).parent/..` **không** phải cú pháp Python hợp lệ; script sửa hàng loạt phải khớp **đúng** mẫu `Path(r"D:\TEST\Gax\Audi…")` và không đụng `.resolve().parent` dạng đúng.
* `kaggle kernels output` **không** có `--file-pattern` ở bản CLI cũ ⇒ watcher v1 đã tải 10 GB thư mục model. Luôn dùng `--file-pattern`.

---

## 8. Tệp dữ liệu tham chiếu

| Nhóm | Tệp |
|---|---|
| Số đo thô (96 dòng, 2 bản chép/câu) | `.work/kaggle_higgs/cer_pilot_rows.json` |
| Số đo sau chuẩn hóa 2 vế | `.work/kaggle_higgs/cer_pilot_rows_fixed.json` |
| Bảng báo cáo (bản đầu, có lỗi Q3a) | `.work/kaggle_higgs/cer_pilot_report.md` |
| MiniMax (32 câu, cache bản chép) | `.work/kaggle_higgs/cer_minimax_pilot_rows.json` |
| F0 MiniMax toàn tập (203 câu) | `.work/kaggle_higgs/f0_minimax_t02.json` |
| Kiểm chéo F0 2 thuật toán | `.work/kaggle_higgs/_f0_crosscheck.txt` |
| So sánh H2 công bằng | `.work/kaggle_higgs/_h2_fair.txt` |
| Manifest kernel v3 | `.work/kaggle_higgs/out_higgs_v3/out_higgs/higgs_manifest.json` |
| Payload Tập 02 (203 câu) | `.work/kaggle_higgs/higgs_payload_t02.json` |
