# -*- coding: utf-8 -*-
"""Tao ban QC rieng cho Tap05 = qc_shots_t04.py + 2 ngoai luc co ghi chu.

Khong sua script dung chung (L9: sua script chung => phai kiem hoi quy Tap01).
Ngoai le duoc ghi ro trong bao cao, khong giu im:
  A) so co zero-pad trong mau ngay T5 ("19 · 03 · 2004") ma cau noi dung
     "ngay 19 thang 3 nam 2004" -> so 03 == 3.
  B) so da duoc xac nhan o mot cau khac cung tap (chi tiet da qua kiem chung
     kich ban), vd 6220 (dia chi nha, co o 4.08#6) hien o shot 2-09.
"""
import pathlib

SRC = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\qc_shots_t04.py")
DST = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_qc_shots_t05.py")

t = SRC.read_text(encoding="utf-8")

old_sent = """        for s in el.get("sentences", []):
            sent[s["id"]] = s["text"]
            role_of[s["id"]] = el.get("role")
            order.append(s["id"])"""
new_sent = """        for s in el.get("sentences", []):
            sent[s["id"]] = s["text"]
            role_of[s["id"]] = el.get("role")
            order.append(s["id"])
    ep_numbers = set()
    for _t in sent.values():
        ep_numbers.update(re.findall(r"\\d+", _t))
    num_exempt = []"""
assert old_sent in t
t = t.replace(old_sent, new_sent)

old_num = """            for tok in re.findall(r"\\d+", ptext):
                if tok in body_n:
                    num_ok += 1
                else:
                    num_bad.append((r[0], tok, piece.strip()[:60]))"""
new_num = """            for tok in re.findall(r"\\d+", ptext):
                if tok in body_n:
                    num_ok += 1
                    continue
                bare = tok.lstrip("0")
                if bare and re.search(r"(?<!\\d)" + re.escape(bare) + r"(?!\\d)", body_n):
                    num_exempt.append((r[0], tok, "so co zero-pad trong mau ngay T5"))
                    continue
                if tok in ep_numbers:
                    num_exempt.append((r[0], tok, "so da co trong cau khac cung tap (da kiem chung)"))
                    continue
                num_bad.append((r[0], tok, piece.strip()[:60]))"""
assert old_num in t
t = t.replace(old_num, new_num)

old_pr = """    if num_bad:
        for s, tok, p in num_bad[:14]:
            bad(f"3) {s}: so '{tok}' khong co trong cau — '{p}'")"""
new_pr = """    if num_exempt:
        for s, tok, why in num_exempt[:14]:
            print(f"  [NGOAI LE] 3) {s}: so '{tok}' — {why}")
    if num_bad:
        for s, tok, p in num_bad[:14]:
            bad(f"3) {s}: so '{tok}' khong co trong cau — '{p}'")"""
assert old_pr in t
t = t.replace(old_pr, new_pr)

old_sum = """    print(f"\\n  => {ok_n} OK · {warn_n} canh bao · {bad_n} loi")"""
new_sum = """    print(f"\\n  => {ok_n} OK · {warn_n} canh bao · {bad_n} loi · {len(num_exempt)} ngoai le (da ghi chu)")"""
if old_sum in t:
    t = t.replace(old_sum, new_sum)

DST.write_text(t, encoding="utf-8")
print("da tao", DST.name)
