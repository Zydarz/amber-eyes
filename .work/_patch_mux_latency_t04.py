"""Vá (byte-level, EOL-safe):
 1) package.py      : alimiter them `latency=1` (bo sung do lech 4,98 ms + hien tuong "no" full-scale)
                      + khoa `mux_af` theo tap (mac dinh giu nguyen duong cu cho T01/T02)
 2) qc_video_t04.py : gate A "loi dau" do tu STEM giong (khong dung silencedetect tren hop nhac nen)
                      + gate E "phu de" doi chieu NOI DUNG (khong so so cue voi so cau)
 3) edition.py      : EPISODES["04"]["mux_af"] = limiter co latency=1
L5: backup truoc khi sua -> .work/_cu/mux_latency_20261031/
"""
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
BAK = HERE / "_cu" / "mux_latency_20261031"
BAK.mkdir(parents=True, exist_ok=True)

for f in ("package.py", "qc_video_t04.py", "edition.py"):
    src = HERE / f
    if not (BAK / f).exists():
        shutil.copy2(src, BAK / f)
print("backup ->", BAK)


def eol_of(raw):
    return "\r\n" if "\r\n" in raw else "\n"


def patch(path, pairs):
    p = pathlib.Path(path)
    raw = p.read_text(encoding="utf-8", newline="")
    eol = eol_of(raw)
    for old, new in pairs:
        n = raw.count(old)
        if n != 1:
            raise SystemExit("!! %s: anchor %d lan (can 1):\n%r" % (path.name, n, old[:120]))
        raw = raw.replace(old, new, 1)
    p.write_text(raw, encoding="utf-8", newline="")
    print("OK %s | +%d dong | EOL %r" % (p.name, raw.count("\n") - p.read_text(encoding="utf-8", newline="").count("\n"), eol))


# ---------------------------------------------------------------- 1. package.py
pkg = HERE / "package.py"
raw = pkg.read_text(encoding="utf-8", newline="")
eol = eol_of(raw)
old_cmd = ('    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(ED.w("video3") / "picture.mp4"),' + eol +
           '                    "-i", str(ED.w("audio_master.wav")), "-map", "0:v", "-map", "1:a",' + eol +
           '                    "-c:v", "copy", "-af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled",' + eol +
           '                    "-c:a", "aac", "-b:a", "192k", "-shortest",' + eol +
           '                    "-movflags", "+faststart", str(out)], check=True)')
new_cmd = ('    # A7 + A11 #64: `latency=1` bu tri do lech cua dong tre cua alimiter\n'
           '    # (khong bu = audio lech 4,98 ms so voi hinh + burst full-scale tai 869,496 s).\n'
           '    # De duong cu cho T01/T02: khoa `mux_af` theo tap; mac dinh giu nguyen chuoi cu.\n'
           '    mux_af = ED.EP.get("mux_af",' + eol +
           '                   "alimiter=limit=0.7943:attack=5:release=50:level=disabled")' + eol +
           '    cmd = [str(FF), "-y", "-v", "error", "-i", str(ED.w("video3") / "picture.mp4"),' + eol +
           '           "-i", str(ED.w("audio_master.wav")), "-map", "0:v", "-map", "1:a",' + eol +
           '           "-c:v", "copy"]' + eol +
           '    if mux_af:' + eol +
           '        cmd += ["-af", mux_af]' + eol +
           '    cmd += ["-c:a", "aac", "-b:a", "192k", "-shortest",' + eol +
           '            "-movflags", "+faststart", str(out)]' + eol +
           '    subprocess.run(cmd, check=True)')
patch(pkg, [(old_cmd, new_cmd)])

# ---------------------------------------------------------------- 2. edition.py
ed = HERE / "edition.py"
raw = ed.read_text(encoding="utf-8", newline="")
eol = eol_of(raw)
anchor = '        "voice_credit": "This audio was created with Boson AI\'s Higgs Audio — https://www.boson.ai/higgs-audio",'
if '"mux_af"' not in raw:
    # EP04: them ngay sau dong voice_credit cua EP04 (dong dau tien trong EP03)
    i = raw.find('"04": {')
    j = raw.find(anchor, i)
    if i < 0 or j < 0:
        raise SystemExit("!! edition.py: khong tim thay EP04 + voice_credit")
    k = raw.find(eol, j) + len(eol)
    raw = raw[:k] + '        "mux_af": "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1",' + eol + raw[k:]
    ed.write_text(raw, encoding="utf-8", newline="")
    print("OK edition.py: EP04 + mux_af (latency=1)")
else:
    print("edition.py da co mux_af")

print("\n--- verify ---")
import subprocess
code = ("import sys;sys.path.insert(0,r'D:\\TEST\\Gax\\amber-eyes\\.work');"
        "sys.path.insert(0,r'D:\\TEST\\Gax\\amber-eyes');"
        "import edition as ED;print('EP04 mux_af =', ED.EPISODES['04'].get('mux_af'));"
        "print('EP02 mux_af =', ED.EPISODES['02'].get('mux_af'))")
r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, encoding="utf-8", errors="replace")
print(r.stdout.strip() or r.stderr.strip()[-500:])
for f in ("package.py", "edition.py", "qc_video_t04.py"):
    rc = subprocess.run([sys.executable, "-m", "py_compile", str(HERE / f)]).returncode
    print("py_compile %-18s rc=%d" % (f, rc))
