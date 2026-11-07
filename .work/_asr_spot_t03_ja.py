import json,re,subprocess,numpy as np,soundfile as sf
from faster_whisper import WhisperModel
from pathlib import Path
W=Path('.work'); tl=json.load(open(W/'timeline_s_JA_t03.json',encoding='utf-8'))['items']
x,sr=sf.read(str(W/'audio_master_JA_t03.wav'),dtype='float32'); m=x.mean(axis=1)
import scipy.signal as ss
m16=ss.resample_poly(m,1,3).astype('float32')   # 48k->16k
model=WhisperModel('small',device='cpu',compute_type='int8',cpu_threads=4)
norm=lambda s:re.sub(r'[\s、。,.！？「」『』（）()\-―—・:：;；\'’“”"]','',s)
def bg(s): s=norm(s); return {s[i:i+2] for i in range(len(s)-1)}
res=[]
for t0 in np.linspace(60,1850,12):
    a=int(t0*16000); seg=m16[a:a+25*16000]
    segs,_=model.transcribe(seg,language='ja',vad_filter=False,beam_size=1)
    for s in segs:
        T=t0+s.start; g=bg(s.text)
        if len(g)<8: continue
        best=max(tl,key=lambda it:len(g&bg(it['text']))/max(1,len(g|bg(it['text']))))
        sc=len(g&bg(best['text']))/max(1,len(g|bg(best['text'])))
        if sc>=0.25: res.append((round(T,1),best['id'],round(best['start'],1),round(T-best['start'],1),round(sc,2)))
for r in res: print(r)
d=np.array([r[3] for r in res]); print('n',len(d),'median offset',np.median(d),'max|off|',abs(d).max(),'ids ordered',[r[1] for r in res]==sorted([r[1] for r in res],key=lambda i:[it['id'] for it in tl].index(i)))
