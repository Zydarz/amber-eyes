"""Kiem chuc H13 tren FILE CUOI: trich khung dung luc cau dang doc, doi chieu chu tren hinh.

- Tu timeline lay moc thoi gian tung cau
- Trich khung tai (start + 0,6 s) tu mp4 cuoi
- In them: cau (loi noi), vai, va chu tren hinh theo bang shot
- Ghep contact sheet de SOI BANG MAT: chu tren hinh phai la cau dang doc

Usage: py -3 .work/_qc_sync_frames_t04.py --ep 04 [--file ...]
"""
import argparse
import json
import pathlib
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

ap = argparse.ArgumentParser()
ap.add_argument("--ep", default="04")
ap.add_argument("--file", default=None)
a = ap.parse_args()
ep = a.ep
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

final = pathlib.Path(a.file) if a.file else (
    ROOT / "02_SAN_XUAT" / f"Tap{ep}" / "xuat_ban" / f"Tap{ep}_master.mp4")
tl = json.loads((WORK / f"timeline_s_t{ep}.json").read_text(encoding="utf-8-sig"))
shots = json.loads((WORK / f"shots_t{ep}.json").read_text(encoding="utf-8-sig"))["shots"]
sent = {i["id"]: i for i in tl["items"]}
shot_by_sent = {}
for s in shots:
    for c in s.get("sentences", []):
        shot_by_sent.setdefault(c, s)

# chon mau: 2 cau dau moi hoi + 8 shot co scrim + 2 cau F0 dac biet + thai ket
acts = sorted({s["act"] for s in shots})
picks = []
for a_ in acts:
    s = next(x for x in shots if x["act"] == a_ and x.get("sentences"))
    picks.append(s["sentences"][0])
for sid in ("1-06", "1-10", "1-15", "1-17", "2-08", "4-03", "4-07", "4-13"):
    s = next((x for x in shots if x["id"] == sid), None)
    if s and s.get("sentences"):
        picks.append(s["sentences"][0])
for c in ("2.08#1", "3.02#2", "5.08#5", "5.10#3"):
    if c in sent:
        picks.append(c)

out = WORK / f"_qc_sync_t{ep}"
out.mkdir(parents=True, exist_ok=True)
for p in out.glob("*.png"):
    p.unlink()

tiles = []
for sid in picks:
    it = sent.get(sid)
    if not it:
        continue
    t = it["start"] + 0.6
    png = out / f"t_{sid.replace('.', '_').replace('#', '_')}.png"
    r = subprocess.run([str(FF), "-v", "error", "-ss", f"{t:.3f}", "-i", str(final),
                        "-frames:v", "1", "-y", str(png)], capture_output=True, text=True)
    if not png.exists() or png.stat().st_size < 5000:
        print(f"  [LOI] {sid} @ {t:.1f}s khong trich duoc khung")
        continue
    s = shot_by_sent.get(sid, {})
    segs = " / ".join(" ".join(e[1] for e in seg["elems"]) for seg in s.get("segments", []))
    print("\n--- %s | vai %s | t=%.1fs | shot %s ---" % (sid, it["role"], t, s.get("id")))
    print("   LOI   : %s" % it["text"][:150])
    print("   CHU   : %s" % (segs[:150] if segs else "(khong co chu)"))
    tiles.append((sid, t, png, it["text"][:70], segs[:70]))

cols, tw, th, pad, hh = 4, 470, 264, 10, 46
rows = (len(tiles) + cols - 1) // cols
W = cols * tw + (cols + 1) * pad
H = rows * (th + hh) + (rows + 1) * pad
sheet = Image.new("RGB", (W, H), (15, 17, 23))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("arial.ttf", 15)
except Exception:
    font = ImageFont.load_default()
for i, (sid, t, png, txt, seg) in enumerate(tiles):
    r, c = i // cols, i % cols
    x = pad + c * (tw + pad)
    y = pad + r * (th + hh + pad)
    d.text((x + 3, y + 2), f"{sid}  t={t:.1f}s", fill=(235, 205, 120), font=font)
    d.text((x + 3, y + 20), f"LOI: {txt}", fill=(170, 200, 235), font=font)
    with Image.open(png) as im:
        sheet.paste(im.resize((tw, th), Image.Resampling.LANCZOS), (x, y + hh))
outp = ROOT / "02_SAN_XUAT" / f"Tap{ep}" / f"qc_dongboi_t{ep}.png"
sheet.save(outp)
print("\n->", outp, sheet.size, "| %d khung" % len(tiles))
