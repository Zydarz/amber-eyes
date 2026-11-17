# PHƯƠNG ÁN — VIDEO AI GIỚI THIỆU KÊNH AMBER EYES

*Ngày: 16/11/2026 · Trạng thái: đề xuất, chờ người dùng chốt hướng*
*Phạm vi: **video quảng bá kênh** (trailer) — KHÔNG thay thế bumper 22,41 s đầu mỗi tập.*

---

## 0. Bối cảnh — kênh đã có gì, còn thiếu gì

| Đã có sẵn (tái sử dụng được, 0 đồng) | Thiếu |
|---|---|
| `assets/brand/` — logo, logo_mark, logo_lockup, wordmark, avatar, watermark, preview (PNG) | Một **video giới thiệu kênh** dùng được để quảng bá ngoài YouTube (trailer, Shorts, social) |
| `assets/brand/intro_kenh.mov` (22,41 s) + bản EN + bản JA — bumper **đầu mỗi tập**, dựng procedural bằng Pillow, không có lời dẫn | Bumper này **không giới thiệu kênh**, chỉ là logo + 2 thẻ miễn trừ + 5 vòng vai |
| 5 linh thú PNG trong `assets/cast/` (H=Cú/Owl host, D=Sói/Wolf điều tra viên, C=Cáo/Fox chuyên gia tâm lý, N1=Cừu/Sheep, N2=Mèo/Cat) | Chưa có video nào cho thấy **5 vai** hoạt động như một ekip |
| 11 nền nhạc `assets/bgm/` (music box, cello, sub drone, piano…) | Chưa có mốc âm thanh "chữ ký" cho trailer |
| 29 tập kịch bản VN/EN/JA/KO + hồ sơ tập + ảnh nền từng tập | Chưa có "chất" của kênh gói lại thành 1 video ngắn |
| Bộ giọng Higgs Audio v3 (bộ A) — đã đo CER, đã qua G8–G13 | Trailer cần lời dẫn (VO) — chưa có file VO nào cho kênh |

**Kết luận chiến lược:** trailer mới phải **tái sử dụng 5 linh thú + logo + nền có sẵn**, chỉ sinh thêm *vài* mảnh AI (video H3 + ảnh MiniMax). Không được dựng lại từ số 0.

---

## 1. Bốn phương án (4 concept)

### CONCEPT A — "SỢI CHỈ ĐỎ" · trailer chính 50–55 s

*Nguyên lý: sợi chỉ đỏ là motif đã có trong logo (`make_logo.py` vẽ thread xuyên logo) → dùng nó làm "đường may" dẫn mắt người xem qua từng cảnh.*

| Mốc | Hình | Lời (Host, giọng trầm ấm) |
|---|---|---|
| 0,0–4,5 s | Nền đen. Sợi chỉ đỏ vẽ từ trái qua (H3 clip: ngòi nổi sáng dần). Mắt hổ phách mở giữa khung. | *(im lặng, chỉ sub-bass)* |
| 4,5–9,5 s | Thread kéo ra → biến thành bảng ghim/bảng hồ sơ (MiniMax ảnh): 6–8 ghim giấy, **không mặt người thật** (chỉ bóng, vật thể). | "Mỗi vụ án bắt đầu bằng một câu hỏi đơn giản." |
| 9,5–15 s | Cú (Host) trong góc trái dưới dạng bust cutout; nền bảng hồ sơ chuyển động chậm. | "Và câu trả lời không nằm ở khám nghiệm hiện trường." |
| 15–21 s | Sói (D) chiếm góc phải, bảng tin tưởng chừng như tấm bia, đèn chuyển từ ấm sang lạnh. | "Nó nằm trong cách kẻ gây án nhìn nạn nhân." |
| 21–27 s | Cáo (C) ở góc dưới; các "chỉ dấu tâm lý" hiện nhanh dạng nhãn giấy. | "…và trong cách hắn biện minh cho chính mình." |
| 27–33 s | Cả 3 vai cùng xuất hiện, khung rộng, ánh mắt hổ phách. | "Hồ sơ có thật. Phân tích có căn cứ." |
| 33–42 s | Chữ do Pillow vẽ: dòng tên các tập nổi lên như thẻ hồ sơ. | "Amber Eyes. Mỗi tập là một hồ sơ." |
| 42–50 s | Logo + wordmark "AMBER EYES" + tagline + số liệu: *29 hồ sơ · 3 vai · 4 ngôn ngữ*. Fade out. | "Phân tích tâm lý tội phạm qua những hồ sơ có thật." |

