"""Sua 2 cong QC bi DUONG TINH GIA trong qc_video_t04.py.

A) "loi dau": `first_speech()` dung silencedetect tren file hop co NHAC NEN
   => khong co khoang lang nao (nhac luon > -50 dBFS) => silence_end dau tien
   la o CUOI TAP (1256,52 s) => bao sai. Do lai tu STEM giong (16 kHz, khong nhac).
B) "phu de": so SO CUE voi SO CAU. subtitles.py TACH CAU dai thanh nhieu cue
   (2 dong x 42 ky tu, <= 6 s) => 324 cue cho 154 cau la DUNG.
   Doi chieu NOI DUNG: noi dung phu de (bo nhan vai) == noi dung kich ban.

Van doi duong cu cho tap khac: chi sua qc_video_t04.py (cong rieng cua T04).
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
QC = HERE / "qc_video_t04.py"


def eol_of(raw):
    return "\r\n" if "\r\n" in raw else "\n"


raw = QC.read_text(encoding="utf-8", newline="")
eol = eol_of(raw)
print("EOL:", repr(eol))

pairs = []

# --- (1) them ham do loi dau tu stem ---
old_fn = ('def first_speech(path):' + eol +
          '    r = run([FF, "-hide_banner", "-nostats", "-i", path, "-af",' + eol +
          '             "silencedetect=noise=-50dB:d=0.5", "-f", "null", "-"])' + eol +
          '    m = re.findall(r"silence_end:\\s*([\\d.]+)", r.stderr)' + eol +
          '    return float(m[0]) if m else None')
new_fn = ('def first_speech(path):' + eol +
          '    """Thoi diem LOI DAU do tu STEM giong (khong nhac nen).' + eol +
          '' + eol +
          '    `silencedetect` tren file hop khong dung: nhac nen luon tren -50 dBFS' + eol +
          '    nen khong co khoang lang nao -> silence_end dau tien ruc o CUOI tap.' + eol +
          '    Stem giong (16 kHz, chi giong) moi do dung thoi diem bat dau len tieng.' + eol +
          '    """' + eol +
          '    import numpy as np' + eol +
          '    import soundfile as sf' + eol +
          '    best = None' + eol +
          '    for role in ("H", "D", "C", "N1", "N2"):' + eol +
          '        p = pathlib.Path(ED.w("stems")) / f"{role}.wav"' + eol +
          '        if not p.exists():' + eol +
          '            return None' + eol +
          '        x, sr = sf.read(str(p), dtype="float32")' + eol +
          '        if len(x) == 0:' + eol +
          '            continue' + eol +
          '        idx = np.where(np.abs(x) > 10 ** (-50 / 20))[0]' + eol +
          '        if len(idx) == 0:' + eol +
          '            continue' + eol +
          '        t = float(idx[0]) / sr' + eol +
          '        best = t if best is None else min(best, t)' + eol +
          '    return best')
pairs.append((old_fn, new_fn))

# --- (2) gate E: doi chieu noi dung ---
old_e = ('        t = srt.read_text(encoding="utf-8-sig")' + eol +
         '        cues = re.findall(r"-->\\s*(\\d+):(\\d+):(\\d+)[,.](\\d+)", t)' + eol +
         '        n = len(cues)' + eol +
         '        sc2 = json.loads(ED.EP["script"].read_text(encoding="utf-8-sig"))' + eol +
         '        want2 = sum(len(el.get("sentences", [])) for el in sc2 if el.get("kind") == "LOI")' + eol +
         '        if n == want2:' + eol +
         '            ok(f"E) phu de {n} cue = so cau ({want2})")' + eol +
         '        else:' + eol +
         '            bad(f"E) phu de {n} cue != so cau {want2}")')
new_e = ('        t = srt.read_text(encoding="utf-8-sig")' + eol +
         '        cues = re.findall(r"-->\\s*(\\d+):(\\d+):(\\d+)[,.](\\d+)", t)' + eol +
         '        n = len(cues)' + eol +
         '        sc2 = json.loads(ED.EP["script"].read_text(encoding="utf-8-sig"))' + eol +
         '        want2 = sum(len(el.get("sentences", [])) for el in sc2 if el.get("kind") == "LOI")' + eol +
         '        # So NOI DUNG: phu de tach cau dai thanh nhieu cue nen khong the so cue voi so cau.' + eol +
         '        blocks = [b for b in re.split(r"\\r?\\n\\r?\\n", t.strip()) if b.strip()]' + eol +
         '        srt_txt = " ".join(" ".join(b.splitlines()[2:]) for b in blocks)' + eol +
         '        srt_txt = re.sub(r"\\[[^\\]]*\\]", " ", srt_txt)' + eol +
         '        scr_txt = " ".join(i["text"] for i in TL["items"])' + eol +
         '        nz = lambda x: re.sub(r"\\s+", "", x).casefold()' + eol +
         '        if nz(srt_txt) == nz(scr_txt):' + eol +
         '            ok(f"E) phu de phu 100% loi thoai ({n} cue / {want2} cau)")' + eol +
         '        else:' + eol +
         '            a, b = nz(srt_txt), nz(scr_txt)' + eol +
         '            k = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))' + eol +
         '            bad(f"E) noi dung phu de KHONG khop kich ban (sai tu ky tu {k}: "' + eol +
         '                f"phu de ...{a[max(0, k - 20):k + 20]}... / kich ban ...{b[max(0, k - 20):k + 20]}...)")')
pairs.append((old_e, new_e))

for old, new in pairs:
    n = raw.count(old)
    if n != 1:
        raise SystemExit("!! anchor khong dung (%d lan):\n%r" % (n, old[:200]))
    raw = raw.replace(old, new, 1)

QC.write_text(raw, encoding="utf-8", newline="")
print("OK qc_video_t04.py: gate A (loi dau tu stem) + gate E (doi chieu noi dung)")

import subprocess
print("py_compile rc =", subprocess.run([sys.executable, "-m", "py_compile", str(QC)]).returncode)
