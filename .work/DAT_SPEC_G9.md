# Đặc tả tạo 4 clip tham chiếu VoxCPM2 mới — G9 (Tập 02, Higgs Audio v3)

**Ngày:** 30/10/2026 (cập nhật sau khi đo đủ 192 audio pilot v3+v4) · **Người chạy:** bạn, trên **Mac mini** (VoxCPM2 cần MPS/Apple Silicon)
**Thời gian ước tính:** ~25–35 phút · **Số lệnh cần chạy: 1**

---

## 1. Vì sao cần làm

Tập 02 có 5 vai: **H** (nam), **D** (nam), **C** (nữ), **N1** (nữ), **N2** (nữ).
Luật **G9** (`AGENTS.md` dòng 111) yêu cầu **hai giọng cùng giới cách nhau ≥ 4 nửa cung**.
⇒ Phải kiểm **4 cặp**: H↔D · C↔N1 · C↔N2 · **N1↔N2**.

Đo lại toàn bộ 192 audio của pilot v3 + pilot v4 (n = 16 mỗi ô C/D/H, n = 8 mỗi ô N1/N2):

| Cặp | F0 hai vai | Khoảng cách | Luật G9 | Kết luận |
|---|---:|---:|---:|---|
| H ↔ D | 131 Hz / 122 Hz | 1,19 nc (AC thô) · 0,01 nc (AC chuẩn hóa) | ≥ 4 | ❌ trượt |
| C ↔ N1 (N1 ← W1) | 205 Hz / 247 Hz | 3,25 nc | ≥ 4 | ❌ trượt |
| C ↔ N2 (N2 ← W1) | 205 Hz / 276 Hz | 5,13 nc | ≥ 4 | ✅ đạt |
| **N1 ↔ N2** (cả hai ← W1) | 247 Hz / 276 Hz | **1,89 nc** | ≥ 4 | ❌ trượt |

> ⚠ Cặp **N1↔N2** trước đây **chưa từng được kiểm** — đây là lý do phát hiện ra vấn đề với phương án cũ.

**Nguyên nhân gốc:** Higgs **không giữ cao độ 1-1 của clip tham chiếu**.
Tỉ lệ `clone / clip gốc` dao động **0,93 → 1,22** (đo ở 9 tổ hợp vai × clip):

| Vai | Clip gốc | Audio clone | Lệch |
|---|---:|---:|---:|
| H | 107 Hz | 131 Hz | **+22%** |
| D | 132 Hz | 122 Hz | **−7%** |
| N1 ← W3 | 157 Hz | 157 Hz | 0% |
| N2 ← W1 | 235 Hz | 276 Hz | **+17%** |

⇒ Không có quy luật để suy ra chắc chắn ⇒ **mọi con số phải đo lại bằng pilot**, không đoán.
⇒ Bộ 7 clip hiện tại **không đủ**. Cần thêm clip mới.

## 2. Cần tạo 4 bộ clip

| Tên | Dùng cho | F0 mục tiêu của **clip** | Vì sao (tính từ số đo thật) |
|---|---|---|---|
| `M_LOW` | dự phòng cho vai **H** | **80–92 Hz** (nam rất trầm) | audio clone phải ≤ 97 Hz để cách D (122 Hz) ≥ 4 nc. Hợp mô tả nhân vật "deep chesty resonance" |
| `M_HIGH` | dự phòng cho vai **D** | **168–182 Hz** (nam cao) | audio clone phải ≥ 165 Hz để cách H (131 Hz) ≥ 4 nc |
| **`W6_LOW`** | **vai N1** (khuyến nghị) | **148–162 Hz** (nữ trầm) | N1 phải **≤ 163 Hz** để cách **cả C (205 Hz) lẫn N2 (276 Hz)** đều ≥ 4 nc |
| `W5_HIGH` | phương án B cho vai **N1** | **258–276 Hz** (nữ cao) | chỉ dùng nếu đổi N2 sang `W6_LOW`; nếu để N2 ← W1 thì clip này làm N1 **sát N2** (~1,7 nc) ❌ |

Cả 4 bộ đều **dự phòng** — sau khi có clip, tôi sẽ đo lại trên Kaggle (audio clone thật) rồi mới chốt
vai nào dùng clip nào. Sinh cả 4 giúp tránh phải quay lại Mac mini lần nữa.

