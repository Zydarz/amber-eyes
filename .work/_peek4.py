import pathlib
EN = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT")
for tap in ("Tap07_EN","Tap03_EN","Tap04_EN"):
    d = EN / tap
    tpl = list(d.glob("CHU_CO_DINH*.md"))
    mo = d / "xuat_ban" / "mo_ta.txt"
    print(f"=== {tap} · mo_ta.txt {len(mo.read_text(encoding='utf-8')) if mo.exists() else '-'} ky tu · template: {[p.name for p in tpl]}")
