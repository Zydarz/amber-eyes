import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
W = ROOT / ".work"

script_ja = json.loads((W / "script_tap02_JA.json").read_text(encoding="utf-8"))
S_ja = {}
for e in script_ja:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S_ja[s["id"]] = s["text"]

def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

vn_lines = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_lines) if i > i0 and l.startswith("**Tổng:"))

en_table = json.loads((W / "shots_text_tap02_EN.json").read_text(encoding="utf-8"))

shots = []
for l in vn_lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    sid = m.group(1)
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    ids = sents(c[1])
    ctx_ja = " ".join(S_ja.get(x, "") for x in ids)
    en_entry = en_table.get(sid, ["—", [], None])
    vn_ph = re.findall(r'ở "([^"]+)"', c[6])
    shots.append({
        "sid": sid,
        "ids": ids,
        "mau": c[3],
        "chu_vn": c[5],
        "beat_vn": c[6],
        "vn_ph": vn_ph,
        "chu_en": en_entry[0],
        "ph_en": en_entry[1],
        "ctx_ja": ctx_ja
    })

print(f"Total shots parsed: {len(shots)}")
with open(W / "_shots_analysis.json", "w", encoding="utf-8") as f:
    json.dump(shots, f, ensure_ascii=False, indent=2)
print("Saved _shots_analysis.json")
