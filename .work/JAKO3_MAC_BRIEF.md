# VIỆC CẦN LÀM TRÊN MAC — VÒNG 3 GIỌNG MẪU TIẾNG NHẬT + TIẾNG HÀN (ja3, ko3): VAI D, C, N1

**Bạn (AI trên Mac) chỉ làm đúng 5 bước dưới đây. Không làm gì khác.**
Không sửa file nào. Không chọn take. Không xoá gì. Không đụng các thư mục giọng mẫu cũ.
Việc của bạn: **kiểm môi trường → sinh JA → sinh KO → đẩy lên git → dán báo cáo.**

---

## Vì sao có lượt này (đọc 30 giây)

Lượt ja2/ko2 (31/10) đã đo xong (`90_LUU_TRU/BaoCao_DoGiongMau_JA2_KO2_20261101.md`): **H và N2 đạt**, nhưng **D, C, N1 trượt** ở cả hai ngôn ngữ. Đọc tiếng Nhật/Hàn, VoxCPM2 cho giọng **cao hơn** bản Việt:
- D (cần 78–88 Hz): thấp nhất 99 Hz (JA), 114 Hz (KO), trùng giọng Host.
- C (cần 200–218 Hz): ra 242–275 Hz. Take JA duy nhất trong dải dài 29,2 s (quá 28 s).
- N1 (cần 148–182 Hz): ra 195–269 Hz.

Lượt này **chỉ sinh lại 3 vai đó**, với câu mô tả trầm hơn và seed mới. Lời đọc C tiếng Nhật đã bỏ câu cuối để ngắn hơn 28 s.

| Vai | Số câu mô tả | Seed (cfg 2.0) | Take mỗi ngôn ngữ |
|---|---:|---|---:|
| D | 4 (4 câu của vòng dc3) | 7, 42, 777, 1234 | 16 |
| C | 3 (alto / contralto / deep alto) | 7, 42, 777, 1234 | 12 |
| W6_LOW (N1) | 3 (low warm / deep alto / husky contralto) | 7, 42, 777, 1234 | 12 |

Tổng **40 take JA + 40 take KO = 80**. Tag mang đuôi `_ja3` / `_ko3`, nên file thô trong `.work/voxcpm_raw/` **không đè** lượt trước. Phía Windows sẽ đo và chọn. **Bạn không cần chọn.**

---

## BƯỚC 1 — Chuẩn bị (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git checkout main
git pull
for L in ja3 ko3; do
  test -f .work/voxcpm_refs_manifest_$L.json && echo "MANIFEST $L OK" || echo "THIEU MANIFEST $L"
  grep -q "voice_ref_voxcpm2_$L" .gitignore && echo "GITIGNORE $L OK" || echo "THIEU GITIGNORE $L"
  test -d assets/voice_ref_voxcpm2_$L && echo "!! THU MUC $L DA TON TAI" || echo "THU MUC $L SACH"
  python3 -c "import json;d=json.load(open('.work/voxcpm_refs_manifest_$L.json',encoding='utf-8'));print('TAKE $L:',sum(len(v['takes'])*len(v['control_variants']) for v in d.values()))"
done
grep -q 'data.get("takes")' .work/voxcpm_generate_g9.py && echo "SCRIPT OK" || echo "SCRIPT CU"
```

**Phải thấy đủ 9 dòng:** `MANIFEST ja3 OK` · `GITIGNORE ja3 OK` · `THU MUC ja3 SACH` · `TAKE ja3: 40` · bốn dòng tương tự cho `ko3` · `SCRIPT OK`.
Thiếu bất kỳ dòng nào → **DỪNG**, dán output vào báo cáo (bước 5), không làm tiếp.

---

## BƯỚC 2 — Sinh 40 take tiếng Nhật (copy nguyên khối, chạy, chờ ~50–80 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
  --manifest .work/voxcpm_refs_manifest_ja3.json \
  --out assets/voice_ref_voxcpm2_ja3 \
  --candidates 1 \
  2>&1 | tee .work/voxcpm_ja3_run.log
```

