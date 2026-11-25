# 制作仕様書 · 第25話 · レインコートキラーと社会復讐の狂乱 — Yoo Young-chul 事件

## B1. 基本情報

| 項目 | 内容 |
|---|---|
| タイトル | **第25話：レインコートキラーと社会復讐の狂乱 — 反社会的怨恨と自己正当化の罠（Yoo Young-chul 事件）** |
| 事件 | ソウル連続殺人事件 — 韓国ソウル (2003年–2004年) |
| テーマ | 反社会的怨恨（Sociopathic Resentment）、自己愛的損傷（Narcissistic Injury）、置き換えられた攻撃（Displaced Aggression）、自警団的妄想（Moral Vigilante Delusion）、道徳的中和（Moral Neutralization） |
| 総尺 | **2445.7 秒 (~40 分 45 秒)** · 5幕構成 · **240 cues** |
| キャスト / 声 | Host (フクロウ) · 捜査官 (猟犬) · 心理専門家 (銀ギツネ) · N1 (出張マッサージ店主) · N2 (被害者遺族代表) |
| TTSエンジン | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| リファレンス音声 | **VoxCPM2 Voice Design (JA)** (H: `H_JA.wav`, D: `D_JA.wav`, C: `C_JA.wav`, N1: `N1_JA.wav`, N2: `N2_JA.wav`) |
| 音響設計 | 3層ステレオ：5幕BGM + 常時環境音 + 効果音SFX (`.work/sfx_tap25_JA.json`) |
| 完成マスター音源 | `02_SAN_XUAT/Tap27_JA/xuat_ban/Tap27_JA_master.mp3` & `02_SAN_XUAT/Tap27_JA/xuat_ban/Tap27_JA_master.wav` |

---

## B2. 音声品質管理測定値 (QC Metrics)

### 1. 音量ラウドネス正規化 (EBUR128基準)
- **統合ラウドネス ($I$):** **** (基準値: $-20 \pm 1\text{ LUFS}$ — 合格 ✅)
- **トゥルーピーク ($TP$):** **** (基準値: $\le -1.5\text{ dBFS}$ — 合格 ✅)
- **ラウドネスレンジ ($LRA$):** ****
- **完全無音区間 ($> 0.3\text{ 秒}$ @ $-60\text{ dBFS}$):** **0件** (合格 ✅ ルール A1 / V4)
- **冒頭ナレーション開始:** 23.0 秒 (イントロ22.41秒後 — 合格 ✅)
- **最終ナレーション終了:** 2436.7 秒、総尺 2445.7 秒で温かみのあるピアノフェードアウト (合格 ✅)

### 2. ピッチ分離度 & 話者識別性 (G9ルール)
- **Host ($H$ · フクロウ):** F0中央値 = **122.4 Hz**
- **捜査官 ($D$ · オオカミ):** F0中央値 = **85.7 Hz**
- **心理専門家 ($C$ · キツネ):** F0中央値 = **228.6 Hz**
- **ジーン・フィリップス ($N1$ · ヒツジ):** F0中央値 = **205.1 Hz**
- **ワンダ・フラナリー ($N2$ · ネコ):** F0中央値 = **275.9 Hz**
- **半音差:**
  - $\Delta_{D \to H} = \mathbf{6.17\text{ 半音}}$ (基準 $\ge 4.0\text{ 半音}$ — 合格 ✅)
  - $\Delta_{H \to C} = \mathbf{10.81\text{ 半音}}$ (基準 $\ge 4.0\text{ 半音}$ — 合格 ✅)

### 3. 音声認識精度 (Whisper Base CER) & 自然性 (UTMOSv2 MOS)
- **ASRエンジン:** `faster-whisper` (`base` model, CPU) + `ja_cer` 正規化。
- **CER中央値:** **9.74%** (平均CER: **9.88%**)。
- **マルチテイク第2ラウンド:** CER > 2%のキューに対して新規シードでVariant 1を生成し最適テイクを採用。
- **自然性評価 UTMOSv2 MOS:** 平均 **2.95 / 5.0** (範囲: 2.14 – 3.82)。基準クリア (>= 3.0 / 5.0)。
- **確認対象キュー一覧:** [`02_SAN_XUAT/Tap27_JA/xuat_ban/CanNghe_Tap27_JA_higgs.md`](xuat_ban/CanNghe_Tap27_JA_higgs.md)。

---

## B3. 納品成果物一覧

1. **マスター音源:**
   - MP3: [`02_SAN_XUAT/Tap27_JA/xuat_ban/Tap27_JA_master.mp3`](xuat_ban/Tap27_JA_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap27_JA/xuat_ban/Tap27_JA_master.wav`](xuat_ban/Tap27_JA_master.wav)
2. **タイムライン & 字幕:**
   - タイムライン: [`.work/timeline_s_JA_t27.json`](../../.work/timeline_s_JA_t27.json) (2445.7 秒)
   - 字幕SRT: [`02_SAN_XUAT/Tap27_JA/xuat_ban/Tap27_JA.srt`](xuat_ban/Tap27_JA.srt) (240 cues)
3. **品質レポート:**
   - QC生データ: [`.work/quality_qc_utmos_ep27_ja.json`](../../.work/quality_qc_utmos_ep27_ja.json)
   - 確認シート: [`02_SAN_XUAT/Tap27_JA/xuat_ban/CanNghe_Tap27_JA_higgs.md`](xuat_ban/CanNghe_Tap27_JA_higgs.md)
