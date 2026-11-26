# PRODUCTION DOSSIER · EPISODE 24 · "MEMORIES OF THE HWASEONG SERIAL KILLER" — EN EDITION

*Hồ sơ sản xuất Tập 24 — bản EN · sinh từ bảng shot chuẩn VN theo A8.1 (mục c): giữ nguyên mã shot / nền / mẫu T / camera; chỉ đổi cột Chữ sang ngôn ngữ đích.*

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Vụ án | Hồ sơ Lee Choon-jae — Hwaseong & Busan, Hàn Quốc (1986–1991) |
| Ngôn ngữ | EN |
| Số câu thoại | 246 (mã câu trùng khớp 100% với bản VN) |
| Số shot | 246 · 155 nền dùng chung cho 3 ngôn ngữ |
| Thời lượng audio | 2137.4 s (35.6 phút) — đo từ master `Tap24_EN_master.mp3` |
| Intro | `assets/brand/intro_kenh_EN.mov` · 0,00–22,41 s |
| Nền | `assets/bg/t24_*.png` — 155 ảnh 2112×1188, dùng chung VN/EN/JA (H25) |

## B2. Cấu trúc 5 Hồi

### ACT 1: THE NIGHT FIELDS OF HWASEONG & 33 YEARS IN THE FOG — 58 shot

### ACT 2: THE PSYCHOLOGICAL DUEL AT BUSAN PRISON & THE CHILLING CONFESSION — 48 shot

### ACT 3: PSYCHOLOGICAL DECONSTRUCTION: THE POWER-CONTROL KILLER & THE CONFESSION PARADOX — 49 shot

### ACT 4: THE CENTURY'S EXONERATION TRIAL & JUSTICE'S FORMAL APOLOGY — 56 shot

### ACT 5: REFLECTIONS & 4 CRITICAL SURVIVAL RED FLAGS AGAINST NOCTURNAL PREDATORS — 35 shot

## B3. Bảng phân vai

| Ký hiệu | Vai trò | Số câu |
|---|---|---:|
| H | Host (Dẫn chuyện) | 130 |
| D | Điều tra viên | 42 |
| C | Chuyên gia tâm lý | 53 |
| N | Người trong cuộc | 21 |
| **TỔNG** | | **246** |

## B4. Danh mục Cue âm thanh & SFX đồng bộ

| Mốc | Hồi | Loại | Mô tả |
|---|---:|---|---|
| `1.01` | 1 | BGM | *Somber Cello, howling winds across barren fields, accompanied by gentle rain creating a suffocating atmosphere of tragedy.* |
| `1.03` | 1 | SFX | *Police sirens blaring urgently in the night, hurried footsteps splashing frantically across muddy soil.* |
| `1.07` | 1 | SFX | *Sound of turning fragile archival paper files, heavy exhausted sigh in an otherwise silent room.* |
| `1.10` | 1 | SFX | *Rhythmic typing on computer keyboard in forensic laboratory, electronic beep of optical DNA scanners.* |
| `1.14` | 1 | BGM | *Cello fades down into deep, tense, probing piano chords.* |
| `2.01` | 2 | BGM | *Deliberate rhythmic pulse, repetitive minimalist piano echoing the suffocating atmosphere of a prison interrogation room.* |
| `2.03` | 2 | SFX | *Slight scraping of metal chairs against concrete floor, pouring hot coffee into paper cups.* |
| `2.06` | 2 | SFX | *Deep intake of breath, firm placement of a paper cup onto a wooden tabletop.* |
| `2.08` | 2 | SFX | *Crisp sound of flipping investigative document pages, frustrated sigh of veteran police officers.* |
| `2.12` | 2 | BGM | *Urgent, sharp violin phrases building dramatic tension before transitioning into deep analytical tones.* |
| `3.01` | 3 | BGM | *Eerie synth pads and deep resonant bass lines underpinning rigorous academic and psychological behavioral analysis.* |
| `3.10` | 3 | BGM | *Deep, warm piano melodies emerge, preparing for the solemn atmosphere of the historic courtroom.* |
| `4.01` | 4 | BGM | *Solemn courtroom chimes reverberating slowly, intertwined with poignant, dignified strings full of emotional gravity.* |
| `4.03` | 4 | SFX | *Three solemn, deliberate strikes of the judicial gavel, followed by gasps and muffled applause.* |
| `4.05` | 4 | SFX | *Continuous rapid clicks of press camera shutters, clamor of broadcast journalists.* |
| `4.09` | 4 | SFX | *Heavy, metallic clang of prison transport vehicle doors shutting resolutely.* |
| `4.15` | 4 | BGM | *Gentle, warm piano melodies create an open reflective space for practical survival lessons.* |
| `5.01` | 5 | BGM | *Warm acoustic strings paired with soft piano melodies, delivering a peaceful yet deeply contemplative ambiance.* |
| `5.06` | 5 | BGM | *Warm piano melodies gradually fade out, concluding in serene silence and profound contemplation.* |

## B5. Kế hoạch triển khai kỹ thuật

1. `parse_shots.py` → `.work/shots_EN.json` (mốc thời gian chỉ lấy từ `timeline_s_EN.json`).
2. `qc_bg_usage.py` → dùng hết 155 ảnh, 0 nền vượt 3 shot/30 s (H22).
3. `build_video3.py --stills` → soi ảnh tĩnh 100 % shot (H9).
4. `build_video3.py --workers 6` → dựng hình.
5. `subtitles.py` + `package.py --mux` → phụ đề, thumbnail, thẻ kết.

## 6. DANH SÁCH SHOT — TẬP 24 (EN)

Nền `t24_*` là **tài sản dùng chung cho cả 3 ngôn ngữ** (H25/A8.1) — mã shot giống nhau luôn dùng cùng một nền.

### INTRO KÊNH · 0,00–22,41 s

Đặt `assets/brand/intro_kenh_EN.mov` tại 0,00 s (A5.7). Không câu thoại nào thuộc intro.

