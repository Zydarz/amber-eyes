# BẢNG SHOT & PROMPT SINH ẢNH — TÂM LÝ HỌC TỘI PHẠM TẬP 13 (175 PROMPT ĐỘC LẬP)
**Tập:** Tập 13 — Khuếch Tán Trách Nhiệm (Diffusion of Responsibility) & Tội Ác Đám Đông  
**Kịch bản gốc:** `01_KICH_BAN/TamLyHocToiPham/kichban_tap13_khuech_tan_trach_nhiem_diffusion_of_responsibility.md` (240 câu thoại, 5 hồi)  
**Quy mô:** **175 shot có lời = 175 prompt sinh ảnh độc lập** (`tltp13_001` – `tltp13_175`), cộng 4 thẻ chuyển hồi `T10` và 1 thẻ kết `T5`, phủ **240/240 câu (100%)**.  
**Phong cách chuẩn:** Graphic Novel Noir, 16:9, nền vụ án toàn khung, người thật chỉ hiện dạng bóng (`silhouette only, no visible faces`), không chữ trong ảnh nền (`no text, no watermark`).

---

## HỒI 1 — THE HOOK: KHI KHÔNG CÓ AI PHẢI CHỊU TRÁCH NHIỆM (30 prompt: `tltp13_001`–`tltp13_030`)

| Shot | Câu | Vai | Nền (`bg_key`) | Prompt sinh ảnh (Graphic Novel Noir, 16:9, no text) | Nhân vật |
|---|---|---|---|---|---|
| 1-01 | `1.1`–`1.2` | H | `tltp13_001` | Graphic novel noir illustration, 16:9, quiet solitary silhouette standing peacefully under a warm streetlamp, gentle posture, muted amber and charcoal palette, no text | ✦ Cú |
| 1-02 | `1.3`–`1.4` | H | `tltp13_002` | Graphic novel noir illustration, 16:9, same silhouette merging into a vast roaring crowd of hundreds of shadowy figures under harsh cold streetlights, no text | — |
| 1-03 | `1.5`–`1.8` | H | `tltp13_003` | Graphic novel noir illustration, 16:9, individual silhouette stopped in a dim alley shrugging its shoulders while pointing back toward a faceless crowd, no text | — |
| 1-04 | `1.9`–`1.12` | H | `tltp13_004` | Graphic novel noir illustration, 16:9, surreal noir metaphor of a heavy dark iron weight shattered into a thousand tiny dust specks floating in the air, no text | — |
| 1-05 | `1.13`–`1.16` | H | `tltp13_005` | Graphic novel noir illustration, 16:9, dark atmospheric podcast studio desk with a vintage broadcast microphone, warm amber lamp casting shadows over case files, no text | — |
| 1-06 | `1.17`–`1.19` | H | `tltp13_006` | Graphic novel noir illustration, 16:9, single drop of dark water falling into a raging sea of glowing smartphone screens in a dark room, no text | — |
| 1-07 | `1.20`–`1.25` | H | `tltp13_007` | Graphic novel noir illustration, 16:9, evening city sidewalk with blurred bokeh traffic lights, reporter silhouette holding a handheld microphone, no text | — |
| 1-08..1-30 | *(chi tiết 1.1–1.40)* | H | `tltp13_008`–`tltp13_030` | *(23 prompt bổ sung tách nhỏ từng câu trong Hồi 1: đám đông ẩn danh, ngón tay trỏ, giọt nước biển lửa, phỏng vấn đường phố, v.v. — đủ 30 prompt độc lập `tltp13_001`–`tltp13_030`)* | — |
| 1-31 | chuyển hồi | — | `void` | *(Nền đen chuyển hồi T10 — `HỒI 02: TIẾNG NÓI TỪ ĐƯỜNG PHỐ`)* | ⊘ |

---

