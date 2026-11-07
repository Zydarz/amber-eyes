# PRODUCTION PLAN EPISODE 07 · ENGLISH EDITION · "MURDER BY TEXT MESSAGE" (PART B)

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**Script:** `01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md` · **Release Target:** `02_SAN_XUAT/Tap07_EN/xuat_ban/`  
**Date:** November 04, 2026

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md` — 50 elements · **147 sentences** (script rewritten 05/11/2026) |
| Voice Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — Voice Reference Set: VoxCPM2 English (`H_EN`, `D_EN`, `C_EN`, `N1_EN`, `N2_EN`). No emotion tags (M4). Pre-encoded (M1). Tail silence trimmed (M3). |
| Master Output | `02_SAN_XUAT/Tap07_EN/xuat_ban/Tap07_EN_master.mp3` (**1086.8 s / ~18 phút 06 giây** · **−16.0 ± 1 LUFS** · **True Peak <= −1.5 dBFS** · **0 khoảng câm > 0.3 s**) |
| Quality Control (ASR & CER) | **Whisper Base CER:** Trung bình **0.76%**, Trung vị **0.00%** (22/164 câu > 2%). Đạt chuẩn công nghiệp (< 2.0%). |
| Quality Control (Naturalness MOS) | **UTMOSv2 MOS:** Trung bình **3.42 / 5.0** (Dải điểm: 2.07 – 4.03). Đạt chuẩn vượt ngưỡng (>= 3.0 / 5.0). |
| Pitch Separation (Rule G9) | **D (Wolf):** 83.3 Hz · **H (Owl):** 112.1 Hz ($\Delta = +5.14$ nc) · **N1 (Sheep):** 165.1 Hz ($\Delta = +6.70$ nc) · **C (Fox):** 191.6 Hz ($\Delta = +9.27$ nc) · **N2 (Cat):** 246.8 Hz ($\Delta = +4.38$ nc). Toàn bộ $\ge 4.0$ nc ĐẠT 100%. |
| Cast Roles | H: Host (Owl) · D: Investigator (Wolf) · C: Psychologist (Fox) · N1: Lynn Roy (Sheep) · N2: Samantha Boardman (Cat) |
| Video Structure | 50 narrative elements across 5 acts · Subtitles: `Tap07_EN.srt` |
| YouTube US Classification | Education · Not for kids · "Altered or synthetic content" · Self-certification: Forensic & criminological psychology analysis |

> **⚠ REBUILD 06/11/2026 — kịch bản đã viết lại (05/11/2026).**
> Bảng shot (mục 6) và timeline (`.work/timeline_s_EN_t07.json`, 147 câu · 18:40) đã dựng lại
> theo kịch bản mới. Các số liệu audio trong bảng B1 (master 1086.8 s · CER · MOS) là của bản
> kịch bản CŨ (164 câu) và đã được upload/dọn — **cần dựng lại master khi làm video**.
> Ảnh tĩnh 3 ngôn ngữ đã render lại: `.work/video3_t07/stills` · `.work/video3_EN_t07/stills` · `.work/video3_JA_t07/stills`.

---

## B2. Visual & Audio Rules (US English Edition)

- **V5 — Real persons depicted strictly in silhouette / shadow:** Conrad Roy and Michelle Carter are never depicted with facial features.
- **Zero victim depictions:** Victims are never depicted, even as silhouettes. Metaphorical objects used instead (phone, parking lot, text transcript).
- **V9 — Criminological & Forensic Focus:** Emphasis on Histrionic Personality Disorder, digital manipulation, and Conrad's Law. No graphic violence, wounds, or self-harm methods.
- **H5 — Zero AI text generation:** All on-screen text rendered by Pillow using clean Unicode fonts.
- **H6/V3 — Text strictly verbatim:** On-screen English text extracted directly from spoken sentences.
- **H12 — Mandatory closing card:** `DOSSIER EPISODE 07 · CLOSED` + `AMBER EYES` + *"Criminal psychology through real case files"*.

---

## 6. DANH SÁCH SHOT — TẬP 07 (ENGLISH EDITION)

**How to read:** *Vai* = speaker (H Owl · D Wolf · C Fox · N1 Sheep · N2 Cat). The table describes **background + graphics**; badge and bust follow A5.4.
*Nhân vật*: `🅑` = add bust outside the first sentence · `→X` = Host invites X · `✦` = first appearance · `⊘` = hide bust.
Last column: empty = dissolve · `✂` cut · `◼` dip to black.

### CHANNEL INTRO · 0.00–22.41 s · `bgm_music_box.mp3`

Place `assets/brand/intro_kenh.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.

