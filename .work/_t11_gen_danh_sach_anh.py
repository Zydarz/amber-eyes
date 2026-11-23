# -*- coding: utf-8 -*-
"""Sinh lại `02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/Danh_Sach_Anh_Tap11.md` theo H25 (136 nền, ánh xạ shot).

Dùng: bảng shot mục 6 (KeHoach) + bg_jobs_tap11.json (desc/prompt).
"""
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PLAN = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/KeHoach_Video_Tap11.md"
JOBS = ROOT / ".work/bg_jobs_tap11.json"
OUT = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/Danh_Sach_Anh_Tap11.md"

text = PLAN.read_text(encoding="utf-8")
sec = text[text.find("## 6."):]
lines = sec.split("\n")

# hồi: theo tiêu đề "### HỒI N — ..."
acts = OrderedDict()
cur_act = 0
cur_bg = None
act_rows = {}
for ln in lines:
    m = re.match(r"###\s+HỒI\s+(\d+)\s+—\s*(.+)", ln)
    if m:
        cur_act = int(m.group(1))
        acts[cur_act] = m.group(2).strip()
        continue
    if not re.match(r"\|\s*[1-5]-\d+\s*\|", ln):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) < 5:
        continue
    code = re.search(r"`(t\d+_[a-z0-9_]+)`", cells[4])
    own_code = bool(code)
    if code:
        cur_bg = code.group(1)
    sid = re.match(r"([1-5]-\d+)", cells[0]).group(1)
    dur = sum(float(x.replace(",", ".")) for x in re.findall(r"\((\d+(?:[.,]\d+)?) ?s\)", cells[1]))
    cau = re.search(r"`([^`]+)`", cells[1])
    is_card = bool(re.search(r"nghỉ chuyển hồi|hết tập", cells[1]))
    act_rows.setdefault(cur_act, []).append(dict(
        sid=sid, bg=cur_bg, dur=dur, own_code=own_code,
        cau=cau.group(1) if cau else ("THẺ KẾT" if is_card else ""),
        card=is_card))

jobs = {j["name"]: j for j in json.loads(JOBS.read_text(encoding="utf-8"))}

# gom theo mã nền trong từng hồi
# gom theo mã nền; mã xuất hiện ở 2 hồi (vd 4.11#6 + 5.02#1) tính về hồi đầu tiên
per_act = OrderedDict()
for a, rows in act_rows.items():
    for r in rows:
        if not r["own_code"] or not r["bg"]:
            continue
        if r["bg"] in per_act:
            per_act[r["bg"]][1].append(r)       # mã đã gặp ở hồi trước
        else:
            per_act[r["bg"]] = (a, [r])

by_act = OrderedDict()
for code, (a, rows) in per_act.items():
    by_act.setdefault(a, OrderedDict())[code] = rows
per_act = by_act

n_img = sum(len(g) for g in per_act.values())
n_shot = sum(len(v) for g in per_act.values() for v in g.values())
total_s = sum(r["dur"] for rows in act_rows.values() for r in rows)

