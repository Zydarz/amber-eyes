# PRODUCTION PLAN EPISODE 20 · "MOMENT OF COLLAPSE ON CAMERA" — EN EDITION

## B1. Episode Information

| Item | Details |
|---|---|
| Episode Title | **Episode 20: Moment of Collapse on Camera — Predatory Stalking & The Bizarre Freeze Response (Stephen McDaniel Case)** |
| Case Background | Lauren Giddings Case at Mercer University Walter F. George School of Law (Macon, Georgia, USA, 2011–2014) |
| Psychological Themes | Predatory Stalker · Predatory Voyeurism · Covert Narcissism · Physiological Freeze Response / Tonic Immobility & Micro-expressions on live broadcast · Cognitive Compartmentalization · Theory of Mind Deficit · Precipitating Trigger & Narcissistic Injury · **CORE EMPHASIS:** Instrumental Remorse & Pathological Self-Pity vs. Authentic Remorse in McDaniel's plea agreement · Moral Injury from Master Key Negligence by property management · Survival Intuition & The Gift of Fear (Gavin de Becker) in Lauren Giddings · Classmates' Bystander Guilt & Family's Moral Fortitude · Academic Sanctuary Illusion & Institutional Student Housing Reforms |
| Format | Forensic Psychological Documentary (Host-Driven) — 5 Acts Standard A2c/K10 |
| Cast Allocation | 4 Primary Voices: **Host (Owl)** (132 sentences) · **Lead Detective (Wolf)** (43 sentences) · **Psychologist (Fox)** (42 sentences) · **Everyday People (N1/N2)**: N1 Mercer Law Classmate (10 sentences at `1.07`) & N2 Giddings Family Representative (9 sentences at `4.09`) |
| Script Scale | **241 sentences** (expanded +29 deep psychological sentences across 5 subjects) · 51 Elements · 32 LOI turns |
| Estimated Runtime | **~28.0 – 30.0 minutes** · Amber eyes Golden Benchmark Standard |
| Multilingual Alignment | **Absolute 1:1 Parity:** Vietnamese (VN: 241), English (EN: 241), Japanese (JA: 241), Korean (KO: 241) |
| YouTube Safety | **Strict Rule V9 Compliance**: 0% gore or graphic violence; 100% focused on behavioral science, interrogation psychology, and 4 practical survival red flags |
| Visual Assets | **63 2112×1188 (16:9 2K) Backgrounds** with prefix `t20_` at `assets/bg/` · Dark Graphic Novel Noir |
| Soundtrack (BGM) | `bgm_cello_sad.mp3` $\rightarrow$ `bgm_ambient_deep.mp3` $\rightarrow$ `bgm_piano_minimal.mp3` $\rightarrow$ `bgm_violin_heart.mp3` $\rightarrow$ `bgm_piano_warm.mp3` |
| Research Reference | [`01_KICH_BAN/Tap20/NghienCuu_TamLy_BoSung_KichBan_Tap20.md`](../../01_KICH_BAN/Tap20/NghienCuu_TamLy_BoSung_KichBan_Tap20.md) |

---

## B2. Production Pipeline Roadmap

### 1. Dossier & Historical Synchronization (Completed)
- [x] Legal and historical facts verified against Bibb County Superior Court records, Macon Police Department, Georgia Bureau of Investigation (GBI), and the WGXA live interview from June 30, 2011.
- [x] Comprehensive behavioral research completed for all 5 subjects, detailing the mechanisms of remorse and psychological defense (`01_KICH_BAN/Tap20/NghienCuu_TamLy_BoSung_KichBan_Tap20.md`).
- [x] Multilingual scripts upgraded to **241 sentences** with 1:1 Parity (`01_KICH_BAN/Tap20/REVIEW_kichban_tap20_multilingual.md`).
- [x] Production acting parameters and pauses established (`acting_tap20_EN.json`), passing `qc_pause_gate.py --pre` with 144 pause cues (60%).

### 2. Pipeline Production Steps
1. **Step 1 (Script Approval):** 241-sentence script verified under 10 Behavioral Indicators (A2c) and Rule K10.
2. **Step 2 (Script Parsing):** Parsed to `.work/script_tap20_EN.json` (241 sentences, 51 elements).
3. **Step 3 (Acting & Pauses):** Verified in `acting_tap20_EN.json` (Rule A13, median pause $\ge 0.6$ s).
4. **Step 4 (TTS Voice Synthesis):** Higgs Audio v3 / MiniMax configured via `edition.py`.
5. **Step 5 (Voice Role Check):** Consistent character identity without pitch alteration (Rule G5: pitch=0).
6. **Step 6 (Master Audio):** Mixed at -16 LUFS, True Peak $\le -1.5$ dBFS, 0 silent gaps $> 0.3$ s.
7. **Step 7 (Shot Table Matching):** 100% matched with 63 shared backgrounds (`t20_*`) via `parse_shots.py`.
8. **Step 8 (Rendering & Packaging):** Final video rendered with `build_video3.py` and muxed via `package.py --mux`.

