# -*- coding: utf-8 -*-
from pathlib import Path

content = Path(".work/edition.py").read_text(encoding="utf-8")

old_part = """    "03": {
        "script": WORK / "script_tap03.json",
        "dir": "Tap03",
        "plan": "KeHoach_Video_Tap03.md",
        "master": "Tap03_master",
        "srt": "Tap03.srt",
        "n_element": {"1.09": "N1", "2.09": "N2"},
        "acting": WORK / "acting_tap03.json",
        "sfx_sheet": WORK / "sfx_tap03.json",
        "act1_cue": "1.14", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_piano_minimal.mp3"),
                2: ("bgm_ambient_deep.mp3",),
                3: "bgm_cello_sad_v2.mp3",
                4: "bgm_sub_drone.mp3",
                5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("IQ 145", "GƯƠNG"),
        "thumb_bg": "t3_brain_mirror",
        "title": "Gã Khổng Lồ IQ 145 — Hồ sơ Edmund Kemper & chiếc gương giải phẫu tâm trí",
        "act_titles": {1: "Hồi 1 · Cuộc gọi nửa đêm từ bốt điện thoại Colorado",
                       2: "Hồi 2 · Hiện trường & chuỗi săn mồi — Nấc thang của sự thay thế",
                       3: "Hồi 3 · Giải phẫu tâm lý — Bên trong bộ não kẻ thái nhân cách tự phản tỉnh",
                       4: "Hồi 4 · Đối thoại với FBI — Nền tảng của nghệ thuật lập hồ sơ tội phạm",
                       5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ & lời kết"},
        "summary": ("1.03#1", "5.08#1"),
        "need": ["1.05#3", "1.10#1", "1.10#10", "1.13#7", "2.04#5", "2.06#2", "3.05#7", "3.05#10", "3.08#8", "3.08#10", "4.05#15", "4.05#19", "4.08#2", "5.02#5", "5.02#7", "5.02#12", "5.05#4", "5.05#5", "5.08#3"],
        "case": "Kemper",
        "n1": ("TRỰC BAN CẢNH SÁT SANTA CRUZ", "Người trực đêm", "TRỰC BAN"),
        "n2": ("CẢNH SÁT QUÁN RƯỢU", "Đồng nghiệp tại The Jury Room", "CẢNH SÁT"),
        "cast": None,                  # dùng giọng mặc định của kênh (bộ A)
    },"""

new_part = """    "03": {
        "script": WORK / ("script_tap03_EN.json" if EN else "script_tap03.json"),
        "dir": "Tap03_EN" if EN else "Tap03",
        "plan": "KeHoach_Video_Tap03_EN.md" if EN else "KeHoach_Video_Tap03.md",
        "master": "Tap03_EN_master" if EN else "Tap03_master",
        "srt": "Tap03_EN.srt" if EN else "Tap03.srt",
        "intro": "intro_kenh_EN_t03.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.09": "N1", "2.09": "N2"},
        "acting": WORK / ("acting_tap03_EN.json" if EN else "acting_tap03.json"),
        "sfx_sheet": WORK / "sfx_tap03.json",
        "act1_cue": "1.14", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_piano_minimal.mp3"),
                2: ("bgm_ambient_deep.mp3",),
                3: "bgm_cello_sad_v2.mp3",
                4: "bgm_sub_drone.mp3",
                5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("THE IQ 145", "GIANT") if EN else ("IQ 145", "GƯƠNG"),
        "thumb_bg": "t3_brain_mirror",
        "title": ("The IQ 145 Giant: Edmund Kemper & The Psychological Autopsy of a Serial Killer | Amber eyes" if EN else
                  "Gã Khổng Lồ IQ 145 — Hồ sơ Edmund Kemper & chiếc gương giải phẫu tâm trí"),
        "act_titles": ({1: "Act 1 · The Midnight Call from a Colorado Payphone",
                        2: "Act 2 · The Scene & Escalation — The Ladder of Substitution",
                        3: "Act 3 · Psychological Autopsy — Inside the Mind of an Analytical Psychopath",
                        4: "Act 4 · Conversations with the FBI — The Foundations of Criminal Profiling",
                        5: "Act 5 · The Verdict, Behavioral Red Flags & Final Thoughts"} if EN else
                       {1: "Hồi 1 · Cuộc gọi nửa đêm từ bốt điện thoại Colorado",
                        2: "Hồi 2 · Hiện trường & chuỗi săn mồi — Nấc thang của sự thay thế",
                        3: "Hồi 3 · Giải phẫu tâm lý — Bên trong bộ não kẻ thái nhân cách tự phản tỉnh",
                        4: "Hồi 4 · Đối thoại với FBI — Nền tảng của nghệ thuật lập hồ sơ tội phạm",
                        5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ & lời kết"}),
        "summary": ("1.03#1", "5.08#1"),
        "need": ["1.05#3", "1.10#1", "1.10#10", "1.13#7", "2.04#5", "2.06#2", "3.05#7", "3.05#10", "3.08#8", "3.08#10", "4.05#15", "4.05#19", "4.08#2", "5.02#5", "5.02#7", "5.02#12", "5.05#4", "5.05#5", "5.08#3"],
        "case": "Kemper",
        "n1": (("SANTA CRUZ POLICE DESK", "Desk Officer on Duty", "DESK OFFICER") if EN else
               ("TRỰC BAN CẢNH SÁT SANTA CRUZ", "Người trực đêm", "TRỰC BAN")),
        "n2": (("BAR PATRON / POLICE", "Jury Room Regular", "OFFICER") if EN else
               ("CẢNH SÁT QUÁN RƯỢU", "Đồng nghiệp tại The Jury Room", "CẢNH SÁT")),
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("SANTA CRUZ POLICE DESK", "Night Shift Perspective"),
                     "N2": ("BAR PATRON / POLICE", "Jury Room Regular")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "DESK OFFICER", "N2": "OFFICER"},
        "cards_en": (
            ("ABOUT THIS DOCUMENTARY", [
                [("Educational content:", 1),
                 (" A forensic & criminal psychology analysis based strictly on public trial exhibits, "
                  "psychiatric evaluations, and official law enforcement archives.", 0)],
                [("Investigative purpose:", 1),
                 (" Produced solely for educational, criminological, and behavioral research.", 0)],
                [("No defamation:", 1),
                 (" Not intended to sensationalize crimes or inflict distress upon victims’ families.", 0)]]),
            ("VIEWER DISCRETION & ADVISORY", [
                [("Mature audience only:", 1),
                 (" Contains mature themes, discussions of serial homicide, and deep psychological analysis. "
                  "Viewer discretion is strongly advised.", 0)],
                [("AI & Dramatization:", 1),
                 (" Narrated with synthetic AI voices. Visuals and character avatars are dramatized "
                  "illustrations and do not depict real persons.", 0)],
                [("Professional boundaries:", 1),
                 (" Not a substitute for professional psychiatric, medical, or legal consultation.", 0)]])),
        "card_geom": {"cw": 1660, "ch": 780, "size": 40, "line_h": 54, "gap": 22, "y0": 178},
        "cast": None,                  # dùng giọng mặc định của kênh (bộ A)
    },"""

assert old_part in content, "old_part not found!"
content = content.replace(old_part, new_part)
Path(".work/edition.py").write_text(content, encoding="utf-8", newline="\n")
print("Updated edition.py successfully!")
