import json, sys
sys.stdout.reconfigure(encoding='utf-8')
script = json.load(open('.work/script_tap05.json', encoding='utf-8'))
sents = {s['id']: s['text'] for el in script if el.get('kind')=='LOI' for s in el.get('sentences',[])}
print("1.10#3:", sents.get('1.10#3'))
print("1.10#5:", sents.get('1.10#5'))
print("3.02#1:", sents.get('3.02#1'))
