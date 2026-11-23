# 制作仕様書 · 第18話 · 郊外の暗闇に隠された真実 — ターピン一家事件

## B1. 基本情報

| 項目 | 内容 |
|---|---|
| タイトル | **第18話：郊外の暗闇に隠された真実 — 強圧的支配、共有精神病と命懸けの脱出（ターピン一家事件）** |
| 事件 | ターピン一家監禁虐待事件 — カリフォルニア州ペリス (2018年1月14日発見) |
| テーマ | 強圧的支配（Coercive Control）、共有精神病（Folie à Deux）、人為的幼態化（Infantilization）とサバイバル・レジリエンス |
| 総尺 | **2302.3 秒 (~38 分 22 秒)** · 5幕構成 · **240 cues** |
| キャスト / 声 | Host (フクロウ) · 捜査官 (オオカミ) · 心理専門家 (キツネ) · N1 (911通報員 · リバーサイド郡緊急司令室) · N2 (医療関係者 · リバーサイド大学医療センター) |
| TTSエンジン | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| リファレンス音声 | **VoxCPM2 Voice Design (JA)** (H: `H_JA.wav`, D: `D_JA.wav`, C: `C_JA.wav`, N1: `N1_JA.wav`, N2: `N2_JA.wav`) |
| 音響設計 | 3層ステレオ：5幕BGM + 常時環境音 + 効果音SFX (`.work/sfx_tap18_JA.json`) |
| 完成マスター音源 | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap18_JA/xuat_ban/Tap18_JA_master.mp3` & `02_SAN_XUAT/Ho_So_Toi_Pham/Tap18_JA/xuat_ban/Tap18_JA_master.wav` |

---

## B2. 音声品質管理測定値 (QC Metrics)

### 1. 音量ラウドネス正規化 (EBUR128基準)
- **統合ラウドネス ($I$):** **** (基準値: $-16 \pm 1\text{ LUFS}$ — 合格 ✅)
- **トゥルーピーク ($TP$):** **** (基準値: $\le -1.5\text{ dBFS}$ — 合格 ✅)
- **ラウドネスレンジ ($LRA$):** ****
- **完全無音区間 ($> 0.3\text{ 秒}$ @ $-60\text{ dBFS}$):** **0件** (合格 ✅ ルール A1 / V4)
- **冒頭ナレーション開始:** 23.0 秒 (イントロ22.41秒後 — 合格 ✅)
- **最終ナレーション終了:** 2293.3 秒、総尺 2302.3 秒で温かみのあるピアノフェードアウト (合格 ✅)

### 2. ピッチ分離度 & 話者識別性 (G9ルール)
- **Host ($H$ · フクロウ):** F0中央値 = **121.2 Hz**
- **捜査官 ($D$ · オオカミ):** F0中央値 = **84.7 Hz**
- **心理専門家 ($C$ · キツネ):** F0中央値 = **230.8 Hz**
- **911通報員 ($N1$ · ヒツジ):** F0中央値 = **214.3 Hz**
- **医療関係者 ($N2$ · ネコ):** F0中央値 = **282.4 Hz**
- **半音差:**
  - $\Delta_{D \to H} = \mathbf{6.20\text{ 半音}}$ (基準値 $\ge 4.0\text{ 半音}$ — 合格 ✅)
  - $\Delta_{H \to C} = \mathbf{11.15\text{ 半音}}$ (基準値 $\ge 4.0\text{ 半音}$ — 合格 ✅)

### 3. 音声認識精度 (Whisper Base CER) & 自然さ (UTMOSv2 MOS)
- **ASRエンジン:** `faster-whisper` (`base` model, CPU) + `ja_cer` 正規化。
- **CER中央値:** **9.02%** (平均CER: **9.94%**)。
- **第2ラウンド・マルチテイク:** CER > 2% の全発話に対して新規シードでVariant 1を自動生成し、最良テイクを採用。
- **UTMOSv2 MOS 自然さスコア:** 平均 **3.00 / 5.0** (範囲: 2.04 – 4.17)。基準値 (>= 3.0 / 5.0) 達成。
- **確認推奨リスト:** [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap18_JA/xuat_ban/CanNghe_Tap18_JA_higgs.md`](xuat_ban/CanNghe_Tap18_JA_higgs.md)。

---

## B3. 納品成果物一覧

1. **マスター音源 (Master Audio):**
   - MP3: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap18_JA/xuat_ban/Tap18_JA_master.mp3`](xuat_ban/Tap18_JA_master.mp3)
   - WAV: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap18_JA/xuat_ban/Tap18_JA_master.wav`](xuat_ban/Tap18_JA_master.wav)
2. **タイムライン・字幕データ:**
   - タイムライン: [`.work/timeline_s_JA_t18.json`](../../.work/timeline_s_JA_t18.json) (2302.3 秒)
   - 字幕 SRT: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap18_JA/xuat_ban/Tap18_JA.srt`](xuat_ban/Tap18_JA.srt) (240 cues)
3. **品質管理レポート:**
   - 詳細QC: [`.work/quality_qc_utmos_ep18_ja.json`](../../.work/quality_qc_utmos_ep18_ja.json)
   - 確認推奨表: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap18_JA/xuat_ban/CanNghe_Tap18_JA_higgs.md`](xuat_ban/CanNghe_Tap18_JA_higgs.md)
