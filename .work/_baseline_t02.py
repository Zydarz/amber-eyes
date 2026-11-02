import json, re
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
def audit(path, name, tlpath):
    tl = json.loads(Path(tlpath).read_text(encoding="utf-8-sig"))
    sh = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    sent = {i["id"]: i for i in tl["items"]}
    def nums(s): return set(re.findall(r"\d+(?:[.,]\d+)?", s))
    viol = []
    for s in sh["shots"]:
        if not s["sentences"]: continue
        txt = " ".join(sent[x]["text"] for x in s["sentences"])
        card = " ".join(e[1] for seg in s["segments"] for e in seg["elems"])
        for n in nums(card):
            if n not in txt:
                # so voi chu so tho (bo so 0 dan)
                digits = n.lstrip("0") or "0"
                if digits not in txt and n not in txt:
                    viol.append((s["id"], n))
    durs = [s["end"]-s["start"] for s in sh["shots"]]
    print(f"--- {name} ---")
    print(f"  shots={len(sh['shots'])} total={tl['total']}  trung binh={sum(durs)/len(durs):.1f}s  max={max(durs):.1f}  >15s={sum(1 for d in durs if d>15)}  <3s={sum(1 for d in durs if d<3)}")
    print(f"  so tren hinh khong co trong cau: {len(viol)}  {viol[:12]}")
audit(W/"shots_t02.json", "TAP 02 (DA XUAT)", W/"timeline_s_t02.json")
audit(W/"shots_t03.json", "TAP 03 (MOI)", W/"timeline_s_t03.json")
