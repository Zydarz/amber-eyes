#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDIT TỔNG HỢP 29 file JA — mọi lớp lỗi nhiễm ngôn ngữ, dùng đúng hàm check
của pipeline + các quy tắc riêng.

    py -3 .work/_ja_final_audit.py
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

RX_HANGUL = re.compile(r"[\u3131-\u318e\uac00-\ud7a3]")
RX_LAT = re.compile(r"[A-Za-z\u00C0-\u024F]{2,}")
CN_WORDS = ["氛围", "气氛", "同步", "特意", "素质", "内在", "外在", "心灵", "情绪",
            "媳妇", "里面", "层面", "结局", "精髓", "束缚", "尴尬", "煎熬", "龟裂",
            "挑逗", "绽放", "狂喜", "沮丧", "体贴", "笼罩", "弥漫", "洋溢", "流淌",
            "闪烁", "苏醒", "抽搐", "狰狞", "凝重", "飘逸", "诡异", "凄凉", "悲壮",
            "豪迈", "澎湃", "压抑", "沉闷", "悦耳", "清脆", "浑厚", "沙哑", "恍惚",
            "迟疑", "狠心", "狡猾", "贪婪", "慷慨", "冷漠"]
LAT_OK = {"dna", "tv", "sns", "fbi", "bgm", "street", "avenue", "road", "court",
          "act", "foundation", "school", "hospital", "prison", "center", "centre",
          "university", "penitentiary", "county", "general", "state", "no",
          "reality", "night", "stalker", "mindhunter", "malin", "malingering",
          "mind", "hunter", "minimalist", "piano", "ambient", "dark", "the",
          "silence", "of", "lambs", "and", "co", "ed", "killer", "bunny",
          "mun", "chausen", "munchausen"}

# ký tự CJK "dính" — bỏ qua dấu câu Nhật (。、・「」…) và khoảng trắng
PUNCT = set("。、・「」（）〔〕【】…―！？：；,.!?;:()[]{}\"'`~ \t　")


def glued_cjk(c):
    if not c:
        return False
    if c in PUNCT:
        return False
    return ("\u3000" <= c <= "\u30ff") or ("\u3400" <= c <= "\u9fff") or ("\uf900" <= c <= "\ufaff")


def strip_diac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def jobs_for(ep):
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    out = []
    for u in units:
        if u["kind"] == "RAW":
            continue
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            if parts:
                for k, p in enumerate(parts):
                    out.append({"id": f"{u['id']}#{k}", "vi": p, "ctx": u["vi"],
                                "kind": "dialogue", "n": 1})
                continue
            out.append({"id": f"{u['id']}#L", "vi": u["vi"], "ctx": u["vi"],
                        "kind": "line", "n": u.get("n", 0)})
            continue
        if u["kind"] == "TABLE":
            out.append({"id": u["id"], "vi": u["vi"], "kind": "table",
                        "cells": u["vi"].split("\t"), "n": 0})
            continue
        out.append({"id": u["id"], "vi": u["vi"], "kind": "meta", "n": 0})
    return out


total_err = 0
for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        print(f"Tap{ep}: KHONG CO CACHE")
        total_err += 1
        continue
    cache = json.loads(cp.read_text(encoding="utf-8"))
    jobs = jobs_for(ep)
    vmap = {j["id"]: j for j in jobs}
    vn_text = M.canonical_vn(ep).read_text(encoding="utf-8")
    vl = vn_text.lower()
    ep_tokens = M.vn_tokens_of(vn_text)

    errs = []
    for j in jobs:
        if j["id"] not in cache:
            continue
        raw = cache[j["id"]].get("ja", "")
        if not isinstance(raw, str) or not raw:
            continue
        ja = M.repair_ja(raw, j["vi"])
        # 1) lỗi cấu trúc theo pipeline (bảng: giữ nguyên \t để check_meta
        #    đối chiếu đúng số ô)
        if j["kind"] == "dialogue":
            ok, reason, kind = M.check_sentence(ja, j["vi"], ep_tokens, j.get("ctx", ""))
        elif j["kind"] == "line":
            ok, reason, kind = M.check_line(ja, j["vi"], j.get("n", 0), ep_tokens)
        else:
            ok, reason, kind = M.check_meta(ja, j["vi"], ep_tokens)
        if not ok:
            errs.append((j["id"], "PIPELINE", reason))
            continue
        # 2) nhiễm ngôn ngữ
        cn = sorted({c for c in ja if c in M.CN_ONLY_CHARS})
        if cn:
            errs.append((j["id"], "CN-ONLY", "".join(cn)))
        if RX_HANGUL.search(ja):
            errs.append((j["id"], "HANGUL", RX_HANGUL.findall(ja)))
        for w in CN_WORDS:
            if w in ja:
                errs.append((j["id"], "CN-WORD", w))
        for m in RX_LAT.finditer(ja):
            w = m.group(0)
            if w.lower() in vl or w.lower() in LAT_OK:
                continue
            a = ja[m.start() - 1] if m.start() > 0 else ""
            b = ja[m.end()] if m.end() < len(ja) else ""
            if glued_cjk(a) or glued_cjk(b):
                errs.append((j["id"], "LAT-JUNK", w))
                break

    if errs:
        print(f"\n########## Tap{ep}: {len(errs)} loi ##########")
        for uid, tag, info in errs:
            print(f"  [{uid}] {tag}: {info}")
            print(f"      {cache[uid].get('ja','')[:150]}")
        total_err += len(errs)
    else:
        print(f"Tap{ep}: OK ({len(cache)} muc)")

print(f"\n\nTONG LOI: {total_err}")
