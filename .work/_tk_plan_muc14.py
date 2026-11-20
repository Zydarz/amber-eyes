# -*- coding: utf-8 -*-
"""Ghi muc 14 (anh nen doc Tap 02) vao KE_HOACH_TIKTOK.md — L6."""
import pathlib
import shutil
import time

P = pathlib.Path("02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md")

TEXT = """
---

## 14. ẢNH NỀN DỌC TẬP 02 — ĐÃ TẠO 26/26 (20/11/2026)

### 14.1 Kết quả đo thật

| Chỉ số | Số đo |
|---|---|
| Số nền dọc `assets/bg/tk02_*.png` | **26/26** — đủ cho cả 5 clip (TK1 9 · TK2 7 · TK3 10 · TK4 8 · TK5 6) |
| Kích thước | **1080×1920 — 26/26 đúng**, sai số 0 |
| Nguồn | **8 nền AI thật** (connector `__matrix__generate_image`, 9:16, area 2K) + **18 nền dự phòng** (crop từ ảnh gốc 16:9) |
| Dòng `provenance.json` | **+26** (8 dòng có `prompt` = AI thật · 18 dòng `prompt: null` = dự phòng) ⇒ 3.722 dòng tổng |
| Backup | `.work/_cu/tk02_provenance_20261120_0859/` · `.work/_cu/tk02_fallback_prov_20261120_1207/` · ảnh v1: `.work/_cu/fallback_v1_20261120_121032/` |

### 14.2 Vì sao 18 nền là bản DỰ PHÒNG (không phải AI)

Connector trả `402` cho 18/26 request: *"the plan allowance cannot cover this image generation and credit auto-consumption is turned off on this account… at least 100 credits of balance are required"*. Lô 3 còn bị `429` *"request limit reached; retry in the next minute"* — nhưng thử lại thì vẫn `402` ⇒ **429 chỉ là che, nguyên nhân gốc là hết credit**.

⇒ Không dừng pipeline: `.work/_tk_fallback_crop_t02.py` **cắt 9:16 từ ảnh nền 16:9 gốc** (`assets/bg/_raw/t2_*`) — **0 credit**, đúng bảng màu của kênh. 18 nền này được đánh dấu riêng trong `provenance.json` (`prompt: null`, `cong_cu` ghi rõ "DU PHONG") để không nhầm là AI thật.

**Khi nào nạp credit → chạy lại:** `.work/_tk_download_imgs_t02.py` (tải node_id → `.work/tk_img_raw_t02/`) → `.work/_tk_postprocess_t02.py` (LANCZOS + grade noir + vignette/grain). Script hậu kỳ **ghi đè đúng tên file** nên chỉ cần copy bản AI mới vào `assets/bg/tk02_<tên>.png` là xong.

### 14.3 Bốn bẫy mới (T17–T20)

| # | Bẫy | Hậu quả | Cách tránh |
|---|---|---|---|
| **T17** | Ảnh gốc 16:9 trong `_raw/` **đã qua grade noir của kênh** (saturation 0,65 · contrast 1,15 · vignette 45 % · grain) — đo được: `t2_two_chairs.jpg` mean 50,3/sat 9,0 vs `.png` mean 47,7/sat 6,9 | Áp lại grade lần nữa ⇒ **tối quá, mất chi tiết bóng** | Bản dự phòng **chỉ** crop + LANCZOS + nền tối vùng chữ, **không** áp grade |
| **T18** | Nhiều ảnh gốc **kẹp letterbox đen** trên/dưới (đo: `t2_gavel.png` còn 182 px đen trên + 182 px đen dưới; `t2_checkpoint.png` 182/181) | Crop thẳng ⇒ mất 24 % chiều cao, chủ thể bị cắt | Dò vùng nội dung bằng `rowmax > 30` **trước khi** crop |
| **T19** | Crop 9:16 từ 16:9 giữ **vệt ngang** nếu profile làm tối dùng `min()` + `linspace` (nhảy giá trị đúng ranh giới 1/3 và 2/3) | **Vết sáng ngang** nổi lên khi chuyển động trên video | Dùng profile **smoothstep liên tục** qua 6 mốc (0,50 → 1,00 → 0,50). Đo lại: `max_row_jump` toàn 26 ảnh ≤ 42,6 (do nét vẽ trong ảnh, không phải do profile) |
| **T20** | `mcode-tools` là wrapper `.cmd` ⇒ `subprocess.run(["mcode-tools", ...])` **không** chạy được (WinError 2) | Script tải ảnh hỏng âm thầm | `shutil.which("mcode-tools")` + `shell=True`; và `Tee-Object` của PowerShell ghi receipt ra **UTF-16** ⇒ đọc JSON bằng `utf-16`/`utf-8-sig` (đã có `read_json_any`) |

### 14.4 Chọn vùng crop (đo được)

`.work/_tk_fallback_crop_t02.py` không crop giữa khung mà chọn cửa sổ 9:16 có **năng lượng nét vẽ cao nhất** (gradient ngang + biến độ cục bộ), giới hạn lệch tối đa 22 % chiều rộng nội dung ⇒ giữ chủ thể. Sau đó ép cân bằng chiều dọc 9:16 rồi LANCZOS về 1080×1920.

**Giới hạn đã biết:** ảnh crop vẫn là **tái dựng của ảnh 16:9** nên bố cục dọc kém bản AI thật (bản AI được vẽ lại để dựng theo chiều dọc). 18 nền này dùng được để **chạy thử pipeline và đo thời lượng thật**, nhưng **nên thay bằng bản AI trước khi đăng** (xem Tập 2.4 — ảnh dựng độc quyền của bản AI là điểm mạnh khi đăng TikTok).
"""


def main():
    t = P.read_text(encoding="utf-8-sig")
    if "## 14. ẢNH NỀN DỌC TẬP 02" in t:
        print("muc 14 da ton tai — bo qua")
        return
    bak = pathlib.Path(".work/_cu") / ("KE_HOACH_TIKTOK_%s.md" % time.strftime("%Y%m%d_%H%M"))
    bak.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(P, bak)
    P.write_text(t.rstrip("\n") + "\n" + TEXT, encoding="utf-8")
    print("da them muc 14 · backup: %s" % bak)


if __name__ == "__main__":
    main()
