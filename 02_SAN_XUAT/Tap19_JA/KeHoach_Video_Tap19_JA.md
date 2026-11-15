# 制作計画書 第19話 · 『頭の中の悪魔という仮面』 — JA EDITION

## B1. エピソード情報

| 項目 | 詳細内容 |
|---|---|
| エピソード名 | **第19話：『頭の中の悪魔』という仮面 — 精神疾患の偽装とカメラが暴いた真実（ニコラス・クルーズ事件）** |
| 対象事件 | マージョリー・ストーンマン・ダグラス高校銃乱射事件（フロリダ州ブロワード郡パークランド、2018年2月14日） |
| 心理学テーマ | 虚病・詐病（*Malingering*） · 真性精神病 vs 反社会性パーソナリティ障害（*ASPD*） · 悪名渇望症候群（*Notoriety Seeking*） · 認知の区画化（*Compartmentalization*）と家族の前での演技 · 道徳的中和技術と責任の外部化 · **中核テーマ:** クルーズの道具的後悔（*Instrumental Remorse*）＆病理的自己憐憫（*Pathological Self-Pity*）と真の悔悟の対比 · 駐在警官スコット・ピーターソンの凍結反応（*Freeze Response*）と道徳的負傷（*Moral Injury*） · 寄宿先スニード夫妻の作為的罪悪感（*Enabler Guilt*） · ネット空間の責任分散（*Diffusion of Responsibility*）と没個性化 · 教員の極限の利他性と防護的自己犠牲（*Protective Sacrifice*） · 生存生徒のサバイバーズ・ギルトと外傷後成長（*PTG / March for Our Lives*） · パークランドの郊外安全神話の錯覚 · 制度的盲視（30回以上の通報と2件のFBI情報提供の放置） · レッドフラッグ法（*Red Flag Law*）と陪審員多数決改革（12-0から8-4へ） |
| 形式 | 調査ドキュメンタリー・ポッドキャスト（ホスト主導型） — 5幕構成 標準A2c/K10 |
| 声の配分 | 4大基本ボイス: **ホスト**（145文、約60%） · **捜査官（ジョン・クルシオ刑事）**（43文、約18%） · **心理学者**（41文、約17%） · **一般人（N1/N2）**: N1 生存生徒（7文 `1.07`）＆ N2 法廷傍聴人/陪審員（6文 `4.09`） |
| 台本規模 | **241文**（5大主体の深層心理解析+31文拡張） · 51エレメント · 32発話ターン |
| 推定時間 | **約29.0 – 32.0分** · Amber eyes ゴールデンベンチマーク準拠 |
| 多言語同期 | **4言語間で1:1完全一致:** ベトナム語（VN: 241文）、英語（EN: 241文）、日本語（JA: 241文）、韓国語（KO: 241文） |
| 安全基準 | **規則V9（YouTube Safe）完全準拠**: 残虐描写や流血表現0%、行動科学、尋問戦略、BTAM脅威評価に完全集中 |
| 推奨BGM | `bgm_sub_drone.mp3` $\rightarrow$ `bgm_ambient_deep.mp3` $\rightarrow$ `bgm_piano_minimal.mp3` $\rightarrow$ `bgm_violin_heart.mp3` $\rightarrow$ `bgm_piano_warm.mp3` |
| 研究報告書 | [`01_KICH_BAN/Tap19/NghienCuu_TamLy_BoSung_KichBan_Tap19.md`](../../01_KICH_BAN/Tap19/NghienCuu_TamLy_BoSung_KichBan_Tap19.md) |
| 制作台本JSON | [`.work/script_tap19.json`](../../.work/script_tap19.json) (VN), [`.work/script_tap19_EN.json`](../../.work/script_tap19_EN.json) (EN), [`.work/script_tap19_JA.json`](../../.work/script_tap19_JA.json) (JA), [`.work/script_tap19_KO.json`](../../.work/script_tap19_KO.json) (KO) |

---

## B2. 制作パイプライン展開計画

1. **ステップ1（台本承認）:** 完了。241文構成の台本が10の心理的指標（A2c）および規則K10に100%合格。
2. **ステップ2（台本分割）:** 制作JSON `.work/script_tap19.json`、`.work/script_tap19_EN.json`、`.work/script_tap19_JA.json`、`.work/script_tap19_KO.json`（各241文）に完全コンパイル。
3. **ステップ3（演技とポーズ）:** A13および `qc_pause_gate.py` に準拠した `acting_tap19_JA.json` の生成。
4. **ステップ4（TTS音声合成）:** 日本語プロダクションキャストによる音声合成。
5. **ステップ5（声の統一性QC）:** `voice_role_check.py` による役ごとの声のアイデンティティ確認。
6. **ステップ6（マスターオーディオ）:** EBUR128（-16 LUFS、TP $\le -1.5$ dBFS）に準拠した3層ミキシング。
7. **ステップ7（ショット表作成）:** `parse_shots.py` を通じた共有背景資産との100%マッチング。
8. **ステップ8（映像レンダリングとパッケージング）:** `build_video3.py` によるレンダリングおよびSRT字幕の統合（`package.py --mux`）。
