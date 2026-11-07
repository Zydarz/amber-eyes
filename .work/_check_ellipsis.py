# -*- coding: utf-8 -*-
"""Check ellipsis '...' across all scripts of Tap 15 and Tap 18."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

for ep in ['Tap15', 'Tap18']:
    for path in [
        f'01_KICH_BAN/{ep}/kichban_{ep.lower()}_23102026.md',
        f'01_KICH_BAN/{ep}_EN/kichban_{ep.lower()}_EN.md',
        f'01_KICH_BAN/{ep}_JA/kichban_{ep.lower()}_JA.md',
        f'01_KICH_BAN/{ep}_KO/kichban_{ep.lower()}_KO.md',
    ]:
        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
        matches = [(i+1, l.strip()) for i, l in enumerate(lines) if '...' in l or '…' in l]
        print(f"{path}: {len(matches)} chỗ có '...' hoặc '…'")
        for idx, text in matches:
            print(f"  Line {idx}: {text[:90]}...")
