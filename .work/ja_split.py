#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bộ tách câu cho dòng thoại tiếng Việt — khớp đúng luật .work/parse_kichban.py.

Vì sao cần riêng: parse_kichban bỏ ** và * trước, rồi tách câu, nên số câu của
một dòng thoại là số câu của bản ĐÃ BỎ MARKER. Muốn dịch theo từng câu mà vẫn
giữ đúng số câu thì phải tách trên bản thô, nhưng điểm ngắt phải trùng với bản
đã bỏ marker.
"""
import re

SENT_END = ".?!…"
CLOSE_QUOTE = "”’'"          # dấu nháy đóng (sau khi chuẩn hoá, ' -> ” )
OPEN_QUOTE = "“‘'"           # dấu nháy mở  (sau khi chuẩn hoá, ' -> “ )
# đúng lớp ký tự mà parse_kichban dùng: [A-ZÀ-ỸĐ“(]
UPPER_CLASS = re.compile(r"[A-ZÀ-ỸĐ“(]")


def _marker_type(line, i):
    """Marker tại vị trí i -> (loại, độ dài)."""
    if i < len(line) and line[i] == "*":
        if i + 1 < len(line) and line[i + 1] == "*":
            j = i
            while j < len(line) and line[j] == "*":
                j += 1
            return "**", j - i
        return "*", 1
    return None, 0


def split_dialogue_sentences(line):
    """Tách dòng thoại thành câu, giữ nguyên ** và *.

    Trả về list câu (không rỗng) hoặc None nếu không xác định được.
    Điểm ngắt trùng với luật của parse_kichban (chạy trên bản đã bỏ marker),
    nên len(kết quả) == số câu mà parse_kichban tính.
    """
    L = len(line)
    parts, start = [], 0
    stack = []          # các marker đang mở (để biết marker nào đóng, marker nào mở)
    i = 0
    while i < L:
        c = line[i]
        if c == "*":
            typ, ln = _marker_type(line, i)
            if stack and stack[-1] == typ:
                stack.pop()
            else:
                stack.append(typ)
            i += ln
            continue
        if c not in SENT_END:
            i += 1
            continue

        j = i + 1
        while j < L and line[j] in CLOSE_QUOTE:
            j += 1

        # marker nằm NGAY sau dấu kết câu (trước khoảng trắng)
        if j < L and line[j] == "*":
            typ, ln = _marker_type(line, j)
            closing = bool(stack) and stack[-1] == typ
            k = j + ln
            while k < L and line[k].isspace():
                k += 1
            q = k
            while q < L and line[q] in OPEN_QUOTE:
                q += 1
            if q < L and UPPER_CLASS.match(line[q]):
                if closing:
                    parts.append(line[start:j + ln])
                    start = k
                    i = k
                else:
                    parts.append(line[start:j])
                    start = j
                    i = j
                continue
            i = j
            continue

        # khoảng trắng, rồi marker, rồi khoảng trắng
        k = j
        while k < L and line[k].isspace():
            k += 1
        if k < L and line[k] == "*":
            typ, ln = _marker_type(line, k)
            closing = bool(stack) and stack[-1] == typ
            k2 = k + ln
            while k2 < L and line[k2].isspace():
                k2 += 1
            q = k2
            while q < L and line[q] in OPEN_QUOTE:
                q += 1
            if q < L and UPPER_CLASS.match(line[q]):
                if closing:
                    parts.append(line[start:k + ln])
                    start = k2
                    i = k2
                else:
                    parts.append(line[start:k])
                    start = k
                    i = k
                continue
            i = j
            continue

        q = k
        while q < L and line[q] in OPEN_QUOTE:
            q += 1
        if q < L and UPPER_CLASS.match(line[q]):
            parts.append(line[start:k])
            start = k
            i = k
            continue
        i = j
    parts.append(line[start:])
    return [p.strip() for p in parts if p.strip()]


def move_trailing_markers(ja: str) -> str:
    """Đưa marker ở CUỐI dòng vào trước dấu kết câu cuối.

    Lý do: parse_kichban tách câu JA bằng ja_split, phần dư sau dấu kết câu
    cuối được tính thành MỘT câu nữa. Nếu dòng kết thúc bằng '*' thì số câu
    JA sẽ nhiều hơn số câu VN.
    """
    m = re.search(r"(\*{1,2})\s*$", ja)
    if not m:
        return ja
    run = m.group(1)
    body = ja[:m.start()].rstrip()
    idx = max(body.rfind("。"), body.rfind("！"), body.rfind("？"), body.rfind("…"))
    if idx < 0:
        return ja
    return body[:idx] + run + body[idx:]


def parts_balanced(parts) -> bool:
    """Mỗi câu phải cân bằng số ** và * (không marker nào mở ở câu này, đóng ở câu sau)."""
    for p in parts:
        if p.count("**") % 2:
            return False
        if (p.count("*") - p.count("**")) % 2:
            return False
    return True


# ---- đếm câu kiểu JA, đúng như parse_kichban.ja_split ----
JA_END = re.compile(r'[。！？…][」』”"）)\]]*')
LATIN_SPLIT = r'(?:(?<=[.?!…])|(?<=[.?!…]”))\s+(?=[A-ZÀ-ỸĐ가-힣“(])'


def ja_split(para):
    parts, last = [], 0
    for m in JA_END.finditer(para):
        parts.append(para[last:m.end()])
        last = m.end()
    tail = para[last:].strip()
    if tail:
        parts.append(tail)
    return parts


def ja_sentences(line: str) -> int:
    """Số câu của một dòng JA theo đúng luật parse_kichban.

    parse_kichban (dòng 50-52) làm đúng thứ tự sau TRƯỚC khi tách câu:
      1. bỏ prefix bullet `* ` / `1. `
      2. xoá toàn bộ `**` và `*`
      3. cắt dấu nháy bao ngoài
    Phải làm y hệt, nếu không số câu đếm được lệch với parser chính.
    """
    t = re.sub(r"^\*\s+", "", line.strip())
    t = re.sub(r"^\d+\.\s+", "", t)
    t = t.replace("**", "").replace("*", "")
    t = t.strip().strip('"“”').strip()
    if not t:
        return 0
    if any(ch in t for ch in '。！？'):
        return len(ja_split(t))
    return len(re.split(LATIN_SPLIT, t))
