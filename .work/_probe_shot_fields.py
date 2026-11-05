import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sh = json.loads(open(".work/shots_t03.json", encoding="utf-8").read())
s = sh["shots"][2]
print("KEYS:", list(s.keys()))
for k, v in s.items():
    print(f"  {k} = {str(v)[:120]}")
