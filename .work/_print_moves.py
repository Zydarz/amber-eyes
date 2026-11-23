import json

shuffle_data = json.load(open('.work/_proposed_shuffle.json', encoding='utf-8'))
for item in shuffle_data:
    old_ep = item['old_ep']
    new_ep = item['new_ep']
    if old_ep != new_ep:
        print(f"Old Tap {old_ep:02d} -> New Tap {new_ep:02d}: {item['title'][:30]}")