### ACT 1: THE NIGHT FIELDS OF HWASEONG & 33 YEARS IN THE FOG

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.02#1` (10,6 s) | H | T1 | `t24_a1_23_rural_village_lane_fog_23`, `still` | *In the late 1980s, across the rural expanse of Hwaseong in Gyeonggi Province, not far from Seoul, an unprecedented atmosphere of gloom and terror descended upon South Korea.* | — | ✦ Owl | |
| 1-02 | `1.02#2` (11,1 s) | H | T1 | `t24_a1_01_desolate_rice_paddies_mist_01`, `pan` | *Beginning in the autumn of 1986 and lasting until the spring of 1991, a harrowing series of 10 murders occurred in rapid succession along quiet rice paddies and secluded dirt roads.* | — | ✦ Owl | |
| 1-03 | `1.02#3` (7,1 s) | H | T1 | `t24_a1_02_rural_village_lane_fog_02`, `push` | *The victims were all women of varying ages, ambushed in the dead of night while walking home from work or crossing isolated rural pathways.* | — | ✦ Owl | |
| 1-04 | `1.02#4` (6,5 s) | H | T1 | `t24_a1_02_rural_village_lane_fog_02`, `pull` | *That relentless sequence of crimes transformed Hwaseong into the most terrifying focal point in modern Korean history.* | — | ✦ Owl | |
| 1-05 | `1.02#5` (7,8 s) | H | T1 | `t24_a1_03_gravel_road_twilight_03`, `still` | *Whenever dusk fell, not a single woman dared step outside her front door, and chilling rumors regarding red clothing spread rapidly across the villages.* | — | ✦ Owl | |
| 1-06 | `1.02#6` (6,0 s) | H | T1 | `t24_a1_03_gravel_road_twilight_03`, `pan` | *It was this legendary cold case that eventually inspired the acclaimed 2003 film Memories of Murder.* | — | ✦ Owl | |
| 1-07 | `1.02#7` (9,2 s) | H | T1 | `t24_a1_04_desolate_rice_paddies_mist_04`, `push` | *At that time, South Korea was experiencing rapid socioeconomic transformation, yet rural street lighting and surveillance infrastructure were virtually non-existent.* | — | ✦ Owl | |
| 1-08 | `1.02#8` (8,1 s) | H | T1 | `t24_a1_04_desolate_rice_paddies_mist_04`, `pull` | *This severe technological void inadvertently turned the vast, unlit agricultural plains into an ideal hunting ground for an anonymous predator.* | — | ✦ Owl | |
| 1-09 | `1.04#1` (6,8 s) | H | T1 | `t24_a1_05_police_patrol_rural_search_05`, `still` | *To hunt down this invisible phantom of terror, the South Korean government launched an investigation of unprecedented magnitude.* | — | ✦ Owl | |
| 1-10 | `1.04#2` (4,6 s) | H | T1 | `t24_a1_05_police_patrol_rural_search_05`, `pan` | *Over 2 million police personnel were deployed throughout the exhaustive multi-year manhunt.* | — | ✦ Owl | |
| 1-11 | `1.04#3` (5,9 s) | H | T1 | `t24_a1_06_police_patrol_rural_search_06`, `push` | *More than 21,000 individuals were brought in for questioning and subjected to intense scrutiny over the years.* | — | ✦ Owl | |
| 1-12 | `1.04#4` (7,3 s) | H | T1 | `t24_a1_06_police_patrol_rural_search_06`, `pull` | *Investigative teams endured immense public pressure, with numerous veteran detectives dedicating their entire careers to catching the perpetrator.* | — | ✦ Owl | |
| 1-13 | `1.04#5` (4,4 s) | H | T1 | `t24_a1_07_police_patrol_rural_search_07`, `still` | *The prolonged stalemate left countless officers thoroughly exhausted and demoralized.* | — | ✦ Owl | |
| 1-14 | `1.04#6` (7,0 s) | H | T1 | `t24_a1_07_police_patrol_rural_search_07`, `pan` | *Even more tragic, a contaminated physical evidence sample led investigators to firmly believe that the perpetrator had blood type B.* | — | ✦ Owl | |
| 1-15 | `1.04#7` (7,0 s) | H | T1 | `t24_a1_08_police_patrol_rural_search_08`, `push` | *That early technical error became a fatal confirmation bias, blinding the entire investigative apparatus for decades to come.* | — | ✦ Owl | |
| 1-16 | `1.05#1` (9,6 s) | C | T1 | `t24_a1_08_police_patrol_rural_search_08`, `pull` | *From a cognitive psychology perspective, the thirty-three-year stalemate of the Hwaseong case originated from a classic psychological phenomenon known as "Cognitive Tunneling.* | — | ✦ Fox | |
| 1-17 | `1.05#2` (11,1 s) | C | T1 | `t24_a1_09_police_patrol_rural_search_09`, `still` | *When an initial, primitive forensic analysis prematurely concluded that the perpetrator possessed blood type B, the entire investigative force unwittingly fell into the trap of "Confirmation Bias.* | — | ✦ Fox | |
| 1-18 | `1.05#3` (7,6 s) | C | T1 | `t24_a1_09_police_patrol_rural_search_09`, `pan` | *They systematically dismissed every suspicious individual with a different blood type, creating a fatal blind spot in their investigative logic.* | — | ✦ Fox | |
| 1-19 | `1.05#4` (10,6 s) | C | T1 | `t24_a1_10_rain_drenched_crossroad_10`, `push` | *This unverified dogma inadvertently granted an absolute shield of immunity to the real predator with blood type O, allowing him to pass through police checkpoints with total impunity.* | — | ✦ Fox | |
| 1-20 | `1.06#1` (7,6 s) | H | T1 | `t24_a1_10_rain_drenched_crossroad_10`, `pull` | *To alleviate the unbearable dread of an invisible threat, the local community of Hwaseong manifested the myth of the red dress on rainy nights.* | — | ✦ Owl | |
| 1-21 | `1.06#2` (13,1 s) | H | T1 | `t24_a1_11_shadowy_window_heavy_curtains_11`, `still` | *In behavioral science, this represents an unconscious coping mechanism: when confronted with arbitrary and incomprehensible evil, the human mind desperately grasps at identifiable patterns to sustain the illusion of control.* | — | ✦ Owl | |
| 1-22 | `1.06#3` (9,0 s) | H | T1 | `t24_a1_12_police_patrol_rural_search_12`, `pan` | *Yet, the tragic cost of that collective delusion was the total disintegration of communal trust, transforming every neighborly glance into an unbearable gaze of suspicion.* | — | ✦ Owl | |
| 1-23 | `1.06#4` (8,0 s) | H | T1 | `t24_a1_12_police_patrol_rural_search_12`, `push` | *Yet despite every human effort, the killer seemed consistently one step ahead of law enforcement, vanishing without a trace into the dense fog.* | — | ✦ Owl | |
| 1-24 | `1.06#5` (9,7 s) | H | T1 | `t24_a1_13_rural_village_lane_fog_13`, `pull` | *In 2006, the 15-year statute of limitations under Korean law officially expired for the Hwaseong cases, leaving behind an open wound devoid of answers.* | — | ✦ Owl | |
| 1-25 | `1.08#1` (8,7 s) | H | T1 | `t24_a1_13_rural_village_lane_fog_13`, `still` | *For over three decades, the Hwaseong case stood as the most agonizing failure of the judiciary and an indelible stain on South Korea's collective conscience.* | — | ✦ Owl | |
| 1-26 | `1.08#2` (5,7 s) | H | T1 | `t24_a1_14_rural_village_lane_fog_14`, `pan` | *The families of the victims endured daily torment, never knowing who had stolen the lives of their cherished loved ones.* | — | ✦ Owl | |
| 1-27 | `1.08#3` (7,2 s) | H | T1 | `t24_a1_14_rural_village_lane_fog_14`, `push` | *Local villagers lived in perpetual mutual suspicion, wondering whether the ruthless serial predator walked freely among their neighbors.* | — | ✦ Owl | |
| 1-28 | `1.08#4` (6,1 s) | H | T1 | `t24_a1_15_dark_detention_interrogation_room_15`, `pull` | *A state of collective paranoia gripped every village, turning familiar neighbors into objects of lingering suspicion.* | — | ✦ Owl | |
| 1-29 | `1.08#5` (7,6 s) | H | T1 | `t24_a1_15_dark_detention_interrogation_room_15`, `still` | *Society's fundamental sense of public safety was shattered, leaving a deep psychological scar across generations of South Korean citizens.* | — | ✦ Owl | |
| 1-30 | `1.08#6` (7,0 s) | H | T1 | `t24_a1_16_police_patrol_rural_search_16`, `pan` | *The impotence of justice appeared permanently buried beneath the dust of time and the aging of the original investigative generation.* | — | ✦ Owl | |
| 1-31 | `1.08#7` (5,0 s) | H | T1 | `t24_a1_16_police_patrol_rural_search_16`, `push` | *Yet true guardians of the law never allowed themselves the luxury of abandoning the pursuit of the truth.* | — | ✦ Owl | |
| 1-32 | `1.09#1` (5,2 s) | N | T1 | `t24_a1_17_desolate_rice_paddies_mist_17`, `pull` | *Picture the vivid memories of a young woman living in Hwaseong during the late 1980s.* | — | — | |
| 1-33 | `1.09#2` (6,8 s) | N | T1 | `t24_a1_17_desolate_rice_paddies_mist_17`, `still` | *Every time we heard the wail of police sirens or sudden shouting in the rice fields, our hearts sank knowing another neighbor had fallen.* | — | — | |
| 1-34 | `1.09#3` (4,2 s) | N | T1 | `t24_a1_18_rain_drenched_crossroad_18`, `pan` | *Parents strictly forbade daughters and sisters from stepping outside once night fell.* | — | — | |
| 1-35 | `1.09#4` (5,5 s) | N | T1 | `t24_a1_18_rain_drenched_crossroad_18`, `push` | *Rumors circulated that the predator specifically targeted women wearing red clothes on rainy nights.* | — | — | |
| 1-36 | `1.09#5` (8,4 s) | N | T1 | `t24_a1_19_rural_village_lane_fog_19`, `pull` | *An unbearable atmosphere of suspicion hung over everything, as men in the village eyed one another warily, terrified that a familiar neighbor might be the monster.* | — | — | |
| 1-37 | `1.09#6` (8,2 s) | N | T1 | `t24_a1_19_rural_village_lane_fog_19`, `still` | *Even the sudden barking of a dog along the ridge or a shadow crossing under the moonlight was enough to make entire households tremble behind barred doors.* | — | — | |
| 1-38 | `1.09#7` (7,8 s) | N | T1 | `t24_a1_20_rural_village_lane_fog_20`, `pan` | *For 33 long years, we lived with bitter sorrow, dreading that the perpetrator would carry his dark secrets to the grave without punishment.* | — | — | |
| 1-39 | `1.09#8` (6,9 s) | N | T1 | `t24_a1_20_rural_village_lane_fog_20`, `push` | *Yet deep within our souls, we held onto the fragile hope that heaven was watching and the truth would eventually step into the light.* | — | — | |
| 1-40 | `1.11#1` (5,1 s) | H | T1 | `t24_a1_21_police_patrol_rural_search_21`, `pull` | *That fragile hope was finally answered through the extraordinary advancements of modern forensic science.* | — | ✦ Owl | |
| 1-41 | `1.11#2` (8,4 s) | H | T1 | `t24_a1_21_police_patrol_rural_search_21`, `still` | *In 2019, the Gyeonggi Nambu Provincial Police Agency submitted preserved cold case evidence from three decades earlier to the National Forensic Service.* | — | ✦ Owl | |
| 1-42 | `1.11#3` (10,1 s) | H | T1 | `t24_a1_22_forensic_dna_laboratory_22`, `pan` | *Utilizing modern DNA extraction methodologies, forensic scientists successfully recovered viable genetic profiles from evidence preserved in the fifth, seventh, and ninth cases.* | — | ✦ Owl | |
| 1-43 | `1.11#4` (8,4 s) | H | T1 | `t24_a1_22_forensic_dna_laboratory_22`, `push` | *Forensic examiners meticulously reconstructed ultra-trace DNA molecules that had rested undisturbed for over 30 years inside evidence storage.* | — | ✦ Owl | |
| 1-44 | `1.11#5` (4,6 s) | H | T1 | `t24_a1_23_rural_village_lane_fog_23`, `pull` | *Modern science finally awakened the silent witnesses that time seemed to have erased forever.* | — | ✦ Owl | |
| 1-45 | `1.11#6` (7,4 s) | H | T1 | `t24_a1_24_forensic_dna_laboratory_24`, `still` | *This newly extracted DNA was immediately matched against the national criminal offender database, yielding an undeniable positive match.* | — | ✦ Owl | |
| 1-46 | `1.11#7` (7,3 s) | H | T1 | `t24_a1_25_busan_prison_steel_corridor_25`, `pan` | *The serial killer was no elusive ghost, but an inmate currently serving a life sentence at Busan Prison named Lee Choon-jae.* | — | ✦ Owl | |
| 1-47 | `1.11#8` (7,6 s) | H | T1 | `t24_a1_26_rural_village_lane_fog_26`, `push` | *A high-stakes psychological confrontation commenced within prison walls, abruptly ending 33 years of concealment beneath the shadows.* | — | ✦ Owl | |
| 1-48 | `1.12#1` (7,0 s) | D | T1 | `t24_a1_27_police_patrol_rural_search_27`, `pull` | *Imagine the overwhelming sensation of an investigator when the DNA results pointed unequivocally to Lee Choon-jae.* | — | ✦ Wolf | |
| 1-49 | `1.12#2` (8,1 s) | D | T1 | `t24_a1_28_rural_village_lane_fog_28`, `still` | *He was 56 years old, sentenced to life imprisonment in 1994 for the murder of his sister-in-law in the city of Cheongju.* | — | ✦ Wolf | |
| 1-50 | `1.12#3` (8,7 s) | D | T1 | `t24_a1_29_busan_prison_steel_corridor_29`, `pan` | *Throughout his 25 years of incarceration at Busan Prison, Lee Choon-jae was officially classified as a quiet, model first-class inmate.* | — | ✦ Wolf | |
| 1-51 | `1.12#4` (8,9 s) | D | T1 | `t24_a1_30_prison_cell_embroidery_desk_30`, `push` | *He had never violated a single prison rule, spent his time peacefully practicing embroidery, and was even under review for potential parole consideration.* | — | ✦ Wolf | |
| 1-52 | `1.12#5` (7,2 s) | D | T1 | `t24_a1_31_busan_prison_steel_corridor_31`, `pull` | *It was a facade of domestic compliance so flawless that prison guards never suspected his unfathomable criminal history.* | — | ✦ Wolf | |
| 1-53 | `1.12#6` (10,6 s) | D | T1 | `t24_a1_32_rural_village_lane_fog_32`, `still` | *However, the most daunting legal hurdle at that moment was that the statute of limitations for all Hwaseong murders had expired in 2006, meaning he could not be newly indicted.* | — | ✦ Wolf | |
| 1-54 | `1.12#7` (6,8 s) | D | T1 | `t24_a1_33_busan_prison_steel_corridor_33`, `pan` | *Our sole purpose in entering Busan Prison was to uncover the unvarnished truth for the victims and their grieving families.* | — | ✦ Wolf | |
| 1-55 | `1.13#1` (5,6 s) | H | T1 | `t24_a1_34_police_patrol_rural_search_34`, `push` | *A specialized task force of veteran detectives and criminal profilers immediately departed for Busan.* | — | ✦ Owl | |
| 1-56 | `1.13#2` (6,5 s) | H | T1 | `t24_a1_35_claustrophobic_interrogation_room_35`, `pull` | *Yet what they were about to encounter inside the interrogation room was neither stubborn denial nor tearful late repentance.* | — | ✦ Owl | |
| 1-57 | `1.13#3` (6,4 s) | H | T1 | `t24_a1_36_rural_village_lane_fog_36`, `still` | *It was an unsettlingly calm and proud demeanor from a serial predator who took covert pride in his monstrous accomplishments.* | — | ✦ Owl | |
| 1-58 | `1.13#4` (6,2 s) | H | T1 | `t24_a1_37_claustrophobic_interrogation_room_37`, `pan` | *A psychological duel began to strip away the mask of humanity and expose the predator hiding in the fog for three decades.* | — | ✦ Owl | |