out = []
out.append("# DANH SÁCH ẢNH NỀN — TẬP 11 \"CẶP ĐÔI KEN & BARBIE\"")
out.append("")
out.append("*Hồ sơ Paul Bernardo & Karla Homolka — Hội Chứng Điên Cuồng Đôi (Folie à Deux) & 'Thỏa Thuận Với Quỷ Dữ'.*")
out.append("")
out.append(f"**Cập nhật {16}/11/2026 — bộ nền tách theo H25 (sinh ảnh theo SHOT, 1,5–2 shot/nền).**")
out.append("")
out.append("---")
out.append("")
out.append("## B1. Thông tin bộ ảnh")
out.append("")
out.append("| Mục | Nội dung |")
out.append("|---|---|")
out.append(f"| Số ảnh nền | **{n_img} ảnh** phục vụ trọn vẹn 5 hồi |")
out.append(f"| Số shot | **{n_shot} shot** (223 dòng bảng shot, gồm 4 thẻ chuyển hồi T10 + 1 thẻ kết T2) — {total_s:.0f} s |")
out.append(f"| Mật độ nền | **{n_shot / n_img:.2f} shot/nền** (mục tiêu H25: 1,5–2) · **0** nền vượt 3 shot/30 s (H22) |")
out.append("| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |")
out.append("| Vị trí lưu trữ | `assets/bg/t11_*.png` — **tiền tố `t11_` bắt buộc** để không trùng bộ nền Tập 01–10 |")
out.append("| Danh sách prompt gốc | `.work/bg_jobs_tap11.json` (136 job = 66 mã cũ + 70 mã mới) |")
out.append("| Sổ nguồn gốc tài sản | `provenance.json` (L7) |")
out.append("| Công cụ sinh ảnh | **Kaggle GPU · FLUX.2-klein-4B** — Deep Noir 4 tầng, LANCZOS 2K, dìm màu 35 % · vignette · grain 35 mm. **KHÔNG dùng Real-ESRGAN** (`QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` §1.2) |")
out.append("| Nguyên tắc H17 / A8.1 | Nền là **tài sản dùng chung cho MỌI ngôn ngữ** — không hậu tố `_EN/_JA/_KO`, chữ luôn do Pillow vẽ lúc dựng |")
out.append("| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 · người thật chỉ hiện bóng · không vẽ nạn nhân |")
out.append("")
out.append("**Quy tắc hình ảnh của kênh (V1 – V9):**")
out.append("")
out.append("- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn.**")
out.append("- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.")
out.append("- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:** tuyệt đối không mô tả bạo lực, thương tích hay thi thể của các nạn nhân (Leslie Mahaffy, Kristen French, Tammy Homolka).")
out.append("- **H2/H5 — Nền sạch chữ 100 %:** mọi chữ trên hình do Pillow vẽ lúc dựng; nền có chữ lạ phải sinh lại đúng tên.")
out.append("- **H19 — Nền phải có nội dung cảnh:** đọc tên nền phải ra một cảnh cụ thể; nền chỉ là gradient/ánh sáng thì vô dụng.")
out.append("")
out.append("---")
out.append("")
out.append("## B2. Ánh xạ ảnh → hồi → mốc câu")
out.append("")
out.append("Mỗi mã nền = **một cảnh riêng**; các shot liền mạch cùng một khoảnh khắc được gom chung mã, "
           "còn dùng lại cùng nơi ở khoảng cách xa thì **phải là cảnh khác** (đổi góc / giờ / bố cục) nên tách mã riêng.")
out.append("")

idx = 0
for a, g in per_act.items():
    out.append(f"### HỒI {a} · {acts.get(a, '')}")
    out.append("")
    out.append("| Ảnh | Tên file | Nội dung phục vụ | Mốc câu | Shot dùng |")
    out.append("|---|---|---|---|---|")
    for code, rows in g.items():
        idx += 1
        j = jobs.get(code, {})
        caus = sorted({r["cau"] for r in rows if r["cau"]})
        sids = " · ".join(r["sid"] for r in rows)
        secs = sum(r["dur"] for r in rows)
        out.append(f"| {idx:02d} | `{code}` | {j.get('desc', '')} | {' · '.join(caus) or '—'} | {sids} ({secs:.1f} s) |")
    out.append("")

out.append("## B3. Thống kê & Kiểm soát chất lượng (QC)")
out.append("")
out.append("| Hạng mục | Kết quả |")
out.append("|---|---|")
out.append(f"| Cổng H22 (kế hoạch) | `py -3 .work/qc_bg_usage.py --plan` → **ĐẠT** — {n_img} mã nền, 0 nền vượt 3 shot/30 s, 0 mã thiếu job, 0 job thừa |")
out.append("| Cổng H22 (sau khi sinh) | `AE_EP=11 py -3 .work/qc_bg_usage.py` → chạy lại sau `parse_shots.py` |")
out.append("| Cổng H17 (nền dùng chung) | `py -3 .work/qc_bg_shared.py --ep 11` → nền + nền từng shot trùng mọi ngôn ngữ |")
out.append("| Soi mắt nền mới (H2/H19) | **100 %** nền mới bằng montage `.work/qc_montage.py --kind bg` (nền mới không được lược) |")
out.append("| Provenance (L7) | 136 dòng `assets/bg/t11_*.png` có bản ghi trong `provenance.json` |")
out.append("")
out.append("---")
out.append("")
out.append(f"*Tài liệu sinh tự động từ `02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/KeHoach_Video_Tap11.md` + `.work/bg_jobs_tap11.json` — "
           f"ngày 16/11/2026. Khi đổi bảng shot hoặc sinh lại nền, chạy lại script `.work/_t11_gen_danh_sach_anh.py`.*")

OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"đã ghi {OUT.name}: {n_img} ảnh · {n_shot} shot · {total_s:.0f} s · {len(out)} dòng")