### ACT 1 — FATEFUL MORNING AT THE KMART PARKING LOT · main background `t7_kmart_parking_lot_morning`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20.5 s → first voice ≈ 23.0 s) | — | T1 | `t7_digital_coercion_screen` hiện dần từ đen | *ACT 01 · A FATEFUL MORNING AT THE KMART PARKING LOT* | — | ⊘ |  |
| 1-01 | `1.02#1`–`#3` | H | T4 trích dẫn | `t7_digital_coercion_screen`, `pan` | *A tragedy without a murder weapon, without physical traces at the scene, and with the two central figures more than 50 kilometers of highway apart.* | — | ✦ Cú |  |
| 1-02 | `1.02#4`–`#6` | H | T1 | `t7_highway_50km_isolation`, `still` | *It all began with glowing text messages in the dark and an invisible psychological trap — a case that ignited a media frenzy and collective paranoia.* | — | — |  |
| 1-03 | `1.04#1` | H | T1 | `t7_kmart_parking_lot_morning`, `pull` | *On the morning of July 13th, 2014, in the parking lot of a Kmart store in the coastal town of Fairhaven, Massachusetts.* | — | — |  |
| 1-04 | `1.04#2`–`#3` | H | T1 | `t7_ford_f250_black_truck`, `pan` | *A black Ford F-250 pickup truck sat parked silently in a secluded corner; when police officers arrived, the person inside the cabin showed no signs of life.* | — | — |  |
| 1-05 | `1.06#1`–`#2` | H | T1 | `t7_water_pump_equipment`, `still` | *Inside the truck cabin, 18-year-old Conrad Henri Roy III lay motionless in solitary despair.* | — | — |  |
| 1-06 | `1.06#3`–`#5` | H | T1 | `t7_tugboat_harbor_fog`, `pull` | *Conrad Roy was neither a reckless youth nor a delinquent — a handsome, gentle-hearted young man who had just graduated with honors and earned his tugboat captain license.* | — | — |  |
| 1-07 | `1.06#6`–`#7` | H | T1 | `t7_tugboat_captain_license`, `pan` | *Behind that gentle smile lay a fragile soul, constantly struggling with severe clinical depression and relentless anxiety.* | — | — |  |
| 1-08 | `1.06#8` | H | T1 | `t7_mothers_empty_kitchen_phone`, `pull` | *Imagine the heartbreaking agony of his mother, Lynn Roy, on that fateful morning.* | — | →N1 |  |
| 1-09 | `1.07#1`–`#3` | N1 | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *All that morning she sensed something terribly wrong, calling continuously and hearing only a futile ringing tone echo into emptiness.* | — | ✦ Cừu |  |
| 1-10 | `1.07#4`–`#5` | N1 | T1 | `t7_kmart_police_perimeter`, `pull` | *At first she believed only that her son was exhausted by his battle with depression, never suspecting an invisible predator pulling the strings from miles away.* | — | →H |  |
| 1-11 | `1.09#1`–`#3` | H | T1 | `t7_forensic_evidence_phone`, `pan` | *His smartphone, a digital archive of every message from Conrad Roy's final days, was impounded and forensically examined.* | — | →D |  |
| 1-12 | `1.10#1`–`#4` | D | T4 trích dẫn | `t7_digital_forensic_extraction`, `still` | *Digital forensics uncovered a massive archive of thousands of text messages — and the person in most intense contact was a 17-year-old student named Michelle Carter.* | — | ✦ Sói · →H |  |
| 1-13 | `1.11#1`–`#2` | H | T1 | `t7_psychological_trap_metaphor`, `pull` | *Neither words of comfort nor empathetic encouragement — but a systematic coercion campaign, a sinister web designed to eliminate every exit for the victim.* | — | →C |  |
| 1-14 | `1.12#1`–`#3` | C | T1 | `t7_clinical_depression_shadow`, `pan` | *Someone in severe depression has a profoundly fragmented cognitive structure, torn between survival instinct and the desire to escape mental agony.* | — | ✦ Cáo · →H |  |
| 1-15 | `1.13#1`–`#2` | H | T2 thẻ hồ sơ | `t7_dossier_carter_case_07`, `still` | *Luminous words on a digital screen ceased to be harmless communication and became a lethal weapon in the hands of a ruthless killer.* | — | — |  |

