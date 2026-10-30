# VIỆC CẦN LÀM TRÊN MAC — VÒNG 2 (giọng D + C)

**Bạn (AI trên Mac) chỉ làm đúng 4 bước dưới đây. Không làm gì khác.**
Không sửa file nào. Không tự "cải thiện" giọng. Không chọn take. Không xoá gì.
Việc của bạn: **sinh file → kiểm đủ file → đẩy lên git → dán báo cáo.**

---

## Vì sao có vòng 2 (đọc 30 giây)

Vòng 1 (thư mục `assets/voice_ref_voxcpm2_dc/`, đã có trên git) **đã xong, KHÔNG làm lại, KHÔNG sửa.**
Phía Windows đã đo vòng 1: quá ít take đúng cao độ.
- Vai **D** (nam khàn trầm) cần F0 **82–95 Hz**. Chỉ 2/9 take đạt, và đều ở mép (96–98 Hz).
- Vai **C** (nữ trong sắc) cần F0 **200–218 Hz**. Take nói nhanh thì bị cao quá (235–254 Hz).

Cao độ phụ thuộc **seed** nhiều hơn câu mô tả, nên vòng 2 **sinh thêm nhiều seed** ra một **thư mục MỚI**
(`assets/voice_ref_voxcpm2_dc2/`). Phía Windows sẽ đo và chọn. **Bạn không cần chọn.**

---

## BƯỚC 1 — Chuẩn bị (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git checkout main
git pull
test -f .work/voxcpm_refs_manifest_dc2.json && echo "MANIFEST OK" || echo "THIEU MANIFEST"
grep -q "voice_ref_voxcpm2_dc2" .gitignore && echo "GITIGNORE OK" || echo "THIEU GITIGNORE"
grep -q -- "--seeds" .work/voxcpm_generate_g9.py && echo "SCRIPT OK" || echo "SCRIPT CU"
test -d assets/voice_ref_voxcpm2_dc2 && echo "!! THU MUC DA TON TAI" || echo "THU MUC SACH"
```

**Phải thấy đủ 4 dòng:** `MANIFEST OK` · `GITIGNORE OK` · `SCRIPT OK` · `THU MUC SACH`.
Thiếu bất kỳ dòng nào → **DỪNG**, dán output vào báo cáo (bước 4), không làm tiếp.

---

## BƯỚC 2 — Sinh 32 take (copy nguyên khối, chạy, chờ ~30–45 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
  --manifest .work/voxcpm_refs_manifest_dc2.json \
  --out assets/voice_ref_voxcpm2_dc2 \
  --seeds 7,13,77,123,256,512,1234,4321 \
  2>&1 | tee .work/voxcpm_dc2_run.log
```

Số take = 2 vai × 2 câu mô tả × 8 seed = **32**. **Để chạy hết, không ngắt.**
Take bị đánh dấu `!!` (lệch cao độ) là **bình thường**: giữ nguyên, không xoá, không chạy lại.

---

## BƯỚC 3 — Kiểm đủ file rồi đẩy lên git (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
echo "WAV: $(ls assets/voice_ref_voxcpm2_dc2/*.wav | wc -l)  (phai = 32)"
echo "TXT: $(ls assets/voice_ref_voxcpm2_dc2/*.txt | wc -l)  (phai = 32)"
test -f assets/voice_ref_voxcpm2_dc2/refs.json && echo "REFS OK"
git add assets/voice_ref_voxcpm2_dc2
echo "WAV da add: $(git diff --cached --name-only | grep -c '\.wav$')  (phai = 32)"
git commit -m "feat(audio): vong 2 - 32 take ung vien VoxCPM2 cho D + C"
git push
git fetch && git status -sb | head -1
```

**Hoàn thành khi và chỉ khi:**
- `WAV: 32`, `TXT: 32`, `REFS OK`, `WAV da add: 32`
- **Dòng cuối là `## main...origin/main`, KHÔNG có chữ `ahead`.**
  Có `ahead` nghĩa là **chưa đẩy lên được**: chạy `git pull --rebase && git push` rồi kiểm lại.

⚠ Nếu `WAV da add` < 32 → **không commit**, dán output vào báo cáo.

---

## BƯỚC 4 — Dán báo cáo này (điền vào chỗ `...`)

```
VONG 2 — KET QUA
Buoc 1: <4 dong OK? dan output>
Buoc 2: chay xong sau ... phut, co loi khong: ...
Bang ket qua (dan NGUYEN VAN phan tu dong "XONG:" den het, trong .work/voxcpm_dc2_run.log):
...
Buoc 3: WAV=... TXT=... WAV da add=...
Commit: <hash>   Dong cuoi git status: <dan nguyen van>
```

---

## Cấm (đọc kỹ)

| Không làm | Vì sao |
|---|---|
| Sửa / sinh lại `assets/voice_ref_voxcpm2_dc/` (vòng 1) | đã đo xong, là dữ liệu so sánh |
| Sửa script, manifest, `.gitignore` | phía Windows quản lý |
| Xoá take lệch cao độ, chọn "take tốt nhất" | Windows phải đo cả take lệch |
| Chỉnh cao độ bằng phần mềm (sox, PSOLA, pitch shift) | làm Higgs đọc sai chữ (đã chứng minh) |
| Báo "xong" khi chưa thấy dòng git **không có `ahead`** | lần trước file không tới được phía Windows |
