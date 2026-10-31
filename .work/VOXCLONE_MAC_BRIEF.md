# VIỆC CẦN LÀM TRÊN MAC — THỬ VoxCPM2 CHẾ ĐỘ CLONE

**Bạn (AI trên Mac) chỉ làm đúng 5 bước dưới đây. Không làm gì khác.**
Không sửa file nào. Không chọn file. Không xoá gì. Không tạo giọng mẫu mới.
Việc của bạn: **kiểm API → sinh 72 file → kiểm đủ → đẩy lên git → dán báo cáo.**

---

## Vì sao làm việc này (đọc 30 giây)

Đến nay kênh dùng VoxCPM2 chỉ để **tạo giọng mẫu**, còn câu thoại do **Higgs** (trên Kaggle) đọc lại.
Higgs khó giữ giọng ổn định. Phía Windows muốn so công bằng: cho **chính VoxCPM2** đọc câu thoại
bằng **chế độ clone** (đưa file giọng mẫu `.wav` + lời mẫu `.txt` vào), cùng giọng mẫu, cùng câu với Higgs.

- 3 vai: Host (`H.wav`), Điều tra viên (`D3_SH`), Chuyên gia (`C2_AB03`) — đều đã có trong repo.
- 12 câu thật mỗi vai × 2 bản = **72 file**. Danh sách câu đã soạn sẵn trong `.work/voxcpm_clone_spec.json`.
- Phía Windows sẽ đo (cao độ, độ đúng chữ, độ ổn định giọng). **Bạn không cần đánh giá.**

---

## BƯỚC 1 — Chuẩn bị (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git checkout main
git pull
test -f .work/voxcpm_clone_spec.json && echo "SPEC OK" || echo "THIEU SPEC"
test -f .work/voxcpm_clone_pilot.py && echo "SCRIPT OK" || echo "THIEU SCRIPT"
grep -q "pilot_voxcpm_clone" .gitignore && echo "GITIGNORE OK" || echo "THIEU GITIGNORE"
test -d assets/pilot_voxcpm_clone && echo "!! THU MUC DA TON TAI" || echo "THU MUC SACH"
```

**Phải thấy đủ 4 dòng:** `SPEC OK` · `SCRIPT OK` · `GITIGNORE OK` · `THU MUC SACH`.
Thiếu dòng nào → **DỪNG**, dán output vào báo cáo (bước 5).

---

## BƯỚC 2 — Kiểm API clone (copy nguyên khối, chạy, ~2–3 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_clone_pilot.py --check 2>&1 | tee .work/voxcpm_clone_check.log
```

Script nạp model, in dòng `CHU KY model.generate: ...`, tìm tham số clone, rồi sinh **thử 1 file**.

**Đi tiếp khi và chỉ khi** thấy cả 3 điều:
- dòng `tham so clone: audio=<tên nào đó>` (không phải `audio=None`)
- dòng `OK  [1/1] ...`
- dòng `XONG: 1/72 file OK`

Nếu thấy `!! DUNG` hoặc `LOI` → **DỪNG**, dán **toàn bộ** `.work/voxcpm_clone_check.log` vào báo cáo.
**Không** tự sửa script để "cho chạy được".

---

## BƯỚC 3 — Sinh đủ 72 file (copy nguyên khối, chạy, ~20–45 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_clone_pilot.py 2>&1 | tee .work/voxcpm_clone_run.log
```

Script tự bỏ qua file đã có (file thử ở bước 2), sinh 71 file còn lại. **Để chạy hết, không ngắt.**
Nếu lỡ bị ngắt: chạy lại đúng lệnh này, script tiếp tục từ chỗ dừng.

---

## BƯỚC 4 — Kiểm đủ file rồi đẩy lên git (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
echo "WAV: $(ls assets/pilot_voxcpm_clone/*.wav | wc -l)  (phai = 72)"
test -f assets/pilot_voxcpm_clone/manifest.json && echo "MANIFEST OK"
git add assets/pilot_voxcpm_clone
echo "WAV da add: $(git diff --cached --name-only | grep -c '\.wav$')  (phai = 72)"
git commit -m "feat(audio): thu VoxCPM2 che do clone - 72 file (H/D3_SH/C2_AB03 x 12 cau x 2 ban)"
git push
git fetch && git status -sb | head -1
```

**Hoàn thành khi và chỉ khi:**
- `WAV: 72`, `MANIFEST OK`, `WAV da add: 72`
- **Dòng cuối là `## main...origin/main`, KHÔNG có chữ `ahead`.**
  Có `ahead` → chạy `git pull --rebase && git push` rồi kiểm lại.

Nếu `WAV` < 72 vì có file `LOI` ở bước 3 → **vẫn commit + push số file đã có**, ghi rõ trong báo cáo.

---

## BƯỚC 5 — Dán báo cáo này (điền vào chỗ `...`)

```
VOXCPM2 CLONE — KET QUA
Buoc 1: <4 dong OK? dan output>
Buoc 2: dan NGUYEN VAN 3 dong: "CHU KY model.generate: ...", "tham so clone: ...", "XONG: ..."
Buoc 3: chay xong sau ... phut | dan NGUYEN VAN phan tu dong "XONG:" den het trong .work/voxcpm_clone_run.log
Buoc 4: WAV=... WAV da add=...
Commit: <hash>   Dong cuoi git status: <dan nguyen van>
```

---

## Cấm (đọc kỹ)

| Không làm | Vì sao |
|---|---|
| Sửa script, spec, `.gitignore` | phía Windows quản lý |
| Đổi `device="mps"` sang CPU, đổi `cfg_value`, `inference_timesteps`, seed | phải giữ nguyên để so công bằng |
| Chuẩn hoá âm lượng / cắt / chỉnh cao độ file ra | phía Windows đo trên file thô |
| Xoá file lỗi, chọn "file tốt nhất" | Windows phải đo cả file lỗi |
| Đụng `assets/voice_ref_voxcpm2*/` | là giọng mẫu đang dùng |
| Báo "xong" khi chưa thấy dòng git **không có `ahead`** | file phải tới được phía Windows |
