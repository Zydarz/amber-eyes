#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra DONG BO: audio Higgs da tai ve (payload 15:51) co khop kich ban hien tai?

H14: doi audio => phai parse_shots + dung lai hinh. Truoc het phai biet audio
dung ban kich ban nao. So sanh text_plain cua payload voi text cua script hien tai.
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"


def norm(s):
    s = re.sub(r"[`*_]", "", s or "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main():
    script = json.loads((WORK / "script_tap04.json").read_text(encoding="utf-8-sig"))
    cur = {}
    for e in script:
        for s in e.get("sentences", []):
            cur[s["id"]] = s["text"]

    pay = json.loads((WORK / "kaggle_higgs" / "higgs_payload_t04.json").read_text(encoding="utf-8-sig"))
    items = pay["items"] if isinstance(pay, dict) and "items" in pay else pay

    man = json.loads((WORK / "kaggle_higgs" / "out_higgs_prod_t04" / "out_higgs_prod_t04"
                      / "higgs_manifest.json").read_text(encoding="utf-8-sig"))
    dl = {m["id"]: m for m in man}

    bad = []
    for it in items:
        sid = it["id"]
        tp = it.get("text_plain") or it.get("text_sent") or ""
        if sid not in cur:
            bad.append((sid, "KHONG CO trong script", tp[:60]))
        elif norm(cur[sid]) != norm(tp):
            bad.append((sid, "KHAC TEXT", f"script={norm(cur[sid])[:60]} | audio={norm(tp)[:60]}"))

    only_cur = sorted(set(cur) - {it["id"] for it in items})
    only_pay = sorted({it["id"] for it in items} - set(cur))

    print("script cau:", len(cur), "| payload items:", len(items), "| manifest id:", len(dl))
    print("LECH:", len(bad))
    for b in bad[:25]:
        print("   ", b)
    if only_cur:
        print("chi trong script:", only_cur[:20])
    if only_pay:
        print("chi trong payload:", only_pay[:20])
    # man hinh khac payload (audio tai ve co dung ban payload khong?)
    mp = {it["id"]: norm(it.get("text_plain") or "") for it in items}
    dd = {k: norm(v.get("text_plain") or "") for k, v in dl.items()}
    diff = [k for k in mp if k in dd and mp[k] != dd[k]]
    print("manifest khac payload:", len(diff), diff[:10])
    print("=> KET LUAN:", "DONG BO" if not bad and not diff else "CO LECH - CAN LAM LAI CHUOI")
    return 0 if (not bad and not diff) else 1


if __name__ == "__main__":
    sys.exit(main())
