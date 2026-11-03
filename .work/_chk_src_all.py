import pathlib, re, sys
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
EN = ROOT / "02_SAN_XUAT"
print(f"{'tap':10} {'nguon':>6} {'#link':>6} {'mo_ta co SOURCES?':>20} {'dang bang':>12} {'mo_ta #link':>10}")
for d in sorted(EN.glob("Tap*_EN")):
    src = d / "nguon_tham_khao_EN.md"
    n_src = 0; shape = "-"
    if src.exists():
        rows = [l for l in src.read_text(encoding="utf-8").splitlines() if l.startswith("| https")]
        n_src = len(rows)
        cells = rows[0].strip("|").split("|") if rows else []
        shape = f"{len(cells)}cot"
    mo = d / "xuat_ban" / "mo_ta.txt"
    has = mo.exists() and "SOURCES" in mo.read_text(encoding="utf-8")
    n_mo = 0
    if mo.exists():
        t = mo.read_text(encoding="utf-8")
        blk = t.split("SOURCES",1)[1] if "SOURCES" in t else ""
        n_mo = len(re.findall(r"https?://", blk))
        n_mo = min(n_mo, n_src) if n_src else n_mo
    print(f"{d.name:10} {n_src:6} {str(has):>20} {shape:>12} {n_mo:10}")
