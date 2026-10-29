# One-off: VN shot table -> EN shot table. Keeps Câu/Vai/Mẫu/Nền/Nhân vật and the Vietnamese
# beat wording (the renderer keys on it); swaps the Chữ cell and the quoted beat phrases to English.
import json, re, sys
from pathlib import Path
ROOT=Path(r"D:\TEST\Gax\Audi"); W=ROOT/".work"
vn=(ROOT/"02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md").read_text(encoding="utf-8").splitlines()
en=json.loads((W/"shots_text_EN.json").read_text(encoding="utf-8"))
S={s['id']:s['text'] for e in json.load(open(W/"script_EN.json",encoding="utf-8")) if e['kind']=='LOI' for s in e['sentences']}
def sents(cell):
    out=[]
    for ma,a,b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?",cell): out+=[f"{ma}#{k}" for k in range(int(a),int(b or a)+1)]
    return out
i0=next(i for i,l in enumerate(vn) if l.startswith("## 6. DANH SÁCH SHOT"))
i1=next(i for i,l in enumerate(vn) if i>i0 and l.startswith("**Tổng:"))
out=[]; errs=[]; done=set()
for l in vn[i0:i1+1]:
    m=re.match(r"\|\s*([1-5]-\d+)\s*\|",l)
    if not m: out.append(l); continue
    sid=m[1]; c=l.strip().strip('|').split('|')
    if sid not in en:
        if c[5].strip()!='—': errs.append(f"{sid}: thiếu bản EN")
        out.append(l); continue
    chu,beat=en[sid]; done.add(sid)
    if '"' not in beat: beat=re.sub(r'ở "','at "',c[6])   # no English phrase (SFX-only row): keep the VN cue
    vn_ph=re.findall(r'ở "([^"]+)"',c[6]); en_ph=re.findall(r'at "([^"]+)"',beat)
    if len(vn_ph)!=len(en_ph): errs.append(f"{sid}: {len(vn_ph)} cụm VN ≠ {len(en_ph)} cụm EN")
    had_forged='giả mạo' in c[6]
    it=iter(en_ph); c[6]=re.sub(r'ở "([^"]+)"',lambda _: 'ở "'+next(it,'??')+'"',c[6])
    if had_forged and 'giả mạo' not in c[6]: c[6]=c[6].rstrip()+' (dấu giả mạo) '   # renderer keys the FORGED stamp on this word
    c[5]=' '+chu+' '
    txt=' '.join(S.get(x,'') for x in sents(c[1]))
    for p in en_ph:
        if txt and p.lower() not in txt.lower(): errs.append(f"{sid}: cụm \"{p}\" không có trong câu {sents(c[1])}")
    out.append('|'+'|'.join(c)+'|')
errs+= [f"{k}: có bản EN nhưng không có dòng VN" for k in en if k not in done]
print("\n".join(errs) or "OK", "· rows", len(done))
json.dump(out,open(W/"_plan_en_table.json","w",encoding="utf-8"),ensure_ascii=False)
