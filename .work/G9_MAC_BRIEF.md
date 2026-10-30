# BRIEF — Tạo 4 clip tham chiếu VoxCPM2 cho G9 (Tập 02, dự án Amber Eyes)

**Người nhận:** AI chạy trên **Mac mini (Apple Silicon)** của tác giả dự án
**Ngày giao:** 30/10/2026
**Người gửi:** tác giả dự án (làm việc qua AI agent trên Windows)
**Mục đích:** sinh 4 file WAV tham chiếu mới bằng **VoxCPM2 Voice Design**, rồi commit lên git.

> Brief này **tự-contained**: không cần đọc tài liệu khác, không cần lịch sử trò chuyện.
> Chạy đúng các lệnh dưới đây, không tự ý sáng tác thêm.

---

## 0. Tóm tắt 1 phút

| Việc | Lệnh |
|---|---|
| **Cần làm** | Chạy 1 script Python đã có sẵn trong repo → sinh 4 clip WAV 24 kHz → commit + push |
| **Cần làm** | Chạy đúng **1 lần**, không sửa script, không sửa manifest |
| **Thời gian** | ~25–40 phút (nạp model + 4 vai × tối đa 5 take) |
| **Kết quả cần** | 4 file `.wav` + 4 file `.txt` + 1 file `refs.json` trong `assets/voice_ref_voxcpm2_g9/` |
| **Cổng sau khi xong** | Báo lại ngay cho tác giả (mục 6) — **KHÔNG** tự đọc thử, **KHÔNG** tự chạy pipeline |

---

## 1. Bối cảnh (để hiểu vì sao con số F0 quan trọng)

Dự án `amber-eyes` là game kể chuyện tội phạm, tập 02 có **5 vai**:

| Vai | Giới | Vai trò | Clip tham chiếu hiện tại |
|---|---|---|---|
| H | nam | người dẫn chuyện | `H.wav` |
| D | nam | thám tử | `D.wav` |
| C | nữ | chuyên gia tâm lý | `C.wav` |
| N1 | nữ | người kể thứ nhất | `W1.wav` |
| N2 | nữ | người kể thứ hai | `W1.wav` |

Hệ thống TTS mới (Higgs Audio v3, chạy trên GPU Kaggle) **clone giọng** từ file tham chiếu.
Luật nội bộ **G9** bắt buộc: **hai giọng cùng giới phải cách nhau ≥ 4 nửa cung** về cao độ nền (F0).

Đo thực nghiệm trên 192 audio mẫu đã xác nhận: **F0 của audio đọc ra được quyết định bởi F0 của clip
tham chiếu**, tỉ lệ `clone / clip` = **1,02–1,06** khi clip ≥ 132 Hz (ở clip rất thấp 107 Hz thì tỉ lệ
nhảy lên 1,22 ⇒ cần chừa biên).

⇒ **Đổi clip tham chiếu là cách duy nhất để tách 2 vai nam.** Bộ clip hiện tại **không đủ**.

| Cặp cần tách | Vấn đề hiện tại | Cần clip mới |
|---|---|---|
| H ↔ D (nam) | cách **1,19 nửa cung** (cần ≥ 4) | 1 clip **nam rất trầm** + 1 clip **nam cao** (dự phòng) |
| C ↔ N1 ↔ N2 (nữ) | C↔N1 = **3,25 nc**, **N1↔N2 = 1,89 nc** (cần ≥ 4) | 1 clip **nữ trầm** (khuyến nghị) + 1 clip **nữ cao** (dự phòng) |

Vì vậy **dải F0 mục tiêu dưới đây là con số cứng, không được tự ý đổi**:

| Tên vai | F0 mục tiêu **của clip** | Dùng cho vai | Bậc thang `control` (script tự dò nhẹ → mạnh) |
|---|---|---|---|
| `M_LOW` | **70–86 Hz** | H (nam rất trầm) | `very-low` → `bass` → `sub-bass` |
| `M_HIGH` | **168–182 Hz** | D (nam cao, dự phòng) | `upper-mid` → `higher` → `high-bright` |
| `W6_LOW` | **148–162 Hz** | N1 (nữ trầm, **khuyến nghị**) | `lower-mid` → `low` → `alto` |
| `W5_HIGH` | **258–276 Hz** | N1 (nữ cao, phương án B) | `very-high` → `high-bright` → `soprano` |

