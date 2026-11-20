# -*- coding: utf-8 -*-
"""Cap nhat muc 14 cua KE_HOACH_TIKTOK.md — so do cuoi + them bay T21 — L6."""
import pathlib
import shutil
import time

P = pathlib.Path("02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md")

OLD_ROWS = """| Chỉ số | Số đo |
|---|---|
| Số nền dọc `assets/bg/tk02_*.png` | **26/26** — đủ cho cả 5 clip (TK1 9 · TK2 7 · TK3 10 · TK4 8 · TK5 6) |
| Kích thước | **1080×1920 — 26/26 đúng**, sai số 0 |
| Nguồn | **8 nền AI thật** (connector `__matrix__generate_image`, 9:16, area 2K) + **18 nền dự phòng** (crop từ ảnh gốc 16:9) |
| Dòng `provenance.json` | **+26** (8 dòng có `prompt` = AI thật · 18 dòng `prompt: null` = dự phòng) ⇒ 3.722 dòng tổng |
| Backup | `.work/_cu/tk02_provenance_20261120_0859/` · `.work/_cu/tk02_fallback_prov_20261120_1207/` · ảnh v1: `.work/_cu/fallback_v1_20261120_121032/` |"""

NEW_ROWS = """| Chỉ số | Số đo |
|---|---|
| Số nền dọc `assets/bg/tk02_*.png` | **26/26** — đủ cho cả 5 clip (TK1 9 · TK2 7 · TK3 10 · TK4 8 · TK5 6) |
| Kích thước | **1080×1920 — 26/26 đúng**, sai số 0 |
| Nguồn | **8 nền AI thật** (connector `__matrix__generate_image`, 9:16, area 2K) + **18 nền dự phòng** (crop từ ảnh gốc 16:9) |
| Dòng `provenance.json` | **+26** (8 dòng có `prompt` = AI thật · 18 dòng `prompt: null` = dự phòng) ⇒ 3.722 dòng tổng |
| Độ sáng vùng chữ hook (y 270–730, x 120–780) | **mean 42,4 · max 56,9** (bộ `tk01_*` đã xuất bản: mean 41,6 · max 74,0) ⇒ không sáng hơn bộ đã đăng |
| Độ sáng vùng phụ đề (y 996–1254) | mean 64,8 (bộ `tk01_*`: 82,1) |
| Vết ngang trong ảnh | đo theo từng cột (`|Δ| > 18` ở > 70 % số cột): **0 dải** trong 26 ảnh — chỉ 2 mép trên/dưới do crop |
| Backup | `.work/_cu/tk02_provenance_20261120_0859/` · `.work/_cu/tk02_fallback_prov_20261120_1207/` · ảnh v1: `.work/_cu/fallback_v1_20261120_121032/` · ảnh v2: `.work/_cu/tk02_fallback_img_20261120_1217/` |

**Quy trình đã chạy (đo được):** `.work/_tk_upload_refs_t02.py` (26/26 URL tham chiếu) → `.work/_tk_build_img_req_t02.py` (3 lô 10+10+6) → `mcode-tools connector call connector__matrix__generate_image` → `.work/_tk_download_imgs_t02.py` (node_id → file) → `.work/_tk_postprocess_t02.py` (8 nền AI) → `.work/_tk_fallback_crop_t02.py` (18 nền dự phòng)."""

OLD_T20 = """| **T20** | `mcode-tools` là wrapper `.cmd` ⇒ `subprocess.run(["mcode-tools", ...])` **không** chạy được (WinError 2) | Script tải ảnh hỏng âm thầm | `shutil.which("mcode-tools")` + `shell=True`; và `Tee-Object` của PowerShell ghi receipt ra **UTF-16** ⇒ đọc JSON bằng `utf-16`/`utf-8-sig` (đã có `read_json_any`) |"""

NEW_T20 = OLD_T20 + """
| **T21** | Profile làm tối dải chữ viết bằng `1 − smoothstep` ở nửa lên ⇒ **nhảy giá trị 0→1 đúng tại biên** (đo được: dải ngang tại row 730 và row 996) | Vệt sáng ngang nổi lên đúng chỗ chữ, rất dễ thấy khi video chuyển động | Nửa lên dùng **smoothstep thuần** (0 tại cạnh ngoài → 1 tại biên trong); nửa xuống dùng `1 − smoothstep`. Sau khi sửa: `max_row_jump` toàn 26 ảnh ≤ 42,6, và **0 dải ngang xuyên suốt chiều ngang** |
| **T22** | Ảnh nền dọc phải **tối vùng chữ** trước khi dựng: 18 nền dự phòng có vùng hook sáng tới 118,8 (bộ `tk01_*` chỉ 41,6) | Chữ trắng trên nền sáng ⇒ mất chữ (H9) | `.work/_tk_fallback_crop_t02.py` tự tìm `depth` (0 → 0,60) để đưa mean vùng hook ≤ 58 và vùng phụ đề ≤ 72, biên mềm 70 px |"""

OLD_14_4 = """### 14.4 Chọn vùng crop (đo được)

`.work/_tk_fallback_crop_t02.py` không crop giữa khung mà chọn cửa sổ 9:16 có **năng lượng nét vẽ cao nhất** (gradient ngang + biến độ cục bộ), giới hạn lệch tối đa 22 % chiều rộng nội dung ⇒ giữ chủ thể. Sau đó ép cân bằng chiều dọc 9:16 rồi LANCZOS về 1080×1920."""

NEW_14_4 = """### 14.4 Chọn vùng crop (đo được)

`.work/_tk_fallback_crop_t02.py` không crop giữa khung mà chọn cửa sổ 9:16 có **năng lượng nét vẽ cao nhất** (gradient ngang + biến độ cục bộ), giới hạn lệch tối đa 22 % chiều rộng nội dung ⇒ giữ chủ thể. Sau đó ép cân bằng chiều dọc 9:16 rồi LANCZOS về 1080×1920.

**Script chạy lại được:** nếu ảnh đã tồn tại mà `provenance.json` **không có `prompt`** ⇒ coi là bản dự phòng và tạo lại (tự backup vào `.work/_cu/tk02_fallback_img_<giờ>/`); nếu **có `prompt`** ⇒ là bản AI thật, **giữ nguyên, không ghi đè**."""


def main():
    t = P.read_text(encoding="utf-8-sig")
    n = 0
    for old, new in ((OLD_ROWS, NEW_ROWS), (OLD_T20, NEW_T20), (OLD_14_4, NEW_14_4)):
        if old not in t:
            raise SystemExit("KHONG TIM THAY khoi can thay:\n%s" % old[:120])
        t = t.replace(old, new, 1)
        n += 1
    bak = pathlib.Path(".work/_cu") / ("KE_HOACH_TIKTOK_%s.md" % time.strftime("%Y%m%d_%H%M"))
    bak.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(P, bak)
    P.write_text(t, encoding="utf-8")
    print("cap nhat %d khoi · backup: %s" % (n, bak))


if __name__ == "__main__":
    main()
