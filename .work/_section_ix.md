
---

## IX. CẬP NHẬT 27/11/2026 — SINH ẢNH TẬP 41/42/43 · SẢN XUẤT TẬP 24–25 · SERIES 140 TẬP · TẬP 69

> **Cách đo:** quét từng file `assets/bg/` (không tin báo cáo cũ), đối chiếu `bg_jobs_tapXX.json` · chạy lại cổng `map_shot_anh.py --check` và `qc_bg_mapping.py` cho các tập liên quan · đếm câu/từ bằng chính parser của dự án (`.work/parse_kichban.py`) · đọc log dựng trong `.work/`.
> **Sao lưu bản gốc trước khi sửa:** `.work/_cu/BaoCao_ThongKe_68_truoc_cap_nhat_IX_20261127.md`

### IX.1. Sinh ảnh nền Tập 41 / 42 / 43 (26/11/2026 chiều, Cloudflare Workers AI FLUX)

**Đo được trên đĩa:** **369 ảnh** mới sinh trong `assets/bg/` (130 file lúc 15h · 239 file lúc 16h ngày 26/11). `provenance.json` tăng từ **6.709 → 7.078 bản ghi**; mẫu bản ghi mới ghi rõ `cong_cu: "Cloudflare Workers AI (@cf/black-forest-labs/flux-1-schnell)"`, `ngay: "2026-11-26"`, `kich_thuoc_goc: [2112, 1188]`, `kiem_tra_thuong_mai: "đạt"` ⇒ **đúng quy trình Cloudflare, 0 ảnh Kaggle lọt vào kho**.

| Tập | Job | File ảnh | `map_shot_anh --check` | `qc_bg_mapping` (H27) | Kết luận |
|---|---:|---:|---|---|---|
| **41** — Dr. Harold Shipman (Anh) | 157 | **157** | **ĐẠT** · 157 shot · lỗi mapping 0 · bảng không cũ · ảnh thiếu 0 | **ĐẠT** (M1 0/157 · M5 0/227 · M4 157/157) | ✔ **Dùng được** (còn thiếu QC soi mắt) |
| **42** — Tsutomu Miyazaki (Nhật Bản) | 210 | **210** | **TRƯỢT** · 8 shot · **216 lỗi mapping** | **TRƯỢT** (M1 **130/210** mã sai · M5 **208/215** câu chưa phủ · M4 **114/210 MẪU CHUNG**) | ✖ **KHÔNG dùng được** — phải sinh lại |
| **43** — Suzane von Richthofen (Brazil) | 159 | **2** | **TRƯỢT** · 159 shot · lỗi mapping 0 · **ảnh thiếu 157** | **ĐẠT** (M1 0/159 · M5 0/240 · M4 159/159) | ⚠ **Prompt tốt, chỉ cần sinh nốt 157 ảnh** |

**Nguyên nhân Tập 42 hỏng (đo trực tiếp trên `bg_jobs_tap42.json`, tạo 26/11 14:38):**
1. **Tên file sai quy ước:** `t42_a1_1_01`, `t42_a2_2_04`… (thêm một đoạn `_hồi_`) trong khi Tập 41/43 dùng `tNN_aX_NN` ⇒ `map_shot_anh.py` không tách được mã câu từ tên → 216 lỗi mapping.
2. **Mã câu là placeholder:** cả 210 job chỉ có **20 giá trị `sentences` phân biệt** (`1.01#1`…`5.01#1`), không khớp câu nào trong kịch bản.
3. **Prompt là bộ mẫu chung:** **181/210 prompt** đều là khuôn *"moody psychological crime documentary background scene (shot N-XX), atmospheric fog, dramatic contrast…"*, chỉ khác số thứ tự ⇒ M4 báo "MẪU CHUNG".
4. **29 prompt còn nhắc bối cảnh không liên quan:** đề tài Hy Lạp cổ đại (đền Artemis/Ephesus, thành phố Athena, v.v.) trong khi Tập 42 là vụ Tsutomu Miyazaki (Nhật Bản, 1988–1989).

⇒ **210 ảnh Tập 42 không dùng cho dựng.** Cần viết lại `bg_jobs_tap42.json` theo đúng mẫu Tập 49 (mục VI.7: mỗi câu một prompt riêng, mã câu thật, tên đúng quy ước `t42_aX_NN_…`) rồi sinh lại toàn bộ.

**Hai rủi ro còn lại:**
- **Chưa có QC soi mắt** cho 369 ảnh này — trong `.work/qc_montage/` không có tờ montage nào cho t41/t42/t43 (tờ mới nhất là `regen_00/01/02.jpg` của Tập 37–39 lúc 26/11 14:20). Bắt buộc soi 100 % trước khi dựng Tập 41.
- **Prompt Tập 41 vẫn dùng mệnh đề cấm chữ kiểu cũ** (`"no text, no watermark"`) — theo bài học mục VIII.4, FLUX bỏ qua mệnh đề này và còn vẽ chữ ⇒ rủi ro chữ AI cao hơn bình thường.