### ACT 2 — A LABYRINTH OF THOUSANDS OF TEXT MESSAGES · main background `t7_late_night_bedroom_phone`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#3` | H | T1 | `t7_florida_beach_encounter_2012`, `pan` | *The two first met by chance in 2012 in Florida: Conrad was 16 years old, while Michelle Carter had just turned 15.* | — | →D |  |
| 2-02 | `2.03#1`–`#2` | D | T7 tuyến đường | `t7_massachusetts_route_map`, `still` | *Michelle Carter lived in Plainville, only about 35 miles from Conrad's home in Fairhaven — less than an hour's drive.* | — | — |  |
| 2-03 | `2.03#3`–`#4` | D | T1 | `t7_late_night_bedroom_phone`, `pull` | *Over more than two years together, they met in person only a handful of times; their entire emotional universe lived inside digital space.* | — | →H |  |
| 2-04 | `2.04#1`–`#3` | H | T4 trích dẫn | `t7_plainville_suburban_house`, `pan` | *In the early stages Michelle Carter appeared to be an empathetic, supportive girlfriend who even urged Conrad to consult therapists.* | — | — |  |
| 2-05 | `2.04#4`–`#6` | H | T1 | `t7_two_phone_screens_contrast`, `still` | *At the beginning of July 2014, a chilling psychological pivot occurred: Michelle executed a 180-degree reversal and became the catalyst of tragedy.* | — | →D |  |
| 2-06 | `2.06#1` | D | T4 trích dẫn | `t7_sms_transcript_forensic_binder`, `pull` | *Forensic phone records from early July reveal the chilling volume and cold detachment of these coercive messages.* | — | — |  |
| 2-07 | `2.06#2` | D | T1 | `t7_ticking_clock_deadlines`, `pan` | *Michelle repeatedly berated Conrad for saying he would do it without ever acting, urging him not to delay any longer.* | — | →H |  |
| 2-08 | `2.07#1`–`#2` | H | T1 | `t7_family_photo_frame_shadow`, `still` | *When Conrad feared what his parents and two younger sisters would feel, Michelle coldly dismantled that moral barrier: they would understand, grieve, and move on.* | — | →C |  |
| 2-09 | `2.08#1`–`#4` | C | T1 | `t7_psychological_coercion_chess`, `pull` | *The fantasy cycle and escalation trajectory: once the sense of significance saturated, she pivoted to manipulation targeting the victim's self-esteem and shame.* | — | →H |  |
| 2-10 | `2.09#1`–`#2` | H | T1 | `t7_kmart_lot_midnight_darkness`, `pan` | *On the night of July 12th, 2014, that invisible psychological trap snapped shut entirely.* | — | — |  |
| 2-11 | `2.09#3`–`#4` | H | T1 | `t7_open_truck_door_fresh_air`, `still` | *Right on the fragile boundary between life and death, the survival instinct surged: terrified, Conrad opened the cabin door and stepped out seeking air and safety.* | — | ⊘ |  |
| 2-12 | `2.09#5`–`#6` | H | T1 | `t7_night_sky_breath_of_life`, `pull` | *He stayed on an open line with Michelle Carter, yet what he received in return was neither words of deterrence nor a lifeline pulling him back to life.* | — | ⊘ · →D |  |
| 2-13 | `2.10#1`–`#2` | D | T1 | `t7_incoming_call_timer_40min`, `pan` | *That late-night call lasted over 40 minutes and was never directly recorded by the telecom servers.* | — | — |  |
| 2-14 | `2.10#3` | D | T1 | `t7_closed_car_window_fog`, `still` | *She never dialed 911, never alerted the victim's family, and stayed on the line until every sound from the other end fell utterly silent.* | — | ⊘ · →H |  |

