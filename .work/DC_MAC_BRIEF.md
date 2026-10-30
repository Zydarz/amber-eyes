# BRIEF — Tạo lại giọng mẫu VoxCPM2 cho 2 vai: Điều tra viên (D) + Chuyên gia (C)

**Người nhận:** AI chạy trên **Mac mini (Apple Silicon)** của tác giả dự án
**Ngày giao:** 30/10/2026
**Mục đích:** sinh **18 clip ứng viên** (2 vai × 3 bậc mô tả × 3 seed) bằng **VoxCPM2 Voice Design**, commit + push.

> Brief **tự-contained**: chạy đúng lệnh dưới đây, không cần đọc tài liệu khác, không tự sáng tác thêm.
> Clip **chưa được dùng** cho sản xuất. Tác giả sẽ đo bản clone trên Kaggle rồi mới chọn.

---

## 0. Tóm tắt 1 phút

| Việc | Giá trị |
|---|---|
| Lệnh | 1 lệnh Python (mục 3), chạy **đúng 1 lần** |
| Thời gian | ~20–35 phút (nạp model + 18 take) |
| Kết quả | 18 `.wav` + 18 `.txt` + 1 `refs.json` trong `assets/voice_ref_voxcpm2_dc/` |
| Sau khi xong | commit + push (mục 6) → gửi báo cáo (mục 8) |
| **KHÔNG** | sửa script/manifest · chạy lại nhiều lần · chạm vào `assets/voice_ref_voxcpm2/` và `assets/voice_ref_voxcpm2_g9/` |

---

## 1. Bối cảnh — vì sao phải làm lại

Kênh có 3 vai chính, đọc bằng **Higgs Audio v3** (clone giọng từ clip mẫu). Bản sản xuất Tập 02 bị người nghe
**nhầm Điều tra viên với Chuyên gia**. Đo F0 trên 416 file: D↔C chỉ cách **1,03 nửa cung**.

Nguyên nhân (đã đo, không phải phỏng đoán):

| Clip mẫu | F0 clip | F0 sau Higgs clone | Nhận xét |
|---|---:|---:|---|
| `H.wav` (Host) | 108 Hz | 130 Hz | Higgs **kéo** giọng nam trung về ~125–130 Hz |
| `D.wav` (D cũ) | 128 Hz | 124 Hz | ⇒ dính Host (0,22 nửa cung) |
| `M_HIGH.wav` (D đang dùng) | 192 Hz | 193 Hz | ⇒ thành **giọng nữ**, dính C |
| `M_LOW.wav` | 96 Hz | **98 Hz** | giọng **rất trầm** thì Higgs **giữ được** |
| `C.wav` (C cũ) | 210 Hz | 205 Hz | giữ được, nhưng CER clone 3,09% (> 2%) |

⇒ Thiết kế mới, 3 vai khác nhau trên **nhiều trục**:

| | Host (giữ `H.wav`) | **D_NEW** — Điều tra viên | **C_NEW** — Chuyên gia |
|---|---|---|---|
| F0 **clip** mục tiêu | — | **82–95 Hz** | **200–218 Hz** |
| F0 sau clone dự kiến | ~130 Hz | ≤ 100 Hz | ~205–215 Hz |
| Chất giọng | ấm, tròn | **khàn, rè, thô** | **trong, sắc** |
| Tốc độ (âm tiết/s) | ~3,4 | **2,9–3,2** (chậm, cụt) | **3,9–4,3** (nhanh, dứt khoát) |

Vì sao C **không** đẩy cao hơn 218 Hz: vai phụ N2 clone ~270 Hz, cần cách ≥ 4 nửa cung.

---

## 2. Môi trường (preflight, 30 giây)

| Hạng mục | Giá trị |
|---|---|
| Python | `/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3` |
| Repo | `/Users/duonganhhai/CodeGit/amber-eyes` (branch `main`) |
| Model | `openbmb/VoxCPM2` đã có trong cache HF (script dùng `local_files_only=True`) |
| `ffmpeg` | có trong `PATH` |

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git pull
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 -c "import voxcpm, torch, numpy, soundfile; print('OK', torch.__version__)"
ffmpeg -version | head -1
grep -n "voice_ref_voxcpm2_dc" .gitignore      # PHAI thay dong: !assets/voice_ref_voxcpm2_dc/*.wav
test -f .work/voxcpm_refs_manifest_dc.json && echo manifest-ok
```

Thiếu bất kỳ dòng nào → **dừng**, báo lại (mục 7).

---

## 3. Lệnh cần chạy (đúng 1 lần)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
    --manifest .work/voxcpm_refs_manifest_dc.json \
    --out assets/voice_ref_voxcpm2_dc \
    --candidates 3 2>&1 | tee .work/voxcpm_dc_run.log
```

Script tự làm:
1. Nạp VoxCPM2 trên MPS.
2. Mỗi vai × mỗi bậc mô tả (`D_NEW`: `vlow-gravel`, `bass-rasp`, `deep-smoker` · `C_NEW`: `crisp`, `bright-auth`, `lecture`)
   × 3 seed (42, 101, 2024) → **sinh hết, không dừng sớm** (cổng thật là đo trên Kaggle).
3. Đóng gói **mọi take** thành WAV 24 kHz mono −18 LUFS, tên `<VAI>_<bậc>_tNN.wav` + `.txt`.
4. Ghi `refs.json` sau **mỗi** take (ngắt giữa chừng vẫn giữ được phần đã xong).
5. In bảng: F0, thời lượng, âm tiết/giây, cờ `OK` / `!!`.

