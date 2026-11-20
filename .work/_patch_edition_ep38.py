# -*- coding: utf-8 -*-
"""Inspect and append EPISODES['38'] into edition.py."""
import sys
from pathlib import Path

ROOT = Path(r"d:\TEST\Gax\amber-eyes")
edition_path = ROOT / ".work" / "edition.py"
text = edition_path.read_text(encoding="utf-8")

# Let's locate "37":
target = '"37": {'
pos = text.find(target)
print("pos of '\"37\": {':", pos)
# Find the end of 37 block:
end_marker = '"cast": None,'
pos_cast = text.find(end_marker, pos)
pos_close = text.find("    },", pos_cast)
print("37 block close at:", pos_close)

ep38_block = '''    '38': {
        'title': 'Hồ Sơ Natascha Kampusch — 3.096 Ngày Dưới Lòng Đất & Ý Chí Sinh Tồn Đánh Bại Thao Túng',
        'dir': 'Tap38',
        'script': ROOT / '.work' / 'script_tap38.json',
        'acting': ROOT / '.work' / 'acting_tap38.json',
        'sfx_sheet': ROOT / '.work' / 'sfx_tap38.json',
        'plan': 'KeHoach_Video_Tap38.md',
        'master': 'Tap38_master',
        'srt': 'Tap38.srt',
        'case': 'NataschaKampusch',
        'cast': None,
        'act1_cue': '1.02#1',
        'silence_cue': '1.05',
        'click_cues': ('1.03', '3.05'),
        'act_titles': {
            1: 'Hồi 1 · Sự biến mất bên đường và chiếc bẫy trắng ngoại ô Vienna',
            2: 'Hồi 2 · 3.096 ngày dưới hầm ngầm 5m² và chiến lược sinh tồn kép',
            3: 'Hồi 3 · Cửa sổ cơ hội vàng và cuộc đào thoát ngoạn mục',
            4: 'Hồi 4 · Sự sụp đổ của ảo tưởng toàn năng và bản án trên đường ray',
            5: 'Hồi 5 · Ngọn nến nhân bản và bài học thức tỉnh xã hội'
        },
        'bed': {
            1: 'bgm_cello_sad.mp3',
            2: 'bgm_ambient_deep.mp3',
            3: 'bgm_piano_minimal.mp3',
            4: 'bgm_violin_heart.mp3',
            5: 'bgm_piano_warm.mp3'
        },
        'n1': ('NHÂN CHỨNG 12 TUỔI', 'Học sinh chứng kiến vụ bắt cóc', 'NHÂN CHỨNG'),
        'n2': ('ERNST HOLZAPFEL', 'Bạn làm ăn kiêm người nghe thú tội cuối cùng', 'HOLZAPFEL'),
        'n_element': {'1.07': 'N1', '4.05': 'N2'},
        'roles_en': {
            'H': ('HOST', 'Your Narrator'),
            'D': ('INVESTIGATOR', 'Vienna Police Case File'),
            'C': ('PSYCHOLOGIST', 'Forensic & Trauma Psychology'),
            'N1': ('12-YEAR-OLD WITNESS', 'Eyewitness Peer'),
            'N2': ('ERNST HOLZAPFEL', 'Associate and Confidant')
        },
        'roles_ja': {
            'H': ('ホスト', 'ナレーター'),
            'D': ('捜査官', 'ウィーン警察捜査記録'),
            'C': ('心理学者', '犯罪心理学・トラウマ分析'),
            'N1': ('12歳の目撃者', '現場目撃の小学生'),
            'N2': ('エルンスト・ホルツアプフェル', '仕事仲間・最後の自白の聞き手')
        },
        'sub_tags_en': {'H': 'HOST', 'D': 'INVESTIGATOR', 'C': 'PSYCHOLOGIST', 'N1': 'WITNESS', 'N2': 'HOLZAPFEL'},
        'sub_tags_ja': {'H': 'ホスト', 'D': '捜査官', 'C': '心理学者', 'N1': '目撃者', 'N2': 'ホルツアプフェル'},
        'summary': ('1.02#1', '3.02#1'),
        'thumb': ('3.096 NGÀY DƯỚI ĐẤT', 'NATASCHA KAMPUSCH'),
        'thumb_bg': 't38_subterranean_vault_door',
        'hashtags': '#TrueCrime #NataschaKampusch #Priklopil #CriminalPsychology #TamLyToiPham #AmberEyes #HoSoVuAn',
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

insertion_point = pos_close + len("    },")
new_text = text[:insertion_point] + "\n" + ep38_block + text[insertion_point:]

edition_path.write_text(new_text, encoding="utf-8")
print("Successfully patched edition.py with EPISODES['38']!")
