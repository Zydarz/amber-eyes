# HỒ SƠ SẢN XUẤT TẬP 01 · BẢN TIẾNG ANH · "POISON IN THE NAME OF A MOTHER’S LOVE" (PHẦN B)

> **TRẠNG THÁI (09/11/2026): KỊCH BẢN VIẾT LẠI (205 câu) — ĐÃ DỰNG LẠI ẢNH TĨNH, VIDEO CŨ KHÔNG CÒN KHỚP ⇒ CẦN DỰNG LẠI.** Bảng shot + timeline mới ở mục 6 và B1; báo cáo QC: `../Tap01/BaoCao_QC_Tap01_20261109.md`. Chạy lại bất kỳ bước nào bằng `AE_LANG=en py -3 .work/<script>.py` (xem `README.md` §5).

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A), giống bản tiếng Việt.
**Kịch bản:** `01_KICH_BAN/Tap01_EN/kichban_tap01_EN.md` · **Chữ cố định:** `CHU_CO_DINH_EN.md` · **Thành phẩm (sau khi dựng):** `02_SAN_XUAT/Tap01_EN/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md`. File này **sao y** bản gốc ở các cột Câu, Vai, Mẫu, Nền, Nhân vật và mô tả beat; chỉ thay:
- cột **Chữ** sang tiếng Anh (chữ hiện trên màn hình);
- các cụm `ở "…"` trong cột **Beat** sang cụm tiếng Anh **có thật** trong câu EN tương ứng (đã kiểm bằng script, 0 lỗi).

Lời mô tả beat vẫn để tiếng Việt vì renderer dò từ khoá tiếng Việt trong đó (“Dấu”, “giả mạo”, “Thanh tiến trình”, `0/3`…).

## B1. Episode data

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap01_EN/kichban_tap01_EN.md` — **rewritten 09/11/2026** (205 sentences, 1-to-1 with the VN master) |
| Turns / sentences / words | 33 / **205** / 3841 — Host 41% · Investigator 28% · Psychology expert 25% · Neighbour (Sheep) 3% · Viewer (Cat) 2% |
| N1 / N2 | `1.07` Neighbour (Sheep) / `4.03` Viewer (Cat) |
| Measured duration | **1669.64 s (27:49)** — intro 0–22.41 s (`.work/timeline_s_EN.json`, ASR-measured from the new master) |
| Act marks | Act 2 · 05:20 · Act 3 · 11:05 · Act 4 · 16:07 · Act 5 · 21:38 |
| Shot table | **203 rows** = 198 shots with speech + 5 silent rows (4 T10 act cards + 1 end card) |
| Backgrounds | **44 images** from `assets/bg/` (shared by all three languages — H17) |
| Stills | **203 PNG** 1920×1080 (`.work/video3_EN/stills/`) — QC gate before rendering video (H9) |
| H10 exceptions | 3 shots > 15 s · 0 shots < 3 s (sentences that really take longer than 15 s to speak — cannot be split without breaking the verbatim-text rule H6/V3) |

## B2. Results and remaining work

| Item | Result |
|---|---|
| Script | Rewritten 09/11/2026: 205 sentences / 5 acts, sentence IDs identical across VN·EN·JA |
| Timeline | Measured from the new master with ASR (faster-whisper `small`, character-coverage alignment on real word timestamps): **VN 205/205 · EN 205/205 · JA 201/205** sentences matched ≥ 0.45 (gate G1 ≥ 97% — passed) |
| Shot table | 203 rows · covers 205/205 sentences · on-screen text is **verbatim script text** (H6/V3, QC 0 errors) |
| Stills | 203 per language · QC H9 (text contrast — 57 shots use `text_scrim`), H10 (duration + background repetition), H12 (end card), H13 (3-way match) — see `BaoCao_QC_Tap01_20261109.md` |
| **Remaining before publishing** | ① Render the video from the new shot table · ② Regenerate subtitles + description + thumbnail · ③ Fill sources for the 9 `need` sentences · ④ User listens through |

## B3. Tap 01 mapping (in `parse_shots.py`)

| Variable | Value |
|---|---|
| `COMBO` / `INSET` / `BG2` | **empty** — the new shot table sets the background directly in the *Nền* column |
| `route_pins` | `1-29` → ("SPRINGFIELD, MISSOURI", "WISCONSIN") (T7 route map) |
| `text_scrim` | see `edition.py` — shots needing the soft dark scrim (H9, union of 3 languages) |

## 6. DANH SÁCH SHOT — TẬP 01 BẢN TIẾNG ANH (cùng cú pháp A7)

**How to read:** *Vai* = speaker (H Owl · D Wolf · C Fox · N1 Sheep · N2 Cat). The table describes **background + graphics**; badge and bust follow A5.4.
*Nhân vật*: `✦` = first appearance · `→X` = speaker change · `⊘` = hide bust.
Last column: empty = dissolve · `◼` dip to black.

### CHANNEL INTRO · 0.00–22.41 s · `bgm_music_box.mp3`

Place `assets/brand/intro_kenh.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.