### IX.2. Trạng thái cổng H27 (`qc_bg_mapping.py`) — đo lại toàn bộ Tập 26–67 ngày 27/11

| Kết quả | Số tập | Danh sách |
|---|---:|---|
| **ĐẠT** | 36 | 26–41, 43, 46–63, 65, 67 |
| **TRƯỢT** | 3 | **42** (M1 130/210 · M5 208/215 · M4 114/210 mẫu chung) · **44** (M1 178/175 · M5 205/240) · **45** (M1 81/174 · M5 147/240) |
| **Chưa có `bg_jobs`** | 3 | 64, 66, 68 (chờ mở rộng kịch bản H23) — **Tập 69 mới cũng chưa lập** |

- Đối chiếu với báo cáo 26/11: **Tập 42 là mới trượt** (do `bg_jobs` tạo mới trong ngày 26/11, chưa qua cổng); **Tập 44 và 45 trượt** vì `bg_jobs_tap44/45.json` được viết lại lúc 26/11 15:00–15:03 nhưng mã câu chưa khớp kịch bản.
- Tập 43 **ĐẠT** cổng H27 ⇒ chỉ cần sinh nốt 157 ảnh, không cần viết lại prompt.

### IX.3. Sản xuất Tập 24 và Tập 25 (26/11 → 27/11)

**Tập 24 (Lee Choon-jae) — hoàn tất 3 ngôn ngữ:**
| Ngôn ngữ | File | Dung lượng | Thời điểm |
|---|---|---:|---|
| VI | `Tap24/xuat_ban/Tap24_master.mp4` | 831,2 MB | 26/11 11:21 |
| EN | `Tap24_EN/xuat_ban/Tap24_EN_master.mp4` | 806,1 MB | 26/11 13:32 |
| JA | `Tap24_JA/xuat_ban/Tap24_JA_master.mp4` | 923,4 MB | 26/11 15:29 |
| Thumbnail | `Tap24/xuat_ban/thumbnail.png` | 1,3 MB | 26/11 11:21 |

**Tập 25 (Yoo Young-chul):**
| Việc | Kết quả |
|---|---|
| Mapping | Bỏ job `a5_24` (thẻ kết) khỏi `bg_jobs_tap25.json` (140→139 job), giữ file làm `--endcard` (H12) → `--check 25` **ĐẠT**: 139 shot · lỗi mapping 0 · ảnh thiếu 0; `qc_bg_mapping 25` ĐẠT (M5 230/230 câu phủ) |
| Timeline | File TTS từng câu/acting/stems đã mất ⇒ dựng timeline từ SRT (`.work/_timeline_from_srt_t25.py`), kiểm ASR (faster-whisper base) lệch **≤ 0,3 s**: VI 2039,64 s · JA 2323,28 s · EN 2050,38 s — khớp thời lượng master (T20) |
| Stems | `make_pseudo_stems.py` (VI, JA) + cổng H24 `qc_wave_gate.py` **ĐẠT** 5 vai × VI/JA (chạm trần 1,5–3,0 %, lệch chuẩn 0,25–0,28, p95 0,90) — *stems giả lập ⇒ chưa thay được cổng A14 tầng 1* |
| Dựng VI | `picture.mp4` 2039,63 s → mux `Tap25_master.mp4` **769,9 MB** (26/11 20:20) · LUFS **−16,0** · true peak **−1,9 dBFS** · giải mã 0 lỗi |
| Dựng JA | `picture.mp4` 2323,27 s → mux `Tap25_JA_master.mp4` **875,9 MB** (26/11 21:15) · LUFS **−16,0** · true peak **−3,7 dBFS** · giải mã 0 lỗi |
| Dựng EN | **ĐANG CHẠY** — master âm thanh đã sinh lại 26/11 20:03 sau khi phát hiện mất giọng ~60 s (1112→1174 s, quanh câu `3.06#4`); timeline EN 27/11 07:57 · `shots_EN_t25.json` 07:57 · ảnh tĩnh 140/140 lúc 07:59:59 · **dựng 4 worker từ 08:00** (khoảng 24 % lúc 08:27) |
| Thẻ kết | Vá `.work/_patch_endcard_t25.py` — `map_shot_anh.py --shots` **không sinh `template`/`segments` cho shot cuối** nên thẻ kết bị trống. **LƯU Ý: script dùng chung chưa được vá ⇒ Tập 26+ cũng sẽ bị trống thẻ kết nếu không vá tương tự** |
| Đóng gói | Không chạy `package.py` nguyên script (cần `audio_master_t25.wav` đã bị dọn; sẽ ghi đè `mo_ta.txt`/thumbnail T10/T15) ⇒ chỉ mux tương đương bằng ffmpeg + `package.thumbnail()`. `mo_ta.txt` và `.srt` giữ nguyên |
| Thumbnail | `edition.py` Tập 25 thiếu `thumb_bg` ⇒ khai `thumb_bg = t25_a1_25_yellow_raincoat_figure_approaching` + nhãn JA; thumbnail VI/JA đã sinh tại `xuat_ban/thumbnail.png` (26/11 20:23) |

