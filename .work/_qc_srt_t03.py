import json, re
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
tl = json.loads((W/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
srt = (Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\xuat_ban\Tap03.srt")).read_text(encoding="utf-8-sig")
blocks = [b for b in re.split(r"\r?\n\r?\n", srt.strip()) if b.strip()]
def ts(s):
    h,m,rest = s.split(":"); sec,ms = rest.split(",")
    return int(h)*3600+int(m)*60+int(sec)+int(ms)/1000
cues=[]
for b in blocks:
    ls=b.splitlines()
    a,bb = ls[1].split(" --> ")
    cues.append((ts(a), ts(bb), "\n".join(ls[2:])))
print(f"so cue: {len(cues)}")
print(f"cue dau: {cues[0][0]:.2f}s   cue cuoi het: {cues[-1][1]:.2f}s   timeline.total: {tl['total']}")
print(f"loi dau: {cues[0][0]:.2f} (can 22,8-23,5)   het: {cues[-1][1]:.2f} (loi cuoi {tl['items'][-1]['end']:.2f})")
# trung / lech
ov=[(i,cues[i][1],cues[i+1][0]) for i in range(len(cues)-1) if cues[i+1][0] < cues[i][1]-0.001]
gap=[(i+1, round(cues[i+1][0]-cues[i][1],2)) for i in range(len(cues)-1) if cues[i+1][0]-cues[i][1] > 0.35]
print(f"cue CHONG nhau: {len(ov)}  {ov[:5]}")
print(f"gap > 0,35s: {len(gap)}")
if gap:
    for i,g in gap[:12]: print(f"    sau cue {i}: {g}s")
long_=[(i+1, round(b-a,2)) for i,(a,b,_) in enumerate(cues) if b-a > 6.0]
print(f"cue > 6s (bi cat gio): {len(long_)} {long_[:12]}")
# kiem tra text cue == script (bỏ tag)
body = " ".join(i["text"] for i in tl["items"])
allcue = " ".join(c[2] for c in cues).replace("\n"," ")
allcue = re.sub(r"\[[^\]]*\]","",allcue)
norm = lambda s: re.sub(r"\s+"," ",s).strip()
miss = [i["id"] for i in tl["items"] if norm(i["text"])[:40] not in norm(allcue)]
print(f"cau khong co trong phu de: {len(miss)} {miss[:6]}")
