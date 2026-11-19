# 制作計画 第15話 · 日本語版 · 「ベティ・ブロデリックの悲劇」

## B1. エピソード概要

| 項目 | 内容 |
|---|---|
| タイトル | **第15話：ガスライティングの被害者が一線を越えるとき――現実操作と破壊的憤怒（ベティ・ブロデリック事件）** |
| 事件名 | エリザベス・“ベティ”・ブロデリック、ダニエル・ブロデリック＆リンダ・コルケナ事件 — アメリカ・カリフォルニア州サンディエゴ（1989年11月5日） |
| 心理テーマ | 現実操作（ガスライティング）、自己愛性損傷、心理的破綻と破壊的憤怒、10の心理行動指標エコシステム |
| 総時間 | **2151.5 秒 (~35 分 51 秒)** · 5幕構成 · **220 cues** |
| 声優・役割 | ホスト（フクロウ）· 捜査官（オオカミ）· 心理学者（キツネ）· N1（ラ・ホヤの親友）· N2（キム・ブロデリック／長女） |
| TTSエンジン | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| 音声モデル | **VoxCPM2 Voice Design JA** (H: `H_JA.wav`, D: `D_JA.wav`, C: `C_JA.wav`, N1: `N1_JA.wav`, N2: `N2_JA.wav`) |
| 音響構成 | 3層ステレオ音響: 5幕BGM + 継続的環境音 + ピンポイント効果音 (`.work/sfx_tap15_JA.json`) |
| マスター出力 | `02_SAN_XUAT/Tap15_JA/xuat_ban/Tap15_JA_master.mp3` & `02_SAN_XUAT/Tap15_JA/xuat_ban/Tap15_JA_master.wav` |

---

## B2. 音声品質管理指標（QC Metrics）

### 1. ラウドネス規格（EBUR128 Loudness）
- **統合ラウドネス ($I$):** **** (基準値: $-16 \pm 1\text{ LUFS}$ — 合格 ✅)
- **トゥルーピーク ($TP$):** **** (基準値: $\le -1.5\text{ dBFS}$ — 合格 ✅)
- **ラウドネス範囲 ($LRA$):** ****
- **絶対無音区間 ($> 0.3\text{ 秒}$ @ $-60\text{ dBFS}$):** **0件** (合格 ✅ 規則 A1 / V4)
- **冒頭ナレーション開始:** 23.0 秒 (オープニング22.41秒後 — 合格 ✅)
- **最終ナレーション終了:** 2142.5 秒, エピソード終了 2151.5 秒 (ピアノの余韻フェードアウト — 合格 ✅)

### 2. ピッチ分離とキャラクター識別（規則 G9）
- **ホスト ($H$ · フクロウ):** F0中央値 = **122.1 Hz**
- **捜査官 ($D$ · オオカミ):** F0中央値 = **85.3 Hz**
- **心理学者 ($C$ · キツネ):** F0中央値 = **230.8 Hz**
- **ラ・ホヤの親友 ($N1$ · ヒツジ):** F0中央値 = **208.7 Hz**
- **キム・ブロデリック ($N2$ · ネコ):** F0中央値 = **280.8 Hz**
- **音高差:**
  - $\Delta_{D \to H} = \mathbf{6.21\text{ 半音}}$ (目標 $\ge 4.0\text{ 半音}$ — 合格 ✅)
  - $\Delta_{H \to C} = \mathbf{11.02\text{ 半音}}$ (目標 $\ge 4.0\text{ 半音}$ — 合格 ✅)

### 3. ASR精度（Whisper Base CER）と自然性（UTMOSv2 MOS）
- **ASRエンジン:** `openai-whisper` (`base` model, CPU) 正規化: `ja_cer`.
- **CER中央値:** **9.56%** (CER平均: **10.79%**).
- **マルチテイク第2巡:** CER > 2% のキューに対し Variant 1 を自動生成し最適テイクを採用.
- **UTMOSv2 MOS 自然性スコア:** 平均 **3.02 / 5.0** (範囲: 2.13 – 3.98)。基準値クリア (>= 3.0 / 5.0)。
- **確認対象キュー一覧:** [`02_SAN_XUAT/Tap15_JA/xuat_ban/CanNghe_Tap15_JA_higgs.md`](xuat_ban/CanNghe_Tap15_JA_higgs.md)。

---

## B3. 納品成果物一覧

1. **マスター音源:**
   - MP3: [`02_SAN_XUAT/Tap15_JA/xuat_ban/Tap15_JA_master.mp3`](xuat_ban/Tap15_JA_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap15_JA/xuat_ban/Tap15_JA_master.wav`](xuat_ban/Tap15_JA_master.wav)
2. **タイムライン・字幕データ:**
   - タイムライン: [`.work/timeline_s_JA_t15.json`](../../.work/timeline_s_JA_t15.json) (2151.5 秒)
   - SRT字幕: [`02_SAN_XUAT/Tap15_JA/xuat_ban/Tap15_JA.srt`](xuat_ban/Tap15_JA.srt) (220 cues)
3. **品質レポート:**
   - QC詳細データ: [`.work/quality_qc_utmos_ep15_ja.json`](../../.work/quality_qc_utmos_ep15_ja.json)
   - 人手確認シート: [`02_SAN_XUAT/Tap15_JA/xuat_ban/CanNghe_Tap15_JA_higgs.md`](xuat_ban/CanNghe_Tap15_JA_higgs.md)
