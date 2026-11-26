# BÁO CÁO DỰNG 15 CLIP TIKTOK — TẬP 03 (VN / EN / JA)

*Ngày: 25/11/2026 · Bộ sản phẩm: `02_SAN_XUAT/TIKTOK/Tap03{,_EN,_JA}/TK{1..5}_video.mp4`*
*Báo cáo ảnh nền liên quan: `BAO_CAO_ANH_NEN_DOC_TAP03.md` · Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 (bước 5) · Quyết định Q5: clip **không chèn chữ***

---

## 1. Kết quả tổng — 15 clip, 153 shot, QC 153/153

**Tiếng Việt (`Tap03/`)**

| Clip | File | Thời lượng | Shot | Nền | Dung lượng | Bitrate | QC nền |
|---|---|---:|---:|---:|---:|---:|---|
| TK1 | `TK1_video.mp4` | 78,34 s | 10 | 5 | 35,7 MB | 3,64 Mbps | 10/10 |
| TK2 | `TK2_video.mp4` | 77,20 s | 10 | 6 | 32,2 MB | 3,33 Mbps | 10/10 |
| TK3 | `TK3_video.mp4` | 73,50 s | 11 | 10 | 26,8 MB | 2,92 Mbps | 11/11 |
| TK4 | `TK4_video.mp4` | 78,88 s | 11 | 11 | 31,2 MB | 3,16 Mbps | 11/11 |
| TK5 | `TK5_video.mp4` | 68,60 s | 9 | 7 | 23,4 MB | 2,73 Mbps | 9/9 |

**English (`Tap03_EN/`)**

| Clip | File | Thời lượng | Shot | Nền | Dung lượng | Bitrate | QC nền |
|---|---|---:|---:|---:|---:|---:|---|
| TK1 | `TK1_video.mp4` | 67,03 s | 10 | 5 | 30,3 MB | 3,61 Mbps | 10/10 |
| TK2 | `TK2_video.mp4` | 75,20 s | 10 | 6 | 30,0 MB | 3,19 Mbps | 10/10 |
| TK3 | `TK3_video.mp4` | 74,50 s | 11 | 10 | 27,4 MB | 2,94 Mbps | 11/11 |
| TK4 | `TK4_video.mp4` | 78,37 s | 11 | 11 | 30,0 MB | 3,06 Mbps | 11/11 |
| TK5 | `TK5_video.mp4` | 68,28 s | 9 | 7 | 24,9 MB | 2,91 Mbps | 9/9 |

**日本語 (`Tap03_JA/`)**

| Clip | File | Thời lượng | Shot | Nền | Dung lượng | Bitrate | QC nền |
|---|---|---:|---:|---:|---:|---:|---|
| TK1 | `TK1_video.mp4` | 89,58 s | 10 | 5 | 38,4 MB | 3,43 Mbps | 10/10 |
| TK2 | `TK2_video.mp4` | 83,13 s | 10 | 6 | 32,2 MB | 3,10 Mbps | 10/10 |
| TK3 | `TK3_video.mp4` | 88,07 s | 11 | 10 | 33,6 MB | 3,06 Mbps | 11/11 |
| TK4 | `TK4_video.mp4` | 91,20 s | 11 | 11 | 33,7 MB | 2,95 Mbps | 11/11 |
| TK5 | `TK5_video.mp4` | 78,88 s | 9 | 7 | 28,1 MB | 2,85 Mbps | 9/9 |

**Kỹ thuật (đo bằng ffprobe, 15/15 PASS):** H.264 Constrained Baseline · 1080×1920 · 30 fps · yuv420p · AAC-LC 48 kHz stereo 191 kbps · `+faststart` · đều ≤ 500 MB.
**Âm thanh:** lấy nguyên `TK{n}_master_audio.mp3` của từng ngôn ngữ (đã loudnorm I=−16). Volumedetect TK1: VN `−18,8 dB` · EN `−19,4 dB` · JA `−19,3 dB` (max ≈ −4,3 dB) — có tiếng, không im.

## 2. QC ảnh nền theo shot (tự động, 153/153)

Script `.work/_tk_qc_video_t03.py` rút frame tại giây bắt đầu mỗi shot, so vector xám 16×28 với các nền của clip để tìm nền gần nhất, rồi đối chiếu với nền mong đợi trong spec.

| Ngôn ngữ | Shot đúng nền | Sai nền | Kết luận |
|---|---:|---:|---|
| VN | 51/51 | 0 | PASS |
| EN | 51/51 | 0 | PASS |
| JA | 51/51 | 0 | PASS |

QC bằng mắt (frame rút tại t=20–25 s): `tk03_phone_booth`, `tk03_basement_stairs` (EN TK3), `tk03_interview_room` (JA TK4) hiện đúng, full-bleed, không chữ, không logo; nhân vật chỉ hiện dạng bóng/quay lưng (không lộ khuôn mặt).

## 3. Mấu chốt kỹ thuật: timeline phải dựng lại cho cả 3 ngôn ngữ

