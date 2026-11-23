# PRODUCTION DOSSIER EPISODE 27 · "NARCISSISTIC INJURY & CO-CONSPIRATOR MANIPULATION" — EN EDITION

## B1. Episode Information

| Item | Content |
|---|---|
| Episode title | **Episode 27: Narcissistic Injury & Co-Conspirator Manipulation — The Binh Phuoc Mass Murder & The 60-Hour Manhunt (The Nguyen Hai Duong File)** |
| Case file | The 2015 Binh Phuoc mass murder (Minh Hung Commune, Chon Thanh District, Binh Phuoc Province, Vietnam, July 2015) |
| Psychological themes | Narcissistic Injury · Destructive Narcissistic Rage · Borrowed Grandiosity · Psychological Manipulation & Coercion · Point of No Return · Cognitive Freezing & Coerced Compliance · Psychological Compartmentalization · Anatomy of Authentic Remorse vs. Pathological Self-Pity |
| Format | Narrator-Led Investigative Documentary — 5 Acts conforming to A2c/K10 standards |
| Voice cast | 4 Voice Roles: **Host** (Owl - 137 sentences) · **Investigator** (Hound - 37 sentences) · **Psychologist** (Fox - 51 sentences) · **Ordinary person** (N1 Sawmill worker: 7 sentences & N2 Trial observer: 8 sentences) |
| Production script scale | **240 sentences** (Fully expanded from 165 sentences conforming to Episode 10 benchmark) · 51 Elements · 32 speech turns |
| Multilingual parity status | Strict **1:1 Parity synchronization** across 3 languages: **Vietnamese (VN - 240 sentences)**, **English (EN - 240 sentences)**, **Japanese (JA - 240 sentences)** |
| Safety standards | **100% YouTube Safe (Rule V9)**: 0% gore, graphic physical violence, or mechanical injury descriptions; 100% focused on behavioral science and survival red flags |
| Visual assets | **60 standard 2112×1188 (16:9 2K) background stills** prefixed with `t27_` in `assets/bg/` · Dark Graphic Novel Noir style |
| BGM soundtrack | Somber Cello $\rightarrow$ Heavy Cellular Bass $\rightarrow$ Minimalist Clinical Piano $\rightarrow$ Sweeping Courtroom Violin $\rightarrow$ Warm Reflective Piano |

---

## B2. Production & Multilingual Pipeline Roadmap

### 1. Dossier & Reference Synchronization (Completed)
- [x] Verified legal facts against official trial verdicts (No. 60/2015/HSST and No. 384/2016/HSPT) and Ministry of Public Security C45 case briefings.
- [x] Completed deep behavioral research dissecting 5 subject groups and 7 analytical tiers (`01_KICH_BAN/Ho_So_Toi_Pham/Tap27/NghienCuu_TamLy_BoSung_KichBan_Tap27.md`).
- [x] Updated production scripts to 240 sentences in strict 1:1 Parity across VN, EN, JA.
- [x] Automated compilation and verification of pipeline JSON files: `.work/script_tap27.json`, `.work/script_tap27_EN.json`, `.work/script_tap27_JA.json`.
- [x] Comprehensive review report assessing multilingual parity and 10 psychological indicators (`01_KICH_BAN/Ho_So_Toi_Pham/Tap27/REVIEW_kichban_tap27_multilingual.md`).

### 2. Next Production Steps (Gated Workflow per `AGENTS.md`)
1. **Gate 1 (Script Approval):** Script upgraded to 240 sentences, passing 0 V9 errors and 100% Parity.
2. **Gate 2 (Script Parsing):** Parsed via `parse_kichban.py` into production JSON files.
3. **Gate 3 (Acting & Pauses):** Generate `acting_tap27_EN.json` measuring inter-sentence pauses per `qc_pause_gate.py`.
4. **Gate 4 (TTS Voice Synthesis):** Generate voice tracks for all 4 roles using configured voice models.
5. **Gate 5 (Voice Role Check):** Run `voice_role_check.py` ensuring identity consistency per role.
6. **Gate 6 (Master Audio Build):** Mix Voice + SFX + BGM adhering to EBUR128 (-16 ± 1 LUFS, TP $\le -1.5$ dBFS).
7. **Gate 7 (Shot Parsing):** Map 100% sentences to 60 background assets via `parse_shots.py`.
8. **Gate 8 (Video Render & Packaging):** Render visual timeline via `build_video3.py` and mux subtitles with `package.py --mux`.
