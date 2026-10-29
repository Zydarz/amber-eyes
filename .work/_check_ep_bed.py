import sys
sys.path.insert(0, '.work')
import edition
for ep_id in ['01', '02', '03', '04', '05']:
    cfg = edition.EPISODES.get(ep_id, {})
    print(f"EP {ep_id}: bed={cfg.get('bed')}")
