#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat muc VI.6 (keim ke anh theo tap) trong bao cao 68 tap — dung anchor ngan."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / "BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md"
lines = MD.read_text(encoding="utf-8").split("\n")
changed = 0

def sub_line(pred, new_text, label):
    global changed
    hits = [i for i, l in enumerate(lines) if pred(l)]
    assert len(hits) == 1, ("anchor khong duy nhat: %s (%d hit)" % (label, len(hits)))
    lines[hits[0]] = new_text
    changed += 1
    print("  OK:", label)

# 1. Dong mo ta do
sub_line(lambda l: l.startswith("- **Đo lại 26/11/2026:** `assets/bg/` có **4,253 file PNG**"),
         "- **Đo lại 27/11/2026:** `assets/bg/` có **4.622 file ảnh** ở gốc + `_raw/` (590 file), `_gemini_backup/` (3), `outputs/` (150, toàn `t15_*`) ⇒ **5.365 file**. Trong 4.622 ảnh gốc: **4.389 ảnh theo tiền tố tập** + 233 ảnh tên cũ không theo tập (`bedroom_door.png`, `cage.png`, `deedee_room.png`…). Đếm theo tiền tố tập và đối chiếu `bg_jobs_tapXX.json`.",
         "dong do 4,253 -> 4.622")

# 2. Tap co du anh
sub_line(lambda l: l.startswith("- **Tập có đủ ảnh theo job (đo 26/11):**"),
         "- **Tập có đủ ảnh theo job (đo 27/11):** **10–30, 36, 37, 38, 39, 40, 41, 42** (28 tập — đủ 100 %). *[25/11: thêm Tập 26 và Tập 40 — xem mục VII; 26/11: thêm Tập 37, 38, 39 — xem mục VIII; **27/11: thêm Tập 41, 42 — xem mục IX.1**]*",
         "danh sach tap du anh")

# 3. Tap thieu mot phan (them dong moi sau dong hien tai)
i = [k for k, l in enumerate(lines) if l.startswith("- **Tập thiếu một phần:**")]
assert len(i) == 1
lines.insert(i[0] + 1, "- **27/11/2026 — Tập 43 (Suzane von Richthofen) mới có 2/159 ảnh**: đợt Cloudflare 26/11 bị dừng giữa chừng ⇒ còn thiếu **157 ảnh** (xem mục IX.1).")
changed += 1
print("  OK: them dong tap thieu mot phan (Tap 43)")

# 4. Tap chua co anh
sub_line(lambda l: "30 tập, cần sinh 4,622 ảnh" in l,
         "  - **Có `bg_jobs` hợp lệ nhưng chưa đủ ảnh (28 tập, cần sinh 4,253 ảnh):** 31, 32, 33, 34, 35, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 67.",
         "danh sach tap thieu anh")
sub_line(lambda l: l.startswith("  - *[26/11/2026: Tập 37, 38, 39 đã sinh đủ bằng Cloudflare"),
         "  - *[26/11/2026: Tập 37, 38, 39 đã sinh đủ bằng Cloudflare — xem mục VIII; Tập 36 đã đủ 157 ảnh. **27/11/2026: Tập 41 (157) và Tập 42 (210) đã sinh đủ bằng Cloudflare — xem mục IX.1; Tập 43 mới có 2/159.**]*",
         "chu thich tap 41/42/43")
sub_line(lambda l: l.strip() == "- **Chưa có `bg_jobs` (3 tập):** 64, 66, 68.",
         "  - **Chưa có `bg_jobs` (3 tập):** 64, 66, 68. **Tập 69 (mới 27/11/2026) cũng chưa lập `bg_jobs`.**",
         "chu thich tap 64/66/68/69")

# 5. Cac dong trong bang keim ke
def bang_row(tap, neu, ghichu):
    hits = [k for k, l in enumerate(lines) if l.startswith("| %d | " % tap)]
    assert len(hits) == 1, ("row tap %d khong duy nhat" % tap, hits)
    lines[hits[0]] = "| %d | %s | %s | %s |" % (tap, neu, ghichu, "")
    print("  OK: dong bang tap", tap)

bang_row(41, "157", "**157**")
lines[[k for k, l in enumerate(lines) if l.startswith("| 41 | ")][0]] = "| 41 | 157 | **157** | ✔ đã đủ ảnh (27/11, Cloudflare FLUX) |"
lines[[k for k, l in enumerate(lines) if l.startswith("| 42 | ")][0]] = "| 42 | 210 | **210** | ✔ đã đủ ảnh (27/11, Cloudflare FLUX) |"
lines[[k for k, l in enumerate(lines) if l.startswith("| 43 | ")][0]] = "| 43 | 159 | **2** | ⚠ đợt Cloudflare 26/11 bị dừng — còn thiếu 157 ảnh |"
changed += 3

MD.write_text("\n".join(lines), encoding="utf-8")
print("da ghi:", MD, "| so dong sua:", changed)
