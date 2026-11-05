# 制作計画 エピソード05 · 日本語版 · 「紫色のフロッピーディスク」 (PART B)

**適用基準:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A)  
**台本:** `01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md` · **出力先:** `02_SAN_XUAT/Tap05_JA/xuat_ban/`  
**固定テキスト・カード:** `02_SAN_XUAT/Tap05_JA/CHU_CO_DINH_JA.md`  
**日付:** 2026年11月4日

---

## B1. エピソード情報

| 項目 | 内容 |
|---|---|
| 台本 | `01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md` — 58 elements · 164 sentences |
| 音声マスター | `02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA_master.mp3` (1471.43 s · -16.28 LUFS · TP -2.00 dBFS) |
| 配役 (日本語版) | H: 梟 (フクロウ) · D: 狼 (オオカミ) · C: 狐 (キツネ) · N1: 羊 (ヒツジ) · N2: 猫 (ネコ) |
| N1 / N2 | `1.09` パークシティ住民 (ヒツジ) / `4.15` ケリー・ローソン - デニス・レイダーの娘 (ネコ) |
| 映像構造 | 全83ショット — 音声70ショット + 間奏・休止13ショット |
| 幕タイトル | 第1幕: 13年の沈黙を破る手紙 · 第2幕: 犯罪現場と心理的署名 · 第3幕: 心理剖検――歪んだ自己愛の内面 · 第4幕: 尋問とデジタル証拠の罠 · 第5幕: 判決、赤い警報と終幕 |
| 背景アセット | 61枚の専用 `t5_*` ノワール背景 (2112×1188 16:9 2K) + `void` |
| YouTube分類 | 教育 · 子ども向けではない · 「合成または加工されたコンテンツ」 · 犯罪心理学・法医学分析 |

---

## B2. 視覚規則 & アラインメント (日本語版)

- **V5 — 実在人物は完全な影/シルエットのみ:** (`t5_compliance_truck_street`, `t5_detective_war_room`, `t5_interrogation_confrontation`, `t5_two_faces_silhouette`). 実在人物の顔貌は一切露出させない。
- **被害者の描写ゼロ:** 被害者の姿はシルエットであっても描写しない。
- **V9 — 犯罪心理学および法医学・デジタルフォレンジックへの焦点:** 暴力的・グロテスクな描写は排除し、心理分析とフロッピーディスクのメタデータ解析に焦点を当てる。
- **H5 — AIテキスト生成禁止:** 画面上のすべての文字はPillowで正確な日本語フォントを用いて描画する。
- **H6/V3 — 読み上げ文と100%一致する画面テキスト:** 画面上の日本語テキストは読み上げ音声の正確な語句と一致させる。
- **H12 — 必須の終幕カード:** `*事件記録 第05話 · 終了*` + `**AMBER EYES**` + `*実際の事件記録から読み解く犯罪心理学*`。
- **H13 — 3方向同期 (映像 — テキスト — 音声):** 全83ショットにおいて1対1の完全同期を達成。

<!--TABLE-->

## 6. DANH SÁCH SHOT — TẬP 05

**Guide:** *Role* = speaker (H Owl · D Wolf · C Fox · N1 Sheep · N2 Cat). Table specifies **background + graphics**; badges & busts placed automatically.  
*Characters*: `🅑` = bust beyond first sentence · `→X` = Host invites X · `✦` = first appearance · `⊘` = bust disabled.  
Last column: blank = dissolve · ✂ cut · ◼ black.

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.  
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.  
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### CHANNEL INTRO · 0.00–22.41 s · `bgm_music_box.mp3`

Place `assets/brand/intro_kenh_JA_t05.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.


Place `assets/brand/intro_kenh_JA_t05.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.

### ACT 1 — 13年の沈黙のあと、再浮上した手紙 · Lead background `t5_wichita_skyline_dusk`


| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20.5 s → lời đầu) | — | T1 | `t5_wichita_skyline_dusk` hiện dần từ đen | *第1幕 · 13年の沈黙のあと、再浮上した手紙* | Typewriter clicks & winter wind | ⊘ |  |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t5_wichita_skyline_dusk` | **2004年3月19日** · *カンザス州ウィシタ市* | Typewriter sound | ✦ Cú |  |
| 1-02 | `1.03#3` | H | T1 | `t5_eagle_newsroom_night` | **THE WICHITA EAGLE 編集局** · *差出人住所のない封筒* | — | 🅑 |  |
| 1-03 | `1.03#4` | H | T1 | `t5_manila_envelope_polaroids` | **VICKI WEGERLE の運転免許証コピー** · *現場写真3枚* | — | 🅑 |  |
| 1-04 | `1.03#5` | H | T2 | `t5_btk_signature_letter` | *中西部全域を覆った恐怖* · **署名：B-T-K** | Stamp on "B-T-K" | ⊘ |  |
| 1-05 | `1.04` (nghỉ 1.5 s) | — | — | giữ 1-04 | — | — | ⊘ |  |
| 1-06 | `1.05#1`–`#2` | H | T1 | `t5_newspaper_bundle_dawn` | **全米を揺るがせたニュース** · *1974年から1991年まで* | Newspaper headline | 🅑 |  |
| 1-07 | `1.05#3`–`#4` | H | T1 | `t5_vintage_typewriter_desk` | **痕跡を残さず消えた幽霊** · *13年間の沈黙* | Typewriter sound | ⊘ |  |
| 1-08 | `1.05#5` | H | T1 | `t5_cold_case_archives` | **ウィシタ警察とFBIの記録** · *死亡または服役と推測* | — | ⊘ |  |
| 1-09 | `1.06` (nghỉ 1.5 s) | — | — | giữ 1-08 | — | — | ⊘ |  |
| 1-10 | `1.07#1` | H | T1 | `t5_park_city_suburb` | *ウィシタ郊外の静かな町* · **パークシティの住民の話** | — | →N1 |  |
| 1-11 | `1.09#1`–`#2` | N1 | T4 lời kể | `t5_park_city_suburb`, `push` | “町中全体が恐怖で息を詰まらせました。” → “人々は窓を点検し、ドアを施錠しました。” | Tape recorder click `1.08` | ✦ Cừu |  |
| 1-12 | `1.09#3` | N1 | T4 lời kể | `t5_suburban_house_locked` | “毎日草刈りをしていた男だったとは誰も予想しませんでした。” | — | ⊘ | →H |
| 1-13 | `1.10#1`–`#4` | H | T1 | `t5_compliance_truck_street` | **司法史における奇異な逆説** · *13年間眠り続けていた* → *当時の科学と技術は無力だった* | — | ✦ Cú |  |
| 1-14 | `1.10#5`–`#7` | H | T1 | `t5_detective_war_room` | *尊敬される市民として生き抜くこともできた* · **なぜ自ら罠へ足を踏み入れたのか** | — | ⊘ |  |
| 1-15 | `1.11` (nghỉ 2 s) | — | — | giữ 1-14, nhạc nền dừng đột ngột | — | Dry clock ticking | ⊘ |  |
| 1-16 | `1.12#1` | H | T1 | `t5_detective_war_room` | *歴史的な頭脳戦の始まり* · **事件を直接指揮した捜査官の話** | — | →D |  |
| 1-17 | `1.14#1`–`#2` | D | T1 | `t5_detective_war_room`, `still` | **捜査班の最初の問い** · *なぜ今なのか？* | Drawer opens & dossier placed `1.13` | ✦ Sói |  |
| 1-18 | `1.14#3`–`#5` | D | T1 | `t5_book_manuscript_desk` | **30周年記念の一連の記事** · *事件に関する書籍の出版発表* | — | 🅑 |  |
| 1-19 | `1.14#6`–`#7` | D | T1 | `t5_narcissist_mirror_shadow`, `push` | *致命的な弱点* · **病的な自愛心を貫く一撃** | — | ⊘ | →H |
| 1-20 | `1.16#1`–`#3` | H | T10 | `t5_amber_eyes_dossier_05` | **忘れられることを受け入れられなかった** · *怪物は今も生きていると誇示する* | Mournful cello `1.15` rises | ✦ Cú |  |
| 1-21 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | **Dennis Rader 事件ファイル** · *自らBTKを名乗った男* | — | ⊘ | ◼ |

