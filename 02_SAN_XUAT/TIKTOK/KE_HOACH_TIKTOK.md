# KẾ HOẠCH TIKTOK — KÊNH AMBER EYES

*Ngày: 18/11/2026 · Trạng thái: đề xuất đã chốt hướng, chờ người dùng duyệt triển khai*
*Ngôn ngữ làm việc: **tiếng Việt** · Tài khoản: **1 tài khoản VN** · Đăng **tay** qua app*

---

## 0. Quyết định đã chốt (18/11/2026)

| # | Quyết định | Giá trị |
|---|---|---|
| Q1 | Định dạng chính | **Clip 45–90 giây, theo series** — mỗi tập YouTube sinh 2–4 clip |
| Q2 | Ngôn ngữ | **Tiếng Việt**, 1 tài khoản `@ambereyes` |
| Q3 | Mục tiêu | **Kéo người xem về YouTube** (tăng watch hours) — không kỳ vọng doanh thu trực tiếp trên TikTok |
| Q4 | Cách đăng | **Đăng tay qua app** — chưa dựng API tự động |

**Lý do Q3 (điểm quan trọng nhất của cả kế hoạch):** TikTok **Creator Rewards Program** chỉ mở ở 8 nước — US, UK, Germany, France, Japan, South Korea, Mexico, Brazil. **Việt Nam không có trong danh sách**, nên tài khoản VN **không nhận tiền từ lượt xem trên TikTok**. Trong khi đó YouTube YPP đã mở đầy đủ tại Việt Nam. ⇒ **TikTok là cửa tìm người xem, YouTube là nơi thu tiền.** Mọi quyết định còn lại đều dằn về hướng đó.

---

## 1. Bối cảnh dự án — có gì để dùng, thiếu gì

| Đã có sẵn (0 đồng) | Dùng cho TikTok |
|---|---|
| 29 tập master 16:9 + `.srt` + `timeline_s_tXX.json` + `shots.json` | nguồn cắt clip, lấy mốc thời gian chính xác |
| ~1.000 ảnh nền 16:9 (`assets/bgm/`, `assets/bg/`) + pipeline FLUX Kaggle | sinh **nền dọc** cho clip (xem bước 5) |
| 5 linh thú cast (`assets/cast/`) + logo + `assets/brand/channel.json` | định dạng nhận diện (chữ trên hình, outro) |
| Trailer 50 s (`assets/brand/trailer_kenh_A_vn.mp4`) | bản dọc làm video mở đầu kênh / post giới thiệu |
| 4 clip b-roll 5,9 s trong `videos/` (không tiếng) | lớp B-roll nền cho clip dọc |
| Bộ giọng Higgs Audio v3 (đã qua G8–G13) | lời dẫn clip — tái dùng y hệt, không tốn credit mới |
| `.work/make_sfx.py` (SFX tổng hợp) + Freesound CC0 | âm thanh clip **không dính bản quyền nền tảng khác** |

| Còn thiếu | Phải làm |
|---|---|
| Nền dọc 9:16 | sinh mới bằng FLUX Kaggle (pipeline có sẵn) hoặc dùng blur-fill 16:9 |
| Script dựng clip dọc | `.work/make_tiktok_clip.py` (mới) |
| Cổng QC clip | `.work/qc_tiktok.py` (mới) |
| Nội dung chữ hook | 1 bộ hook tiếng Việt cho 10 chỉ dấu tâm lý (K10) |

---

## 2. Những ràng buộc TikTok bắt buộc tuân thủ (đã kiểm chứng 18/11/2026)

### 2.1 Kỹ thuật

| Mục | Yêu cầu |
|---|---|
| Khung | **1080 × 1920 (9:16)** · H.264 · **30 fps** · MP4 faststart |
| Dung lượng | ≤ 500 MB (thực tế 60–120 MB/clip) |
| Âm thanh | AAC 48 kHz, mono hoặc stereo |
| Thời lượng | ghi trong app ≤ 10 phút · **upload ≤ 60 phút** · Series: mỗi clip 30 s – 20 phút |
| Caption | tối đa **2.200 ký tự** (theo Content Posting API) |

**Safe zone** (theo template In-Feed của TikTok, bám thiết kế "xấu nhất"):

```
1080 × 1920
┌──────────────────────────┐  y=0
│  tránh 240 px (tab feed)│
│ ┌──────────────────────┐ │
│ │ vùng chữ AN TOÀN     │ │  x: 120 → 780
│ │  y: 240 → 1260       │ │  (tránh thêm 300 px bên phải dưới y=840)
│ │  (nút like/comment/  │ │
│ │   share ở mép phải)  │ │
│ └──────────────────────┘ │
│  tránh 660 px (caption,  │
│  username, tên sound)    │
└──────────────────────────┘  y=1920
```

⇒ **Phụ đề burn-in đặt ở y ≈ 1.020–1.230 px**, font ≥ 48 px, đậm, tối đa 2 dòng, căn trái trong x 120–780. Không đặt chữ ở 4 mép.

### 2.2 Chính sách nội dung

| Quy tắc TikTok | Áp dụng cho AMBER EYES |
|---|---|
| Cấm nội dung **gây sốc / máu meát / kinh dị** | Kênh đã tuân thủ V9 (không mô tả bạo lực, thương tích, thi thể, cách gây án) ⇒ **vốn đã an toàn**. Giữ nguyên V9 khi cắt clip — TikTok xử lý nặng hơn YouTube |
| Cho phép **"tài liệu/giao dục nâng cao nhận thức về hành vi tội phạm"** | Đây đúng là mô hình của kênh (10 chỉ dấu tâm lý K10) ⇒ nêu rõ tính chất *phân tích*, không phải *phóng sự giật gân* |
| Cấm **khen ngợi/tôn vinh tội phạm**, cấm hướng dẫn phạm tội | Không dùng hook kiểu "anh ta đã giết… một cách tuyệt hay"; không nêu kỹ thuật/thủ đoạn |
| Cấm **AIGC không ghi nhãn** | Bắt buộc bật toggle "AI-generated content" + ghi nhãn trong caption + watermark chữ nhỏ |
| Cấm **nội dung "không có gì mới"** → **không được hiện trên For You** | **Không được up lại video 16:9 của YouTube**, không được mang watermark nền tảng khác. Phải xuất bản dọc riêng từ master sạch |
| Cấm trùng lặp: *"Đừng đăng lại nội dung của chính bạn"* | Mỗi clip một file riêng, mở đầu khác nhau, không re-upload cùng file |

### 2.3 Âm thanh — điểm rủi ro lớn nhất

> **Bằng chứng:** "Each platform's licensed music library only covers that platform. TikTok's Commercial Music Library is cleared for TikTok only, YouTube's Audio Library is cleared for YouTube only." (Adobe Premiere — Music licensing FAQ) + GEMA.

Trong `provenance.json` có **213 tài sản từ YouTube Audio Library**:

- **2 file BGM**: `assets/bgm/bgm_guitar_acoustic_60s.mp3`, `assets/bgm/bgm_church_organ.mp3`
- **211 file SFX** trong `assets/sfx/t3/`, `assets/sfx/t2/` … (nền môi trường + tiếng động)

⇒ **Điều khoản của YouTube Audio Library chỉ cho dùng trong nội dung trên YouTube. Clip TikTok dùng các file này là dùng sai giấy phép.** Rủi ro: âm thanh bị mute, video bị gỡ, kênh bị trừ điểm.

**Luật âm thanh cho clip TikTok (áp dụng từ clip đầu tiên):**

| Nguồn | Trạng thái |
|---|---|
| BGM MiniMax Music (9 file trong `assets/bgm/`) | ✅ dùng được — **có điều kiện**: phải xác minh quyền thương mại của bề mặt đã sinh (xem mục 2.4) |
| SFX tự tổng hợp `.work/make_sfx.py` | ✅ dùng được — của chính kênh |
| Freesound **CC0** | ✅ dùng được — đã quy định CC0 trong A8 |
| **YouTube Audio Library** (2 BGM + 211 SFX) | ❌ **CẤM trong clip TikTok** |
| TikTok Commercial Music Library | ⚠️ chỉ dùng âm thanh gốc *trong app*, **không nhúng vào file** (nếu nhúng thì file đó không dùng lại được cho YouTube) |
| Nhạc trending | ❌ không dùng — không kiểm soát được bản quyền và không tái sử dụng được |

⇒ **Quyết định thiết kế:** âm thanh clip TikTok **dựng riêng**, chỉ gồm *giọng + BGM MiniMax + SFX tổng hợp/CC0*. Kết quả: một file master sạch, đăng được ở mọi nền tảng, không bao giờ bị claim.

### 2.4 Cần xác minh trước khi dùng BGM MiniMax ở clip *thương mại*

`provenance.json` ghi BGM sinh bằng **"MiniMax Music — sinh nhạc qua mcode-tools"**. Điều khoản MiniMax có hai lớp:

- **Open Platform (API)**: người dùng **giữ quyền sở hữu** nội dung sinh ra; không cấm thương mại hóa ⇒ ✅ dùng được.
- **MiniMax Audio app / web (bản consumer)**: điều khoản ghi *"permit you to use the Services for your personal, non-commercial use only"*; gói trả phí có ghi *"Commercial Use rights for new songs made"*.

⇒ **Việc cần làm (1 lần, trước khi đăng clip đầu tiên):** xác minh bề mặt nào đã sinh 9 file BGM. Nếu là app consumer mà không có gói thương mại ⇒ **thay 9 file BGM bằng SFX tổng hợp + Freesound CC0** (hoặc mua 1 gói Audio Package rẻ nhất). Ghi kết quả vào `provenance.json` (L7).

---

## 3. Chiến lược nội dung — "Chỉ dấu" series

### 3.1 Vì sao cấu trúc này

