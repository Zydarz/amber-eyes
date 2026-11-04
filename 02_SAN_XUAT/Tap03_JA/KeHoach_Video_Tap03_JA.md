# HỒ SƠ SẢN XUẤT TẬP 03 · BẢN TIẾNG NHẬT · 「第03話：IQ 145の怪物と心を探る鏡」 (PHẦN B)

> **TRẠNG THÁI: ĐÃ DỰNG XONG VIDEO TẬP 03 BẢN TIẾNG NHẬT + QC ĐẦU RA ĐẠT TOÀN BỘ (32/32 CỔNG)**
>
> **Thành phẩm:** `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4` — 1927,900 s (0:32:07,90) · 57.837 khung · h264 1920×1080@30 + AAC 48 kHz stereo · 650,3 MB.
> **Báo cáo QC:** `02_SAN_XUAT/Tap03_JA/BaoCao_QC_Tap03_JA_20261103.md`
> **Số đo chính:** lệch timeline **0,010 s** (H14) · true peak **−3,3 dBFS** (A7) · LUFS **−16,3** · lệch A/V **0,0 ms** (A11 #64) · giải mã **0 lỗi** · ảnh tĩnh ↔ khung hình thật **110/110 khớp** (MAE TB 3,86) · mô tả **2.658 ký tự / 24 link nguồn**.
> **Việc còn lại của người dùng:** nghe duyệt · quyết định về nhãn vai riêng cho bản JA (mục 8 của báo cáo) · dọn đĩa theo `AGENTS.md` §11 **sau khi đăng**.

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md` (Bản 1, 02/11/2026), `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` (§4.4), `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`.
**Kịch bản:** `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md` · **Thành phẩm:** `02_SAN_XUAT/Tap03_JA/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md`.

---

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`, 218 câu, 55 elements) |
| Lượt nói / câu | 31 / **218 câu**. Host (H) 103 câu (47%) · Điều tra viên (D) 56 câu (26%) · Chuyên gia (C) 41 câu (19%) · Trực ban (N1) 9 câu (4%) · Cảnh sát quán rượu (N2) 9 câu (4%). Mã câu trùng 100% bản VN (`script_tap03_JA.json`) |
| N1 / N2 | `1.09` サンタクルーズ警察当直 (Cừu) / `2.09` 酒場の同僚警察官 (Mèo) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) vận hành trên Apple Silicon Mac qua MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (Apache-2.0, độc lập tiếng Nhật theo §4.4):<br>• **H (Cú):** `H_JA.wav` ← `assets/voice_ref_voxcpm2_ja2/H_jactrl_t01.wav` (123.1 Hz)<br>• **D (Sói):** `D_JA.wav` ← `assets/voice_ref_voxcpm2_ja3/D_smokerbass_ja3_t02.wav` (85.5 Hz)<br>• **C (Cáo):** `C_JA.wav` ← `assets/voice_ref_voxcpm2_ja3/C_deepalto_ja3_t03.wav` (228.6 Hz)<br>• **N1 (Cừu):** `N1_JA.wav` ← `assets/voice_ref_voxcpm2_ja3/W6_LOW_huskycontralto_ja3_t04.wav` (212.4 Hz)<br>• **N2 (Mèo):** `N2_JA.wav` ← `assets/voice_ref_voxcpm2_ja2/W5_HIGH_vnctrl_ja_t02.wav` (275.9 Hz) |
| Tách bạch cao độ (G9) | $\Delta_{\text{D}\to\text{H}} = 6.31\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) · $\Delta_{\text{H}\to\text{C}} = 10.72\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) |
| Đo CER | Chuẩn hóa hiragana qua `ja_cer.py` (pykakasi), median CER hiragana 4.55% |
| Đo MOS | `sarulab-speech/UTMOSv2` trên CPU (M5), trung bình 2.98 / 5.0 |
| Cắt đuôi câm (M3) | Tự động quét và cắt đuôi câm $> 0.8\text{ s}$ ở $-45\text{ dBFS}$, giữ $0.3\text{ s} + 30\text{ ms}$ fade-out |
| Thẻ cảm xúc (M4) | **CẤM tuyệt đối** mọi thẻ `<|emotion:...|>`; chỉ dùng ngắt nhịp `<|prosody:pause|>` sau `:` trước câu trích |
| Master Audio | `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp3` (44 MB, 1927.91 s ~ 32 phút 07.9 s)<br>• Integrated Loudness: **-16.2 LUFS** (chuẩn -16 ± 1 LUFS)<br>• True Peak: **-1.6 dBFS** (chuẩn ≤ -1.5 dBFS)<br>• LRA: **4.4 LU**<br>• Câm tuyệt đối > 0.3 s @ -60 dBFS: **0 lỗi (ĐẠT V4/A1)**<br>• Mốc lời đầu: **23.0 s** (chuẩn 22.8–23.5 s, intro nhạc 22.41 s)<br>• Mốc lời cuối kết thúc: **1918.9 s**, đuôi piano ấm fade out đến 1927.9 s |
| Phụ đề | `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA.srt` (238 cues, khớp 100% timeline hòa âm) |
| Video (thành phẩm) | `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4` — 1927,900 s · 57.837 khung = `int(1927,91 × 30)` · h264 1920×1080@30 + AAC 48 kHz stereo 197 kbps · 650,3 MB · faststart<br>• Dựng 100 % hình từ `timeline_s_JA_t03.json` + `shots_JA_t03.json` (110 shot) ⇒ H14 đạt (lệch 0,010 s)<br>• **32/32 cổng QC đạt** — xem `BaoCao_QC_Tap03_JA_20261103.md` |

