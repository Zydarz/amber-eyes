# PRODUCTION PLAN EPISODE 08 · ENGLISH EDITION · "WHEN GENIUSES ARE BRAINWASHED" (PART B)

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**Script:** `01_KICH_BAN/Tap08_EN/kichban_tap08_EN.md` · **Release Target:** `02_SAN_XUAT/Tap08_EN/xuat_ban/`  
**Date:** November 06, 2026

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap08_EN/kichban_tap08_EN.md` — 53 elements · **171 sentences** |
| Voice Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — Voice Reference Set: VoxCPM2 English (`H_EN`, `D_EN`, `C_EN`, `N1_EN`, `N2_EN`). No emotion tags (M4). Pre-encoded (M1). Tail silence trimmed (M3). |
| Master Output | ⛔ **OLD MASTER REMOVED (A11 §8)** — `02_SAN_XUAT/Tap08_EN/xuat_ban/Tap08_EN_master.mp3` no longer exists. Current timeline is an **ESTIMATE**: `timeline_s_EN_t08.json` = **1309,4 s / ~21 phút 49 giây** (`.work/_build_timeline_t08.py`), stills-only. Re-run TTS + `build_audio3.py` before building the video. |
| Quality Control (ASR & CER) | *(Số đo của master cũ — master đã bị dọn; cần đo lại sau khi dựng lại TTS)* **Whisper Base CER:** Trung bình **0.86%**, Trung vị **0.00%** (25/165 câu > 2%). Đạt chuẩn công nghiệp (< 2.0%). |
| Quality Control (Naturalness MOS) | *(Số đo của master cũ)* **UTMOSv2 MOS:** Trung bình **3.43 / 5.0** (Dải điểm: 1.88 – 4.36). Đạt chuẩn vượt ngưỡng (>= 3.0 / 5.0). |
| Pitch Separation (Rule G9) | **D (Wolf):** 83.2 Hz · **H (Owl):** 111.9 Hz ($\Delta = +5.13$ nc) · **N1 (Sheep):** 173.3 Hz ($\Delta = +7.58$ nc) · **C (Fox):** 188.2 Hz ($\Delta = +9.01$ nc) · **N2 (Cat):** 250.0 Hz ($\Delta = +4.91$ nc). Toàn bộ $\ge 4.0$ nc ĐẠT 100%. |
| Cast Roles | H: Host (Owl) · D: Investigator (Wolf) · C: Psychologist (Fox) · N1: Tokyo Commuter (Sheep) · N2: Dr. Ikuo Hayashi (Cat) |
| Video Structure | 53 narrative elements across 5 acts · Subtitles: `Tap08_EN.srt` (⛔ cũ — 333 cue từ bản 165 câu; phải sinh lại từ timeline 171 câu) |
| YouTube US Classification | Education · Not for kids · "Altered or synthetic content" · Self-certification: Forensic & criminological psychology analysis |

---

## B2. Visual & Audio Rules (US English Edition)

- **V5 — Real persons depicted strictly in silhouette / shadow:** Shoko Asahara and cult members are never depicted with recognizable facial features.
- **Zero victim depictions:** Victims are never depicted, even as silhouettes. Metaphorical objects used instead (subway turnstiles, umbrella, chemical canisters, courtroom shadows).
- **V9 — Criminological & Forensic Focus:** Emphasis on cult psychology, existential vacuum, neural depletion, and moral inversion. No graphic violence, bodily harm, or chemical synthesis recipes.
- **H5 — Zero AI text generation:** All on-screen text rendered by Pillow using clean Unicode fonts.
- **H6/V3 — Text strictly verbatim:** On-screen English text extracted directly from spoken sentences.
- **H12 — Mandatory closing card:** `DOSSIER EPISODE 08 · CLOSED` + `AMBER EYES` + *"Criminal psychology through real case files"*.

## 6. DANH SÁCH SHOT — TẬP 08 (ENGLISH EDITION)

**How to read:** *Vai* = speaker (H Owl · D Wolf · C Fox · N1 Sheep · N2 Cat). The table describes **background + graphics**; badge and bust follow A5.4.
*Nhân vật*: `🅑` = add bust outside the first sentence · `→X` = Host invites X · `✦` = first appearance · `⊘` = hide bust.
Last column: empty = dissolve · `✂` cut · `◼` dip to black.

**Status 06/11/2026:** script rewritten 05/11/2026 (53 elements · 171 sentences) ⇒ shot table rebuilt with **108 shots**. The old master audio was cleaned up (A11 §8), so `timeline_s_EN_t08.json` is an **estimated** timeline (`.work/_build_timeline_t08.py`) usable for stills only; re-run TTS + `build_audio3.py` before building the video.

### CHANNEL INTRO · 0.00–22.41 s · `bgm_music_box.mp3`

Place `assets/brand/intro_kenh.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.