**Cảnh báo chất lượng còn treo ở Tập 25:** shot dài (VI **58 shot > 15 s**, 4 shot > 30 s; JA 64 > 15 s, 18 > 30 s) · chữ AI trong ảnh nền (`shot_2-046` băng vàng chữ giả, `shot_5-121` biển POLICE; chưa soi full-res `a1_28`, `a1_18`, `a2_08`) · ảnh gần đen (`a1_32`, `a1_22`, `a3_14`, `a2_16`) · stems giả lập nên A14 tầng 1 chưa kiểm được · timeline dựng từ SRT · chưa nghe duyệt cuối.

### IX.4. Series mới: **"BẢY TÂM LÝ VÀ HÀNH VI" — 140 tập / 14 chuyên đề**

- **Vị trí:** `01_KICH_BAN/BayTamLyVaHanhVi/` — **140/140 tập** đều có `kichban_tapXX.md` + `REVIEW_kichban_tapXX.md`.
- **Đo bằng chính parser dự án** (`.work/parse_kichban.py`, chạy lại 27/11): **3.897 phần tử thoại · 26.912 câu · 765.276 từ** — trung bình **192 câu · 5.466 từ/tập**; không tập nào vượt 280 câu.
- **14 chuyên đề (10 tập mỗi chuyên đề):** ChuyenDe00 Bảy Hào Quang & Ảo Tưởng Thuộc Ác · ChuyenDe01 Tự Bảo Vệ Cắt Đứt Đạo Đức · ChuyenDe02 Bỏ Ba Bong Tối & Thái Nhân Cách · ChuyenDe03 Quỹ Đạo Leo Thang & Điểm Gãy Tâm Lý · ChuyenDe04 Thao Túng & Kiểm Soát Tâm Lý · ChuyenDe05 Đấu Trí & Phỏng Vấn · ChuyenDe06 Tâm Lý Học Hiện Trường & Hành Vi Pháp Y · ChuyenDe07 Tâm Lý Học Đám Đông & Điểm Mù Xã Hội · ChuyenDe08 Nạn Nhân Học & Cẩm Nang Sinh Tồn · ChuyenDe09 Trí Nhớ & Nhân Chứng Án Oan · ChuyenDe10 Tâm Thần Học & Pháp Y · ChuyenDe11 Sinh Học Thần Kinh & Tâm Lý Học Phát Triển · ChuyenDe12 Tâm Lý Đồng Phạm · ChuyenDe13 Kỹ Nghệ Xã Hội & Tâm Lý Tội Phạm Kỹ Nguyên Số.
- **Chưa làm:** chưa lập `bg_jobs`, chưa có `Bang_Shot_Anh`, chưa vào `02_SAN_XUAT`, chưa dựng video.

### IX.5. Cập nhật series 45 tập "Tâm Lý Học Tội Phạm" (đo lại từ `index_45_tap.json`)

| Chỉ số | Số đo mới 27/11 | So với báo cáo 26/11 |
|---|---:|---|
| Số tập | **45** | không đổi |
| Câu thoại | **10.545 câu** | thay cho "681 lượt thoại" (đo cũ, chỉ tính mẫu chung) |
| Từ | **229.559 từ** | thay cho 125.132 từ |
| Job ảnh nền | **4.295 job** | + "sẵn sàng khởi tạo theo prompt chuyên đề" |
| Tập đạt ngưỡng H25/H27 | **14/45** (01–07, 29, 30, 35–38, 40) | có danh sách cụ thể |
| Tập trùng prompt (M4) | **8 tập**: 29 (171/175), 30 (161/175), 31 (148/175), 32 (141/175), 33 (135/175), 34 (129/175), 39 (10/175), 43 (12/175) | mới đo được |
| Tập chưa có `bg_jobs` | **4 tập**: 41, 42, 44, 45 | mới đo được |
| JSON đã tách | **45/45** tại `.work/tlhtp/script_tlhtp_tapXX.json` + `index_45_tap.json` | — |
| Thư mục sản xuất | `02_SAN_XUAT/TamLyHocToiPham/` = **135 thư mục** (Tap01–45 × VI/EN/JA) + 3 thư mục chuyên đề "Công Tắc Tắt Lương Tâm" (VI/EN/JA) | — |
| Bảng tổng hợp | `02_SAN_XUAT/TamLyHocToiPham/BANG_TONG_HOP_SAN_XUAT_45_TAP.md` (26/11 15:35) | — |