---

## 2. Môi trường (kiểm tra trước khi chạy)

| Hạng mục | Giá trị mong đợi |
|---|---|
| Máy | Mac mini, **Apple Silicon** (MPS) — KHÔNG chạy được trên Windows |
| Python | `/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3` |
| Repo | `/Users/duonganhhai/CodeGit/amber-eyes` (branch `main`) |
| Thư viện Python | `voxcpm`, `torch`, `numpy`, `soundfile` — đã có trong venv trên |
| `ffmpeg` | phải có trong `PATH` (`ffmpeg -version` chạy được) |
| Model `openbmb/VoxCPM2` | phải **đã nằm trong cache HuggingFace** cục bộ (script dùng `local_files_only=True`) |

**Preflight (chạy trước, 30 giây):**

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git pull
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 -c "import voxcpm, torch, numpy, soundfile; print('OK', torch.__version__)"
ffmpeg -version | head -1
```

Nếu cả 3 lệnh trên OK → sang bước 3. Nếu lỗi → xem mục 7.

---

## 3. Lệnh cần chạy (đúng 1 lần)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py
```

**Script này tự làm hết** (không cần can thiệp tay trong lúc chạy):

1. Nạp model VoxCPM2 trên MPS.
2. Với **mỗi vai**, thử lần lượt các biến thể `control` **từ nhẹ đến mạnh**, sinh 1 take mỗi bậc,
   đo F0 của take đó, và **dừng ngay** khi có take nằm trong dải mục tiêu.
   Nếu hết bậc mà chưa trúng dải → sinh thêm tối đa 3 take của bậc gần nhất.
3. Đóng gói take thắng thành **WAV 24 kHz mono, −18 LUFS** (chuẩn của dự án), kèm `.txt` (lời đọc mẫu).
4. Ghi `assets/voice_ref_voxcpm2_g9/refs.json` với đúng schema của bộ clip gốc.
5. In ra bảng F0 từng take + kết luận từng vai.

**Thời gian:** nạp model ~1–2 phút, mỗi take ~40–90 giây ⇒ tổng **~25–40 phút**.
**Không được** ngắt giữa chừng. Nếu cần dừng, để chạy hết rồi mới xử lý.

---

## 4. Màn hình kết quả mong đợi

```
--- M_LOW  (muc tieu F0 70-86 Hz) ---
  > [very-low] M_LOW_very-low_take01.wav (seed=42, cfg=2.0)... 51s | 24.1s | F0 82.4 Hz [TRONG DAI]
  => DUNG trong dai, dung tai day: M_LOW_very-low_take01.wav
  => DONG GOI assets/voice_ref_voxcpm2_g9/M_LOW.wav (24 kHz mono, 24.1s, F0 82.4 Hz)
...
XONG:
  M_HIGH    OK    .../assets/voice_ref_voxcpm2_g9/M_HIGH.wav
  M_LOW     OK    .../assets/voice_ref_voxcpm2_g9/M_LOW.wav
  W5_HIGH   OK    .../assets/voice_ref_voxcpm2_g9/W5_HIGH.wav
  W6_LOW    OK    .../assets/voice_ref_voxcpm2_g9/W6_LOW.wav
```

### Tiêu chí nghiệm thu (kiểm theo thứ tự này)

| # | Tiêu chí | Đạt khi |
|---|---|---|
| 1 | Script chạy xong, **exit code 0** | không có traceback |
| 2 | Cả **4 vai** in dòng `=> DONG GOI ...` | đủ 4 vai |
| 3 | Dòng `=> DONG GOI` **không có** tiếp đầu `!!` | F0 trong dải **và** thời lượng 16–28 s |
| 4 | Có đủ 9 file | 4 `.wav` + 4 `.txt` + 1 `refs.json` trong `assets/voice_ref_voxcpm2_g9/` |
| 5 | `refs.json` có 4 key | `M_LOW`, `M_HIGH`, `W6_LOW`, `W5_HIGH` |

### Kiểm tra nhanh sau khi chạy

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
ls -la assets/voice_ref_voxcpm2_g9/
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 -c "
import json
d = json.load(open('assets/voice_ref_voxcpm2_g9/refs.json'))
for k, v in d.items():
    print(k, v['f0_median_hz'], 'Hz |', v['seconds'], 's |', v['notes'])
