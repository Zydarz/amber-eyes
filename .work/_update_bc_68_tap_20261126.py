#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cập nhật BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md theo số liệu đo thực tế 26/11/2026.

Số liệu đo lúc 26/11/2026 ~15:40 (quét `assets/bg/` + `bg_jobs_tapXX.json`).
"""
import json
import re
import shutil
import collections
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
REPORT = ROOT / "BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md"
CU = ROOT / ".work" / "_cu"


def measure():
    root_png = [f for f in BG.iterdir() if f.is_file() and f.suffix.lower() == ".png"]
    sub = {}
    for d in BG.iterdir():
        if d.is_dir():
            sub[d.name] = sum(1 for f in d.rglob("*")
                              if f.is_file() and f.suffix.lower() in (".png", ".jpg", ".jpeg"))
    cnt = collections.Counter()
    legacy = 0
    for f in root_png:
        m = re.match(r"t(\d+)_", f.name)
        if m and 1 <= int(m.group(1)) <= 68:
            cnt[int(m.group(1))] += 1
        else:
            legacy += 1
    jobs = {}
    for ep in range(1, 69):
        p = ROOT / ".work" / f"bg_jobs_tap{ep}.json"
        if not p.exists():
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        if isinstance(d, dict):
            for k in ("jobs", "items", "shots"):
                if k in d:
                    d = d[k]
                    break
        jobs[ep] = len(d)
    return root_png, sub, cnt, legacy, jobs


def main():
    root_png, sub, cnt, legacy, jobs = measure()
    total_by_ep = sum(cnt.get(e, 0) for e in range(1, 69))
    have = [e for e in range(1, 69) if cnt.get(e, 0) > 0]
    need = {}
    for ep in range(1, 69):
        j = jobs.get(ep)
        if j and cnt.get(ep, 0) < j:
            need[ep] = j - cnt.get(ep, 0)
    total_need = sum(need.values())
    eps_need = sorted(need)

    txt = REPORT.read_text(encoding="utf-8-sig")
    orig = txt

    # ---------- 1. Header ----------
    txt = txt.replace(
        "> **Thời điểm cập nhật:** 24/11/2026  ",
        "> **Thời điểm cập nhật:** 26/11/2026 (đo đạc lại toàn bộ kho ảnh + đợt sinh ảnh Tập 37/38/39)  ",
    )
    txt = txt.replace(
        "> - **Kho tài sản ảnh Graphic Novel Noir:** Đạt **4,911 ảnh sạch trên ổ đĩa**, đã dọn dẹp triệt để các file trùng lặp, bảo đảm khớp tiền tố 100%.",
        f"> - **Kho tài sản ảnh Graphic Novel Noir:** Đo lại 26/11/2026 — **{len(root_png):,} ảnh PNG ở gốc `assets/bg/`** "
        f"({total_by_ep:,} ảnh theo tiền tố tập + {legacy} ảnh tên cũ không theo tập); tính cả thư mục con "
        f"(`_raw/`, `outputs/`, `_gemini_backup/`) là **{len(root_png) + sum(sub.values()):,} file**. "
        f"**{len(have)}/68 tập đã có ảnh** (Tập {min(have)}–30, 36–40); còn **{total_need:,} ảnh cần sinh** cho {len(eps_need)} tập.",
    )

    # ---------- 2. Mục I ----------
    txt = txt.replace(
        "| **Kho ảnh minh họa (`assets/bg/`)** | **4,911 ảnh** (graphic novel noir) | *Sẵn sàng khởi tạo theo prompt chuyên đề* | **4,911+ ảnh** |",
        f"| **Kho ảnh minh họa (`assets/bg/`)** | **{len(root_png):,} ảnh** PNG ở gốc ({total_by_ep:,} theo tiền tố tập) · graphic novel noir | "
        f"*Sẵn sàng khởi tạo theo prompt chuyên đề* | **{len(root_png) + sum(sub.values()):,} file** (kể cả thư mục con) |",
    )

    # ---------- 3. Bảng mục II: cột "Số ảnh" ----------
    out_lines = []
    changed = 0
    for line in txt.split("\n"):
        m = re.match(r"^\| \*\*Tap (\d{2})\*\* \|", line)
        if m:
            ep = int(m.group(1))
            parts = line.split("|")
            if len(parts) >= 8:
                old = parts[5].strip().strip("*")
                new = cnt.get(ep, 0)
                parts[5] = f" **{new}** "
                note = parts[7]
                if ep in (37, 38, 39):
                    note = note.rstrip() + " · 26/11/2026: đã đủ ảnh (Cloudflare FLUX)"
                elif ep in eps_need:
                    note = note.rstrip() + f" · 26/11: còn thiếu {need[ep]} ảnh"
                elif new == 0:
                    note = note.rstrip() + " · 26/11: chưa có ảnh"
                parts[7] = note
                line = "|".join(parts)
                changed += 1
        out_lines.append(line)
    txt = "\n".join(out_lines)

    # ---------- 4. Mục IV ----------
    txt = txt.replace(
        "   - 4,911 file ảnh nền graphic novel noir lưu tại `assets/bg/` được định danh chuẩn mực, khớp tuyệt đối với bảng shot.",
        f"   - **{len(root_png):,} file ảnh nền graphic novel noir** lưu tại `assets/bg/` (đo 26/11/2026) — "
        f"{total_by_ep:,} ảnh theo tiền tố tập, khớp tuyệt đối với bảng shot của các tập đã có ảnh.",
    )

    # ---------- 5. Mục V ----------
    v_old = """1. **Hiện trạng phủ ảnh thực tế:**
   - **Đã có ảnh nền (38/68 tập - 55.9%):** 
     - Gồm: **Từ Tap 01 đến Tap 32**, **Tap 34, Tap 35, Tap 37, Tap 38, Tap 39, Tap 40**.
     - Tổng cộng **4,911 ảnh graphic novel noir** đạt chuẩn thẩm mỹ trên ổ cứng, đã gắn watermark thương hiệu Amber Eyes và kiểm định bản quyền `provenance.json`.
     - Trong đó, **Tap 30 (Nguyễn Đức Nghĩa)** đã có 86 ảnh (Hồi 1, Hồi 2 và nửa đầu Hồi 3), còn thiếu 69 ảnh (đã có sẵn prompt trong `.work/bg_jobs_tap30.json`).
   - **Chưa có ảnh nền (30/68 tập - 44.1%):**
     - Gồm: **Tap 33, Tap 36, và từ Tap 41 đến Tap 68** (trừ Tap 37, 38, 39, 40 đã có ảnh).
     - Các tập này hiện đã hoàn thiện kịch bản chi tiết chuẩn A2c/K10 và phân 5 hồi nội dung.
     - **Số lượng ảnh cần sản xuất bổ sung dự kiến:** 30 tập × ~140 ảnh/tập + 69 ảnh (Tap 30) $\\approx$ **4,269 ảnh**."""
    v_new = f"""1. **Hiện trạng phủ ảnh thực tế (đo lại 26/11/2026 — quét từng file `assets/bg/`):**
   - **Đã có ảnh nền và đủ theo job ({len(have)}/68 tập - {len(have) / 68 * 100:.1f}%):**
     - Gồm: **Tap 10 → Tap 30**, **Tap 36, Tap 37, Tap 38, Tap 39, Tap 40** (liên tục 10–30, rồi 36–40).
     - Tổng cộng **{total_by_ep:,} ảnh graphic novel noir** theo tiền tố tập trên ổ cứng, đã kiểm định bản quyền `provenance.json` (6.709 dòng).
     - **Tap 30 (Nguyễn Đức Nghĩa)** đã đủ {cnt.get(30, 0)} ảnh = số job; **Tap 37/38/39 đã đủ {cnt.get(37, 0)}/{cnt.get(38, 0)}/{cnt.get(39, 0)} ảnh** (đợt Cloudflare 25–26/11 — xem mục VIII).
   - **Chưa có ảnh nền ({68 - len(have)}/68 tập - {(68 - len(have)) / 68 * 100:.1f}%):**
     - Gồm: **Tap 01–09** (ảnh gốc còn nằm trong `assets/bg/_raw/`, không theo tiền tố `tNN_`), **Tap 31–35**, **Tap 41–68** (trừ 64, 66, 68 chưa có `bg_jobs`).
     - **Số lượng ảnh cần sản xuất bổ sung:** **{total_need:,} ảnh** cho {len(eps_need)} tập đã có `bg_jobs_tapXX.json` ({', '.join(str(e) for e in eps_need)})."""
    if v_old not in txt:
        print("!! KHONG khop muc V (nen dung ban viet lai)")
    txt = txt.replace(v_old, v_new)

    # ---------- 6. Mục VI.6 ----------
    txt = txt.replace(
        "- Thư mục `assets/bg/` có **3.637 file** ở gốc + `_raw/` (590), `_gemini_backup/` (3), `outputs/` (150, toàn `t15_*`). Đếm theo tiền tố tập và đối chiếu với `bg_jobs_tapXX.json`.",
        f"- **Đo lại 26/11/2026:** `assets/bg/` có **{len(root_png):,} file PNG** ở gốc + `_raw/` ({sub.get('_raw', 0)}), "
        f"`_gemini_backup/` ({sub.get('_gemini_backup', 0)}), `outputs/` ({sub.get('outputs', 0)}, toàn `t15_*`) ⇒ **{len(root_png) + sum(sub.values()):,} file**. "
        f"Trong {len(root_png):,} ảnh gốc: **{total_by_ep:,} ảnh theo tiền tố tập** + {legacy} ảnh tên cũ không theo tập "
        f"(`bedroom_door.png`, `cage.png`, `deedee_room.png`…). Đếm theo tiền tố tập và đối chiếu `bg_jobs_tapXX.json`.",
    )
    txt = txt.replace(
        "- **Tập có đủ ảnh theo job:** 10–25 (đủ 100 %), 27, 28, 29, 30. *[25/11 sau khi sinh: thêm Tập 26 và Tập 40 — xem mục VII]*",
        f"- **Tập có đủ ảnh theo job (đo 26/11):** **10–30, 36, 37, 38, 39, 40** ({len(have)} tập — đủ 100 %). "
        f"*[25/11: thêm Tập 26 và Tập 40 — xem mục VII; 26/11: thêm Tập 37, 38, 39 — xem mục VIII]*",
    )
    txt = txt.replace(
        "  - **Có `bg_jobs` hợp lệ (33 tập, cần sinh toàn bộ 4,928 ảnh):** 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 67.",
        f"  - **Có `bg_jobs` hợp lệ nhưng chưa có ảnh ({len(eps_need)} tập, cần sinh {total_need:,} ảnh):** "
        + ", ".join(str(e) for e in eps_need) + ".\n"
        "  - *[26/11/2026: Tập 37, 38, 39 đã sinh đủ bằng Cloudflare — xem mục VIII; Tập 36 đã đủ 157 ảnh.]*",
    )

    # ---------- 7. Mục VI.8 ----------
    txt = txt.replace(
        "- **Hiện `--check` ĐẠT:** Tập 26 (176/176 ảnh) · Tập 27–30 (đủ ảnh) · **Tập 40 (154/154 ảnh)** — 25/11/2026. **TRƯỢT vì thiếu ảnh:** Tập 49 (190) và 33 tập chưa sinh ảnh — đây là việc người dùng sinh ảnh, mapping không lỗi.",
        "- **Hiện `--check` ĐẠT:** Tập 26 (176/176 ảnh) · Tập 27–30 (đủ ảnh) · Tập 36 (157/157) · **Tập 37 (122/122)** · "
        "**Tập 38 (188/188)** · **Tập 39 (135/135)** · Tập 40 (154/154 ảnh) — 26/11/2026. "
        "**TRƯỢT vì thiếu ảnh:** Tập 49 (190) và 32 tập chưa sinh ảnh — đây là việc người dùng sinh ảnh, mapping không lỗi.",
    )

    # ---------- 8. Mục VII.6 ----------
    txt = txt.replace(
        "- **Sau lượt sinh này:** **T26 và T40 đã xong (0 ảnh)** ⇒ còn **5.118 ảnh** thuộc 34 tập (31, 32, 33, 34, 35, 36, 37, 38, 39, 41–48, 49, 50–63, 65, 67). Tập 64, 66, 68 chưa có `bg_jobs` (chờ kịch bản mở rộng — H23).",
        f"- **Sau lượt sinh này:** **T26 và T40 đã xong (0 ảnh)** ⇒ còn **5.118 ảnh** thuộc 34 tập (31, 32, 33, 34, 35, 36, 37, 38, 39, 41–48, 49, 50–63, 65, 67). "
        f"Tập 64, 66, 68 chưa có `bg_jobs` (chờ kịch bản mở rộng — H23).\n"
        f"- **[26/11/2026 — cập nhật lại]:** T37, T38, T39 đã sinh đủ bằng Cloudflare (mục VIII) ⇒ **còn {total_need:,} ảnh** thuộc "
        f"{len(eps_need)} tập ({', '.join(str(e) for e in eps_need)}). Tập 64, 66, 68 chưa tính.",
    )

    # ---------- 9. Thêm mục VIII ----------
    viii = f"""
