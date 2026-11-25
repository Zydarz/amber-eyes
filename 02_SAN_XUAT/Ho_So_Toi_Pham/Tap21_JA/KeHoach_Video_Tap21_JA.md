# 制作仕様書 · 第20話 · 『家族の魂を天国へ送るため』にすべてを奪った男 — ジョン・リスト事件

## B1. 基本情報

| 項目 | 内容 |
|---|---|
| タイトル | **第20話：『家族の魂を天国へ送るため』にすべてを奪った男 — 強迫性人格障害（OCPD）と18年間の逃亡劇（ジョン・リスト事件）** |
| 事件 | ジョン・リスト一家殺害事件 — ニュージャージー州ウェストフィールド (1971年11月9日) |
| テーマ | 強迫性人格障害（OCPD）、道徳的中和技術と狂気の救済論、ロバート・クラークとしての18年間の逃亡生活、フランク・ベンダーの法医学胸像 |
| 総尺 | **2560.4 秒 (~42 分 40 秒)** · 5幕構成 · **248 cues** |
| キャスト / 声 | Host (フクロウ) · 捜査官 (オオカミ) · 心理専門家 (キツネ) · N1 (ジーン・フィリップス · 演劇教師) · N2 (ワンダ・フラナリー · コロラドの隣人) |
| TTSエンジン | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| リファレンス音声 | **VoxCPM2 Voice Design (JA)** (H: `H_JA.wav`, D: `D_JA.wav`, C: `C_JA.wav`, N1: `N1_JA.wav`, N2: `N2_JA.wav`) |
| 音響設計 | 3層ステレオ：5幕BGM + 常時環境音 + 効果音SFX (`.work/sfx_tap20_JA.json`) |
| 完成マスター音源 | `02_SAN_XUAT/Tap21_JA/xuat_ban/Tap21_JA_master.mp3` & `02_SAN_XUAT/Tap21_JA/xuat_ban/Tap21_JA_master.wav` |

---

## B2. 音声品質管理測定値 (QC Metrics)

### 1. 音量ラウドネス正規化 (EBUR128基準)
- **統合ラウドネス ($I$):** **** (基準値: $-20 \pm 1\text{ LUFS}$ — 合格 ✅)
- **トゥルーピーク ($TP$):** **** (基準値: $\le -1.5\text{ dBFS}$ — 合格 ✅)
- **ラウドネスレンジ ($LRA$):** ****
- **完全無音区間 ($> 0.3\text{ 秒}$ @ $-60\text{ dBFS}$):** **0件** (合格 ✅ ルール A1 / V4)
- **冒頭ナレーション開始:** 23.0 秒 (イントロ22.41秒後 — 合格 ✅)
- **最終ナレーション終了:** 2551.4 秒、総尺 2560.4 秒で温かみのあるピアノフェードアウト (合格 ✅)

### 2. ピッチ分離度 & 話者識別性 (G9ルール)
- **Host ($H$ · フクロウ):** F0中央値 = **123.1 Hz**
- **捜査官 ($D$ · オオカミ):** F0中央値 = **85.0 Hz**
- **心理専門家 ($C$ · キツネ):** F0中央値 = **235.3 Hz**
- **ジーン・フィリップス ($N1$ · ヒツジ):** F0中央値 = **211.6 Hz**
- **ワンダ・フラナリー ($N2$ · ネコ):** F0中央値 = **275.9 Hz**
- **半音差:**
  - $\Delta_{D \to H} = \mathbf{6.42\text{ 半音}}$ (基準 $\ge 4.0\text{ 半音}$ — 合格 ✅)
  - $\Delta_{H \to C} = \mathbf{11.22\text{ 半音}}$ (基準 $\ge 4.0\text{ 半音}$ — 合格 ✅)

### 3. 音声認識精度 (Whisper Base CER) & 自然性 (UTMOSv2 MOS)
- **ASRエンジン:** `faster-whisper` (`base` model, CPU) + `ja_cer` 正規化。
- **CER中央値:** **9.25%** (平均CER: **9.42%**)。
- **マルチテイク第2ラウンド:** CER > 2%のキューに対して新規シードでVariant 1を生成し最適テイクを採用。
- **自然性評価 UTMOSv2 MOS:** 平均 **2.98 / 5.0** (範囲: 2.08 – 3.90)。基準クリア (>= 3.0 / 5.0)。
- **確認対象キュー一覧:** [`02_SAN_XUAT/Tap21_JA/xuat_ban/CanNghe_Tap21_JA_higgs.md`](xuat_ban/CanNghe_Tap21_JA_higgs.md)。

---

## B3. 納品成果物一覧

1. **マスター音源:**
   - MP3: [`02_SAN_XUAT/Tap21_JA/xuat_ban/Tap21_JA_master.mp3`](xuat_ban/Tap21_JA_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap21_JA/xuat_ban/Tap21_JA_master.wav`](xuat_ban/Tap21_JA_master.wav)
2. **タイムライン & 字幕:**
   - タイムライン: [`.work/timeline_s_JA_t21.json`](../../.work/timeline_s_JA_t21.json) (2560.4 秒)
   - 字幕SRT: [`02_SAN_XUAT/Tap21_JA/xuat_ban/Tap21_JA.srt`](xuat_ban/Tap21_JA.srt) (248 cues)
3. **品質レポート:**
   - QC生データ: [`.work/quality_qc_utmos_ep20_ja.json`](../../.work/quality_qc_utmos_ep20_ja.json)
   - 確認シート: [`02_SAN_XUAT/Tap21_JA/xuat_ban/CanNghe_Tap21_JA_higgs.md`](xuat_ban/CanNghe_Tap21_JA_higgs.md)