"
```

**Mong đợi:** 4 dòng, mỗi dòng có `notes = []` (rỗng), F0 nằm trong dải mục tiêu ở mục 1.

---

## 5. Nếu một vai KHÔNG trúng dải F0

Script **vẫn xuất clip gần nhất** và in cảnh báo dạng:

```
  !! KHONG co take nao trong dai 70-86 Hz. Van lay take gan nhat: M_LOW_bass_take03.wav (F0 94.2 Hz)
```

**Cách xử lý đúng:** **KHÔNG tự sửa script, KHÔNG tự thêm bậc thang, KHÔNG xoá file.**
→ Vẫn làm bước 6 (commit + push) → rồi **báo lại cho tác giả**, kèm dòng cảnh báo nguyên văn.
Tác giả sẽ dùng số đo đó để quyết định bước tiếp theo (ví dụ dùng đồng thời `M_LOW` + `M_HIGH` cho
H và D để chắc chắn đạt G9).

> Lưu ý: **1–2 vai lệch dải là chấp nhận được**, miễn là **≥ 2 vai trúng dải** và còn đủ file để
> tác giả đo trên GPU. Đừng chạy lại script nhiều lần.

---

## 6. Commit + push (bắt buộc, để tác giả lấy được kết quả)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git add assets/voice_ref_voxcpm2_g9
git status --short
git commit -m "feat(audio): them 4 clip tham chieu VoxCPM2 cho G9 (Tap 02)"
git push
```

**Kiểm tra trước khi commit:**
- `git status --short` phải hiện **9 file trong `assets/voice_ref_voxcpm2_g9/`**:
  **4 file `.wav`** + 4 file `.txt` + 1 file `refs.json`.
- ⚠ **BẮT BUỘC phải thấy đủ 4 dòng kết thúc bằng `.wav` trong `git status`.**
  Repo có luật `.gitignore` ignore toàn cục `*.wav` (chỉ gỡ cho `assets/voice_ref_voxcpm2/*.wav`).
  Nếu lần `git pull` của bạn **chưa có** dòng gỡ cho `assets/voice_ref_voxcpm2_g9/*.wav` thì
  `git add` sẽ **bỏ qua im lặng file .wav** ⇒ mất toàn bộ kết quả.
  → Nếu thấy thiếu `.wav`: **đừng commit**, báo lại ngay (tác giả sẽ sửa `.gitignore` và bạn pull lại).
- Thư mục `.work/voxcpm_raw/` (bản 48 kHz trung gian) **đã bị `.gitignore`** → **KHÔNG** `git add` nó.
- Nếu `git status` hiện thêm file lạ ngoài `assets/voice_ref_voxcpm2_g9/` → **đừng commit**, báo lại.

Sau `git push` xong, báo lại cho tác giả (mục 8).

---

## 7. Xử lý sự cố

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| `ModuleNotFoundError: No module named 'voxcpm'` | chạy sai Python | dùng đúng `/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3`; kiểm tra `ls /Users/duonganhhai/ai/voxcpm2_project/.venv/bin/` |
| `ffmpeg` not found | thiếu ffmpeg trong PATH | `brew install ffmpeg`, hoặc báo lại (không tự cài phần mềm hệ thống) |
| Lỗi kiểu `offline` / `cannot load model` / `LocalEntryNotFoundError` | model `openbmb/VoxCPM2` **chưa có trong cache** cục bộ | script dùng `local_files_only=True` ⇒ cần mạng tải 1 lần. **Báo lại tác giả trước khi đổi cấu hình**; nếu được phép thì chạy 1 lần riêng để tải model về cache, rồi chạy lại script nguyên vẹn |
| `MPS backend out of memory` | RAM không đủ | báo lại; **đừng** tự đổi `device="mps"` thành `"cpu"` (sẽ mất hàng giờ) |
| Script kẹt > 60 phút mà không có dòng mới | có thể take đang dài bất thường | chờ thêm 10 phút rồi báo lại; **đừng kill giữa chừng** nếu chưa hết 60 phút |
| `git push` báo từ chối (rejected) | nhánh local lệch remote | `git pull --rebase` rồi `git push` lại; nếu vẫn lỗi thì báo lại |

