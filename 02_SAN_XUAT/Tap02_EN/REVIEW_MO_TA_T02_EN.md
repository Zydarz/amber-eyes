# KIỂM ĐỊNH MÔ TẢ ↔ VIDEO — TẬP 02 BẢN TIẾNG ANH
**Ngày kiểm:** 02/11/2026 · **Đối tượng:** `xuat_ban/description.txt` + `xuat_ban/mo_ta.txt` (2 file trùng nhau) so với `Tap02_EN_master.mp4` + `Tap02_EN.srt`
**Nguồn đối chiếu:** `Tap02_EN.srt` (402 cue) · `.work/timeline_s_EN_t02.json` · `KeHoach_Video_Tap02_EN.md` (bảng shot 151 dòng) · `assets/voice_ref_voxcpm2_en2/refs.json` · `REVIEW_EN.md` · ffprobe trên `Tap02_EN_master.mp4`

---

## 0. KẾT LUẬN NHANH

| Hạng mục | Trạng thái |
|---|---|
| Đoạn mở đầu (July 2009 · CFB Trenton · QEII) | ✅ khớp 100% với lời đọc |
| "4 dangerous stages" (voyeurism → trộm cắp → xông nhà → giết) | ✅ khớp — video có card đếm 0/4, 4 thẻ ghim |
| "Detective Sergeant Jim Smyth" | ✅ khớp (00:00:13:47, 00:15:08) |
| Mốc chương (chapters) | ❌ **lệch ~2–3 s về trước** → đã sửa |
| 4 bullet "nội dung tập" | ⚠ 3/4 dùng từ không có trong video → đã sửa |
| Disclaimer (bệnh lý, 486.4, vợ) | ✅ khớp / đã chỉnh 1 cụm |
| Hotline khủng hoảng | ✅ 4/4 số đúng (CRCVC đã verify web) |
| Claim "không dùng giọng người thật" | ✅ **đúng, có bằng chứng** |
| 📚 SOURCES | ❌ **[PENDING] — 30/30 dòng chưa có nguồn. Đây là blocker duy nhất còn lại** |

---

## 1. MỐC CHƯƠNG — LỆCH (đã sửa)

Mốc trong mô tả cũ được lấy từ timeline cũ (bản MiniMax 25/10), **không** từ timeline Higgs hiện hành (`timeline_s_EN_t02.json`). Mỗi mốc cũ đều rơi vào ~2–3 s **trước** lúc lời đọc hồi kia bắt đầu ⇒ người xem bấm chapter bị đọng ở đuôi hồi trước.

| Chapter | Mô tả cũ | **Mô tả mới** | Cue SRT thực tế | Lệch cũ |
|---|---|---|---|---|
| Intro & Advisory | 00:00 | **00:00** | intro kênh 0,00–22,41 s (thẻ A + thẻ B) | 0 |
| Act 1 | 00:20 | **00:23** | `[HOST] July 2009.` @ 00:23.00 | −3,0 s |
| Act 2 | 04:40 | **04:42** | `When Jessica Lloyd vanished…` @ 04:42.40 | −2,4 s |
| Act 3 | 08:13 | **08:16** | `Confronting the dossier…` @ 08:15.63 | −2,6 s |
| Act 4 | 13:30 | **13:33** | `Sunday, February 7th, 2010.` @ 13:32.89 | −2,9 s |
| Act 5 | 18:32 | **18:35** | `October 2010.` @ 18:34.76 | −2,8 s |

**Nguồn chuẩn:** `KeHoach_Video_Tap02_EN.md` dòng "Âm thanh" — *hồi 23.0–280.4 · 282.4–493.63 · 495.63–810.89 · 812.89–1112.76 · 1114.76–1383.79 s*. Cả 6 mốc mới đều trùng với cue SRT đầu tiên của từng hồi.

### 1.1 Xác minh trực tiếp trên MP4 (trích frame tại đúng mốc mới)

Đã chạy `ffmpeg -ss <mốc> -i Tap02_EN_master.mp4 -frames:v 1` — **cả 5 frame đều hiện đúng card tiêu đề hồi**, tức mốc chapter mới rơi đúng vào khoảnh giây hồi bắt đầu:

| Mốc | Frame thật trong video |
|---|---|
| 00:23 | `ACT 01` — **THE EXTREME CONTRAST BEHIND A COLONEL'S RANK** |
| 04:42 | `ACT 02` — **THE 4 STAGES OF THE ABYSS** |
| 08:16 | `ACT 03` — **INSIDE THE MIND OF A TWO-FACED PREDATOR** |
| 13:33 | `ACT 04` — **BREAKING A MILITARY MIND** |
| 18:35 | `ACT 05` — **THE VERDICT, RED FLAGS & CLOSING THOUGHTS** |