### ACT 2 — 犯罪現場＆事件ファイル――二面獣の心理的署名 · Lead background `t5_btk_signature_letter`


| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `t5_darkened_house_exterior` | **1974年 · 最初の事件** · *手紙による挑発的メッセージ* | Heartbeat & magnetic tape | ✦ Cú |  |
| 2-02 | `2.02#3`–`#4` | H | T2 | `t5_btk_signature_metaphor` | *自ら作った頭文字* · **B-T-K** | Stamp on "BTK" | 🅑 | →D |
| 2-03 | `2.04#1`–`#3` | D | T8 | `t5_btk_signature_metaphor`, `still` | **犯行の手口（MO）** · *侵入し、遂行し、逃走する* | Flipping crime scene photos `2.03` | ✦ Sói |  |
| 2-04 | `2.04#4`–`#5` | D | T1 | `t5_darkened_house_exterior`, `push` | *心理的署名（Signature）* · **感情面のニーズを満たす行為** | — | 🅑 |  |
| 2-05 | `2.04#6`–`#8` | D | T1 | `t5_trophy_lockbox` | **記念品（Trophy）の略奪** · *運転免許証や所持品を持ち去る* | — |  |  |
| 2-06 | `2.04#9`–`#10` | D | T1 | `t5_public_library_bookshelves` | *記念品を何度も取り出して眺める* · **暗黒の幻想を追体験する** | — | ⊘ | →H |
| 2-07 | `2.05#1`–`#4` | H | T1 | `t5_gloves_forensic_desk` | **極めて狡猾な手口** · *入念な計画と現場の隠蔽* | — | ✦ Cú | →D |
| 2-08 | `2.06#1` | D | T1 | `t5_air_force_service_era` | *指紋や痕跡を残さなかった* · **30年間にわたり捜査を阻んだ壁** | — | ✦ Sói |  |
| 2-09 | `2.06#2` | D | T1 | `t5_rader_house_park_city` | **昼の世界のDennis Rader** · *良き夫、二人の子供の父親* | — |  |  |
| 2-10 | `2.06#3` | D | T1 | `t5_lutheran_church_exterior` | **キリスト教ルーテル教会協議会の議長** · *ボーイスカウトの隊長* | — |  |  |
| 2-11 | `2.06#4` | D | T1 | `t5_scout_camp_campfire` | **パークシティの法令遵守調査員** · *草の高さや犬の鎖を厳格に取り締まる* | — | ⊘ |  |
| 2-12 | `2.06#5`–`#6` | D | T1 | `t5_compliance_truck_street` | *隣人たちの記憶* · **規則に異常なほど厳格な男** | — | ⊘ |  |
| 2-13 | `2.06#7` | D | T1 | `t5_compliance_measuring_tape`, `push` | *二重生活の仮面* · **誰も裏の顔に気づかなかった** | Tape measure sound | ⊘ | →H |
| 2-14 | `2.07#1`–`#4` | H | T3 so sánh | `t5_two_faces_silhouette` | *昼の顔* · **模範市民 · 敬虔な信者 · 手本となる父親** → *夜の顔* · **命を奪う冷酷な捕食者** | Sub-drop on "predator" | ✦ Cú | →C |
| 2-15 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第3幕* · **心理剖検――歪んだ殺人者の脳内** | — | ⊘ | ◼ |

### ACT 3 — 心理剖検――歪んだ殺人者の脳内 · Lead background `t5_narcissist_mirror_shadow`


| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1`–`#3` | C | T2 | `t5_compartmentalization_cabinet` | **心理専門家の分析** · *悪性ナルシシズムと精神の分断* | Stamp on "Compartmentalization" | ✦ Cáo |  |
| 3-02 | `3.02#4`–`#5` | C | T1 | `t5_concrete_wall_divide` | **精神の分断（Compartmentalization）** · *人格を切り離す防衛機制* | — | 🅑 |  |
| 3-03 | `3.02#6`–`#7` | C | T1 | `t5_factor_x_shadow`, `push` | *日常生活と暗黒の衝動* · **罪悪感を感じることなく共存させる** | — | ⊘ |  |
| 3-04 | `3.03` (nghỉ 1.5 s) | — | — | giữ 3-03 | **悪性ナルシシズム（Malignant Narcissism）** · *優越性と全能感への病的な執着* | — | ⊘ |  |
| 3-05 | `3.04#1`–`#3` | H | T1 | `t5_factor_x_shadow` | *共感性の完全な欠如* · **他者を自らの道具とみなす** | — | ✦ Cú | →C |
| 3-06 | `3.05#1`–`#3` | C | T2 | `t5_projection_mask` | *典型的な防御機構* · **投影と合理化 · RATIONALIZATION & PROJECTION** · *“X Factor”* | Stamp on "Rationalization & Projection" | ✦ Cáo |  |
| 3-07 | `3.05#4`–`#5` | C | T1 | `t5_family_dinner_warmth` | **注目の依存症（Addiction to Attention）** · *世間からの注目こそが最高の報酬* | — | ⊘ | →H |
| 3-08 | `3.06#1`–`#3` | H | T1 | `t5_narcissistic_throne` | *13年間の沈黙の苦痛* · **忘れ去られることへの恐怖** | — | ✦ Cú | →C |
| 3-09 | `3.07#1`–`#2` | C | T2 | `t5_narcissistic_throne`, `still` | **本の出版予告という引き金** · *BTKは死んだという推測への反発* | Dấu mộc ở "Ái kỷ ác tính" | ✦ Cáo |  |
| 3-10 | `3.07#3`–`#4` | C | T1 | `t5_secret_scrapbook` | *自らの存在を誇示するため* · **怪物は再び姿を現した** | — | 🅑 |  |
| 3-11 | `3.07#5`–`#7` | C | T1 | `t5_fear_of_oblivion`, `push` | **ナルシシストの最大の恐怖：忘却** · *無名の公務員として死ぬより捕まる危険を選ぶ* | Sub-drop ở "Sự lãng quên" | ⊘ | →H |
| 3-12 | `3.08#1`–`#3` | H | T1 | `t5_hubris_chessboard` | **注目への渇望が生んだ盲点** · *歴史的なフォレンジックの罠へ* | — | ✦ Cú |  |
| 3-13 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第4幕* · **尋問の心理戦＆フロッピーディスクの罠** | — | ⊘ | ◼ |

### ACT 4 — 尋問の心理戦＆フロッピーディスク技術の罠 · Lead background `t5_interrogation_room`


| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1`–`#4` | H | T5 ngày | `t5_winter_home_depot` | **2004年から2005年** · *メディアや警察へ送られた一連の通信* | Tiếng gió đông & quạt server | ✦ Cú |  |
| 4-02 | `4.02#5` | H | T1 | `t5_cereal_box_pickup` | **警察の捜査戦略** · *殺人犯の傲慢さと虚栄心を利用する* | — | 🅑 |  |
| 4-03 | `4.02#6`–`#9` | H | T1 | `t5_handwritten_note_floppy` | *手紙での奇妙な質問* · **フロッピーディスクは追跡可能か？** | — | ⊘ | →D |
| 4-04 | `4.04#1`–`#5` | D | T2 | `t5_newspaper_classified_494` | **捜査班の決断** · *新聞広告を通じた偽りの回答* | Lật báo giấy `4.03` | ✦ Sói |  |
| 4-05 | `4.04#6`–`#7` | D | T1 | `t5_ksas_tv_station` | **“フロッピーディスクは安全で追跡できない”** · *新聞の告知欄* | — | 🅑 |  |
| 4-06 | `4.04#8` | D | T1 | `t5_purple_floppy_disk`, `push` | *罠にかかったDennis Rader* · **紫色のフロッピーディスクの送付** | Tiếng nạp đĩa mềm `4.05` | ⊘ | →H |
| 4-07 | `4.06#1`–`#2` | H | T1 | `t5_digital_forensics_lab` | **警察デジタルフォレンジック研究室** · *専門家 Randy Stone がディスク情報を詳細にスキャン* | Tiếng gõ phím vi tính | ✦ Cú |  |
| 4-08 | `4.06#3`–`#6` | H | T8 | `t5_metadata_screen` | **デジタルフォレンジック捜査** · *ディスク内メタデータの解析* | Sub-drop ở Metadata | ⊘ |  |
| 4-09 | `4.07` (nghỉ 2 s) | — | — | giữ 4-08, nhạc nền dừng đột ngột | **CHRIST LUTHERAN CHURCH** · *削除された文書に残された教会名* | Nền quạt server vo ve | ⊘ |  |
| 4-10 | `4.08#1`–`#3` | D | T1 | `t5_church_website_search` | **最後の修正者：DENNIS** · *教会のウェブサイトに記載された議長名* | — | ✦ Sói |  |
| 4-11 | `4.08#4`–`#5` | D | T1 | `t5_traffic_camera_pickup` | *30年間の捜査の突破口* · **容疑者Dennis Raderの特定** | — | 🅑 |  |
| 4-12 | `4.08#6`–`#9` | D | T2 | `t5_dna_pap_smear_vial` | **DNA採取と科学鑑定** · *現場のDNAとの完全な一致* | Dấu mộc ở "Khẳng định 100%" | ⊘ | →H |
| 4-13 | `4.10#1`–`#4` | H | T1 | `t5_highway_takedown_arrest`, `push` | **2005年2月25日 · 逮捕** · *自宅近くの路上で身柄を拘束* | Còi xe cảnh sát & phanh `4.09` | ✦ Cú | →D |
| 4-14 | `4.12#1`–`#4` | D | T1 | `t5_interrogation_confrontation` | *尋問室での驚愕* · **“なぜ警察は嘘をついたのか？”** | Cửa sắt đóng sầm `4.11` | ✦ Sói |  |
| 4-15 | `4.12#5`–`#8` | D | T1 | `t5_shattered_mask_confession`, `push` | *家族の悲痛な証言* · **父親の二重生活に直面した娘** | — | ⊘ | →H |
| 4-16 | `4.14#1`–`#2` | H | T1 | `t5_kerri_rawson_tears` | *悲痛な証言* · **KERRI RAWSON — DENNIS RADERの娘** | Điểm nhấn stinger `4.13` | ✦ Cú | →N2 |
| 4-17 | `4.15#1`–`#4` | N2 | T4 lời kể | `t5_kerri_rawson_tears`, `still` | “世間は彼を怪物として知っています…しかし私にとって、彼はかつて素晴らしい父親でした…” | Tiếng bật cassette `4.15#1` | ✦ Kerri |  |
| 4-18 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第5幕* · **判決、赤い警報の教訓＆終幕** | — | ⊘ | ◼ |

### ACT 5 — 判決、赤い警報の教訓＆終幕 · Lead background `t5_courtroom_sentencing`


| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1`–`#2` | H | T5 ngày | `t5_sedgwick_courtroom` | **法廷での詳細な自白** · *淡々と語られた犯行の記録* | Tiếng búa tòa án gõ 3 tiếng `5.01` | ✦ Cú |  |
| 5-02 | `5.02#3` | H | T1 | `t5_judge_gavel_verdict`, `push` | *感情の揺らぎのない冷酷さ* · **自らの行為を誇るかのような語り口** | Sub-drop ở "175 năm" | ⊘ |  |
| 5-03 | `5.02#4`–`#5` | H | T1 | `t5_el_dorado_prison` | **判決：10回の終身刑** · *最低175年間の仮釈放なし* | — | ⊘ |  |
| 5-04 | `5.03` (nghỉ 1.5 s) | — | — | giữ 5-03 | — | — | ⊘ |  |
| 5-05 | `5.04#1`–`#2` | H | T1 | `t5_solitary_confinement_cell` | **日常生活における4つの赤い警告** · *完璧な仮面の裏に潜む悪質自己愛人格の見分け方* | — | ✦ Cú | →C+D |
| 5-06 | `5.05#1`–`#3` | C | T9 `1/4` | `t5_redflag_rule_control` | **第1の兆候：ルールと支配への異常な執着** · *他者を服従させるための病的な厳格さ* | — | ✦ Cáo |  |
| 5-07 | `5.05#4`–`#5` | C | T9 `2/4` | `t5_redflag_shallow_affect` | **第2の兆候：温かい外見の裏にある感情の欠如** · *社会生活に紛れ込む共感性の完全な欠如* | — | 🅑 | →D |
| 5-08 | `5.06#1`–`#2` | D | T9 `3/4` | `t5_redflag_secret_trophies` | **第3の兆候：他人の物品を密かに保管する習慣** · *戦利品として他人の私物を隠し持つ危険な兆候* | — | ✦ Sói |  |
| 5-09 | `5.06#3`–`#5` | D | T9 `4/4` | `t5_redflag_narcissistic_hubris` | **第4の兆候：認められたいと渇望する自己愛的な欲求** · *脆い自我と名声への抑えきれない渇望* | — | 🅑 |  |
| 5-10 | `5.07` (nghỉ 2 s) | — | — | giữ 5-09, Piano dâng lên nhẹ nhàng | **番組を共にしてくれた専門家と捜査官に感謝します** | Piano ấm áp | ⊘ |  |
| 5-11 | `5.08#1`–`#5` | H | T1 | `t5_justice_dawn_sunlight` | **闇は常に真実の光の前に頭を下げざるを得ません** · *Dennis Raderの事件記録が残した因果律の教訓* | — | ✦ Cú |  |
| 5-12 | `5.09` (nghỉ 1.5 s) | — | — | giữ 5-11 | — | — | ⊘ |  |
| 5-13 | `5.10#1`–`#2` | H | T1 | `t5_closing_typewriter_rose` | **専門家・調査員・リスナーの皆様に深く感謝いたします** | Folder closes `5.11` | ✦ Cú |  |
| 5-14 | `5.10#3` | H | T1 | `t5_closing_typewriter_rose`, `still` | **次回の犯罪心理分析ファイルでお会いしましょう** → `#3`: *常に警戒を怠らず、善意ある心を* | Decisive typewriter strike | 🅑 |  |
| 5-15 | hết tập (10 s) | — | T1 | `t5_closing_typewriter_rose` | **事件記録 第05話 · 終了** · *AMBER EYES · 実際の事件記録から読み解く犯罪心理学* | Cello sustains 5s then fades out `5.12` | ⊘ | ◼ |

**Tổng: 83 shot** (Hồi 1: 22 shot · Hồi 2: 15 shot · Hồi 3: 13 shot · Hồi 4: 18 shot · Hồi 5: 15 shot) · Phủ 100% 164/164 câu · 100% nền có file.

---

## APPENDIX A (Episode 05 EN) — SCRIPT TURNS & SENTENCES BREAKDOWN

- Total Elements: 58 (33 speech turns, 11 BGM/SFX beats, 14 pauses/transitions).
- Total Sentences: 164.
- Roles: Host (H) 48.2% · Investigator (D) 32.9% · Psychologist (C) 14.6% · Park City Resident (N1) 1.8% · Kerri Rawson (N2) 2.5%.

---

## APPENDIX B (Episode 05 EN) — FACT-CHECKING & V9 COMPLIANCE

- Fact-checking: 100% verified against public court records (State of Kansas v. Dennis L. Rader), Sedgwick County District Court transcripts, and Wichita Police Department archives.
- V9 content safety: Strictly non-violent educational documentary format compliant with YouTube US monetization policies.

---

## 7. Báo cáo Sản xuất Audio Higgs & Đánh giá Chất lượng (02/11/2026)

