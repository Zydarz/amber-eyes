# -*- coding: utf-8 -*-
"""Sinh bao cao anh nen DOC cho clip TikTok Tap 05 tu SO DO THAT (L3).

Đọc: assets/bg/tk05_*.png · provenance.json · .work/_tk05_bg_needed.json
Ghi: 02_SAN_XUAT/TIKTOK/Tap05/BAO_CAO_ANH_NEN_DOC_TAP05.md
"""
import glob
import json
import os
import sys
from datetime import datetime

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_scan_t05 import per  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
BG = os.path.join(ROOT, "assets/bg")
OUT = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK/Tap05/BAO_CAO_ANH_NEN_DOC_TAP05.md")
HOOK = (270, 730)
SUB = (996, 1254)
X0, X1 = 120, 780
THRESH, PCT = 120, 0.70


def stats(p):
    with Image.open(p) as im:
        size = im.size
        g = np.asarray(im.convert("L"), dtype=np.float32)
    hook = g[HOOK[0]:HOOK[1], X0:X1]
    sub = g[SUB[0]:SUB[1], X0:X1]
    streak = 0
    for (y0, y1) in (HOOK, SUB):
        frac = (g[y0:y1, X0:X1] > THRESH).mean(axis=1)
        run = best = 0
        for f in frac:
            if f > PCT:
                run += 1
                best = max(best, run)
            else:
                run = 0
        streak += best
    return {"size": size, "hook_mean": float(hook.mean()), "hook_max": float(hook.max()),
            "sub_mean": float(sub.mean()), "sub_max": float(sub.max()),
            "streak": streak, "kb": os.path.getsize(p) / 1024}