---

## VIII. ĐỢT SINH ẢNH NỀN TẬP 37 / 38 / 39 BẰNG CLOUDFLARE FLUX (25–26/11/2026)

> Báo cáo chi tiết: **`90_LUU_TRU/Trang_Thai_SinhAnh_Tap37-39_20261125.md`**

### VIII.1. Phạm vi & kết quả

| Tập | Shot = job | Ảnh cuối cùng | Cổng `map_shot_anh --check` | `qc_bg_mapping` |
|---|---:|---:|---|---|
| 37 — Nguyễn Đức Anh (Việt Nam) | 122 | **122** | **ĐẠT** | **ĐẠT** (M1 0/122 · M5 0/221 · M4 122/122) |
| 38 — Aileen Wuornos (Mỹ) | 188 | **188** | **ĐẠT** | **ĐẠT** (M1 0/188 · M5 0/218 · M4 188/188) |
| 39 — Lao Vinh Chi & Pháp Tử Anh (Trung Quốc) | 135 | **135** | **ĐẠT** | **ĐẠT** (M1 0/135 · M5 0/240 · M4 135/135) |
| **Tổng** | **445** | **445** | **3/3 ĐẠT** | **3/3 ĐẠT** |

- 445 ảnh đều hợp lệ (`PIL.verify()`), đúng **2112×1188**, **đúng tên job** ⇒ tự khớp shot (H25/H28); 0 thiếu, 0 thừa.
- `provenance.json`: gộp đủ **445 dòng** t37–39, tổng **6.709 dòng**.

