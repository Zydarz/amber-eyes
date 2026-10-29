import json, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data = json.load(open('.work/script_tap04.json', encoding='utf-8'))
sents_map = {s['id']: s['text'] for e in data if e['kind'] == 'LOI' for s in e['sentences']}

ntk_lines = open('02_SAN_XUAT/Tap04/xuat_ban/nguon_tham_khao.md', encoding='utf-8').readlines()
print("--- CHECKING NGUON_THAM_KHAO SENTENCE IDS ---")
for line in ntk_lines:
    m = re.match(r'\|\s*`([^`]+)`\s*\|\s*([^|]+)\s*\|', line)
    if m:
        cid, snippet = m[1], m[2].strip()
        actual = sents_map.get(cid)
        if actual:
            print(f"[OK] {cid}: found -> {actual[:60]}...")
        else:
            print(f"[MISSING] {cid} NOT FOUND! Snippet: {snippet}")
            # Try to locate which sentence has this snippet
            for sid, text in sents_map.items():
                if any(w in text for w in snippet.split()[:4]):
                    print(f"   --> Found in {sid}: {text[:60]}...")
                    break