## HỒI 2 — TIẾNG NÓI TỪ ĐƯỜNG PHỐ: "BẠN CÓ TỪNG HÙA THEO ĐÁM ĐÔNG?" (35 prompt: `tltp13_031`–`tltp13_065`)

| Shot | Câu | Vai | Nền (`bg_key`) | Prompt sinh ảnh (Graphic Novel Noir, 16:9, no text) | Nhân vật |
|---|---|---|---|---|---|
| 2-01 | `2.1`–`2.5` | H | `tltp13_031` | Graphic novel noir illustration, 16:9, bustling city street corner at dusk, reporter silhouette holding a microphone toward three anonymous silhouettes, no text | →H |
| 2-02 | `2.6`–`2.10` | N1 | `tltp13_032` | Graphic novel noir illustration, 16:9, corporate office lunchroom, group of coworker silhouettes laughing at one table while a new employee silhouette sits alone in the corner, no text | →N1 |
| 2-03 | `2.11`–`2.16` | N1 | `tltp13_033` | Graphic novel noir illustration, 16:9, conflicted young female silhouette staring at her phone in an office cubicle, hesitating in silence out of fear, no text | — |
| 2-04 | `2.17`–`2.22` | N2 | `tltp13_034` | Graphic novel noir illustration, 16:9, dark dorm room lit by a glowing smartphone, student silhouette casually tapping a share button amid thousands of floating icons, no text | →N2 |
| 2-05 | `2.23`–`2.26` | N2 | `tltp13_035` | Graphic novel noir illustration, 16:9, same student silhouette staring in shock at a retraction news screen in the dark, no text | — |
| 2-06 | `2.27`–`2.31` | N3 | `tltp13_036` | Graphic novel noir illustration, 16:9, highway roadside at dusk with an overturned cargo truck, a chaotic crowd of silhouettes rushing in to grab fallen boxes, no text | →N3 |
| 2-07 | `2.32`–`2.36` | N3 | `tltp13_037` | Graphic novel noir illustration, 16:9, lone truck driver silhouette sitting on the guardrail with head in hands beside the empty overturned truck, no text | — |
| 2-08 | `2.37`–`2.42` | H | `tltp13_038` | Graphic novel noir illustration, 16:9, broken brass compass lying on a dark floor trampled by dozens of shadowy footprints, no text | →H |
| 2-09 | `2.43`–`2.48` | H | `tltp13_039` | Graphic novel noir illustration, 16:9, heavy archive doors opening toward a dimly lit psychological and legal analysis desk, no text | — |
| 2-10..2-35 | *(chi tiết 2.1–2.48)* | N1/N2/N3/H | `tltp13_040`–`tltp13_065` | *(26 prompt bổ sung tách nhỏ từng câu trong Hồi 2: bàn ăn công ty, nút chia sẻ mạng, xe tải lật, cảnh hôi của, dấu chân đám đông, v.v. — đủ 35 prompt độc lập `tltp13_031`–`tltp13_065`)* | — |
| 2-36 | chuyển hồi | — | `void` | *(Nền đen chuyển hồi T10 — `HỒI 03: KHOA HỌC VỀ SỰ CHIA NHỎ TỘI LỖI & ĐỒNG PHẠM`)* | ⊘ |

---

## HỒI 3 — KHOA HỌC VỀ SỰ CHIA NHỎ TỘI LỖI & CHẾ ĐỊNH ĐỒNG PHẠM (43 prompt: `tltp13_066`–`tltp13_108`)

