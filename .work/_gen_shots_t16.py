# Sinh bang shot Tap16 (VI/EN/JA) tu timeline + bo anh hien co. Cung ma shot & nen cho ca 3 ngon ngu (H17).
import json, re, glob, os
from pathlib import Path
from collections import Counter
W = Path(__file__).parent; R = W.parent
TL = {l: json.load(open(W / f"timeline_s{s}_t16.json", encoding="utf-8")) for l, s in (("VI", ""), ("EN", "_EN"), ("JA", "_JA"))}
PLAN = {"VI": R/"02_SAN_XUAT/Tap16/KeHoach_Video_Tap16.md", "EN": R/"02_SAN_XUAT/Tap16_EN/KeHoach_Video_Tap16_EN.md", "JA": R/"02_SAN_XUAT/Tap16_JA/KeHoach_Video_Tap16_JA.md"}
ids = [i["id"] for i in TL["VI"]["items"]]
avg = {}
for k, i in enumerate(ids):
    avg[i] = sum(TL[l]["items"][k]["end"] - TL[l]["items"][k]["start"] for l in TL) / 3
act = {i["id"]: i["act"] for i in TL["VI"]["items"]}
ROLE = {i["id"]: i["role"] for i in TL["VI"]["items"]}
newfiles = {os.path.basename(p)[:-4] for p in glob.glob(str(R/"assets/bg/t16_a?_c*.png"))}
def N(a, c):
    p = f"t16_a{a}_c{c:02d}_"
    m = [x for x in newfiles if x.startswith(p)]
    assert len(m) == 1, (p, m)
    return m[0]
def O(s): return "t16_" + s
FLAG = {"5.05#3": ("01", N(5, 6)), "5.05#6": ("02", N(5, 7)), "5.05#9": ("03", N(5, 9)), "5.05#12": ("04", N(5, 11))}
FLAG_NEXT = {"5.05#4": N(5, 6), "5.05#7": N(5, 7), "5.05#10": N(5, 9), "5.05#13": N(5, 11)}
POOL = {
 1: [N(1,1), O("westfield_residential_avenue_spring"), N(1,7), O("breeze_knoll_snowy_porch_mail"), N(1,3), N(1,2), N(1,6),
     O("autumn_sunlight_westfield_suburb"), N(1,4), O("accountant_ledger_red_deficit_ink"), N(1,5), O("breeze_knoll_attic_staircase_shadows"),
     N(1,8), N(1,9), O("forensic_ballistics_evidence_markers"), N(1,10), O("breeze_knoll_grand_ballroom_empty"), N(1,11), N(1,12), O("chevrolet_impala_airport_parking_snow")],
 2: [N(2,1), N(2,2), O("carved_family_album_empty_silhouettes"), N(2,3), N(2,4), N(2,5), N(2,6), N(2,7), O("interstate_bus_terminal_rain_neon"),
     N(2,8), N(2,9), N(2,10), O("cold_case_dossier_archives_dust"), N(2,11), N(2,12), N(2,13), N(2,14), N(2,15)],
 3: [N(3,1), N(3,2), N(3,3), O("lutheran_cross_austere_study_wall"), N(3,4), O("john_list_a4_01_mansion"), N(3,5), N(3,6), N(3,7), N(3,8),
     O("cognitive_compartmentalization_cabinet"), N(3,9), N(3,10), N(3,11), O("suburban_church_pew_hymnal_solitude"), N(3,12), N(3,13)],
 4: [N(4,1), N(4,2), O("frank_bender_sculpting_clay_tools"), N(4,3), N(4,4), N(4,5), O("vintage_crt_television_broadcast_amw"), N(4,6),
     O("colorado_neighbor_whispering_telephone"), N(4,7), N(4,8), N(4,9), N(4,10),
     O("richmond_accounting_office_desk_arrest"), N(4,11), O("john_list_a4_12_mansion"), N(4,12)],
 5: [O("courtroom_gavel_mahogany_verdict"), N(5,1), N(5,2), O("state_prison_iron_bars_solitary_cell"), N(5,3), N(5,4), N(5,5),
     O("four_redflags_overview_banner"), N(5,8), O("redflag1_rigid_perfectionism_inflexibility"), O("redflag3_financial_status_concealment"),
     O("redflag2_higher_purpose_neutralization"), N(5,10), O("redflag4_total_family_isolation"), O("vigilance_and_compassion_porch_lantern"), N(5,12), O("john_list_a5_09_mansion")],
}
CLOSE = "t16_amber_eyes_closing_dossier_list"
allb = [b for v in POOL.values() for b in v] + [CLOSE] + [b for _, b in FLAG.values()]
missing = [b for b in set(allb) if not (R/"assets/bg"/f"{b}.png").exists()]
assert not missing, missing
bgof = {}
flagbg = {b for _, b in FLAG.values()}
for n in range(1, 6):
    its = [i for i in ids if act[i] == n]
    skip = (set(FLAG) | set(FLAG_NEXT)) if n == 5 else set()
    pool = [b for b in POOL[n] if not (n == 5 and b in flagbg)]
    rest = [i for i in its if i not in skip]
    tot = sum(avg[i] for i in rest); acc = 0
    for i in rest:
        mid = acc + avg[i] / 2; acc += avg[i]
        bgof[i] = pool[min(len(pool) - 1, int(mid / tot * len(pool)))]
    if n == 5:
        for i, (_, b) in FLAG.items(): bgof[i] = b
        for i, b in FLAG_NEXT.items():
            if i in act: bgof[i] = b
