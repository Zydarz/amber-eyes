import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ED_PATH = ROOT / ".work" / "edition.py"

txt = ED_PATH.read_text(encoding="utf-8")

old_thumb = '"thumb": ("THE TWO-FACED", "COLONEL") if EN else ("ĐẠI TÁ", "HAI MẶT"),'
new_thumb = '"thumb": ("THE TWO-FACED", "COLONEL") if EN else ("二重生活の", "大佐") if JA else ("ĐẠI TÁ", "HAI MẶT"),'
assert old_thumb in txt, "old_thumb not found"
txt = txt.replace(old_thumb, new_thumb, 1)

old_title = '''        "title": ("The Double Life of Colonel Russell Williams: Behavioral Escalation & "
                  "The Psychology of a Predator | Amber eyes" if EN else
                  "Đại Tá Hai Mặt — Quy luật leo thang hành vi & sự phân mảnh tâm trí (vụ Russell Williams)"),'''
new_title = '''        "title": ("The Double Life of Colonel Russell Williams: Behavioral Escalation & "
                  "The Psychology of a Predator | Amber eyes" if EN else
                  "ラッセル・ウィリアムズ大佐の二重生活――行動のエスカレーションと捕食者の心理学 | Amber eyes" if JA else
                  "Đại Tá Hai Mặt — Quy luật leo thang hành vi & sự phân mảnh tâm trí (vụ Russell Williams)"),'''
assert old_title in txt, "old_title not found"
txt = txt.replace(old_title, new_title, 1)

old_act = '''        "act_titles": ({1: "Act 1 · The Extreme Contrast Behind a Colonel’s Rank",
                        2: "Act 2 · The Scene & Dossier — The 4 Stages of the Abyss",
                        3: "Act 3 · Psychological Autopsy — Inside the Mind of a Two-Faced Predator",
                        4: "Act 4 · The Interrogation Room — Breaking a Military Mind",
                        5: "Act 5 · The Verdict, Red Flags & Closing Thoughts"} if EN else
                       {1: "Hồi 1 · Sự tương phản phía sau quân hàm đại tá", 2: "Hồi 2 · 4 bậc thang của vực thẳm",
                        3: "Hồi 3 · Bên trong bộ não của sát nhân hai mặt", 4: "Hồi 4 · Nghệ thuật bẻ gãy bộ óc quân sự",
                        5: "Hồi 5 · Phán quyết, cảnh báo đỏ & lời kết"}),'''
new_act = '''        "act_titles": ({1: "Act 1 · The Extreme Contrast Behind a Colonel’s Rank",
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
                        5: "Hồi 5 · Phán quyết, cảnh báo đỏ & lời kết"}),'''
assert old_act in txt, "old_act not found"
txt = txt.replace(old_act, new_act, 1)

old_n = '''        "n1": (("BASE PERSONNEL", "Military Community Perspective", "BASE PERSONNEL") if EN else
               ("BINH SĨ CĂN CỨ TRENTON", "Nhân vật hình dung", "BINH SĨ")),
        "n2": (("CASE OBSERVER", "Public Reaction", "CASE OBSERVER") if EN else
               ("KHÁN GIẢ", "Theo dõi vụ án", "KHÁN GIẢ")),'''
new_n = '''        "n1": (("BASE PERSONNEL", "Military Community Perspective", "BASE PERSONNEL") if EN else
               ("トレントン基地関係者", "軍関係者の証言", "関係者") if JA else
               ("BINH SĨ CĂN CỨ TRENTON", "Nhân vật hình dung", "BINH SĨ")),
        "n2": (("CASE OBSERVER", "Public Reaction", "CASE OBSERVER") if EN else
               ("ツイード住民", "市民の反応", "住民") if JA else
               ("KHÁN GIẢ", "Theo dõi vụ án", "KHÁN GIẢ")),'''
assert old_n in txt, "old_n not found"
txt = txt.replace(old_n, new_n, 1)

ED_PATH.write_text(txt, encoding="utf-8")
print("Đã vá edition.py thành công!")
