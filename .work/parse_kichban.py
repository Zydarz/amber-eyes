# Parse a script (Vietnamese, English or Korean edition) -> elements (turns/cues) and sentences.
# usage: py -3 .work/parse_kichban.py <kichban.md> <out.json>
import re, json, sys

ROLES={'HOST':'H','NGƯỜI BÌNH THƯỜNG':'N','ĐIỀU TRA VIÊN':'D','CHUYÊN GIA TÂM LÝ':'C',
       'ORDINARY PERSON':'N','INVESTIGATOR':'D','PSYCHOLOGIST':'C',
       'ĐẶC VỤ FBI':'D','CẢNH SÁT ĐỊA PHƯƠNG':'N',
       # Korean edition: 막 = act · 호스트/수사관/심리학자/일반인 + 2 vai đặc biệt
       '호스트':'H','수사관':'D','심리학자':'C','일반인':'N',
       '연방수사국':'D','지역경찰':'N',
       # Japanese edition: 第N幕 = act · ホスト/捜査官/心理学者/一般人 + 2 vai đặc biệt
       'ホスト':'H','捜査官':'D','心理学者':'C','一般人':'N',
       'FBI特別捜査官':'D','地方警察':'N'}

# câu tiếng Nhật: mỗi 。/！/？/… kết thúc một câu (kể cả dấu đóng nháy đi kèm)
JA_END = re.compile(r'[。！？…][」』”"）)\]]*')


def ja_split(para):
    """Tách câu tiếng Nhật: mỗi dấu kết câu (kèm dấu đóng nháy) là một câu."""
    parts, last = [], 0
    for m in JA_END.finditer(para):
        parts.append(para[last:m.end()])
        last = m.end()
    tail = para[last:].strip()
    if tail:
        parts.append(tail)
    return parts


def vn_quotes(paras):
    """Bản tiếng Việt: '…' = trích dẫn nguyên văn -> “…”.

    Trích dẫn có thể TRÀI NHIỀU DÒNG (kịch bản viết 1 câu 1 dòng, dấu nháy mở ở
    câu đầu và đóng ở câu cuối). Regex theo dòng cũ bỏ sót dấu nháy => phải
    theo dõi trạng thái mở/đóng xuyên suốt element.
    """
    out, opened = [], False
    for p in paras:
        buf = []
        for i, ch in enumerate(p):
            if ch == "'":
                prev = p[i - 1] if i > 0 else ""
                nxt = p[i + 1] if i + 1 < len(p) else ""
                if prev.isalpha() and nxt.isalpha():
                    buf.append(ch)          # dấu nháy kép của tiếng Anh
                else:
                    buf.append('”' if opened else '“')
                    opened = not opened
            else:
                buf.append(ch)
        out.append(''.join(buf))
    return out

# câu VN/EN/Hàn: . ? ! … (kể cả .”) rồi tới chữ hoa / chữ Hán / chữ Hangeul
LATIN_SPLIT = r'(?:(?<=[.?!…])|(?<=[.?!…]”))\s+(?=[A-ZÀ-ỸĐ가-힣“(])'

# Vai CHỈ có trong bản tiếng Việt -> nhận diện bản VN (bản EN/Hàn/Nhật dùng
# dấu nháy cong ‘…’ cho trích dẫn, còn dấu ' là dấu nháy kép của tiếng Anh).
VN_ROLE_HDR = re.compile(
    r'^\*\*(?:NGƯỜI BÌNH THƯỜNG|ĐIỀU TRA VIÊN|CHUYÊN GIA TÂM LÝ|ĐẶC VỤ FBI|CẢNH SÁT ĐỊA PHƠNG)\*\*', re.M)


def parse_lines(src):
    """Script text (list of lines) -> list of elements."""
    act=0; els=[]; cur=None; n=0
    vn = bool(VN_ROLE_HDR.search('\n'.join(src)))
    def new(kind,**kw):
        nonlocal n; n+=1; e=dict(id=f"{act}.{n:02d}",act=act,kind=kind,**kw); els.append(e); return e
    for line in src:
        s=line.strip()
        m=re.match(r'^## (?:HỒI|ACT|막|第)\s*(\d)',s)
        if m: act=int(m[1]); n=0; cur=None; continue
        if act==0 or not s or s=='---': continue
        m=re.match(r'^\*\*('+'|'.join(ROLES)+r')\*\*\s*(?:\*\((.*?)\)\*)?\s*:',s)
        if m: cur=dict(role=ROLES[m[1]],direction=m[2] or ''); continue
        m=re.match(r'^\*\*\[(SFX|BGM)\]:\*\*\s*(.*)',s)
        if m: new(m[1],desc=m[2]); continue
        m=re.match(r'^\*\*\[(?:Nghỉ ([\d.]+) giây|Pause ([\d.]+) seconds?|정지 ([\d.]+)초|休止 ([\d.]+)秒)(.*?)\]\*\*',s)
        if m: new('NGHI',sec=float(m[1] or m[2] or m[3] or m[4]),desc=m[5].strip(' –-')); continue
        if cur is None: continue
        t=re.sub(r'^\*\s+','',s); t=re.sub(r'^\d+\.\s+','',t)
        t=t.replace('**','').replace('*','')
        t=t.strip().strip('"“”').strip()
        t=re.sub(r"(?<![A-Za-z0-9])'([^']+)'(?![A-Za-z0-9])",r'“\1”',t)                  # trích dẫn trên 1 dòng
        t=re.sub(r"‘(.*?)’(?![A-Za-z])",r'“\1”',t)        # English/Korean edition: ‘…’ (’ inside a word = apostrophe)
        if not t: continue
        if els and els[-1]['kind']=='LOI' and els[-1]['role']==cur['role'] and els[-1].get('_open'):
            els[-1]['paras'].append(t)
        else:
            e=new('LOI',role=cur['role'],direction=cur['direction'],paras=[t],_open=True)
        # a cue between paragraphs closes the turn element
    for i,e in enumerate(els):
        if e['kind']!='LOI' and i>0 and els[i-1]['kind']=='LOI': els[i-1]['_open']=False
    # re-merge handled above only while open; now split sentences
    for e in els:
        e.pop('_open',None)
        if e['kind']=='LOI':
            if vn and any("'" in p for p in e['paras']):
                # Bản VN: trích dẫn TRẢI NHIỀU DÒNG ('…' mở ở câu đầu, đóng ở câu
                # cuối) => regex theo dòng không khớp, dấu nháy ' bị sót lại.
                # Đóng mở xuyên element cho các dấu ' còn sót.
                e['paras']=vn_quotes(e['paras'])
            # câu cắt ở . ? ! … (kể cả .”) khi theo sau là chữ hoa / chữ Hán / chữ Hangeul
            # bản Nhật: cắt ở 。 ！ ？ … (kể cả dấu đóng nháy)
            parts=[]
            for para in e['paras']:
                if any(ch in para for ch in '。！？'):
                    parts.extend(ja_split(para))
                else:
                    parts.extend(re.split(LATIN_SPLIT,para))
            e['text']=' '.join(e['paras']); e.pop('paras')
            e['sentences']=[dict(id=f"{e['id']}#{k}",text=p,words=len(p.split())) for k,p in enumerate(parts,1)]
    return els


def parse_file(src_path, out_path=None):
    """Script file -> elements; optionally also write the json next to it."""
    els=parse_lines(open(src_path,encoding='utf-8').read().splitlines())
    if out_path:
        json.dump(els,open(out_path,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    return els


if __name__=="__main__":
    parse_file(sys.argv[1], sys.argv[2])
