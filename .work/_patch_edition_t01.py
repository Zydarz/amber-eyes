# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

path = Path(".work/edition.py")
content = path.read_text(encoding="utf-8")

old_block = """        "title": ("Ep. 01: Poison Disguised as Mother’s Love | The Psychology of Gypsy Rose Blanchard (FDIA)" if EN else
                  "第01話 · 母の愛という名の毒薬 | Gypsy Rose Blanchardの心理学 (FDIA)" if JA else
                  "01화 · 엄마의 사랑이라는 이름의 독약 | Gypsy Rose Blanchard의 심리학 (FDIA)" if KO else
                  "Tập 01: Độc Dược Nhân Danh Tình Mẹ | Tâm lý học tội phạm: Gypsy Rose Blanchard (FDIA)"),
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
        # Hashtag dòng cuối mô tả YouTube (bản tiếng Việt). Bản EN có sẵn trong
        # CHU_CO_DINH_EN.md; bản JA/KO chưa có dòng hashtag.
        "hashtags": "#TrueCrime #CriminalPsychology #MunchausenSyndrome #GypsyRoseBlanchard #FDIA #ForensicPsychology #Documentary #AmberEyes #TamLyToiPham #PhamVan #HoiTo",
        "summary": ("1.13#2", "3.02#5"),
        "need": ["4.15#2", "5.02#3", "5.04#2", "2.07#10", "3.05#5", "3.07#2", "4.07#8", "4.10#5"],"""

new_block = """        "title": ("Ep. 01: Poison in the Name of Mother’s Love | Criminal Psychology: Gypsy Rose & Dee Dee Blanchard (FDIA & 10 Behavioral Markers)" if EN else
                  "第01話 · 母の愛という名の毒薬 | 犯罪心理学：ジプシー・ローズ＆ディー・ディー・ブランチャード（代理型ミュンハウゼン症候群＆10の心理指標）" if JA else
                  "01화 · 모성이라는 이름의 독약 | 범죄심리학: 집시 로즈 & 디디 블랜차드 (대리인에 의한 뮌하우젠 증후군 & 10가지 심리 지표)" if KO else
                  "Tập 01: Độc Dược Nhân Danh Tình Mẹ | Tâm lý học tội phạm: Gypsy Rose Blanchard (FDIA & 10 Chỉ Dấu Tâm Lý)"),
        "act_titles": ({1: "Act 1 · The Moment Trust Broke & Social Blind Spots", 2: "Act 2 · Crime Scene & The Escalating Medical Abyss",
                        3: "Act 3 · Psychological Autopsy — Inside the Mind of FDIA", 4: "Act 4 · The Victim's Perspective — Why Couldn't Gypsy Just Stand Up?",
                        5: "Act 5 · Forensic Verdict, Psychological Judgment & Survival Red Flags"} if EN else
                       {1: "第1幕 · 信頼が崩れる瞬間＆社会の盲点", 2: "第2幕 · 犯罪現場＆医療の深淵へのエスカレーション",
                        3: "第3幕 · 心理剖検――FDIA犯罪者の脳の内部", 4: "第4幕 · 被害者の視点――ジプシーはなぜ立ち上がれなかったのか？",
                        5: "第5幕 · 法医学的判定、心理の審判＆生存のための赤い警告"} if JA else
                       {1: "제1막 · 무너진 신뢰의 순간 & 사회적 맹점", 2: "제2막 · 범죄 현장 & 의료 심연으로의 에스컬레이션",
                        3: "제3막 · 심리 부검――FDIA 범죄자의 뇌 속으로", 4: "제4막 · 피해자의 시선――집시는 왜 일어서지 못했는가?",
                        5: "제5막 · 법의학적 판결, 심리적 심판 & 생존을 위한 위험 신호"} if KO else
                       {1: "Hồi 1 · Khoảnh khắc đứt gãy niềm tin & Điểm mù xã hội", 2: "Hồi 2 · Hiện trường & Quỹ đạo leo thang của vực thẳm y tế",
                        3: "Hồi 3 · Giải phẫu tâm lý — Bên trong bộ não kẻ mắc FDIA", 4: "Hồi 4 · Góc nhìn nạn nhân — Tại sao Gypsy không đứng dậy?",
                        5: "Hồi 5 · Phán quyết pháp y, bản án tâm lý & Cảnh báo đỏ sinh tồn"}),
        # Hashtag dòng cuối mô tả YouTube (bản tiếng Việt). Bản EN có sẵn trong
        # CHU_CO_DINH_EN.md; bản JA/KO chưa có dòng hashtag.
        "hashtags": "#TrueCrime #CriminalPsychology #MunchausenSyndrome #GypsyRoseBlanchard #FDIA #ForensicPsychology #Documentary #AmberEyes #TamLyToiPham #PhamVan #HoiTo",
        "summary": ("1.13#2", "3.02#5"),
        "need": ["5.02#3", "5.04#2", "2.07#10", "3.07#2", "4.07#8", "4.10#5"],"""

c_norm = content.replace("\r\n", "\n")
o_norm = old_block.replace("\r\n", "\n")
n_norm = new_block.replace("\r\n", "\n")

if o_norm in c_norm:
    updated = c_norm.replace(o_norm, n_norm)
    path.write_text(updated, encoding="utf-8")
    print("SUCCESS: Updated edition.py for Episode 01!")
else:
    print("ERROR: old_block not found in edition.py")
