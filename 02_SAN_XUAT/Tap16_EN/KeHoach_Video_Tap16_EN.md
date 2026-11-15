# PRODUCTION PLAN EPISODE 16 · "ANNIHILATING HIS ENTIRE FAMILY TO SEND THEM TO HEAVEN" — EN EDITION

## B1. Episode Information

| Item | Details |
|---|---|
| Episode Title | **Episode 16: Annihilating His Entire Family to 'Send Them to Heaven' — OCPD & The 18-Year Flight (The John List Case)** |
| Case Background | The Breeze Knoll Mansion Murders (Westfield, New Jersey, USA, November 9, 1971) & The Historic 1971–1989 Manhunt via *America's Most Wanted* and Frank Bender's Forensic Bust |
| Psychological Themes | Obsessive-Compulsive Personality Disorder (OCPD) · Altruistic Familicide · Moral Neutralization: Appeal to Higher Loyalties · **CORE FOCUS:** Inability for Genuine Remorse & Narcissistic Collapse in John List (pathological self-pity for lost patriarchal status and societal reputation vs complete void of contrition or grief for five murdered relatives) · Reactions of Enablers / Inadvertent Accomplices: Enabler Guilt & Toxic Compartmentalization from mother Alma List and wife Delores Miller · Ignored Intuitive Warnings & Survival Instincts (*The Gift of Fear*) of 16-year-old Patricia List · Witness Moral Injury & Bystander Guilt in drama teacher Jean Phillips and Colorado neighbor Wanda Flannery · Suburban Blindspot & Elite Complacency in Westfield · Forensic Sculptural Breakthrough by Frank Bender combined with grassroots television mobilization via *America's Most Wanted* · 4 Practical Survival Red Flags against Pathological Domestic Controllers |
| Format | Forensic Psychological Documentary (Host-Driven) — 5 Acts Standard A2c/K10 |
| Cast Allocation | 4 Primary Voices: **Host (Owl)** (137 sentences) · **Lead Detective (Wolf)** (46 sentences) · **Psychologist (Fox)** (48 sentences) · **Everyday People (N1/N2)**: N1 Jean Phillips (14 sentences at `1.07`) & N2 Wanda Flannery (12 sentences at `4.09`) · Declared `n_element`: `1.07` (N1), `4.09` (N2) |
| Script Scale | **257 sentences** (expanded +37 deep psychological sentences across 5 subjects) · 51 Elements · 32 LOI turns |
| Estimated Runtime | **~29.5 – 31.5 minutes** · Amber eyes Golden Benchmark Standard |
| Multilingual Alignment | **Absolute 1:1 Parity:** Vietnamese (VN: 257), English (EN: 257), Japanese (JA: 257), Korean (KO: 257) |
| YouTube Safety | **Strict Rule V9 Compliance**: 0% gore or graphic violence; 100% focused on behavioral science, forensic psychiatry, and practical survival red flags |
| Visual Assets | **83 2112×1188 (16:9 2K) Backgrounds** with prefix `t16_` at `assets/bg/` · Deep Noir Graphic Novel |
| Soundtrack (BGM) | `bgm_church_organ.mp3` $\rightarrow$ `bgm_ambient_deep.mp3` $\rightarrow$ `bgm_piano_minimal.mp3` $\rightarrow$ `bgm_violin_heart.mp3` $\rightarrow$ `bgm_piano_warm.mp3` |
| Research Reference | [`01_KICH_BAN/Tap16/NghienCuu_TamLy_BoSung_KichBan_Tap16.md`](../../01_KICH_BAN/Tap16/NghienCuu_TamLy_BoSung_KichBan_Tap16.md) |

---

## B2. Production Pipeline Roadmap

### 1. Dossier & Historical Synchronization (Completed)
- [x] Legal and historical facts verified against Union County Superior Court archives, Westfield Police Department records, FBI Declassified Vault files, and the original May 21, 1989 broadcast of *America's Most Wanted*.
- [x] Comprehensive behavioral research completed for all 5 subjects (Perpetrator John List, Enablers, Victims, Witnesses, Suburban Community), addressing the core mechanism of remorse and psychological defense (`01_KICH_BAN/Tap16/NghienCuu_TamLy_BoSung_KichBan_Tap16.md`).
- [x] Multilingual scripts upgraded to **257 sentences** with absolute 1:1 Parity (`01_KICH_BAN/Tap16/REVIEW_kichban_tap16_multilingual.md`).
- [x] Production acting parameters and pauses established (`acting_tap16_EN.json`), passing `qc_pause_gate.py --pre` with 144 pause cues (56%, 0 unfamiliar codes, 0 out-of-range pauses).
- [x] Multilingual YouTube metadata files (`mo_ta.txt`, `description.txt`) and reference lists (`nguon_tham_khao_EN.md`) updated.
- [x] Dynamic multilingual routing configured in `.work/edition.py` for `EPISODES["16"]`.

