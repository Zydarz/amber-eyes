import json, sys
sys.stdout.reconfigure(encoding='utf-8')

def check(path):
    d = json.load(open(path, encoding='utf-8'))
    loi = [e for e in d if e.get('kind') == 'LOI']
    total_s = sum(len(e.get('sentences', [])) for e in loi)
    print(f"File: {path}")
    print(f"Elements: {len(d)}, Turns: {len(loi)}, Sentences: {total_s}")
    from collections import defaultdict
    acts = defaultdict(int)
    for e in loi:
        acts[e['act']] += len(e.get('sentences', []))
    for a in sorted(acts):
        print(f"  Act {a}: {acts[a]} sentences")
    for e in d:
        desc = e.get('desc', '') or str(e.get('sec', ''))
        sc = len(e.get('sentences', []))
        print(f"  {e['id']} | {e['kind']:4} | {e.get('role', ' '):2} | s={sc:2} | {desc[:40]}")

if __name__ == '__main__':
    check(sys.argv[1])
