# -*- coding: utf-8 -*-
"""Tap14: map 147 anh nen -> 210 cau (DP don dieu theo hoi) roi sinh shots_*_t14.json (VI/EN/JA)
va bang shot cua KeHoach_Video_Tap14.md. Mau theo _generate_shots_t13.py (chay tu thu muc goc repo)."""
import json, re, sys, unicodedata
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
W = Path(".work")
tl = {"vi": json.load(open(W/"timeline_s_t14.json", encoding="utf-8")),
      "en": json.load(open(W/"timeline_s_EN_t14.json", encoding="utf-8")),
      "ja": json.load(open(W/"timeline_s_JA_t14.json", encoding="utf-8"))}
desc = json.load(open(W/"_t14_bg_desc.json", encoding="utf-8"))   # name -> [act, desc, first_sentence_anchor]
CLOSING = "t14_b5_closing_dossier_ribbon_wax_seal"                 # danh rieng cho the ket (T2)

def toks(s):
    s = unicodedata.normalize("NFC", s.lower())
    w = re.findall(r"[a-zà-ỹ0-9]+", s)
    return set(w[i]+" "+w[i+1] for i in range(len(w)-1)) | {x for x in w if len(x) >= 4}

vi_items = tl["vi"]["items"]
dur_max = {}
for k in tl:
    for it in tl[k]["items"]:
        dur_max[it["id"]] = max(dur_max.get(it["id"], 0), it["end"]-it["start"])
sent_to_bg = {}
import collections
for act in range(1, 6):
    S = [it for it in vi_items if it["act"] == act]
    ms = open(W/f"_map_t14_a{act}.txt", encoding="utf-8").read().split()
    assert len(ms) == len(S), (act, len(ms), len(S))
    for it, nm in zip(S, ms):
        full = nm if nm.startswith("t14_") else "t14_" + nm
        assert full in desc, full
        sent_to_bg[it["id"]] = full
use = collections.defaultdict(list)
for sid, nm in sent_to_bg.items(): use[nm].append(sid)
unused = [n for n in desc if n not in use and n != CLOSING]
print("anh chua dung:", unused)
for nm, ids in use.items():
    for lang in tl:
        d = {it["id"]: it["end"]-it["start"] for it in tl[lang]["items"]}
        tot = sum(d[i] for i in ids)
        if len(ids) > 3 or tot > 30: print("VI PHAM H22", nm, len(ids), lang, round(tot, 1))
