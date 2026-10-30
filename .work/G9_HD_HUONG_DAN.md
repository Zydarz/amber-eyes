# Làm lại ở Vox — G9 H↔D (tách 2 vai nam) + vai N1

**Ngày:** 30/10/2026 · **Người chạy:** bạn, trên **Mac mini** · **Số lệnh: 1**

---

## PHẦN 1 — Hiểu vấn đề trong 5 phút

### 1.1 "Tách 2 vai nam" nghĩa là gì

Tập 02 có 3 vai chính: **H** (người dẫn chuyện, nam), **D** (thám tử, nam), **C** (chuyên gia tâm lý, nữ).
Người xem phải **nghe mà biết câu đó ai đang nói**, chỉ bằng giọng.

Luật **G9** trong `AGENTS.md` đặt ngưỡng: hai giọng cùng giới phải cách nhau **≥ 4 nửa cung**.
4 nửa cung ≈ giọng thấp hơn 1,26 lần. Ví dụ: 130 Hz và 164 Hz là đúng 4 nửa cung.

### 1.2 Hiện trạng đo được (số thật, không phải ước lượng)

Đo lại toàn bộ **192 audio** của pilot v3 + pilot v4 (2 thuật toán F0: AC thô và AC chuẩn hóa + parabolic).
Mỗi ô vai × clip có **n = 16** (C/D/H) hoặc **n = 8** (N1/N2).

| Vai | F0 của **clip tham chiếu** | F0 của **audio đã sinh ra** | Khoảng cách | Yêu cầu | Kết luận |
|---|---:|---:|---:|---:|---|
| **H** | 108 Hz | **131 Hz** | — | — | — |
| **D** | 128 Hz | **122 Hz** | **1,19 nc** (AC thô) · **0,01 nc** (AC chuẩn hóa) | ≥ 4 | ❌ **TRƯỢT** |

Hai vai gần như **cùng cao độ**. Người xem sẽ lẫn.

### 1.3 Tại sao lệch như vậy — đây là mấu chốt

> **Higgs bắt chước CHẤT GIỌNG của clip mẫu (âm sắc, chất tạp âm) nhưng KHÔNG bắt chước CAO ĐỘ 1-1.**
> Một clip cao hơn 20 Hz **không** bảo đảm audio clone cao hơn 20 Hz.

Chứng cứ (đo được ở 9 tổ hợp vai × clip, cả 2 bộ pilot):

| Vai | Clip gốc | Audio clone | Lệch | Higgs làm gì |
|---|---:|---:|---:|---|
| H | 107 Hz | 131 Hz | **+22%** | đẩy **LÊN** |
| D | 132 Hz | 122 Hz | **−7%** | đẩy **XUỐNG** |
| C | 200 Hz | 205 Hz | +3% | giữ gần như nguyên |
| N1 ← W1 | 235 Hz | 247 Hz | +5% | giữ gần như nguyên |
| N1 ← W2 | 189 Hz | 197 Hz | +4% | giữ gần như nguyên |
| N1 ← W3 | 157 Hz | 157 Hz | 0% | giữ gần như nguyên |
| N2 ← W1 | 235 Hz | 276 Hz | **+17%** | đẩy **LÊN** |
| N2 ← W2 | 189 Hz | 207 Hz | +9% | đẩy lên nhẹ |
| N2 ← W3 | 157 Hz | 171 Hz | +9% | đẩy lên nhẹ |

⇒ Tỉ lệ **clone / clip gốc** dao động **0,93 → 1,22**. Không có quy luật nào để suy ra chắc chắn.
Đó là lý do mọi con số trong tài liệu này đều phải **đo lại**, không được suy đoán.

**Hệ quả quan trọng:** *không thể sửa bằng cách chỉnh tham số lúc đọc* (temperature, seed, …).
Phải **đổi chính clip tham chiếu**, rồi **đo lại bằng pilot** mới chốt.

### 1.4 Vậy cần con số bao nhiêu

Tính từ số đo thật (giữ H ở 131 Hz, D ở 122 Hz, C ở 205 Hz, N2 ← W1 ở 276 Hz):

| Muốn | Điều kiện | Nghĩa là clip tham chiếu phải ở |
|---|---|---|
| **Hạ H xuống** | H ≤ 122 / 1,26 = **≤ 97 Hz** | khoảng **70–100 Hz** (→ `M_LOW`) |
| **Nâng D lên** | D ≥ 131 × 1,26 = **≥ 165 Hz** | khoảng **150–190 Hz** (→ `M_HIGH`) |
| **Hạ N1 xuống** | N1 ≤ 205 / 1,26 = **≤ 163 Hz** | khoảng **140–175 Hz** (→ `W6_LOW`) |

**Hai hướng cho H↔D — hãy chọn theo mô tả nhân vật:**

