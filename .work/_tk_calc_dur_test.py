# -*- coding: utf-8 -*-
"""Tối ưu độ dài và cấu trúc 5 clip TikTok Tập 04 trên cả 3 ngôn ngữ VI, EN, JA.
Đảm bảo tất cả 5 clip đều nằm nghiêm ngặt trong 60 - 90s (cổng QC: 45 - 95s).
"""
import json, re
from collections import defaultdict
import sys
sys.path.insert(0, '.work')
try:
    from vi_cer import vi_numbers
except Exception:
    def vi_numbers(x): return x

def get_rates(fn, is_ja=False):
    d = json.load(open(f'.work/{fn}', encoding='utf-8'))
    dur = defaultdict(float)
    units = defaultdict(int)
    for it in d['items']:
        txt = re.sub(r'<#[\d.]+#>', ' ', it['text'])
        n = len(txt.replace(' ', '').strip()) if is_ja else len([w for w in txt.split() if w.strip()])
        dur[it['role']] += it['end'] - it['start']
        units[it['role']] += n
    return {r: dur[r]/units[r] for r in dur}

R_VI = get_rates('timeline_s_t04.json', False)
R_EN = get_rates('timeline_s_EN_t04.json', False)
R_JA = get_rates('timeline_s_JA_t04.json', True)

vi_map = {it['id']: it['text'] for it in json.load(open('.work/timeline_s_t04.json', encoding='utf-8'))['items']}
en_map = {it['id']: it['text'] for it in json.load(open('.work/timeline_s_EN_t04.json', encoding='utf-8'))['items']}
ja_map = {it['id']: it['text'] for it in json.load(open('.work/timeline_s_JA_t04.json', encoding='utf-8'))['items']}

