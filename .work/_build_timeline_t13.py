import json
import re

sc_vi = json.load(open('.work/script_tap13.json', encoding='utf-8'))
sc_en = json.load(open('.work/script_tap13_EN.json', encoding='utf-8'))
sc_ja = json.load(open('.work/script_tap13_JA.json', encoding='utf-8'))

INTRO = 22.41
FIRST_VOICE = 23.0
GAP_SENT = 0.35
GAP_ELEM = 0.70
GAP_ACT = 2.0
OUTRO = 11.10

# Speech rates (chars/s for VI, words/s for EN, chars/s for JA)
RATE_VI = 15.20
RATE_EN = 2.40  # words/s
RATE_JA = 5.98

def build_timeline(lang):
    if lang == 'vi':
        sc = sc_vi
    elif lang == 'en':
        sc = sc_en
    else:
        sc = sc_ja
        
    items = []
    markers = [{'type': 'INTRO', 'start': 0.0, 'end': INTRO}]
    acts = {}
    
    t = FIRST_VOICE
    current_act = 1
    act_start = t
    
    for e in sc:
        eid = e['id']
        act_num = e['act']
        
        # Check act transition
        if act_num > current_act:
            acts[str(current_act)] = [round(act_start, 3), round(t, 3)]
            markers.append({'type': 'ACT', 'act': act_num, 'start': round(t, 3), 'end': round(t + GAP_ACT, 3)})
            t += GAP_ACT
            current_act = act_num
            act_start = t
            
        kind = e.get('kind')
        if kind in ('BGM', 'SFX', 'NGHI'):
            if kind == 'NGHI':
                markers.append({'type': 'NGHI', 'id': eid, 'start': round(t, 3), 'end': round(t + 1.5, 3), 'desc': e.get('desc', '')})
                t += 1.5
            else:
                markers.append({'type': kind, 'id': eid, 'at': round(t, 3), 'desc': e.get('desc', '')})
        elif kind == 'LOI':
            sents = e.get('sentences', [])
            role = e.get('role')
            if role == 'N':
                # Map N to N1 or N2 based on element
                if eid == '1.07':
                    role = 'N1'
                elif eid == '4.06':
                    role = 'N2'
                else:
                    role = 'N1'
            for i, s in enumerate(sents):
                sid = s['id']
                txt = s['text']
                if lang == 'en':
                    n_words = len(txt.split())
                    dur = max(1.2, n_words / RATE_EN)
                elif lang == 'ja':
                    n_chars = len(txt)
                    dur = max(1.2, n_chars / RATE_JA)
                else: # vi
                    n_chars = len(txt)
                    dur = max(1.2, n_chars / RATE_VI)
                    
                dur = round(dur, 3)
                it_start = round(t, 3)
                it_end = round(t + dur, 3)
                items.append({
                    'id': sid,
                    'element': eid,
                    'act': act_num,
                    'role': role,
                    'start': it_start,
                    'end': it_end,
                    'text': txt
                })
                t = it_end
                if i < len(sents) - 1:
                    t += GAP_SENT
                else:
                    t += GAP_ELEM
                    
    # Finish last act
    acts[str(current_act)] = [round(act_start, 3), round(t - GAP_ELEM, 3)]
    # adjust markers and total
    last_item_end = items[-1]['end']
    total = round(last_item_end + OUTRO, 2)
    
    res = {
        'total': total,
        'intro': INTRO,
        'items': items,
        'markers': markers,
        'acts': acts,
        '_master': f'estimated_{lang}'
    }
    return res

for lang in ('vi', 'en', 'ja'):
    res = build_timeline(lang)
    if lang == 'vi':
        out_name = '.work/timeline_s_t13.json'
    elif lang == 'en':
        out_name = '.work/timeline_s_EN_t13.json'
    else:
        out_name = '.work/timeline_s_JA_t13.json'
    with open(out_name, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print(f'Saved {out_name}: items={len(res["items"])}, total={res["total"]}')
