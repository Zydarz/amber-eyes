# QUY TẮC TẠO AUDIO BẰNG HIGGS AUDIO v3 — bản 4 (31/10/2026)

> Dành cho mọi AI làm audio kênh Amber eyes bằng Higgs. Đọc cùng `AGENTS.md`. Khi engine là Higgs, file này **thay mục 4 (Giọng đọc) và T2, T8, T9** của AGENTS.md.
> Bản 3 viết lại từ kinh nghiệm dựng **Tập 02** bằng Higgs (29–31/10/2026): 10 lượt chạy thử, 2 lượt sản xuất, 1 vòng 2. Mỗi luật có lý do là **một lỗi đã thật sự xảy ra**, kèm số đo.
> **Bản 4** thêm kinh nghiệm dựng **Tập 03** (cả tập + 2 vòng sửa, 31/10/2026) và quy trình chạy cho tập bất kỳ (§7, §14). Bản 3: `.work/_cu/QUY_TAC_AUDIO_HIGGS_v3_20261031.md`.
> Bản trước nữa (MLX/Mac + nhật ký đo): `.work/_cu/QUY_TAC_AUDIO_HIGGS_v2_20261030.md`. Số đo đầy đủ: `90_LUU_TRU/BaoCao_H2_Higgs_Pilot_Tap02_20261030.md`, `90_LUU_TRU/BaoCao_DoGiongMau_DC_20261030.md`, `02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md` Phụ lục C.

Từ khoá: **PHẢI** · **CẤM** · **NÊN** — như AGENTS.md.

---

## 0. Tóm tắt 1 phút

| # | Luật quan trọng nhất | Lỗi đã gặp |
|---|---|---|
| 1 | **Đo trên bản Higgs đã đọc, không đo trên giọng mẫu.** Giọng mẫu nghe khác nhau ≠ bản đọc khác nhau | `H.wav` 108 Hz và `D.wav` 128 Hz → Higgs đọc ra 130 và 124 Hz (0,22 nửa cung) |
| 2 | **G9 xét MỌI cặp vai đứng liền nhau, kể cả khác giới** | D (nam) ← `M_HIGH` 192 Hz → Higgs đọc 193 Hz, cách C (nữ) 1,03 nửa cung → người nghe nhầm D với C. G9 cũ chỉ xét cùng giới nên lọt |
| 3 | **CẤM mọi thẻ `<|emotion:…|>`** | `sadness`/`surprise` làm giọng nam vọt ~1 quãng tám: Host câu buồn 203–228 Hz (nghe như nữ) |
| 4 | **Giọng nam: chỉ dùng giọng mẫu ≤ 96 Hz hoặc chấp nhận vùng ~125 Hz** — Higgs kéo giọng nam trung (105–130 Hz) về ~125 Hz | Chỉ được **một** vai nam ở vùng ~125 Hz |
| 5 | **CẤM chỉnh cao độ giọng mẫu bằng xử lý tín hiệu** (phase vocoder, TD-PSOLA, sox…) | Giọng mẫu đọc ASR 0% nhưng Higgs clone ra CER 8–12%, sai nội dung |
| 6 | **Mỗi câu ≥ 2 bản, chọn bản theo CER + loại bản lệch cao độ**, rồi vòng 2 cho câu trượt | 29 → 12 câu > 2% sau vòng 2; lượt chọn đầu từng lấy nhầm bản lệch cao độ khi hoà CER |
| 7 | **Chuyển cache ASR cũ trước khi đo lượt mới** — cache đặt theo tên file | File Host lượt mới trùng tên lượt cũ → sẽ lấy bản chép của audio cũ |
| 8 | **Kịch bản đổi số câu ⇒ mọi file khoá theo mã câu phải chuyển theo NỘI DUNG** (acting, sfx, tts_manifest) | Tập 03: Higgs đọc câu 5.02#12 thành câu khác, 2.06#2 đọc lại câu cũ vi phạm V9 — CER **không** bắt được |
| 9 | **Ưu tiên giữ đúng 3 giọng chính (H, D, C).** Vai phụ N1/N2 dùng bộ giọng chung, không ép theo giới tính kịch bản (người dùng chốt 31/10/2026) | Tập 03: N1 giọng nữ đọc lời cảnh sát nam — người nghe có lúc tưởng D đổi giọng; người dùng chấp nhận |

---

## 1. Phạm vi và trạng thái

- **Engine sản xuất:**
  - **Trên Cloud (Kaggle GPU):** Higgs Audio v3 (`bosonai/higgs-tts-3-4b`, trọng số gốc) chạy trên Kaggle GPU (2 × Tesla T4, transformers) theo quy trình file này.
  - **Trên Mac Apple Silicon (M1/M2/M3/M4):** Higgs Audio v3 (`bosonai/higgs-audio-v3-tts-4b`) chạy local qua MLX theo bộ quy tắc độc lập tại `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md` (chuẩn hóa 02/11/2026 sau khi tối ưu kỹ thuật pre-encoding và cắt đuôi câm, sản xuất thành công Tập 04 EN và Tập 05 EN trên Mac mini M2 16GB).
- **Mac mini** dùng để: (1) tạo giọng mẫu bằng VoxCPM2; (2) chạy trực tiếp production Higgs Audio v3 MLX + Whisper CER + UTMOSv2 MOS theo `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`.
- **Đã dùng sản xuất:** Tập 02 (31/10/2026). **Tập 03:** người dùng chốt dùng Higgs + bộ giọng mẫu Tập 02 (31/10/2026), đang sinh hồi 3. Các tập khác vẫn MiniMax.
- **Đang so sánh:** VoxCPM2 chế độ clone đọc thẳng câu thoại (`.work/VOXCLONE_MAC_BRIEF.md`) — chưa có số đo. Đổi engine phải qua số đo (G13).

## 2. Giấy phép

- Trọng số: *Boson Higgs Audio v3 Research and Non-Commercial License* — kênh mình sở hữu thuộc **Creator Use Grant II-A**: được đăng và kiếm tiền.
- **PHẢI ghi công trong mô tả YouTube mọi tập dùng Higgs** (người dùng chốt 30/10/2026: chỉ trong mô tả, **không** ghép vào audio):
  `This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio`
