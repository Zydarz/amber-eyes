# HỒ SƠ SẢN XUẤT TẬP 01 · BẢN TIẾNG NHẬT · 「母の愛という名の毒薬」 (PHẦN B)

> **TRẠNG THÁI: CHỜ DUYỆT GIỌNG ĐỌC & DỰNG**

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản:** `01_KICH_BAN/Tap01_JA/kichban_tap01_JA.md` · **Chữ cố định:** `00_TIEU_CHUAN/CHU_CO_DINH_JA.md` · **Thành phẩm:** `02_SAN_XUAT/Tap01_JA/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md`. Bảng shot giữ nguyên các cột Câu, Vai, Mẫu, Nền, Nhân vật và mô tả beat; chỉ thay:
- cột **Chữ** sang tiếng Nhật chuẩn phát thanh tài liệu (Pillow vẽ chữ với `YuGothB.ttc` / `YuGothM.ttc`);
- các cụm `ở "…"` trong cột **Beat** sang cụm tiếng Nhật **có thật** trong câu JA tương ứng.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap01_JA/kichban_tap01_JA.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`, 128 câu, 33 lượt nói, passed `_qc_ja.py`) |
| Lượt nói / câu | 33 / **128**. Host 50% · Chuyên gia 24% · Điều tra viên 20% · Người bình thường 5%. Mã câu trùng 100% bản VN (`script_tap01_JA.json`) |
| N1 / N2 | `1.07` 証人 (Cừu) / `4.03` 視聴者 (Mèo) |
| Bảng shot | 122 dòng = 104 shot có lời + 18 dòng không lời |
| Nền dùng | 45 ảnh `assets/bg/` (dùng lại 100% của bản VN/EN) |
| Giọng dự kiến | H `Japanese_GentleButler` 0.95 · D `Japanese_SeriousCommander` 0.97 · C `Japanese_DependableWoman` 0.95 · N1 `Japanese_KindLady` 0.95 · N2 `Japanese_DecisivePrincess` 0.95 |

## B3. Ánh xạ riêng (trong `parse_shots.py`)

Giống hệt bản VN (`COMBO`, `BG2`, `INSET`), vì số hiệu shot và nền không đổi.

## 6. DANH SÁCH SHOT — TẬP 01 BẢN TIẾNG NHẬT

**Đọc bảng:** *Vai* = người đang nói (H ホスト · D 捜査官 · C 心理学者 · N1 証人 · N2 視聴者).

## 6. DANH SÁCH SHOT — TẬP 01 (bảng mẫu, viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X (hiện badge chờ) · `✦` = lần đầu xuất hiện (thẻ giới thiệu) · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` (chỉ hình, shot I-01 → I-04, chi tiết ở A5.7) ở 0,00 s. Không câu thoại nào thuộc intro.

