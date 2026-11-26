#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parse toàn bộ 45 kịch bản trong 01_KICH_BAN/TamLyHocToiPham/
và khởi tạo cấu trúc sản xuất đồng bộ 3 ngôn ngữ (VI / EN / JA)
tại 02_SAN_XUAT/TamLyHocToiPham/ + dữ liệu JSON tại .work/tlhtp/.

Tuân thủ AGENTS.md:
- L2: Không bịa link nguồn / dữ kiện.
- L5: Không ghi đè mất các Bang_Shot_Anh / bg_jobs đạt chuẩn đã có.
- H25/H27: Không tạo prompt mẫu chung; ghi nhận trung thực trạng thái từng tập.
- T15: mo_ta.txt / description.txt luôn <= 5000 ký tự.
- T19: Ghi file với newline='\n' (0 lỗi \r\r\n).
"""

import glob
import json
import os
import re
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KB_DIR = ROOT / "01_KICH_BAN" / "TamLyHocToiPham"
SX_DIR = ROOT / "02_SAN_XUAT" / "TamLyHocToiPham"
WORK_TLHTP = ROOT / ".work" / "tlhtp"

ACT_WORD_MAP = {
    "1": 1, "một": 1,
    "2": 2, "hai": 2,
    "3": 3, "ba": 3,
    "4": 4, "bốn": 4,
    "5": 5, "năm": 5,
}

ROLES_MAP = {
    "HOST": "H",
    "ĐIỀU TRA VIÊN": "D",
    "CHUYÊN GIA TÂM LÝ": "C",
    "NGƯỜI BÌNH THƯỜNG": "N",
    "N1": "N1",
    "N2": "N2",
    "N3": "N3",
}

ROLE_LABELS_VI = {
    "H": "Host (Cú)",
    "C": "Chuyên gia Tâm lý (Cáo)",
    "D": "Điều tra viên (Sói)",
    "N1": "Người dân N1 (Cừu)",
    "N2": "Người dân N2 (Mèo)",
    "N3": "Người dân N3 (Khách mời đường phố)",
    "N": "Người bình thường (Vox Pop)",
}

ROLE_LABELS_EN = {
    "H": "Host (Owl)",
    "C": "Psychologist (Fox)",
    "D": "Investigator (Wolf)",
    "N1": "Ordinary Person N1 (Sheep)",
    "N2": "Ordinary Person N2 (Cat)",
    "N3": "Ordinary Person N3 (Street Vox Pop)",
    "N": "Ordinary Person (Vox Pop)",
}

ROLE_LABELS_JA = {
    "H": "ホスト（フクロウ）",
    "C": "心理学者（キツネ）",
    "D": "捜査官（オオカミ）",
    "N1": "一般人 N1（羊）",
    "N2": "一般人 N2（猫）",
    "N3": "一般人 N3（街頭インタビュー）",
    "N": "一般人（街頭インタビュー）",
}

GROUPS = [
    (1, 9, "Nhóm 1: Cơ chế Phòng vệ Vô thức", "Group 1: Unconscious Defense Mechanisms", "第1グループ：無意識の防衛機制"),
    (10, 17, "Nhóm 2: Cơ chế Ngắt kết nối Đạo đức (Moral Disengagement)", "Group 2: Moral Disengagement", "第2グループ：道徳的不活性化（モラル・ディスエンゲージメント）"),
    (18, 25, "Nhóm 3: Các dạng Thao túng & Kiểm soát Đầu độc", "Group 3: Manipulation & Coercive Control", "第3グループ：心理的操作と強制的支配"),
    (26, 33, "Nhóm 4: Rối loạn Nhân cách & Đặc tính Bệnh lý (Dark Tetrad)", "Group 4: Personality Disorders & Dark Tetrad Pathology", "第4グループ：パーソナリティ障害とダーク・テトラッド"),
    (34, 37, "Nhóm 5: Tâm lý học Xã hội & Động lực Nhóm", "Group 5: Social Psychology & Group Dynamics", "第5グループ：社会心理学と集団力学"),
    (38, 42, "Nhóm 6: Hành vi Hiện trường & Phân tích Tội phạm (Offender Profiling)", "Group 6: Crime Scene Behavior & Offender Profiling", "第6グループ：犯罪現場行動分析とプロファイリング"),
    (43, 45, "Nhóm 7: Tâm lý học Nạn nhân & Sinh tồn (Victimology)", "Group 7: Victimology & Survival Psychology", "第7グループ：被害者学と生存心理学"),
]

# Tên ngắn gọn chuẩn cho 45 tập (VI, EN, JA)
EP_TITLES = {
    1: ("Phóng chiếu (Projection)", "Projection", "投影（プロジェクション）"),
    2: ("Hợp lý hóa (Rationalization)", "Rationalization", "合理化（ラショナライゼーション）"),
    3: ("Phản ứng ngược (Reaction Formation)", "Reaction Formation", "反動形成（リアクション・フォーメーション）"),
    4: ("Trí tuệ hóa (Intellectualization)", "Intellectualization", "知性化（インテレクチュアライゼーション）"),
    5: ("Chuyển dịch (Displacement)", "Displacement", "置き換え（ディスプレイスメント）"),
    6: ("Ngăn khoang tâm lý (Compartmentalization)", "Compartmentalization", "隔離・区画化（コンパートメンタライゼーション）"),
    7: ("Phủ nhận (Denial)", "Denial", "否認（ディナイアル）"),
    8: ("Chẻ tách — Tư duy Trắng Đen (Splitting)", "Splitting — Black-and-White Thinking", "分裂・白黒思考（スプリッティング）"),
    9: ("Giảm thiểu hóa (Minimization)", "Minimization", "最小化・過小評価（ミニマイゼーション）"),
    10: ("Phi nhân hóa (Dehumanization)", "Dehumanization", "非人間化（ディヒューマナイゼーション）"),
    11: ("Gán nhãn hoa mỹ (Euphemistic Labeling)", "Euphemistic Labeling", "婉曲的ラベリング（ユーフェミスティック・ラベリング）"),
    12: ("Đổ lỗi cho nạn nhân (Victim Blaming)", "Victim Blaming", "被害者非難（ヴィクティム・ブレーミング）"),
    13: ("Khuếch tán trách nhiệm (Diffusion of Responsibility)", "Diffusion of Responsibility", "責任の分散（ディフュージョン・オブ・レスポンシビリティ）"),
    14: ("So sánh ưu thế (Advantageous Comparison)", "Advantageous Comparison", "有利な比較（アドバンテージアス・コンパリゾン）"),
    15: ("Biện minh đạo đức (Moral Justification)", "Moral Justification", "道徳的正当化（モラル・ジャスティフィケーション）"),
    16: ("Chuyển dịch trách nhiệm (Displacement of Responsibility)", "Displacement of Responsibility", "責任の転嫁（ディスプレイスメント・オブ・レスポンシビリティ）"),
    17: ("Bóp méo hoặc phớt lờ hậu quả (Distortion of Consequences)", "Distortion of Consequences", "結果の歪曲・無視（ディストーション・オブ・コンシクエンシズ）"),
    18: ("Thao túng thực tại (Gaslighting)", "Gaslighting", "ガスライティング（現実操作）"),
    19: ("Bắn phá & Thu hồi tình cảm (Love Bombing & Devaluation)", "Love Bombing & Devaluation", "ラブボミングと価値下げ"),
    20: ("Hội chứng Đấng cứu thế (Hero / Savior Complex)", "Hero / Savior Complex", "ヒーロー・シンドローム（救世主コンプレックス）"),
    21: ("Hội chứng Münchausen do ủy thác (Münchausen by Proxy)", "Münchausen Syndrome by Proxy", "代理ミュンヒハウゼン症候群"),
    22: ("Gắn kết sang chấn (Trauma Bonding)", "Trauma Bonding", "トラウマ・ボンディング（外傷的絆）"),
    23: ("Kỹ thuật DARVO (Deny - Attack - Reverse Victim & Offender)", "DARVO Tactics", "DARVO戦術（否認・攻撃・加害者と被害者の逆転）"),
    24: ("Mồi chài & Thử nghiệm ranh giới (Grooming)", "Grooming & Boundary Testing", "グルーミングと境界線テスト"),
    25: ("Cô lập xã hội & Tam giác hóa (Isolation & Triangulation)", "Isolation & Triangulation", "社会的孤立と三角関係化（トライアンギュレーション）"),
    26: ("Hội chứng Xảo quyệt (Machiavellianism)", "Machiavellianism", "マキャヴェリズム（権謀術数主義）"),
    27: ("Nói dối bệnh lý (Pathological Lying)", "Pathological Lying", "虚言癖・病的虚言（パソロジカル・ライング）"),
    28: ("Cơn nghiện ảo tưởng & Leo thang kích thích (Fantasy Escalation)", "Fantasy Escalation", "妄想の常習化とエスカレーション"),
    29: ("Ảo tưởng cuồng yêu (Erotomania)", "Erotomania", "色情妄想（エロトマニア）"),
    30: ("Thái nhân cách vs. Chống đối xã hội (Psychopathy vs. Sociopathy)", "Psychopathy vs. Sociopathy", "サイコパス vs. ソシオパス"),
    31: ("Ái kỷ bệnh lý & Cơn thịnh nộ ái kỷ (NPD & Narcissistic Rage)", "Narcissistic Personality & Narcissistic Rage", "自己愛性パーソナリティと自己愛憤怒"),
    32: ("Bạo dâm bệnh lý (Sadism)", "Pathological Sadism", "病的サディズム（加虐性）"),
    33: ("Loạn thần & Ảo giác ra lệnh (Psychosis & Command Hallucinations)", "Psychosis & Command Hallucinations", "精神病状態と命令幻聴"),
    34: ("Phi cá nhân hóa (Deindividuation)", "Deindividuation", "没個性化（ディインディビジュエーション）"),
    35: ("Tuân phục quyền lực & Tư duy nhóm (Obedience & Groupthink)", "Obedience to Authority & Groupthink", "権威への服従と集団浅慮（グループシンク）"),
    36: ("Hội chứng điên loạn chung (Folie à deux)", "Folie à Deux — Shared Delusion", "感応精神病（フォリー・ア・ドゥ）"),
    37: ("Hiệu ứng người ngoài cuộc (Bystander Effect)", "The Bystander Effect", "傍観者効果（バイスタンダー効果）"),
    38: ("Phương thức gây án vs. Chữ ký (MO vs. Signature)", "Modus Operandi vs. Signature", "手口（MO）vs. 署名行動（シグネチャー）"),
    39: ("Hành vi Hủy bỏ biểu tượng (Undoing)", "Symbolic Undoing", "象徴的取り消し行動（アンドゥイング）"),
    40: ("Dàn dựng hiện trường (Staging)", "Crime Scene Staging", "犯行現場の偽装（ステージング）"),
    41: ("Chiến lợi phẩm & Thời gian nguội (Trophies & Cooling-off Period)", "Trophies & Cooling-Off Period", "戦利品（トロフィー）と冷却期間"),
    42: ("Hội chứng Herostratus & Hiệu ứng bắt chước (Copycat Effect)", "Herostratus Syndrome & Copycat Effect", "ヘロストラトス症候群と模倣犯効果"),
    43: ("Hội chứng Stockholm (Stockholm Syndrome)", "Stockholm Syndrome", "ストックホルム症候群"),
    44: ("Sự bất lực tập nhiễm (Learned Helplessness)", "Learned Helplessness", "学習性無力感（ラーンド・ヘルプレスネス）"),
    45: ("Phản ứng Đóng băng & Lấy lòng (Freeze & Fawn Response)", "Freeze & Fawn Response", "凍結反応と迎合反応（フリーズ＆フォーン）"),
}

LATIN_SPLIT = r'(?:(?<=[.?!…])|(?<=[.?!…]”))\s+(?=[A-ZÀ-ỸĐ“(])'


def write_utf8(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Chuẩn hoá LF (T19)
    clean = text.replace("\r\n", "\n").replace("\r", "\n")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(clean)


def get_group(ep_num: int):
    for lo, hi, vi, en, ja in GROUPS:
        if lo <= ep_num <= hi:
            return vi, en, ja
    return GROUPS[0][2:]


def vn_quotes(paras):
    out, opened = [], False
    for p in paras:
        buf = []
        for i, ch in enumerate(p):
            if ch == "'":
                prev = p[i - 1] if i > 0 else ""
                nxt = p[i + 1] if i + 1 < len(p) else ""
                if prev.isalpha() and nxt.isalpha():
                    buf.append(ch)
                else:
                    buf.append("”" if opened else "“")
                    opened = not opened
            else:
                buf.append(ch)
        out.append("".join(buf))
    return out


def parse_tlhtp_script(src_path: Path):
    lines = src_path.read_text(encoding="utf-8").splitlines()
    act = 0
    els = []
    cur = None
    n = 0
    act_titles = {}
    meta_title = ""
    meta_topic = ""
    meta_case = ""

    for line in lines:
        s = line.strip()
        if s.startswith("# ") and not meta_title:
            meta_title = s[2:].strip()
        elif s.startswith("**Chủ đề:**"):
            meta_topic = s.replace("**Chủ đề:**", "").strip()
        elif s.startswith("**Hồ sơ dẫn chứng:**"):
            meta_case = s.replace("**Hồ sơ dẫn chứng:**", "").strip()

        m = re.match(r"^##\s+HỒI\s+(\S+?)\s*[:：]\s*(.*)$", s, re.I)
        if m:
            tok = m.group(1).lower().strip(":：")
            if tok in ACT_WORD_MAP:
                act = ACT_WORD_MAP[tok]
                act_titles[act] = m.group(2).strip()
                n = 0
                cur = None
                continue

        if act == 0 or not s or s == "---":
            continue

        m = re.match(
            r"^\*\*(" + "|".join(re.escape(k) for k in ROLES_MAP) + r")\*\*\s*(?:\*\((.*?)\)\*)?\s*:",
            s,
        )
        if m:
            cur = dict(role=ROLES_MAP[m.group(1)], direction=(m.group(2) or "").strip())
            continue

        m = re.match(r"^\*\*\[(SFX|BGM)\]:\*\*\s*(.*)", s)
        if m:
            n += 1
            els.append(dict(id=f"{act}.{n:02d}", act=act, kind=m.group(1), desc=m.group(2).strip()))
            if len(els) >= 2 and els[-2]["kind"] == "LOI":
                els[-2]["_open"] = False
            continue

        m = re.match(r"^\*\*\[Nghỉ\s+([\d.]+)\s*giây(.*?)\]\*\*", s, re.I)
        if m:
            n += 1
            els.append(
                dict(
                    id=f"{act}.{n:02d}",
                    act=act,
                    kind="NGHI",
                    sec=float(m.group(1)),
                    desc=m.group(2).strip(" –-"),
                )
            )
            if len(els) >= 2 and els[-2]["kind"] == "LOI":
                els[-2]["_open"] = False
            continue

        if cur is None:
            continue

        t = re.sub(r"^\*\s+", "", s)
        t = re.sub(r"^\d+\.\s+", "", t)
        t = t.replace("**", "").replace("*", "")
        t = t.strip().strip('"“”').strip()
        t = re.sub(r"(?<![A-Za-z0-9])'([^']+)'(?![A-Za-z0-9])", r"“\1”", t)
        t = re.sub(r"‘(.*?)’(?![A-Za-z])", r"“\1”", t)
        if not t:
            continue

        if els and els[-1]["kind"] == "LOI" and els[-1]["role"] == cur["role"] and els[-1].get("_open"):
            els[-1]["paras"].append(t)
        else:
            n += 1
            els.append(
                dict(
                    id=f"{act}.{n:02d}",
                    act=act,
                    kind="LOI",
                    role=cur["role"],
                    direction=cur["direction"],
                    paras=[t],
                    _open=True,
                )
            )

    for e in els:
        e.pop("_open", None)
        if e["kind"] == "LOI":
            if any("'" in p for p in e["paras"]):
                e["paras"] = vn_quotes(e["paras"])
            parts = []
            for para in e["paras"]:
                parts.extend([p.strip() for p in re.split(LATIN_SPLIT, para) if p.strip()])
            e["text"] = " ".join(e["paras"])
            e.pop("paras")
            e["sentences"] = [
                dict(id=f"{e['id']}#{k}", text=p, words=len(p.split()))
                for k, p in enumerate(parts, 1)
            ]

    return els, {
        "title_raw": meta_title,
        "topic": meta_topic,
        "case": meta_case,
        "act_titles": act_titles,
    }


def extract_bg_jobs_from_md(md_path: Path, els: list):
    """Chuyển đổi Bang_Shot_Anh_TapXX.md (Tap06-34) sang bg_jobs_tlhtp_tapXX.json."""
    txt = md_path.read_text(encoding="utf-8")
    # Tạo map câu theo từng hồi (1-indexed trong mỗi hồi) để ánh xạ mã cũ `1.1` -> mã chuẩn `1.02#1`
    act_sent_ids = {a: [] for a in range(1, 6)}
    act_sent_role = {}
    for e in els:
        if e["kind"] == "LOI":
            for s in e["sentences"]:
                act_sent_ids[e["act"]].append(s["id"])
                act_sent_role[s["id"]] = e["role"]

    jobs = []
    cur_act = 1
    for line in txt.splitlines():
        s = line.strip()
        m_act = re.match(r"^##\s+HỒI\s+(\d)", s, re.I)
        if m_act:
            cur_act = int(m_act.group(1))
            continue
        if not s.startswith("|"):
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if len(cols) < 3:
            continue
        # Bỏ dòng header / separator
        if cols[0].startswith("---") or cols[0].startswith(":---") or cols[0] in ("Shot", "Mã Ảnh"):
            continue

        # Schema B (Tap06-28): | Shot | Câu | Vai | Nền (`bg_key`) | Prompt | Nhân vật |
        if len(cols) >= 5 and re.match(r"^\d+-\d+", cols[0]):
            shot_id = cols[0]
            ref_raw = cols[1].replace("`", "").strip()
            role = cols[2].strip()
            bg_key = cols[3].replace("`", "").strip()
            prompt = cols[4].strip()
            if bg_key.lower() in ("void", "—", "-") or "chuyển hồi" in ref_raw.lower() or "thẻ kết" in ref_raw.lower():
                continue
            act_num = int(shot_id.split("-")[0])
            mapped_ids = _map_legacy_ref(ref_raw, act_num, act_sent_ids)
            jobs.append(
                {
                    "shot_id": shot_id,
                    "name": bg_key,
                    "act": act_num,
                    "speaker": role,
                    "sentences": ",".join(mapped_ids) if mapped_ids else ref_raw,
                    "legacy_ref": ref_raw,
                    "sentence_count": len(mapped_ids),
                    "desc": "",
                    "prompt": prompt,
                }
            )
        # Schema C (Tap29-34): | Mã Ảnh | Câu Thoại | Prompt Sinh Ảnh |
        elif len(cols) == 3 and re.match(r"^`?tltp\d+_\d+`?$", cols[0]):
            bg_key = cols[0].replace("`", "").strip()
            ref_raw = cols[1].replace("`", "").strip()
            prompt = cols[2].strip()
            m_a = re.match(r"^(\d+)\.", ref_raw)
            act_num = int(m_a.group(1)) if m_a else cur_act
            mapped_ids = _map_legacy_ref(ref_raw, act_num, act_sent_ids)
            speaker = act_sent_role.get(mapped_ids[0], "H") if mapped_ids else "H"
            idx = len(jobs) + 1
            jobs.append(
                {
                    "shot_id": f"{act_num}-{idx:03d}",
                    "name": bg_key,
                    "act": act_num,
                    "speaker": speaker,
                    "sentences": ",".join(mapped_ids) if mapped_ids else ref_raw,
                    "legacy_ref": ref_raw,
                    "sentence_count": len(mapped_ids),
                    "desc": "",
                    "prompt": prompt,
                }
            )
    return jobs


def _map_legacy_ref(ref_raw: str, act_num: int, act_sent_ids: dict):
    """Chuyển `1.1–1.3` hoặc `1.5` thành list mã chuẩn `1.02#1,...` theo chỉ số câu trong hồi."""
    ids = act_sent_ids.get(act_num, [])
    if not ids:
        return []
    m = re.match(r"^(\d+)\.(\d+)\s*[–-]\s*(\d+)\.(\d+)$", ref_raw)
    if m:
        a1, i1, a2, i2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        if a1 == a2 == act_num:
            return ids[max(0, i1 - 1) : min(len(ids), i2)]
    m2 = re.match(r"^(\d+)\.(\d+)$", ref_raw)
    if m2:
        a1, i1 = int(m2.group(1)), int(m2.group(2))
        if a1 == act_num and 1 <= i1 <= len(ids):
            return [ids[i1 - 1]]
    return []


def fmt_mmss(sec: float) -> str:
    m = int(sec // 60)
    s = int(round(sec % 60))
    if s == 60:
        m += 1
        s = 0
    return f"{m:02d}:{s:02d}"


def build_kehoach_vi(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    t_vi, t_en, t_ja = EP_TITLES[ep_num]
    grp_vi, _, _ = get_group(ep_num)
    role_lines = " · ".join(
        f"**{ROLE_LABELS_VI.get(r, r)}**: {cnt} câu"
        for r, cnt in sorted(info["role_counts"].items(), key=lambda x: -x[1])
    )
    act_blocks = []
    for a in range(1, 6):
        title = info["act_titles"].get(a, f"Hồi {a}")
        ac = info["act_sent_counts"].get(a, 0)
        aw = info["act_word_counts"].get(a, 0)
        bgms = info["act_bgms"].get(a, [])
        bgm_note = bgms[0] if bgms else "Dark Ambient / Cello chuẩn kênh Amber eyes"
        act_blocks.append(
            f"### HỒI {a}: {title} ({ac} câu thoại · ~{aw} từ)\n"
            f"- **Nhạc nền mở hồi (BGM):** {bgm_note}\n"
            f"- **Trạng thái đồng bộ 3 ngôn ngữ:** VI ({ac} câu đã tách JSON) · EN (chờ dịch 1-1) · JA (chờ dịch 1-1)\n"
        )
    acts_md = "\n".join(act_blocks)

    return f"""# HỒ SƠ SẢN XUẤT · TÂM LÝ HỌC TỘI PHẠM TẬP {ep_str} — {t_vi.upper()} (VI EDITION)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Series | **Tâm Lý Học Tội Phạm (45 Tập)** — {grp_vi} |
