# VIỆC CẦN LÀM TRÊN MAC — BỘ GIỌNG MẪU TIẾNG HÀN THEO SEED BỘ VIỆT (ko2)

**Bạn (AI trên Mac) chỉ làm đúng 4 bước dưới đây. Không làm gì khác.**
Không sửa file nào. Không chọn take. Không xoá gì. Không đụng các thư mục giọng mẫu cũ.
Việc của bạn: **kiểm môi trường → sinh file → đẩy lên git → dán báo cáo.**

---

## Vì sao có lượt này (đọc 30 giây)

Tập 02 tiếng Hàn sẽ đọc bằng Higgs, nên cần giọng mẫu **đọc lời tiếng Hàn** nhưng **giữ danh tính** 5 giọng Việt đã chốt.
Bộ `assets/voice_ref_voxcpm2_ko/` cũ (30/10) **không dùng**: H 121 Hz và D 135 Hz chỉ cách nhau ~1,9 nửa cung (cần ≥ 4), và bộ này sinh trước vòng D/C mới. Phía Windows cũng không có file `.wav` của bộ cũ, chỉ có `.txt`.

Lượt này làm giống hệt lượt en2: lấy **nguyên câu mô tả + seed** của từng giọng Việt, lời đọc là tiếng Hàn (lấy lại từ `.txt` của bộ `ko` cũ).
Mỗi seed chạy 2 kiểu câu mô tả: `vnctrl_ko` (nguyên văn, có "Vietnamese Standard") và `koctrl` (đổi thành "Korean Standard").
Tag khác với en2 (`vnctrl`/`enctrl`) và ja2 (`vnctrl_ja`/`jactrl`), nên file thô trong `.work/voxcpm_raw/` **không đè** file của hai lượt đó.

| Vai | Giọng Việt đã chốt | Seed (cfg) | Số take |
|---|---|---|---:|
| H | `H.wav` | 42, 101, 2024 (2.0) | 3 × 2 = 6 |
| D | `D3_SH` (subbass-husky) | 7, 42, 101, 2024 (2.0). Thêm 2 seed vì en2 không có D nào trong dải | 4 × 2 = 8 |
| C | `C2_AB03` (alto-brisk) | 77, 42 (2.0) | 2 × 2 = 4 |
| W5_HIGH (N2) | `W5_HIGH` | 2024, 42 (2.0) | 2 × 2 = 4 |
| W6_LOW (N1) | `W6_LOW` | 999 (2.5), 42 (2.0) | 2 × 2 = 4 |

Tổng **26 take**. Phía Windows sẽ đo và chọn. **Bạn không cần chọn.**

---

## BƯỚC 1 — Chuẩn bị (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git checkout main
git pull
test -f .work/voxcpm_refs_manifest_ko2.json && echo "MANIFEST OK" || echo "THIEU MANIFEST"
grep -q "voice_ref_voxcpm2_ko2" .gitignore && echo "GITIGNORE OK" || echo "THIEU GITIGNORE"
grep -q 'data.get("takes")' .work/voxcpm_generate_g9.py && echo "SCRIPT OK" || echo "SCRIPT CU"
test -d assets/voice_ref_voxcpm2_ko2 && echo "!! THU MUC DA TON TAI" || echo "THU MUC SACH"
python3 -c "import json;d=json.load(open('.work/voxcpm_refs_manifest_ko2.json',encoding='utf-8'));print('TAKE:',sum(len(v['takes'])*len(v['control_variants']) for v in d.values()))"
```

**Phải thấy đủ 5 dòng:** `MANIFEST OK` · `GITIGNORE OK` · `SCRIPT OK` · `THU MUC SACH` · `TAKE: 26`.
Thiếu bất kỳ dòng nào → **DỪNG**, dán output vào báo cáo (bước 4), không làm tiếp.

---

## BƯỚC 2 — Sinh 26 take (copy nguyên khối, chạy, chờ ~30–50 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
  --manifest .work/voxcpm_refs_manifest_ko2.json \
  --out assets/voice_ref_voxcpm2_ko2 \
  --candidates 1 \
  2>&1 | tee .work/voxcpm_ko2_run.log
```

`--candidates 1` chỉ để bật chế độ ứng viên; seed lấy từ khoá `takes` trong manifest. **Không** thêm `--seeds`.
**Để chạy hết, không ngắt.**
Take bị đánh dấu `!!` (lệch cao độ / thời lượng) là **bình thường**: giữ nguyên, không xoá, không chạy lại.
Cột "am/s" đếm theo dấu cách nên không phải số âm tiết tiếng Hàn. Đây là **bình thường**, bỏ qua.

---

## BƯỚC 3 — Kiểm đủ file rồi đẩy lên git (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
echo "WAV: $(ls assets/voice_ref_voxcpm2_ko2/*.wav | wc -l)  (phai = 26)"
echo "TXT: $(ls assets/voice_ref_voxcpm2_ko2/*.txt | wc -l)  (phai = 26)"
test -f assets/voice_ref_voxcpm2_ko2/refs.json && echo "REFS OK"
git add assets/voice_ref_voxcpm2_ko2
git add -f .work/voxcpm_ko2_run.log   # .work/ bi gitignore -> bat buoc -f
echo "WAV da add: $(git diff --cached --name-only | grep -c '\.wav$')  (phai = 26)"
git commit -m "feat(audio): bo giong mau KO theo seed bo VN - 26 take VoxCPM2 (ko2)"
git push
git fetch && git status -sb | head -1
```

**Hoàn thành khi và chỉ khi:**
- `WAV: 26`, `TXT: 26`, `REFS OK`, `WAV da add: 26`
- **Dòng cuối là `## main...origin/main`, KHÔNG có chữ `ahead`.**
  Có `ahead` nghĩa là **chưa đẩy lên được**: chạy `git pull --rebase && git push` rồi kiểm lại.

⚠ Nếu `WAV da add` < 26 → **không commit**, dán output vào báo cáo.

---

## BƯỚC 4 — Dán báo cáo này (điền vào chỗ `...`)

```
KO2 — KET QUA
Buoc 1: <5 dong OK? dan output>
Buoc 2: chay xong sau ... phut, co loi khong: ...
Bang ket qua (dan NGUYEN VAN moi dong "  > ..." trong .work/voxcpm_ko2_run.log):
...
So take [TRONG DAI] (khong co "!!"): .../26
Buoc 3: WAV=... TXT=... WAV da add=...
Commit: <hash>   Dong cuoi git status: <dan nguyen van>
```

---

## Cấm (đọc kỹ)

| Không làm | Vì sao |
|---|---|
| Sửa / sinh lại `voice_ref_voxcpm2`, `_dc`, `_dc2`, `_dc3`, `_g9`, `_en`, `_en2`, `_ja`, `_ja2`, `_ko` | là giọng đã chốt hoặc dữ liệu so sánh |
| Chép take KO vào thư mục giọng Việt/Anh, vào `.work/kaggle_higgs/dataset_voxcpm2*/`, hoặc đổi tên thành `H.wav`, `C.wav`… | mỗi ngôn ngữ một bộ **tách riêng hoàn toàn**, chép vào sẽ ghi đè giọng đã chốt (Higgs §4.4) |
| Sửa script, manifest, `.gitignore` | phía Windows quản lý |
| Xoá take lệch, chọn "take tốt nhất" | Windows phải đo cả take lệch |
| Chỉnh cao độ bằng phần mềm (sox, PSOLA, pitch shift) | làm Higgs đọc sai chữ (đã chứng minh) |
| Báo "xong" khi chưa thấy dòng git **không có `ahead`** | file phải tới được phía Windows |