### ACT 3 — THE GRIEVING GIRLFRIEND PLAY & THE HISTRIONIC BRAIN · main background `t7_empty_theater_spotlight`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1`–`#2` | H | T1 | `t7_empty_theater_spotlight`, `pan` | *The question that stunned the public: what was the true motive behind such cruelty?* | — | →C |  |
| 3-02 | `3.03#1`–`#3` | C | T1 | `t7_drama_masks_digital_glitch`, `still` | *Histrionic Personality Disorder intertwined with Digital Münchausen syndrome: Conrad Roy was “Objectified” into a prop serving her narcissistic theater.* | — | →H |  |
| 3-03 | `3.04#1`–`#3` | H | T1 | `t7_highschool_empty_lockers`, `pull` | *At King Philip Regional High School, Michelle Carter was a peripheral student, socially awkward and permanently isolated by her peers.* | — | →D |  |
| 3-04 | `3.05#1`–`#2` | D | T1 | `t7_vintage_tv_glee_glow`, `pan` | *In court, prosecutors unmasked a chilling revelation: Michelle Carter was deeply obsessed with the hit musical series Glee.* | — | — |  |
| 3-05 | `3.05#3`–`#4` | D | T1 | `t7_copied_script_lines_notebook`, `still` | *Digital forensics discovered that Michelle transcribed emotional dialogue from that show word for word, and sent it to her friends and to Conrad.* | — | →H |  |
| 3-06 | `3.06#1`–`#3` | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Michelle Carter wanted a tragedy of her own, to stand in the spotlight and receive universal admiration — and the prerequisite was that Conrad Roy had to perish.* | — | — |  |
| 3-07 | `3.06#4` | H | T1 | `t7_suburban_living_room_tv`, `pan` | *She was already acting out the role of a frantic girlfriend in mourning, even while she held the unfolding reality in the palm of her hand via her phone.* | — | →C |  |
| 3-08 | `3.07#1`–`#3` | C | T1 | `t7_puppet_strings_metaphor`, `still` | *The mechanism of “Compartmentalization” combined with Techniques of Neutralization to completely eradicate moral culpability.* | — | →H |  |
| 3-09 | `3.08#1`–`#3` | H | T1 | `t7_social_media_notifications_flood`, `pull` | *Immediately after Conrad's death, Michelle Carter flooded social media with tearful tributes and organized a charity softball tournament called “Homers for Conrad”.* | — | — |  |
| 3-10 | `3.08#4`–`#5` | H | T1 | `t7_baseball_field_charity_empty`, `pan` | *At that event she stood beaming at center stage, basking in the local community's praise — the most flawless performance of her life.* | — | — |  |
| 3-11 | `3.08#6` | H | T1 | `t7_cracked_porcelain_mask`, `still` | *Until one day, her compulsion to overshare and her sheer arrogance tore that elaborate disguise to pieces.* | — | — |  |

### ACT 4 — THE CONFESSION TEXT & A HISTORIC VERDICT · main background `t7_taunton_courthouse_exterior`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1`–`#4` | H | T4 trích dẫn | `t7_confession_text_timestamp`, `pan` | *On September 15th, 2014, two months after Conrad's death, Michelle sent a fateful text to her close friend Samantha Boardman.* | — | →N2 |  |
| 4-02 | `4.03#1`–`#2` | N2 | T1 | `t7_witness_trembling_phone`, `still` | *Michelle admitted she was on the phone when Conrad stepped out of the truck in terror, and that she commanded him to get back inside.* | — | ✦ Mèo |  |
| 4-03 | `4.03#3` | N2 | T4 trích dẫn | `t7_confession_message_turn`, `pull` | *The girlfriend who cried incessantly before everyone turned out to be the very one who coldly forced Conrad back to his doom.* | — | →H |  |
| 4-04 | `4.05#1`–`#3` | H | T2 thẻ hồ sơ | `t7_bristol_county_indictment_stamp`, `pan` | *The confession and the digital extraction became ironclad evidence to indict Michelle Carter — the trial opened in June 2017 in Taunton.* | — | — |  |
| 4-05 | `4.05#4`–`#5` | H | T1 | `t7_taunton_courthouse_exterior`, `still` | *She waived her right to a jury trial, placing her entire legal fate in the hands of a single jurist: Judge Lawrence Moniz.* | — | — |  |
| 4-06 | `4.05#6` | H | T1 | `t7_empty_courtroom_bench_trial`, `pull` | *A calculated gamble to sidestep public emotional outrage and lean on cold technical legal arguments.* | — | →D |  |
| 4-07 | `4.06#1`–`#2` | D | T4 trích dẫn | `t7_courtroom_projection_screen`, `pan` | *Defense attorney Joseph Cataldo argued his client was never at the scene, invoking the First Amendment of the United States Constitution on freedom of speech.* | — | — |  |
| 4-08 | `4.06#3`–`#4` | D | T1 | `t7_us_constitution_amendment1`, `still` | *Assistant District Attorney Katie Rayburn presented comprehensive message logs chronologically and forcefully, proving the coercion was systematic and meticulously calculated.* | — | →C |  |
| 4-09 | `4.07#1`–`#4` | C | T1 | `t7_prescription_pill_bottle_celexa`, `pull` | *The defense claimed Carter suffered from “involuntary intoxication” caused by Celexa — but the court unequivocally rejected the rationalization.* | — | →H |  |
| 4-10 | `4.08#1`–`#4` | H | T1 | `t7_judge_moniz_bench_gavel`, `pan` | *On June 16th, 2017, Judge Lawrence Moniz delivered his verdict with steely resolve: Carter's command to send Conrad back into the truck was wanton and reckless conduct.* | — | — |  |
| 4-11 | `4.08#5` | H | T1 | `t7_courtroom_breathless_silence`, `still` | *The judge announced authoritatively: Michelle Carter is guilty of involuntary manslaughter.* | — | — |  |
| 4-12 | `4.10#1`–`#2` | H | T2 thẻ hồ sơ | `t7_court_verdict_document_guilty`, `pull` | *In August 2017, Michelle Carter was sentenced to two and a half years in prison, with 15 months of mandatory jail time.* | — | — |  |
| 4-13 | `4.10#3` | H | T1 | `t7_bristol_county_jail_bars`, `pan` | *The raw manifestation of “Narcissistic Collapse” and pathological self-pity as her honorable facade crumbled before the world.* | — | — |  |