### ACT 1 — A FATEFUL MORNING BENEATH THE STREETS OF TOKYO · main background `t8_tokyo_dawn_fog`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s) | — | T1 | `t8_tokyo_dawn_fog` hiện dần từ đen | *ACT 01 · A FATEFUL MORNING BENEATH THE STREETS OF TOKYO* | — | ⊘ |  |
| 1-01 | `1.02#1`–`#2` | H | T1 | `t8_tokyo_dawn_fog`, `pull` | *On the morning of Monday, March 20, 1995, Tokyo awakened to its usual brisk rhythm of life. Millions of commuters crowded into the subterranean labyrinth of the subway network.* | — | ✦ Cú |  |
| 1-02 | `1.02#3` | H | T1 | `t8_commuter_crowd_station`, `still` | *It was precisely eight o'clock in the morning, the peak rush hour of the entire day.* | — | — |  |
| 1-03 | `1.02#4` | H | T1 | `t8_subway_tracks_perspective`, `pull` | *Five subway trains across three vital artery lines — Chiyoda, Marunouchi and Hibiya — hurtled toward Kasumigaseki Station.* | — | — |  |
| 1-04 | `1.02#5`–`#6` | H | T1 | `t8_kasumigaseki_facade`, `pan` | *Home to the nation's key ministries and the National Police Agency. Japan still took immense pride in its “myth of public safety” — one of the lowest violent crime rates in the world.* | — | — |  |
| 1-05 | `1.04#1` | H | T1 | `t8_chemical_structure_sarin`, `still` | *Yet on each of those trains, men boarded carrying a neurotoxic chemical capable of catastrophic devastation.* | — | — |  |
| 1-06 | `1.04#2` | H | T1 | `t8_umbrella_puncture_action`, `pull` | *Using umbrellas ground to razor-sharp tips, they punctured plastic bags filled with lethal liquid directly onto train floors.* | — | — |  |
| 1-07 | `1.04#3` | H | T1 | `t8_train_doors_closing`, `pan` | *As train doors opened at bustling stations, these perpetrators slipped quietly into the morning crowds, leaving toxic vapors to rise silently among the passengers.* | — | — |  |
| 1-08 | `1.04#4` | H | T4 trích dẫn | `t8_newspaper_wrapped_package`, `still` | *A calculated, coordinated chemical strike aimed directly at innocent citizens.* | — | — |  |
| 1-09 | `1.06#1`–`#2` | H | T1 | `t8_subway_car_mist_vapor`, `pull` | *Within mere minutes, a nightmare unprecedented in Japan's postwar history erupted beneath the streets of Tokyo. Imagine what an ordinary passenger on board experienced that fateful morning.* | — | →N1 |  |
| 1-10 | `1.07#1`–`#2` | N1 | T4 lời kể | `t8_subway_platform_tunnel_dark`, `still` | *I was standing reading a book on the train when I caught a strange, faint odor, almost like paint thinner. Suddenly my eyes began burning and everything around me went pitch black.* | — | ✦ Cừu |  |
| 1-11 | `1.07#3` | N1 | T1 | `t8_dropped_novel_glasses`, `pull` | *My chest tightened into suffocation, and people around me began coughing uncontrollably before rushing blindly toward the exits.* | — | — |  |
| 1-12 | `1.07#4`–`#5` | N1 | T1 | `t8_subway_stairs_escape`, `pan` | *No one understood what was happening, and raw terror instantly consumed the entire platform. It truly felt as though the end of the world had descended upon us in broad daylight.* | — | — |  |
| 1-13 | `1.09#1` | H | T1 | `t8_ambulances_tokyo_street`, `still` | *The chemical strike claimed the lives of fourteen innocent people and severely injured over five thousand eight hundred commuters.* | — | →H |  |
| 1-14 | `1.09#2` | H | T1 | `t8_hospital_triage_corridor`, `pull` | *Two courageous subway station workers, Kazumasa Takahashi and Tsuneo Hishinuma, heroically removed the toxic bags with their bare hands to protect passengers and made the ultimate sacrifice.* | — | — |  |
| 1-15 | `1.09#3`–`#4` | H | T1 | `t8_subway_platform_tunnel_dark`, `still` | *Thousands of survivors were left grappling with severe long-term psychological trauma. Collective paranoia gripped the metropolis: commuters held their breath descending subway stairs and inspected under every seat.* | — | — |  |
| 1-16 | `1.09#5` | H | T1 | `t8_subway_exit_sunlight`, `pull` | *The entire transportation and emergency medical infrastructure of the world's largest metropolis fell into an unprecedented state of paralysis.* | — | — |  |
| 1-17 | `1.11#1` | D | T1 | `t8_tokyo_police_hq`, `pan` | *Immediately following reports of toxic gas releases at Kasumigaseki Station, the National Police Agency recognized this as a coordinated, large-scale terrorist attack.* | — | ✦ Sói |  |
| 1-18 | `1.11#2` | D | T1 | `t8_incident_board_map`, `still` | *The perpetrators intentionally targeted transit lines converging on central government ministries to paralyze the nation's governing apparatus.* | — | — |  |
| 1-19 | `1.11#3`–`#4` | D | T1 | `t8_chemical_structure_sarin`, `pull` | *The operational scheme was meticulously calculated, deploying five synchronized attackers at the exact peak of commuter congestion. The substance was sarin, an artificial nerve agent extraordinarily hazardous and complex to synthesize.* | — | — |  |
| 1-20 | `1.11#5` | D | T2 thẻ hồ sơ | `t8_aum_shinrikyo_emblem_shadow`, `still` | *Every operational footprint at the scene pointed swiftly toward an enigmatic religious organization known as Aum Shinrikyo.* | — | — |  |
| 1-21 | `1.12#1`–`#3` | H | T1 | `t8_dossier_elite_scientists`, `pull` | *Yet what stunned Japan and the world went far beyond the sheer cruelty of the strike itself. The perpetrators were neither a foreign military unit nor hardened street criminals operating on society's margins.* | — | →C |  |
| 1-22 | `1.12#4`–`#5` | H | T1 | `t8_kasumigaseki_facade`, `pan` | *Behind this devastating assault stood top-tier scientists, medical doctors, and intellectual elites educated at Japan's most prestigious universities. Their immaculate academic credentials had created a lethal “Halo Effect”, blinding society and law enforcement for years.* | — | — |  |
| 1-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 02* · **THE BASE AT THE FOOT OF MOUNT FUJI** | — | ⊘ | ◼ |