### ACT 2: THE PSYCHOLOGICAL DUEL AT BUSAN PRISON & THE CHILLING CONFESSION

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (8,0 s) | H | T1 | `t24_a2_01_police_patrol_rural_search_01`, `push` | *During the initial days of questioning at Busan Prison, Lee Choon-jae maintained his gentle demeanor, firmly denying any connection to the Hwaseong killings.* | — | ✦ Owl | |
| 2-02 | `2.02#2` (8,1 s) | H | T1 | `t24_a2_01_police_patrol_rural_search_01`, `pull` | *He possessed a keen understanding of legal technicalities, knowing the statute of limitations had passed and believing the police had no leverage against a lifer.* | — | ✦ Owl | |
| 2-03 | `2.02#3` (8,3 s) | H | T1 | `t24_a2_02_prison_visitation_glass_partition_02`, `still` | *He greeted the interrogators politely, smiled softly, and convincingly played the part of an innocent man burdened by bureaucratic nuisance.* | — | ✦ Owl | |
| 2-04 | `2.02#4` (7,1 s) | H | T1 | `t24_a2_02_prison_visitation_glass_partition_02`, `pan` | *That brazen calm served as a formidable psychological bulwark, fortified by 25 years of perfecting his public facade.* | — | ✦ Owl | |
| 2-05 | `2.02#5` (4,8 s) | H | T1 | `t24_a2_03_police_patrol_rural_search_03`, `push` | *To dismantle that defensive wall, law enforcement deployed seasoned criminal profilers.* | — | ✦ Owl | |
| 2-06 | `2.04#1` (6,7 s) | H | T1 | `t24_a2_03_police_patrol_rural_search_03`, `pull` | *The criminal profiling team spent numerous sessions simply establishing rapport and conversational trust with Lee Choon-jae.* | — | ✦ Owl | |
| 2-07 | `2.04#2` (7,3 s) | H | T1 | `t24_a2_04_prison_visitation_glass_partition_04`, `still` | *They refrained from aggressive accusations, choosing instead to listen patiently to the inner musings of a man isolated for a quarter of a century.* | — | ✦ Owl | |
| 2-08 | `2.04#3` (8,2 s) | H | T1 | `t24_a2_04_prison_visitation_glass_partition_04`, `pan` | *According to behavioral profilers, this empathetic listening directly targeted the killer's primary vulnerability: his desperate desire for recognition.* | — | ✦ Owl | |
| 2-09 | `2.04#4` (7,2 s) | H | T1 | `t24_a2_05_claustrophobic_interrogation_room_05`, `push` | *The psychologists skillfully converted the interrogation room into an arena where Lee Choon-jae felt his narcissism subtly acknowledged.* | — | ✦ Owl | |
| 2-10 | `2.04#5` (7,1 s) | H | T1 | `t24_a2_05_claustrophobic_interrogation_room_05`, `pull` | *As his model prisoner facade gently loosened, his pathological pride began searching for an opportunity to assert dominance.* | — | ✦ Owl | |
| 2-11 | `2.04#6` (8,2 s) | H | T1 | `t24_a2_06_police_patrol_rural_search_06`, `still` | *When detectives finally presented irrefutable forensic DNA evidence directly before him, the final fortress of Lee Choon-jae's composure fractured.* | — | ✦ Owl | |
| 2-12 | `2.04#7` (2,1 s) | H | T1 | `t24_a2_06_police_patrol_rural_search_06`, `pan` | *At long last, he began to speak.* | — | ✦ Owl | |
| 2-13 | `2.04#8` (4,0 s) | H | T1 | `t24_a2_07_busan_prison_steel_corridor_07`, `push` | *His subsequent disclosure stunned every investigator present in the room.* | — | ✦ Owl | |
| 2-14 | `2.04#9` (6,8 s) | H | T1 | `t24_a2_07_busan_prison_steel_corridor_07`, `pull` | *Why would a man who remained utterly silent behind bars for twenty-five years suddenly confess to a horrific string of cold cases?* | — | ✦ Owl | |
| 2-15 | `2.04#10` (3,6 s) | H | T1 | `t24_a2_08_prison_visitation_glass_partition_08`, `still` | *Was it the late awakening of a dormant conscience at the twilight of his life?* | — | ✦ Owl | |
| 2-16 | `2.04#11` (4,5 s) | H | T1 | `t24_a2_08_prison_visitation_glass_partition_08`, `pan` | *Or did a completely different psychological dynamic lie beneath that chilling composure?* | — | ✦ Owl | |
| 2-17 | `2.05#1` (5,5 s) | C | T1 | `t24_a2_09_prison_visitation_glass_partition_09`, `push` | *Criminal psychology confirms that Lee Choon-jae’s confession was entirely devoid of genuine remorse.* | — | ✦ Fox | |
| 2-18 | `2.05#2` (9,5 s) | C | T1 | `t24_a2_09_prison_visitation_glass_partition_09`, `pull` | *True remorse requires affective empathy—the capacity to resonate with the agony inflicted upon victims—a faculty completely absent in a malignant narcissist.* | — | ✦ Fox | |
| 2-19 | `2.05#3` (8,4 s) | C | T1 | `t24_a2_10_prison_visitation_glass_partition_10`, `still` | *His willingness to speak was triggered by the total collapse of the strategic utility of secrecy once the statute of limitations expired in 2006.* | — | ✦ Fox | |
| 2-20 | `2.05#4` (9,3 s) | C | T1 | `t24_a2_10_prison_visitation_glass_partition_10`, `pan` | *Aware that the legal system could no longer impose additional capital punishment, his defensive fear dissipated, paving the way for "Narcissistic Grandiosity" to emerge.* | — | ✦ Fox | |
| 2-21 | `2.05#5` (9,9 s) | C | T1 | `t24_a2_11_police_patrol_rural_search_11`, `push` | *He perceived the interrogation room as a dark stage where he could fulfill his craving for notoriety, boasting that he had outmaneuvered two million police officers for over three decades.* | — | ✦ Fox | |
| 2-22 | `2.07#1` (6,4 s) | D | T1 | `t24_a2_11_police_patrol_rural_search_11`, `pull` | *From that pivotal moment onward, Lee Choon-jae embarked upon an astonishing and chilling sequence of confessions.* | — | ✦ Wolf | |
| 2-23 | `2.07#2` (9,8 s) | D | T1 | `t24_a2_12_police_patrol_rural_search_12`, `still` | *He not only admitted to all 10 Hwaseong murders under active review, but voluntarily confessed to four additional homicides and dozens of sexual assaults.* | — | ✦ Wolf | |
| 2-24 | `2.07#3` (7,5 s) | D | T1 | `t24_a2_12_police_patrol_rural_search_12`, `pan` | *He even sketched detailed floor plans and environmental maps of various crime scenes from memory after more than 30 years.* | — | ✦ Wolf | |
| 2-25 | `2.07#4` (7,8 s) | D | T1 | `t24_a2_13_police_patrol_rural_search_13`, `push` | *He pinpointed exact bushes, irrigation ditches, and prevailing wind directions from each night without referencing investigative files.* | — | ✦ Wolf | |
| 2-26 | `2.07#5` (8,8 s) | D | T1 | `t24_a2_13_police_patrol_rural_search_13`, `pull` | *That uncanny precision demonstrated that he had mentally replayed those gruesome memories thousands of times like prized psychological trophies.* | — | ✦ Wolf | |
| 2-27 | `2.07#6` (8,0 s) | D | T1 | `t24_a2_14_police_patrol_rural_search_14`, `still` | *According to detectives, he recounted every atrocity in a flat, conversational tone, displaying zero emotional remorse.* | — | ✦ Wolf | |
| 2-28 | `2.07#7` (7,2 s) | D | T1 | `t24_a2_14_police_patrol_rural_search_14`, `pan` | *In those past years, police officers had crossed paths with him multiple times without ever realizing who he was.* | — | ✦ Wolf | |
| 2-29 | `2.09#1` (6,7 s) | H | T1 | `t24_a2_15_police_patrol_rural_search_15`, `push` | *Lee Choon-jae's voluntary confession and smug composure exposed a bitter, ironic failure in the historical investigation.* | — | ✦ Owl | |
| 2-30 | `2.09#2` (8,0 s) | H | T1 | `t24_a2_15_police_patrol_rural_search_15`, `pull` | *During the active killing spree, Lee Choon-jae had actually been stopped and questioned three separate times by local police as a suspicious resident.* | — | ✦ Owl | |
| 2-31 | `2.09#3` (6,9 s) | H | T1 | `t24_a2_16_police_patrol_rural_search_16`, `still` | *Each time, however, he was released, primarily because preliminary forensic tests at the time did not match his biological profile.* | — | ✦ Owl | |
| 2-32 | `2.09#4` (7,2 s) | H | T1 | `t24_a2_16_police_patrol_rural_search_16`, `pan` | *Investigators back then were fixated exclusively on suspects with blood type B, whereas Lee Choon-jae possessed blood type O.* | — | ✦ Owl | |
| 2-33 | `2.09#5` (6,5 s) | H | T1 | `t24_a2_17_forensic_investigation_desk_17`, `push` | *That critical mismatch in blood typing became a virtual license to roam freely, allowing the monster to continue his reign of terror.* | — | ✦ Owl | |
| 2-34 | `2.09#6` (8,1 s) | H | T1 | `t24_a2_17_forensic_investigation_desk_17`, `pull` | *The primitive state of forensic technology and an overreliance on subjective intuition allowed the nation's most dangerous predator to slip through their fingers.* | — | ✦ Owl | |
| 2-35 | `2.09#7` (5,5 s) | H | T1 | `t24_a2_18_police_patrol_rural_search_18`, `still` | *The devastating cost of those systemic shortcomings was the needless loss of additional innocent human lives.* | — | ✦ Owl | |
| 2-36 | `2.10#1` (8,4 s) | D | T1 | `t24_a2_18_police_patrol_rural_search_18`, `pan` | *Consider the perplexing question every detective faced: why confess openly when the legal system can no longer impose additional penalties?* | — | ✦ Wolf | |
| 2-37 | `2.10#2` (8,2 s) | D | T1 | `t24_a2_19_forensic_dna_laboratory_19`, `push` | *According to public records, Lee Choon-jae remarked that once DNA evidence surfaced, maintaining deception was entirely pointless.* | — | ✦ Wolf | |
| 2-38 | `2.10#3` (7,0 s) | D | T1 | `t24_a2_20_police_patrol_rural_search_20`, `pull` | *He even looked back at the investigators with an arrogant smirk, asking: “I thought you guys would have caught me a long time ago.”* | — | ✦ Wolf | |
| 2-39 | `2.10#4` (7,2 s) | D | T1 | `t24_a2_21_prison_visitation_glass_partition_21`, `still` | *Certain profilers noted that an overpowering craving for historical notoriety compelled him to unveil his dark secrets.* | — | ✦ Wolf | |
| 2-40 | `2.10#5` (7,4 s) | D | T1 | `t24_a2_22_police_patrol_rural_search_22`, `pan` | *Yet his comprehensive confession also exposed another grievous institutional injustice that had festered for three decades.* | — | ✦ Wolf | |
| 2-41 | `2.11#1` (9,2 s) | H | T1 | `t24_a2_23_dark_detention_interrogation_room_23`, `push` | *Among the 10 Hwaseong cases, the eighth murder in 1988 had been officially declared solved by authorities following the arrest of a young man named Yoon Sung-yeo.* | — | ✦ Owl | |
| 2-42 | `2.11#2` (7,6 s) | H | T1 | `t24_a2_24_dark_detention_interrogation_room_24`, `pull` | *That physically disabled man was subjected to severe coercion and served 20 grueling years in prison for a heinous crime he never committed.* | — | ✦ Owl | |
| 2-43 | `2.11#3` (10,7 s) | H | T1 | `t24_a2_25_police_patrol_rural_search_25`, `still` | *Driven by intense public pressure, police utilized physical torture, starvation, and sleep deprivation to extract a false confession from an impoverished young man unable to defend himself.* | — | ✦ Owl | |
| 2-44 | `2.11#4` (5,6 s) | H | T1 | `t24_a2_26_prison_visitation_glass_partition_26`, `pan` | *That catastrophic miscarriage of justice robbed an innocent human being of his youth, honor, and future.* | — | ✦ Owl | |
| 2-45 | `2.11#5` (7,8 s) | H | T1 | `t24_a2_27_dark_detention_interrogation_room_27`, `push` | *Lee Choon-jae's unequivocal admission that he alone perpetrated the eighth murder triggered a nationwide reckoning within the South Korean judicial system.* | — | ✦ Owl | |
| 2-46 | `2.11#6` (5,5 s) | H | T1 | `t24_a2_28_prison_visitation_glass_partition_28`, `pull` | *Historical truth was finally brought to light through the convergence of scientific certainty and moral conscience.* | — | ✦ Owl | |
| 2-47 | `2.11#7` (7,6 s) | H | T1 | `t24_a2_29_shadowy_window_heavy_curtains_29`, `still` | *Criminal psychologists subsequently embarked on dissecting Lee Choon-jae's personality architecture: a classic power-control serial predator.* | — | ✦ Owl | |
| 2-48 | `2.11#8` (6,9 s) | H | T1 | `t24_a2_30_prison_visitation_glass_partition_30`, `pan` | *It was the chilling intersection of private sociopathic malice and the glaring vulnerabilities of an emerging judicial apparatus.* | — | ✦ Owl | |