### ACT 1 — THE MOMENT TRUST BROKE & COLLECTIVE BLINDSPOTS · main background `house_night`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.03#1`–`#2` (5.5 s) | H | T1 | `house_night`, `pull` | **June fourteenth, twenty fifteen.** → *In the quiet suburban town of Springfield, Missouri.* | — | ✦ Cú |  |
| 1-02 | `1.03#3` (5.5 s) | H | T1 | `night_street`, `still` | *It was a stifling summer evening as darkness descended over the peaceful neighborhood streets.* | — | — |  |
| 1-03 | `1.03#4` (9.9 s) | H | T1 | `phone_dark`, `push` | *Suddenly, on the shared Facebook page of the town’s most beloved mother-daughter duo – Dee Dee Blanchard and her severely disabled daughter Gypsy Rose – a short, chilling status appeared.* | — | — |  |
| 1-04 | `1.03#5` (9.3 s) | H | T1 | `phone_dark`, `pan` | *The hostile message declared that the devoted mother was dead inside her home, throwing the entire community into immediate panic.* | — | — |  |
| 1-05 | `1.05#1` (5.2 s) | H | T1 | `crowd_house`, `pull` | *Distraught neighbors quickly gathered around the small pink bungalow at twenty-one zero three North Volunteer Way.* | — | — |  |
| 1-06 | `1.05#2` (5.7 s) | H | T1 | `charity`, `still` | *That very house had been built and gifted to them by the renowned charitable foundation Habitat for Humanity.* | — | — |  |
| 1-07 | `1.05#3` (7.3 s) | H | T1 | `charity`, `push` | *The family had also received all-expenses-paid trips from Make-A-Wish and continuous financial aid from generous donors across the country.* | — | — |  |
| 1-08 | `1.05#4` (6.6 s) | H | T1 | `crowd_house`, `pan` | *Hundreds of local volunteers and neighbors had once wept with joy as they built the custom wheelchair ramp leading to the front porch.* | — | — |  |
| 1-09 | `1.05#5` (4.6 s) | H | T1 | `house_night`, `pull` | *For years, that modest home stood as a shining symbol of unconditional maternal devotion.* | — | — |  |
| 1-10 | `1.05#6` (6.8 s) | H | T1 | `house_night`, `still` | *To comprehend the sheer shock and disbelief that gripped the town, let us hear from a neighbor who watched their lives unfold for years.* | — | →N1 |  |
| 1-11 | `1.07#1` (5.4 s) | N1 | T1 | `house_night`, `push` | *To everyone living in this town, that little pink house was a sanctuary of pure human kindness.* | — | ✦ Cừu |  |
| 1-12 | `1.07#2` (7.4 s) | N1 | T1 | `house_night`, `pan` | *Dee Dee was an extraordinary single mother who sacrificed every ounce of personal happiness to nurse her frail daughter Gypsy Rose.* | — | — |  |
| 1-13 | `1.07#3` (10.8 s) | N1 | T1 | `wheelchair_room`, `pull` | *The girl suffered from an endless medical list: total paralysis from the waist down, acute leukemia, muscular dystrophy, severe epilepsy, and the mental capacity of a seven-year-old child.* | — | — |  |
| 1-14 | `1.07#4` (5.9 s) | N1 | T1 | `wheelchair_gypsy`, `still` | *The sight of that exhausted mother patiently pushing the wheelchair through our streets was etched into all our memories.* | — | — |  |
| 1-15 | `1.07#5` (5.1 s) | N1 | T1 | `crowd_house`, `push` | *Anyone who saw them together was moved to tears by Dee Dee’s boundless resilience and grace.* | — | — |  |
| 1-16 | `1.07#6` (4.4 s) | N1 | T1 | `house_night`, `pan` | *We genuinely believed she was a living saint walking among us.* | — | →H |  |
| 1-17 | `1.08#1` (6.5 s) | H | T1 | `house_police`, `pull` | *Yet, when police deputies finally forced the door open that cold night, a horrifyingly different reality awaited them.* | — | — |  |
| 1-18 | `1.08#2` (4.6 s) | H | T1 | `bedroom_door`, `still` | *The mother – Dee Dee Blanchard – lay dead upon her bed, having perished days earlier.* | — | ⊘ |  |
| 1-19 | `1.08#3` (4.6 s) | H | T1 | `bedroom_door`, `push` | *A suffocating odor of decay and stale neglect hung heavily throughout the darkened rooms.* | — | — |  |
| 1-20 | `1.08#4` (4.4 s) | H | T1 | `empty_room`, `pan` | *Meanwhile, her frail, bedridden daughter Gypsy Rose had vanished without a trace.* | — | — |  |
| 1-21 | `1.08#5` (7.3 s) | H | T1 | `wheelchair_room`, `pull` | *The custom wheelchair that the girl supposedly needed every second of her life was left standing abandoned in the living room.* | — | — |  |
| 1-22 | `1.08#6` (6.1 s) | H | T1 | `clinical`, `still` | *Dozens of oxygen tanks, feeding tubes, and hundreds of vital prescription bottles remained untouched on the shelves.* | — | ⊘ |  |
| 1-23 | `1.08#7` (4.0 s) | H | T1 | `spotlight`, `push` | *An eerie, chilling silence enveloped the entire crime scene.* | — | — |  |
| 1-24 | `1.08#8` (4.5 s) | H | T1 | `night_screen`, `pan` | *Panic rippled across the nation as breaking news broadcasts took over the airwaves.* | — | — |  |
| 1-25 | `1.08#9` (6.7 s) | H | T1 | `night_street`, `pull` | *Citizens feared a ruthless predator had murdered the saintly mother and abducted a helpless invalid who could not walk a single step.* | — | — |  |
| 1-26 | `1.08#10` (6.0 s) | H | T1 | `pinboard`, `still` | *A nationwide search was immediately launched under the desperate assumption that Gypsy would die within hours without her medication.* | — | — |  |
| 1-27 | `1.08#11` (6.2 s) | H | T1 | `interrogation`, `push` | *Let us listen to the Investigator describe the dramatic turning point when law enforcement finally tracked down the suspects.* | — | →D |  |
| 1-28 | `1.11#1` (9.1 s) | D | T1 | `pinboard`, `pan` | *For the first forty-eight hours, our investigative task force operated under extreme urgency, racing to rescue a dying handicapped girl.* | — | ✦ Sói |  |
| 1-29 | `1.11#2` (10.6 s) | D | T7 tuyến đường | `route_night`, `pull` | *Digital forensics tracing the IP address behind the disturbing social media post quickly led our team to a residence in Big Bend, Wisconsin, over eight hundred kilometers away.* | — | — |  |
| 1-30 | `1.11#3` (6.8 s) | D | T1 | `interrogation_gypsy`, `still` | *There, law enforcement officers apprehended a young man named Nicholas Godejohn alongside a young woman.* | — | — |  |
| 1-31 | `1.11#4` (5.9 s) | D | T1 | `interrogation_gypsy`, `push` | *However, the moment the interrogation room door swung open, our entire perception of reality collapsed.* | — | — |  |
| 1-32 | `1.11#5` (5.5 s) | D | T1 | `interrogation_gypsy`, `pan` | *Walking into our interrogation room that day, Gypsy Rose Blanchard was not in a wheelchair.* | — | — |  |
| 1-33 | `1.11#6` (6.0 s) | D | T1 | `interrogation_gypsy`, `pull` | *She was walking completely unassisted on her own two feet, carrying herself with effortless composure.* | — | — |  |
| 1-34 | `1.11#7` (6.9 s) | D | T1 | `spotlight`, `still` | *Her eyes were sharp, observant, and fully aware, displaying none of the lethargy of a terminally ill patient.* | — | — |  |
| 1-35 | `1.11#8`–`#9` (6.7 s) | D | T1 | `clinical`, `push` | **There was no trace of leukemia.** → *There was no spinal cord damage, nor any signs of muscular dystrophy.* | — | — |  |
| 1-36 | `1.11#10` (7.1 s) | D | T1 | `brain_desk`, `pan` | *Her cognitive faculties were completely intact – the keen mind of a twenty-three-year-old woman, not a child of seven.* | — | — |  |
| 1-37 | `1.11#11` (8.1 s) | D | T1 | `two_shadows`, `pull` | *And the mastermind who orchestrated the demise of that celebrated mother...* → *was none other than the fragile daughter the entire nation had wept for.* | — | →H |  |
| 1-38 | `1.13#1` (2.9 s) | H | T1 | `podcast_desk`, `still` | *Welcome to Amber eyes’ criminal psychology dossier.* | — | — |  |
| 1-39 | `1.13#2` (10.5 s) | H | T1 | `house_night`, `push` | *Today, we step inside the pink house in Springfield to unravel one of the most bizarre and tragic phenomena in medical and legal history: The Gypsy Rose Blanchard Dossier.* | — | — |  |
| 1-40 | `1.13#3` (15.4 s) | H | T1 | `brain_desk`, `pan` | *We will dissect two profound psychological mechanisms: Factitious Disorder Imposed on Another and Learned Helplessness – to answer the agonizing question:* → *How could an elaborate medical prison endure for twenty-three years in broad daylight, shielded by the blinding halo of charity?* | — | — |  |
| 1-41 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 02* · **CRIME SCENE & THE ESCALATING MEDICAL ABYSS** | — | ⊘ | ◼ |

