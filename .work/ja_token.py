#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chuẩn hoá token Latin để so khớp giữa VN và JA (bỏ dấu câu ở hai đầu)."""
import re

STRIP = "'\",.;:!?()[]{}<>·・—–-_"


def norm_token(t: str) -> str:
    """'Cabrillo.' -> 'cabrillo' ; 'ass\\'' -> 'ass'"""
    return t.strip(STRIP).lower()


def tokens_of(text: str) -> list:
    """Danh sách token Latin đã chuẩn hoá (giữ nguyên thứ tự, có thể trùng)."""
    return [norm_token(w) for w in re.findall(r"[A-Za-z][A-Za-z0-9\-'.]{1,}", text or "")]


def token_set(text: str) -> set:
    return {t for t in tokens_of(text) if t}


def foreign_scripts(text: str) -> list:
    """Ký tự không phải Latin mà lẫn vào (Cyrillic / Greek) -> model bóp méo."""
    bad = []
    for ch in text or "":
        o = ord(ch)
        if 0x0400 <= o <= 0x04FF or 0x0370 <= o <= 0x03FF or 0x0500 <= o <= 0x052F:
            bad.append(ch)
    return sorted(set(bad))
