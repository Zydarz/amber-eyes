#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VÒNG 2 — sinh lại 3 nền Tập 11 vẫn còn chữ sau vòng 1.

Vòng 1 sửa được 29/32. 3 nền còn lỗi vì VẬT THỂ CÓ SẴN BỐ CỤC CHỮ:
  - `haunted_new_identity_shadow`  : hộ chiếu MỞ ⇒ trang định danh có sẵn ô ảnh + ô tên
  - `triumphant_smile_deal_with_devil`: tờ "plea bargain" ⇒ AI in tiêu đề lên
  - `six_8mm_tapes_bag`             : vỏ băng có sẵn dải nhãn ⇒ AI ghi ký hiệu
Cách sửa vòng 2: ĐỔI CẢ BỐ CỤC, không chỉ đổi mô tả bề mặt.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
JOBS = ROOT / ".work" / "bg_jobs_tap11.json"
OUT = ROOT / ".work" / "bg_jobs_tap11_detext3_r2.json"

BLANK = "completely blank and unmarked with no writing at all"

NEW = {
"t11_haunted_new_identity_shadow":
 "Still life of a passport booklet lying CLOSED and FACE-DOWN on wet winter pavement so that only its plain smooth unmarked back cover can be seen, a single blank embossed crest shape on the cover with no lettering, no photograph panel and no identity page anywhere, permanent looming shadows of past crimes falling across it, eternal moral exile and social ostracism, " + BLANK + ".",

"t11_triumphant_smile_deal_with_devil":
 "Metaphorical psychological visual: a torn sheet of old blank paper crumbling into ash on the floor of a dark interrogation room, backlit by the eerie formless glow of a vintage monitor showing only blank white light, a plain sheet of empty unmarked paper with no printed lines and no lettering anywhere on it, the bitter sting of being utterly duped by a monster, " + BLANK + ".",

"t11_six_8mm_tapes_bag":
 "Forensic evidence handover still life: a brown canvas duffel bag unzipped on a police evidence locker counter revealing six 8mm magnetic video cassette tapes inside plain unmarked plastic cases, the cases are smooth bare shells with no label strip and no sticker anywhere, a bare metal locker wall behind, autumn 1994 turning point, stark graphic noir, " + BLANK + ".",
}


def main():
    jobs = {j["name"]: j for j in json.loads(JOBS.read_text(encoding="utf-8"))}
    out = []
    for i, (n, p) in enumerate(NEW.items(), start=1):
        old = jobs[n]
        out.append({
            "name": n, "act": old.get("act", 1), "sentences": old.get("sentences", ""),
            "desc": old.get("desc", ""), "prompt": p, "seed": 41000 + i,
            "why": "vong 2: doi ca bo cuc vat the (co san o chu)",
        })
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ghi {OUT.relative_to(ROOT)} · {len(out)} job vong 2")
    for j in out:
        print(f"  {j['name']} seed={j['seed']}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