### 第1幕 — 信頼が崩れる瞬間 · nền chủ đạo `house_night`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s, chồng lên phần đen cuối intro) | — | T1 | `house_police` hiện dần từ đen, `push` | *第1幕 · 信頼が崩れる瞬間* | Đèn cảnh sát quét; drone dâng | ⊘ | |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `house_night` mờ | **2015年6月14日** · *ミズーリ州スプリングフィールド* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T11 | `phone_dark` | *母娘の共同SNSアカウント* → **街全体を息を呑ませた1行のステータス** | Bài đăng hiện dạng các dòng mờ, không đọc được chữ, ở "短く不吉な" | | |
| 1-03 | `1.04` (nghỉ 2 s) | — | — | giữ 1-02, ánh đỏ nhấp nháy | — | — | | |
| 1-04 | `1.05#1` | H | T1 | `house_police` + `crowd` | **パステルピンクの小さな家** · *ミズーリ州スプリングフィールド* (番地は画面に表示しない — 個人宅) | — | | |
| 1-05 | `1.05#2` | H | T1 | `house_night`, `pull` | *次は:* **同じ通りに住む住民** | — | →N1 | |
| 1-06 | `1.07#1` | N1 | T4 lời kể | `house_night` ấm, mờ | “聖なる母の愛の象徴” | — | ✦ Cừu | |
| 1-07 | `1.07#2` | N1 | T8 | `wheelchair_room` + `deedee_wheelchair` | *街全体が信じていたこと* · *腰から下の麻痺 · 白血病 · 筋ジストロフィー · 重度のてんかん · 知能は7歳程度* | Mỗi mục tại cụm từ | | |
| 1-08 | `1.07#3` | N1 | T4 lời kể | `house_night` ấm | “この町の誰もが感動と称賛の涙を流した” | — | 🅑 | |
| 1-09 | `1.08#1` | H | T1 | `bedroom_door` | **母親は死亡していた** | — | | |
| 1-10 | `1.08#2` | H | T1 | `empty_room`, `still` | **GYPSY ROSEは姿を消した** | — | ⊘ | ✂ |
| 1-11 | `1.08#3`–`#4` | H | T1 | `wheelchair_room` | **車椅子 · 酸素ボンベ · 数十本の薬瓶** | `#3` sáng xe lăn, `#4` sáng kệ | | |
| 1-12 | `1.08#5` | H | T3 | `wheelchair_room` tối + dấu `?` lớn | *全米が問う* · **母親の死を招いたのは一体誰なのか？** | — | | |
| 1-13 | `1.08#6` | H | T1 | `interrogation`, `push` | *次は:* **事件担当の捜査官** | — | →D | |
| 1-14 | `1.09`–`1.10` (nghỉ 2 s) | — | — | giữ 1-13, nhiễu bộ đàm `cold` | — | — | ⊘ | |
| 1-15 | `1.11#1` | D | T2 | `pinboard` | **全国指名手配・捜索令** | Dấu mộc ở "全国に捜索令" | ✦ Sói | |
| 1-16 | `1.11#2` | D | T7 | `route_night` | **その翌日** · *ウィスコンシン州 — 数百マイル彼方* | Đường tự vẽ, số đếm | | |
| 1-17 | `1.11#3`–`#4` | D | T1 | `interrogation` + `gypsy_stand` | **彼女は自力で歩いていた** | Đèn treo sáng ở `#4` | | |
| 1-18 | `1.11#5`–`#7` | D | T8 gạch bỏ | giấy hồ sơ trên `records` | *白血病 · 筋ジストロフィー · 脳損傷* | Mỗi câu gạch một mục | | ✂ |
| 1-19 | `1.11#8` | D | T1 `hero` | `bedroom_door` + `gypsy_stand`, tối dần | **彼女の小さな愛娘** | Tiêu đề ở "小さな愛娘" | 🅑 P2 | |
| 1-20 | `1.13#1` | H | T1 | `podcast_desk`, cassette quay | **犯罪心理プロファイリング・ケースファイル** | "Tách" ở đầu | 🅑 | |
| 1-21 | `1.13#2` | H | T9 → T10 | `house_night` | **代理型ミュンハウゼン症候群** → *第01話 · 母の愛という名の毒薬* | Thuật ngữ ở "代理型ミュンハウゼン症候群"; tên tập cuối câu | | |
| 1-22 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第2幕* · **精神刑務所での23年間** | — | ⊘ | ◼ |

