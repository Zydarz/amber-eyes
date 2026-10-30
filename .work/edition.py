# -*- coding: utf-8 -*-
"""Language edition + episode switch shared by the pipeline scripts.

    AE_LANG=en py -3 .work/<script>.py     -> English edition (Tap01_EN)
    AE_LANG=ko py -3 .work/<script>.py     -> Korean edition  (Tap01_KO)
    AE_EP=02 py -3 .work/<script>.py       -> Tập 02 (bản tiếng Việt)
    py -3 .work/<script>.py                -> Tập 01 tiếng Việt, đường dẫn như cũ

Every English output carries an _EN suffix or lives under 02_SAN_XUAT/Tap01_EN, every Korean
output carries a _KO suffix or lives under 02_SAN_XUAT/Tap01_KO, and every Tập 02 intermediate
file carries a _t02 suffix, so no edition or episode overwrites another.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   # gốc dự án = thư mục cha của .work (tự dòng, không cứng đường dẫn)
WORK = ROOT / ".work"
LANG = os.environ.get("AE_LANG", "vi").strip().lower()
EN = LANG == "en"
KO = LANG == "ko"
JA = LANG == "ja"
EPN = os.environ.get("AE_EP", "01").strip().zfill(2)
if (EN or KO or JA) and not (EPN.isdigit() and 1 <= int(EPN) <= 29):
    raise SystemExit("Bản tiếng Anh/Hàn/Nhật hỗ trợ từ Tập 01 đến Tập 29 (AE_EP=01..29).")
SUF = ("_EN" if EN else ("_KO" if KO else ("_JA" if JA else ""))) + ("" if EPN == "01" else f"_t{EPN}")


def w(name):
    """.work data file or folder for this edition/episode: 'timeline_s.json' -> 'timeline_s_t02.json'."""
    p = Path(name)
    return WORK / (p.stem + SUF + p.suffix)


# ---------------------------------------------------------------- per-episode settings
# Mọi chỗ trước đây viết cứng cho Tập 01 trong các script (A12) nằm ở đây.
EPISODES = {
    "01": {
        "script": WORK / ("script_EN.json" if EN else "script_v2.json"),
        "dir": "Tap01_EN" if EN else "Tap01",
        "plan": "KeHoach_Video_Tap01_EN.md" if EN else "KeHoach_Video_Tap01.md",
        "master": "Tap01_EN_master" if EN else "Tap01_master",
        "srt": "Tap01_EN.srt" if EN else "Tap01.srt",
        "intro": "intro_kenh_EN.mov" if EN else "intro_kenh.mov",
        "tts_fix": {"1.03#1": "June fourteenth, twenty fifteen."},
        "n_element": {"1.07": "N1", "4.03": "N2"},
        "acting": w("acting.json") if EN else None,        # acting_EN.json
        "sfx_sheet": None,
        # build_audio3: nhạc Hồi 1 vào ở mốc · "im lặng tuyệt đối" · tiếng "Tách"
        "act1_cue": "1.12", "silence_cue": "1.09", "click_cues": ("1.06", "1.12"),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: "bgm_ambient_deep.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [
            ("police_siren_distant.wav", "1.02", -2.80, -3), ("door_knock.wav", "1.02", -0.90, -2),
            ("radio_chatter.wav", "1.10", -3.00, -6), ("heart_beep.wav", "2.01", -5.03, -18),
            ("paper_rustle.wav", "2.03", -1.00, -8), ("lock_door.wav", "2.08", -1.10, -2),
            ("heartbeat_slow.wav", "4.01", -4.97, -18), ("chains.wav", "4.06", -2.50, -5),
            ("keyboard_night.wav", "4.14", -2.20, -12), ("gavel.wav", "5.01", -1.10, 1),
            ("folder_close.wav", "5.13", -0.47, -8)],
        # parse_shots: cảnh ghép sẵn, đổi nền trong shot, ảnh ghim
        "combo": {"1-04": "crowd_house", "1-07": "deedee_room", "1-17": "interrogation_gypsy",
                  "1-19": "bedroom_door_gypsy", "2-02": "wheelchair_gypsy", "3-02": "fog_deedee",
                  "3-10": "fog_deedee", "3-11": "spotlight_deedee", "3-12": "spotlight_deedee",
                  "3-20": "wheelchair_gypsy", "4-04": "wheelchair_spot", "4-06": "glass_box_gypsy",
                  "4-19": "night_street_gypsy", "4-21": "house_return", "4-24": "crowd_away",
                  "4-30": "godejohn_screen", "4-31": "two_shadows", "5-16": "house_free",
                  "4-10": "cage", "5-17": "cage_open", "4-22": "night_screen",
                  "2-13": "pinboard", "2-14": "pinboard", "2-15": "pinboard"},
        "inset": {"2-14": "storm"},
        "bg2": {"4-10": "cage_open", "4-22": "screen_off"},
        "flag_hold_shots": ("5-14",),                          # dòng giữ hình vẽ đủ 4 cờ
        "route_pins": {"1-16": ("SPRINGFIELD, MISSOURI", "WISCONSIN")},   # T7: nhãn 2 ghim
        # package
        "thumb": ("POISON IN THE NAME", "OF A MOTHER’S LOVE") if EN else ("母の愛という名の", "毒薬") if JA else ("엄마의 사랑이라는", "이름의 독약") if KO else ("ĐỘC DƯỢC", "NHÂN DANH TÌNH MẸ"),
        "title": ("The Blanchard Case: Deciphering Munchausen Syndrome by Proxy | Amber eyes" if EN else
                  "母の愛という名の毒薬――代理型ミュンハウゼン症候群を解読（Blanchard事件） | Amber eyes" if JA else
                  "엄마의 사랑이라는 이름의 독약――대리 뮌하우젠 증후군(FDIA) 해독 (Blanchard 사건) | Amber eyes" if KO else
                  "Độc Dược Nhân Danh Tình Mẹ — Giải mã Hội chứng Münchausen qua trung gian"),
        "act_titles": ({1: "Act 1 · The Moment Trust Broke", 2: "Act 2 · 23 Years in a Medical Prison",
                        3: "Act 3 · Inside the Mind of an FDIA Perpetrator", 4: "Act 4 · Why Didn't Gypsy Walk Away?",
                        5: "Act 5 · Forensic Verdict & Epilogue"} if EN else
                       {1: "第1幕 · 信頼が崩れる瞬間", 2: "第2幕 · 精神刑務所での23年間",
                        3: "第3幕 · FDIA犯罪者の脳の内部", 4: "第4幕 · なぜGypsyは逃げなかったのか？",
                        5: "第5幕 · 司法の裁き、レッドフラッグ＆教訓"} if JA else
                       {1: "제1막 · 신뢰가 무너지는 순간", 2: "제2막 · 의료 감옥에서의 23년",
                        3: "제3막 · FDIA 가해자의 뇌 속", 4: "제4막 · 왜 Gypsy는 도망치지 못했는가?",
                        5: "제5막 · 사법적 단죄와 레드플래그, 그리고 교훈"} if KO else
                       {1: "Hồi 1 · Khoảnh khắc đứt gãy niềm tin", 2: "Hồi 2 · 23 năm trong nhà tù y khoa",
                        3: "Hồi 3 · Bên trong bộ não của kẻ mắc FDIA", 4: "Hồi 4 · Tại sao Gypsy không đứng dậy?",
                        5: "Hồi 5 · Phán quyết pháp y & lời kết"}),
        "summary": ("1.13#2", "3.02#5"),
        "need": ["4.15#2", "5.02#3", "5.04#2", "2.07#10", "3.05#5", "3.07#2", "4.07#8", "4.10#5"],
        "case": "Blanchard", "n1": (("SPRINGFIELD RESIDENT", "Longtime neighbor", "SPRINGFIELD RESIDENT") if EN else
                                    ("スプリングフィールド住民", "長年の隣人", "証人") if JA else
                                    ("스프링필드 주민", "오랜 이웃", "증인") if KO else
                                    ("NGƯỜI DÂN SPRINGFIELD", "Hàng xóm nhiều năm", "NGƯỜI DÂN")),
        "n2": (("VIEWER", "Following the case", "VIEWER") if EN else
               ("視聴者", "事件を見守る人", "視聴者") if JA else
               ("시청자", "사건을 지켜본 사람", "시청자") if KO else
               ("KHÁN GIẢ", "Theo dõi vụ án", "KHÁN GIẢ")),
        "cast": None if (EN or JA or KO) else {"H": ("audiobook_male_1", 0.90), "D": ("male-qn-qingse", 0.95), "C": ("audiobook_female_1", 0.92)},   # giữ giọng Tập 01 đã xuất
        "cast_ko": True,
    },
    "02": {
        "script": WORK / ("script_tap02_EN.json" if EN else "script_tap02.json"),
        "dir": "Tap02_EN" if EN else "Tap02",
        "plan": "KeHoach_Video_Tap02_EN.md" if EN else "KeHoach_Video_Tap02.md",
        "master": "Tap02_EN_master" if EN else "Tap02_master",
        "srt": "Tap02_EN.srt" if EN else "Tap02.srt",
        "intro": "intro_kenh_EN_t02.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.07": "N1", "4.06": "N2"},
        "acting": WORK / ("acting_tap02_EN.json" if EN else "acting_tap02.json"),
        "sfx_sheet": WORK / "sfx_tap02.json",
        "act1_cue": "1.16", "silence_cue": "1.09", "click_cues": ("1.06",),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad_v2.mp3", "bgm_sub_drone.mp3"), 4: "bgm_sub_drone.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],                                        # Tập 02 dùng sfx_sheet
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},                                      # T7 Tập 02: ghim không nhãn (không nêu địa điểm nhà nạn nhân)
        "thumb": ("THE TWO-FACED", "COLONEL") if EN else ("二重生活の", "大佐") if JA else ("ĐẠI TÁ", "HAI MẶT"),
        "thumb_bg": "t2_two_chairs",                           # nền thumbnail (Tập 01 mặc định house_police)
        "title": ("The Double Life of Colonel Russell Williams: Behavioral Escalation & "
                  "The Psychology of a Predator | Amber eyes" if EN else
                  "ラッセル・ウィリアムズ大佐の二重生活――行動のエスカレーションと捕食者の心理学 | Amber eyes" if JA else
                  "Đại Tá Hai Mặt — Quy luật leo thang hành vi & sự phân mảnh tâm trí (vụ Russell Williams)"),
        "act_titles": ({1: "Act 1 · The Extreme Contrast Behind a Colonel’s Rank",
                        2: "Act 2 · The Scene & Dossier — The 4 Stages of the Abyss",
                        3: "Act 3 · Psychological Autopsy — Inside the Mind of a Two-Faced Predator",
                        4: "Act 4 · The Interrogation Room — Breaking a Military Mind",
                        5: "Act 5 · The Verdict, Red Flags & Closing Thoughts"} if EN else
                       {1: "第1幕 · 大佐の階級章の裏にある極端なコントラスト",
                        2: "第2幕 · 現場と証拠ファイル――深淵への4段階",
                        3: "第3幕 · 心理解剖――二重生活の捕食者の内面",
                        4: "第4幕 · 取調室――軍人の頭脳を打ち砕く",
                        5: "第5幕 · 判決、危険信号、そして結びの考察"} if JA else
                       {1: "Hồi 1 · Sự tương phản phía sau quân hàm đại tá", 2: "Hồi 2 · 4 bậc thang của vực thẳm",
                        3: "Hồi 3 · Bên trong bộ não của sát nhân hai mặt", 4: "Hồi 4 · Nghệ thuật bẻ gãy bộ óc quân sự",
                        5: "Hồi 5 · Phán quyết, cảnh báo đỏ & lời kết"}),
        "summary": ("1.18#3", "3.04#1"),
        "need": ["1.03#4", "1.05#1", "1.05#2", "1.10#2", "1.12#2", "1.14#2", "1.17#3", "2.04#1", "2.04#2",
                 "2.05#6", "2.05#7", "2.05#13", "2.05#15", "2.08#7", "3.08#10", "4.03#6", "4.08#3",
                 "4.08#7", "4.10#1", "4.10#3", "4.10#7", "4.10#8", "4.10#9", "4.11#5", "4.11#8", "4.12#2",
                 "5.02#4", "5.04#2", "5.04#3", "5.04#5", "5.04#6", "5.04#7", "5.04#8", "5.04#9"],
        "case": "Williams",
        "n1": (("BASE PERSONNEL", "Military Community Perspective", "BASE PERSONNEL") if EN else
               ("トレントン基地関係者", "軍関係者の証言", "関係者") if JA else
               ("BINH SĨ CĂN CỨ TRENTON", "Nhân vật hình dung", "BINH SĨ")),
        "n2": (("CASE OBSERVER", "Public Reaction", "CASE OBSERVER") if EN else
               ("ツイード住民", "市民の反応", "住民") if JA else
               ("KHÁN GIẢ", "Theo dõi vụ án", "KHÁN GIẢ")),
        # ---- bản tiếng Anh: nhãn vai (CHU_CO_DINH_EN.md §3)
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("BASE PERSONNEL", "Military Community Perspective"),
                     "N2": ("CASE OBSERVER", "Public Reaction")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "BASE PERSONNEL", "N2": "CASE OBSERVER"},
        # ---- bản tiếng Anh: thẻ cảnh báo intro (CHU_CO_DINH_EN.md §2) — chữ dài hơn bản Tập 01
        # nên thẻ rộng hơn, chữ nhỏ hơn, mỗi gạch đầu dòng tự xuống dòng.
        "cards_en": (
            ("ABOUT THIS DOCUMENTARY", [
                [("Educational content:", 1),
                 (" A forensic & criminal psychology analysis based strictly on public records, "
                  "trial exhibits, and official police interrogation transcripts.", 0)],
                [("Investigative purpose:", 1),
                 (" Produced solely for educational, criminological, and public safety awareness.", 0)],
                [("No defamation:", 1),
                 (" Not intended to defame, harass, or inflict distress upon any innocent individuals "
                  "or victims’ families.", 0)]]),
            ("VIEWER DISCRETION & ADVISORY", [
                [("Mature audience only:", 1),
                 (" Contains mature themes, discussions of burglary, stalking, and non-graphic "
                  "accounts of violent crime. Viewer discretion is advised.", 0)],
                [("AI & Dramatization:", 1),
                 (" Narrated with synthetic AI voices. Visuals and character avatars are "
                  "dramatized illustrations and do not depict real persons.", 0)],
                [("Professional boundaries:", 1),
                 (" Not a substitute for professional legal, medical, or psychiatric advice.", 0)]])),
        "card_geom": {"cw": 1660, "ch": 780, "size": 40, "line_h": 54, "gap": 22, "y0": 178},
        "cast": None,                  # dùng giọng mặc định của kênh (bộ A)
    },
    "03": {
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
    },
    "04": {
        "script": WORK / "script_tap04.json",
        "dir": "Tap04",
        "plan": "KeHoach_Video_Tap04.md",
        "master": "Tap04_master",
        "srt": "Tap04.srt",
        "n_element": {"1.07": "N1", "4.06": "N2"},
        "acting": WORK / "acting_tap04.json",
        "sfx_sheet": WORK / "sfx_tap04.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.06", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: "bgm_sub_drone.mp3", 4: "bgm_ambient_deep.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},                                      # T7 Tập 02: ghim không nhãn (không nêu địa điểm nhà nạn nhân)
        "thumb": ("THIÊN THẦN", "TỬ THẦN"),
        "thumb_bg": "t4_somerset_exterior",
        "title": "Thiên Thần Tử Thần — Phức cảm Chúa trời và 16 năm lặng câm của 9 bệnh viện (vụ Charles Cullen)",
        "act_titles": {1: "Hồi 1 · Nghịch lý của người y tá mẫu mực", 2: "Hồi 2 · Lỗ hổng chết người của máy phát thuốc",
                       3: "Hồi 3 · Bên trong bộ não của kẻ mang Phức cảm Chúa trời", 4: "Hồi 4 · Đấu trí thẩm vấn và bước ngoặt điều tra",
                       5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ và lời kết"},
        "summary": ("1.10#3", "3.02#1"),
        "need": [],
        "case": "Cullen", "n1": ("NỮ Y TÁ SOMERSET", "Đồng nghiệp ca đêm", "Y TÁ"),
        "n2": ("AMY LOUGHREN", "Đồng nghiệp trực tiếp", "AMY"),
        "cast": None,
    },
    "05": {
        "script": WORK / ("script_tap05_EN.json" if EN else "script_tap05.json"),
        "dir": "Tap05_EN" if EN else "Tap05",
        "plan": "KeHoach_Video_Tap05_EN.md" if EN else "KeHoach_Video_Tap05.md",
        "master": "Tap05_EN_master" if EN else "Tap05_master",
        "srt": "Tap05_EN.srt" if EN else "Tap05.srt",
        "intro": "intro_kenh_EN_t05.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.09": "N1", "4.15": "N2"},
        "acting": WORK / ("acting_tap05_EN.json" if EN else "acting_tap05.json"),
        "sfx_sheet": WORK / "sfx_tap05.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 4: "bgm_ambient_deep.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {"2-06": "t5_park_trashcan_drop", "2-10": "t5_church_council_altar"},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("THE PURPLE", "FLOPPY DISK") if EN else ("CHIẾC ĐĨA MỀM", "MÀU TÍM"),
        "thumb_bg": "t5_purple_floppy_disk",
        "title": ("The Purple Floppy Disk: Narcissistic Addiction & Compartmentalization (The BTK Dennis Rader Case) | Amber eyes"
                  if EN else "Chiếc Đĩa Mềm Màu Tím — Sự phân mảnh tâm trí và cơn nghiện ái kỷ (vụ BTK Dennis Rader)"),
        "act_titles": ({1: "Act 1 · The Letter Resurfaces After 13 Years of Silence",
                        2: "Act 2 · The Crime Scene & Psychological Signature of a Two-Faced Predator",
                        3: "Act 3 · Inside the Mind of Malignant Narcissism",
                        4: "Act 4 · The Interrogation & The Digital Forensic Trap",
                        5: "Act 5 · The Verdict, Red Flags & Closing Thoughts"} if EN else
                       {1: "Hồi 1 · Bức thư tái xuất sau 13 năm lặng căm", 2: "Hồi 2 · Chữ ký tâm lý của con thú hai mặt",
                        3: "Hồi 3 · Bên trong bộ não ái kỷ ác tính", 4: "Hồi 4 · Đấu trí thẩm vấn và bẫy công nghệ đĩa mềm",
                        5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ và lời kết"}),
        "summary": ("1.10#5", "3.02#1"),
        "need": [],
        "case": "Rader",
        "n1": (("PARK CITY RESIDENT", "Suburban Neighbor", "RESIDENT") if EN else
               ("NGƯỜI DÂN PARK CITY", "Hàng xóm ngoại ô", "NGƯỜI DÂN")),
        "n2": (("KERRI RAWSON", "Daughter of Dennis Rader", "KERRI") if EN else
               ("KERRI RAWSON", "Con gái ruột", "KERRI")),
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("PARK CITY RESIDENT", "Suburban Neighbor"),
                     "N2": ("KERRI RAWSON", "Daughter of Dennis Rader")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "PARK CITY RESIDENT", "N2": "KERRI RAWSON"},
        "cards_en": (
            ("ABOUT THIS DOCUMENTARY", [
                [("Educational content:", 1),
                 (" A forensic & criminal psychology analysis based strictly on public records, "
                  "trial exhibits, and official police interrogation transcripts.", 0)],
                [("Investigative purpose:", 1),
                 (" Produced solely for educational, criminological, and public safety awareness.", 0)],
                [("No defamation:", 1),
                 (" Not intended to defame, harass, or inflict distress upon any innocent individuals "
                  "or victims’ families.", 0)]]),
            ("VIEWER DISCRETION & ADVISORY", [
                [("Mature audience only:", 1),
                 (" Contains mature themes, discussions of serial homicide, and non-graphic "
                  "accounts of violent crime. Viewer discretion is advised.", 0)],
                [("AI & Dramatization:", 1),
                 (" Narrated with synthetic AI voices. Visuals and character avatars are dramatized "
                  "illustrations and do not depict real persons.", 0)],
                [("Professional boundaries:", 1),
                 (" Not a substitute for professional legal, medical, or psychiatric advice.", 0)]])),
        "cast": None,
    },
    "06": {
        "script": WORK / "script_tap06.json",
        "dir": "Tap06",
        "plan": "KeHoach_Video_Tap06.md",
        "master": "Tap06_master",
        "srt": "Tap06.srt",
        "tts_fix": {"5.04#3": "Hắn chỉ nhếch mép buông ra một lời chửi thề ngạo mạn đầy thù hận: Hãy cút đi."},
        "n_element": {"1.09": "N1", "4.04": "N2"},
        "acting": WORK / "acting_tap06.json",
        "sfx_sheet": WORK / "sfx_tap06.json",
        "act1_cue": "1.06", "silence_cue": "1.05", "click_cues": ("1.08", "4.03"),
        "bed": {1: "bgm_piano_minimal.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_sub_drone.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NỤ CƯỜI CHÚ HỀ", "29 BÍ MẬT DƯỚI SÀN"),
        "thumb_bg": "t6_clown_mirror_chiaroscuro",
        "title": "Nụ Cười Chú Hề & 29 Bí Mật Dưới Sàn Nhà — Mặt nạ ái kỷ và sự phủ nhận trách nhiệm bệnh lý (vụ John Wayne Gacy)",
        "act_titles": {1: "Hồi 1 · Bức ảnh với Đệ nhất phu nhân và cậu bé hiệu thuốc", 2: "Hồi 2 · Cuộc đấu trí trên đường phố Des Plaines",
                       3: "Hồi 3 · Khoảng không gian tối dưới nền nhà Summerdale", 4: "Hồi 4 · Vở kịch đa nhân cách và lời nói dối bệnh lý",
                       5: "Hồi 5 · Tôi là nạn nhân thứ 34 và bài học về mặt nạ ái kỷ"},
        "summary": ("1.02#1", "3.07#1"),
        "need": [],
        "case": "Gacy", "n1": ("KIM BYERS", "Nhân viên hiệu thuốc", "KIM"),
        "n2": ("MIKE ALBRECHT", "Sĩ quan theo dõi Des Plaines", "ALBRECHT"),
        "cast": None,
    },
    "07": {
        "script": WORK / "script_tap07.json",
        "dir": "Tap07",
        "plan": "KeHoach_Video_Tap07.md",
        "master": "Tap07_master",
        "srt": "Tap07.srt",
        "n_element": {"1.07": "N1", "4.03": "N2"},
        "acting": WORK / "acting_tap07.json",
        "sfx_sheet": WORK / "sfx_tap07.json",
        "act1_cue": "1.12", "silence_cue": "1.04", "click_cues": ("1.02", "4.08"),
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
        "summary": ("1.02#1", "3.04#1"),
        "need": [],
        "case": "Carter", "n1": ("BÀ LYNN ROY", "Mẹ của nạn nhân", "BÀ ROY"),
        "n2": ("SAMANTHA BOARDMAN", "Bạn thân của Michelle", "SAMANTHA"),
        "cast": None,
    },
    "08": {
        "script": WORK / "script_tap08.json",
        "dir": "Tap08",
        "plan": "KeHoach_Video_Tap08.md",
        "master": "Tap08_master",
        "srt": "Tap08.srt",
        "n_element": {"1.07": "N1", "4.08": "N2"},
        "acting": WORK / "acting_tap08.json",
        "sfx_sheet": WORK / "sfx_tap08.json",
        "act1_cue": "1.12", "silence_cue": "1.04", "click_cues": ("1.02", "4.09"),
        "bed": {1: "bgm_piano_minimal.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_sub_drone.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("KHI THIÊN TÀI", "BỊ TẨY NÃO"),
        "title": "Khi Các Thiên Tài Bị Tẩy Não — Thao túng tâm lý tinh hoa và thảm họa Sarin (vụ Aum Shinrikyo & Shoko Asahara)",
        "act_titles": {1: "Hồi 1 · Buổi sáng định mệnh dưới lòng đất Tokyo", 2: "Hồi 2 · Khu căn cứ dưới chân núi Phú Sĩ và phòng thí nghiệm tử thần",
                       3: "Hồi 3 · Nghịch lý của các thiên tài khoa học", 4: "Hồi 4 · Ma thuật tẩy não & khái niệm Poa đẫm máu",
                       5: "Hồi 5 · Phán quyết lịch sử & bài học về sự tự do tư tưởng"},
        "summary": ("1.02#1", "3.04#1"),
        "need": [],
        "case": "Aum", "n1": ("HÀNH KHÁCH TOKYO", "Nhân chứng sống sót", "HÀNH KHÁCH"),
        "n2": ("BÁC SĨ IKUO HAYASHI", "Cựu bác sĩ Aum", "HAYASHI"),
        "cast": None,
    },
    "09": {
        "script": WORK / "script_tap09.json",
        "dir": "Tap09",
        "plan": "KeHoach_Video_Tap09.md",
        "master": "Tap09_master",
        "srt": "Tap09.srt",
        "n_element": {"1.07": "N1", "4.05": "N2"},
        "acting": WORK / "acting_tap09.json",
        "sfx_sheet": WORK / "sfx_tap09.json",
        "act1_cue": "1.12", "silence_cue": "1.05", "click_cues": ("1.02", "4.06"),
        "bed": {1: "bgm_guitar_acoustic_60s.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NGHỆ THUẬT", "XÓA BỎ BẢN NGÃ"),
        "title": "Nghệ Thuật Xóa Bỏ Bản Ngã — Hồ sơ Charles Manson & Thảm kịch Gia đình Manson",
        "act_titles": {1: "Hồi 1 · Đêm đen trên đồi Beverly và dấu chấm hết của Mùa hè Tình yêu", 2: "Hồi 2 · Ảo ảnh Helter Skelter tại trang trại Spahn Ranch",
                       3: "Hồi 3 · Nghệ thuật xóa bỏ bản ngã (Cơ chế tẩy não 3 giai đoạn)", 4: "Hồi 4 · Lời khai trước tòa và cái bẫy quyền lực của kẻ không chạm tay",
                       5: "Hồi 5 · Phán quyết lịch sử & bài học về sự tự chủ tinh thần"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Manson", "n1": ("CƯ DÂN LOS ANGELES", "Nhân chứng thời đại", "CƯ DÂN"),
        "n2": ("LINDA KASABIAN", "Cựu thành viên Gia đình Manson", "KASABIAN"),
        "cast": None,
    },
    "10": {
        "script": WORK / "script_tap10.json",
        "dir": "Tap10",
        "plan": "KeHoach_Video_Tap10.md",
        "master": "Tap10_master",
        "srt": "Tap10.srt",
        "n_element": {"1.07": "N1", "4.05": "N2"},
        "acting": WORK / "acting_tap10.json",
        "sfx_sheet": WORK / "sfx_tap10.json",
        "act1_cue": "1.12", "silence_cue": "1.05", "click_cues": ("1.03", "4.06"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("CHIẾC HỘP GỖ", "7 NĂM VÔ HÌNH"),
        "thumb_bg": "t10_wooden_box_under_bed_shadow",
        "title": "Chiếc Hộp Gỗ Dưới Gầm Giường — Sự Bất Lực Tập Nhiễm & Bóng Ma 'The Company' (Hồ Sơ Colleen Stan)",
        "act_titles": {1: "Hồi 1 · Chuyến xe định mệnh và chiếc hộp đen dưới gầm giường", 2: "Hồi 2 · Bảy năm trong bóng tối và sự biến mất của thời gian",
                       3: "Hồi 3 · Nghịch lý ngày về và sự bất lực tập nhiễm", 4: "Hồi 4 · Sự rạn nứt của lồng giam và cuộc giải cứu ngầm",
                       5: "Hồi 5 · Ánh sáng sau bảy năm địa ngục & Sự hồi sinh kỳ diệu"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Colleen", "n1": ("BẠN CỦA COLLEEN", "Nhân chứng thời đại", "BẠN BÈ"),
        "n2": ("JANICE HOOKER", "Đồng phạm kiêm người giải cứu", "JANICE"),
        "cast": None,
    },
    "11": {
        "script": WORK / "script_tap11.json",
        "dir": "Tap11",
        "plan": "KeHoach_Video_Tap11.md",
        "master": "Tap11_master",
        "srt": "Tap11.srt",
        "n_element": {"1.05": "N1", "4.05": "N2"},
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
        "act_titles": {1: "Hồi 1 · Vỏ bọc hoàn hảo của Cặp đôi Ken & Barbie", 2: "Hồi 2 · Chiếc mặt nạ rơi xuống và thỏa thuận với quỷ dữ",
                       3: "Hồi 3 · Giải mã hội chứng điên cuồng đôi (Folie à Deux)", 4: "Hồi 4 · Sáu cuốn băng trên trần nhà và sự sụp đổ của một ảo tưởng",
                       5: "Hồi 5 · Bài học đắt giá về mặt nạ nạn nhân & Lời cảnh tỉnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Bernardo", "n1": ("NGƯỜI HÀNG XÓM", "Cư dân Port Dalhousie", "HÀNG XÓM"),
        "n2": ("CÔNG TỐ VIÊN", "Điều tra viên vụ án", "CÔNG TỐ VIÊN"),
        "cast": None,
    },
    "12": {
        "script": WORK / "script_tap12.json",
        "dir": "Tap12",
        "plan": "KeHoach_Video_Tap12.md",
        "master": "Tap12_master",
        "srt": "Tap12.srt",
        "n_element": {"1.07": "N1", "4.10": "N2"},
        "acting": WORK / "acting_tap12.json",
        "sfx_sheet": WORK / "sfx_tap12.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("THẢM KỊCH", "JONESTOWN"),
        "title": "Thảm Kịch Jonestown — Khi 918 Con Người Cùng Bước Vào Chỗ Chết (Hồ Sơ Jim Jones & Peoples Temple)",
        "act_titles": {1: "Hồi 1 · Lời hứa thiên đường và bóng ma nơi rừng sâu", 2: "Hồi 2 · Cuộc phục kích đường băng và tiếng còi báo động định mệnh",
                       3: "Hồi 3 · Giải mã cơ chế tâm lý: Từ phục tùng đến tư duy tập thể", 4: "Hồi 4 · Cuộn băng tử thần Q 042 và tiếng nói phản kháng cô đơn",
                       5: "Hồi 5 · Bài học đắt giá về tâm lý bầy đàn & Lời cảnh tỉnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Jonestown", "n1": ("LESLIE WAGNER-WILSON", "Cựu thành viên Peoples Temple", "CỰU TÍN ĐỒ"),
        "n2": ("ĐIỀU TRA VIÊN FBI", "Tiếp cận hiện trường Jonestown", "ĐIỀU TRA VIÊN"),
        "cast": None,
    },
    "13": {
        "script": WORK / "script_tap13.json",
        "dir": "Tap13",
        "plan": "KeHoach_Video_Tap13.md",
        "master": "Tap13_master",
        "srt": "Tap13.srt",
        "n_element": {"1.07": "N1", "4.06": "N2"},
        "acting": WORK / "acting_tap13.json",
        "sfx_sheet": WORK / "sfx_tap13.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("CON NHÀ", "NGƯỜI TA"),
        "title": "Vỏ Bọc 'Con Nhà Người Ta' & Lời Nói Dối 10 Năm (Hồ Sơ Jennifer Pan)",
        "act_titles": {1: "Hồi 1 · Vỏ bọc 'Con nhà người ta' và tòa tháp dối lừa mười năm", 2: "Hồi 2 · Đêm kinh hoàng tại đại lộ Helen và cuộc gọi 911",
                       3: "Hồi 3 · Giải mã tâm lý: Từ 'Cha mẹ hổ' đến hội chứng nói dối bệnh lý", 4: "Hồi 4 · Đấu trí phòng thẩm vấn & Sự thức tỉnh của người cha",
                       5: "Hồi 5 · Bản án lương tâm & Lời cảnh tỉnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Pan", "n1": ("BẠN HỌC", "Bạn thời phổ thông", "BẠN HỌC"),
        "n2": ("HUEI HANN PAN", "Người cha sống sót", "NGƯỜI CHA"),
        "cast": None,
    },
    "14": {
        "script": WORK / "script_tap14.json",
        "dir": "Tap14",
        "plan": "KeHoach_Video_Tap14.md",
        "master": "Tap14_master",
        "srt": "Tap14.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap14.json",
        "sfx_sheet": WORK / "sfx_tap14.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NẠN NHÂN", "GASLIGHTING"),
        "title": "Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới Tội Ác (Hồ Sơ Betty Broderick)",
        "act_titles": {1: "Hồi 1 · Người vợ hy sinh và chiếc bẫy thao túng thực tại", 2: "Hồi 2 · Cuộc chiến pháp lý tàn khốc và sự đứt gãy tâm lý",
                       3: "Hồi 3 · Giải mã tâm lý: Gaslighting, tổn thương ái kỷ & bẫy nạn nhân", 4: "Hồi 4 · Năm phát đạn rạng sáng và phiên tòa chia rẽ nước Mỹ",
                       5: "Hồi 5 · Bài học đắt giá về rủi ro hôn nhân & Lời cảnh tỉnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Broderick", "n1": ("BẠN THÂN LA JOLLA", "Bạn thân của Betty", "BẠN THÂN"),
        "n2": ("KIM BRODERICK", "Con gái lớn", "CON GÁI"),
        "cast": None,
    },
    "15": {
        "script": WORK / "script_tap15.json",
        "dir": "Tap15",
        "plan": "KeHoach_Video_Tap15.md",
        "master": "Tap15_master",
        "srt": "Tap15.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap15.json",
        "sfx_sheet": WORK / "sfx_tap15.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("CƠN CUỒNG GHEN", "RANH GIỚI"),
        "title": "Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới — Nỗi Sợ Bị Ruồng Bỏ & Thảm Kịch Phòng Tắm (Hồ Sơ Jodi Arias)",
        "act_titles": {1: "Hồi 1 · Ám ảnh độc hại và thảm kịch trong buồng tắm", 2: "Hồi 2 · Dấu vết kỹ thuật số và chiếc bình xăng bí mật",
                       3: "Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ranh giới (BPD) & Cơn cuồng nộ ruồng bỏ", 4: "Hồi 4 · Trò ảo thuật phòng thẩm vấn và phiên tòa truyền hình",
                       5: "Hồi 5 · Phán quyết chung thân & 4 cảnh báo đỏ của mối quan hệ ám ảnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Arias", "n1": ("BẠN THÂN MESA", "Đồng nghiệp của Travis", "BẠN THÂN"),
        "n2": ("BỒI THẨM ĐOÀN", "Hạt Maricopa", "BỒI THẨM"),
        "cast": None,
    },
    "16": {
        "script": WORK / "script_tap16.json",
        "dir": "Tap16",
        "plan": "KeHoach_Video_Tap16.md",
        "master": "Tap16_master",
        "srt": "Tap16.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap16.json",
        "sfx_sheet": WORK / "sfx_tap16.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_church_organ.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("ĐƯA LÊN", "THIÊN ĐÀNG"),
        "title": "Kẻ Sát Hại Cả Gia Đình Để 'Đưa Họ Lên Thiên Đàng' (Hồ Sơ John List)",
        "act_titles": {1: "Hồi 1 · Biệt thự u ám Breeze Knoll và khám phá kinh hoàng sau một tháng", 2: "Hồi 2 · Vụ mất tích thế kỷ và chiếc kéo cắt mặt trong album ảnh",
                       3: "Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ám ảnh cưỡng chế (OCPD) & Bẫy ngụy biện đạo đức", 4: "Hồi 4 · Bức tượng sáp của Frank Bender và cú điện thoại từ America's Most Wanted",
                       5: "Hồi 5 · Bài học đắt giá về sự cuồng kiểm soát & 4 cảnh báo đỏ"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "List", "n1": ("JEAN PHILLIPS", "Giáo viên dạy kịch", "GIÁO VIÊN"),
        "n2": ("WANDA FLANERY", "Hàng xóm tại Colorado", "HÀNG XÓM"),
        "cast": None,
    },
    "17": {
        "script": WORK / "script_tap17.json",
        "dir": "Tap17",
        "plan": "KeHoach_Video_Tap17.md",
        "master": "Tap17_master",
        "srt": "Tap17.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap17.json",
        "sfx_sheet": WORK / "sfx_tap17.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NGỤC TÙ", "NGOẠI Ô"),
        "title": "13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Kiểm Soát Cưỡng Chế & Cú Nhảy Sinh Tồn (Hồ Sơ Gia Đình Turpin)",
        "act_titles": {1: "Hồi 1 · Cú nhảy qua cửa sổ rạng sáng và cuộc gọi 911 từ chiếc điện thoại hỏng", 2: "Hồi 2 · Ngục tù ngoại ô và vỏ bọc hoàn hảo của gia đình kiểu mẫu",
                       3: "Hồi 3 · Giải mã tâm lý: Kiểm soát cưỡng chế, ảo tưởng điên cuồng đôi & sự ấu trĩ hóa nạn nhân", 4: "Hồi 4 · Bản cáo trạng rúng động và phiên tòa đối diện công lý",
                       5: "Hồi 5 · Hành trình tái sinh từ tro tàn & 4 cảnh báo đỏ về bạo hành gia đình kín"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Turpin", "n1": ("TRỰC TỔNG ĐÀI 911", "Tổng đài viên Hạt Riverside", "TỔNG ĐÀI"),
        "n2": ("ĐẠI DIỆN Y TẾ", "Bác sĩ Bệnh viện Riverside", "BÁC SĨ"),
        "cast": None,
    },
    "18": {
        "script": WORK / "script_tap18.json",
        "dir": "Tap18",
        "plan": "KeHoach_Video_Tap18.md",
        "master": "Tap18_master",
        "srt": "Tap18.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap18.json",
        "sfx_sheet": WORK / "sfx_tap18.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NGÀY TẬN THẾ", "DOOMSDAY MOM"),
        "title": "Lời Tiên Tri Ngày Tận Thế & Ảo Tưởng Ma Quỷ (Hồ Sơ Lori Vallow & Chad Daybell)",
        "act_titles": {1: "Hồi 1 · Bãi biển Hawaii và bí ẩn hai đứa trẻ biến mất", 2: "Hồi 2 · Mảnh đất nông trại và bí mật dưới lòng đất",
                       3: "Hồi 3 · Giải mã tâm lý: Hoang tưởng tôn giáo chia sẻ & cơ chế phi nhân tính hóa", 4: "Hồi 4 · Bản án trần thế và phán quyết tử hình",
                       5: "Hồi 5 · Nỗi đau đọng lại & 4 cảnh báo đỏ về các hội nhóm cuồng tín"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Vallow", "n1": ("KAY WOODCOCK", "Bà nội của bé JJ", "BÀ NỘI"),
        "n2": ("BỒI THẨM ĐOÀN", "Hạt Ada, Idaho", "BỒI THẨM"),
        "cast": None,
    },
    "19": {
        "script": WORK / "script_tap19.json",
        "dir": "Tap19",
        "plan": "KeHoach_Video_Tap19.md",
        "master": "Tap19_master",
        "srt": "Tap19.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap19.json",
        "sfx_sheet": WORK / "sfx_tap19.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_sub_drone.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("MÀN KỊCH", "CON QUỶ"),
        "title": "Màn Kịch 'Con Quỷ Trong Đầu' — Giả Bệnh Tâm Thần & Sự Thật Trước Máy Quay (Hồ Sơ Nikolas Cruz)",
        "act_titles": {1: "Hồi 1 · Căn phòng hỏi cung và lời nói dối về 'con quỷ'", 2: "Hồi 2 · Chiếc máy quay không chớp mắt và khoảnh khắc chiếc mặt nạ rơi xuống",
                       3: "Hồi 3 · Giải mã tâm lý: Giả bệnh tâm thần (Malingering) vs. Loạn thần thực sự", 4: "Hồi 4 · Bản án 34 án chung thân và sự phán xét của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa bạo lực học đường"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Cruz", "n1": ("HỌC SINH PARKLAND", "Sống sót thảm kịch", "HỌC SINH"),
        "n2": ("BỒI THẨM ĐOÀN", "Hạt Broward, Florida", "BỒI THẨM"),
        "cast": None,
    },
    "20": {
        "script": WORK / "script_tap20.json",
        "dir": "Tap20",
        "plan": "KeHoach_Video_Tap20.md",
        "master": "Tap20_master",
        "srt": "Tap20.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap20.json",
        "sfx_sheet": WORK / "sfx_tap20.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("KHOẢNH KHẮC", "SỤP ĐỔ"),
        "title": "Khoảnh Khắc Sụp Đổ Trước Ống Kính — Ám Ảnh Rình Rập & Phản Ứng Đóng Băng Kỳ Dị (Hồ Sơ Stephen McDaniel)",
        "act_titles": {1: "Hồi 1 · Cuộc phỏng vấn định mệnh & tin báo bất ngờ từ thùng rác", 2: "Hồi 2 · Bức tượng đá trong phòng hỏi cung & cú sốc nhận thức",
                       3: "Hồi 3 · Giải mã tâm lý: Kẻ rình rập ngầm & phản ứng đóng băng kỳ dị", 4: "Hồi 4 · Phán quyết chung thân & sự trừng phạt của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa kẻ rình rập ngầm"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "McDaniel", "n1": ("BẠN HỌC TRƯỜNG LUẬT", "Hàng xóm Barristers Hall", "BẠN HỌC"),
        "n2": ("ĐẠI DIỆN GIA ĐÌNH", "Chị gái của Lauren Giddings", "GIA ĐÌNH"),
        "cast": None,
    },
    "21": {
        "script": WORK / "script_tap21.json",
        "dir": "Tap21",
        "plan": "KeHoach_Video_Tap21.md",
        "master": "Tap21_master",
        "srt": "Tap21.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap21.json",
        "sfx_sheet": WORK / "sfx_tap21.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("LOẠN THẦN", "SAU SINH"),
        "title": "Bi Kịch Của Cơn Loạn Thần Sau Sinh — Khi Ảo Giác Đánh Cắp Thiên Chức Làm Mẹ (Hồ Sơ Andrea Yates)",
        "act_titles": {1: "Hồi 1 · Cuộc gọi 911 rạng sáng & ngôi nhà im lìm tại Houston", 2: "Hồi 2 · Vực thẳm của sự cô độc & tiếng chuông cảnh báo bị phớt lờ",
                       3: "Hồi 3 · Giải mã tâm lý: Loạn thần sau sinh (Psychosis) & hoang tưởng cứu chuộc", 4: "Hồi 4 · Phiên tòa lịch sử & phán quyết Không có tội vì lý do tâm thần",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện Loạn thần sau sinh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Yates", "n1": ("HÀNG XÓM CLEAR LAKE", "Cư dân Houston, Texas", "HÀNG XÓM"),
        "n2": ("BỒI THẨM ĐOÀN", "Tòa án Hạt Harris, Texas", "BỒI THẨM"),
        "cast": None,
    },
    "22": {
        "script": WORK / "script_tap22.json",
        "dir": "Tap22",
        "plan": "KeHoach_Video_Tap22.md",
        "master": "Tap22_master",
        "srt": "Tap22.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap22.json",
        "sfx_sheet": WORK / "sfx_tap22.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NƯỚC MẮT", "CÁ SẤU"),
        "title": "Nước Mắt Cá Sấu Của Kẻ Thuê Sát Thủ Giết Chồng — Thao Túng Trơ Trẽn & Màn Kịch Trước Máy Quay (Hồ Sơ Dalia Dippolito)",
        "act_titles": {1: "Hồi 1 · Màn kịch hiện trường giả & nước mắt người vợ mới cưới", 2: "Hồi 2 · Ván bài lật ngửa & nghệ thuật thao túng trơ trẽn (Gaslighting)",
                       3: "Hồi 3 · Giải mã tâm lý: Sự thao túng trơ trẽn & nhân cách ái kỷ ác tính", 4: "Hồi 4 · Cuộc chiến pháp lý 8 năm & bản án 16 năm tù giam",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện kẻ thao túng trục lợi"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Dippolito", "n1": ("HÀNG XÓM BOYNTON BEACH", "Nhân chứng tại hiện trường", "HÀNG XÓM"),
        "n2": ("BỒI THẨM ĐOÀN", "Tòa án Hạt Palm Beach, Florida", "BỒI THẨM"),
        "cast": None,
    },
    "23": {
        "script": WORK / "script_tap23.json",
        "dir": "Tap23",
        "plan": "KeHoach_Video_Tap23.md",
        "master": "Tap23_master",
        "srt": "Tap23.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap23.json",
        "sfx_sheet": WORK / "sfx_tap23.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NIGHT STALKER", "SAY MÊ KẺ ÁC"),
        "title": "Ám Ảnh 'Night Stalker' & Bí Ẩn Hội Chứng Say Mê Tội Phạm (Hồ Sơ Richard Ramirez)",
        "act_titles": {1: "Hồi 1 · Mùa hè rực lửa 1985 & cơn ác mộng rình rập ban đêm", 2: "Hồi 2 · Phiên tòa cuồng loạn & những người hâm mộ kẻ sát nhân",
                       3: "Hồi 3 · Giải mã tâm lý: Chấn thương não bộ & hội chứng say mê tội phạm (Hybristophilia)", 4: "Hồi 4 · Di sản tư pháp & sự sụp đổ của một ảo tượng",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện hội chứng say mê độc hại"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Ramirez", "n1": ("CƯ DÂN ĐÔNG LOS ANGELES", "Nhân chứng vây bắt năm 1985", "CƯ DÂN"),
        "n2": ("NHÀ BÁO THEO DÕI PHIÊN TÒA", "Tòa Thượng thẩm Los Angeles", "NHÀ BÁO"),
        "cast": None,
    },
    "24": {
        "script": WORK / "script_tap24.json",
        "dir": "Tap24",
        "plan": "KeHoach_Video_Tap24.md",
        "master": "Tap24_master",
        "srt": "Tap24.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap24.json",
        "sfx_sheet": WORK / "sfx_tap24.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("KÝ ỨC", "HWASEONG"),
        "title": "Ký Ức Kẻ Sát Nhân Hwaseong — Sự Thật 33 Năm Dưới Lớp Sương Mù & Lời Thú Tội Muộn Màng (Hồ Sơ Lee Choon-jae)",
        "act_titles": {1: "Hồi 1 · Những cánh đồng đêm Hwaseong & 33 năm trong sương mù", 2: "Hồi 2 · Cuộc đấu trí tại Trại giam Busan & lời tự bạch lạnh gáy",
                       3: "Hồi 3 · Giải mã tâm lý: Kẻ sát nhân kiểm soát quyền lực (Power-Control) & nghịch lý thú tội", 4: "Hồi 4 · Phiên tòa giải oan thế kỷ & lời xin lỗi của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa tội phạm săn mồi ban đêm"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Lee", "n1": ("CƯ DÂN HWASEONG", "Sống trong nỗi sợ hãi thập niên 1980", "CƯ DÂN"),
        "n2": ("NGƯỜI ĐƯỢC MINH OAN", "Nạn nhân án oan 20 năm", "MINH OAN"),
        "cast": None,
    },
    "25": {
        "script": WORK / "script_tap25.json",
        "dir": "Tap25",
        "plan": "KeHoach_Video_Tap25.md",
        "master": "Tap25_master",
        "srt": "Tap25.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap25.json",
        "sfx_sheet": WORK / "sfx_tap25.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("SÁT NHÂN", "ÁO MƯA"),
        "title": "Sát Nhân Áo Mưa & Cơn Cuồng Nộ Thù Hận Xã Hội — Vỏ Bọc Tự Ti & Tội Ác Đội Lốt Phán Xét (Hồ Sơ Yoo Young-chul)",
        "act_titles": {1: "Hồi 1 · Cơn ác mộng áo mưa vàng & Những bóng ma sau cánh cửa biệt thự Seoul", 2: "Hồi 2 · Cuộc đào tẩu chớp nhoáng & Sự trơ tráo sau chiếc mặt nạ phán xét",
                       3: "Hồi 3 · Giải mã tâm lý: Thù hận xã hội (Sociopathic Resentment) & Cơ chế đổ lỗi ngoại hóa", 4: "Hồi 4 · Bản án tử hình & Phán quyết nghiêm minh của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện nhân cách thù hận xã hội"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Yoo", "n1": ("CHỦ CƠ SỞ MASSAGE", "Nhân chứng Mapo năm 2004", "MASSAGE"),
        "n2": ("GIA ĐÌNH NẠN NHÂN", "Con trai nạn nhân Sinsa-dong", "GIA ĐÌNH"),
        "cast": None,
    },
    "26": {
        "script": WORK / "script_tap26.json",
        "dir": "Tap26",
        "plan": "KeHoach_Video_Tap26.md",
        "master": "Tap26_master",
        "srt": "Tap26.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap26.json",
        "sfx_sheet": WORK / "sfx_tap26.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NỮ HỘ SINH", "KOTOBUKI"),
        "title": "Nữ Hộ Sinh Kotobuki & Tội Ác Dưới Lớp Vỏ Bọc Từ Thiện — Sự Suy Đồi Đạo Đức & Bi Kịch Hậu Chiến (Hồ Sơ Miyuki Ishikawa)",
        "act_titles": {1: "Hồi 1 · Đêm đông Tokyo 1948 & Chiếc xe kéo bí ẩn trên phố vắng", 2: "Hồi 2 · Đế chế Kotobuki & Đường dây trục lợi từ nỗi tuyệt vọng",
                       3: "Hồi 3 · Giải mã tâm lý: Sự suy đồi đạo đức & Cơ chế tự biện minh hậu chiến", 4: "Hồi 4 · Bản án trước vành móng ngựa & Bước ngoặt thể chế hậu chiến",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ bảo vệ trẻ em trước các cơ sở trục lợi"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Ishikawa", "n1": ("CẢNH SÁT TUẦN TRA", "Đồn Cảnh sát Waseda năm 1948", "TUẦN TRA"),
        "n2": ("NGƯỜI MẸ NẠN NHÂN", "Nạn nhân Nhà hộ sinh Kotobuki", "NGƯỜI MẸ"),
        "cast": None,
    },
    "27": {
        "script": WORK / "script_tap27.json",
        "dir": "Tap27",
        "plan": "KeHoach_Video_Tap27.md",
        "master": "Tap27_master",
        "srt": "Tap27.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap27.json",
        "sfx_sheet": WORK / "sfx_tap27.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("ÁI KỶ TRẢ THÙ", "BÌNH PHƯỚC"),
        "title": "Tổn Thương Ái Kỷ & Thao Túng Đồng Phạm — Cơn Cuồng Nộ Trả Thù Sau Đổ Vỡ Tình Cảm (Hồ Sơ Nguyễn Hải Dương)",
        "act_titles": {1: "Hồi 1 · Buổi sáng định mệnh tại Minh Hưng & Hiện trường biệt thự đẫm máu", 2: "Hồi 2 · Màn kịch tại đám tang & Cuộc đại phá án thần tốc trong 60 giờ",
                       3: "Hồi 3 · Giải mã tâm lý: Tổn thương ái kỷ (Narcissistic Injury) & Nghệ thuật thao túng đồng phạm", 4: "Hồi 4 · Phiên tòa lưu động tại Bình Phước & Bản án nghiêm khắc của pháp luật",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện kẻ thao túng, thù hận độc hại"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Duong", "n1": ("NGƯỜI LÀM CÔNG XƯỞNG GỖ", "Nhân chứng phát hiện vụ án", "XƯỞNG GỖ"),
        "n2": ("NHÂN CHỨNG PHIÊN TÒA", "Người theo dõi phiên tòa Bình Phước", "NHÂN CHỨNG"),
        "cast": None,
    },
    "28": {
        "script": WORK / "script_tap28.json",
        "dir": "Tap28",
        "plan": "KeHoach_Video_Tap28.md",
        "master": "Tap28_master",
        "srt": "Tap28.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap28.json",
        "sfx_sheet": WORK / "sfx_tap28.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("BI KỊCH", "LÊ VĂN LUYỆN"),
        "title": "Cơn Cuồng Loạn Trong Đêm Mưa Bão & Bi Kịch Vị Thành Niên — Sự Trượt Dài Từ Thế Giới Ảo (Hồ Sơ Lê Văn Luyện)",
        "act_titles": {1: "Hồi 1 · Đêm mưa bão tại Phố Sàn & Tiệm vàng im lìm trong buổi sáng định mệnh", 2: "Hồi 2 · Cuộc đại truy lùng xuyên biên giới & Khoảnh khắc bắt giữ tại Na Hình",
                       3: "Hồi 3 · Giải mã tâm lý: Tội phạm vị thành niên & Hội chứng chuột cùng đường", 4: "Hồi 4 · Phiên tòa lịch sử tại Bắc Giang & Nguyên tắc pháp quyền nhân đạo",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa tội phạm đột nhập ban đêm"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Luyen", "n1": ("NGƯỜI DÂN PHỐ SÀN", "Hàng xóm tiệm vàng Ngọc Bích", "HÀNG XÓM"),
        "n2": ("NHÂN CHỨNG PHIÊN TÒA", "Người theo dõi phiên tòa Bắc Giang", "NHÂN CHỨNG"),
        "cast": None,
    },
    "29": {
        "script": WORK / "script_tap29.json",
        "dir": "Tap29",
        "plan": "KeHoach_Video_Tap29.md",
        "master": "Tap29_master",
        "srt": "Tap29.srt",
        "n_element": {"1.07": "N1", "4.07": "N2"},
        "acting": WORK / "acting_tap29.json",
        "sfx_sheet": WORK / "sfx_tap29.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 2: "bgm_cello_sad.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NỖI SỢ", "BỊ BỎ RƠI"),
        "title": "Sát Nhân Từ Nỗi Sợ Bị Bỏ Rơi Bệnh Lý & Ảo Tưởng Kiểm Soát Tuyệt Đối (Hồ Sơ Jeffrey Dahmer)",
        "act_titles": {1: "Hồi 1 · Căn hộ 213 & Khoảnh khắc người sống sót trốn thoát lúc nửa đêm", 2: "Hồi 2 · Cuộc thẩm vấn 60 giờ & Lời thú tội của kẻ cô đơn cùng cực",
                       3: "Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ranh giới & Ảo tưởng sở hữu", 4: "Hồi 4 · Phiên tòa Milwaukee & Tranh biện: Điên loạn hay Tỉnh táo tàn nhẫn?",
                       5: "Hồi 5 · Bài học cảnh tỉnh xã hội & 4 cảnh báo đỏ nhận diện kẻ săn mồi"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Dahmer", "n1": ("TRACY EDWARDS", "Người trốn thoát khỏi căn hộ 213", "EDWARDS"),
        "n2": ("THÂN NHÂN NẠN NHÂN", "Đại diện thân nhân tại tòa Milwaukee", "THÂN NHÂN"),
        "cast": None,
    },
}
if EPN not in EPISODES:
    raise SystemExit(f"Chưa khai báo tập {EPN} trong edition.EPISODES")
EP = EPISODES[EPN]

# ---------------------------------------------------------------- bản tiếng Hàn (KO) & Nhật (JA)
# Kịch bản KO: 01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md  (chuẩn: 00_TIEU_CHUAN/CHU_CO_DINH_KO.md)
# Kịch bản JA: 01_KICH_BAN/TapXX_JA/kichban_tapXX_JA.md  (chuẩn: 00_TIEU_CHUAN/CHU_CO_DINH_JA.md)
# Cùng mã câu với bản VN nên dùng chung được acting_tapXX.json / shots.json / sfx_tapXX.json.
KO_SRC = ROOT / "01_KICH_BAN" / f"Tap{EPN}_KO" / f"kichban_tap{EPN}_KO.md"
JA_SRC = ROOT / "01_KICH_BAN" / f"Tap{EPN}_JA" / f"kichban_tap{EPN}_JA.md"
if KO:
    EP = dict(EP)
    EP["script"] = WORK / f"script_tap{EPN}_KO.json"
    EP["dir"] = f"Tap{EPN}_KO"
    EP["plan"] = f"KeHoach_Video_Tap{EPN}_KO.md"
    EP["master"] = f"Tap{EPN}_KO_master"
    EP["srt"] = f"Tap{EPN}_KO.srt"
    EP["acting"] = WORK / f"acting_tap{EPN}_KO.json"
    EP["intro"] = f"intro_kenh_KO_t{EPN}.mov"
    if not KO_SRC.exists():
        raise SystemExit(f"Chưa có kịch bản tiếng Hàn: {KO_SRC}")
if JA:
    EP = dict(EP)
    EP["script"] = WORK / f"script_tap{EPN}_JA.json"
    EP["dir"] = f"Tap{EPN}_JA"
    EP["plan"] = f"KeHoach_Video_Tap{EPN}_JA.md"
    EP["master"] = f"Tap{EPN}_JA_master"
    EP["srt"] = f"Tap{EPN}_JA.srt"
    EP["acting"] = WORK / f"acting_tap{EPN}_JA.json"
    EP["intro"] = f"intro_kenh_JA_t{EPN}.mov"
    if not JA_SRC.exists():
        raise SystemExit(f"Chưa có kịch bản tiếng Nhật: {JA_SRC}")

SCRIPT_JSON = EP["script"]
EP_DIR = ROOT / "02_SAN_XUAT" / EP["dir"]
OUT_DIR = EP_DIR / "xuat_ban"
PLAN = EP_DIR / EP["plan"]
MASTER = EP["master"]
SRT = EP["srt"]
N_ELEMENT = EP["n_element"]
ACTING = EP["acting"]
INTRO_MOV = ROOT / "assets" / "brand" / EP.get("intro", "intro_kenh.mov")

# ---------------------------------------------------------------- on-screen strings
TAGLINE = ("Criminal psychology through real case files" if EN else
           "実際の事件記録から読み解く犯罪心理学" if JA else
           " 범죄심리학 — 실사 사건 기록으로 읽는 인간 심리" if KO else
           "Phân tích tâm lý tội phạm qua những hồ sơ có thật")
ROLE_NAME = ((EP.get("roles_en") or
              {"H": ("HOST", "Your narrator"), "D": ("INVESTIGATOR", "Blanchard case file"),
               "C": ("PSYCHOLOGIST", "Criminal psychology"),
               "N1": ("SPRINGFIELD RESIDENT", "Longtime neighbor"), "N2": ("VIEWER", "Following the case")})
             if EN else
             {"H": ("ホスト", "ストーリーテラー"), "D": ("捜査官", f"事件記録 {EP['case']}"),
              "C": ("心理学者", "犯罪心理学"),
              "N1": ("証人", "当事者"), "N2": ("視聴者", "事件を見守る人")} if JA else
             {"H": ("호스트", "내레이터"), "D": ("수사관", f"사건 기록 {EP['case']}"),
              "C": ("심리학자", "범죄심리학"),
              "N1": ("증인", "당사자"), "N2": ("시청자", "사건을 지켜본 사람")} if KO else
             {"H": ("HOST", "Người dẫn chuyện"), "D": ("ĐIỀU TRA VIÊN", f"Hồ sơ vụ án {EP['case']}"),
              "C": ("CHUYÊN GIA TÂM LÝ", "Tâm lý học tội phạm"),
              "N1": EP["n1"][:2], "N2": EP["n2"][:2]})
SUB_TAG = ((EP.get("sub_tags_en") or
            {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST", "N1": "RESIDENT", "N2": "VIEWER"}) if EN else
           {"H": "ホスト", "D": "捜査官", "C": "心理学者", "N1": "証人", "N2": "視聴者"} if JA else
           {"H": "호스트", "D": "수사관", "C": "심리학자", "N1": "증인", "N2": "시청자"} if KO else
           {"H": "HOST", "D": "ĐIỀU TRA VIÊN", "C": "CHUYÊN GIA TÂM LÝ", "N1": EP["n1"][2], "N2": EP["n2"][2]})
UI = ({"next": "NEXT", "illus": "ILLUSTRATION", "intro_line": "Fictional character · AI voice · Dramatized",
       "stamp_forged": "FORGED", "stamp_secret": "CONFIDENTIAL"} if EN else
      {"next": "次へ", "illus": "イメージ", "intro_line": "架空のキャラクター · AI音声 · 演出",
       "stamp_forged": "偽造", "stamp_secret": "機密"} if JA else
      {"next": "다음", "illus": "모식화", "intro_line": "가상 인물 · AI 음성 · 각색",
       "stamp_forged": "위조", "stamp_secret": "기밀"} if KO else
      {"next": "TIẾP THEO", "illus": "MINH HOẠ", "intro_line": "Nhân vật minh hoạ · giọng đọc AI",
       "stamp_forged": "GIẢ MẠO", "stamp_secret": "MẬT"})

# intro disclaimer cards: (title, [[(text, highlighted)]])
if EN and EP.get("cards_en"):
    CARD_A, CARD_B = EP["cards_en"]
else:
    CARD_A = (("ABOUT THIS VIDEO", [
        [("Educational", 1), (" content: an analysis of criminal psychology.", 0)],
        [("Based on ", 0), ("public records", 1), ("; sources are in the description.", 0)],
        [("Not intended to accuse or defame anyone.", 0)]]) if EN else
        ("본 콘텐츠에 대하여", [
        [("본 영상은 ", 0), ("교육 목적", 1), ("의 범죄심리학 분석 콘텐츠입니다.", 0)],
        [("공개된 공식 기록", 1), ("을 기반으로 제작되었으며, 출처는 설명란에 기재되어 있습니다.", 0)],
        [("특정인을 비방하거나 단죄하려는 의도가 없습니다.", 0)]]) if KO else
        ("この動画について", [
        [("本動画は", 0), ("教育目的", 1), ("の犯罪心理学分析コンテンツです。", 0)],
        [("公開記録", 1), ("に基づいており、出典は概要欄に記載されています。", 0)],
        [("特定の個人を非難または中傷する意図はありません。", 0)]]) if JA else
        ("VỀ NỘI DUNG NÀY", [
        [("Nội dung ", 0), ("giáo dục", 1), (", phân tích tâm lý học tội phạm.", 0)],
        [("Dựa trên ", 0), ("tư liệu công khai", 1), (", nguồn ở phần mô tả.", 0)],
        [("Không nhằm kết tội hay bôi nhọ bất kỳ ai.", 0)]]))
    CARD_B = (("BEFORE YOU WATCH", [
        [("Not suitable for children", 1), (".", 0)],
        [("Sounds and images are ", 0), ("for illustration only", 1), (".", 0)],
        [("Not a substitute for medical, psychological or legal advice.", 0)]]) if EN else
        ("시청 전 유의사항", [
        [("청소년에게 적합하지 않을 수 있습니다", 1), (".", 0)],
        [("음향 및 시각 자료는 ", 0), ("이해를 돕기 위한 연출", 1), ("입니다.", 0)],
        [("본 내용은 의학적, 심리학적 또는 법률적 조언을 대신할 수 없습니다.", 0)]]) if KO else
        ("ご視聴前の注意", [
        [("お子様向けではありません", 1), ("。", 0)],
        [("音声および画像は", 0), ("イメージ", 1), ("です。", 0)],
        [("医学的、心理学的、または法的なアドバイスに代わるものではありません。", 0)]]) if JA else
        ("LƯU Ý TRƯỚC KHI XEM", [
        [("Nội dung ", 0), ("không phù hợp cho trẻ em", 1), (".", 0)],
        [("Âm thanh và hình ảnh ", 0), ("chỉ mang tính minh hoạ", 1), (".", 0)],
        [("Không thay thế tư vấn y khoa, tâm lý hay pháp lý.", 0)]]))

# ---------------------------------------------------------------- TTS cast (voice_id, base speed)
# Bản EN: `English_Deep-VoicedGentleman` (vai D của Tập 01 EN) bị đổi màu khi đổi cảm xúc
# (G10 23/10: "Investigator -> 3 người"; thí nghiệm .work/_voice_band_test.py cho thấy
# tốc độ đọc KHÔNG làm đổi người, chỉ CẢM XÚC mới đổi — với vai D của Tập 02 có cảm xúc
# sad/fearful ở các câu then chốt). `English_Trustworth_Man` giữ nguyên 1 người ở cả 4
# cảm xúc (SPEAKERS: 1) và vẫn tách bạch với Host · Chuyên gia.
CAST = ({"H": ("English_magnetic_voiced_man", 0.95), "D": ("English_Trustworth_Man", 0.97),
         "C": ("English_Wiselady", 0.95), "N1": ("English_SentimentalLady", 0.95),
         "N2": ("English_captivating_female1", 0.95)} if EN else
        # BẢN TIẾNG NHẬT (JA): 5 giọng chuẩn qua thử nghiệm ASR CER 0% & F0 phân tách rõ
        {"H": ("Japanese_GentleButler", 0.95), "D": ("Japanese_SeriousCommander", 0.97),
         "C": ("Japanese_DependableWoman", 0.95), "N1": ("Japanese_KindLady", 0.95),
         "N2": ("Japanese_DecisivePrincess", 0.95)} if JA else
        # BẢN TIẾNG HÀN: chưa có bộ giọng đã qua G8–G10 (cần thử giọng tiếng Hàn thật).
        # Không dùng nhầm bộ giọng VN/EN — sẽ ra giọng đọc sai ngôn ngữ.
        {"H": ("Korean_CalmGentleman", 0.95), "D": ("Korean_ColdYoungMan", 0.95),
         "C": ("Korean_DecisiveQueen", 0.92), "N1": ("Korean_GentleWoman", 0.95),
         "N2": ("Korean_SweetGirl", 0.95)} if KO else
        # BỘ A (chốt 23/10/2026, BaoCao_GiongDoc_Tap02.md §4): ổn định danh tính khi đổi cảm xúc, 3 vai tách bạch
        {"H": ("English_CaptivatingStoryteller", 0.90), "D": ("Korean_ColdYoungMan", 0.95),
         "C": ("English_AssertiveQueen", 0.92), "N1": ("Vietnamese_kindhearted_girl", 0.95),
         "N2": ("English_captivating_female1", 0.95)})
if EP["cast"]:
    CAST = {**CAST, **EP["cast"]}
if KO and not EP.get("cast_ko"):
    raise SystemExit(
        "Bản tiếng Hàn chưa có bộ giọng đã qua G8–G10.\n"
        "  1) thử giọng: py -3 .work/voice_audition.py (chọn giọng tiếng Hàn)\n"
        "  2) khai 'cast_ko' trong EPISODES của edition.py cho tập này\n"
        "  3) chạy G10: py -3 .work/voice_role_check.py\n"
        "Kịch bản tiếng Hàn đã sẵn sàng ở 01_KICH_BAN/Tap%s_KO/ — chỉ thiếu bước chọn giọng." % EPN)

# TTS-only spelling for sentences the voice would read the wrong way (screen text unchanged)
TTS_FIX = (EP.get("tts_fix", {}) if EN else {})

# Bản EN dùng lại diễn xuất của bản VN (cùng mã câu): manifest VN của chính tập đó
# + tốc độ gốc của bộ giọng VN để tự tính lệch tốc độ. Bản KO dùng chung mã câu với VN.
VN_MANIFEST = (WORK / (f"tts_manifest_t{EPN}.json" if EPN != "01" else "tts_manifest.json")) if (EN or KO or JA) else None
VN_CAST_BASE = {"H": 0.90, "D": 0.95, "C": 0.92, "N1": 0.95, "N2": 0.95}