- **AI dùng cho:** 1 clip H3 (thread/eyes, 6–8 s) · 3–4 ảnh MiniMax (bảng hồ sơ, phòng thẩm vấn) · TTS giọng Host · SFX + music box.
- **Rủi ro:** dễ thành "video quảng cáo rỗng" nếu VO dài. ⇒ **giữ VO ≤ 6 câu, mỗi câu ≤ 7 s**.
- **Chi phí:** cao nhất trong 4 concept (H3 + ảnh mới) — cần người dùng duyệt credit (L4).

---

### CONCEPT B — "MỘT HỒ SƠ, BA CÁCH NHÌN" · trailer 35–40 s

*Nguyên lý: đúng cái kênh đang làm — 3 vai đọc cùng một hồ sơ. Concept này **trung thành với nội dung hiện có** nhất.*

| Mốc | Hình | Lời |
|---|---|---|
| 0–4 s | Thẻ hồ sơ giấy (Pillow) đóng sập xuống, ghi nhãn đỏ (chữ vẽ bằng Pillow, không nhờ AI). | Host: "Cùng một hồ sơ. Ba cách nhìn." |
| 4–12 s | Góc điều tra: nền t02/t05 (có sẵn) + Sói bust cutout, màu lạnh. | Sói: "Sự kiện xảy ra lúc 22 giờ. Chi tiết này không ai bỏ sót." |
| 12–21 s | Góc chuyên gia: nền có sẵn + Cáo bust cutout, màu ấm/violet. | Cáo: "Nhưng cái đáng nói không phải lúc 22 giờ. Mà là điều hắn tin về bản thân." |
| 21–30 s | Góc host: Cú bust cutout giữa khung, nền tối dần. | Host: "Vì thế, tập này ta đọc hồ sơ khác — từ trong tâm lý ra." |
| 30–36 s | Logo + tagline + dòng "Tập 01–29 · Có thật · Có nguồn". | Host: "Amber Eyes." |

- **AI dùng cho:** **gần như không sinh ảnh mới** — chỉ TTS 3 vai + dựng Pillow/ffmpeg. Dùng lại nền tập có sẵn.
- **Ưu điểm lớn nhất:** rẻ nhất, nhanh nhất, tái dùng được cho **nhiều tập** (mỗi tập một bản trailer riêng → công cụ marketing mạnh).
- **Rủi ro:** Cảnh báo giọng — vai Sói (điều tra viên) của bộ A có **CER 3,1 %** (điểm yếu đã ghi nhận). Nếu đặt lời dài cho Sói → phải dùng giọng thay thế trong `90_LUU_TRU/BaoCao_SangLocGiongDieuTraVien_20261027.md`, hoặc rút lời Sói còn ≤ 8 s.

---

### CONCEPT C — "MỐI CHỈ DẤU" · 30–35 s + template tái dùng

*Nguyên lý: 10 chỉ dấu tâm lý là "hàng hoá" độc quyền của kênh (K10). Biến nó thành hiệu ứng thị giác chữ dập (stamp) trên thẻ hồ sơ.*

| Mốc | Hình | Lời |
|---|---|---|
| 0–3 s | Nền giấy hồ sơ, con dấu đỏ đóng xuống lần 1. | Host: "Đây là mười dấu hiệu." |
| 3–24 s | 10 con dấu đóng nhanh, mỗi cái 1,6–2 s, kèm 1 dòng định nghĩa (chữ Pillow). Mỗi con dấu đi kèm 1 khung hình nền rút từ các tập đã dựng (đã có sẵn trên đĩa). | Host (nhanh, dứt khoát): mười câu, mỗi câu ≤ 6 từ. |
| 24–30 s | Con dấu cuối = logo; 5 vòng vai sáng lên (tái dùng đúng hiệu ứng trong `make_intro.py`). | Host: "Mười dấu hiệu. Một hồ sơ. Amber Eyes." |

