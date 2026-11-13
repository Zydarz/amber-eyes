import sys
sys.path.insert(0, '.work')
import parse_kichban as PK

vn = PK.parse_file('01_KICH_BAN/Tap11/kichban_tap11_23102026.md')
ja = PK.parse_file('01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md')

print(f"VN: {len(vn)} elements, JA: {len(ja)} elements")
for i in range(max(len(vn), len(ja))):
    v = vn[i] if i < len(vn) else {}
    j = ja[i] if i < len(ja) else {}
    vid, jid = v.get('id'), j.get('id')
    vs, js = len(v.get('sentences', [])), len(j.get('sentences', []))
    if vid != jid or vs != js:
        print(f"Turn [{vid}]: VN has {vs} sents, JA has {js} sents (diff={js - vs})")
