"""SMOKE TEST parse_shots.py cho Tap04 — timeline gia lap.

Muc dich: bat loi parse (mau cau sai, moc thieu, cot sai) TRUOC khi render 1 gio,
khong phai doi lai audio xong moi phat hien. Script nay:
  1. sao luu timeline_s_t04.json / shots_t04.json hien tai
  2. tao timeline gia lap tu script_tap04.json (moi cau 3,5 s, lech 23,0 s)
  3. chay parse_shots.py
  4. kiem tra ket qua: so shot, phu cau, nen
  5. khoi phuc file goc

Chay:  py -3 .work/_smoke_parse_t04.py
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
TL = WORK / "timeline_s_t04.json"
SH = WORK / "shots_t04.json"
BK = WORK / "_cu" / "smoke_t04"

BK.mkdir(parents=True, exist_ok=True)
for p in (TL, SH):
    if p.exists():
        shutil.copy2(p, BK / p.name)
        print(f"sao luu {p.name}")
    else:
        print(f"khong co {p.name} (se duoc tao moi)")

script = json.loads((WORK / "script_tap04.json").read_text(encoding="utf-8-sig"))
items, markers, acts = [], [], []
t = 23.0
for el in script:
    if el.get("kind") == "LOI":
        for s in el.get("sentences", []):
            items.append({"id": s["id"], "element": el["id"], "act": el.get("act"),
                          "role": el.get("role"), "start": round(t, 3),
                          "end": round(t + 3.0, 3), "text": s["text"]})
            t += 3.5
    else:
        markers.append({"id": el["id"], "type": el.get("kind", "PAUSE"),
                        "start": round(t, 3), "end": round(t + 1.5, 3)})
        t += 1.5
markers.insert(0, {"type": "INTRO", "start": 0.0, "end": 22.41})
# moc ACT cho 5 hoi
for a in range(1, 6):
    acts.append({"type": "ACT", "act": a, "start": round(22.41 + a * 1.0, 3),
                 "end": round(23.91 + a * 1.0, 3)})
markers += acts
markers.sort(key=lambda m: m["start"])
tl = {"total": round(t + 8.0, 3), "intro": {"start": 0.0, "end": 22.41},
      "items": items, "markers": markers, "acts": acts}
TL.write_text(json.dumps(tl, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"timeline gia lap: {len(items)} cau, total {tl['total']} s")

env = os.environ.copy()
env["AE_EP"] = "04"
env["PYTHONIOENCODING"] = "utf-8"
r = subprocess.run([sys.executable, str(WORK / "parse_shots.py")], cwd=str(ROOT),
                   env=env, capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
print("--- parse_shots ---")
print(r.stdout.strip() or r.stderr.strip()[-1500:])

if r.returncode != 0:
    print("=> LOI PARSE")
else:
    sh = json.loads(SH.read_text(encoding="utf-8-sig"))["shots"]
    want = [s["id"] for el in script if el.get("kind") == "LOI"
            for s in el.get("sentences", [])]
    got = [c for s in sh for c in s.get("sentences", [])]
    print(f"=> {len(sh)} shot · phu cau {'OK' if got == want else 'SAI'} "
          f"({len(got)}/{len(want)}) · nen thieu: "
          f"{[s['id'] for s in sh if not s.get('bg')]}")
    print("=> mau mau:", sh[0]["id"], sh[0]["bg"], "| shot cuoi:", sh[-1]["id"], sh[-1]["bg"])

# khoi phuc
for p in (TL, SH):
    b = BK / p.name
    if b.exists():
        shutil.copy2(b, p)
        print(f"da khoi phuc {p.name}")
    elif p.exists():
        p.unlink()
        print(f"da xoa {p.name} (khong co ban goc)")
