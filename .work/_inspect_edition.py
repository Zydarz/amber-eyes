import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import edition

t04 = edition.EPISODES.get('04', {})
print('Keys in EPISODES["04"]:', list(t04.keys()))
for k in t04:
    val = str(t04[k])
    if len(val) > 100:
        val = val[:100] + '...'
    print(f"  {k}: {val}")