---

## B2. Tiêu đề và Thẻ hồi tiếng Nhật

- **Tiêu đề YouTube:** `第03話 · IQ 145の怪物と心を探る鏡 | エドモンド・ケンパーの心理学 (サイコパス)`
- **Thumbnail:** Dòng 1: `IQ 145の` · Dòng 2: `怪物` · Nền: `t3_brain_mirror`
- **Tiêu đề các hồi (Act titles):**
  - **第1幕 ·** コロラドの電話ボックスから届く深夜の通話
  - **第2幕 ·** 現場と狩りの連鎖――代替の階段
  - **第3幕 ·** 心理剖検――内省型サイコパスの脳の内側
  - **第4幕 ·** FBIとの対話――犯罪プロファイリング技術の基礎
  - **第5幕 ·** 判決、赤い警鐘の教訓＆終幕

---

---

---

## 6. DANH SÁCH SHOT — TẬP 03 (JA)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

**Bản JA:** cột *Chữ* dùng tiếng Nhật chuẩn phát thanh tài liệu (Pillow vẽ chữ với `YuGothB.ttc` / `YuGothM.ttc`); các cụm `ở "…"` trong cột *Beat* là cụm tiếng Nhật **có thật** trong câu JA của shot đó (`phrase_time()` dò trong text câu để đặt thời điểm).

