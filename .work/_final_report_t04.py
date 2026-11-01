"""Bao cao giam sat cuoi Tap 04 — chay 3 cong QC + kiem ke thanh pham, gom 1 file md.

Usage: py -3 .work/_final_report_t04.py --ep 04
Output: 02_SAN_XUAT/Tap04/BAO_CAO_GIAM_SAT_T04.md
"""
import argparse
import json
import pathlib
import subprocess
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FP = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

ap = argparse.ArgumentParser()
ap.add_argument("--ep", default="04")
a = ap.parse_args()
ep = a.ep
OUT = ROOT / "02_SAN_XUAT" / ("Tap%s" % ep)

env = {"AE_EP": ep, "PYTHONIOENCODING": "utf-8", "PATH": None}


def run(script, args=()):
    r = subprocess.run([sys.executable, str(WORK / script), *args], cwd=str(ROOT),
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={**dict(__import__("os").environ), "AE_EP": ep, "PYTHONIOENCODING": "utf-8"})
    return (r.stdout or "") + (("\n[stderr]\n" + r.stderr) if r.stderr.strip() else "")


def dur(p):
    r = subprocess.run([str(FP), "-v", "error", "-show_entries", "format=duration", "-of",
                        "csv=p=0", str(p)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip().splitlines()[0])
    except Exception:
        return None


def human(n):
    return "%.1f MB" % (n / 1e6) if n is not None else "?"


parts = []
parts.append("# BÁO CÁO GIÁM SÁT — TẬP %s (dựng lại %s)" % (ep, datetime.now().strftime("%d/%m/%Y %H:%M")))

# ---- 1. bang do ----
tl = json.loads((WORK / ("timeline_s_t%s.json" % ep)).read_text(encoding="utf-8-sig"))
sh = json.loads((WORK / ("shots_t%s.json" % ep)).read_text(encoding="utf-8-sig"))
sel = json.loads((WORK / ("higgs_selection_t%s.json" % ep)).read_text(encoding="utf-8-sig"))
rows = sel["selection"]
parts.append("## 1. Số đo nền\n")
parts.append("| Hạng mục | Giá trị |")
parts.append("|---|---|")
parts.append("| Câu trong kịch bản / timeline | %d |" % len(tl["items"]))
parts.append("| Timeline total | %.3f s |" % tl["total"])
parts.append("| Shot | %d (tb %.1f s · dài nhất %.1f s · ngắn nhất %.1f s) |" % (
    len(sh["shots"]),
    sum(s["end"] - s["start"] for s in sh["shots"]) / len(sh["shots"]),
    max(s["end"] - s["start"] for s in sh["shots"]),
    min(s["end"] - s["start"] for s in sh["shots"])))
parts.append("| Shot dài > 16 s | %d/%d |" % (
    sum(1 for s in sh["shots"] if s["end"] - s["start"] > 16), len(sh["shots"])))
parts.append("| Bản Higgs đã chọn | %d câu · CER TB %.2f%% · câu > 2%%: %d |" % (
    len(rows), 100 * sum(v["cer"] for v in rows.values() if v["cer"] is not None) / len(rows),
    sum(1 for v in rows.values() if v["cer"] is not None and v["cer"] > 0.02)))
parts.append("| Lệch shots ↔ timeline | %.4f s |" % abs(sh["total"] - tl["total"]))
parts.append("")

# ---- 2. cong QC ----
for title, script, args in (
    ("2. Cổng P10 — audio master", "qc_tap04.py", ("--gate", "P10", "--ep", ep)),
    ("3. Cổng bảng shot", "qc_shots_t04.py", ("--ep", ep)),
    ("4. Cổng giám sát cuối A–G", "qc_video_t04.py", ("--ep", ep)),
):
    out = run(script, args)
    parts.append("## %s\n" % title)
    parts.append("```\n%s\n```\n" % out.strip())

# ---- 3. kem ke thanh pham ----
parts.append("## 5. Kiểm kê thành phẩm\n")
parts.append("| File | Dung lượng | Thời lượng |")
parts.append("|---|---|---|")
for f in sorted((OUT / "xuat_ban").glob("*")):
    d = dur(f) if f.suffix in (".mp4", ".mp3", ".wav") else None
    parts.append("| `xuat_ban/%s` | %s | %s |" % (f.name, human(f.stat().st_size),
                                                  ("%.2f s" % d) if d else "—"))
parts.append("")

outp = OUT / ("BAO_CAO_GIAM_SAT_T%s.md" % ep)
outp.write_text("\n".join(parts), encoding="utf-8")
print("->", outp)
