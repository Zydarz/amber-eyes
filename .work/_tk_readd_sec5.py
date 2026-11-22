# -*- coding: utf-8 -*-
"""Them lai muc 5 (anh nen doc) vao KE_HOACH_CLIP_TAP03.md sau khi chay lai generator."""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
p = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK", "Tap03", "KE_HOACH_CLIP_TAP03.md")

SEC = """
---

## 5. Ảnh nền dọc — đã dựng 20/11/2026

*Chi tiết đo thật + bẫy gặp được: `02_SAN_XUAT/TIKTOK/Tap03/BAO_CAO_ANH_NEN_DOC_TAP03.md`*

| Hạng mục | Số đo |
|---|---|
| Số nền dọc | **28/28** · 1080×1920 đúng 28/28 · phủ **51/51 shot** (TK1 10 · TK2 10 · TK3 11 · TK4 11 · TK5 9) |
| Nguồn | **12 AI thật** (MiniMax `generate_image`, 9:16, 2K) + **16 dự phòng** crop từ ảnh 16:9 gốc (`t3_*`) — allowance hết ở lô 3 (lỗi 402) |
| Vùng chữ | hook mean **45,1** (≤ 58) · sub mean **53,4** (≤ 72) · **0** vệt sáng ngang |
| provenance.json | **28** dòng (12 có `prompt` · 16 `prompt: null` = dự phòng) |
| QC mắt | Soi **100 %** 28 nền + 2 tờ zoom 1:1 → đúng phong cách graphic-noir, **0 mặt lộ**, **0 chữ lạ** |

Cột **Nền** ở mục 2.1–2.5 và trường `bg` trong `SPEC_AUDIO_CLIP_TAP03.json` (VN/EN/JA) trỏ tới **`tk03_*`** — đúng ảnh dọc 9:16 trong `assets/bg/`. Ánh xạ sang ảnh gốc 16:9 nằm trong `NEN_SRC` của `.work/_build_tk_tap03.py` (`tk03_x` → `t3_x`).

Cần nâng 16 nền dự phòng thành AI thật → bật **Settings → Usage & model → Credits → credit auto-consumption** rồi chạy `.work/_tk_gen_bg_extra_t03.py` → `_tk_download_imgs_t03.py` → `_tk_postprocess_t03.py`.
"""

s = io.open(p, encoding="utf-8").read()
if "## 5. Ảnh nền dọc" in s:
    print("muc 5 da co - khong them")
    sys.exit(0)
s = s.rstrip("\n") + "\n" + SEC
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("da them muc 5 vao", p)
