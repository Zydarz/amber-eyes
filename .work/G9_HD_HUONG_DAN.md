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

| Vai | F0 của **clip tham chiếu** | F0 của **audio đã sinh ra** | Khoảng cách | Yêu cầu | Kết luận |
|---|---:|---:|---:|---:|---|
| **H** | 108 Hz | **130 Hz** | — | — | — |
| **D** | 128 Hz | **121 Hz** | **0,23 nửa cung** | ≥ 4 | ❌ **TRƯỢT** |

Hai vai gần như **cùng cao độ**. Người xem sẽ lẫn.

### 1.3 Tại sao lệch như vậy — đây là mấu chốt

> **Higgs bắt chước CHẤT GIỌNG của clip mẫu (âm sắc, chất tạp âm) nhưng KHÔNG bắt chước CAO ĐỘ.**
> Nó tự chọn cao độ theo cách *nó* thấy hợp tự nhiên. Với giọng nam, Higgs luôn chọn quanh **120–130 Hz**.

Chứng cứ (đo được ở 4 vai):

| Vai | Clip gốc | Audio clone | Lệch | Higgs làm gì |
|---|---:|---:|---:|---|
| H | 108 Hz | 130 Hz | **+20%** | đẩy **LÊN** |
| D | 128 Hz | 121 Hz | **−8%** | đẩy **XUỐNG** |
| C | 210 Hz | 205 Hz | −4% | giữ gần như nguyên |
| N1 ← W1 | 253 Hz | 245 Hz | −3% | giữ gần như nguyên |

⇒ Hai clip nam 108 Hz và 128 Hz (cách nhau 20 Hz) **bị kéo về cùng một chỗ ~125 Hz**.

**Hệ quả quan trọng:** *không thể sửa bằng cách chỉnh tham số lúc đọc* (temperature, seed, …).
Phải **đổi chính clip tham chiếu**.

### 1.4 Vậy cần con số bao nhiêu

Tính từ số đo thật (giữ H ở 130 Hz, D ở 121 Hz):

| Muốn | Điều kiện | Nghĩa là |
|---|---|---|
| **Nâng D lên** | D ≥ 130 × 1,26 = **≥ 164 Hz** | clip tham chiếu của D phải cao hơn ~170 Hz |
| **Hạ H xuống** | H ≤ 121 / 1,26 = **≤ 96 Hz** | clip tham chiếu của H phải thấp hơn ~85 Hz |
| **Nâng N1 lên** (cách C 205 Hz) | N1 ≥ 205 × 1,26 = **≥ 258 Hz** | clip tham chiếu của N1 phải ~265 Hz |

**Hai hướng cho H↔D — hãy chọn theo mô tả nhân vật:**

| Hướng | Clip mới cho ai | Kết quả dự kiến | Khớp nhân vật? |
|---|---|---|---|
| **A** | `M_LOW` (nam rất trầm) cho **H**, giữ `D.wav` cho D | H ~90 Hz ⇒ cách D (121) ≈ 5,1 nc | ✅ **H tốt hơn** — vai H vốn được mô tả *"low-pitched, deep chesty resonance"*; vai D giữ nguyên *"late fifties, gravelly"* |
| **B** | giữ `H.wav` cho H, `M_HIGH` (nam cao) cho **D** | D ~168 Hz ⇒ cách H (130) ≈ 4,4 nc | ⚠ vai D thành tenor cao, lệch *"late fifties, gravelly"* |

⇒ **Ưu tiên hướng A.** Vì vậy script sinh **cả hai** bộ (`M_LOW` + `M_HIGH`) — đo xong mới chốt.

### 1.5 Về vai N1

| Cặp | MiniMax (bộ đang chạy) | Higgs hiện tại | Cần |
|---|---:|---:|---:|
| C ↔ N1 | 3,07 nc (đã trượt) | 3,07 nc | ≥ 4 |
| C ↔ N2 | 1,78 nc (đã trượt) | **5,13 nc ✅** | ≥ 4 |
| N1 ↔ N2 | 1,3 nc | 2,03 nc | hai vai này **không hồi nào cùng xuất hiện** |

Nên `N1 ← W5_HIGH` (clip nữ ~265 Hz) để C↔N1 lên ~4,3 nc.
Hệ quả: N1 (262 Hz) và N2 (276 Hz) sẽ gần nhau (~1 nc) — **giống hệt** bộ MiniMax hiện tại (1,3 nc),
và hai vai này không bao giờ cùng hồi (N1 ở hồi 1, N2 ở hồi 4) nên người nghe không gặp nhau.

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
| `W5_HIGH` (cho N1) | 258–276 Hz | `very high-pitched` → `high-pitched` → `soprano` |

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
  => DONG GOI assets/voice_ref_voxcpm2_g9/M_LOW.wav (24 kHz mono, F0 87.3 Hz)
```

Rồi commit:

```bash
git add assets/voice_ref_voxcpm2_g9
git commit -m "feat(audio): them 3 clip tham chieu VoxCPM2 cho G9 (Tap 02)"
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

1. Tôi đưa 3 clip mới vào dataset Kaggle → **pilot v5**: đo F0 của audio clone + CER (2 lượt ASR).
2. Chốt ánh xạ vai dựa trên **số đo thật** (không đoán):
   `H ← H.wav | M_LOW` · `D ← D.wav | M_HIGH` · `C ← C.wav` · `N1 ← W5_HIGH` · `N2 ← W1`
3. **H3**: nghe mù V7 (H↔D, H↔W4, D↔W4, W2↔C) + G8 ổn định danh tính.
4. Sinh 203 câu (3 bản/câu) → **H4** *(đang dừng chờ bạn chốt phần ghi công Boson)*.

---

## File liên quan

| File | Vai trò |
|---|---|
| `.work/voxcpm_generate_g9.py` | **Script chạy trên Mac mini** (dò thang + đóng gói 24 kHz) |
| `.work/voxcpm_refs_manifest_g9.json` | Mô tả giọng + thang `control` + dải F0 của 3 clip mới |
| `.work/DAT_SPEC_G9.md` | Đặc tả ngắn (bản này là bản giải thích đầy đủ) |
| `90_LUU_TRU/BaoCao_H2_Higgs_Pilot_Tap02_20261030.md` | Báo cáo H2 — mục 6 & 7 mô tả 2 lỗi G9 này |
| `.work/voxcpm_generate_all.py` | Script gốc tạo 7 clip (để đối chiếu cách dùng) |