| Hướng | Clip mới cho ai | Kết quả dự kiến | Khớp nhân vật? |
|---|---|---|---|
| **A** | `M_LOW` (nam rất trầm) cho **H**, giữ `D.wav` cho D | H ~90 Hz ⇒ cách D (122) ≈ 5,1 nc | ✅ **H tốt hơn** — vai H vốn được mô tả *"low-pitched, deep chesty resonance"*; vai D giữ nguyên *"late fifties, gravelly"* |
| **B** | giữ `H.wav` cho H, `M_HIGH` (nam cao) cho **D** | D ~168 Hz ⇒ cách H (131) ≈ 4,4 nc | ⚠ vai D thành tenor cao, lệch *"late fifties, gravelly"* |

⇒ **Ưu tiên hướng A.** Vì vậy script sinh **cả hai** bộ (`M_LOW` + `M_HIGH`) — đo xong mới chốt.

### 1.5 Vai N1 — đây là chỗ đã sửa lại sau khi đo đủ số liệu

> **Cảnh báo:** bản đầu tiên của tài liệu này chọn `W5_HIGH` (nữ ~265 Hz) cho N1.
> Đo lại đủ cặp thì thấy cách đó **tạo ra một vi phạm G9 mới**. Chi tiết bên dưới.

Tập 02 có **3 vai nữ**: C (chuyên gia), N1 (người kể thứ nhất), N2 (người kể thứ hai).
Luật G9 áp dụng cho **mọi cặp cùng giới**, tức là **3 cặp**: C↔N1 · C↔N2 · **N1↔N2**.
(Cặp N1↔N2 trước đây **chưa từng được kiểm** — đây là lý do phát hiện ra vấn đề.)

Số đo thật (n = 8 mỗi ô, cả 2 bộ pilot):

| Cặp | N1 ← W1 | N2 ← W1 | Kết luận |
|---|---:|---:|---|
| C ↔ N1 (C = 205 Hz) | 3,25 nc | | ❌ trượt |
| C ↔ N2 (C = 205 Hz) | | 5,13 nc | ✅ đạt |
| **N1 ↔ N2** (cả hai ← W1) | | | **1,89 nc ❌ trượt** |

Nếu đưa N1 lên `W5_HIGH` (258–276 Hz) để sửa C↔N1, thì **N1 sẽ áp sát N2** (276 Hz) —
khoảng cách rơi về **~1,7 nc**, tức là **một vi phạm G9 mới**, chỉ đổi tên người vi phạm.

**Cách sửa đúng:** vì C đã ở 205 Hz và N2 đã ở 276 Hz (cách nhau 5,13 nc ✅), nên N1
**không thể nằm giữa** — nó phải nằm **dưới 163 Hz**. Đó là lý do cần clip **nữ trầm** `W6_LOW`,
**không phải** clip nữ cao.

| Phương án | C ↔ N1 | C ↔ N2 | N1 ↔ N2 | Clip mới cần |
|---|---:|---:|---:|---|
| **A (khuyến nghị)** N1 ← `W6_LOW` (~155 Hz), N2 ← `W1` | 4,6–4,8 ✅ | 4,9–5,1 ✅ | 9,5–9,8 ✅ | **1 clip nữ trầm** |
| B N1 ← `W5_HIGH` (~265 Hz), N2 ← `W6_LOW` | 4,0 ⚠ | 4,6–4,8 ✅ | 9,5–9,8 ✅ | **1 clip nữ cao + 1 clip nữ trầm** |
| C giữ nguyên N1 ← W1, N2 ← W1 | 3,25 ❌ | 5,13 ✅ | 1,89 ❌ | không đạt G9 |

⇒ Script sinh **cả `W5_HIGH` lẫn `W6_LOW`** để bạn chọn sau khi đo. Nếu theo khuyến nghị:
chỉ cần `W6_LOW` cho N1, `N2` giữ `W1` (đã có sẵn, CER 0,63% ✅).

---

## PHẦN 2 — Làm lại ở Vox (VoxCPM2)

### 2.1 Cơ chế: từ khoá trong `control` điều khiển cao độ

VoxCPM2 Voice Design sinh clip mẫu từ **câu mô tả** (trường `control`). Từ khoá cao độ trong câu mô tả
quyết định cao độ. Đây là bảng **đo thật** từ 7 clip hiện có:

| Giới | Câu mô tả có cụm từ | F0 đạt được |
|---|---|---:|
| nam | *"**low-pitched** and warm with a deep chesty resonance"* (H) | 108 Hz |
| nam | *"**mid-low-pitched**, rough and gravelly"* (D) | 128 Hz |
| nam | *"**lower mid-pitched** and slightly rough"* (W4) | 137 Hz |
| nam | *"**medium-pitched** and clear with a light youthful timbre"* (W3) | 162 Hz |
| nữ | *"**mid-pitched** and soft"* (W2) / *"mid-pitched and clear"* (C) | 200 / 210 Hz |
| nữ | *"**higher-pitched** and bright"* (W1) | 253 Hz |

⇒ **Để lên cao hơn:** dùng `higher-pitched` → `high-pitched` → `soprano`.
⇒ **Để xuống thấp hơn:** dùng `very low-pitched` → `bass` → `sub-bass`.