⇒ Tên hồi trong mô tả cũng khớp **1:1** với tiêu đề trên hình. (Mốc cũ rơi vào khoảng nghỉ giữa hồi, người xem thấy thẻ hồi trước.)

> ⚠ **CHU_CO_DINH_EN.md** (template mô tả US) trước đây ghi `00:23 / 05:13 / 09:33 / 15:07 / 21:16` — lệch tới **2 phút 42 s** ở Act 5. Đã đồng bộ về bảng mới. Bài học: **mốc chương phải lấy từ timeline cuối, không copy từ tập khác hay từ bản dựng cũ.**

---

## 2. 4 BULLET "NỘI DUNG TẬP" — 3/4 SAI TỪ KHÓA (đã sửa)

Bullet nào nói đúng thứ **không có trong video** thì người xem bấm vào tìm sẽ thấy không có ⇒ mất uy tín.

| # | Bullet cũ | Vấn đề | **Bullet mới** |
|---|---|---|---|
| 1 | `Behavioral Escalation & **Dopamine Tolerance**: Why deviances never remain stagnant.` | Video nói **"Dopamine Desensitization"** (00:09:18). Chữ "tolerance"/"deviances"/"stagnant" **0 lần** trong SRT | `Behavioral Escalation & **Dopamine Desensitization**: Why every transgression demands a bigger thrill to feel the same.` |
| 2 | `…How an elite mind split into two entirely detached lives **without internal conflict**.` | Video nói ngược lại: *"the brain to isolate **conflicting cognitive streams**"* (00:10:57) và *"contradiction without collapsing into madness?"* (00:10:44) | `…How an elite mind isolated two **conflicting cognitive streams without collapsing into madness**.` |
| 3 | `…using **rapport building, active listening**, and behavioral pressure.` | "rapport" / "active listening" **0 lần** trong SRT. Video mô tả kỹ thuật khác: *"never raised his voice… a flat, calm, **disarming cadence**, systematically guiding Williams into the trap of overconfidence"* (00:15:08) + áp lực *"Investigators are at your home right now"* (00:16:21) | `…used a **calm, disarming cadence and surgical psychological pressure** to dismantle a formidable military mind.` |
| 4 | `**4 Critical Red Flags**: Recognizing hidden predators…` | ⚠ **CÓ THẬT — nhưng chỉ là card trên hình**, không được đọc. Shot `5-14` (cue `5.06#2` @ 00:20:30) hiện card **"FOUR CRITICAL RED FLAGS"**; shot `5-13` hiện **"SPOTTING PREDATORS EARLY"**. Lời đọc không liệt kê 4 cờ ⇒ giữ "4" sẽ tạo kỳ vọng vượt quá video | `**Spotting Predators Early**: Four critical red flags concealed behind spotless moral facades.` (ghép đúng 2 card) |

---

## 3. ĐOẠN MỞ ĐẦU — KHỚP 100%

| Câu trong mô tả | Bằng chứng trong SRT |
|---|---|
| "In July 2009" | 00:23.00 `[HOST] July 2009.` |
| "CFB Trenton, Canada's largest military airbase" | 00:25.09 "At Canadian Forces Base Trenton —" / 00:26.84 "the largest air force base in the Canadian military." |
| "flew Queen Elizabeth II and the Canadian Prime Minister" | 00:49.15 "Elizabeth II and the" / 00:51.97 "Prime Minister of Canada." |
| "model husband whose wife served as an associate director at the Heart and Stroke Foundation" | 00:52.32–01:00.68 (khớp nguyên văn) |
| "progressed through four dangerous stages: nocturnal voyeurism → break-ins → home invasions → homicide" | 05:07.88 "4 distinct stages" · 05:27.68 "The first stage: **Voyeurism**" · 05:38.86 "The second stage: **Breaking and entering**" · 06:17.29 "The third stage: **Infiltration of occupied homes**" · 06:35.10 "the final stage: **Murder**" — card trên hình đếm 0/4 |

---

## 4. DISCLAIMER & HOTLINE

