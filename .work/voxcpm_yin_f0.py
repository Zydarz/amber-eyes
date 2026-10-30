import sys, numpy as np, soundfile as sf, glob, os
def yin(x, sr, fmin=60, fmax=400, win=0.04, hop=0.01, th=0.15):
    W=int(win*sr); H=int(hop*sr); tmin=int(sr/fmax); tmax=int(sr/fmin); out=[]
    for s in range(0,len(x)-W-tmax,H):
        f=x[s:s+W+tmax]
        if np.sqrt((f[:W]**2).mean())<0.02: continue
        d=np.array([np.sum((f[:W]-f[t:t+W])**2) for t in range(tmax+1)])
        c=np.cumsum(d[1:]); dn=np.ones_like(d); dn[1:]=d[1:]*np.arange(1,tmax+1)/np.maximum(c,1e-12)
        cand=np.where(dn[tmin:]<th)[0]
        if not len(cand): continue
        t=tmin+cand[0]
        while t+1<=tmax and dn[t+1]<dn[t]: t+=1
        if 1<=t<tmax:
            a,b,cc=dn[t-1],dn[t],dn[t+1]; den=a-2*b+cc; t=t+(0.5*(a-cc)/den if den else 0)
        out.append(sr/t)
    return np.array(out)
for p in sys.argv[1:]:
    x,sr=sf.read(p,dtype='float32')
    if x.ndim>1: x=x.mean(1)
    f=yin(x,sr); m=np.median(f)
    lo=np.mean(f<m/1.6)*100; hi=np.mean(f>m*1.6)*100
    p10,p90=np.percentile(f,[10,90])
    print(f"{os.path.basename(p)[:-4]:28} YIN med {m:6.1f}  p10 {p10:6.1f}  p90 {p90:6.1f}  voiced {len(f):4d}  octave-low {lo:4.1f}%  octave-high {hi:4.1f}%")
