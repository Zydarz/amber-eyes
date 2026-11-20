# Sinh bang shot Tap17 (VI/EN/JA) tu timeline + 130 anh (80 co moc cau + 50 bo sung). Cung ma shot & nen cho 3 ngon ngu (H17/H25).
import json, re, sys
from pathlib import Path
W = Path(__file__).parent; R = W.parent
J1 = json.load(open(W/"bg_jobs_tap17.json", encoding="utf-8")); J2 = json.load(open(W/"bg_jobs_tap17_new50.json", encoding="utf-8"))
TL = {l: json.load(open(W/f"timeline_s{s}_t17.json", encoding="utf-8")) for l, s in (("VI", ""), ("EN", "_EN"), ("JA", "_JA"))}
PLAN = {"VI": R/"02_SAN_XUAT/Tap17/KeHoach_Video_Tap17.md", "EN": R/"02_SAN_XUAT/Tap17_EN/KeHoach_Video_Tap17_EN.md", "JA": R/"02_SAN_XUAT/Tap17_JA/KeHoach_Video_Tap17_JA.md"}
CLOSE = "t17_amber_eyes_closing_dossier_turpin"
ids = [i["id"] for i in TL["VI"]["items"]]; act = {i["id"]: i["act"] for i in TL["VI"]["items"]}; ROLE = {i["id"]: i["role"] for i in TL["VI"]["items"]}
for l in TL: assert [i["id"] for i in TL[l]["items"]] == ids
avg = {i: max(TL[l]["items"][k]["end"]-TL[l]["items"][k]["start"] for l in TL) for k, i in enumerate(ids)}  # max 3 ngon ngu (H22 do theo ngon ngu dai nhat)
def rng(s):
    m = re.match(r"(\d\.\d+)#(\d+)(?:[–-]#(\d+))?", s.strip()); 
    return [f"{m[1]}#{k}" for k in range(int(m[2]), int(m[3] or m[2])+1)] if m else []
bgof = {}; anchored = {}   # sentence -> primary image
for j in J1:
    for s in rng(j["sentences"]):
        if s in ids: anchored.setdefault(s, j["name"])
ranges = {}   # image -> sentences
for s in ids:
    if s in anchored: ranges.setdefault(anchored[s], []).append(s)
fill_img = {n: [j["name"] for j in J2 if j["act"] == n] for n in range(1, 6)}
fill_img[5] = [x for x in fill_img[5]]
unanch = [j["name"] for j in J1 if j["name"] not in ranges]
# cau khong co anh moc: dung anh cua cau truoc
last = None
for s in ids:
    if s in anchored: last = anchored[s]
    elif last: anchored[s] = last
for n in range(1, 6):
    segs = []   # (image, [sentences]) theo thu tu
    for s in [x for x in ids if act[x] == n]:
        if segs and segs[-1][0] == anchored[s]: segs[-1][1].append(s)
        else: segs.append((anchored[s], [s]))
    cand = sorted([k for k, (_, ss) in enumerate(segs) if len(ss) >= 2], key=lambda k: -sum(avg[x] for x in segs[k][1]))
    fills = list(fill_img[n]); assert len(fills) <= len(cand), (n, len(fills), len(cand))
    pick = sorted(cand[:len(fills)])
    for k, (img, ss) in enumerate(segs):
        for s in ss: bgof[s] = img
    for k, f in zip(pick, fills):     # cau cuoi cua cum -> anh bo sung
        bgof[segs[k][1][-1]] = f
# H22: nen vuot 3 shot/30 s -> doi cau cuoi cum sang anh chua dung; anh chua dung -> nhan cau dai nhat cung hoi
def usage():
    from collections import Counter
    c = Counter(bgof.values()); d = Counter()
    for q, b in bgof.items(): d[b] += avg[q]
    return c, d
for _ in range(60):
    c, d = usage(); bad = [b for b in c if c[b] > 3 or d[b] > 25.5]
    if not bad: break
    b = bad[0]; sents = [q for q in ids if bgof[q] == b]; moved = False
    for q in (sents[-1], sents[0]):
        i = ids.index(q)
        for nb in ((i+1, i+2) if q == sents[-1] else (i-1, i-2)):
            if 0 <= nb < len(ids) and act[ids[nb]] == act[q]:
                t = bgof[ids[nb]]
                if t != b and c[t] < 3 and d[t] + avg[q] <= 25.5: bgof[q] = t; moved = True; break
        if moved: break
    if not moved:
        unused = [j for j in J1+J2 if j["name"] not in c and j["name"] != CLOSE]
        if unused: bgof[sents[-1]] = unused[0]["name"]
        else: print("KHONG GIAI DUOC", b); break