### 7.1. Cấu hình & Giọng mẫu VoxCPM2
- **Engine TTS:** Higgs Audio v3 (chạy local trên Mac mini M2 qua MLX).
- **Bộ giọng mẫu VoxCPM2 EN (Bộ A EN):**
  - **Host (H · Cú):** `English_magnetic_voiced_man` (tốc độ 0.95, F0 trung vị $112.1\text{ Hz}$).
  - **Điều tra viên (D · Sói):** `English_Trustworth_Man` (tốc độ 0.97, F0 trung vị $84.2\text{ Hz}$).
  - **Chuyên gia tâm lý (C · Cáo):** `English_Wiselady` (tốc độ 0.95, F0 trung vị $189.0\text{ Hz}$).
  - **Nhân chứng (N1 · Cừu):** `English_SentimentalLady` (tốc độ 0.95, F0 trung vị $164.4\text{ Hz}$).
  - **Khách mời (N2 · Mèo):** `English_captivating_female1` (tốc độ 0.95, F0 trung vị $221.2\text{ Hz}$).

### 7.2. Tách bạch cao độ (Quy tắc G9)
- **D → H:** $12 \times \log_2(112.1 / 84.2) = 4.96\text{ nửa cung}$ (ĐẠT $\ge 4.0\text{ nc}$).
- **H → C:** $12 \times \log_2(189.0 / 112.1) = 9.03\text{ nửa cung}$ (ĐẠT $\ge 4.0\text{ nc}$).
- **D → C:** $12 \times \log_2(189.0 / 84.2) = 13.99\text{ nửa cung}$ (ĐẠT $\ge 4.0\text{ nc}$).
- **H → N1:** $12 \times \log_2(164.4 / 112.1) = 6.62\text{ nửa cung}$ (ĐẠT $\ge 4.0\text{ nc}$).

### 7.3. Đánh giá chất lượng bằng Whisper CER & UTMOSv2 MOS
- **Tổng số câu đo:** 164 câu.
- **Whisper CER:**
  - Trung bình: **1.04%** · Trung vị: **0.00%**.
  - Số câu CER $> 2\%$: **24/164 câu** (chủ yếu do tên riêng "Rader" $\to$ "Raider", "Rawson" $\to$ "Rossin" hoặc định dạng ngày tháng `19th` $\to$ `19`).
- **UTMOSv2 MOS (Thang điểm tự nhiên 1.0 – 5.0):**
  - Toàn tập: Trung bình **3.37 / 5.0** (Min: 2.11, Max: 4.09).
  - Vai C (Chuyên gia): Trung bình **3.68** (3.31 – 4.03).
  - Vai H (Host): Trung bình **3.49** (2.92 – 4.09).
  - Vai N1 (Nhân chứng): Trung bình **3.34** (2.84 – 3.77).
  - Vai D (Điều tra viên): Trung bình **3.10** (2.11 – 3.53).
  - Vai N2 (Kerri Rawson): Trung bình **2.90** (2.62 – 3.36).

### 7.4. Mốc thời gian & Phụ đề
- **Tổng thời lượng:** **1272.50 s** (~21 phút 12 giây).
- **Intro kênh:** 0.00 – 22.41 s (`bgm_music_box.mp3`).
- **Lời đầu:** 23.00 s (`1.03#1` Host).
- **Lời cuối:** 1263.50 s (`5.10#3` Host).
- **Thẻ kết (Closing card):** 1263.50 – 1272.50 s (9.0 s fade out).
- **Phân bổ hồi:** H1 23.0–273.6s, H2 275.6–506.2s, H3 508.2–715.1s, H4 717.1–1045.9s, H5 1047.9–1263.5s.
- **File Timeline:** `.work/timeline_s_EN_t05.json`.
- **File Phụ đề:** `02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN.srt` (356 cue).
- **File Danh sách nghe kiểm tra:** `02_SAN_XUAT/Tap05_EN/CanNghe_Tap05_EN_higgs.md`.

### 7.5. Master Audio (03/11/2026)
- **File Master:** `02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp3` (29 MB).
- **Integrated Loudness:** **-16.3 LUFS** (đạt chuẩn -16 ± 1 LUFS).
- **True Peak:** **-1.9 dBFS** (đạt chuẩn $\le -1.5\text{ dBFS}$).
- **LRA (Loudness Range):** 3.6 LU.
- **Kiểm tra khoảng câm (Rule A1 / V4 @ -60dB):** **0 lỗi**.
- **Hiệu ứng & Tiếng động:** Đủ 10 đoạn môi trường (ambience) + 18 hiệu ứng tiếng động (SFX) khớp kịch bản.


