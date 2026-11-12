# HỒ SƠ SẢN XUẤT TẬP 09 · "NGHỆ THUẬT XÓA BỎ BẢN NGÃ" — 日本語版

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **第09話: 自我を消滅させる芸術** |
| Vụ án | Hồ sơ Charles Manson & Thảm kịch Gia đình Manson (Los Angeles, California, Hoa Kỳ, 1969) |
| Chủ đề | Cơ chế tẩy não 3 giai đoạn (Unfreezing – Changing – Refreezing), Bạo lực & thao túng tâm lý bầy đàn |
| Tổng thời lượng | **1721.43 s (~28 phút 41 giây)** · 5 hồi · **199 câu thoại** · **196 shot** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Cư dân LA) · N2 (Linda Kasabian) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design JA** (H: `H_JA.wav`, D: `D_JA.wav`, C: `C_JA.wav`, N1: `N1_JA.wav`, N2: `N2_JA.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap09.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap09_JA/xuat_ban/Tap09_JA_master.mp4` & `02_SAN_XUAT/Tap09_JA/xuat_ban/Tap09_JA.mp4` |

---

## B2. Số đo Kiểm soát Chất lượng Audio & Video (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **-16.28 LUFS** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **-2.05 dBFS** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** **4.50**
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.14 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng video xuất bản:** 1721.43 s (khớp audio 1721.45 s, $\Delta = 0.017\text{ s} \le 0.05\text{ s}$ — ĐẠT ✅ H14)

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Video & Thumbnail:**
   - MP4 Master: [`02_SAN_XUAT/Tap09_JA/xuat_ban/Tap09_JA_master.mp4`](xuat_ban/Tap09_JA_master.mp4) (653.4 MB)
   - MP4 Kênh: [`02_SAN_XUAT/Tap09_JA/xuat_ban/Tap09_JA.mp4`](xuat_ban/Tap09_JA.mp4) (653.4 MB)
   - Thumbnail: [`02_SAN_XUAT/Tap09_JA/xuat_ban/thumbnail.png`](xuat_ban/thumbnail.png) (1.40 MB)
2. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap09_JA/xuat_ban/Tap09_JA_master.mp3`](xuat_ban/Tap09_JA_master.mp3) (55.1 MB)
   - WAV: [`02_SAN_XUAT/Tap09_JA/xuat_ban/Tap09_JA_master.wav`](xuat_ban/Tap09_JA_master.wav) (330.5 MB)
3. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_JA_t09.json`](../../.work/timeline_s_JA_t09.json) (1721.45 s)
   - Bảng shot: [`.work/shots_JA_t09.json`](../../.work/shots_JA_t09.json) (196 shots)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap09_JA/xuat_ban/Tap09_JA.srt`](xuat_ban/Tap09_JA.srt) (412 cues)

---

---

---

## 6. DANH SÁCH SHOT — TẬP 09 (JA)

**表の読み方:** *Vai* = 話者 (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo)。表は **背景 + グラフィック** を表す。バッジと半身像は A5.4 に従う。
*キャラクター* 列: `✦` = 初登場 · `→X` = 次のショットの話者 · `⊘` = 半身像を消す。
最終列: 空欄 = ディゾルブ · `✂` = カット · `◼` = フェードアウト。
*文字* 列 = そのショットの台本の一文を **そのまま** (A7/V3/H6): 40 文字以上 ⇒ *斜体*、40 文字未満 ⇒ **太字**。

### チャンネル・イントロ · 0.00–22.41 s

`assets/brand/intro_kenh_JA.mov` を 0.00 s に置く (A5.7)。イントロに台詞は無い。

### 第01幕 — 愛の夏と1969年8月8日の夜

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-01 | `1.02#1` (6.1 s) | H | T1 | `t9_summer_of_love_hippie_la`, `pan` | *「1960年代後半のアメリカは、ヒッピームーブメントの熱狂的な高揚感に包まれていました。* | — | ✦ Cú |  |
| 1-02 | `1.02#2` (6.6 s) | H | T1 | `t9_summer_of_love_hippie_la`, `pull` | *何十万人もの若者たちが全米各地からカリフォルニアへと押し寄せ、『愛の夏（Summer of Love）』に身を投じました。* | — | — |  |
| 1-03 | `1.02#3` (6.1 s) | H | T1 | `t9_acoustic_guitar_flower_crown`, `still` | **彼らは髪に花を飾り、偏見のない自由な世界を共に夢見ていました。** | — | — |  |
| 1-04 | `1.02#4` (8.4 s) | H | T1 | `t9_los_angeles_skyline_1969`, `push` | *当時の若者の目には、ロサンゼルスの輝く黄金色の陽射しこそが、魂の覚醒と精神的解放の象徴に映っていたのです。* | — | — |  |
| 1-05 | `1.02#5` (9.4 s) | H | T1 | `t9_withered_flower_on_asphalt`, `pan` | *しかし彼らは、その純真な時代が恐ろしい悪夢によって永遠に幕を下ろそうとしているとは、夢にも思っていませんでした。」* | — | — |  |
| 1-06 | `1.04#1` (5.8 s) | H | T1 | `t9_confiscated_clocks_broken_mirror`, `pull` | **「その純真でロマンチックな光景は、ある運命の夏の夜、無残にも砕け散りました。** | — | — |  |
| 1-07 | `1.04#2` (10.3 s) | H | T1 | `t9_cielo_drive_estate_night`, `still` | *1969年8月8日の夜から9日の未明にかけて、10050 Cielo Driveに建つ豪華な邸宅に想像を絶する暗黒が襲いかかりました。* | — | — |  |
| 1-08 | `1.04#3` (6.3 s) | H | T1 | `t9_beverly_hills_gate_road`, `push` | *その家は、きらびやかなBeverly Hillsに近い人里離れた丘の上にひっそりと佇んでいました。* | — | — |  |
| 1-09 | `1.04#4` (7.5 s) | H | T1 | `t9_cielo_drive_living_room_somber`, `pan` | *名匠Roman Polanski監督が借りていたその邸宅は、極めて冷酷な集団暴行の現場と化してしまったのです。* | — | — |  |
| 1-10 | `1.04#5`–`#6` (10.9 s) | H | T1 | `t9_broken_porcelain_doll_desert`, `pull` | **何の罪もない5人の命が、瞬く間に奪われました。** → `#6`: *被害者の中には、妊娠ほぼ9ヶ月だった監督の若き妻であり、美しい女優のSharon Tateが含まれていました。* | — | — |  |
| 1-11 | `1.04#7` (4.8 s) | H | T1 | `t9_redflag2_severed_family_photos`, `still` | **さらに彼女の親しい4人の友人たちも、同様に命を奪われたのです。」** | — | — |  |
| 1-12 | `1.06#1` (9.1 s) | H | T1 | `t9_waverly_drive_residence_night`, `push` | *「それからわずか24時間足らずの後、Los Feliz地区の3301 Waverly Driveで、極めて類似した悲劇が再び繰り返されました。* | — | — |  |
| 1-13 | `1.06#2` (6.7 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `pan` | *実業家のLeno LaBiancaとその妻Rosemaryが、自宅のリビングで無残にも命を奪われたのです。* | — | — |  |
| 1-14 | `1.06#3` (8.0 s) | H | T1 | `t9_newspaper_headline_helter_skelter`, `pull` | *無実の家庭を標的にした無慈悲な連続襲撃は、南カリフォルニア全域の安全神話を完全に打ち砕きました。* | — | — |  |
| 1-15 | `1.06#4` (6.0 s) | H | T1 | `t9_los_angeles_skyline_1969`, `still` | *それは、アメリカの都市史上かつてない集団的偏執病の恐ろしい幕開けとなったのです。* | — | — |  |
| 1-16 | `1.06#5` (5.8 s) | H | T1 | `t9_retro_radio_broadcast_table`, `push` | *あの暗闇に満ちた日々を直接生き抜いた、あるロサンゼルス住民の悲痛な声をお聞きください。」* | — | →N1 |  |
| 1-17 | `1.07#1` (9.3 s) | N1 | T4 lời kể | `t9_retro_radio_broadcast_table`, `pan` | *「あの朝、ラジオがSharon Tateの邸宅で起きた惨劇を繰り返し報じたとき、ロサンゼルスの街全体が恐怖で麻痺してしまいました。* | — | ✦ Cừu |  |
| 1-18 | `1.07#2` (5.4 s) | N1 | T4 lời kể | `t9_waverly_drive_residence_night`, `pull` | **日が暮れると、誰も玄関のドアから一歩も外に出ようとはしませんでした。** | — | — |  |
| 1-19 | `1.07#3` (10.3 s) | N1 | T4 lời kể | `t9_gun_shop_empty_shelves`, `still` | *人々は銃を買い求め、窓の鍵を補強し、防犯用の番犬を探し回ったため、金物屋の棚からは防犯用品が一瞬で消え去りました。* | — | — |  |
| 1-20 | `1.07#4` (7.5 s) | N1 | T4 lời kể | `t9_intact_valuables_diorama`, `push` | *最も恐ろしかったのは、侵入者たちの動機が金品や高価な宝飾品を奪うことではなかったという点です。* | — | — |  |
| 1-21 | `1.07#5` (4.3 s) | N1 | T4 lời kể | `t9_intact_valuables_diorama`, `pan` | **邸宅内の高価な財産には、一切手が付けられていませんでした。** | — | — |  |
| 1-22 | `1.07#6`–`#7` (9.0 s) | N1 | T4 lời kể | `t9_vacant_eyes_doll_shadow`, `pull` | **それはあまりにも無意味で、無差別で、冷酷な残虐性そのものでした。** → `#7`: **私たちの『愛の夏』は、まさにあの夜に息絶えたのです。」** | — | →H |  |
| 1-23 | `1.09#1`–`#2` (8.8 s) | H | T1 | `t9_lapd_investigation_room`, `still` | **「双方の現場には、極めて異様で不気味な痕跡が残されていました。** → `#2`: **一般的な強盗や窃盗の形跡はまったく見当たりませんでした。** | — | — |  |
| 1-24 | `1.09#3` (14.2 s) | H | T1 | `t9_bloody_letters_forensic_wall`, `push` | *しかし壁やドアには、犯行グループによって『PIG』、『RISE』、そしてスペルを誤った一文字『HEALTER SKELTER』という不気味な言葉が殴り書きされていたのです。* | — | — |  |
| 1-25 | `1.09#4` (7.8 s) | H | T1 | `t9_invisible_puppet_master_shadow`, `pan` | *全米は言葉を失い、これほど非人間的な蛮行を駆り立てた真の動機とは一体何だったのかと問いかけました。」* | — | →D |  |
| 1-26 | `1.10#1` (8.3 s) | D | T1 | `t9_lapd_investigation_room`, `pull` | *「事件発生からの数週間、ロサンゼルス市警察は答えのない迷宮の前で完全に立ち往生していました。* | — | ✦ Sói |  |
| 1-27 | `1.10#2` (8.0 s) | D | T1 | `t9_beverly_hills_gate_road`, `still` | *女優Sharon Tateの家族と、LaBianca夫妻との間には、個人的な繋がりなど一切存在しなかったからです。* | — | — |  |
| 1-28 | `1.10#3` (6.2 s) | D | T1 | `t9_los_angeles_county_crime_map`, `push` | *2つの現場は何十キロも離れており、被害者たちの社会的立場もまったく異なっていました。* | — | — |  |
| 1-29 | `1.10#4` (7.4 s) | D | T1 | `t9_bloody_letters_forensic_wall`, `pan` | *それにもかかわらず、現場に残された状況設定は、まったく同一の不気味なサインを示していたのです。* | — | — |  |
| 1-30 | `1.10#5` (7.0 s) | D | T1 | `t9_dark_triad_psychological_symbol`, `pull` | *科学捜査の観点から、私たちは実行犯が個人的な怨恨で行動したのではないと見抜きました。* | — | — |  |
| 1-31 | `1.10#6` (7.4 s) | D | T1 | `t9_invisible_puppet_master_shadow`, `still` | *彼らは影の黒幕によって遠隔操作された、不気味な劇場の台本を実行しているかのように見えたのです。* | — | — |  |
| 1-32 | `1.10#7` (4.2 s) | D | T1 | `t9_intact_valuables_diorama`, `push` | **それは一般的な侵入犯の突発的な凶行ではありませんでした。** | — | — |  |
| 1-33 | `1.10#8` (3.3 s) | D | T1 | `t9_shadow_devil_dialogue_noir`, `pan` | **狂信的な命令を冷徹に実行した結果だったのです。」** | — | →H |  |
| 1-34 | `1.12#1`–`#2` (13.3 s) | H | T1 | `t9_summer_of_love_hippie_la`, `pull` | **「Amber Eyesへようこそ。** → `#2`: *本日私たちは、20世紀の犯罪心理学において最も戦慄的で難解な記録の1つ、Charles Mansonとマンソン・ファミリーの悲劇の扉を開きます。* | — | — |  |
| 1-35 | `1.12#3` (8.6 s) | H | T1 | `t9_prison_cell_bars_shadow`, `still` | *生涯の半分以上を刑務所で過ごした一人の放浪者が、いかにしてエリートの若者たちを良心なき破壊の道具へと変貌させたのか。* | — | — |  |
| 1-36 | `1.12#4` (9.4 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `push` | *そして、自己愛性パーソナリティ障害者が振るう自我解体の技術が、いかにして集団全体を操り人形に仕立て上げたのかを解き明かしていきます。」* | — | — |  |
| 1-37 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *第02幕* · **マansonファミリーとスパン・ランチ** | — | ⊘ | ◼ |

### 第02幕 — マンソンファミリーとスパン・ランチ

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1` (8.0 s) | H | T1 | `t9_midnight_convoy_old_ford`, `pull` | *「悪夢の連鎖の糸を引く影を突き止めるため、捜査陣は華やかなハリウッドの邸宅街を遠く離れることになりました。* | — | — |  |
| 2-02 | `2.02#2` (4.6 s) | H | T1 | `t9_spahn_ranch_western_facade`, `still` | *彼らは荒涼としたSanta Susana Valleyの奥地へと足を踏み入れました。* | — | — |  |
| 2-03 | `2.02#3` (4.1 s) | H | T1 | `t9_spahn_ranch_western_facade`, `push` | **向かった先は、Chatsworth郊外に位置するSpahn Ranchでした。** | — | — |  |
| 2-04 | `2.02#4` (6.1 s) | H | T1 | `t9_spahn_ranch_dilapidated_porch`, `pan` | *そこは、前世紀の西部劇映画の撮影に使われていた、朽ち果てた古いロケ用のセットでした。* | — | — |  |
| 2-05 | `2.02#5` (9.8 s) | H | T1 | `t9_gate_of_spahn_ranch_departure`, `pull` | *腐食した木造の小屋と乾いた土埃の中で、数十人の若者からなる奇妙な集団が、社会から完全に孤立して暮らしていたのです。」* | — | →D |  |
| 2-06 | `2.04#1` (6.1 s) | D | T1 | `t9_haight_ashbury_psychedelic_street`, `still` | *「彼らは自らを『ファミリー（The Manson Family）』という、一見すると温かみのある呼称で呼び合っていました。* | — | — |  |
| 2-07 | `2.04#2` (6.8 s) | D | T1 | `t9_manson_shadow_campfire_desert`, `push` | *牧場において絶対的な権力を握り君臨していたのが、Charles Milles Mansonでした。* | — | — |  |
| 2-08 | `2.04#3` (8.2 s) | D | T1 | `t9_manson_shadow_campfire_desert`, `pan` | *彼は小柄な体躯でありながら、まるで催眠術のように鋭く冷徹な眼光を持つ34歳の男でした。* | — | — |  |
| 2-09 | `2.04#4` (7.5 s) | D | T1 | `t9_dark_triad_psychological_symbol`, `pull` | *身元調査の結果、Mansonは高潔な指導者でも啓発的な哲学者でもないことが判明しました。* | — | — |  |
| 2-10 | `2.04#5` (9.2 s) | D | T1 | `t9_prison_cell_bars_shadow`, `still` | *少年院や連邦刑務所の冷たい格子の中で、人生の半分以上を過ごしてきた根っからの常習犯罪者だったのです。* | — | — |  |
| 2-11 | `2.04#6` (7.5 s) | D | T1 | `t9_gun_shop_empty_shelves`, `push` | *彼の前科記録は、窃盗、小切手偽造、売春斡旋といった罪で埋め尽くされていました。」* | — | →H |  |
| 2-12 | `2.05#1` (8.8 s) | H | T1 | `t9_haight_ashbury_psychedelic_street`, `pan` | *「1967年3月に釈放されたMansonは、サンフランシスコのHaight-Ashburyにおけるヒッピームーブメントの中心地に直接足を踏み入れました。* | — | — |  |
| 2-13 | `2.05#2` (11.5 s) | H | T1 | `t9_acoustic_guitar_flower_crown`, `pull` | *自由な愛と若者の純真さを賛美する反体制文化を目の当たりにしたMansonは、流浪の導師という『ハロー効果』を最大限に利用して捕食者の本性を覆い隠しました。* | — | — |  |
| 2-14 | `2.05#3` (9.4 s) | H | T1 | `t9_acoustic_guitar_flower_crown`, `still` | *アコースティックギターを手に自由を謳う歌を口ずさみ、反抗期や自己同一性の危機に苦しむ若者たちを急速に惹きつけていったのです。* | — | — |  |
| 2-15 | `2.05#4` (5.4 s) | H | T1 | `t9_gate_of_spahn_ranch_departure`, `push` | *彼は若者たちをSpahn Ranchへと連れ去り、閉鎖的な世界を築き上げました。* | — | — |  |
| 2-16 | `2.05#5` (7.2 s) | H | T1 | `t9_apocalyptic_desert_hideout`, `pan` | *そこで彼は、『Helter Skelter』と名付けた狂気じみた終末論を、彼らの心へと植え付け始めたのです。」* | — | →D |  |
| 2-17 | `2.06#1` (13.3 s) | D | T1 | `t9_invisible_puppet_master_shadow`, `pull` | *「諜報活動と証拠の照合を通じて、私たちはMansonの犯罪が突発的に発生したのではなく、5つの明確な段階からなる行動のエスカレーション軌道をたどっていたことを突き止めました。* | — | — |  |
| 2-18 | `2.06#2`–`#3` (10.1 s) | D | T1 | `t9_runaway_teenager_bus_stop`, `still` | **第1段階: 少年非行と欺瞞。** → `#3`: *Mansonは何十年にもわたる刑務所生活を通じて、心理操作と病的な虚言の技術を洗練させました。* | — | — |  |
| 2-19 | `2.06#4` (4.1 s) | D | T1 | `t9_trauma_bonding_group_shadows`, `push` | **第2段階: カルトの形成と精神的支配。** | — | — |  |
| 2-20 | `2.06#5` (10.5 s) | D | T1 | `t9_lsd_hallucinogen_distorted_reality`, `pan` | *Spahn Ranchにおいて大量の幻覚剤LSDと集団的儀式を用い、若い信者たちの人格構造を解体しました。* | — | — |  |
| 2-21 | `2.06#6` (4.7 s) | D | T1 | `t9_confiscated_clocks_broken_mirror`, `pull` | **第3段階: 夜間侵入ゲーム『Creepy Crawling』。** | — | — |  |
| 2-22 | `2.06#7` (11.9 s) | D | T1 | `t9_midnight_convoy_old_ford`, `still` | *Mansonは夜中に信者たちを率いて民家に忍び込ませ、物品を盗むのではなく家具の配置をずらすことで、全能感と不可視の支配力を実験させました。* | — | — |  |
| 2-23 | `2.06#8` (4.5 s) | D | T1 | `t9_gun_shop_empty_shelves`, `push` | **第4段階: 武装した暴力の顕在化。** | — | — |  |
| 2-24 | `2.06#9` (13.7 s) | D | T1 | `t9_midnight_convoy_old_ford`, `pan` | *1969年7月下旬、Mansonは麻薬密売人のBernard Croweを銃撃して重傷を負わせ、金銭トラブルから音楽家のGary Hinmanを殺害するよう命じました。* | — | — |  |
| 2-25 | `2.06#10`–`#11` (12.8 s) | D | T1 | `t9_cielo_drive_road_sign_shadow`, `pull` | **第5段階: 集団的破壊の極致。** → `#11`: *暴力への閾値が麻痺したMansonは、象徴的な虐殺を実行するためにCielo DriveとWaverly Driveの襲撃を命じたのです。* | — | — |  |
| 2-26 | `2.06#12` (4.5 s) | D | T1 | `t9_apocalyptic_desert_hideout`, `still` | **このエスカレーションは、明確な心理的法則を浮き彫りにしています。** | — | — |  |
| 2-27 | `2.06#13` (9.3 s) | D | T1 | `t9_burning_id_cards_ashes`, `push` | *最初の境界侵犯が放置されたとき、飢えた暗黒の妄想は、現実世界においてさらなる破滅を貪り求めるようになるのです。」* | — | →H |  |
| 2-28 | `2.08#1` (6.9 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `pan` | *「では、Cielo Driveの邸宅への襲撃を引き起こした直接的な心理的引き金とは何だったのでしょうか。* | — | — |  |
| 2-29 | `2.08#2` (9.5 s) | H | T1 | `t9_recording_studio_rejected_demo`, `pull` | *救世主の仮面の裏で、MansonはThe Beatlesを超える偉大なロックミュージシャンになるという病的な自己愛の妄想を抱き続けていました。* | — | — |  |
| 2-30 | `2.08#3` (7.8 s) | H | T1 | `t9_recording_studio_rejected_demo`, `still` | *彼はレコード契約を勝ち取ろうと、Columbia Recordsの著名な音楽プロデューサーであるTerry Melcherに執拗に接近しました。* | — | — |  |
| 2-31 | `2.08#4` (10.4 s) | H | T1 | `t9_broken_porcelain_doll_desert`, `push` | *しかし、Melcherが契約を拒絶しアルバムの発売を後押ししなかったとき、Mansonの脆弱な自己愛は極限の屈辱を味わうことになったのです。* | — | — |  |
| 2-32 | `2.08#5` (5.5 s) | H | T1 | `t9_manson_shadow_campfire_desert`, `pan` | **拒絶されたという強烈な屈辱感は、破壊的な報復の憤怒へと変貌しました。」** | — | →D |  |
| 2-33 | `2.09#1` (8.7 s) | D | T1 | `t9_cielo_drive_estate_night`, `pull` | *「10050 Cielo Driveの邸宅は、Roman Polanski監督が入居する直前に、まさにTerry Melcherが賃貸していた家でした。* | — | — |  |
| 2-34 | `2.09#2` (9.9 s) | D | T1 | `t9_cielo_drive_road_sign_shadow`, `still` | *Melcherがすでに退去したことを知りながらも、Mansonは自分を拒絶したハリウッドの特権階級への怒りを晴らすために、この場所を選定したのです。* | — | — |  |
| 2-35 | `2.09#3` (9.3 s) | D | T1 | `t9_kasabian_escape_night_highway`, `push` | *彼はCharles Tex Watsonと3人の女性信者に対し、家の中にいる者を全員抹殺せよという明確な命令を下しました。* | — | — |  |
| 2-36 | `2.09#4` (5.6 s) | D | T1 | `t9_bloody_letters_forensic_wall`, `pan` | *現場において、私たちは手口（MO）と心理的サイン（Signature）を明確に区別しています。* | — | — |  |
| 2-37 | `2.09#5` (7.0 s) | D | T1 | `t9_lapd_investigation_room`, `pull` | **手口とは、電話線を切断し、刃物を用い、逃走のために証拠を隠滅することでした。** | — | — |  |
| 2-38 | `2.09#6` (14.3 s) | D | T1 | `t9_interlocking_knots_rope`, `still` | *それに対して不変の心理的サインとは、ドアに『PIG』と書き残し、被害者たちを1本のナイロンロープで繋ぎ止めて不気味な劇場空間を演出しようとした行為そのものでした。」* | — | →H |  |
| 2-39 | `2.10#1` (9.8 s) | H | T1 | `t9_los_angeles_county_crime_map`, `push` | *「被害者学の観点から見れば、Cielo DriveやWaverly Driveに集まっていた人々は、Mansonに対して何の怨恨も抱いていませんでした。* | — | — |  |
| 2-40 | `2.10#2` (16.9 s) | H | T1 | `t9_broken_porcelain_doll_desert`, `pan` | *才能あふれる女優Sharon Tate、著名なヘアスタイリストのJay Sebring、Abigail Folger、Wojciech Frykowski、若きSteven Parent、そしてLenoとRosemary LaBianca夫妻は、いずれも夢と尊厳に満ちた生きた人間でした。* | — | — |  |
| 2-41 | `2.10#3` (8.3 s) | H | T1 | `t9_yearbook_photos_shadow`, `pull` | *彼らは、誇大妄想的な自己愛者の屈辱的な失敗のために、身代わりの小道具として理不尽に命を奪われたのです。* | — | — |  |
| 2-42 | `2.10#4` (7.1 s) | H | T1 | `t9_withered_flower_on_asphalt`, `still` | *彼らは単なる悲劇の犠牲者の名前としてではなく、かけがえのない人間として記憶されるべき存在です。」* | — | — |  |
| 2-43 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *第03幕* · **自我を消滅させる三段階** | — | ⊘ | ◼ |

### 第03幕 — 自我を消滅させる三段階

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` (6.8 s) | H | T1 | `t9_los_angeles_skyline_1969`, `pan` | *「実行犯グループの正体が公表されたとき、アメリカ全土はかつてない精神的動揺に襲われました。* | — | — |  |
| 3-02 | `3.02#2` (8.3 s) | H | T1 | `t9_yearbook_photos_shadow`, `pull` | *現場で直接指揮を執っていたのは、Texas出身の元優等生であり高校の陸上スターだったCharles “Tex” Watsonでした。* | — | — |  |
| 3-03 | `3.02#3` (4.9 s) | H | T1 | `t9_spahn_ranch_dilapidated_porch`, `still` | **彼に同行していたのは、まともな中流家庭で育った若い女性たちでした。** | — | — |  |
| 3-04 | `3.02#4` (9.9 s) | H | T1 | `t9_haight_ashbury_psychedelic_street`, `push` | *Susan Atkinsは教会の聖歌隊で歌い、Patricia Krenwinkelは温厚で知られ、Leslie Van Houtenは高校の元ホームカミングプリンセスでした。* | — | — |  |
| 3-05 | `3.02#5` (9.8 s) | H | T1 | `t9_shadow_devil_dialogue_noir`, `pan` | *なぜ教育を受けたごく普通の若者たちが、自ら良心を放棄し、冷酷無比な破壊の道具へと進んで身を落としてしまったのでしょうか。」* | — | →C |  |
| 3-06 | `3.03#1` (15.3 s) | C | T1 | `t9_kurt_lewin_three_stages_diagram`, `pull` | *「この現象を解明するには、心理学者Kurt Lewinが提唱し、後にEdgar Schein教授がマインドコントロールの解明に応用した認知変化の3段階モデルを用いる必要があります。* | — | ✦ Cáo |  |
| 3-07 | `3.03#2` (7.0 s) | C | T1 | `t9_kurt_lewin_three_stages_diagram`, `still` | *すなわち、自我の解凍（Unfreezing）、認知的変革（Changing）、そして行動の再凍結（Refreezing）です。* | — | — |  |
| 3-08 | `3.03#3`–`#4` (11.6 s) | C | T1 | `t9_dark_triad_psychological_symbol`, `push` | **Charles Mansonは、神秘的な超能力を持っていたわけではありません。** → `#4`: **集団心理を操る最も冷酷な技術を、直感的に使いこなす名人だったに過ぎないのです。** | — | — |  |
| 3-09 | `3.03#5` (5.8 s) | C | T1 | `t9_kurt_lewin_three_stages_diagram`, `pan` | **この人格剥奪のプロセスは、計算された順序で着実に実行されました。」** | — | →H |  |
| 3-10 | `3.05#1` (5.7 s) | H | T1 | `t9_kurt_lewin_three_stages_diagram`, `pull` | *「第1段階は、従来の自我を融解させるプロセス、すなわち解凍（Unfreezing）です。* | — | — |  |
| 3-11 | `3.05#2` (7.3 s) | H | T1 | `t9_unfreezing_love_bombing_circle`, `still` | *新しい若者がSpahn Ranchに足を踏み入れると、Mansonは即座に『愛の爆撃（Love Bombing）』戦術を展開しました。* | — | — |  |
| 3-12 | `3.05#3` (6.0 s) | H | T1 | `t9_unfreezing_love_bombing_circle`, `push` | **彼は彼らを抱きしめ、瞳をじっと見つめ、完全無欠な存在であると囁きかけました。** | — | — |  |
| 3-13 | `3.05#4` (5.4 s) | H | T1 | `t9_blind_devotion_extinguished_candle`, `pan` | **本来の家族が残した孤独や感情の空白を、巧みに埋めてみせたのです。」** | — | →C |  |
| 3-14 | `3.06#1` (6.5 s) | C | T1 | `t9_redflag2_severed_family_photos`, `pull` | **「しかし、その温かい抱擁の直後に待っていたのは、過酷な社会的孤立の罠でした。** | — | — |  |
| 3-15 | `3.06#2` (9.8 s) | C | T1 | `t9_burning_id_cards_ashes`, `still` | *Mansonは信者たちに対し、所持金を捨て、身分証明書を手放し、両親との連絡を完全に断ち切るよう要求しました。* | — | — |  |
| 3-16 | `3.06#3` (9.6 s) | C | T1 | `t9_burning_id_cards_ashes`, `push` | *彼らの本名を奪い、Sadie、Katie、Luluといった奇妙な偽名を与えることで、過去のアイデンティティを消去したのです。* | — | — |  |
| 3-17 | `3.06#4` (5.8 s) | C | T1 | `t9_lsd_hallucinogen_distorted_reality`, `pan` | **夜の儀式では、信者たちに高用量の幻覚剤LSDを投与しました。** | — | — |  |
| 3-18 | `3.06#5` (5.9 s) | C | T1 | `t9_blind_devotion_extinguished_candle`, `pull` | **Manson自身はごく微量しか口にせず、冷静な支配力を常に維持していました。** | — | — |  |
| 3-19 | `3.06#6` (8.9 s) | C | T1 | `t9_inverted_cross_moral_confusion`, `still` | *薬物による幻覚と肉体的疲弊の二重の攻撃により、若者たちの自我の防壁は完全に崩壊しました。* | — | — |  |
| 3-20 | `3.06#7` (5.5 s) | C | T1 | `t9_trauma_bonding_group_shadows`, `push` | **彼らの精神は、急速に純白の空白地帯へと変えられていったのです。」** | — | →H |  |
| 3-21 | `3.07#1` (6.2 s) | H | T1 | `t9_changing_night_desert_sermon`, `pan` | *「第2段階は、認知的再プログラミング、すなわち変革（Changing）のプロセスです。* | — | — |  |
| 3-22 | `3.07#2` (10.8 s) | H | T1 | `t9_changing_night_desert_sermon`, `pull` | *信者たちが自律的な批判的思考力を失うと、Mansonは彼らの無防備な心へと終末思想を系統的に注入し始めました。」* | — | →C |  |
| 3-23 | `3.08#1` (11.2 s) | C | T1 | `t9_vinyl_record_white_album`, `still` | *「彼はThe Beatlesのホワイトアルバムに収録された楽曲『Helter Skelter』を、間もなく勃発する人種間戦争の神聖な予言へと歪曲しました。* | — | — |  |
| 3-24 | `3.08#2` (6.6 s) | C | T1 | `t9_blind_devotion_extinguished_candle`, `push` | *自らをイエス・キリストの再来であり、唯一無二の真理の基準として君臨させたのです。* | — | — |  |
| 3-25 | `3.08#3` (9.6 s) | C | T1 | `t9_mastermind_conspiracy_law_book`, `pan` | *信者たちの良心の痛痒を麻痺させるため、MansonはSykesとMatzaの犯罪学理論における中和の技術（Techniques of Neutralization）を叩き込みました。* | — | — |  |
| 3-26 | `3.08#4` (14.3 s) | C | T1 | `t9_inverted_cross_moral_confusion`, `pull` | *より高位の忠誠心への訴え: Mansonは、Helter Skelterにおける殺人行為は犯罪ではなく、全人類の愛に奉仕するための崇高な精神的解放であると説きました。* | — | — |  |
| 3-27 | `3.08#5` (13.0 s) | C | T1 | `t9_shadow_devil_dialogue_noir`, `still` | *被害者の客体化と非人間化: 被害者は人間ではなく、浄化されるべき資本主義体制の偽善的な象徴である『Pigs（ブタども）』に過ぎないと教え込みました。* | — | — |  |
| 3-28 | `3.08#6` (12.8 s) | C | T1 | `t9_interlocking_knots_rope`, `push` | *個人的責任の否定: 行動の意志は宇宙の使命へと転嫁され、信者たちは神聖な命令を執行する無謬の道具に過ぎないと自己正当化させました。* | — | — |  |
| 3-29 | `3.08#7` (11.6 s) | C | T1 | `t9_vacant_eyes_doll_shadow`, `pan` | *Manson自身について言えば、彼は他者の心を推し量る心の理論（Theory of Mind）を完全に欠落させており、他者の苦痛に対して完璧に無感覚でした。* | — | — |  |
| 3-30 | `3.08#8`–`#9` (12.4 s) | C | T1 | `t9_broken_porcelain_doll_desert`, `pull` | **被害者の命乞いは、彼の同情心を呼び起こすことはありませんでした。** → `#9`: *それは悪性自己愛者の心を熱狂させる、病的な権力の性的興奮（power arousal）の引き金となったのです。* | — | — |  |
| 3-31 | `3.08#10` (8.8 s) | C | T1 | `t9_invisible_puppet_master_shadow`, `still` | *彼は信者たちを愛する仲間としてではなく、支配の妄想を満たすための自我の延長物としか見なしていませんでした。」* | — | →H |  |
| 3-32 | `3.10#1` (5.7 s) | H | T1 | `t9_kurt_lewin_three_stages_diagram`, `push` | *「そして、支配機構を固定化するための最後の段階、すなわち再凍結（Refreezing）です。* | — | — |  |
| 3-33 | `3.10#2` (8.4 s) | H | T1 | `t9_vacant_eyes_doll_shadow`, `pan` | *若い信者たちが決して正気を取り戻さず、一般社会へと逃げ帰らないよう、Mansonはどのようにして縛り付けたのでしょうか。」* | — | →C |  |
| 3-34 | `3.11#1` (6.4 s) | C | T1 | `t9_trauma_bonding_group_shadows`, `pull` | *「その答えこそが、集団的凶行への共謀による極限のトラウマ・ボンディング（Trauma Bonding）でした。* | — | — |  |
| 3-35 | `3.11#2` (10.1 s) | C | T1 | `t9_interlocking_knots_rope`, `still` | *集団暴力という共通の罪に全員の手を染めさせることで、Mansonは彼らを分かち難い共犯の絆へと強固に縛り付けました。* | — | — |  |
| 3-36 | `3.11#3` (5.4 s) | C | T1 | `t9_burning_id_cards_ashes`, `push` | **個人の罪悪感は、群衆心理の中に完全に溶解してしまいました。** | — | — |  |
| 3-37 | `3.11#4` (9.1 s) | C | T1 | `t9_gate_of_spahn_ranch_departure`, `pan` | *人類共通の究極の禁忌を踏み越えてしまったとき、日常の平穏な生活へと戻る道は永遠に焼き払われたのです。* | — | — |  |
| 3-38 | `3.11#5` (7.9 s) | C | T1 | `t9_manson_shadow_campfire_desert`, `pull` | *彼らの運命は、それ以降、独裁的な指導者の権力へと絶対的に繋ぎ止められることになりました。」* | — | — |  |
| 3-39 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *第04幕* · **捜査・証人・裁判** | — | ⊘ | ◼ |

### 第04幕 — 捜査・証人・裁判

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` (8.4 s) | H | T1 | `t9_death_valley_barker_ranch_raid`, `push` | *「1969年8月の凶行の連鎖の後、犯行グループは荒涼としたDeath Valleyの砂漠へと潜伏しました。* | — | — |  |
| 4-02 | `4.02#2` (7.2 s) | H | T1 | `t9_death_valley_barker_ranch_raid`, `pan` | **膠着状態に陥っていた警察の捜査は、1969年10月に思わぬ転機を迎えました。** | — | — |  |
| 4-03 | `4.02#3` (9.2 s) | H | T1 | `t9_kasabian_escape_night_highway`, `pull` | *砂漠地帯で多発していた車両窃盗団を一斉摘発した合同捜査班が、Mansonと数十人の信者たちを拘束したのです。* | — | — |  |
| 4-04 | `4.02#4` (7.4 s) | H | T1 | `t9_lapd_investigation_room`, `still` | *当初、捜査官たちは自分たちがTate-LaBianca虐殺の首謀者を拘束しているとは露知らずにいました。」* | — | →D |  |
| 4-05 | `4.03#1` (6.9 s) | D | T1 | `t9_sybil_brand_jail_corridor`, `push` | *「事態の突破口は、皮肉にも犯人自身の抑えきれない自己愛的な傲慢さからもたらされました。* | — | — |  |
| 4-06 | `4.03#2` (7.6 s) | D | T1 | `t9_sybil_brand_jail_corridor`, `pan` | *Sybil Brand刑務所に勾留されていた女性信者のSusan Atkinsが、自慢したい衝動に抗えなかったのです。* | — | — |  |
| 4-07 | `4.03#3` (8.6 s) | D | T1 | `t9_prison_cell_bars_shadow`, `pull` | *彼女は同房の2人の受刑者に対し、Cielo Driveの邸宅での犯行の詳細を誇らしげに語って聞かせました。* | — | — |  |
| 4-08 | `4.03#4` (6.6 s) | D | T1 | `t9_lapd_investigation_room`, `still` | **その衝撃的な告白は、直ちにロサンゼルス市警察の専任捜査班へと通報されました。** | — | — |  |
| 4-09 | `4.03#5` (7.7 s) | D | T1 | `t9_bloody_letters_forensic_wall`, `push` | **この供述をもとに、捜査官たちは物証、現場の指紋、弾道検査を迅速に照合しました。** | — | — |  |
| 4-10 | `4.03#6` (5.4 s) | D | T1 | `t9_yearbook_photos_shadow`, `pan` | **犯行グループの全体像が、白日の下に完全に暴かれたのです。」** | — | →H |  |
| 4-11 | `4.04#1` (9.4 s) | H | T1 | `t9_courtroom_gavel_bench`, `pull` | *「しかし、自ら武器を握らなかった黒幕を有罪にするため、検察側はカルトの内部から真実を語る生き証人を必要としていました。* | — | — |  |
| 4-12 | `4.04#2` (5.1 s) | H | T1 | `t9_linda_kasabian_witness_dossier`, `still` | **その人物こそが、当時20歳の若い母親だったLinda Kasabianでした。** | — | — |  |
| 4-13 | `4.04#3` (7.3 s) | H | T1 | `t9_cielo_drive_front_gate_fog`, `push` | *彼女は両夜とも見張り役として現場に同行したものの、暴力の行使を拒否し、その後に逃亡していました。* | — | — |  |
| 4-14 | `4.04#4` (5.3 s) | H | T1 | `t9_kasabian_escape_night_highway`, `pan` | **法廷でMansonと対峙した彼女の、魂を揺さぶる証言をお聞きください。」** | — | →N2 |  |
| 4-15 | `4.05#1` (7.5 s) | N2 | T4 lời kể | `t9_linda_kasabian_witness_dossier`, `pull` | *「証言台に立ち、Charles Mansonの目を真正面から見つめたとき、背筋を凍りつかせるような悪寒が走りました。* | — | ✦ Mèo |  |
| 4-16 | `4.05#2` (8.1 s) | N2 | T4 lời kể | `t9_vacant_eyes_doll_shadow`, `still` | *Spahn Ranchで共に生活していた友人たちは、今や糸の切れた操り人形のように空虚な眼差しでそこに座っていました。* | — | — |  |
| 4-17 | `4.05#3` (5.0 s) | N2 | T4 lời kể | `t9_trauma_bonding_group_shadows`, `push` | **彼らはもはや、他人の苦痛や恐怖を感じ取る心を失っていました。** | — | — |  |
| 4-18 | `4.05#4` (7.7 s) | N2 | T4 lời kể | `t9_blind_devotion_extinguished_candle`, `pan` | *Mansonの巧妙な言葉によって、彼らが少しずつ自分自身を見失っていくのを、私はこの目で見てきたのです。* | — | — |  |
| 4-19 | `4.05#5` (5.3 s) | N2 | T4 lời kể | `t9_courtroom_gavel_bench`, `pull` | **証言台に立つことは、私の人生で最も恐ろしく苦しい決断でした。** | — | — |  |
| 4-20 | `4.05#6` (6.9 s) | N2 | T4 lời kể | `t9_scales_of_justice_broken_chains`, `still` | *しかし、罪のない被害者たちに正義を取り戻すためには、真実を語らなければならないと悟ったのです。* | — | — |  |
| 4-21 | `4.05#7` (6.2 s) | N2 | T4 lời kể | `t9_open_birdcage_dawn_horizon`, `push` | **かつて私の魂を支配した邪悪な影を振り払う道は、それしかありませんでした。」** | — | →H |  |
| 4-22 | `4.07#1` (9.6 s) | H | T1 | `t9_los_angeles_hall_of_justice`, `pan` | *「Charles Mansonと共犯者たちに対する裁判は、Charles Older裁判長の主宰のもと、1970年6月に正式に幕を開けました。* | — | — |  |
| 4-23 | `4.07#2` (8.9 s) | H | T1 | `t9_los_angeles_hall_of_justice`, `pull` | *それはアメリカの司法史上、最も長期化し、巨額の費用を要し、そして最も異様な公判の1つとなりました。* | — | — |  |
| 4-24 | `4.07#3` (8.2 s) | H | T1 | `t9_collective_hysteria_three_shaved_heads`, `still` | *裁判所の外では、残された信者たちが歩道に座り込み、頭を丸坊主にして証言台に立つ証人たちを威嚇し続けました。* | — | — |  |
| 4-25 | `4.07#4` (6.1 s) | H | T1 | `t9_prosecutor_desk_evidence_files`, `push` | *歴史的な重責が、副検事Vincent Bugliosiの双肩に重くのしかかっていました。」* | — | →D |  |
| 4-26 | `4.08#1` (8.3 s) | D | T1 | `t9_prosecutor_desk_evidence_files`, `pan` | *「検察側にとって最大の法的挑戦は、Charles Manson自身の直接的な有罪を立証することでした。* | — | — |  |
| 4-27 | `4.08#2` (6.4 s) | D | T1 | `t9_cielo_drive_estate_night`, `pull` | *8月8日の夜、彼はSharon Tateの邸宅には一切足を踏み入れていませんでした。* | — | — |  |
| 4-28 | `4.08#3` (5.9 s) | D | T1 | `t9_midnight_convoy_old_ford`, `still` | *翌夜のLaBianca邸においても、信者たちが凶行に及ぶ前に現場を立ち去っていました。* | — | — |  |
| 4-29 | `4.08#4` (10.7 s) | D | T1 | `t9_mastermind_conspiracy_law_book`, `push` | *弁護側は、Manson自身の手が武器に触れていない以上、殺人の罪で断罪することは不可能であると強硬に主張しました。* | — | — |  |
| 4-30 | `4.08#5` (8.0 s) | D | T1 | `t9_prosecutor_desk_evidence_files`, `pan` | *冷徹な論理と鉄壁の証拠構築により、Bugliosi検事は記念碑的な法理論を打ち立てました。* | — | — |  |
| 4-31 | `4.08#6` (4.5 s) | D | T1 | `t9_mastermind_conspiracy_law_book`, `pull` | *それこそが、共謀および代位責任の法理（Conspiracy and Vicarious Liability）でした。* | — | — |  |
| 4-32 | `4.08#7` (13.1 s) | D | T1 | `t9_interlocking_knots_rope`, `still` | *彼は陪審員に対し、実行犯たちは単なる手足の延長に過ぎず、犯行を支配した脳と唯一の悪意ある意志はCharles Mansonにあったと証明してみせたのです。* | — | — |  |
| 4-33 | `4.08#8` (6.6 s) | D | T1 | `t9_shadow_devil_dialogue_noir`, `push` | *直接手を下さずとも、すべての蛮行は彼の絶対的な命令から生み出されたものだったのです。」* | — | →C |  |
| 4-34 | `4.09#1` (6.8 s) | C | T1 | `t9_dark_triad_psychological_symbol`, `pan` | **「法廷における被告たちの振る舞いは、集団的暗示と極端な否認機制の典型例でした。** | — | — |  |
| 4-35 | `4.09#2` (8.1 s) | C | T1 | `t9_carved_x_symbol_forehead`, `pull` | *Mansonは額にナイフで『X』の印を刻み、人間社会から自らを抹殺したと宣言しました。* | — | — |  |
| 4-36 | `4.09#3` (7.9 s) | C | T1 | `t9_collective_hysteria_three_shaved_heads`, `still` | *翌日には女性被告たちも同じく額にXを刻み、手を繋いで歌いながら法廷に入廷してきました。* | — | — |  |
| 4-37 | `4.09#4` (8.5 s) | C | T1 | `t9_shadow_devil_dialogue_noir`, `push` | *Mansonは法廷の支配権を失いかけた際、弁護側の机を跳び越えて裁判長を襲撃しようとさえしました。* | — | — |  |
| 4-38 | `4.09#5` (5.9 s) | C | T1 | `t9_two_faced_benevolent_mask`, `pan` | *それは、法廷を個人の舞台へと変えようとする劇的な自己愛（Theatrical Narcissism）の露骨な現れでした。* | — | — |  |
| 4-39 | `4.09#6` (6.9 s) | C | T1 | `t9_vacant_eyes_doll_shadow`, `pull` | **集団の妄想に守られている間、彼らは本物の罪悪感や悔恨を抱いてはいませんでした。** | — | — |  |
| 4-40 | `4.09#7` (6.9 s) | C | T1 | `t9_scales_of_justice_broken_chains`, `still` | **彼の誇大自己の真の崩壊は、法の厳格な鉄槌が下された瞬間にこそ始まったのです。」** | — | →H |  |
| 4-41 | `4.10#1` (6.7 s) | H | T1 | `t9_scales_of_justice_broken_chains`, `push` | *「しかし、すべての茶番劇と不気味な心理工作も、正義の光を覆い隠すことはできませんでした。* | — | — |  |
| 4-42 | `4.10#2` (12.2 s) | H | T1 | `t9_courtroom_jury_verdict_dossier`, `pan` | *数ヶ月におよぶ激しい審理の末、1971年1月25日、陪審員団はMansonと3人の女性共犯者に対し歴史的な有罪評決を下しました。* | — | — |  |
| 4-43 | `4.10#3` (6.3 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `pull` | *『愛の夏』を覆い尽くしていた暗黒の帳は、法の支配によって正式に引き裂かれたのです。」* | — | — |  |
| 4-44 | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | *第05幕* · **歴史的判決と教訓** | — | ⊘ | ◼ |

### 第05幕 — 歴史的判決と教訓

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` (10.3 s) | H | T1 | `t9_courtroom_jury_verdict_dossier`, `push` | *「1971年3月、Charles Manson、Susan Atkins、Patricia Krenwinkel、そしてLeslie Van Houtenに対し死刑が言い渡されました。* | — | — |  |
| 5-02 | `5.02#2` (10.4 s) | H | T1 | `t9_california_supreme_court_columns`, `pan` | *しかし1972年、カリフォルニア州最高裁判所は歴史的なPeople vs Anderson判決において、死刑制度を一時的に違憲と判断しました。* | — | — |  |
| 5-03 | `5.02#3` (7.6 s) | H | T1 | `t9_corcoran_state_prison_watchtower`, `pull` | *Mansonと共犯者たちのすべての死刑判決は、仮釈放の可能性を含む終身刑へと自動的に減刑されました。* | — | — |  |
| 5-04 | `5.02#4` (10.6 s) | H | T1 | `t9_corcoran_state_prison_watchtower`, `still` | *しかし、その後の半世紀近くにわたり行われた数十回もの仮釈放審査において、Charles Mansonの釈放申請はすべて断固として却下され続けました。* | — | — |  |
| 5-05 | `5.02#5` (7.0 s) | H | T1 | `t9_scales_of_justice_broken_chains`, `push` | *仮釈放委員会は、遺族たちの癒えることのない悲痛な叫びを前に、確固たる姿勢を崩さなかったのです。」* | — | →D |  |
| 5-06 | `5.04#1` (14.1 s) | D | T1 | `t9_mastermind_conspiracy_law_book`, `pan` | *「Manson事件は、精神を操り犯罪を指揮した主犯が直接手を下した実行犯と同等の刑事責任を負わねばならないという、現代司法における不滅の判例を確立しました。* | — | — |  |
| 5-07 | `5.04#2` (6.0 s) | D | T1 | `t9_courtroom_gavel_bench`, `pull` | **法は、心理的権力が犯罪の防壁として機能し得ないことを明確に宣言しました。** | — | — |  |
| 5-08 | `5.04#3` (7.7 s) | D | T1 | `t9_corcoran_state_prison_watchtower`, `still` | *Charles Mansonは、カリフォルニア州で最も警備の厳重な刑務所の中で残りの生涯を過ごしました。* | — | — |  |
| 5-09 | `5.04#4` (5.4 s) | D | T1 | `t9_waverly_drive_residence_night`, `push` | **そして2017年11月19日、83歳で病没しました。** | — | — |  |
| 5-10 | `5.04#5` (9.1 s) | D | T1 | `t9_withered_flower_on_asphalt`, `pan` | *彼は鉄格子の向こうで絶対的な孤独のうちにその生涯を閉じ、アメリカの歴史に拭い去れぬ汚名を遺したのです。」* | — | →C |  |
| 5-11 | `5.05#1` (11.0 s) | C | T1 | `t9_courtroom_jury_verdict_dossier`, `pull` | *「心理学の観点から言えば、Charles Mansonに科された最も過酷な刑罰は、肉体を閉じ込める壁ではなく、社会からの完全な忘却でした。* | — | — |  |
| 5-12 | `5.05#2` (7.3 s) | C | T1 | `t9_recording_studio_rejected_demo`, `still` | *晩年に至るまで、Mansonは注目の飢えを満たそうと、狂ったようにメディアのインタビューを求め続けました。* | — | — |  |
| 5-13 | `5.05#3` (7.4 s) | C | T1 | `t9_two_faced_benevolent_mask`, `push` | *その浅ましい姿は、誇大自己が完全に崩壊した際に露呈する病的な自己憐憫（Pathological Self-Pity）そのものでした。* | — | — |  |
| 5-14 | `5.05#4` (14.2 s) | C | T1 | `t9_open_birdcage_dawn_horizon`, `pan` | *一方、Leslie Van HoutenやPatricia Krenwinkelといった元信者たちは、数十年の時を経てマインドコントロールの霧が晴れた後、底知れぬ良心の呵責に苛まれ続けました。* | — | — |  |
| 5-15 | `5.05#5` (7.7 s) | C | T1 | `t9_withered_flower_on_asphalt`, `pull` | *彼らは自らの青春と人格を一人のペテン師に捧げてしまったという痛恨の事実を悟ったのです。* | — | — |  |
| 5-16 | `5.05#6` (11.4 s) | C | T1 | `t9_redflag3_fortress_paranoia_wall`, `still` | *この悲劇は私たちに警告しています――人間が孤独と実存的真空に直面したとき、愛を名る捕食者の格好の餌食になってしまうのだと。* | — | — |  |
| 5-17 | `5.05#7` (6.2 s) | C | T1 | `t9_two_faced_benevolent_mask`, `push` | **心理的捕食者は、決して悪魔の角を生やして現れるわけではありません。** | — | — |  |
| 5-18 | `5.05#8` (7.5 s) | C | T1 | `t9_two_faced_benevolent_mask`, `pan` | *彼らは常に、誰よりも深く理解し共感してくれる友人の姿を装って近づいてくるのです。」* | — | →H |  |
| 5-19 | `5.07#1` (14.3 s) | H | T1 | `t9_amber_eyes_closing_dossier`, `pull` | *「現代社会に潜む有害な心理的支配の罠から自らと大切な人を守るため、Amber EyesはGavin de Beckerの『The Gift of Fear』の原則に基づき、4つの生存のためのレッドフラッグ（Survival Red Flags）を提言します。* | — | — |  |
| 5-20 | `5.07#2` (3.6 s) | H | T8 cờ | `t9_redflag1_love_bombing_trap`, `still` | *01* · **レッドフラッグ1: 過剰な愛の爆撃（LOVE BOMBING）への警戒。** | — | — |  |
| 5-21 | `5.07#3` (9.0 s) | H | T1 | `t9_unfreezing_love_bombing_circle`, `push` | *出会った直後からあなたを過度に絶賛し、急速な親密さを強要してくる個人や集団は、あなたの警戒本能を麻痺させようとしています。* | — | — |  |
| 5-22 | `5.07#4` (3.8 s) | H | T8 cờ | `t9_redflag2_severed_family_photos`, `pan` | *02* · **レッドフラッグ2: 社会的孤立と境界線の剥奪。** | — | — |  |
| 5-23 | `5.07#5` (10.8 s) | H | T1 | `t9_burning_id_cards_ashes`, `pull` | *家族との関係を絶ち、友人を捨て、アイデンティティを変え、献身の証明として財産を差し出すよう要求されたなら、直ちにその場から立ち去ってください。* | — | — |  |
| 5-24 | `5.07#6` (4.7 s) | H | T8 cờ | `t9_redflag3_fortress_paranoia_wall`, `still` | *03* · **レッドフラッグ3: 敵対的な二元論的思考。** | — | — |  |
| 5-25 | `5.07#7` (11.2 s) | H | T1 | `t9_redflag3_fortress_paranoia_wall`, `push` | *有害な組織は常に外部の世界への恐怖を煽り立て、自らこそが唯一の安全な避難所であると信じ込ませることで、あなたの認知を集団の檻に閉じ込めます。* | — | — |  |
| 5-26 | `5.07#8` (3.7 s) | H | T8 cờ | `t9_redflag4_sacred_conscience_compass`, `pan` | *04* · **レッドフラッグ4: 自身の良心を他者に委ねてはならない。** | — | — |  |
| 5-27 | `5.07#9` (11.8 s) | H | T1 | `t9_redflag4_sacred_conscience_compass`, `pull` | *自称指導者が崇高な大義を名目に、法律や道徳的良心に反する行為を求めてきたなら、それは破滅へと続く最初の一歩に他なりません。* | — | — |  |
| 5-28 | `5.07#10` (10.7 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `still` | *直感が告げる違和感を常に信じてください――漠然とした不安こそが、あなたの命を守るために進化学が授けてくれたかけがえのない贈り物なのですから。」* | — | — |  |
| 5-29 | `5.09#1` (7.0 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `push` | *「真の自由とは、現実から逃避することでも、偽りの救世主に魂を委ねることでもありません。* | — | — |  |
| 5-30 | `5.09#2` (9.6 s) | H | T1 | `t9_open_birdcage_dawn_horizon`, `pan` | *自らの思考の主権を握り、個人の主体性を保ち、自らの行動に責任を引き受ける勇気の中にこそ、真の自由は宿るのです。* | — | — |  |
| 5-31 | `5.09#3` (11.4 s) | H | T1 | `t9_amber_eyes_closing_dossier`, `pull` | *本日、この重厚な歴史的記録の解剖に同席してくださった専門家の皆様、そして最後まで耳を傾けてくださった視聴者の皆様に心より感謝申し上げます。* | — | — |  |
| 5-32 | `5.09#4` (12.7 s) | H | T1 | `t9_amber_eyes_closing_dossier`, `still` | *常に明晰な理性を保ち、ご自身の直感に耳を傾け、平穏な日常を守り抜いてください――それでは、次なる事件記録でお会いしましょう。」* | — | — |  |
| 5-33 | 最終カード (0.0 s) | — | T2 | `t9_amber_eyes_closing_dossier`, `still` | **事件ファイル 第09話 · 終結** · *AMBER EYES · 実録の事件記録から読み解く犯罪心理学* | — | ⊘ | ◼ |

**Tổng:** 192 行 · 199 文 · 5 幕 · 背景 65 種 (MiniMax, 09/11/2026)。表は 09/11/2026 に書き直した台本 (199 文) に基づき再作成。
ショット長は master mp3 に固定したタイムライン (VN, 実測) に基づく。EN/JA は第08話係数で **推計** (誤差 0,000%) ⇒ 実音声ができたらタイムラインを作り直し画像を再レンダリングすること (T20/H14)。
短い 12 文は H10 (≥ 3 秒) のため同一 element の次の文と統合。15 秒超の 1 文 (2.10#2) は 画面文字を 2 ブロック + beat に分割 (A7)。
