# PRODUCTION CASE FILE EPISODE 25 · "THE YELLOW RAINCOAT KILLER" — EN EDITION

## B1. Episode Information

| Item | Content |
|---|---|
| Episode Title | **Episode 25: The Yellow Raincoat Killer & The Fury of Sociopathic Resentment — Inferiority Mask & The Atrocity of Fake Vigilantism (The Yoo Young-chul File)** |
| True Case | The Seoul Serial Homicides by Yoo Young-chul (Seoul, South Korea, 2003–2004) |
| Psychological Themes | Sociopathic Resentment · Narcissistic Injury · Displaced Aggression · Moral Vigilante Delusion · Moral Neutralization · Genuine Remorse vs. Pathological Self-Pity |
| Format | Criminal Psychology Investigative Documentary (Host-Driven Documentary) — 5 Acts Standard A2/K10 |
| Voice Cast | 4 Voices: **Host** (Owl - 95 sentences) · **Investigator** (Hound - 28 sentences) · **Psychological Expert** (Silver Fox - 27 sentences) · **Ordinary Person** (N1 Massage Parlor Owner: 7 sentences & N2 Victim Family Representative: 8 sentences) |
| Script Scale | **165 sentences** · 51 elements · 32 speech turns |
| Research Supplement | In-depth behavioral research & 10 psychological markers document (`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/NghienCuu_TamLy_BoSung_KichBan_Tap25.md`) dated 2026-11-15 for 3 languages (VN / EN / JA) |
| Safety Standard | **Strict Compliance with Rule V9 (YouTube Safe)**: 0% gore, graphic physical violence, blood, or mutilation; 100% focused on behavioral science and 4 practical warning red flags |
| Visual Assets | **60 shared background images in 2112×1188 (16:9 2K)** with prefix `t25_` located at `assets/bg/` · Dark Graphic Novel Noir style |
| BGM Progression | Somber Cello $\rightarrow$ Chilling Deep Ambient $\rightarrow$ Academic Minimalist Piano $\rightarrow$ Solemn Courtroom Violin $\rightarrow$ Warm Reflective Piano |

---

## B2. Production Pipeline & Multilingual Synchronization

### 1. File Synchronization & Fact-Checking (Completed)
- [x] Historical & judicial fact-checking verified with 100% accuracy via SMPA, Supreme Court of Korea, and Profiler Kwon Il-yong's memoirs (`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/REVIEW_kichban_tap25.md`).
- [x] Multi-perspective behavioral analysis across 5 subjects (Perpetrator, Unconscious Accomplice/Victims, Brave Witness, Victim Families, Society) and multilingual dialogue supplement (`01_KICH_BAN/Ho_So_Toi_Pham/Tap25/NghienCuu_TamLy_BoSung_KichBan_Tap25.md`).
- [x] Updated YouTube video metadata (`description.txt`) and judicial source references (`nguon_tham_khao_EN.md`).

### 2. Next Pipeline Milestones (Quality Gates per `AGENTS.md`)
1. **Gate 1 (Script Approval):** User reviews and approves the psychological supplement; integrates into master scripts `kichban_tap25_23102026.md`, `kichban_tap25_EN.md`, `kichban_tap25_JA.md`.
2. **Gate 2 (Script Parsing):** Parse into `.work/script_tap25_EN.json`.
3. **Gate 3 (Acting & Pause Gate):** Generate acting file with pause gates (`qc_pause_gate.py`).
4. **Gate 4 (TTS Voice Synthesis):** Synthesize voices using Higgs Audio v3 / MiniMax.
5. **Gate 5 (Voice Role Check):** Run `voice_role_check.py` to ensure role consistency.
6. **Gate 6 (Master Audio Mix):** Multi-track audio mix meeting EBUR128 standard (-16 LUFS, TP $\le -1.5$ dBFS).
7. **Gate 7 (Shot List Matching):** Map all sentences to the 60 shared `t25_*` visual assets via `parse_shots.py`.
8. **Gate 8 (Video Render & Mux):** Render picture track with `build_video3.py` and mux subtitles using `package.py --mux`.

---

## B3. 5-Act Structure & Associated Background Assets (60 Images)

All 60 shared visual assets (`assets/bg/t25_*.png`) are organized across 5 acts:
- **Act 1 (12 images):** `t25_yoo_young_chul_a1_01_mapo_police` to `a1_12_escape_police_station_rain`
- **Act 2 (12 images):** `t25_yoo_young_chul_a2_01_handcuff_interrogation` to `a2_12_raincoat_killer_myth`
- **Act 3 (12 images):** `t25_yoo_young_chul_a3_01_profiler_dialogue` to `a3_12_pathological_self_pity`
- **Act 4 (12 images):** `t25_yoo_young_chul_a4_01_seoul_central_court` to `a4_12_justice_restored`
- **Act 5 (12 images):** `t25_yoo_young_chul_a5_01_modern_seoul_skyline` to `a5_12_outtro_subscribe_card`
