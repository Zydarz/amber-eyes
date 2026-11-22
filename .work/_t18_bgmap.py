import json,re,collections
from pathlib import Path
W=Path(__file__).parent
def expand(s):
    out=[]
    for part in s.split(';'):
        part=part.strip()
        m=re.match(r'(\d\.\d+)#(\d+)(?:–#(\d+))?',part)
        a,b=int(m[2]),int(m[3] or m[2]); out+= [f"{m[1]}#{k}" for k in range(a,b+1)]
    return out
def build():
    jobs=json.load(open(W/'bg_jobs_tap18.json',encoding='utf-8'))
    new=json.load(open(W/'bg_jobs_tap18_new61.json',encoding='utf-8'))
    split=json.load(open(W/'t18_split_61_raw.json',encoding='utf-8'))
    tl=json.load(open(W/'timeline_s_t18.json',encoding='utf-8')); ids=[i['id'] for i in tl['items']]
    bg={}
    for j in jobs:
        for s in expand(j['sentences']): bg[s]=j['name']
    for n,sp in zip(new,split):
        for s in sp['sids']: bg[s]=n['name']
    return ids,bg,jobs,new
if __name__=='__main__':
    ids,bg,jobs,new=build()
    print(len(bg),[i for i in ids if i not in bg],[s for s in bg if s not in ids])
    # contiguous chunks
    ch=[];prev=None
    for i in ids:
        if bg.get(i)!=prev: ch.append([bg.get(i),[]]);prev=bg.get(i)
        ch[-1][1].append(i)
    print(len(ch),'chunks'); c=collections.Counter(b for b,_ in ch); print('bg with >1 chunk',[(k,v) for k,v in c.items() if v>1])
    used={b for b,_ in ch}; print('unused',[j['name'] for j in jobs+new if j['name'] not in used])
