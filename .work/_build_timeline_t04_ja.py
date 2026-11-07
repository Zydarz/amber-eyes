import json,sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
WORK=Path("D:/TEST/Gax/amber-eyes/.work")
script=json.loads((WORK/"script_tap04_JA.json").read_text(encoding="utf-8"))
raw=json.loads((WORK/"_t04_ja_aligned_raw.json").read_text(encoding="utf-8"))
# noi suy cau thieu khop giua 2 cau lan can
for i,r in enumerate(raw):
    if r["start"] is None:
        a=max((x for x in raw[:i] if x["end"] is not None),key=lambda x:x["end"],default=None)
        b=next((x for x in raw[i+1:] if x["start"] is not None),None)
        n=1;j=i+1
        while j<len(raw) and raw[j]["start"] is None: n+=1;j+=1
        k=i
        while k>0 and raw[k-1]["start"] is None: k-=1
        slot=(b["start"]-a["end"])/(n+ (i-k))
        # chia deu khoang trong theo thu tu
        idx=i-k
        s0=a["end"]+0.12+idx*slot; e0=s0+slot-0.12
        r["start"]=round(s0,3); r["end"]=round(e0,3); r["interp"]=True
items_tl=[]
prev_end=22.41
for r in raw:
    st,en=r["start"],r["end"]
    if r["id"]=="1.03#1": st=max(23.0,st)
    if st<prev_end+0.12: st=prev_end+0.12
    if en<=st+0.5: en=st+1.2
    items_tl.append({"id":r["id"],"element":r["element"],"act":r["act"],"role":r["role"],"start":round(st,3),"end":round(en,3),"text":r["text"]})
    prev_end=en

# ---- tinh chinh bien cau theo nang luong that cua master (16 kHz mono)
import numpy as np, soundfile as sf
_a,_sr=sf.read(str(WORK/"speech_full_ja_t04_16k.wav"),dtype="float32")
_H=0.05; _w=int(_H*_sr); _n=len(_a)//_w
_db=20*np.log10(np.sqrt((_a[:_n*_w].reshape(_n,_w)**2).mean(axis=1))+1e-9)
TH=-27.0
def _loud(t): return _db[min(_n-1,max(0,int(t/_H)))]>TH
for i,it in enumerate(items_tl):
    lo=items_tl[i-1]["end"] if i else 22.41
    hi=items_tl[i+1]["start"] if i+1<len(items_tl) else 1946.7
    # mo rong ve phia truoc / sau khi con tieng noi, khong vuot qua cau ke
    t=it["start"]
    while t-_H>lo+0.03 and _loud(t-_H): t-=_H
    it["start"]=round(t,3)
    t=it["end"]
    while t+_H<hi-0.03 and _loud(t+_H): t+=_H
    it["end"]=round(t,3)

# ---- khoang trong > 1.0 s ma phan lon la tieng noi: tieng noi thuoc ve cau co do phu ASR thap hon
covs={r["id"]:r["cov"] for r in raw}
def _quiet_runs(t0,t1,minlen=0.2,q=-30.0):
    runs=[];st=None;t=t0
    while t<t1:
        qq=_db[min(_n-1,int(t/_H))]<q
        if qq and st is None: st=t
        if not qq and st is not None:
            if t-st>=minlen: runs.append((st,t))
            st=None
        t+=_H
    if st is not None and t1-st>=minlen: runs.append((st,t1))
    return runs
for i in range(1,len(items_tl)):
    a,b=items_tl[i-1],items_tl[i]
    g=b["start"]-a["end"]
    if g<=1.0: continue
    nl=sum(1 for t in np.arange(a["end"],b["start"],_H) if _loud(t))/(g/_H)
    if nl<0.5: continue
    runs=_quiet_runs(a["end"],b["start"])
    if not runs: a["end"]=round(b["start"]-0.15,3); continue
    if covs[a["id"]]<=covs[b["id"]]:
        a["end"]=round(runs[-1][0],3)          # tieng noi con lai la duoi cua cau truoc
    else:
        b["start"]=round(runs[0][1],3)         # tieng noi la phan dau cua cau sau

# cau ke nhau: giu khoang >= 0.1 s (neu cham thi chia doi)
for i in range(1,len(items_tl)):
    a,b=items_tl[i-1],items_tl[i]
    if b["start"]<a["end"]+0.1:
        m=(a["end"]+b["start"])/2; a["end"]=round(m-0.05,3); b["start"]=round(m+0.05,3)


# ---- ghi de co do that (ASR bo sot; do nang luong master 16 kHz, cua so 0,25 s, sang -13..-23 dB, im < -30 dB)
OVERRIDE={}
for _it in items_tl:
    if _it["id"] in OVERRIDE: _it["start"],_it["end"]=OVERRIDE[_it["id"]]
