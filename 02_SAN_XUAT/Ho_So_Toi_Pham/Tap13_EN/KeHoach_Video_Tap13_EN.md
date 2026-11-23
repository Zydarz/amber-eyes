# PRODUCTION PLAN EPISODE 13 · ENGLISH EDITION · "THE GOLDEN CHILD FAÇADE"

## B1. Episode Overview

| Field | Content |
|---|---|
| Episode Title | **Episode 13: The 'Golden Child' Façade & The 10-Year Deception (Jennifer Pan Case)** |
| True Crime Case | Jennifer Pan Staged Home Invasion — Markham, Ontario, Canada (Nov 8, 2010) |
| Psychology Core | Tiger Parenting, Maladaptive Perfectionism, Pathological Lying, Identity Fragmentation & 10-Indicator Behavioral Ecosystem |
| Total Duration | **1820.4 s (~30 min 20 sec)** · 5 Acts · **210 cues** |
| Characters / Voice | Host (Owl) · Investigator (Wolf) · Psychologist (Fox) · N1 (High School Friend) · N2 (Huei Hann Pan, Surviving Father) |
| TTS Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| Reference Voices | **VoxCPM2 Voice Design EN** (H: `H_EN.wav`, D: `D_EN.wav`, C: `C_EN.wav`, N1: `N1_EN.wav`, N2: `N2_EN.wav`) |
| Sound Engineering | 3-Layer Stereo: 5-Act BGM + Continuous Ambience + Targeted SFX (`.work/sfx_tap13_EN.json`) |
| Master Output | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap13_EN/xuat_ban/Tap13_EN_master.mp3` & `02_SAN_XUAT/Ho_So_Toi_Pham/Tap13_EN/xuat_ban/Tap13_EN_master.wav` |

---

## B2. Audio Quality Control Metrics

### 1. Loudness Compliance (EBUR128)
- **Integrated Loudness ($I$):** **** (Standard: $-16 \pm 1\text{ LUFS}$ — PASS ✅)
- **True Peak ($TP$):** **** (Standard: $\le -1.5\text{ dBFS}$ — PASS ✅)
- **Loudness Range ($LRA$):** ****
- **Absolute Silence ($> 0.3\text{ s}$ at $-60\text{ dBFS}$):** **0 errors** (PASS ✅ Rule A1 / V4)
- **First Voice Cue:** 23.0 s (post-intro 22.41 s — PASS ✅)
- **Last Voice Cue:** 1811.4 s, episode ends at 1820.4 s with smooth piano fade out (PASS ✅)

### 2. Pitch Separation & Character Identity (G9 Rule)
- **Host ($H$ · Owl):** Median F0 = **112.1 Hz**
- **Investigator ($D$ · Wolf):** Median F0 = **84.2 Hz**
- **Psychologist ($C$ · Fox):** Median F0 = **189.0 Hz**
- **High School Friend ($N1$ · Sheep):** Median F0 = **171.4 Hz**
- **Huei Hann Pan ($N2$ · Cat):** Median F0 = **240.0 Hz**
- **Pitch Distance:**
  - $\Delta_{D \to H} = \mathbf{4.96\text{ semitones}}$ (Target $\ge 4.0\text{ nc}$ — PASS ✅)
  - $\Delta_{H \to C} = \mathbf{9.03\text{ semitones}}$ (Target $\ge 4.0\text{ nc}$ — PASS ✅)

### 3. ASR Accuracy (Whisper Base CER) & Naturalness (UTMOSv2 MOS)
- **ASR Engine:** `openai-whisper` (`base` model, CPU) via `en_cer` normalization.
- **Median CER:** **0.00%** (Mean CER: **0.60%**).
- **Multi-take Pass 2:** Auto-generated Variant 1 for cues with CER > 2% and selected optimal take.
- **UTMOSv2 MOS Naturalness:** Mean **3.45 / 5.0** (Range: 2.47 – 4.17). Passed threshold (>= 3.0 / 5.0).
- **Review Report:** [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap13_EN/xuat_ban/CanNghe_Tap13_EN_higgs.md`](xuat_ban/CanNghe_Tap13_EN_higgs.md).

---

## B3. Deliverables Inventory

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap13_EN/xuat_ban/Tap13_EN_master.mp3`](xuat_ban/Tap13_EN_master.mp3)
   - WAV: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap13_EN/xuat_ban/Tap13_EN_master.wav`](xuat_ban/Tap13_EN_master.wav)
2. **Timeline & Subtitles:**
   - Timeline: [`.work/timeline_s_EN_t13.json`](../../.work/timeline_s_EN_t13.json) (1820.4 s)
   - Subtitles SRT: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap13_EN/xuat_ban/Tap13_EN.srt`](xuat_ban/Tap13_EN.srt) (210 cues)
3. **Quality Reports:**
   - Full QC Log: [`.work/quality_qc_utmos_ep13_en.json`](../../.work/quality_qc_utmos_ep13_en.json)
   - Human Review Sheet: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap13_EN/xuat_ban/CanNghe_Tap13_EN_higgs.md`](xuat_ban/CanNghe_Tap13_EN_higgs.md)
