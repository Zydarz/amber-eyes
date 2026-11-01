# VIỆC CẦN LÀM TRÊN MAC — VÒNG 4 TIẾNG HÀN: CHỈ VAI D (ko4)

**Bạn (AI trên Mac) chỉ làm đúng 4 bước dưới đây. Không làm gì khác.**
Không sửa file nào. Không chọn take. Không xoá gì. Không đụng các thư mục giọng mẫu cũ.

---

## Vì sao có lượt này (đọc 30 giây)

Tiếng Hàn đã có H, C, N1, N2. **Chỉ còn thiếu Điều tra viên (D)**: qua 24 take (ko2 + ko3), không take nào xuống dưới 101 Hz; cần 78–88 Hz để không trùng giọng Host khi Higgs đọc.
VoxCPM2 tất định: cùng câu mô tả + seed ⇒ ra y hệt lần trước. Nên lượt này dùng **8 seed mới**, 2 câu mô tả tốt nhất của vòng 3 và 2 câu mô tả mới trầm hơn.

| Câu mô tả | Seed (cfg 2.0) | Take |
|---|---|---:|
| `smokerbass`, `bassgravel` (vòng 3), `oldbass`, `basso` (mới) | 3, 11, 99, 256, 500, 888, 2025, 4096 | 4 × 8 = 32 |

Tag mang đuôi `_ko4`, không đè file thô lượt trước. Phía Windows đo và chọn. **Bạn không cần chọn.**

---

## BƯỚC 1 — Chuẩn bị (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git checkout main
git pull
test -f .work/voxcpm_refs_manifest_ko4.json && echo "MANIFEST OK" || echo "THIEU MANIFEST"
grep -q "voice_ref_voxcpm2_ko4" .gitignore && echo "GITIGNORE OK" || echo "THIEU GITIGNORE"
grep -q 'data.get("takes")' .work/voxcpm_generate_g9.py && echo "SCRIPT OK" || echo "SCRIPT CU"
test -d assets/voice_ref_voxcpm2_ko4 && echo "!! THU MUC DA TON TAI" || echo "THU MUC SACH"
python3 -c "import json;d=json.load(open('.work/voxcpm_refs_manifest_ko4.json',encoding='utf-8'));print('TAKE:',sum(len(v['takes'])*len(v['control_variants']) for v in d.values()))"
```

**Phải thấy đủ 5 dòng:** `MANIFEST OK` · `GITIGNORE OK` · `SCRIPT OK` · `THU MUC SACH` · `TAKE: 32`.
Thiếu dòng nào → **DỪNG**, dán output vào báo cáo (bước 4).

---

## BƯỚC 2 — Sinh 32 take (copy nguyên khối, chạy, chờ ~40–65 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
  --manifest .work/voxcpm_refs_manifest_ko4.json \
  --out assets/voice_ref_voxcpm2_ko4 \
  --candidates 1 \
  2>&1 | tee .work/voxcpm_ko4_run.log
```

**Không** thêm `--seeds`. Để chạy hết, không ngắt. Take có `!!` là **bình thường**: giữ nguyên.

---

## BƯỚC 3 — Kiểm đủ file rồi đẩy lên git (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
echo "WAV: $(ls assets/voice_ref_voxcpm2_ko4/*.wav | wc -l)  TXT: $(ls assets/voice_ref_voxcpm2_ko4/*.txt | wc -l)  (phai = 32 / 32)"
test -f assets/voice_ref_voxcpm2_ko4/refs.json && echo "REFS OK"
git add assets/voice_ref_voxcpm2_ko4
git add -f .work/voxcpm_ko4_run.log   # .work/ bi gitignore -> bat buoc -f
echo "WAV da add: $(git diff --cached --name-only | grep -c '\.wav$')  (phai = 32)"
git commit -m "feat(audio): vong 4 giong mau KO - vai D (ko4 32 take VoxCPM2)"
git push
git fetch && git status -sb | head -1
```

**Hoàn thành khi và chỉ khi:** `WAV: 32 TXT: 32`, `REFS OK`, `WAV da add: 32`, và **dòng cuối là `## main...origin/main`, KHÔNG có `ahead`** (có `ahead` → `git pull --rebase && git push` rồi kiểm lại).
⚠ `WAV da add` < 32 → **không commit**, dán output vào báo cáo.

---

## BƯỚC 4 — Dán báo cáo này

```
KO4 — KET QUA
Buoc 1: <5 dong OK? dan output>
Buoc 2: chay xong sau ... phut, co loi khong: ...
So take [TRONG DAI] (khong co "!!"): .../32
Buoc 3: WAV=... TXT=... WAV da add=...
Commit: <hash>   Dong cuoi git status: <dan nguyen van>
```

---

## Cấm

| Không làm | Vì sao |
|---|---|
| Sửa / sinh lại mọi thư mục `assets/voice_ref_voxcpm2*` khác | là giọng đã chốt hoặc dữ liệu so sánh |
| Chép take sang thư mục / dataset khác, đổi tên thành `D.wav`… | mỗi ngôn ngữ một bộ tách riêng (Higgs §4.4) |
| Sửa script, manifest, `.gitignore` | phía Windows quản lý |
| Xoá take lệch, chọn "take tốt nhất" | Windows phải đo cả take lệch |
| Chỉnh cao độ bằng phần mềm (sox, PSOLA, pitch shift) | làm Higgs đọc sai chữ (đã chứng minh) |
| Báo "xong" khi git còn `ahead` | file phải tới được phía Windows |