### ACT 3: PSYCHOLOGICAL DECONSTRUCTION: THE POWER-CONTROL KILLER & THE CONFESSION PARADOX

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (7,6 s) | H | T1 | `t24_a3_01_forensic_investigation_desk_01`, `push` | *The case of Lee Choon-jae provides behavioral science with a textbook paradigm of what criminologists classify as a Power-Control Serial Killer.* | — | ✦ Owl | |
| 3-02 | `3.02#2` (10,0 s) | H | T1 | `t24_a3_01_forensic_investigation_desk_01`, `pull` | *Unlike predators motivated by financial gain or psychiatric hallucinations, this typology derives ultimate psychological gratification through total dominance over their victims.* | — | ✦ Owl | |
| 3-03 | `3.02#3` (5,0 s) | H | T1 | `t24_a3_02_dark_detention_interrogation_room_02`, `still` | *In daily routine interactions, Lee Choon-jae appeared entirely unassuming and mundane.* | — | ✦ Owl | |
| 3-04 | `3.02#4` (8,6 s) | H | T1 | `t24_a3_02_dark_detention_interrogation_room_02`, `pan` | *His cognitive apparatus operated through radical compartmentalization: an obedient relative on one side, and a cold-blooded nocturnal predator on the other.* | — | ✦ Owl | |
| 3-05 | `3.02#5` (6,7 s) | H | T1 | `t24_a3_03_prison_cell_embroidery_desk_03`, `push` | *Yet beneath that mundane exterior surged a pathological craving for absolute control and deeply repressed sadistic aggression.* | — | ✦ Owl | |
| 3-06 | `3.03#1` (9,6 s) | C | T1 | `t24_a3_03_prison_cell_embroidery_desk_03`, `pull` | *Under the classification framework developed by Holmes and DeBurger, power-control serial killers perceive the unilateral power of life and death as the ultimate psychological high.* | — | ✦ Fox | |
| 3-07 | `3.03#2` (8,3 s) | C | T1 | `t24_a3_04_behavioral_science_study_desk_04`, `still` | *This theoretical model posits that such offenders frequently experience pervasive feelings of personal inadequacy and social impotence in ordinary life.* | — | ✦ Fox | |
| 3-08 | `3.03#3` (7,5 s) | C | T1 | `t24_a3_04_behavioral_science_study_desk_04`, `pan` | *To compensate for real-world emasculation, the predator seeks omnipotent authority by preying exclusively upon vulnerable targets.* | — | ✦ Fox | |
| 3-09 | `3.03#4` (5,6 s) | C | T1 | `t24_a3_05_behavioral_science_study_desk_05`, `push` | *This explanatory framework precisely illuminates the behavioral pathology exhibited by Lee Choon-jae.* | — | ✦ Fox | |
| 3-10 | `3.03#5` (6,2 s) | C | T1 | `t24_a3_05_behavioral_science_study_desk_05`, `pull` | *Behaviorally, one must maintain a strict demarcation between Modus Operandi and Psychological Signature.* | — | ✦ Fox | |
| 3-11 | `3.03#6` (13,4 s) | C | T1 | `t24_a3_06_behavioral_science_study_desk_06`, `still` | *His Modus Operandi involved selecting desolate field paths, operating under cover of darkness, and discarding forensic traces to evade capture; his Signature, however, was binding victims using their own personal apparel.* | — | ✦ Fox | |
| 3-12 | `3.03#7` (9,8 s) | C | T1 | `t24_a3_06_behavioral_science_study_desk_06`, `pan` | *Those ritualistic knots served no practical escape utility; rather, they represented a pathological psychological imprint asserting supreme subjugation over the victim.* | — | ✦ Fox | |
| 3-13 | `3.03#8` (8,6 s) | C | T1 | `t24_a3_07_behavioral_science_study_desk_07`, `push` | *The obsessive repetition across 14 murders was not a matter of biological compulsion, but an insidious psychological addiction to absolute dominance.* | — | ✦ Fox | |
| 3-14 | `3.03#9` (7,1 s) | C | T1 | `t24_a3_07_behavioral_science_study_desk_07`, `pull` | *Such consistent behavioral patterns exemplify the clinical diagnostic criteria of severe antisocial personality disorder.* | — | ✦ Fox | |
| 3-15 | `3.04#1` (8,2 s) | H | T1 | `t24_a3_08_police_patrol_rural_search_08`, `still` | *Yet what stunned psychological profilers most was not merely his past deeds, but his chilling detachment when recounting them after 33 years.* | — | ✦ Owl | |
| 3-16 | `3.04#2` (5,3 s) | H | T1 | `t24_a3_08_police_patrol_rural_search_08`, `pan` | *Far from exhibiting fear or remorse, he described his atrocities with casual nonchalance.* | — | ✦ Owl | |
| 3-17 | `3.04#3` (8,1 s) | H | T1 | `t24_a3_09_behavioral_science_study_desk_09`, `push` | *He utilized moral disengagement techniques, rationalizing the taking of human lives as though it were an uncontrollable, natural routine.* | — | ✦ Owl | |
| 3-18 | `3.04#4` (6,6 s) | H | T1 | `t24_a3_09_behavioral_science_study_desk_09`, `pull` | *This psychological paradox is decoded by behavioral experts through the lens of post-statute-of-limitations grandiosity.* | — | ✦ Owl | |
| 3-19 | `3.05#1` (9,6 s) | C | T1 | `t24_a3_10_shadowy_window_heavy_curtains_10`, `still` | *When a power-control predator realizes that the judicial system possesses no statutory mechanism to impose further legal retribution, their defensive fear evaporates.* | — | ✦ Fox | |
| 3-20 | `3.05#2` (5,0 s) | C | T1 | `t24_a3_10_shadowy_window_heavy_curtains_10`, `pan` | *In its place, an unbridled narcissistic hunger for dark recognition surges to the forefront.* | — | ✦ Fox | |
| 3-21 | `3.05#3` (4,7 s) | C | T1 | `t24_a3_11_police_patrol_rural_search_11`, `push` | *For 33 years, Lee Choon-jae guarded these secrets in complete silence.* | — | ✦ Fox | |
| 3-22 | `3.05#4` (7,6 s) | C | T1 | `t24_a3_11_police_patrol_rural_search_11`, `pull` | *The arrival of police armed with incontrovertible DNA evidence provided him the long-awaited stage to step into historical notoriety.* | — | ✦ Fox | |
| 3-23 | `3.05#5` (6,0 s) | C | T1 | `t24_a3_12_shadowy_window_heavy_curtains_12`, `still` | *Lee Choon-jae's criminal trajectory adhered to a classic fantasy addiction and behavioral escalation cycle.* | — | ✦ Fox | |
| 3-24 | `3.05#6` (10,4 s) | C | T1 | `t24_a3_12_shadowy_window_heavy_curtains_12`, `pan` | *It began with voyeurism, stalking, and minor boundary intrusions; yet as tolerance built, he experienced fantasy starvation, escalating inexorably into lethal violence.* | — | ✦ Fox | |
| 3-25 | `3.05#7` (4,9 s) | C | T1 | `t24_a3_13_crime_scene_confession_sketch_13`, `push` | *Scholars widely agree that his confessions stemmed in no way from genuine moral conscience.* | — | ✦ Fox | |
| 3-26 | `3.05#8` (6,8 s) | C | T1 | `t24_a3_13_crime_scene_confession_sketch_13`, `pull` | *The meticulous sketches he rendered represented an explicit psychological revival of the omnipotent control he once savored.* | — | ✦ Fox | |
| 3-27 | `3.05#9` (4,0 s) | C | T1 | `t24_a3_14_behavioral_science_study_desk_14`, `still` | *This behavior manifests the defining hallmarks of malignant narcissism.* | — | ✦ Fox | |
| 3-28 | `3.06#1` (5,2 s) | H | T1 | `t24_a3_14_behavioral_science_study_desk_14`, `pan` | *Lee Choon-jae's cold grandiosity unmasked the ruthless essence of a predatory sociopath.* | — | ✦ Owl | |
| 3-29 | `3.06#2` (7,8 s) | H | T1 | `t24_a3_15_dark_detention_interrogation_room_15`, `push` | *Yet ironically, that very arrogance handed the master key of legal redemption to an innocent man who had endured decades of unfathomable injustice.* | — | ✦ Owl | |
| 3-30 | `3.06#3` (6,9 s) | H | T1 | `t24_a3_15_dark_detention_interrogation_room_15`, `pull` | *The predator's illusion of absolute supremacy was ultimately dismantled by the enduring resilience of truth and human dignity.* | — | ✦ Owl | |
| 3-31 | `3.07#1` (7,5 s) | C | T1 | `t24_a3_16_crime_scene_confession_sketch_16`, `still` | *The case of Yoon Sung-yeo, wrongfully convicted for the eighth murder, represents an agonizing case study in Coerced Confession.* | — | ✦ Fox | |
| 3-32 | `3.07#2` (13,0 s) | C | T1 | `t24_a3_16_crime_scene_confession_sketch_16`, `pan` | *According to Yoon's testimony and official findings, he was subjected to brutal sleep deprivation, severe physical abuse, and relentless coercion in 1989, forcing his signature onto a falsified confession.* | — | ✦ Fox | |
| 3-33 | `3.07#3` (8,4 s) | C | T1 | `t24_a3_17_dark_detention_interrogation_room_17`, `push` | *When human psychology is pushed to extreme physiological breaking points, an individual will readily admit to false charges merely to terminate immediate torment.* | — | ✦ Fox | |
| 3-34 | `3.07#4` (8,0 s) | C | T1 | `t24_a3_17_dark_detention_interrogation_room_17`, `pull` | *Under prolonged torture and complete sensory isolation, an individual's cognitive defense mechanisms collapse into profound learned helplessness.* | — | ✦ Fox | |
| 3-35 | `3.07#5` (9,2 s) | C | T1 | `t24_a3_18_dark_detention_interrogation_room_18`, `still` | *When physical anguish eclipses the threshold of psychological endurance, short-term survival instincts compel surrender, even at the cost of lifelong honor.* | — | ✦ Fox | |
| 3-36 | `3.07#6` (8,1 s) | C | T1 | `t24_a3_18_dark_detention_interrogation_room_18`, `pan` | *To understand why an innocent young man like Yoon Sung-yeo signed a false murder confession, we must confront the absolute limits of human physiology.* | — | ✦ Fox | |
| 3-37 | `3.07#7` (8,5 s) | C | T1 | `t24_a3_19_dark_detention_interrogation_room_19`, `push` | *Under relentless physical abuse and seventy-two continuous hours of sleep deprivation, the human brain enters a state of severe "Cognitive Resource Depletion.* | — | ✦ Fox | |
| 3-38 | `3.07#8` (11,9 s) | C | T1 | `t24_a3_20_behavioral_science_study_desk_20`, `pull` | *At that threshold, "Temporal Discounting" dominates all consciousness: the victim loses the capacity to weigh a future twenty-year prison sentence, desperate solely to end the physical agony in the immediate second.* | — | ✦ Fox | |
| 3-39 | `3.07#9` (7,8 s) | C | T1 | `t24_a3_21_shadowy_window_heavy_curtains_21`, `still` | *Signing that false confession was not an act of cowardice, but the inevitable biological collapse of an organism subjected to overwhelming trauma.* | — | ✦ Fox | |
| 3-40 | `3.08#1` (6,5 s) | D | T1 | `t24_a3_22_dark_detention_interrogation_room_22`, `pan` | *Tragically, those who extracted that false confession were not common criminals, but sworn officers of the law.* | — | ✦ Wolf | |
| 3-41 | `3.08#2` (12,5 s) | D | T1 | `t24_a3_23_behavioral_science_study_desk_23`, `push` | *Under crushing institutional pressure to close cases, they compromised their moral compass, turning an impoverished, disabled young man into an expendable scapegoat to quell public outrage.* | — | ✦ Wolf | |
| 3-42 | `3.08#3` (13,6 s) | D | T1 | `t24_a3_24_behavioral_science_study_desk_24`, `pull` | *That gradual ethical decay serves as an enduring warning for criminal justice: whenever justice is subordinated to quota pressure and confirmation bias, the enforcers of law can easily become the authors of catastrophic tragedy.* | — | ✦ Wolf | |
| 3-43 | `3.08#4` (4,6 s) | D | T1 | `t24_a3_25_dark_detention_interrogation_room_25`, `still` | *Lee Choon-jae's confession definitively cleared the path for judicial rehabilitation.* | — | ✦ Wolf | |
| 3-44 | `3.08#5` (7,6 s) | D | T1 | `t24_a3_26_behavioral_science_study_desk_26`, `pan` | *It underscores that forensic science and procedural ethics must walk hand in hand to safeguard fundamental human rights.* | — | ✦ Wolf | |
| 3-45 | `3.08#6` (6,2 s) | D | T1 | `t24_a3_27_suwon_courtroom_judicial_benches_27`, `push` | *And the courtroom at Suwon District Court would soon bear witness to an extraordinary restoration of justice.* | — | ✦ Wolf | |
| 3-46 | `3.09#1` (6,9 s) | H | T1 | `t24_a3_28_forensic_dna_laboratory_28`, `pull` | *Forensic behavioral analyses completed the comprehensive profile of the Hwaseong serial killer and the surrounding systemic tragedies.* | — | ✦ Owl | |
| 3-47 | `3.09#2` (8,5 s) | H | T1 | `t24_a3_29_forensic_investigation_desk_29`, `still` | *Now, the attention of an entire nation turned toward a historic retrial to restore the honor of the innocent and officially close the darkest chapter of the century.* | — | ✦ Owl | |
| 3-48 | `3.09#3` (7,7 s) | H | T1 | `t24_a3_30_behavioral_science_study_desk_30`, `pan` | *It was a courtroom proceeding that could impose no new legal punishment upon the killer, yet offered supreme solace to the moral conscience of a nation.* | — | ✦ Owl | |
| 3-49 | `3.09#4` (6,6 s) | H | T1 | `t24_a3_31_behavioral_science_study_desk_31`, `push` | *A sacred moment wherein objective truth and human dignity finally triumphed over state coercion and historical error.* | — | ✦ Owl | |

