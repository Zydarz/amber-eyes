# Đặc tả tạo 3 clip tham chiếu VoxCPM2 mới — G9 (Tập 02, Higgs Audio v3)

**Ngày:** 30/10/2026 · **Người chạy:** bạn, trên **Mac mini** (VoxCPM2 cần MPS/Apple Silicon)
**Thời gian ước tính:** ~20–30 phút · **Số lệnh cần chạy: 1**

---

## 1. Vì sao cần làm

Hai vai nam của Tập 02 đang **gần như cùng cao độ** nên người nghe dễ lẫn:

| Vai | Cao độ của **audio đã sinh ra** | Khoảng cách | Luật G9 yêu cầu | Kết luận |
|---|---:|---:|---:|---|
| H (người dẫn chuyện) | 130 Hz | **0,23 nửa cung** | ≥ 4 | ❌ trượt |
| D (thám tử) | 121 Hz | | | |

Và vai nữ phụ N1 (245 Hz) cách vai nữ chính C (205 Hz) chỉ 3,07 nửa cung.

**Nguyên nhân gốc:** Higgs **không giữ cao độ của clip tham chiếu** — nó kéo mọi giọng nam về cùng một
vùng ~120–130 Hz:

| Vai | Cao độ clip gốc | Cao độ audio clone | Lệch |
|---|---:|---:|---:|
| H | 108 Hz | 130 Hz | **+20%** |
| D | 128 Hz | 121 Hz | **−8%** |

⇒ Bộ 7 clip hiện tại **không đủ**. Cần thêm clip mới.

## 2. Cần tạo 3 bộ clip

| Tên | Dùng cho | F0 mục tiêu của clip | Vì sao |
|---|---|---|---|
| `M_HIGH` | dự phòng cho vai **D** | **168–182 Hz** (nam cao) | để audio clone ra ≥ 164 Hz, cách vai H (130 Hz) ≥ 4 nửa cung |
| `M_LOW` | dự phòng cho vai **H** | **80–92 Hz** (nam rất trầm) | để audio clone ra ≤ 96 Hz, cách vai D (121 Hz) ≥ 4 nửa cung. Hợp mô tả nhân vật "deep chesty resonance" |
| `W5_HIGH` | vai **N1** | **258–276 Hz** (nữ cao) | để audio clone ra ≥ 258 Hz, cách vai C (205 Hz) ≥ 4 nửa cung |

Cả 3 bộ đều **dự phòng** — sau khi có clip, tôi sẽ đo lại trên Kaggle (audio clone thật) rồi mới chốt
vai nào dùng clip nào. Sinh cả 3 giúp tránh phải quay lại Mac mini lần nữa.

## 3. Cách chạy

Trong terminal trên **Mac mini**, tại thư mục repo `amber-eyes`:

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py
```

Script sẽ tự:

1. nạp VoxCPM2 trên MPS;
2. sinh tối đa 5 take cho mỗi bộ, dừng sớm nếu có take nào F0 nằm trong dải mục tiêu;
3. tự chọn take có F0 sát giữa dải nhất;
4. đóng gói sang WAV **24 kHz mono, −18 LUFS** (đúng chuẩn `QUY_TAC_AUDIO_HIGGS.md` §4);
5. in ra bảng F0 từng take.

**Kiểm tra trước khi commit** — màn hình phải có dạng:

```
M_HIGH   ... CHON: M_HIGH_take0N.wav (F0 xxx.x Hz)
M_LOW    ... CHON: M_LOW_take0N.wav  (F0 xxx.x Hz)
W5_HIGH  ... CHON: W5_HIGH_take0N.wav (F0 xxx.x Hz)
```

Nếu một bộ **không** có take nào trong dải (in `[LECH]` hết), **vẫn chạy tiếp** — tôi sẽ xử lý.

## 4. Gửi lại cho tôi

```bash
git add assets/voice_ref_voxcpm2_g9
git commit -m "feat(audio): them 3 clip tham chieu VoxCPM2 cho G9 (Tap 02)"
git push
```

> Thư mục `assets/voice_ref_voxcpm2_g9_raw/` (bản 48 kHz trung gian) đã được `.gitignore` — **không** commit,
> chỉ cần bản 24 kHz trong `assets/voice_ref_voxcpm2_g9/`.

## 5. Tôi làm gì tiếp

1. Đưa 3 clip mới vào dataset Kaggle → chạy **pilot v5** (đo F0 audio clone + CER cho từng clip, 2 lượt ASR).
2. Chốt ánh xạ vai: `H ← ?` · `D ← ?` · `N1 ← W5_HIGH` · `N2 ← W1` · `C ← C.wav`.
3. H3: nghe mù V7 (H↔D, H↔W4, D↔W4, W2↔C) + G8.
4. Sinh 203 câu Tập 02 (3 bản/câu) → **H4** (đọc 1 hồi + mix + QC).

> ⛔ Theo quyết định của bạn: **dừng trước H4** cho tới khi chốt được phần **ghi công Boson**.
> Bước 1–3 không phát ra audio sản xuất nên vẫn làm được bình thường.

## 6. File liên quan

| File | Vai trò |
|---|---|
| `.work/voxcpm_generate_g9.py` | **Script chạy trên Mac mini** (sinh + đóng gói 1 lệnh) |
| `.work/voxcpm_refs_manifest_g9.json` | Mô tả giọng + văn bản + dải F0 của 3 clip mới |
| `.work/voxcpm_generate_all.py` | Script gốc tạo 7 clip (để tham khảo) |
| `.work/higgs_make_refs_voxcpm.py` | Script đóng gói 7 clip gốc (để tham khảo) |
| `90_LUU_TRU/BaoCao_H2_Higgs_Pilot_Tap02_20261030.md` | Báo cáo H2 (mục 6 & 7 nói về 2 lỗi G9 này) |
