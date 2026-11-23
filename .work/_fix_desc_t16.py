import re, json, os, sys
sys.path.insert(0, r"d:\TEST\Gax\amber-eyes\.work")
R = r"d:\TEST\Gax\amber-eyes"
def mmss(t):
    n = int(t + .5); return f"{n//60:02d}:{n%60:02d}"
CFG = {
 "VI": (r"02_SAN_XUAT\Ho_So_Toi_Pham\Tap16\xuat_ban\mo_ta.txt", "", "00:00 Intro & Khuyến cáo an toàn", "⏱ MỐC CHƯƠNG"),
 "EN": (r"02_SAN_XUAT\Ho_So_Toi_Pham\Tap16_EN\xuat_ban\description.txt", "_EN", "00:00 Intro & Advisory", "⏱ CHAPTER TIMESTAMPS"),
 "JA": (r"02_SAN_XUAT\Ho_So_Toi_Pham\Tap16_JA\xuat_ban\description.txt", "_JA", "00:00 イントロ＆注意事項", "⏱ タイムスタンプ"),
}
os.environ["AE_EP"] = "16"
import importlib
for L, (rel, suf, intro, head) in CFG.items():
    os.environ["AE_LANG"] = "" if L == "VI" else L
    import edition as ED; importlib.reload(ED)
    tl = json.load(open(rf"{R}\.work\timeline_s{suf}_t16.json", encoding="utf-8"))
    st = {}
    for it in tl["items"]:
        a = it.get("act")
        if a and a not in st: st[a] = it["start"]
    chap = [intro] + [f"{mmss(st[a])} {ED.EP['act_titles'][a]}" for a in sorted(st)]
    p = rf"{R}\{rel}"
    t = open(p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    lines = t.split("\n")
    lines[0] = ED.EP["title"] + " | Amber eyes"
    i = lines.index(head)
    j = i + 1
    while re.match(r"^\d\d:\d\d ", lines[j]): j += 1
    lines[i+1:j] = chap
    t = "\n".join(lines)
    tags = {"VI": "#AmberEyes #TrueCrime #TamLyToiPham #JohnList #BreezeKnoll #OCPD #AmericasMostWanted #FrankBender #TheGiftOfFear #10ChiDauTamLy #CanhBaoDo #PhamVan #HoiTo",
            "EN": None, "JA": None}[L]
    if tags: t = re.sub(r"\n#AmberEyes[^\n]*$", "\n" + tags, t.rstrip("\n"))
    t = t.rstrip("\n") + "\n"
    for q in (p, p.replace("xuat_ban\\", "")):          # xuat_ban + thư mục tập (mo_ta/description)
        open(q, "w", encoding="utf-8", newline="\n").write(t)
    if L != "VI":
        open(rf"{R}\{os.path.dirname(rel)}\mo_ta.txt", "w", encoding="utf-8", newline="\n").write(t)
        open(os.path.join(R, os.path.dirname(rel).replace("\\xuat_ban", ""), "mo_ta.txt"), "w", encoding="utf-8", newline="\n").write(t)
    print(L, len(t), "ky tu |", chap)
