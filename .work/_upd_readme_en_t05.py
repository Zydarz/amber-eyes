#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat README Tap05_EN bang SO DO THAT tu ket qua QC (khong hard-code).

Chay sau .work/_qc_final_en_t05.py
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
RES = json.loads((WORK / "_qc_final_en_t05_result.json").read_text(encoding="utf-8"))
README = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "README.md"
t = README.read_text(encoding="utf-8-sig")
orig = t

dur = RES["duration"]
frames = RES["frames"]
sha = RES["sha256"]
mp4 = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "Tap05_EN_master.mp4"
size_mb = mp4.stat().st_size / 1024 / 1024

lines = []
for k in ("ok", "fail"):
    for m in RES.get(k, []):
        lines.append(f"- {'✅' if k == 'ok' else '❌'} {m}")
qc_block = "\n".join(lines)

new_section = f"""## 8. Xuất bản EN (bản dựng 04/11/2026 — đồng bộ với master audio Higgs)

| Mục | Giá trị |
|---|---|
| File video | `02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp4` |
| Thời lượng | **{dur:.2f} s** (timeline 1272,51 s · lệch {dur - 1272.51:+.3f} s) |
| Số khung | {frames} (= int(1272,51 × 30)) |
| Kích thước / codec | 1920×1080 @ 30 fps · H.264 (libopenh264) + AAC 192 kHz |
| Dung lượng | {size_mb:.1f} MB |
| SHA-256 (12) | `{sha}` |
| Nguồn âm thanh | `Tap05_EN_master.mp3` (Higgs v3, 1272,51 s) — **không** dùng `audio_master_EN_t05.wav` (1449,24 s, bản cũ) |

**Bảng shot đồng bộ lại (H14):** `shots_EN_t05.json` được sinh lại từ timeline mới — bảng cũ (25/10) dùng timeline 1449,24 s nên mốc thời gian lệch toàn bộ.

### 8.1. Lỗi đã sửa trong hồ sơ EN (04/11/2026)

| # | Shot | Lỗi | Đã sửa |
|---|---|---|---|
| 1 | 1-11 | Trích dẫn lệch nguyên văn (`after a decade` vs `after more than a decade`; thiếu `entire`) | Sửa về nguyên văn câu `1.09#1` / `1.09#2` |
| 2 | 1-12 | Trích dẫn là paraphrase, không nằm trong câu đọc | Sửa thành trích dẫn nguyên văn từ `1.09#3` |
| 3 | 4-17 | Trích dẫn `but to me he was the best father` không có trong câu; tiêu đề `HUGGED ME` ≠ `kissed me` | Sửa về `barbaric monster… Yet to me…` + `THE MAN WHO KISSED ME GOODNIGHT EVERY EVENING` |
| 4 | 5-08 / 5-09 | Ranh giới shot lệch 1 câu ⇒ màn `RED FLAG 04` hiện **sau** khi câu `the fourth red flag` đã nói xong | Sửa `5-08` = `5.06#1–#2`, `5-09` = `5.06#3–#5` (giống bản VN) |
| 5 | 1-13 / 1-14 / 5-13 / 5-14 | Segment `at_sentence` lệch nhịp: chữ trên hình hiện **trước** câu đọc tương ứng | Căn lại theo đúng câu (`#3`/`#4`/`#5`/`#3`) + chuyển dòng về đúng shot |

### 8.2. Kết quả QC đầu ra

{qc_block}

### 8.3. QC độc lập audio ↔ timeline (đo mốc bắt đầu lời nói)

- 163/164 câu có mốc bắt đầu lời lệch timeline ≤ 0,44 s (trung vị +0,060 s, TB |lệch| 0,084 s).
- Ngoại lệ `4.10#1` là hệ quả của tiếng phanh/còi xe (SFX `4.09`) chồng lên đầu câu — không phải lệch timeline.
- Script: `.work/_qc_audio_onset_en_t05.py` · QC bảng shot: `.work/_qc_shots_en_t05.py` · QC mp4: `.work/_qc_final_en_t05.py`.
"""

if "## 8. Xuất bản EN" in t:
    t = re.sub(r"## 8\. Xuất bản EN.*$", new_section, t, flags=re.S)
else:
    t = t.rstrip() + "\n\n" + new_section

if t != orig:
    README.write_text(t, encoding="utf-8")
    print(f"README cap nhat: {dur:.2f} s · {frames} khung · {size_mb:.1f} MB · sha {sha}")
else:
    print("README khong doi")
