#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét prompt 136 nền Tập 11 tìm câu YÊU CẦU chữ — nguyên nhân gốc (bài học Tập 10).

Không phải "AI ngẫu nhiên viết chữ": khi prompt bảo vẽ vật mang chữ (biển, bìa,
nhãn, giấy có dòng ký), FLUX sẽ bịa ra chữ vô nghĩa. Sửa đúng là GỠ thông tin
chữ khỏi prompt, không phải thêm "no text" vào NEG.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
JOBS = ROOT / ".work" / "bg_jobs_tap11.json"
OUT = ROOT / ".work" / "_t11" / "prompt_textscan.json"

# cụm chỉ ra "vật mang chữ"
PAT = [
    r"\bmark(?:ed|s|ing)\b", r"\blabel(?:l)?ed\b", r"\blabels?\b", r"\btext\b",
    r"\bwords?\b", r"\bwrit(?:e|es|ten|ing)\b", r"\bsign(?:ed|ature)?\b",
    r"\bprinted\b", r"\bprint\b", r"\btitled?\b", r"\bheadline\b", r"\bcaption",
    r"\bengrav(?:ed|ing)\b", r"\binscri(?:p|bed|ption)\b", r"\btyped\b",
    r"\bcover\b", r"\bspine\b", r"\bform\b", r"\bnotice\b", r"\bplacard\b",
    r"\bposter\b", r"\bnewspaper\b", r"\bheadline\b", r"\bbanner\b",
    r"\btag\b", r"\bplate\b", r"\bbadge\b", r"\bdocket\b", r"\bmanuscript\b",
    r"\bhandwritten\b", r"\bhand-written\b", r"\bsignature\b", r"\breceipt\b",
    r"\bcertificate\b", r"\bdiploma\b", r"\bcard\b", r"\bposter\b", r"\bsheet of",
    r"\bpaper (?:with|showing|reading)\b", r"\bbook\b", r"\bfolder\b",
    r"\bbinder\b", r"\breceipts?\b", r"\bmap of\b", r"\bdiagram\b", r"\bchart\b",
    r"\btag\b", r"\bemblem\b", r"\bcrest\b", r"\bcoat of arms\b",
]
RX = re.compile("|".join(PAT), re.I)


def main():
    jobs = json.loads(JOBS.read_text(encoding="utf-8"))
    flagged = []
    for j in jobs:
        p = j.get("prompt", "")
        hits = sorted({m.group(0).lower() for m in RX.finditer(p)})
        if hits:
            flagged.append({"name": j["name"], "hits": hits, "prompt": p})
    OUT.write_text(json.dumps(flagged, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(flagged)}/{len(jobs)} prompt co tu khoa chu")
    for f in flagged:
        print(f"  {f['name']:<48} {','.join(f['hits'])}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
