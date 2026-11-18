# KẾ HOẠCH CLIP TIKTOK — TẬP 01 · "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ"

*Ngày: 18/11/2026 · Trạng thái: **kế hoạch đã chốt, chưa sản xuất** (audio do người dùng tự tạo)*
*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Bảng đặc tả audio (máy đọc được): `02_SAN_XUAT/TIKTOK/Tap01/SPEC_AUDIO_CLIP_TAP01.json`*

---

## 0. Tóm tắt chốt

| Hạng mục | Giá trị |
|---|---|
| Số clip | **4 clip** (thêm 1 clip thưởng dự phòng — mục 7) |
| Mỗi clip | 45–95 s (mục tiêu 60–90 s) · 8–12 câu thoại |
| Chủ đề | Mỗi clip = **1 chỉ dấu tâm lý** (K10) của Tập 01 |
| Ngôn ngữ | Tiếng Việt · vai H / D / C / N1 / N2 |
| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (đúng giọng của tập) — không dùng bộ A MiniMax |
| Hình | Nền 16:9 có sẵn trong `assets/bg/` (44 nền) · dựng 9:16 · Pillow vẽ chữ |
| Chi phí | **0 đồng** (Kaggle GPU có sẵn) — trừ thời gian chờ GPU |
| Việc cần người dùng | Tạo **40 file WAV** (43 nếu làm thêm clip thưởng) theo `SPEC_AUDIO_CLIP_TAP01.json` (mục 5) |

---

## 1. Vì sao viết lời dẫn mới cho clip, không cắt từ audio tập

| Phương án | Đánh giá |
|---|---|
| **A — Lời dẫn mới cho clip (CHỌN)** | Hook 3 giây đúng chuẩn TikTok; 1 clip = 1 chỉ dấu; chỉ cần **40 câu ngắn** (43 nếu kèm clip thưởng) thay vì 205 câu; không phụ thuộc media tập đã bị dọn |
| B — Cắt nguyên đoạn từ audio tập | Phải dựng lại toàn bộ audio tập (205 câu ≈ 25–40 phút Kaggle, ở `assets/…/xuat_ban/` media đã bị xoá 12/11); lời dẫn tập viết để *nghe*, không để *giữ chân*; không có hook 3 giây ⇒ **trượt đối với TikTok** |

⇒ Chọn A. Chi tiết kỹ thuật audio ở mục 5.

---

## 2. Bốn clip và chỉ dấu tâm lý tương ứng (K10)

| Clip | Chỉ dấu | Chủ đề | Hook trên màn hình (0–3 s) |
|---|---|---|---|
| **TK1** | #2 Thủ đoạn vs Chữ ký tâm lý | Khoảnh khắc bước ngoặt: cô ấy bước vào phòng thẩm vấn bằng đôi chân của chính mình | *"Cô ấy không ngồi trên xe lăn. Cô ấy bước đi."* |
| **TK2** | #6 Sự bất lực tập nhiễm | Vì sao cô ấy chưa từng chạy trốn — Seligman 1967 | *"Vì sao cô ấy không bao giờ chạy trốn?"* |
| **TK3** | #3 Sự cung cấp ái kỷ + #9 Điểm mù xã hội | Động cơ không phải tiền, mà là sự kính ngợng | *"Bà ta không cần tiền. Bà ta cần sự kính ngợng."* |
| **TK4** | #10 Bộ 4 cảnh báo đỏ sinh tồn | 4 dấu hiệu đỏ để nhận ra trẻ em đang bị bệnh trong chính ngôi nhà mình | *"4 dấu hiệu đỏ sinh tồn — lưu lại clip này."* |

**Thứ tự đăng:** TK1 → TK4 → TK2 → TK3 (TK1 để thu hút, TK4 để kéo lượt chia sẻ/lưu, TK2–TK3 để xây chủ đề "hệ sinh thái 10 chỉ dấu").

---

## 3. Diễn xuất từng clip (lời đọc + hình + âm)

> Quy ước vai: **H** = Host (Cú) · **D** = Điều tra viên (Sói) · **C** = Chuyên gia tâm lý (Cáo) · **N1** = Người dân (Cừu) · **N2** = Khán giả (Mèo)
> `pause_after` = thời gian im lặng chèn **giữa hai câu** (0,2–1,2 s — luật G2). Emotion chỉ dùng 4 giá trị an toàn (G3). Tốc độ lệch −0,06…+0,02 (G4).
> Mỗi câu bắt đầu bằng mã câu `TKx.yy#z` — dùng làm tên file WAV và mã câu trong hồ sơ.

