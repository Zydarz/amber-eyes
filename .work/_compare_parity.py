import json, sys
sys.stdout.reconfigure(encoding='utf-8')

def compare(path_a, path_b, name_a="A", name_b="B"):
    a = json.load(open(path_a, encoding='utf-8'))
    b = json.load(open(path_b, encoding='utf-8'))
    if len(a) != len(b):
        print(f"FAILED: Element count mismatch: {name_a}={len(a)} vs {name_b}={len(b)}")
        return False
    diffs = []
    for i, (ea, eb) in enumerate(zip(a, b)):
        eid = ea['id']
        akind, bkind = ea['kind'], eb['kind']
        arole, brole = ea.get('role'), eb.get('role')
        asc, bsc = len(ea.get('sentences', [])), len(eb.get('sentences', []))
        if eid != eb['id']:
            diffs.append(f"Element {i} ID mismatch: {eid} vs {eb['id']}")
        if akind != bkind:
            diffs.append(f"{eid} Kind mismatch: {name_a}={akind} vs {name_b}={bkind}")
        if arole != brole:
            diffs.append(f"{eid} Role mismatch: {name_a}={arole} vs {name_b}={brole}")
        if asc != bsc:
            diffs.append(f"{eid} Sentences mismatch: {name_a}={asc} vs {name_b}={bsc}")
    if diffs:
        print(f"FAILED: {len(diffs)} differences between {name_a} and {name_b}:")
        for d in diffs:
            print(f"  - {d}")
        return False
    total_s = sum(len(e.get('sentences', [])) for e in a if e.get('kind') == 'LOI')
    print(f"SUCCESS: 100% PARITY between {name_a} and {name_b}! ({len(a)} elements, {total_s} sentences)")
    return True

if __name__ == '__main__':
    compare(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
