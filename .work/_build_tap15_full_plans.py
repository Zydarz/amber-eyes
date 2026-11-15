#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 15 — Build Production Plan Dossiers (KeHoach_Video_Tap15.md) for VI, EN, JA.
Also generates shots_t15.json, shots_EN_t15.json, shots_JA_t15.json.
"""
import json
import re
from pathlib import Path

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"

sc_vi = json.load(open(WORK / "script_tap15.json", encoding="utf-8"))
sc_en = json.load(open(WORK / "script_tap15_EN.json", encoding="utf-8"))
sc_ja = json.load(open(WORK / "script_tap15_JA.json", encoding="utf-8"))

tl_vi = json.load(open(WORK / "timeline_s_t15.json", encoding="utf-8"))
tl_en = json.load(open(WORK / "timeline_s_EN_t15.json", encoding="utf-8"))
tl_ja = json.load(open(WORK / "timeline_s_JA_t15.json", encoding="utf-8"))

sent_to_bg = json.load(open(WORK / "_tap15_sent_to_bg.json", encoding="utf-8"))

ACT_TITLES = {
    "vi": {
        1: "HỒI 1 — ÁM ẢNH ĐỘC HẠI VÀ THẢM KỊCH TRONG BUỒNG TẮM",
        2: "HỒI 2 — DẤU VẾT KỸ THUẬT SỐ VÀ CHIẾC BÌNH XĂNG BÍ MẬT",
        3: "HỒI 3 — GIẢI MÃ TÂM LÝ: RỐI LOẠN NHÂN CÁCH RANH GIỚI & CƠN CUỒNG NỘ RUỒNG BỎ",
        4: "HỒI 4 — TRÒ ẢO THUẬT PHÒNG THẨM VẤN VÀ PHIÊN TÒA TRUYỀN HÌNH",
        5: "HỒI 5 — PHÁN QUYẾT CHUNG THÂN & 4 CẢNH BÁO ĐỎ CỦA MỐI QUAN HỆ ÁM ẢNH"
    },
    "en": {
        1: "ACT 1 — TOXIC OBSESSION AND THE TRAGEDY IN THE BATHROOM",
        2: "ACT 2 — DIGITAL EVIDENCE AND SECRET GASOLINE CANS",
        3: "ACT 3 — PSYCHOLOGICAL DECODING: BPD AND ABANDONMENT RAGE",
        4: "ACT 4 — INTERROGATION MIND GAMES AND THE TELEVISED TRIAL",
        5: "ACT 5 — LIFE SENTENCE AND 4 RED FLAGS OF TOXIC ENTANGLEMENTS"
    },
    "ja": {
        1: "第01幕 — 執着の毒気と浴室の惨劇",
        2: "第02幕 — デジタル証拠と秘密のガソリン携行缶",
        3: "第03幕 — 心理解剖：境界性パーソナリティ障害と見捨てられの激怒",
        4: "第04幕 — 取調室の心理戦と全米放映法廷劇",
        5: "第05幕 — 終身刑確定と破滅的関係の4大警戒シグナル"
    }
}

ACT_TRANSITION_CARDS = {
    2: {
        "vi": ("*HỒI 02*", "**DẤU VẾT KỸ THUẬT SỐ VÀ CHIẾC BÌNH XĂNG BÍ MẬT**"),
        "en": ("*ACT 02*", "**DIGITAL EVIDENCE AND SECRET GASOLINE CANS**"),
        "ja": ("*第02幕*", "**デジタル証拠と秘密のガソリン携行缶**")
    },
    3: {
        "vi": ("*HỒI 03*", "**GIẢI MÃ TÂM LÝ: RỐI LOẠN NHÂN CÁCH RANH GIỚI & CƠN CUỒNG NỘ RUỒNG BỎ**"),
        "en": ("*ACT 03*", "**PSYCHOLOGICAL DECODING: BPD AND ABANDONMENT RAGE**"),
        "ja": ("*第03幕*", "**心理解剖：境界性パーソナリティ障害と見捨てられの激怒**")
    },
    4: {
        "vi": ("*HỒI 04*", "**TRÒ ẢO THUẬT PHÒNG THẨM VẤN VÀ PHIÊN TÒA TRUYỀN HÌNH**"),
        "en": ("*ACT 04*", "**INTERROGATION MIND GAMES AND THE TELEVISED TRIAL**"),
        "ja": ("*第04幕*", "**取調室の心理戦と全米放映法廷劇**")
    },
    5: {
        "vi": ("*HỒI 05*", "**PHÁN QUYẾT CHUNG THÂN & 4 CẢNH BÁO ĐỎ CỦA MỐI QUAN HỆ ÁM ẢNH**"),
        "en": ("*ACT 05*", "**LIFE SENTENCE AND 4 RED FLAGS OF TOXIC ENTANGLEMENTS**"),
        "ja": ("*第05幕*", "**終身刑確定と破滅的関係の4大警戒シグナル**")
    }
}

CLOSING_CARD = {
    "vi": "**HỒ SƠ TẬP 15 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật*",
    "en": "**CASE FILE 15 · CONCLUDED** · *AMBER EYES · True Crime Criminal Psychology Analysis*",
    "ja": "**事件ファイル 第15話 · 終結** · *AMBER EYES · 実録の事件記録から読み解く犯罪心理学*"
}

CAM_CYCLE = ["pan", "pull", "still", "push"]
FLAG_SENTS = {"5.06#1": 1, "5.07#1": 2, "5.08#1": 3, "5.09#1": 4}
TESTIMONY_ELEMS = {"1.07", "4.06"}

ROLE_NAME = {"H": "Cú", "D": "Sói", "C": "Cáo", "N1": "Cừu", "N2": "Mèo"}

items_vi = {it["id"]: it for it in tl_vi["items"]}
items_en = {it["id"]: it for it in tl_en["items"]}
items_ja = {it["id"]: it for it in tl_ja["items"]}

acts_data = {1: [], 2: [], 3: [], 4: [], 5: []}
for e in sc_vi:
    if "sentences" in e and e["sentences"]:
        act = e["act"]
        for s in e["sentences"]:
            acts_data[act].append({
                "id": s["id"],
                "eid": e["id"],
                "role": e["role"] if e["role"] != "N" else ("N1" if e["id"] == "1.07" else "N2")
            })

first_seen = set()

def build_shot_table(lang):
    out = []
    shot_items_json = []
    cam_idx = 0
    
    tl_map = {"vi": items_vi, "en": items_en, "ja": items_ja}[lang]
    
    for act in range(1, 6):
        out.append(f"### {ACT_TITLES[lang][act]}")
        out.append("")
        out.append("| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        
        act_sents = acts_data[act]
        n_act = len(act_sents)
        
        for idx, item in enumerate(act_sents):
            sid = item["id"]
            eid = item["eid"]
            role = item["role"]
            next_role = act_sents[idx + 1]["role"] if idx + 1 < n_act else None
            
            tl_it = tl_map[sid]
            dur = round(tl_it["end"] - tl_it["start"], 1)
            dur_str = f"{dur:.1f} s".replace(".", ",") if lang == "vi" else f"{dur:.1f} s"
            
            shot_id = f"{act}-{idx+1:02d}"
            
            if sid in FLAG_SENTS:
                template = "T8 cờ" if lang == "vi" else ("T8 flag" if lang == "en" else "T8 旗")
            elif eid in TESTIMONY_ELEMS:
                template = "T4"
            else:
                template = "T1"
                
            bg = sent_to_bg[sid]
            cam = CAM_CYCLE[cam_idx % len(CAM_CYCLE)]
            cam_idx += 1
            bg_cam = f"`{bg}`, `{cam}`"
            
            txt = tl_it["text"].strip()
            if sid in FLAG_SENTS:
                flag_num = FLAG_SENTS[sid]
                txt_formatted = f"*0{flag_num}* · **{txt.upper()}**" if lang != "ja" else f"*0{flag_num}* · **{txt}**"
            else:
                txt_formatted = f"*{txt}*" if len(txt) >= 40 else f"**{txt}**"
            
            char_col = "—"
            if role not in first_seen:
                first_seen.add(role)
                char_col = f"✦ {ROLE_NAME[role]}"
            elif next_role and next_role != role:
                char_col = f"→{next_role}"
            elif idx == n_act - 1 and act < 5:
                next_act_first_role = acts_data[act + 1][0]["role"]
                char_col = f"→{next_act_first_role}"
                
            transition_col = ""
            
            row_str = f"| {shot_id} | `{sid}` ({dur_str}) | {role} | {template} | {bg_cam} | {txt_formatted} | — | {char_col} | {transition_col} |"
            out.append(row_str)
            
            shot_items_json.append({
                "id": shot_id,
                "sentence_id": sid,
                "element": eid,
                "act": act,
                "role": role,
                "template": template,
                "bg": bg,
                "camera": cam,
                "start": tl_it["start"],
                "end": tl_it["end"],
                "duration": dur,
                "text": txt
            })
            
        # Transition cards MUST have 'chuyển hồi' for parse_shots.py regex
        if act < 5:
            card_id = f"{act}-{n_act+1:02d}"
            label, title = ACT_TRANSITION_CARDS[act + 1][lang]
            lbl_trans = "nghỉ chuyển hồi (2 s)"
            card_row = f"| {card_id} | {lbl_trans} | — | T10 | `void`, `still` | {label} · {title} | — | ⊘ | ◼ |"
            out.append(card_row)
            out.append("")
        else:
            card_id = f"5-{n_act+1:02d}"
            lbl_end = "hết tập (0,0 s)"
            closing_txt = CLOSING_CARD[lang]
            close_row = f"| {card_id} | {lbl_end} | — | T2 | `t15_amber_eyes_closing_dossier_arias`, `still` | {closing_txt} | — | ⊘ | ◼ |"
            out.append(close_row)
            out.append("")
            
    return "\n".join(out), shot_items_json

plan_headers = {
    "vi": """# HỒ SƠ SẢN XUẤT TẬP 15 · "CƠN CUỒNG GHEN RỐI LOẠN NHÂN CÁCH RANH GIỚI" — VI EDITION

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 15: Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới — Nỗi Sợ Bị Ruồng Bỏ & Thảm Kịch Phòng Tắm (Hồ Sơ Jodi Arias)** |
| Vụ án | Hồ sơ Travis Alexander & Jodi Arias (Mesa, Arizona, Hoa Kỳ, 2008–2015) |
| Chủ đề | Rối loạn nhân cách ranh giới (BPD) · Ái kỷ ác tính & Cơ chế không thể hối hận · Sang chấn thứ cấp của người hỗ trợ vô thức · Cảm giác tội lỗi của người ngoài cuộc (Bystander Guilt) · Hiện tượng Rạp xiếc truyền thông & 4 cảnh báo đỏ sinh tồn |
| Tổng thời lượng | **1886.19 s (~31 phút 26 giây)** · 5 hồi · **220 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Bạn thân Travis - Cừu) · N2 (Bồi thẩm viên Maricopa - Mèo) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) |
| Timeline | [`.work/timeline_s_t15.json`](../../.work/timeline_s_t15.json) — **ước lượng chuẩn xác** theo tốc độ đo thật (T20) |
| Số shot | **225** dòng (220 shot nội dung + 4 thẻ chuyển hồi + 1 thẻ kết) |

