import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')

with open('.work/vn_sentences_dump.txt', 'w', encoding='utf-8') as out:
    for idx, el in enumerate(vn):
        kind = el.get('kind')
        role = el.get('role')
        el_id = el.get('id')
        sents = el.get('sentences', [])
        out.write(f"Element {idx+1} [ID: {el_id}, Kind: {kind}, Role: {role}, Sentences: {len(sents)}]\n")
        if kind != 'LOI':
            out.write(f"  Non-dialogue: {el.get('desc', el.get('sec'))}\n")
        else:
            for s in sents:
                out.write(f"  {s['id']}: {s['text']}\n")
        out.write("\n")
print(f"Total elements: {len(vn)}, Total sentences: {sum(len(e.get('sentences', [])) for e in vn)}")