- **AI dùng cho:** gần như **0 ảnh mới** — chỉ dùng ảnh nền tập đã có + Pillow dập chữ. TTS Host.
- **Khả năng mở rộng mạnh nhất:** làm được **một bản 10 s cho mỗi tập** làm cold-open → biến mỗi tập thành 2 video (trailer tập + full tập).
- **Rủi ro:** thuần đồ hoạ, cảm xúc thấp hơn Concept A → dùng cho **kênh/series**, không dùng làm video quảng bá chính.

---

### CONCEPT D — "15 GIÂY, DỌC" · short 9:16, 15–20 s

*Nguyên lý: bản dọc cho Shorts/TikTok/Reels — khung 9:16 1080×1920, 3 nhịp cắt.*

| Nhịp | Nội dung |
|---|---|
| 0–3 s | Hook: mặt bóng trên nền đỏ, chữ trên màn hình: *"Hắn không giấu tội. Hắn kể một câu chuyện khác."* (chữ Pillow) |
| 3–11 s | 3 cảnh nhanh (mắt hổ phách · ghim hồ sơ · 5 vai), VO 2 câu |
| 11–16 s | Logo + tagline + "Tập mới mỗi tuần" |

- **AI dùng cho:** 1 clip H3 ngắn + ảnh có sẵn + TTS.
- **Lưu ý:** dựng **riêng** khung 9:16 — không cắt từ bản 16:9 (sẽ mất 2/3 khung, vi phạm tinh thần "mọi khung đều có chủ đích").

---

## 2. So sánh nhanh

| | A · Sợi chỉ đỏ | B · 3 cách nhìn | C · 10 dấu hiệu | D · Dọc 15 s |
|---|---|---|---|---|
| Thời lượng | 50–55 s | 35–40 s | 30–35 s | 15–20 s |
| Ảnh AI mới | 3–4 + 1 clip H3 | 0 | 0 | 1 clip H3 |
| TTS | 1 vai | 3 vai | 1 vai | 1 vai |
| Tái dùng tài sản có sẵn | 50 % | **90 %** | 95 % | 70 % |
| Rủi ro credit | Cao | **Thấp** | Rất thấp | Trung bình |
| Cảm xúc | Cao | Vừa | Thấp | Cao |
| Dùng để | Trailer chính | Trailer + promo từng tập | Series + cold-open | Social |

**Đề xuất lộ trình:** **B trước** (rẻ, nhanh, dùng được ngay) → **A làm trailer chính** → **C làm template tái dùng** → **D làm bản dọc**. B và C dùng chung một bộ VO Host nên chỉ tốn TTS một lần.

---

## 3. Lộ trình sản xuất (bám đúng quy trình của dự án)

| Bước | Việc | Cổng / Đạt khi | Ghi chú |
|---|---|---|---|
| 1 | Chốt concept + lời dẫn (VN) | Người dùng duyệt **văn bản lời** trước khi đọc | L4: hỏi trước việc tốn credit |
| 2 | `make_trailer_script.py` → tách câu, vai, `acting_trailer.json` | Giống `parse_kichban.py` + `make_acting_tapXX.py` | Tái dùng nguyên xi |
| 3 | TTS bằng Higgs Audio v3 (bộ A) | **G1–G4**: không `...`, không `<#s#>`, 1 nghỉ `<#0.35#>` sau dấu `:`, 4 cảm xúc an toàn, pitch = 0 | Đo **CER** từng vai (G12) |
| 4 | `voice_role_check.py` (mở rộng cho trailer) | G9/G10: nghe mù ra đúng 1 người, 3 vai tách bạch | Bắt buộc — không có video thì tai khách cũng không chấp nhận |
| 5 | Sinh ảnh AI (MiniMax) + clip H3 | Ảnh có **nội dung cảnh** (H19), không lộ mặt thật, không chữ rác | Ghi `provenance.json` (L7) |
| 6 | Dựng hình `build_video3`-style cho trailer | 1920×1080@30 · **H9**: đo tương phản chữ trên nền mới → 0 chữ chìm | Nền MiniMax sáng hơn nền procedural ⇒ **phải đo lại toàn bộ** |
| 7 | Âm thanh: SFX + music box + sub drone | A1 (V4): **0 khoảng câm > 0,3 s**; A7: −16 LUFS ± 1, TP ≤ −1,5 dBFS, `latency=1` | Đo trên mp4 cuối, không đo trên wav trung gian |
| 8 | Phụ đề (nếu đăng Shorts) | Khớp ± 0,05 s | `subtitles.py` |
| 9 | Đóng gói `package.py --mux` | 0 lỗi giải mã, thumbnail đúng, có thẻ kết | |
| 10 | Bản EN / JA / KO | 1-1 với bản VN | `CHU_CO_DINH_EN/JA/KO.md` |