### ACT 2 — THE BASE AT THE FOOT OF MOUNT FUJI AND THE DEATH LABORATORY · main background `t8_mount_fuji_dawn_somber`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `t8_mount_fuji_dawn_somber`, `pull` | *At dawn on March 22, 1995 — exactly two days after the subway horror beneath Tokyo — over one thousand police officers and chemical warfare specialists mobilized simultaneously.* | — | — |  |
| 2-02 | `2.02#3` | H | T1 | `t8_hazmat_officers_formation`, `still` | *Equipped with heavy gas masks and specialized oxygen tanks.* | — | — |  |
| 2-03 | `2.02#4`–`#5` | H | T1 | `t8_police_convoy_kamikuishiki`, `pan` | *The convoy advanced on Aum Shinrikyo's sprawling compound in Kamikuishiki village, completely isolated at the foot of Mount Fuji — the most extensive search and seizure operation in the history of Japanese law enforcement.* | — | →D |  |
| 2-04 | `2.04#1`–`#2` | D | T1 | `t8_satyam_compound_aerial`, `still` | *The cult's complex, known as Satyam, comprised dozens of monolithic concrete structures fortified with round-the-clock surveillance camera networks. Outwardly, the site posed as a peaceful meditation monastery and an organic agricultural enterprise.* | — | ✦ Sói |  |
| 2-05 | `2.04#3`–`#4` | D | T1 | `t8_satyam_7_exterior`, `pull` | *When investigators entered the building designated as Satyam Number 7, forensic specialists were chilled by what they uncovered. Inside lay no sacred statues or tranquil meditation halls, but a fully operational, industrial-grade chemical weapons factory.* | — | — |  |
| 2-06 | `2.04#5` | D | T1 | `t8_chemical_precursor_drums`, `still` | *Police seized dozens of tons of precursor chemicals alongside advanced organic synthesis machinery valued at millions of dollars.* | — | — |  |
| 2-07 | `2.04#6` | D | T1 | `t8_mi17_helicopter_hangar`, `pan` | *Furthermore, the cult had secretly imported a Russian Mi-17 military helicopter and was actively cultivating deadly anthrax spores.* | — | — |  |
| 2-08 | `2.05#1`–`#2` | H | T3 so sánh | `t8_newspaper_wrapped_package`, `still` | *MODUS OPERANDI* **Bagged umbrellas, staged getaway cars** → *PSYCHOLOGICAL SIGNATURE* **Manifesting the apocalypse** | — | — |  |
| 2-09 | `2.05#3`–`#5` | H | T1 | `t8_aum_shinrikyo_emblem_shadow`, `pull` | *Yet the psychological trigger that launched the strike on that precise date arose from sheer panic within cult leadership. An internal leak revealed a full-scale raid on Kamikuishiki scheduled for March 22 — so the sarin offensive was ordered within a desperate 48-hour window.* | — | — |  |
| 2-10 | `2.05#6`–`#7` | H | T1 | `t8_weapons_of_mass_destruction`, `still` | *His indelible psychological Signature remained the obsessive compulsion to manifest his apocalyptic prophecies into physical reality. He desperately needed to validate his World War Three prophecy before the eyes of his followers.* | — | — |  |
| 2-11 | `2.07#1` | D | T1 | `t8_matsumoto_night_1994`, `pan` | *Subsequent criminal investigations exposed a years-long escalation trajectory of violence that had steadily radicalized the group.* | — | — |  |
| 2-12 | `2.07#2`–`#5` | D | T6 dòng thời gian | `t8_sarin_synthesis_laboratory`, `still` | *First step · Yoga and levitation* → *Second step · Seizure and confinement* → *Third step · Murder in 1989* → *Fourth step · Matsumoto in 1994* | — | — |  |
| 2-13 | `2.07#6`–`#7` | D | T1 | `t8_sakamoto_lawyer_desk`, `pull` | *This behavioral pattern proved that violence escalated relentlessly as the cult sank deeper into unchecked megalomania. The Tokyo subway horror marked the ultimate crescendo of that murderous escalation cycle.* | — | — |  |
| 2-14 | `2.08#1`–`#2` | H | T1 | `t8_mountain_grave_memorial`, `still` | *A religious sect claiming to offer spiritual liberation possessed an arsenal capable of mass extermination. Stimulus tolerance drove their satisfaction threshold ever further, transforming small deceptive parlor tricks into catastrophic terrorism.* | — | — |  |
| 2-15 | `2.08#3`–`#4` | H | T1 | `t8_asahara_shadow_profile`, `pull` | *How did a partially blind ex-patent-medicine salesman successfully assemble and control brilliant intellectuals to construct such a death machine? The answer resides deep within the darkest corridors of behavioral psychology.* | — | — |  |
| 2-16 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 03* · **THE PARADOX OF SCIENTIFIC GENIUS** | — | ⊘ | ◼ |

