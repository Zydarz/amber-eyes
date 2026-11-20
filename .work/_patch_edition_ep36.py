# -*- coding: utf-8 -*-
"""Insert EPISODES['36'] into edition.py."""
from pathlib import Path

edition_path = Path('.work/edition.py')
text = edition_path.read_text(encoding='utf-8')

ep36_block = '''    '36': {
        'title': 'Tiếng Nói Trong Tâm Trí — Khởi Phát Tâm Thần Phân Liệt & Cơn Địa Chấn Thurston High (Hồ Sơ Kip Kinkel)',
        'dir': 'Tap36',
        'script': ROOT / '.work' / 'script_tap36.json',
        'acting': ROOT / '.work' / 'acting_tap36.json',
        'sfx_sheet': ROOT / '.work' / 'sfx_tap36.json',
        'plan': 'KeHoach_Video_Tap36.md',
        'master': 'Tap36_master',
        'srt': 'Tap36.srt',
        'case': 'KipKinkel',
        'cast': None,
        'act1_cue': '1.02',
        'silence_cue': '1.04',
        'click_cues': ('1.02', '4.02'),
        'act_titles': {
            1: 'Hồi 1 · Cơn địa chấn Thurston High & Ảo tưởng bình yên thôn dã',
            2: 'Hồi 2 · Điểm mù gia đình giáo viên & Quỹ đạo leo thang ảo giác',
            3: 'Hồi 3 · Ngòi nổ điểm gãy 20/05/1998 & Cơn ác mộng căn tin',
            4: 'Hồi 4 · Phòng hỏi cung, ảo thanh mệnh lệnh & Bản chất sự hối hận',
            5: 'Hồi 5 · Bản án 111 năm, sự thức tỉnh sau 23 năm & Bài học sinh tồn'
        },
        'bed': {
            1: 'bgm_cello_sad.mp3',
            2: 'bgm_ambient_deep.mp3',
            3: 'bgm_piano_minimal.mp3',
            4: 'bgm_violin_heart.mp3',
            5: 'bgm_piano_warm.mp3'
        },
        'n1': ('BẠN HỌC THURSTON', 'Nhân chứng hiện trường', 'BẠN HỌC'),
        'n2': ('KIP KINKEL (2021)', 'Kẻ thủ ác sau 23 năm', 'KIP'),
        'n_element': {'1.07': 'N1', '4.05': 'N2'},
        'roles_en': {
            'H': ('HOST', 'Your Narrator'),
            'D': ('INVESTIGATOR', 'Kip Kinkel Case File'),
            'C': ('PSYCHOLOGIST', 'Behavioral & Forensic Dynamics'),
            'N1': ('THURSTON CLASSMATE', 'Eyewitness Peer'),
            'N2': ('KIP KINKEL (2021)', 'Perpetrator Testimony')
        },
        'roles_ja': {
            'H': ('ホスト', 'ナレーター'),
            'D': ('捜査官', '事件記録 キップ・キンケル'),
            'C': ('心理学者', '犯罪心理学'),
            'N1': ('サーストン高校同級生', '現場の目撃者'),
            'N2': ('キップ・キンケル (2021)', '23年後の自白')
        },
        'sub_tags_en': {'H': 'HOST', 'D': 'INVESTIGATOR', 'C': 'PSYCHOLOGIST', 'N1': 'CLASSMATE', 'N2': 'KIP'},
        'sub_tags_ja': {'H': 'ホスト', 'D': '捜査官', 'C': '心理学者', 'N1': '同級生', 'N2': 'キップ'},
        'summary': ('1.02#1', '3.02#1'),
        'thumb': ('TIẾNG NÓI TRONG TÂM TRÍ', 'KIP KINKEL 1998'),
        'thumb_bg': 't36_thurston_high_cafeteria_shadow',
        'hashtags': '#TrueCrime #KipKinkel #ThurstonHigh #CriminalPsychology #TamLyToiPham #AmberEyes #HoSoVuAn',
        'mux_af': 'alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1',
        'bg2': {},
        'combo': {},
        'flag_hold_shots': (),
        'inset': {},
        'need': [],
        'route_pins': {},
        'sfx_cues': [],
        'text_scrim': []
    },
'''

target = '    "37": {'
assert target in text, f"Target not found in {edition_path}"

new_text = text.replace(target, ep36_block + target)
edition_path.write_text(new_text, encoding='utf-8')
print("Successfully inserted EPISODES['36'] into edition.py")
