"""Tao bo thu giong Higgs theo hoi cho Tap 04 (tuong duong Tap 03: thu_giong_higgs_hoi3/).

- Copy clip DA CHON (higgs_selection_t04.json) vao 02_SAN_XUAT/Tap04/thu_giong_higgs/
  ten: <act>_<stt>_<id>_<vai>_cer<NN>.wav      (cer NN = CER x100 cua ban chon)
- Ghep tung hoi thanh 1 file: HOI<act>_nghe_lien.wav  (nghe lien, dung thu tu kich ban)
Input : .work/higgs_selection_t04.json + .work/timeline_s_t04.json
Output: 02_SAN_XUAT/Tap04/thu_giong_higgs/*.wav + HOI<n>_nghe_lien.wav
"""
import json
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
EPN = "04"

FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
SRC = HERE / ("audio_s_higgs_t%s" % EPN)
OUT = ROOT / "02_SAN_XUAT" / ("Tap%s" % EPN) / "thu_giong_higgs"
OUT.mkdir(parents=True, exist_ok=True)

sel = json.loads((HERE / ("higgs_selection_t%s.json" % EPN)).read_text(encoding="utf-8-sig"))["selection"]
tl = json.loads((HERE / ("timeline_s_t%s.json" % EPN)).read_text(encoding="utf-8-sig"))

# act cua tung cau: theo marker ACT
acts = sorted([m for m in tl["markers"] if m["type"] == "ACT"], key=lambda m: m["start"])
items = tl["items"]


def act_of(t):
    a = 1
    for m in acts:
        if t >= m["start"]:
            a = m["act"]
    return a


by_act = {}
for it in items:
    by_act.setdefault(act_of(it["start"]), []).append(it)

n_copied = 0
for act, its in sorted(by_act.items()):
    files = []
    for k, it in enumerate(its, 1):
        s = sel.get(it["id"])
        if not s:
            print("  !! khong co ban chon cho", it["id"])
            continue
        src = SRC / s["dst"]
        if not src.exists():
            print("  !! thieu file:", src)
            continue
        cer = s["cer"]
        cern = "cer%02d" % round(100 * cer) if cer is not None else "cerNA"
        name = "%d_%02d_%s_%s_%s.wav" % (act, k, it["id"].replace(".", "_").replace("#", "_"),
                                         it["role"], cern)
        shutil.copy2(src, OUT / name)
        files.append(OUT / name)
        n_copied += 1
    if not files:
        continue
    lst = OUT / ("_hoi%d.txt" % act)
    lst.write_text("".join("file '%s'\n" % f.as_posix() for f in files), encoding="utf-8")
    outwav = OUT / ("HOI%d_nghe_lien.wav" % act)
    r = subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c:a", "pcm_s16le", str(outwav)], capture_output=True, text=True)
    lst.unlink()
    if r.returncode != 0:
        print("  !! concat hoi %d that bai: %s" % (act, r.stderr[:300]))
    else:
        dur = subprocess.run([str(HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"),
                              "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(outwav)],
                             capture_output=True, text=True).stdout.strip()
        print("HOI%d: %d clip | nghe_lien %.1f s" % (act, len(files), float(dur or 0)))

print("tong clip copy:", n_copied, "->", OUT)