**Intro:** đặt `assets/brand/intro_kenh_JA_t03.mov` ở 0,00 s (sinh bằng `py -3 .work/make_intro.py` với `AE_LANG=ja AE_EP=03` — thẻ cảnh báo tiếng Nhật). Không câu thoại nào thuộc intro.
Renderer hiện ảnh intro ở 0,00–20,50 s; shot `1-00` (20,50 s → lời đầu 23,0 s) mở dần từ đuôi đen của intro.

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20.5 s → lời đầu 23.0 s) | — | T1 | `t3_phone_booth` hiện dần từ đen | *第1幕 · コロラドの電話ボックスから届く深夜の通話* | Tiếng gió rít, tiếng đồng xu, quay số | ⊘ |  |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t3_case_file` | **1973年4月24日** · *午前4時 · コロラド州プエブロ* | Gõ từng ký tự | ✦ Cú |  |
| 1-02 | `1.03#3`–`#4` | H | T1 | `t3_dispatch_desk` | *1,600キロメートル以上 · カリフォルニア州サンタクルーズ* · **当直電話のベルが静寂を破った** → `#4`: *向こうの男の声は低く温かく、奇妙なほど冷静だった* | — |  |  |
| 1-03 | `1.03#5`–`#6` | H | T1 | `t3_phone_booth`, `push` | **EDMUND KEMPER** · *道沿いの公衆電話から通話* → `#6`: **BIG ED** · *2メートル06 · 約127キログラム* | Tiêu đề ở "Big Ed" |  |  |
| 1-04 | `1.03#7` | H | T1 | `t3_bar_stool_shadow` | **THE JURY ROOMというバー** · *巡回勤務の後もビールを飲んで警察官たちと親しげに話した* | — |  |  |
| 1-05 | `1.03#8` | H | T1 | `t3_bedroom_door` | **そのわずか数日前のこと** · *彼は自分の母親を殺していた* | — | ⊘ |  |
| 1-06 | `1.04` (nghỉ 1.5 s) | — | — | giữ 1-05 | — | — | ⊘ |  |
| 1-07 | `1.05#1`–`#2` | H | T2 | `t3_dispatch_desk` | *サンタクルーズの夜勤当直* · **血の気が凍った言葉** | Dấu mộc ở "血の気が凍った" |  |  |
| 1-08 | `1.05#3`–`#4` | H | T4 lời kể | `t3_case_photos` | *INSIDE DETECTIVE 1973年8月号* → `#4`: “私は母と、その友人を殺しました。” | — | ⊘ |  |
| 1-09 | `1.05#5`–`#7` | H | T4 lời kể | `t3_case_file` | “そして、女子学生たちを殺しました。 6人でした。 私はあなたたちに、彼女たちの遺体をどこに埋めたか教えられます。” | — | ⊘ |  |
| 1-10 | `1.06` (nghỉ 1 s) | — | — | giữ 1-09 | — | — | ⊘ |  |
| 1-11 | `1.07#1`–`#3` | H | T1 | `t3_phone_booth` | **通話が切れると、彼はかけ直した** → `#2`: *さらに人を殺してしまうことを恐れていた* → `#3`: *数時間後、巡回車が公衆電話の横で止まった* | — |  |  |
| 1-12 | `1.07#4` | H | T1 | `t3_case_file` | **抵抗せず自首** · *車内に3丁の銃と数百発の弾薬* | Tiếng "Tách" (SFX `1.08`) ở cuối | →N1 |  |
| 1-13 | `1.09#1`–`#4` | N1 | T4 lời kể | `t3_dispatch_desk` mờ | “最初は、Edが酔っ払ってふざけるように電話をかけてきたのだと思っていました。” → `#4`: “私たちに人を派遣して家を確認するよう指示しました。” | — | ✦ Trực ban |  |
| 1-14 | `1.09#5`–`#6` | N1 | T4 lời kể | `t3_phone_booth` | → `#5`: “数時間後、プエブロ警察の巡回車が公衆電話の横に止まった。” → `#6`: “私たちはそこに座っていた彼を見つけましたが、コーヒーを買う列に並んでいる人のように平然としていました。” | — | 🅑 |  |
| 1-15 | `1.09#7`–`#9` | N1 | T4 lời kể | `t3_bar_stool_shadow` | “私たちは彼をサンタ・クルーズへ連れて行きました。” → `#9`: “長い間、カリフォルニア州全体が必死に探していた人物が、毎晩私たちのすぐ隣に座っていたのです。” | — | ⊘ |  |
| 1-16 | `1.10#1`–`#2` | H | T2 | `t3_apartos_house` | *オード・ドライブ609A番地 · アプトス* · **現場に突入** → `#2`: *Clarnell Strandberg · 52歳* | Dấu mộc ở "現場に突入" | 🅑 | ✂ |
| 1-17 | `1.10#3`–`#4` | H | T1 | `t3_bedroom_door` | *同じ日の午後 · Sara Taylor “Sally” Hallett · 59歳* → `#4`: **女子学生殺人魔** *(The Co-ed Killer)* | Tiêu đề ở "The Co-ed Killer" |  |  |
| 1-18 | `1.10#5`–`#6` | H | T1 | `t3_case_file`, `pull` | **警察の巧みな罠には捕まらなかった** → `#6`: *発見につながる痕跡を一切残さなかった* | — |  |  |
| 1-19 | `1.10#7`–`#11` | H | T4 lời kể | `t3_phone_booth` | **自ら公衆電話ボックスに入り、投降した** → `#10`: “私を止めてください。 私はそれをもう一度するつもりです。” | — | ⊘ |  |
| 1-20 | `1.10#12`–`#14` | H | T1 | `t3_prison_corridor`, `push` | **自分が止められなくなることを恐れて電話した** · *FBI捜査官の視点を聞く* | — | →D |  |
| 1-21 | `1.11`–`1.12` (nghỉ 2 s) | — | — | `t3_gate_slam` | — | Tiếng bước chân, cửa sắt "Rầm" | ⊘ |  |
| 1-22 | `1.13#1`–`#2` | D | T1 | `t3_giant_doorway` | **FBIの犯罪記録史上、唯一無二のケース** · *身長2メートル06 · IQ 145 · 地球上でも最も賢い0.13％の集団* | — | ✦ Sói |  |
| 1-23 | `1.13#3`–`#4` | D | T1 | `t3_brain_mirror` | **非凡な自己認識能力** · *置かれた状況をかばうことも、罪を否定することもしなかった* | — |  |  |
| 1-24 | `1.13#5`–`#6` | D | T2 | `t3_fbi_corridor` | *BSU · FBI* · **犯罪性格研究プロジェクト** · *Criminal Personality Research Project · 行動科学部門の最初の研究者* | Dấu mộc ở "Criminal Personality Research Project" |  |  |
| 1-25 | `1.13#7`–`#9` | D | T8 | `t3_case_file` | *36人の連続殺人犯 · VICAPネットワークの土台 · 標準化された科学* | Mỗi mục ở cụm từ |  |  |
| 1-26 | `1.15#1`–`#2` | H | T10 | `t3_brain_mirror` | **IQ 145の巨漢と、内なる怪物を読み解く鏡** | Tên tập ở cuối | 🅑 |  |
| 1-27 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第2幕* · **現場と狩りの連鎖――代替の階段** | — | ⊘ | ◼ |
| 2-01 | `2.02#1` | H | T1 | `t3_rain_wipers` | **1970年代初め · サンタ・クラルズ** · *ヒッピー運動の自由な空気* | Mưa rả rích, gạt nước |  |  |
| 2-02 | `2.02#2` | H | T1 | `t3_hitchhiker` | **ヒッチハイキング** · *親指を立てて道を尋ねる · 当時一般的で、表面上は害のない文化* | Tiêu đề ở "Hitchhiking" |  |  |
| 2-03 | `2.02#3` | H | T1 | `t3_ucsc_campus` | **UCSC** · *不可解な失踪の影が構内全体を覆い始めた* | — |  |  |
| 2-04 | `2.04#1`–`#2` | H | T2 | `t3_case_photos` | **行方不明者たちのファイル** · *連続殺人事件の6人の被害者* | Lật ảnh (SFX `2.03`) ở đầu | 🅑 | ✂ |
| 2-05 | `2.04#3`–`#4` | H | T8 | `t3_santacruz_street` | *1972年5月7日 · Mary Ann PesceとAnita Luchessa（いずれも18歳） · 1人を制圧し、もう1人を車のトランクに閉じ込めた* | Mỗi mục ở cụm từ |  |  |
| 2-06 | `2.04#5`–`#6` | H | T8 | `t3_case_photos` | *1972年9月14日 · Aiko Koo（15歳） · 1973年1月7日 · Cindy Schall（18歳）* | — | ⊘ |  |
| 2-07 | `2.04#7`–`#8` | H | T1 | `t3_backyard_garden` | *海へ逃げた* → `#8`: **母親の庭に遺体を埋めた** | — | ⊘ |  |
| 2-08 | `2.04#9` | H | T1 | `t3_ucsc_campus` | **UCSCの女子学生2人** · *Rosalind Thorpe（23歳）とAlice Liu（21歳）* | — |  |  |
| 2-09 | `2.05` (nghỉ 1.5 s) | — | — | giữ 2-08 | — | — | ⊘ |  |
| 2-10 | `2.06#1` | H | T1 | `t3_ravine` | **サンタ・クリアズ山地** · *遺体は深い峡谷に散らばって発見された* | — | ⊘ |  |
| 2-11 | `2.06#2` | H | T1 | `t3_backyard_garden` | **母親の庭に埋められた** · *母の寝室の窓に正対するように* | — | ⊘ |  |
| 2-12 | `2.06#3`–`#5` | H | T1 | `t3_case_photos` | **法医学的な痕跡は皆無** · *指紋も、見慣れない繊維も、目撃者もいなかった* | — | →D |  |
| 2-13 | `2.07#1` | D | T1 | `t3_under_seat` | **動く死の罠** · *精緻なModus Operandi* | — | ✦ Sói |  |
| 2-14 | `2.07#2`–`#5` | D | T1 | `t3_galaxie` | **1969年型 · 黄色いFord Galaxie** · *大学の職員用駐車場のステッカー · 誰にも目立たない安全な車* | Tiêu đề ở "Ford Galaxie" |  |  |
| 2-15 | `2.07#6`–`#7` | D | T8 | `t3_trunk` | *トランクには全てを前もって用意 · 1人を手錠で拘束し、もう1人を閉じ込めた* | — | ⊘ |  |
| 2-16 | `2.07#8`–`#9` | D | T1 | `t3_case_file` | *ネバダ州レノのレンタカーに3丁の銃と200発を超える弾薬* | — |  |  |
| 2-17 | `2.07#10`–`#12` | D | T3 so sánh | `t3_bar_stool_shadow` | *巨大な体格 2メートル06* · **知性の仮面と偽りの礼儀** · *静かで穏やかな声 · 知性的な眼鏡 · 端正な服装* | Cột phải ở `#12` |  |  |
| 2-18 | `2.07#13`–`#14` | D | T5 | `t3_hitchhiker` | **約150人** · *犯行前にリハーサルとして人を乗せていた* | Số đếm 0 → 150 |  |  |
| 2-19 | `2.08#1`–`#3` | H | T1 | `t3_courthouse_exterior` | **最大の疑問：** *なぜ自分を追い詰めている人々と友人になれたのか？* | — | →N2 |  |
| 2-20 | `2.09#1`–`#3` | N2 | T1 | `t3_bar_jury_room` | **THE JURY ROOM** · *Santa Cruz地方裁判所の真正向かい* → `#2`: “Big Edは、いつもいつものバーの隅に座っていた。” | — | ✦ Cảnh sát |  |
| 2-21 | `2.09#4`–`#6` | N2 | T4 lời kể | `t3_bar_stool_shadow` | → `#4`: “Big Edは、警察官になることすら考えていました。” → `#5`: “しかし、ああした体格では、どこからも採用してもらえませんでした。” | — | 🅑 |  |
| 2-22 | `2.09#7`–`#9` | N2 | T4 lời kể | `t3_bar_stool_shadow`, `push` | → `#7`: “Edはビールを飲みながらうなずき、分析しながら、殺人者の心理に関する仮説も示してくれました。” → `#8`: “あの者は、私たちと一緒にビールを飲みながら、その追跡そのものについて冗談を言っていたのです。” | — | ⊘ |  |
| 2-23 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第3幕* · **心理剖検――内省型サイコパスの脳の内側** | — | ⊘ | ◼ |
| 3-01 | `3.02#1`–`#2` | H | T1 | `t3_basement_stairs` | **モンタナ州の湿った暗い地下室** · *1950年代 · 囚われた幼少期* | Nước nhỏ giọt, cello u ám |  |  |
| 3-02 | `3.03` (nghỉ 2 s) | — | — | giữ 3-01 | — | — | ⊘ |  |
| 3-03 | `3.04#1` | H | T1 | `t3_layers_stair` | *傾聴する：* **3つの病理層を深掘りする専門家の見解** | — | →C |  |
| 3-04 | `3.05#1`–`#2` | C | T2 | `t3_mother_shadow` | *有害な母子関係の病理* · **3層のメカニズム** · *先天的な反社会性人格* | Dấu mộc ở "Toxic Mother-Son Pathology" | ✦ Cáo |  |
| 3-05 | `3.05#3`–`#5` | C | T9 `1/3` | `t3_coal_furnace` | **第1層：地下の深淵** · *心理的去勢（Psychological Castration）* → **Clarnell Strandberg** · *アルコール依存 · 威圧的で支配的な性格* | Thuật ngữ ở đầu |  |  |
| 3-06 | `3.05#6` | C | T1 | `t3_small_bed` | **8歳から** · *石炭ストーブのそばの冷たい地下室で眠っていた* | — | ⊘ |  |
| 3-07 | `3.05#7`–`#8` | C | T1 | `t3_trapdoor` | **ダイニングテーブルの真下の落とし戸** · *テーブルを持ち上げなければ出られなかった* | — |  |  |
| 3-08 | `3.05#9`–`#12` | C | T1 | `t3_basement_stairs`, `still` | *醜悪な姿の侮辱で自己尊重を破壊* → `#12`: *異常で、忌むべき存在であり、生きるに値しない* | — |  |  |
| 3-09 | `3.06` (nghỉ 1.5 s) | — | — | giữ 3-08 | — | — | ⊘ |  |
| 3-10 | `3.07#1` | H | T1 | `t3_mother_shadow` mờ | **思春期における母親への憎しみはどう変わったのか？** | — | →C |  |
| 3-11 | `3.08#1`–`#3` | C | T9 `2/3` | `t3_atascadero` | **第2層：投射と代理被害者** · *15歳で祖父母を銃殺 · 1964年8月27日 · アタスカデロ* | — | 🅑 |  |
| 3-12 | `3.08#4`–`#6` | C | T8 | `t3_textbooks` | *アタスカデロで5年間 · MMPI尺度を自行開発 · 1969年12月18日（21歳の誕生日）に釈放* | Mỗi mục ở cụm từ |  |  |
| 3-13 | `3.08#7`–`#9` | C | T3 so sánh | `t3_mother_shadow` | *母親：権力の偶像と恐怖* · **代替の被害者を求めた脳** | Cột phải ở `#8` |  |  |
| 3-14 | `3.08#10`–`#13` | C | T1 | `t3_ucsc_campus` | **代理被害者** *(Proxy Victims)* · *自由への渇望を体現する若い女性たち* | — | ⊘ |  |
| 3-15 | `3.09` (nghỉ 2 s) | — | — | giữ 3-14 | — | — | ⊘ |  |
| 3-16 | `3.10#1` | H | T1 | `t3_brain_mirror` | *第3層* · **Kemperと他の連続殺人者との違い？** | — | →C |  |
| 3-17 | `3.11#1`–`#3` | C | T9 `3/3` | `t3_self_observation` | **理知的解離と異常な自己内省能力** · *The Introspective Psychopath ― IQ 145、初回の測定では136* | — | 🅑 |  |
| 3-18 | `3.11#4`–`#6` | C | T1 | `t3_brain_mirror` | **感情を完全に切り離した** · *渴望を科学者のように観察していた* | — | ⊘ |  |
| 3-19 | `3.11#7`–`#8` | C | T1 | `t3_bedroom_door` | **最後の一歩：** *実母を殺すため帰る* | — | ⊘ |  |
| 3-20 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第4幕* · **FBIとの対話――犯罪プロファイリングの基盤** | — | ⊘ | ◼ |
| 4-01 | `4.02#1`–`#3` | H | T5 ngày | `t3_vacaville_1978` | **1978年 · バカビル** · *カリフォルニア州立医療施設（CMF）* | Tiếng cassette "Cạch" (SFX `4.01`) | ✦ Cú |  |
| 4-02 | `4.02#4`–`#6` | H | T1 | `t3_two_agents` | **John Douglas & Robert Ressler** · *FBI行動科学部門（BSU）* | — |  |  |
| 4-03 | `4.02#7`–`#8` | H | T1 | `t3_interview_room` | **最大の疑問：** *私たちの脳は本当はどう動いているのか？* | — |  |  |
| 4-04 | `4.03` (nghỉ 1.5 s) | — | — | giữ 4-03 | — | — | ⊘ |  |
| 4-05 | `4.04#1` | H | T1 | `t3_fbi_corridor`, `push` | *傾聴する：* **FBI特別検査官の歴史的出会いを再現** | — | →D |  |
| 4-06 | `4.05#1`–`#3` | D | T1 | `t3_giant_doorway` | **巨大すぎて扉枠いっぱいに広がった** → `#3`: *大学教授のような声で話した* | — | ✦ Sói |  |
| 4-07 | `4.05#4`–`#7` | D | T1 | `t3_interview_room` | *IQ 145 · 彼が自分たちより賢いのではと心配した* → `#7`: *母親から残酷な扱いを受けた話をするときだけ涙が込み上げた* | — |  |  |
| 4-08 | `4.05#8`–`#11` | D | T1 | `t3_cassette` | **数時間続く作業セッション** · *数年にわたる多次の面接* | — | 🅑 |  |
| 4-09 | `4.05#12`–`#16` | D | T4 lời kể | `t3_interview_room` | → `#15`: “その後、私は他の人を助けられる方法を見つけられることを願っています――おそらく、彼らは私を研究し、私のような人が私たちが行うことの原因を探り当てられるでしょう” | — |  |  |
| 4-10 | `4.05#17`–`#19` | D | T2 | `t3_fbi_corridor` | *Criminal Personality Research Project* · **36人の性犯罪殺人犯** · *1985年のVICAPネットワーク* | Lật sổ (SFX `4.06`) ở đầu |  |  |
| 4-11 | `4.07#1` | D | T1 | `t3_interview_room`, `still` | **性格を左右する3つの概念** | — |  |  |
| 4-12 | `4.07#2`–`#5` | D | T9 `1/3` | `t3_fantasy_spiral` | **概念01：暴力妄想サイクル** *(Violent Fantasy Cycle)* | — |  |  |
| 4-13 | `4.07#6`–`#7` | D | T9 `2/3` | `t3_trophy_box` | **概念02：戦利品** *(Trophies/Souvenirs)* · *絶対的な権力感の再体験* | — |  |  |
| 4-14 | `4.07#8`–`#10` | D | T9 `3/3` | `t3_phone_booth` | **概念03：犯罪を止めた理由** · *止まれないことへの恐怖* | — | ⊘ |  |
| 4-15 | `4.08#1`–`#3` | H | T3 so sánh | `t3_organized_split` | **組織型の殺人者** *(Organized)* · *vs 非組織型（Disorganized）* · *The Lust Murderer（1980）* | Cột phải ở `#2` | ✦ Cú |  |
| 4-16 | `4.08#4`–`#5` | H | T9 | `t3_signature_trace` | **心理的署名** *(Behavioral Signature)* · *物理的痕跡とともに犯罪者に残るもの* | — |  |  |
| 4-17 | `4.08#6`–`#7` | H | T1 | `t3_brain_mirror` | *古典作品へのひらめき：* **羊たちの沈黙 ＆ MINDHUNTER** | — | 🅑 |  |
| 4-18 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第5幕* · **判決、赤い警鐘の教訓＆終幕** | — | ⊘ | ◼ |
| 5-01 | `5.01`–`5.02#1` | H | T5 ngày | `t2_gavel` | **1973年10月23日** · *サンタ・クルーズ郡高等裁判所* | Búa gõ (SFX `5.01`) ở đầu | ✦ Cú |  |
| 5-02 | `5.02#2`–`#4` | H | T2 | `t3_courtroom_1973` | *検察官Peter Chang* · **8件の判決を同時執行** · *Harry Brauer判事* | Dấu mộc ở "判決8件を同時執行" |  |  |
| 5-03 | `5.02#5`–`#6` | H | T1 | `t3_courtroom_1973`, `push` | **司法史上例のない要求：** *拷問によって死ぬまで処刑される死刑* | — | ⊘ |  |
| 5-04 | `5.02#7`–`#10` | H | T8 | `t3_life_sentence` | *CMFバカビル · 赦免申請は10回を超えて却下 · 次回は2031年* | Mỗi mục ở cụm từ |  |  |
| 5-05 | `5.02#11`–`#12` | H | T4 lời kể | `t3_life_sentence`, `still` | “社会は、いかなる形でも私を受け入れる準備ができていません。 そのことについて彼らを責めるつもりはありません。” | — | ⊘ |  |
| 5-06 | `5.03` (nghỉ 2 s) | — | — | giữ 5-05 | — | — | ⊘ |  |
| 5-07 | `5.04#1` | H | T1 | `t3_red_flags` | **4つの赤い警告** *(Red Flags)* · *暴力的な人格の初期形成を早期に発見する* | — | →C+D |  |
| 5-08 | `5.05#1`–`#3` | C | T9 `1/4` | `t3_red_flags` | **兆候01：Macdonald Triad** · *意図的な動物虐待 · 放火癖 · 異常に長引く遺尿* | — | ✦ Cáo |  |
| 5-09 | `5.05#4`–`#6` | C | T1 | `t3_small_bed` | **動物虐待の反復** · *10歳で飼い猫を虐待 · 3年後に別の猫でも繰り返す* | — | ⊘ |  |
| 5-10 | `5.05#7`–`#8` | C | T9 `2/4` | `t3_basement_stairs` | **兆候02：極端な心理的虐待** · *閉ざされた空間に隔離 · 長期にわたり人の尊厳を踏みにじること* | — |  |  |
| 5-11 | `5.06#1`–`#2` | D | T9 `3/4` | `t3_fantasy_spiral` | **兆候03：現実から切り離された暴力の幻想世界** · *支配の幻想 · 武器の収集 · 病的な研究に没頭* | — | ✦ Sói |  |
| 5-12 | `5.06#3`–`#4` | D | T9 `4/4` | `t3_self_observation` | **兆候04：高い知性と冷たさ** · *Shallow Affect — 自己防御としての理屈* | — |  |  |
| 5-13 | `5.07` (nghỉ 2 s) | — | — | `t3_closing_desk` | — | Nhạc piano dâng lên nhẹ nhàng | ⊘ |  |
| 5-14 | `5.08#1`–`#3` | H | T1 | `t3_closing_desk`, `pull` | **人間味に富んだ細部：** *刑務所の看守 · 警察副署長Bruce Colomy* | — | ✦ Cú |  |
| 5-15 | `5.08#4`–`#5` | H | T4 lời kể | `t3_courtroom_1973` | “私にとって、かつて持っていたかった父親です” | — | 🅑 |  |
| 5-16 | `5.08#6`–`#8` | H | T1 | `t3_gift_drowned` | **天才的な脳と卓越した体力** → `#8`: *虐待と憎悪に満ちた水槽に沈められ、凶悪な破壊兵器へ* | — | ⊘ |  |
| 5-17 | `5.08#9`–`#11` | H | T1 | `t3_life_sentence` | **悪を鉄格子の向こうに閉じ込めるのは法の責任** → `#11`: *子どもの心の傷を家庭内で認め、守り、癒すことこそ唯一の方法* | — | 🅑 |  |
| 5-18 | `5.09` (nghỉ 1.5 s) | — | — | giữ 5-17 | — | — | ⊘ |  |
| 5-19 | `5.10#1`–`#2` | H | T1 | `t3_closing_desk` | **専門家とリスナーへの感謝** · *犯罪心理学の分析ファイル* | — | 🅑 |  |
| 5-20 | `5.10#3` | H | T1 | `t3_brain_mirror`, `push` | **愛を絶やさず、子どもに耳を傾けよう** · *次の『犯罪心理学の解剖』エピソードでまたお会いしましょう* | — |  |  |
| 5-21 | `5.11`–`5.12` (hết tập) | — | T10 | `t3_closing_desk` | **AMBER EYES** · *次回のエピソードをお楽しみに* | Đóng hồ sơ, tắt cassette, cello fade out | ⊘ | ◼ |
**Tổng: 110 shot — 93 shot có lời + 17 khoảng nghỉ / chuyển cảnh**
**Tổng:** 110 shot — 93 shot có lời + 17 khoảng nghỉ / chuyển cảnh (bản JA giữ nguyên cột Câu, Vai, Mẫu, Nền, Nhân vật; chỉ thay cột *Chữ* và cụm `ở "…"` trong cột *Beat*).