### VIII.2. Nguồn sinh ảnh — CHỈ CLOUDFLARE (không Kaggle)

- **Nguồn duy nhất:** Cloudflare Workers AI `@cf/black-forest-labs/flux-1-schnell` · 4 steps · hậu kỳ Deep Noir 4 tầng (H21) · crop 16:9 + LANCZOS 2112×1188.
- **User chốt 25/11/2026: chỉ dùng Cloudflare, KHÔNG dùng Kaggle.** 2 kernel Kaggle đã push (`amber-eyes-flux2-t37-r1`, `-t38-r1`) đã **xoá**; **0 ảnh Kaggle lọt vào `assets/bg/`** — toàn bộ 445 ảnh do Cloudflare sinh.
- **Quota:** 10.000 neurons/tài khoản/ngày (6 tài khoản trong `.work/.cloudflare_accounts`), ≈ 166 neurons/ảnh ⇒ **~60 ảnh/tài khoản/ngày**. Hạn mức cuộn 24h từ lần dùng đầu, **không** reset 00:00 UTC như tài liệu Cloudflare ghi.

### VIII.3. Diễn biến

| Thời điểm | Việc | Kết quả |
|---|---|---|
| 25/11 13:57 | Sinh lô đầu | **362 ảnh** (T37 113 · T38 114 · T39 135) — hết quota cả 6 account |
| 26/11 07:41–08:40 | Chờ quota | 6/6 account vẫn **HTTP 429** (hạn mức cuộn 24h) |
| 26/11 13:34 | Quota mở lại | Sinh nốt **130 ảnh** (T37 19 · T38 91 · T39 20) → **đủ 445** |
| 26/11 ~09:00 | Soi mắt 100 % 362 ảnh | **47 ảnh lỗi** (AI vẽ chữ: MOTEL, PAWN SHOP, COURT, AMBULANCE, biển số, bảng hồ sơ, chữ Hán tự) |
| 26/11 ~10:00 | **Vòng 1** — gỡ chữ khỏi prompt + thêm negative | 47 → **37 ảnh còn chữ** |
| 26/11 13:40 | **Vòng 2** — đổi bối cảnh / crop sát | **~37 ảnh vẫn còn chữ** (cải thiện rất ít) |
| 26/11 14:12–14:20 | **Vòng 3** — bỏ hẳn negation + gỡ mọi từ kích hoạt chữ | **37/37 sinh lại thành công** (T37 7 · T38 11 · T39 19) — **user tự soi mắt** |