### 2.2 Script đã dựng sẵn — dò thang tự động

Với mỗi vai, script thử lần lượt các biến thể `control` **từ nhẹ đến mạnh**, sinh 1 take mỗi bậc,
đo F0, và **dừng ngay** khi có take nào nằm trong dải mục tiêu. Nếu hết thang mà chưa trúng,
nó sinh thêm take của bậc gần nhất.

| Vai | Dải F0 clip | Bậc thang `control` (nhẹ → mạnh) |
|---|---|---|
| `M_LOW` (cho H) | 80–92 Hz | `very low-pitched` → `bass` → `sub-bass` |
| `M_HIGH` (cho D) | 168–182 Hz | `upper mid-pitched` → `higher-pitched` → `high-pitched` |
| `W6_LOW` (cho N1, **khuyến nghị**) | 148–162 Hz | `lower mid-pitched` → `low-pitched` → `alto` |
| `W5_HIGH` (cho N1, phương án B) | 258–276 Hz | `very high-pitched` → `high-pitched` → `soprano` |

### 2.3 Chạy

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py
```

Màn hình mong đợi:

```
--- M_LOW  (muc tieu F0 80-92 Hz) ---
  > [very-low] M_LOW_very-low_take01.wav (seed=42, cfg=2.0)... 38s | 24.1s | F0 87.3 Hz [TRONG DAI]
  => DUNG trong dai, dung tai day: M_LOW_very-low_take01.wav
  => DONG GOI assets/voice_ref_voxcpm2_g9/M_LOW.wav (24 kHz mono, 24.1s, F0 87.3 Hz)
```

Rồi commit:

```bash
git add assets/voice_ref_voxcpm2_g9
git commit -m "feat(audio): them 4 clip tham chieu VoxCPM2 cho G9 (Tap 02)"
git push
```

### 2.4 Nếu KHÔNG trúng dải F0

Không sao — script vẫn xuất clip gần nhất và in cảnh báo. Khi đó báo lại tôi, tôi sẽ:
1. tính lại ngưỡng G9 bằng **số đo thật** của clip vừa tạo (vì drift Higgs không tuyến tính),
2. nếu cần, bổ sung thêm bậc thang mới vào `control_variants` trong
   `.work/voxcpm_refs_manifest_g9.json` rồi bạn chạy lại (chỉ mất vài phút).

### 2.5 Nếu bạn muốn tự chỉnh tay

Mở `.work/voxcpm_refs_manifest_g9.json`, sửa `control_variants` (thêm/xoá bậc), sửa `f0_target`,
rồi chạy lại lệnh trên. Chỉ cần giữ đúng cấu trúc:

```json
"control_variants": [
  { "tag": "ten-ngan", "control": "..." },
  { "tag": "ten-ngan-2", "control": "..." }
]
```

---

## PHẦN 3 — Sau khi có clip

1. Tôi đưa clip mới vào dataset Kaggle → **pilot v5/v6**: đo F0 của audio clone + CER (2 lượt ASR).
2. Chốt ánh xạ vai dựa trên **số đo thật** (không đoán). Bảng ứng viên:
   - H ← `H.wav` **hoặc** `M_LOW` (hướng A, khuyến nghị)
   - D ← `D.wav` **hoặc** `M_HIGH` (hướng B)
   - C ← `C.wav` (giữ nguyên — đã đạt CER 0% và cách H/D rất xa)
   - N1 ← `W6_LOW` (khuyến nghị) **hoặc** `W5_HIGH` + N2 ← `W6_LOW`
   - N2 ← `W1` (giữ nguyên — CER 0,63%, C↔N2 = 5,13 nc)
3. **H3**: nghe mù V7 (H↔D, H↔W4, D↔W4, W2↔C) + G8 ổn định danh tính.
4. Sinh 203 câu (3 bản/câu) → **H4** *(đang dừng chờ bạn chốt phần ghi công Boson)*.

---

## File liên quan

| File | Vai trò |
|---|---|
| `.work/voxcpm_generate_g9.py` | **Script chạy trên Mac mini** (dò thang + đóng gói 24 kHz) |
| `.work/voxcpm_refs_manifest_g9.json` | Mô tả giọng + thang `control` + dải F0 của **4** clip mới |
| `.work/DAT_SPEC_G9.md` | Đặc tả ngắn (bản này là bản giải thích đầy đủ) |
| `90_LUU_TRU/BaoCao_H2_Higgs_Pilot_Tap02_20261030.md` | Báo cáo H2 — mục 6 & 7 mô tả 2 lỗi G9 này |
| `.work/voxcpm_generate_all.py` | Script gốc tạo 7 clip (để đối chiếu cách dùng) |
| `.work/kaggle_higgs/_g9_matrix.py` | Script dựng bảng G9 đầy đủ từ 192 audio pilot v3+v4 (chạy lại được) |
| `.work/kaggle_higgs/g9_matrix.json` | Kết quả bảng G9 (số đo thật) |