### IX.6. Tập 69 — hồ sơ vụ án mới (27/11/2026)

- **Tên:** *Hồ Sơ Đoàn Văn Sáng — VỎ BỌC CÔNG QUYỀN, HỘI NHÓM KÍN VÀ MƯỜI THÁNG SỐNG HAI MẶT TẠI LẠNG SƠN* (Việt Nam — huyện Hữu Lũng, tỉnh Lạng Sơn).
- **File:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap69/kichban_tap69.md` (52.806 byte · 376 dòng · tạo 27/11 08:05).
- **Đo:** **5 Hồi** · **40 lượt thoại** (HOST 16 · ĐIỀU TRA VIÊN 12 · CHUYÊN GIA TÂM LÝ 10 · NGƯỜI BÌNH THƯỜNG 2) · **234 câu** trong dấu nháy · thời lượng dự kiến **26–29 phút (~1.650 s)**.
- **Chủ đề tâm lý:** Hiệu ứng Hào quang (Halo Effect) · Cơ chế chia ngăn nhận thức (Compartmentalization) · Quỹ đạo leo thang ảo tưởng qua không gian mạng (Fantasy Escalation) · Sự phi nhân hóa (Dehumanization) · Nạn nhân học trong môi trường cô lập xã hội.
- **Chưa có:** `bg_jobs`, `Bang_Shot_Anh`, thư mục `02_SAN_XUAT/Ho_So_Toi_Pham/Tap69` (số thư mục 02_SAN_XUAT vẫn là 245, 01_KICH_BAN đã lên 246).

### IX.7. Việc cần quyết / ưu tiên tiếp theo (thứ tự đề xuất)

1. **Tập 42 — viết lại `bg_jobs_tap42.json`** theo mẫu Tập 49 (mục VI.7): mỗi câu một prompt riêng + mã câu thật + tên đúng quy ước `t42_aX_NN_…`; rồi **xoá 210 ảnh bộ mẫu chung** và sinh lại.  *(L4 — cần duyệt trước khi tốn credit)*
2. **Tập 44, 45 — sửa cổng H27:** M1 (mã câu sai) và M5 (câu chưa phủ) đều phải về 0 trước khi sinh ảnh.
3. **Tập 41 — soi mắt 100 % 157 ảnh** (chưa có QC) rồi mới dựng; cần soi kỹ các ảnh có biển/bảng/giấy.
4. **Tập 43 — sinh nốt 157 ảnh** bằng Cloudflare (prompt đã ĐẠT cổng H27).
5. **Vá `map_shot_anh.py`** để thẻ kết luôn có `template`/`segments` — hiện Tập 26+ sẽ bị trống thẻ kết (vá riêng cho Tập 25 đã ở `.work/_patch_endcard_t25.py`).
6. **Tập 25 EN** — theo dõi dựng xong, mux, đo LUFS/true peak, soi thẻ kết.
7. **Tập 64, 66, 68** — mở rộng kịch bản (K1–K10, H23) rồi mới lập `bg_jobs`.
8. **Tập 69** — lập `bg_jobs` + `Bang_Shot_Anh` để vào dây chuyền.
9. **8 shot dài 30–34 s** ở Tập 27/29/36/37/47 — chờ có `timeline_s` đo thật rồi mới tách (mục VI.4).

### IX.8. Bảng tổng hợp kho ảnh sau đợt 26–27/11 (đo lại toàn bộ)

| Vùng | Số lượng | Ghi chú |
|---|---:|---|
| `assets/bg/` gốc — **theo tiền tố tập** | **4.389** | 27 tập đủ ảnh + Tập 43 (2) |
| `assets/bg/` gốc — **tên cũ không theo tập** | **233** | `bedroom_door.png`, `cage.png`, `deedee_room.png`… |
| **Tổng file ở gốc `assets/bg/`** | **4.622** | +369 so với 26/11 |
| `assets/bg/_raw/` | 590 file (280 PNG) | ảnh gốc Tập 01–09 chưa đổi tên |
| `assets/bg/outputs/` | 150 PNG | toàn `t15_*` |
| `assets/bg/_gemini_backup/` | 3 PNG | — |
| **Tổng toàn kho** | **5.365 file** | +369 so với 26/11 (4.996) |
| `provenance.json` | **7.078 bản ghi** | +369 so với 26/11 (6.709) |
| **Cần sinh thêm** | **4.463 ảnh / 29 tập** | 31–35, 42–63, 65, 67 |
