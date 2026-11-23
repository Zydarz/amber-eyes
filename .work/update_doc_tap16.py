import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with open(ROOT / ".work" / "bg_jobs_tap16.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

lines = []
lines.append('# DANH SÁCH ẢNH NỀN — TẬP 16 "JOHN_LIST" (FLUX.2 DEEP NOIR 2K)')
lines.append('')
lines.append('*Hồ sơ John List — Westfield, New Jersey. Cập nhật ngày 2026-11-15.*')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## B1. Thông tin bộ ảnh')
lines.append('')
lines.append('| Mục | Nội dung |')
lines.append('|---|---|')
lines.append(f'| Số ảnh chuẩn hóa | **{len(jobs)}** ảnh phục vụ trọn vẹn 5 hồi (chuẩn ~3.1 câu/ảnh, 0 lặp nền) |')
lines.append('| Kích thước chuẩn | 2112×1188 (16:9 2K), lưu trữ tại `assets/bg/` |')
lines.append('| Vị trí lưu trữ | `assets/bg/t16_*.png` — **tiền tố `t16_` bắt buộc** |')
lines.append('| Danh sách prompt gốc | `.work/bg_jobs_tap16.json` |')
lines.append('| Sổ nguồn gốc tài sản | `provenance.json` (đạt 100% kiểm tra thương mại) |')
lines.append('| Công nghệ sinh ảnh | Kaggle GPU Multi-T4 (`black-forest-labs/FLUX.2-klein-4B`) |')
lines.append('| Tiêu chuẩn kỹ thuật | `QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` v1.0 (Deep Noir Chiaroscuro) |')
lines.append('| Hậu kỳ đồ họa | Color grading dìm màu (sat 0.65, contrast 1.15) + Noir Vignette + Film Grain 35mm |')
lines.append('')
lines.append('## B2. Chi tiết 5 Hồi')
lines.append('')

for a in range(1, 6):
    act_jobs = [j for j in jobs if j.get('act') == a]
    lines.append(f'### Hồi {a} ({len(act_jobs)} ảnh)')
    for j in act_jobs:
        d = j.get('desc', '').replace('\n', ' ')
        lines.append(f'- `{j["name"]}`: {d[:120]}...')
    lines.append('')

out_path = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap16" / "Danh_Sach_Anh_Tap16.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write('\n'.join(lines))

print(f"Updated {out_path} successfully with {len(jobs)} images!")
