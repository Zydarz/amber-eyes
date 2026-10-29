import json, sys

script = json.load(open('.work/script_tap05.json', encoding='utf-8'))
all_sent_ids = set()
for el in script:
    if el.get('kind') == 'LOI':
        for s in el.get('sentences', []):
            all_sent_ids.add(s['id'])

sfx = json.load(open('.work/sfx_tap05.json', encoding='utf-8'))
for a, b, f, db in sfx['ambience']:
    assert a in all_sent_ids, f"ambience start {a} not in script"
    assert b in all_sent_ids, f"ambience end {b} not in script"

for a, b in sfx['music_drop']['ranges']:
    assert a in all_sent_ids, f"music_drop start {a} not in script"
    assert b in all_sent_ids, f"music_drop end {b} not in script"

print("All ambience and music_drop sentence IDs match script 100%!")
