# PRODUCTION PLAN EPISODE 19 · "THE 'DEMON IN THE HEAD' CHARADE" — EN EDITION

## B1. Episode Information

| Field | Details |
|---|---|
| Episode Title | **Episode 19: The 'Demon in the Head' Charade — Malingering & Truth on Camera (The Nikolas Cruz Dossier)** |
| Criminal Case | The Marjory Stoneman Douglas High School Massacre (Parkland, Broward County, Florida, USA, February 14, 2018) |
| Psychological Themes | Malingering · True Psychosis vs. Antisocial Personality Disorder (*ASPD*) · Notoriety Seeking Syndrome · Cognitive Compartmentalization & Emotional Theatrics before family · Moral Neutralization & Externalization of Blame · **CORE FOCUS:** Instrumental Remorse & Pathological Self-Pity vs. Genuine Contrition · Moral Injury & Freeze Response of School Resource Officer Scot Peterson · Enabler Guilt of host family James & Kimberly Snead · Diffusion of Responsibility & De-individuation in online forums · Extreme Altruism & Protective Sacrifice of educators · Survivor's Guilt & Post-Traumatic Growth (*PTG*) of March for Our Lives · Suburban Illusion of Safety in Parkland · Institutional Blindspots (30+ police calls & 2 FBI tip-offs ignored) · Red Flag Laws & Florida Jury Supermajority Reform (12-0 to 8-4) |
| Format | Investigative Documentary Podcast (Host-Driven) — 5 Acts standard A2c/K10 |
| Voice Casting | 4 Core Voices: **Host** (145 sentences, ~60%) · **Investigator (Detective John Curcio)** (43 sentences, ~18%) · **Psychologist** (41 sentences, ~17%) · **Ordinary Person (N1/N2)**: N1 Parkland survivor (7 sentences at `1.07`) & N2 Courtroom observer / Juror (6 sentences at `4.09`) |
| Script Scale | **241 sentences** (+31 deep psychological expansion sentences across 5 entities) · 51 Elements · 32 LOI turns |
| Estimated Runtime | **~29.0 – 32.0 minutes** · Golden Benchmark of Amber eyes |
| Language Alignment | **Absolute 1:1 Parity across 4 languages:** Vietnamese (VN: 241), English (EN: 241), Japanese (JA: 241), Korean (KO: 241) |
| Safety Standard | **Strict Compliance with Rule V9 (YouTube Safe)**: 0% gore or sensational violence; 100% forensic behavioral science, interrogation strategy, and BTAM threat assessment |
| BGM Tracklist | `bgm_sub_drone.mp3` $\rightarrow$ `bgm_ambient_deep.mp3` $\rightarrow$ `bgm_piano_minimal.mp3` $\rightarrow$ `bgm_violin_heart.mp3` $\rightarrow$ `bgm_piano_warm.mp3` |
| Deep Research File | [`01_KICH_BAN/Tap19/NghienCuu_TamLy_BoSung_KichBan_Tap19.md`](../../01_KICH_BAN/Tap19/NghienCuu_TamLy_BoSung_KichBan_Tap19.md) |
| Production Scripts | [`.work/script_tap19.json`](../../.work/script_tap19.json) (VN), [`.work/script_tap19_EN.json`](../../.work/script_tap19_EN.json) (EN), [`.work/script_tap19_JA.json`](../../.work/script_tap19_JA.json) (JA), [`.work/script_tap19_KO.json`](../../.work/script_tap19_KO.json) (KO) |

---

## B2. Production Roadmap

1. **Step 1 (Script Review):** Completed. 241-sentence script meets 100% of 10 Psychological Indicators (A2c) and Rule K10.
2. **Step 2 (Script Parsing):** Compiled to production JSON `.work/script_tap19.json`, `.work/script_tap19_EN.json`, `.work/script_tap19_JA.json`, `.work/script_tap19_KO.json` (241 LOI sentences each).
3. **Step 3 (Acting & Pauses):** Generate `acting_tap19_EN.json` conforming to A13 and `qc_pause_gate.py`.
4. **Step 4 (TTS Voiceover):** Voice generation using English production cast.
5. **Step 5 (Voice Consistency QC):** Run `voice_role_check.py` to ensure single vocal identity per role.
6. **Step 6 (Master Audio):** Mix Voice + SFX + BGM adhering to EBUR128 (-16 LUFS, TP $\le -1.5$ dBFS).
7. **Step 7 (Shot Table):** Map 100% lines to shared visual assets via `parse_shots.py`.
8. **Step 8 (Rendering & Packaging):** Video render via `build_video3.py` and muxing with SRT subtitles via `package.py --mux`.
