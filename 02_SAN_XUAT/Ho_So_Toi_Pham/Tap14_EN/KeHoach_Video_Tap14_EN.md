# PRODUCTION PLAN EPISODE 14 · ENGLISH EDITION · "THE BETTY BRODERICK TRAGEDY"

## B1. Episode Overview

| Field | Content |
|---|---|
| Episode Title | **Episode 14: When a Gaslighting Victim Crosses the Line into Murder (The Betty Broderick Case)** |
| True Crime Case | Elisabeth 'Betty' Broderick, Daniel Broderick & Linda Kolkena — La Jolla & Marston Hills, San Diego, California, USA (Nov 5, 1989) |
| Psychology Core | Gaslighting, Narcissistic Injury, Psychological Snapping, Compartmentalization & 10-Indicator Behavioral Ecosystem |
| Total Duration | **1922.4 s (~32 min 02 sec)** · 5 Acts · **210 cues** |
| Characters / Voice | Host (Owl) · Investigator (Wolf) · Psychologist (Fox) · N1 (La Jolla Friend) · N2 (Kim Broderick - Eldest Daughter) |
| TTS Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| Reference Voices | **VoxCPM2 Voice Design EN** (H: `H_EN.wav`, D: `D_EN.wav`, C: `C_EN.wav`, N1: `N1_EN.wav`, N2: `N2_EN.wav`) |
| Sound Engineering | 3-Layer Stereo: 5-Act BGM + Continuous Ambience + Targeted SFX (`.work/sfx_tap14_EN.json`) |
| Master Output | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap14_EN/xuat_ban/Tap14_EN_master.mp3` & `02_SAN_XUAT/Ho_So_Toi_Pham/Tap14_EN/xuat_ban/Tap14_EN_master.wav` |

---

## B2. Audio Quality Control Metrics

### 1. Loudness Compliance (EBUR128)
- **Integrated Loudness ($I$):** **** (Standard: $-16 \pm 1\text{ LUFS}$ — PASS ✅)
- **True Peak ($TP$):** **** (Standard: $\le -1.5\text{ dBFS}$ — PASS ✅)
- **Loudness Range ($LRA$):** ****
- **Absolute Silence ($> 0.3\text{ s}$ at $-60\text{ dBFS}$):** **0 errors** (PASS ✅ Rule A1 / V4)
- **First Voice Cue:** 23.0 s (post-intro 22.41 s — PASS ✅)
- **Last Voice Cue:** 1913.4 s, episode ends at 1922.4 s with smooth piano fade out (PASS ✅)

### 2. Pitch Separation & Character Identity (G9 Rule)
- **Host ($H$ · Owl):** Median F0 = **112.7 Hz**
- **Investigator ($D$ · Wolf):** Median F0 = **83.6 Hz**
- **Psychologist ($C$ · Fox):** Median F0 = **186.0 Hz**
- **La Jolla Friend ($N1$ · Sheep):** Median F0 = **164.2 Hz**
- **Kim Broderick ($N2$ · Cat):** Median F0 = **241.2 Hz**
- **Pitch Distance:**
  - $\Delta_{D \to H} = \mathbf{5.16\text{ semitones}}$ (Target $\ge 4.0\text{ nc}$ — PASS ✅)
  - $\Delta_{H \to C} = \mathbf{8.68\text{ semitones}}$ (Target $\ge 4.0\text{ nc}$ — PASS ✅)

### 3. ASR Accuracy (Whisper Base CER) & Naturalness (UTMOSv2 MOS)
- **ASR Engine:** `openai-whisper` (`base` model, CPU) via `en_cer` normalization.
- **Median CER:** **0.00%** (Mean CER: **0.43%**).
- **Multi-take Pass 2:** Auto-generated Variant 1 for cues with CER > 2% and selected optimal take.
- **UTMOSv2 MOS Naturalness:** Mean **3.42 / 5.0** (Range: 2.63 – 4.27). Passed threshold (>= 3.0 / 5.0).
- **Review Report:** [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap14_EN/xuat_ban/CanNghe_Tap14_EN_higgs.md`](xuat_ban/CanNghe_Tap14_EN_higgs.md).

---

## B3. Deliverables Inventory

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap14_EN/xuat_ban/Tap14_EN_master.mp3`](xuat_ban/Tap14_EN_master.mp3)
   - WAV: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap14_EN/xuat_ban/Tap14_EN_master.wav`](xuat_ban/Tap14_EN_master.wav)
2. **Timeline & Subtitles:**
   - Timeline: [`.work/timeline_s_EN_t14.json`](../../.work/timeline_s_EN_t14.json) (1922.4 s)
   - Subtitles SRT: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap14_EN/xuat_ban/Tap14_EN.srt`](xuat_ban/Tap14_EN.srt) (210 cues)
3. **Quality Reports:**
   - Full QC Log: [`.work/quality_qc_utmos_ep14_en.json`](../../.work/quality_qc_utmos_ep14_en.json)
   - Human Review Sheet: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap14_EN/xuat_ban/CanNghe_Tap14_EN_higgs.md`](xuat_ban/CanNghe_Tap14_EN_higgs.md)
