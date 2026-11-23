# PRODUCTION DOSSIER · EPISODE 19 · "13 CAPTIVE CHILDREN IN A SUBURBAN DUNGEON — COERCIVE CONTROL & SURVIVAL LEAP"

## B1. Episode Overview

| Field | Detail |
|---|---|
| Title | **Ep. 19: 13 Captive Children in a Suburban Dungeon — Coercive Control, Shared Delusional Disorder & The Leap for Survival (The Turpin Family Case)** |
| Case | Turpin Family Captivity & Torture Case — Perris, California (Jan 14, 2019) |
| Psychological Focus | Coercive Control, Folie à Deux (Shared Psychotic Disorder), Deliberate Infantilization & Survival Resilience |
| Total Duration | **2024.5 s (~33 min 44 sec)** · 5 Acts · **241 cues** |
| Voice Cast | Host (Owl) · Investigator (Wolf) · Expert (Fox) · N1 (911 Dispatcher · Riverside County) · N2 (Healthcare Representative · Riverside University Health System) |
| TTS Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) on Apple Silicon MLX |
| Reference Dataset | **VoxCPM2 Voice Design (EN)** (H: `H_EN.wav`, D: `D_EN.wav`, C: `C_EN.wav`, N1: `N1_EN.wav`, N2: `N2_EN.wav`) |
| Soundscape | 3-Layer Stereo: 5-Act BGM + Continuous Ambience + Dynamic SFX (`.work/sfx_tap19_EN.json`) |
| Final Master Audio | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap19_EN/xuat_ban/Tap19_EN_master.mp3` & `02_SAN_XUAT/Ho_So_Toi_Pham/Tap19_EN/xuat_ban/Tap19_EN_master.wav` |

---

## B2. Audio Quality Control Metrics (QC Metrics)

### 1. Loudness Normalization (EBUR128 Standard)
- **Integrated Loudness ($I$):** **** (Standard: $-16 \pm 1\text{ LUFS}$ — PASS ✅)
- **True Peak ($TP$):** **** (Standard: $\le -1.5\text{ dBFS}$ — PASS ✅)
- **Loudness Range ($LRA$):** ****
- **Absolute Silence ($> 0.3\text{ s}$ at $-60\text{ dBFS}$):** **0 errors** (PASS ✅ Rule A1 / V4)
- **First cue onset:** 23.0 s (after 22.41 s Intro — PASS ✅)
- **Last cue end:** 2015.5 s, concluding total audio at 2024.5 s with smooth piano fade out (PASS ✅)

### 2. Pitch Separation & Speaker Differentiation (Rule G9)
- **Host ($H$ · Owl):** Median F0 = **112.1 Hz**
- **Investigator ($D$ · Wolf):** Median F0 = **84.5 Hz**
- **Expert ($C$ · Fox):** Median F0 = **186.0 Hz**
- **911 Dispatcher ($N1$ · Sheep):** Median F0 = **167.8 Hz**
- **Healthcare Rep ($N2$ · Cat):** Median F0 = **240.0 Hz**
- **Pitch Distance:**
  - $\Delta_{D \to H} = \mathbf{4.90\text{ semitones}}$ (Target $\ge 4.0\text{ st}$ — PASS ✅)
  - $\Delta_{H \to C} = \mathbf{8.76\text{ semitones}}$ (Target $\ge 4.0\text{ st}$ — PASS ✅)

### 3. Speech Recognition Accuracy (Whisper Base CER) & Naturalness (UTMOSv2 MOS)
- **ASR Engine:** `faster-whisper` (`base` model, CPU) with `en_cer` normalization.
- **Median CER:** **0.00%** (Mean CER: **0.61%**).
- **Round 2 Multi-take:** Automatically generated Variant 1 with new deterministic seeds for cues with CER > 2%, selecting the best take.
- **Naturalness UTMOSv2 MOS:** Mean = **3.46 / 5.0** (Range: 2.38 – 4.12). Passed standard (>= 3.0 / 5.0).
- **Review List:** [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap19_EN/xuat_ban/CanNghe_Tap19_EN_higgs.md`](xuat_ban/CanNghe_Tap19_EN_higgs.md).

---

## B3. Deliverables Summary

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap19_EN/xuat_ban/Tap19_EN_master.mp3`](xuat_ban/Tap19_EN_master.mp3)
   - WAV: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap19_EN/xuat_ban/Tap19_EN_master.wav`](xuat_ban/Tap19_EN_master.wav)
2. **Timeline Data & Subtitles:**
   - Timeline: [`.work/timeline_s_EN_t19.json`](../../.work/timeline_s_EN_t19.json) (2024.5 s)
   - Subtitles SRT: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap19_EN/xuat_ban/Tap19_EN.srt`](xuat_ban/Tap19_EN.srt) (241 cues)
3. **Monitoring Reports:**
   - Detailed QC: [`.work/quality_qc_utmos_ep19_en.json`](../../.work/quality_qc_utmos_ep19_en.json)
   - Review Table: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap19_EN/xuat_ban/CanNghe_Tap19_EN_higgs.md`](xuat_ban/CanNghe_Tap19_EN_higgs.md)