### 第2幕 — 犯罪現場＆診療記録 · nền chủ đạo `wheelchair_room`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `bedroom_door` | **寝室ではない** · *2015年6月* | Tiêu đề ở `#2` | | |
| 2-02 | `2.02#3` | H | T5 | `wheelchair_room` + `gypsy_wheelchair` | *本当の事件現場* · **23年間** | Số đếm | | |
| 2-03 | `2.04#1`–`#5` | H | T6 | `records`, `pan` | *1991年 · 完全に健康な誕生* → *生後3ヶ月 · 睡眠時無呼吸症* → *捏造された病歴の始まり* → *7歳 · 脊髄損傷 · 車椅子* → *丸刈り頭 · 白血病の化学療法* | Mỗi câu một mốc | ⊘ | |
| 2-04 | `2.06#1` | H | T1 | `clinical` | **単なる嘘にとどまらない** | — | 🅑 | |
| 2-05 | `2.06#2` | H | T2 | `records` | **数千ページの診療記録** · *Gypsyの身体への直接的な医療介入* | — | | |
| 2-06 | `2.06#3` | H | T1 | `pinboard` mờ, `push` | *次は:* **捜査官による記録の開示** | — | →D | |
| 2-07 | `2.07#1` | D | T2 | `pinboard` | **医療記録に残された3つの痕跡** | Bộ đếm `0/3` | | |
| 2-08 | `2.07#2` | D | T3 `1/3` | `wheelchair_room` cận kệ thuốc | **高用量の抗てんかん薬** · *てんかんではないにもかかわらず* | Phụ ở "てんかんではない" | | |
| 2-09 | `2.07#3` | D | T3 `2/3` | `clinical` | **胃への栄養チューブ** | — | | |
| 2-10 | `2.07#4` | D | T3 `3/3` | `clinical` tối | **不要な手術** · *医師の前で作られた偽りの症状に基づく* | — | | |
| 2-11 | `2.07#5` | D | T5 | `clinical` + lưới ~100 biểu tượng bác sĩ (Pillow) | **数百人の医師** · *誰も気づかなかったのか？* | Biểu tượng hiện dần | | |
| 2-12 | `2.07#6` | D | T9 | `pinboard`, `pull` | **行動原理** *(Modus Operandi)* | 3 thẻ trống ghim lên | 🅑 | |
| 2-13 | `2.07#7` | D | T2 trên bảng ghim | camera dời tới thẻ 1 | *01* · **かつて看護助手** · *医療用語を熟知していた* | — | | |
| 2-14 | `2.07#8`–`#9` | D | T2 trên bảng ghim | thẻ 2 có ảnh `storm` thu nhỏ | *02 · 2005年* · **ハリケーン・カトリーナ** → `#9`: *病歴はすべてDee Dee本人の口述によるもの* | Dây đỏ nối ở `#9` | | |
| 2-15 | `2.07#10` | D | T2 trên bảng ghim | thẻ 3 + ghi chú Consolas | *03* · **疑いを持たれたら → 病院を変え、引っ越す** · *Dr. Bernardo Flasterstein · 2007年* (文字のみ, V5) | Kéo ra thấy cả bảng | | |
| 2-16 | `2.09#1`–`#2` | H | T1 | `house_closed` | **窓は常に固く閉ざされていた** · *学校に通わせてもらえなかった* | Tiếng khoá cửa ở đầu | | |
| 2-17 | `2.09#3` | H | T5 | `house_closed` mờ | **−4歳** · *永遠に未成年でいさせるための年齢詐称* | — | | |
| 2-18 | `2.09#4` | H | T1 | `house_night` + bóng song sắt ghép từ lọ thuốc, ống truyền (Pillow) | **鉄格子のない刑務所** | Song sắt ở "処方箋" | | |
| 2-19 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第3幕* · **FDIA犯罪者の脳の内部** | — | ⊘ | ◼ |