| Mục | Kết luận |
|---|---|
| "Psychological analyses … not an official clinical diagnosis" | ✅ khớp — 00:08:39 "no official clinical diagnosis has ever been released" |
| "Section 486.4 publication ban" | ✅ đúng, khớp `REVIEW_EN.md` §3 |
| "former spouse … completely exonerated" | ⚠ đổi → **"was fully cleared of any wrongdoing"** ("exonerated" là thuật ngữ pháp lý nặng, hơn cả việc chưa bị truy tố) |
| RAINN 1-800-656-4673 / rainn.org (24/7) | ✅ đúng |
| National DV Hotline 1-800-799-SAFE, text START → 88788 | ✅ đúng |
| VictimConnect 1-855-4-VICTIM | ✅ đúng |
| CRCVC 1-877-232-2610 | ✅ **số đúng** (verify crcvc.ca 02/11/2026) — nhưng tên chính thức là **Canadian _Resource_ Centre** for Victims of Crime; thêm giờ mở cửa `Mon-Fri 8:30am-4:30pm ET` (không phải 24/7 như RAINN/DV) |

---

## 5. CLAIM GIỌNG ĐỌC — ✅ ĐÚNG, CÓ BẰNG CHỨNG

Mô tả ghi: *"all narration … generated with Boson AI Higgs Audio v3, voice-cloned from reference clips that were themselves produced by AI text-to-speech for this channel. No real person's voice was recorded, used, or cloned."*

Đã truy nguồn tới tận gốc:
- `KeHoach_Video_Tap02_EN.md` dòng 243: *"Người dùng chốt: bản EN dùng **Higgs Audio v3**"* ✅ đúng phiên bản.
- `assets/voice_ref_voxcpm2_en2/refs.json`: mọi giọng mẫu đều có `"voice_source": "VoxCPM2 (OpenBMB) - Voice Design"`, `"model": "openbmb/VoxCPM2"`, kèm `control_instruction` mô tả giọng bằng **văn bản** (ví dụ *"A man in his early forties, low-pitched and warm…"*) ⇒ **TTS thuần từ text, không có giọng người thật làm nguồn**.
- `thu_giong_kiem_vai/report.md`: 5/5 vai đều ghi "(Higgs Audio v3)" → **G10 ĐẠT**.

⇒ Câu khai báo này **chính xác**, giữ nguyên.

---

## 6. THUMBNAIL & FILE ĐẦU RA

| Kiểm | Kết quả |
|---|---|
| `thumbnail.png` | ✅ 1280×720 · chữ "THE TWO-FACED COLONEL" khớp `CHU_CO_DINH_EN.md` §1B · 2 nhân vật sói/cáo khớp vai D/C |
| `Tap02_EN_master.mp4` | 1392,77 s (23:12,77) · 1920×1080 @30/1 · h264 + aac 48 kHz stereo · 503.893.749 byte — khớp QC |
| `Tap02_EN_master.mp3` | 1392,79 s — lệch 0,023 s so với video ✅ |
| `Tap02_EN.srt` | 402 cue · cue cuối kết thúc 00:23:03,79 · khớp QC |

---

## 7. ⚠ CÒN LẠI TRƯỚC KHI ĐĂNG (chưa đụng vì cần quyết định của bạn)

1. **📚 SOURCES — blocker.** `nguon_tham_khao_EN.md` có **30 dòng, 30/30 đều ⚠ "chưa có nguồn"** ⇒ câu *"All factual events, dates, and quotes are sourced from public court records, the OPP interrogation transcripts, and verified journalistic archives"* đang là **khẳng định vượt quá bằng chứng đang có**. Không tự điền link bịa — cần tra từng dòng rồi dán vào mục 📚.
2. **Bật "Altered or synthetic content"** khi đăng YouTube (đã ghi trong `REVIEW_EN.md`).
3. **Rà điều khoản thương mại Higgs Audio v3** (đã ghi công trong mô tả).
4. **Nghe lại toàn tập** — đặc biệt hồi 3 (mốc 08:16) và hồi 5 (mốc 18:35) sau khi đổi chapter.

---

## 8. FILE ĐÃ SỬA

| File | Thay đổi |
|---|---|
| `xuat_ban/description.txt` | 12 dòng sửa (5 mốc chương + 4 bullet + 1 disclaimer + 1 hotline + 1 dòng PENDING) · 3.661 → 3.814 byte · UTF-8 **không BOM**, CRLF |
| `xuat_ban/mo_ta.txt` | giống hệt `description.txt` (sha256 trùng) |
| `CHU_CO_DINH_EN.md` | mốc chương trong template + 4 bullet + disclaimer + hotline |
| `KeHoach_Video_Tap02_EN.md` | dòng "Gói đăng" (mốc chương mới) + dòng "Còn lại trước khi đăng" (thêm ⑤) |

**Bản gốc còn nguyên trong lịch sử git** — revert bằng `git checkout -- <file>` nếu cần.
