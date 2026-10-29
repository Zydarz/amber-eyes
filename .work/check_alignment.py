import json
import os
import sys

with open('.work/script_tap06.json', 'r', encoding='utf-8') as f:
    script_data = json.load(f)

with open('.work/timeline_s_t06.json', 'r', encoding='utf-8') as f:
    timeline_data = json.load(f)

print(f"script_data type: {type(script_data)}")
if isinstance(script_data, dict):
    print(f"Keys count: {len(script_data)}, sample keys: {list(script_data.keys())[:5]}")
    sample_key = list(script_data.keys())[0]
    print(f"Sample value for {sample_key}: {script_data[sample_key]}")

print(f"timeline_data type: {type(timeline_data)}")
if isinstance(timeline_data, dict):
    print(f"Timeline keys: {list(timeline_data.keys())[:10]}")
    if 'cues' in timeline_data:
        print(f"Timeline cues count: {len(timeline_data['cues'])}")
        print(f"Sample cue: {list(timeline_data['cues'].items())[:2]}")
