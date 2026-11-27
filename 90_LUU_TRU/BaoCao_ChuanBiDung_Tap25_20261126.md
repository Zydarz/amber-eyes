# Báo cáo chuẩn bị dựng video Tập 25 (Yoo Young-chul) — 26/11/2026

Dừng ở mốc **sau bước 8 (ảnh tĩnh)** chờ người dùng duyệt. Chưa dựng `picture.mp4`.

## 1. Việc đã làm
| # | Việc | Kết quả |
|---|---|---|
| 1 | Sửa mapping: câu `5.05#20` bị 2 ảnh (`a5_22` chuông đăng ký + `a5_24` thẻ kết). Bỏ job `a5_24` khỏi `bg_jobs_tap25.json` (140→139 job), giữ file ảnh làm `--endcard` (H12). Sao lưu: `.work/_cu/bg_jobs_tap25_truoc_tach_endcard_20261126.json` | `map_shot_anh.py --check 25` ĐẠT: 139 shot, lỗi mapping 0, ảnh thiếu 0 · `qc_bg_mapping.py 25` ĐẠT (M5 230/230 câu phủ) |
| 2 | Tập 25 mất file TTS từng câu/acting/timeline/stems (chỉ còn master) ⇒ dựng timeline từ SRT + kịch bản bằng `.work/_timeline_from_srt_t25.py` (khớp ký tự, nội suy trong cue). `CanNghe_*` là bản cũ (lệch tuyến tính tới 9 s, ghi 2048,6 s; master thật 2039,64 s) — **không dùng** | Kiểm ASR (faster-whisper base) tại 3 điểm/ngôn ngữ: lệch ≤ 0,3 s. `timeline_s_t25.json` (2039,64 s) · `_EN_` (2050,38 s) · `_JA_` (2323,28 s) = đúng thời lượng master (T20). 230 câu; N1=9, N2=10, H=128, C=44, D=39 |
| 3 | Stems giả lập `make_pseudo_stems.py` (VI, JA) + cổng H24 `qc_wave_gate.py` | ĐẠT cả 5 vai × VI/JA (chạm trần 1,5–3,0 %, lệch chuẩn 0,25–0,28, p95 0,90). Ghi chú: stems giả ⇒ **không thay cổng A14 tầng 1** |
| 4 | `map_shot_anh.py --shots 25 --lang vi/ja/en --endcard t25_a5_24_…` | `shots_t25.json`, `shots_JA_t25.json`, `shots_EN_t25.json` (140 shot gồm thẻ kết) |
| 5 | Ảnh tĩnh mọi shot `build_video3.py --stills all` | VI 140/140 (56 s) · JA 140/140 · `.work/video3_t25/stills`, `.work/video3_JA_t25/stills` |

## 2. Lỗi chặn
- **EN: master MẤT GIỌNG ~60 s (1112 → 1174 s, quanh câu `3.06#4`)** (A14). Đo: năng lượng −38 dB (chỉ nhạc nền), whisper chỉ ra ảo giác lặp. VI/JA quét 1 s/khung: 0 khoảng ≥ 4 s. EN **KHÔNG được dựng** cho tới khi sinh lại/cắt master.

## 3. Việc còn tồn (cần quyết định)
- Shot quá dài (H10 ≤ 15 s / H22 ≤ 30 s, số ước theo timeline thật): VI 58 shot > 15 s, 4 shot > 30 s · JA 64 > 15 s, 18 > 30 s. Giải pháp đúng luật = **sinh thêm ảnh** (tốn credit, L4).
- Chữ AI trong ảnh (H26) thấy trên ảnh tĩnh: `shot_2-046` (băng vàng chữ giả), `shot_5-121` (biển POLICE), cần soi full-res cả các nền đã nêu: `a1_28`, `a1_18`, `a2_08` (người nằm, V9), `a1_32/a1_22/a3_14/a2_16` (gần đen).
- Thẻ kết `shot_5-140` (ảnh sổ hồ sơ): ảnh tĩnh giữa shot chưa thấy chữ AMBER EYES — phải kiểm khung `total − 2 s` sau khi dựng (H12/H14).

