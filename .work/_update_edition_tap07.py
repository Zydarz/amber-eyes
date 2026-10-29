import sys
from pathlib import Path

p = Path(".work/edition.py")
content = p.read_text(encoding="utf-8")

old_str = '''        "act1_cue": "1.12", "silence_cue": "1.04", "click_cues": ("1.02", "4.08"),
        "bed": {1: "bgm_piano_minimal.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_sub_drone.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("BẢN ÁN GIẾT NGƯỜI", "BẰNG TIN NHẮN"),
        "title": "Bản Án Giết Người Bằng Tin Nhắn — Thao túng tâm lý và hội chứng Münchausen kỹ thuật số (vụ Michelle Carter & Conrad Roy)",
        "act_titles": {1: "Hồi 1 · Buổi sáng định mệnh tại bãi đỗ xe Kmart", 2: "Hồi 2 · Mê cung hai mươi nghìn dòng tin nhắn",
                       3: "Hồi 3 · Vở kịch cô bạn gái đau khổ & bộ não ái kỷ kịch tính", 4: "Hồi 4 · Dòng tin nhắn đầy tội lỗi và bản án lịch sử",
                       5: "Hồi 5 · Đạo đức không gian số & Đạo luật Conrad"},
        "summary": ("1.01#1", "3.04#1"),'''

new_str = '''        "act1_cue": "1.04", "silence_cue": "1.06", "click_cues": ("1.02",),
        "bed": {1: "bgm_piano_minimal.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_cello_sad.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("BẢN ÁN GIẾT NGƯỜI", "BẰNG TIN NHẮN"),
        "title": "Bản Án Giết Người Bằng Tin Nhắn — Thao túng tâm lý và hội chứng Münchausen kỹ thuật số (vụ Michelle Carter & Conrad Roy)",
        "act_titles": {1: "Hồi 1 · Buổi sáng định mệnh tại bãi đỗ xe Kmart", 2: "Hồi 2 · Mê cung hai mươi nghìn dòng tin nhắn",
                       3: "Hồi 3 · Vở kịch cô bạn gái đau khổ & bộ não ái kỷ kịch tính", 4: "Hồi 4 · Dòng tin nhắn đầy tội lỗi và bản án lịch sử",
                       5: "Hồi 5 · Đạo đức không gian số & Đạo luật Conrad"},
        "summary": ("1.02#1", "3.04#1"),'''

# Normalize newlines
content_norm = content.replace("\r\n", "\n")
old_norm = old_str.replace("\r\n", "\n")
new_norm = new_str.replace("\r\n", "\n")

if old_norm in content_norm:
    content_norm = content_norm.replace(old_norm, new_norm, 1)
    # Write back keeping original line endings if CRLF
    if "\r\n" in content:
        content_norm = content_norm.replace("\n", "\r\n")
    p.write_text(content_norm, encoding="utf-8")
    print("Updated edition.py successfully!")
else:
    print("ERROR: old_str not found in edition.py!")
    sys.exit(1)
