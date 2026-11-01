import sys
sys.path.append('.work')
from parse_kichban import parse_file

vn = parse_file('01_KICH_BAN/Tap04/kichban_tap04_23102026.md')
en = parse_file('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md')

with open('.work/sfx_bgm_diff.txt', 'w', encoding='utf-8') as out:
    for i, (v, e) in enumerate(zip(vn, en)):
        vk = v.get('kind')
        ek = e.get('kind')
        if vk != 'LOI' or ek != 'LOI':
            out.write(f"Elem {i+1} [{v.get('id')} / {e.get('id')}] (Kind: VN={vk}, EN={ek}):\n")
            out.write(f"  VN: {v.get('desc', v.get('sec'))}\n")
            out.write(f"  EN: {e.get('desc', e.get('sec'))}\n")
print("Done")
