"""Sua cong G (the ket) trong qc_video_t04.py: do DO SANG thay vi kich thuoc file.

Hien tai: chi kiem `png.stat().st_size > 5000` ⇒ khung DEN trong (44 KB) cung "OK".
A11 #55: "trich khung tai timeline.total - 2 s ... xem the ket co that khong".
Sua:
  - trich khung theo gioi thuc cua shot cuoi (start + 1,5 s) va do % pixel sang (chu trang)
    => bat duoc loi "mat the ket" that su
  - trich them khung tai total-2 s va BAO CAO: renderer mo dan shot cuoi ra den 3 s cuoi
    (dung chung T01-T03) => khung nay den la hop le, khong phai loi
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
QC = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\qc_video_t04.py")
raw = QC.read_text(encoding="utf-8", newline="")
eol = "\r\n" if "\r\n" in raw else "\n"

old_helper = ('def main():' + eol)
new_helper = ('def bright_ratio(png, thr=140):' + eol +
              '    """Ti le pixel sang (>thr) cua khung — do bang mau chu tren hinh (242,239,233)."""' + eol +
              '    from PIL import Image' + eol +
              '    with Image.open(png) as im:' + eol +
              '        g = im.convert("L")' + eol +
              '        w, h = g.size' + eol +
              '        px = g.load()' + eol +
              '        n = 0' + eol +
              '        tot = 0' + eol +
              '        for y in range(0, h, 4):' + eol +
              '            for x in range(0, w, 4):' + eol +
              '                tot += 1' + eol +
              '                if px[x, y] > thr:' + eol +
              '                    n += 1' + eol +
              '        return n / max(1, tot)' + eol +
              eol +
              eol +
              'def main():' + eol)
if raw.count(old_helper) != 1:
    raise SystemExit("!! khong tim def main()")
raw = raw.replace(old_helper, new_helper, 1)

old_g = ('    # ---------------- G. the ket' + eol +
         '    if final.exists():' + eol +
         '        tot = dur(final)' + eol +
         '        if tot:' + eol +
         '            png = WORK / f"_qc_endcard_{ep}.png"' + eol +
         '            r = run([FF, "-v", "error", "-ss", f"{max(0, tot - 2):.3f}", "-i", final,' + eol +
         '                     "-frames:v", "1", "-y", str(png)])' + eol +
         '            if png.exists() and png.stat().st_size > 5000:' + eol +
         '                ok(f"G) trich khung the ket tai {tot - 2:.2f}s OK ({png.stat().st_size} bytes)")' + eol +
         '                print(f"  (khung the ket: {png})")' + eol +
         '            else:' + eol +
         '                bad(f"G) khong trich duoc khung the ket tai {tot - 2:.2f}s")')
new_g = ('    # ---------------- G. the ket' + eol +
         '    if final.exists():' + eol +
         '        tot = dur(final)' + eol +
         '        if tot:' + eol +
         '            sh_last = None' + eol +
         '            if shots_p.exists():' + eol +
         '                sh_last = json.loads(shots_p.read_text(encoding="utf-8-sig"))["shots"][-1]' + eol +
         '            # thuc te: the ket hien ro o giua shot cuoi (render fade dan den o 3 s cuoi)' + eol +
         '            t_card = (sh_last["start"] + 1.5) if sh_last else max(0, tot - 2)' + eol +
         '            png = WORK / f"_qc_endcard_{ep}.png"' + eol +
         '            r = run([FF, "-v", "error", "-ss", f"{t_card:.3f}", "-i", final,' + eol +
         '                     "-frames:v", "1", "-y", str(png)])' + eol +
         '            if png.exists() and png.stat().st_size > 5000:' + eol +
         '                br = bright_ratio(png)' + eol +
         '                if br > 0.0005:' + eol +
         '                    ok(f"G) the ket co chu tai {t_card:.1f}s ({br * 100:.2f}% pixel sang)")' + eol +
         '                else:' + eol +
         '                    bad(f"G) khung the ket tai {t_card:.1f}s khong co chu ({br * 100:.3f}% pixel sang)")' + eol +
         '                print(f"  (khung the ket: {png})")' + eol +
         '            else:' + eol +
         '                bad(f"G) khong trich duoc khung the ket tai {t_card:.1f}s")' + eol +
         '            # A11 #55: khung tai total-2 s — renderer mo dan shot cuoi 3 s cuoi => den' + eol +
         '            png2 = WORK / f"_qc_endcard_{ep}_cuoi.png"' + eol +
         '            run([FF, "-v", "error", "-ss", f"{max(0, tot - 2):.3f}", "-i", final,' + eol +
         '                 "-frames:v", "1", "-y", str(png2)])' + eol +
         '            b2 = bright_ratio(png2) if png2.exists() else 0.0' + eol +
         '            if b2 > 0.0005:' + eol +
         '                ok(f"G) khung tai total-2 s van co chu ({b2 * 100:.2f}% pixel sang)")' + eol +
         '            else:' + eol +
         '                warn("G) khung tai total-2 s den — outro cua renderer mo dan shot cuoi 3 s cuoi"' + eol +
         '                      " (dung chung T01-T03); the ket da kiem o giua shot cuoi")')
if raw.count(old_g) != 1:
    raise SystemExit("!! khong tim khoi gate G (%d lan)" % raw.count(old_g))
raw = raw.replace(old_g, new_g, 1)

QC.write_text(raw, encoding="utf-8", newline="")
print("OK gate G: do do sang that")
import subprocess
print("py_compile rc =", subprocess.run([sys.executable, "-m", "py_compile", str(QC)]).returncode)
