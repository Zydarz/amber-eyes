# VIỆC CẦN LÀM TRÊN MAC — BỘ GIỌNG MẪU TIẾNG ANH THEO SEED BỘ VIỆT (en2)

**Bạn (AI trên Mac) chỉ làm đúng 4 bước dưới đây. Không làm gì khác.**
Không sửa file nào. Không chọn take. Không xoá gì. Không đụng các thư mục giọng mẫu cũ.
Việc của bạn: **kiểm seed → sinh file → đẩy lên git → dán báo cáo.**

---

## Vì sao có lượt này (đọc 30 giây)

Bản tiếng Anh sẽ đọc bằng Higgs, nên cần giọng mẫu **đọc lời tiếng Anh** nhưng **giữ danh tính** 5 giọng Việt đã chốt (người dùng quyết định 31/10/2026).
Bộ `assets/voice_ref_voxcpm2_en/` cũ (30/10) **không dùng**: nó sinh trước vòng D/C mới, nên D và C là người khác.

Lượt này lấy **nguyên câu mô tả + seed** của từng giọng Việt đã chốt, chỉ thay lời đọc bằng tiếng Anh:

| Vai | Giọng Việt đã chốt | Seed (cfg) | Seed dự phòng |
|---|---|---|---|
| H | `H.wav` | 42 (2.0) — **suy ra**, cần xác nhận ở bước 1 | 101, 2024 |
| D | `D_NEW_subbass-husky_t02` | 7 (2.0) — đã ghi | 42 |
| C | `C_NEW_alto-brisk_t03` | 77 (2.0) — đã ghi | 42 |
| W5_HIGH | `W5_HIGH_soprano_take01` | 2024 (2.0) — **suy ra** | 42 |
| W6_LOW | `W6_LOW_low_take05` | 999 (2.5) — **suy ra** | 42 |

Mỗi seed chạy 2 kiểu câu mô tả: `vnctrl` (nguyên văn, có "Vietnamese Standard") và `enctrl` (đổi thành "English Standard").
Tổng **22 take**. Phía Windows sẽ đo và chọn. **Bạn không cần chọn.**

---

## BƯỚC 1 — Chuẩn bị + xác nhận seed (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
git checkout main
git pull
test -f .work/voxcpm_refs_manifest_en2.json && echo "MANIFEST OK" || echo "THIEU MANIFEST"
grep -q "voice_ref_voxcpm2_en2" .gitignore && echo "GITIGNORE OK" || echo "THIEU GITIGNORE"
grep -q 'data.get("takes")' .work/voxcpm_generate_g9.py && echo "SCRIPT OK" || echo "SCRIPT CU"
test -d assets/voice_ref_voxcpm2_en2 && echo "!! THU MUC DA TON TAI" || echo "THU MUC SACH"
echo "--- seed that cua giong VN (de doi chieu, KHONG sua gi) ---"
for r in H W5_HIGH W6_LOW; do
  f=.work/voxcpm_raw/$r/takes.json
  if [ -f "$f" ]; then
    python3 -c "import json,sys;[print('$r',t.get('take'),'seed',t.get('seed'),'cfg',t.get('cfg')) for t in json.load(open('$f'))]"
  else echo "$r: KHONG CO $f"; fi
done
```

**Phải thấy đủ 4 dòng:** `MANIFEST OK` · `GITIGNORE OK` · `SCRIPT OK` · `THU MUC SACH`.
Thiếu bất kỳ dòng nào → **DỪNG**, dán output vào báo cáo (bước 4), không làm tiếp.
Phần "seed that" **chỉ để báo cáo** — dù seed khác bảng trên vẫn chạy tiếp bước 2, không sửa manifest.

---

## BƯỚC 2 — Sinh 22 take (copy nguyên khối, chạy, chờ ~25–40 phút)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py \
  --manifest .work/voxcpm_refs_manifest_en2.json \
  --out assets/voice_ref_voxcpm2_en2 \
  --candidates 1 \
  2>&1 | tee .work/voxcpm_en2_run.log
```

`--candidates 1` chỉ để bật chế độ ứng viên; seed lấy từ khoá `takes` của từng vai trong manifest. **Không** thêm `--seeds`.
Số take = H 3×2 + D 2×2 + C 2×2 + W5 2×2 + W6 2×2 = **22**. **Để chạy hết, không ngắt.**
Take bị đánh dấu `!!` (lệch cao độ / thời lượng) là **bình thường**: giữ nguyên, không xoá, không chạy lại.

---

## BƯỚC 3 — Kiểm đủ file rồi đẩy lên git (copy nguyên khối, chạy)

```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
echo "WAV: $(ls assets/voice_ref_voxcpm2_en2/*.wav | wc -l)  (phai = 22)"
echo "TXT: $(ls assets/voice_ref_voxcpm2_en2/*.txt | wc -l)  (phai = 22)"
test -f assets/voice_ref_voxcpm2_en2/refs.json && echo "REFS OK"
git add assets/voice_ref_voxcpm2_en2 .work/voxcpm_en2_run.log
echo "WAV da add: $(git diff --cached --name-only | grep -c '\.wav$')  (phai = 22)"
git commit -m "feat(audio): bo giong mau EN theo seed bo VN - 22 take VoxCPM2 (en2)"
git push
git fetch && git status -sb | head -1
```

**Hoàn thành khi và chỉ khi:**
- `WAV: 22`, `TXT: 22`, `REFS OK`, `WAV da add: 22`
- **Dòng cuối là `## main...origin/main`, KHÔNG có chữ `ahead`.**
  Có `ahead` nghĩa là **chưa đẩy lên được**: chạy `git pull --rebase && git push` rồi kiểm lại.

⚠ Nếu `WAV da add` < 22 → **không commit**, dán output vào báo cáo.

---

## BƯỚC 4 — Dán báo cáo này (điền vào chỗ `...`)

```
EN2 — KET QUA
Buoc 1: <4 dong OK? dan output, KE CA phan "seed that">
Buoc 2: chay xong sau ... phut, co loi khong: ...
Bang ket qua (dan NGUYEN VAN tu dong "XONG:" den het, trong .work/voxcpm_en2_run.log):
...
So take [TRONG DAI] (khong co "!!"): .../22
Buoc 3: WAV=... TXT=... WAV da add=...
Commit: <hash>   Dong cuoi git status: <dan nguyen van>
```

---

## Cấm (đọc kỹ)

| Không làm | Vì sao |
|---|---|
| Sửa / sinh lại `voice_ref_voxcpm2`, `_dc`, `_dc2`, `_dc3`, `_g9`, `_en` | là giọng đã chốt hoặc dữ liệu so sánh |
| Chép take EN vào thư mục giọng Việt hoặc `.work/kaggle_higgs/dataset_voxcpm2/`, đổi tên thành `H.wav`, `C.wav`… | bộ EN và bộ VN **tách riêng hoàn toàn** — chép vào sẽ ghi đè giọng Việt đã chốt (Higgs §4.4) |
| Sửa script, manifest, `.gitignore` (kể cả khi seed bước 1 khác bảng) | phía Windows quản lý |
| Xoá take lệch, chọn "take tốt nhất" | Windows phải đo cả take lệch |
| Chỉnh cao độ bằng phần mềm (sox, PSOLA, pitch shift) | làm Higgs đọc sai chữ (đã chứng minh) |
| Báo "xong" khi chưa thấy dòng git **không có `ahead`** | file phải tới được phía Windows |
