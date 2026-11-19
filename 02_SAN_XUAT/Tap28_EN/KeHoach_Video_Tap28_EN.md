# PRODUCTION DOSSIER EPISODE 28 · "STORMY NIGHT FRENZY & JUVENILE TRAGEDY" — EN EDITION
## THE LE VAN LUYEN CASE FILE — THE NGOC BICH GOLD SHOP MASS ROBBERY

## B1. Episode Information

| Item | Content |
|---|---|
| Episode title | **Episode 28: Stormy Night Frenzy & Juvenile Tragedy — The Ngoc Bich Gold Shop Robbery & The Cross-Border Manhunt (The Le Van Luyen File)** |
| Case file | The Ngoc Bich Gold Shop Robbery (Pho San, Phuong Son Commune, Luc Nam District, Bac Giang Province, Vietnam, August 2011) |
| Psychological themes | Juvenile Criminal Psychology · Biological Prefrontal Cortex Underdevelopment · Virtual Desensitization from Online Gaming · Cornered Rat Syndrome / Panic-Induced Frenzy · Blind Familial Concealment & Tribal Protection Instincts · Lifelong Trauma & Survivor Guilt (*Complex PTSD & Survivor Guilt*) · Deconstructing Remorse: Ego-Centric Self-Pity vs. Authentic Moral Remorse |
| Format | Narrator-Led Investigative Documentary — 5 Acts conforming to A2c/K10 standards |
| Voice cast | 4 Voice Roles: **Host** (Owl - 137 sentences) · **Investigator** (Hound - 37 sentences) · **Psychologist** (Fox - 51 sentences) · **Ordinary person** (N1 Pho San resident: 7 sentences & N2 Courtroom observer: 8 sentences) |
| Production script scale | **240 sentences** (Fully expanded from 165 sentences conforming to Episode 10 benchmark) · 51 Elements · 32 speech turns |
| Multilingual parity status | Strict **1:1 Parity synchronization** across 3 languages: **Vietnamese (VN - 240 sentences)**, **English (EN - 240 sentences)**, **Japanese (JA - 240 sentences)** |
| Safety standards | **100% YouTube Safe (Rule V9)**: 0% gore, graphic physical violence, or mechanical injury descriptions; 100% focused on behavioral science, investigative procedures, humanitarian principles, and 4 nocturnal break-in red flags |
| Visual assets | **60 standard 2112×1188 (16:9 2K) background stills** prefixed with `t28_` in `assets/bg/` · Dark Graphic Novel Noir style |
| BGM soundtrack | Stormy Somber Cello $\rightarrow$ Driving Manhunt Heavy Bass $\rightarrow$ Minimalist Clinical Academic Piano $\rightarrow$ Solemn Courtroom Violin $\rightarrow$ Warm Reflective Humanistic Piano |

---

## B2. Production & Multilingual Pipeline Roadmap

### 1. Dossier & Reference Synchronization (Completed)
- [x] Verified legal facts against official trial verdicts (No. 03/2012/HSST and No. 186/2012/HSPT) and Bac Giang Provincial Procuracy indictment (`01_KICH_BAN/Tap28/REVIEW_kichban_tap28.md`).
- [x] Completed deep behavioral research dissecting 5 subject groups and the psychology of remorse (`01_KICH_BAN/Tap28/NghienCuu_TamLy_BoSung_KichBan_Tap28.md`).
- [x] Updated production scripts to 240 sentences in strict 1:1 Parity across VN, EN, JA.
- [x] Automated compilation and verification of pipeline JSON files: `.work/script_tap28.json`, `.work/script_tap28_EN.json`, `.work/script_tap28_JA.json`.
- [x] Comprehensive review report assessing multilingual parity, 9 Golden Rules V1–V9, and A2c/K10 standards (`01_KICH_BAN/Tap28/REVIEW_kichban_tap28.md`).

### 2. Next Production Steps (Gated Workflow per `AGENTS.md`)
1. **Gate 1 (Script Approval):** Script upgraded to 240 sentences, passing 0 V9 errors and 100% Parity.
2. **Gate 2 (Script Parsing):** Parsed via `parse_kichban.py` into production JSON files.
3. **Gate 3 (Acting & Pauses):** Generate `acting_tap28_EN.json` measuring inter-sentence pauses per `qc_pause_gate.py`.
4. **Gate 4 (TTS Voice Synthesis):** Generate voice tracks for all 4 roles using configured voice models.
5. **Gate 5 (Voice Role Check):** Run `voice_role_check.py` ensuring identity consistency per role.
6. **Gate 6 (Master Audio Build):** Mix Voice + SFX + BGM adhering to EBUR128 (-16 ± 1 LUFS, TP $\le -1.5$ dBFS).
7. **Gate 7 (Shot Parsing):** Map 100% sentences to 60 background assets via `parse_shots.py`.
8. **Gate 8 (Video Render & Packaging):** Render visual timeline via `build_video3.py` and mux subtitles with `package.py --mux`.
