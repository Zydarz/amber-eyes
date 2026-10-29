# -*- coding: utf-8 -*-
with open(r'd:\TEST\Gax\Audi\.work\edition.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        # package
        "thumb": ("POISON IN THE NAME", "OF A MOTHER’S LOVE") if EN else ("母の愛という名の", "毒薬") if JA else ("ĐỘC DƯỢC", "NHÂN DANH TÌNH MẸ"),
        "title": ("The Blanchard Case: Deciphering Munchausen Syndrome by Proxy | Amber eyes" if EN else
                  "母の愛という名の毒薬――代理型ミュンハウゼン症候群を解読（Blanchard事件） | Amber eyes" if JA else
                  "Độc Dược Nhân Danh Tình Mẹ — Giải mã Hội chứng Münchausen qua trung gian"),
        "act_titles": ({1: "Act 1 · The Moment Trust Broke", 2: "Act 2 · 23 Years in a Medical Prison",
                        3: "Act 3 · Inside the Mind of an FDIA Perpetrator", 4: "Act 4 · Why Didn't Gypsy Walk Away?",
                        5: "Act 5 · Forensic Verdict & Epilogue"} if EN else
                       {1: "第1幕 · 信頼が崩れる瞬間", 2: "第2幕 · 精神刑務所での23年間",
                        3: "第3幕 · FDIA犯罪者の脳の内部", 4: "第4幕 · なぜGypsyは逃げなかったのか？",
                        5: "第5幕 · 司法の裁き、レッドフラッグ＆教訓"} if JA else
                       {1: "Hồi 1 · Khoảnh khắc đứt gãy niềm tin", 2: "Hồi 2 · 23 năm trong nhà tù y khoa",
                        3: "Hồi 3 · Bên trong bộ não của kẻ mắc FDIA", 4: "Hồi 4 · Tại sao Gypsy không đứng dậy?",
                        5: "Hồi 5 · Phán quyết pháp y & lời kết"}),
        "summary": ("1.13#2", "3.02#5"),
        "need": ["4.15#2", "5.02#3", "5.04#2", "2.07#10", "3.05#5", "3.07#2", "4.07#8", "4.10#5"],
        "case": "Blanchard", "n1": (("SPRINGFIELD RESIDENT", "Longtime neighbor", "SPRINGFIELD RESIDENT") if EN else
                                    ("スプリングフィールド住民", "長年の隣人", "証人") if JA else
                                    ("NGƯỜI DÂN SPRINGFIELD", "Hàng xóm nhiều năm", "NGƯỜI DÂN")),
        "n2": (("VIEWER", "Following the case", "VIEWER") if EN else
               ("視聴者", "事件を見守る人", "視聴者") if JA else
               ("KHÁN GIẢ", "Theo dõi vụ án", "KHÁN GIẢ")),
        "cast": None if (EN or JA) else {"H": ("audiobook_male_1", 0.90), "D": ("male-qn-qingse", 0.95), "C": ("audiobook_female_1", 0.92)},   # giữ giọng Tập 01 đã xuất'''

replacement = '''        # package
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
        "cast_ko": True,'''

if target in content:
    content = content.replace(target, replacement, 1)
    print("Replaced target 1")
else:
    print("Target 1 NOT found")

target2 = '''        {"H": ("Korean_Storyteller_M", 0.92), "D": ("Korean_ColdYoungMan", 0.95),
         "C": ("Korean_ProfessionalWoman", 0.92), "N1": ("Korean_EmotionGirl", 0.95),
         "N2": ("Korean_CaptivatingFemale", 0.95)} if KO else'''

replacement2 = '''        {"H": ("Korean_CalmGentleman", 0.95), "D": ("Korean_ColdYoungMan", 0.95),
         "C": ("Korean_DecisiveQueen", 0.92), "N1": ("Korean_GentleWoman", 0.95),
         "N2": ("Korean_SweetGirl", 0.95)} if KO else'''

if target2 in content:
    content = content.replace(target2, replacement2, 1)
    print("Replaced target 2")
else:
    print("Target 2 NOT found")

with open(r'd:\TEST\Gax\Audi\.work\edition.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved edition.py")