## 3. Cách chạy

Trong terminal trên **Mac mini**, tại thư mục repo `amber-eyes`:

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py
```

Script sẽ tự:

1. nạp VoxCPM2 trên MPS;
2. với mỗi vai, thử các `control_variants` **từ nhẹ đến mạnh**, sinh 1 take mỗi bậc, đo F0,
   **dừng sớm** ngay khi có take nào nằm trong dải mục tiêu; hết thang thì sinh thêm take của bậc gần nhất;
3. đóng gói sang WAV **24 kHz mono, −18 LUFS** (đúng chuẩn `QUY_TAC_AUDIO_HIGGS.md` §4),
   tự kiểm thời lượng 16–28 s và ghi `notes` nếu lệch;
4. xuất `assets/voice_ref_voxcpm2_g9/<ROLE>.wav` + `.txt` + `refs.json` (cùng schema với bộ 7 clip gốc).

**Kiểm tra trước khi commit** — màn hình phải có dạng:

```
--- M_LOW  (muc tieu F0 80-92 Hz) ---
  > [very-low] M_LOW_very-low_take01.wav (seed=42, cfg=2.0)... 38s | 24.1s | F0 87.3 Hz [TRONG DAI]
  => DUNG trong dai, dung tai day: M_LOW_very-low_take01.wav
  => DONG GOI assets/voice_ref_voxcpm2_g9/M_LOW.wav (24 kHz mono, 24.1s, F0 87.3 Hz)
```

Nếu một bộ **không** có take nào trong dải (in `[LECH]` hết), **vẫn chạy tiếp** — tôi sẽ xử lý.

## 4. Gửi lại cho tôi

```bash
git add assets/voice_ref_voxcpm2_g9
git commit -m "feat(audio): them 4 clip tham chieu VoxCPM2 cho G9 (Tap 02)"
git push
```

> Thư mục `assets/voice_ref_voxcpm2_g9_raw/` (bản 48 kHz trung gian) đã được `.gitignore` — **không** commit,
> chỉ cần bản 24 kHz trong `assets/voice_ref_voxcpm2_g9/`.

## 5. Tôi làm gì tiếp

1. Đưa clip mới vào dataset Kaggle → chạy **pilot v5/v6** (đo F0 audio clone + CER cho từng clip, 2 lượt ASR).
2. Chốt ánh xạ vai **bằng số đo thật** — bảng ứng viên:
   - `H ← H.wav` **hoặc** `M_LOW` · `D ← D.wav` **hoặc** `M_HIGH` · `C ← C.wav` (giữ)
   - `N1 ← W6_LOW` (khuyến nghị) **hoặc** `N1 ← W5_HIGH` + `N2 ← W6_LOW` · `N2 ← W1` (giữ, CER 0,63%)
3. H3: nghe mù V7 (H↔D, H↔W4, D↔W4, W2↔C) + G8.
4. Sinh 203 câu Tập 02 (3 bản/câu) → **H4** (đọc 1 hồi + mix + QC).

> ⛔ Theo quyết định của bạn: **dừng trước H4** cho tới khi chốt được phần **ghi công Boson**.
> Bước 1–3 không phát ra audio sản xuất nên vẫn làm được bình thường.

## 6. File liên quan

| File | Vai trò |
|---|---|
| `.work/voxcpm_generate_g9.py` | **Script chạy trên Mac mini** (sinh + đóng gói 1 lệnh) |
| `.work/voxcpm_refs_manifest_g9.json` | Mô tả giọng + văn bản + dải F0 của 4 clip mới |
| `.work/G9_HD_HUONG_DAN.md` | Bản giải thích đầy đủ (vì sao, số đo ra sao) |
| `.work/voxcpm_generate_all.py` | Script gốc tạo 7 clip (để tham khảo) |
| `.work/higgs_make_refs_voxcpm.py` | Script đóng gói 7 clip gốc (để tham khảo) |
| `.work/kaggle_higgs/_g9_matrix.py` | Dựng bảng G9 đầy đủ từ 192 audio pilot v3+v4 (chạy lại được) |
| `90_LUU_TRU/BaoCao_H2_Higgs_Pilot_Tap02_20261030.md` | Báo cáo H2 (mục 6 & 7 nói về 2 lỗi G9 này) |
