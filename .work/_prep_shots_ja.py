import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

s_ja = json.load(open(".work/script_tap02_JA.json", encoding="utf-8"))
S_ja = {}
for e in s_ja:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S_ja[s["id"]] = s["text"]

def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

vn_lines = open("02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md", encoding="utf-8").readlines()
en_table = json.load(open(".work/shots_text_tap02_EN.json", encoding="utf-8"))

shots = []
for l in vn_lines:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if m:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        sid = m.group(1)
        ids = sents(c[1])
        ctx_ja = " ".join(S_ja.get(x, "") for x in ids)
        en_entry = en_table.get(sid, ["—", [], None])
        shots.append({
            "sid": sid,
            "cau": c[1],
            "vai": c[2],
            "mau": c[3],
            "nen": c[4],
            "chu_vn": c[5],
            "beat_vn": c[6],
            "chu_en": en_entry[0],
            "phrases_en": en_entry[1],
            "ctx_ja": ctx_ja
        })

print(f"Total shots parsed: {len(shots)}")
print("Sample shot 1-01:", shots[1])