### 第3幕 — 心理剖検――FDIA犯罪者の脳の内部 · nền chủ đạo `clinical`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T5 | `void`, `still` | *すべての根底にある問い* · **なぜ？** | Đúng ở "なぜ？" | ⊘ | ✂ |
| 3-02 | `3.02#2` | H | T1 | `fog` + `deedee_wheelchair` | **寄付基金 · チャリティーハウス · 無料の旅行** | — | | |
| 3-03 | `3.02#3`–`#4` | H | T3 | `charity` | **金銭は単なる副次的な利益に過ぎない** | Đồng xu mờ ở `#4` | | |
| 3-04 | `3.02#5` | H | T9 | `brain_desk` | **代理型ミュンハウゼン症候群** · *DSM-5-TR: 他者に課す虚偽性障害 (FDIA)* | Dòng DSM ở "DSM-5-TR" | | |
| 3-05 | `3.03` (nghỉ) | — | — | giữ 3-04 | *次は:* **犯罪心理学の専門家** | — | | |
| 3-06 | `3.04#1`–`#2` | H | T1 | `brain_desk`, `push` | **病気詐称 (Malingering)** · *利益や責任逃れが目的* → **虚偽性障害 (Factitious Disorder)** · *病気そのものの役割を求める心理的動機* | — | →C | |
| 3-07 | `3.05#1` | C | T9 | `brain_desk` + sơ đồ `brain3` | **注意 · 同情 · 感情的な崇敬** | 3 vòng sáng lần lượt | ✦ Cáo | |
| 3-08 | `3.05#2` | C | T4 | `brain_desk` tối, tầng 1 sáng + `halo` | **内的な利益** *(Internal Incentive)* | — | | |
| 3-09 | `3.05#3`–`#4` | C | T3 so sánh | `brain_desk` mờ | **3層の心理の深淵** | Cột phải ở `#4` | | |
| 3-10 | `3.05#5`–`#6` | C | T1 | `fog` + `deedee_wheelchair` mờ | *第1層* · **悪性自己愛 (Malignant Narcissism)** · *「完璧な犠牲的母親」という仮面* | Tiêu đề ở `#6` | | |
| 3-11 | `3.05#7` | C | T1 | `spotlight` + `deedee_wheelchair` | **突然、宇宙の中心になった** | Đèn bật ở "突然" | | ✂ |
| 3-12 | `3.05#8` | C | T1 | `spotlight` + biểu tượng bác sĩ, hàng xóm, tờ báo | **依存的な賞賛への渇望** | Mỗi biểu tượng ở cụm từ | | |
| 3-13 | `3.05#9` | C | T5 | `void` + đường nhịp tăng vọt | *第2層* · **見捨てられることへの病的な恐怖** · *絶対的な支配への固執* | Nhịp nhấp nháy | 🅑 P2 | |
| 3-14 | `3.06` (nghỉ) | — | — | tối dần | **子供は成長し、去っていく** | — | | |
| 3-15 | `3.07#1` | H | T1 | `brain_desk` | **永久に手元に縛り付ける方法とは？** | — | | |
| 3-16 | `3.07#2` | H | T2 | `records` | **「病気で、母に完全に依存している」と信じ込ませる** | — | →C | |
| 3-17 | `3.08#1` | C | T9 | `brain_desk`, tầng 2 sáng | **娘の人生を完全に掌握する唯一の人物** | — | | |
| 3-18 | `3.08#2`–`#4` | C | T3 | `hands` | — | 3 beat | | |
| 3-19 | `3.08#5` | C | T1 `hero` | `void`, tối dần | *第3段階* · **人格の消去のシグネチャ** *(Signature)* | Tiêu đề ở "思い信じさせる" | ⊘ | |
| 3-20 | `3.08#6` | C | T3 | `wheelchair_room` + `gypsy_wheelchair` | **丸刈りの頭 · 子ども用のドレス** · *20歳を過ぎても* | — | | |
| 3-21 | `3.09` (nghỉ) | — | — | giữ 3-20 | **大人になることの剥奪** *(Infantilization)* | — | | |
| 3-22 | `3.10#1` | C | T9 | `brain_desk`, tầng 3 sáng | **女性としての発達を一切拒絶した** | — | | |
| 3-23 | `3.10#2` | C | T3 | `dress_hanger` | **永遠に7歳の磁器人形** | — | | |
| 3-24 | `3.10#3`–`#4` | C | T9 | `dress_hanger` mờ | **極度の知能 · 精緻な手腕 · 卓越した説得力** | Thuật ngữ ở `#4` | 🅑 | |
| 3-25 | `3.10#5`–`#6` | C | T1 | `doll` | **完璧な愛の仮面** | Tiêu đề ở "磁器人形" | | |
| 3-26 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第4幕* · **尋問＆転換点――なぜGYPSYは逃げなかったのか？** | — | ⊘ | ◼ |