json.dump(sent_to_bg, open(W/"_t14_sent_to_bg.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

ACT_T = {
 "vi": {1: ("HỒI 01", "NGƯỜI VỢ HY SINH VÀ CHIẾC BẪY THAO TÚNG THỰC TẠI"), 2: ("HỒI 02", "CUỘC CHIẾN PHÁP LÝ TÀN KHỐC VÀ SỰ ĐỨT GÃY TÂM LÝ"),
        3: ("HỒI 03", "GIẢI MÃ TÂM LÝ: GASLIGHTING, TỔN THƯƠNG ÁI KỶ & BẪY NẠN NHÂN"), 4: ("HỒI 04", "NĂM PHÁT ĐẠN RẠNG SÁNG VÀ PHIÊN TÒA CHIA RẼ NƯỚC MỸ"),
        5: ("HỒI 05", "BÀI HỌC ĐẮT GIÁ VỀ RỦI RO HÔN NHÂN & LỜI CẢNH TỈNH")},
 "en": {1: ("ACT 01", "THE SACRIFICING WIFE AND THE TRAP OF REALITY MANIPULATION"), 2: ("ACT 02", "A BRUTAL LEGAL WAR AND THE PSYCHOLOGICAL BREAKING POINT"),
        3: ("ACT 03", "PSYCHOLOGICAL DECODING: GASLIGHTING, NARCISSISTIC INJURY & THE VICTIM TRAP"), 4: ("ACT 04", "FIVE SHOTS AT DAWN AND THE TRIAL THAT DIVIDED AMERICA"),
        5: ("ACT 05", "A COSTLY LESSON ABOUT MARRIAGE RISKS & A WARNING")},
 "ja": {1: ("第01幕", "犠牲の妻と現実操作の罠"), 2: ("第02幕", "過酷な法廷闘争と心理的な断絶"),
        3: ("第03幕", "心理解剖：ガスライティング、自己愛の傷つきと被害者の罠"), 4: ("第04幕", "夜明けの五発の銃声とアメリカを二分した裁判"),
        5: ("第05幕", "結婚のリスクが残した高価な教訓と警告")}}
T2 = {"vi": ("HỒ SƠ TẬP 14 · ĐÃ ĐÓNG", "AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật"),
      "en": ("EPISODE 14 DOSSIER · CLOSED", "AMBER EYES · Criminal Psychology Through True Case Files"),
      "ja": ("第14話 事件記録 · 終結", "AMBER EYES · 実際の事件記録から読み解く犯罪心理学")}
CAMS = ["pan", "pull", "still", "push"]
N_EL = {"1.07": "N1", "4.09": "N2"}

def mkflags(intro=False, nobust=False):
    return {"bust": False, "nobust": nobust, "intro": intro, "handoff": [], "dual": False, "guests": False, "p2": False}

def gen(lang):
    T = tl[lang]; shots = []; ci = 0
    for act in range(1, 6):
        A = [it for it in T["items"] if it["act"] == act]
        for k, it in enumerate(A, 1):
            sid = it["id"]; eid = it["element"]; sh = f"{act}-{k:02d}"
            s0 = 22.8 if sh == "1-01" else it["start"]-0.2
            s1 = A[k]["start"]-0.2 if k < len(A) else it["end"]
            tpl, var = ("T4", "testimony") if eid in N_EL else ("T1", "")
            role = N_EL.get(eid, it["role"])
            shots.append({"id": sh, "act": act, "start": round(s0, 3), "end": round(s1, 3), "role": role, "sentences": [sid],
                          "template": tpl, "variant": var, "bg": sent_to_bg[sid], "bg2": None, "inset": None, "camera": CAMS[ci % 4],
                          "segments": [{"at_sentence": None, "elems": [["ital", it["text"]]]}], "beats": [], "beat_text": "—",
                          "flags": mkflags(intro=(sh == "1-01")), "hold": False, "transition": "dissolve"}); ci += 1
        if act < 5:
            am = [m for m in T["markers"] if m["type"] == "ACT" and m.get("act") == act+1][0]
            a, b = ACT_T[lang][act+1]
            shots.append({"id": f"{act}-{len(A)+1:02d}", "act": act, "start": am["start"], "end": am["end"], "role": None, "sentences": [],
                          "template": "T10", "variant": "", "bg": "void", "bg2": None, "inset": None, "camera": "still",
                          "segments": [{"at_sentence": None, "elems": [["ital", a], ["bold", b]]}], "beats": [], "beat_text": "—",
                          "flags": mkflags(nobust=True), "hold": False, "transition": "dip"})
    A5 = [it for it in T["items"] if it["act"] == 5]
    ta, tb = T2[lang]
    shots.append({"id": f"5-{len(A5)+1:02d}", "act": 5, "start": shots[-1]["end"], "end": T["total"], "role": None, "sentences": [],
                  "template": "T2", "variant": "", "bg": CLOSING, "bg2": None, "inset": None, "camera": "still",
                  "segments": [{"at_sentence": None, "elems": [["bold", ta], ["ital", tb]]}], "beats": [], "beat_text": "—",
                  "flags": mkflags(nobust=True), "hold": False, "transition": "dip"})
    for i in range(len(shots)-1): shots[i]["end"] = shots[i+1]["start"]
    return {"total": T["total"], "shots": shots}

OUT = {"vi": "shots_t14.json", "en": "shots_EN_t14.json", "ja": "shots_JA_t14.json"}
for lang in ("vi", "en", "ja"):
    r = gen(lang)
    json.dump(r, open(W/OUT[lang], "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Saved", OUT[lang], len(r["shots"]), "shots, total", r["total"])

# ---- bang shot cho KeHoach_Video_Tap14.md (VI) ----
shots = json.load(open(W/OUT["vi"], encoding="utf-8"))["shots"]
smap = {it["id"]: it for it in tl["vi"]["items"]}
RN = {"H": "Cú", "D": "Sói", "C": "Cáo", "N1": "Cừu", "N2": "Mèo"}
HDR = {a: "### " + ACT_T["vi"][a][0] + " — " + ACT_T["vi"][a][1] for a in range(1, 6)}
seen = set(); lines = []
for a in range(1, 6): pass
plan = Path("02_SAN_XUAT/Tap14/KeHoach_Video_Tap14.md")
base = plan.read_text(encoding="utf-8")
base = base.split("\n## 6. DANH SÁCH SHOT")[0].rstrip() + "\n"
L = ["", "---", "", "## 6. DANH SÁCH SHOT — TẬP 14 (VI)", "",
     "**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.",
     "Cột *Nhân vật*: `✦` = lần đầu xuất hiện · `→X` = vai của shot kế tiếp · `⊘` = tắt bán thân.",
     "Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.",
     "Cột *Chữ* = **NGUYÊN VĂN** câu kịch bản của shot (A7/V3/H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ký tự ⇒ **đậm**.",
     "Nền `t14_*` là **tài sản dùng chung cho cả 3 ngôn ngữ** (H17/A8.1) — mã shot giống nhau luôn dùng cùng một nền.",
     "Gán nền ↔ câu: quy hoạch động đơn điệu theo hồi (`.work/_generate_shots_t14.py`), 147 ảnh dùng hết, mỗi nền ≤ 3 shot và ≤ 30 s.", "",
     "### INTRO KÊNH · 0,00–22,41 s", "", "Đặt `assets/brand/intro_kenh.mov` tại 0,00 s (A5.7). Không câu thoại nào thuộc intro.", ""]
cur = 0
for i, s in enumerate(shots):
    if s["act"] != cur:
        cur = s["act"]; L += [HDR[cur], "", "| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |", "|---|---|---|---|---|---|---|---|---|"]
    role = s["role"] or "—"; tp = s["template"]
    parts = []
    for sg in s["segments"]:
        for kind, val in sg["elems"]:
            parts.append(f"**{val}**" if kind == "bold" else f"*{val}*" if kind == "ital" else val)
    chu = " · ".join(parts) if tp in ("T10", "T2") else "".join(parts)
    if s["sentences"]:
        it = smap[s["sentences"][0]]; cau = f"`{it['id']}` ({it['end']-it['start']:.1f} s)".replace(".", ",", 1) if False else f"`{it['id']}` ({str(round(it['end']-it['start'],1)).replace('.', ',')} s)"
    else:
        cau = "nghỉ chuyển hồi (2 s)" if tp == "T10" else "hết tập (0,0 s)"
    nv = "—"
    if s["role"] and s["role"] not in seen: seen.add(s["role"]); nv = "✦ " + RN[s["role"]]
    elif tp in ("T10", "T2"): nv = "⊘"
    elif i+1 < len(shots) and shots[i+1]["role"] and shots[i+1]["role"] != s["role"]: nv = "→" + shots[i+1]["role"]
    L.append(f"| {s['id']} | {cau} | {role} | {'T4 lời kể' if tp == 'T4' else tp} | `{s['bg']}`, `{s['camera']}` | {chu} | — | {nv} | {'◼' if tp in ('T10','T2') else ''} |")
plan.write_text(base + "\n".join(L) + "\n", encoding="utf-8")
print("Wrote", plan, len(shots), "shots")
