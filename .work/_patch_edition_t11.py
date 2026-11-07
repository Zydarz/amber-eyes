import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

path = Path('.work/edition.py')
text = path.read_text(encoding='utf-8')

# Tìm vị trí bắt đầu và kết thúc của "11": { ... }
start_marker = '    "11": {'
end_marker = '    "12": {'

s_idx = text.find(start_marker)
e_idx = text.find(end_marker)

if s_idx == -1 or e_idx == -1:
    print("Cannot find markers!")
    sys.exit(1)

old_block = text[s_idx:e_idx]
print("Old block:\n", old_block)

new_block = '''    "11": {
        "script": WORK / "script_tap11.json",
        "dir": "Tap11",
        "plan": "KeHoach_Video_Tap11.md",
        "master": "Tap11_master",
        "srt": "Tap11.srt",
        "n_element": {"1.06": "N1", "4.08": "N2"},
        "acting": WORK / "acting_tap11.json",
        "sfx_sheet": WORK / "sfx_tap11.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.06"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("KEN & BARBIE", "THỎA THUẬN VỚI QUỶ DỮ"),
        "title": "Cặp Đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi & Thỏa Thuận Với Quỷ Dữ (Hồ Sơ Paul Bernardo & Karla Homolka)",
        "act_titles": {1: "Hồi 1 · Vỏ bọc hoàn hảo của Cặp đôi Ken & Barbie",
                       2: "Hồi 2 · Hiện trường & Vực thẳm leo thang — 4 nấc thang tội ác",
                       3: "Hồi 3 · Giải mã liên minh bệnh hoạn — Điên cuồng đôi & Trung hòa đạo đức",
                       4: "Hồi 4 · Thỏa thuận với Quỷ dữ & Sự sụp đổ của mặt nạ nạn nhân",
                       5: "Hồi 5 · Phán quyết, di chứng tư pháp & Bài học cảnh báo đỏ"},
        "summary": ("1.03#1", "3.02#1"),
        "need": [],
        "case": "Bernardo", "n1": ("NGƯỜI HÀNG XÓM", "Cư dân Port Dalhousie", "HÀNG XÓM"),
        "n2": ("CÔNG TỐ VIÊN", "Điều tra viên vụ án", "CÔNG TỐ VIÊN"),
        "cast": None,
    },
'''

new_text = text[:s_idx] + new_block + text[e_idx:]
path.write_text(new_text, encoding='utf-8')
print("Successfully patched edition.py!")
