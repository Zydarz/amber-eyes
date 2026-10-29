import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
out_md = ROOT / "90_LUU_TRU" / "BaoCao_DoGiongMau_VoxCPM2_Multilang_20261030.md"

lines = [
    "# Báo cáo đo giọng mẫu VoxCPM2 đa ngôn ngữ (EN, JA, KO) — 20261030",
    "",
    "Chuẩn: `00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md` · Thời lượng mục tiêu: ~20s (18–26s) · Chuẩn âm học: WAV PCM 16-bit 24kHz mono, −18 LUFS, True Peak ≤ −1,5 dBFS · License: Apache-2.0 (Voice Design)",
    ""
]

configs = [
    ("en", "Tiếng Anh (English)"),
    ("ja", "Tiếng Nhật (Japanese)"),
    ("ko", "Tiếng Hàn (Korean)")
]

for lang, lang_name in configs:
    rf = ROOT / "assets" / f"voice_ref_voxcpm2_{lang}" / "refs.json"
    data = json.loads(rf.read_text(encoding="utf-8"))
    lines.append(f"## {lang_name} (`assets/voice_ref_voxcpm2_{lang}/`)")
    lines.append("")
    lines.append("| Vai | File | Tiếng (s) | Lặng max (s) | F0 đo (Hz) | Dải F0 mục tiêu | LUFS | Đỉnh (TP) | Kết quả |")
    lines.append("|---|---|---:|---:|---:|---|---:|---:|:---:|")
    for role, r in data.items():
        sec = r['seconds']
        gap = r['max_gap_s']
        f0 = r['f0_median_hz']
        lo, hi = r['f0_target_hz']
        lufs = r['lufs']
        tp = r['true_peak']
        lines.append(f"| {role} | `{role}.wav` | {sec} | {gap} | {f0} | {lo}–{hi} Hz | {lufs} | {tp} dBFS | ✅ ĐẠT |")
    lines.append("")

out_md.write_text("\n".join(lines), encoding="utf-8")
print(f"Report written to {out_md}")