- Giọng mẫu VoxCPM2 (Voice Design): Apache-2.0, không cần ghi công.
- **CẤM** clone giọng người thật (người trong vụ án, phóng viên, diễn viên, giọng tải từ YouTube/MiniMax/ElevenLabs).
- *Tóm tắt giấy phép, không phải tư vấn pháp lý.*

## 3. Hành vi của Higgs đã đo được (căn cứ cho mọi luật)

| Hành vi | Số đo | Hệ quả |
|---|---|---|
| Cao độ bản đọc **do giọng mẫu quyết định** | Cùng clip cho 2 vai → F0 gần như y hệt (W4: 140,4 / 141,2 Hz) | Đổi giọng = đổi giọng mẫu; không có tham số nào khác |
| **Kéo giọng nam trung** về ~125 Hz | `H.wav` 108→130 Hz (+20%) · `D.wav` 128→124 Hz · `M_LOW` 96→98 Hz | Giọng nam ≤ 96 Hz giữ được; 105–130 Hz dồn về một chỗ |
| Giọng nữ và giọng rất trầm **giữ gần nguyên** (±3%) | `C2_AB03` 210→209 Hz · `D3_SH` 89→88 Hz · `M_HIGH` 192→193 Hz | Giọng nam cao (> 180 Hz) **thành giọng nữ** |
| Thẻ `sadness`/`surprise` làm **giọng nam** vọt cao | Host sad 213 Hz (neutral 126) · D surprised 172–247 Hz · **giọng nữ không bị** | CẤM thẻ cảm xúc (mục 5) |
| Bỏ thẻ → cảm xúc **không còn lệch** | Host sad 125 Hz · D surprised 88 Hz (416 file, 31/10) | |
| **Âm đầu câu** dễ mờ/sai | "Vợ"→"Mợ", "Đó"→"nó", "Ban đầu"→"thăng dầu", mất "Thứ", "Trong", "Cuối" | Cần ≥ 2 bản + vòng 2 (mục 7) |
| Tốc độ **không điều khiển được** | D3_SH 4,0 âm/s, Host 3,4–3,55 (thiết kế D chậm hơn) | Chưa có cách sửa (mục 11) |
| Thỉnh thoảng 1 bản lệch cao độ ≥ 4 nửa cung | 5/474 file (Tập 02) | Loại bằng `--exclude` (mục 7) |

## 4. Giọng mẫu (giọng tham chiếu)

### 4.1 Bộ giọng đang dùng (Tập 02, người dùng chốt 31/10/2026)

Dataset Kaggle `chiduong2026/amber-eyes-voice-ref-voxcpm2`. Phép gán: `.work/g9_role_map.json`.

| Vai | Giọng mẫu | Nguồn trong repo | F0 bản đọc (câu neutral, AC/YIN) |
|---|---|---|---|
| Host (Cú) | `H.wav` | `assets/voice_ref_voxcpm2/H.wav` | 122 / 128 Hz |
| Điều tra viên (Sói) | `D3_SH.wav` | `assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02` (seed 7) | 88 / 88 Hz |
| Chuyên gia (Cáo) | `C2_AB03.wav` | `assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03` (seed 77) | 207 / 209 Hz |
| N1 (nữ trầm) | `W6_LOW.wav` | `assets/voice_ref_voxcpm2_g9/` | 178 Hz |
| N2 (nữ cao) | `W5_HIGH.wav` | `assets/voice_ref_voxcpm2_g9/` | 287–290 Hz |

Khoảng cách (Tập 02): H-D 5,69 · H-C 8,54 · D-C 14,82 · C-N2 5,66 · H-N1 5,75 nửa cung. **C-N1 2,56 — chưa đạt**, chỉ chấp nhận vì N1 không bao giờ đứng liền C (kiểm lại cho mỗi tập, mục 8).

