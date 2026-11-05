#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update edition.py titles and act_titles for Episode 04 cleanly preserving newlines."""
import py_compile
import sys

def main():
    with open('.work/edition.py', 'r', encoding='utf-8', newline='') as f:
        content = f.read()

    # We determine newline style
    nl = '\r\n' if '\r\n' in content else '\n'

    old_block = nl.join([
        '        "title": ("Ep. 04: The Angel of Death | The Psychology of Charles Cullen (God Complex)" if EN else',
        '                  "第04話 · 死の天使と神のコンプレックス――9つの病院を巡った16年の沈黙の裏にある秘密 | チャールズ・カレンの心理学" if JA else',
        '                  "Tập 04: Thiên Thần Tử Thần | Tâm lý học tội phạm: Charles Cullen (Phức cảm Chúa trời)"),',
        '        "act_titles": ({1: "Act 1 · The Paradox of the Model Nurse",',
        '                        2: "Act 2 · The Deadly Loophole of the Dispensing Machine",',
        '                        3: "Act 3 · Inside the Mind of the Covert God Complex",',
        '                        4: "Act 4 · Interrogation & The Turning Point",',
        '                        5: "Act 5 · The Verdict, Red Flags & Epilogue"} if EN else',
        '                       {1: "第1幕 · つかみ――模範の看護師の逆説",',
        '                        2: "第2幕 · 歪んだ心理のプロファイル――神のコンプレックスと無力感の補償",',
        '                        3: "第3幕 · 道徳的無効化と被害者の人間性の剥奪",',
        '                        4: "第4幕 · 捜査官の心理戦と潜入看護師の勇気",',
        '                        5: "第5幕 · 終幕――法廷、制度的沈黙への警鐘、そして終幕"} if JA else',
        '                       {1: "Hồi 1 · Nghịch lý của người y tá mẫu mực", 2: "Hồi 2 · Lỗ hổng chết người của máy phát thuốc",',
        '                        3: "Hồi 3 · Bên trong bộ não của kẻ mang Phức cảm Chúa trời", 4: "Hồi 4 · Đấu trí thẩm vấn và bước ngoặt điều tra",',
        '                        5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ và lời kết"}),'
    ])

    new_block = nl.join([
        '        "title": ("Ep. 04: The Angel of Death & The God Complex | Criminal Psychology: Charles Cullen" if EN else',
        '                  "第04話 · 死の天使と神コンプレックス | 犯罪心理学：チャールズ・カレン事件" if JA else',
        '                  "04화 · 죽음의 천사와 신 콤플렉스 | 범죄심리학: 찰스 컬런 사건" if KO else',
        '                  "Tập 04: Thiên Thần Tử Thần & Phức Cảm Chúa Trời | Tâm lý học tội phạm: Charles Cullen (Phức cảm Chúa trời)"),',
        '        "act_titles": ({1: "Act 1 · The Paradox of the Model Nurse",',
        '                        2: "Act 2 · The Crime Scene – The Escalation Trajectory of the Abyss",',
        '                        3: "Act 3 · Psychological Autopsy – Inside the Brain of the God Complex",',
        '                        4: "Act 4 · The Interrogation & The Breakthrough",',
        '                        5: "Act 5 · The Verdict, Survival Red Flags & Epilogue"} if EN else',
        '                       {1: "第1幕 · 模範的看護師のパラドックス",',
        '                        2: "第2幕 · 犯行現場――深淵のエスカレーション軌道",',
        '                        3: "第3幕 · 心理解剖――神コンプレックスの脳内",',
        '                        4: "第4幕 · 取調の攻防――捜査の重大な転換点",',
        '                        5: "第5幕 · 判決、生存への警告と結び"} if JA else',
        '                       {1: "제1막 · 모범 간호사의 역설",',
        '                        2: "제2막 · 범죄 현장 – 심연의 에스컬레이션 궤적",',
        '                        3: "제3막 · 심리 부검 – 신 콤플렉스의 뇌 속으로",',
        '                        4: "제4막 · 심문실의 공방 – 수사의 결정적 돌파구",',
        '                        5: "제5막 · 판결, 생존을 위한 경고와 맺음말"} if KO else',
        '                       {1: "Hồi 1 · Nghịch lý của người y tá mẫu mực",',
        '                        2: "Hồi 2 · Hiện trường & Hồ sơ tội ác – Quỹ đạo leo thang của vực thẳm",',
        '                        3: "Hồi 3 · Giải phẫu tâm lý – Bên trong bộ não của kẻ mang Phức cảm Chúa trời",',
        '                        4: "Hồi 4 · Đấu trí thẩm vấn & Bước ngoặt điều tra",',
        '                        5: "Hồi 5 · Phán quyết, Bài học cảnh báo đỏ & Lời kết"}),'
    ])

    if old_block not in content:
        print("ERROR: old_block not found in content!")
        sys.exit(1)

    content = content.replace(old_block, new_block, 1)

    # Add cast_ko
    old_cast = nl.join([
        '        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",',
        '                        "N1": "SOMERSET NURSE", "N2": "AMY LOUGHREN"},',
        '        "cast": None,'
    ])
    new_cast = nl.join([
        '        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",',
        '                        "N1": "SOMERSET NURSE", "N2": "AMY LOUGHREN"},',
        '        "cast": None,',
        '        "cast_ko": True,'
    ])

    if old_cast in content:
        content = content.replace(old_cast, new_cast, 1)
        print("Added cast_ko to EPISODES 04")
    else:
        print("Note: old_cast not found, cast_ko might already be present.")

    with open('.work/edition.py', 'w', encoding='utf-8', newline='') as f:
        f.write(content)

    py_compile.compile('.work/edition.py', doraise=True)
    print("SUCCESS: Updated and compiled .work/edition.py")

if __name__ == '__main__':
    main()