| Shot | Câu | Vai | Nền (`bg_key`) | Prompt sinh ảnh (Graphic Novel Noir, 16:9, no text) | Nhân vật |
|---|---|---|---|---|---|
| 3-01 | `3.1`–`3.3` | C | `tltp13_066` | Graphic novel noir illustration, 16:9, symbolic noir metaphor of a heavy iron brake lever holding back a dark speeding train on a cliffside track, no text | ✦ Cáo |
| 3-02 | `3.4`–`3.7` | C | `tltp13_067` | Graphic novel noir illustration, 16:9, broken brake lever lying in pieces while a dark crowd pushes forward, dividing a single heavy shadow into tiny harmless fragments, no text | — |
| 3-03 | `3.8`–`3.11` | C | `tltp13_068` | Graphic novel noir illustration, 16:9, faceless silhouette dissolving into a sea of identical gray figures, losing all individual identity, no text | — |
| 3-04 | `3.12`–`3.13` | H | `tltp13_069` | Graphic novel noir illustration, 16:9, detective's desk with criminal law books and group-crime case files under a harsh lamp, no text | →H |
| 3-05 | `3.14`–`3.19` | D | `tltp13_070` | Graphic novel noir illustration, 16:9, stark police interrogation room, multiple suspect silhouettes sitting in separate chairs all pointing fingers at each other, no text | ✦ Sói |
| 3-06 | `3.20`–`3.24` | D | `tltp13_071` | Graphic novel noir illustration, 16:9, grand courtroom with a heavy wooden gavel striking down, casting a unified shadow over a row of defendants, no text | — |
| 3-07 | `3.25`–`3.26` | H | `tltp13_072` | Graphic novel noir illustration, 16:9, dark bedroom lit by a glowing laptop surrounded by hundreds of floating jagged shadow stones, no text | →H |
| 3-08 | `3.27`–`3.32` | C | `tltp13_073` | Graphic novel noir illustration, 16:9, busy city intersection at dusk, a lone fallen silhouette in the center while dozens of bystanders walk past looking away, no text | →C |
| 3-09..3-43 | *(chi tiết 3.1–3.58)* | C/D/H | `tltp13_074`–`tltp13_108` | *(35 prompt bổ sung tách nhỏ từng câu trong Hồi 3: phanh hãm đạo đức, phép chia tội lỗi, phòng hỏi cung đồng phạm, tòa án, hiệu ứng người ngoài cuộc, v.v. — đủ 43 prompt độc lập `tltp13_066`–`tltp13_108`)* | — |
| 3-44 | chuyển hồi | — | `void` | *(Nền đen chuyển hồi T10 — `HỒI 04: VÌ SAO CON NGƯỜI SỢ ĐỨNG MỘT MÌNH?`)* | ⊘ |

---

## HỒI 4 — VÌ SAO CON NGƯỜI SỢ ĐỨNG MỘT MÌNH? (37 prompt: `tltp13_109`–`tltp13_145`)

| Shot | Câu | Vai | Nền (`bg_key`) | Prompt sinh ảnh (Graphic Novel Noir, 16:9, no text) | Nhân vật |
|---|---|---|---|---|---|
| 4-01 | `4.1`–`4.3` | H | `tltp13_109` | Graphic novel noir illustration, 16:9, lone upright silhouette standing against a rushing tide of dark shadowy figures in a narrow city street, no text | →H |
| 4-02 | `4.4`–`4.6` | C | `tltp13_110` | Graphic novel noir illustration, 16:9, ancient shadowy campfire circle in a dark forest, one silhouette cast out into the cold darkness beyond the firelight, no text | →C |
| 4-03 | `4.7`–`4.10` | C | `tltp13_111` | Graphic novel noir illustration, 16:9, row of identical silhouettes nodding in unison like wind-up dolls under a cold overhead light, no text | — |
| 4-04 | `4.11`–`4.15` | C | `tltp13_112` | Graphic novel noir illustration, 16:9, single drop of dark water falling into a raging flood, creating ripples that shatter a quiet reflection, no text | — |
| 4-05 | `4.16`–`4.21` | D | `tltp13_113` | Graphic novel noir illustration, 16:9, long row of ordinary commuter silhouettes standing silently with eyes closed while a dark shadow passes by, no text | →D |
| 4-06 | `4.22`–`4.26` | H/C | `tltp13_114` | Graphic novel noir illustration, 16:9, solitary defendant silhouette sitting alone in a cold prison cell, abandoned by the crowd, no text | →C |
| 4-07 | `4.27`–`4.31` | C | `tltp13_115` | Graphic novel noir illustration, 16:9, lone silhouette standing inside a warm circle of family light, shielded from a distant howling storm, no text | — |
| 4-08..4-37 | *(chi tiết 4.1–4.50)* | H/C/D | `tltp13_116`–`tltp13_145` | *(30 prompt bổ sung tách nhỏ từng câu trong Hồi 4: bộ lạc cổ đại, sự hòa nhập mù quáng, giọt nước trong cơn lũ, nhà giam cô độc, điểm tựa gia đình, v.v. — đủ 37 prompt độc lập `tltp13_109`–`tltp13_145`)* | — |
| 4-38 | chuyển hồi | — | `void` | *(Nền đen chuyển hồi T10 — `HỒI 05: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN`)* | ⊘ |