### ACT 2 — THE SCENE & DOSSIER: THE ABERRANT MEDICAL ESCALATION · main background `wheelchair_room`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (6.7 s) | H | T1 | `brain_desk`, `pull` | *To comprehend why a young woman would resort to an extreme act against her own mother to escape, we must examine the true crime scene.* | — | — |  |
| 2-02 | `2.02#2` (5.1 s) | H | T1 | `bedroom_door`, `still` | *The actual scene of this tragedy was not the Missouri bedroom on that June night in twenty fifteen.* | — | — |  |
| 2-03 | `2.02#3` (7.6 s) | H | T1 | `wheelchair_room`, `push` | *The true scene was the physical body of Gypsy Rose herself, subjected to medical confinement and invasive interventions for twenty-three years.* | — | — |  |
| 2-04 | `2.02#4` (5.2 s) | H | T1 | `clinical`, `pan` | *A young girl with a frail frame, sunken eyes, and a mouth completely stripped of her natural teeth.* | — | — |  |
| 2-05 | `2.02#5` (7.9 s) | H | T1 | `pinboard`, `pull` | *This pathological trajectory did not occur overnight; it was constructed across four escalating stages of medical abuse spanning more than two decades.* | — | — |  |
| 2-06 | `2.02#6` (4.3 s) | H | T1 | `records`, `still` | *I invite the Investigator to disclose the details of the recovered medical records.* | — | →D |  |
| 2-07 | `2.04#1` (10.5 s) | D | T1 | `records`, `push` | *Piecing together thousands of archived pages from dozens of regional hospitals, we reconstructed Dee Dee Blanchard’s systematic pattern of abuse across four distinct phases:* | — | — |  |
| 2-08 | `2.04#2` (3.5 s) | D | T1 | `pinboard`, `pan` | *Stage One: Fabricating Initial Symptoms.* | — | — |  |
| 2-09 | `2.04#3` (4.7 s) | D | T1 | `house_dawn`, `pull` | *Gypsy Rose was born in nineteen ninety-one as a completely healthy infant.* | — | — |  |
| 2-10 | `2.04#4` (9.0 s) | D | T1 | `clinical`, `still` | *Yet when the baby was barely three months old, Dee Dee began carrying her to emergency rooms, insisting her daughter suffered from unexplained sleep apnea.* | — | — |  |
| 2-11 | `2.04#5` (11.2 s) | D | T1 | `wheelchair_room`, `push` | *By the time Gypsy turned seven, following a minor scrape on her knee from a tricycle fall,* → *Dee Dee claimed the child sustained irreversible spinal damage and forced her into a wheelchair permanently.* | — | — |  |
| 2-12 | `2.04#6`–`#7` (10.9 s) | D | T1 | `pinboard`, `pan` | *Stage Two: Physical Violation and Chemical Alteration.* → *When verbal falsehoods were no longer sufficient, Dee Dee began tampering directly with her daughter’s biology.* | — | — |  |
| 2-13 | `2.04#8` (8.0 s) | D | T1 | `clinical`, `pull` | *She forced Gypsy to ingest high doses of the anti-seizure medication Tegretol for years despite completely normal EEG results.* | — | — |  |
| 2-14 | `2.04#9` (11.2 s) | D | T1 | `clinical`, `still` | *The severe side effects of the drug combined with induced malnutrition destroyed the girl’s dental enamel, leaving her teeth completely rotted until doctors were forced to surgically extract them all.* | — | ⊘ |  |
| 2-15 | `2.04#10` (11.7 s) | D | T1 | `clinical`, `push` | *She pressured surgeons into surgically installing a feeding tube directly into the child’s stomach, turning a girl capable of normal eating into someone utterly dependent on liquid formula.* | — | ⊘ |  |
| 2-16 | `2.04#11` (9.6 s) | D | T1 | `clinical`, `pan` | *She even convinced specialists at Children’s Mercy Hospital to surgically excise Gypsy’s salivary glands after secretly administering medication that dried out her mouth.* | — | ⊘ |  |
| 2-17 | `2.04#12` (3.9 s) | D | T1 | `pinboard`, `pull` | *Stage Three: System Manipulation and Evading Detection.* | — | — |  |
| 2-18 | `2.04#13` (8.1 s) | D | T1 | `records`, `still` | *Dee Dee previously worked as a nurse’s aide, allowing her to fluently wield medical terminology and describe textbook symptoms to deceive physicians.* | — | — |  |
| 2-19 | `2.04#14` (7.5 s) | D | T1 | `clinical`, `push` | *Prior to clinical appointments, she routinely applied numbing agents or irritants to induce artificial physical reactions on her daughter.* | — | — |  |
| 2-20 | `2.04#15` (13.6 s) | D | T1 | `storm`, `pan` | *In two thousand and five, when Hurricane Katrina devastated Louisiana,* → *she seized upon the natural disaster to claim Gypsy’s entire medical history was lost in the floodwaters, erasing past diagnostic baselines.* | — | — |  |
| 2-21 | `2.04#16` (4.1 s) | D | T1 | `pinboard`, `pull` | *Stage Four: Total Erasure of Identity and Autonomy.* | — | — |  |
| 2-22 | `2.04#17` (8.3 s) | D | T1 | `deedee_room`, `still` | *Dee Dee systematically shaved her daughter’s head, telling everyone the baldness was caused by chemotherapy for leukemia.* | — | — |  |
| 2-23 | `2.04#18` (9.8 s) | D | T1 | `dress_hanger`, `push` | *She forced Gypsy to wear childlike princess dresses, oversized glasses, and strictly prohibited her from speaking to outsiders without direct parental oversight.* | — | →H |  |
| 2-24 | `2.06#1` (7.3 s) | H | T1 | `brain_desk`, `pan` | *Through the lens of behavioral science, this relentless control reflects a distinct Modus Operandi and Psychological Signature.* | — | — |  |
| 2-25 | `2.06#2` (5.9 s) | H | T1 | `pinboard`, `pull` | *Let us hear the Psychologist analyze the crucial distinction between the perpetrator’s method and her inner signature.* | — | →C |  |
| 2-26 | `2.07#1` (6.6 s) | C | T9 thuật ngữ | `brain_desk`, `still` | **Modus Operandi and Psychological Signature** · *In forensic psychology, we draw a rigorous line between Modus Operandi and Psychological Signature:* | — | ✦ Cáo |  |
| 2-27 | `2.07#2` (6.2 s) | C | T1 | `records`, `push` | *The Modus Operandi encompasses the practical steps a perpetrator takes to commit an offense and avoid apprehension.* | — | — |  |
| 2-28 | `2.07#3` (9.7 s) | C | T1 | `pinboard`, `pan` | *With Dee Dee, her MO evolved dynamically: she mastered*“Doctor shopping” | — | — |  |
| 2-29 | `2.07#4` (11.8 s) | C | T1 | `records`, `pull` | *In two thousand and seven, pediatric neurologist Doctor Bernardo Flasterstein in Missouri noted in Gypsy’s file that he found no evidence of muscular dystrophy or paralysis, suspecting the mother suffered from Munchausen by proxy.* | — | — |  |
| 2-30 | `2.07#5` (8.5 s) | C | T1 | `interrogation`, `still` | *The doctor openly confronted Dee Dee regarding the child’s completely normal physical exam.* | — | — |  |
| 2-31 | `2.07#6` (9.9 s) | C | T1 | `house_return`, `push` | *Sensing the imminent danger of exposure, Dee Dee immediately severed all contact with him, angrily accused him of incompetence, and fled to a completely different healthcare network.* | — | — |  |
| 2-32 | `2.07#7` (7.8 s) | C | T1 | `brain_desk`, `pan` | *Conversely, the Psychological Signature is the immutable core behavior that satisfies the offender’s pathological emotional appetite.* | — | — |  |
| 2-33 | `2.07#8`–`#9` (11.0 s) | C | T1 | `doll`, `pull` | *Dee Dee’s signature was the Forced Infantilization of her offspring.* → *She altered Gypsy’s birth certificate, legally transforming a twenty-year-old young woman into a sixteen-year-old child on paper.* | — | — |  |
| 2-34 | `2.07#10` (6.0 s) | C | T1 | `doll`, `still` | *She compelled her daughter to wear colorful wigs, clutch stuffed animals, and speak in a high-pitched baby voice.* | — | — |  |
| 2-35 | `2.07#11` (8.7 s) | C | T1 | `spotlight_deedee`, `push` | *Dee Dee did not merely want a sick child; she desperately craved an eternal porcelain doll who would remain utterly helpless and bound to her existence forever.* | — | →H |  |
| 2-36 | `2.08#1` (6.7 s) | H | T1 | `brain_desk`, `pan` | *Alongside that psychological signature, Dee Dee’s perception of her child revealed the profound cruelty of the disorder.* | — | — |  |
| 2-37 | `2.08#2` (6.7 s) | H | T1 | `spotlight_deedee`, `pull` | *Dee Dee never viewed Gypsy as an autonomous human being endowed with personal desires, feelings, or the right to health.* | — | — |  |
| 2-38 | `2.08#3` (8.6 s) | H | T1 | `glass_box`, `still` | *In her warped cognitive architecture, Gypsy was demoted to a “living prop” – a biological tool utilized to harvest societal adulation and sympathy.* | — | — |  |
| 2-39 | `2.08#4` (6.3 s) | H | T1 | `clinical`, `push` | *Every unnecessary injection and invasive surgery evoked no maternal agony within Dee Dee’s mind.* | — | — |  |
| 2-40 | `2.08#5` (5.4 s) | H | T1 | `cage`, `pan` | *They were merely reinforcement pins driven deeper into the glass cage enclosing a captive human soul.* | — | — |  |
| 2-41 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 03* · **PSYCHOLOGICAL AUTOPSY — INSIDE THE MIND OF FDIA** | — | ⊘ | ◼ |

