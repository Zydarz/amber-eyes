import sys, json, re, difflib
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
from parse_kichban import parse_file
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
old_els = parse_file(ROOT/".work"/"_cu"/"kichban_tap03_22102026_truoc_V9_20261031.md")
new_els = parse_file(ROOT/"01_KICH_BAN"/"Tap03"/"kichban_tap03_22102026.md")
def byel(els):
    return {e["id"]: [s["text"] for s in e.get("sentences",[])] for e in els if e["kind"]=="LOI"}
O, N = byel(old_els), byel(new_els)

def norm(s):
    return re.sub(r"\s+"," ", s.replace("“",'"').replace("”",'"').replace("**","")).strip().lower()
# old id -> new id, by best-match alignment inside same element
old2new = {}
for el in sorted(set(O)|set(N)):
    o, n = O.get(el,[]), N.get(el,[])
    sm = difflib.SequenceMatcher(None, [norm(x) for x in o], [norm(y) for y in n])
    for a,b,size in sm.get_matching_blocks():
        for k in range(size):
            old2new[f"{el}#{a+1}"] = f"{el}#{b+1}"
print("mapped:", len(old2new), "/", sum(len(v) for v in O.values()))

plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]; sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
bad = []
for l in sec.splitlines():
    if not re.match(r"\|\s*[1-5]-\d+", l): continue
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    sid, cau = cells[0], cells[1]
    olds = []
    for ma,a,b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cau):
        for k in range(int(a), int(b or a)+1): olds.append(f"{ma}#{k}")
    if not olds: continue
    mapped = [old2new.get(x) for x in olds]
    if any(m_ is None for m_ in mapped):
        bad.append((sid, cau, mapped, "KHONG MAP DUOC")); continue
    # expected contiguous new range
    nums = [int(x.split("#")[1]) for x in mapped]
    exp = f"{mapped[0].split('#')[0]}#{nums[0]}–#{nums[-1]}" if len(nums)>1 else mapped[0]
    got = cau.strip("`").replace("`–`","–")
    # build normalized "el#a–#b" strings for comparison
    def normrange(c):
        mm = re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", c)
        if not mm: return None
        ma,a,b = mm[0]
        return (ma, int(a), int(b or a))
    g = normrange(got); e = normrange(exp)
    if g != e:
        bad.append((sid, cau, mapped, f"MOI: {exp}"))
print()
if bad:
    print("=== CANH CHONH PHAI SUA ===")
    for sid, cau, mapped, note in bad:
        print(f"  {sid}: hien tai [{cau}]  ->  {note}")
        for o,m_ in zip([c for c in [cau]],[m_]):
            pass
else:
    print("TAT CA HANG DUNG")
