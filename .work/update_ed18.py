import pathlib

ed_path = pathlib.Path('.work/edition.py')
text = ed_path.read_text(encoding='utf-8')

backup_path = pathlib.Path('.work/_cu/edition.py.bak_t18_update')
backup_path.parent.mkdir(parents=True, exist_ok=True)
backup_path.write_text(text, encoding='utf-8')

old_part = '''    "18": {
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
    },'''

new_part = '''    "18": {
        "script": WORK / ("script_tap18_EN.json" if EN else "script_tap18_JA.json" if JA else "script_tap18_KO.json" if KO else "script_tap18.json"),
        "dir": "Tap18_EN" if EN else "Tap18_JA" if JA else "Tap18_KO" if KO else "Tap18",
        "plan": "KeHoach_Video_Tap18_EN.md" if EN else "KeHoach_Video_Tap18_JA.md" if JA else "KeHoach_Video_Tap18_KO.md" if KO else "KeHoach_Video_Tap18.md",
        "master": "Tap18_EN_master" if EN else "Tap18_JA_master" if JA else "Tap18_KO_master" if KO else "Tap18_master",
        "srt": "Tap18_EN.srt" if EN else "Tap18_JA.srt" if JA else "Tap18_KO.srt" if KO else "Tap18.srt",
        "intro": "intro_kenh_EN_t18.mov" if EN else "intro_kenh_JA_t18.mov" if JA else "intro_kenh_KO_t18.mov" if KO else "intro_kenh.mov",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / ("acting_tap18_EN.json" if EN else "acting_tap18_JA.json" if JA else "acting_tap18_KO.json" if KO else "acting_tap18.json"),
        "sfx_sheet": WORK / ("sfx_tap18_EN.json" if (EN and (WORK / "sfx_tap18_EN.json").exists()) else "sfx_tap18_JA.json" if (JA and (WORK / "sfx_tap18_JA.json").exists()) else "sfx_tap18.json"),
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("DOOMSDAY MOM", "CULT OF DEATH") if EN else ("終末の預言", "カルトの狂気") if JA else ("종말의 예언", "사이비의 광기") if KO else ("NGÀY TẬN THẾ", "DOOMSDAY MOM"),
        "title": ("Ep. 18: Doomsday Prophecy & Demonic Delusions | Criminal Psychology: Lori Vallow & Chad Daybell (Folie à Deux & 10 Psychological Markers)" if EN else
                  "第18話：終末の予言と悪魔の妄想 — 共有精神病と2人の子どもの悲劇（ロリ・ヴァロウ＆チャド・デイベル事件）" if JA else
                  "18화: 종말의 예언과 악마의 망상 — 공유정신병과 두 아이의 비극 (로리 밸로우 & 채드 데이벨 사건)" if KO else
                  "Lời Tiên Tri Ngày Tận Thế & Ảo Tưởng Ma Quỷ (Hồ Sơ Lori Vallow & Chad Daybell)"),
        "act_titles": ({1: "Act 1 · The Hawaii Beach and the Mystery of Two Missing Children", 2: "Act 2 · The Pet Cemetery and the Secrets Beneath the Earth",
                        3: "Act 3 · Psychological Decoding: Shared Delusional Disorder & Dehumanization", 4: "Act 4 · Earthly Justice and the Death Penalty Verdict",
                        5: "Act 5 · Lingering Pain & 4 Red Flags of Cultic Extremism"} if EN else
                       {1: "第1幕 · ハワイのビーチと消えた2人の子どもの謎", 2: "第2幕 · 農場の片隅と地下に眠る戦慄の秘密",
                        3: "第3幕 · 心理分析：共有精神病（フォリ・ア・ドゥ）と非人間化の罠", 4: "第4幕 · 現世の裁きと下された死刑判決",
                        5: "第5幕 · 残された痛みとカルト・狂信的集団を見抜く4つの危険信号"} if JA else
                       {1: "제1막 · 하와이 해변과 사라진 두 아이의 미스터리", 2: "제2막 · 농장 땅속에 묻힌 참혹한 진실",
                        3: "제3막 · 심리 해체: 공유정신병(Folie à Deux)과 비인간화 메커니즘", 4: "제4막 · 지상의 심판과 선고된 사형 판결",
                        5: "제5막 · 남겨진 고통과 사이비 광신 집단의 4가지 위험 신호"} if KO else
                       {1: "Hồi 1 · Bãi biển Hawaii và bí ẩn hai đứa trẻ biến mất", 2: "Hồi 2 · Mảnh đất nông trại và bí mật dưới lòng đất",
                        3: "Hồi 3 · Giải mã tâm lý: Hoang tưởng tôn giáo chia sẻ & cơ chế phi nhân tính hóa", 4: "Hồi 4 · Bản án trần thế và phán quyết tử hình",
                        5: "Hồi 5 · Nỗi đau đọng lại & 4 cảnh báo đỏ về các hội nhóm cuồng tín"}),
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Vallow", "n1": (("KAY WOODCOCK", "JJ's Grandmother", "GRANDMOTHER") if EN else
                                ("ケイ・ウッドコック", "JJの祖母", "祖母") if JA else
                                ("케이 우드콕", "JJ의 할머니", "할머니") if KO else
                                ("KAY WOODCOCK", "Bà nội của bé JJ", "BÀ NỘI")),
        "n2": (("ADA COUNTY JURY", "Ada County Jury Representative", "JURY") if EN else
                ("エイダ郡陪審員", "エイダ郡陪審員代表", "陪審員") if JA else
                ("에이다 카운티 배심원", "배심원 대표", "배심원") if KO else
                ("BỒI THẨM ĐOÀN", "Hạt Ada, Idaho", "BỒI THẨM")),
        "cast": None,
    },'''

assert old_part in text, "old_part not found!"
text = text.replace(old_part, new_part)
ed_path.write_text(text, encoding="utf-8")
print("Updated edition.py successfully!")
