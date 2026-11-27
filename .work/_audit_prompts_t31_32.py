#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rà prompt t31/t32 LẦN 2: bỏ negation trước, rồi tìm vật có khả năng sinh chữ.

Negation không có tác dụng với FLUX.1-schnell (bài học T37-39), nên "no text"
không tính là yếu tố bảo vệ — ta chấm rủi ro theo VẬT mang chữ trong cảnh.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

NEG = [
    "no text", "no lettering", "no letters", "no words", "no word", "no numbers",
    "no number", "no signs", "no sign", "no labels", "no label", "no logos",
    "no logo", "no watermark", "no writing", "no printed text", "no signage",
    "without text", "textless", "blank text",
]

# Vật cụ thể có khả năng bị FLUX vẽ chữ lên
RISK = {
    "sign/signage": ["sign", "signage", "signboard", "street sign", "shop sign"],
    "biển cửa hàng": ["shop", "storefront", "store front", "diner", "pawn", "motel",
                       "hotel", "nightclub", "dance hall", "market stall", "booth", "barber"],
    "biển/bảng treo": ["board", "banner", "plaque", "bulletin", "menu", "easel",
                        "poster", "notice", "banner"],
    "giấy có chữ": ["calendar", "form", "receipt", "map", "ledger", "diary", "note",
                     "notebook", "document", "paper", "file folder", "folder", "label",
                     "certificate", "manifest", "logbook", "list"],
    "màn hình": ["screen", "monitor", "display", "laptop", "computer", "tablet"],
    "số/chữ trên vật": ["number", "numbers", "digit", "digits", "engraving", "engraved",
                         "inscription", "stamp", "printed", "printed text", "writing",
                         "spines", "logo", "brand", "badge"],
    "xe/biển số": ["license plate", "licence plate", "number plate", "bus", "ambulance",
                    "taxi", "van", "truck", "motorcycle", "car", "aircraft", "airplane",
                    "ship", "boat", "vehicle"],
    "chữ Hán/LED": ["chinese", "hanzi", "kanji", "neon sign", "neon light", "neon",
                     "glowing sign", "led sign"],
    "tòa nhà có biển": ["facade", "courthouse", "temple", "government building",
                         "bank building", "corporate tower", "headquarters"],
    "điện thoại": ["smartphone", "phone", "mobile phone"],
}


def strip_neg(p: str) -> str:
    out = p
    for n in NEG:
        out = re.sub(r"[,;]?\s*" + re.escape(n) + r"\b", "", out, flags=re.I)
    return out


def risk_of(prompt: str):
    p = " " + prompt.lower() + " "
    out = []
    for label, words in RISK.items():
        for w in words:
            # cho phép số nhiều: calendar/calendars, paper/papers, plate/plates...
            if re.search(r"\b" + re.escape(w) + r"(?:s|es)?\b", p):
                out.append(label)
                break
    return out


def main():
    lines = []
    for ep in (31, 32):
        path = WORK / f"bg_jobs_tap{ep}.json"
        jobs = json.loads(path.read_text(encoding="utf-8"))
        clean, risky = [], []
        for j in jobs:
            h = risk_of(strip_neg(j["prompt"]))
            (risky if h else clean).append((j["name"], h))
        lines.append(f"===== TAP {ep}: {len(jobs)} job | {len(clean)} an toan | {len(risky)} rui ro =====")
        for name, h in risky:
            lines.append(f"{ep}\t{name}\t{', '.join(h)}")
    out = "\n".join(lines)
    (WORK / "_audit_t31_32_r3.txt").write_text(out, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