### ACT 3 — PSYCHOLOGICAL AUTOPSY: INSIDE THE FDIA MIND · main background `brain_desk`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (4.0 s) | H | T1 | `void`, `pull` | *At this juncture, every observer must confront the haunting question:* | — | — |  |
| 3-02 | `3.02#2` (6.2 s) | H | T1 | `fog_deedee`, `still` | *What could possibly compel a mother to inflict such prolonged torment upon her own flesh and blood for twenty-three years?* | — | — |  |
| 3-03 | `3.02#3` (6.5 s) | H | T1 | `charity`, `push` | *Many commentators hastily assume Dee Dee orchestrated the deception purely for government checks and complimentary trips to Disneyland.* | — | — |  |
| 3-04 | `3.02#4` (6.0 s) | H | T1 | `records`, `pan` | *Yet if financial gain were the primary driver, a fraudster would adopt far simpler and less agonizing schemes.* | — | — |  |
| 3-05 | `3.02#5` (5.1 s) | H | T1 | `brain_desk`, `pull` | *From a forensic psychiatric perspective, material perks were merely incidental side benefits.* | — | — |  |
| 3-06 | `3.02#6` (8.4 s) | H | T1 | `brain_desk`, `still` | *The driving engine behind Dee Dee Blanchard’s behavior was a severe psychiatric condition: Factitious Disorder Imposed on Another (FDIA).* | — | — |  |
| 3-07 | `3.02#7` (5.2 s) | H | T1 | `brain_desk`, `push` | *I invite the Psychologist to dissect the cognitive strata operating within the mind of this perpetrator.* | — | →C |  |
| 3-08 | `3.04#1` (7.3 s) | C | T9 thuật ngữ | `clinical`, `pan` | **DSM-5-TR** · *Under the diagnostic framework of the DSM-5-TR, FDIA is fundamentally distinct from ordinary Malingering.* | — | — |  |
| 3-09 | `3.04#2` (7.0 s) | C | T1 | `records`, `pull` | *A malingerer fakes illness for external incentives such as financial payouts and avoids unnecessary public exposure.* | — | — |  |
| 3-10 | `3.04#3` (7.6 s) | C | T9 thuật ngữ | `spotlight_deedee`, `still` | **Narcissistic Supply** · *A perpetrator of FDIA, however, craves a far more insidious and intoxicating currency: Narcissistic Supply.* | — | — |  |
| 3-11 | `3.04#4`–`#5` (8.6 s) | C | T1 | `brain_desk`, `push` | *Dissecting Dee Dee Blanchard’s psyche reveals three interwoven pathological layers:* → *Layer One: The Addiction to the Saintly Mother Halo.* | — | — |  |
| 3-12 | `3.04#6` (12.3 s) | C | T1 | `fog`, `pan` | *Prior to motherhood, Dee Dee’s life was an unrelenting sequence of personal failures: petty shoplifting charges, ostracization by her relatives, and a marriage to Rod Blanchard that collapsed when she was twenty-four.* | — | — |  |
| 3-13 | `3.04#7` (3.9 s) | C | T1 | `fog`, `pull` | *She was a marginalized, unremarkable figure starved for validation.* | — | — |  |
| 3-14 | `3.04#8` (7.6 s) | C | T1 | `house_night`, `still` | *Yet the moment she assumed the identity of the courageous single mother battling to save a doomed child, her social reality transformed.* | — | — |  |
| 3-15 | `3.04#9` (7.9 s) | C | T1 | `crowd_house`, `push` | *Everywhere she went, doctors treated her with deference, neighbors shed tears of admiration, and local newspapers celebrated her heroism.* | — | — |  |
| 3-16 | `3.04#10` (5.5 s) | C | T1 | `void`, `pan` | *This overwhelming public reverence filled the pathological void of inadequacy festering inside her ego.* | — | — |  |
| 3-17 | `3.04#11` (8.8 s) | C | T1 | `clinical`, `pull` | *Every chorus of praise affirming*“You are the most selfless mother alive” | — | →H |  |
| 3-18 | `3.06#1` (3.1 s) | H | T1 | `house_night`, `still` | *Yet that public saintliness was only the outer façade.* | — | — |  |
| 3-19 | `3.06#2` (4.3 s) | H | T1 | `house_closed`, `push` | *What was unfolding within Dee Dee’s intimate family relationships behind closed doors?* | — | — |  |
| 3-20 | `3.06#3` (4.4 s) | H | T1 | `records`, `pan` | *Let us hear the Investigator share the familial background uncovered during the inquiry.* | — | →D |  |
| 3-21 | `3.07#1` (9.0 s) | D | T1 | `records`, `pull` | *When we interviewed Dee Dee’s extended maternal relatives in Louisiana, family members universally voiced intense dread regarding her character.* | — | — |  |
| 3-22 | `3.07#2` (7.1 s) | D | T1 | `locked_door`, `still` | *They disclosed that from her youth, Dee Dee demonstrated extreme psychological manipulation and controlling tendencies.* | — | — |  |
| 3-23 | `3.07#3` (7.5 s) | D | T1 | `locked_door`, `push` | *Her own family even harbored grave suspicions that she played a role in compromising her biological mother’s health prior to her death.* | — | — |  |
| 3-24 | `3.07#4` (6.5 s) | D | T1 | `corridor`, `pan` | *A maternal aunt revealed that relatives once caught Dee Dee deliberately poisoning family meals.* | — | — |  |
| 3-25 | `3.07#5` (6.7 s) | D | T1 | `house_closed`, `pull` | *Following Gypsy’s birth, Dee Dee completely severed ties with her family and systematically isolated the infant from the father, Rod Blanchard.* | — | — |  |
| 3-26 | `3.07#6` (13.1 s) | D | T1 | `records`, `still` | *Month after month, the father dutifully mailed child support checks, but Dee Dee continually lied that Gypsy was severely brain-damaged and could neither speak nor see him.* | — | — |  |
| 3-27 | `3.07#7` (6.7 s) | D | T1 | `locked_door`, `push` | *Rod Blanchard was even banned from attending the charitable house handover ceremony celebrating his daughter.* | — | — |  |
| 3-28 | `3.07#8` (7.3 s) | D | T1 | `crowd_away`, `pan` | *Family members were treated as hazardous threats who had to be purged, because they alone possessed the ability to see through her mask.* | — | →C |  |
| 3-29 | `3.08#1` (5.9 s) | C | T9 thuật ngữ | `brain_desk`, `pull` | **The Mechanism of Compartmentalization** · *From this calculated isolation emerges Layer Two: The Mechanism of Compartmentalization.* | — | — |  |
| 3-30 | `3.08#2` (5.1 s) | C | T1 | `hands`, `still` | *Dee Dee’s brain maintained two hermetically sealed mental compartments that never interacted:* | — | — |  |
| 3-31 | `3.08#3` (7.8 s) | C | T1 | `hands`, `push` | *One compartment housed the doting mother who stayed awake all night massaging her daughter’s limbs, singing lullabies, and blending special meals.* | — | — |  |
| 3-32 | `3.08#4` (7.4 s) | C | T1 | `deedee_room`, `pan` | *The other compartment housed a cold-blooded abuser willing to tie her daughter to a bedpost to force-feed toxic medications.* | — | — |  |
| 3-33 | `3.08#5` (8.8 s) | C | T1 | `glass_box`, `pull` | *Dee Dee utilized maternal devotion as a*“Shield of Normalcy” | — | — |  |
| 3-34 | `3.08#6` (5.1 s) | C | T9 thuật ngữ | `brain_desk`, `still` | **Techniques of Neutralization and the Deficit of Affective Empathy** · *And Layer Three is: Techniques of Neutralization and the Deficit of Affective Empathy.* | — | — |  |
| 3-35 | `3.08#7`–`#8` (11.3 s) | C | T1 | `records`, `push` | *Dee Dee suffered from an acute impairment in Theory of Mind.* → *She was entirely numb to the genuine physical torture Gypsy endured with every needle prick, catheter insertion, or surgical incision.* | — | — |  |
| 3-36 | `3.08#9` (10.3 s) | C | T1 | `hands`, `pan` | *She rationalized her conduct through warped cognitive justifications:*“She is too fragile; the cruel outside world will destroy her; my control alone keeps her alive.” | — | — |  |
| 3-37 | `3.08#10` (6.5 s) | C | T1 | `void`, `pull` | *She blamed circumstance, celebrated victimhood, and anointed herself as the sole arbiter of her daughter’s existence.* | — | — |  |
| 3-38 | `3.08#11` (9.2 s) | C | T1 | `house_night`, `still` | *This moral disengagement neutralized any flicker of guilt, allowing Dee Dee to sleep peacefully every night beside a daughter writhing in artificially manufactured agony.* | — | — |  |
| 3-39 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 04* · **THE VICTIM'S VIEW — WHY COULDN'T GYPSY STAND UP?** | — | ⊘ | ◼ |