**Ngân sách credit (ước tính, cần đo thật):** Concept B/C ≈ **0 credit ảnh** + TTS; Concept A ≈ 4 ảnh MiniMax + 1 clip H3 (6–8 s). Phải xin người dùng duyệt trước (L4).

---

## 4. BẪY đã biết — phải chặn trước khi làm

| # | Bẫy | Cách chặn |
|---|---|---|
| 1 | **AI tự vẽ chữ** khi prompt có thông tin chữ (từng xảy ra với "104 Years Sentencing", "THE COMPANY", bìa "Stan Case Study") | Gỡ **mọi** thông tin chữ khỏi prompt, mô tả bề mặt trưng + thêm *"completely blank and unmarked with no lettering of any kind"*. Mọi chữ trên màn hình **Pillow vẽ sau**, không nhờ AI |
| 2 | **Nền MiniMax sáng hơn nền procedural** ⇒ chữ chìm | Đo H9 lại **toàn bộ** sau khi lắp nền; bật `text_scrim` nếu cần; lặp tối đa 3 vòng đo–bật–render–đo |
| 3 | Georgia thiếu 92 ký tự tiếng Việt | Chữ có dấu dùng **Segoe UI / Malgun / Yu Gothic**; Georgia chỉ cho wordmark "AMBER EYES" (không dấu) |
| 4 | Vai Sói có CER 3,1 % | Rút lời Sói ≤ 8 s, hoặc dùng giọng thay thế trong báo cáo sàng lọc |
| 5 | V4 — câm tuyệt đối > 0,3 s khi tắt nhạc | Luôn có lớp nền môi trường dưới; đo bằng `qc_pause_gate.py --pre` |
| 6 | Cấm commit media (L10) | Chỉ commit tài liệu + code; `.mov`/`.mp4`/`png` nền vẫn nằm trên đĩa |
| 7 | Bẫy "no text" trong NEG **không đủ** | Xem bẫy #1 — phải gỡ chữ khỏi prompt, không chỉ thêm câu cấm |
| 8 | Sửa `edition.py` bằng script dễ sinh SyntaxError | Sau mỗi lần sửa text-based: `ast.parse()` file, kiểm chạy lệnh dựng |
| 9 | 1 file nền dùng chung cho nhiều ngôn ngữ ⇒ **pixel lệch** là bình thường (camera move + crossfade + hạt phim) | Không phải lỗi; không cần render lại nền |

---

## 5. Việc cần người dùng chốt

1. **Concept nào làm trước** (B là đề xuất) — hoặc chốt cả 4 theo lộ trình.
2. **Có lời dẫn (VO) hay không** — trailer không có lời dẫn rẻ hơn, nhưng kênh đang có sẵn 3 giọng đẹp, dùng VO sẽ "bán" được kênh hơn nhiều.
3. **Ngôn ngữ**: chỉ VN, hay dựng luôn EN/JA/KO từ bản VN (như các tập)?
4. **Có được dùng credit MiniMax (ảnh + H3) không** (L4) — quyết định này chốt Concept A/Có, hay chỉ B.
5. **Trailer dùng ở đâu**: trang kênh YouTube, Shorts, Facebook/TikTok, hay chèn đầu mỗi tập?

---

## 6. Tài liệu liên quan

- `assets/brand/channel.json` — token thương hiệu (màu, font, logo, intro) — nguồn duy nhất cho trailer
- `.work/make_intro.py` — kỹ thuật logo layers, wordmark typing, card, 5 vòng vai (tái dùng nguyên vẹn)
- `.work/make_logo.py` — `ml.INK/RED/AMBER/TEXT/MUTED`, `ml.wordmark()`, `ml.tagline()`, `ml.make_mark()`
- `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` — tiêu chuẩn dựng (A3 lệnh, A9 QC)
- `AGENTS.md` — L4 (xin duyệt credit) · L7 (provenance) · L10 (không commit media) · K4/V9 (cấm chi tiết bạo lực)