### 2. Pipeline Production Steps
1. **Step 1 (Script Approval):** 257-sentence script verified under 10 Behavioral Indicators (A2c) and Rule K10.
2. **Step 2 (Script Parsing):** Parsed to `.work/script_tap16_EN.json` (257 sentences, 51 elements).
3. **Step 3 (Acting & Pauses):** Verified in `acting_tap16_EN.json` (Rule A13, median pause $\ge 0.6$ s).
4. **Step 4 (TTS Voice Synthesis):** Higgs Audio v3 / MiniMax configured via `edition.py`.
5. **Step 5 (Voice Role Check):** Consistent character identity without pitch alteration (Rule G5: pitch=0).
6. **Step 6 (Master Audio):** Mixed at -16 LUFS, True Peak $\le -1.5$ dBFS, 0 silent gaps $> 0.3$ s.
7. **Step 7 (Shot Table Matching):** 100% matched with 83 shared backgrounds (`t16_*`) via `parse_shots.py`.
8. **Step 8 (Rendering & Packaging):** Final video rendered with `build_video3.py` and muxed via `package.py --mux`.

---

## B3. 5 Acts & 10 Behavioral Indicators Structure

### ACT 1: THE GLOOMY BREEZE KNOLL MANSION AND THE HORRIFIC DISCOVERY
- **Runtime:** ~6.8 mins · **58 sentences** (enhanced at `1.02`, `1.07`, `1.10`)
- **BGM:** `bgm_church_organ.mp3` (Ominous church organ, howling wind through window panes, desolate falling snow)
- **Psychological Focus:** Suburban Blindspot & Family Façade at Breeze Knoll (`1.02`); blaring lights and internal speaker hymns pacifying neighbor suspicions for a full month; Patricia's ignored survival intuition and drama teacher Jean Phillips's witness moral injury (`1.07`); forensic examination in the ballroom under the Tiffany glass ceiling confirming cold calculation without hesitation markers (`1.10`).

### ACT 2: THE DISAPPEARANCE OF THE CENTURY AND SCISSORS IN PHOTO ALBUMS
- **Runtime:** ~5.2 mins · **45 sentences** (enhanced at `2.02`, `2.06`, `2.10`)
- **BGM:** `bgm_ambient_deep.mp3` (Deep cavernous ambient, metallic clock ticking, interstate railway rumblings)
- **Psychological Focus:** Extreme cognitive compartmentalization: calmly eating lunch and washing dishes post-crime before excising his own facial likeness from all family albums (`2.02`); tactical evasion MO: excusing children from school, stopping deliveries, withdrawing final savings, and parking at JFK Airport before boarding a train to Denver (`2.06`); suburban paralysis and investigative cold trail lasting nearly two decades (`2.10`).

### ACT 3: PSYCHOLOGICAL DECODING: OCPD & THE MORAL NEUTRALIZATION TRAP
- **Runtime:** ~6.2 mins · **53 sentences** (enhanced at `3.03`, `3.05`, `3.07`)
- **BGM:** `bgm_piano_minimal.mp3` (Minimalist clinical piano with resonant drone, academic autopsy atmosphere)
- **Psychological Focus:** Etiology of OCPD: rigid maternal dogma, authoritarian mealtime silence, and binary moral perfectionism (`3.03`); precipitating trigger: concealed unemployment, sham commutes in business suits, drained maternal life savings, and imminent bank foreclosure (`3.05`); objectification of family and rationalization via "Appeal to Higher Loyalties" to "deliver souls to heaven before spiritual corruption" (`3.07`).

