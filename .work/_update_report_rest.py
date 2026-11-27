#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat cac muc con lai + them muc IX vao bao cao 68 tap (27/11/2026)."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / "BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md"
lines = MD.read_text(encoding="utf-8").split("\n")
n = 0

def sub(pred, new, label, count=1):
    global n
    hits = [i for i, l in enumerate(lines) if pred(l)]
    assert len(hits) == count, ("anchor %s: %d hit (can %d)" % (label, len(hits), count))
    lines[hits[0]] = new
    n += 1
    print("  OK:", label)

# ---------- A. Bang muc II: Tập 42 ----------
sub(lambda l: l.startswith("| **Tap 42**"),
    "| **Tap 42** | Hồ Sơ Tsutomu Miyazaki — Căn Phòng 5.000 Cuốn Băng & Vực Thẳm Tách Rời Thực Tại | Nhật Bản | **240** | **210** | **245** | Quy tắc chuẩn (240 câu + 5 thẻ chuyển/kết) · **27/11: có 210 file ảnh NHƯNG cổng H27 TRƯỢT** — `bg_jobs_tap42.json` là bộ mẫu chung chưa viết lại ⇒ **chưa dùng được cho dựng** (xem mục IX.1) |",
    "dong Tap 42 (muc II)")

# ---------- B. Muc V ----------
sub(lambda l: l.strip().startswith("- **Đã có ảnh nền và đủ theo job (28/68 tập - 41.2%):**"),
    "   - **Đã có ảnh nền đủ file VÀ mapping ĐẠT (27/69 tập - 39.1%):**",
    "muc V - danh sach tap du anh")
sub(lambda l: l.strip().startswith("- Gồm: **Tap 10 → Tap 30**, **Tap 36, Tap 37, Tap 38, Tap 39, Tap 40, Tap 41, Tap 42**"),
    "     - Gồm: **Tap 10 → Tap 30**, **Tap 36, Tap 37, Tap 38, Tap 39, Tap 40, Tap 41** (liên tục 10–30, rồi 36–41).",
    "muc V - gom tap")
sub(lambda l: l.strip().startswith("- Tổng cộng **4.389 ảnh graphic novel noir**"),
    "     - Tổng cộng **4.389 ảnh graphic novel noir** theo tiền tố tập trên ổ cứng, đã kiểm định bản quyền `provenance.json` (**7.078 bản ghi**).",
    "muc V - tong cong anh (gia tri giu nguyen)")
sub(lambda l: l.strip().startswith("- **Tap 30 (Nguyễn Đức Nghĩa)** đã đủ"),
    "     - **Tap 30 (Nguyễn Đức Nghĩa)** đã đủ **204 ảnh** = số job; **Tap 37/38/39 đã đủ 122/188/135 ảnh** (đợt Cloudflare 25–26/11 — xem mục VIII); **Tap 41 mới đủ 157/157 ảnh** và **cổng `--check 41` ĐẠT** (đợt Cloudflare 26/11 — xem mục IX.1).",
    "muc V - ghi chu tap 30/37/38/39/41")
sub(lambda l: l.strip().startswith("- **Chưa đủ ảnh nền (40/68 tập - 58.8%):**"),
    "   - **Có đủ file ảnh nhưng mapping TRƯỢT (1 tập):** **Tap 42** — 210 file ảnh tồn tại nhưng `bg_jobs_tap42.json` là **bộ mẫu chung chưa viết lại** ⇒ phải sinh lại (mục IX.1).",
    "muc V - tap 42")
sub(lambda l: l.strip().startswith("- Gồm: **Tap 01–09** (ảnh gốc còn nằm trong `assets/bg/_raw/`"),
    "   - **Chưa đủ ảnh nền (41/69 tập - 59.4%):**\n     - Gồm: **Tap 01–09** (ảnh gốc còn nằm trong `assets/bg/_raw/`, không theo tiền tố `tNN_`), **Tap 31–35**, **Tap 43–63** (Tap 43 mới có 2/159 ảnh), **Tap 65, Tap 67**, **Tap 64, 66, 68** (chưa có `bg_jobs`) và **Tap 69** (mới 27/11).",
    "muc V - tap chua du anh")
sub(lambda l: l.strip().startswith("- **Số lượng ảnh cần sản xuất bổ sung:** **4.253 ảnh** cho 28 tập"),
    "     - **Số lượng ảnh cần sản xuất bổ sung:** **4.463 ảnh** cho **29 tập** (31, 32, 33, 34, 35, 42, 43–63, 65, 67) — trong đó **210 ảnh của Tập 42 là ảnh phải sinh lại** (file hiện có là bộ mẫu chung, không dùng được).",
    "muc V - tong anh can sinh")

# ---------- C. Muc IV ----------
sub(lambda l: l.strip().startswith("- **4,253 file ảnh nền graphic novel noir**"),
    "   - **4.622 file ảnh nền graphic novel noir** lưu tại `assets/bg/` (đo 27/11/2026) — 4.389 ảnh theo tiền tố tập; khớp tuyệt đối với bảng shot của các tập đã có ảnh **và mapping ĐẠT** (Tập 42 là ngoại lệ — xem mục IX.1).",
    "muc IV - so file anh nen")