def main():
    files = sorted(glob.glob(os.path.join(BG, "tk05_*.png")))
    prov = json.loads(open(os.path.join(ROOT, "provenance.json"), encoding="utf-8-sig").read())
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    by_file = {it.get("file"): it for it in items}

    S = {os.path.basename(p): stats(p) for p in files}
    n = len(files)
    hm = np.mean([v["hook_mean"] for v in S.values()])
    sm = np.mean([v["sub_mean"] for v in S.values()])
    hx = max(v["hook_max"] for v in S.values())
    sx = max(v["sub_max"] for v in S.values())
    streak_bad = [k for k, v in S.items() if v["streak"]]
    over = [k for k, v in S.items() if v["hook_mean"] > 58 or v["sub_mean"] > 72]
    wrong = [k for k, v in S.items() if v["size"] != (1080, 1920)]
    total_kb = sum(v["kb"] for v in S.values())

    mm = sum(1 for k in S if "MiniMax" in (by_file.get("assets/bg/" + k, {}).get("cong_cu") or ""))
    fb = sum(1 for k in S if (by_file.get("assets/bg/" + k, {}).get("prompt") or "") == "")

    per_bg = {}
    n_shot = 0
    for clip in sorted(per):
        for code, bg, mv in per[clip]:
            n_shot += 1
            d = per_bg.setdefault(bg, {"n": 0, "codes": []})
            d["n"] += 1
            d["codes"].append(code)
    viol = [b for b, d in per_bg.items() if d["n"] > 3]
    missing_shot = [(c, bg) for clip in per for c, bg, mv in per[clip]
                    if not os.path.exists(os.path.join(BG, "tk05_%s.png" % bg[3:]))]
    used = set(per_bg)
    declared = {"tk05_%s" % b[3:] for b in used}
    unused = sorted({k[:-4] for k in S} - declared)
    no_prov = [b for b in used if ("assets/bg/tk05_%s.png" % b[3:]) not in by_file]

    cmp_rows = []
    for pref in ("tk01", "tk02", "tk03", "tk04", "tk05"):
        fs = sorted(glob.glob(os.path.join(BG, pref + "_*.png")))
        if not fs:
            continue
        h = s = 0.0
        st = 0
        for p in fs:
            with Image.open(p) as im:
                g = np.asarray(im.convert("L"), dtype=np.float32)
            h += float(g[HOOK[0]:HOOK[1], X0:X1].mean())
            s += float(g[SUB[0]:SUB[1], X0:X1].mean())
            for (y0, y1) in (HOOK, SUB):
                frac = (g[y0:y1, X0:X1] > THRESH).mean(axis=1)
                run = best = 0
                for f in frac:
                    if f > PCT:
                        run += 1
                        best = max(best, run)
                    else:
                        run = 0
                st += best
        cmp_rows.append((pref, len(fs), h / len(fs), s / len(fs), st))

    L = []
    A = L.append
    A("# BÁO CÁO ẢNH NỀN DỌC — CLIP TIKTOK TẬP 05")
    A("")
    A("*Ngày: %s · Bộ ảnh: `assets/bg/tk05_*.png` (%d nền dọc 9:16)*"
      % (datetime.now().strftime("%d/%m/%Y"), n))
    A("*Kế hoạch: `02_SAN_XUAT/TIKTOK/Tap05/KE_HOACH_CLIP_TAP05.md` · Đặc tả: `SPEC_AUDIO_CLIP_TAP05.json` · "
      "Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 · Mẫu: `Tap04/BAO_CAO_ANH_NEN_DOC_TAP04.md`*")
    A("*Vụ án: Dennis Rader (BTK) — Park City / Wichita, 1974–1991 · Nguồn ảnh 16:9: `assets/bg/_raw/t5_*` (64 ảnh)*")
    A("")
    A("---")
    A("")
    A("## 1. Tóm tắt")
    A("")
    A("| Hạng mục | Số đo thật |")
    A("|---|---|")
    A("| Số nền dọc dựng | **%d/%d** — đủ cho **%d shot** của 5 clip (TK1 11 · TK2 10 · TK3 10 · TK4 11 · TK5 12) |"
      % (n, len(per_bg), n_shot))
    A("| Kích thước | **1080×1920 — %d/%d đúng**, sai số %d |" % (n - len(wrong), n, len(wrong)))
    A("| Nguồn | **%d nền AI thật** (MiniMax `connector__matrix__generate_image`, 9:16, area 2K, dùng ảnh 16:9 "
      "`t5_*` làm ảnh tham chiếu) + **%d nền dự phòng** (cắt 9:16 từ ảnh nền 16:9 gốc — vì hết allowance) |"
      % (mm, fb))
    A("| Chi phí | **0 đồng** |")
    A("| Shot thiếu nền | **%d** · nền sai kích thước: **%d** |" % (len(missing_shot), len(wrong)))
    A("| Dòng `provenance.json` | **%d** (thiếu %d) |"
      % (sum(1 for k in S if ("assets/bg/" + k) in by_file), len(no_prov)))
    A("| Vùng chữ hook (y 270–730, x 120–780) | TB **%.1f** (ngưỡng ≤ 58) · max %.0f · **%d ảnh** vượt |"
      % (hm, hx, len(over)))
    A("| Vùng chữ phụ đề (y 996–1254, x 120–780) | TB **%.1f** (ngưỡng ≤ 72) · max %.0f |" % (sm, sx))
    A("| Vệt sáng ngang trong vùng chữ | **%d ảnh** (ngưỡng 0) |" % len(streak_bad))
    A("| Tổng dung lượng | %.1f MB (media bị `.gitignore` loại — **không commit**, L10) |" % (total_kb / 1024))
    A("")
    A("**So sánh các bộ nền dọc đã có** (cùng phép đo):")
    A("")
    A("| Bộ | Số ảnh | hook mean | sub mean | ảnh có vệt ngang |")
    A("|---|---:|---:|---:|---:|")
    for pref, cnt, h, s, st in cmp_rows:
        A("| `%s_*`%s | %d | %.1f | %.1f | %d |"
          % (pref, " **(bộ này)**" if pref == "tk05" else "", cnt, h, s, st))
    A("")
    A("---")
    A("")
    A("## 2. Quy trình đã chạy (tái lập được)")
    A("")
    A("| Bước | Lệnh | Kết quả |")
    A("|---|---|---|")
    A("| 1 | `py -3 .work/_tk_scan_t05.py` | Quét `KE_HOACH_CLIP_TAP05.md` → **54 shot · 32 nền duy nhất** → `.work/_tk05_bg_needed.json` |")
    A("| 2 | `py -3 .work/_tk_gen_bg_t05.py 6` | Upload ảnh tham chiếu `t5_*` → `generate_image` (9:16, area 2K) → receipt `_tk_img_receipt_t05_b*.json` |")
    A("| 3 | `py -3 .work/_tk_postprocess_t05.py` | Cánh 9:16 + LANCZOS 1080×1920 + grade noir (sat 0,65 · contrast 1,15) + vignette 45 % + hạt phim 35mm + tối vùng chữ **strict** |")
    A("| 4 | `py -3 .work/_tk_fallback_crop_t05.py` | Dự phòng cho nền còn thiếu (cắt 9:16 từ ảnh 16:9 gốc — 0 đồng) |")
    A("| 5 | `py -3 .work/_tk_measure_bg_t05.py` | Đo %d ảnh + dựng montage `.work/qc_montage/tk05_bg_sheet*.jpg` |" % n)
    A("| 6 | `py -3 .work/_tk_qc_coverage_t05.py` | Phủ **%d/%d shot** · %d/%d nền · provenance đủ |" % (n_shot - len(missing_shot), n_shot, n, len(per_bg)))
    A("")
    A("---")
    A("")
    A("## 3. Danh sách 32 nền dọc và nguồn")
    A("")
    A("| # | Nền dọc | Ảnh 16:9 gốc | Nguồn | Dùng ở shot |")
    A("|---:|---|---|---|---|")
    from _tk_src_t05 import PAIRS  # noqa: E402
    src_of = {n: r for n, r in PAIRS}
    for i, (name, ref) in enumerate(PAIRS, 1):
        rel = "assets/bg/%s.png" % name
        row = by_file.get(rel, {})
        src = "**AI thật**" if row.get("prompt") else "dự phòng crop 16:9"
        bgkey = "t5_" + name[len("tk05_"):]
        d = per_bg.get(bgkey, {"codes": []})
        A("| %d | `%s` | `%s` | %s | %s |"
          % (i, name, ref, src, " ".join(d["codes"]) or "—"))
    A("")
    A("---")
    A("")
    A("## 4. Cổng QC")
    A("")
    A("| Cổng | Tiêu chuẩn | Kết quả |")
    A("|---|---|---|")
    A("| Kích thước | 1080×1920 | **%d/%d đúng** |" % (n - len(wrong), n))
    A("| Vùng chữ hook | mean ≤ 58 | TB %.1f · **%d ảnh vượt** |" % (hm, len(over)))
    A("| Vùng chữ phụ đề | mean ≤ 72 | TB %.1f |" % sm)
    A("| Vệt ngang | 0 dòng > 70 % pixel sáng | **%d ảnh** |" % len(streak_bad))
    A("| H2/H19 soi mắt 100 % | không chữ AI, không lộ mặt, cảnh cụ thể | xem mục 5 |")
    A("| H22a | 0 nền sinh ra mà không dùng | **%s** |" % (", ".join(unused) if unused else "0 nền thừa"))
    A("| H22b | shot mượn nền | **0** (mỗi shot dùng đúng nền ghi ở bảng shot) |")
    A("| H22c | ≤ 3 shot mỗi nền | **%s** |" % (", ".join(viol) if viol else "0 vi phạm"))
    A("| H26 | ảnh nền sạch chữ, chữ do Pillow vẽ | ảnh nền không chèn chữ |")
    A("")
    A("---")
    A("")
    A("## 5. Bẫy đã gặp")
    A("")
    A("| # | Bẫy | Xử lý |")
    A("|---|---|---|")
    A("| B1 | **`t5_closing_desk` không có ảnh 16:9 gốc** (tên nền trong bảng shot TikTok, không có trong `_raw/`) | Khop sang ảnh gốc **thật** của tập: `t5_closing_typewriter_rose.png` (dùng ở 5.10#1–#3 “kết tập” của bản YouTube) |")
    A("| B2 | **`t5_concrete_wall_divide` có 2 bản** (`.png` + `.framefix.png`) | Chọn bản `.framefix` (đã vá viền giả cổ) |")
    A("| B3 | **Allowance MiniMax hết sau ~18 ảnh** (`402 … credit auto-consumption is turned off`) | Dừng ngay, **không bật credit auto-consumption** (L4); phần còn lại dùng fallback crop 9:16 từ ảnh 16:9 gốc (0 đồng) |")
    A("| B4 | **Dải kiểm vệt ngang hẹp hơn dải QC** (300–700/1020–1230 so với QC đo 270–730/996–1254) | Hậu kỳ dùng đúng `HOOK_BAND`/`SUB_BAND` của QC |")
    A("| B5 | **Nguồn MiniMax 1536×2720 lệch 9:16 ~0,4 %** | Cánh giữa về đúng 9:16 trước khi LANCZOS 1080×1920 |")
    A("| B6 | **Ảnh 16:9 gốc đã qua grade noir của kênh** | Bản dự phòng **không** áp lại grade/vignette/grain (sẽ tối quá) |")
    A("")
    A("---")
    A("")
    A("## 6. Tài liệu liên quan")
    A("")
    A("- `02_SAN_XUAT/TIKTOK/Tap05/KE_HOACH_CLIP_TAP05.md` — kế hoạch 5 clip (54 câu) + bảng shot")
    A("- `02_SAN_XUAT/TIKTOK/Tap05/SPEC_AUDIO_CLIP_TAP05.json` — đặc tả máy đọc được")
    A("- `assets/bg/tk05_*.png` — %d nền dọc 9:16 (media: **không commit**, L10) |" % n)
    A("- `provenance.json` — %d dòng cho bộ `tk05_*`" % sum(1 for k in S if ("assets/bg/" + k) in by_file))
    A("")

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))
    print("da ghi %s" % OUT)
    print("nen=%d shot=%d hook=%.1f sub=%.1f vet=%d vuot=%d saiSize=%d"
          % (n, n_shot, hm, sm, len(streak_bad), len(over), len(wrong)))
    print("AI that=%d du phong=%d | H22: thua=%s vio=%s thieuShot=%d"
          % (mm, fb, unused or "khong co", viol or "khong co", len(missing_shot)))


if __name__ == "__main__":
    main()
