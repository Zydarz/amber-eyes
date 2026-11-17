# -*- coding: utf-8 -*-
"""Ghi 5 bẫy mới (Tập 11, 16/11/2026) vào TIEU_CHUAN_DUNG_VIDEO.md mục A11 + cập nhật AGENTS.md H25."""
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
STD = ROOT / "00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md"
AG = ROOT / "AGENTS.md"

ROWS = [
    "| 165 | **Ước lượng “số nền cần = ceil(tot/2)” BỎ QUA cả ràng buộc 30 s và vế “liền mạch” của H25 ⇒ số ảnh thiếu luôn thấp hơn thật.** Tập 11 (16/11/2026): 223 shot / 66 nền cũ = 3,4 shot/nền, **24 nền vượt H22**. Công thức `ceil(223/2)=112` cho ra “thiếu 46 ảnh”, nhưng khi tách theo **cụm liền mạch** (cùng mã nền dùng lại ở hồi khác = cảnh khác ⇒ phải tách mã) và **≤ 30 s/nhóm**, số nền thật là **136 ⇒ thiếu 70 ảnh** | Ước lượng phải **đo bằng script trên bảng shot**, đừng dùng công thức. Tập 11: 223 shot → **135 nhóm** (cụm liền mạch, ≤ 2 shot/nhóm, ≤ 30 s) + **1 nền riêng cho thẻ kết** (T2) = **136 nền · 1,64 shot/nền · 0 vi phạm H22 ở cả VI/EN/JA** · 70 ảnh mới. Công cụ: `.work/_t11_apply_split.py --plan/--apply` (tách + ghi bảng shot 3 ngôn ngữ) |",
    "| 166 | **Cổng `--plan` GÁN thẻ chuyển hồi (`void`) vào nền TRƯỚC (+1 shot, +2 s) — nền ngay trước thẻ phải còn headroom.** Tập 11 (16/11/2026): `qc_bg_usage.plan_check` chỉ đổi `cur` khi dòng có mã `t\\d+_[a-z0-9_]+`; dòng thẻ mang `void` nên `cur` giữ nguyên ⇒ **2 s của thẻ cộng vào nền trước**. Nền 2 shot/17 s sát thẻ → 3 shot/19 s vẫn ĐẠT, nhưng nền 2 shot/29 s sát thẻ sẽ **vượt 30 s** dù bảng shot trông hợp lệ | Khi lập kế hoạch tách: mọi nhóm **đứng trước** một thẻ chuyển hồi phải có **≤ 2 shot** và **≤ 28 s**. Cột “Nền + bóng” của thẻ **để nguyên `void`** (không đổi sang mã thật) |",
    "| 167 | **Ảnh nền đi qua Real-ESRGAN bị CẤM (`QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` §1.2) ⇒ phải gỡ ở **3 nơi**: jobs + `provenance.json` + file trên đĩa.** Tập 11 (16/11/2026): 4 file `t11_*` có bản ghi Real-ESRGAN; 2 file không shot nào dùng (`t11_battered_woman_syndrome_file`, `t11_toxic_devotion_cruelty`) ⇒ cổng H22 ① báo “ảnh sinh không dùng = 4”; 2 file kia (`t11_fragile_beauty_manipulation`, `t11_obedient_accomplice_strings`) tái dùng được cho nhóm mới | (1) `bg_jobs_tapXX.json` — xoá job; (2) `provenance.json` — xoá dòng; (3) `assets/bg/` — **xoá file** sau khi sao lưu `.work/_cu/` (không để nằm thừa). File được tái dùng cho nhóm mới thì **sinh lại qua đúng pipeline** (không upscaler) để ghi đè bản cũ |",
    "| 168 | **Một mã nền có thể trải qua 2 hồi (vd `4.11#6` + `5.02#1`) ⇒ khi thống kê “số nền theo hồi” phải đếm DISTINCT toàn cục, không cộng theo từng hồi.** Tập 11 (16/11/2026): tài liệu báo “137 ảnh” trong khi cổng đo **136** | Đếm distinct toàn cục rồi mới gán mỗi mã về hồi của shot **ĐẦU TIÊN** nó xuất hiện |",
    "| 169 | **Sinh ảnh hàng loạt trên Kaggle: PATCH khuôn `make_nb_tapXX_parallel.py` thay vì viết lại notebook từ đầu.** Tập 11 (16/11/2026): sinh **70 ảnh mới** bằng `.work/kaggle_flux/make_nb_tap11_new70.py` — tạo file jobs tạm chỉ gồm ảnh cần sinh → patch **2 dòng** trong khuôn (đổi `JOBS_FILE` + tiền tố zip) → `exec` ⇒ giữ nguyên pipeline 2 GPU staggered chống OOM (A11 #159), không rủi ro gõ lại 270 dòng sai pipeline | Khuôn dùng cho mọi đợt sinh bổ sung: `make_nb_tapXX_<số ảnh>.py`; watcher đồng bộ: `watch_and_sync_tapXX.py` (tải zip → giải nén → `assets/bg/` → cập nhật `provenance.json`) |",
]

t = STD.read_text(encoding="utf-8")
i = t.find("## A11")
lines = t[i:].split("\n")
# chèn ngay sau dòng bảng cuối cùng (row 164) — dòng trống kế tiếp
j = 0
for n, l in enumerate(lines):
    if l.startswith("| 164"):
        j = n
        break
new = lines[:j + 1] + ROWS + lines[j + 1:]
STD.write_text(t[:i] + "\n".join(new), encoding="utf-8")
print(f"A11: đã thêm {len(ROWS)} mục (165–169) sau dòng 164")

# ---- AGENTS.md: cập nhật bằng chứng của H25 ----
a = AG.read_text(encoding="utf-8")
old_tail = ("Đo 16/11/2026 bằng `--plan`: kế hoạch Tập 10 = 71 nền/244 shot (thiếu ≥ 38), "
            "Tập 11 = 66/223 (thiếu ≥ 32, 4 job thừa), Tập 12 = 79/254 (thiếu ≥ 27, 4 job thừa, "
            "bảng shot không ghi thời lượng ⇒ không đo được 30 s). Nguyên nhân gốc: danh sách ảnh được lập "
            "**cố định ~70 cảnh** rồi bảng shot gán lặp cho đủ")
new_tail = (old_tail +
            ". **Tập 11 đã áp dụng H25 (16/11/2026):** 66 nền/223 shot (3,4 shot/nền) → tách theo **cụm liền mạch** "
            "(≤ 2 shot/nhóm, ≤ 30 s; nền trước thẻ chuyển hồi ≤ 28 s) + nền riêng cho thẻ kết ⇒ **136 nền · "
            "1,64 shot/nền · 0 vi phạm H22 ở cả VI/EN/JA** (`qc_bg_usage.py --plan` ĐẠT) ⇒ **70 ảnh mới** "
            "(3 mã cũ tái dùng, 2 ảnh thừa Real-ESRGAN đã gỡ khỏi jobs + provenance + đĩa). "
            "**Ước lượng `ceil(tot/2)` SAI** — phải đo bằng script (TIEU_CHUAN A11 #165–169)")
if old_tail in a:
    a = a.replace(old_tail, new_tail)
    AG.write_text(a, encoding="utf-8")
    print("AGENTS.md: đã cập nhật bằng chứng H25 (Tập 11)")
else:
    print("AGENTS.md: KHÔNG tìm thấy đoạn cần cập nhật — kiểm tra lại")