### ACT 3 — THE PARADOX OF SCIENTIFIC GENIUS · main background `t8_asahara_shadow_profile`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1`–`#2` | H | T1 | `t8_asahara_shadow_profile`, `pull` | *At the helm of Aum Shinrikyo stood Shoko Asahara, whose birth name was Chizuo Matsumoto. Born into an impoverished multi-child family in Kumamoto, he suffered congenital blindness in one eye and severely restricted vision in the other.* | — | — |  |
| 3-02 | `3.02#3` | H | T1 | `t8_todai_red_gate_shadow`, `still` | *In his youth, Matsumoto repeatedly failed competitive entrance examinations for the prestigious University of Tokyo.* | — | — |  |
| 3-03 | `3.02#4` | H | T1 | `t8_chinese_herbal_apothecary`, `pull` | *He later opened an acupuncture clinic and received criminal fines for peddling fraudulent Chinese medicines.* | — | — |  |
| 3-04 | `3.02#5` | H | T4 trích dẫn | `t8_asahara_shadow_profile`, `still` | *A man of fragmented education, unkempt appearance, and profound malignant narcissism.* | — | — |  |
| 3-05 | `3.02#6`–`#7` | H | T1 | `t8_devotion_altar_kneeling`, `pan` | *Yet prostrating at the feet of this partially blind charlatan were some of Japan's finest scientific minds. They eagerly surrendered their fortunes, rational intellects, and moral compasses to a man once dismissed by mainstream society.* | — | — |  |
| 3-06 | `3.03#1`–`#2` | D | T2 thẻ hồ sơ | `t8_dossier_elite_scientists`, `still` | *Forensic profiles of Aum's inner sanctum astonished seasoned detectives with the extraordinary intellectual caliber assembled. Heading the cult's Ministry of Chemistry was Masami Tsuchiya, a brilliant organic chemistry master's graduate from prestigious Tsukuba University.* | — | — |  |
| 3-07 | `3.03#3` | D | T1 | `t8_cosmic_physics_observatory`, `pull` | *Directing the Ministry of Science and Technology was Hideo Murai, a talented Osaka University astrophysicist with published research in cosmic radiation.* | — | — |  |
| 3-08 | `3.03#4` | D | T1 | `t8_virology_electron_microscope`, `still` | *Overseeing the medical division and biological weapons was Seiichi Endo, who completed advanced molecular virology studies at Kyoto University.* | — | — |  |
| 3-09 | `3.03#5`–`#6` | D | T1 | `t8_cardiac_surgery_theatre`, `pan` | *Another key operative was Doctor Tomomasa Nakagawa, an accredited medical physician. Most striking of all, running the cult's medical clinic was Doctor Ikuo Hayashi, a Keio University-educated cardiologist who had served as department chief at a national hospital.* | — | — |  |
| 3-10 | `3.04#1` | H | T4 trích dẫn | `t8_stethoscope_abandoned_drain`, `still` | *A respected cardiologist who had sworn the Hippocratic Oath to preserve human life, brilliant scholars with dazzling academic horizons.* | — | — |  |
| 3-11 | `3.04#2`–`#3` | H | T1 | `t8_intellectual_hubris_chess`, `pull` | *Why did these accomplished professionals abandon their careers to manufacture chemical weapons against their fellow citizens? What systematically demolished the rational cognitive defenses of the nation's brightest minds?* | — | — |  |
| 3-12 | `3.05#1` | C | T9 thuật ngữ | `t8_tokyo_stock_crash_1990`, `still` | **Existential Vacuum** *(A socio-psychological condition)* | — | ✦ Cáo |  |
| 3-13 | `3.05#2`–`#3` | C | T1 | `t8_corporate_salaryman_cogs`, `pull` | *During the early 1990s, Japan endured the devastating collapse of its postwar bubble economy. Japanese society operated as an immense pressure vessel, reducing individual identities to anonymous cogs inside corporate conglomerates.* | — | — |  |
| 3-14 | `3.05#4` | C | T1 | `t8_yoga_meditation_incense`, `still` | *Many elite youths achieved flawless academic scores, yet experienced profound alienation and an agonizing spiritual void regarding life's purpose.* | — | — |  |
| 3-15 | `3.05#5`–`#6` | C | T1 | `t8_asahara_shadow_profile`, `pan` | *Precisely when these brilliant minds felt most isolated, Shoko Asahara presented an expertly disguised verbal snare. He skillfully intertwined Eastern esoteric mysticism with cutting-edge scientific terminology like quantum mechanics, energy fields, and apocalyptic physics.* | — | — |  |
| 3-16 | `3.05#7` | C | T1 | `t8_moral_rationalization_books`, `still` | *This pseudo-scientific synthesis struck a resonant chord in young intellectuals searching for transcendental meaning.* | — | — |  |
| 3-17 | `3.06#1`–`#2` | H | T1 | `t8_intellectual_hubris_chess`, `pull` | *Highly educated individuals harbor a dangerous psychological vulnerability: immense intellectual arrogance. They firmly convince themselves that they are far too clever and analytical to ever fall prey to crude manipulation.* | — | — |  |
| 3-18 | `3.06#3`–`#4` | H | T1 | `t8_moral_rationalization_books`, `still` | *When Asahara bestowed upon them the identity of chosen guardians charged with cosmic salvation, their intellectual hubris sealed the trap. Their formidable intellect failed to protect them; instead, it became an engine of sophisticated rationalization for unthinkable atrocities.* | — | — |  |
| 3-19 | `3.07#1`–`#2` | C | T1 | `t8_yoga_meditation_incense`, `pull` | *To sustain their dual lives, these intellectual disciples engaged in rigorous cognitive Compartmentalization. They locked their civilian identities — gentle fathers, loving sons, ethical professionals — inside one mental drawer, entirely sealed off from the darkness of Satyam.* | — | — |  |
| 3-20 | `3.07#3`–`#5` | C | T1 | `t8_devotion_altar_kneeling`, `pan` | *Concurrently, the guru indoctrinated them with psychological Objectification and dehumanization of victims. In the distorted worldview of Aum scientists, ordinary citizens were no longer human beings with families, but spiritually defiled souls obstructing cosmic purification. Agonized pleas and human lives were reduced to cold data points within chemical synthesis logs.* | — | — |  |
| 3-21 | `3.07#6`–`#8` | C | T1 | `t8_bio_incubator_pathogens`, `still` | *An equally devastating tragedy engulfed the families of these brilliant young intellectuals. Devoted parents, who had celebrated their children's triumphs at premier universities, saw their family identities pulverized when their sons were revealed as terrorists. Countless parents resigned from lifelong careers, living out their remaining days prostrating in public apologies.* | — | — |  |
| 3-22 | `3.08#1`–`#3` | H | T1 | `t8_broken_hippocratic_oath`, `pan` | *Intellect severed from affective empathy becomes the deadliest instrument on earth. Cognitive fragmentation allowed individuals once celebrated as societal role models to orchestrate mass slaughter without feeling internal guilt. Yet to translate warped conviction into physical extermination, the cult deployed mind control techniques far more insidious than ideological manipulation alone.* | — | — |  |
| 3-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 04* · **BRAINWASHING AND THE POA DOCTRINE** | — | ⊘ | ◼ |