TITLE = {"VI": ["BIỆT THỰ U ÁM BREEZE KNOLL VÀ KHÁM PHÁ KINH HOÀNG SAU MỘT THÁNG", "VỤ MẤT TÍCH THẾ KỶ VÀ CHIẾC KÉO CẮT MẶT TRONG ALBUM ẢNH",
          "GIẢI MÃ TÂM LÝ: RỐI LOẠN NHÂN CÁCH ÁM ẢNH CƯỠNG CHẾ (OCPD) & BẪY NGỤY BIỆN ĐẠO ĐỨC", "BỨC TƯỢNG SÁP CỦA FRANK BENDER VÀ CÚ ĐIỆN THOẠI TỪ AMERICA'S MOST WANTED",
          "BÀI HỌC ĐẮT GIÁ VỀ SỰ CUỒNG KIỂM SOÁT & 4 CẢNH BÁO ĐỎ"],
 "EN": ["THE GLOOMY BREEZE KNOLL MANSION AND THE HORRIFIC DISCOVERY AFTER A MONTH", "THE VANISHING OF THE CENTURY AND THE SCISSORS IN THE FAMILY ALBUM",
        "PSYCHOLOGICAL DECODING: OCPD AND THE MORAL-NEUTRALIZATION TRAP", "FRANK BENDER'S WAX BUST AND THE CALL FROM AMERICA'S MOST WANTED",
        "THE COSTLY LESSON OF CONTROL OBSESSION AND 4 RED FLAGS"],
 "JA": ["陰鬱なBreeze Knoll邸と一か月後の戦慄の発見", "世紀の失踪とアルバムの顔を切り抜いたハサミ", "心理解剖：強迫性パーソナリティ障害（OCPD）と道徳的正当化の罠",
        "Frank Benderの蝋像とAmerica's Most Wantedからの一本の電話", "支配欲の代償と4つのレッドフラグ"]}
ACTH = {"VI": "HỒI %02d", "EN": "ACT %02d", "JA": "第%02d幕"}
ENDC = {"VI": "**HỒ SƠ TẬP 16 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật*",
        "EN": "**CASE FILE 16 · CONCLUDED** · *AMBER EYES · True Crime Criminal Psychology Analysis*",
        "JA": "**事件ファイル 第16話 · 終結** · *AMBER EYES · 実録の事件記録から読み解く犯罪心理学*"}
NAME = {"H": "Cú", "D": "Sói", "C": "Cáo", "N1": "Cừu", "N2": "Mèo"}
CAM = ["pan", "pull", "still", "push"]
def clean(t): return t.replace("*", "").replace("|", "｜").strip()
for L in ("VI", "EN", "JA"):
    items = {i["id"]: i for i in TL[L]["items"]}
    out = ["## 6. DANH SÁCH SHOT — TẬP 16 (%s)" % L, "",
           "Bảng sinh tự động bởi `.work/_gen_shots_t16.py` (cùng mã shot và nền cho cả VI/EN/JA — H17). *Chữ* = nguyên văn câu của shot (H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ⇒ **đậm**.", "",
           "### INTRO KÊNH · 0,00–22,41 s", "", "Đặt `assets/brand/intro_kenh.mov` tại 0,00 s. Không câu thoại nào thuộc intro.", ""]
    seen = set(); cam = 0; nshots = 0
    for n in range(1, 6):
        out += ["### HỒI %d" % n, "", "| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |", "|---|---|---|---|---|---|---|---|---|"]
        k = 0
        for i in [x for x in ids if act[x] == n]:
            k += 1; it = items[i]; r = ROLE[i]; t = clean(it["text"])
            if i in FLAG:
                mau = "T8 cờ"; chu = f"*{FLAG[i][0]}* · **{t}**"; nv = "⊘"
            else:
                mau = "T4" if r in ("N1", "N2") else "T1"
                chu = f"*{t}*" if len(t) >= 40 else f"**{t}**"
                nv = f"✦ {NAME[r]}" if r not in seen else "—"
                seen.add(r)
            dur = f"{it['end']-it['start']:.1f}".replace(".", ",")
            out.append(f"| {n}-{k:02d} | `{i}` ({dur} s) | {r} | {mau} | `{bgof[i]}`, `{CAM[cam % 4]}` | {chu} | — | {nv} |  |")
            cam += 1
        k += 1
        if n < 5:
            out.append(f"| {n}-{k:02d} | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *{ACTH[L] % (n+1)}* · **{TITLE[L][n]}** | — | ⊘ | ◼ |")
            out.append("")
        else:
            out.append(f"| 5-{k:02d} | hết tập (0,0 s) | — | T2 | `{CLOSE}`, `still` | {ENDC[L]} | — | ⊘ | ◼ |")
        nshots += k
    out += ["", f"**Tổng:** {nshots} dòng · {len(ids)} câu · 5 hồi · nền dùng {len(set(bgof.values()))+1} loại (FLUX 2K Colab/Kaggle). Bỏ 31 gradient 24/10 và 22 ảnh phố Westfield lặp (H19)."]
    p = PLAN[L]; txt = open(p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*", txt, re.M)
    txt = (txt[:m.start()].rstrip() + "\n\n") if m else (txt.rstrip() + "\n\n---\n\n")
    open(p, "w", encoding="utf-8", newline="\n").write(txt + "\n".join(out) + "\n")
    print(L, nshots, "dong")
c = Counter(bgof.values()); print("nen", len(c) + 1, "max shot/nen", c.most_common(3))