### 3.1 CLIP TK1 — "Cô ấy bước vào phòng thẩm vấn bằng đôi chân của chính mình"

*Mục tiêu 65–85 s (ước tính ~78 s theo nhịp tập) · BGM `bgm_sub_drone.mp3` (MiniMax) · SFX: tiếng máy ghi âm "Tách" (tổng hợp) + nền phòng kín (tổng hợp)*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nền | Chuyển động |
|---|---|---|---|---|---|---|---|
| `TK1.01#1` | H | neutral | −0,02 | 0,5 | Sau bốn mươi tám giờ truy tìm, cô ấy bước vào phòng thẩm vấn bằng đôi chân của chính mình. | `interrogation_gypsy` | still |
| `TK1.01#2` | H | neutral | −0,02 | 0,6 | Người dân Mỹ lo rằng một kẻ sát nhân đã bắt cóc một thiếu nữ không thể tự bước đi. | `crowd_house` | pull |
| `TK1.01#3` | D | neutral | −0,03 | 0,7 | Nhưng khoảnh khắc cánh cửa phòng thẩm vấn mở ra, toàn bộ nhận thức của chúng tôi sập đổ. | `interrogation_gypsy` | push |
| `TK1.01#4` | D | neutral | −0,03 | 0,5 | Gypsy Rose Blanchard không hề ngồi trên xe lăn. | `interrogation_gypsy` | still |
| `TK1.01#5` | D | neutral | −0,03 | 0,6 | Cô ta tự bước đi vững chãi bằng chính đôi chân của mình, phong thái hoàn toàn bình thường. | `interrogation_gypsy` | pan |
| `TK1.01#6` | C | neutral | −0,02 | 0,6 | Từ đây, tâm lý học tội phạm tách làm hai khái niệm: thủ đoạn và chữ ký tâm lý. | `brain_desk` | pull |
| `TK1.01#7` | C | neutral | −0,02 | 0,5 | Thủ đoạn là những gì kẻ phạm tội làm để thực hiện hành vi và né tránh sự trừng phạt. | `records` | push |
| `TK1.01#8` | C | neutral | −0,02 | 0,5 | Ở đây, thủ đoạn liên tục biến đổi: đổi bệnh viện và chuyển chỗ ở ngay khi một bác sĩ bắt đầu nghi ngờ. | `pinboard` | pan |
| `TK1.01#9` | C | neutral | −0,02 | 0,5 | Chữ ký tâm lý thì bất biến, sinh ra để thỏa mãn nhu cầu cảm xúc bệnh lý cốt lõi. | `brain_desk` | still |
| `TK1.01#10` | C | neutral | −0,02 | 0,5 | Chữ ký của bà ta là tước đoạt tuổi trưởng thành: khai man ngày sinh, biến cô con gái hai mươi tuổi thành một đứa trẻ mười sáu tuổi trên giấy tờ. | `doll` | pull |
| `TK1.01#11` | C | sad | −0,04 | 0,7 | Bà ta không chỉ muốn con mình bệnh tật. Bà ta muốn con mình không bao giờ lớn. | `spotlight_deedee` | push |
| `TK1.01#12` | H | neutral | −0,02 | 0,0 | Tập một của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `podcast_desk` | still |