### 第4幕 — 尋問＆転換点――なぜGYPSYは逃げなかったのか？ · nền chủ đạo `interrogation`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` | H | T1 | `night_screen` + bong bóng bình luận mờ (Pillow, không tên) | *社会の最大の疑問* · **なぜ立ち上がって走り出さなかったのか？** | — | | |
| 4-02 | `4.02#2` | H | T1 | `night_screen`, `push` | **完全に歩くことができた** · *鉄格子のない家* | — | →N2 | |
| 4-03 | `4.03#1` | N2 | T4 lời kể | `night_screen` | *次は:* **事件を見守る視聴者の視点** | — | ✦ Mèo | |
| 4-04 | `4.03#2`–`#3` | N2 | T4 lời kể | `wheelchair_room` tối, xe lăn trống dưới đèn rọi | “なぜ車椅子から立ち上がって助けを求めなかったのか？” | Mỗi câu một dòng | 🅑 ở `#3` | |
| 4-05 | `4.04` (nghỉ) | — | — | tối dần | *次は:* **心理学の専門家の回答** | — | | |
| 4-06 | `4.05#1` | H | T1 | `glass_box` + `gypsy_wheelchair` nhỏ | **20世紀の心理学における最も残酷な概念の1つ** | — | | |
| 4-07 | `4.05#2` | H | T3 | `locked_door` · 2 thẻ thuật ngữ | **学習性無力感** *(Learned Helplessness)* · *Martin Seligman · 1967年* | Mỗi thẻ ở cụm từ | →C | |
| 4-08 | `4.07#1` | C | T9 | `cage` đóng | **逃げられない環境に長期間置かれた生き物** | Tiếng xích ở đầu | | |
| 4-09 | `4.07#2` | C | T4 `hero` | `cage` đóng, tối dần | **電気ショック · 反復される苦痛** | Câu trích ở cụm từ | | |
| 4-10 | `4.07#3` | C | T1 | `cage` đóng → mở (hoà tan 2 nền cùng seed) | **檻の扉が開いていても、逃げようとしない** | Cửa mở ở "檻の扉" | | |
| 4-11 | `4.07#4` | C | T1 | `locked_door` | **「自分は何をしても無力だ」と脳が学習した** | — | 🅑 P2 | |
| 4-12 | `4.07#5`–`#6` | C | T3 | `hands` | **母の手が娘の手を強く握りしめる** | — | | |
| 4-13 | `4.07#7` | C | T3 | `hands`, ánh `cold` | **沈黙を強要する警告** | Hai bàn tay khép chặt hơn ở "さらに強くなる" | | |
| 4-14 | `4.07#8` | C | T2 | `locked_door` | **ドアが閉ざされると、厳しい懲罰が待っていた** | Khe sáng tắt ở "閉ざされ" | | |
| 4-15 | `4.08` (nghỉ) | — | — | tối dần | **23年間、一度も反抗を試みなかったわけではない** | — | | |
| 4-16 | `4.09#1` | H | T1 | `locked_door`, khe sáng dưới cửa | **2011年** · *SF大会 · 男性の知人* | — | | ✂ |
| 4-17 | `4.09#2` | H | T2 | `records` | **逃走の試み** · *モーテル* | — | | |
| 4-18 | `4.09#3` | H | T1 | `pinboard` mờ | **わずか数時間後** | — | →D | |
| 4-19 | `4.10#1` | D | T6 | `night_street` + `gypsy_stand` | **Dee Deeが追跡し、連れ戻した** | — | | |
| 4-20 | `4.10#2`–`#3` | D | T2 | `pinboard`, tập giấy tờ, dấu `GIẢ MẠO` | **「知的障害の未成年者」とする偽造書類** | Dấu mộc ở "偽造書類" | | |
| 4-21 | `4.10#4` | D | T1 | `house_night` + `gypsy_walk` đi về nhà | **ベッドに縛り付けられ、飢餓状態に置かれた** | — | | |
| 4-22 | `4.10#5` | D | T1 | `screen_off` | **コンピューターの破壊 · 外部との完全な断絶** | Màn hình tắt dần ở "壊し" | 🅑 P2 | |
| 4-23 | `4.11` (nghỉ) | — | — | tối dần | **あらゆる救助の道が遮断された** | — | | |
| 4-24 | `4.12#1` | H | T1 | `night_street` + `crowd` quay lưng | **逃げ道のない心理的トラップ** | — | | |
| 4-25 | `4.12#2` | H | T1 | `locked_door` + một sợi chỉ mảnh (Pillow) | **唯一の窓：秘密のインターネット** | — | →C | |
| 4-26 | `4.13#1` | C | T9 | `hands` mờ | **オンライン交際サイト** · *2012年* | — | | |
| 4-27 | `4.13#2` | C | T4 | `dress_hanger` tối | **Nicholas Godejohn** · *孤立した男性* | Câu trích ở cụm từ | | |
| 4-28 | `4.13#3` | C | T3 | `void` + đường ranh giới tan dần (Pillow) | **何千通もの深夜のメッセージ** | Đường tan trong câu | | |
| 4-29 | `4.15#1` | H | T1 | `corridor` | **暗い妄想の共有** | Tiếng bàn phím ở đầu | | |
| 4-30 | `4.15#2` | H | T1 | `night_screen` + `godejohn_screen` | **「母が消えなければ、自分は救われない」という確信** | — | | |
| 4-31 | `4.15#3` | H | T9 | `void` + 2 bóng người, bóng đổ hoà làm một | **感応精神病 (FOLIE À DEUX)** *(2人の狂気)* | Bóng nhập ở "狂気" | | |
| 4-32 | `4.15#4`–`#5` | H | T1 `hero` | `house_night`, cửa mở, ánh sáng tràn | *母が消えて初めて…* → **2015年6月** | Cửa sáng ở "ドアを開けて" | ⊘ | |
| 4-33 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *第5幕* · **司法の裁き、レッドフラッグ＆教訓** | — | ⊘ | ◼ |