## BƯỚC 3 — Sinh 40 take tiếng Hàn (chạy SAU khi bước 2 xong hẳn, ~50–80 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
  --manifest .work/voxcpm_refs_manifest_ko3.json \
  --out assets/voice_ref_voxcpm2_ko3 \
  --candidates 1 \
  2>&1 | tee .work/voxcpm_ko3_run.log
```

Cho cả bước 2 và 3:
- `--candidates 1` chỉ để bật chế độ ứng viên; seed lấy từ manifest. **Không** thêm `--seeds`.
- **Không chạy hai bước cùng lúc.** Để chạy hết, không ngắt.
- Take có `!!` (lệch cao độ / thời lượng) là **bình thường**: giữ nguyên, không xoá, không chạy lại.
- Cột "am/s" không đúng với tiếng Nhật/Hàn. Bỏ qua.

---

## BƯỚC 4 — Kiểm đủ file rồi đẩy lên git (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
for L in ja3 ko3; do
  echo "$L WAV: $(ls assets/voice_ref_voxcpm2_$L/*.wav | wc -l)  TXT: $(ls assets/voice_ref_voxcpm2_$L/*.txt | wc -l)  (phai = 40 / 40)"
  test -f assets/voice_ref_voxcpm2_$L/refs.json && echo "$L REFS OK"
  git add assets/voice_ref_voxcpm2_$L
  git add -f .work/voxcpm_${L}_run.log   # .work/ bi gitignore -> bat buoc -f
done
echo "WAV da add: $(git diff --cached --name-only | grep -c '\.wav$')  (phai = 80)"
git commit -m "feat(audio): vong 3 giong mau JA/KO - D, C, N1 (ja3 40 + ko3 40 take VoxCPM2)"
git push
git fetch && git status -sb | head -1
```

**Hoàn thành khi và chỉ khi:**
- `ja3 WAV: 40 TXT: 40`, `ko3 WAV: 40 TXT: 40`, `ja3 REFS OK`, `ko3 REFS OK`, `WAV da add: 80`
- **Dòng cuối là `## main...origin/main`, KHÔNG có chữ `ahead`.**
  Có `ahead` nghĩa là **chưa đẩy lên được**: chạy `git pull --rebase && git push` rồi kiểm lại.

⚠ Nếu `WAV da add` < 80 → **không commit**, dán output vào báo cáo.

---

## BƯỚC 5 — Dán báo cáo này (điền vào chỗ `...`)

```
JA3/KO3 — KET QUA
Buoc 1: <9 dong OK? dan output>
Buoc 2 (JA): chay xong sau ... phut, co loi khong: ...
Buoc 3 (KO): chay xong sau ... phut, co loi khong: ...
So take [TRONG DAI] (khong co "!!"): JA .../40   KO .../40
Buoc 4: ja3 WAV=... TXT=...  ko3 WAV=... TXT=...  WAV da add=...
Commit: <hash>   Dong cuoi git status: <dan nguyen van>
```

(Không cần dán từng dòng take: log đã nằm trong git.)

---

## Cấm (đọc kỹ)

| Không làm | Vì sao |
|---|---|
| Sửa / sinh lại mọi thư mục `assets/voice_ref_voxcpm2*` khác (`_dc*`, `_g9`, `_en*`, `_ja`, `_ja2`, `_ko`, `_ko2`…) | là giọng đã chốt hoặc dữ liệu so sánh |
| Chép take JA/KO vào thư mục giọng ngôn ngữ khác, vào `.work/kaggle_higgs/dataset_voxcpm2*/`, hoặc đổi tên thành `H.wav`, `C.wav`… | mỗi ngôn ngữ một bộ **tách riêng hoàn toàn** (Higgs §4.4) |
| Sửa script, manifest, `.gitignore` | phía Windows quản lý |
| Xoá take lệch, chọn "take tốt nhất" | Windows phải đo cả take lệch |
| Chỉnh cao độ bằng phần mềm (sox, PSOLA, pitch shift) | làm Higgs đọc sai chữ (đã chứng minh) |
| Báo "xong" khi chưa thấy dòng git **không có `ahead`** | file phải tới được phía Windows |