Kênh đã có **10 chỉ dấu tâm lý & hành vi** (K10 / tiêu chuẩn A2c) — đây là tài sản độc quyền, tách biệt với hầu hết kênh true crime (họ kể chuyện, không phân tích). TikTok cần **một lý do để quay lại lần 2**: *mỗi clip dạy đúng một dấu hiệu*, xem xong muốn biết dấu hiếu tiếp theo.

**Cấu trúc series:**

```
Series TikTok: "CHỈ DẤU" (mỗi tập hồ sơ = 1 playlist gồm 2–4 clip)
  Clip 1 — Dấu hiệu #1: chủ nghĩa làm mình vượt quá ranh giới đạo đức
  Clip 2 — Dấu hiệu #3: tuyển chọn nạn nhân có điểm yếu
  Clip 3 — Dấu hiệu #7: thủ đoạn (MO) khác dấu ấn (signature)
  Clip 4 — "Bản án tâm lý" + dẫn về tập đầy đủ trên YouTube
```

Mỗi clip có **chỉ dấu tâm lý** làm chủ đề, **tập hồ sơ** làm ngữ cảnh. Người xem TikTok không cần xem cả tập 25 phút để hiểu clip; người xem YouTube nhận được "phần còn lại".

### 3.2 Khung thời gian 1 clip (mẫu 60–75 s)

| Mốc | Nội dung | Ghi chú |
|---|---|---|
| 0,0–3,0 s | **Hook chữ trên hình**, 1 câu, ≤ 12 từ, đặt ở y 300–700 | quyết định giữ người xem hay lướt |
| 3,0–12,0 s | Câu mở ngữ cảnh (giọng Host) + nền tối, chữ phụ | nói **"hãy hình dung"** cho phần minh hoạ (K3) |
| 12,0–45,0 s | Thân bài: chỉ dấu, 2–3 ví dụ từ hồ sơ, chữ trên hình dạng thẻ hồ sơ | không nêu chi tiết bạo lực (V9) |
| 45,0–58,0 s | **Phản chuyển**: "nhưng dấu hiệu này chưa nói lên tất cả" | tạo khoảng trống |
| 58,0–68,0 s | Chốt: 1 dòng tóm tắt + tên tập + CTA "Xem tập đầy đủ ở YouTube (link trong bio)" | ảnh chụp màn hình? không — chữ Pillow |
| 68,0–75,0 s | Thẻ kết: logo + "Amber Eyes · Hồ sơ có thật" | đúng khuôn của tập (H-kết) |

### 3.3 Bộ hook chữ (mẫu — cần duyệt, L4/K2)

> Không dùng câu trích bịa; không nêu tội danh cụ thể trong hook; không giật tít "rùng rợn".

1. *"Hắn không giấu tội. Hắn kể một câu chuyện khác."*
2. *"Có một câu hỏi mà cảnh sát hỏi sai."*
3. *"Kẻ gây án chọn nạn nhân. Không phải ngẫu nhiên."*
4. *"Ba dấu hiệu tâm lý đã có từ năm đầu tiên."*
5. *"Hồ sơ này khép lại — nhưng câu hỏi thì không."*

### 3.4 Caption (mẫu)

```
Hắn không giấu tội. Hắn kế một câu chuyện khác. 👁️

Tập 02 · Đại tá hai mặt — chỉ dấu #2: nạn nhân không ngẫu nhiên.
Hồ sơ có thật, dữ kiện có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Từ khóa: Amber Eyes, tâm lý tội phạm, hồ sơ tội phạm

#AmberEyes #TamLyToiPham #HosoCoThat #PhanTich #TrueCrime
#HorrorStory #TamsLy #MoiTuanMotTap
```

- Dòng 1 = hook (lặp lại chữ hook trên hình) → TikTok index caption cho tìm kiếm.
- **Luôn có "Tập N" + tên tập** → gom chủ đề theo series.
- Hashtag: 5–8, trong đó 2 hashtag thương hiệu cố định (`#AmberEyes`, `#HosoCoThat`) để không rơi khỏi chủ đề.
- Có dòng *"Hồ sơ có thật, dữ kiện có nguồn"* → giảm rủi ro tin giả.
- Có dòng *"Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý"* → nhãn AIGC (bắt buộc).

---

## 4. Pipeline sản xuất clip dọc

> Bám đúng quy trình của dự án (AGENTS L1–L11, tiêu chuẩn A3/A9). Mọi bước có cổng đo thật, không "nói xong" khi chưa đo (L3).

### Bước 0 — Cổng vào: chỉ dựng từ tập đã có QC đạt

Danh sách tập sẵn sàng (đã có master + QC đầy đủ): **Tập 02, 05, 06, 07** (VN). Tập 01 phải dựng lại trước (README ghi "video hiện có không còn khớp kịch bản").
⇒ Bắt đầu bằng **Tập 02** (QC 10/10 cổng, có `Tap02_master.mp4` + `Tap02.srt` + `timeline_s_t02.json`).

### Bước 1 — Chọn khoảnh cắt (tự động, có người duyệt)

- Input: `timeline_s_t02.json` (mốc thời gian từng câu) + `shots.json` + `Tap02.srt`.
- Script `.work/_tk_pick_segments.py`: tìm các đoạn liên tiếp **45–90 s** có ≥ 1 câu chứa nội dung chỉ dấu tâm lý (khớp từ khoá trong `K10` của hồ sơ tập) → xuất 4 đề xuất/tập kèm mốc bắt đầu–kết thời gian.
- **Cổng:** người dùng duyệt danh sách đoạn (L6 — quyết định nội dung không tự ý chốt).

### Bước 2 — Lời dẫn clip (viết mới, không cắt từ kịch bản tập)

- Viết `02_SAN_XUAT/TIKTOK/TapXX/Kichban_Clip_TapXX.md` theo khung 3.2: mỗi clip có câu hook + 4–6 câu thân bài + 1 câu chốt.
- **Áp dụng đầy đủ luật kịch bản của kênh:** K1 (đối chiếu nguồn) · K2 (câu trích nguyên văn) · K3 (không gán lời thoại cho người thật) · K4/V9 (không mô tả bạo lực) · K5 (không chẩn đoán) · K8 (logic) · K10 (10 chỉ dấu).
- **Cổng:** người dùng duyệt văn bản lời dẫn trước khi đọc giọng.

### Bước 3 — Giọng đọc (tái dùng y hệt bộ A)

- `parse_kichban.py`-style → `acting_tiktok_tXX.json` → `tts_sentences.py` (Higgs, bộ A: Host `English_CaptivatingStoryteller` 0,90 · C `English_AssertiveQueen` 0,92).
- **G1–G4, G11**: không `...`, không `<#s#>`, 1 nghỉ `<#0.35#>` sau dấu `:`, 4 cảm xúc an toàn, pitch = 0, số đọc bằng chữ.
- **G10/G12**: đo CER từng vai, nghe liền theo vai.
- ⚠ **Vai Sói (điều tra viên) có CER 3,1 %** — trong clip nên ưu tiên **Host + Chuyên gia** (Cáo); nếu cần Sói thì rút lời ≤ 8 s hoặc đổi giọng theo `90_LUU_TRU/BaoCao_SangLocGiongDieuTraVien_20261027.md`.

### Bước 4 — Nền dọc 9:16 (điểm tốn công nhất)

> **Không cắt từ bản 16:9** — sẽ mất 2/3 khung, vi phạm tinh thần "mọi khung đều có chủ đích" (đã ghi ở `PhuongAn_Video_GioiThieu_Kenh.md` Concept D).

| Phương án | Cách làm | Chi phí | Chất lượng |
|---|---|---|---|
| **A (khuyến nghị)** | Sinh **nền dọc** bằng pipeline FLUX Kaggle đã có sẵn (`.work/bg_jobs_*.json` → Kaggle kernel) — 1080×1920, ~40–60 nền dùng chung cho toàn bộ clip | 0 đồng, chờ Kaggle | cao, đúng phong cách |
| B (MVP) | Dùng nền 16:9 có sẵn: **blur-fill** hai mép + zoom chậm 4 % + lớp hạt phim | 0 đồng, làm ngay | trung bình, hợp lý cho lô đầu |

⇒ **Đề xuất: B cho 3 clip thử nghiệm (Tập 02), A cho lô tiếp theo sau khi template được duyệt.**

**Cổng H19:** nền phải có **nội dung cảnh**, không gradient trừu tượng. **Bẫy #1:** gỡ mọi thông tin chữ khỏi prompt (AI vẽ chữ rác); chữ trên hình **luôn do Pillow vẽ sau**.

### Bước 5 — Chữ trên hình (Pillow)

