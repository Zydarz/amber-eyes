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

## 6. DANH SÁCH SHOT — TẬP 05 (dựng lại 05/11/2026 theo kịch bản v4 — 209 câu, 209 câu phủ)

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20.5 s → lời đầu) | — | T1 | `t5_wichita_skyline_dusk` hiện dần từ đen | *第1幕 · 13年の沈黙のあと、再浮上した手紙* | Typewriter clicks & winter wind | ⊘ |  |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t5_wichita_skyline_dusk` | **2004年3月19日** · *ウィチタ市・カンザス州・アメリカ* | Typewriter sound | ✦ Cú |  |
| 1-02 | `1.03#3` | H | T1 | `t5_eagle_newsroom_night` | **VICKI WEGERLEの運転免許証コピー** · *1986年に命を奪われ未解決事件となっていた被害者* | — | 🅑 |  |
| 1-03 | `1.03#4` | H | T1 | `t5_manila_envelope_polaroids` | **署名された3つの頭文字** · “B-T-K” · *数十年にわたりアメリカ中西部を恐怖に陥れた* | — | 🅑 |  |
| 1-04 | `1.03#5` | H | T2 | `t5_btk_signature_letter` | *冷徹な宣言* · **かつて地域を震撼させた連続犯が公式に再び戻った** | Stamp on "B-T-K" | ⊘ |  |
| 1-05 | `1.04` (nghỉ 1.5 s) | — | — | giữ 1-04 | — | — | ⊘ |  |
| 1-06 | `1.05#1`–`#2` | H | T1 | `t5_newspaper_bundle_dawn` | **全米を震撼させたBTK再出現** · *1974年から1991年にかけて10人もの無辜の市民の命を奪う* | Newspaper headline | 🅑 |  |
| 1-07 | `1.05#3`–`#4` | H | T1 | `t5_vintage_typewriter_desk` | **何の痕跡も残さず姿を消した亡霊** · *13年間、新たな事件も書簡も浮上せず* | Typewriter sound | ⊘ |  |
| 1-08 | `1.05#5` | H | T1 | `t5_cold_case_archives` | **ウィチタ警察とFBIの認識** · *犯人は死亡したか、別名で刑務所に服役中のでしょう* | — | ⊘ |  |
| 1-09 | `1.06` (nghỉ 1.5 s) | — | — | giữ 1-08 | — | — | ⊘ |  |
| 1-10 | `1.07#1` | H | T1 | `t5_park_city_suburb` | *心情を思い浮かべてください* · **ウィチタ郊外の静かな町Park Cityの住民** | — | →N1 |  |
| 1-11 | `1.09#1`–`#3` | N1 | T4 lời kể | `t5_park_city_suburb`, `push` | “10年以上を経てBTKが再び手紙を送ってきたと知ったとき、町全体が恐怖で息をのみました。” → `#3`: “人々は銃を買い足し、鍵を取り替え、センサーライトを設置し、日が暮れる前に雨戸を固く閉ざしました。” | Tape recorder click `1.08` | ✦ Cừu |  |
| 1-12 | `1.09#4`–`#5` | N1 | T4 lời kể | `t5_suburban_house_locked` | “全米が捜し求めていた怪物が、毎日近所の芝生の長さを測りに来ていたあの誠実な職員だったとは、夢にも思いませんでした” | — | ⊘ | →H |
| 1-13 | `1.10#1`–`#3` | H | T1 | `t5_compliance_truck_street` | **犯罪捜査史で最も奇妙な逆説** · *犯人は13年もの間、完璧な冬眠状態を維持* → `#3`: *かつての現場の手がかりは完全に冷え切っていた* | — | ✦ Cú |  |
| 1-14 | `1.10#4` | H | T1 | `t5_compliance_truck_street` | **当時の技術では正体を掴めず** · *いかなる手がかりも得られなかった* | — | ✦ Cú |  |
| 1-15 | `1.10#5`–`#7` | H | T1 | `t5_detective_war_room` | **何がその怪物を突き動かし、自ら沈黙を破らせたのか** → `#6`: *なぜあれほど極端に慎重だった捕食者が、自ら光の中へと踏み出たのか* | — | ⊘ |  |
| 1-16 | `1.11` (nghỉ 2 s) | — | — | giữ 1-14, nhạc nền dừng đột ngột | — | Dry clock ticking | ⊘ |  |
| 1-17 | `1.12#1` | H | T1 | `t5_detective_war_room` | *捜査官に事件ファイルを開いていただきましょう* · **歴史的な心理戦の幕開け** | — | →D |  |
| 1-18 | `1.14#1`–`#2` | D | T1 | `t5_detective_war_room`, `still` | **専従班が抱いた最大の疑問** · *「なぜ今なのか」という点* → `#2`: *彼の眠れる衝動を爆発させた心理的引き金が判明* | Drawer opens & dossier placed `1.13` | ✦ Sói |  |
| 1-19 | `1.14#3`–`#5` | D | T1 | `t5_book_manuscript_desk` | **BTK初犯から30年を記念する特集記事** · *弁護士Robert Beattieが死亡説や忘れ去られた存在説を提示* | — | 🅑 |  |
| 1-20 | `1.14#6`–`#7` | D | T1 | `t5_narcissist_mirror_shadow`, `push` | **病的な自尊心への致命的な一撃** · *Dennis Raderは自分が忘れ去られることに耐えられなかった* | — | ⊘ | →H |
| 1-21 | `1.16#1`–`#3` | H | T10 | `t5_amber_eyes_dossier_05` | **紫色のフロッピーディスク & 悪性自己愛** · *Dennis Rader（BTK）事件ファイル* · *10の心理的指標エコシステム* | Mournful cello `1.15` rises | ✦ Cú |  |
| 1-22 | `1.16#4` | H | T10 | `t5_amber_eyes_dossier_05` | **なぜ一枚の紫色のフロッピーディスクが難攻不落の要塞を崩したのか** | Mournful cello `1.15` rises | ✦ Cú |  |
| 1-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | **Dennis Rader 事件ファイル** · *自らBTKを名乗った男* | — | ⊘ | ◼ |
| 2-01 | `2.02#1`–`#2` | H | T1 | `t5_darkened_house_exterior` | **1974年から1991年にかけて彼が残した痕跡** · *極めて特異な手口と心理的署名* | Heartbeat & magnetic tape | ✦ Cú |  |
| 2-02 | `2.02#3`–`#5` | H | T2 | `t5_btk_signature_metaphor` | *自らに付けた呼び名* · **BTK** · *拘束・苦痛・命の破壊を意味する3つの英単語の頭文字* | Stamp on "BTK" | 🅑 | →D |
| 2-03 | `2.04#1`–`#3` | D | T8 | `t5_btk_signature_metaphor`, `still` | *FBI行動科学部 · 心理的署名* · *MOは環境に応じて柔軟に変化する* · *Signatureは内面的な感情を満たすため決して変わらない* | Flipping crime scene photos `2.03` | ✦ Sói |  |
| 2-04 | `2.04#4`–`#5` | D | T1 | `t5_darkened_house_exterior`, `push` | **3つの特徴** · *第1の特徴：無力な被害者を前に絶対的な権力を行使し完全に支配したいという欲求* | — | 🅑 |  |
| 2-05 | `2.04#6`–`#7` | D | T1 | `t5_trophy_lockbox` | **第2の特徴：戦利品『Trophies』の保管** · *一人でいるときに興奮を反芻するため* → `#7`: *第3の特徴：法執行機関やマスメディアを挑発したいという欲求* | — |  |  |
| 2-06 | `2.04#8`–`#9` | D | T1 | `t5_public_library_bookshelves` | **秘密と挑発** · *公共図書館の本の中や公園のゴミ箱に残した小包* → `#9`: *これらの戦利品や挑発状こそが捕食者の異常な精神状態を物語っていた* | — | ⊘ | →H |
| 2-07 | `2.05#1`–`#3` | H | T1 | `t5_gloves_forensic_desk` | **4段階の危険な『妄想のエスカレーション軌道』** · *ある日突然生じたものではない* → `#3`: *第1段階：小動物への虐待と夜間の覗き行為* | — | ✦ Cú | →D |
| 2-08 | `2.05#4`–`#6` | H | T1 | `t5_gloves_forensic_desk` | **4段階の妄想の階段** → `#4`: *第2段階：民家への忍び込みと女性の私的な衣服の収集* → `#5`: *第3段階：明確な標的を定めて住居に侵入* → `#6`: *第4段階：人命を奪い異様な写真を演出する凶行* | — | ✦ Cú | →D |
| 2-09 | `2.05#7` | H | T1 | `t5_gloves_forensic_desk` | **際限なく強い刺激を求め続ける捕食者** · *外部からの決定的な制止がない限り* | — | ✦ Cú | →D |
| 2-10 | `2.06#1`–`#2` | D | T1 | `t5_air_force_service_era` | **DENNIS RADER · 1945年生まれ** · *4年間アメリカ空軍に服役し司法行政学の学位を取得* | — | ✦ Sói |  |
| 2-11 | `2.06#3` | D | T1 | `t5_rader_house_park_city` | **Park City · 6220番地** · *インディペンデンス通り · 妻と2人の子供を育て上げた家長* | — |  |  |
| 2-12 | `2.06#4` | D | T1 | `t5_lutheran_church_exterior` | **キリスト・ルーテル教会の教会評議会議長** · *鍵の管理や財務運営を任されていた* | — |  |  |
| 2-13 | `2.06#5` | D | T1 | `t5_scout_camp_campfire` | **カブスカウトの隊長** · *子供たちに野外技術や正直さを教えていた* | — | ⊘ |  |
| 2-14 | `2.06#6`–`#7` | D | T1 | `t5_compliance_truck_street` | **1991年から市役所の規則遵守指導員** · *見回り・芝生の長さの測定・放し飼いの動物の取り締まり* | — | ⊘ |  |
| 2-15 | `2.06#8` | D | T1 | `t5_compliance_measuring_tape`, `push` | **『ハロー効果』と正常性バイアス** · *30年間にわたり町の目を曇らせる巨大な死角* | Tape measure sound | ⊘ | →H |
| 2-16 | `2.07#1`–`#3` | H | T3 so sánh | `t5_two_faces_silhouette` | *昼間：誠実な地域の番人・模範的な父親* · **夜間：窓の外を徘徊する冷酷な狩人** · *1974年から1988年までADT警備会社に勤務* | Sub-drop on "predator" | ✦ Cú | →C |
| 2-17 | `2.07#4`–`#6` | H | T3 so sánh | `t5_two_faces_silhouette` | *昼間：誠実な地域の番人・模範的な父親* · **夜間：窓の外を徘徊する冷酷な狩人** · *30年以上も破綻せずに共存できたのはなぜ* | Sub-drop on "predator" | ✦ Cú | →C |
| 2-18 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第3幕* · **心理剖検――歪んだ殺人者の脳内** | — | ⊘ | ◼ |
| 3-01 | `3.02#1`–`#3` | C | T2 | `t5_compartmentalization_cabinet` | *第一の防衛機制* · **精神の分断（コンパートメンタライゼーション）** · *認知の引き出しを完全に分離して閉ざす驚異的な能力* | Stamp on "Compartmentalization" | ✦ Cáo |  |
| 3-02 | `3.02#4`–`#6` | C | T1 | `t5_concrete_wall_divide` | **罪悪感や良心の呵責を全く覚えない** · *意識の中で凶行は別の引き出しに隔離されていた* → `#6`: *家族や親族は『正常性の防壁』として利用されていた* | — | 🅑 |  |
| 3-03 | `3.02#7`–`#8` | C | T1 | `t5_factor_x_shadow`, `push` | **妄想的な概念『要因X（Factor X）』** · *自らの内に潜む闇を弁解するために警方への手紙で執拗に繰り返した* | — | ⊘ |  |
| 3-04 | `3.03` (nghỉ 1.5 s) | — | — | giữ 3-03 | **悪性ナルシシズム（Malignant Narcissism）** · *優越性と全能感への病的な執着* | — | ⊘ |  |
| 3-05 | `3.04#1`–`#3` | H | T1 | `t5_factor_x_shadow` | *極めて異様な概念ですね、先生* · **行動科学の観点から『要因X』の正体とは何だったのでしょうか？** | — | ✦ Cú | →C |
| 3-06 | `3.05#1`–`#3` | C | T2 | `t5_projection_mask` | *第二の防衛機制* · **合理化と心理的投射** · *典型的な『道徳的合理化技術』* | Stamp on "Rationalization & Projection" | ✦ Cáo |  |
| 3-07 | `3.05#4`–`#5` | C | T2 | `t5_projection_mask` | *第二の防衛機制* · **合理化と心理的投射** · *『内なる要因Xに強いられたのだ』という詭弁* | Stamp on "Rationalization & Projection" | ✦ Cáo |  |
| 3-08 | `3.05#6`–`#8` | C | T1 | `t5_family_dinner_warmth` | **個人の道徳的責任をきれいに拭い去る** · *恐ろしい悲劇を起こした後も平然と帰宅して夕食を楽しむ* | — | ⊘ | →H |
| 3-09 | `3.06#1`–`#3` | H | T1 | `t5_narcissistic_throne` | **背筋が凍るほど精巧な自己欺瞞** · *Raderが被害者たちに向けていた内面の眼差し* → `#3`: *なぜ悲痛な懇願が同情心すら呼び起こさなかったのか* | — | ✦ Cú | →C |
| 3-10 | `3.06#4` | H | T1 | `t5_narcissistic_throne` | **決定的な瞬間に人間としての温もりを消し去ったもの** | — | ✦ Cú | →C |
| 3-11 | `3.07#1`–`#3` | C | T2 | `t5_narcissistic_throne`, `still` | *次の機制* · **被害者の『客体化（物扱い）』と非人間化** · *悪性自己愛と反社会性人格障害の結合：共感能力の完全な欠如* | Dấu mộc ở "Ái kỷ ác tính" | ✦ Cáo |  |
| 3-12 | `3.07#4`–`#5` | C | T1 | `t5_secret_scrapbook` | **冷たく『プロジェクト』と呼んでいた** → `#5`: *頭の中の加虐的なシナリオを演じるための『生きた小道具』* | — | 🅑 |  |
| 3-13 | `3.07#6`–`#8` | C | T1 | `t5_fear_of_oblivion`, `push` | **被害者の涙や命乞いは哀れみを誘わなかった** · *むしろ全能の支配感を高める感覚的刺激として機能* → `#8`: *人間が小道具に格下げされたとき、凶行は機械のように冷徹に執行される* | Sub-drop ở "Sự lãng quên" | ⊘ | →H |
| 3-14 | `3.08#1`–`#3` | H | T1 | `t5_hubris_chessboard` | **温和な笑顔の裏の、骨の髄まで冷たい無慈悲さ** → `#3`: *何が30年間にわたり自身を守ってきた防壁を自ら破壊させたのか* | — | ✦ Cú |  |
| 3-15 | `3.08#4` | H | T1 | `t5_hubris_chessboard` | **悪性自己愛は自己破滅の種を宿しているのか？** | — | ✦ Cú |  |
| 3-16 | `3.09#1`–`#3` | C | T2 | `t5_narcissistic_throne` | *第三の機制* · **世間の注目への病的な依存と妄想の飢餓** · *大衆の関心と社会的な恐怖は誇大自己を支える酸素* | Stamp on "世間の注目への病的な依存" | ⊘ |  |
| 3-17 | `3.09#4`–`#5` | C | T1 | `t5_fear_of_oblivion` | **自己愛者にとって最も耐えがたい地獄** · *世間からの完全な忘却* | Sub-drop on "世間からの完全な忘却" | 🅑 |  |
| 3-18 | `3.09#6`–`#7` | C | T1 | `t5_secret_scrapbook` | **悪名への渇望** · *忘れ去られるくらいなら危険を冒してでも再び世間を震撼させる道* → `#7`: *悪名への渇望が生存本能と合理的な理性を完全に盲目にした* | — | ⊘ |  |
| 3-19 | `3.10#1`–`#2` | H | T2 | `t5_hubris_chessboard` | *専門家の結論* · **傲慢さ — 捕食者の首を絞める罠** · *自らが全ての捜査陣よりも優秀だと錯覚していた* | Stamp on "傲慢さ" | ✦ Cú |  |
| 3-20 | `3.10#3` | H | T1 | `t5_winter_home_depot` | **司法史上最も信じがたい技術的失策** · *その盲目的な過信がRaderを導いた* | — | ⊘ |  |
| 3-21 | `3.10#4` | H | T1 | `t5_detective_war_room` | *捜査官から振り返っていただきましょう* · **紫色のフロッピーディスクを巡る運命的な心理戦** | — | →D |  |
| 3-22 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第4幕* · **尋問の心理戦＆フロッピーディスクの罠** | — | ⊘ | ◼ |
| 4-01 | `4.02#1`–`#3` | H | T5 ngày | `t5_winter_home_depot` | **2005年初頭** · *メディアへの挑発的な小包を繰り返していたDennis Raderの新たなアイデア* → `#2`: *コンピュータファイルでのやり取りへと手段を更新したい* → `#3`: *59歳のRaderはデジタル技術の根本的な仕組みについて全くの無知* | Tiếng gió đông & quạt server | ✦ Cú |  |
| 4-02 | `4.02#4` | H | T5 ngày | `t5_winter_home_depot` | **2005年1月下旬** · *ウィチタのHome Depot駐車場のピックアップトラックの荷台にシリアル箱を密かに置いた* | Tiếng gió đông & quạt server | ✦ Cú |  |
| 4-03 | `4.02#5` | H | T1 | `t5_cereal_box_pickup` | **シリアル箱の中身** · *捜査官へ宛てた手書きのメモ* | — | 🅑 |  |
| 4-04 | `4.02#6`–`#8` | H | T1 | `t5_handwritten_note_floppy` | **信じられないほど無邪気な質問** · “フロッピーディスクでやり取りしてもコンピュータまで追跡されませんか？ 正直に答えてください” → `#8`: *The Wichita Eagle紙の三行広告欄に暗号で回答を掲載するよう要求* | — | ⊘ | →D |
| 4-05 | `4.02#9` | H | T1 | `t5_handwritten_note_floppy` | **30年間固く閉ざされていた城壁についに亀裂** | — | ⊘ | →D |
| 4-06 | `4.04#1`–`#3` | D | T2 | `t5_newspaper_classified_494` | *30年ぶりの決定機* · **そのメモがKen Landwehr警部の机に置かれたとき、部屋全体が息をのみました** · *直ちに一流のデジタル鑑識専門家に助言を求めた* | Lật báo giấy `4.03` | ✦ Sói |  |
| 4-07 | `4.04#4`–`#6` | D | T2 | `t5_newspaper_classified_494` | *The Wichita Eagle紙の広告欄* · “レックス、送っても大丈夫だ” → `#6`: *自分が状況を支配しているという錯覚に溺れ、警察の言葉を信じ込んだ* | Lật báo giấy `4.03` | ✦ Sói |  |
| 4-08 | `4.04#7`–`#8` | D | T1 | `t5_ksas_tv_station` | **2005年2月中旬** · *書類に包まれた1.44メガバイトの紫色Memorex製フロッピーディスク* | — | 🅑 |  |
| 4-09 | `4.04#9` | D | T1 | `t5_purple_floppy_disk`, `push` | **私たちが仕掛けた技術的な罠が完全に作動** | Tiếng nạp đĩa mềm `4.05` | ⊘ | →H |
| 4-10 | `4.06#1`–`#2` | H | T1 | `t5_digital_forensics_lab` | **デジタル鑑識室** · *鑑識専門家のRandy Stoneがディスクの磁気セクタを精密に復元* | Tiếng gõ phím vi tính | ✦ Cú |  |
| 4-11 | `4.06#3`–`#5` | H | T8 | `t5_metadata_screen` | *隠されたメタデータが開かれた* · *TestA.rtfファイルほかに過去に削除されたWordファイルを復元* → `#5`: *モニター上に決定的な2行のデータがはっきりと表示* | Sub-drop ở Metadata | ⊘ |  |
| 4-12 | `4.06#6`–`#7` | H | T8 | `t5_metadata_screen` | *1行目には『最終更新者：Dennis』* · *2行目には『登録団体：キリスト・ルーテル教会』* | Sub-drop ở Metadata | ⊘ |  |
| 4-13 | `4.07` (nghỉ 2 s) | — | — | giữ 4-08, nhạc nền dừng đột ngột | **CHRIST LUTHERAN CHURCH** · *削除された文書に残された教会名* | Nền quạt server vo ve | ⊘ |  |
| 4-14 | `4.08#1`–`#3` | D | T1 | `t5_church_website_search` | **検索キーワード：キリスト・ルーテル教会 ウィチタ Dennis** · *教会評議会の会長はまさにDennis Raderだった* | — | ✦ Sói |  |
| 4-15 | `4.08#4`–`#6` | D | T1 | `t5_traffic_camera_pickup` | **Home Depot駐車場の防犯カメラと完全一致** · *娘が大学の診療所に残していた生体組織検体を令状で確保* | — | 🅑 |  |
| 4-16 | `4.08#7`–`#9` | D | T2 | `t5_dna_pap_smear_vial` | *DNA鑑定の結果は決定的* · **明白な父子関係** · *もはや何の疑いもありません* | Dấu mộc ở "Khẳng định 100%" | ⊘ | →H |
| 4-17 | `4.08#10` | D | T2 | `t5_dna_pap_smear_vial` | *捜査員たちによる包囲* · **Park Cityの自宅を完全包囲** | Dấu mộc ở "Khẳng định 100%" | ⊘ | →H |
| 4-18 | `4.10#1`–`#3` | H | T1 | `t5_highway_takedown_arrest`, `push` | **2005年2月25日の昼** · *パトカーが前後から遮断したピックアップトラック* | Còi xe cảnh sát & phanh `4.09` | ✦ Cú | →D |
| 4-19 | `4.10#4`–`#6` | H | T1 | `t5_highway_takedown_arrest`, `push` | **傲慢な仮面は粉々に砕け散った** · *全能の幻影を奪われて動揺する哀れな自己愛患者* | Còi xe cảnh sát & phanh `4.09` | ✦ Cú | →D |
| 4-20 | `4.12#1`–`#3` | D | T1 | `t5_interrogation_confrontation` | **取調室の古典的な対決** · “なぜフロッピーについて私に嘘をついたのですか” → `#3`: “あなたを逮捕するためです” | Cửa sắt đóng sầm `4.11` | ✦ Sói |  |
| 4-21 | `4.12#4`–`#5` | D | T1 | `t5_interrogation_confrontation` | **『自己愛の完全崩壊』** · *罠に落ち正体が暴かれたことを悟る* | Cửa sắt đóng sầm `4.11` | ✦ Sói |  |
| 4-22 | `4.12#6`–`#8` | D | T1 | `t5_shattered_mask_confession`, `push` | **仮面は完全に剥がれ落ちた** · *10件の凶行を長時間をかけて自供* | — | ⊘ | →H |
| 4-23 | `4.14#1`–`#3` | H | T1 | `t5_kerri_rawson_tears` | *その痛切な告白をお聞きください* · **KERRI RAWSON — DENNIS RADERの実の娘** | Điểm nhấn stinger `4.13` | ✦ Cú | →N2 |
| 4-24 | `4.15#1`–`#3` | N2 | T4 lời kể | `t5_kerri_rawson_tears`, `still` | “世界は父を怪物と見なしていますが、私にとっては最も模範的な父親でした。” → `#3`: “FBI特別捜査官がドアを叩き、父がBTKだと告げられた瞬間、足元の世界が完全に崩れ去りました。” | Tiếng bật cassette `4.15#1` | ✦ Kerri |  |
| 4-25 | `4.15#4`–`#6` | N2 | T4 lời kể | `t5_kerri_rawson_tears`, `still` | “最大の苦痛は単なる恐怖ではなく、信じていた絆の完全な裏切りでした。” → `#5`: “毎晩おやすみのキスをしてくれた優しい父親が、数多くの家庭を破壊した悪魔だったという真実をどう受け止めればいいのでしょうか？” | Tiếng bật cassette `4.15#1` | ✦ Kerri |  |
| 4-26 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第5幕* · **判決、赤い警報の教訓＆終幕** | — | ⊘ | ◼ |
| 5-01 | `5.02#1`–`#3` | H | T5 ngày | `t5_sedgwick_courtroom` | **2005年8月18日** · *セジウィック郡地方裁判所 · Gregory Waller判事* | Tiếng búa tòa án gõ 3 tiếng `5.01` | ✦ Cú |  |
| 5-02 | `5.02#4` | H | T1 | `t5_judge_gavel_verdict`, `push` | **『病的な自己憐憫』** · *遺族への真摯な悔悟を一切示さず* | Sub-drop ở "175 năm" | ⊘ |  |
| 5-03 | `5.02#5`–`#7` | H | T1 | `t5_el_dorado_prison` | **El Dorado刑務所の独房** · *社会から完全に隔離され最期まで永遠の沈黙と向き合う* | — | ⊘ |  |
| 5-04 | `5.03` (nghỉ 1.5 s) | — | — | giữ 5-03 | — | — | ⊘ |  |
| 5-05 | `5.04#1`–`#3` | H | T1 | `t5_solitary_confinement_cell` | **30年の時を経て幕を閉じたBTK事件** · *いかなる電子的痕跡も完全に消し去ることはできない* | — | ✦ Cú | →C+D |
| 5-06 | `5.04#4` | H | T1 | `t5_solitary_confinement_cell` | **生存のための4つの赤い警告** · *日常の中で悪の仮面を見抜くため* | — | ✦ Cú | →C+D |
| 5-07 | `5.05#1`–`#3` | C | T9 `1/4` | `t5_redflag_rule_control` | **第1の信号：極端なルール統制への執着** · *些細な規則に異常に執着し他人を威圧・処罰しようとする人物* | — | ✦ Cáo |  |
| 5-08 | `5.05#4` | C | T9 `1/4` | `t5_redflag_rule_control` | *第一の危険信号* · **抑圧された支配欲が暴力的な形で噴出する機会を待つ** | — | ✦ Cáo |  |
| 5-09 | `5.05#5`–`#7` | C | T9 `2/4` | `t5_redflag_shallow_affect` | **第2の信号：社交的な外面の裏にある感情的な断絶** · *浅薄な情動（Shallow Affect）* | — | 🅑 | →D |
| 5-10 | `5.06#1`–`#3` | D | T9 `3/4` | `t5_redflag_secret_trophies` | **第3の信号：他人の私物を戦利品のように密かに収集する習癖** · *私物や身分証、私的な記念品を隠し持つ* | — | ✦ Sói |  |
| 5-11 | `5.06#4`–`#6` | D | T9 `4/4` | `t5_redflag_narcissistic_hubris` | **第4の信号：どんな代償を払ってでも認められ賞賛されたい渇望** · *巨大な自己肯定感の欠落* | — | 🅑 |  |
| 5-12 | `5.06#7` | D | T9 `4/4` | `t5_redflag_narcissistic_hubris` | *最後の危険信号* · **自尊心を刺激されれば自ら隙を晒して自滅への道をたどる** | — | 🅑 |  |
| 5-13 | `5.07` (nghỉ 2 s) | — | — | giữ 5-09, Piano dâng lên nhẹ nhàng | **番組を共にしてくれた専門家と捜査官に感謝します** | Piano ấm áp | ⊘ |  |
| 5-14 | `5.08#1`–`#3` | H | T1 | `t5_justice_dawn_sunlight` | **悪が持つ必然的な自滅の法則** · *自らの内的自己愛の怪物だけは決して欺くことができなかった* | — | ✦ Cú |  |
| 5-15 | `5.08#4`–`#6` | H | T1 | `t5_justice_dawn_sunlight` | **目覚めた警戒心** · *日常の安全の境界を守るため* | — | ✦ Cú |  |
| 5-16 | `5.08#7` | H | T1 | `t5_justice_dawn_sunlight` | **専門家とリスナーの皆さまに深く感謝申し上げます** | — | ✦ Cú |  |
| 5-17 | `5.09` (nghỉ 1.5 s) | — | — | giữ 5-11 | — | — | ⊘ |  |
| 5-18 | `5.10#1`–`#2` | H | T1 | `t5_closing_typewriter_rose` | **常に心の平安を保ち、自らを守り、日々の平穏を大切にする** | Folder closes `5.11` | ✦ Cú |  |
| 5-19 | `5.10#3` | H | T1 | `t5_closing_typewriter_rose`, `still` | **次回の犯罪心理分析ファイルでお会いしましょう** · *安らかな夜をお過ごしください* | Decisive typewriter strike | 🅑 |  |
| 5-20 | hết tập (10 s) | — | T1 | `t5_closing_typewriter_rose` | **事件記録 第05話 · 終了** · *AMBER EYES · 実際の事件記録から読み解く犯罪心理学* | Cello sustains 5s then fades out `5.12` | ⊘ | ◼ |

**Tổng: 96 shot** (Hồi 1: 24 shot · Hồi 2: 18 shot · Hồi 3: 22 shot · Hồi 4: 26 shot · Hồi 5: 20 shot) · Phủ 100% 209/209 câu · chữ trên hình lấy từ câu đang đọc (H6).

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