# ---------- D. Muc VI.1 ----------
sub(lambda l: l.strip().startswith("- **Đạt (39 tập):** 26–48, 50–63, 65, 67"),
    "- **Đo lại 27/11/2026 — Đạt (36 tập):** 26–41, 43, 46–63, 65, 67 (mã câu hợp lệ, prompt không trùng, phủ 100% câu).",
    "muc VI.1 - danh sach DAT")
sub(lambda l: l.strip().startswith("- **Trượt:** Tập 49 (98/146 mã câu sai"),
    "- **Đo lại 27/11/2026 — Trượt (3 tập):**\n"
    "  - **Tập 42** (Tsutomu Miyazaki): M1 **130/210 mã sai** · M5 **208/215 câu chưa phủ** · M4 **114/210 MẪU CHUNG** — `bg_jobs_tap42.json` là bộ mẫu chung tạo 26/11, **chưa viết lại** (mục IX.1).\n"
    "  - **Tập 44** (Suzane von Richthofen): M1 **178/175 mã sai** · M5 **205/240 câu chưa phủ**.\n"
    "  - **Tập 45** (Lâm Quá Vân): M1 **81/174 mã sai** · M5 **147/240 câu chưa phủ**.\n"
    "  - *[Đính chính 25/11: Tập 49 trượt do đo nhầm file `…_backup_61cau.md`; đã viết lại toàn bộ 190 prompt — nay **ĐẠT**, xem VI.7.]*\n"
    "- **Chưa có `bg_jobs`:** Tập 64, 66, 68. Ba tập này **bị loại khỏi mapping** theo quyết định của người dùng. **Tập 69 (mới 27/11/2026) cũng chưa lập `bg_jobs`.**",
    "muc VI.1 - danh sach TRUOT")

# ---------- E. Muc VI.8: trang thai --check ----------
sub(lambda l: l.strip().startswith("- **Hiện `--check` ĐẠT:** Tập 26 (176/176 ảnh)"),
    "- **Hiện `--check` ĐẠT:** Tập 26 (176/176 ảnh) · Tập 27–30 (đủ ảnh) · Tập 36 (157/157) · **Tập 37 (122/122)** · **Tập 38 (188/188)** · **Tập 39 (135/135)** · Tập 40 (154/154 ảnh) — 26/11/2026. **27/11/2026:** Tập 41 **ĐẠT** (157 shot · lỗi mapping 0 · bảng không cũ · ảnh thiếu 0) · Tập 25 **ĐẠT** (139 shot) · **Tập 42 TRƯỢT — 216 lỗi mapping** (`bg_jobs` là bộ mẫu chung) · Tập 43 TRƯỢT (thiếu 157 ảnh). **TRƯỢT vì thiếu ảnh:** Tập 49 (190) và các tập chưa sinh ảnh — đây là việc người dùng sinh ảnh, mapping không lỗi.",
    "muc VI.8 - trang thai --check")

# ---------- F. Muc VII.6: tong so anh can sinh ----------
sub(lambda l: l.strip().startswith("- **[26/11/2026 — cập nhật lại]:** T37, T38, T39 đã sinh đủ bằng Cloudflare"),
    "- **[27/11/2026 — cập nhật lại]:** T41 đã sinh đủ 157 ảnh bằng Cloudflare (mục IX.1); **T42 có 210 file nhưng là bộ mẫu chung ⇒ phải viết lại & sinh lại (tính như chưa có)** ⇒ **còn 4.463 ảnh** thuộc **29 tập** (31, 32, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 67). Tập 64, 66, 68, 69 chưa tính.",
    "muc VII.6 - tong so anh can sinh")

# ---------- G. Muc VI.6: dong bang tap 42 ----------
sub(lambda l: l.startswith("| 42 | 210 | **210** |"),
    "| 42 | 210 | **210** | ⚠ có file nhưng `bg_jobs` là bộ mẫu chung — mapping TRƯỢT, phải viết lại & sinh lại |",
    "muc VI.6 - dong bang tap 42")
sub(lambda l: l.strip().startswith("- **Tập có đủ ảnh theo job (đo 27/11):**"),
    "- **Tập có đủ ảnh theo job (đo 27/11):** **10–30, 36, 37, 38, 39, 40, 41** (27 tập — đủ 100 % **và** mapping ĐẠT); **Tập 42 có đủ 210 file nhưng mapping TRƯỢT** (mục IX.1). *[25/11: thêm Tập 26 và Tập 40 — xem mục VII; 26/11: thêm Tập 37, 38, 39 — xem mục VIII; **27/11: thêm Tập 41 — xem mục IX.1**]*",
    "muc VI.6 - danh sach tap du anh")

MD.write_text("\n".join(lines), encoding="utf-8")
print("da ghi | so dong sua:", n)
