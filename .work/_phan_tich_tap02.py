# -*- coding: utf-8 -*-
"""F: Phan tich TAP 02 — viet lai chuoi bien doi trong .py + phan bo giong/cam xuc/nhip."""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_EP"] = "02"
WORK = Path(r"D:\TEST\Gax\Audi\.work")
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

man = json.loads((WORK / "tts_manifest_t02.json").read_text(encoding="utf-8"))
print(f"=== TAP 02 · {len(man)} cau · edition.EPN={ED.EPN} · ED.EN={ED.EN} · ED.SUF={ED.SUF} ===")
print(f"CAST dang dung: {ED.CAST}")
print(f"VN_CAST_BASE  : {ED.VN_CAST_BASE}")
print(f"EP['cast']     : {ED.EP.get('cast')}   (None = dung bo A mac dinh)")
print(f"EP['acting']  : {ED.EP.get('acting')}")
print(f"TTS_FIX       : {len(ED.TTS_FIX)} muc")
for k, v in ED.TTS_FIX.items():
    print(f"   {k}: {v!r}")
print()

# ---- phan bo ----
per_role = defaultdict(lambda: {"n": 0, "voice": Counter(), "emo": Counter(),
                                "spd": [], "pitch": Counter(), "pause": 0, "fix": 0})
for it in man:
    r = per_role[it["role"]]
    r["n"] += 1
    r["voice"][it["voice"]] += 1
    r["emo"][it["emotion"]] += 1
    r["spd"].append(it["speed"])
    r["pitch"][it.get("pitch", 0)] += 1
    if re.search(r"<#[\d.]+#>", it["text"]):
        r["pause"] += 1
    if it["id"] in ED.TTS_FIX:
        r["fix"] += 1

ROLE = {"H": "Host (Cu)", "D": "Dieu tra vien (Soi)", "C": "Chuyen gia (Cao)", "N1": "N1 (Cuu)", "N2": "N2 (Meo)"}
print("--- PHAN BO THEO VAI ---")
for role in ["H", "D", "C", "N1", "N2"]:
    if role not in per_role:
        continue
    r = per_role[role]
    print(f"{ROLE[role]:22s} {r['n']:4d} cau ({r['n']/len(man)*100:4.1f}%)  voice={dict(r['voice'])}")
    print(f"{'':22s}  cam xuc: {dict(r['emo'])}")
    print(f"{'':22s}  speed : min {min(r['spd'])} / max {max(r['spd'])} / trung viet {sorted(r['spd'])[len(r['spd'])//2]}")
    print(f"{'':22s}  pitch : {dict(r['pitch'])}   thau ngat <#x#>: {r['pause']}   TTS_FIX: {r['fix']}")
print()

# ---- lời đọc vs câu gốc (G6) ----
def norm(t):
    t = re.sub(r"<#[\d.]+#>", " ", t)
    t = re.sub(r"[^\w\s]", " ", t.lower(), flags=re.UNICODE)
    return re.sub(r"\s+", " ", t).strip()

diff = []
for it in man:
    a, b = norm(it["text"]), norm(it["display"])
    if a != b:
        diff.append((it["id"], it["role"], it["text"], it["display"]))
print(f"--- G6: lời đọc riêng khac cau goc: {len(diff)}/{len(man)} ---")
for sid, role, t, d in diff[:12]:
    print(f"   {sid:9s} [{role}] doc: {t}")
    print(f"   {'':9s}      goc: {d}")
print()

# ---- chỗ khác nhau có phải do doi so -> chu? ----
NUM = re.compile(r"\d")
num_only = 0
other = []
for sid, role, t, d in diff:
    # so lai: thay moi chu so trong 'display' bang tuong duong 'text'
    if NUM.search(d):
        num_only += 1
    else:
        other.append((sid, role, t, d))
print(f"   trong {len(diff)} cau khac: {num_only} co chu so o cau goc (doi so->chu), {len(other)} khong co")
for sid, role, t, d in other[:10]:
    print(f"   KHONG PHAI SO->CHU  {sid} [{role}]")
    print(f"      doc: {t}")
    print(f"      goc: {d}")
print()

# ---- co bao gioi trong cau nao? ----
print("--- THAU NGAT <#x#> TRONG BAN TIENG VIET ---")
hits = [(it["id"], it["role"], it["text"]) for it in man if re.search(r"<#[\d.]+#>", it["text"])]
print(f"   so cau co thau ngat: {len(hits)}")
for h in hits[:8]:
    print("   ", h[0], h[1], h[2][:110])
print()

# ---- dau ... trong lời đọc (G1) ----
dots = [it["id"] for it in man if "..." in it["text"]]
print(f"--- G1: cau nao con dau '...' trong loi doc: {len(dots)} ---")
print("   ", dots[:15])
print()

# ---- ampe / dau ngoai trong lời đọc ----
paren = [(it["id"], it["text"]) for it in man if re.search(r"\([^)]*\)", it["text"])]
print(f"--- G7: con chu thich trong ngoac trong loi doc: {len(paren)} ---")
for p in paren[:8]:
    print("   ", p[0], p[1][:120])