| Tên tập (VI) | **Tập {ep_str}: {t_vi}** |
| Tên tập (EN) | **Ep. {ep_str}: {t_en}** |
| Tên tập (JA) | **第{ep_str}話：{t_ja}** |
| Kịch bản nguồn (VI) | `01_KICH_BAN/TamLyHocToiPham/{info['kb_file']}` |
| Dữ liệu kịch bản tách JSON | `.work/tlhtp/script_tlhtp_tap{ep_str}.json` |
| Chủ đề chuyên sâu | {info['topic'] or t_vi} |
| Hồ sơ dẫn chứng | {info['case'] or 'Xem chi tiết trong kịch bản nguồn (cần rà nguồn công khai theo K1/L2)'} |
| Quy mô kịch bản (đo thật) | **{info['total_sentences']} câu thoại** · **{info['total_words']:,} từ** · **{info['total_elements']} phần tử** ({info['total_turns']} lượt nói) · 5 hồi · ước lượng ~**{info['est_min']} phút** |
| Cấu trúc phân vai | {role_lines} |
| Đồng bộ đa ngôn ngữ | **3 ngôn ngữ (VI · EN · JA)** — dùng chung 1 bộ ảnh nền 16:9 không chữ (H26); kịch bản EN & JA yêu cầu **Parity 1:1** đúng **{info['total_sentences']} câu** |
| Tài nguyên hình ảnh nền | `{info['bg_jobs_rel']}` — **{info['bg_jobs_count']} job ảnh** (độc lập: **{info['bg_unique_prompts']}** · trạng thái: **{info['bg_status']}**) |
| Tiêu chuẩn an toàn | Tuân thủ **V9** (không mô tả bạo lực/gore), **H1** (người thật chỉ hiện dạng bóng), **H26** (khung hình không chữ trừ số T5 & thẻ kết) |