### ACT 4: FRANK BENDER'S FORENSIC BUST AND THE CALL FROM AMERICA'S MOST WANTED
- **Runtime:** ~6.8 mins · **58 sentences** (enhanced at `4.02`, `4.06`, `4.09`, `4.11` — **CORE FOCUS**)
- **BGM:** `bgm_violin_heart.mp3` (Tense dramatic violin with resonant courtroom gavel strikes)
- **Psychological Focus:** Seamless identity assumption as Robert Clark in Colorado and Virginia without nightmares or remorse (`4.02`, `4.06`); Frank Bender's forensic aging masterpiece accounting for OCPD facial habits and horn-rimmed spectacles aired to 22 million viewers; neighbor Wanda Flannery overcoming hesitation to place the decisive call (`4.09`); forensic distinction between authentic remorse and List's narcissistic collapse: weeping only for stripped status and wounded pride while remaining completely void of grief for his five victims (`4.11`); Judge Wertheimer's condemnation: *"His soul is as black and cold as the day of November 9, 1971,"* imposing five consecutive life terms.

### ACT 5: AWAKENING LESSONS ON OBSESSIVE CONTROL & 4 SURVIVAL RED FLAGS
- **Runtime:** ~5.0 mins · **43 sentences** (enhanced at `5.02`, `5.03`, `5.04`)
- **BGM:** `bgm_piano_warm.mp3` (Warm dignified piano, philosophical closure, timeless human reflection)
- **Psychological Focus:** Shattering suburban complacency: external respectability cannot mask domestic tyranny (`5.02`); survival wisdom of *The Gift of Fear*: honoring intuitive dread and validating cries for help (`5.03`, `5.04`); 4 classic survival red flags against controlling patriarchs (`5.05`):
  1. Micro-management and coercive financial isolation.
  2. Rigid moral absolutism and self-righteous religious delusions.
  3. Desperate pathological deception to uphold an outward mask of success.
  4. Total emotional detachment and annihilation of empathy.

---

## B4. 83 Shared Background Visual Assets (`assets/bg/t16_*.png`)

All 83 Deep Noir Graphic Novel 2K backgrounds shared identically across all language editions (H17):

### Act 1 (16 Backgrounds)
- `t16_john_list_a1_01_ocpd`: Breeze Knoll mansion on a snowy winter night with dim glowing windows.
- `t16_john_list_a1_02_bank_account`: Vintage intercom speakers broadcasting hollow church organ hymns through vacant halls.
- `t16_john_list_a1_03_scissors`: Meticulously arranged Victorian dining table reflecting oppressive domestic discipline.
- `t16_john_list_a1_04_family_photos`: Respectable pious family portrait contrasting against suffocating hidden debts.
- `t16_john_list_a1_05_frank_bender`: Patricia's empty drama classroom with anxious glances cast toward the window.
- `t16_john_list_a1_06_sculpture`: Patricia and her brothers walking across the schoolyard under ominous shadows.
- `t16_john_list_a1_07_amw`: Teacher Jean Phillips holding the suspicious typed absence note in disbelief.
- `t16_john_list_a1_08_breeze_knoll`: Breeze Knoll front porch covered in snow with piled-up unread newspapers.
- `t16_john_list_a1_09_westfield`: Westfield police patrol cruisers cautiously approaching the dark mansion.
- `t16_john_list_a1_10_mansion`: Cavernous ballroom under the stained-glass Tiffany skylight frozen in eerie silence.
- `t16_john_list_a1_11_tiffany`: Forensic investigators sweeping flashlights across the polished wooden floor.
- `t16_john_list_a1_12_ocpd`: Narrow wooden staircase ascending into the isolated attic quarters of Alma List.
- `t16_breeze_knoll_snowy_porch_mail`: Front porch engulfed in December snow with yellowed mail and newspapers.
- `t16_breeze_knoll_grand_ballroom_empty`: Desolate ballroom under Tiffany dome glowing with cold luminescence.
- `t16_breeze_knoll_attic_staircase_shadows`: Staircase leading into the attic shrouded in impenetrable darkness.
- `t16_forensic_ballistics_evidence_markers`: Yellow evidence tents marking shell casings on the polished floorboards.