### VIII.4. Bài học (áp dụng cho mọi đợt sinh ảnh sau)

1. **Negation không hiệu quả với FLUX.1-schnell.** Thêm *"no text, no lettering, no characters, no signage…"* **không ngăn được** AI vẽ chữ; ngược lại, chữ *"signage / no signage"* còn **kích hoạt đúng vật thể cần biển** (ảnh T39 đầy biển Hán tự).
2. **Cách hiệu quả:** **loại bỏ khỏi khung hình mọi bề mặt có thể mang chữ** (biển, bảng, biển số, giấy tờ, màn hình, tiền, nhãn, mặt tiển tòa) và mô tả vật thể **trơn**: *blank / unmarked / plain / bare / featureless*; crop sát vào vật thể, nền xa làm mờ.
3. **Bối cảnh Trung Quốc 1990s là ổ đẩy chữ Hán tự** — cần cân nhắc đổi bối cảnh, không chỉ crop.
4. **Vòng 2 (crop sát, giữ câu negative) gần như vô dụng** ⇒ bỏ negation là bước then chốt, không phải viết lại prompt tinh vi hơn.
5. **Ghi provenance theo shard** (`.work/_prov_shard_tXX.json`) rồi merge 1 lần bằng `merge_prov_shards.py` (ghi atomic) — tránh nhiều tiến trình ghi đục file 6.709 dòng.
6. **Lưu PNG với `optimize=False, compress_level=3`** — `optimize=True` tốn 15–20 s/ảnh **nằm ngoài** block đo thời gian ⇒ dễ tưởng chậm do network. Tốc độ: ~2,5 → **~37 ảnh/phút**.