### ACT 4: THE CENTURY'S EXONERATION TRIAL & JUSTICE'S FORMAL APOLOGY

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (5,4 s) | H | T1 | `t24_a4_01_dark_detention_interrogation_room_01`, `pull` | *In 2020, a historic retrial commenced at the Suwon District Court in Gyeonggi Province.* | — | ✦ Owl | |
| 4-02 | `4.02#2` (9,0 s) | H | T1 | `t24_a4_01_dark_detention_interrogation_room_01`, `still` | *Sitting at the defense table was not a dangerous felon, but 53-year-old Yoon Sung-yeo, a physically disabled man who had served 20 wrongful years behind bars.* | — | ✦ Owl | |
| 4-03 | `4.02#3` (7,9 s) | H | T1 | `t24_a4_02_busan_prison_steel_corridor_02`, `pan` | *To establish the incontrovertible truth, the court summoned an extraordinary witness: Lee Choon-jae, escorted from prison under armed guard.* | — | ✦ Owl | |
| 4-04 | `4.02#4` (5,3 s) | H | T1 | `t24_a4_02_busan_prison_steel_corridor_02`, `push` | *In November 2020, Lee Choon-jae appeared publicly to testify under oath before the nation.* | — | ✦ Owl | |
| 4-05 | `4.02#5` (5,1 s) | H | T1 | `t24_a4_03_dark_detention_interrogation_room_03`, `pull` | *Facing the bench, he unequivocally testified that he alone was the true perpetrator of the eighth murder.* | — | ✦ Owl | |
| 4-06 | `4.02#6` (8,0 s) | H | T1 | `t24_a4_03_dark_detention_interrogation_room_03`, `still` | *For the first time in over three decades, the actual serial killer and the wrongfully convicted man sat mere meters apart within the same courtroom.* | — | ✦ Owl | |
| 4-07 | `4.02#7` (5,9 s) | H | T1 | `t24_a4_04_dark_detention_interrogation_room_04`, `pan` | *That decisive declaration echoed through breathless silence, shaking the conscience of citizens across South Korea.* | — | ✦ Owl | |
| 4-08 | `4.04#1` (5,7 s) | H | T1 | `t24_a4_04_dark_detention_interrogation_room_04`, `push` | *On December 17, 2020, the court formally declared Yoon Sung-yeo not guilty of all charges.* | — | ✦ Owl | |
| 4-09 | `4.04#2` (6,8 s) | H | T1 | `t24_a4_05_suwon_courtroom_judicial_benches_05`, `pull` | *The presiding judicial panel offered a public, official apology to Yoon for the catastrophic failures of the historical judicial system.* | — | ✦ Owl | |
| 4-10 | `4.04#3` (7,5 s) | H | T1 | `t24_a4_05_suwon_courtroom_judicial_benches_05`, `still` | *After carrying the branding of a heinous murderer for over 30 years, he finally walked out of the courthouse with his head held high as an innocent citizen.* | — | ✦ Owl | |
| 4-11 | `4.04#4` (5,7 s) | H | T1 | `t24_a4_06_dark_detention_interrogation_room_06`, `pan` | *Tears streamed down the weathered cheeks of a man who had dedicated half his life to reclaiming his stolen identity.* | — | ✦ Owl | |
| 4-12 | `4.04#5` (5,1 s) | H | T1 | `t24_a4_06_dark_detention_interrogation_room_06`, `push` | *That landmark ruling closed one of the most agonizing chapters of wrongful conviction in modern history.* | — | ✦ Owl | |
| 4-13 | `4.06#1` (10,3 s) | D | T1 | `t24_a4_07_police_patrol_rural_search_07`, `pull` | *In July 2020, upon releasing the final comprehensive investigation report, Gyeonggi Nambu Police Chief Bae Yong-ju convened a national press conference.* | — | ✦ Wolf | |
| 4-14 | `4.06#2` (4,3 s) | D | T1 | `t24_a4_07_police_patrol_rural_search_07`, `still` | *He bowed deeply before the television cameras in a formal public apology.* | — | ✦ Wolf | |
| 4-15 | `4.06#3` (7,8 s) | D | T1 | `t24_a4_08_police_patrol_rural_search_08`, `pan` | *The apology was extended to the victims and their bereaved families, acknowledging that law enforcement failed to uncover the truth far sooner.* | — | ✦ Wolf | |
| 4-16 | `4.06#4` (9,0 s) | D | T1 | `t24_a4_08_police_patrol_rural_search_08`, `push` | *It was equally directed toward Yoon Sung-yeo and all individuals subjected to coercion and unlawful treatment during past investigative efforts.* | — | ✦ Wolf | |
| 4-17 | `4.06#5` (7,4 s) | D | T1 | `t24_a4_09_police_patrol_rural_search_09`, `pull` | *Before the broadcast cameras of the nation, a subsequent generation of police commanders bowed to atone for historical pain.* | — | ✦ Wolf | |
| 4-18 | `4.06#6` (7,8 s) | D | T1 | `t24_a4_09_police_patrol_rural_search_09`, `still` | *It was a painful yet indispensable reckoning for the police force to confront its history and rebuild shattered public trust.* | — | ✦ Wolf | |
| 4-19 | `4.06#7` (8,2 s) | D | T1 | `t24_a4_10_police_patrol_rural_search_10`, `pan` | *That belated institutional apology proved that while justice may be deferred, historical truth can never be permanently distorted.* | — | ✦ Wolf | |
| 4-20 | `4.07#1` (8,2 s) | H | T1 | `t24_a4_10_police_patrol_rural_search_10`, `push` | *After thirty years of silence and institutional denial, what compelled police leadership to bow in humble repentance before the entire nation in 2020?* | — | ✦ Owl | |
| 4-21 | `4.07#2` (5,8 s) | H | T1 | `t24_a4_11_police_patrol_rural_search_11`, `pull` | *What was the precise psychological mechanism that dismantled the unyielding wall of bureaucratic self-preservation?* | — | ✦ Owl | |
| 4-22 | `4.08#1` (10,3 s) | C | T1 | `t24_a4_11_police_patrol_rural_search_11`, `still` | *The awakening and repentance of the police force in the Hwaseong case was driven by the catastrophic collapse of "Cognitive Self-Deception" under the indisputable weight of modern forensic science.* | — | ✦ Fox | |
| 4-23 | `4.08#2` (6,6 s) | C | T1 | `t24_a4_12_police_patrol_rural_search_12`, `pan` | *For three decades, past investigators could reassure their consciences that they had merely committed minor procedural errors.* | — | ✦ Fox | |
| 4-24 | `4.08#3` (11,9 s) | C | T1 | `t24_a4_12_police_patrol_rural_search_12`, `push` | *However, when Lee Choon-jae's DNA matched conclusively, and when the perpetrator effortlessly drew the exact floor plan of case number eight without case files, every layer of rationalization evaporated.* | — | ✦ Fox | |
| 4-25 | `4.08#4` (10,4 s) | C | T1 | `t24_a4_13_police_patrol_rural_search_13`, `pull` | *Law enforcement was confronted with profound "Moral Injury"—the psychological devastation of recognizing that their own actions had stolen half a lifetime from an innocent disabled man.* | — | ✦ Fox | |
| 4-26 | `4.08#5` (9,8 s) | C | T1 | `t24_a4_14_official_police_press_conference_14`, `still` | *That public bow of apology was far more than legal compliance; it was a desperate psychological necessity to unburden their collective conscience from thirty years of repressed guilt.* | — | ✦ Fox | |
| 4-27 | `4.10#1` (6,4 s) | H | T1 | `t24_a4_14_official_police_press_conference_14`, `pan` | *Lee Choon-jae could receive no new judicial sentence due to the statutory expiration dating back to 2006.* | — | ✦ Owl | |
| 4-28 | `4.10#2` (5,7 s) | H | T1 | `t24_a4_15_suwon_courtroom_judicial_benches_15`, `push` | *Nevertheless, he continues to serve life imprisonment without parole for his separate 1994 conviction.* | — | ✦ Owl | |
| 4-29 | `4.10#3` (7,2 s) | H | T1 | `t24_a4_15_suwon_courtroom_judicial_benches_15`, `pull` | *While judicial statutes may limit legal penalties, the verdict of human conscience and history will permanently brand his name in infamy.* | — | ✦ Owl | |
| 4-30 | `4.10#4` (6,0 s) | H | T1 | `t24_a4_16_hall_of_justice_marble_corridor_16`, `still` | *Consider the personal reflections witnessed by a lifelong advocate of Yoon Sung-yeo throughout this arduous journey.* | — | ✦ Owl | |
| 4-31 | `4.11#1` (4,7 s) | N | T1 | `t24_a4_16_hall_of_justice_marble_corridor_16`, `pan` | *For over 30 years, Yoon's life resembled an endless, suffocating nightmare.* | — | — | |
| 4-32 | `4.11#2` (8,9 s) | N | T1 | `t24_a4_17_hall_of_justice_marble_corridor_17`, `push` | *He was merely an impoverished, disabled young man repairing farm machinery, yet he was scapegoated and coerced into taking the blame for another's crime.* | — | — | |
| 4-33 | `4.11#3` (7,7 s) | N | T1 | `t24_a4_17_hall_of_justice_marble_corridor_17`, `pull` | *He endured 20 years in prison, lost his youth, and upon release continued to suffer under the heavy stigma of public ostracism.* | — | — | |
| 4-34 | `4.11#4` (6,1 s) | N | T1 | `t24_a4_18_hall_of_justice_marble_corridor_18`, `still` | *Yet his unshakeable faith in his own innocence sustained him as he waited for the day the truth would be exposed.* | — | — | |
| 4-35 | `4.11#5` (6,0 s) | N | T1 | `t24_a4_18_hall_of_justice_marble_corridor_18`, `pan` | *The moment the judge declared him innocent, the crushing boulder that had weighed upon half his life was finally lifted.* | — | — | |
| 4-36 | `4.11#6` (5,5 s) | N | T1 | `t24_a4_19_hall_of_justice_marble_corridor_19`, `push` | *No monetary compensation could ever restore the two decades of stolen youth taken from his soul.* | — | — | |
| 4-37 | `4.11#7` (6,1 s) | N | T1 | `t24_a4_19_hall_of_justice_marble_corridor_19`, `pull` | *Yet the paramount victory was that his human dignity and honorable name were completely vindicated.* | — | — | |
| 4-38 | `4.11#8` (6,9 s) | N | T1 | `t24_a4_20_dark_detention_interrogation_room_20`, `still` | *He wishes to impart to anyone enduring adversity: please never surrender your faith in moral righteousness and truth.* | — | — | |
| 4-39 | `4.11#9` (5,1 s) | N | T1 | `t24_a4_20_dark_detention_interrogation_room_20`, `pan` | *May no innocent human being ever again endure the harrowing injustice that was visited upon him.* | — | — | |
| 4-40 | `4.11#10` (9,9 s) | N | T1 | `t24_a4_21_police_patrol_rural_search_21`, `push` | *Standing in that courtroom in 2020, watching the former investigators bow their heads in tears before me, the lingering fire of bitterness in my heart dissolved into profound sorrow.* | — | — | |
| 4-41 | `4.11#11` (7,2 s) | N | T1 | `t24_a4_21_police_patrol_rural_search_21`, `pull` | *I realized that vengeance could never reclaim the twenty years of stolen youth; it would only keep my soul chained within the prison of the past.* | — | — | |
| 4-42 | `4.11#12` (8,1 s) | N | T1 | `t24_a4_22_official_police_press_conference_22`, `still` | *Their belated apology, while powerless to erase the cold beatings of 1989, finally restored my sacred dignity as a human being.* | — | — | |
| 4-43 | `4.11#13` (9,8 s) | N | T1 | `t24_a4_22_official_police_press_conference_22`, `pan` | *I chose forgiveness not because their grave error was trivial, but to liberate myself and to grant those flawed men an opportunity to reclaim their lost humanity.* | — | — | |
| 4-44 | `4.12#1` (6,4 s) | D | T1 | `t24_a4_23_hall_of_justice_marble_corridor_23`, `push` | *The Hwaseong tragedy served as a profound catalyst for sweeping judicial reforms across South Korea.* | — | ✦ Wolf | |
| 4-45 | `4.12#2` (11,2 s) | D | T1 | `t24_a4_24_hall_of_justice_marble_corridor_24`, `pull` | *In 2015, the National Assembly passed the landmark Taewan Act, completely abolishing the statute of limitations for first-degree murder cases carrying capital punishment.* | — | ✦ Wolf | |
| 4-46 | `4.12#3` (8,4 s) | D | T1 | `t24_a4_25_hall_of_justice_marble_corridor_25`, `still` | *This vital legislative reform ensures that perpetrators of such heinous crimes can now be prosecuted regardless of how much time has elapsed.* | — | ✦ Wolf | |
| 4-47 | `4.12#4` (6,6 s) | D | T1 | `t24_a4_26_hall_of_justice_marble_corridor_26`, `pan` | *The legislation stands as a historic milestone, affirming that time will never afford a safe sanctuary for murder.* | — | ✦ Wolf | |
| 4-48 | `4.12#5` (7,5 s) | D | T1 | `t24_a4_27_claustrophobic_interrogation_room_27`, `push` | *Concurrently, mandatory audio and video recording during interrogations has been widely institutionalized to eliminate coercion.* | — | ✦ Wolf | |
| 4-49 | `4.12#6` (6,2 s) | D | T1 | `t24_a4_28_hall_of_justice_marble_corridor_28`, `pull` | *These systemic advancements were purchased through the tears, suffering, and sacrifices of an entire generation.* | — | ✦ Wolf | |
| 4-50 | `4.13#1` (9,4 s) | C | T1 | `t24_a4_29_police_patrol_rural_search_29`, `still` | *The paramount lesson of the Lee Choon-jae case is a stern warning against investigations steered by subjective bias and blind overconfidence in speculative hypotheses.* | — | ✦ Fox | |
| 4-51 | `4.13#2` (8,9 s) | C | T1 | `t24_a4_30_forensic_dna_laboratory_30`, `pan` | *Modern forensic science, particularly advanced DNA technology and rigorous behavioral profiling, serves as an indispensable bulwark for objective reality.* | — | ✦ Fox | |
| 4-52 | `4.13#3` (8,4 s) | C | T1 | `t24_a4_31_hall_of_justice_marble_corridor_31`, `push` | *A progressive judicial system must remain fundamentally skeptical of subjective assumptions while maintaining supreme reverence for independent physical evidence.* | — | ✦ Fox | |
| 4-53 | `4.13#4` (9,5 s) | C | T1 | `t24_a4_32_hall_of_justice_marble_corridor_32`, `pull` | *The seamless integration of professional ethics and precise scientific methodology constitutes our strongest foundation for deterring crime and protecting innocent human lives.* | — | ✦ Fox | |
| 4-54 | `4.14#1` (3,9 s) | H | T1 | `t24_a4_33_hall_of_justice_marble_corridor_33`, `still` | *Thirty-three years shrouded in dense fog have officially drawn to a close.* | — | ✦ Owl | |
| 4-55 | `4.14#2` (7,6 s) | H | T1 | `t24_a4_34_hall_of_justice_marble_corridor_34`, `pan` | *The sacred names and enduring dignity of the innocent women lost decades ago have finally been restored to the reverence they rightfully deserve.* | — | ✦ Owl | |
| 4-56 | `4.14#3` (5,9 s) | H | T1 | `t24_a4_35_hall_of_justice_marble_corridor_35`, `push` | *Yet the lessons of community safety and vigilance against concealed predators remain an enduring, invaluable legacy.* | — | ✦ Owl | |

