#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap07 — viet lai muc 6 (bang shot) theo 147 cau moi (A11 #67, H14).

- Doc bang shot cu (62 shot / 164 cau) tu ban luu .work/_cu/t07_shottable_147cu/
- Doi khoang 'cau' sang 147 cau moi; them shot moi cho 1.06#8 va thẻ kết 5-10
- Tinh lai 'handoff' (→X) = vai dong ke tiep (A11 #88)
- Sua caption co so khong co trong cau (QC A9.2 co so 5)
- Ghi lai file ke hoach (idempotent: luon doc tu ban luu goc)
"""
import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PLAN = ROOT / "02_SAN_XUAT" / "Tap07" / "KeHoach_Video_Tap07.md"
BACKUP = ROOT / ".work" / "_cu" / "t07_shottable_147cu"
BACKUP.mkdir(parents=True, exist_ok=True)
BAK_FILE = BACKUP / "KeHoach_Video_Tap07.md.bak"
if BAK_FILE.exists():
    SRC_FILE = BAK_FILE
else:
    shutil.copy2(PLAN, BAK_FILE)
    SRC_FILE = BAK_FILE

ROLES = ("H", "D", "C", "N1", "N2")

# ------------------------------------------------------------------ kế hoạch mới
# (new_id, old_id|None, cau|None, chu|None, nen|None, vai|None, mau|None, anchor|None)
# anchor: vị trí chèn dòng sinh mới ("old_id" hoặc "END")
NEW_ROWS = [
    # ---- HỒI 1
    ("1-00", "1-00", None, None, None, None, None, None),
    ("1-01", "1-01", None, None, None, None, None, None),
    ("1-02", "1-02", None, None, None, None, None, None),
    ("1-03", "1-03", None, None, None, None, None, None),
    ("1-04", "1-04", None, None, None, None, None, None),
    ("1-05", "1-05", None, None, None, None, None, None),
    ("1-06", "1-06", None, None, None, None, None, None),
    ("1-07", "1-07", None, None, None, None, None, None),
    # --- SHOT MỚI cho 1.06#8 ("Hãy hình dung nỗi đau của mẹ cậu, bà Lynn Roy...")
    ("1-08", None, "`1.06#8`",
     "*Gian bếp gia đình im lặng trong buổi sáng, chiếc điện thoại úp trên bàn ăn bên tách cà phê đã nguội ngắt...*",
     "`t7_mothers_empty_kitchen_phone`, `pull`", "H", "T1", "1-08"),
    ("1-09", "1-08", "`1.07#1`–`#3`", None, None, None, None, None),
    ("1-10", "1-09", "`1.07#4`–`#5`", None, None, None, None, None),
    ("1-11", "1-10", None, None, None, None, None, None),
    ("1-12", "1-11", None, None, None, None, None, None),
    ("1-13", "1-12", None, None, None, None, None, None),
    ("1-14", "1-13", None, None, None, None, None, None),
    # bìa hồ sơ: bỏ số "07" (không có trong câu → QC A9.2 cổng 5)
    ("1-15", "1-14", None,
     "*Bìa hồ sơ điều tra vụ án Amber Eyes đặt trên bàn gỗ sẫm màu, dây thừ buộc chắc bên cạnh chiếc kính lúp và cây bút sắt cạnh...*",
     None, None, None, None),
    # ---- HỒI 2
    ("2-01", "2-01", None, None, None, None, None, None),
    ("2-02", "2-02", None, None, None, None, None, None),
    # "3 giờ sáng" → "ba giờ sáng" (quy ước Tập 06: giờ viết chữ)
    ("2-03", "2-03", None,
     "*Góc phòng ngủ thiếu niên lúc ba giờ sáng, ánh sáng màn hình điện thoại xanh lạnh rọi xuống chăn nhàu nát...*",
     None, None, None, None),
    ("2-04", "2-04", None, None, None, None, None, None),
    ("2-05", "2-05", None, None, None, None, None, None),
    ("2-06", "2-06", "`2.06#1`", None, None, None, None, None),
    ("2-07", "2-07", "`2.06#2`", None, None, None, None, None),
    ("2-08", "2-08", "`2.07#1`–`#2`", None, None, None, None, None),
    ("2-09", "2-09", None, None, None, None, None, None),
    ("2-10", "2-10", "`2.09#1`–`#2`", None, None, None, None, None),
    ("2-11", "2-11", "`2.09#3`–`#4`", None, None, None, None, None),
    ("2-12", "2-12", "`2.09#5`–`#6`", None, None, None, None, None),
    ("2-13", "2-13", None,
     "*Chiếc điện thoại nằm trên nắp xe ướt đầy nước mưa, sóng âm thanh xanh lạnh nhấp nháy trên màn hình dưới ánh trăng mờ...*",
     None, None, None, None),
    ("2-14", "2-14", None, None, None, None, None, None),
    # ---- HỒI 3
    ("3-01", "3-01", None, None, None, None, None, None),
    ("3-02", "3-02", None, None, None, None, None, None),
    ("3-03", "3-03", None, None, None, None, None, None),
    ("3-04", "3-04", None, None, None, None, None, None),
    ("3-05", "3-05", None, None, None, None, None, None),
    ("3-06", "3-06", None, None, None, None, None, None),
    ("3-07", "3-07", "`3.06#4`", None, None, None, None, None),
    ("3-08", "3-08", None, None, None, None, None, None),
    ("3-09", "3-09", None, None, None, None, None, None),
    ("3-10", "3-10", "`3.08#4`–`#5`", None, None, None, None, None),
    ("3-11", "3-11", "`3.08#6`", None, None, None, None, None),
    # ---- HỒI 4
    ("4-01", "4-01", "`4.02#1`–`#4`", None, None, None, None, None),
    ("4-02", "4-02", "`4.03#1`–`#2`", None, None, None, None, None),
    ("4-03", "4-03", "`4.03#3`",
     "*Tập tài liệu in lời khai nhân chứng được đóng dấu tiếp nhận, các dòng khai về tin nhắn nằm ngay ngắn dưới con dấu đỏ...*",
     None, None, None, None),
    ("4-04", "4-04", None, None, None, None, None, None),
    ("4-05", "4-05", None, None, None, None, None, None),
    ("4-06", "4-06", None, None, None, None, None, None),
    ("4-07", "4-07", None, None, None, None, None, None),
    ("4-08", "4-08", None, None, None, None, None, None),
    ("4-09", "4-09", None, None, None, None, None, None),
    ("4-10", "4-10", None, None, None, None, None, None),
    ("4-11", "4-11", "`4.08#5`", None, None, None, None, None),
    ("4-12", "4-12", None, None, None, None, None, None),
    ("4-13", "4-13", None, None, None, None, None, None),
    # ---- HỒI 5
    ("5-01", "5-01", None, None, None, None, None, None),
    ("5-02", "5-02", "`5.02#4`–`#5`", None, None, None, None, None),
    ("5-03", "5-03", None, None, None, None, None, None),
    # T8 "cờ": nhãn số trong ngoặc nghiêng để renderer tô cờ đúng thứ tự
    # (mẫu Tập 01: *01* · **TIÊU ĐỀ**). Bản cũ ghi "Cảnh báo đỏ N: ..." → không lên hình.
    ("5-04", "5-04", "`5.04#1`–`#2`",
     "*01* · **CẢNH BÁO ĐỎ 1 — CẢNH GIÁC TRƯỚC CÁC MỐI QUAN HỆ ẢO SIÊU TỐC VÀ CÔ LẬP**",
     None, None, None, None),
    # tách shot cờ đỏ 1 (38,2 s → 2 shot) để giữ nhịp hình ngang Tập 06
    ("5-05", None, "`5.04#3`–`#4`",
     "*Bong bóng thuỷ tinh phát sáng cô lập giữa rừng cây tăm tối, bên trong là một bóng người bị giam trong không gian số khép kín không lối ra...*",
     "`t7_redflag1_isolated_virtual_bubble`, `still`", "H", "T1", "5-05"),
    ("5-06", "5-05", None, None, None, None, None, None),
    ("5-07", "5-06", "`5.04#8`–`#10`",
     "*03* · **CẢNH BÁO ĐỎ 3 — HỘI CHỨNG KHAO KHÁT SỰ CHÚ Ý VÀ KỊCH TÍN HÓA BI KỊCH**",
     None, None, None, None),
    ("5-08", "5-07", "`5.04#11`–`#12`",
     "*04* · **CẢNH BÁO ĐỎ 4 — LẮNG NGHE BẢN NĂNG SINH TỒN VÀ DỨT KHOÁT CẮT ĐỨT LIÊN LẠC**",
     None, None, None, None),
    # tách shot cờ đỏ 4 (37,9 s → 2 shot)
    ("5-09", None, "`5.04#13`–`#15`",
     "*Chiếc điện thoại thông minh bị đặt úp mặt xuống chiếc bàn gỗ sáng bên cửa sổ bình minh, ánh nắng đầu ngày rọi qua lưng điện thoại...*",
     "`t7_redflag4_disconnect_phone_dawn`, `pull`", "H", "T1", "5-08"),
    ("5-10", "5-08", "`5.04#16`–`#17`", None, None, None, None, None),
    ("5-11", "5-09", "`5.04#18`–`#19`",
     "*Chồng hồ sơ đã đóng dấu trên bàn gỗ, bên cạnh bình hoa bông hồng trắng và ngọn nến đang cháy trong buổi sáng sớm...*",
     None, None, "T1", None),
    # --- THẺ KẾT (tách khỏi câu thoại — mẫu Tập 06, H12)
    ("5-12", None, "hết tập (10 s)",
     "*HỒ SƠ TẬP 07 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật*",
     "`t7_closing_dossier_white_rose`, `pull`", "—", "T1", "END"),
]

# ------------------------------------------------------------------ đọc bảng cũ
lines = SRC_FILE.read_text(encoding="utf-8-sig").split("\n")
old_rows = {}
for i, ln in enumerate(lines):
    m = re.match(r"^\|\s*([1-5]-\d+)\s*\|", ln)
    if not m:
        continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    c += [""] * (9 - len(c))
    old_rows[c[0]] = {"id": c[0], "cau": c[1], "vai": c[2], "mau": c[3], "nen": c[4],
                       "chu": c[5], "beat": c[6], "nv": c[7], "tr": c[8], "_line": i}

missing_old = [r[1] for r in NEW_ROWS if r[1] and r[1] not in old_rows]
if missing_old:
    raise SystemExit("Dong cu khong ton tai: " + ", ".join(missing_old))

# ------------------------------------------------------------------ dựng dòng mới
rows = []
row_of_old = {}
insert_before = {}
for new_id, old_id, cau, chu, nen, vai, mau, anchor in NEW_ROWS:
    if old_id:
        src = old_rows[old_id]
        r = {k: src[k] for k in ("cau", "vai", "mau", "nen", "chu", "beat", "nv", "tr")}
    else:
        r = {"cau": "", "vai": "—", "mau": "T1", "nen": "", "chu": "", "beat": "—",
             "nv": "", "tr": "—"}
    if cau is not None:
        r["cau"] = cau
    if chu is not None:
        r["chu"] = chu
    if nen is not None:
        r["nen"] = nen
    if vai is not None:
        r["vai"] = vai
    if mau is not None:
        r["mau"] = mau
    r["id"] = new_id
    rows.append(r)
    if old_id:
        row_of_old[old_id] = r
    else:
        if anchor == "END":
            insert_before.setdefault("__END__", []).append(r)
        else:
            insert_before.setdefault(anchor, []).append(r)

# ------------------------------------------------------------------ handoff (A11 #88)
for i, r in enumerate(rows):
    nv = re.sub(r"→[A-Z0-9+]+", "", r["nv"]).strip()
    exp = []
    if i + 1 < len(rows):
        nxt = rows[i + 1]
        if r["vai"] in ROLES and nxt["vai"] in ROLES and nxt["vai"] != r["vai"]:
            exp = ["→" + nxt["vai"]]
    parts = [p for p in (nv, *exp) if p]
    r["nv"] = " · ".join(parts) if parts else "—"

# ------------------------------------------------------------------ ghi lại
out = []
written = 0
for ln in lines:
    m = re.match(r"^\|\s*([1-5]-\d+)\s*\|", ln)
    if m:
        old_id = m.group(1)
        for ins in insert_before.get(old_id, []):
            out.append("| " + " | ".join([ins["id"], ins["cau"], ins["vai"], ins["mau"],
                                          ins["nen"], ins["chu"], ins["beat"], ins["nv"],
                                          ins["tr"]]) + " |")
            written += 1
        r = row_of_old[old_id]
        out.append("| " + " | ".join([r["id"], r["cau"], r["vai"], r["mau"], r["nen"],
                                      r["chu"], r["beat"], r["nv"], r["tr"]]) + " |")
        written += 1
        # dòng sinh mới gắn cuối bảng (thẻ kết) phải nằm NGAY sau dòng cũ cuối cùng
        if old_id == "5-09":
            for ins in insert_before.get("__END__", []):
                out.append("| " + " | ".join([ins["id"], ins["cau"], ins["vai"], ins["mau"],
                                              ins["nen"], ins["chu"], ins["beat"], ins["nv"],
                                              ins["tr"]]) + " |")
                written += 1
    else:
        out.append(ln)
assert written == len(rows), f"so dong ghi {written} != {len(rows)}"

text = "\n".join(out)
text = text.replace("5 hồi · 164 câu thoại", "5 hồi · 147 câu thoại")
text = text.replace("chuẩn hóa trích dẫn `“…”` (164/164 câu)",
                    "chuẩn hóa trích dẫn `“…”` (147/147 câu)")
text = text.replace("**Tổng: 62 shot** (1 shot mở đầu 1-00 + 61 shot theo câu thoại). "
                    "Phủ kín 164 câu thoại trọn vẹn.",
                    "**Tổng: 66 shot** (1 shot mở đầu 1-00 + 64 shot theo câu thoại "
                    "+ 1 shot thẻ kết). Phủ kín 147 câu thoại trọn vẹn "
                    "(bảng viết lại 03/11/2026 sau khi vá V9).")

PLAN.write_text(text, encoding="utf-8")

print(f"Da ghi {len(rows)} dong vao {PLAN.name}")
print(f"Ban luu goc: {BAK_FILE}")
print()
for r in rows:
    print(f"{r['id']:>5} | {r['cau']:<24} | {r['vai']:<3} | {r['mau']:<14} | "
          f"{r['nen'][:46]:<46} | nv={r['nv']}")
