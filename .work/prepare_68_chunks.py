import json
import re

tl = json.load(open('.work/timeline_s_t14.json', encoding='utf-8'))['items']
tl_map = {x['id']: x for x in tl}
jobs_77 = json.load(open('.work/bg_jobs_tap14.json', encoding='utf-8'))
assigned = set()
for j in jobs_77:
    s = j['sentences']
    if '–' in s:
        parts = s.split('–')
        elem = parts[0].split('#')[0]
        s_idx = int(parts[0].split('#')[1])
        e_idx = int(parts[1].replace('#',''))
        for i in range(s_idx, e_idx + 1):
            assigned.add(f'{elem}#{i}')
    else:
        assigned.add(s)

uncovered = [x for x in tl if x['id'] not in assigned]

chunks = []
cur_chunk = []
for item in uncovered:
    if cur_chunk and cur_chunk[0]['act'] != item['act']:
        chunks.append(cur_chunk)
        cur_chunk = [item]
    elif len(cur_chunk) >= 2:
        chunks.append(cur_chunk)
        cur_chunk = [item]
    elif cur_chunk and (cur_chunk[0]['end'] - cur_chunk[0]['start']) + (item['end'] - item['start']) > 24.0:
        chunks.append(cur_chunk)
        cur_chunk = [item]
    else:
        cur_chunk.append(item)
if cur_chunk:
    chunks.append(cur_chunk)

idx = 0
while len(chunks) < 68 and idx < len(chunks):
    if len(chunks[idx]) == 2:
        item1 = [chunks[idx][0]]
        item2 = [chunks[idx][1]]
        chunks.pop(idx)
        chunks.insert(idx, item2)
        chunks.insert(idx, item1)
        idx += 2
    else:
        idx += 1

STYLE_PREFIX = "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
MOOD_CORE = "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
NEGATIVE_SUFFIX = "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, full-bleed 16:9."

new_jobs = []

for i, ch in enumerate(chunks, 1):
    act = ch[0]['act']
    sent_ids = [x['id'] for x in ch]
    full_text = " ".join(x['text'] for x in ch)
    sent_str = ch[0]['id'] if len(ch) == 1 else f"{ch[0]['id']}–#{ch[-1]['id'].split('#')[1]}"
    
    # Generate meaningful unique code and contextual description based on text
    # We will build specific scenes tailored to Betty Broderick case
    new_jobs.append({
        "num": i,
        "act": act,
        "sentences": sent_str,
        "text": full_text
    })

print(f"Prepared {len(new_jobs)} chunks successfully.")