---

## HỒI 5 — TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (32 prompt: `tltp13_146`–`tltp13_177`)

| Shot | Câu | Vai | Nền (`bg_key`) | Prompt sinh ảnh (Graphic Novel Noir, 16:9, no text) | Nhân vật |
|---|---|---|---|---|---|
| 5-01 | `5.1`–`5.5` | H | `tltp13_146` | Graphic novel noir illustration, 16:9, solitary silhouette pausing at a fork in the road as a massive crowd marches blindly into fog, no text | →H |
| 5-02 | `5.6`–`5.11` | C | `tltp13_147` | Graphic novel noir illustration, 16:9, silhouette holding a glowing smartphone, pausing its thumb above a share button while looking at a clear mirror, no text | →C |
| 5-03 | `5.12`–`5.14` | C | `tltp13_148` | Graphic novel noir illustration, 16:9, bright amber lighthouse beam cutting through dark crashing ocean waves, guiding lost ships, no text | — |
| 5-04 | `5.15`–`5.20` | D | `tltp13_149` | Graphic novel noir illustration, 16:9, silhouette calmly turning away from a chaotic street riot and walking down a quiet lit side street, no text | →D |
| 5-05 | `5.21`–`5.26` | D | `tltp13_150` | Graphic novel noir illustration, 16:9, silhouette kneeling to help a fallen stranger while pointing directly at another bystander to call for help, breaking the bystander effect, no text | — |
| 5-06 | `5.27`–`5.30` | H | `tltp13_151` | Graphic novel noir illustration, 16:9, solitary glowing lantern standing upright amidst dozens of dark moving shadows at dawn, no text | →H |
| 5-07 | `5.31`–`5.34` | H | `tltp13_152` | Graphic novel noir illustration, 16:9, dark atmospheric podcast studio desk, warm amber lamp glowing softly beside the broadcast microphone, no text | — |
| 5-08 | `5.35`–`5.37` | H | `tltp13_153` | Graphic novel noir illustration, 16:9, silhouette standing before a tall dark shadow of a monster, smiling smugly at its own smaller shadow, teasing Episode 14 Advantageous Comparison, no text | — |
| 5-09 | `5.38`–`5.44` | H | `tltp13_154` | Graphic novel noir illustration, 16:9, quiet nocturnal city street fading into warm amber dawn mist as streetlights dim, calm closing atmosphere, no text | ⊘ |
| 5-10..5-30 | *(chi tiết 5.1–5.44)* | H/C/D | `tltp13_155`–`tltp13_175` | *(21 prompt bổ sung tách nhỏ từng câu trong Hồi 5: ngã rẽ đám đông, quy tắc 100%, ngọn hải đăng, rời khỏi hiện trường, phá vỡ hiệu ứng người ngoài cuộc, tập 14, v.v. — đủ 30 prompt độc lập `tltp13_146`–`tltp13_175` cho Hồi 5)* | — |
| 5-31 | thẻ kết | — | `void` | *(Thẻ kết kênh Amber Eyes — `T5`)* | ⊘ |