---
## 4. CẬP NHẬT 26/11/2026 (tối) — ĐÃ DỰNG VI + JA (EN không dựng — master mất giọng 60 s, A14)

**Phát hiện & vá giữa chừng:** thẻ kết hiện **không có chữ** (H12) vì `map_shot_anh.py --shots` không sinh `template`/`segments` cho shot cuối; renderer chỉ vẽ chữ thẻ kết khi có hai khoá này. Vá bằng `.work/_patch_endcard_t25.py` (VI: T2 "HỒ SƠ TẬP 25 · ĐÃ ĐÓNG" + khẩu hiệu; JA: nhãn đỏ "事件ファイル · 終結" + "第25話" + khẩu hiệu; tránh ngắt "第2|5話"). Bản sao lưu: `.work/_cu/shots{,_JA}_t25_truoc_endcard_20261126.json`. **Còn lại cho Tập 26+: chưa sửa `map_shot_anh.py` (script dùng chung) ⇒ thẻ kết của các tập sau cũng sẽ trống nếu không vá tương tự.**

| Việc | VI | JA |
|---|---|---|
| Dựng | VI dựng đủ lần 1 (không chữ thẻ kết) → dựng lại ĐUÔI từ khung 45894 (1529,8 s) rồi nối `part_00..02` cũ + đuôi mới. Sao lưu bản cũ: `.work/_cu/video3_t25_truoc_endcard_20261126/` | dừng lần 1 (10 %), vá, dựng lại đủ (4 worker) |
| `picture.mp4` / timeline | 2039,63 / 2039,64 s | 2323,27 / 2323,28 s |
| Ranh giới nối | MAE 0,00/255 tại 1529,7 s và 1529,83 s | — |
| Thẻ kết | khung 2033 s có chữ | khung 2318 s có chữ |
| Sóng giọng (3 khung liên tiếp) | đổi hình | đổi hình (Host) |
| Mux (`Tap25[_JA]_master.mp4`) | limiter `0.7943:…:latency=1` | limiter `0.63:…:latency=1` |
| LUFS (mp4) | −16,0 | −16,0 |
| True peak (mp4) | −1,9 dBFS | −3,7 dBFS |
| Giải mã | 0 lỗi | 0 lỗi |
| Độ dài mp4 | 2039,63 s | 2323,27 s |
| Kích thước | 807 MB | 918 MB |

**Không chạy `package.py` nguyên script** (cần `audio_master_t25.wav` đã bị dọn; sẽ ghi đè `mo_ta.txt`, thumbnail — T10/T15). Chỉ gọi `mux`-tương đương bằng ffmpeg và `package.thumbnail()`. `mo_ta.txt` và `.srt` giữ nguyên.
**Thumbnail (H11):** `edition.py` Tập 25 thiếu `thumb_bg` ⇒ khai `thumb_bg = t25_a1_25_yellow_raincoat_figure_approaching` và `thumb` JA (`レインコートの / 殺人鬼`); sao lưu `.work/_cu/edition_truoc_thumb_t25_20261126.py`. Thumbnail VI/JA đã sinh ở `xuat_ban/thumbnail.png`.

**Cảnh báo chất lượng còn lại (chưa xử lý):** shot dài H10/H22 (VI 58 shot > 15 s, JA 64; > 30 s: VI 4, JA 18) · chữ AI trong ảnh nền (`shot_2-046` băng vàng, `shot_5-121` biển POLICE; chưa soi full-res `a1_28`, `a1_18`, `a2_08`) · ảnh gần đen (`a1_32`, `a1_22`, `a3_14`, `a2_16`) · stems giả lập nên A14 tầng 1 chưa kiểm được · timeline dựng từ SRT (ASR ±0,3 s) vì file TTS từng câu đã mất · chưa nghe duyệt cuối.
