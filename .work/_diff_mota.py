import pathlib, difflib
a = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_cu\en_t03_fix_20261103\mo_ta.txt.bak").read_text(encoding="utf-8").splitlines()
b = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban\mo_ta.txt").read_text(encoding="utf-8").splitlines()
out = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_diff_mota.txt")
txt = "\n".join(difflib.unified_diff(a, b, "cu", "moi", lineterm="", n=2))
out.write_text(txt, encoding="utf-8")
print("diff lines:", len(txt.splitlines()))
# kiem tra khoi CHAPTERS / SOURCES trong file moi
new = "\n".join(b)
for k in ("CHAPTERS", "SOURCES", "Amber Eyes", "111", "988"):
    print(f"  {k!r} trong mo_ta.txt moi: {k in new}")
print("--- dong dau file moi ---")
for l in b[:6]: print("   ", l[:150])