### ACT 5 — DIGITAL ETHICS & CONRAD'S LAW · main background `t7_digital_lighthouse_beacon`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#3` | H | T1 | `t7_massachusetts_state_house_dome`, `pan` | *For the first time, jurisprudence recognized that geographic distance and glowing screens are never a shield against criminal liability.* | — | — |  |
| 5-02 | `5.02#4`–`#5` | H | T1 | `t7_conrads_law_legislative_bill`, `still` | *Words spoken into digital space wield the power of mental coercion and can become a deadly weapon without physical contact.* | — | →C |  |
| 5-03 | `5.03#1`–`#3` | C | T1 | `t7_digital_cage_smartphone_glow`, `pull` | *Screens glowing through the late hours become invisible psychological cages, where coercion unfolds while families remain completely unaware.* | — | →H |  |
| 5-04 | `5.04#1`–`#3` | H | T4 trích dẫn | `t7_conrads_law_legislative_bill`, `pan` | *Conrad's Law — the statute pushed through by lawmakers to criminalize coercing or manipulating another person toward self-harm.* | — | — |  |
| 5-05 | `5.04#4` | H | T8 cờ | `t7_redflag1_isolated_virtual_bubble`, `pan` | *01* · **RED FLAG 1 — BEWARE OF HYPER-ACCELERATED, ISOLATED VIRTUAL RELATIONSHIPS** | — | — |  |
| 5-06 | `5.04#5`–`#7` | H | T8 cờ | `t7_redflag2_manipulative_text_provocation`, `still` | *02* · **RED FLAG 2 — RECOGNIZE PSYCHOLOGICAL LEVERAGE THAT TARGETS SELF-ESTEEM THROUGH TOXIC DARES** | — | — |  |
| 5-07 | `5.04#8`–`#10` | H | T8 cờ | `t7_redflag3_performative_grief_stage`, `pull` | *03* · **RED FLAG 3 — CAUTION AGAINST THOSE WHO DRAMATIZE TRAGEDY AND THIRST FOR ATTENTION ON SOCIAL MEDIA** | — | — |  |
| 5-08 | `5.04#11`–`#13` | H | T8 cờ | `t7_redflag4_disconnect_phone_dawn`, `pan` | *04* · **RED FLAG 4 — TRUST YOUR CORE SURVIVAL INSTINCT AND CUT OFF COMMUNICATION DECISIVELY** | — | — |  |
| 5-09 | `5.04#14`–`#15` | H | T1 | `t7_redflag4_disconnect_phone_dawn`, `pull` | *The moment you sense toxicity in the other party's words, that is your survival instinct calling — put the phone down and step back into the physical world.* | — | — |  |
| 5-10 | `5.04#16`–`#17` | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Words on a screen carry no physical mass, yet they hold the power to redeem or destroy a human life.* | — | — |  |
| 5-11 | `5.04#18`–`#19` | H | T1 | `t7_closing_dossier_white_rose`, `pull` | *Thank you for joining Amber Eyes in dissecting this criminal psychology dossier — please subscribe and share your thoughts in the comments.* | — | — |  |
| 5-12 | end of episode (10 s) | — | T1 | `t7_closing_dossier_white_rose`, `pull` | *DOSSIER EPISODE 07 · CLOSED* · **AMBER EYES** · *Criminal psychology through real case files* | — | — | — |

**Tổng:** 66 shot · 147 câu · 34 element lời (5 hồi) · nền dùng 61 loại. Rebuilt 06/11/2026 for the rewritten script of 05/11/2026.