### Act 2 (15 Backgrounds)
- `t16_john_list_a2_01_family_photos`: Leather family album open on a wooden table with cut-out facial silhouettes.
- `t16_john_list_a2_02_frank_bender`: Heavy metal shears resting beside charred remnants of excised photographic scraps.
- `t16_john_list_a2_03_sculpture`: Kitchen counter with cleaned plates after a calm post-homicide sandwich meal.
- `t16_john_list_a2_04_amw`: JFK Airport long-term parking lot obscured under swirling freezing rain.
- `t16_john_list_a2_05_breeze_knoll`: Nocturnal transcontinental train departing the East Coast toward Colorado.
- `t16_john_list_a2_06_westfield`: Faded FBI Most Wanted poster pinned against a weathered station precinct wall.
- `t16_john_list_a2_07_mansion`: The sole surviving youth identification photograph of John List.
- `t16_john_list_a2_08_tiffany`: Dust-laden cold-case archive box sitting inside New Jersey police storage.
- `t16_john_list_a2_09_ocpd`: Solitary silhouette of an accountant working late behind blinds in Denver.
- `t16_john_list_a2_10_bank_account`: Suburban church service where John List fabricated his new domestic identity.
- `t16_john_list_a2_11_scissors`: Two decades of investigative deadlock against a phantom who left zero paper trail.
- `t16_carved_family_album_empty_silhouettes`: Opened family album displaying sharply excised oval holes.
- `t16_chevrolet_impala_airport_parking_snow`: Abandoned 1963 Chevrolet Impala iced over at JFK airport parking.
- `t16_interstate_bus_terminal_rain_neon`: Bus terminal bathed in cold neon reflections in the midnight rain.
- `t16_cold_case_dossier_archives_dust`: Thickly dusted unsolved homicide dossier boxes in New Jersey records.

### Act 3 (15 Backgrounds)
- `t16_john_list_a3_01_amw`: Forensic psychiatric archive analyzing OCPD clinical trait matrices.
- `t16_john_list_a3_02_breeze_knoll`: Childhood memories of overbearing maternal surveillance in Michigan.
- `t16_john_list_a3_03_westfield`: Accounting ledger with micro-recorded expenses tracked down to the exact cent.
- `t16_john_list_a3_04_mansion`: Authoritarian childhood dining room enforced under total mealtime silence.
- `t16_john_list_a3_05_tiffany`: Bank boardroom where John List received his humiliating termination notice.
- `t16_john_list_a3_06_ocpd`: Commuter train bench where List read newspapers daily to conceal unemployment.
- `t16_john_list_a3_07_bank_account`: Mother Alma's passbook depleted systematically to the final cent.
- `t16_john_list_a3_08_scissors`: Foreclosure eviction notice served upon Breeze Knoll resting on the desk.
- `t16_john_list_a3_09_family_photos`: Deepening ideological rift with daughter Patricia pursuing theatrical arts.
- `t16_john_list_a3_10_frank_bender`: 5-page handwritten confession to Pastor Rehwinkel detailing soul salvation.
- `t16_john_list_a3_11_sculpture`: Forensic chart of cognitive neutralization: Appeal to Higher Loyalties.
- `t16_lutheran_church_stained_glass_cross`: Stained-glass church cross casting elongated shadows across flagstone.
- `t16_forensic_psychiatry_dossier_ocpd`: Forensic clinical file dissecting OCPD rigidity and moral fallacies.
- `t16_bank_foreclosure_notice_envelope`: Foreclosure notice envelope lying beside hollow financial folders.
- `t16_confession_letter_fountain_pen`: Five-page pen-and-ink confession letter resting beside a vintage desk lamp.

### Act 4 (16 Backgrounds)
- `t16_john_list_a4_01_breeze_knoll`: Sun-drenched Philadelphia sculpture studio of forensic artist Frank Bender.
- `t16_john_list_a4_02_westfield`: Gray clay bust taking shape under Bender's anatomical and psychological modeling.
- `t16_john_list_a4_03_mansion`: Completed aging bust wearing retro horn-rimmed glasses and detached gaze.
- `t16_john_list_a4_04_tiffany`: Studio set of *America's Most Wanted* preparing the landmark 1989 broadcast.
- `t16_john_list_a4_05_ocpd`: Live television broadcast displaying the bust to 22 million viewers.
- `t16_john_list_a4_06_bank_account`: FBI switchboard flooded with hundreds of civilian telephone tips.
- `t16_john_list_a4_07_scissors`: Quiet suburban house in Midlothian, Virginia where Robert Clark resided.
- `t16_john_list_a4_08_family_photos`: Neighbor Wanda Flannery watching the broadcast in shock in her living room.
- `t16_john_list_a4_09_frank_bender`: Flannery placing the crucial phone call connecting Clark to List.
- `t16_john_list_a4_10_sculpture`: FBI agents and local detectives moving in to arrest Clark at his accounting firm.
- `t16_john_list_a4_11_amw`: Moment glasses are removed and fingerprint comparison confirms John List.
- `t16_john_list_a4_12_breeze_knoll`: Packed courtroom of Union County Superior Court during the 1990 trial.
- `t16_frank_bender_sculpture_bust_clay`: Forensic clay age-progression bust resting on a wooden sculpting armature.
- `t16_amw_television_broadcast_screen`: Vintage 1980s television screen broadcasting the forensic bust.
- `t16_fbi_arrest_robert_clark_handcuffs`: Steel handcuffs snapping around the wrists of the suited fugitive.
- `t16_union_county_courtroom_sentencing`: Stern courtroom where judge pronounces five consecutive life sentences.