bgof[ids[-1]] = 't17_endcard_investigative_archive_wall'  # anh thua cuoi cung -> cau chot tap
allb = set(bgof.values()) | {CLOSE}
miss = [b for b in allb if not (R/"assets/bg"/f"{b}.png").exists()]; assert not miss, miss
ACTT = {"VI": {}, "EN": {}, "JA": {}}
sys.path.insert(0, str(W))
TITLE = {"VI": ["NGỤC TÙ NGOẠI Ô VÀ VỎ BỌC HOÀN HẢO", "GIẢI MÃ KIỂM SOÁT CƯỠNG CHẾ & FOLIE À DEUX", "BẢN ÁN CÔNG LÝ & SỰ SỤP ĐỔ CÁI TÔI", "TÁI SINH & BỐN CẢNH BÁO ĐỎ SINH TỒN"],
         "EN": ["THE SUBURBAN DUNGEON AND THE PERFECT FACADE", "DECODING COERCIVE CONTROL & FOLIE À DEUX", "THE VERDICT AND THE COLLAPSE OF THE EGO", "REBIRTH & THE FOUR SURVIVAL RED FLAGS"],
         "JA": ["郊外の監禁部屋と完璧な仮面", "強圧的支配とフォリ・ア・ドゥの解読", "判決と自我の崩壊", "再生と4つのレッドフラッグ"]}
ACTH = {"VI": "HỒI %02d", "EN": "ACT %02d", "JA": "第%02d幕"}
ENDC = {"VI": "**HỒ SƠ TẬP 17 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật*",
        "EN": "**CASE FILE 17 · CONCLUDED** · *AMBER EYES · True Crime Criminal Psychology Analysis*",
        "JA": "**事件ファイル 第17話 · 終結** · *AMBER EYES · 実録の事件記録から読み解く犯罪心理学*"}
NAME = {"H": "Cú", "D": "Sói", "C": "Cáo", "N1": "Cừu", "N2": "Mèo"}
CAM = ["pan", "pull", "still", "push"]
def clean(t): return t.replace("*", "").replace("|", "｜").strip()
for L in ("VI", "EN", "JA"):
    items = {i["id"]: i for i in TL[L]["items"]}
    out = ["## 6. DANH SÁCH SHOT — TẬP 17 (%s)" % L, "",
           "Bảng sinh tự động bởi `.work/_gen_shots_t17.py` (cùng mã shot và nền cho cả VI/EN/JA — H17). *Chữ* = nguyên văn câu của shot (H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ⇒ **đậm**.", "",
           "### INTRO KÊNH · 0,00–22,41 s", "", "Đặt `assets/brand/intro_kenh.mov` tại 0,00 s. Không câu thoại nào thuộc intro.", ""]
    seen = set(); cam = 0; nshots = 0
    for n in range(1, 6):
        out += ["### HỒI %d" % n, "", "| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |", "|---|---|---|---|---|---|---|---|---|"]
        k = 0
        for i in [x for x in ids if act[x] == n]:
            k += 1; it = items[i]; r = ROLE[i]; t = clean(it["text"])
            mau = "T4" if r in ("N1", "N2") else "T1"
            chu = f"*{t}*" if len(t) >= 40 else f"**{t}**"
            nv = f"✦ {NAME[r]}" if r not in seen else "—"; seen.add(r)
            dur = f"{it['end']-it['start']:.1f}".replace(".", ",")
            out.append(f"| {n}-{k:02d} | `{i}` ({dur} s) | {r} | {mau} | `{bgof[i]}`, `{CAM[cam % 4]}` | {chu} | — | {nv} |  |"); cam += 1
        k += 1
        if n < 5:
            out.append(f"| {n}-{k:02d} | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *{ACTH[L] % (n+1)}* · **{TITLE[L][n-1]}** | — | ⊘ | ◼ |"); out.append("")
        else:
            out.append(f"| 5-{k:02d} | hết tập (0,0 s) | — | T2 | `{CLOSE}`, `still` | {ENDC[L]} | — | ⊘ | ◼ |")
        nshots += k
    out += ["", f"**Tổng:** {nshots} dòng · {len(ids)} câu · 5 hồi · nền dùng {len(set(bgof.values()))+1} loại (FLUX 2K Kaggle)."]
    p = PLAN[L]; txt = open(p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*", txt, re.M)
    txt = (txt[:m.start()].rstrip() + "\n\n") if m else (txt.rstrip() + "\n\n---\n\n")
    open(p, "w", encoding="utf-8", newline="\n").write(txt + "\n".join(out) + "\n"); print(L, nshots, "dong")
from collections import Counter
c = Counter(bgof.values()); dur = Counter()
for s, b in bgof.items(): dur[b] += avg[s]
print("nen dung", len(c)+1, "/130 | thua:", [j["name"] for j in J1+J2 if j["name"] not in c and j["name"] != CLOSE][:20])
print("max shot/nen", c.most_common(3), "| max s/nen", [(b, round(v)) for b, v in dur.most_common(3)])
