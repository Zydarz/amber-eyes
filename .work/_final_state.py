import pathlib, re, hashlib, subprocess
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
OUT = ROOT / "02_SAN_XUAT" / "Tap03_EN" / "xuat_ban"
print("=== THAM PHAM ===")
for n in ("Tap03_EN_master.mp4", "Tap03_EN_master.mp3", "Tap03_EN.srt", "mo_ta.txt", "description.txt", "thumbnail.png", "nguon_tham_khao_EN.md"):
    p = OUT / n
    print(f"  {n:28} {'OK ' if p.exists() else 'THIEU'} {p.stat().st_size if p.exists() else 0:>12,} byte")
t = (OUT / "mo_ta.txt").read_text(encoding="utf-8")
i = t.find("\U0001F4DA SOURCES")
blk = t[i:].split("\n\n",1)[0]
print(f"  mo_ta.txt: {len(t)} ky tu · {len(re.findall(r'https?://', blk))} link nguon · [PENDING? {'[PENDING' in t}]")
print("=== GOC THEO TAP ===")
for n in ("KeHoach_Video_Tap03_EN.md", "CHU_CO_DINH_EN.md", "BaoCao_QC_Tap03_EN_20261103.md", "nguon_tham_khao_EN.md"):
    p = ROOT / "02_SAN_XUAT" / "Tap03_EN" / n
    print(f"  {n:36} {'OK ' if p.exists() else 'THIEU'} {p.stat().st_size if p.exists() else 0:>8,} byte")
print("=== WORK ===")
for n in ("picture.mp4",):
    p = ROOT / ".work" / "video3_EN_t03" / n
    print(f"  {n:20} {p.stat().st_size:>12,} byte")
sf = ROOT / ".work" / "video3_EN_t03" / "stills_final"
print("  stills_final:", len(list(sf.glob('*.png'))), "khung")
print("  qc sheets:", len(list((ROOT/'.work'/'qc_final_EN_t03').glob('sheet_*.png'))), "contact sheet")
