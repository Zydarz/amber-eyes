import json, sys, re
from pathlib import Path

# Load Vietnamese parsed script
with open('.work/script_tap02.json', 'r', encoding='utf-8') as f:
    vn_script = json.load(f)

# Load English parsed script to help cross-reference
with open('.work/temp_verify_en_t02.json', 'r', encoding='utf-8') as f:
    en_script = json.load(f)

print(f"Loaded VN: {len(vn_script)} elements, EN: {len(en_script)} elements")