### ACT 5: REFLECTIONS & 4 CRITICAL SURVIVAL RED FLAGS AGAINST NOCTURNAL PREDATORS

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (6,9 s) | H | T1 | `t24_a5_01_modern_hwaseong_smart_security_dawn_01`, `pull` | *Today, the rural landscape of old Hwaseong has evolved into a thriving, modern metropolis in Gyeonggi Province.* | — | ✦ Owl | |
| 5-02 | `5.02#2` (4,4 s) | H | T1 | `t24_a5_01_modern_hwaseong_smart_security_dawn_01`, `still` | *Yet the memory of those lost women remains etched indelibly in the hearts of the community.* | — | ✦ Owl | |
| 5-03 | `5.02#3` (7,4 s) | H | T1 | `t24_a5_02_modern_hwaseong_smart_security_dawn_02`, `pan` | *The sorrow of the past stands as an enduring reminder of the necessity of illumination and infrastructure along isolated paths.* | — | ✦ Owl | |
| 5-04 | `5.02#4` (8,0 s) | H | T1 | `t24_a5_02_modern_hwaseong_smart_security_dawn_02`, `push` | *The rural dirt roads once blanketed in pitch darkness are now brightly illuminated by comprehensive municipal streetlights and surveillance networks.* | — | ✦ Owl | |
| 5-05 | `5.02#5` (7,2 s) | H | T1 | `t24_a5_03_police_patrol_rural_search_03`, `pull` | *Remembering this tragic case is not meant to cultivate fear, but to serve as a beacon guiding vigilant awareness and community solidarity.* | — | ✦ Owl | |
| 5-06 | `5.03#1` (9,4 s) | D | T1 | `t24_a5_03_police_patrol_rural_search_03`, `still` | *From a law enforcement perspective, the most profound lesson is that police must maintain relentless accountability and never succumb to complacency.* | — | ✦ Wolf | |
| 5-07 | `5.03#2` (8,7 s) | D | T1 | `t24_a5_04_forensic_dna_laboratory_04`, `pan` | *The continuous evolution of forensic identification technologies represents our ultimate weapon in reopening and solving historical cold cases.* | — | ✦ Wolf | |
| 5-08 | `5.03#3` (9,2 s) | D | T1 | `t24_a5_04_forensic_dna_laboratory_04`, `push` | *Every physical evidence sample, no matter how minute, must be preserved with meticulous care, for future science may decode what remains unsolvable today.* | — | ✦ Wolf | |
| 5-09 | `5.03#4` (7,3 s) | D | T1 | `t24_a5_05_forensic_investigation_desk_05`, `pull` | *Unresolved homicide files must remain under continuous review to ensure that every crime is held accountable before the law.* | — | ✦ Wolf | |
| 5-10 | `5.04#1` (8,4 s) | C | T1 | `t24_a5_05_forensic_investigation_desk_05`, `still` | *Nocturnal predatory offenders routinely exploit geographic isolation, darkness, and lapses in situational awareness to perpetrate violence.* | — | ✦ Fox | |
| 5-11 | `5.04#2` (6,5 s) | C | T1 | `t24_a5_06_dark_isolated_sidewalk_night_06`, `pan` | *They typically conduct preliminary reconnaissance, surveilling behavioral routines to strike when their target is most isolated.* | — | ✦ Fox | |
| 5-12 | `5.04#3` (9,2 s) | C | T1 | `t24_a5_06_dark_isolated_sidewalk_night_06`, `push` | *Behavioral psychology affirms that innate human intuition and unease represent an invaluable evolutionary gift, signaling peril before logical reasoning engages.* | — | ✦ Fox | |
| 5-13 | `5.04#4` (8,6 s) | C | T1 | `t24_a5_07_modern_hwaseong_smart_security_dawn_07`, `pull` | *Elevating personal situational awareness, varying travel routes, and avoiding walking alone through unlit spaces remain fundamental survival tenets.* | — | ✦ Fox | |
| 5-14 | `5.04#5` (6,8 s) | C | T1 | `t24_a5_07_modern_hwaseong_smart_security_dawn_07`, `still` | *Vigilant familial support and cohesive neighborhood networks serve as our strongest fortress in deterring predatory intrusion.* | — | ✦ Fox | |
| 5-15 | `5.04#6` (9,5 s) | C | T1 | `t24_a5_08_forensic_investigation_desk_08`, `pan` | *The closure of the Lee Choon-jae case marks not merely a triumph of forensic DNA technology, but the moral ascension of a society courageous enough to confront its own past.* | — | ✦ Fox | |
| 5-16 | `5.04#7` (8,3 s) | C | T1 | `t24_a5_08_forensic_investigation_desk_08`, `push` | *A truly civilized society is not one immune to failure, but one that dares to look directly into its historical wounds in order to reform and heal.* | — | ✦ Fox | |
| 5-17 | `5.04#8` (15,8 s) | C | T1 | `t24_a5_09_dark_detention_interrogation_room_09`, `pull` | *The hard-won freedom and vindicated honor of Yoon Sung-yeo stand as a sacred testament: the ultimate benchmark of justice lies not in the severity of punishment inflicted upon the guilty, but in the unyielding protection of the dignity of the most vulnerable before the shadows of authority.* | — | ✦ Fox | |
| 5-18 | `5.05#1` (11,5 s) | H | T1 | `t24_a5_10_rain_drenched_crossroad_10`, `still` | *To empower our audience, particularly women and young commuters, in safeguarding personal safety during nighttime transit, Amber Eyes presents four classic survival red flags distilled from the Lee Choon-jae case.* | — | ✦ Owl | |
| 5-19 | `5.05#2` (7,7 s) | H | T1 | `t24_a5_10_rain_drenched_crossroad_10`, `pan` | *Red Flag Number 1: The habit of solitary transit along fixed, unvarying routes through desolate, poorly illuminated terrain.* | — | ✦ Owl | |
| 5-20 | `5.05#3` (5,2 s) | H | T1 | `t24_a5_11_modern_hwaseong_smart_security_dawn_11`, `push` | *Predators patiently monitor daily routines to identify predictable moments and vulnerabilities.* | — | ✦ Owl | |
| 5-21 | `5.05#4` (8,4 s) | H | T1 | `t24_a5_11_modern_hwaseong_smart_security_dawn_11`, `pull` | *Proactively vary your transit routes, bypass dimly lit shortcuts, and consistently communicate your expected arrival time with family when traveling late.* | — | ✦ Owl | |
| 5-22 | `5.05#5` (5,9 s) | H | T1 | `t24_a5_12_night_street_creeping_silhouette_12`, `still` | *Red Flag Number 2: Intuitive awareness of an individual trailing behind or appearing repeatedly along your commute.* | — | ✦ Owl | |
| 5-23 | `5.05#6` (8,3 s) | H | T1 | `t24_a5_12_night_street_creeping_silhouette_12`, `pan` | *If you notice a pedestrian matching your pace, or a vehicle slowing down abnormally alongside you, never dismiss the suspicion or pretend not to notice.* | — | ✦ Owl | |
| 5-24 | `5.05#7` (8,4 s) | H | T1 | `t24_a5_13_police_patrol_rural_search_13`, `push` | *Immediately move toward well-lit commercial establishments, convenience stores, or populated areas, and contact loved ones or authorities without hesitation.* | — | ✦ Owl | |
| 5-25 | `5.05#8` (7,8 s) | H | T1 | `t24_a5_13_police_patrol_rural_search_13`, `pull` | *Red Flag Number 3: Compromised situational awareness caused by earphone immersion or mobile phone distraction while walking alone at night.* | — | ✦ Owl | |
| 5-26 | `5.05#9` (8,1 s) | H | T1 | `t24_a5_14_empty_subway_underpass_14`, `still` | *Listening to loud audio or remaining fixated on a mobile screen entirely eliminates your natural sensory perception and reaction time against imminent threats.* | — | ✦ Owl | |
| 5-27 | `5.05#10` (7,2 s) | H | T1 | `t24_a5_14_empty_subway_underpass_14`, `pan` | *Keep your eyes scanning your perimeter, keep your ears attentive, and remain in a state of prepared alertness for unexpected circumstances.* | — | ✦ Owl | |
| 5-28 | `5.05#11` (8,1 s) | H | T1 | `t24_a5_15_shadowy_window_heavy_curtains_15`, `push` | *Red Flag Number 4: Unsettling domestic habits and concealed aggressive behaviors exhibited by acquaintances within your immediate social sphere.* | — | ✦ Owl | |
| 5-29 | `5.05#12` (7,0 s) | H | T1 | `t24_a5_16_shadowy_window_heavy_curtains_16`, `pull` | *According to Korean press reports, Lee Choon-jae exhibited severe domestic abuse tendencies prior to his 1994 arrest.* | — | ✦ Owl | |
| 5-30 | `5.05#13` (8,3 s) | H | T1 | `t24_a5_17_dark_detention_interrogation_room_17`, `still` | *When an acquaintance displays extreme controlling tendencies or cruelty toward women or animals, it signals a personality profile with heightened violent potential.* | — | ✦ Owl | |
| 5-31 | `5.05#14` (7,3 s) | H | T1 | `t24_a5_18_modern_hwaseong_smart_security_dawn_18`, `pan` | *Recognizing these subtle behavioral red flags early and resolutely establishing firm safety boundaries is your most effective shield.* | — | ✦ Owl | |
| 5-32 | `5.05#15` (8,3 s) | H | T1 | `t24_a5_19_modern_hwaseong_smart_security_dawn_19`, `push` | *The fundamental right of every woman to return home safely after an honest day's labor must always stand as the inviolable baseline of a civilized society.* | — | ✦ Owl | |
| 5-33 | `5.05#16` (5,7 s) | H | T1 | `t24_a5_20_forensic_investigation_desk_20`, `pull` | *Thank you for joining Amber Eyes in this profound and deeply reflective behavioral forensic examination today.* | — | ✦ Owl | |
| 5-34 | `5.05#17` (8,6 s) | H | T1 | `t24_a5_21_modern_hwaseong_smart_security_dawn_21`, `still` | *Please subscribe to the channel, activate the notification bell, and share this vital message with your loved ones to foster awareness and safety across our communities.* | — | ✦ Owl | |
| 5-35 | `5.05#18` (4,8 s) | H | T1 | `t24_a5_22_forensic_investigation_desk_22`, `pan` | *Farewell for now, and we look forward to welcoming you in our upcoming investigative profiles.* | — | ✦ Owl | |

**Tổng: 246 shot** (Hồi 1: 58 · Hồi 2: 48 · Hồi 3: 49 · Hồi 4: 56 · Hồi 5: 35) · 155 nền · Phủ 100 % 246/246 câu · thời lượng lời 1860 s (master 2137 s).