**Thẻ chữ trên hình (overlay card):** hiện ở `TK1.01#6`, 2,5 s — *"THỦ ĐOẠN (MODUS OPERANDI) ≠ CHỮ KÝ TÂM LÝ (SIGNATURE)"*
**Nguồn dữ kiện:** `01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md` (1.08#9 · 1.11#1–#6 · 2.07#1–#3, #7–#9, #11) + `02_SAN_XUAT/Tap01/nguon_tham_khao.md` (Flasterstein 2007).

---

### 3.2 CLIP TK2 — "Vì sao cô ấy không bao giờ chạy trốn"

*Mục tiêu 65–90 s (ước tính ~82 s) · BGM `bgm_ambient_deep.mp3` (MiniMax) · SFX: nền phòng kín (tổng hợp) + tiếng kim loại va chạm (tổng hợp)*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nền | Chuyển động |
|---|---|---|---|---|---|---|---|
| `TK2.01#1` | N2 | neutral | −0,02 | 0,4 | Suốt hàng chục năm trời, trước mặt hàng trăm bác sĩ, y tá, cảnh sát và các tình nguyện viên từ thiện, cô ấy chưa từng một lần đứng bật dậy khỏi chiếc xe lăn để kêu cứu. | `wheelchair_room` | still |
| `TK2.01#2` | H | neutral | −0,02 | 0,5 | Để trả lời, ta phải nhìn vào hai cơ chế giam hãm nhận thức: sự bất lực tập nhiễm và gắn kết chấn thương. | `brain_desk` | pull |
| `TK2.01#3` | C | neutral | −0,02 | 0,6 | Năm 1967, nhà tâm lý học Martin Seligman công bố thí nghiệm kinh điển về sự bất lực tập nhiễm. | `cage` | push |
| `TK2.01#4` | C | neutral | −0,02 | 0,4 | Khi sinh vật bị nhốt trong phòng kín và phải chịu những cú sốc điện ngẫu nhiên không thể né tránh, sau nhiều lần thử phản kháng thất bại, nó hoàn toàn từ bỏ ý chí chiến đấu. | `cage` | pan |
| `TK2.01#5` | C | neutral | −0,02 | 0,5 | Kể cả khi người ta mở toang cửa lồng và không còn dòng điện nào cản trở, con vật vẫn nằm im cam chịu. | `cage_open` | push |
| `TK2.01#6` | C | neutral | −0,02 | 0,5 | Bộ não bị tổn thương tâm lý sâu sắc sẽ đi đến một kết luận cố định: mọi sự kháng cự đều là vô nghĩa. | `brain_desk` | still |
| `TK2.01#7` | C | sad | −0,03 | 0,5 | Mỗi lần con gái ngồi trước mặt bác sĩ, bàn tay mẹ luôn nắm chặt. Người ngoài nhìn vào tưởng đó là cái nắm tay chan chứa yêu thương. | `hands` | pull |
| `TK2.01#8` | C | sad | −0,03 | 0,6 | Với cô bé, đó là tín hiệu đe dọa: nếu cô bé nói sai một lời, bàn tay mẹ sẽ siết chặt đến bầm tím. | `hands` | pan |
| `TK2.01#9` | H | neutral | −0,02 | 0,6 | Đó là cách một đứa trẻ học được rằng phản kháng là vô ích. | `cage_open` | still |
| `TK2.01#10` | H | neutral | −0,02 | 0,0 | Tập một của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `podcast_desk` | still |

**Thẻ chữ:** `TK2.01#2` → *"2 CƠ CHẾ GIAM HÃM NHẬN THỨC"* (2,5 s) · `TK2.01#3` → *"SỰ BẤT LỰC TẬP NHIỄM (LEARNED HELPLESSNESS)"* (3 s) · `TK2.01#6` → *"“MỌI SỰ KHÁNG CỰ ĐỀU LÀ VÔ NGHĨA”"* (2,5 s)
**Nguồn:** 4.03#4 · 4.05#2 · 4.07#1–#8 (Seligman 1967 — thí nghiệm bất lực tập nhiễm).

---

### 3.3 CLIP TK3 — "Bà ta không cần tiền. Bà ta cần sự kính ngợng"

*Mục tiêu 60–80 s (ước tính ~71 s) · BGM `bgm_cello_sad.mp3` (MiniMax) · SFX: nền văn phòng (tổng hợp) + lật hồ sơ giấy (tổng hợp)*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nền | Chuyển động |
|---|---|---|---|---|---|---|---|
| `TK3.01#1` | H | neutral | −0,02 | 0,4 | Nhiều người nghĩ bà ta làm tất cả chỉ vì tiền trợ cấp và những chuyến đi Disneyland miễn phí. | `records` | pull |
| `TK3.01#2` | H | neutral | −0,02 | 0,5 | Nhưng nếu chỉ vì lòng tham tài chính, kẻ phạm tội sẽ chọn cách lừa đảo ít phiền phức và tốn kém hơn nhiều. | `records` | pan |
| `TK3.01#3` | C | neutral | −0,02 | 0,5 | Theo cẩm nang chẩn đoán tâm thần DSM-5-TR, hội chứng FDIA hoàn toàn khác với hành vi giả bệnh trục lợi. | `brain_desk` | still |
| `TK3.01#4` | C | neutral | −0,02 | 0,5 | Kẻ giả bệnh trục lợi sẽ dựng chuyện để kiếm tiền rồi bí mật hưởng thụ trong bóng tối. | `records` | push |
| `TK3.01#5` | C | neutral | −0,02 | 0,6 | Còn kẻ mắc hội chứng FDIA thì đói khát một thứ chất gây nghiện tinh vi hơn nhiều: sự cung cấp ái kỷ. | `spotlight_deedee` | still |
| `TK3.01#6` | C | sad | −0,03 | 0,5 | Trước khi sinh con, cuộc đời bà ta là một chuỗi thất bại: bị gia đình xa lánh, hôn nhân tan vỡ lúc mới hai mươi tư tuổi. | `records` | pull |
| `TK3.01#7` | C | neutral | −0,02 | 0,5 | Nhưng khoảnh khắc bà ta khoác lên mình chiếc áo người mẹ đơn thân kiên cường nuôi con tàn tật, toàn bộ thế giới bỗng đảo chiều. | `spotlight_deedee` | push |
| `TK3.01#8` | C | neutral | −0,02 | 0,5 | Mỗi lời khen ngợi bà là người mẹ vĩ đại nhất là một liều dopamine tiêm thẳng vào não bộ. | `records` | still |
| `TK3.01#9` | N1 | sad | −0,03 | 0,6 | Chúng tôi đã hoàn toàn tin tưởng rằng bà ấy là một vị thánh sống giữa đời thực. | `house_night` | pull |
| `TK3.01#10` | H | neutral | −0,02 | 0,0 | Tập một của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `podcast_desk` | still |

**Thẻ chữ:** `TK3.01#3` → *"FDIA ≠ GIẢ BỆNH TRỤC LỢI (MALINGERING)"* (3 s) · `TK3.01#5` → *"SỰ CUNG CẤP ÁI KỶ (NARCISSISTIC SUPPLY)"* (3 s) · `TK3.01#9` → *"ĐIỂM MÙ XÃ HỘI"* (2,5 s)
**Nguồn:** 3.02#3–#4 · 3.04#1–#3 (DSM-5-TR) · 3.05#2, #4, #7 · 1.07#6 (lời người dân).

---

### 3.4 CLIP TK4 — "4 dấu hiệu đỏ sinh tồn"

*Mục tiêu 70–90 s (ước tính ~80 s) · BGM `bgm_piano_minimal.mp3` (MiniMax) · SFX: nền bệnh viện (tổng hợp) + gõ cửa (tổng hợp)*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nền | Chuyển động |
|---|---|---|---|---|---|---|---|
| `TK4.01#1` | H | neutral | −0,02 | 0,4 | Bốn dấu hiệu đỏ để nhận ra một đứa trẻ đang bị bệnh trong chính ngôi nhà của mình. | `records` | pull |
| `TK4.01#2` | H | neutral | −0,02 | 0,5 | Dưới góc độ tâm lý và lâm sàng y khoa, cộng đồng cần đặc biệt lưu tâm đến hai chỉ dấu cảnh báo đầu tiên. | `clinical` | pan |
| `TK4.01#3` | C | neutral | −0,02 | 0,5 | Cảnh báo đỏ thứ nhất: bệnh sử phức tạp bất thường và mâu thuẫn xét nghiệm. Danh sách bệnh hiểm nghèo kéo dài triền miên, nhưng kết quả kiểm tra khách quan luôn bình thường hoặc trái ngược lời kể của người chăm sóc. | `records` | still |
| `TK4.01#4` | C | neutral | −0,02 | 0,5 | Cảnh báo đỏ thứ hai: triệu chứng chỉ xuất hiện khi có mặt người chăm sóc, và lập tức thuyên giảm khi bệnh nhân được cách ly hoặc nằm trong khu vực có camera giám sát độc lập. | `clinical` | push |
| `TK4.01#5` | D | neutral | −0,03 | 0,5 | Cảnh báo đỏ thứ ba: thói quen đổi bác sĩ và nghiện sự chú ý. Người chăm sóc liên tục đổi phòng khám ngay khi bị chất vấn, đồng thời phô trương bệnh tật của con lên mạng xã hội để tìm kiếm sự thương hại. | `pinboard` | pan |
| `TK4.01#6` | D | neutral | −0,03 | 0,6 | Cảnh báo đỏ thứ tư: sự cô lập tuyệt đối khỏi cộng đồng. Nạn nhân bị cắt đứt khỏi trường học, bạn bè và người thân, dưới chiêu bài bảo vệ sức khỏe yếu ớt. | `crowd_away` | push |
| `TK4.01#7` | H | neutral | −0,02 | 0,6 | Bốn dấu hiệu này không chỉ nằm trong một hồ sơ. Chúng là những gì cộng đồng phải biết để canh giữ trẻ em. | `two_shadows` | still |
| `TK4.01#8` | H | neutral | −0,02 | 0,0 | Lưu lại clip này. Xem hồ sơ đầy đủ tập một ở link trong bio. | `podcast_desk` | still |

**Thẻ chữ (đánh số ①②③④, hiện 2,5 s mỗi thẻ):**
`TK4.01#3` → *"① BỆNH SỬ PHỨC TẠP MÂU THUẪN XÉT NGHIỆM"* · `TK4.01#4` → *"② TRIỆU CHỨNG CHỈ XUẤT HIỆN KHI CÓ NGƯỜI CHĂM SÓC"* · `TK4.01#5` → *"③ ĐỔI BÁC SĨ + NGHIỆN SỰ CHÚ Ý"* · `TK4.01#6` → *"④ CÔ LẬP TUYỆT ĐỐI KHỎI CỘNG ĐỒNG"*
**Nguồn:** 5.04#3 (bốn tín hiệu cảnh báo đỏ) · 5.05#1–#4 · 5.06#2–#3.

---

## 4. Bố cục màn hình 9:16 (1080 × 1920)

Áp dụng safe zone của TikTok (bám template In-Fead, thiết kế theo trường hợp xấu nhất):

| Thành phần | Vị trí (x, y) | Cỡ chữ | Ghi chú |
|---|---|---|---|
| **Chữ hook** (0–3 s) | x 120–780, y 300–700 | 76 px đậm, tối đa 2 dòng | có `text_scrim`; chữ Pillow vẽ sau, **không** để AI vẽ chữ |
| **Phụ đề burn-in** | x 120–780, y 1.020–1.230 | 52 px, tối đa 2 dòng | nền scrim mờ 35 %; **nguyên văn** lời đọc (G6) |
| **Thẻ chữ overlay** | x 120–780, y 780–980 | 44 px | card tối 60 %, bo góc 12 px, hiện 2,5–3 s rồi fade 0,4 s |
| **Logo** | x 120–260, y 60–160 | — | tránh x > 780 (nút like/comment/share) |
| **Nền** | phủ kín 1080×1920 | — | phương án B: blur-fill + zoom 4 %; phương án A: nền dọc sinh mới |

Chuyển động `pull` / `push` / `pan` / `still` dùng đúng bộ của pipeline hiện tại (`.work/build_video3.py`).

---

## 5. Chỉ dẫn tạo audio (phần người dùng làm)

> **Mục tiêu:** 40 câu → 40 file WAV 24 kHz mono (43 nếu làm thêm clip thưởng TK5). Đây là phần duy nhất còn lại để dựng clip.

### 5.1 Engine: Higgs Audio v3 + giọng mẫu VoxCPM2 (đúng giọng của tập)

| Tham số | Giá trị (đã kiểm chứng trên pipeline Tập 02–08) |
|---|---|
| Mô hình | `bosonai/higgs-tts-3-4b` (Higgs Audio v3) |
| Dataset giọng mẫu | `chiduong2026/amber-eyes-voice-ref-voxcpm2` (đã có sẵn, `ready`) |
| Vai → clip tham chiếu | **H → `H.wav`** · **D → `D3_SH.wav`** · **C → `C2_AB03.wav`** · **N1 → `W6_LOW.wav`** · **N2 → `W5_HIGH.wav`** |
| temperature / top_p / top_k | 0,8 / 0,95 / 50 |
| max_new_tokens | 1.196 (≈ 47 s — dư cho câu ngắn) |
| sample_rate | 24.000 Hz · `fade_in_ms` 30 · `fade_out_ms` 15 |
| Seed | `sha256(id\|role\|ref\|temp\|vN)` → `int(hex[:8],16)`; **sinh 2 bản/câu** (v0, v1) |
| Cấm | mọi thẻ `<\|emotion:...\|>` — **chỉ** dùng `<\|prosody:pause\|>` sau dấu `:` trước câu trích |
| Chuyển số thành chữ | tự động (G11): "1967" → "một nghìn chín trăm sáu mươi bảy" |

**Quy trình Kaggle (theo đúng P1–P9 của `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md`):**

```
P1  py -3 .work/export_higgs_payload.py            # xuất payload (tập 01)
P1b py -3 .work/build_spec.py                       # prod_spec.json + payload
P2  py -3 .work/build_nb.py --mode prod
    py -3 .work/prep_push_dirs.py prod
P3  kaggle datasets version -p "…\.work\kaggle_higgs\dataset_voxcpm2" -m "…"
    kaggle datasets status chiduong2026/amber-eyes-voice-ref-voxcpm2      # phải = ready
P4  kaggle kernels push -p "…\_push_prod_t01"
P5  py -3 .work/watch_kernel.py --slug <slug> --out .work/kaggle_higgs/out_higgs_prod_t01 \
        --pattern "out_higgs_prod_t01/.*\.(wav|json|log)"
P6  py -3 .work/measure_cer_prod.py --rounds 2 --workers 2              # ngưỡng CER < 2 % (G12)
P7  py -3 .work/check_higgs_f0.py                                     # G9 ≥ 4 nửa cung cho H–D, C–H, C–D
P9  py -3 .work/finish_prod.py                                         # chọn bản tốt nhất
```

**Lưu ý Kaggle (bẫy đã gặp):**
- Chỉ **2 phiên GPU đồng thời** trên 1 tài khoản ⇒ xếp tối đa 2 kernel; kernel đang *queued* cũng tính.
- Token Kaggle hết hạn sau ~12 h ⇒ `kaggle kernels status` báo *"Permission 'kernels.get' was denied"* dù kernel vẫn chạy → refresh token (không `kaggle auth login`).
- CLI nằm ở `%LOCALAPPDATA%\kaggle-venv\Scripts\kaggle.exe` (ngoài PATH).
- **40 câu ≈ 6–10 phút GPU** (≈ 7 s/câu) — không cần chạy cả tập.

### 5.2 Quy ước đặt tên & thư mục (bắt buộc để dựng được video)

```
.work/audio_s_tk_t01/
├── TK1.01_01.wav      # <clip>.<câu>_<số câu>.wav   (mã "TK1.01#1" → "TK1.01_01.wav")
├── TK1.01_02.wav
├── …
├── TK4.01_08.wav
└── manifest_tk_t01.json
```

`manifest_tk_t01.json` (mỗi dòng một câu):

```json
{"id": "TK1.01#1", "vai": "H", "file": "TK1.01_01.wav", "dur": 6.42,
 "emotion": "neutral", "speed": -0.02, "pause_after": 0.5, "variant": 0}
```

> Nếu bạn tạo audio bằng công cụ khác (MiniMax, ElevenLabs…), chỉ cần đặt tên đúng quy ước trên và xuất `manifest` cùng định dạng; phần dựng video không phụ thuộc Higgs.

### 5.3 Cổng kiểm audio (bắt buộc trước khi dựng video)

| Cổng | Ngưỡng | Cách đo |
|---|---|---|
| Đủ file | 40/40 WAV + manifest (43 nếu kèm TK5) | đếm file |
| Định dạng | 24.000 Hz, mono, PCM 16-bit | `ffprobe` |
| Độ dài mỗi câu | 1,5–14 s | đo trên file |
| Tổng clip | 45–95 s | cộng `dur` + `pause_after` |
| CER | **< 2 %** mỗi câu (G12) | Whisper (`measure_cer_prod.py`) |
| F0 / G9 | H–D ≥ 4 nc · C–H ≥ 4 nc · C–D ≥ 4 nc | `check_higgs_f0.py` |
| Nghe mù (G10) | mỗi vai nghe liền ra **1 người**, 3 vai tách bạch | tai người |
| Không câm | 0 khoảng > 0,3 s ở −60 dB trong clip | `qc_pause_gate.py --pre` |
| Lời đọc | đúng **nguyên văn** dòng trong `SPEC_AUDIO_CLIP_TAP01.json` (G6) | so từng chữ |

---

## 6. Âm thanh nền của clip (bản quyền — áp dụng tuyệt đối)

| Nguồn | Clip TikTok |
|---|---|
| `assets/bgm/bgm_sub_drone.mp3`, `bgm_ambient_deep.mp3`, `bgm_cello_sad.mp3`, `bgm_piano_minimal.mp3` (MiniMax Music) | ✅ dùng được |
| `assets/bgm/bgm_guitar_acoustic_60s.mp3`, `bgm_church_organ.mp3` | ❌ **YouTube Audio Library ⇒ cấm trên TikTok** |
| SFX tự tổng hợp bằng `.work/make_sfx.py` | ✅ dùng được |
| SFX Freesound **CC0** | ✅ dùng được |
| 211 file SFX trong `assets/sfx/t2/`, `assets/sfx/t3/` (YouTube Audio Library) | ❌ **cấm trên TikTok** |

Mức: giọng −16 LUFS (đo trên mp4 cuối) · BGM −26 dB khi có lời, nâng −14 dB ở nghỉ 0,8–1,2 s trước câu chốt · **luôn có lớp nền môi trường** bên dưới (A1/V4: cấm câm tuyệt đối > 0,3 s).

---

## 7. Clip thưởng (dự phòng, làm sau khi 4 clip trên đã đo)

**TK5 — "Câu nói trong nhà tù"** (~45 s) · vai D + H · nền `prison_window`, `court_dawn`
D: "Khi bước vào trại cải tạo nữ, cô ấy đưa ra một lời thú nhận khiến các chuyên gia tâm lý học pháp y phải nghẹn ngào." (5.04#1)
C (đọc nguyên văn câu trích, có nguồn ABC News 20/20): *"Trong nhà tù của pháp luật, lần đầu tiên trong đời tôi cảm thấy mình thực sự được tự do hơn cả khi sống trong ngôi nhà của mẹ."*
H: "Ngày 28 tháng 12 năm 2023, cô ấy bước ra khỏi trại giam sau 85 % thời hạn bản án." (5.04#7)
⇒ Dùng cho clip thứ 5 hoặc làm **bài ghim trang**.

---

## 8. Caption + hashtag (mẫu, sẵn sàng dán)

**TK1**
```
Cô ấy không ngồi trên xe lăn. Cô ấy bước đi. 👁️

Tập 01 · Độc dược nhân danh tình mẹ — chỉ dấu #2: thủ đoạn và chữ ký tâm lý.
Hồ sơ có thật, dữ kiện có nguồn.

📺 Xem tập đầy đủ ở link trong bio
🔎 Chỉ dấu tâm lý · FDIA · hồ sơ có thật

#AmberEyes #TamLyToiPham #HosoCoThat #PhanTichTamLy #TrueCrime #MoiTuanMotTap
```

**TK2**
```
Vì sao cô ấy không bao giờ chạy trốn?

Tập 01 — chỉ dấu #6: sự bất lực tập nhiễm (Seligman, 1967).
Hồ sơ có thật, dữ kiện có nguồn.

📺 Xem tập đầy đủ ở link trong bio

#AmberEyes #TamLyToiPham #HosoCoThat #LearnedHelplessness #TraumaBonding #TamLyHoc
```

**TK3**
```
Bà ta không cần tiền. Bà ta cần sự kính ngợng. 👁️

Tập 01 — chỉ dấu #3: sự cung cấp ái kỷ (narcissistic supply).
Hồ sơ có thật, dữ kiện có nguồn.

📺 Xem tập đầy đủ ở link trong bio

#AmberEyes #TamLyToiPham #HosoCoThat #NarcissisticSupply #FDIA #MoiTuanMotTap
```

**TK4**
```
4 dấu hiệu đỏ sinh tồn — lưu lại clip này.

Tập 01 — cảnh báo đỏ: bệnh sử mâu thuẫn xét nghiệm · triệu chứng chỉ xuất hiện khi có người chăm sóc · đổi bác sĩ + nghiện sự chú ý · cô lập khỏi cộng đồng.
Hồ sơ có thật, dữ kiện có nguồn.

📺 Xem tập đầy đủ ở link trong bio

#AmberEyes #TamLyToiPham #HosoCoThat #CanhGiuTreEm #LanhDanh #MoiTuanMotTap
```

> **Bắt buộc kèm theo mỗi caption:** dòng *"Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự."* + bật toggle **"AI-generated content"** khi đăng (TikTok bắt buộc ghi nhãn AIGC).

---

## 9. Hợp đồng giữa phần audio và phần dựng video

| Người làm | Việc | Bàn giao |
|---|---|---|
| **Người dùng** | Tạo 40 WAV + `manifest_tk_t01.json` theo mục 5 | `.work/audio_s_tk_t01/` |
| **AI (sau khi được duyệt)** | Dựng 4 clip 9:16: Pillow dựng nền + chữ, trộn BGM/SFX, chuẩn hoá −16 LUFS, xuất mp4 + caption, chạy 14 cổng QC | `02_SAN_XUAT/TIKTOK/Tap01/clip01…04.mp4` + `BaoCao_QC_TikTok_Tap01.md` |

**Quy tắc dựng video bám tiêu chuẩn:** H6 (chữ = nguyên văn lời đọc) · H9 (đo tương phản chữ, bật `text_scrim` nếu cần) · H17 (mọi ngôn ngữ cùng nền) · A1 (0 khoảng câm > 0,3 s) · A7 (−16 LUFS, TP ≤ −1,5 dBFS) · G6 (lời đọc không đổi chữ) · **L10 (không commit media)**.

---

## 10. Cổng QC clip (14 mục — đo thật, không "nói xong" khi chưa đo)

| # | Kiểm | Ngưỡng |
|---|---|---|
| 1 | Khung / tỉ lệ | 1080 × 1920, 9:16 |
| 2 | Codec / fps | H.264 + AAC, 30 fps |
| 3 | Dung lượng | ≤ 500 MB |
| 4 | Độ dài | 45–95 s |
| 5 | Âm lượng | −16 ± 1 LUFS · true peak ≤ −1,5 dBFS |
| 6 | Khoảng câm | 0 khoảng > 0,3 s @ −60 dB |
| 7 | Lệch hình/tiếng | ≤ 0,05 s |
| 8 | Giải mã | 0 lỗi |
| 9 | **Safe zone** | mọi chữ trong x 120–780, y 240–1.260 |
| 10 | **Watermark** | 0 khung chứa watermark nền tảng khác |
| 11 | **Chữ** | 0 chữ rác · 0 chữ trùng · 0 chữ chìm (đo tương phản) |
| 12 | **Mặt người thật** | 0 vi phạm |
| 13 | **Từ cấm V9** | 0 từ trong danh sách A9.2 |
| 14 | **Hook** | 3 giây đầu có chữ hook đọc được ở 100 % khung |

**Riêng cho Tập 01:** mọi dữ kiện trong lời đọc phải truy được về `01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md` + `02_SAN_XUAT/Tap01/nguon_tham_khao.md` (K1/K2); **không** thêm tên riêng, số liệu hay chi tiết mới ngoài hai file này.

---

## 11. Lịch trình đề xuất (chưa bắt đầu)

| Tuần | Việc | Người |
|---|---|---|
| 1 | Người dùng tạo audio 40 câu (mục 5) · AI viết script dựng + QC | Người dùng + AI |
| 2 | Dựng & đo 4 clip → người dùng duyệt hình + nghe giọng | AI → người dùng |
| 3 | Đăng TK1 + TK4 (2 clip/tuần) · ghi số đo vào `02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv` | Người dùng |
| 4 | Đăng TK2 + TK3 · quyết định có làm nền dọc FLUX (phương án A) cho các tập sau không | Người dùng |

---

## 12. Tài liệu liên quan

- `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` — kế hoạch mẹ (spec TikTok, chính sách, cổng QC, rủi ro)
- `02_SAN_XUAT/TIKTOK/Tap01/SPEC_AUDIO_CLIP_TAP01.json` — **bảng đặc tả audio máy đọc được** (dùng để sinh WAV)
- `01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md` — kịch bản gốc 205 câu (nguồn của mọi câu trong clip)
- `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md` — bảng shot 203 dòng (nguồn của mọi nền/chuyển động)
- `02_SAN_XUAT/Tap01/nguon_tham_khao.md` — nguồn đối chiếu dữ kiện
- `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` — quy trình Higgs P0–P10 (Kaggle)
- `AGENTS.md` — L4/L5/L6/L7/L10 · K1–K10 · G1–G13 · A1–A11 · H6/H9/H17
