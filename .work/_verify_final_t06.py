"""Kiem chung CUOI: thanh pham + tai lieu sau khi dung lai Tap06."""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
OUT = ROOT / "02_SAN_XUAT" / "Tap06" / "xuat_ban"
ok = True


def chk(cond, msg):
    global ok
    print(("  OK   " if cond else "  FAIL ") + msg)
    if not cond:
        ok = False


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


print("== 1. THANH PHAM ==")
master = OUT / "Tap06_master.mp4"
chk(master.exists(), f"Tap06_master.mp4 ton tai ({master.stat().st_size:,} B)")
chk(sha(master).startswith("951bb0ba44f2"), f"sha256 khop: {sha(master)[:16]}…")
for n in ("Tap06_master.mp3", "Tap06.srt", "mo_ta.txt", "nguon_tham_khao.md", "thumbnail.png"):
    p = OUT / n
    chk(p.exists() and p.stat().st_size > 0, f"{n} ({p.stat().st_size:,} B)")

pic = ROOT / ".work" / "video3_t06" / "picture.mp4"
chk(pic.exists() and pic.stat().st_size == 446191166, f"picture.mp4 {pic.stat().st_size:,} B")

print("\n== 2. TAI LIEU: BOM / NUL / CRLF ==")
for rel in ("02_SAN_XUAT/Tap06/BaoCao_QC_Tap06_20261102.md",
            "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md",
            "00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md",
            "README.md", "provenance.json"):
    b = (ROOT / rel).read_bytes()
    chk(b[:3] != b"\xef\xbb\xbf", f"{rel}: khong BOM")
    chk(b.count(0) == 0, f"{rel}: 0 byte NUL")

print("\n== 3. A11: lien tiep 1..N, khong trung ==")
txt = (ROOT / "00_TIEU_CHUAN" / "TIEU_CHUAN_DUNG_VIDEO.md").read_text(encoding="utf-8")
nums = [int(m.group(1)) for m in re.finditer(r"(?m)^\|\s*(\d+)\s*\|", txt)]
chk(len(set(nums)) == len(nums), f"khong trung so ({len(nums)} muc)")
chk(nums == list(range(1, len(nums) + 1)), f"lien tiep 1..{len(nums)}")
chk(len(nums) == 103, f"co du 103 muc (them #100-#103)")

print("\n== 4. PROVENANCE ==")
d = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
files = [x.get("file") for x in d]
chk(len(set(files)) == len(files), f"khong trung 'file' ({len(d)} muc)")
need = [".work/_build_video3_split.py", ".work/_concat_t06_parts.py", ".work/_qc_lag_t06.py",
        "02_SAN_XUAT/Tap06/xuat_ban/Tap06_master.mp4"]
for n in need:
    chk(n in files, f"co dong provenance: {n}")
mp4 = next(x for x in d if x.get("file", "").endswith("Tap06_master.mp4"))
chk(mp4.get("sha256") == sha(master), "sha256 trong provenance == file thật")
chk(mp4.get("ngay") == "2026-11-03", f"ngay = {mp4.get('ngay')}")

print("\n== 5. BAO CAO QC: co bang do ==")
qc = (ROOT / "02_SAN_XUAT/Tap06" / "BaoCao_QC_Tap06_20261102.md").read_text(encoding="utf-8")
for s in ("23 OK · 2 cảnh báo · 0 lỗi", "+0,0 ms", "37.751 frame", "12/12 khớp",
          "951bb0ba44f2", "4.138 ký tự", "321 cue"):
    chk(s in qc, f"báo cáo có: {s}")

print("\n== 6. BUILD_VIDEO3.PY KHONG DOI ==")
r = subprocess.run(["git", "diff", "--stat", "--", ".work/build_video3.py"], cwd=str(ROOT),
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
chk(not r.stdout.strip(), f"build_video3.py khong bi sua ({r.stdout.strip() or 'diff rong'})")

print("\n== KET QUA ==")
print("TAT CA DA DAT" if ok else "CO MUC FAIL")
sys.exit(0 if ok else 1)
