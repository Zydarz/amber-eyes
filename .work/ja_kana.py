#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phiên âm Latin -> Katakana (xấp xỉ) — dùng để đối chiếu tên địa danh.

Bản đơn giản theo ký tự, đủ để nhận ra các tên đã được dịch sang Katakana.
"""
import re

_C = {
    "a": "ア", "i": "イ", "u": "ウ", "e": "エ", "o": "オ",
    "ka": "カ", "ki": "キ", "ku": "ク", "ke": "ケ", "ko": "コ",
    "sa": "サ", "si": "シ", "su": "ス", "se": "セ", "so": "ソ",
    "ta": "タ", "ti": "ティ", "tu": "ツ", "te": "テ", "to": "ト",
    "na": "ナ", "ni": "ニ", "nu": "ヌ", "ne": "ネ", "no": "ノ",
    "ha": "ハ", "hi": "ヒ", "hu": "フ", "he": "ヘ", "ho": "ホ",
    "ma": "マ", "mi": "ミ", "mu": "ム", "me": "メ", "mo": "モ",
    "ya": "ヤ", "yu": "ユ", "yo": "ヨ",
    "ra": "ラ", "ri": "リ", "ru": "ル", "re": "レ", "ro": "ロ",
    "wa": "ワ", "wi": "ウィ", "we": "ウェ", "wo": "ウォ",
    "n": "ン", "m": "ム", "l": "ル", "r": "ル",
    "b": "ブ", "p": "プ", "f": "フ", "g": "グ", "h": "ハ", "j": "ジ",
    "k": "ク", "s": "ス", "t": "ト", "d": "ド", "z": "ズ",
    "c": "ク", "q": "ク", "x": "クス", "v": "ヴ", "w": "ウ", "y": "イ",
}
_SMALL = {"ア": "ァ", "イ": "ィ", "ウ": "ゥ", "エ": "ェ", "オ": "ォ",
          "ヤ": "ャ", "ユ": "ュ", "ヨ": "ョ", "ツ": "ッ"}


def to_katakana(text: str) -> str:
    s = re.sub(r"[^A-Za-z]+", " ", text or "").strip().lower()
    if not s:
        return ""
    words = []
    for w in s.split():
        out = ""
        i = 0
        while i < len(w):
            two = w[i:i + 2]
            if two in ("sh", "ch", "th", "ph", "wh"):
                out += {"sh": "シ", "ch": "チ", "th": "ス", "ph": "フ", "wh": "ウ"}[two]
                i += 2
                continue
            if two in _C:
                out += _C[two]
                i += 2
                continue
            if w[i] in _C:
                k = _C[w[i]]
                out += k
                i += 1
                continue
            i += 1
        # nguyên âm dài ở cuối âm tiết
        out = re.sub(r"([ウ])ー", r"\1ー", out)
        # nguyên âm đôi -> âm tiết dài
        out = re.sub(r"([アイウエオ])ー", r"\1ー", out)
        words.append(out)
    return "・".join(words)


def katakana_runs(text: str) -> list:
    return re.findall(r"[ァ-ヴー]{3,}", text or "")