### ACT 4 — BRAINWASHING AND THE POA DOCTRINE · main background `t8_poa_twisted_doctrine`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1`–`#2` | H | T1 | `t8_concrete_cell_isolation`, `pull` | *Inside Aum's closed monastic camps, disciples remained completely isolated from the outside world. Passports and identification cards were confiscated, communications with parents were severed, and access to independent news was forbidden.* | — | — |  |
| 4-02 | `4.02#3`–`#4` | H | T1 | `t8_malnutrition_solitary_bowl`, `still` | *Yet the most sinister weapon utilized to crush independent will was systematic physical exhaustion. Followers were restricted to merely two or three hours of sleep nightly while enduring severe caloric restriction and malnutrition.* | — | — |  |
| 4-03 | `4.02#5` | H | T1 | `t8_frontal_lobe_brain_scan`, `pan` | *When the human brain experiences chronic exhaustion, the prefrontal cortex governing critical judgment and moral reasoning shuts down, inducing unquestioning obedience.* | — | — |  |
| 4-04 | `4.03#1`–`#2` | D | T1 | `t8_psi_headgear_electrodes`, `still` | *Police records exposed bizarre technological devices deployed by cult leadership to manipulate follower neurochemistry. They constructed an electrode-lined headpiece named PSI, mandating that disciples wear it for hours on end.* | — | ✦ Sói |  |
| 4-05 | `4.03#3`–`#4` | D | T1 | `t8_hallucinogen_ritual_hall`, `pull` | *The cult claimed this contraption synchronized the wearer's brainwaves with the guru's transcendent frequencies, charging thousands of dollars monthly per device. Furthermore, forensic teams discovered that the cult secretly administered potent hallucinogens like LSD and psychotropics during nocturnal rituals.* | — | — |  |
| 4-06 | `4.03#5` | D | T1 | `t8_bio_incubator_pathogens`, `still` | *Under chemical intoxication and sensory deprivation, young intellectuals genuinely hallucinated divine auras around Asahara, losing any remaining skepticism.* | — | — |  |
| 4-07 | `4.04#1` | H | T9 thuật ngữ | `t8_poa_twisted_doctrine`, `still` | **Poa** *(Tibetan Phowa — Consciousness Transference)* | — | — |  |
| 4-08 | `4.04#2` | H | T1 | `t8_buddhist_mandala_distortion`, `pull` | *In traditional Tibetan Buddhism, Phowa is a sacred meditation practice concerning conscious spiritual transference at the threshold of natural death.* | — | — |  |
| 4-09 | `4.04#3`–`#4` | H | T4 trích dẫn | `t8_broken_hippocratic_oath`, `still` | *Asahara weaponized this ancient spiritual concept into a murderous theological license to extinguish human life. He disguised cold-blooded homicide beneath the sacred veneer of supreme spiritual mercy.* | — | — |  |
| 4-10 | `4.05#1`–`#2` | C | T1 | `t8_apocalypse_prophecy_scroll`, `pull` | *Asahara preached that secular society was irreparably corrupted and hurtling toward an inevitable nuclear Armageddon. He asserted that ordinary civilians, by continuing to live in ignorance, were accumulating disastrous spiritual karma that would plunge them into hell.* | — | ✦ Cáo |  |
| 4-11 | `4.05#3`–`#4` | C | T1 | `t8_devotion_altar_kneeling`, `still` | *Consequently, terminating their physical lives before they accumulated further karmic debt was framed not as murder, but as an act of absolute compassion. This represents the absolute zenith of Moral Disengagement and cognitive neutralization techniques.* | — | — |  |
| 4-12 | `4.05#5`–`#6` | C | T1 | `t8_moral_rationalization_books`, `pan` | *By completely inverting universal ethics, perpetrators genuinely believed their hands were executing holy deeds to rescue their victims. Simultaneously, displacement of responsibility convinced them that they were mere instruments carrying out the absolute will of the Supreme Master.* | — | — |  |
| 4-13 | `4.06#1`–`#2` | H | T1 | `t8_dr_hayashi_umbrella_subway`, `still` | *That demonic theological inversion paralyzed the moral compass of Doctor Ikuo Hayashi, formerly chief of a prestigious cardiology ward. On the morning of March 20, the very hands trained to heal punctured two sarin bags on the Chiyoda subway line.* | — | — |  |
| 4-14 | `4.06#3` | H | T4 trích dẫn | `t8_tokyo_court_witness_stand`, `pull` | *Listen to how that broken man confronted his shattered soul before the Tokyo District Court.* | — | →N2 |  |
| 4-15 | `4.08#1`–`#2` | N2 | T4 lời kể | `t8_grand_courtroom_proceedings`, `still` | *Standing before this court, I do not seek any forgiveness for myself. I was a medical doctor who swore a solemn oath to protect human life at all costs.* | — | ✦ Mèo |  |
| 4-16 | `4.08#3`–`#5` | N2 | T1 | `t8_tokyo_court_witness_stand`, `pull` | *Yet I allowed a twisted ideology to blind my conscience, inflicting irreversible agony upon innocent fellow human beings. Looking into the grief-stricken eyes of the victims' families, I know there is no salvation for my guilt other than confessing the absolute truth. I kneel before the court and submit to the most severe punishment under the law.* | — | — |  |
| 4-17 | `4.09#1`–`#2` | H | T1 | `t8_tokyo_court_gavel_strike`, `still` | *Doctor Hayashi's courageous, detailed confession provided investigators with the indispensable breakthrough needed to unravel Aum's criminal syndicate. Yet another violent shockwave struck directly before the public eye.* | — | — |  |
| 4-18 | `4.09#3` | H | T1 | `t8_murai_assassination_cameras`, `pan` | *On April 23, 1995, cult science minister Hideo Murai was stabbed to death before live television cameras outside Aum's Tokyo headquarters to silence weapon secrets.* | — | — |  |
| 4-19 | `4.09#4` | H | T1 | `t8_police_convoy_kamikuishiki`, `still` | *Despite violent obstruction, the legal dragnet steadily closed around the supreme architect.* | — | — |  |
| 4-20 | `4.09#5` | H | T5 ngày | `t8_hidden_ceiling_hideout`, `still` | *DATE OF DISCOVERY* · **MAY 16 · 1995** | — | — |  |
| 4-21 | `4.09#6`–`#7` | H | T1 | `t8_asahara_shadow_profile`, `pan` | *The self-proclaimed savior of humanity crouched shivering in absolute darkness, clutching ten million yen in cash and gold bars. The prophetic mask shattered, exposing the pathetic terror of a charlatan undergoing complete Narcissistic Collapse.* | — | — |  |
| 4-22 | `4.11#1`–`#3` | D | T1 | `t8_tokyo_court_gavel_strike`, `still` | *The humiliating capture of Shoko Asahara stripped away the entire illusion surrounding the toxic cult leader. There was no supernatural levitation, no divine protection rescuing him from the reach of justice. He stood exposed as a ruthless manipulator, willing to sacrifice hundreds of followers solely to safeguard his personal survival.* | — | — |  |
| 4-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 05* · **THE HISTORIC VERDICT & THE LESSON** | — | ⊘ | ◼ |

