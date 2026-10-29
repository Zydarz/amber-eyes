import json, sys
sys.stdout.reconfigure(encoding='utf-8')

jobs = json.load(open('.work/bg_jobs_tap05.json', encoding='utf-8'))
for j in jobs:
    if j['name'] in ('t5_btk_signature_letter', 't5_handwritten_note_floppy', 't5_newspaper_classified_494', 't5_metadata_screen', 't5_church_website_search', 't5_kerri_rawson_tears'):
        print(f"--- {j['name']} ---")
        print(j['prompt'])
