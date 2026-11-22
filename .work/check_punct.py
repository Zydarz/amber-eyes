# -*- coding: utf-8 -*-
import json

for lang, fn in [('VN', '.work/out_tap46_vn.json'), ('EN', '.work/out_tap46_en.json'), ('JA', '.work/out_tap46_ja.json')]:
    items = json.load(open(fn, encoding='utf-8'))
    no_punct = 0
    valid_ends = ('.', '!', '?', '”', '」', '。', '！', '？', '"')
    for item in items:
        if 'sentences' in item:
            for s in item['sentences']:
                t = s['text']
                if not t.endswith(valid_ends):
                    no_punct += 1
                    print(f"No end punct [{lang}] {s['id']}: {t}")
    print(f"{lang}: total without standard terminal punctuation = {no_punct}")
