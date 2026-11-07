import json,re,unicodedata,difflib,sys
sys.stdout.reconfigure(encoding='utf-8')
W='D:/TEST/Gax/amber-eyes/.work/'
script=json.load(open(W+'script_tap04_EN.json',encoding='utf-8'))
rc=json.load(open(W+'speech_full_recognized_en_t04_small.json',encoding='utf-8'))
def nz(t): return re.sub(r'[^\w\s]',' ',unicodedata.normalize('NFC',t).lower()).split()
S=[]  # sentences
for e in script:
    if e['kind']=='LOI':
        role=e['role']
        if role=='N': role='N1' if e['id']=='1.07' else 'N2'
        for s in e['sentences']: S.append(dict(id=s['id'],element=e['id'],act=e['act'],role=role,text=s['text']))
st=[];
for i,s in enumerate(S):
    for t in nz(s['text']): st.append((t,i))
aw=[]
for r in rc:
    for w in r['words']:
        for t in nz(w['word']): aw.append((t,w['start'],w['end']))
N,M=len(st),len(aw); print('script tokens',N,'asr tokens',M)
def sc(a,b):
    if a==b: return 2.0
    r=difflib.SequenceMatcher(None,a,b).ratio()
    return 1.0 if r>=0.7 else (-0.6 if r<0.4 else 0.0)
NEG=-1e9; GAP=-0.5; BAND=260
import array
prev={}; ptr=[None]*(N+1)
rows=[None]*(N+1)
def rng(i):
    c=int(i*M/N); return max(0,c-BAND),min(M,c+BAND)
lo,hi=rng(0); cur={j:(j*GAP,'L') for j in range(lo,hi+1)}; rows[0]=cur
for i in range(1,N+1):
    lo,hi=rng(i); new={}
    for j in range(lo,hi+1):
        best,k=NEG,None
        p=rows[i-1]
        if j-1 in p and j>0: v=p[j-1][0]+sc(st[i-1][0],aw[j-1][0]); best,k=v,'D'
        if j in p and p[j][0]+GAP>best: best,k=p[j][0]+GAP,'U'
        if j-1 in new and new[j-1][0]+GAP>best: best,k=new[j-1][0]+GAP,'L'
        if k: new[j]=(best,k)
    rows[i]=new
i,j=N,M
if j not in rows[N]: j=max(rows[N],key=lambda x:rows[N][x][0])
match={}
while i>0:
    k=rows[i][j][1]
    if k=='D':
        if st[i-1][0]==aw[j-1][0] or sc(st[i-1][0],aw[j-1][0])>=1.0: match[i-1]=j-1
        i-=1;j-=1
    elif k=='U': i-=1
    else: j-=1
per={}
for ti,aj in match.items(): per.setdefault(st[ti][1],[]).append(aw[aj])
items=[];nomatch=[]
for si,s in enumerate(S):
    m=per.get(si)
    ntok=len([1 for t in st if t[1]==si])
    if not m or len(m)<max(2,0.35*ntok): nomatch.append((s['id'],len(m or []),ntok)); items.append(dict(s,start=None,end=None,cov=len(m or [])/ntok)); continue
    items.append(dict(s,start=min(x[1] for x in m),end=max(x[2] for x in m),cov=len(m)/ntok))
print('weak/no match',len(nomatch),nomatch[:20])
json.dump(items,open(W+'_t04_en_aligned_raw.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
