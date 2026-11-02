#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC so sanh JA Tap02 voi ban VN/EN: line endings, phan bo do dai shot, so cue phu de."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def srt_info(p):
    if not Path(p).exists():
        return None
    b = Path(p).read_bytes()
    crlf = b.count(b"\r\n")
    lf = b.count(b"\n")
    txt = b.decode("utf-8-sig", errors="replace").replace("\r\n", "\n")
    blocks = [x for x in txt.strip().split("\n\n") if x.strip()]

    def sec(ts):
        h, m, s = ts.split(":")
        s, ms = s.split(",")
        return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

    cues = []
    bad = 0
    for blk in blocks:
        ls = blk.splitlines()
        if len(ls) < 3 or " --> " not in ls[1]:
            bad += 1
            continue
        a, z = ls[1].split(" --> ")
        cues.append((sec(a), sec(z), " ".join(ls[2:])))
    return {"crlf": crlf, "lf": lf, "n": len(cues), "bad": bad, "cues": cues}


print("=== A. LINE ENDINGS + SO CUE ===")
files = {
    "JA Tap02 (MOI)": ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA.srt",
    "JA Tap02 (CU)": W / "_cu/ja_t02_20261102/Tap02_JA.srt",
    "VN Tap02": ROOT / "02_SAN_XUAT/Tap02/xuat_ban/Tap02.srt",
    "EN Tap02": ROOT / "02_SAN_XUAT/Tap02_EN/xuat_ban/Tap02_EN.srt",
}
info = {}
for k, p in files.items():
    i = srt_info(p)
    if not i:
        print(f"  {k:<20} KHONG CO")
        continue
    info[k] = i
    end = i["cues"][-1][1] if i["cues"] else 0
    print(f"  {k:<20} cue={i['n']:<5} CRLF={i['crlf']:<5} LF={i['lf']:<5} "
          f"block_lo={i['bad']}  het={end:.2f}s")

print("\n=== B. PHAN BO DO DAI SHOT (JA moi vs VN goc) ===")
for tag, path in [("JA t02", W / "shots_JA_t02.json"), ("VN t02", W / "shots_t02.json")]:
    if not path.exists():
        continue
    sh = json.loads(path.read_text(encoding="utf-8-sig"))
    s = sh["shots"]
    d = sorted(round(x["end"] - x["start"], 1) for x in s)
    over15 = sum(1 for v in d if v > 15)
    under3 = sum(1 for v in d if v < 3)
    print(f"  {tag}: {len(s)} shot · total {sh['total']}s · nganh {d[0]} · trung "
          f"{d[len(d)//2]} · dai {d[-1]} · >15s={over15} · <3s={under3}")

print("\n=== C. SHOT JA: SO SANH VOI VN THEO ID ===")
ja = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
vn = json.loads((W / "shots_t02.json").read_text(encoding="utf-8-sig"))["shots"]
vmap = {s["id"]: s for s in vn}
diff_bg = []
diff_tpl = []
for s in ja:
    v = vmap.get(s["id"])
    if not v:
        print("  JA co shot khong co o VN:", s["id"])
        continue
    if s["bg"] != v["bg"]:
        diff_bg.append((s["id"], v["bg"], s["bg"]))
    if s["template"] != v["template"]:
        diff_tpl.append((s["id"], v["template"], s["template"]))
print(f"  nen khac = {len(diff_bg)} {diff_bg[:6]}")
print(f"  mau khac = {len(diff_tpl)} {diff_tpl[:6]}")

print("\n=== D. CHI CHOT: PHAI LAY TU CAU DANG DOC (V3/H6) ===")
tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it for it in tl["items"]}
bad_num = []
for s in ja:
    if not s["sentences"]:
        continue
    txt = " ".join(sent[i]["text"] for i in s["sentences"])
    for kind, val in [(k, v) for seg in s["segments"] for k, v in seg["elems"]]:
        if kind == "bold":
            # so chuoi chu in dam phai xuat hien trong cau (bo dau nhan)
            core = val.replace(" ", "")
            if core and core not in txt.replace(" ", "").replace("　", ""):
                bad_num.append((s["id"], val[:40]))
print(f"  chu in dam khong tim thay trong cau = {len(bad_num)}")
for x in bad_num[:12]:
    print("     ", x)
