# VIỆC CẦN LÀM TRÊN MAC — VÒNG 3 (CHỈ giọng D)

**Bạn (AI trên Mac) chỉ làm đúng 4 bước dưới đây. Không làm gì khác.**
Không sửa file nào. Không chọn take. Không xoá gì. Không đụng giọng C.
Việc của bạn: **sinh file → kiểm đủ file → đẩy lên git → dán báo cáo.**

---

## Vì sao có vòng 3 (đọc 30 giây)

Vòng 1 (`assets/voice_ref_voxcpm2_dc/`) và vòng 2 (`assets/voice_ref_voxcpm2_dc2/`) **đã xong. KHÔNG làm lại, KHÔNG sửa.**
Phía Windows đã cho Higgs đọc thử trên Kaggle:
- Giọng **C** đã đạt, đã chọn. **Vòng này không làm C.**
- Giọng **D** (nam khàn trầm) đọc đúng chữ, nhưng **chưa đủ trầm**: chỉ cách giọng Host 3,6–3,9 nửa cung (cần ≥ 4).
- Higgs giữ gần nguyên cao độ giọng mẫu D ⇒ cần giọng mẫu D **trầm hơn: 78–88 Hz** (vòng trước 89–98 Hz).

Vòng 3 sinh **16 take D**: 4 câu mô tả trầm hơn × 4 seed (42, 7 là 2 seed đã ra giọng trầm; 2718, 9001 là seed mới).
Phía Windows sẽ đo và chọn. **Bạn không cần chọn.**

---

## BƯỚC 1 — Chuẩn bị (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git checkout main
git pull
test -f .work/voxcpm_refs_manifest_dc3.json && echo "MANIFEST OK" || echo "THIEU MANIFEST"
grep -q "voice_ref_voxcpm2_dc3" .gitignore && echo "GITIGNORE OK" || echo "THIEU GITIGNORE"
grep -q -- "--seeds" .work/voxcpm_generate_g9.py && echo "SCRIPT OK" || echo "SCRIPT CU"
test -d assets/voice_ref_voxcpm2_dc3 && echo "!! THU MUC DA TON TAI" || echo "THU MUC SACH"
```

**Phải thấy đủ 4 dòng:** `MANIFEST OK` · `GITIGNORE OK` · `SCRIPT OK` · `THU MUC SACH`.
Thiếu bất kỳ dòng nào → **DỪNG**, dán output vào báo cáo (bước 4), không làm tiếp.

---

## BƯỚC 2 — Sinh 16 take (copy nguyên khối, chạy, chờ ~15–25 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
  --manifest .work/voxcpm_refs_manifest_dc3.json \
  --out assets/voice_ref_voxcpm2_dc3 \
  --seeds 42,7,2718,9001 \
  2>&1 | tee .work/voxcpm_dc3_run.log
```

Số take = 1 vai × 4 câu mô tả × 4 seed = **16**. **Để chạy hết, không ngắt.**
Take bị đánh dấu `!!` (lệch cao độ) là **bình thường**: giữ nguyên, không xoá, không chạy lại.

---

## BƯỚC 3 — Kiểm đủ file rồi đẩy lên git (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
echo "WAV: $(ls assets/voice_ref_voxcpm2_dc3/*.wav | wc -l)  (phai = 16)"
echo "TXT: $(ls assets/voice_ref_voxcpm2_dc3/*.txt | wc -l)  (phai = 16)"
test -f assets/voice_ref_voxcpm2_dc3/refs.json && echo "REFS OK"
git add assets/voice_ref_voxcpm2_dc3
echo "WAV da add: $(git diff --cached --name-only | grep -c '\.wav$')  (phai = 16)"
git commit -m "feat(audio): vong 3 - 16 take ung vien VoxCPM2 cho D (78-88 Hz)"
git push
git fetch && git status -sb | head -1
```

**Hoàn thành khi và chỉ khi:**
- `WAV: 16`, `TXT: 16`, `REFS OK`, `WAV da add: 16`
- **Dòng cuối là `## main...origin/main`, KHÔNG có chữ `ahead`.**
  Có `ahead` nghĩa là **chưa đẩy lên được**: chạy `git pull --rebase && git push` rồi kiểm lại.

⚠ Nếu `WAV da add` < 16 → **không commit**, dán output vào báo cáo.

---

## BƯỚC 4 — Dán báo cáo này (điền vào chỗ `...`)

```
VONG 3 — KET QUA
Buoc 1: <4 dong OK? dan output>
Buoc 2: chay xong sau ... phut, co loi khong: ...
Bang ket qua (dan NGUYEN VAN phan tu dong "XONG:" den het, trong .work/voxcpm_dc3_run.log):
...
So take [TRONG DAI] (khong co "!!"): .../16
Buoc 3: WAV=... TXT=... WAV da add=...
Commit: <hash>   Dong cuoi git status: <dan nguyen van>
```

---

## Cấm (đọc kỹ)

| Không làm | Vì sao |
|---|---|
| Sửa / sinh lại `assets/voice_ref_voxcpm2_dc/` hoặc `_dc2/` | đã đo xong, là dữ liệu so sánh |
| Sinh giọng C | C đã chọn xong |
| Sửa script, manifest, `.gitignore` | phía Windows quản lý |
| Xoá take lệch cao độ, chọn "take tốt nhất" | Windows phải đo cả take lệch |
| Chỉnh cao độ bằng phần mềm (sox, PSOLA, pitch shift) | làm Higgs đọc sai chữ (đã chứng minh) |
| Báo "xong" khi chưa thấy dòng git **không có `ahead`** | file phải tới được phía Windows |