### ACT 4 — THE VICTIM'S PRISON: WHY DIDN'T GYPSY WALK AWAY? · main background `locked_door`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (5.7 s) | H | T1 | `night_screen`, `push` | *When the stunning truth of the case broke into public consciousness, a fierce wave of skepticism erupted.* | — | — |  |
| 4-02 | `4.02#2` (5.4 s) | H | T1 | `night_screen`, `pan` | *Many observers struggled to reconcile Gypsy Rose’s actions, greeting her narrative with harsh suspicion.* | — | — |  |
| 4-03 | `4.02#3` (5.0 s) | H | T1 | `spotlight`, `pull` | *They argued that an adult possessed the inherent agency to seek help or flee an abusive guardian.* | — | — |  |
| 4-04 | `4.02#4` (3.8 s) | H | T1 | `podcast_desk`, `still` | *Let us listen to a prominent question voiced by the public following the case.* | — | →N2 |  |
| 4-05 | `4.03#1` (7.6 s) | N2 | T1 | `house_night`, `push` | *There is something fundamental I simply cannot fathom: She knew beyond any shadow of a doubt that her legs functioned perfectly.* | — | ✦ Mèo |  |
| 4-06 | `4.03#2` (6.8 s) | N2 | T1 | `house_night`, `pan` | *Every night behind closed bedroom doors, she stood up, walked around freely, and raided the kitchen pantry for food.* | — | — |  |
| 4-07 | `4.03#3` (5.6 s) | N2 | T1 | `crowd_house`, `pull` | *She even attended science fiction conventions in costume, interacting with strangers in crowded halls.* | — | — |  |
| 4-08 | `4.03#4` (11.5 s) | N2 | T1 | `wheelchair_room`, `still` | *Why, over all those years, before hundreds of doctors, nurses, police officers, and charity volunteers, did Gypsy never once stand up from that wheelchair to shout for help and expose her mother?* | — | →H |  |
| 4-09 | `4.05#1` (6.1 s) | H | T1 | `spotlight`, `push` | *That is an intuitive question for anyone assessing the situation from the perspective of an autonomous, free individual.* | — | — |  |
| 4-10 | `4.05#2` (10.1 s) | H | T1 | `brain_desk`, `pan` | *Yet to decipher Gypsy’s paralysis, we cannot apply ordinary adult logic; we must examine two invisible psychological shackles: Learned Helplessness and Trauma Bonding.* | — | — |  |
| 4-11 | `4.05#3` (3.4 s) | H | T1 | `clinical`, `pull` | *I ask the Psychologist to unpack this cognitive imprisonment.* | — | →C |  |
| 4-12 | `4.07#1` (7.4 s) | C | T9 thuật ngữ | `clinical`, `still` | **Learned Helplessness** · *In nineteen sixty-seven, pioneering psychologist Martin Seligman formulated the seminal paradigm of Learned Helplessness.* | — | — |  |
| 4-13 | `4.07#2` (12.3 s) | C | T1 | `cage`, `push` | *In his classic experiments, when an animal was placed in a chamber and subjected to unpredictable shocks from which no evasion was possible, after repeated failed attempts to resist, the creature ceased struggling altogether.* | — | — |  |
| 4-14 | `4.07#3` (9.5 s) | C | T1 | `cage_open`, `pan` | *Even when researchers subsequently opened the chamber door and removed the electric current, the animal remained motionless, whimpering in passive despair rather than stepping outside.* | — | — |  |
| 4-15 | `4.07#4` (6.5 s) | C | T1 | `brain_desk`, `pull` | *A severely traumatized brain internalizes a fatalistic cognitive conviction:*“Any struggle is futile.” | — | — |  |
| 4-16 | `4.07#5` (8.3 s) | C | T1 | `hands`, `still` | *Consider Gypsy’s developmental reality: From her earliest memories, whenever she sat before a doctor, Dee Dee gripped her tiny hand tightly.* | — | — |  |
| 4-17 | `4.07#6` (4.9 s) | C | T1 | `hands`, `push` | *To an unsuspecting observer, it appeared to be a warm, protective maternal clasp.* | — | — |  |
| 4-18 | `4.07#7` (9.0 s) | C | T1 | `hands`, `pan` | *To Gypsy, it was a lethal warning signal: If she uttered an incorrect word or shifted her legs, her mother’s fingernails dug into her flesh until it bruised.* | — | ⊘ |  |
| 4-19 | `4.07#8` (6.0 s) | C | T1 | `brain_desk`, `pull` | *Dee Dee conditioned her daughter into believing she was mentally impaired and that mother alone knew what was safe.* | — | — |  |
| 4-20 | `4.07#9` (7.8 s) | C | T1 | `house_closed`, `still` | *And behind the closed doors of that pink house awaited physical beatings, days of starvation, and explicit threats of abandonment.* | — | →H · ⊘ |  |
| 4-21 | `4.09#1`–`#2` (13.1 s) | H | T1 | `house_closed`, `push` | *Gypsy was not devoid of resistance; she had indeed attempted escape.* → *In police archives, investigators documented a pivotal crisis that occurred in twenty eleven – an event that permanently shattered her hope in society.* | — | →D |  |
| 4-22 | `4.10#1` (6.2 s) | D | T1 | `night_street`, `pan` | *In twenty eleven, at the age of nineteen, Gypsy gathered the courage to orchestrate a midnight escape.* | — | — |  |
| 4-23 | `4.10#2` (6.7 s) | D | T1 | `night_street_gypsy`, `pull` | *She slipped out of her bedroom and fled to the apartment of an acquaintance in the area, desperately begging for sanctuary.* | — | — |  |
| 4-24 | `4.10#3` (4.6 s) | D | T1 | `house_night`, `still` | *The terrified girl pleaded with the occupants to conceal her and keep her mother away.* | — | — |  |
| 4-25 | `4.10#4` (7.1 s) | D | T1 | `records`, `push` | *Yet within hours, Dee Dee materialized at the doorstep clutching an imposing stack of fraudulent medical affidavits.* | — | — |  |
| 4-26 | `4.10#5` (9.5 s) | D | T1 | `crowd_house`, `pan` | *Weeping profusely before the bewildered hosts, she insisted her daughter possessed the cognitive capacity of a toddler and was undergoing a severe psychotic delusion.* | — | — |  |
| 4-27 | `4.10#6` (5.9 s) | D | T1 | `crowd_house`, `pull` | *The neighbors instantly surrendered to the saintly mother’s tears and returned Gypsy to her custody.* | — | — |  |
| 4-28 | `4.10#7` (5.4 s) | D | T1 | `house_closed`, `still` | *Following that night, Dee Dee smashed Gypsy’s computer with a hammer right before her eyes.* | — | — |  |
| 4-29 | `4.10#8` (7.8 s) | D | T1 | `cage`, `push` | *She chained the girl to her metal bed frame for two consecutive weeks, warning her that authorities would never believe the words of a madwoman.* | — | →H · ⊘ |  |
| 4-30 | `4.11#1` (10.4 s) | H | T1 | `void`, `pan` | *That devastating crisis in twenty eleven drove the final nail into Gypsy’s cognitive coffin: Society would always worship her mother’s halo, rendering her own voice entirely invisible.* | — | — |  |
| 4-31 | `4.11#2` (4.1 s) | H | T1 | `clinical`, `pull` | *And beyond terror, the Psychologist points to a second psychological knot.* | — | →C |  |
| 4-32 | `4.12#1` (2.8 s) | C | T9 thuật ngữ | `hands`, `still` | **Trauma Bonding** · *That was the invisible shackle of Trauma Bonding.* | — | — |  |
| 4-33 | `4.12#2` (10.2 s) | C | T1 | `hands`, `push` | *Dee Dee was the tormentor poisoning Gypsy’s body, yet she was also the sole human being who embraced her every night, brushed her hair, and whispered that Gypsy was her precious angel.* | — | — |  |
| 4-34 | `4.12#3` (12.9 s) | C | T1 | `glass_box`, `pan` | *This erratic oscillation between terrifying brutality and suffocating affection completely dismantled the victim’s psychological defense mechanisms, binding Gypsy in a web of simultaneous hatred and absolute dependence.* | — | — |  |
| 4-35 | `4.12#4` (8.4 s) | C | T1 | `void`, `pull` | *In an entirely isolated universe, love and abuse became inextricably fused, blinding the victim to any healthy boundaries of survival.* | — | →H |  |
| 4-36 | `4.14#1` (9.7 s) | H | T1 | `cage`, `still` | *With every legitimate avenue of rescue extinguished in her mind, cornered survival instinct sought an extreme resolution.* | — | — |  |
| 4-37 | `4.14#2` (8.4 s) | H | T1 | `godejohn_screen`, `push` | *In twenty twelve, through covert internet access, Gypsy connected with Nicholas Godejohn – a twenty-four-year-old youth with an established history of autism and personality disturbances.* | — | — |  |
| 4-38 | `4.14#3` (7.3 s) | H | T9 thuật ngữ | `two_shadows`, `pan` | **Folie à Deux** · *Two deeply isolated and troubled psyches collided, descending into the perilous shared delusion known as Folie à Deux – Shared Madness.* | — | — |  |
| 4-39 | `4.14#4` (6.1 s) | H | T1 | `two_shadows`, `pull` | *A dark fantasy of romantic salvation propelled both into an irreversible scheme of termination.* | — | — |  |
| 4-40 | `4.14#5` (7.3 s) | H | T1 | `house_night`, `still` | *And on the night of June fourteenth, twenty fifteen, the door of the pink house was unlocked from within...* | — | — |  |
| 4-41 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *ACT 05* · **FORENSIC VERDICT, PSYCHOLOGICAL JUDGMENT & RED FLAGS** | — | ⊘ | ◼ |