---

## 8. BÁO CÁO KẾT QUẢ (gửi lại cho tác giả)

Sau khi `git push` xong, gửi lại đúng nội dung này (điền vào chỗ trống, kèm **ảnh chụp màn hình terminal**
nếu tiện):

```
TẠO CLIP G9 — KẾT QUẢ
──────────────────────
Máy / Python: <...>
Thời gian chạy: <...> phút
Exit code: <0 / khác>

Bảng F0 từng vai (chép nguyên văn từ output script):
  M_LOW   : F0 ... Hz | ... s | [TRONG DAI] / [LECH]
  M_HIGH  : F0 ... Hz | ... s | [TRONG DAI] / [LECH]
  W6_LOW  : F0 ... Hz | ... s | [TRONG DAI] / [LECH]
  W5_HIGH : F0 ... Hz | ... s | [TRONG DAI] / [LECH]

Các dòng cảnh báo (nếu có, chép nguyên văn):
  <...>

File đã tạo (ls output):
  <...>

Git:
  commit: <hash>
  push: OK / lỗi <...>
```

---

## 9. TUYỆT ĐỐI KHÔNG LÀM

| Không | Vì sao |
|---|---|
| Không sửa `.work/voxcpm_generate_g9.py` | script đã được verify; mọi thay đổi phải do tác giả quyết định sau khi có số đo |
| Không sửa `.work/voxcpm_refs_manifest_g9.json` (đổi `f0_target`, thêm/xoá bậc thang) | dải F0 là con số cứng suy ra từ 192 audio đã đo |
| Không chạy lại script nhiều lần để "thử lấp lánh" | tốn ~30 phút/lần, kết quả vẫn phải đo lại trên GPU |
| Không xoá `.work/voxcpm_raw/` | là bản trung gian 48 kHz để đối chiếu |
| Không `git add` thư mục nào ngoài `assets/voice_ref_voxcpm2_g9/` | tránh lôi file rác vào repo |
| Không tự đọc thử, không chạy pipeline TTS/mix/đóng gói video | việc đó chạy trên GPU Kaggle, phía tác giả lo |
| Không dùng bộ giọng MiniMax để thay thế | chưa xác nhận điều khoản sử dụng |
| Không xoá/ghi đè bộ clip gốc `assets/voice_ref_voxcpm2/` | bộ gốc vẫn đang dùng cho Tập 02 |
| Không tự ý đổi `--device`, `temperature`, seed | không thuộc phạm vi nhiệm vụ này |

---

## 10. File liên quan (để tra cứu, không cần mở)

| File | Vai trò |
|---|---|
| `.work/voxcpm_generate_g9.py` | **script cần chạy** — dò thang `control`, đo F0, đóng gói 24 kHz |
| `.work/voxcpm_refs_manifest_g9.json` | đặc tả 4 vai: dải F0 mục tiêu + 3 bậc `control` mỗi vai + lời đọc mẫu |
| `.work/voxcpm_generate_all.py` | script gốc tạo bộ 7 clip (để đối chiếu cách dùng) |
| `.work/higgs_make_refs_voxcpm.py` | script gốc đóng gói bộ 7 clip (để đối chiếu schema `refs.json`) |
| `.work/G9_HD_HUONG_DAN.md` | giải thích đầy đủ vì sao cần 4 clip này (số đo gốc) |
| `.work/DAT_SPEC_G9.md` | đặc tả ngắn (bản này là bản rút gọn) |
| `.gitignore` | xem dòng `!assets/voice_ref_voxcpm2_g9/*.wav` — **quan trọng**, xem mục 6 |
| `assets/voice_ref_voxcpm2/` | bộ 7 clip gốc đang dùng — **không đụng vào** |

---

## 11. Sau khi nhận được kết quả

Tác giả sẽ: đưa 4 clip lên Kaggle → chạy **pilot v6** (đo F0 audio clone + CER cho từng clip) →
chốt ánh xạ vai (H/D/C/N1/N2) bằng số đo thật → nghe mù → đọc 203 câu → dựng video.

**Cần bạn làm thêm gì sau khi push?** Không. Hẹn gặp lại ở bước pilot v6.