Tap03 **không có** `timeline_tk{1..5}.json` (Tap01/Tap02 có) — đây là input bắt buộc để cắt shot theo giây nói. Nguồn gốc (`build_tiktok_master_audio_tk03.py`) đã bị dọn, WAV từng câu cũng không còn (`.work/audio_s_tk_t03_vi|en|ja` không tồn tại) ⇒ không tái lập được bằng cách tính lại.

**Đường đã thử và bị loại:** VAD theo dải giọng nói 200–4000 Hz — BGM chế ngự hoàn toàn, cho ra 15–32 đoạn/clip so với 9–11 câu, không dùng được.

**Cách đã dùng (đạt):** ASR + forced alignment.
1. `faster-whisper small` (model đã có sẵn trong cache HF, CPU int8) chạy trên master WAV → word timestamps. Cache tại `.work/_tk_asr_tk03_{clip}_{lang}.json`.
2. Token spec (51 câu) căn với token ASR bằng Needleman–Wunsch, similarity = `difflib` (ngưỡng 0,45).
3. Mỗi câu lấy `start` = token khớp đầu, `end` = token khớp cuối → `timeline_tk{n}.json`.

**Khác biệt theo ngôn ngữ — điểm kỹ thuật chính của lần này:**

| Ngôn ngữ | Đơn vị căn | Vì sao |
|---|---|---|
| VN | **word** | Whisper tách từ theo khoảng trắng |
| EN | **word** | Tương tự VN |
| JA | **char** (ký tự) | Tiếng Nhật **không có khoảng trắng**; whisper trả token kiểu Nhật (`私/を/止/めて/…`) còn text trong spec là câu liền ⇒ phải bung token ASR thành ký tự và nội suy thời gian trong từng token |

**Đối chiếu chéo với spec (đo thật):**

| Ngôn ngữ | Clip | Câu khớp ASR | Dòng nội suy | Tổng tiếng đo | Tổng `est_dur_s` |
|---|---|---:|---:|---:|---:|
| VN | TK1–TK5 | 51/51 | 0 | 338,36 s | 331,08 s |
| EN | TK1–TK5 | 51/51 | 0 | 323,72 s | 329,19 s |
| JA | TK1–TK5 | 51/51 | 0 | 384,58 s | 384,15 s |

⇒ **153/153 câu (51 × 3 ngôn ngữ) có mốc thời gian thật, 0 câu phải nội suy.** Sai lệch tổng tiếng nói so với ước lượng của spec ≤ 2,2 % (JA), ≤ 6,3 % (VN) — nằm trong sai số ước lượng từ trước.

## 4. Script đã tạo (`.work/`)

| Script | Việc |
|---|---|
| `_tk_asr_timeline_t03.py` | ASR + forced alignment (word cho VN/EN, char cho JA) → `timeline_tk{1..5}.json` cho 3 thư mục; có cache ASR nên chạy lại rất nhanh |
| `_build_tk_tap03_video_notext.py` | Dựng clip 9:16 không chữ từ `tk03_*.png` + camera still/push/pull/pan + master audio; nhận `<VN\|EN\|JA>` |
| `_tk_qc_video_t03.py` | QC ffprobe + đối chiếu ảnh nền theo từng shot |
| `_tk_asr_probe.py` | Chạy thử ASR 1 clip/lang, xem độ mịn timestamp |
| `_tk_vad_timeline_t03.py` | Đường VAD băng bỏ (giữ lại làm tài liệu về bẫy) |

**Tái lập:**

```powershell
py -3 .work/_tk_asr_timeline_t03.py --lang VN --write     # (lặp cho EN, JA)
py -3 .work/_build_tk_tap03_video_notext.py VN             # (lặp cho EN, JA)
py -3 .work/_tk_qc_video_t03.py --lang VN                 # (lặp cho EN, JA)
```

Render mất ~4–5 phút/clip (PIL dựng từng frame là nút thắt); chạy song song 2 ngôn ngữ được.

## 5. Việc còn lại (không chặn xem, chặn đăng)

1. **Điền link YouTube Tập 03** vào 5 file `Caption_TK{1..5}.txt` mỗi ngôn ngữ (15 file) — hiện còn placeholder `[LINK_TẬP 03 — cần điền]`.
2. **Bật toggle "AI-generated content"** khi đăng TikTok (bắt buộc theo mục 2.2 của kế hoạch).
3. **Nâng 16 nền dự phòng thành AI thật** khi bật credit auto-consumption (xem mục 6 của `BAO_CAO_ANH_NEN_DOC_TAP03.md`) — ưu tiên `two_agents` → `interview_room` → `mother_shadow` → `gift_drowned` → `life_sentence`. Không ảnh nào trong 15 clip này sai nền, nhưng 16 nền dự phòng là bản crop từ ảnh 16:9 nên chất lượng thấp hơn nhóm AI thật.
4. **Thời lượng JA dài hơn VN** (78,9–91,2 s so với 68,6–78,9 s) — vẫn trong biên series 30 s–20 phút, nhưng nếu muốn đồng nhất với VN thì cần nén tốc độ đọc ở bước TTS, không phải ở bước dựng video.

> **Không commit media (L10):** 15 file MP4 nằm trong `02_SAN_XUAT/TIKTOK/Tap03{,_EN,_JA}/` và bị `.gitignore` loại (`*.mp4`). Chỉ commit tài liệu + script + timeline.
