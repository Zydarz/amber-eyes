# 制作計画 第12話 · 日本語版 · 「ジョーンズタウンの悲劇」

**適用基準:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**台本:** `01_KICH_BAN/Tap12_JA/kichban_tap12_JA.md` · **出力先:** `02_SAN_XUAT/Tap12_JA/xuat_ban/`  
**日付:** 2026年11月14日

---

## B1. エピソード情報

| 項目 | 内容 |
|---|---|
| 台本 | `01_KICH_BAN/Tap12_JA/kichban_tap12_JA.md` — 53要素 · **249 文** |
| 音声エンジン | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — 参照音声セット: VoxCPM2 Japanese (`H_JA`, `D_JA`, `C_JA`, `N1_JA`, `N2_JA`)。感情タグなし (M4)。事前エンコード済み (M1)。末尾無音トリム済み (M3)。 |
| マスター出力 | `02_SAN_XUAT/Tap12_JA/xuat_ban/Tap12_JA_master.mp3` (**2519.4 秒 / ~41 分 59 秒** · **統合ラウドネス: -16.2 LUFS** · **True Peak: -1.7 dBFS** · **無音 > 0.3 秒 ゼロ**) |
| 品質管理 (ASR & CER) | **Whisper Base CER:** 平均 = **8.67%**, 中央値 = **8.11%** (229/249 文 > 2%)。目標 (< 2.0%)。 |
| 品質管理 (自然さ MOS) | **UTMOSv2 MOS:** 平均 = **2.95 / 5.0** (範囲: 2.11 – 3.88)。目標 (>= 3.0 / 5.0)。 |
| ピッチ分離 (規則 G9) | **D (オオカミ):** 87.4 Hz · **H (フクロウ):** 121.8 Hz ($\Delta = +5.76$ 半音) · **C (キツネ):** 227.5 Hz ($\Delta = +10.81$ 半音)。 |
| 配役 | H: ホスト (フクロウ) · D: 捜査官 (オオカミ) · C: 心理学者 (キツネ) · N1: レスリー・ワグナー＝ウィルソン (元信者・羊) · N2: FBI捜査官 (猫) |
| 映像構造 | 53要素 · 5幕構成 · 字幕: `Tap12_JA.srt` |

---

## B2. 納品ファイル一覧

1. **マスター音声:**
   - MP3: [`02_SAN_XUAT/Tap12_JA/xuat_ban/Tap12_JA_master.mp3`](xuat_ban/Tap12_JA_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap12_JA/xuat_ban/Tap12_JA_master.wav`](xuat_ban/Tap12_JA_master.wav)
2. **タイムライン＆字幕:**
   - タイムライン: [`.work/timeline_s_JA_t12.json`](../../.work/timeline_s_JA_t12.json) (2519.4 秒)
   - 字幕: [`02_SAN_XUAT/Tap12_JA/xuat_ban/Tap12_JA.srt`](xuat_ban/Tap12_JA.srt) (249 cues)
3. **QC レポート:**
   - 品質レポート: [`.work/quality_qc_utmos_ep12_ja.json`](../../.work/quality_qc_utmos_ep12_ja.json)
   - 確認文リスト: [`02_SAN_XUAT/Tap12_JA/CanNghe_Tap12_JA_higgs.md`](xuat_ban/CanNghe_Tap12_JA_higgs.md)