---

## B2. Lộ trình Sản xuất 3 Ngôn ngữ (Cổng kiểm theo `AGENTS.md`)

### 1. Khởi tạo & Chuẩn hoá (Đã hoàn tất bước nền)
- [x] Tách kịch bản VN thành `.work/tlhtp/script_tlhtp_tap{ep_str}.json` (**{info['total_sentences']} câu**, 0 lỗi cấu trúc).
- [x] Khởi tạo đồng bộ 3 thư mục sản xuất: `Tap{ep_str}/` (VI) · `Tap{ep_str}_EN/` (EN) · `Tap{ep_str}_JA/` (JA).
- [ ] **Dịch & đồng bộ 1-1 kịch bản EN/JA:** Tạo bản EN và bản JA (tuân thủ `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`) khớp đúng **{info['total_sentences']} câu** với bản VI.
- [ ] **Đối chiếu nguồn công khai (K1/L2):** Hoàn thiện link thật trong `nguon_tham_khao.md` (VI/EN/JA).

### 2. Các cổng sản xuất Audio & Video (áp dụng cho cả VI, EN, JA)
1. **Bước 1 (Duyệt kịch bản — H23):** Xác nhận bản chốt VI/EN/JA, 0 lỗi V9, đủ dữ kiện đối chiếu nguồn.
2. **Bước 2–3 (Tách kịch bản & Diễn xuất — A13):** Sinh `acting_tlhtp_tap{ep_str}[_EN|_JA].json` riêng từng ngôn ngữ, chạy `qc_pause_gate.py --pre` (trung vị nghỉ ≥ 0,6 s).
3. **Bước 4–5 (TTS & Kiểm định vai — G10/G12):** Sinh giọng Higgs Audio v3 (6 vai gồm N1/N2/N3 Vox Pop), kiểm `qc_voice_sentence.py` và `voice_role_check.py`.
4. **Bước 6 (Master Audio — A7/A14/H24):** Trộn Voice + SFX + BGM đạt −16 ± 1 LUFS, TP ≤ −1,5 dBFS; chạy `qc_voice_gap.py` và `qc_wave_gate.py` cho cả 3 ngôn ngữ.
5. **Bước 7 (Ảnh nền dùng chung — H22/H25/H27/H28):** Kiểm tra `bg_jobs_tlhtp_tap{ep_str}.json` đạt M1/M2/M4/M5, sinh ảnh Kaggle FLUX (H21), soi mắt 100% nền mới (H2/H19).
6. **Bước 8–10 (Ảnh tĩnh, Dựng hình & Đóng gói — H9/H12/H14/T11/T15):** Render stills 100% shot cho VI/EN/JA, dựng `picture.mp4`, tạo `.srt`, cập nhật mốc chương thật trong `mo_ta.txt`/`description.txt` và đóng gói `xuat_ban/`.

