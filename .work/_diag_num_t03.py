import sys, re, json
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
import importlib.util
spec = importlib.util.spec_from_file_location("qc4", r"D:\TEST\Gax\amber-eyes\.work\qc_shots_t04.py")
qc = importlib.util.module_from_spec(spec)
sys.argv = ["qc4"]
try: spec.loader.exec_module(qc)
except SystemExit: pass
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
tl = json.loads((ROOT/".work"/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
sent = {i["id"]: i["text"] for i in tl["items"]}
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]; sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
targets = {"1-01","1-24","1-25","2-04","2-05","2-06","3-05","3-12","3-17","4-11","4-12","4-13","4-14","5-04","5-08"}
for r in rows:
    if r[0] not in targets: continue
    codes=[]
    for ma,x,y in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", r[1]):
        codes += [f"{ma}#{k}" for k in range(int(x), int(y or x)+1)]
    body = " ".join(sent.get(c,"") for c in codes)
    body_n = qc.norm_num(body); body_low = re.sub(r"\s+"," ",body.lower())
    print(f"### {r[0]}  codes={codes[0]}..{codes[-1]}")
    for c in codes: print(f"    {c}: {sent.get(c,'')[:135]}")
    print(f"    body_n = {body_n[:260]}")
    for piece in re.split(r"→|`#\d+`:", r[5]):
        ptext = qc.strip_md(piece)
        mo = re.match(r"\s*(DẤU HIỆU|TẦNG|KHÁI NIỆM|CẢNH BÁO)\s+0(\d)\b", ptext)
        if mo:
            print(f"    ORDINAL? n={mo.group(2)} can 'thứ {qc.ORDINAL.get(int(mo.group(2)),'x')}' co trong body_low: {f'thứ {qc.ORDINAL.get(int(mo.group(2)),chr(120))}' in body_low}")
            if f"thứ {qc.ORDINAL.get(int(mo.group(2)),'x')}" in body_low: continue
        for tok in re.findall(r"\d+", ptext):
            print(f"    NUM '{tok}' -> {'OK' if tok in body_n else 'FAIL'}")
    for q in re.findall(r"“([^”]+)”", r[5]):
        qn = qc.norm_num(re.sub(r"\s+"," ",q.strip()))
        print(f"    QUOTE {'OK' if qn in re.sub(chr(92)+'s+',' ',body_n) else 'FAIL'}: {q[:80]}")
    print()