### 第5幕 — 司法の裁き、レッドフラッグ＆教訓 · nền chủ đạo `court_dawn`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` | H | T1 | `court_dawn` | **ミズーリ州裁判所** | Búa gõ ở đầu câu | | |
| 5-02 | `5.02#2` | H | T2 | `court_dawn` mờ | *法的には* · **明白な重罪** | — | | |
| 5-03 | `5.02#3` | H | T2 | `court_dawn` mờ + bảng tên trên bàn (Pillow) | *Dan Patterson · Greene郡検察官* (文字のみ, V5) · **主謀者であると同時に、虐待の犠牲者** | Tiêu đề ở "主謀者" | | |
| 5-04 | `5.03` (nghỉ) | — | — | giữ 5-03 | — | — | | |
| 5-05 | `5.04#1` | H | T5 | `court_dawn` | *2016年 · 司法取引 · 第2級殺人* · **懲役10年** · *同罪における法定最低刑* | Số đếm 0 → 10 | | |
| 5-06 | `5.04#2` | H | T4 `hero` | `prison_window` | *仮釈放後のGYPSYの言葉* → “刑務所に入って、人生で初めて、母の家で暮らしていた時よりも自由を感じました。” | Câu trích từng dòng từ dấu `:` | ⊘ | |
| 5-07 | `5.04#3` | H | T5 | `prison_window`, nắng sáng dần | *2023年12月* · **85%服役** · *仮釈放により釈放* | Thanh tiến trình | | |
| 5-08 | `5.05` (nghỉ) | — | — | sáng dần | — | — | | |
| 5-09 | `5.06#1` | H | T1 | `court_dawn`, `pull` | **4つの警戒すべきレッドフラッグ** *(Red Flags)* · *心理学者＆捜査官* | — | →C+D | |
| 5-10 | `5.07#1` | C | T8 cờ | `void` đỏ sẫm, 4 ô cờ | *01* · **濃厚な病歴 — 検査結果との絶え間ない矛盾** | Cờ 1 tô đầy | hai badge | |
| 5-11 | `5.07#2` | C | T8 cờ | cờ 2 | *02* · **症状が保護者の面前でのみ現れる** | — | hai badge | |
| 5-12 | `5.08#1` | D | T8 cờ | cờ 3 | *03* · **医療行為への積極性 · 病気の見せびらかし · 頻繁な転院** | 3 cụm theo cụm từ | hai badge · Sói sáng | |
| 5-13 | `5.08#2` | D | T8 cờ | cờ 4 | *04* · **学校、友人、親族からの完全な孤立** + dấu mộc “保護という口実” | Dấu mộc ở cụm từ | hai badge | |
| 5-14 | `5.09` (nghỉ 2,5 s) | — | T8 | đủ 4 cờ, `still` | 4つのレッドフラッグ要約 | — | ⊘ | |
| 5-15 | `5.10#1` | H | T1 | `podcast_desk`, đèn ấm dần | **事件記録は閉じられた** | — | | |
| 5-16 | `5.10#2` | H | T1 `hero` | `house_dawn` + `gypsy_walk`, xe lăn bỏ lại | **自分の脚で歩き始める** | Trời sáng dần | ⊘ | |
| 5-17 | `5.10#3` | H | T1 | `cage` mở, nắng | **天使の衣を纏ったもの** | Tiêu đề ở "天使の衣" | | |
| 5-18 | `5.11` (nghỉ) | — | — | giữ 5-17 | — | — | | |
| 5-19 | `5.12#1` | H | T1 | `podcast_desk` | **ゲストの皆様、ありがとうございました** · *架空のキャラクター · AI音声* | Dàn khách mời: 5 ảnh P0 sáng lần lượt | dàn khách mời | |
| 5-20 | `5.12#2` | H | T10 | `podcast_desk` mờ | **また次の事件でお会いしましょう** · *コメント欄にあなたのご意見をお寄せください* | — | 🅑 | |
| 5-21 | `5.13`–`5.14` | — | T2 | `podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | *事件記録 第01話 · 完結* · **AMBER EYES** · *実際の事件記録から読み解く犯罪心理学* | Bìa gập ở "Bụp"; mờ ra đen | ⊘ | ◼ |

**Tổng: 122 dòng = 104 shot có lời + 18 dòng không lời.** Phủ 128/128 câu, đúng thứ tự, cột Vai khớp người nói (kiểm tra bằng script ngày 22/10; `validate_shots.py` phải lặp lại).
**Tổng: 122 shot · Đã hoàn thiện và đối chiếu 100% câu và beat tiếng Nhật.**