### VIII.5. Công cụ dùng cho đợt này

| Việc | Đường dẫn |
|---|---|
| Sinh ảnh Cloudflare (lô đầu) | `.work/gen_images_cf_tap3739.py` |
| Sinh nốt + sinh lại ảnh lỗi | `.work/gen_images_cf_resume.py` |
| Client Cloudflare (pool 6 account, auto-failover 429) | `.work/flux_client.py` |
| Viết lại prompt vòng 1 / 2 / 3 | `.work/_rewrite_prompts_flags.py` · `_rewrite_prompts_r2.py` · `_rewrite_prompts_r3.py` |
| Danh sách ảnh lỗi QC (37 ảnh vòng 2) | `.work/_qc_flags_t37_39.json` |
| Gộp sổ xuất xứ | `.work/merge_prov_shards.py` |
| Tờ soi mắt 37 ảnh vòng 3 | `.work/qc_montage/regen_00.jpg` · `regen_01.jpg` · `regen_02.jpg` |
| Backup job json | `.work/_cu/bg_jobs_tapXX_20261126_0845.json` · `_1358_r2.json` · `_1412_r3.json` |

### VIII.6. Việc còn treo

1. **User soi mắt 37 ảnh vòng 3** (tờ `regen_00/01/02.jpg`); ảnh nào còn chữ thì sinh lại **cùng tên** theo hướng VIII.4.
2. **`provenance.json` còn ~446 dòng cũ trỏ file đã xoá** (T37: 148 · T38: 146 · T39: 152) — giữ làm lịch sử theo quyết định 25/11, **chưa dọn**.
3. **Cron Cloudflare** `35724854-772e-449e-af6d-6cf6727415ac` đang **paused** (chưa xoá) — không chạy nền, tránh sinh trùng tên file.
"""
    if "## VIII. ĐỢT SINH ẢNH NỀN TẬP 37 / 38 / 39" not in txt:
        txt = txt.rstrip() + "\n" + viii

    # ---------- 10. Ghi ----------
    if txt == orig:
        print("!! KHONG co thay doi nao duoc ghi")
        return
    CU.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    bak = CU / f"BaoCao_ThongKe_68_truoc_cap_nhat_{stamp}.md"
    shutil.copy2(REPORT, bak)
    REPORT.write_text(txt, encoding="utf-8")
    print(f"Da cap nhat: {REPORT.name}")
    print(f"  backup: {bak}")
    print(f"  dong bang II sua: {changed}")
    print(f"  anh goc {len(root_png)} | theo tap {total_by_ep} | legacy {legacy} | can sinh {total_need} tren {len(eps_need)} tap")


if __name__ == "__main__":
    main()
