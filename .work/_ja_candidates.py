#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng danh sách mục cache có dấu hiệu "tiếng Nhật lai tiếng khác" (rác model).

Dấu hiệu:
  A) từ Latin dính NGAY vào ký tự CJK (không có khoảng trắng) -> thường là rác.
  B) từ Trung dùng kanji HỢP LỆ trong tiếng Nhật (氛围/气氛/同步...) -> không tồn tại ở Nhật.

    py -3 .work/_ja_candidates.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

# từ Trung: dùng kanji hợp lệ ở Nhật nhưng CỤM TỪ không tồn tại trong tiếng Nhật
# (đã loại 冷静 果断 痛苦 好奇 茫然 沉默 独特 惊讶 深思 疑惑 愤怒 温柔 ... vì
#  những từ này đều là từ Nhật hợp lệ)
CN_WORDS = ["氛围", "气氛", "同步", "特意", "素质", "内在", "外在", "心灵", "情绪",
            "媳妇", "里面", "层面", "结局", "精髓", "束缚", "尴尬", "煎熬", "龟裂",
            "挑逗", "绽放", "狂喜", "沮丧", "体贴", "笼罩", "弥漫", "洋溢", "流淌",
            "闪烁", "苏醒", "抽搐", "狰狞", "凝重", "飘逸", "诡异", "凄凉", "悲壮",
            "豪迈", "澎湃", "压抑", "沉闷", "悦耳", "清脆", "浑厚", "沙哑", "恍惚",
            "迟疑", "狠心", "狡猾", "贪婪", "慷慨", "冷漠", "同步", "毋庸置疑"]

# thuật ngữ / tên riêng hợp lệ (không phải rác) -> bỏ qua
LAT_OK = {"dna", "tv", "sns", "fbi", "street", "avenue", "road", "court", "act",
          "foundation", "school", "hospital", "prison", "center", "centre",
          "university", "penitentiary", "county", "general", "state", "no",
          "reality", "night", "stalker", "mindhunter", "malin", "malingering",
          "mind", "hunter", "minimalist", "piano", "ambient", "dark", "the",
          "silence", "of", "lambs", "and", "the", "co", "ed", "killer", "bunny",
          "mun", "chausen", "munchausen"}

RX_LAT = re.compile(r"[A-Za-z\u00C0-\u024F]{2,}")
CJK = lambda c: ("぀" <= c <= "ヿ") or ("㐀" <= c <= "鿿") or ("豈" <= c <= "﫿")


def suspicious(ja: str):
    why = []
    for m in RX_LAT.finditer(ja):
        a = ja[m.start() - 1] if m.start() > 0 else ""
        b = ja[m.end()] if m.end() < len(ja) else ""
        if CJK(a) or CJK(b):
            why.append(f"LAT:{m.group(0)}")
    for w in CN_WORDS:
        if w in ja:
            why.append(f"CNW:{w}")
    return why


rows = []
for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    vn_text = M.canonical_vn(ep).read_text(encoding="utf-8").lower()
    d = json.loads(cp.read_text(encoding="utf-8"))
    for k, v in d.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        ja = v.get("ja", "")
        if not isinstance(ja, str) or not ja:
            continue
        why = []
        for m in RX_LAT.finditer(ja):
            w = m.group(0)
            if w.lower() in vn_text or w.lower() in LAT_OK:
                continue                      # có trong bản VN / thuật ngữ hợp lệ
            a = ja[m.start() - 1] if m.start() > 0 else ""
            b = ja[m.end()] if m.end() < len(ja) else ""
            if CJK(a) or CJK(b):
                why.append(f"LAT:{w}")
        for w in CN_WORDS:
            if w in ja:
                why.append(f"CNW:{w}")
        if why:
            rows.append((ep, k, why, ja))

print(f"=== {len(rows)} muc ngoi doi ===")
for ep, k, why, ja in rows:
    print(f"\nTap{ep} {k}  [{', '.join(why)}]")
    print(f"  {ja[:220]}")
