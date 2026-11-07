import json,re,unicodedata,sys
sys.stdout.reconfigure(encoding='utf-8')
W='D:/TEST/Gax/amber-eyes/.work/'
script=json.load(open(W+'script_tap04_JA.json',encoding='utf-8'))
rc=json.load(open(W+'speech_full_recognized_ja_t04_small.json',encoding='utf-8'))
def kata2hira(s): return ''.join(chr(ord(c)-0x60) if 'ァ'<=c<='ヶ' else c for c in s)
def nz(t):
    t=kata2hira(unicodedata.normalize('NFKC',t).lower())
    return [c for c in t if re.match(r'\w',c)]
S=[]
for e in script:
    if e['kind']=='LOI':
        role=e['role']
        if role=='N': role='N1' if e['id']=='1.07' else 'N2'
        for s in e['sentences']: S.append(dict(id=s['id'],element=e['id'],act=e['act'],role=role,text=s['text']))
st=[]
for i,s in enumerate(S):
    for c in nz(s['text']): st.append((c,i))
aw=[]
for r in rc:
    for w in r['words']:
        cs=nz(w['word'])
        if not cs: continue
        d=(w['end']-w['start'])/len(cs)
        for k,c in enumerate(cs): aw.append((c,w['start']+k*d,w['start']+(k+1)*d))
N,M=len(st),len(aw);print('script chars',N,'asr chars',M)
GAP=-0.5;BAND=int(sys.argv[1]) if len(sys.argv)>1 else 600
def rng(i):
    c=int(i*M/N);return max(0,c-BAND),min(M,c+BAND)
NEG=-1e9
rows=[None]*(N+1)
lo,hi=rng(0);rows[0]={j:(j*GAP,'L') for j in range(lo,hi+1)}
for i in range(1,N+1):
    lo,hi=rng(i);new={};p=rows[i-1];a=st[i-1][0]
    for j in range(lo,hi+1):
        best,k=NEG,None
        if j>0 and (j-1) in p: best,k=p[j-1][0]+(2.0 if a==aw[j-1][0] else -0.7),'D'
        if j in p and p[j][0]+GAP>best: best,k=p[j][0]+GAP,'U'
        if (j-1) in new and new[j-1][0]+GAP>best: best,k=new[j-1][0]+GAP,'L'
        if k: new[j]=(best,k)
    rows[i]=new
    rows[i-1]=None if i>1 and False else rows[i-1]
i,j=N,M
if j not in rows[N]: j=max(rows[N],key=lambda x:rows[N][x][0])
match={}
bt=rows
# backtrack needs all rows kept
while i>0:
    k=rows[i][j][1]
    if k=='D':
        if st[i-1][0]==aw[j-1][0]: match[i-1]=j-1
        i-=1;j-=1
    elif k=='U': i-=1
    else: j-=1
per={}
for ti,aj in match.items(): per.setdefault(st[ti][1],[]).append(aw[aj])
cnt={}
for c,si in st: cnt[si]=cnt.get(si,0)+1
items=[];nom=[]
for si,s in enumerate(S):
    m=per.get(si,[]);n=cnt[si]
    if len(m)<max(3,0.25*n): nom.append((s['id'],len(m),n));items.append(dict(s,start=None,end=None,cov=len(m)/n));continue
    m=sorted(m,key=lambda x:x[1])
    items.append(dict(s,start=m[0][1],end=m[-1][2],cov=len(m)/n))
import statistics
print('mean cov',round(statistics.mean(x['cov'] for x in items),3),'weak',len(nom),nom[:25])
json.dump(items,open(W+'_t04_ja_aligned_raw.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
