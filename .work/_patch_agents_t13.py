#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them quy uoc T13 vao AGENTS.md (guin xuong dong CRLF)."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\AGENTS.md")
raw = p.read_bytes().decode("utf-8")

anchor = "của mốc ghi trong mô tả |"
assert raw.count(anchor) == 1, raw.count(anchor)

row = (
    "| T13 | **`package.py` (nhánh VN) ghi đè `mo_ta.txt` + `nguon_tham_khao.md` bằng khung RỖNG mỗi lần chạy ⇒ nguồn đã điền bị mất.** "
    "Đã vá 02/11/2026: `package.py` đọc nguồn thật từ `02_SAN_XUAT/<Tập>/nguon_mo_ta.txt` "
    "(khối chèn vào mục 📚 NGUỒN THAM KHẢO của mô tả) + `02_SAN_XUAT/<Tập>/nguon_tham_khao.md` "
    "(bảng đối chiếu từng câu). Không có file ⇒ giữ hành vi cũ (khung rỗng), **KHÔNG bịa nguồn** "
    "| Mỗi tập mới: tạo 2 file đó trong `EP_DIR` rồi chạy `AE_EP=XX python .work/package.py` "
    "(**không** `--mux` nếu không cần ghép lại video). Mô tả YouTube giới hạn **5000 ký tự** ⇒ "
    "`nguon_mo_ta.txt` phải rút gọn (1 dòng tên nguồn + URL), bảng đầy đủ để ở `nguon_tham_khao.md`. "
    "Kiểm link: `fbi.gov` / `leb.fbi.gov` / `britannica.com` chặn bot (403/WAF) nhưng **mở bình thường bằng trình duyệt** "
    "— đừng kết luận \"link chết\" |"
)

raw = raw.replace(anchor, anchor + "\r\n" + row)
p.write_bytes(raw.encode("utf-8"))
print("AGENTS.md: them dong T13 · len =", len(raw))
