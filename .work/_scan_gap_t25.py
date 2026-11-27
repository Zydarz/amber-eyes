import sys,subprocess,wave,numpy as np,json
sys.path.insert(0,'.work'); sys.stdout.reconfigure(encoding='utf-8')
import _timeline_from_srt_t25 as T
for lang in ('vi','en','ja'):
    tl,_,_=T.build(lang); mst=T.B/T.CFG[lang][2]
    subprocess.run([str(T.FF),'-y','-v','error','-i',str(mst),'-ac','1','-ar','16000','.work/_scan.wav'],check=True)
    w=wave.open('.work/_scan.wav'); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype('float32')/32768; w.close()
    n=int(len(x)/16000); db=np.array([20*np.log10(np.sqrt((x[i*16000:(i+1)*16000]**2).mean())+1e-9) for i in range(n)])
    # ngưỡng: giọng thường ~ -20..-17 dB/1s; nhạc nền ~ -36..-42
    low=db<-28; runs=[];i=0
    while i<n:
        if low[i]:
            j=i
            while j<n and low[j]: j+=1
            runs.append((i,j)); i=j
        else: i+=1
    items=tl['items']; intro=22.41
    bad=[]
    for a,b in runs:
        if b-a>=4 and a>intro and b<tl['total']-12:
            # có phải ranh giới hồi / nghỉ giữa câu?
            near=[it['id'] for it in items if it['start']<=b and it['end']>=a]
            bad.append((a,b,b-a,near[:3]))
    print(lang,'median dB',round(float(np.median(db)),1),'| runs thấp>=4s ngoài intro/outro:',len(bad))
    for r in bad: print('   %ds-%ds (%ds) câu %s'%r)