# ---- cat bien theo khoang lang o RIA cau (<-40 dB, >=0.4 s): ASR tieng Nhat tho -> bien cau co the nam trong khoang lang
def _edge_trim(it):
    s,e=it["start"],it["end"]
    i0,i1=int(s/_H),int(e/_H)
    seg=_db[i0:i1]<-40.0
    # dau cau
    k=0
    while k<len(seg) and seg[k]: k+=1
    # cho phep lech 0.2 s: tim run lang dau tien bat dau trong 0.2 s dau
    j=0
    while j<len(seg) and not seg[j] and j*_H<0.2: j+=1
    if j<len(seg) and seg[j] and j*_H<0.2:
        r=j
        while r<len(seg) and seg[r]: r+=1
        if (r-j)*_H>=0.4 and r<len(seg): it["start"]=round((i0+r)*_H-0.03,3)
    # cuoi cau
    seg=_db[int(it["start"]/_H):i1]<-40.0
    j=len(seg)-1
    while j>=0 and not seg[j] and (len(seg)-1-j)*_H<0.2: j-=1
    if j>=0 and seg[j] and (len(seg)-1-j)*_H<0.2:
        r=j
        while r>=0 and seg[r]: r-=1
        if (j-r)*_H>=0.4 and r>=0: it["end"]=round((int(it["start"]/_H)+r+1)*_H+0.03,3)
for _it in items_tl:
    if _it["id"] not in OVERRIDE: _edge_trim(_it)
# ---- chinh mot dau (None = giu): ASR bo sot vai tu dau cau sau quang ngat (do nang luong 16 kHz)
ADJ={"4.02#2":(1215.95,None),   # tieng noi bat dau 1215.98 (chu Latin trong cau lam DP lech)
     "5.06#3":(1798.19,None),   # "この法律は、" 1798.2-1799.0
     "5.10#4":(1933.85,None)}   # loi bat dau 1933.85
for _it in items_tl:
    if _it["id"] in ADJ:
        _s,_e=ADJ[_it["id"]]
        if _s is not None: _it["start"]=_s
        if _e is not None: _it["end"]=_e
for _i in range(1,len(items_tl)):
    assert items_tl[_i]["start"]>=items_tl[_i-1]["end"]-1e-6,(items_tl[_i-1]["id"],items_tl[_i]["id"])

# Reconstruct acts boundaries
acts = {}
for it in items_tl:
    act = it["act"]
    if act not in acts:
        acts[act] = [it["start"], it["end"]]
    else:
        acts[act][1] = it["end"]

# Markers construction
markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]

elem_span = {}
for it in items_tl:
    eid = it["element"]
    if eid not in elem_span:
        elem_span[eid] = [it["start"], it["end"]]
    else:
        elem_span[eid][1] = it["end"]

cur_act = None
for idx, e in enumerate(script):
    eid = e["id"]
    act = e["act"]
    
    if cur_act is not None and act != cur_act:
        prev_act_end = acts[cur_act][1]
        act_st = acts[act][0]
        m_en = round(act_st - 0.20, 3)
        m_st = round(max(prev_act_end + 0.10, m_en - 2.0), 3)
        assert m_st < m_en, ("ACT marker dao nguoc", act, m_st, m_en)
        markers.append({"type": "ACT", "act": act, "start": m_st, "end": m_en})
    cur_act = act
    
    if e.get("kind") == "NGHI":
        sec = e.get("sec", 1.5)
        prev_elem_id = script[idx - 1]["id"] if idx > 0 else None
        next_elem_id = script[idx + 1]["id"] if idx < len(script) - 1 else None
        
        p_end = elem_span.get(prev_elem_id, [23.0, 23.0])[1] if prev_elem_id in elem_span else 23.0
        n_st = elem_span.get(next_elem_id, [p_end + sec, p_end + sec])[0] if next_elem_id in elem_span else p_end + sec
        
        mst = round(p_end + 0.05, 3)
        men = round(min(n_st - 0.15, mst + sec), 3)
        if men <= mst + 0.2:
            men = round(mst + 1.2, 3)
        markers.append({
            "type": "NGHI",
            "id": eid,
            "start": mst,
            "end": men,
            "desc": e.get("desc", "")
        })
    elif e.get("kind") in ("SFX", "BGM"):
        next_elem_id = script[idx + 1]["id"] if idx < len(script) - 1 else None
        at_time = elem_span.get(next_elem_id, [23.0, 23.0])[0] if next_elem_id in elem_span else 23.0
        markers.append({
            "type": e.get("kind"),
            "id": eid,
            "at": round(at_time, 3),
            "desc": e.get("desc", "")
        })

# Total duration of Tap04_master.mp3 is 1519.08
TOTAL_DUR = 1946.670

timeline_out = {
    "total": round(TOTAL_DUR, 3),
    "intro": 22.41,
    "items": items_tl,
    "markers": markers,
    "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}
}

out_tl = WORK / "timeline_s_JA_t04.json"
out_tl.write_text(json.dumps(timeline_out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved new timeline to {out_tl}")
print(f"Total sentences: {len(items_tl)}, Total markers: {len(markers)}")
print(f"First sentence start: {items_tl[0]['start']}s, Last sentence end: {items_tl[-1]['end']}s")
print(f"Acts boundaries: {timeline_out['acts']}")
