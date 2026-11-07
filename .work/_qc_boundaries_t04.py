import json,sys,numpy as np,soundfile as sf
sys.stdout.reconfigure(encoding='utf-8')
tl,wav=sys.argv[1],sys.argv[2]
t=json.load(open(tl,encoding='utf-8'));it=t['items']
a,sr=sf.read(wav,dtype='float32')
H=0.05;w=int(H*sr);n=len(a)//w
db=20*np.log10(np.sqrt((a[:n*w].reshape(n,w)**2).mean(1))+1e-9)
def runs(t0,t1,q=-40,minlen=0.5):
    fr=db[int(t0/H):int(t1/H)]<q;out=[];s=None
    for i,v in enumerate(fr):
        if v and s is None:s=i
        if (not v or i==len(fr)-1) and s is not None:
            e=i+(1 if v and i==len(fr)-1 else 0)
            if (e-s)*H>=minlen: out.append((round(t0+s*H,2),round(t0+e*H,2)))
            s=None
    return out
print('interior silence >=0.5s (<-40dB):')
for x in it:
    r=runs(x['start']+0.1,x['end']-0.1)
    if r: print(' ',x['id'],round(x['start'],2),round(x['end'],2),r)
print('boundaries w/o dip < -33 dB within +-0.4s:')
for i in range(1,len(it)):
    b0,b1=it[i-1]['end'],it[i]['start']
    seg=db[int((b0-0.4)/H):int((b1+0.4)/H)+1]
    if len(seg) and seg.min()>-33: print(' ',it[i-1]['id'],it[i]['id'],round(b0,2),round(b1,2),round(float(seg.min()),1))