Script **từ chối chạy** nếu `assets/voice_ref_voxcpm2_dc/refs.json` đã tồn tại (chống ghi đè).
Nếu gặp lỗi này → **không xoá**, báo lại.

---

## 4. Kết quả mong đợi

```
--- D_NEW  (muc tieu F0 clip 82-95 Hz) ---
  > D_NEW_vlow-gravel_t01 (seed=42, cfg=2.0)... 55s | 22.4s | F0 91.3 Hz | 3.05 am/s  [TRONG DAI]
  ...
XONG: 18 ung vien trong .../assets/voice_ref_voxcpm2_dc
```

### Nghiệm thu

| # | Tiêu chí | Đạt khi |
|---|---|---|
| 1 | Exit code 0, không traceback | |
| 2 | Đủ 18 `.wav` + 18 `.txt` + `refs.json` | `ls assets/voice_ref_voxcpm2_dc | wc -l` = **37** |
| 3 | **D_NEW**: ≥ 2 take cờ `[TRONG DAI]` (F0 77–101 Hz, 16–28 s) | |
| 4 | **C_NEW**: ≥ 2 take cờ `[TRONG DAI]` (F0 188–231 Hz, 16–28 s) | |

Không đạt 3 hoặc 4 → **vẫn commit + push**, ghi rõ trong báo cáo. **Không** tự thêm bậc, **không** chạy lại.

### Bước nghe nhanh (bắt buộc, 5 phút)

Nghe **mỗi vai 2 take có F0 gần giữa dải nhất**, ghi nhận xét 1 dòng/take:
- D_NEW: có **khàn/rè** thật không? Có nghe như người **50+**? Có méo, tiếng lạ, đọc sai chữ?
- C_NEW: có **trong, sắc, nhanh**? Có đọc sai chữ, nuốt âm?

Chỉ **ghi nhận xét**, không xoá take nào.

---

## 5. Nếu lệch dải

Script vẫn đóng gói take lệch, cờ `!!`. Đây là dữ liệu — **giữ nguyên**, báo lại nguyên văn dòng `!!`.

---

## 6. Commit + push

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git add assets/voice_ref_voxcpm2_dc
git status --short          # PHAI thay 18 dong .wav + 18 .txt + refs.json, KHONG file nao khac
git commit -m "feat(audio): 18 clip ung vien VoxCPM2 cho vai D (khan tram) + C (trong sac)"
git push
```

- Thiếu file `.wav` trong `git status` → **không commit**, báo lại (lỗi `.gitignore`).
- `.work/voxcpm_raw/` và `.work/voxcpm_dc_run.log` bị ignore — **không** `git add -f`.
- `git push` bị từ chối → `git pull --rebase` rồi push lại.

---

## 7. Sự cố

| Triệu chứng | Xử lý |
|---|---|
| `No module named 'voxcpm'` | dùng đúng Python ở mục 2 |
| `ffmpeg` not found | báo lại (không tự cài phần mềm hệ thống) |
| `LocalEntryNotFoundError` / offline | model chưa có cache → **báo lại trước khi đổi cấu hình** |
| `MPS backend out of memory` | báo lại; **không** đổi sang CPU |
| `refs.json da ton tai` | không xoá, báo lại |
| Kẹt > 10 phút ở 1 take | chờ đến 15 phút rồi báo lại |

---

## 8. Báo cáo gửi tác giả

```
TAO GIONG D_NEW + C_NEW — KET QUA
Thoi gian chay: ... phut | Exit code: ...
Bang (chep nguyen van phan "XONG:" trong .work/voxcpm_dc_run.log):
  ...
So take [TRONG DAI]: D_NEW .../9 · C_NEW .../9
Nghe nhanh:
  D_NEW_<...>: <khan? 50+? loi?>
  D_NEW_<...>: ...
  C_NEW_<...>: <trong? sac? nhanh? loi?>
  C_NEW_<...>: ...
Dong canh bao (neu co): ...
Git: commit <hash> | push OK/loi
```

---

## 9. TUYỆT ĐỐI KHÔNG

| Không | Vì sao |
|---|---|
| Sửa `.work/voxcpm_generate_g9.py`, `.work/voxcpm_refs_manifest_dc.json` | dải F0 suy ra từ 416 file đã đo |
| Chạy lại để "thử thêm" | mọi take vẫn phải đo lại trên Kaggle |
| Hạ/nâng cao độ bằng phần mềm (phase vocoder, PSOLA, sox pitch) | đã thử: Higgs đọc sai nội dung, CER 8–12% |
| Đụng `assets/voice_ref_voxcpm2/`, `assets/voice_ref_voxcpm2_g9/` | đang dùng cho bản hiện tại |
| Tự chạy TTS / Higgs / dựng audio | phía tác giả làm trên Kaggle |

---

## 10. Sau khi tác giả nhận kết quả

1. Upload 18 ứng viên lên dataset Kaggle `chiduong2026/amber-eyes-voice-ref-voxcpm2`.
2. Chạy thử clone: mỗi ứng viên đạt × 12 câu đúng vai × 2 bản. Đo **F0 sau clone** (D ≤ 100 Hz, C 200–225 Hz),
   **CER < 2%**, tốc độ.
3. G9 **mọi cặp kể cả khác giới** (H↔D, H↔C, D↔C ≥ 4 nửa cung) · G8 (4 cảm xúc → 1 người) ·
   nghe mù xen kẽ 3 vai → phải ra **3 người**.
4. Tác giả nghe duyệt → sinh lại 109 câu D + 100 câu C → ghép.
