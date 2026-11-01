# -*- coding: utf-8 -*-
"""Them bai hoc A11 #68 (T05, 01/11/2026) vao TIEU_CHUAN_DUNG_VIDEO.md."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\00_TIEU_CHUAN\TIEU_CHUAN_DUNG_VIDEO.md")
lines = p.read_text(encoding="utf-8").splitlines()

row68 = (
    "| 68 | **Báo cáo G10 ghi sai tên giọng sau khi đổi engine TTS** (Tập 05, 01/11/2026): "
    "`voice_role_check.py` in nhãn vai bằng `ED.CAST[role][0]` — tức tên giọng **MiniMax** "
    "(`English_CaptivatingStoryteller`, `Korean_ColdYoungMan`…) — trong khi audio đã chạy "
    "**Higgs Audio v3** với file tham chiếu `H.wav / D3_SH.wav / C2_AB03.wav / W6_LOW.wav / W5_HIGH.wav` "
    "⇒ báo cáo nói sai giọng thật đã dùng để dựng. Lưu ý: `tts_manifest_tXX.json` **không có** field `ref_wav` "
    "(chỉ có `voice` kiểu MiniMax); `ref_wav` nằm ở `higgs_selection_tXX.json` | "
    "Nhãn giọng phải lấy từ **nguồn audio thật của tập**: đọc `ref_wav` trong `higgs_selection_tXX.json` "
    "(tệp chỉ tồn tại ở tập đã chạy Higgs) ⇒ in `` `H.wav` (Higgs Audio v3) ``; tập không có tệp này "
    "(MiniMax) thì giữ nguyên `ED.CAST[role][0]`. **Sửa script dùng chung ⇒ phải kiểm hồi quy Tập 01** (L9): "
    "chạy `_verify_voice_label.py` trên các tổ hợp (vi/en × tập 01–07) và chứng minh nhãn Tập 01 **không đổi**; "
    "báo cáo đang tồn tại của tập khác sửa tay bằng đúng logic của script đã vá, **không** sửa tay lệch logic |"
)

idx = next(i for i, l in enumerate(lines) if l.startswith("| 67 |"))
lines.insert(idx + 1, row68)
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("da them A11 #68 tai dong", idx + 2)