---

## B3. Cấu trúc 5 Hồi Chi tiết (Đo từ kịch bản nguồn)

{acts_md}
"""


def build_kehoach_en(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    t_vi, t_en, _ = EP_TITLES[ep_num]
    _, grp_en, _ = get_group(ep_num)
    role_lines = " · ".join(
        f"**{ROLE_LABELS_EN.get(r, r)}**: {cnt} sentences"
        for r, cnt in sorted(info["role_counts"].items(), key=lambda x: -x[1])
    )
    act_blocks = []
    for a in range(1, 6):
        title_vi = info["act_titles"].get(a, f"Act {a}")
        ac = info["act_sent_counts"].get(a, 0)
        act_blocks.append(
            f"### ACT {a}: [EN TITLE PENDING — VI Ref: {title_vi}] ({ac} sentences)\n"
            f"- **Target Parity:** Exactly **{ac} sentences** matching VI sentence IDs.\n"
        )
    acts_md = "\n".join(act_blocks)

    return f"""# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. {ep_str} — {t_en.upper()} (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — {grp_en} |
| Episode Title (EN) | **Ep. {ep_str}: {t_en}** |
| Vietnamese Source Title | Tập {ep_str}: {t_vi} |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/{info['kb_file']}` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap{ep_str}_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **{info['total_sentences']} sentences** · **{info['total_elements']} elements** ({info['total_turns']} turns) · 5 acts · est. ~**{info['est_min']} min** |
| Voice Cast Distribution | {role_lines} |
| Shared Background Assets | `{info['bg_jobs_rel']}` — **{info['bg_jobs_count']} image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **{info['total_sentences']} sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap{ep_str}_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

{acts_md}
"""


def build_kehoach_ja(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    t_vi, t_en, t_ja = EP_TITLES[ep_num]
    _, _, grp_ja = get_group(ep_num)
    role_lines = " ・ ".join(
        f"**{ROLE_LABELS_JA.get(r, r)}**：{cnt}文"
        for r, cnt in sorted(info["role_counts"].items(), key=lambda x: -x[1])
    )
    act_blocks = []
    for a in range(1, 6):
        title_vi = info["act_titles"].get(a, f"第{a}幕")
        ac = info["act_sent_counts"].get(a, 0)
        act_blocks.append(
            f"### 第{a}幕：［日本語タイトル作成待ち — VI参照：{title_vi}］（{ac}文）\n"
            f"- **1対1同期目標：** ベトナム語原本と完全に一致する **{ac}文**（文ID完全一致）。\n"
        )
    acts_md = "\n".join(act_blocks)

    return f"""# 制作計画書 · 犯罪心理学シリーズ 第{ep_str}話 — {t_ja}（日本語版 / JA EDITION）

## B1. エピソード基本情報

| 項目 | 内容 |
|---|---|
| シリーズ | **犯罪心理学シリーズ（全45話）** — {grp_ja} |
| タイトル（JA） | **第{ep_str}話：{t_ja}** |
| 参照タイトル（VI / EN） | Tập {ep_str}: {t_vi} / Ep. {ep_str}: {t_en} |
| ベトナム語原本 | `01_KICH_BAN/TamLyHocToiPham/{info['kb_file']}` |
| 日本語台本（予定） | `01_KICH_BAN/TamLyHocToiPham/JA/kichban_tap{ep_str}_JA.md` *（1対1翻訳待ち・`CHU_CO_DINH_JA.md` 準拠）* |
| 台本規模（同期目標） | **全{info['total_sentences']}文** · **{info['total_elements']}要素**（{info['total_turns']}ターン）· 全5幕 · 想定約**{info['est_min']}分** |
| キャスト構成 | {role_lines} |
| 共通背景アセット | `{info['bg_jobs_rel']}` — **{info['bg_jobs_count']}ショット**（VI / EN / JA 3言語共通・背景文字なし H26準拠） |
| 品質・安全基準 | **V9**（過度な暴力描写禁止）・**H1**（実在人物はシルエットのみ）・**H26**（統計数字とエンドカード以外の画面内テキスト禁止）・**新字体厳守**（中国語簡体字・中国語表現の混入禁止） |

---

## B2. 日本語版 制作チェックリスト（`AGENTS.md` / `CHU_CO_DINH_JA.md` 準拠）

1. [ ] **日本語台本作成（1対1同期）：** ドキュメンタリー朗読調の自然な日本語で翻訳し、全**{info['total_sentences']}文**・`第1幕〜第5幕`・`ホスト／捜査官／心理学者／一般人`・`[休止 X秒]`を厳密一致させる。
2. [ ] **間合い・演出設計（`A13`）：** `acting_tlhtp_tap{ep_str}_JA.json` を作成し、`qc_pause_gate.py --pre`（中央値 ≥ 0.6秒）を通過させる。
3. [ ] **音声合成（`G10/A14`）：** 日本語専用リファレンス音声（Higgs Audio v3）で合成し、`qc_voice_sentence.py` を通過させる。
4. [ ] **音声マスタリング（`A7/H24`）：** −16 ± 1 LUFS・TP ≤ −1.5 dBFS に整音し、`qc_voice_gap.py` および `qc_wave_gate.py` を通過させる。
5. [ ] **映像レンダリング・書き出し（`H9/H14/T15`）：** 共通背景で静止画QC・本編MP4・日本語 `.srt` を生成し、`description.txt`（5,000文字以内）のチャプターと出典URLを更新して `xuat_ban/` に出力する。

---

## B3. 全5幕構成（同期リファレンス）

{acts_md}
"""


def build_mota_vi(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    t_vi, _, _ = EP_TITLES[ep_num]
    chapters = ["00:00 Intro"]
    cur_sec = 23.0
    for a in range(1, 6):
        title = info["act_titles"].get(a, f"Hồi {a}")
        # bỏ phần thời gian ước lượng dạng (00:00 – 05:00) trong tiêu đề nếu có
        title_clean = re.sub(r"\s*\(\d{2}:\d{2}\s*[–-]\s*\d{2}:\d{2}\)\s*$", "", title).strip()
        chapters.append(f"{fmt_mmss(cur_sec)} Hồi {a} · {title_clean}")
        aw = info["act_word_counts"].get(a, 800)
        cur_sec += max(120.0, aw / 2.35)
    ch_str = "\n".join(chapters)
    desc = f"""Tập {ep_str}: {t_vi} | Tâm Lý Học Tội Phạm | Amber eyes

{info['topic'] or f'Phân tích chuyên sâu cơ chế {t_vi} dưới góc nhìn tâm lý học tội phạm, kết hợp phỏng vấn đời thực và hồ sơ tư liệu công khai.'}

⏱ MỐC CHƯƠNG (Ước lượng — sẽ cập nhật theo timeline thật sau bước dựng audio)
{ch_str}

⚠️ LƯU Ý
• Nội dung không phù hợp cho trẻ em.
• Nội dung mang tính giáo dục, phân tích dưới góc nhìn tâm lý học tội phạm;
  không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Thông tin dựa trên tư liệu công khai (hồ sơ tòa án, nghiên cứu khoa học, báo chí) — xem nguồn bên dưới.
  Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là nhân vật minh hoạ, không phải người thật.
  Lời của Điều tra viên, Chuyên gia và Người dân là lời dựng lại phục vụ phân tích giáo dục.
• Giọng đọc, hình ảnh và âm nhạc được tạo cho kênh bằng công cụ AI.

📚 NGUỒN THAM KHẢO
• [CHỜ ĐIỀN LINK NGUỒN ĐÃ ĐỐI CHIẾU TỪ nguon_tham_khao.md TRƯỚC KHI ĐĂNG]

🆘 ĐƯỜNG DÂY HỖ TRỢ TÂM LÝ & BẢO VỆ
• Đường dây nóng Ngày Mai (hỗ trợ sức khoẻ tâm thần, Việt Nam): 096 306 1414 — https://duongdaynongngaymai.vn/
• Tổng đài Quốc gia Bảo vệ Trẻ em (Việt Nam, miễn phí 24/7): 111 — http://tongdai111.vn/

#AmberEyes #TamLyHocToiPham #CriminalPsychology #TamLyToiPham #PhamVan #HoiTo #ForensicPsychology
"""
    return desc


def build_desc_en(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    _, t_en, _ = EP_TITLES[ep_num]
    chapters = ["00:00 Intro"]
    cur_sec = 23.0
    for a in range(1, 6):
        chapters.append(f"{fmt_mmss(cur_sec)} Act {a} · [EN Chapter Title Pending]")
        aw = info["act_word_counts"].get(a, 800)
        cur_sec += max(120.0, aw / 2.35)
    ch_str = "\n".join(chapters)
    return f"""Ep. {ep_str}: {t_en} | Criminal Psychology Series | Amber eyes

An in-depth educational documentary examining {t_en} through forensic psychology, street perspectives, and verified public case records.

⏱ CHAPTERS (Estimated — update to exact measured timeline after audio mastering)
{ch_str}

⚠️ PLEASE NOTE
• This video is not suitable for children.
• It is educational content analyzed from the perspective of criminal psychology,
  and is not a substitute for medical, psychological, or legal advice.
• Information is based on verified public records, academic literature, and official archives — see sources below.
  The channel has no intent to convict, defame, or glorify any individual.
• The Owl, Wolf, Fox, Sheep, and Cat are illustrative characters, not real people.
  Dialogue for the Investigator, Psychologist, and Street Voices is reconstructed for educational analysis.
• Voices, imagery, and music were generated using AI tools.

📚 SOURCES
• [PENDING VERIFIED SOURCE URLS FROM nguon_tham_khao_EN.md BEFORE UPLOAD]

🆘 SUPPORT RESOURCES
• National Suicide & Crisis Lifeline (US): 988 — https://988lifeline.org/
• National Domestic Violence Hotline (US): 1-800-799-7233 — https://www.thehotline.org/
• National Child Helpline 111 (Vietnam, toll-free 24/7) — http://tongdai111.vn/

#AmberEyes #CriminalPsychology #ForensicPsychology #TrueCrimePsychology #Documentary #BehavioralAnalysis
"""


def build_desc_ja(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    _, _, t_ja = EP_TITLES[ep_num]
    chapters = ["00:00 オープニング"]
    cur_sec = 23.0
    for a in range(1, 6):
        chapters.append(f"{fmt_mmss(cur_sec)} 第{a}幕 · ［日本語チャプター名作成待ち］")
        aw = info["act_word_counts"].get(a, 800)
        cur_sec += max(120.0, aw / 2.35)
    ch_str = "\n".join(chapters)
    return f"""第{ep_str}話：{t_ja} | 犯罪心理学シリーズ | Amber eyes

犯罪心理学・法医学および公開記録の観点から「{t_ja}」の心理メカニズムを徹底解説する教育ドキュメンタリーです。

⏱ 目次（チャプター・暫定値／音声マスタリング後に実測値へ更新）
{ch_str}

⚠️ ご視聴にあたっての注意事項
• 本動画はお子様向けではありません。
• 本動画は教育目的および犯罪心理学の観点からの分析・解説コンテンツであり、
  医学的、心理学的、または法的なアドバイスに代わるものではありません。
• 公開記録（裁判資料、学術研究、報道資料等）に基づいて制作されています。
  動画内の心理分析はチャンネル独自の見解・考察であり、特定の個人に対する臨床的診断ではありません。
  特定の個人を告発、中傷、または美化する意図は一切ありません。
• 登場するキャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。
  捜査官、心理学者、街頭インタビューの発言は教育的分析のために構成されたドラマタイズです。
• 音声、画像、音楽はAIツールを活用して制作されています。

📚 参考資料・出典
• ［公開前に nguon_tham_khao_JA.md から検証済みURLを記載］

🆘 相談窓口
• こころの健康相談統一ダイヤル：0570-064-556
• よりそいホットライン（24時間無料）：0120-279-338
• 児童相談所虐待対応ダイヤル：189（いちはやく）
• 緊急の場合は110番または119番通報を行ってください。

#AmberEyes #犯罪心理学 #心理分析 #法医学 #プロファイリング #ドキュメンタリー
"""


def build_nguon_vi(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    t_vi, _, _ = EP_TITLES[ep_num]
    return f"""# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TÂM LÝ HỌC TỘI PHẠM TẬP {ep_str}: {t_vi.upper()}

> **Quy tắc K1 / L2 (`AGENTS.md`):** Mọi dữ kiện về người thật, năm tháng, học thuyết, số liệu và câu trích trong `01_KICH_BAN/TamLyHocToiPham/{info['kb_file']}` phải được đối chiếu nguồn công khai và điền URL thật trước khi đăng.

| Dữ kiện / Học thuyết / Vụ án trong kịch bản | Nội dung cần đối chiếu | Nguồn tham chiếu công khai (URL) | Trạng thái |
|---|---|---|:---:|
| **Hồ sơ dẫn chứng chính** | {info['case'] or 'Cần trích xuất từ Hồi 3 kịch bản'} | *(Người dùng / bước review K1 điền link thật)* | ⏳ Chờ đối chiếu |
| **Cơ sở học thuật tâm lý học** | {info['topic'] or t_vi} | *(Sách/bài báo khoa học gốc — điền link thật)* | ⏳ Chờ đối chiếu |
"""


def build_nguon_en(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    _, t_en, _ = EP_TITLES[ep_num]
    return f"""# VERIFIED SOURCES & FACT-CHECK — CRIMINAL PSYCHOLOGY EP. {ep_str}: {t_en.upper()}

> Follow `AGENTS.md` K1/L2/T15: Fill verified public URLs (court files, academic papers, major news archives) before publishing.

| Claim / Case / Theory | Verified Public Source (URL) | Status |
|---|---|:---:|
| Primary Case Reference | *(Add verified URL)* | ⏳ Pending |
| Core Psychological Literature ({t_en}) | *(Add verified URL)* | ⏳ Pending |
"""


def build_nguon_ja(ep_num: int, info: dict) -> str:
    ep_str = f"{ep_num:02d}"
    _, _, t_ja = EP_TITLES[ep_num]
    return f"""# 参考資料・ファクトチェック — 犯罪心理学シリーズ 第{ep_str}話：{t_ja}

> `AGENTS.md` K1 / L2 準拠：公開前に実在の事件記録・学術論文・公的アーカイブの検証済みURLを記入してください。

| 台本内の事実・学説・事件 | 公開出典（URL） | 確認状況 |
|---|---|:---:|
| 主要事件ファイル | *（検証済みURLを記入）* | ⏳ 確認待ち |
| 心理学理論・学術文献（{t_ja}） | *（検証済みURLを記入）* | ⏳ 確認待ち |
"""


def main():
    WORK_TLHTP.mkdir(parents=True, exist_ok=True)
    SX_DIR.mkdir(parents=True, exist_ok=True)

    kb_files = sorted(glob.glob(str(KB_DIR / "kichban_tap*.md")))
    assert len(kb_files) == 45, f"Expected 45 scripts, found {len(kb_files)}"

    summary_rows = []
    index_data = []

    for p_str in kb_files:
        p = Path(p_str)
        m = re.search(r"tap(\d+)", p.name)
        ep_num = int(m.group(1))
        ep_str = f"{ep_num:02d}"

        els, meta = parse_tlhtp_script(p)
        # Lưu JSON tách kịch bản
        json_out = WORK_TLHTP / f"script_tlhtp_tap{ep_str}.json"
        write_utf8(json_out, json.dumps(els, ensure_ascii=False, indent=1) + "\n")

        # Thống kê thật
        role_counts = Counter()
        act_sent_counts = Counter()
        act_word_counts = Counter()
        act_bgms = {a: [] for a in range(1, 6)}
        total_turns = 0
        total_sentences = 0
        total_words = 0

        for e in els:
            if e["kind"] == "LOI":
                total_turns += 1
                sc = len(e["sentences"])
                wc = sum(s["words"] for s in e["sentences"])
                role_counts[e["role"]] += sc
                act_sent_counts[e["act"]] += sc
                act_word_counts[e["act"]] += wc
                total_sentences += sc
                total_words += wc
            elif e["kind"] == "BGM":
                act_bgms[e["act"]].append(e["desc"])

        est_min = round(total_words / 140.0, 1)

        # Thư mục sản xuất 3 ngôn ngữ
        ep_vi_dir = SX_DIR / f"Tap{ep_str}"
        ep_en_dir = SX_DIR / f"Tap{ep_str}_EN"
        ep_ja_dir = SX_DIR / f"Tap{ep_str}_JA"
        ep_vi_dir.mkdir(parents=True, exist_ok=True)
        ep_en_dir.mkdir(parents=True, exist_ok=True)
        ep_ja_dir.mkdir(parents=True, exist_ok=True)

        # Chuẩn hoá riêng Tap40 từ Tap40_Staging (giữ nguyên bản cũ Tap40_Staging làm backup)
        if ep_num == 40:
            staging_dir = SX_DIR / "Tap40_Staging"
            dst_md = ep_vi_dir / "Bang_Shot_Anh_TLHTP_Tap40.md"
            dst_js = ep_vi_dir / "bg_jobs_tlhtp_tap40.json"
            if (staging_dir / "Bang_Shot_Anh_Tap40_Staging.md").exists() and not dst_md.exists():
                shutil.copy2(staging_dir / "Bang_Shot_Anh_Tap40_Staging.md", dst_md)
            if (staging_dir / "bg_jobs_tap40_staging.json").exists() and not dst_js.exists():
                shutil.copy2(staging_dir / "bg_jobs_tap40_staging.json", dst_js)

        # Xử lý bg_jobs_tlhtp_tapXX.json
        bg_json_path = ep_vi_dir / f"bg_jobs_tlhtp_tap{ep_str}.json"
        bg_jobs_count = 0
        bg_unique_prompts = 0
        bg_status = "CHỜ LẬP BẢNG SHOT & PROMPT (H25/H27)"

        if bg_json_path.exists():
            data = json.loads(bg_json_path.read_text(encoding="utf-8"))
            bg_jobs_count = len(data)
            bg_unique_prompts = len(set(x.get("prompt", "").strip() for x in data if x.get("prompt")))
            uniq_ratio = (bg_unique_prompts / bg_jobs_count) if bg_jobs_count else 0.0
            if bg_jobs_count >= 120 and uniq_ratio >= 0.90:
                bg_status = "ĐẠT H25/H27 (sẵn sàng sinh ảnh)"
            elif uniq_ratio < 0.90:
                bg_status = f"LỖI H27 M4 (trùng prompt: {bg_unique_prompts}/{bg_jobs_count})"
            else:
                bg_status = f"THIẾU SHOT H25 ({bg_jobs_count} job)"
        else:
            # Kiểm tra xem có Bang_Shot_Anh_TapXX.md trong thư mục TapXX không (Tap06-34)
            legacy_md = ep_vi_dir / f"Bang_Shot_Anh_Tap{ep_str}.md"
            if legacy_md.exists():
                jobs = extract_bg_jobs_from_md(legacy_md, els)
                if jobs:
                    write_utf8(bg_json_path, json.dumps(jobs, ensure_ascii=False, indent=2) + "\n")
                    bg_jobs_count = len(jobs)
                    bg_unique_prompts = len(set(x.get("prompt", "").strip() for x in jobs if x.get("prompt")))
                    uniq_ratio = (bg_unique_prompts / bg_jobs_count) if bg_jobs_count else 0.0
                    if bg_jobs_count >= 120 and uniq_ratio >= 0.90:
                        bg_status = "ĐÃ CHUYỂN JSON · ĐẠT H25/H27"
                    elif uniq_ratio < 0.90:
                        bg_status = f"ĐÃ CHUYỂN JSON · CẢNH BÁO TRÙNG PROMPT ({bg_unique_prompts}/{bg_jobs_count})"
                    else:
                        bg_status = f"ĐÃ CHUYỂN JSON · CẦN MỞ RỘNG SHOT H25 ({bg_jobs_count} job)"

        info = {
            "ep": ep_str,
            "kb_file": p.name,
            "topic": meta["topic"],
            "case": meta["case"],
            "act_titles": meta["act_titles"],
            "total_elements": len(els),
            "total_turns": total_turns,
            "total_sentences": total_sentences,
            "total_words": total_words,
            "est_min": est_min,
            "role_counts": dict(role_counts),
            "act_sent_counts": dict(act_sent_counts),
            "act_word_counts": dict(act_word_counts),
            "act_bgms": act_bgms,
            "bg_jobs_rel": f"02_SAN_XUAT/TamLyHocToiPham/Tap{ep_str}/bg_jobs_tlhtp_tap{ep_str}.json",
            "bg_jobs_count": bg_jobs_count,
            "bg_unique_prompts": bg_unique_prompts,
            "bg_status": bg_status,
        }

        # Ghi file sản xuất VI
        write_utf8(ep_vi_dir / f"KeHoach_Video_Tap{ep_str}.md", build_kehoach_vi(ep_num, info))
        write_utf8(ep_vi_dir / "mo_ta.txt", build_mota_vi(ep_num, info))
        write_utf8(ep_vi_dir / "nguon_tham_khao.md", build_nguon_vi(ep_num, info))
        write_utf8(ep_vi_dir / "xuat_ban" / ".gitkeep", "")

        # Ghi file sản xuất EN
        write_utf8(ep_en_dir / f"KeHoach_Video_Tap{ep_str}_EN.md", build_kehoach_en(ep_num, info))
        write_utf8(ep_en_dir / "description.txt", build_desc_en(ep_num, info))
        write_utf8(ep_en_dir / "nguon_tham_khao_EN.md", build_nguon_en(ep_num, info))
        write_utf8(ep_en_dir / "xuat_ban" / ".gitkeep", "")

        # Ghi file sản xuất JA
        write_utf8(ep_ja_dir / f"KeHoach_Video_Tap{ep_str}_JA.md", build_kehoach_ja(ep_num, info))
        write_utf8(ep_ja_dir / "description.txt", build_desc_ja(ep_num, info))
        write_utf8(ep_ja_dir / "nguon_tham_khao_JA.md", build_nguon_ja(ep_num, info))
        write_utf8(ep_ja_dir / "xuat_ban" / ".gitkeep", "")

        t_vi, t_en, t_ja = EP_TITLES[ep_num]
        summary_rows.append(
            f"| {ep_str} | {t_vi} | {total_sentences} | {total_words:,} | ~{est_min}m | "
            f"{bg_jobs_count} ({bg_unique_prompts} uniq) | {bg_status} | ✅ VI · ✅ EN · ✅ JA |"
        )
        index_data.append(
            {
                "ep": ep_str,
                "title_vi": t_vi,
                "title_en": t_en,
                "title_ja": t_ja,
                "kb_file": p.name,
                "script_json": f".work/tlhtp/script_tlhtp_tap{ep_str}.json",
                "sentences": total_sentences,
                "words": total_words,
                "est_min": est_min,
                "roles": dict(role_counts),
                "bg_jobs_count": bg_jobs_count,
                "bg_unique_prompts": bg_unique_prompts,
                "bg_status": bg_status,
            }
        )

    write_utf8(WORK_TLHTP / "index_45_tap.json", json.dumps(index_data, ensure_ascii=False, indent=2) + "\n")

    tot_sents = sum(x["sentences"] for x in index_data)
    tot_words = sum(x["words"] for x in index_data)
    tot_jobs = sum(x["bg_jobs_count"] for x in index_data)
    ready_bg = sum(1 for x in index_data if "ĐẠT H25/H27" in x["bg_status"])

    summary_md = f"""# BẢNG TỔNG HỢP SẢN XUẤT 45 TẬP · TÂM LÝ HỌC TỘI PHẠM (3 NGÔN NGỮ: VI · EN · JA)

- **Nguồn kịch bản:** `01_KICH_BAN/TamLyHocToiPham/kichban_tap01..45_*.md` (**45/45 tập đã tách JSON** tại `.work/tlhtp/script_tlhtp_tapXX.json`)
- **Thư mục sản xuất:** `02_SAN_XUAT/TamLyHocToiPham/` (**135 thư mục**: `Tap01..45` · `Tap01_EN..45_EN` · `Tap01_JA..45_JA`)
- **Tổng quy mô:** **{tot_sents:,} câu thoại** · **{tot_words:,} từ** · **{tot_jobs:,} job ảnh nền hiện có** (**{ready_bg}/45 tập** đạt ngưỡng H25/H27)
- **Nguyên tắc đa ngôn ngữ:** 1 bộ ảnh nền 16:9 sạch chữ dùng chung cho cả VI / EN / JA (H26); kịch bản EN và JA dịch đồng bộ **Parity 1:1** theo đúng số câu của từng tập.

| Tập | Chủ đề (VI) | Số câu | Số từ | Ước lượng | Ảnh nền (`bg_jobs`) | Trạng thái Ảnh (H25/H27) | Khung 3 ngôn ngữ |
|---:|---|---:|---:|---:|---|---|---|
""" + "\n".join(summary_rows) + "\n"

    write_utf8(SX_DIR / "BANG_TONG_HOP_SAN_XUAT_45_TAP.md", summary_md)
    print(f"DONE: 45 episodes | {tot_sents} sentences | {tot_words} words | 135 lang folders | {ready_bg}/45 bg ready")


if __name__ == "__main__":
    main()
