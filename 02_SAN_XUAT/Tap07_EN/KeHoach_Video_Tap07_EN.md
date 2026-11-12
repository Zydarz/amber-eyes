# PRODUCTION PLAN EPISODE 07 · ENGLISH EDITION · "MURDER BY TEXT MESSAGE" (PART B)

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**Script:** `01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md` · **Release Target:** `02_SAN_XUAT/Tap07_EN/xuat_ban/`  
**Date:** November 04, 2026

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md` — 50 elements · **219 sentences** (script rewritten 07/11/2026) |
| Voice Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — Voice Reference Set: VoxCPM2 English (`H_EN`, `D_EN`, `C_EN`, `N1_EN`, `N2_EN`). No emotion tags (M4). Pre-encoded (M1). Tail silence trimmed (M3). |
| Master Output | `02_SAN_XUAT/Tap07_EN/xuat_ban/Tap07_EN_master.mp3` (**1086.8 s / ~18 phút 06 giây** · **−16.0 ± 1 LUFS** · **True Peak <= −1.5 dBFS** · **0 khoảng câm > 0.3 s**) |
| Quality Control (ASR & CER) | **Whisper Base CER:** Trung bình **0.76%**, Trung vị **0.00%** (22/164 câu > 2%). Đạt chuẩn công nghiệp (< 2.0%). |
| Quality Control (Naturalness MOS) | **UTMOSv2 MOS:** Trung bình **3.42 / 5.0** (Dải điểm: 2.07 – 4.03). Đạt chuẩn vượt ngưỡng (>= 3.0 / 5.0). |
| Pitch Separation (Rule G9) | **D (Wolf):** 83.3 Hz · **H (Owl):** 112.1 Hz ($\Delta = +5.14$ nc) · **N1 (Sheep):** 165.1 Hz ($\Delta = +6.70$ nc) · **C (Fox):** 191.6 Hz ($\Delta = +9.27$ nc) · **N2 (Cat):** 246.8 Hz ($\Delta = +4.38$ nc). Toàn bộ $\ge 4.0$ nc ĐẠT 100%. |
| Cast Roles | H: Host (Owl) · D: Investigator (Wolf) · C: Psychologist (Fox) · N1: Lynn Roy (Sheep) · N2: Samantha Boardman (Cat) |
| Video Structure | 50 narrative elements across 5 acts · Subtitles: `Tap07_EN.srt` |
| YouTube US Classification | Education · Not for kids · "Altered or synthetic content" · Self-certification: Forensic & criminological psychology analysis |

> **⚠ REBUILD 09/11/2026 — kịch bản đã viết lại (07/11/2026, 219 câu / 50 element).**
> Bảng shot (mục 6) và timeline (`.work/timeline_s_EN_t07.json`, 219 câu · **27:19**) đã dựng lại
> theo kịch bản mới; lớp chữ trên hình = **nguyên văn câu kịch bản** của shot (219/219 câu).
> Các số liệu audio trong bảng B1 (master 1086.8 s · CER · MOS) là của bản kịch bản CŨ (164 câu)
> và đã được upload/dọn — **cần dựng lại master khi làm video**. Timeline hiện là **ước lượng**
> (theo RATE ký tự/s của timeline cũ) ⇒ thời lượng shot trong bảng là số tạm.
> Ảnh tĩnh 3 ngôn ngữ (223 ảnh/ngôn ngữ): `.work/video3_t07/stills` · `.work/video3_EN_t07/stills` · `.work/video3_JA_t07/stills`.
> **H9**: `text_scrim` 65 shot (đo thật, hợp 3 ngôn ngữ) — sau khi áp: **0 shot** vượt ngưỡng (max 6,6% EN).
> **H12**: `OUTRO` 10 s → **6 s** ⇒ end card (`5-37`) sáng rõ (max 250 · 25,0% pixel sáng).
> Thẻ giới thiệu nhân vật đặt cao + có nền tối ⇒ hết chữ đè chữ; hồi quy Tập 01: hash không đổi.

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
| 1-01 | `1.02#1` (1.7 s) | H | T1 | `t7_digital_coercion_screen`, `pull` | **Welcome back to Amber Eyes.** | — | ✦ Cú |  |
| 1-02 | `1.02#2` (7.3 s) | H | T1 | `t7_highway_50km_isolation`, `still` | *Today, we dissect an unprecedented criminal profile: hands-off crime and lethal psychological manipulation within digital space.* | — | — |  |
| 1-03 | `1.02#3` (8.3 s) | H | T1 | `t7_digital_lighthouse_beacon`, `push` | *Imagine a tragedy with no physical weapon, no physical trace of a fight at the scene, and two central figures separated by more than 56 kilometers.* | — | — |  |
| 1-04 | `1.02#4` (7.5 s) | H | T1 | `t7_social_media_notifications_flood`, `pan` | *Yet, a young woman who was merely 17 years old at the time was subsequently convicted of historic manslaughter in an American court.* | — | — |  |
| 1-05 | `1.02#5` (7.2 s) | H | T1 | `t7_night_sky_breath_of_life`, `pull` | *The entire catastrophe originated from text messages glowing silently in the dead of night and an invisible psychological trap.* | — | — |  |
| 1-06 | `1.02#6` (6.6 s) | H | T1 | `t7_digital_coercion_screen`, `still` | *The case ignited a global media frenzy alongside intense collective paranoia, sending shockwaves throughout society.* | — | — |  |
| 1-07 | `1.02#7` (8.7 s) | H | T1 | `t7_highway_50km_isolation`, `push` | *A grave wake-up call regarding the darkest corners of our hyper-connected virtual world, where words can transform into lethal weapons against human life.* | — | — |  |
| 1-08 | `1.04#1` (7.0 s) | H | T1 | `t7_kmart_parking_lot_morning`, `pan` | *On the morning of July 13, 2014, in the parking lot of a Kmart store in the coastal town of Fairhaven, Massachusetts.* | — | — |  |
| 1-09 | `1.04#2` (7.0 s) | H | T1 | `t7_ford_f250_black_truck`, `pull` | *A black Ford F-250 pickup truck sat completely motionless for hours in a secluded corner behind the department store.* | — | — |  |
| 1-10 | `1.04#3` (7.7 s) | H | T1 | `t7_kmart_police_perimeter`, `still` | *When local police officers approached the vehicle and opened the door, the individual inside the cabin exhibited no signs of life.* | — | — |  |
| 1-11 | `1.04#4` (6.4 s) | H | T1 | `t7_closed_car_window_fog`, `push` | *A suffocating atmosphere permeated the enclosed interior of the vehicle beneath the sweltering summer heat.* | — | — |  |
| 1-12 | `1.04#5` (7.5 s) | H | T1 | `t7_water_pump_equipment`, `pan` | *The morning sun beat down mercilessly upon the steaming asphalt lot, yet inside the cabin lingered the cold silence of despair.* | — | — |  |
| 1-13 | `1.04#6` (7.8 s) | H | T1 | `t7_kmart_parking_lot_morning`, `pull` | *There were no signs of physical altercation, and the victim's personal belongings remained neatly undisturbed on the passenger seat.* | — | — |  |
| 1-14 | `1.06#1` (6.1 s) | H | T1 | `t7_water_pump_equipment`, `still` | *Inside the truck cabin, 18-year-old Conrad Henri Roy III lay completely motionless in solitary despair.* | — | — |  |
| 1-15 | `1.06#2` (4.7 s) | H | T1 | `t7_tugboat_harbor_fog`, `push` | *He had taken his own life following a protracted, agonizing internal conflict.* | — | — |  |
| 1-16 | `1.06#3` (6.5 s) | H | T1 | `t7_tugboat_captain_license`, `pan` | *Conrad Roy was neither a rebellious youth nor a delinquent as popular social misconceptions frequently assume.* | — | — |  |
| 1-17 | `1.06#4` (6.9 s) | H | T1 | `t7_highschool_empty_lockers`, `pull` | *He was a handsome young man, profoundly kind-hearted, hardworking, and blessed with a bright vocational future ahead.* | — | — |  |
| 1-18 | `1.06#5` (9.1 s) | H | T1 | `t7_family_photo_frame_shadow`, `still` | *Conrad had just graduated from high school with honors and proudly earned his marine captain's license to continue his family's maritime towing tradition.* | — | — |  |
| 1-19 | `1.06#6` (6.8 s) | H | T1 | `t7_water_pump_equipment`, `push` | *Yet behind that gentle smile lay a fragile soul, constantly battling severe depression and chronic social anxiety.* | — | — |  |
| 1-20 | `1.06#7` (9.3 s) | H | T1 | `t7_tugboat_harbor_fog`, `pan` | *He had proactively sought medical assistance on multiple occasions, consulting licensed therapists in an earnest effort to overcome his psychological darkness.* | — | — |  |
| 1-21 | `1.06#8` (6.1 s) | H | T1 | `t7_tugboat_captain_license`, `pull` | *Listen now to the heart-wrenching anguish of his mother, Lynn Roy, on that fateful, terrifying morning.* | — | →N1 |  |
| 1-22 | `1.07#1` (6.9 s) | N1 | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *All throughout that morning, a mother's instinct kept warning me that something terribly wrong had happened to my son.* | — | ✦ Cừu |  |
| 1-23 | `1.07#2` (6.6 s) | N1 | T1 | `t7_incoming_call_timer_40min`, `push` | *I repeatedly dialed Conrad's number, but my calls were met only with endless, hollow ringing into empty silence.* | — | — |  |
| 1-24 | `1.07#3` (6.6 s) | N1 | T1 | `t7_witness_trembling_phone`, `pan` | *The moment I received the notification call from local police, my entire world completely collapsed into pieces.* | — | — |  |
| 1-25 | `1.07#4` (8.1 s) | N1 | T1 | `t7_late_night_bedroom_phone`, `pull` | *Initially, I thought in utter heartbreak that my boy had simply surrendered to the persistent depression he had struggled with for so long.* | — | — |  |
| 1-26 | `1.07#5` (8.2 s) | N1 | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *Our family could never have fathomed that an unseen predator had been pulling psychological strings, pushing my son to his demise from afar.* | — | — |  |
| 1-27 | `1.07#6` (6.4 s) | N1 | T1 | `t7_incoming_call_timer_40min`, `push` | *The agony of losing my precious son will forever remain an unhealed scar etched deeply into a mother's heart.* | — | →H |  |
| 1-28 | `1.09#1` (6.7 s) | H | T1 | `t7_dossier_carter_case_07`, `pan` | *The tragedy seemed poised to be filed away as merely another painful teen heartbreak in local municipal police archives.* | — | — |  |
| 1-29 | `1.09#2` (7.6 s) | H | T1 | `t7_forensic_evidence_phone`, `pull` | *However, standard investigative protocols mandated that detectives confiscate and examine all personal effects belonging to the deceased.* | — | — |  |
| 1-30 | `1.09#3` (5.7 s) | H | T1 | `t7_sms_transcript_forensic_binder`, `still` | *Conrad Roy's mobile smartphone was immediately secured and transferred to digital forensics examiners.* | — | — |  |
| 1-31 | `1.09#4` (6.5 s) | H | T1 | `t7_digital_forensic_extraction`, `push` | *They needed to uncover any potential clues that could explain the sudden decision of a recently graduated young man.* | — | →D |  |
| 1-32 | `1.10#1` (7.8 s) | D | T1 | `t7_digital_forensic_extraction`, `pan` | *The investigation was assigned directly to Detective Scott Gordon of the Fairhaven Police Department for digital forensic analysis.* | — | ✦ Sói |  |
| 1-33 | `1.10#2` (8.8 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *When forensic technicians completed an extraction of the phone's internal storage, they unearthed a staggering archive of over 20,000 text messages.* | — | — |  |
| 1-34 | `1.10#3` (9.2 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *The person communicating most intensely with Conrad during his final weeks was a 17-year-old high school girl residing in Plainville named Michelle Carter.* | — | — |  |
| 1-35 | `1.10#4` (6.9 s) | D | T1 | `t7_sms_transcript_forensic_binder`, `push` | *And what unfolded across those transcript pages sent chills down the spines of the most seasoned veteran detectives.* | — | — |  |
| 1-36 | `1.10#5` (5.0 s) | D | T1 | `t7_digital_forensic_extraction`, `pan` | *These were by no means clumsy attempts at peer consolation or youthful awkwardness.* | — | — |  |
| 1-37 | `1.10#6` (7.6 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *This was a sophisticated, systematic, and calculated campaign designed to ensure that the vulnerable victim could not turn back.* | — | — |  |
| 1-38 | `1.10#7` (5.8 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *Each word acted as a psychological barb tightening around the defenses of a mind in deep crisis.* | — | →H |  |
| 1-39 | `1.11#1` (6.0 s) | H | T1 | `t7_psychological_trap_metaphor`, `push` | *A revelation that completely overturned the initial assessments of Bristol County law enforcement authorities.* | — | — |  |
| 1-40 | `1.11#2` (6.8 s) | H | T1 | `t7_psychological_coercion_chess`, `pan` | *The mobile phone was not merely a passive communication instrument, but had served as the actual scene of an invisible crime.* | — | — |  |
| 1-41 | `1.11#3` (6.8 s) | H | T1 | `t7_puppet_strings_metaphor`, `pull` | *The victim had been guided step-by-step into a premeditated psychological snare without even realizing he was being trapped.* | — | — |  |
| 1-42 | `1.11#4` (5.8 s) | H | T1 | `t7_digital_cage_smartphone_glow`, `still` | *The glowing touch screen had become an inescapable cage suffocating every natural instinct to seek rescue.* | — | →C |  |
| 1-43 | `1.12#1` (8.9 s) | C | T1 | `t7_clinical_depression_shadow`, `push` | *In behavioral psychology, an individual experiencing severe clinical depression suffers from a profound erosion of cognitive functioning and resistance willpower.* | — | ✦ Cáo |  |
| 1-44 | `1.12#2` (8.4 s) | C | T1 | `t7_psychological_coercion_chess`, `pan` | *They lose psychological self-protective mechanisms, experience extreme perceptual narrowing, and become hyper-dependent on an external emotional source.* | — | — |  |
| 1-45 | `1.12#3` (8.7 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *When a predatory manipulator enters that hermetic bubble, their judgment rapidly takes on the power of absolute coercion over the victim's vulnerable psyche.* | — | — |  |
| 1-46 | `1.12#4` (7.3 s) | C | T1 | `t7_night_sky_breath_of_life`, `still` | *A collapse in the Theory of Mind prevents the suffering individual from recognizing that the other party is weaponizing their pain.* | — | — |  |
| 1-47 | `1.12#5` (7.4 s) | C | T1 | `t7_clinical_depression_shadow`, `push` | *Emotional isolation within digital space creates an optimal environment for a manipulator to establish total psychological dominance.* | — | — |  |
| 1-48 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 02* · **A LABYRINTH OF THOUSANDS OF TEXT MESSAGES** | — | ⊘ | ◼ |

### ACT 2 — A LABYRINTH OF THOUSANDS OF TEXT MESSAGES · main background `t7_late_night_bedroom_phone`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (6.7 s) | H | T1 | `t7_florida_beach_encounter_2012`, `pan` | *To comprehend the nature of this psychological snare, we must journey back to the summer of 2012 in the state of Florida.* | — | — |  |
| 2-02 | `2.02#2` (7.1 s) | H | T1 | `t7_two_phone_screens_contrast`, `pull` | *There, 16-year-old Conrad Roy and 15-year-old Michelle Carter met by chance while on family vacations visiting mutual relatives.* | — | — |  |
| 2-03 | `2.02#3` (7.7 s) | H | T1 | `t7_social_media_notifications_flood`, `still` | *A bond of mutual empathy swiftly formed between the two teenagers, as both harbored private emotional wounds and felt alienated from peers.* | — | — |  |
| 2-04 | `2.02#4` (7.1 s) | H | T1 | `t7_massachusetts_route_map`, `push` | *They exchanged phone numbers and sustained regular communication after returning to their respective hometowns in Massachusetts.* | — | — |  |
| 2-05 | `2.02#5` (5.9 s) | H | T1 | `t7_plainville_suburban_house`, `pan` | *A peculiar dynamic began to blossom and evolve almost exclusively across countless lines of text messages.* | — | — |  |
| 2-06 | `2.02#6` (8.1 s) | H | T7 tuyến đường | `t7_massachusetts_route_map`, `pull` | *The town of Plainville where Michelle resided was situated merely 35 miles from Conrad's residence in Mattapoisett, less than an hour's drive away.* | — | — |  |
| 2-07 | `2.02#7` (7.4 s) | H | T1 | `t7_florida_beach_encounter_2012`, `still` | *Yet paradoxically, over the span of more than two years maintaining their relationship, they met face-to-face only a handful of times.* | — | — |  |
| 2-08 | `2.02#8` (5.4 s) | H | T1 | `t7_two_phone_screens_contrast`, `push` | *Their romance existed almost entirely within the virtual ether of glowing mobile phone displays.* | — | — |  |
| 2-09 | `2.02#9` (7.5 s) | H | T1 | `t7_social_media_notifications_flood`, `pan` | *They confided their deepest secrets, silent anxieties, and darkest impulses without ever having to navigate real-world physical reality.* | — | — |  |
| 2-10 | `2.02#10` (7.8 s) | H | T1 | `t7_massachusetts_route_map`, `pull` | *Cyberspace fostered an illusion of absolute intimacy while entirely lacking the grounding accountability of genuine interpersonal interaction.* | — | →C |  |
| 2-11 | `2.03#1` (10.7 s) | C | T1 | `t7_late_night_bedroom_phone`, `still` | *During the initial phase of their correspondence, text logs reveal that Michelle Carter acted as a supportive friend, urging Conrad to consult psychiatrists and take medication.* | — | — |  |
| 2-12 | `2.03#2` (7.4 s) | C | T1 | `t7_copied_script_lines_notebook`, `push` | *However, a bizarre and chilling shift began to materialize in early July 2014, roughly ten days prior to the fatal event.* | — | — |  |
| 2-13 | `2.03#3` (4.5 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pan` | *Michelle's posture underwent an abrupt and sinister 180-degree reversal.* | — | — |  |
| 2-14 | `2.03#4` (9.8 s) | C | T1 | `t7_staged_tragedy_mirror`, `pull` | *Rather than encouraging her boyfriend to persist with professional therapy, she began proactively suggesting, validating, and nudging Conrad toward fatal action.* | — | — |  |
| 2-15 | `2.03#5` (6.2 s) | C | T1 | `t7_late_night_bedroom_phone`, `still` | *This marked the active initiation of Fantasy Addiction and the lethal Escalation of Commitment Trap.* | — | — |  |
| 2-16 | `2.03#6` (8.3 s) | C | T1 | `t7_copied_script_lines_notebook`, `push` | *The manipulator developed an insatiable craving for a tragic climax to finalize the dramatic narrative scripted within her imagination.* | — | →D |  |
| 2-17 | `2.05#1` (6.4 s) | D | T1 | `t7_sms_transcript_forensic_binder`, `pan` | *The digital archive preserved dialogues that leave anyone reading them stunned by Michelle's calculated coldness.* | — | — |  |
| 2-18 | `2.05#2` (7.9 s) | D | T1 | `t7_confession_message_turn`, `pull` | *Whenever Conrad voiced hesitation or visceral fear, Michelle consistently weaponized cruel rhetoric to attack his sense of masculine pride.* | — | — |  |
| 2-19 | `2.05#3` (5.4 s) | D | T4 trích dẫn | `t7_witness_trembling_phone`, `still` | *She texted:*“You always say you're gonna do it, but you never do, you're just putting it off.” | — | — |  |
| 2-20 | `2.05#4` (9.0 s) | D | T1 | `t7_psychological_coercion_chess`, `push` | *When Conrad expressed torment that his parents and two younger sisters would be devastated by his loss, Michelle callously stripped away his final moral anchor.* | — | — |  |
| 2-21 | `2.05#5` (6.8 s) | D | T4 trích dẫn | `t7_sms_transcript_forensic_binder`, `pan` | *She wrote:*“Your family will be sad for a while, but they will get over it, they will know you're not in pain anymore.” | — | — |  |
| 2-22 | `2.05#6` (7.9 s) | D | T1 | `t7_confession_message_turn`, `pull` | *Michelle even went so far as to offer detailed instructions on acquiring machinery and selecting an isolated location to prevent detection.* | — | — |  |
| 2-23 | `2.05#7` (7.4 s) | D | T1 | `t7_witness_trembling_phone`, `still` | *This pressure was relentless, arriving at a cadence of dozens of messages per hour, completely encircling the young man's thoughts.* | — | — |  |
| 2-24 | `2.05#8` (8.3 s) | D | T1 | `t7_psychological_coercion_chess`, `push` | *She interrogated him over every tactical detail: whether he had secured the pump, whether his phone was charged, and precisely when he would begin.* | — | →H |  |
| 2-25 | `2.06#1` (9.6 s) | H | T1 | `t7_puppet_strings_metaphor`, `pan` | *From the perspective of investigative behavioral science, this represents an extraordinarily dangerous form of Digital Coercive Control.* | — | — |  |
| 2-26 | `2.06#2` (8.3 s) | H | T1 | `t7_psychological_coercion_chess`, `pull` | *The predator did not deploy physical violence, but targeted the victim's deep-seated guilt and existential fragility.* | — | — |  |
| 2-27 | `2.06#3` (8.7 s) | H | T1 | `t7_digital_cage_smartphone_glow`, `still` | *By dismantling his emotional support network with his family, Michelle funneled Conrad into an absolute cognitive dead end.* | — | — |  |
| 2-28 | `2.06#4` (10.9 s) | H | T1 | `t7_psychological_trap_metaphor`, `push` | *He became convinced that the only way to demonstrate personal worth and avoid disappointing his girlfriend was to follow through on this tragic commitment.* | — | — |  |
| 2-29 | `2.06#5` (9.0 s) | H | T1 | `t7_puppet_strings_metaphor`, `pan` | *The invisible trap snapped firmly shut as the victim was completely isolated between the physical world and digital cyberspace.* | — | — |  |
| 2-30 | `2.06#6` (10.0 s) | H | T1 | `t7_psychological_coercion_chess`, `pull` | *Every psychological exit for the 18-year-old was systematically sealed off by messages that sounded affectionate yet delivered fatal coercion.* | — | — |  |
| 2-31 | `2.08#1` (4.9 s) | H | T1 | `t7_kmart_lot_midnight_darkness`, `still` | *On the night of July 12, 2014, that ruthless psychological snare snapped shut completely.* | — | — |  |
| 2-32 | `2.08#2` (8.1 s) | H | T1 | `t7_water_pump_equipment`, `push` | *Conrad Roy drove his black Ford F-250 pickup into the Kmart parking lot in Fairhaven and began operating the combustion pump inside the sealed cabin.* | — | — |  |
| 2-33 | `2.08#3` (7.7 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pan` | *However, as hazardous fumes began accumulating and primal survival instincts violently took over, the 18-year-old was overwhelmed with terror.* | — | — |  |
| 2-34 | `2.08#4` (6.0 s) | H | T1 | `t7_closed_car_window_fog`, `pull` | *He pushed open the truck door, stepped outside into the fresh night air, and sought to preserve his own life.* | — | — |  |
| 2-35 | `2.08#5` (6.8 s) | H | T1 | `t7_night_sky_breath_of_life`, `still` | *The causal chain of self-destructive intent was at that precise moment shattered by the victim's deliberate act of survival.* | — | — |  |
| 2-36 | `2.08#6` (6.4 s) | H | T1 | `t7_kmart_lot_midnight_darkness`, `push` | *During those critical moments, Conrad remained connected on a live phone call with Michelle Carter back in Plainville.* | — | — |  |
| 2-37 | `2.08#7` (5.0 s) | H | T1 | `t7_water_pump_equipment`, `pan` | *And at that fragile threshold between life and death, an unimaginable decision was voiced.* | — | — |  |
| 2-38 | `2.08#8` (5.0 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pull` | *A command spoken into the darkness stripped away the young man's final opportunity to live.* | — | →D |  |
| 2-39 | `2.09#1` (5.6 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *This is the decisive factual element that determined the entire legal culpability of the case.* | — | — |  |
| 2-40 | `2.09#2` (9.6 s) | D | T1 | `t7_confession_message_turn`, `push` | *Over a phone call spanning many minutes, when Conrad wept and confessed that he was terrified and had stepped out of the vehicle, Michelle did not tell him to stop.* | — | — |  |
| 2-41 | `2.09#3` (7.1 s) | D | T1 | `t7_ticking_clock_deadlines`, `pan` | *She did not call 911, nor did she reach out to Conrad's mother despite possessing her home address and telephone number.* | — | — |  |
| 2-42 | `2.09#4` (6.7 s) | D | T4 trích dẫn | `t7_incoming_call_timer_40min`, `pull` | *Instead, Michelle issued a cold, unequivocal verbal order through the receiver:*“Get back in the truck right now.” | — | — |  |
| 2-43 | `2.09#5` (7.7 s) | D | T1 | `t7_two_phone_screens_contrast`, `still` | *That direct verbal command extinguished the victim's last glimmer of survival, coercing him to climb back into the hazardous cabin.* | — | — |  |
| 2-44 | `2.09#6` (5.8 s) | D | T1 | `t7_confession_message_turn`, `push` | *An act of callous inhumanity demonstrating total, wanton disregard for the sanctity of human life.* | — | — |  |
| 2-45 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 03* · **THE GRIEVING GIRLFRIEND PLAY & THE HISTRIONIC BRAIN** | — | ⊘ | ◼ |

### ACT 3 — THE GRIEVING GIRLFRIEND PLAY & THE HISTRIONIC BRAIN · main background `t7_empty_theater_spotlight`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (5.7 s) | H | T1 | `t7_empty_theater_spotlight`, `pan` | *A profound question that left the general public and courtroom legal experts completely bewildered:* | — | — |  |
| 3-02 | `3.02#2` (8.2 s) | H | T1 | `t7_cracked_porcelain_mask`, `pull` | *What plausible motive could compel a 17-year-old high school girl, raised in a comfortable and stable suburban family, to commit such cruelty?* | — | — |  |
| 3-03 | `3.02#3` (7.5 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *She harbored no personal vengeance, had no financial disputes, and stood to gain zero insurance benefits from Conrad Roy's demise.* | — | — |  |
| 3-04 | `3.02#4` (7.0 s) | H | T1 | `t7_staged_tragedy_mirror`, `push` | *To uncover the answer, we must perform a deep psychological autopsy on Michelle Carter's underlying personality structure.* | — | — |  |
| 3-05 | `3.02#5` (7.3 s) | H | T1 | `t7_empty_theater_spotlight`, `pan` | *A distorted psyche fueled by an insatiable hunger for attention and an obsessive desire to play the starring role in a tragedy.* | — | — |  |
| 3-06 | `3.02#6` (5.7 s) | H | T1 | `t7_cracked_porcelain_mask`, `pull` | *Concealed beneath her wholesome suburban schoolgirl persona lay an abyss of existential emptiness.* | — | — |  |
| 3-07 | `3.02#7` (7.8 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *A lost soul willing to sacrifice the very life of her companion merely to purchase fleeting moments in the limelight of social sympathy.* | — | →C |  |
| 3-08 | `3.03#1` (9.1 s) | C | T1 | `t7_highschool_empty_lockers`, `push` | *Under the lens of forensic psychiatry, Michelle Carter's behavior manifested hallmark traits of Histrionic Personality Disorder intertwined with pathological narcissism.* | — | — |  |
| 3-09 | `3.03#2` (7.9 s) | C | T1 | `t7_cracked_porcelain_mask`, `pan` | *At King Philip Regional High School, Michelle was an unremarkable student, socially awkward, and largely devoid of genuine, intimate friendships.* | — | — |  |
| 3-10 | `3.03#3` (7.3 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *She felt perpetually invisible and isolated, harboring a desperate, frantic craving to become the focal center of validation and pity.* | — | — |  |
| 3-11 | `3.03#4` (8.3 s) | C | T1 | `t7_vintage_tv_glee_glow`, `still` | *To compensate for profound internal vacuity, her narcissistic mind concocted a melodramatic soap-opera narrative where she starred as the tragic heroine.* | — | — |  |
| 3-12 | `3.03#5` (6.2 s) | C | T1 | `t7_highschool_empty_lockers`, `push` | *And vulnerable Conrad Roy was inadvertently selected to serve as the living prop for her grand emotional theater.* | — | — |  |
| 3-13 | `3.03#6` (5.5 s) | C | T1 | `t7_cracked_porcelain_mask`, `pan` | *Such profound objectification reduced a human partner to a mere supplier of narcissistic sustenance.* | — | — |  |
| 3-14 | `3.03#7` (7.1 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *When the prop ceased to fulfill its dramatic function, the manipulator felt no compunction in nudging it toward total destruction.* | — | →H |  |
| 3-15 | `3.04#1` (8.3 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *During trial proceedings, prosecutors demonstrated that Michelle Carter possessed a bizarre, consuming fixation with the musical television series Glee.* | — | — |  |
| 3-16 | `3.04#2` (5.1 s) | H | T1 | `t7_suburban_living_room_tv`, `push` | *In particular, she harbored an intense idolization of lead actress Lea Michele in real life.* | — | — |  |
| 3-17 | `3.04#3` (7.9 s) | H | T1 | `t7_drama_masks_digital_glitch`, `pan` | *In 2013, actor Cory Monteith, Lea Michele's on-screen co-star and off-screen romantic partner, tragically died from an accidental drug overdose.* | — | — |  |
| 3-18 | `3.04#4` (9.9 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *The striking imagery of Lea Michele appearing before the world in elegant black mourning attire, embraced by outpouring adoration from millions, became seared into Michelle's mind.* | — | — |  |
| 3-19 | `3.04#5` (6.8 s) | H | T1 | `t7_vintage_tv_glee_glow`, `still` | *She desperately coveted the revered status of the “grieving widow girlfriend” enveloped in communal sympathy and reverence.* | — | — |  |
| 3-20 | `3.04#6` (4.9 s) | H | T1 | `t7_suburban_living_room_tv`, `push` | *A morbid fantasy took root, metastasizing into an uncontrollable, compulsive obsession.* | — | — |  |
| 3-21 | `3.04#7` (7.9 s) | H | T1 | `t7_drama_masks_digital_glitch`, `pan` | *She went so far as to plagiarize dialogue verbatim from television episodes into her text messages to friends, artificially scripting her grief.* | — | →D |  |
| 3-22 | `3.06#1` (7.6 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *Message logs recovered by Detective Gordon exposed a chilling reality regarding Michelle's psychological rehearsal prior to the death.* | — | — |  |
| 3-23 | `3.06#2` (7.2 s) | D | T1 | `t7_social_media_notifications_flood`, `still` | *On July 10 and 11, 2014, two full days before Conrad actually passed away, Michelle began sending frantic texts to classmates.* | — | — |  |
| 3-24 | `3.06#3` (7.7 s) | D | T1 | `t7_confession_message_turn`, `push` | *She tearfully fabricated claims that Conrad had gone missing, that he had likely taken his life, and that she was completely shattered.* | — | — |  |
| 3-25 | `3.06#4` (6.3 s) | D | T1 | `t7_ticking_clock_deadlines`, `pan` | *Yet in reality, Conrad Roy was alive, spending regular time with his family, having initiated zero fatal acts.* | — | — |  |
| 3-26 | `3.06#5` (8.4 s) | D | T1 | `t7_copied_script_lines_notebook`, `pull` | *Michelle had pre-written the tragic script, assigned dramatic roles to everyone, and the sole missing element was the actual demise of the young man.* | — | — |  |
| 3-27 | `3.06#6` (7.8 s) | D | T1 | `t7_social_media_notifications_flood`, `still` | *She had already publicized her tragedy to peers, and having raised the curtain, she could not permit her theatrical production to unravel.* | — | — |  |
| 3-28 | `3.06#7` (7.0 s) | D | T1 | `t7_confession_message_turn`, `push` | *This calculated preparation established undeniable evidence of premeditated forethought rather than an impulsive reaction.* | — | →H |  |
| 3-29 | `3.07#1` (5.7 s) | H | T1 | `t7_cracked_porcelain_mask`, `pan` | *This represents the decisive Precipitating Stressor and Psychological Tipping Point of the entire case.* | — | — |  |
| 3-30 | `3.07#2` (8.2 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Having prematurely announced to classmates that Conrad had perished, Michelle was gripped by pathological terror: the horror of exposure as a fraud.* | — | — |  |
| 3-31 | `3.07#3` (8.7 s) | H | T1 | `t7_puppet_strings_metaphor`, `still` | *If Conrad had changed his mind and chosen to live, the delicate narrative facade she labored to construct would have instantly disintegrated into humiliation.* | — | — |  |
| 3-32 | `3.07#4` (5.5 s) | H | T1 | `t7_night_sky_breath_of_life`, `push` | *Her fragile narcissistic ego could not tolerate public exposure and mockery under any circumstance.* | — | — |  |
| 3-33 | `3.07#5` (6.7 s) | H | T1 | `t7_cracked_porcelain_mask`, `pan` | *Consequently, on the night of July 12, Michelle's urging transformed from toxic coaxing into frantic, coercive hysteria.* | — | — |  |
| 3-34 | `3.07#6` (5.9 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *Conrad's death became an existential necessity solely to preserve the integrity of her fabricated reality.* | — | — |  |
| 3-35 | `3.07#7` (6.2 s) | H | T1 | `t7_puppet_strings_metaphor`, `still` | *A human life was treated as disposable collateral merely to safeguard the brittle pride of a pathological liar.* | — | →C |  |
| 3-36 | `3.08#1` (6.3 s) | C | T1 | `t7_suburban_living_room_tv`, `push` | *Here we witness the sophisticated execution of Cognitive Compartmentalization alongside Moral Disengagement Techniques.* | — | — |  |
| 3-37 | `3.08#2` (7.5 s) | C | T1 | `t7_clinical_depression_shadow`, `pan` | *In front of parents and educators in Plainville, Michelle maintained the pristine persona of a polite daughter, diligent student, and volunteer.* | — | — |  |
| 3-38 | `3.08#3` (6.6 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *Yet within her secret digital silo, she ruthlessly demoted a human soul into a expendable pawn upon her emotional chessboard.* | — | — |  |
| 3-39 | `3.08#4` (8.3 s) | C | T1 | `t7_psychological_coercion_chess`, `still` | *Michelle anesthetized her conscience through cognitive neutralizations, convincing herself she was “saving” Conrad from worldly agony into a serene afterlife.* | — | — |  |
| 3-40 | `3.08#5` (6.6 s) | C | T1 | `t7_suburban_living_room_tv`, `push` | *A total deficit in affective empathy converted her into an icy predator masquerading behind the facade of a benevolent angel.* | — | — |  |
| 3-41 | `3.08#6` (5.8 s) | C | T1 | `t7_clinical_depression_shadow`, `pan` | *Moral disengagement allowed her to sleep soundly at night immediately after transmitting directives of death.* | — | — |  |
| 3-42 | `3.08#7` (6.7 s) | C | T1 | `t7_drama_masks_digital_glitch`, `pull` | *Her criminal psyche justified the act by insisting that all ultimate culpability belonged to fate and the victim's own despair.* | — | →H |  |
| 3-43 | `3.09#1` (7.4 s) | H | T1 | `t7_baseball_field_charity_empty`, `still` | *Immediately following Conrad's passing, Michelle Carter stepped center stage into the dramatic spotlight she had coveted for years.* | — | — |  |
| 3-44 | `3.09#2` (8.1 s) | H | T1 | `t7_social_media_notifications_flood`, `push` | *She published a deluge of sorrowful tributes across social media, broadcasting emotional memories and receiving hundreds of consoling messages.* | — | — |  |
| 3-45 | `3.09#3` (7.9 s) | H | T1 | `t7_confession_message_turn`, `pan` | *Not stopping there, Michelle spearheaded a charity softball tournament titled Homers for Conrad to raise funds for mental health awareness.* | — | — |  |
| 3-46 | `3.09#4` (7.3 s) | H | T1 | `t7_staged_tragedy_mirror`, `pull` | *She appeared radiant, addressing crowds, graciously accepting bouquets as the living embodiment of resilient, selfless devotion.* | — | — |  |
| 3-47 | `3.09#5` (9.6 s) | H | T1 | `t7_baseball_field_charity_empty`, `still` | *The psychological signature of the perpetrator stood laid bare: She relished every second of public adulation, constructing social status upon the grave of her boyfriend.* | — | — |  |
| 3-48 | `3.09#6` (6.2 s) | H | T1 | `t7_social_media_notifications_flood`, `push` | *The ultimate narcissistic gratification, cloaked flawlessly in the deceptive mantle of humanitarian charity.* | — | — |  |
| 3-49 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 04* · **THE CONFESSION TEXT & A HISTORIC VERDICT** | — | ⊘ | ◼ |

### ACT 4 — THE CONFESSION TEXT & A HISTORIC VERDICT · main background `t7_taunton_courthouse_exterior`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (8.2 s) | H | T1 | `t7_confession_message_turn`, `pan` | *Yet the flawless mask of the saintly, grieving girlfriend could not survive indefinitely against the unyielding illumination of objective truth.* | — | — |  |
| 4-02 | `4.02#2` (8.2 s) | H | T1 | `t7_confession_text_timestamp`, `pull` | *In criminal psychology, histrionic narcissists harbor an inherent Achilles' heel: the compulsive need to boast and validate their covert power.* | — | — |  |
| 4-03 | `4.02#3` (6.6 s) | H | T1 | `t7_psychological_trap_metaphor`, `still` | *Michelle Carter could not suppress the inner urge to boast to someone about her unseen puppet-mastery over events.* | — | — |  |
| 4-04 | `4.02#4` (6.0 s) | H | T1 | `t7_cracked_porcelain_mask`, `push` | *That reckless arrogance generated a piece of golden evidence that permanently sealed her judicial fate.* | — | — |  |
| 4-05 | `4.02#5` (5.6 s) | H | T1 | `t7_confession_message_turn`, `pan` | *Two months after Conrad's departure, a fateful message was dispatched into the digital darkness.* | — | — |  |
| 4-06 | `4.02#6` (5.1 s) | H | T1 | `t7_confession_text_timestamp`, `pull` | *A careless written confession that shattered the deceit hidden behind theatrical tears.* | — | →N2 |  |
| 4-07 | `4.03#1` (6.8 s) | N2 | T1 | `t7_confession_text_timestamp`, `still` | *On the evening of September 15, 2014, I unexpectedly received a lengthy text message from Michelle Carter on my phone.* | — | ✦ Mèo |  |
| 4-08 | `4.03#2` (7.2 s) | N2 | T1 | `t7_witness_trembling_phone`, `push` | *When I opened the screen to read it, my entire body began trembling uncontrollably in disbelief at the words before my eyes.* | — | — |  |
| 4-09 | `4.03#3` (4.7 s) | N2 | T4 trích dẫn | `t7_incoming_call_timer_40min`, `pan` | *Michelle wrote:*“His death is my fault like honestly I could have stopped him.” | — | — |  |
| 4-10 | `4.03#4` (7.1 s) | N2 | T4 trích dẫn | `t7_two_phone_screens_contrast`, `pull` | *She continued:*“I was on the phone with him and he got out of the car because he was scared and I told him to get back in.” | — | — |  |
| 4-11 | `4.03#5` (7.0 s) | N2 | T1 | `t7_confession_text_timestamp`, `still` | *I stood completely paralyzed with sheer horror, realizing who this girl the entire school had been comforting truly was.* | — | — |  |
| 4-12 | `4.03#6` (4.1 s) | N2 | T1 | `t7_witness_trembling_phone`, `push` | *That message haunted my thoughts for many agonizing months thereafter.* | — | →D |  |
| 4-13 | `4.05#1` (7.5 s) | D | T1 | `t7_bristol_county_indictment_stamp`, `pan` | *The confession text sent to Samantha Boardman instantly became the cornerstone of the Bristol County District Attorney's indictment.* | — | — |  |
| 4-14 | `4.05#2` (7.8 s) | D | T1 | `t7_taunton_courthouse_exterior`, `pull` | *In early 2015, Michelle Carter was officially indicted by a grand jury for Involuntary Manslaughter, stunning the American legal landscape.* | — | — |  |
| 4-15 | `4.05#3` (6.3 s) | D | T1 | `t7_empty_courtroom_bench_trial`, `still` | *The trial convened in June 2017 before the Bristol County Juvenile Court in the town of Taunton, Massachusetts.* | — | — |  |
| 4-16 | `4.05#4` (6.4 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *Significantly, the defendant waived her constitutional right to a trial by a jury composed of ordinary citizens.* | — | — |  |
| 4-17 | `4.05#5` (7.2 s) | D | T1 | `t7_bristol_county_indictment_stamp`, `pan` | *Michelle and her defense counsel elected instead for a bench trial decided solely by a single magistrate: Judge Lawrence Moniz.* | — | — |  |
| 4-18 | `4.05#6` (5.8 s) | D | T1 | `t7_taunton_courthouse_exterior`, `pull` | *A calculated legal gamble aimed at sidestepping the intense public indignation of the local community.* | — | — |  |
| 4-19 | `4.05#7` (6.1 s) | D | T1 | `t7_empty_courtroom_bench_trial`, `still` | *They wagered that a seasoned judge would rule rigidly upon strict statutory wording rather than raw emotion.* | — | — |  |
| 4-20 | `4.05#8` (5.3 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *Yet the unvarnished reality of the digital forensic record would decisively dictate her fate.* | — | →H |  |
| 4-21 | `4.06#1` (7.5 s) | H | T1 | `t7_courtroom_projection_screen`, `pan` | *The courtroom captured worldwide headlines as a battleground between opposing legal paradigms and behavioral interpretations.* | — | — |  |
| 4-22 | `4.06#2` (8.3 s) | H | T1 | `t7_us_constitution_amendment1`, `pull` | *Defense attorney Joseph Cataldo argued vigorously that Michelle was not physically present at the parking lot and wielded no lethal weapon.* | — | — |  |
| 4-23 | `4.06#3` (6.7 s) | H | T1 | `t7_sms_transcript_forensic_binder`, `still` | *The defense asserted her messages represented constitutionally protected speech shielded by the First Amendment.* | — | — |  |
| 4-24 | `4.06#4` (8.9 s) | H | T1 | `t7_taunton_courthouse_exterior`, `push` | *Conversely, Assistant District Attorney Katie Rayburn presented thousands of pages of records proving a deliberate, systematic campaign of coercion.* | — | — |  |
| 4-25 | `4.06#5` (7.5 s) | H | T1 | `t7_courtroom_projection_screen`, `pan` | *The prosecution demonstrated that Michelle deployed language like a poison dart aimed at an emotionally incapacitated victim.* | — | — |  |
| 4-26 | `4.06#6` (5.9 s) | H | T1 | `t7_us_constitution_amendment1`, `pull` | *Each razor-sharp evidentiary point systematically exposed the indefensible cruelty of the accused.* | — | →C |  |
| 4-27 | `4.07#1` (4.5 s) | C | T1 | `t7_prescription_pill_bottle_celexa`, `still` | *To shield their client, the defense enlisted psychiatrist Doctor Peter Breggin.* | — | — |  |
| 4-28 | `4.07#2` (8.7 s) | C | T1 | `t7_clinical_depression_shadow`, `push` | *They posited that Michelle suffered from “involuntary intoxication” caused by side effects of the antidepressant Celexa, impairing her capacity for empathy.* | — | — |  |
| 4-29 | `4.07#3` (6.3 s) | C | T1 | `t7_courtroom_projection_screen`, `pan` | *However, this rationalization was thoroughly demolished by prosecutors and forensic behavioral specialists alike.* | — | — |  |
| 4-30 | `4.07#4` (8.9 s) | C | T1 | `t7_psychological_coercion_chess`, `pull` | *Michelle's conduct displayed calculated forethought: deleting records, instructing peers to purge messages, and organizing fundraisers with remarkable lucidity.* | — | — |  |
| 4-31 | `4.07#5` (7.4 s) | C | T1 | `t7_prescription_pill_bottle_celexa`, `still` | *This was not chemical impairment of judgment, but the cold deliberation of a narcissistic personality executing moral neutralization.* | — | →D |  |
| 4-32 | `4.08#1` (6.7 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *On June 16, 2017, the entire courtroom fell dead silent as Judge Lawrence Moniz began delivering his legal verdict.* | — | — |  |
| 4-33 | `4.08#2` (7.6 s) | D | T1 | `t7_courtroom_breathless_silence`, `pan` | *The judge meticulously noted that when Conrad stepped out of the truck, he had broken the chain of self-harm and reclaimed his life.* | — | — |  |
| 4-34 | `4.08#3` (8.3 s) | D | T1 | `t7_courtroom_projection_screen`, `pull` | *However, Michelle's subsequent verbal order to “get back in” accompanied by total failure to summon aid constituted wanton and reckless conduct.* | — | — |  |
| 4-35 | `4.08#4` (8.0 s) | D | T1 | `t7_ticking_clock_deadlines`, `still` | *The judge observed that the defendant created a life-threatening situation and wholly failed in her fundamental duty to render assistance.* | — | — |  |
| 4-36 | `4.08#5` (6.2 s) | D | T1 | `t7_judge_moniz_bench_gavel`, `push` | *Not a single phone call was placed to 911 despite the defendant knowing the exact coordinates of the truck.* | — | — |  |
| 4-37 | `4.08#6` (5.0 s) | D | T1 | `t7_courtroom_breathless_silence`, `pan` | *Judge Moniz solemnly declared: Michelle Carter is guilty of Involuntary Manslaughter.* | — | — |  |
| 4-38 | `4.08#7` (6.3 s) | D | T1 | `t7_courtroom_projection_screen`, `pull` | *A historic ruling dismantling the myth that words uttered from afar cannot constitute homicide under the law.* | — | →H |  |
| 4-39 | `4.09#1` (7.2 s) | H | T1 | `t7_court_verdict_document_guilty`, `still` | *In August 2017, Michelle Carter was sentenced to two and a half years of confinement, with 15 months to be served behind bars.* | — | — |  |
| 4-40 | `4.09#2` (7.9 s) | H | T1 | `t7_bristol_county_jail_bars`, `push` | *At the moment the sentence was announced, the once proud, aloof teenager broke down completely, weeping uncontrollably at the defense table.* | — | — |  |
| 4-41 | `4.09#3` (5.1 s) | H | T1 | `t7_courtroom_breathless_silence`, `pan` | *Yet psychologists recognized those tears were by no means genuine remorse for Conrad Roy.* | — | — |  |
| 4-42 | `4.09#4` (8.1 s) | H | T1 | `t7_cracked_porcelain_mask`, `pull` | *This was the classic manifestation of Narcissistic Collapse, where an entire grandiose illusion of immunity and vanity was publicly shattered.* | — | — |  |
| 4-43 | `4.09#5` (6.9 s) | H | T1 | `t7_court_verdict_document_guilty`, `still` | *The manipulator was finally forced to look into the unforgiving mirror of justice, exposing her true nature to the world.* | — | — |  |
| 4-44 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 05* · **DIGITAL ETHICS & CONRAD'S LAW** | — | ⊘ | ◼ |

### ACT 5 — DIGITAL ETHICS & CONRAD'S LAW · main background `t7_digital_lighthouse_beacon`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (6.9 s) | H | T1 | `t7_massachusetts_state_house_dome`, `push` | *The sentence handed down to Michelle Carter did more than conclude a sensational criminal proceeding in Massachusetts.* | — | — |  |
| 5-02 | `5.02#2` (6.8 s) | H | T1 | `t7_conrads_law_legislative_bill`, `pan` | *It inaugurated a profound transformation in human legal consciousness and ethical accountability in the digital era.* | — | — |  |
| 5-03 | `5.02#3` (7.7 s) | H | T1 | `t7_digital_lighthouse_beacon`, `pull` | *For the first time in modern jurisprudence, courts recognized that physical distance and glass screens offer no sanctuary for crime.* | — | — |  |
| 5-04 | `5.02#4` (7.7 s) | H | T1 | `t7_massachusetts_route_map`, `still` | *Words are not merely emotional expressions; when deployed with coercive malice, they possess the lethal capacity to extinguish life.* | — | — |  |
| 5-05 | `5.02#5` (7.6 s) | H | T1 | `t7_night_sky_breath_of_life`, `push` | *The verdict established an enduring legal precedent safeguarding vulnerable souls against insidious psychological violence online.* | — | — |  |
| 5-06 | `5.02#6` (7.1 s) | H | T1 | `t7_massachusetts_state_house_dome`, `pan` | *An unmistakable moral demarcation was drawn between freedom of speech and the predatory coercion of another human being.* | — | — |  |
| 5-07 | `5.02#7` (5.2 s) | H | T1 | `t7_conrads_law_legislative_bill`, `pull` | *A monumental legal lesson for all who navigate connected platforms in our modern world.* | — | — |  |
| 5-08 | `5.02#8` (8.1 s) | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *From the searing crucible of bereavement, Lynn Roy, Conrad's mother, alongside Massachusetts legislators, has fought tirelessly for years.* | — | — |  |
| 5-09 | `5.02#9` (4.7 s) | H | T1 | `t7_massachusetts_route_map`, `push` | *They have relentlessly championed landmark legislation known as 'Conrad's Law'.* | — | — |  |
| 5-10 | `5.02#10` (9.5 s) | H | T1 | `t7_night_sky_breath_of_life`, `pan` | *The bill's core mandate is to formally criminalize the coercion or encouragement of another person to end their life, carrying penalties up to five years in prison.* | — | — |  |
| 5-11 | `5.02#11` (6.8 s) | H | T1 | `t7_massachusetts_state_house_dome`, `pull` | *The legislation seeks to seal dangerous legal loopholes exploited by sophisticated digital psychological predators.* | — | — |  |
| 5-12 | `5.02#12` (7.3 s) | H | T1 | `t7_conrads_law_legislative_bill`, `still` | *Transforming enduring grief into concrete legal protections so that other families are spared the tragedy that befell Conrad.* | — | →C |  |
| 5-13 | `5.03#1` (5.8 s) | C | T1 | `t7_digital_cage_smartphone_glow`, `push` | *The case leaves a profound societal imprint upon parents navigating the modern smartphone revolution.* | — | — |  |
| 5-14 | `5.03#2` (8.6 s) | C | T1 | `t7_suburban_living_room_tv`, `pan` | *Many parents awoke to the terrifying realization that even while a child sits safely in their bedroom, they can be hunted by unseen predators from afar.* | — | — |  |
| 5-15 | `5.03#3` (6.5 s) | C | T1 | `t7_family_photo_frame_shadow`, `pull` | *Digital displays can become perilous gateways when genuine emotional connection and attentive dialogue are absent.* | — | — |  |
| 5-16 | `5.03#4` (5.6 s) | C | T1 | `t7_mothers_empty_kitchen_phone`, `still` | *In closing this case, we must fully restore dignity and profound respect to Conrad Henri Roy III.* | — | — |  |
| 5-17 | `5.03#5` (7.5 s) | C | T1 | `t7_digital_cage_smartphone_glow`, `push` | *He was never a cold statistic, but a gifted young man, an accomplished maritime tugboat captain imbued with warmth and sensitivity.* | — | — |  |
| 5-18 | `5.03#6` (5.8 s) | C | T1 | `t7_suburban_living_room_tv`, `pan` | *His loss is monumental, yet his story has sounded an enduring wake-up call to protect the vulnerable.* | — | — |  |
| 5-19 | `5.03#7` (6.9 s) | C | T1 | `t7_digital_lighthouse_beacon`, `pull` | *A poignant reminder that compassionate listening and genuine human empathy remain our strongest shields against darkness.* | — | →H |  |
| 5-20 | `5.04#1` (8.2 s) | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Drawing from criminal psychology and the foundational principles of The Gift of Fear, we distill vital survival insights to detect toxic manipulators.* | — | — |  |
| 5-21 | `5.04#2` (6.5 s) | H | T1 | `t7_redflag1_isolated_virtual_bubble`, `push` | *Across virtual spaces teeming with disembodied relationships, four critical red flags must be permanently remembered.* | — | — |  |
| 5-22 | `5.04#3` (7.4 s) | H | T1 | `t7_redflag2_manipulative_text_provocation`, `pan` | *Recognizing these early warning indicators empowers individuals to shield themselves and loved ones from coercive psychological traps.* | — | — |  |
| 5-23 | `5.04#4` (2.0 s) | H | T8 cờ | `t7_redflag1_isolated_virtual_bubble`, `pull` | *01* · **RED FLAG 1: SYSTEMATIC ISOLATION.** | — | — |  |
| 5-24 | `5.04#5` (9.2 s) | H | T1 | `t7_redflag3_performative_grief_stage`, `still` | *The manipulator persistently sows distrust, severing your bonds with family, relatives, and real-world friends to establish themselves as your sole emotional lifeline.* | — | — |  |
| 5-25 | `5.04#6` (2.9 s) | H | T8 cờ | `t7_redflag2_manipulative_text_provocation`, `push` | *02* · **RED FLAG 2: COERCIVE CONTROL DISGUISED AS DEVOTION.** | — | — |  |
| 5-26 | `5.04#7` (8.0 s) | H | T1 | `t7_redflag4_disconnect_phone_dawn`, `pan` | *Your communication, messages, and daily schedule are intensely monitored under the deceptive pretense of “passionate love” or artificial empathy.* | — | — |  |
| 5-27 | `5.04#8` (2.8 s) | H | T8 cờ | `t7_redflag3_performative_grief_stage`, `pull` | *03* · **RED FLAG 3: WEAPONIZED GUILT AND MORAL INVERSION.** | — | — |  |
| 5-28 | `5.04#9` (8.8 s) | H | T1 | `t7_closing_dossier_white_rose`, `still` | *The predator continually makes you feel defective, leveraging your vulnerabilities to demean you and demanding proof of devotion through extreme self-sacrifice.* | — | — |  |
| 5-29 | `5.04#10` (3.3 s) | H | T8 cờ | `t7_redflag4_disconnect_phone_dawn`, `push` | *04* · **RED FLAG 4: NURTURING DARKNESS OVER MEDICAL INTERVENTION.** | — | — |  |
| 5-30 | `5.04#11` (9.1 s) | H | T1 | `t7_digital_lighthouse_beacon`, `pan` | *When you are overwhelmed, rather than guiding you toward professional therapy, they validate self-destructive impulses, romanticizing tragedy into something alluring.* | — | — |  |
| 5-31 | `5.04#12` (7.8 s) | H | T1 | `t7_redflag1_isolated_virtual_bubble`, `pull` | *If you or anyone you know is struggling through severe emotional distress or overwhelming thoughts, remember: You are never alone in the dark.* | — | — |  |
| 5-32 | `5.04#13` (4.7 s) | H | T1 | `t7_digital_lighthouse_beacon`, `still` | *Caring hands and professional resources stand ready to guide you through the storm.* | — | — |  |
| 5-33 | `5.04#14` (6.8 s) | H | T1 | `t7_open_truck_door_fresh_air`, `push` | *In Vietnam, contact the National Child Protection Helpline at 111, or the Ngay Mai Depression Support Line at 096 306 1414.* | — | — |  |
| 5-34 | `5.04#15` (5.6 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pan` | *In the United States and internationally, call or text the 988 Crisis Lifeline for immediate support.* | — | — |  |
| 5-35 | `5.04#16` (5.7 s) | H | T1 | `t7_open_truck_door_fresh_air`, `pull` | *Have the courage to reach out and seek support from those who truly cherish you in the physical world.* | — | — |  |
| 5-36 | `5.04#17`–`#18` (7.5 s) | H | T1 | `t7_redflag2_manipulative_text_provocation`, `still` | *Episode 07 is hereby officially concluded.* → *Thank you for listening to and supporting the deep behavioral insights of Amber Eyes.* | — | — |  |
| 5-37 | hết tập (7,5 s) | — | T1 | `t7_closing_dossier_white_rose`, `pull` | **CASE FILE 07 · CLOSED** · *AMBER EYES · Criminal psychology through real case files* | — | ⊘ | ◼ |

**Tổng:** 223 shot · 219 câu · 31 element lời (5 hồi) · nền dùng 62 loại. Rebuilt 09/11/2026 for the rewritten script of 07/11/2026 (219 câu). Shot durations are **estimated** (no new audio master yet).
