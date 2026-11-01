"""Thay muc 6 (bang shot) cua ke hoach Tap04 bang bang shot moi (154 cau).

Lam an toan: sao luu file ke hoach cu truoc khi ghi de (L5), chi thay DUNG
khoi muc 6, giu nguyen phan con lai cua ke hoach.
"""
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
PLAN = ROOT / "02_SAN_XUAT" / "Tap04" / "KeHoach_Video_Tap04.md"
NEW = ROOT / ".work" / "_shots_t04_new.md"
BK = ROOT / ".work" / "_cu" / "kehoach_tap04_truoc_bangshot_20261031.md"

src = PLAN.read_text(encoding="utf-8-sig")
new_sec = NEW.read_text(encoding="utf-8-sig")

i = src.index("## 6.")
# ket thuc muc 6: dong "**Tổng:" gan nhat sau do
j = src.index("\n**Tổng:", i)
j = src.index("\n", src.index("\n", j) + 1) + 1
old_sec = src[i:j]

BK.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(PLAN, BK)
print(f"Sao luu: {BK.name} ({BK.stat().st_size} bytes)")

out = src[:i] + new_sec.rstrip("\n") + "\n\n" + src[j:]
PLAN.write_text(out, encoding="utf-8")
print(f"Da ghi: {PLAN.name} ({PLAN.stat().st_size} bytes)")
print(f"  section 6 cu: {len(old_sec)} ky tu -> moi: {len(new_sec)} ky tu")