---

## B3. 5 Acts & 10 Behavioral Indicators Structure

### ACT 1: THE FATEFUL INTERVIEW & THE UNEXPECTED DISCOVERY
- **Runtime:** ~6.5 mins · **55 sentences** (enhanced at `1.02`, `1.07`, `1.10`)
- **BGM:** `bgm_cello_sad.mp3` (Ominous dark ambient, slow deep drums, metallic clock ticking)
- **Psychological Focus:** Academic Sanctuary Illusion at Mercer Law (`1.02`); McDaniel playing the devoted friend on WGXA; Lauren's intuitive dread and classmates' bystander guilt (`1.07`); live narcissistic collapse on camera when news of the dumpster discovery breaks (`1.10`).

### ACT 2: THE STONE STATUE IN THE INTERROGATION ROOM & COGNITIVE SHOCK
- **Runtime:** ~5.5 mins · **47 sentences** (enhanced at `2.02`, `2.06`, `2.10`)
- **BGM:** `bgm_ambient_deep.mp3` (Cold minimalist ambient, steady electronic ticking)
- **Psychological Focus:** Artificially simulated immobility for 12+ hours to suppress micro-expressions (`2.02`); discovery of the master key exposing property management negligence (`2.06`); forensic recovery of digital search history demonstrating escalating voyeuristic addiction (`2.10`).

### ACT 3: PSYCHOLOGICAL DISSECTION: THE PREDATORY STALKER & TONIC IMMOBILITY
- **Runtime:** ~6.0 mins · **49 sentences** (enhanced at `3.03`, `3.05`, `3.07`)
- **BGM:** `bgm_piano_minimal.mp3` (Minimalist piano with deep drone, clinical academic atmosphere)
- **Psychological Focus:** Predatory voyeurism and severe Theory of Mind deficit (`3.03`); Lauren's packed moving boxes triggering acute narcissistic injury and homicidal compulsion (`3.05`); cognitive compartmentalization and biological tonic immobility reflex (`3.07`).

### ACT 4: THE LIFE VERDICT & RETRIBUTION OF JUSTICE
- **Runtime:** ~6.5 mins · **54 sentences** (enhanced at `4.02`, `4.06`, `4.10`, `4.11` — **CORE EMPHASIS**)
- **BGM:** `bgm_violin_heart.mp3` (Tense violin with resonant court gavel strikes)
- **Psychological Focus:** Arrogance crushed after 3 years in confinement (`4.02`); the plea bargain as cowardly instrumental remorse to dodge the death penalty (`4.06`); enduring moral injury suffered by negligent building staff (`4.10`); forensic distinction between authentic remorse and pathological self-pity (`4.11`); family's triumphant moral dignity and life sentence without parole for 30 years (`4.09`).

### ACT 5: AWAKENING LESSONS & 4 RED FLAGS AGAINST COVERT STALKING
- **Runtime:** ~4.5 mins · **36 sentences** (enhanced at `5.02`, `5.03`, `5.04`)
- **BGM:** `bgm_piano_warm.mp3` (Warm dignified piano, reflective philosophy)
- **Psychological Focus:** Nationwide institutional reforms in campus housing security (`5.02`); structural security custody lessons (`5.03`); survival philosophy of *The Gift of Fear* (`5.04`); 4 classic red flags for detecting covert predators (`5.05`).

---

## B4. Quality Control Verification (QC Gates)

| QC Gate | Standard Benchmark | Result | Status |
|---|---|---|:---:|
| **Gate 1: YouTube Safe (V9)** | AGENTS.md & §A9.2 | 0 forbidden words, 0% graphic violence | ✅ PASS |
| **Gate 2: Punctuation & Ellipsis (G1)** | Rule G1 & G6 | 0 ellipsis `...`/`…`, natural cadence | ✅ PASS |
| **Gate 3: Exact Measurement (L3)** | Rule L3 | 241 sentences, 51 elements, 32 LOI turns | ✅ PASS |
| **Gate 4: 10 Behavioral Indicators (A2c)** | §A2c & Rule K10 | 10 indicators verified across 5 subjects | ✅ PASS |
| **Gate 5: Multilingual Parity** | Rule L8 & §A2b | 100% parity across VN, EN, JA, KO | ✅ PASS |
| **Gate 6: Pause Pre-gate (A13)** | Rule A13 & `qc_pause_gate.py` | 144 pause cues (60%), median $\ge 0.6$ s | ✅ PASS |
| **Gate 7: Shared Visual Assets (H17)** | Rule H17 | 63 `t20_` backgrounds shared across all editions | ✅ PASS |