- **Dùng chung bộ này cho mọi tập** (danh tính nhân vật cố định). Đổi giọng mẫu = đổi giọng nhân vật → L4 + mục 4.3.
- Vai phụ N1/N2 của tập mới: chọn theo giới/tuổi ghi trong kịch bản (A11 #51), rồi kiểm mục 8.

### 4.2 Chuẩn file giọng mẫu

| Mục | Yêu cầu |
|---|---|
| Nguồn | **VoxCPM2 Voice Design** trên Mac (`.work/voxcpm_generate_g9.py --candidates/--seeds`) |
| Độ dài | 16–28 s tiếng, không khoảng lặng > 1,5 s bên trong |
| Định dạng | WAV PCM16 mono 24 kHz, −18 ± 1 LUFS, đỉnh ≤ −1,5 dBFS, kèm `.txt` khớp từng chữ |
| Lời đọc | Đúng kiểu câu của vai, cảm xúc trung tính; lời đã chứng minh tốt: `D.txt` (biên bản), `C.txt` (phân tích), `H.txt` (dẫn chuyện) |
| Độ đúng chữ | ASR 2 lượt trên chính giọng mẫu: **CER 0%, 0 lỗi thanh điệu** (`.work/voxcpm_do_dc.py --asr`) |
| CẤM | Chỉnh cao độ/tốc độ bằng phần mềm; giọng tải ngoài; giọng người thật |

### 4.3 Tạo hoặc thay giọng mẫu — quy trình có cổng

| Bước | Việc | ĐẠT khi |
|---|---|---|
| R1 | Mac sinh **nhiều ứng viên**: câu mô tả × seed (16–32 take/vai). **Seed quyết định cao độ hơn câu mô tả** (cùng câu ra 90–195 Hz); seed **42 và 7** ra giọng nam trầm ổn định. Sàn VoxCPM2 ≈ 88 Hz | Có ≥ 2 take trong dải F0 mục tiêu (2 thuật toán) |
| R2 | Đo giọng mẫu: `voxcpm_do_dc.py` (V2–V6) + `voxcpm_yin_f0.py` + ASR 2 lượt | CER 0%, sàn ồn ≤ −55 dB |
| R3 | **Chạy thử trên Kaggle**: 3–4 ứng viên × 12 câu thật của đúng vai (8 neutral + sad/fearful/surprised) × 2 bản, kèm giọng đã chốt của vai đứng cạnh làm đối chứng (`prep_v9.py --mode …`, `build_nb.py`, `analyze_pilot_v9.py --tag … --cer`, `_v9_padtest.py`, `_v9_final.py`) | Mục 8 đạt **trên bản đọc** |
| R4 | Người dùng nghe file xen kẽ (H D C D H C D H C) | Người dùng duyệt (L4) |

Dải F0 giọng mẫu **nên nhắm** (suy từ mục 3): nam rất trầm **82–92 Hz** · nữ **200–218 Hz** (để cách N2 ~270–290 Hz ≥ 4 nc). **Không** nhắm nam 105–180 Hz nếu đã có Host ở ~125 Hz.

### 4.4 TÁCH RIÊNG giọng mẫu tiếng Việt và tiếng Anh (người dùng chốt 31/10/2026)

**Luật: bộ giọng mẫu mỗi ngôn ngữ là một bộ ĐỘC LẬP, không bao giờ dùng chung thư mục, dataset, bảng gán vai hay tên file.** Lý do: tên file VN hiện tại trần trụi (`H.wav`, `C.wav`, `W5_HIGH.wav`) — chép một file EN cùng tên vào là **ghi đè giọng Việt đã chốt**, và Higgs clone ra giọng khác mà không có lỗi nào báo.

| Tầng | Tiếng Việt (giữ nguyên, CẤM đổi) | Tiếng Anh (riêng) |
|---|---|---|
| Ứng viên Mac (`assets/`) | `voice_ref_voxcpm2/`, `_dc/`, `_dc2/`, `_dc3/`, `_g9/` | `voice_ref_voxcpm2_en2/` (22 take, manifest `.work/voxcpm_refs_manifest_en2.json`) |
| Tên clip đã chốt | `H.wav`, `D3_SH.wav`, `C2_AB03.wav`, `W6_LOW.wav`, `W5_HIGH.wav` | **PHẢI có đuôi `_EN`**: `H_EN.wav`, `D_EN.wav`, `C_EN.wav`, `N1_EN.wav`, `N2_EN.wav` (+ `.txt` lời tiếng Anh) |
| Thư mục dataset cục bộ | `.work/kaggle_higgs/dataset_voxcpm2/` | `.work/kaggle_higgs/dataset_voxcpm2_en/` |
| Dataset Kaggle | `chiduong2026/amber-eyes-voice-ref-voxcpm2` | `chiduong2026/amber-eyes-voice-ref-voxcpm2-en` (`ref_dir` = `/kaggle/input/amber-eyes-voice-ref-voxcpm2-en`) |
| Bảng gán vai | `.work/g9_role_map.json` | `.work/g9_role_map_EN.json` |
| Số đo F0/G9 | §4.1 (đo trên bản Higgs đọc tiếng Việt) | Đo lại riêng trên bản Higgs đọc **tiếng Anh** — CẤM mượn số của bản Việt |

- **CẤM** chép clip EN vào thư mục/dataset VN và ngược lại; **CẤM** đổi tên/ghi đè clip VN để "dùng chung".
- **Code (khi tham số hoá `AE_LANG`)** PHẢI chọn thư mục dataset, slug, `ref_dir`, bảng gán vai theo ngôn ngữ, và **tự chặn**: chạy EN mà bảng gán vai trỏ clip không có đuôi `_EN` → dừng; chạy VN mà gặp clip `_EN` → dừng.
- Bộ `assets/voice_ref_voxcpm2_en/` (30/10) **lưu trữ, không dùng**: sinh độc lập trước vòng D/C mới nên D/C là người khác; D 101 Hz dễ bị Higgs dồn sát Host (§3).

**Cách tạo bộ EN (en2):** dùng **nguyên câu mô tả + seed** của từng giọng Việt đã chốt, chỉ thay lời đọc bằng tiếng Anh; mỗi seed × 2 kiểu câu mô tả (`vnctrl` nguyên văn / `enctrl` "English Standard"). Brief: `.work/EN2_MAC_BRIEF.md`. Seed D 7, C 77 có ghi trong `refs.json`; **H 42, W5 2024, W6 (2.5, 999) là suy ra** — Mac đối chiếu `voxcpm_raw/*/takes.json`.
- ⚠ Cùng seed + câu mô tả nhưng khác lời đọc **không bảo đảm cùng âm sắc** ⇒ đo F0 + người dùng nghe so VN↔EN (R4) trước khi chốt. Chốt xong mới đổi tên `_EN` và chép vào `dataset_voxcpm2_en/`.

**Kết quả en2 (31/10/2026, `90_LUU_TRU/BaoCao_DoGiongMau_EN2_20261031.md`):** **cùng seed KHÔNG giữ danh tính** — D seed 7 ra 85–145 Hz (VN 88). H, C, N1, N2 có ứng viên trong dải; D chưa có (nghe `D_vnctrl_t01`, AC 145 / YIN 85). CER tiếng Anh chưa đo được (chưa có bộ chuẩn hoá EN).

**Chuỗi Higgs đã hỗ trợ `AE_LANG=en` (31/10/2026).** Mọi tên file/thư mục/dataset/slug lấy từ một chỗ: `.work/higgs_paths.py`. Bản Việt giữ nguyên tên cũ — đã kiểm hồi quy: payload Tập 02 cũ = mới, `build_spec` Tập 02/03 cũ = mới từng byte, notebook + push Tập 02/03/03-hồi 3/04 cũ = mới, mọi đường dẫn P5–P9 Tập 02/03/04 trùng. Bản EN:
- Payload `higgs_payload_EN_t02.json`: bỏ mọi thẻ ngắt MiniMax `<#x#>` giữa câu (lời đọc EN có sẵn), chỉ giữ `<|prosody:pause|>` sau `:`; "Elizabeth II" → "Elizabeth the Second" (K7, chỉ lời đọc). Chữ số giữ nguyên (Higgs đọc tiếng Anh tự nhiên).
- CER: `.work/en_cer.py` (cùng giao diện `vi_cer`, số → chữ tiếng Anh cả 2 vế, năm đọc kiểu năm). ASR hỏi "Transcribe verbatim in English".
- Kernel `amber-eyes-higgs-prod-en-tXX[-aN]-kaggle-gpu`, dataset `amber-eyes-voice-ref-voxcpm2-en`, đầu ra `out_higgs_prod_EN_tXX`, master `02_SAN_XUAT/TapXX_EN/xuat_ban/TapXX_EN_master.mp3`.
- `build_spec.py` không sinh pilot v6–v8 (clip VN) cho bản EN; `build_spec`/`build_spec_r2` chặn clip sai ngôn ngữ (`check_ref_lang`).
- Bộ giọng EN **TẠM** (`g9_role_map_EN.json`): H ← `H_vnctrl_t01`, D ← `D_vnctrl_t01`, C ← `C_enctrl_t01`, N1 ← `W6_LOW_vnctrl_t01`, N2 ← `W5_HIGH_enctrl_t01`. Giọng mẫu: ASR 2 lượt CER 0% cả 5. Chạy thử hồi 4 Tập 02 EN (đủ 5 vai, 47 câu, 102 file).

**Bộ JA/KO (ja2, ko2 — 31/10/2026, chưa chạy):** làm theo cách en2. Brief `.work/JA2_MAC_BRIEF.md`, `.work/KO2_MAC_BRIEF.md`; manifest `.work/voxcpm_refs_manifest_ja2.json` / `_ko2.json` (26 take mỗi bộ, D thêm seed 101/2024); thư mục `assets/voice_ref_voxcpm2_ja2/`, `_ko2/`. Bộ `_ja`/`_ko` cũ (30/10) **không dùng**: H~D chỉ 0,14 nc (JA) / ~1,9 nc (KO), và báo cáo `BaoCao_DoGiongMau_VoxCPM2_Multilang_20261030.md` ghi "ĐẠT" dù 6/7 giọng JA ngoài dải F0. Còn thiếu trước khi chạy Higgs JA/KO: `higgs_paths.py` mới nhận `vi|en`, chưa có CER tiếng Nhật/Hàn, chưa có `g9_role_map_JA/KO.json`, chưa có dòng `provenance.json`. ⚠ `.work/*` bị gitignore ⇒ log trên Mac phải `git add -f` riêng (en2 từng phải commit log sau).

**Chuỗi Higgs hỗ trợ `AE_LANG=ja` (01/11/2026).** `higgs_paths.py` nhận `vi|en|ja` (biến `FOREIGN`, `JA`; hậu tố `_JA`, dataset `chiduong2026/amber-eyes-voice-ref-voxcpm2-ja` → thư mục `.work/kaggle_higgs/dataset_voxcpm2_ja/`, bảng gán vai `.work/g9_role_map_JA.json`, clip bắt buộc đuôi `_JA`). Hồi quy L9: mọi giá trị `higgs_paths` vi/en × Tập 02/03/04 × cả tập/hồi 3 **trùng hệt** bản cũ; payload VN/EN `--check` không đổi (lệch 1.10#2 của VN Tập 02 có từ trước). Lời đọc JA: chữ số → số kanji (`ja_cer.ja_numbers`, 2009年 → 二千九年), bỏ `<#x#>`/`...`; tên Latin (Russell Williams, Elizabeth II) giữ nguyên — xem CER chạy thử. CER JA: `.work/ja_cer.py` (pykakasi, so trên **cách đọc hiragana** cả hai vế ⇒ không tính lỗi chính tả kana↔kanji của ASR). Bộ giọng: H `ja2/H_vnctrl_ja_t02` · D `ja3/D_lowgrowl_ja3_t01` · C `ja3/C_deepalto_ja3_t03` · N1 `ja3/W6_LOW_huskycontralto_ja3_t04` · N2 `ja2/W5_HIGH_vnctrl_ja_t02` (5 dòng `provenance.json`). ⚠ Trên giọng mẫu H 106,7 Hz – D 93,0 Hz chỉ ~2,4 nc ⇒ G9 H–D phải đo trên bản đọc. Chạy thử hồi 4 (94 file): kernel `amber-eyes-higgs-prod-ja-t02-a4-kaggle-gpu`. **Kết quả (01/11/2026): 94/94 file OK (~15 phút Kaggle). F0 câu neutral: H 105,0/96,6 · D 90,1/89,5 · C 226,4/242,9 Hz (AC/YIN). G9: D–H 1,33 nc ❌ TRƯỢT · C–H 13,3 · C–D 16,0 ✅. G8: 3 bản H lệch. CER (`ja_cer`, 2 lượt, bản tốt nhất): 39/47 câu ≤ 2%; 8 câu > 2% đa số do tên riêng/ASR (ツイード↔ツィード), lỗi đọc thật: 将校→商工 (4.06#4), 鑑識→監視 (4.08#5), スミス→済み (4.08#3). ⇒ DỪNG trước khi chạy cả tập: cần đổi giọng mẫu H hoặc D (chờ người dùng).** `check_higgs_f0.py` chỉ đọc thư mục cả tập; với chạy thử 1 hồi phải trỏ `PROD` vào `P.PROD` (đã làm bằng wrapper, chưa sửa script). **Vòng 2 (01/11/2026, người dùng đồng ý thử):** H → `ja2/H_jactrl_t01` (mẫu 122,1 Hz, CER mẫu 1,2%), D → `ja3/D_smokerbass_ja3_t02` (mẫu 87,4 Hz, CER mẫu 1,9%; `D_lowgrowl_ja3_t02` bị ASR trả "[No speech]" ⇒ loại). Bản đọc: H 122,8/129,0 · D 83,9/82,1 · C 226,4/242,9 Hz ⇒ G9 D–H **6,59 nc ✅**, C–H 10,6 ✅, C–D 17,2 ✅ · G8 0 bản lệch ✅ · CER 38/47 câu ≤ 2% (9 câu > 2%, cần nghe: 大佐 bị ASR nghe 対差/対談, オタワ→小田原, 尋問調書→陰謀聴取). Chờ người dùng nghe `02_SAN_XUAT/Tap02_JA/thu_giong_higgs/Hoi4_JA_higgs_vong2_ban1.mp3` trước khi chạy cả tập. Vòng 1 sao lưu ở `.work/_cu/ja_vong1_20261101/`. **Cả tập (01/11/2026, người dùng duyệt):** lượt 1 406 file (~65 phút Kaggle) → 52/203 câu > 2% · G9 D–H 6,23 · C–H 10,4 · H–N1 8,2 · C–D 17,0 nc ✅ · G8 loại 3 bản H → vòng 2 104 file → **35/203 câu > 2%** (nhiều câu do tên Latin trong câu gốc mà ASR viết katakana: Nissan Pathfinder, Elizabeth II — CER giả). **Lỗi mới: 2 file Higgs có đuôi gần câm ~40 s** (`1.03#2`, `3.07#3` dài đúng 47,6 s = trần `max_new_tokens`, −61…−72 dB sau lời) — CER vẫn 0%, silencedetect trên master **không bắt được** vì nền môi trường che ⇒ master lần 1 dài thừa 82,5 s. Đã cắt đuôi (giữ 0,3 s + fade 30 ms, gốc ở `.work/_cu/ja_duoi_cam_20261101/`) rồi chạy lại `build_audio3.py`. Master: `02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp3` 1791,8 s · −16,2 LUFS · −2,4 dBFS · 0 khoảng câm · lời đầu 23,0 s ✅. Danh sách nghe: `CanNghe_Tap02_JA_higgs.md`. **Luật:** sau P9 PHẢI quét mọi file đã cài tìm đuôi < −45 dB dài > 0,8 s (file dài ≈ trần token là dấu hiệu).

**Trạng thái:** người dùng chốt bộ giọng EN sau khi nghe hồi 4 (31/10/2026). **Tập 02 EN đã có master Higgs** (`02_SAN_XUAT/Tap02_EN/xuat_ban/Tap02_EN_master.mp3`, 1434,4 s, cổng §9 đạt) — số đo trong hồ sơ tập EN. Higgs đọc tiếng Anh đúng chữ tốt hơn tiếng Việt (lượt 1: 4/203 câu > 2% so với 29/203 bản VN) và **không** kéo Host lên ~125 Hz (112–116 Hz). Chuỗi P1–P9 **chưa** đọc `AE_LANG` (tên file sẽ ghi đè bản Việt: `higgs_payload_t02.json`, `Tap02_master.mp3`; `lang` cứng `"vi"`; `vi_numbers`, `vi_cer`) ⇒ phải tham số hoá + kiểm hồi quy Tập 02 VN từng byte (L9) trước khi chạy Kaggle bản EN.

## 5. Văn bản gửi vào Higgs

| Luật | Quy định |
|---|---|
| **Thẻ cảm xúc** | **CẤM mọi `<|emotion:…|>`** (cả `fear`, để đồng nhất). Cấu hình: `g9_role_map.json` khoá `"_emotion_tags": false` — `build_spec.py` và `build_spec_r2.py` đều đọc khoá này. Cảm xúc thể hiện bằng ngắt giữa câu (G2), nhạc và tiếng động |
| Ngắt | Chỉ `<|prosody:pause|>` **sau dấu `:` trước câu trích** (G1). CẤM thẻ khác (`speed_*`, `pitch_*`, `style:*`, `expressive_*`, `sfx:*`) |
| Số | `vi_numbers()` của `tts_sentences.py` (G11). Ký hiệu (%, $, km) viết bằng chữ (K7) |
| Thẻ MiniMax | Xoá `<#…#>` và `...` |
| Độ dài | Mỗi câu < 47 s (`max_new_tokens = 1196` ≈ 47,8 s ở 25,02 Hz). Câu dài tách tại dấu câu |
| Câu gốc | Phụ đề và chữ trên hình lấy câu gốc (G6); payload giữ `text_plain` |
| Kiểm | Sau `build_spec.py`: **0 thẻ `<|emotion` trong payload**, text khớp lượt trước ngoài việc bỏ thẻ |

## 6. Tham số sinh (đã chốt)

| Tham số | Giá trị |
|---|---|
| `temperature` | **0,8** mọi vai (`GEN_PARAMS.temp_by_role` trong `build_spec.py`) |
| `top_p` / `top_k` | 0,95 / 50 |
| `max_new_tokens` | 1196 (tính từ frame-rate đo thật 25,02 Hz) |
| `fade_ms` | 30 |
| seed | `sha256(id|role|ref|temp|vN)` → `torch.manual_seed` + `cuda.manual_seed_all` trước mỗi câu; cùng seed ra cùng kết quả trên card nào cũng vậy |
| Bản / câu | **2** (`variants [0,1]`); câu có trích dẫn **3**; vòng 2 thêm 2 bản (biến 2,3 hoặc 3,4) |
| Đầu ra | WAV 24 kHz mono, không chuẩn hoá (`build_audio3.py` chuẩn hoá ở master) |
| Phần cứng | 2 worker × 1 T4; VRAM đỉnh ~10 GB; **416 file ≈ 42 phút**, 58 file ≈ 6 phút |
| Mã hoá giọng mẫu | `model._encode_reference(...)` **1 lần/clip rồi cache** |

## 7. Quy trình sản xuất một tập — từng lệnh

Mọi lệnh chạy từ thư mục repo với `AE_EP=XX` (không đặt ⇒ Tập 02, ra **đúng từng byte** bản đã push — đã kiểm 6/6 file lượt 1 và 4/4 file vòng 2). `AE_ACT=N` chỉ sinh một hồi (spec/payload/kernel mang hậu tố `_aN`). Đặt `PYTHONIOENCODING=utf-8`; Kaggle CLI ở `%LOCALAPPDATA%\kaggle-venv\Scripts\kaggle.exe`. Tên file tập khác 02 mang hậu tố `_tXX`; kernel `amber-eyes-higgs-prod-tXX-kaggle-gpu` và `…-tXX-r2-…`.

| # | Việc | Lệnh | ĐẠT khi |
|---|---|---|---|
| P0 | **Kiểm đầu vào khớp kịch bản** (§14.2) + giới tính vai phụ (§14.3) + sao lưu lượt cũ (L5) | `py -3 .work/parse_kichban.py <md> .work/script_tapXX.json` · so mã câu của `acting_tapXX.json`, `sfx_tapXX.json`, `EPISODES[XX]` theo nội dung · sinh lại `tts_manifest_tXX.json` · `py -3 .work/_qc_bgm_bed_start.py` | 0 mã câu lệch · mọi `alt` khớp câu hiện tại · nhạc 5/5 hồi OK |
| P1a | Payload nguồn | `py -3 .work/export_higgs_payload.py` | 0 chữ số · 0 ngoặc ngoại ngữ · 0 `...` |
| P1 | Spec + payload Kaggle | `py -3 .work/build_spec.py` | `the cam xuc: BO`, đủ câu, "OK: moi clip + file .txt deu co" |
| P2 | Notebook + thư mục push | `py -3 .work/build_nb.py --mode prod` · `py -3 .work/prep_push_dirs.py prod` | `verify: OK` |
| P3 | Dataset | PowerShell: `kaggle datasets version -p "D:\…\.work\kaggle_higgs\dataset_voxcpm2" -m "…"` → lặp `kaggle datasets status chiduong2026/amber-eyes-voice-ref-voxcpm2` | `ready` |
| P4 | Chạy | `kaggle kernels push -p "…\_push_prod_tXX"` | `RUNNING` |
| P5 | Chờ + tải (nền) | `py -3 .work/watch_kernel.py --slug <slug> --out .work/kaggle_higgs/out_higgs_prod_tXX --pattern "out_higgs_prod_tXX/.*\.(wav|json|log)"` | `XONG: n OK / 0 FAIL` mỗi worker |
| P6 | CER (nền) | `py -3 .work/measure_cer_prod.py --rounds 2 --workers 2` | 0 lỗi connector · 0 file thiếu ASR |
| P7 | F0 + G9 + danh sách loại | `py -3 .work/check_higgs_f0.py` (sau vòng 2/3: `--new-only`) | G9 mọi cặp liền kề ≥ 4 nc · xem dòng "câu MỌI bản đều bị loại" |
| P8 | Vòng 2 | `py -3 .work/build_spec_r2.py --max-cer 0.02 --exclude .work/higgs_exclude_f0_tXX.json` → `build_nb.py --mode r2` → `prep_push_dirs.py r2` → P3–P5 (out `out_higgs_r2_tXX`) → `py -3 .work/merge_r2.py` → P6 (cache, chỉ đo file mới) → P7 `--new-only` | Câu > 2% giảm |
| P8b | Vòng 3 (câu đổi chữ, câu mọi bản bị loại) | đổi tên `out_higgs_r2_tXX` → `…_vong2` và `higgs_manifest.before_r2.json` → `…before_r2_vong2.json` · `build_spec_r2.py --max-cer 99 --ids "a#1,b#2" --exclude …` → như P8 | Số thứ tự bản tự nối tiếp, không trùng file vòng 2 |
| P9 | Chọn bản + master | `py -3 .work/finish_prod.py` | 0 bản chọn trong danh sách loại · đủ số câu |
| P10 | Cổng master (§9) + danh sách cần nghe kèm mốc thời gian + ghi hồ sơ tập (L6) | ffmpeg ở `.work/ffmpeg/…/bin/ffmpeg.exe`: `ebur128=peak=true`, `silencedetect` | §9 đạt |

**Số mốc:** Tập 02 — lượt 1 29/203 câu > 2% → vòng 2 12/203 (~7 là tên riêng/ASR dao động). Tập 04 (31/10) — lượt 1 28/154 (316 file, 41 phút) → vòng 2 (66 file) 18/154 → master 21 câu cần nghe, đa số mất chữ đầu câu ("Thế nhưng"→"Nhưng"). Tập 03 — lượt 1 45/218 (455 file, 53 phút) → vòng 2 (94 file) 22/218 → vòng 3 (8 file, sửa chữ) → master: 24/218 cần nghe, đa số ASR nghe nhầm "Kemper".

## 8. Cổng giọng — đo trên bản đọc

| Cổng | Cách đo | ĐẠT khi |
|---|---|---|
| **G9 mở rộng** | F0 trung vị **câu neutral** của mỗi vai, **2 thuật toán** (AC `voice_audition.f0_median` + YIN `voxcpm_yin_f0.yin`), lấy **min** | **Mọi cặp vai đứng liền nhau trong kịch bản** (tính từ `script_tapXX.json`, kể cả khác giới) **≥ 4 nửa cung**. Cặp không liền kề < 4: ghi vào hồ sơ, người dùng chấp nhận |
| **G8** | Mỗi câu cảm xúc so với trung vị neutral của chính vai | 0 bản **được chọn** lệch ≥ 4 nửa cung |
| **CER** | `listen_audio` 2 lượt/file, lấy lượt xấu hơn, chuẩn hoá 2 vế bằng `vi_cer.py` (Q3a) | Mỗi câu có ≥ 1 bản ≤ 2%; câu còn > 2% → liệt kê cho người dùng nghe (mục 10) |
| Nghe mù | `listen_audio` hỏi "mấy người nói" trên file xen kẽ | **Chỉ tham khảo**: 2 lượt Tập 02 cho kết quả mâu thuẫn (Q4) — không thay được F0 + tai người dùng |

## 9. Cổng master (bước 6 AGENTS.md)

0 khoảng câm > 0,3 s ở −60 dB · −16 ± 1 LUFS · đỉnh ≤ −1,5 dBFS · lời đầu 22,8–23,5 s.
Tập 02 (31/10): 1411,9 s · −16,2 LUFS · −1,7 dBFS · 0 · 23,0 s ✅.
Tập 03 (31/10): 1683,7 s · −16,2 LUFS · −1,7 dBFS (sau giới hạn đỉnh; `loudnorm` linear để lại −1,0) · 0 · 23,0 s ✅. `build_audio3.py` tự giới hạn đỉnh −2,5 dBFS khi mp3 vượt −1,5.

## 10. Đọc kết quả ASR — đừng kết luận sai

| Hiện tượng | Ví dụ Tập 02 | Xử lý |
|---|---|---|
| ASR bỏ chữ đầu câu | "Thứ dẫn…" → "Dẫn…" (câu 14 từ → 6,5%) | Chèn 0,5 s lặng rồi ASR lại (`_v9_padtest.py`) cứu ~30%; còn lại xếp "cần nghe" |
| Tên riêng nước ngoài | Tweed→"Thuýt", Lloyd→"Lôi", Smyth→"Smark/Smith", Genest→"Cenes" | Chấp nhận (xem thêm `cer_prop`) |
| ASR dao động | Cùng file: 2,3% → 266,7% giữa 2 lượt | Không kết luận từ 1 lượt (Q6) |
| Sai giống nhau ở 2 engine | "Thứ hắn lấy đi" → "nhãn lady" (Higgs) / "Thương hiệu Han Lady" (MiniMax) | Nghi ASR; người dùng nghe |
| Câu ngắn | < 12 từ: 1 lỗi = 6–20% | Báo riêng (Q3c) |
| Lỗi thật | "Vợ"→"Mợ", "Và đó là"→"Đây là" | Vòng 2; vẫn sai → báo người dùng, **không** tự sửa chữ câu |

Báo cáo cho người dùng: danh sách câu còn > 2% kèm **mốc thời gian trong master** (`timeline_s_tXX.json`).

## 11. Bẫy kỹ thuật đã gặp

| Bẫy | Cách làm đúng |
|---|---|
| Cache ASR `_asr_cache_prod/` đặt theo **tên file** → lượt mới trùng tên dùng bản chép cũ | Chuyển cache vào bản sao lưu ở P0 |
| `build_spec_r2.py` đọc payload gốc **còn thẻ cảm xúc** | Đã sửa: đọc `_emotion_tags`. Mọi script sinh payload PHẢI đọc khoá này |
| Chọn bản khi **hoà CER** lấy nhầm bản lệch cao độ | `--exclude` cho `install_higgs_audio.py` và `build_spec_r2.py` |
| Câu có bản tốt nhất bị loại vì lệch cao độ → không vào vòng 2 | `build_spec_r2.py --exclude` |
| 6 luồng ASR → hàng loạt `connector_tool_error (latency_ms=0)` | `--workers 2` (~13 lượt/phút) |
| `measure_cer_prod.py` lỗi in báo cáo (`%` chưa escape) | Đã sửa; dữ liệu ghi trước bước in nên không mất |
| Slug Kaggle **sinh từ `title`** | `prep_push_dirs.py` khai `slug` khớp title; sai → kernel trùng |
| `kaggle kernels output` không lọc → tải cả model 10 GB | Luôn `--pattern` (`watch_kernel.py`) |
| Cảnh báo "not valid tags" khi push | Vô hại |
| Chèn code bằng heredoc Python có `\|` → SyntaxWarning | Kiểm dòng regex trong file + đếm byte `\x00`/`\x08` (T4) |

## 12. Chưa giải quyết

1. ~~Tham số hoá theo `AE_EP`~~ — xong toàn chuỗi (31/10/2026, dùng cho Tập 03).
2. **Tốc độ** D nhanh hơn Host — Higgs không có tham số tốc độ; thử `atempo` sau khi đọc (G4: −0,06…+0,02) chưa làm.
3. **Âm đầu câu** — cơ chế chưa rõ (Higgs hay fade-in 30 ms?). Chưa thử tăng/giảm `fade_ms`.
4. **C-N1 2,56 nửa cung** — cần giọng nữ sạch ≤ 160 Hz nếu tập sau có N1 đứng cạnh C.
7. Giọng nam cho vai phụ — **không làm** (người dùng chốt 31/10/2026, §14.3).
8. **Một số câu ngắn của Host bị Higgs đọc trầm ~5 nc ở mọi bản** (Tập 03 1.03#8, 6/6 bản ~95 Hz). Chưa rõ nguyên nhân; thử đổi dấu câu/thêm từ dẫn ở lời đọc riêng.
5. **So sánh VoxCPM2 clone** — chờ Mac (`.work/VOXCLONE_MAC_BRIEF.md`).
6. Cập nhật bảng bộ giọng ở mục 4 AGENTS.md khi người dùng chốt Higgs cho các tập sau.

Lỗi mới: thêm dòng vào mục 3/10/11 ở đây **và** tiêu chuẩn A11 (L6).

## 14. Kinh nghiệm sau Tập 02 và Tập 03

### 14.1 Cái đã chạy tốt — giữ nguyên

| Kinh nghiệm | Số đo |
|---|---|
| **Bộ giọng mẫu dùng lại được giữa các tập**: F0 bản đọc gần như không đổi theo nội dung | C 209 → 207 Hz · D 88 → 89 · H 128 → 129; G9 các cặp lệch ≤ 0,4 nc giữa 2 tập ⇒ dùng F0 tập trước để duyệt G9 sơ bộ trước khi tốn GPU (vẫn đo lại trên bản đọc) |
| **Seed tất định**: sinh lại ra đúng từng byte | 78/78 file hồi 3 trùng byte giữa lượt riêng hồi và lượt cả tập ⇒ sinh thử một hồi không phí; chép cache ASR sang lượt cả tập |
| **Bỏ thẻ cảm xúc** giữ cao độ ổn định | Câu sad/fearful/surprised của H, D, C lệch ≤ 0,6 nc so với neutral (Tập 03) |
| **Vòng 2 hiệu quả** | Tập 02: 29 → 12 câu > 2% · Tập 03: 45 → 22 · hồi 3 Tập 03: 10 → 4 (3.05#3 15% → 5%) |
| **Chạy thử một hồi trước** (`AE_ACT`) | 38 câu ≈ 10 phút Kaggle + 15 phút đo — người dùng nghe được giọng trước khi chạy cả tập ~1 giờ |
| Thời gian thực tế | Kaggle ~7 s/file (455 file ≈ 53 phút + ~10 phút tải) · ASR ~13 lượt/phút (`--workers 2`) |

### 14.2 Lỗi đã gặp và luật rút ra

| # | Lỗi | Luật |
|---|---|---|
| K1 | **Payload Tập 02 làm tay**, chứa 3 phép đổi chữ ngầm không ghi ở đâu | Payload PHẢI sinh bằng `export_higgs_payload.py`; mọi phép đổi chữ PHẢI nằm trong code |
| K2 | **Script viết cứng cho một tập** chặn tập sau | Script mới đọc `AE_EP` từ đầu; Tập 02 giữ tên file cũ để kiểm hồi quy từng byte |
| K3 | **`script_tap03.json` cũ (220 câu) lệch kịch bản (218)**; `parse_kichban.py` chạy thiếu tham số chỉ báo lỗi, JSON cũ vẫn nằm đó | Sau khi sửa kịch bản: chạy lại với 2 tham số và so số câu |
| K4 | **Acting/sfx/tts_manifest theo mã câu cũ** ⇒ lời đọc riêng `alt` gắn nhầm câu: đọc câu khác, đọc lại câu cũ vi phạm V9 | P0: chuyển mã theo nội dung; so mọi `alt` với câu hiện tại. **CER không phát hiện được** vì so với chính chữ đã gửi |
| K5 | Câu có **mọi bản** bị loại bị bỏ khỏi vòng 2 | Đã sửa `build_spec_r2.py`; `check_higgs_f0.py` in danh sách này |
| K6 | Cache ASR theo tên file — tên wav trùng giữa các tập | Cache riêng mỗi tập (`_asr_cache_prod_tXX`) |
| K7 | Nhạc nền hồi 5 Tập 03 không khớp kịch bản (A10) | Chạy `_qc_bgm_bed_start.py` ở P0 |
| K8 | `loudnorm` linear để lại đỉnh −1,0 dBFS | Đo đỉnh trên **mp3**; `build_audio3.py` tự giới hạn |
| K9 | N1/N2 giọng nữ đọc lời cảnh sát nam ⇒ khi nghe tưởng "Điều tra viên thành nữ"; đo lại thì D vẫn 89 Hz (0/56 bản > 120 Hz) | Khi người nghe báo "vai X đổi giọng": kiểm F0 bản đã chọn của vai X **và** xem đoạn đó có phải vai phụ không, trước khi sửa gì |
| K10 | Kaggle CLI trên Git Bash: đường dẫn `/` làm `datasets version` lỗi | Chạy P3/P4 bằng PowerShell, đường dẫn `\` |
| K11 | Tập 05 (01/11): `finish_prod.py` ghi đè `xuat_ban/TapXX_master.mp3` của bản MiniMax cũ, không sao lưu (L5); câu ngắn 2.04#2 của D: 8/8 seed đều đọc ở 115–131 Hz (vùng Host), lỗi theo câu chứ không theo seed | Trước P9: chép `xuat_ban/TapXX_master.mp3` + `timeline_s_tXX.json` vào `.work/_cu/`. Câu có mọi bản lệch F0 qua 2 vòng ⇒ dừng thử seed, đưa người dùng nghe hoặc đề xuất sửa chữ (cần duyệt kịch bản) |
| K12 | **Câu ngắn của D (≤ 8 từ, câu cụt/liệt kê) bị Higgs đẩy cao giọng về vùng Host** — đo T03–T05: câu dài D 88–89 Hz (n > 340) nhưng câu ≤ 8 từ trung vị 90/130/108 Hz; T04 "Đúng như vậy." vào master ở 122 Hz, T03 hai câu 110 Hz lọt ngưỡng 4 nc. Kéo dài câu T05 2.04#2 (8 → 14 từ) giảm 115–131 → 106–118 Hz: **có tác dụng nhưng không triệt để** | Khi viết kịch bản: lời D NÊN ≥ 9 từ, tránh câu cụt "Thứ nhất: …" đứng riêng. Khi chọn bản D: ưu tiên bản F0 thấp nhất khi CER bằng nhau (`finish_prod.py` chưa xét F0). Nếu nhiều câu ngắn vẫn > 105 Hz ⇒ cân nhắc giọng mẫu D khác (phải qua G8/G9) |

### 14.3 Vai phụ (N1/N2)

- **Người dùng chốt 31/10/2026: chỉ cần giữ 3 giọng chính; N1/N2 giọng nào cũng được** ⇒ mọi tập dùng chung N1 = `W6_LOW` (nữ trầm ~176 Hz), N2 = `W5_HIGH` (nữ cao ~285 Hz), kể cả khi kịch bản ghi nhân chứng nam. **Không** tạo giọng mẫu mới cho vai phụ trừ khi người dùng yêu cầu.
- Vẫn PHẢI đạt G9 với vai đứng liền kề (thường là Host): Tập 03 H–N1 5,46 · H–N2 13,81 nc.
- Nếu sau này cần giọng nam cho vai phụ: phải cách Host ≥ 4 nc **và** D ≥ 4 nc; vùng trống ~150–165 Hz. `M_LOW` (98 Hz) quá gần D, `D.wav` (~124 Hz) trùng Host.

### 14.4 Báo cáo cho người dùng

- Danh sách câu cần nghe PHẢI có **mốc thời gian trong master** (`timeline_s_tXX.json`) và bản chép ASR.
- Đa số câu > 2% là ASR nghe nhầm tên riêng ("Kemper" → "Camper/Kem Bờ/Ember"); tách riêng câu nghi lỗi thật (CER > 10%, chữ phổ thông sai) để người dùng nghe trước.

## 13. Nguồn

- Model card v3: https://huggingface.co/bosonai/higgs-audio-v3-tts-4b
- Danh mục thẻ: https://huggingface.co/bosonai/higgs-tts-3-4b/blob/main/PROMPTING.md
- Giấy phép: https://huggingface.co/bosonai/higgs-tts-3-4b/blob/main/LICENSE
- Loader transformers mượn: `multimodalart/higgs-audio-v3-tts-4b-transformers`
- VoxCPM2: `openbmb/VoxCPM2` (Apache-2.0)
