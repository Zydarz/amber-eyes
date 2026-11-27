import sys,subprocess,re,unicodedata,json
sys.path.insert(0,'.work'); sys.stdout.reconfigure(encoding='utf-8')
import _timeline_from_srt_t25 as T
from faster_whisper import WhisperModel
lang=sys.argv[1]; ids=sys.argv[2:]
tl,_,_=T.build(lang); it={i['id']:i for i in tl['items']}
mst=T.B/T.CFG[lang][2]
m=WhisperModel('base',device='cpu',compute_type='int8')
def norm(s): return re.sub(r'[\W_]+',' ',unicodedata.normalize('NFKC',s).lower()).split()
for sid in ids:
    s=it[sid]['start']; a=max(0,s-8)
    subprocess.run([str(T.FF),'-y','-v','error','-ss',str(a),'-t','22','-i',str(mst),'-ac','1','-ar','16000','.work/_spot.wav'],check=True)
    import wave,numpy as np
    w=wave.open('.work/_spot.wav'); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype('float32')/32768; w.close()
    segs,_=m.transcribe(x,language={'vi':'vi','en':'en','ja':'ja'}[lang],word_timestamps=True,vad_filter=False)
    segs=list(segs)
    print('==',sid,'SRT start',round(s,2),'|',it[sid]['text'][:70])
    for sg in segs: print('   %.1f-%.1f %s'%(a+sg.start,a+sg.end,sg.text.strip()[:80]))
    ws=[w for sg in segs for w in sg.words]
    tgt=norm(it[sid]['text'])[:3] if lang!='ja' else None
    found=None
    for k in range(len(ws)-2):
        got=norm(' '.join(x.word for x in ws[k:k+3]))
        if lang=='ja':
            if unicodedata.normalize('NFKC',it[sid]['text'])[:4] in unicodedata.normalize('NFKC',''.join(x.word for x in ws[k:k+4])): found=ws[k].start; break
        elif got[:2]==tgt[:2]: found=ws[k].start; break
    print(sid,'SRT start',s,'| ASR start', None if found is None else round(a+found,2),'| lech', None if found is None else round(s-(a+found),2))