- Tái dùng `assets/brand/channel.json` (màu/font/logo) và `.work/make_logo.py` (`ml.INK/RED/AMBER/TEXT/MUTED`).
- **Georgia chỉ cho wordmark "AMBER EYES"**; chữ có dấu dùng **Segoe UI / Malgun / Yu Gothic** (bẫy #3).
- Phụ đề burn-in theo lời đọc đã đo CER (đồng bộ tuyệt đối, G6): y 1.020–1.230 px, x 120–780, font 52 px đậm, nền scrim mờ 35 %.
- Vị trí chữ: hook ở nửa trên (y 300–700), phụ đề ở dải dưới an toàn, logo góc phải trên (y < 240 ⇒ đặt y 60–200 nhưng **tránh x > 780**).

### Bước 6 — Âm thanh (chỉ nguồn an toàn — mục 2.3)

- Lấy stem giọng từ `audio_s_t02/` → trộn BGM MiniMax + SFX tổng hợp/CC0.
- Chuẩn hoá **2 lượt** `loudnorm I=-16:TP=-1.5:LRA=11` (A7) — TikTok không yêu cầu loud hơn, giữ đồng nhất với kênh YouTube.
- **A1/V4**: không câm tuyệt đối > 0,3 s; luôn có lớp nền môi trường dưới.
- **Đo lại trên mp4 cuối**, không đo trên wav trung gian (A7).

### Bước 7 — Cổng QC clip (script mới `.work/qc_tiktok.py`)

Đạt **toàn bộ** mới được đăng:

| # | Kiểm | Ngưỡng |
|---|---|---|
| T1 | Khung / tỉ lệ | 1080 × 1920, 9:16 |
| T2 | Codec / fps | H.264 + AAC, 30 fps |
| T3 | Dung lượng | ≤ 500 MB |
| T4 | Độ dài | 30–95 s (mục tiêu 45–90) |
| T5 | Âm lượng | −16 ± 1 LUFS · true peak ≤ −1,5 dBFS |
| T6 | Khoảng câm | 0 khoảng > 0,3 s ở −60 dB |
| T7 | Lệch hình/tiếng | ≤ 0,05 s |
| T8 | Giải mã | 0 lỗi |
| T9 | **Safe zone** | mọi khung chữ nằm trong x 120–780, y 240–1260 (tự động kiểm bằng mask vùng UI) |
| T10 | **Không watermark nền tảng khác** | 0 khung chứa watermark YouTube/TikTok |
| T11 | **Chữ AI** | 0 chữ rác / 0 chữ trùng / 0 chữ chìm (đo tương phản) |
| T12 | **Không mặt người thật** | 0 vi phạm (giữ nguyên nguyên tắc kênh) |
| T13 | **Từ cấm** | không có từ trong danh sách A9.2 (V9) |
| T14 | Hook | trong 3 giây đầu có chữ hook đọc được ở 100 % khung |

Báo cáo: `02_SAN_XUAT/TIKTOK/TapXX/BaoCao_QC_TikTok_TapXX.md` (theo khuôn báo cáo QC hiện có của dự án).

### Bước 8 — Đóng gói

```
02_SAN_XUAT/TIKTOK/TapXX/
├── clip01_<ten>.mp4          # master 9:16 sạch, không watermark
├── clip01_caption.txt        # caption + hashtag + nhãn AIGC
├── clip01_qc.md              # báo cáo QC
└── checklist_dang.md         # trạng thái các mục đăng
```

> **L10: không commit media.** Chỉ commit tài liệu + code + config; mp4 nằm trên đĩa, bị `.gitignore` loại.

### Bước 9 — Đăng (tay)

Đăng trên app: **đăng bản master sạch** (không tải lại từ YouTube), bật **toggle "AI-generated content"**, dán caption, chọn **thẻ bìa (cover) 9:16**, đặt **tài khoản 18+** nếu nội dung nhạy cảm.

---

## 5. Thiết lập tài khoản (1 lần, trước khi đăng clip đầu tiên)

| Hạng mục | Việc |
|---|---|
| Handle | `@ambereyes` — kiểm tra còn trống, đăng ký ngay (handle trống có thể bị giữ) |
| Loại tài khoản | **Personal** (Business làm hạn chế nhạc và không dùng được cho khoản thưởng) |
| Ảnh đại diện | `assets/brand/avatar_800.png` → cắt 720×720, nền tối, mắt hổ phách |
| Bio (≤ 80 ký tự) | `Phân tích tâm lý tội phạm qua hồ sơ có thật. Hồ sơ có thật, dữ kiện có nguồn. ↓ xem tập đầy đủ` |
| Link | → trang kênh YouTube (dùng link-in-bio nếu cần nhiều đích) · **Tập 01: `https://youtu.be/lDVXjeFLn48`** (19/11/2026) |
| Bật | "AI-generated content" mặc định khi đăng · ghim bài giới thiệu |
| Quyền riêng tư | 18+ (nội dung hồ sơ tội phạm) |
| Ngôn ngữ ứng dụng | Tiếng Việt |
| Bảo mật | 2FA, không bật "bình luận tất cả" cho tài khoản mới |

**Bài ghim đầu tiên:** bản dọc 15–20 s của trailer (Concept D trong `PhuongAn_Video_GioiThieu_Kenh.md`) + 1 câu giới thiệu kênh.

---

## 6. Lịch đăng và mở rộng

### 6.1 Nhịp đăng

- **2–3 clip/tuần** là nhịp an toàn (Buffer: đăng ≥ 1/tuần trong 20 tuần → +450 % tương tác mỗi bài).
- Bắt đầu với **3 clip/tuần trong 4 tuần đầu** → 12 clip → đủ dữ liệu để chốt template.
- Ưu tiên **nhất quán** hơn tần suất: giữ đúng khung giờ (đề xuất 20:00–22:00 giờ VN, dựa trên dữ liệu thật của TikTok Studio sau 2 tuần).

### 6.2 Lộ trình 90 ngày

| Giai đoạn | Nội dung | Số clip | Mốc đo |
|---|---|---|---|
| **T0 (2 ngày)** | Tạo tài khoản, brand kit dọc, xác minh BGM MiniMax (mục 2.4), làm bản dọc trailer | 1 | tài khoản hoạt động, 1 video đăng thử |
| **T1 (tuần 1–2)** | Pipeline clip Tập 02 (phương án B — blur-fill), 3 clip | 3 | `.work/qc_tiktok.py` đạt 14/14 cổng |
| **T2 (tuần 3–4)** | Sinh nền dọc FLUX (phương án A), làm lại 3 clip Tập 02 + 3 clip Tập 05 | 6 | đo hold-rate để so B vs A |
| **T3 (tuần 5–8)** | 3 clip/tuần cho Tập 05, 06, 07 | 12 | chốt template cuối cùng |
| **T4 (tháng 3)** | Mở rộng Tập 01 (sau khi dựng lại) + Tập 08–12 | 12 | playlist "Hồ sơ 01" lên profile |
| **T5 (tháng 4–6)** | Toàn bộ 29 tập × 2–4 clip | ~87 | phủ đủ series |

**Tổng công việc ước tính:** 1 clip ≈ 1,5–3 giờ máy (nếu chạy tự động hoá) ⇒ 87 clip ≈ **130–260 giờ**. Đây là lý do **phải tự động hoá** bằng `.work/make_tiktok_clip.py` chứ không dựng tay từng clip.

---

## 7. Đo lường (L3 — không nói "xong" khi chưa đo)

Bảng theo dõi `02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv`:

| Chỉ số | Nguồn | Mục tiêu tham khảo |
|---|---|---|
| Lượt xem 3 giây (hold rate) | TikTok Studio | ≥ 60 % |
| Tỉ lệ xem hết | TikTok Studio | ≥ 25 % (clip 60 s) |
| Thời gian xem trung bình | TikTok Studio | ≥ 22 s |
| Lượt xem YouTube tăng sau khi đăng | YouTube Studio (so sánh 7 ngày trước/sau) | +20 % |
| Click vào link bio | TikTok Studio | ≥ 1 % lượt xem |
| Comment hỏi về tập | thủ công | ≥ 3/tập |

**Vòng lặp:** sau 12 clip → chọn **2 chủ đề + 1 cấu trúc hook** cho tốt nhất → nhân bản cho các tập còn lại.

---

## 8. Rủi ro và bẫy (chặn trước khi làm)

| # | Bẫy | Hệ quả | Cách chặn |
|---|---|---|---|
| **T1** | Dùng nhạc/SFX từ YouTube Audio Library trong clip TikTok | mute/gỡ video, trừ điểm kênh | danh sách đen 213 file trong mục 2.3; `qc_tiktok.py` kiểm provenance từng file âm thanh trong clip |
| **T2** | Đăng lại video 16:9 của YouTube, hoặc bản tải về có watermark | **không hiện trên For You** | chỉ xuất bản dọc riêng từ master sạch (bước 7) |
| **T3** | Không bật nhãn AIGC | video bị gỡ / hạn chế | bật toggle + dòng ghi nhãn trong caption + watermark nhỏ trên hình |
| **T4** | Hook giật tít kiểu giật gân ("đáng sợ", "rùng rợn") | vi phạm "sensational content" | giữ V9 + K5; hook mang tính *phân tích* |
| **T5** | Kỳ vọng kiếm tiền trực tiếp trên TikTok ở VN | thất vọng | Creator Rewards không mở ở VN (mục 0) ⇒ mọi số đo hướng về YouTube |
| **T6** | Dùng nhạc TikTok Commercial Music Library nhúng vào file | file đó không tái dùng được cho YouTube | chỉ dùng âm thanh **đã nhúng sẵn** trong master |
| **T7** | Giả định BGM MiniMax được phép thương mại | rủi ro pháp lý | xác minh mục 2.4 trước clip đầu; ghi vào `provenance.json` |
| **T8** | Crop 16:9 → 9:16 | mất 2/3 khung, mất tinh thần hình ảnh | dựng nền dọc riêng (bước 4) |
| **T9** | Chữ trên hình bị UI TikTok che | không đọc được | safe zone T9 |
| **T10** | AI vẽ chữ rác | vi phạm chất lượng (đã xảy ra nhiều lần) | gỡ chữ khỏi prompt; Pillow vẽ sau (bẫy #1) |
| **T11** | Nhiều phiên cùng sửa file tài liệu chung | mất dòng đã viết | backup `.work/_cu/` trước khi ghi (L5); **không commit** khi còn phiên khác đang sửa (L10) |
| **T12** | Đăng lại cùng một file ở tài khoản khác | cả tài khoản mất đề xuất | 1 tài khoản, 1 file = 1 lần đăng |

---

## 9. Việc cần người dùng chốt / làm (checklist)

| # | Việc | Người |
|---|---|---|
| 1 | Duyệt **kế hoạch này** | Người dùng |
| 2 | Duyệt **bộ hook chữ** (mục 3.3) trước khi viết kịch bản clip | Người dùng |
| 3 | Duyệt **danh sách 4 đoạn cắt** đề xuất cho Tập 02 trước khi dựng (bước 1) | Người dùng |
| 4 | Tạo tài khoản `@ambereyes` (mục 5) | Người dùng |
| 5 | **Xác minh quyền thương mại BGM MiniMax** (mục 2.4) | Người dùng + AI tra ToS |
| 6 | Cho phép chạy FLUX Kaggle sinh nền dọc (0 đồng, chờ GPU) — hoặc chấp nhận phương án B | Người dùng |
| 7 | Gộp bộ luật T1–T14 vào `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (mục A11) | Người dùng duyệt, AI thực hiện |

---

## 10. Bộ luật TikTok (đề xuất gộp vào tiêu chuẩn, mục A11)

| # | Luật |
|---|---|
| **T1** | **CẤM** dùng tài sản từ YouTube Audio Library (2 BGM + 211 SFX) trong bất kỳ tài sản nào định đăng TikTok. Chỉ dùng: BGM MiniMax (đã xác minh thương mại) · SFX tự tổng hợp · Freesound CC0 |
| **T2** | **CẤM** đăng lại video 16:9 của YouTube hoặc bản tải về có watermark. TikTok xuất bản dọc riêng từ master sạch |
| **T3** | **PHẢI** bật toggle "AI-generated content" khi đăng **và** ghi dòng nhãn AIGC trong caption |
| **T4** | **PHẢI** giữ nguyên V9 + K4 + K5 trong clip (TikTok xử lý nặng hơn YouTube) |
| **T5** | **CẤM** hook giật tít kiểu giật gân; hook phải mang tính phân tích |
| **T6** | **PHẢI** đặt mọi chữ trong safe zone x 120–780, y 240–1260 (1080×1920) |
| **T7** | **PHẢI** đo 14 cổng QC (`.work/qc_tiktok.py`) trước khi đăng; 0 lỗi |
| **T8** | **CẤM** commit media TikTok (L10) — chỉ tài liệu + code |
| **T9** | **PHẢI** ghi nguồn âm thanh dùng trong clip vào `provenance.json` (L7) |
| **T10** | **CẤM** dùng nhạc TikTok Commercial Music Library nhúng trong file master (file đó không tái dùng được cho YouTube) |
| **T11** | **PHẢI** có "Tập N" + tên tập trong caption (gom chủ đề series) |
| **T12** | **CẤM** đăng lại cùng một file ở tài khoản khác |
| **T13** | **PHẢI** đo lại âm lượng trên mp4 cuối, không đo trên wav trung gian (A7) |
| **T14** | **CẤM** cắt 16:9 → 9:16; phải dựng nền dọc riêng (phương án A) hoặc blur-fill (phương án B) |

---

## 11. Tài liệu liên quan

- `AGENTS.md` — L1–L11 (luật chung) · K1–K10 (kịch bản) · G1–G13 (giọng) · A1–A11 (âm thanh) · H9/H17/H19 (hình)
- `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` — mục A3 (lệnh chạy), A9 (QC), A11 (bài học)
- `02_SAN_XUAT/BRAND/PhuongAn_Video_GioiThieu_Kenh.md` — Concept D (bản dọc 15–20 s) tái dùng cho bài ghim
- `assets/brand/channel.json` — token thương hiệu (màu, font, logo)
- `provenance.json` — sổ nguồn gốc tài sản (L7)
- `README.md` — trạng thái từng tập (chọn tập nguồn)

## 12. Nguồn tham khảo (kiểm chứng 18/11/2026)

- TikTok Community Guidelines (bản 25/08/2026, hiệu lực 24/09/2026) — phần "Shocking and Graphic Content", "Violent and Criminal Behavior" — https://scanrecords.org/archive/tiktok/guidelines
- TikTok Ads — Violence and Dangerous Activities (01/2026) — https://ads.tiktok.com/resources/help/article/tiktok-ads-policy-violence-and-dangerous-activities
- TikTok — AIGC disclosure (toggle "AI-generated content", C2PA) — https://seller-us.tiktok.com/university/essay?knowledge_id=491489038501663
- TikTok — Unoriginal Content (không có gì mới ⇒ không hiện For You) — https://seller-th.tiktok.com/university/essay?knowledge_id=10011344
- TikTok Creator Rewards Program (8 nước; video > 1 phút; 10k follower + 100k view/30 ngày) — https://support.tiktok.com/de/business-and-creator/creator-rewards-program/creator-rewards-program
- TikTok Content Posting API (Direct Post: client chưa audit ⇒ private, 5 user/24h, ~15 post/ngày) — https://developers.tiktok.com/docs/en/content-sharing-guidelines
- TikTok video specs & safe zone (1080×1920; top 240 / bottom 660 / side 120 / right 300 dưới y=840) — https://ads.tiktok.com/business/creativecenter (mẫu In-Feed) · https://hubstudio.ai/resources/insights/tiktok-video-specs
- Adobe Premiere — Music licensing FAQ (thư viện nhạc mỗi nền tảng chỉ phủ nền tảng đó) — https://helpx.adobe.com/premiere/mobile/add-audio/music-licensing-faq.html
- YouTube YPP — expanded program đã mở đầy đủ tại Việt Nam — https://support.google.com/youtube/answer/13429240
- YouTube — thay đổi ngưỡng YPP từ 01/02/2027 (Shorts cần 10M view/90 ngày) — https://support.google.com/youtube/blog/451804019
- MiniMax Audio — Music Creation Terms of Use (quyền thương mại phụ thuộc bề mặt dùng) — https://www.minimax.io/audio/doc/terms-of-service-music.html
- TikTok Series (30 s–20 phút/clip, tối đa 80 clip) — https://uppbeat.io/blog/tiktok/how-to-make-a-series-on-tiktok

---

## 13. Trạng thái triển khai — bộ kịch bản clip theo tập (cập nhật 20/11/2026)

### 13.1 Đã xong

| Tập | Bộ kịch bản clip | Trạng thái |
|---|---|---|
| 01 | `02_SAN_XUAT/TIKTOK/Tap01/KE_HOACH_CLIP_TAP01.md` + `SPEC_AUDIO_CLIP_TAP01.json` + caption/mô tả dài | ✅ đã xuất bản (4 clip) |
| **02** | `02_SAN_XUAT/TIKTOK/Tap02/KE_HOACH_CLIP_TAP02.md` + `SPEC_AUDIO_CLIP_TAP02.json` + `Caption_TK*.txt` + `MoTa_Dai_TK*.txt` | ✅ **kịch bản đã viết (5 clip, 53 câu)** — chờ người dùng duyệt rồi đọc giọng |

**Cách sinh:** `.work/_build_tk_tap02.py` là **nguồn sự thật duy nhất** — sinh ra cả `.md` lẫn `.json` lẫn caption, nên không thể lệch nhau (G6). Sửa kịch bản thì sửa file đó rồi chạy lại, **đừng sửa tay file kết quả**.

### 13.2 Bẫy mới phát hiện khi làm Tập 02 (bổ sung cho bảng mục 8)

| # | Bẫy | Hệ quả | Cách chặn |
|---|---|---|---|
| **T13** | SFX Tập 02 có **hai bản cùng tên**: `assets/sfx/t2/*.wav` (YouTube Audio Library — **cấm**) và `assets/sfx/t2/_code/*.wav` (tự tổng hợp — **được**) | dùng nhầm bản cấm ⇒ mute/gỡ video | clip TikTok lấy SFX **từ `_code/`**; `qc_tiktok.py` kiểm provenance từng file |
| **T14** | Bản 16:9 đã xử lý `assets/bg/t2_*.png` **đã bị dọn khỏi `assets/bg/`** — chỉ còn ảnh gốc `assets/bg/_raw/t2_*` (2752×1536) | pipeline cũ không tìm thấy nền | clip dọc dùng `tk02_*` riêng; nếu dùng phương án B blur-fill thì lấy trực tiếp từ `_raw/`; muốn chạy lại pipeline cũ thì `fix_backgrounds.py` |
| **T15** | Tập 02 dùng **bộ giọng khác Tập 01** cho vai D và C (`D_NEW_subbass-husky_t02`, `C_NEW_alto-brisk_t03`) | clip lệch giọng với tập trên YouTube ⇒ nghe "hai người khác nhau" | clip **bắt buộc** dùng đúng refs trong `SPEC_AUDIO_CLIP_TAP02.json` (`ROLE_REF_MAP` của `.work/generate_higgs_prod_t02vi.py`) |
| **T16** | Ước lượng thời lượng clip bằng cảm tính | cổng QC độ dài (45–95 s) bị lệch ⇒ phải cắt lại từ đầu | đo **tỉ lệ đọc thật** theo vai trên master tập (`.work/timeline_s_tXX.json`, timeline đo bằng ASR), rồi chiếu theo số từ **sau khi đổi số→chữ** (`vi_numbers`) |

### 13.3 Cách ước lượng thời lượng clip (đã kiểm chứng, dùng lại cho tập sau)

| Bước | Làm gì | Kết quả đo được (Tập 02) |
|---|---|---|
| 1 | Đọc `.work/timeline_s_tXX.json` (timeline **đo bằng ASR trên mp4 thành phẩm**) | 203 câu, tổng 1.346,5 s lời |
| 2 | Đếm số từ **sau `vi_numbers()`** (đúng phần TTS đọc) | H 3,37 · D 3,73 · C 4,15 từ/giây |
| 3 | Ước lượng từng câu = số từ × tỉ lệ của vai đó; cộng `pause_after` | 5 clip: 62,5–82,6 s |
| 4 | **Kiểm chéo leave-one-out** trên 203 câu thật | MAE 11,0 %/câu · trung vị 6,7 % |
| 5 | **Mô phỏng mức clip** (nhóm 13 câu × 2.000 lần) | MAE 3,7 % · p90 7,3 % ⇒ clip 80 s có sai số ±5,8 s |

⇒ Số trên là **ước lượng có cơ sở đo**, không phải số đo thật của clip (chưa có WAV). Số đo thật lấy sau khi sinh WAV: cộng `dur` từng file + `pause_after`, rồi đo lại trên mp4 cuối (A7).

### 13.4 Tự kiểm kịch bản trước khi đọc giọng

`.work/_build_tk_tap02.py` tự chạy **14 mục kiểm** mỗi lần sinh lại (tất cả đang **ĐẠT**):

`V9/A9.2 từ cấm` · `G1 (một thẻ <#0.35#>/câu, sau dấu ':', không '...')` · `G3/G4/G5 (emotion · speed · pitch=0)` · `V3 (số trên thẻ overlay phải có trong câu được trỏ tới)` · `hook ≤ 12 từ` · `caption ≤ 2.200 ký tự` · `hashtag 5–8 có #AmberEyes + #HosoCoThat` · `độ dài clip trong cổng 45–95 s` · `file nguồn của nền dọc có thật` · `K10 mỗi clip ≥ 1 chỉ dấu` · `K5 có câu cảnh báo không có chẩn đoán lâm sàng` · `K2 câu trích nguyên văn trong kịch bản tập` · `G6 .md/.json chung nguồn` · `L3 thời lượng có số đo thật làm cơ sở`.

### 13.5 Việc còn lại cho Tập 02

| # | Việc | Người |
|---|---|---|
| 1 | Duyệt văn bản lời dẫn `KE_HOACH_CLIP_TAP02.md` **trước khi đọc giọng** (L4) | Người dùng |
| 2 | **Điền link YouTube Tập 02** — hiện là placeholder `[LINK_TẬP 02 — cần điền]`, không tự bịa (L2) | Người dùng |
| 3 | Sửa **xung đột thương hiệu lốp xe** trong kịch bản tập: `1.17#1` ghi *Kumho*, `nguon_tham_khao.md` ghi *Yokohama IG20* (clip không nêu thương hiệu nào nên vẫn an toàn) | Người dùng |
| 4 | Sinh **26 nền dọc `tk02_*`** (mục 7 của `KE_HOACH_CLIP_TAP02.md`) — **ĐÃ XONG 26/26** (mục 14); 8 nền AI thật + 18 nền dự phòng crop, cần thay 18 nền dự phòng khi có credit | AI (cần duyệt FLUX) |
| 5 | **Xác minh quyền thương mại BGM MiniMax** (mục 2.4) — vẫn chưa làm | Người dùng + AI |
| 6 | Tạo **53 file WAV** theo `SPEC_AUDIO_CLIP_TAP02.json` + qua 7 cổng audio (mục 5.3) | Người dùng |
| 7 | Dựng 5 clip 9:16 + chạy 14 cổng QC clip + `BaoCao_QC_TikTok_Tap02.md` | AI (sau khi được duyệt) |
| 8 | **Điền link YouTube Tập 02** vào 5 file caption + profile (đang placeholder) | Người dùng |

---

## 14. ẢNH NỀN DỌC TẬP 02 — ĐÃ TẠO 26/26 (20/11/2026)

### 14.1 Kết quả đo thật

| Chỉ số | Số đo |
|---|---|
| Số nền dọc `assets/bg/tk02_*.png` | **26/26** — đủ cho cả 5 clip (TK1 9 · TK2 7 · TK3 10 · TK4 8 · TK5 6) |
| Kích thước | **1080×1920 — 26/26 đúng**, sai số 0 |
| Nguồn | **8 nền AI thật** (connector `__matrix__generate_image`, 9:16, area 2K) + **18 nền dự phòng** (crop từ ảnh gốc 16:9) |
| Dòng `provenance.json` | **+26** (8 dòng có `prompt` = AI thật · 18 dòng `prompt: null` = dự phòng) ⇒ 3.722 dòng tổng |
| Độ sáng vùng chữ hook (y 270–730, x 120–780) | **mean 42,4 · max 56,9** (bộ `tk01_*` đã xuất bản: mean 41,6 · max 74,0) ⇒ không sáng hơn bộ đã đăng |
| Độ sáng vùng phụ đề (y 996–1254) | mean 64,8 (bộ `tk01_*`: 82,1) |
| Vết ngang trong ảnh | đo theo từng cột (`|Δ| > 18` ở > 70 % số cột): **0 dải** trong 26 ảnh — chỉ 2 mép trên/dưới do crop |
| Backup | `.work/_cu/tk02_provenance_20261120_0859/` · `.work/_cu/tk02_fallback_prov_20261120_1207/` · ảnh v1: `.work/_cu/fallback_v1_20261120_121032/` · ảnh v2: `.work/_cu/tk02_fallback_img_20261120_1217/` |

**Quy trình đã chạy (đo được):** `.work/_tk_upload_refs_t02.py` (26/26 URL tham chiếu) → `.work/_tk_build_img_req_t02.py` (3 lô 10+10+6) → `mcode-tools connector call connector__matrix__generate_image` → `.work/_tk_download_imgs_t02.py` (node_id → file) → `.work/_tk_postprocess_t02.py` (8 nền AI) → `.work/_tk_fallback_crop_t02.py` (18 nền dự phòng).

### 14.2 Vì sao 18 nền là bản DỰ PHÒNG (không phải AI)

Connector trả `402` cho 18/26 request: *"the plan allowance cannot cover this image generation and credit auto-consumption is turned off on this account… at least 100 credits of balance are required"*. Lô 3 còn bị `429` *"request limit reached; retry in the next minute"* — nhưng thử lại thì vẫn `402` ⇒ **429 chỉ là che, nguyên nhân gốc là hết credit**.

⇒ Không dừng pipeline: `.work/_tk_fallback_crop_t02.py` **cắt 9:16 từ ảnh nền 16:9 gốc** (`assets/bg/_raw/t2_*`) — **0 credit**, đúng bảng màu của kênh. 18 nền này được đánh dấu riêng trong `provenance.json` (`prompt: null`, `cong_cu` ghi rõ "DU PHONG") để không nhầm là AI thật.

**Khi nào nạp credit → chạy lại:** `.work/_tk_download_imgs_t02.py` (tải node_id → `.work/tk_img_raw_t02/`) → `.work/_tk_postprocess_t02.py` (LANCZOS + grade noir + vignette/grain). Script hậu kỳ **ghi đè đúng tên file** nên chỉ cần copy bản AI mới vào `assets/bg/tk02_<tên>.png` là xong.

### 14.3 Sáu bẫy mới (T17–T22)

| # | Bẫy | Hậu quả | Cách tránh |
|---|---|---|---|
| **T17** | Ảnh gốc 16:9 trong `_raw/` **đã qua grade noir của kênh** (saturation 0,65 · contrast 1,15 · vignette 45 % · grain) — đo được: `t2_two_chairs.jpg` mean 50,3/sat 9,0 vs `.png` mean 47,7/sat 6,9 | Áp lại grade lần nữa ⇒ **tối quá, mất chi tiết bóng** | Bản dự phòng **chỉ** crop + LANCZOS + nền tối vùng chữ, **không** áp grade |
| **T18** | Nhiều ảnh gốc **kẹp letterbox đen** trên/dưới (đo: `t2_gavel.png` còn 182 px đen trên + 182 px đen dưới; `t2_checkpoint.png` 182/181) | Crop thẳng ⇒ mất 24 % chiều cao, chủ thể bị cắt | Dò vùng nội dung bằng `rowmax > 30` **trước khi** crop |
| **T19** | Crop 9:16 từ 16:9 giữ **vệt ngang** nếu profile làm tối dùng `min()` + `linspace` (nhảy giá trị đúng ranh giới 1/3 và 2/3) | **Vết sáng ngang** nổi lên khi chuyển động trên video | Dùng profile **smoothstep liên tục** qua 6 mốc (0,50 → 1,00 → 0,50). Đo lại: `max_row_jump` toàn 26 ảnh ≤ 42,6 (do nét vẽ trong ảnh, không phải do profile) |
| **T20** | `mcode-tools` là wrapper `.cmd` ⇒ `subprocess.run(["mcode-tools", ...])` **không** chạy được (WinError 2) | Script tải ảnh hỏng âm thầm | `shutil.which("mcode-tools")` + `shell=True`; và `Tee-Object` của PowerShell ghi receipt ra **UTF-16** ⇒ đọc JSON bằng `utf-16`/`utf-8-sig` (đã có `read_json_any`) |
| **T21** | Profile làm tối dải chữ viết bằng `1 − smoothstep` ở nửa lên ⇒ **nhảy giá trị 0→1 đúng tại biên** (đo được: dải ngang tại row 730 và row 996) | Vệt sáng ngang nổi lên đúng chỗ chữ, rất dễ thấy khi video chuyển động | Nửa lên dùng **smoothstep thuần** (0 tại cạnh ngoài → 1 tại biên trong); nửa xuống dùng `1 − smoothstep`. Sau khi sửa: `max_row_jump` toàn 26 ảnh ≤ 42,6, và **0 dải ngang xuyên suốt chiều ngang** |
| **T22** | Ảnh nền dọc phải **tối vùng chữ** trước khi dựng: 18 nền dự phòng có vùng hook sáng tới 118,8 (bộ `tk01_*` chỉ 41,6) | Chữ trắng trên nền sáng ⇒ mất chữ (H9) | `.work/_tk_fallback_crop_t02.py` tự tìm `depth` (0 → 0,60) để đưa mean vùng hook ≤ 58 và vùng phụ đề ≤ 72, biên mềm 70 px |

### 14.4 Chọn vùng crop (đo được)

`.work/_tk_fallback_crop_t02.py` không crop giữa khung mà chọn cửa sổ 9:16 có **năng lượng nét vẽ cao nhất** (gradient ngang + biến độ cục bộ), giới hạn lệch tối đa 22 % chiều rộng nội dung ⇒ giữ chủ thể. Sau đó ép cân bằng chiều dọc 9:16 rồi LANCZOS về 1080×1920.

**Script chạy lại được:** nếu ảnh đã tồn tại mà `provenance.json` **không có `prompt`** ⇒ coi là bản dự phòng và tạo lại (tự backup vào `.work/_cu/tk02_fallback_img_<giờ>/`); nếu **có `prompt`** ⇒ là bản AI thật, **giữ nguyên, không ghi đè**.

**Giới hạn đã biết:** ảnh crop vẫn là **tái dựng của ảnh 16:9** nên bố cục dọc kém bản AI thật (bản AI được vẽ lại để dựng theo chiều dọc). 18 nền này dùng được để **chạy thử pipeline và đo thời lượng thật**, nhưng **nên thay bằng bản AI trước khi đăng** (xem Tập 2.4 — ảnh dựng độc quyền của bản AI là điểm mạnh khi đăng TikTok).

---

## 15. MÔ TẢ + CAPTION TIKTOK TẬP 02 — 5/5 ĐẠT (20/11/2026)

### 15.1 File bàn giao (đo được)

| File | Ký tự | Dán vào đâu |
|---|---|---|
| `MoTa_Dai_TK1.txt` | **2.915** | ô **Description** của TikTok Studio |
| `MoTa_Dai_TK2.txt` | **2.923** | ô Description |
| `MoTa_Dai_TK3.txt` | **3.093** | ô Description |
| `MoTa_Dai_TK4.txt` | **3.158** | ô Description |
| `MoTa_Dai_TK5.txt` | **2.240** | ô Description |
| `Caption_TK1.txt` … `Caption_TK5.txt` | **422 / 430 / 440 / 425 / 422** (phần dán) | ô **caption** khi đăng |

Tất cả nằm trong `02_SAN_XUAT/TIKTOK/Tap02/`. Mỗi file caption = **phần dán** (trước dấu `---`) + **phần "Ghi chú khi đăng"** (KHÔNG dán).

### 15.2 Cấu trúc mô tả dài (5 khối, giữ nguyên cho mọi tập sau)

`hook` → `Tập N · tên tập — chỉ dấu #X` → `📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio` → `——————` → **khối CHỈ DẤU** (phân tích) → `——————` → **BỐI CẢNH HỒ SƠ** → `——————` → **NGUỒN THAM KHẢO** → `——————` → **LƯU Ý** (6 dòng: AI tạo hình/giọng · không phù hợp trẻ em · giáo dục, không thay thế tư vấn y tế/pháp lý · tư liệu công khai, không kết tội ai · Cú/Sói/Cáo là linh thú minh hoạ · hồ sơ có thật) → 7 hashtag.

### 15.3 QC độc lập — `.work/_qc_mota_tap02.py` — **0 lỗi / 10 tệp**

| Cổng | Kết quả |
|---|---|
| Từ cấm V9/A9.2 (máu · thi thể · sát hại · đòn · trói · bầm · đập · đầu độc · diệt cỏ · bỏ đói · móc áo) trong caption + mô tả dài | **0 lỗi** (10/10 tệp) |
| Giới hạn ký tự | caption 422–440 ≤ 2.200 · Description 2.240–3.158 ≤ 4.000 |
| Hashtag | **7** mỗi tệp (5–8), đủ `#AmberEyes` + `#HosoCoThat` |
| Nhãn AIGC trong caption | 5/5 có, **nằm trong phần dán** |
| Mô tả dài | 5/5 có `LƯU Ý` + `NGUỒN THAM KHẢO` + cảnh báo trẻ em + "không phải phóng sự" |
| Số liệu truy về nguồn | **15/15 mục** có trong `kichban_tap02_22102026.md` / `nguon_tham_khao.md` (82 · 88 · 25 năm · 46 tuổi · 37 tuổi · Marie-France Comeau · Jessica Lloyd · Nissan Pathfinder · Hubert Genest · Robert Scott · Jim Smyth · Trenton · Tweed · Belleville · 2010 ONSC 5946) |

Thời lượng tập YouTube đo được: `timeline_s_t02.json` → **1.519,08 s = 25,3 phút** ⇒ dòng "Xem tập đầy đủ (25 phút)" trong mô tả dài là **đúng số đo thật**.

### 15.4 Một lỗi thật đã sửa: nhãn AIGC nằm ngoài phần dán (T23)

**Bẫy:** generator ghi dòng *"Nội dung do AI tạo hình và giọng…"* vào **phần "Ghi chú khi đăng"** (KHÔNG dán) ⇒ người đăng phải **tự gõ thêm** khi dán. Bất kỳ lần đăng nào quên ⇒ **vi phạm luật T3** (TikTok bắt buộc ghi nhãn AIGC trong caption) ⇒ video bị gỡ hoặc hạn chế.

**Đã sửa ở nguồn:** `.work/_build_tk_tap02.py` — `DONG_AIGC` nay nằm **trong thân caption** (ngay trước dòng hashtag), và thêm mục QC **7b** kiểm nhãn AIGC nằm đúng trong phần dán (`cap.split("\n---")[0]`). Sau khi sửa: **5/5 đạt**, caption dài thêm ~85 ký tự (vẫn ≤ 2.200).

⇒ Nguyên tắc: **thứ bắt buộc phải nằm trong phần dán**, không được đẩy sang phần ghi chú. Phần ghi chú chỉ chứa việc *thao tác* khi đăng (bật toggle, dán link, tên file).

### 15.5 Ba bẫy QC mới (T24–T26)

| # | Bẫy | Hậu quả | Cách tránh |
|---|---|---|---|
| **T24** | QC đếm hashtag bằng `#\w+` ⇒ **mã chỉ dấu `#8`, `#9`, `#10` bị tính là hashtag** | Báo động giả "9 hashtag, vượt giới hạn" → mất thời gian điều tra | Lọc `re.fullmatch(r"#\d+", t)` trước khi đếm |
| **T25** | QC kiểm tra caption **cả file** (gồm phần ghi chú) thay vì **phần dán** | Báo động giả "thiếu cảnh báo trẻ em" — dòng đó cố ý nằm ở mô tả dài (ô Description), không phải caption | Tách `cap.split("\n---")[0]` rồi kiểm riêng caption và mô tả dài |
| **T26** | Caption ghi "Độ dài caption: NNN ký tự" **tính cả phần ghi chú** | Báo nhầm độ dài (1.126 thay vì 399) ⇒ tưởng gần trần 2.200 | `len(cap)` phải đo **phần dán**; con số trong file phải khớp độ dài thật khi dán |

### 15.6 Việc còn lại

| # | Việc | Người |
|---|---|---|
| 1 | **Điền link YouTube Tập 02** — đang là placeholder `[LINK_TẬP 02 — cần điền]` trong cả 5 file caption; **không tự bịa** (L2) | Người dùng |
| 2 | Thay dòng "Xem tập đầy đủ ở link trong bio" trong caption bằng URL thật **nếu** TikTok cho phép (URL gõ tay trong caption không click được — dán vào ô Links/Website của profile mới click được) | Người dùng |
| 3 | Bật toggle **"AI-generated content"** khi đăng (dòng nhãn AIGC **đã có sẵn** trong caption) | Người dùng |
| 4 | Xác minh quyền thương mại BGM MiniMax (mục 2.4) — chưa làm, ảnh hưởng cả 5 clip | Người dùng + AI |

---

## 16. MÔ TẢ NGẮN TIKTOK TẬP 02 — 5/5 ĐẠT (20/11/2026)

### 16.1 Vì sao cần bản mô tả ngắn

TikTok Studio có **2 ô**: *caption* (khi đăng) và *Description* (ô mô tả). Tập 01 đã có **một** bản mô tả dài duy nhất (2.930–3.935 ký tự). Người đăng cần một bản **rút gọn** để dán nhanh khi có nhiều clip, và để kiểm tra chất lượng chữ trước khi đọc giọng.

**Chuẩn tham chiếu:** `02_SAN_XUAT/TIKTOK/Tap01/MoTa_Dai_TK1.txt` — 1.078 ký tự, 10 dòng. Bài học: **file tên "MoTa_Dai" nhưng nội dung ngắn** — dùng nó làm mẫu chuẩn, đừng dùng làm mẫu bản dài.

### 16.2 File bàn giao (đo được)

| File | Ký tự (QC) | Đối chiếu chuẩn Tập 01 (1.078–1.369) |
|---|---|---|
| `MoTa_Ngan_TK1.txt` | **1.424** | dài hơn chuẩn (đủ 4 nấc thang + NẤC 4) |
| `MoTa_Ngan_TK2.txt` | **1.525** | dài hơn chuẩn một chút (nhiều mốc thời gian) |
| `MoTa_Ngan_TK3.txt` | **1.578** | dài hơn chuẩn một chút |
| `MoTa_Ngan_TK4.txt` | **1.544** | dài hơn chuẩn một chút |
| `MoTa_Ngan_TK5.txt` | **1.360** | ✔ trong khoảng |

Tất cả nằm trong `02_SAN_XUAT/TIKTOK/Tap02/`, **sinh từ generator** `.work/_build_tk_tap02.py` (dict `MO_TA_NGAN`) — không sửa tay file kết quả (G6: 1 generator = 1 nguồn sự thật).

### 16.3 Cấu trúc bản ngắn (rút từ chuẩn Tập 01)

```
dòng 1  hook (chữ trên hình)  👁️
dòng 2  Tập 02 · Đại tá hai mặt — Chỉ dấu #X: …
         (đoạn dẫn)
         • NẤC 1 — …
         • NẤC 2 — …
         • NẤC 3 — …
         Bước ngoặt của hồ sơ này: …
         Theo bạn, …? 👇
📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: …
🔎 Hồ sơ có thật, … · nội dung do AI tạo hình và giọng … · không phù hợp cho trẻ em.
5 hashtag CamelCase
```

**Cố ý KHÔNG có** (đặc trưng bản dài, không có ở chuẩn Tập 01): dấu kẻ `——————`, khối `LƯU Ý`, khối `NGUỒN THAM KHẢO`.

### 16.4 Bốn quy tắc rút ra (T27–T30)

| # | Quy tắc | Lý do |
|---|---|---|
| **T27** | **Dòng 1 của mô tả phải là hook** — hoặc `clip["hook"]` (chữ trên hình), hoặc lời đọc câu 1 | TikTok chỉ hiện **~100 ký tự** đầu trước khi bấm "more" ⇒ hook nằm ngoài dòng 1 = mất hook |
| **T28** | **Dòng 1 bản ngắn phải KHỚP bản dài** | Người đăng có thể chọn 1 trong 2 bản; nếu 2 bản mở đầu khác nhau thì họ dán nhầm ⇒ 2 video khác nhau cùng 1 clip |
| **T29** | Bản ngắn giữ **5 hashtag CamelCase** (`#AmberEyes #TamLyToiPham #HosoCoThat #… #TrueCrime`) | Đồng bộ caption + bản dài Tập 02 (Tập 01 dùng chữ thường — **đừng trộn 2 hệ** trong cùng tập) |
| **T30** | Bản ngắn **có** nhãn AIGC + cảnh báo trẻ em **trong dòng 🔎** | Nâng cao hơn Tập 01, an toàn TikTok; hợp lệ vì nằm ở Description, không phải caption |
| **T31** | **QC so chuỗi tiếng Việt phải không phân biệt hoa thường** (`m.lower()`) | Check `"không phù hợp cho trẻ em" not in m` **báo động giả** vì bản ngắn viết *"**K**hông phù hợp cho trẻ em"* ở đầu câu (chữ K hoa) ⇒ tưởng thiếu cảnh báo khi thực ra có. Sửa tại nguồn `.work/_build_tk_tap02.py` (mục 15) |

### 16.5 QC độc lập — `.work/_qc_mota_tap02.py` — **0 lỗi / 15 tệp**

| Cổng | Kết quả |
|---|---|
| Từ cấm V9/A9.2 trong caption + bản dài + bản ngắn | **0 lỗi** (15/15 tệp) |
| Giới hạn ký tự | caption 422–440 ≤ 2.200 · bản dài 2.240–3.158 ≤ 4.000 · **bản ngắn 1.360–1.578 ≤ 4.000** |
| Cảnh báo trẻ em | bản dài 5/5 · **bản ngắn 5/5** (caption **không** bắt buộc — theo chuẩn Tập 01) |
| Nhãn AIGC | caption 5/5 (trong phần dán) · bản dài 5/5 · bản ngắn 5/5 |
| Dòng 1 bản ngắn khớp bản dài | 5/5 ✔ |
| Số liệu truy về nguồn | **15/15 mục** ✔ (không mục nào mới sinh ở bản ngắn) |

QC đã tách **3 mode** (`dai` / `ngan` / `caption`) vì 3 loại tệp có bộ quy tắc khác nhau — kiểm tra chung một ngưỡng sẽ ra báo động giả.

### 16.6 Việc còn lại (mô tả ngắn)

| # | Việc | Người |
|---|---|---|
| 1 | Chọn 1 trong 2 bản khi đăng: **bản ngắn** (dán nhanh, có cảnh báo trẻ em) **hoặc** bản dài (đầy đủ nguồn tham khảo) — **không dán cả hai** (trùng nội dung) | Người dùng |
| 2 | **Điền link YouTube Tập 02** — placeholder `[LINK_TẬP 02 — cần điền]` trong cả 5 caption; bản ngắn dùng câu "bấm nút liên kết ngay đầu trang cá nhân" nên **không** cần sửa nếu dán link vào ô Links/Website của profile | Người dùng |
| 3 | Duyệt văn bản lời dẫn trước khi đọc giọng (L4) | Người dùng |

---

## 17. RÀ CHÍNH TẢ & NGÔN NGỮ BỘ TEXT TẬP 02 (20/11/2026)

**Phạm vi:** 15 file bàn giao (5 caption + 5 mô tả dài + 5 mô tả ngắn) + đối chiếu chuẩn văn phong `Tap01/` (caption, `MoTa_Dai_TK1.txt` = mẫu bản ngắn).
**Cách sửa:** mọi thay đổi nằm trong **generator** `.work/_build_tk_tap02.py` (G6), chạy bằng 2 script patch có **assert số lần khớp** (26 + 3 + 1 mục) ⇒ không có thay thế "mù" và luôn có backup trong `.work/_cu/`. Lời đọc (voice) và các chuỗi QC nội bộ **không** bị đụng tới.

### 17.1 Lỗi chính tả / kỹ thuật trình bày (đã sửa)

| # | Lỗi | Sửa |
|---|---|---|
| 1 | `( Gavin de Becker)` — thừa khoảng trắng trong ngoặc | `(Gavin de Becker)` |
| 2 | `Nguyên lý "The Gift of Fear"` — gọi một **cuốn sách** là "nguyên lý" | `Sách "The Gift of Fear"` |
| 3 | `toà` (dấu huyền) lẫn với `tòa` (dấu sắc) **trong cùng một file** | thống nhất `tòa` (10 chỗ: 4 "trước toà" + 5 "hồ sơ toà án" + 1 nguồn) |
| 4 | Dấu nháy cong `“ ”` trong 8 cụm của bản dài | đổi sang nháy thẳng `" "` — đúng văn phong Tập 01 |
| 5 | `— chỉ dấu #X` ở bản dài vs `— Chỉ dấu #X` ở bản ngắn | thống nhất `Chỉ dấu` (khớp `Tap01/MoTa_Dai_TK1.txt`) |
| 6 | `thay vì chiếc BMW ông ta vẫn thường đi` — thiếu mạo từ | `… chiếc BMW **mà** ông ta vẫn thường đi` (nguyên văn kịch bản:54) |

### 17.2 Lỗi nhất quán nội bộ (đã sửa)

| # | Lỗi | Sửa |
|---|---|---|
| 7 | `dữ kiện có nguồn` (12 chỗ) lẫn `dữ liệu có nguồn` (6 chỗ) — **ngay trong cùng một file** (dòng 4 vs mục LƯU Ý) | thống nhất **`dữ liệu có nguồn`** — đúng chuẩn dự án (Tap01 caption + `MoTa_Dai_TK1.txt` + slogan) |
| 8 | Caption ghi `Xem tập đầy đủ ở link trong bio` — thiếu thời lượng và nền tảng | `Xem tập đầy đủ (25 phút) trên YouTube — link trong bio` (khớp bản dài + Tap01) |
| 9 | TK4: bản dài gọi tòa là *"Tòa án Cấp cao Ontario"*, mục nguồn gọi là *"Tòa Thượng thẩm Belleville"* — 2 tên cho 1 cơ quan | thống nhất **`Tòa Thượng thẩm Ontario`** (khớp trích dẫn `2010 ONSC 5946`), nguồn ghi rõ *"phiên xử tại Belleville"* |
| 10 | TK4: *"nỗi đau đớn"* (ngắn) vs *"nỗi đau đớn cùng cực"* (dài); *"sự tự thương hại bản thân thảm hại"* vs *"sự thương hại bản thân tột độ"* | thống nhất 2 cụm theo bản dài (nguyên văn kịch bản:217) |
| 11 | TK4: bản ngắn ghi *"quân hàm bị thu hồi"*, bản dài ghi *"toàn quyền Canada thu hồi quân hàm"* | thống nhất **"quân hàm bị toàn quyền Canada thu hồi"** |
| 12 | TK1: hook + TK3 nói **"82 vụ trộm"**, nhưng bản dài/ngắn nói *"82 vụ đột nhập và đột nhập bất thành"* | thống nhất **"82 vụ trộm đồ riêng tư"** (theo `nguon_tham_khao.md`: 82 vụ đột nhập trộm đồ lót 2007–2009) |
| 13 | TK1 bản ngắn lặp từ: *"rình rập ban đêm, đứng ngoài bóng tối để **rình rập** phụ nữ…"* | `NẤC 1 — nhìn trộm ban đêm: đứng ngoài bóng tối để rình rập phụ nữ qua khung cửa sổ` |

### 17.3 Lỗi NỘI DUNG (đã sửa — quan trọng nhất)

| # | Lỗi | Sửa |
|---|---|---|
| 14 | **Bản ngắn TK1 nói "bốn nấc thang" nhưng chỉ liệt kê 3 bullet** (NẤC 1–3) — người đọc đếm sẽ thấy thiếu | **Bổ sung NẤC 4** (đoạt mạng nạn nhân — Marie-France Comeau, 37 tuổi; hai tháng sau là Jessica Lloyd) ⇒ khớp hook "Bốn nấc thang" và bản dài |

### 17.4 Thuật ngữ khó hiểu

| # | Thuật ngữ | Xử lý |
|---|---|---|
| 15 | `cơ chế **dung nạp** kích thích` — không phải cách gọi tiếng Việt của *stimulus satiation* | đã đổi thành **`cơ chế bão hoà kích thích`** (chỉ có trong bản dài, **không** có trong lời đọc ⇒ không lệch voice) |
| 16 | `trạng thái **đói ảo tưởng**` — nguyên văn kịch bản tập (dòng 133) và **cũng nằm trong lời đọc clip TK1** | **ĐÃ CHỐT (20/11/2026, người dùng): GIỮ NGUYÊN** — khớp tuyệt đối kịch bản tập + lời đọc + video YouTube Tập 02 đã dựng. Không sửa ở bất kỳ tầng nào (kịch bản · voice · mô tả) |

### 17.5 Ba bẫy QC mới (T32–T34)

| # | Bẫy | Cách tránh |
|---|---|---|
| **T32** | **Thay dấu nháy cong bằng `replace()` toàn cục sẽ làm vỡ cú pháp Python** — chuỗi `"“MỘT MÓN KỶ NIỆM”"` (chữ overlay SFX) nằm trong `"..."` ⇒ thay thành `"MỘT MÓN KỶ NIỆM"` làm hỏng file | Thay **từng cụm có mô tả rõ** (8 cụm trong mô tả dài), **không** thay toàn cục; luôn `py -3 -m py_compile` sau khi vá |
| **T33** | **Số ký tự QC ≠ số ký tự người dùng dán** — QC đếm cả ký tự xuống dòng (`\n`), nên luôn **cao hơn** số thực tế (TK1 ngắn: QC 1.424, thực 1.408) | Không sao: vẫn < trần 4.000 (Description) / 2.200 (caption). Nhưng **phải ghi rõ quy ước** trong báo cáo, nếu không sẽ tưởng bị vượt trần |
| **T34** | **Mô tả ngắn phải khớp SỐ MỤC liệt kê với câu dẫn** — "bốn nấc thang" + 3 bullet là lỗi *đếm* mà QC ký tự/hashtag **không bắt được** | Thêm QC: đếm số bullet `•` và so với số từ định lượng trong câu dẫn ("bốn nấc" ⇒ 4 bullet) |

### 17.6 Kết quả sau khi rà

| Cổng | Kết quả |
|---|---|
| Self-QC generator | **16/16 ĐẠT** |
| QC độc lập `.work/_qc_mota_tap02.py` | **0 lỗi / 15 tệp** |
| 15/15 mục số liệu truy được về nguồn | ✔ (không mục nào mới sinh) |
| Từ cấm V9/A9.2 | 0 lỗi |
| Từ cấm **tự thêm** (toà, dữ kiện, “”, Nguyên lý) | **0** sau khi vá |
| Backup | `_build_tk_tap02_20261120_1435/1437/1438.py`, `provenance_20261120_1439.json` |

---

## 18. GÓI SẢN XUẤT CLIP TIKTOK TẬP 03 (20/11/2026)

*Vụ án Edmund Kemper · "Gã khổng lồ IQ 145 & Chiếc gương giải phẫu tâm trí"*
*Kế hoạch chi tiết: `02_SAN_XUAT/TIKTOK/Tap03/KE_HOACH_CLIP_TAP03.md` (VN) · `Tap03_EN/KE_HOACH_CLIP_TAP03_EN.md` (EN) · `Tap03_JA/KE_HOACH_CLIP_TAP03_JA.md` (JA)*

### 18.1 Tổng quan bộ 3 ngôn ngữ (VN · EN · JA)

| Bản | Thư mục | Số clip | Tổng câu | Thời lượng | File đặc tả TTS | Trạng thái |
|---|---|---|---|---|---|---|
| **Tiếng Việt (VN)** | `02_SAN_XUAT/TIKTOK/Tap03/` | 5 | 53 | 64.8 – 75.1 s | `SPEC_AUDIO_CLIP_TAP03.json` | ✅ Kịch bản đã rà soát chính tả, sẵn sàng đọc giọng |
| **Tiếng Anh (EN)** | `02_SAN_XUAT/TIKTOK/Tap03_EN/` | 5 | 53 | 63.5 – 79.5 s | `SPEC_AUDIO_CLIP_TAP03.json` | ✅ Đồng bộ 100%, sẵn sàng đọc giọng Higgs EN |
| **Tiếng Nhật (JA)** | `02_SAN_XUAT/TIKTOK/Tap03_JA/` | 5 | 53 | 71.9 – 85.4 s | `SPEC_AUDIO_CLIP_TAP03.json` | ✅ Đồng bộ 100%, sẵn sàng đọc giọng Higgs JA |

### 18.2 Bảng 5 clip và chỉ dấu tâm lý Tập 03

| Clip | Chỉ dấu tâm lý (K10) | Chủ đề | Hook tiếng Việt | Hook tiếng Anh (EN) | Hook tiếng Nhật (JA) |
|---|---|---|---|---|---|
| **TK1** | #4 · #6 | Sự sụp đổ ảo tưởng & Điểm gãy tâm lý | *"Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa."* | *"Stop me. I’m going to do it again."* | *「私を止めてください。私はそれをもう一度するつもりです。」* |
| **TK2** | #9 · #1 | Hiệu ứng hào quang & Điểm mù xã hội | *"Uống bia cùng cảnh sát. Và bàn về chính vụ án của mình."* | *"Drinking with the police. And discussing his own murders."* | *「警察官とビールを飲み、自らの事件について語る。」* |
| **TK3** | #2 · #3 | Chấn thương mẫu hệ & Nạn nhân thay thế | *"Tám tuổi. Bị nhốt dưới tầng hầm có cửa sập dưới bàn ăn."* | *"Eight years old. Locked in a basement with a trapdoor under the table."* | *「8歳。食卓の下にある落とし戸の地下室に閉じ込められた。」* |
| **TK4** | #7 · #8 | Vòng lặp ảo tưởng & FBI Mindhunter | *"IQ một trăm bốn mươi lăm. Bộ não thay đổi vĩnh viễn FBI."* | *"An IQ of 145. The mind that changed the FBI forever."* | *「IQ 145。FBIの捜査手法を永遠に変えた頭脳。」* |
| **TK5** | #10 | Nạn nhân học & 4 cảnh báo đỏ sinh tồn | *"Bốn chỉ dấu cảnh báo sớm. Để không ai phải trở thành nạn nhân."* | *"Four early warning signs. So that no one becomes a victim."* | *「4つの初期警告サイン。犠牲者を二度と出さないために。」* |

### 18.3 Các tài nguyên đã cập nhật
- Generator Python: `.work/_build_tk_tap03.py` (bản VN) và `.work/_build_tk_tap03_multilang.py` (bản EN + JA).
- Sổ theo dõi tập trung: `02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv` đã nạp đủ 21 dòng (Tập 02 VN: 5 clip, Tập 03 VN/EN/JA: 15 clip).

## 19. GÓI SẢN XUẤT CLIP TIKTOK TẬP 02 ĐA NGÔN NGỮ (EN · JA) (20/11/2026)

*Vụ án Đại tá Russell Williams · "Đại tá hai mặt và Vực thẳm leo thang hành vi"*
*Kế hoạch chi tiết: `02_SAN_XUAT/TIKTOK/Tap02/KE_HOACH_CLIP_TAP02.md` (VN) · `Tap02_EN/KE_HOACH_CLIP_TAP02_EN.md` (EN) · `Tap02_JA/KE_HOACH_CLIP_TAP02_JA.md` (JA)*

### 19.1 Tổng quan bộ 3 ngôn ngữ (VN · EN · JA)

| Bản | Thư mục | Số clip | Tổng câu | Thời lượng ước lượng | File đặc tả TTS | Trạng thái |
|---|---|---|---|---|---|---|
| **Tiếng Việt (VN)** | `02_SAN_XUAT/TIKTOK/Tap02/` | 5 | 53 | 56.1 – 82.6 s | `SPEC_AUDIO_CLIP_TAP02.json` | ✅ Kịch bản và mô tả đã rà soát chính tả, sẵn sàng đọc giọng |
| **Tiếng Anh (EN)** | `02_SAN_XUAT/TIKTOK/Tap02_EN/` | 5 | 53 | 56.1 – 81.9 s | `SPEC_AUDIO_CLIP_TAP02.json` | ✅ Đồng bộ 100%, chuẩn tốc độ đo timeline_s_EN_t02 |
| **Tiếng Nhật (JA)** | `02_SAN_XUAT/TIKTOK/Tap02_JA/` | 5 | 53 | 64.3 – 81.2 s | `SPEC_AUDIO_CLIP_TAP02.json` | ✅ Đồng bộ 100%, chuẩn tốc độ đo timeline_s_JA_t02 |

### 19.2 Bảng 5 clip và chỉ dấu tâm lý Tập 02 (3 ngôn ngữ)

| Clip | Chỉ dấu tâm lý (K10) | Chủ đề | Hook tiếng Việt | Hook tiếng Anh (EN) | Hook tiếng Nhật (JA) |
|---|---|---|---|---|---|
| **TK1** | #8 · #6 | Quỹ đạo leo thang | *"Bốn nấc thang. Tám mươi hai vụ trộm. Rồi một vụ án mạng."* | *"Four escalation steps. Eighty-two burglaries. Then murder."* | *「4つの階段。82件の侵入。そして殺人へと至る軌跡。」* |
| **TK2** | #9 · #1 | Hiệu ứng hào quang | *"Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào."* | *"Matching tire treads. Yet the police saluted him on his way."* | *「タイヤ痕の一致。それでも警察はその男に敬礼して見送った。」* |
| **TK3** | #5 · #3 | Phân mảnh tâm trí | *"Hai cuộc đời. Một cơ thể. Một câu chuyện để tự bào chữa."* | *"Two lives. One body. A story to self-justify."* | *「2つの人生。1つの身体。自己正当化のための物語。」* |
| **TK4** | #4 · #1 | Sụp đổ cái tôi ái kỷ | *"Không một lời xin lỗi nào nhắc tới nạn nhân."* | *"Not a single apology mentioned the victims."* | *「被害者に向けられた謝罪はただの一言もなかった。」* |
| **TK5** | #10 | Nạn nhân học và Trực giác | *"Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó."* | *"If you feel unease, never rationalize it away."* | *「曖昧な違和感を覚えたなら、決して見過ごしてはならない。」* |

### 19.3 Công cụ và tài nguyên đã tạo
- Bộ sinh tự động: `.work/_build_tk_tap02_multilang.py` (sinh 100% tài nguyên EN và JA từ dữ liệu gốc, không sửa tay).
- Sổ theo dõi tập trung: `02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv` đã cập nhật 10 dòng clip EN và JA cho Tập 02.
