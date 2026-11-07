# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md')
loi = [e for e in p if e['kind'] == 'LOI']

for e in loi:
    for s in e['sentences']:
        txt = s['text']
        # remove internal apostrophes like Sheriff's or Sheriff’s
        clean_txt = re.sub(r'([a-zA-Z])[’\']([a-zA-Z])', r'\1\2', txt)
        open_q = clean_txt.count('“') + clean_txt.count('‘')
        close_q = clean_txt.count('”') + clean_txt.count('’')
        if open_q != close_q:
            print(f"[{s['id']}] Mismatch: open={open_q}, close={close_q} in: {txt}")
