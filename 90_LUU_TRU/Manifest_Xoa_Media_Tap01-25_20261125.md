# Manifest xóa media tập 1–25

**Ngày:** 25/11/2026
**Người thực hiện:** MCode (agent), theo yêu cầu trực tiếp của user
**Quyết định:** user chọn (a) phạm vi = chỉ file thành phẩm trong `xuat_ban`; (b) xóa cả `.mp3`; (c) xóa **vĩnh viễn** để giải phóng dung lượng ổ D:

## Phạm vi đã xóa

Toàn bộ file media nằm trong `02_SAN_XUAT/Ho_So_Toi_Pham/TapXX*/xuat_ban/`.

Lưu ý: **chỉ 4 tập còn file thành phẩm** — Tap15, Tap21, Tap22, Tap23 (mỗi tập có 3 bản ngôn ngữ: VN, `_EN`, `_JA`).
Các tập 1–14, 16–20, 24–25 không còn master nào trong `xuat_ban` (đã bị dọn trước đó hoặc chưa dựng).

| Tập | File | Kích thước (MB) |
|---|---|---:|
| Tap15 | Tap15_master.mp3 / .mp4 / .wav | 42,4 / 697,9 / 339,0 |
| Tap15_EN | Tap15_EN_master.mp3 / .mp4 / .wav | 41,6 / 683,1 / 332,5 |
| Tap15_JA | Tap15_JA_master.mp3 / .mp4 / .wav | 49,0 / 807,6 / 392,4 |
| Tap21 | Tap21_master.mp3 / .mp4 / .wav | 55,1 / 1242,7 / 441,1 |
| Tap21_EN | Tap21_EN_master.mp3 / .mp4 / .wav | 50,4 / 1136,1 / 403,3 |
| Tap21_JA | Tap21_JA_master.mp3 / .mp4 / .wav | 58,4 / 1314,3 / 467,0 |
| Tap22 | Tap22_master.mp3 / .mp4 / .wav | 53,6 / 1012,8 / 428,5 |
| Tap22_EN | Tap22_EN_master.mp3 / .mp4 / .wav | 49,2 / 937,1 / 393,4 |
| Tap22_JA | Tap22_JA_master.mp3 / .mp4 / .wav | 59,1 / 1118,6 / 472,5 |
| Tap23 | Tap23_master.mp3 / .mp4 / .wav | 54,9 / 1045,5 / 439,1 |
| Tap23_EN | Tap23_EN_master.mp3 / .mp4 / .wav | 48,8 / 929,6 / 390,1 |
| Tap23_JA | Tap23_JA_master.mp3 / .mp4 / .wav | 58,6 / 1114,5 / 468,8 |

**Tổng: 36 file, 17,22 GB.**
Dung lượng trống ổ D: trước xóa: 41,1 GB.

## KHÔNG đụng vào (giữ nguyên)

- `.work/` — toàn bộ file trung gian dựng: `plain_t18`–`plain_t23` (+`_EN`, `_JA`), `video3_t15` (+`_EN`, `_JA`), `stems_t15` (+`_EN`, `_JA`), `audio_master_t15/16/17` (+`_EN`, `_JA`) ≈ 26,6 GB
- `.work/kaggle_higgs/` — 942 file WAV TTS gốc (348,5 MB), dùng chung cho QC/CER
- `assets/sfx/t2 … t25` — thư viện tiếng động riêng theo tập (0,77 GB), vẫn dựng lại được
- `assets/sfx/t26 … t29`, `assets/bgm/`, `assets/brand/`, `assets/bg/`, `assets/voice_ref_*`, `assets/pilot_voxcpm_clone/`
- `02_SAN_XUAT/sfx_youtube/` — kho SFX gốc tải về
- `90_LUU_TRU/thu_giong/` — 12 file mẫu giọng
- Mọi file tài liệu: kịch bản, hồ sơ tập, báo cáo QC, timeline, `.srt`, `thumbnail.png`, `mo_ta.txt`

## Khả năng khôi phục

KHÔNG — xóa vĩnh viễn theo lựa chọn của user. Các file này không có trong git (`.gitignore` loại `*.mp3`, `*.mp4`, `*.wav`).
Muốn dựng lại phải chạy lại pipeline TTS → `build_audio3.py` → `build_video3.py` → `package.py --mux` cho tập tương ứng.

## Bài học / lưu ý cho lần sau

- Xóa media phải hỏi user trước (luật L4 trong `AGENTS.md`) — đã làm, có questionnaire ghi rõ 3 quyết định.
- Luật L10 (không commit media) đã giữ: repo không phình thêm byte nào.
- Nếu cần dựng lại tập đã xóa master: file trung gian trong `.work/` còn nguyên cho Tap15 (`.work/video3_t15`, `.work/stems_t15`, `.work/audio_master_t15.wav`) và Tap21–23 (`.work/plain_t21`–`t23`).
