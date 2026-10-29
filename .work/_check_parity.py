import json, sys
sys.stdout.reconfigure(encoding='utf-8')
data_vn = json.load(open('.work/script_tap05.json', encoding='utf-8'))
print("VN elements:", len(data_vn))
