# 制作計画・管理ファイル 第25話 · 「黄色いレインコートの殺人鬼」 — 日本語版 (JA EDITION)

## B1. エピソード基本情報

| 項目 | 内容 |
|---|---|
| エピソード名 | **第25話 · 詳細台本：Yoo Young-chul 事件ファイル―レインコートキラーと社会復讐の狂乱 — 日本語版** |
| 題材事件 | ソウル連続殺人事件（Yoo Young-chul 事件、韓国ソウル、2003年–2004年） |
| 心理学テーマ | 反社会的怨恨（Sociopathic Resentment）· 自己愛的損傷（Narcissistic Injury）· 置き換えられた攻撃（Displaced Aggression）· 自警団的妄想（Moral Vigilante Delusion）· 道徳的中和（Moral Neutralization）· 真の悔悟 vs 病的自己憐憫 |
| フォーマット | 犯罪心理学ドキュメンタリー（Host-Driven Documentary）— 5幕構成 標準 A2/K10 |
| 声優・配役構成 | 4役：**Host**（フクロウ - 95文）· **捜査官**（猟犬 - 28文）· **心理学者**（銀ギツネ - 27文）· **一般人**（N1 出張マッサージ店主：7文 ＆ N2 被害者遺族代表：8文） |
| 原本台本規模 | **165文** · 51構成要素 · 32発言ターン |
| 研究・補足資料 | 5主体心理変容解読＆行動科学補足資料（`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/NghienCuu_TamLy_BoSung_KichBan_Tap25.md`、2026年11月15日付、3言語対応） |
| 安全基準 | **規則V9（YouTube Safe）の完全遵守**：残酷描写、血液、遺体損壊の描写を0%排除。100%行動科学と4つの実用的レッドフラッグ分析に特化 |
| 映像リソース | **60枚の共通背景画像 2112×1188（16:9 2K）**、接頭辞 `t25_`、保存先 `assets/bg/` · ダーク・グラフィック・ノベル・ノワール調 |
| BGM進行 | 憂愁のチェロ $\rightarrow$ 緊迫のディープアンビエント $\rightarrow$ 学術的ミニマルピアノ $\rightarrow$ 法廷の荘厳なバイオリン $\rightarrow$ 終幕の温かなピアノ |

---

## B2. 制作パイプライン＆多言語同期ロードマップ

### 1. 資料同期および事実検証（完了済み）
- [x] ソウル地方警察庁（SMPA）、韓国大法院判決文、プロファイラーKwon Il-yongの回顧録に基づく100%事実検証の実施（`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/REVIEW_kichban_tap25.md`）。
- [x] 5主体（犯人、無意識の共犯／被害者、勇敢な目撃者、遺族、市民社会）の行動心理学的深層分析および多言語補足対話の作成（`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/NghienCuu_TamLy_BoSung_KichBan_Tap25.md`）。
- [x] YouTube動画メタデータ（`description.txt`）および公式参考資料リンク（`nguon_tham_khao_JA.md`）の更新。

### 2. 次の制作工程（`AGENTS.md` のゲート管理に準拠）
1. **ゲート1（台本承認）：** ユーザーによる心理分析補足内容の確認と承認。公式台本（VN / EN / JA）への統合。
2. **ゲート2（台本解析）：** `.work/script_tap25_JA.json` へのパース。
3. **ゲート3（演技指導とポーズゲート）：** `qc_pause_gate.py` に準拠した間合いの設定。
4. **ゲート4（TTS音声合成）：** Higgs Audio v3 / MiniMax による4役の音声生成。
5. **ゲート5（役ごとの声の一貫性検査）：** `voice_role_check.py` による検証。
6. **ゲート6（マスター音源ミキシング）：** EBUR128規格（-16 LUFS、TP $\le -1.5$ dBFS）に準拠した3層ミックス。
7. **ゲート7（ショットリスト照合）：** 共通背景画像60枚（`t25_*`）とのマッピング。
8. **ゲート8（映像レンダリングとパッケージング）：** `build_video3.py` による映像合成および字幕srtの統合。

---

## B3. 5幕構成と共通背景画像一覧（全60枚）

全60枚の背景画像（`assets/bg/t25_*.png`）は、5幕の進行に合わせて緻密に配置されています：
- **第1幕（12枚）：** `t25_yoo_young_chul_a1_01_mapo_police` ～ `a1_12_escape_police_station_rain`
- **第2幕（12枚）：** `t25_yoo_young_chul_a2_01_handcuff_interrogation` ～ `a2_12_raincoat_killer_myth`
- **第3幕（12枚）：** `t25_yoo_young_chul_a3_01_profiler_dialogue` ～ `a3_12_pathological_self_pity`
- **第4幕（12枚）：** `t25_yoo_young_chul_a4_01_seoul_central_court` ～ `a4_12_justice_restored`
- **第5幕（12枚）：** `t25_yoo_young_chul_a5_01_modern_seoul_skyline` ～ `a5_12_outtro_subscribe_card`
