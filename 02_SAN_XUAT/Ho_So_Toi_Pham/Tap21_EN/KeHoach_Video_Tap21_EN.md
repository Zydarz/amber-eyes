# PRODUCTION DOSSIER EPISODE 21 · "THE POSTPARTUM PSYCHOSIS TRAGEDY & THE ETERNAL PRISON OF CONSCIENCE" — EN EDITION

## B1. Episode Information

| Item | Details |
|---|---|
| Episode Title | **Episode 21: The Postpartum Psychosis Tragedy — When Delusions Stole Motherhood & The Eternal Prison of Conscience (The Andrea Yates Case)** |
| Case | Clear Lake Tragedy of Five Children (Houston, Texas, USA, June 20, 2001) & Historical Legal Battle (2002–2006) |
| Psychological Themes | Acute Postpartum Psychosis (*PPP*) · Altruistic Filicide · Salvation Delusion · **KEY FOCUS:** Post-Psychotic Awakening, Ego Collapse & Catastrophic Moral Injury of Andrea Yates · Lifelong Self-Imposed Penance at Kerrville State Hospital (consistently declining release petitions, knitting items to support the children's memorial fund) · Authoritarian Patriarchal Pressure, Normalcy Bias & Enabler Guilt of Russell "Rusty" Yates · Spiritual Abuse & Moral Disengagement of Preacher Michael Woroniecki · Bureaucratic Blindspot & Clinical Complacency of Dr. Mohammed Saeed · The 7-Year-Old Noah's Desperate Survival Flight & Victim Dignity · Latecomer's Torment & Counterfactual Thinking of Grandmother Dora Yates · Suburban Blindspot & Halo Effect in Clear Lake · Judicial Awakening: M'Naghten Rule Boundary vs. Fabricated Expert Evidence of Park Dietz · Legacy of the Yates Children Memorial Fund & 4 Red Flags for PPP Recognition |
| Format | Host-Driven Criminal Psychological Documentary Podcast — 5 Acts conforming to Golden Benchmark A2c/K10 |
| Cast Allocation | 4 Voice Roles: **Host (Owl)** (122 sentences) · **Lead Investigator (Wolf)** (50 sentences) · **Forensic Psychologist (Fox)** (48 sentences) · **Ordinary Persons (N1/N2)**: N1 Clear Lake Neighbor (12 sentences) & N2 Harris County Juror (9 sentences) · Declared `n_element`: `1.07` (N1), `4.09` (N2) |
| Script Scale | **248 spoken sentences** (expanded +36 deep behavioral sentences) · 51 structural elements · 32 dialogue turns |
| Estimated Runtime | **~28.5 minutes** · Fulfills Amber eyes channel Golden Production Benchmark |
| Multilingual Parity | **Exact 1:1 Parity across all 3 primary languages:** Vietnamese (VN: 248 sentences), English (EN: 248 sentences), Japanese (JA: 248 sentences) (and Korean KO: 248 sentences) |
| Content Safety | **Strict compliance with Rule V9 (YouTube Safe)**: 0% graphic gore, bodily trauma, or suffocation depictions; 100% focused on psychiatric behavioral science, clinical empathy, and 4 life-saving survival red flags |
| Visual Assets | **63 background images at 2112×1188 (16:9 2K)** with prefix `t21_` located at `assets/bg/` · Dark Graphic Novel Noir Style |
| BGM Suite | Somber Cello & Rain Ambient $\rightarrow$ Minimalist Piano & Dark Drones $\rightarrow$ Tense Strings $\rightarrow$ Courtroom Gavel & Somber Chamber $\rightarrow$ Warm Reflective Piano |
| Deep Behavioral Research | [`01_KICH_BAN/Ho_So_Toi_Pham/Tap21/NghienCuu_TamLy_BoSung_KichBan_Tap21.md`](../../01_KICH_BAN/Ho_So_Toi_Pham/Tap21/NghienCuu_TamLy_BoSung_KichBan_Tap21.md) |

---

## B2. Production Pipeline Roadmap

### 1. Dossier & Source Synchronization (Completed)
- [x] Verified 100% factual accuracy against Harris County District Court records, Texas First Court of Appeals decisions (171 S.W.3d 215), and psychiatric forensic evaluations (`01_KICH_BAN/Ho_So_Toi_Pham/Tap21/REVIEW_kichban_tap21.md`).
- [x] Completed deep behavioral analysis across 5 subject groups (Perpetrator, Enablers/Catalysts, Victims, Family/Witnesses, Suburban Community/Society) with expanded dialogues in 3 languages (`01_KICH_BAN/Ho_So_Toi_Pham/Tap21/NghienCuu_TamLy_BoSung_KichBan_Tap21.md`).
- [x] Upgraded and synchronized 3-language scripts to **248 sentences** with 1:1 structural parity (`01_KICH_BAN/Ho_So_Toi_Pham/Tap21/REVIEW_kichban_tap21_multilingual.md`).
- [x] Updated multilingual YouTube video descriptions (`mo_ta.txt`, `description.txt`) and reference citations (`nguon_tham_khao.md`) for VN / EN / JA.

### 2. Next Production Gates (Per `AGENTS.md`)
1. **Gate 1 (Script Review):** Master 248-sentence script passed with 100% adherence to the 10 Psychological Indicators Ecosystem (A2c) and Rule K10.
2. **Gate 2 (Script Parsing):** Parsed to `.work/script_tap21_EN.json` (248 LOI sentences).
3. **Gate 3 (Acting & Pause Gate):** Generate `make_acting_tap21_en.py` / `acting_tap21_EN.json` (median pause $\ge 0.6$ s, $\le 25\%$ pauses $< 0.4$ s per `qc_pause_gate.py --pre`).
4. **Gate 4 (TTS Voice Synthesis):** Synthesize 4 roles via MiniMax / Higgs Audio v3 per `CAST` configuration in `edition.py`.
5. **Gate 5 (Voice Role Audit):** Run `voice_role_check.py` to ensure timbre continuity and zero pitch distortion (G5: pitch=0).
6. **Gate 6 (Master Audio):** 3-layer audio mix (Voice + SFX + BGM) conforming to EBU-R128 (-16 LUFS, TP $\le -1.5$ dBFS, 0 silence gaps $> 0.3$ s).
7. **Gate 7 (Shot Table):** Map 100% sentences to 63 shared backgrounds `t21_*` via `parse_shots.py` (`qc_bg_shared.py --ep 21` PASS).
8. **Gate 8 (Video Render & Packaging):** Render via `build_video3.py` and mux subtitles with `package.py --mux`.

---

## B3. 5-Act Structure & 10 Psychological Indicators Mapping (A2c/K10)

### ACT 1: THE DAWN 911 CALL & THE SILENT HOUSTON RESIDENCE
- **Estimated Duration:** ~6.5 minutes · **58 sentences** (expanded +8 sentences at `1.07` and `1.10`)
- **BGM:** `bgm_ambient_deep.mp3` (Somber Cello combined with steady rain, distant sirens)
- **Psychological Focus & Indicators:**
  - *Indicator 1 (Social Impact) & Indicator 9 (Halo Effect):* The facade of a devoted former nurse and model Christian family created a catastrophic suburban blindspot in Clear Lake.
  - *Latecomer's Torment:* Witness N1 at `1.07` captures the agonizing grief of paternal grandmother Dora Yates, missing the threshold by barely thirty fateful minutes.
  - *Indicator 10 (Victimology & Primal Survival Instinct):* Investigator at `1.10` recounts the frantic hallway flight of seven-year-old Noah facing the twisted salvation delusion of his psychotic mother.

### ACT 2: THE ABYSS OF ISOLATION & THE OVERLOOKED WARNINGS
- **Estimated Duration:** ~5.5 minutes · **48 sentences** (expanded +7 sentences at `2.06` and `2.10`)
- **BGM:** Minimalist staccato piano, racing heartbeat pulse, and oppressive electronic drone
- **Psychological Focus & Indicators:**
  - *Indicator 3 (Compartmentalization) & Indicator 6 (Psychological Trigger):* Rapid succession of 5 births in 5 years; the death of Andrea's father shattering her emotional anchor.
  - *Russell Yates's Patriarchal Pressure:* Investigator at `2.06` analyzes rigid bus confinement, Woroniecki's correspondence, and reckless disregard for Dr. Starbranch's explicit pregnancy prohibition.
  - *Bureaucratic Medical Failure:* Host at `2.10` dissects Dr. Saeed's fatal decision to abruptly discontinue Haldol two weeks prior to the catastrophe.

### ACT 3: PSYCHOLOGICAL DECODING: POSTPARTUM PSYCHOSIS & SALVATION DELUSION
- **Estimated Duration:** ~6.0 minutes · **50 sentences** (expanded +7 sentences at `3.03` and `3.07`)
- **BGM:** Chilling electronic drone, dissonant violin tension
- **Psychological Focus & Indicators:**
  - *Indicator 2 (Altruistic Filicide):* Psychological expert at `3.03` draws an absolute boundary between calculated malice and psychotic altruistic filicide; maternal devotion hijacked by biochemical storm to save children from damnation.
  - *Indicator 5 (Reality Rupture):* Expert at `3.07` illuminates the total collapse of reality testing; modern civilization's maturity measured by discerning illness from wickedness.

### ACT 4: THE HISTORICAL RETRIAL & THE NOT GUILTY VERDICT
- **Estimated Duration:** ~6.5 minutes · **55 sentences** (expanded +8 sentences at `4.06` and `4.11`)
- **BGM:** Resonant courtroom gavel, dramatic chamber cello
- **Psychological Focus & Indicators:**
  - *Post-Psychotic Awakening:* Investigator at `4.06` recounts the clearing of psychotic fog in jail hospital; catastrophic moral injury and convulsive ego collapse when realizing her own hands took her children's lives.
  - *Indicator 4 (Self-Imposed Penance):* Expert at `4.11` contrasts narcissistic self-pity with authentic remorse; Andrea's consistent refusal of release hearings at Kerrville State Hospital to knit memorial goods for her children.
  - *M'Naghten Rule & Overturning Perjury:* The 2006 jury overturned Park Dietz's fabricated Law & Order testimony, establishing a compassionate precedent of NGRI.

### ACT 5: THE WAKE-UP CALL, YATES MEMORIAL LEGACY & 4 RED FLAGS
- **Estimated Duration:** ~5.0 minutes · **37 sentences** (expanded +6 sentences at `5.03` and `5.04`)
- **BGM:** Warm Reflective Piano resonating into a peaceful fadeout
- **Psychological Focus & Indicators:**
  - *Yates Children Memorial Fund:* Investigator at `5.03` reviews the institutional transformation of medicine and law into a shield for vulnerable mothers.
  - *Community Responsibility:* Expert at `5.04` warns that home sanctity cannot rest on silent maternal suffering; PPD is an urgent biological SOS.
  - *Indicator 10 (4 Survival Red Flags):* Host at `5.05` summarizes: (1) Sudden unresponsiveness and vacant stare; (2) Bizarre religious/spiritual delusions; (3) Command auditory hallucinations; (4) Persistent insomnia paired with severe agitation or exhaustion.

---

## B4. 63 Background Images Catalog (`assets/bg/t21_*.png`)
*(Full mapping of 63 2K images across all 5 acts corresponding to `Danh_Sach_Anh_Tap21.md`)*.
