# HỒ SƠ SẢN XUẤT TẬP 04 · BẢN TIẾNG NHẬT · 「第04話：死の天使と神のコンプレックス――9つの病院を巡った16年の沈黙の裏にある秘密」

> **TRẠNG THÁI: ĐÃ HOÀN THÀNH DỰNG VIDEO VÀ ĐÓNG GÓI XUẤT BẢN (BƯỚC 10 ĐẠT — 13/13 CỔNG QC PASS)**

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md` (Bản 1, 02/11/2026), `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` (§4.4), `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`.
**Kịch bản:** `01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md` · **Thành phẩm:** `02_SAN_XUAT/Tap04_JA/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md`.

---

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`, 166 câu, 61 elements) |
| Lượt nói / câu | **166 câu**. Host (H) 79 câu (47.6%) · Điều tra viên (D) 44 câu (26.5%) · Chuyên gia (C) 34 câu (20.5%) · Y tá Somerset N1 (Cừu) 4 câu (2.4%) · Y tá ca đêm N2 (Mèo) 5 câu (3.0%). |
| N1 / N2 | `1.07` NỮ Y TÁ SOMERSET (Cừu) / `4.06` Y TÁ CA ĐÊM (Mèo) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) vận hành trên Apple Silicon Mac qua MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (Apache-2.0, độc lập tiếng Nhật theo §4.4):<br>• **H (Cú):** `H_JA.wav` (121.8 Hz)<br>• **D (Sói):** `D_JA.wav` (83.3 Hz)<br>• **C (Cáo):** `C_JA.wav` (227.5 Hz)<br>• **N1 (Cừu):** `N1_JA.wav` (218.2 Hz)<br>• **N2 (Mèo):** `N2_JA.wav` (289.2 Hz) |
| Tách bạch cao độ (G9) | $\Delta_{\text{D}\to\text{H}} = 6.57\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) · $\Delta_{\text{H}\to\text{C}} = 10.81\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) |
| Đo CER | Chuẩn hóa kanji số theo G11 / `ja_cer.py` (pykakasi), tự động chạy Multi-take vòng 2 cho các câu cần tối ưu |
| Đo MOS | `sarulab-speech/UTMOSv2` trên CPU (M5), trung bình **3.00 / 5.0** (min 2.04, max 3.99, ĐẠT $\ge 3.0$) |
| Cắt đuôi câm (M3) | Tự động quét và cắt đuôi câm $> 0.8\text{ s}$ ở $-45\text{ dBFS}$, giữ $0.3\text{ s} + 30\text{ ms}$ fade-out |
| Thẻ cảm xúc (M4) | **CẤM tuyệt đối** mọi thẻ `<|emotion:...|>`; chỉ dùng ngắt nhịp `<|prosody:pause|>` sau `:` trước câu trích |
| Master Audio | `02_SAN_XUAT/Tap04_JA/xuat_ban/Tap04_JA_master.mp3` (36 MB, 1581.8 s ~ 26 phút 21.8 s)<br>• Integrated Loudness: **-16.2 LUFS** (chuẩn -16 ± 1 LUFS)<br>• True Peak: **-1.8 dBFS** (chuẩn ≤ -1.5 dBFS)<br>• LRA: **4.6 LU**<br>• Câm tuyệt đối > 0.3 s @ -60 dBFS: **0 lỗi (ĐẠT V4/A1)**<br>• Mốc lời đầu: **23.0 s** (chuẩn 22.8–23.5 s, intro nhạc 22.41 s)<br>• Mốc lời cuối kết thúc: **1572.8 s**, đuôi piano ấm fade out đến 1581.8 s |
| Master Video | `02_SAN_XUAT/Tap04_JA/xuat_ban/Tap04_JA_master.mp4` (589 MB, 1581.77 s ~ 26 phút 21.8 s, 47,453 frames @ 30 fps)<br>• Codec: H.264 High@L4.1 1920x1080 + AAC 48 kHz stereo 192 kbps<br>• Lệch hình - tiếng: **0.00 ms** (Cross-correlation 5 cửa sổ ĐẠT A/V Sync)<br>• Lệch thời lượng timeline: **-0.023 s** (ĐẠT chuẩn ±0.05 s)<br>• Audio sau limiter: **-16.3 LUFS**, True Peak **-3.10 dBFS** (ĐẠT chuẩn A7 / -16 ± 1 LUFS & ≤ -1.5 dBFS)<br>• Giải mã ffmpeg: **0 lỗi** (ĐẠT A11 #5)<br>• Faststart: **moov atom at byte 36** (ĐẠT chuẩn web streaming) |
| Phụ đề | `02_SAN_XUAT/Tap04_JA/xuat_ban/Tap04_JA.srt` (188 cues, khớp 100% timeline hòa âm) |

---

## B2. Tiêu đề và Thẻ hồi tiếng Nhật

- **Tiêu đề YouTube:** `第04話 · 死の天使と神のコンプレックス――9つの病院を巡った16年の沈黙の裏にある秘密 | チャールズ・カレンの心理学`
- **Thumbnail:** Dòng 1: `死の天使` · Dòng 2: `16年の沈黙`
- **Tiêu đề các hồi (Act titles):**
  - **第1幕 ·** つかみ――模範の看護師の逆説 (23.0 s – 274.2 s)
  - **第2幕 ·** 歪んだ心理のプロファイル――神のコンプレックスと無力感の補償 (276.2 s – 666.4 s)
  - **第3幕 ·** 道徳的無効化と被害者の人間性の剥奪 (668.4 s – 966.0 s)
  - **第4幕 ·** 捜査官の心理戦と潜入看護師の勇気 (968.0 s – 1277.8 s)
  - **第5幕 ·** 終幕――法廷、制度的沈黙への警鐘、そして終幕 (1279.8 s – 1572.8 s)

---

---

## 6. DANH SÁCH SHOT — TẬP 04 (JA)

**Đọc bảng:** *Vai* = người đang nói (H ホスト · D 捜査官 · C 心理学者 · N1 証人 · N2 視聴者). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

**Bản JA:** cột *Chữ* dùng tiếng Nhật chuẩn phát thanh tài liệu (Pillow vẽ chữ với `YuGothB.ttc` / `YuGothM.ttc`); các cụm `ở "…"` trong cột *Beat* là cụm tiếng Nhật **có thật** trong câu JA của shot đó (`phrase_time()` dò trong text câu để đặt thời điểm).

**Intro:** đặt `assets/brand/intro_kenh_JA_t04.mov` ở 0,00 s (sinh bằng `py -3 .work/make_intro.py` với `AE_LANG=ja AE_EP=04` — thẻ cảnh báo tiếng Nhật). Không câu thoại nào thuộc intro.
Renderer hiện ảnh intro ở 0,00–20,50 s; shot `1-00` (20,50 s → lời đầu 23,0 s) mở dần từ đuôi đen của intro.

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20.5 s → lời đầu) | — | T1 | `t4_somerset_exterior` hiện dần từ đen | *第1幕 · つかみ――模範の看護師の逆説* | Tiếng còi cấp cứu, máy thở ICU | ⊘ |  |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t4_somerset_exterior` | **2003年秋** · *Somerset Medical Center* → `#2`: *ニュージャージー州ソマービル町* | Gõ từng ký tự | ✦ Cú |  |
| 1-02 | `1.03#3` | H | T1 | `t4_icu_night` | **第ICU（集中治療室）** · *冷たい白い蛍光灯の光に満ちた* | — |  |  |
| 1-03 | `1.03#4` | H | T1 | `t4_cullen_silhouette`, `push` | **43歳の男** · *痩身で声も小さく* · *温和な笑顔* → *同僚の代わりに夜勤を引き受ける* | — |  |  |
| 1-04 | `1.04` (nghỉ 1.5 s) | — | — | giữ 1-03 | — | — | ⊘ |  |
| 1-05 | `1.05#1` | H | T2 | `t4_nurse_station` | *高圧な医療環境* · **生と死の境目** · *信頼できる同僚* | ở "生と死の境目" | 🅑 |  |
| 1-06 | `1.05#2`–`#3` | H | T1 | `t4_code_blue_aftermath` | **真っ先に駆けつけて助け** · *蘇生が奏功しなかった後には病室を片づけた* → `#3`: *同僚たちの信頼と愛着* | Tiếng sốc tim & flatline | ⊘ | →N1 |
| 1-07 | `1.07#1`–`#2` | N1 | T4 lời kể | `t4_breakroom_night` | “私たち看護師全員にとって、Charlieは素晴らしい友人でした。” → `#2`: “彼は親切で気を配り、苛立つこともなく、患者には常に細やかな思いやりを注いでいました。” | — | ✦ Y tá |  |
| 1-08 | `1.07#3`–`#4` | N1 | T4 lời kể | `t4_breakroom_night`, `push` | “夜勤が過酷で疲れているとき、彼は自分から、最も苦労の多い仕事を何の不平も言わずに引き受けました。” → `#4`: “病院の中で、彼のように親切で献身的な同僚を疑う者は一人もいませんでした。” | — | ⊘ | →H |
| 1-09 | `1.08#1` | H | T1 | `t4_corridor_shadow` | **真っ白な白衣の奥で** · *幽霊のような死神が病院の各廊下を静かに歩いていた* | — | ✦ Cú |  |
| 1-10 | `1.08#2`–`#4` | H | T1 | `t4_patient_room_night` | **68歳の司祭 FLORIAN GALL** · *肺炎と感染に伴う合併症で入院* → `#3`: *順調に回復し退院の準備* → `#4`: **劇的な不整脈を発し、心停止に至った** | — | ⊘ |  |
| 1-11 | `1.10#1` | H | T2 | `t4_toxicology_lab` | *法医学の毒性物質検査結果* · **安全域を数十倍も上回るDIGOXIN濃度** · *心臓を補助するきわめて強力な薬* | ở "安全域を数十倍も上回っている" | 🅑 |  |
| 1-12 | `1.10#2`–`#3` | H | T1 | `t4_digoxin_vial`, `push` | **医療上の誤りではない** · *許容上限を数十倍も超える* → `#3`: **意図的に静脈内へ直接注射された** | ở "意図的に" | ⊘ |  |
| 1-13 | `1.11` (nghỉ 2 s) | — | — | giữ 1-12 | — | — | ⊘ |  |
| 1-14 | `1.12#1` | H | T1 | `t4_case_file_open` | *事件の衝撃* · **事件を担当した捜査官の話を聞く** | — | →D |  |
| 1-15 | `1.14#1`–`#2` | D | T1 | `t4_case_file_open` | **CHARLES CULLENの勤務歴** · *事件担当チームの前に驚愕すべき事実が明らかに* → `#2`: *Somerset病院は最初の職場ではなかった* | — | ✦ Sói |  |
| 1-16 | `1.14#3`–`#4` | D | T8 | `t4_ten_hospitals_map` | *16年間：9つの病院と1つの老人ホーム* · *夜勤中に心停止で異常死亡する割合が跳ね上がっていた* | ở "老人ホーム" · ở "跳ね上がって" |  |  |
| 1-17 | `1.14#5`–`#6` | D | T1 | `t4_ten_hospitals_map`, `pull` | **自供：40人** · *疫学専門家の見積もり：300から400人* → `#6`: **アメリカ医療史で最も多くの命を奪った殺人者** | — | ⊘ | →H |
| 1-18 | `1.16#1`–`#3` | H | T10 | `t4_somerset_exterior` | **死の天使** · *隠された神のコンプレックス · 9つの病院にまたがる組織的な沈黙の秘密* | Tên tập ở cuối | 🅑 |  |
| 1-19 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第2幕* · **歪んだ心理のプロファイル――神のコンプレックスと無力感の補償** | — | ⊘ | ◼ |
| 2-01 | `2.02#1`–`#2` | H | T1 | `t4_sterile_room` | **無菌の治療室** · *患者が命と絶対的な信頼を託していた場所* | Nhạc piano tối giản | ✦ Cú |  |
| 2-02 | `2.02#3` | H | T8 | `t4_lethal_trio` | *現代医療が生み出した救命薬を凶器に* · **DIGOXIN、INSULIN、VECURONIUM** | ở "Insulin" · ở "Vecuronium" |  |  |
| 2-03 | `2.03` (nghỉ 1.5 s) | — | — | giữ 2-02 | — | — | ⊘ |  |
| 2-04 | `2.04#1`–`#2` | H | T1 | `t4_pyxis_station` | **自動薬剤管理システムの機械的な隙** · *16年間にわたり数百人の命を奪い、痕跡を残さない* | — | →D |  |
| 2-05 | `2.06#1`–`#2` | D | T1 | `t4_pyxis_station`, `still` | **PYXIS MEDSTATION** · *自動配薬キャビネット* · *個人ごとの暗証番号でログインし患者名を選択* | — | ✦ Sói |  |
| 2-06 | `2.06#3`–`#4` | D | T1 | `t4_pyxis_drawer_ajar` | **運用ソフトウェアの重大な脆弱性** · *操作時刻と操作者の身元をすべて記録するシステム* | — |  |  |
| 2-07 | `2.06#5`–`#6` | D | T3 so sánh | `t4_pyxis_cancel_screen` | *自分が担当していない患者* · **特別管理薬の高用量取り出し指示** · *DigoxinやInsulin* | ở "特別管理薬" |  |  |
| 2-08 | `2.06#7`–`#8` | D | T1 | `t4_pyxis_cancel_screen`, `push` | **タッチスクリーンの「注文を取り消す」ボタンを押す** · *引き出しが閉じる前に薬瓶を取り出しポケットへ* | — | ⊘ |  |
| 2-09 | `2.06#9` | D | T1 | `t4_pyxis_cancel_screen` | **取引を「取り消し」として記録** · *電子台帳には取り出された記録が一つも残らない* | — | ✦ Sói |  |
| 2-10 | `2.06#10` | D | T1 | `t4_saline_storage` | **生理食塩水バッグ保管庫** · *保管庫のNaClバッグへ過剰量の薬液を注入* | — | ⊘ |  |
| 2-11 | `2.06#11` | D | T1 | `t4_syringe_shadow` | **誤って投与された患者** · *攻撃源を知らないまま呼吸不全または突然の心停止に陥る* | — | ⊘ | →H |
| 2-12 | `2.07#1`–`#4` | H | T1 | `t4_sterile_room` | **痕跡を残さない完璧な方法** · *警告のベルはすでにはるか昔から鳴らされていた* | — | ✦ Cú | →D |
| 2-13 | `2.08#1`–`#3` | D | T2 | `t4_urgent_memo` | *NJ毒物対策センター長 STEVEN MARCUS博士* · **2003年7月の緊急警告** · *患者に有害な薬物を意図的に注射している* | ở "緊急警告" | ✦ Sói |  |
| 2-14 | `2.08#4`–`#6` | D | T1 | `t4_boardroom_empty` | **SOMERSET病院の経営陣** · *約3か月にわたり沈黙を保つ · 少なくとも5人の無実の患者が犠牲に* | — | ⊘ | →H |
| 2-15 | `2.10#1`–`#3` | H | T1 | `t4_locked_archives`, `push` | **なぜ明白な兆候を無視できたのか？** · *他の9つの病院でも発見されることなく転職できた理由* | — | ✦ Cú | →C |
| 2-16 | `2.11#1`–`#3` | C | T2 | `t4_institutional_bystander` | *組織心理学と法社会学* · **制度内の傍観者効果** · *Saint Barnabas病院 1992年：静かに退職することを許した* | ở "傍観者効果" | ✦ Cáo |  |
| 2-17 | `2.11#4`–`#6` | C | T1 | `t4_institutional_bystander`, `still` | *Warren病院 1993年：評判の毀損を恐れて事件を閉じる* → `#6`: **ST. LUKE病院 2002年：針廃棄箱から多数の指定薬物瓶を発見** | — | ⊘ |  |
| 2-18 | `2.11#7`–`#8` | C | T1 | `t4_neutral_letter` | **確認の手紙** · *彼の勤務については一切否定的評価をしていない* → *次の病院へ容易に移れるようにした* | — |  |  |
| 2-19 | `2.11#9`–`#11` | C | T1 | `t4_neutral_letter`, `push` | **商業化された医療システム** · *時限爆弾を近隣の病院へ渡し、組織の財政上の安定を優先した* | — | ⊘ |  |
| 2-20 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第3幕* · **道徳的無効化と被害者の人間性の剥奪** | — | ⊘ | ◼ |
| 3-01 | `3.02#1`–`#3` | H | T1 | `t4_god_complex_metaphor` | **この男を実際に動かしている動機は何か？** · *冷徹な弁明：「彼らの苦しみを終わらせたかった」* | Nhạc drone trầm đục | ✦ Cú |  |
| 3-02 | `3.02#4`–`#7` | H | T1 | `t4_god_complex_metaphor`, `push` | **「安らかな死を授ける慈悲の天使」の肖像** · *極めて有害な病的なコンプレックスを隠す偽りの仮面* | — | →C |  |
| 3-03 | `3.04#1`–`#3` | C | T1 | `t4_childhood_window` | **重度に分断された人格像** · *童年期の深い傷 · 生後7ヶ月で父を失う* → `#3`: *17歳のとき母親が交通事故で死亡* | — | ✦ Cáo |  |
| 3-04 | `3.04#4`–`#6` | C | T5 ngày | `t4_rainy_hearse_1977` | **1977年 · 病院が母の遺体を勝手に火葬** · *医療機関に対する深い憤り* → `#6`: *隠された神のコンプレックス* | — | ⊘ | →H |
| 3-05 | `3.05` (nghỉ 1.5 s) | — | — | giữ 3-04 | — | — | ⊘ |  |
| 3-06 | `3.06#1`–`#2` | H | T1 | `t4_cullen_silhouette`, `push` | **病的な代償メカニズム** · *劣等感と無力感に満ちた男が、白衣を着ることで全能感を見出す* | — | ✦ Cú | →C |
| 3-07 | `3.07#1`–`#2` | C | T1 | `t4_childhood_window` | **日常生活において** · *Cullenは完全に無力で、目立たない存在だった* | — | ✦ Cáo |  |
| 3-08 | `3.07#3`–`#5` | C | T1 | `t4_hypodermic_control`, `push` | **集中治療室の夜勤帯** · *たった一本の注射器で、人の生死を左右する絶対的な権力を握る* | ở "絶対的な権力" | ⊘ | →H |
| 3-09 | `3.08#1`–`#2` | H | T1 | `t4_two_faces_mask` | **「慈悲深い心」から行動していると自らを説得** · *自らの脳でどのように良心を騙したのか？* | — | ✦ Cú | →C |
| 3-10 | `3.09#1`–`#4` | C | T2 | `t4_two_faces_mask` | *第2のメカニズム* · **道徳的中立化技術** *(Moral Neutralization)* · *深い慈悲の情に訴える自己正当化* | ở "道徳的中立化技術" | ✦ Cáo |  |
| 3-11 | `3.09#5`–`#7` | C | T1 | `t4_broken_mercy`, `push` | **自己正当化の仮面を完全に打破** · *通常の手術から回復した21歳のMichael Strenko* → `#7`: **人の生死を左右する権力行使への渇望** | — | ⊘ | →H |
| 3-12 | `3.10#1`–`#3` | H | T1 | `t4_innocent_files`, `push` | **CULLENは誰一人も救っていない** · *病弱な患者たちの命を生贄にして、自らの人格危機を鎮めた* | — | ⊘ |  |
| 3-13 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第4幕* · **捜査官の心理戦と潜入看護師の勇気** | — | ⊘ | ◼ |
| 4-01 | `4.02#1`–`#2` | H | T5 ngày | `t4_prosecutor_office` | **2003年10月** · *Somerset郡検察局 · 刑事Tim BraunとDanny Baldwin* | Tiếng bước chân vội vã | ✦ Cú |  |
| 4-02 | `4.02#3`–`#5` | H | T1 | `t4_detectives_shadow` | **病院経営陣による頑固な沈黙の壁** · *真実への扉を開けられる唯一の人物：看護師Amy Loughren* | — | →D |  |
| 4-03 | `4.04#1`–`#3` | D | T1 | `t4_pyxis_printout` | **PYXISアクセスログ** · *数百ページにわたる印刷物* · *心臓病患者に不要な筋弛緩薬Vecuroniumを数十回分引き出す* | — | ✦ Sói |  |
| 4-04 | `4.04#4`–`#5` | D | T1 | `t4_wire_recorder`, `push` | **危険な心筋疾患を抱えながら** · *小型録音機を身につけ、Charles Cullenに接近することを決断* | — | ⊘ | →N2 |
| 4-05 | `4.06#1`–`#3` | N2 | T4 lời kể | `t4_amy_scrubs` | “刑事がCharlieの薬剤管理記録を見せてくれたとき、足元の地面が完全に崩れ落ちるようでした。” → `#2`: “Charlieは私にとって最も親しい友人で…” → `#3`: “しかし、私は看護師です。” | — | ✦ Amy |  |
| 4-06 | `4.06#4`–`#5` | N2 | T4 lời kể | `t4_amy_scrubs`, `push` | “私たちの職業上の誓いは、生命を守ることであり、悪と共謀することではありません。” → `#5`: “自分は決して背を向けられないと知っていた。” | — | ⊘ | →H |
| 4-07 | `4.08#1`–`#2` | H | T5 ngày | `t4_somerville_diner` | **2003年12月12日** · *ブリッジウォーターのレストラン* | Tiếng kéo ghế, dao nĩa | ✦ Cú |  |
| 4-08 | `4.08#3`–`#5` | H | T1 | `t4_diner_table` | **木製のテーブルを挟んで向かい合う** · *Amyは穏やかにCullenに自首を勧めた* → `#5`: *Cullenは困惑し、目は虚ろになりながらも戦うと宣言* | — | ⊘ |  |
| 4-09 | `4.09` (nghỉ 1.5 s) | — | — | giữ 4-08 | — | — | ⊘ |  |
| 4-10 | `4.11#1`–`#3` | H | T1 | `t4_parking_arrest`, `push` | **駐車場での逮捕** · *捜査官たちが飛び出して制圧し、その場で身柄を拘束* | — | →D |  |
| 4-11 | `4.12#1`–`#3` | D | T1 | `t4_interrogation_room` | **SOMERSET尋問室** · *石像のように微動だにせず、質問にも答えず24時間座り続ける* | — | ✦ Sói |  |
| 4-12 | `4.12#4`–`#5` | D | T1 | `t4_warm_sweater` | **決定的な切り札：AMY LOUGHREN** · *警察としてではなく、かつての友人として温かいセーターを渡す* | — |  |  |
| 4-13 | `4.12#6`–`#7` | D | T4 lời kể | `t4_confession_tape` | “Charlie、もし本当に罪を償うつもりなら、被害者家族に答えが得られるようにしてください…” → `#7`: *Cullenのこけた頬には、涙がながく伝い落ちた* | — |  |  |
| 4-14 | `4.12#8`–`#12` | D | T1 | `t4_confession_tape`, `push` | **頭を下げて告白した** · *「私はただ、彼らの苦しみに終止符を打てればよかっただけです」* → `#12`: **偽りの仮面が崩壊し、16年間の殺人を語り始めた** | Tiếng còng tay | ⊘ |  |
| 4-15 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第5幕* · **法廷、制度的沈黙への警鐘、そして終幕** | — | ⊘ | ◼ |
| 5-01 | `5.02#1`–`#2` | H | T5 ngày | `t4_somerset_courtroom` | **2006年3月** · *サマセット郡高等裁判所 · Paul W. Armstrong判事* | — | ✦ Cú |  |
| 5-02 | `5.02#3`–`#4` | H | T1 | `t4_judge_gavel`, `push` | **連続する11件の終身刑** · *さらに7件の終身刑が加わり合計18件の終身刑 · 最低刑期397年* | Tiếng búa tòa | ⊘ |  |
| 5-03 | `5.02#5`–`#7` | H | T1 | `t4_trenton_state_prison` | **ニュージャージー州立刑務所 (トレントン)** · *外界とは完全に隔絶された場所で服役中* | — | ⊘ |  |
| 5-04 | `5.03` (nghỉ 1.5 s) | — | — | giữ 5-03 | — | — | ⊘ |  |
| 5-05 | `5.04#1`–`#2` | H | T1 | `t4_institutional_bystander` | **なぜ16年間も阻止されなかったのか？** · *9つの医療機関を渡り歩き、誰も彼を止めようとしなかった* | — | ✦ Cú |  |
| 5-06 | `5.04#3`–`#4` | H | T2 | `t4_cullen_law_doc` | *ニュージャージー州が制定* · **CULLEN法** · *医療従事者の説明責任・報告強化法* | ở "Cullen法" | 🅑 |  |
| 5-07 | `5.04#5`–`#6` | H | T1 | `t4_red_flags_board` | **医療従事者の重大な不正行為に対する報告義務** → `#6`: **組織に潜む捕食者についての4つの赤い警告 (RED FLAGS)** | — | →C |  |
| 5-08 | `5.05#1`–`#2` | C | T9 `1/4` | `t4_redflag_savior` | **第1の兆候：偽の救済者症候群** · *危機時には最初の一人として現れる一方、仕事ぶりはきわめて曖昧* | — | ✦ Cáo |  |
| 5-09 | `5.05#3`–`#5` | C | T9 `2/4` | `t4_redflag_savior`, `push` | **第2の兆候：継ぎはぎの職歴と頻繁な転職** · *短期間の勤務を繰り返して職場を変え、明確な理由を示さずに去る* | — | →D |  |
| 5-10 | `5.06#1`–`#2` | D | T9 `3/4` | `t4_redflag_resumes` | **第3の兆候：権限を超えて管理システムを操作する不正行為** · *担当範囲外のデータにアクセスし、保管庫を開けた直後に取り消す* | — | ✦ Sói |  |
| 5-11 | `5.06#3`–`#4` | D | T9 `4/4` | `t4_redflag_resumes`, `push` | **第4の兆候：集団の異様な沈黙** · *管理部門が内々で処理し、法的な介入を避け、苦情をなだめようとする* | — | ⊘ | →H |
| 5-12 | `5.07` (nghỉ 1.5 s) | — | — | giữ 5-11 | — | — | ⊘ |  |
| 5-13 | `5.08#1`–`#3` | H | T1 | `t4_beacon_window` | **礼節の衣を纏った危険な悪** · *人々の無関心と沈黙の陰に隠れ、数百人の命を奪った* | — | ✦ Cú |  |
| 5-14 | `5.08#4`–`#6` | H | T1 | `t4_beacon_window`, `push` | **生命の聖厳さを守る灯台** · *看護師Amy Loughrenの勇気と、妥協を許さない堅固な意志* | — | ⊘ |  |
| 5-15 | `5.09` (nghỉ 1.5 s) | — | — | `t4_case_file_open` | — | Tiếng gấp hồ sơ | ⊘ |  |
| 5-16 | `5.10#1`–`#2` | H | T1 | `t4_case_file_open` | **リスナーの皆様へ心より感謝申し上げます** · *最後までご視聴いただき誠にありがとうございました* | — | ✦ Cú |  |
| 5-17 | `5.10#3` | H | T1 | `t4_case_file_open`, `still` | **常に警戒を怠らず、大切な人の安全を大事に** · *次回の犯罪心理分析ファイルでお会いしましょう* | Tiếng tắt máy ghi âm | 🅑 |  |
| 5-18 | hết tập (10 s) | — | T1 | `t4_case_file_open` | *事件記録 第04話 · 終了* · **AMBER EYES** · *実際の事件記録から読み解く犯罪心理学* | Nhạc fade out | ⊘ | ◼ |

**Tổng: 86 shot** (Hồi 1: 20 shot · Hồi 2: 20 shot · Hồi 3: 13 shot · Hồi 4: 15 shot · Hồi 5: 18 shot) · Phủ 100% 166/166 câu · 100% nền có file · chữ trên hình lấy từ câu đang đọc (H6).
