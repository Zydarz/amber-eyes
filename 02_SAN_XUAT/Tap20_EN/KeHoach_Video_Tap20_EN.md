# PRODUCTION DOSSIER · EPISODE 20 · "ANNIHILATING HIS ENTIRE FAMILY TO 'SEND THEM TO HEAVEN' — JOHN LIST"

## B1. Episode Overview

| Field | Detail |
|---|---|
| Title | **Ep. 20: Annihilating His Entire Family to 'Send Them to Heaven' — OCPD & The 18-Year Flight (The John List Case)** |
| Case | John Emil List Familicide — Breeze Knoll, Westfield, New Jersey (Nov 9, 1971) |
| Psychological Focus | Obsessive-Compulsive Personality Disorder (OCPD), Moral Neutralization & False Salvation, 18-Year Fugitive Flight as Robert Clark & Frank Bender's Forensic Bust |
| Total Duration | **2054.1 s (~34 min 14 sec)** · 5 Acts · **241 cues** |
| Voice Cast | Host (Owl) · Investigator (Wolf) · Expert (Fox) · N1 (Jean Phillips · Drama Teacher) · N2 (Wanda Flanery · Colorado Neighbor) |
| TTS Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| Reference Dataset | **VoxCPM2 Voice Design (EN)** (H: `H_EN.wav`, D: `D_EN.wav`, C: `C_EN.wav`, N1: `N1_EN.wav`, N2: `N2_EN.wav`) |
| Soundscape | 3-Layer Stereo: 5-Act BGM + Continuous Ambience + Dynamic SFX (`.work/sfx_tap20_EN.json`) |
| Final Master Audio | `02_SAN_XUAT/Tap20_EN/xuat_ban/Tap20_EN_master.mp3` & `02_SAN_XUAT/Tap20_EN/xuat_ban/Tap20_EN_master.wav` |

---

## B2. Audio Quality Control Metrics (QC Metrics)

### 1. Loudness Normalization (EBUR128 Standard)
- **Integrated Loudness ($I$):** **** (Standard: $-20 \pm 1\text{ LUFS}$ — PASS ✅)
- **True Peak ($TP$):** **** (Standard: $\le -1.5\text{ dBFS}$ — PASS ✅)
- **Loudness Range ($LRA$):** ****
- **Absolute Silence ($> 0.3\text{ s}$ at $-60\text{ dBFS}$):** **0 errors** (PASS ✅ Rule A1 / V4)
- **First cue onset:** 23.0 s (after 22.41 s Intro — PASS ✅)
- **Last cue end:** 2045.1 s, concluding total audio at 2054.1 s with smooth piano fade out (PASS ✅)

### 2. Pitch Separation & Speaker Differentiation (Rule G9)
- **Host ($H$ · Owl):** Median F0 = **112.1 Hz**
- **Investigator ($D$ · Wolf):** Median F0 = **85.1 Hz**
- **Expert ($C$ · Fox):** Median F0 = **189.7 Hz**
- **Jean Phillips ($N1$ · Sheep):** Median F0 = **165.0 Hz**
- **Wanda Flanery ($N2$ · Cat):** Median F0 = **228.6 Hz**
- **Pitch Distance:**
  - $\Delta_{D \to H} = \mathbf{4.78\text{ semitones}}$ (Target $\ge 4.0\text{ st}$ — PASS ✅)
  - $\Delta_{H \to C} = \mathbf{9.10\text{ semitones}}$ (Target $\ge 4.0\text{ st}$ — PASS ✅)

### 3. Speech Accuracy (Whisper Base CER) & Naturalness (UTMOSv2 MOS)
- **ASR Engine:** `faster-whisper` (`base` model, CPU) with `en_cer` normalization.
- **Median CER:** **0.00%** (Mean CER: **0.42%**).
- **Multi-take Round 2:** Generated Variant 1 with fresh seed for cues with CER > 2% and selected optimal take.
- **Naturalness UTMOSv2 MOS:** Mean **3.43 / 5.0** (Range: 2.50 – 4.09). Passed standard (>= 3.0 / 5.0).
- **Human verification report:** [`02_SAN_XUAT/Tap20_EN/xuat_ban/CanNghe_Tap20_EN_higgs.md`](xuat_ban/CanNghe_Tap20_EN_higgs.md).

---

## B3. Deliverables Inventory

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap20_EN/xuat_ban/Tap20_EN_master.mp3`](xuat_ban/Tap20_EN_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap20_EN/xuat_ban/Tap20_EN_master.wav`](xuat_ban/Tap20_EN_master.wav)
2. **Timeline & Subtitles:**
   - Timeline: [`.work/timeline_s_EN_t20.json`](../../.work/timeline_s_EN_t20.json) (2054.1 s)
   - Subtitles SRT: [`02_SAN_XUAT/Tap20_EN/xuat_ban/Tap20_EN.srt`](xuat_ban/Tap20_EN.srt) (241 cues)
3. **Verification Reports:**
   - QC Raw Data: [`.work/quality_qc_utmos_ep20_en.json`](../../.work/quality_qc_utmos_ep20_en.json)
   - Verification Sheet: [`02_SAN_XUAT/Tap20_EN/xuat_ban/CanNghe_Tap20_EN_higgs.md`](xuat_ban/CanNghe_Tap20_EN_higgs.md)
