import json, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import edition

with open('.work/script_tap02.json', 'r', encoding='utf-8') as f:
    script = json.load(f)

print('Total elements:', len(script))
loi = [x for x in script if x.get('kind') == 'LOI']
print('Total LOI elements:', len(loi))
sentences = [s for x in loi for s in x.get('sentences', [])]
print('Total sentences:', len(sentences))

ep = edition.EPISODES['02']
print('act1_cue in script:', any(x['id'] == ep['act1_cue'] for x in script))
print('silence_cue in script:', any(x['id'] == ep['silence_cue'] for x in script))
for cue in ep.get('click_cues', ()):
    print(f'click_cue {cue} in script:', any(x['id'] == cue for x in script))

for k, v in ep.get('n_element', {}).items():
    match = [x for x in script if x['id'] == k]
    role = match[0].get('role') if match else None
    print(f'n_element {k}={v}: found={bool(match)}, role={role}')

sum_keys = ep.get('summary', ())
for sk in sum_keys:
    el_id, s_idx = sk.split('#')
    s_idx = int(s_idx)
    match = [x for x in loi if x['id'] == el_id]
    has_sent = match and len(match[0]['sentences']) >= s_idx
    sent_text = match[0]['sentences'][s_idx-1]['text'] if has_sent else 'MISSING'
    print(f'summary {sk}: found={has_sent} -> "{sent_text[:50]}..."')

need_keys = ep.get('need', [])
missing_need = []
for nk in need_keys:
    el_id, s_idx = nk.split('#')
    s_idx = int(s_idx)
    match = [x for x in loi if x['id'] == el_id]
    if not (match and len(match[0]['sentences']) >= s_idx):
        missing_need.append(nk)

print(f'Need keys check: total={len(need_keys)}, missing={len(missing_need)}')
if missing_need:
    print('Missing need keys:', missing_need)
