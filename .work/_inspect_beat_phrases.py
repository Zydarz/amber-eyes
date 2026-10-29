import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
shots = json.load(open(".work/_shots_analysis.json", encoding="utf-8"))
for s in shots:
    if s["vn_ph"]:
        print(f"{s['sid']}: vn_ph={s['vn_ph']} | ph_en={s['ph_en']} | ctx_ja={s['ctx_ja']}")