clips = [
    {
        'id': 'TK1',
        'hook': ('Nhập lệnh lấy thuốc độc. Rồi nhấn hủy chỉ sau một giây.',
                 'Ordered lethal drugs. Then hit cancel one second later.',
                 '劇薬を出庫し、わずか1秒後に取り消しボタンを押す。'),
        'cta': ('Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.',
                'Episode four of Amber Eyes. Watch the full documentary via the bio link.',
                'Amber Eyes第4話。プロフィールリンクから完全版ドキュメンタリーをご覧ください。'),
        'items': [
            ('H', 'hook', 0.5),
            ('D', '2.06#1', 0.6),
            ('D', '2.06#3', 0.6),
            ('D', '2.06#4', 0.6),
            ('D', '2.06#5', 0.7),
            ('D', '2.06#14', 0.7),
            ('C', '2.08#5', 0.7),
            ('C', '2.11#7', 0.7),
            ('H', 'cta', 0.0)
        ]
    },
    {
        'id': 'TK2',
        'hook': ('Người y tá hiền lành nhất bệnh viện. Lại là kẻ sát nhân tàn khốc nhất.',
                 'The gentlest nurse on the ward. And America’s most prolific killer.',
                 '病院で最も温厚だった看護師。その正体は、史上最悪の殺人鬼だった。'),
        'cta': ('Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.',
                'Episode four of Amber Eyes. Watch the full documentary via the bio link.',
                'Amber Eyes第4話。プロフィールリンクから完全版ドキュメンタリーをご覧ください。'),
        'items': [
            ('H', 'hook', 0.5),
            ('H', '1.03#1', 0.5),
            ('H', '1.03#2', 0.6),
            ('H', '1.03#4', 0.6),
            ('H', '1.03#6', 0.6),
            ('H', '1.05#2', 0.6),
            ('N1', '1.07#1', 0.6),
            ('N1', '1.07#2', 0.6),
            ('N1', '1.07#5', 0.7),
            ('C', '2.11#1', 0.7),
            ('H', 'cta', 0.0)
        ]
    },
    {
        'id': 'TK3',
        'hook': ('Chiếc micro dưới áo khoác mùa đông. Và cuộc hẹn sinh tử tại quán ăn.',
                 'A hidden wire beneath her winter coat. A deadly dinner with her best friend.',
                 'セーターの下の盗聴マイク。親友との命懸けのダイナー密会。'),
        'cta': ('Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.',
                'Episode four of Amber Eyes. Watch the full documentary via the bio link.',
                'Amber Eyes第4話。プロフィールリンクから完全版ドキュメンタリーをご覧ください。'),
        'items': [
            ('H', 'hook', 0.5),
            ('H', '4.02#7', 0.6),
            ('D', '4.04#1', 0.6),
            ('D', '4.04#6', 0.6),
            ('N2', '4.06#6', 0.7),
            ('H', '4.08#3', 0.6),
            ('H', '4.08#6', 0.7),
            ('H', '4.08#8', 0.7),
            ('D', '4.12#5', 0.7),
            ('H', 'cta', 0.0)
        ]
    },
    {
        'id': 'TK4',
        'hook': ('Chín bệnh viện biết hắn có vấn đề. Nhưng tất cả đều chọn im lặng.',
                 'Nine hospitals suspected him. Every single one chose silence.',
                 '9つの病院が彼を疑っていた。しかし全員が沈黙を選んだ。'),
        'cta': ('Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.',
                'Episode four of Amber Eyes. Watch the full documentary via the bio link.',
                'Amber Eyes第4話。プロフィールリンクから完全版ドキュメンタリーをご覧ください。'),
        'items': [
            ('H', 'hook', 0.5),
            ('D', '1.14#2', 0.6),
            ('D', '1.14#3', 0.6),
            ('D', '1.14#4', 0.6),
            ('D', '1.14#5', 0.7),
            ('D', '1.14#7', 0.7),
            ('C', '5.05#6', 0.7),
            ('D', '5.06#2', 0.7),
            ('H', 'cta', 0.0)
        ]
    },
    {
        'id': 'TK5',
        'hook': ('Bài học sinh tồn lớn nhất: Đừng bao giờ im lặng trước cái ác.',
                 'The greatest survival lesson: Never stay silent in the face of wrong.',
                 '最大の生存の教訓：決して不正の前に沈黙してはならない。'),
        'cta': ('Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.',
                'Episode four of Amber Eyes. Watch the full documentary via the bio link.',
                'Amber Eyes第4話。プロフィールリンクから完全版ドキュメンタリーをご覧ください。'),
        'items': [
            ('H', 'hook', 0.5),
            ('H', '1.16#4', 0.6),
            ('H', '1.16#5', 0.7),
            ('D', '5.06#2', 0.6),
            ('D', '5.06#5', 0.6),
            ('H', '5.08#4', 0.7),
            ('H', '5.08#6', 0.7),
            ('H', '5.08#7', 0.8),
            ('H', 'cta', 0.0)
        ]
    }
]

for c in clips:
    # calc VI
    dur_vi = 0.0
    for role, cid, pause in c['items']:
        txt = c['hook'][0] if cid == 'hook' else (c['cta'][0] if cid == 'cta' else vi_map[cid])
        w = len([x for x in vi_numbers(re.sub(r'<#[\d.]+#>', ' ', txt)).split() if x.strip()])
        dur_vi += w * R_VI[role] + pause
    # calc EN
    dur_en = 0.0
    for role, cid, pause in c['items']:
        txt = c['hook'][1] if cid == 'hook' else (c['cta'][1] if cid == 'cta' else en_map[cid])
        w = len([x for x in re.sub(r'<#[\d.]+#>', ' ', txt).split() if x.strip()])
        dur_en += w * R_EN[role] + pause
    # calc JA
    dur_ja = 0.0
    for role, cid, pause in c['items']:
        txt = c['hook'][2] if cid == 'hook' else (c['cta'][2] if cid == 'cta' else ja_map[cid])
        w = len(re.sub(r'<#[\d.]+#>', ' ', txt).replace(' ', '').strip())
        dur_ja += w * R_JA[role] + pause
    print(f"{c['id']}: VI={dur_vi:.1f}s, EN={dur_en:.1f}s, JA={dur_ja:.1f}s (Lines: {len(c['items'])})")
