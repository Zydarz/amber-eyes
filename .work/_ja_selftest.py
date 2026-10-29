#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm chứng các quy tắc cốt lõi của pipeline JA (không gọi LLM).

1. check_sentence: 1 câu VN -> đúng 1 câu JA (đủ/đúng 1 dấu kết câu, cấm …)
2. check_line: dòng n câu -> đúng n câu JA  (bắt được lỗi "dịch cả dòng còn 1 câu")
3. split: tách câu khớp luật parse_kichban, giữ marker cân bằng
4. move: marker ở cuối dòng
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from ja_split import ja_sentences, parts_balanced, split_dialogue_sentences  # noqa: E402

fails = []


def ck(name, cond, detail=""):
    print(("  OK   " if cond else "  FAIL ") + name + (f"   [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


print("== 1. check_sentence ==")
ok, why, _k = M.check_sentence("母を殺しました。", "Tôi đã giết mẹ tôi.")
ck("câu JA hợp lệ", ok, why)
ok, why, _k = M.check_sentence("母を殺しました。母は私ukarhi.", "Tôi đã giết mẹ tôi.")
ck("câu JA có 2 dấu kết câu bị chặn", not ok, why)
ok, why, _k = M.check_sentence("母を殺しました……", "Tôi đã giết mẹ tôi.")
ck("câu JA có … bị chặn", not ok, why)
ok, why, _k = M.check_sentence("母を殺しました", "Tôi đã giết mẹ tôi.")
ck("câu JA không có dấu kết câu bị chặn", not ok, why)
ok, why, _k = M.check_sentence("**母を殺しました。**", "**Tôi đã giết mẹ tôi.**")
ck("marker ** được giữ", ok, why)
ok, why, _k = M.check_sentence("母を殺しました。", "**Tôi đã giết mẹ tôi.**")
ck("mất marker ** bị chặn", not ok, why)

print("\n== 2. check_line (dòng nhiều câu) ==")
vi4 = ("Tôi đã giết mẹ tôi và người bạn của bà. Và tôi đã giết mấy cô nữ sinh đó. "
       "Sáu người. Tôi có thể chỉ cho các anh biết tôi đã chôn những mảnh vụn của họ ở đâu.")
ck("VN dòng này = 4 câu", M.official_counts([vi4])[0] == 4, str(M.official_counts([vi4])[0]))
ok, why, _k = M.check_line("母を殺しました。友人も殺しました。6人だ。遺骸の場所を教えます。", vi4, 4)
ck("dòng JA 4 câu được chấp nhận", ok, why)
ok, why, _k = M.check_line("母と友人を殺した――女子学生たちも殺した、6人だ――遺骸の場所を。", vi4, 4)
ck("dòng JA gộp còn 1 câu bị chặn (lỗi cũ)", not ok, why)
ok, why, _k = M.check_line("母を殺しました。友人も殺しました。6人だ。", vi4, 4)
ck("dòng JA thiếu 1 câu bị chặn", not ok, why)

print("\n== 3. tách câu ==")
p = split_dialogue_sentences("Câu một. Câu hai **đậm**. Câu ba.")
ck("tách 3 câu", len(p) == 3, str(p))
ck("marker cân bằng", parts_balanced(p))
p2 = split_dialogue_sentences("*'Câu một. Câu hai.'*")
ck("dòng có * bao ngoài -> KHÔNG cân bằng => phải rơi về chế độ 'line'",
   not parts_balanced(p2), str(p2))

print("\n== 4. ja_sentences khớp parse_kichban ==")
for s, want in [
    ("母を殺しました。", 1),
    ("母を殺しました。友人も。6人だ。", 3),
    ("*   **第1の徴候: iddy。**", 1),
    ("第1文。**第2文。**", 2),
    ('"第1文。第2文。"', 2),
]:
    got = ja_sentences(s)
    ck(f"ja_sentences({s[:22]!r}) = {want}", got == want, f"được {got}")

print("\n== 5. prompt 'line' có mang n ==")
pr, _ = M.build_prompt([{"id": "u1#L", "vi": vi4, "n": 4}], "line")
ck('prompt chứa "n": 4', '"n": 4' in pr)

print("\n== 6. repair_ja (sửa cơ học) ==")
ck("… -> ――", M.repair_ja("母を殺しました……", "Tôi đã giết mẹ tôi.") == "母を殺しました――",
   M.repair_ja("母を殺しました……", "Tôi đã giết mẹ tôi."))
ck("khôi phục dấu * bị rớt",
   M.repair_ja("*Âm nhạc chuyển sang.", "*Âm nhạc chuyển sang.*") == "*Âm nhạc chuyển sang.*",
   M.repair_ja("*Âm nhạc chuyển sang.", "*Âm nhạc chuyển sang.*"))

print("\n== 7. phân loại lỗi cấu trúc vs chất lượng ==")
ok, why, k = M.check_sentence("母を殺しました。母は私ukarhi.", "Tôi đã giết mẹ tôi.")
ck("sai số dấu kết câu => structure", k == "structure", f"{k} / {why}")
ok, why, k = M.check_sentence("母を殺しました。", "Tôi đã giết mẹ tôi.")
ck("đạt => kind rỗng", ok and k == "", f"{k} / {why}")

print("\n" + ("TẤT CẢ ĐẠT" if not fails else f"LỖI: {fails}"))
sys.exit(1 if fails else 0)
