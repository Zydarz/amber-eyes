"""Sua EPISODES["04"]["summary"] cho mo ta YouTube — theo mau T03 da phat.

T03: ("1.03#1", "5.08#1") = [mo ta khong khí] + [cau moc cau hoi, tu noi trong cau]
T04 cu: ("1.10#3", "3.02#1") = "Đó là một hành vi có chủ đích. Đến đây, ... câu hỏi cốt lõi:"
       → bat dau giua dong, ket bang dau hai cham → khong doc duoc khi mo ta.
T04 moi: ("1.03#1", "5.08#2") = "Mùa thu năm 2003." + "Cái ác nguy hiểng nhất ..."
       → cung mau cau nguyen van trong kich ban (L2/H6), tu noi, moi nguoi doc.
Chi dung o mo ta (package.py) — KHONG dung o video.
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ED = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\edition.py")

old = '        "summary": ("1.10#3", "3.02#1"),'
new = '        "summary": ("1.03#1", "5.08#2"),'

raw = ED.read_text(encoding="utf-8", newline="")
if '"voice_credit"' not in raw:
    raise SystemExit("!! edition.py chua co voice_credit — hay chay _patch_credit_t04.py truoc")
n = raw.count(old)
print("so lan thay:", n)
if n != 1:
    raise SystemExit("!! khong tim thay anchor summary cu (can 1 lan)")
raw = raw.replace(old, new, 1)
ED.write_text(raw, encoding="utf-8", newline="")
print("OK: EP04 summary ->", new.strip())

# verify import that + hien gia tri
import subprocess
code = (
    "import sys;sys.path.insert(0,r'D:\\TEST\\Gax\\amber-eyes\\.work');"
    "sys.path.insert(0,r'D:\\TEST\\Gax\\amber-eyes');"
    "import edition as ED,json,pathlib;"
    "print('summary =', ED.EPISODES['04']['summary']);"
    "tl=json.loads(pathlib.Path(r'D:\\TEST\\Gax\\amber-eyes\\.work\\timeline_s_t04.json')"
    ".read_text(encoding='utf-8-sig'));"
    "s={i['id']:i['text'] for i in tl['items']};"
    "print('text =', ' '.join(s[k] for k in ED.EPISODES['04']['summary']));"
    "print('credit =', ED.EPISODES['04'].get('voice_credit'))"
)
print(subprocess.run([sys.executable, "-c", code], capture_output=True, text=True,
                     encoding="utf-8", errors="replace").stdout)
