#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rút gọn 14 tiêu đề JA để không xuống dòng lỗi (orphan <=3 ký tự) / cắt giữa từ Latin."""
import json
from pathlib import Path

P = Path(r"D:/TEST/Gax/amber-eyes/.work/shots_text_tap03_JA.json")
d = json.loads(P.read_text(encoding="utf-8-sig"))

FIX = {
    "1-02": ("当直電話のベルが響き、静かな空気を破った", "当直電話のベルが静寂を破った"),
    "1-18": ("警察が仕掛けた巧みな罠には捕まらなかった", "警察の巧みな罠には捕まらなかった"),
    "1-24": ("Criminal Personality Research Project",
             "犯罪性格研究プロジェクト"),
    "3-11": ("第2層：投射のメカニズムと代理被害者", "第2層：投射と代理被害者"),
    "3-16": ("Kemperと他の連続殺人者の決定的な違いは？", "Kemperと他の連続殺人者との違い？"),
    "3-20": ("FBIとの対話――犯罪プロファイリング技術の基礎", "FBIとの対話――犯罪プロファイリングの基盤"),
    "4-05": ("FBI特別検査官による歴史的出会いの再現", "FBI特別検査官の歴史的出会いを再現"),
    "4-06": ("巨大すぎて扉枠いっぱいに広がっていた", "巨大すぎて扉枠いっぱいに広がった"),
    "4-17": ("THE SILENCE OF THE LAMBS & MINDHUNTER", "羊たちの沈黙 ＆ MINDHUNTER"),
    "5-08": ("兆候01：幼少期のMacdonald Triad", "兆候01：Macdonald Triad"),
    "5-10": ("兆候02：家族による極端な心理的虐待", "兆候02：極端な心理的虐待"),
    "5-12": ("兆候04：高い知性と感情の冷たさ", "兆候04：高い知性と冷たさ"),
}

applied = []
for sid, (old, new) in FIX.items():
    chu = d[sid][0]
    if old not in chu:
        raise SystemExit(f"{sid}: khong tim thay '{old}' trong: {chu}")
    d[sid][0] = chu.replace(old, new)
    applied.append(sid)

# 1-24: dua ten tieng Anh day du vao dong phu
d["1-24"][0] = ("*BSU · FBI* · **犯罪性格研究プロジェクト** · "
                "*Criminal Personality Research Project · 行動科学部門の最初の研究者*")
applied.append("1-24(sub)")

P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("da sua:", ", ".join(applied))