### ACT 5 — THE HISTORIC VERDICT & THE LESSON ON FREE THOUGHT · main background `t8_tokyo_dawn_restored_peace`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#2` | H | T1 | `t8_grand_courtroom_proceedings`, `pull` | *The legal trials of Aum Shinrikyo spanned over two decades, comprising one of the most voluminous judicial dockets in Japanese history. Throughout his lengthy trial, Shoko Asahara feigned madness, muttering incoherent gibberish and refusing meaningful engagement with judges or defense counsel.* | — | — |  |
| 5-02 | `5.02#3`–`#5` | H | T1 | `t8_tokyo_court_gavel_strike`, `still` | *This behavior exemplifies classic Narcissistic Collapse and Pathological Self-Pity. Accustomed to uninhibited dominion, he could not bear the indignity of reality once stripped of his manufactured aura of omnipotence. He preferred retreating into mute withdrawal rather than acknowledging the ruinous bankruptcy of his apocalyptic delusion.* | — | — |  |
| 5-03 | `5.03#1` | D | T1 | `t8_thirteen_death_verdicts`, `pan` | *Following exhaustive legal proceedings, the Supreme Court of Japan affirmed the ultimate penalty: capital punishment for Shoko Asahara and twelve core disciples.* | — | ✦ Sói |  |
| 5-04 | `5.03#2` | D | T2 thẻ hồ sơ | `t8_dossier_elite_scientists`, `still` | *Among those condemned were lead chemist Masami Tsuchiya, virologist Seiichi Endo, arms procurement minister Kiyohide Hayakawa, and Doctor Tomomasa Nakagawa.* | — | — |  |
| 5-05 | `5.03#3`–`#5` | D | T1 | `t8_tokyo_court_gavel_strike`, `pull` | *In contrast, Doctor Ikuo Hayashi received life imprisonment, spared the gallows due to his genuine remorse, public repentance, and pivotal cooperation with investigators. In July 2018, the sentences of execution by hanging were formally carried out for Shoko Asahara and all twelve convicted co-conspirators. The decisive hand of justice brought closure to a dark chapter that haunted Japanese society for twenty-three years.* | — | — |  |
| 5-06 | `5.04#1`–`#2` | H | T1 | `t8_tokyo_detention_house_dawn`, `still` | *The tragedy shattered societal innocence and catalyzed sweeping legislative and institutional reforms across Japan. Parliament substantially revised the Religious Corporations Act and enacted specialized security statutes to monitor organizations capable of indiscriminate violence.* | — | — |  |
| 5-07 | `5.04#3` | H | T1 | `t8_murakami_underground_book`, `pull` | *In his acclaimed documentary book “Underground”, novelist Haruki Murakami spent months interviewing dozens of survivors and former Aum members.* | — | — |  |
| 5-08 | `5.04#4`–`#6` | H | T1 | `t8_fragile_boundary_mirror`, `pan` | *He concluded that the boundary separating ordinary citizens from fanatical extremists is far more fragile than modern society dares to admit. When modern life becomes excessively atomized and unfeeling, vulnerable individuals inevitably seek toxic life rafts to anchor their loneliness. True evil does not merely arrive from external monsters; it germinates where human empathy and authentic connection have withered away.* | — | — |  |
| 5-09 | `5.05#1`–`#2` | C | T1 | `t8_tokyo_dawn_restored_peace`, `still` | *The Aum Shinrikyo tragedy offers a chilling warning regarding the vulnerabilities of human cognition. Prestigious academic credentials and formidable logical intellect offer zero immunity against insidious psychological manipulation.* | — | ✦ Cáo |  |
| 5-10 | `5.05#3`–`#4` | C | T1 | `t8_tokyo_dawn_fog`, `pull` | *On the contrary, when exceptional minds lose their grounding in foundational human values, they can become the most devastating weapons of cruelty. Fanaticism invariably begins with intoxicating promises of absolute truth standing above universal ethical norms.* | — | — |  |
| 5-11 | `5.06#1` | H | T1 | `t8_mountain_grave_memorial`, `still` | *To safeguard ourselves and those we love from manipulative, high-control groups, Amber Eyes highlights four vital survival red flags from this historical file.* | — | — |  |
| 5-12 | `5.06#2` | H | T8 cờ | `t8_redflag1_social_isolation`, `still` | *01* · **RED FLAG 1 — SOCIAL ISOLATION & SEVERING SUPPORT NETWORKS** | — | — |  |
| 5-13 | `5.06#3` | H | T1 | `t8_corporate_salaryman_cogs`, `pull` | *Any healthy community respects your family ties and independent social circles; if a group demands cutting contact with loved ones or filtering outside information, walk away immediately.* | — | — |  |
| 5-14 | `5.06#4` | H | T8 cờ | `t8_redflag2_physical_exhaustion`, `still` | *02* · **RED FLAG 2 — PHYSICAL DEPRIVATION TO PARALYZE CRITICAL THINKING** | — | — |  |
| 5-15 | `5.06#5` | H | T1 | `t8_malnutrition_solitary_bowl`, `pull` | *Exercise utmost vigilance toward organizations enforcing chronic sleep deprivation, severe fasting, or exhausting labor under the guise of spiritual purification.* | — | — |  |
| 5-16 | `5.06#6` | H | T8 cờ | `t8_redflag3_cult_of_personality`, `still` | *03* · **RED FLAG 3 — ABSOLUTE AUTHORITARIANISM & FORBIDDING INQUIRY** | — | — |  |
| 5-17 | `5.06#7` | H | T1 | `t8_devotion_altar_kneeling`, `pull` | *Genuine mentors encourage critical thinking and verify empirical reality; only predatory manipulators place themselves above the law and classify honest doubt as sin.* | — | — |  |
| 5-18 | `5.06#8` | H | T8 cờ | `t8_redflag4_moral_inversion`, `still` | *04* · **RED FLAG 4 — MORAL INVERSION & WEAPONIZED HATRED** | — | — |  |
| 5-19 | `5.06#9`–`#10` | H | T1 | `t8_fragile_boundary_mirror`, `pan` | *Decisively reject any doctrine that rationalizes inflicting harm upon fellow human beings in the name of a higher spiritual cause. Authentic truth is never forged upon deception, manufactured fear, or the suffering of our fellow human beings.* | — | — |  |
| 5-20 | `5.08#1` | H | T1 | `t8_tokyo_dawn_restored_peace`, `still` | *The light of intellect holds true value only when guided by genuine compassion and an awake moral conscience.* | — | — |  |
| 5-21 | `5.08#2`–`#4` | H | T1 | `t8_tokyo_dawn_fog`, `pan` | *Thank you for joining Amber Eyes in dissecting today's criminal psychology case file. Please subscribe to the channel, share this documentary, and share your perspective in the comments below. Until our next case file, stay vigilant and take care.* | — | — |  |
| 5-22 | — | — | T1 | `t8_tokyo_dawn_restored_peace` | *DOSSIER EPISODE 08 · CLOSED* · **AMBER EYES** · *Criminal psychology through real case files* | — | ⊘ |  |

**Tổng:** 108 shot · 171 câu · 33 element lời (5 hồi) · nền dùng 70 loại. Rebuilt 06/11/2026 from the rewritten script of 05/11/2026 (53 elements · 171 sentences).