### ACT 5 — FORENSIC VERDICT, PSYCHOLOGICAL SENTENCE & SURVIVAL RED FLAGS · main background `court_dawn`

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (7.7 s) | H | T1 | `court_dawn`, `push` | *The legal proceedings surrounding Gypsy Rose Blanchard in Missouri evolved into one of the most morally complex dilemmas in American jurisprudence.* | — | — |  |
| 5-02 | `5.02#2` (6.7 s) | H | T1 | `court_dawn`, `pan` | *Under statutory criminal law, actively conspiring to terminate a parent’s life constitutes an unmitigated felony.* | — | — |  |
| 5-03 | `5.02#3` (10.5 s) | H | T1 | `records`, `pull` | *Yet when confronted with undeniable clinical evidence proving twenty-three years of torture and chemical assault, Greene County Prosecuting Attorney Dan Patterson faced an unprecedented ethical paradox.* | — | — |  |
| 5-04 | `5.02#4` (12.9 s) | H | T1 | `court_dawn`, `still` | *The prosecutor conceded this was the most extraordinary proceeding of his career: an individual who was undeniably a perpetrator,* → *yet simultaneously the surviving victim of an unimaginable cycle of prolonged torture.* | — | — |  |
| 5-05 | `5.02#5` (8.4 s) | H | T1 | `spotlight`, `push` | *It presented a rare juncture where the scales of justice had to balance statutory retribution against profound compassion for a soul broken by captivity.* | — | — |  |
| 5-06 | `5.04#1` (11.3 s) | H | T1 | `prison_window`, `pan` | *In twenty sixteen, through a negotiated plea agreement, Gypsy Rose Blanchard pleaded guilty to second-degree murder, receiving a ten-year prison sentence – the most lenient term legally accessible for homicide.* | — | — |  |
| 5-07 | `5.04#2` (7.0 s) | H | T1 | `prison_window`, `pull` | *Meanwhile, Nicholas Godejohn received a sentence of life imprisonment without the possibility of parole for carrying out the physical act.* | — | — |  |
| 5-08 | `5.04#3` (6.6 s) | H | T1 | `court_dawn`, `still` | *Gypsy’s ten-year sentence stood as a historic equilibrium between the rigidity of the law and forensic psychiatric humanity.* | — | — |  |
| 5-09 | `5.04#4` (5.1 s) | H | T1 | `prison_window`, `push` | *Let us hear the Investigator share the psychological paradox discovered behind the penitentiary walls.* | — | →D |  |
| 5-10 | `5.05#1` (8.7 s) | D | T1 | `prison_window`, `pan` | *Upon entering the Chillicothe Correctional Center, Gypsy Rose offered a statement that moved seasoned forensic clinicians to profound contemplation.* | — | — |  |
| 5-11 | `5.05#2` (9.7 s) | D | T1 | `prison_window`, `pull` | *She declared:*“Living inside a state prison, for the first time in my life, I feel truly freer than I ever was inside my mother’s home.” | — | — |  |
| 5-12 | `5.05#3` (7.8 s) | D | T1 | `prison_window`, `still` | *Within the prison walls, her physical body was confined behind bars, but her spirit was finally unbound.* | — | ⊘ |  |
| 5-13 | `5.05#4` (9.4 s) | D | T1 | `house_dawn`, `push` | *She was permitted to grow out her natural hair, enjoy regular meals by mouth, abandon the wheelchair, and walk freely on her own feet without fear of medical assault.* | — | — |  |
| 5-14 | `5.05#5` (5.4 s) | D | T1 | `clinical`, `pan` | *Prison dentists fitted her with a complete set of dental prosthetics, restoring her human smile.* | — | — |  |
| 5-15 | `5.05#6` (6.2 s) | D | T1 | `house_dawn`, `pull` | *She successfully earned her high school diploma, experiencing formal education for the first time in her existence.* | — | — |  |
| 5-16 | `5.05#7` (10.8 s) | D | T1 | `house_free`, `still` | *On December twenty-eighth, twenty twenty-three, having served eighty-five percent of her sentence, Gypsy Rose Blanchard walked out of the prison gates to reclaim her life.* | — | →H |  |
| 5-17 | `5.06#1` (7.4 s) | H | T1 | `spotlight`, `push` | *The societal shockwaves of the Blanchard tragedy resonated across global child protection agencies and public healthcare institutions.* | — | — |  |
| 5-18 | `5.06#2` (9.1 s) | H | T1 | `records`, `pan` | *It brutally unmasked the systemic failure of disconnected hospital networks, which allowed perpetrators of Munchausen by proxy to deceive medical facilities with impunity.* | — | — |  |
| 5-19 | `5.06#3` (8.9 s) | H | T1 | `records`, `pull` | *Across numerous jurisdictions, inter-agency protocols between clinics, schools, and social services were overhauled to shield vulnerable minors from medical abuse.* | — | — |  |
| 5-20 | `5.06#4` (8.3 s) | H | T1 | `brain_desk`, `still` | *To protect innocent dependents and prevent similar tragedies, we present the Four Survival Red Flags synthesized by our Psychologist and Investigator.* | — | →C |  |
| 5-21 | `5.07#1` (7.6 s) | C | T1 | `clinical`, `push` | *From a forensic and clinical psychiatric standpoint, observers must remain vigilant regarding the first two diagnostic markers:* | — | — |  |
| 5-22 | `5.07#2` (4.6 s) | C | T8 cờ | `clinical`, `pan` | *01* · **Red Flag One: Inexplicably Complex History and Objective Contradictions.** | — | — |  |
| 5-23 | `5.07#3` (11.6 s) | C | T1 | `records`, `pull` | *The dependent carries an extensive roster of catastrophic diagnoses, yet objective laboratory and radiological tests continually return normal or flatly contradict the caregiver’s dramatic assertions.* | — | — |  |
| 5-24 | `5.07#4` (3.4 s) | C | T8 cờ | `clinical`, `still` | *02* · **Red Flag Two: Situational Emergence of Symptoms.** | — | — |  |
| 5-25 | `5.07#5` (10.6 s) | C | T1 | `records`, `push` | *The bizarre medical anomalies manifest exclusively in the physical presence of the caregiver, vanishing or rapidly improving when the patient is isolated or monitored under objective surveillance.* | — | — |  |
| 5-26 | `5.07#6` (7.7 s) | C | T1 | `clinical`, `pan` | *Upon separation from the caregiver, the patient’s physical vitality often rebounds dramatically without intensive medical intervention.* | — | →D |  |
| 5-27 | `5.08#1` (6.8 s) | D | T1 | `pinboard`, `pull` | *From a behavioral and social investigative perspective, we emphasize the remaining two behavioral indicators:* | — | — |  |
| 5-28 | `5.08#2` (4.6 s) | D | T8 cờ | `pinboard`, `still` | *03* · **Red Flag Three: Doctor Shopping and Attention Addiction.** | — | — |  |
| 5-29 | `5.08#3` (15.2 s) | D | T1 | `records`, `push` | *The caregiver routinely engages in*“Doctor shopping” | — | — |  |
| 5-30 | `5.08#4` (4.0 s) | D | T8 cờ | `house_closed`, `pan` | *04* · **And Red Flag Four: Enforced Social Seclusion.** | — | — |  |
| 5-31 | `5.08#5` (8.4 s) | D | T1 | `crowd_away`, `pull` | *The victim is completely severed from schooling, peers, and extended relatives under the benevolent pretext of*“shielding fragile health.” | — | — |  |
| 5-32 | `5.08#6` (5.5 s) | D | T1 | `spotlight`, `still` | *The caregiver fiercely insists on being the sole gatekeeper of the dependent’s narrative and survival.* | — | →H |  |
| 5-33 | `5.10#1` (7.9 s) | H | T1 | `house_dawn`, `push` | *The dossier on the pink bungalow in Springfield draws to a close, yet its inquiry into the nature of empathy and human ethics echoes unresolved.* | — | — |  |
| 5-34 | `5.10#2` (7.6 s) | H | T1 | `house_dawn`, `pan` | *Authentic parental devotion serves as wings that empower a child to grow robust, stand resilient on their own feet, and freely explore the world.* | — | — |  |
| 5-35 | `5.10#3` (13.5 s) | H | T1 | `cage_open`, `pull` | *When maternal devotion is perverted into an instrument of selfish ownership, when care transforms into an agonizing cage feeding an adult’s pathological ego...* → *that which wears the mantle of love can inflict devastation far deadlier than any blade.* | — | — |  |
| 5-36 | `5.10#4` (5.3 s) | H | T1 | `charity`, `still` | *Compassion devoid of discernment inadvertently cultivates fertile ground where calculated cruelty thrives.* | — | — |  |
| 5-37 | `5.10#5` (9.9 s) | H | T1 | `house_dawn`, `push` | *The enduring wisdom bequeathed by this tragic inquiry is an urgent imperative: Never allow anyone’s outward aura of sanctity to disarm your vigilant intuition and moral clarity.* | — | — |  |
| 5-38 | `5.12#1` (8.5 s) | H | T1 | `podcast_desk`, `pan` | *Our gratitude to the expert guests who contributed their forensic insights, and our deepest thanks to you for walking alongside us to the final minutes of this exploration.* | — | — |  |
| 5-39 | `5.12#2` (5.2 s) | H | T1 | `house_night`, `pull` | *Your empathy and discernment inspire our mission to illuminate the darkest corners of criminal psychology.* | — | — |  |
| 5-40 | `5.12#3` (10.9 s) | H | T1 | `podcast_desk`, `still` | *Share your reflections in the comments below, preserve your intellectual vigilance, and we look forward to greeting you in our next psychological dossier.* | — | — |  |
| 5-41 | hết tập (7.0 s) | — | T1 | `void` | **CASE FILE 01 · CLOSED** · *AMBER EYES · Criminal psychology through real case files* | — | ⊘ | ◼ |

**Tổng:** 203 rows (198 shots with speech + 4 act cards + 1 end card) · 205 sentences · 33 speech elements (5 acts) · 44 backgrounds. Rebuilt 09/11/2026 for the rewritten script of 09/11/2026 (205 sentences); shot durations measured from the new master mp3 (ASR).
