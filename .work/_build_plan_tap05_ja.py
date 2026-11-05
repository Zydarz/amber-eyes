# -*- coding: utf-8 -*-
"""Generate clean KeHoach_Video_Tap05_JA.md for Japanese Edition."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

ja_table = json.loads((W / "shots_text_tap05_JA.json").read_text(encoding="utf-8"))
en_plan = (ROOT / "02_SAN_XUAT/Tap05_EN/KeHoach_Video_Tap05_EN.md").read_text(encoding="utf-8")

lines = en_plan.splitlines()
out_lines = []
in_shots = False

HEADER = """# 制作計画 エピソード05 · 日本語版 · 「紫色のフロッピーディスク」 (PART B)

**適用基準:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A)  
**台本:** `01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md` · **出力先:** `02_SAN_XUAT/Tap05_JA/xuat_ban/`  
**固定テキスト・カード:** `02_SAN_XUAT/Tap05_JA/CHU_CO_DINH_JA.md`  
**日付:** 2026年11月4日

---

## B1. エピソード情報

| 項目 | 内容 |
|---|---|
| 台本 | `01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md` — 58 elements · 164 sentences |
| 音声マスター | `02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA_master.mp3` (1471.43 s · -16.28 LUFS · TP -2.00 dBFS) |
| 配役 (日本語版) | H: 梟 (フクロウ) · D: 狼 (オオカミ) · C: 狐 (キツネ) · N1: 羊 (ヒツジ) · N2: 猫 (ネコ) |
| N1 / N2 | `1.09` パークシティ住民 (ヒツジ) / `4.15` ケリー・ローソン - デニス・レイダーの娘 (ネコ) |
| 映像構造 | 全83ショット — 音声70ショット + 間奏・休止13ショット |
| 幕タイトル | 第1幕: 13年の沈黙を破る手紙 · 第2幕: 犯罪現場と心理的署名 · 第3幕: 心理剖検――歪んだ自己愛の内面 · 第4幕: 尋問とデジタル証拠の罠 · 第5幕: 判決、赤い警報と終幕 |
| 背景アセット | 61枚の専用 `t5_*` ノワール背景 (2112×1188 16:9 2K) + `void` |
| YouTube分類 | 教育 · 子ども向けではない · 「合成または加工されたコンテンツ」 · 犯罪心理学・法医学分析 |

---

## B2. 視覚規則 & アラインメント (日本語版)

- **V5 — 実在人物は完全な影/シルエットのみ:** (`t5_compliance_truck_street`, `t5_detective_war_room`, `t5_interrogation_confrontation`, `t5_two_faces_silhouette`). 実在人物の顔貌は一切露出させない。
- **被害者の描写ゼロ:** 被害者の姿はシルエットであっても描写しない。
- **V9 — 犯罪心理学および法医学・デジタルフォレンジックへの焦点:** 暴力的・グロテスクな描写は排除し、心理分析とフロッピーディスクのメタデータ解析に焦点を当てる。
- **H5 — AIテキスト生成禁止:** 画面上のすべての文字はPillowで正確な日本語フォントを用いて描画する。
- **H6/V3 — 読み上げ文と100%一致する画面テキスト:** 画面上の日本語テキストは読み上げ音声の正確な語句と一致させる。
- **H12 — 必須の終幕カード:** `*事件記録 第05話 · 終了*` + `**AMBER EYES**` + `*実際の事件記録から読み解く犯罪心理学*`。
- **H13 — 3方向同期 (映像 — テキスト — 音声):** 全83ショットにおいて1対1の完全同期を達成。

<!--TABLE-->
"""

ACT_HEADERS_JA = {
    1: "### ACT 1 — 13年の沈黙のあと、再浮上した手紙 · Lead background `t5_wichita_skyline_dusk`",
    2: "### ACT 2 — 犯罪現場＆事件ファイル――二面獣の心理的署名 · Lead background `t5_btk_signature_letter`",
    3: "### ACT 3 — 心理剖検――歪んだ殺人者の脳内 · Lead background `t5_narcissist_mirror_shadow`",
    4: "### ACT 4 — 尋問の心理戦＆フロッピーディスク技術の罠 · Lead background `t5_interrogation_room`",
    5: "### ACT 5 — 判決、赤い警報の教訓＆終幕 · Lead background `t5_courtroom_sentencing`"
}

for l in lines:
    if l.startswith("## 6. DANH SÁCH SHOT"):
        in_shots = True
        out_lines.append(HEADER)
        out_lines.append(l)
        continue
    
    if in_shots:
        if l.startswith("### ACT 1"):
            out_lines.append(ACT_HEADERS_JA[1])
            continue
        elif l.startswith("### ACT 2"):
            out_lines.append(ACT_HEADERS_JA[2])
            continue
        elif l.startswith("### ACT 3"):
            out_lines.append(ACT_HEADERS_JA[3])
            continue
        elif l.startswith("### ACT 4"):
            out_lines.append(ACT_HEADERS_JA[4])
            continue
        elif l.startswith("### ACT 5"):
            out_lines.append(ACT_HEADERS_JA[5])
            continue
        elif "intro_kenh" in l:
            out_lines.append("Place `assets/brand/intro_kenh_JA_t05.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.")
            continue
        
        m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
        if m:
            sid = m.group(1)
            parts = [p.strip() for p in l.strip().strip("|").split("|")]
            # parts: [Shot, Câu, Vai, Mẫu, Nền, Chữ, Beat, Nhân vật, Cắt]
            if sid in ja_table:
                chu_ja = ja_table[sid][0]
                parts[5] = chu_ja
            new_line = "| " + " | ".join(parts) + " |"
            out_lines.append(new_line)
            continue
        
        out_lines.append(l)

out_text = "\n".join(out_lines) + "\n"
plan_path = ROOT / "02_SAN_XUAT/Tap05_JA/KeHoach_Video_Tap05_JA.md"
plan_path.write_text(out_text, encoding="utf-8")
print(f"Successfully generated {plan_path} with {len(out_lines)} lines.")
