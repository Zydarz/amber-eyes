# PRODUCTION PLAN EPISODE 38 (EN)

**Case:** Natascha Kampusch & Wolfgang Priklopil — 3,096 Days Underground  
**Standards:** Standard A2c / Rule K10 (10-Indicator Behavioral Ecosystem), Rule V9 (100% YouTube Safe), Rule G1–G13.  
**Script Path:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap33_EN/kichban_tap33_EN.md` (52 elements, exactly 240 sentences)  
**Script JSON:** `.work/script_tap33_EN.json`  

---

## Technical Specifications & Cast
- **Episode Title:** Episode 38: Natascha Kampusch — 3,096 Days Underground & The Indomitable Spirit Defeating Mind Control
- **Format:** Narrator-led Documentary Podcast (Host-driven with Forensic Investigator, Behavioral Psychologist, and Eyewitness/Insider accounts).
- **Target Duration:** 28:00 – 32:00
- **Voice Allocation:** Host ~52% (124 sentences), Forensic Investigator ~21% (50 sentences), Behavioral Psychologist ~22% (53 sentences), Ordinary Person/Witness ~5% (13 sentences: N1 5 sentences, N2 8 sentences).
- **Parity Status:** 100% 1:1 Parity with Vietnamese Master Script across all 52 elements.

---

## Production Pipeline Checklist
- [x] **Step 1: Script Approved** (240 sentences, V9 PASS, K10 PASS)
- [x] **Step 2: Script Parsed** (`parse_kichban.py` -> `.work/script_tap33_EN.json`)
- [x] **Step 3: Configuration & Acting Setup** (Declared in `edition.py`, `acting_tap33.json` prepared)
- [ ] **Step 4: Voice Synthesis (TTS)** (`tts_sentences.py`)
- [ ] **Step 5: Voice Role Check** (`voice_role_check.py` G8–G10)
- [ ] **Step 6: Master Audio Assembly** (`build_audio3.py`, `qc_pause_gate.py`)
- [ ] **Step 7: Shot Table Generation** (`parse_shots.py`)
- [ ] **Step 8: Stills Generation & Visual QC** (`build_video3.py --stills`)
- [ ] **Step 9: Video Rendering** (`build_video3.py --workers 6`)
- [ ] **Step 10: Subtitles & Packaging** (`subtitles.py`, `package.py --mux`)
