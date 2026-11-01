"""Vá thẻ vai N2 của Tập 04 theo K3 (người dùng duyệt 31/10/2026).

Vấn đề: sau khi vá kịch bản, lượt N2 KHÔNG còn nói ngôi thứ nhất như Amy
Loughren — Điều tra viên dẫn "Hãy hình dung tâm trạng của một người y tá khi ấy"
(xem `01_KICH_BAN/Tap04/REVIEW_kichban_tap04.md`, mục K3 của "Vá nội dung lần 2").

Nhưng `edition.py` vẫn còn:
  n2 = ("AMY LOUGHREN", "Đồng nghiệp trực tiếp", "AMY")
→ ROLE_NAME["N2"] = ("AMY LOUGHREN", "Đồng nghiệp trực tiếp") hiện trên THẺ
  GIỚI THIỆU, và SUB_TAG["N2"] = "AMY" hiện trên MỖI dòng thoại N2.
  Tức là gán lời bịa cho người thật ⇒ vi phạm K3.

Sửa: đổi thành nhân vật hình dung, theo đúng tiền lệ Tập 01
(`"n1": ("BINH SĨ CĂN CỨ TRENTON", "Nhân vật hình dung", "BINH SĨ")`).

Luật áp dụng: A11 (vá ĐÚNG giá trị, giữ dấu nháy, import thật để kiểm),
L5 (đã sao lưu .work/_cu/bed_t04_20261031/edition.py).

Chạy:  py -3 .work/_patch_n2_t04.py
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
ED = ROOT / ".work" / "edition.py"

src = ED.read_text(encoding="utf-8")

OLD = '"n2": ("AMY LOUGHREN", "Đồng nghiệp trực tiếp", "AMY"),'
NEW = '"n2": ("Y TÁ CA ĐÊM", "Nhân vật hình dung", "Y TÁ CA ĐÊM"),'

if OLD not in src:
    print("KHONG TIM THAY dong n2 can sua — DUNG (co the da sua roi)")
    sys.exit(1)
if src.count(OLD) != 1:
    print(f"CANH BAO: tim thay {src.count(OLD)} lan — DUNG")
    sys.exit(1)

new_src = src.replace(OLD, NEW)

# chốt: khác duy nhất la 1 dong nay
if src.replace(OLD, "") != new_src.replace(NEW, ""):
    print("SAI: thay doi ngoai dong n2 — DUNG")
    sys.exit(1)

ED.write_text(new_src, encoding="utf-8")
print("DA VA:")
print("  CU :", OLD)
print("  MOI:", NEW)