### Act 5 (21 Backgrounds)
- `t16_john_list_a5_01_westfield`: Overgrown foundation ruins of Breeze Knoll after the mysterious 1972 fire.
- `t16_john_list_a5_02_mansion`: Peaceful Westfield community grounds restored following justice delivered.
- `t16_john_list_a5_03_tiffany`: New Jersey State Prison where John List served out his life terms until death.
- `t16_john_list_a5_04_ocpd`: Behavioral reflection on obsessive control and the collapse of perfect facades.
- `t16_john_list_a5_05_bank_account`: Red Flag 1: Coercive financial micro-management and familial isolation.
- `t16_john_list_a5_06_scissors`: Red Flag 2: Dogmatic moral absolutism and self-righteous punishment logic.
- `t16_john_list_a5_07_family_photos`: Red Flag 3: Desperate pathological deception to defend a social mask.
- `t16_john_list_a5_08_frank_bender`: Red Flag 4: Emotional numbness and systematic annihilation of empathy.
- `t16_john_list_a5_09_sculpture`: *The Gift of Fear* philosophy: Validating survival intuition and setting boundaries.
- `t16_john_list_a5_10_amw`: Philosophical Amber eyes channel closing reflection and farewell signoff.
- `t16_john_list_a5_11_breeze_knoll`: Sunset descending over New Jersey valleys evoking quiet contemplation.
- `t16_john_list_a5_12_westfield`: Memorial honoring the innocent victims: Alma, Helen, Patricia, John Jr., Frederick.
- `t16_breeze_knoll_ruins_fire_remains`: Moss-covered stone foundation ruins of the mansion after the blaze.
- `t16_state_prison_corridor_iron_bars`: Bleak prison corridor lined with gray iron cell bars.
- `t16_gift_of_fear_red_flags_notebook`: Open notebook recording four practical survival red flags beside a pen.
- `t16_victim_memorial_five_candles`: Five white memorial candles flickering in the darkness for the victims.
- `t16_amber_eyes_closing_monolith`: The Amber eyes owl emblem in dark graphic novel styling closing the episode.
- `t16_westfield_suburban_facade_autumn`: Suburban street lined with golden autumn leaves and stately trees.
- `t16_financial_audit_desk_empty`: Vacant late-night accounting desk with unfinished ledgers.
- `t16_sculptor_hands_clay_detail`: Sculptor's hands meticulously working clay wrinkles around facial eyes.
- `t16_courtroom_gavel_justice_shadow`: Wooden gavel resting on the judge's bench under sharp dramatic lighting.

---

## B5. Quality Control Gate Results (QC Gates)

| Quality Gate | Standard Reference | Measured Verification | Status |
|---|---|---|:---:|
| **Gate 1: YouTube Safety (Rule V9)** | `AGENTS.md` Sec. 3 & `TIEU_CHUAN` §A9.2 | 0 forbidden words, 0 graphic gore, 100% YouTube Safe | ✅ PASSED |
| **Gate 2: Punctuation & Formatting (G1)** | `AGENTS.md` G1 & G6 | 0 ellipses (`...`/`…`), standard pause markers | ✅ PASSED |
| **Gate 3: Quantitative Parity (L3)** | `AGENTS.md` L3 | Exactly 257 sentences, 51 elements, 32 LOI turns | ✅ PASSED |
| **Gate 4: 10 Behavioral Indicators (A2c)** | `TIEU_CHUAN` §A2c & Rule K10 | Complete 10 indicators, deep dissection of 5 subjects | ✅ PASSED |
| **Gate 5: Multilingual Alignment (Parity)** | `AGENTS.md` L8 & §A2b | Absolute 1:1 Parity across VN, EN, JA, KO (257 sentences) | ✅ PASSED |
| **Gate 6: Audio Pause Gate Pre-check (A13)** | `AGENTS.md` A13 & `qc_pause_gate.py` | 144 pause cues (56%), 0 foreign IDs, median $\ge 0.6$ s | ✅ PASSED |
| **Gate 7: Shared Visual Assets (H17)** | `AGENTS.md` H17 & `Danh_Sach_Anh_Tap16` | 83 standard `t16_` backgrounds shared identically | ✅ PASSED |