---

## 6. DANH SÁCH SHOT — TẬP 15 (VI)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `✦` = lần đầu xuất hiện · `→X` = vai của shot kế tiếp · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.
Cột *Chữ* = **NGUYÊN VĂN** câu kịch bản của shot (A7/V3/H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ký tự ⇒ **đậm**.
Nền `t15_*` là **tài sản dùng chung cho cả 3 ngôn ngữ** (H17/A8.1) — mã shot giống nhau luôn dùng cùng một nền.

### INTRO KÊNH · 0,00–22,41 s

Đặt `assets/brand/intro_kenh.mov` tại 0,00 s (A5.7). Không câu thoại nào thuộc intro.

""",
    "en": """# HỒ SƠ SẢN XUẤT TẬP 15 · "CƠN CUỒNG GHEN RỐI LOẠN NHÂN CÁCH RANH GIỚI" — EN EDITION

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Ep. 15: Borderline Jealousy & Abandonment Rage — Tragedy in the Bathroom (The Jodi Arias Case)** |
| Vụ án | The Travis Alexander & Jodi Arias case file (Mesa, Arizona, USA, 2008–2015) |
| Chủ đề | Borderline Personality Disorder (BPD) · Malignant Narcissism & Structural Absence of Remorse · Secondary Trauma of Unwitting Enablers · Bystander Guilt · Media Circus Phenomenon & 4 Survival Red Flags |
| Tổng thời lượng | **1799.17 s (~29 phút 59 giây)** · 5 hồi · **220 câu thoại** |
| Diễn viên / Giọng | Host (Hawk) · Wolf (Investigator) · Fox (Psychologist) · N1 (Travis's Friend - Lamb) · N2 (Maricopa Juror - Cat) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) |
| Timeline | [`.work/timeline_s_EN_t15.json`](../../.work/timeline_s_EN_t15.json) — **measured rate estimate** (T20) |
| Số shot | **225** dòng (220 shot nội dung + 4 thẻ chuyển hồi + 1 thẻ kết) |

---

## 6. DANH SÁCH SHOT — TẬP 15 (EN)

**How to read:** *Vai* = speaker (H Hawk · D Wolf · C Fox · N1 Lamb · N2 Cat). The table describes **background + graphic**; badge and portrait are set by A5.4.
Column *Character*: `✦` = first appearance · `→X` = next shot's speaker · `⊘` = portrait off.
Last column: empty = dissolve · `✂` cut · `◼` fade to black.
Column *Text* = **VERBATIM** script line of the shot (A7/V3/H6): ≥ 40 chars ⇒ *italic*, < 40 chars ⇒ **bold**.
The `t15_*` backgrounds are **shared assets for all three languages** (H17/A8.1) — the same shot id always uses the same background.

### CHANNEL INTRO · 0.00–22.41 s

Place `assets/brand/intro_kenh.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.

""",
    "ja": """# HỒ SƠ SẢN XUẤT TẬP 15 · "CƠN CUỒNG GHEN RỐI LOẠN NHÂN CÁCH RANH GIỚI" — JA EDITION

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **第15話: 境界性嫉妬と見捨てられの激怒 — 浴室の惨劇（ジョディ・アリアス事件記録）** |
| Vụ án | トラヴィス・アレクサンダー＆ジョディ・アリアス事件記録（米国アリゾナ州メサ、2008–2015） |
| Chủ đề | 境界性パーソナリティ障害（BPD） · 悪性自己愛と真の後悔の構造的欠落 · 無意識の加担者の二次的トラウマ · 傍観者の罪悪感（バイスタンダー・ギルト） · メディア・サーカス現象と4大生存警告シグナル |
| Tổng thời lượng | **2122.59 s (~35 phút 23 giây)** · 5 hồi · **220 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Bạn thân Travis - Cừu) · N2 (Bồi thẩm viên Maricopa - Mèo) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) |
| タイムライン | [`.work/timeline_s_JA_t15.json`](../../.work/timeline_s_JA_t15.json) — **実測レートに基づく高精度推定** (T20) |
| Số shot | **225** dòng (220 shot nội dung + 4 thẻ chuyển hồi + 1 thẻ kết) |

---

## 6. DANH SÁCH SHOT — TẬP 15 (JA)

**表の読み方:** *Vai* = 話者 (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo)。表は **背景 + グラフィック** を表す。バッジと半身像は A5.4 に従う。
*キャラクター* 列: `✦` = 初登場 · `→X` = 次のショットの話者 · `⊘` = 半身像を消す。
最終列: 空欄 = ディゾルブ · `✂` = カット · `◼` = フェードアウト。
*文字* 列 = そのショットの台本の一文を **そのまま** (A7/V3/H6): 40 文字以上 ⇒ *斜体*、40 文字未満 ⇒ **太字**。
背景 `t15_*` は **3言語共通資産** (H17/A8.1) — 同一ショットIDは常に同一背景を使用。

### チャンネル導入 · 0.00–22.41 秒

0.00秒に `assets/brand/intro_kenh.mov` を配置 (A5.7)。セリフなし。

"""
}

plan_footers = {
    "vi": """**Tổng:** 225 dòng · 220 câu · 5 hồi · nền dùng 84 loại (FLUX 2K Kaggle, 15/11/2026). Bảng xây dựng theo kịch bản bổ sung phân tích tâm lý chuyên sâu (220 câu). Thời lượng shot lấy từ timeline ước lượng chuẩn xác (tốc độ đo thật Tap 08, T20).
""",
    "en": """**Tổng:** 225 rows · 220 lines · 5 acts · 84 backgrounds (FLUX 2K Kaggle, 15/11/2026). Table built from enriched psychological script (220 lines). Shot durations come from calibrated timeline (measured rate from Tap 08, T20).
""",
    "ja": """**Tổng:** 225 行 · 220 文 · 5 幕 · 背景 84 種 (FLUX 2K Kaggle, 15/11/2026)。心理分析拡充新台本 (220 文) に基づき作成。ショット長は実測レートに基づく推定タイムラインに基づく。
"""
}

# VI
first_seen.clear()
sec6_vi, shots_vi = build_shot_table("vi")
plan_vi = plan_headers["vi"] + sec6_vi + "\n" + plan_footers["vi"]
Path(ROOT / "02_SAN_XUAT/Tap15/KeHoach_Video_Tap15.md").write_text(plan_vi, encoding="utf-8")
json.dump(shots_vi, open(WORK / "shots_t15.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# EN
first_seen.clear()
sec6_en, shots_en = build_shot_table("en")
plan_en = plan_headers["en"] + sec6_en + "\n" + plan_footers["en"]
Path(ROOT / "02_SAN_XUAT/Tap15_EN/KeHoach_Video_Tap15_EN.md").write_text(plan_en, encoding="utf-8")
json.dump(shots_en, open(WORK / "shots_EN_t15.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# JA
first_seen.clear()
sec6_ja, shots_ja = build_shot_table("ja")
plan_ja = plan_headers["ja"] + sec6_ja + "\n" + plan_footers["ja"]
Path(ROOT / "02_SAN_XUAT/Tap15_JA/KeHoach_Video_Tap15_JA.md").write_text(plan_ja, encoding="utf-8")
json.dump(shots_ja, open(WORK / "shots_JA_t15.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print("Updated Tap 15 plans with correct transition syntax!")
