"""Báo cáo theo ELEMENT cho Tập 04: mã cũ vs mã mới, để dựng lại bảng shot.

In ra từng element (1.03, 1.05, ...) kèm số câu cũ / câu mới và TOÀN BỘ câu mới
để ánh xạ thủ công sang bảng shot mới.

Chạy:  py -3 .work/_report_t04_elements.py
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

OLD = WORK / "_cu" / "tap04_truoc_dung_lai_20261031" / "script_tap04.json"
NEW = WORK / "script_tap04.json"


def elements(path):
    sc = json.loads(path.read_text(encoding="utf-8-sig"))
    out = []
    for el in sc:
        if el.get("kind") != "LOI":
            continue
        out.append((el["id"], el.get("role"), el.get("sentences", [])))
    return out


def main():
    old = {e[0]: e for e in elements(OLD)}
    new = {e[0]: e for e in elements(NEW)}
    only_old = [k for k in old if k not in new]
    only_new = [k for k in new if k not in old]
    print(f"element: CU {len(old)} · MOI {len(new)} · chi cu {only_old} · chi moi {only_new}\n")
    for eid in new:
        o = old.get(eid)
        oc = len(o[2]) if o else 0
        nc = len(new[eid][2])
        flag = "  <-- SOI" if oc != nc else ""
        print(f"=== {eid}  ({new[eid][1]})  cu {oc} -> moi {nc}{flag}")
        if o:
            for s in o[2]:
                print(f"   CU  {s['id']}: {s['text']}")
        for s in new[eid][2]:
            print(f"   MOI {s['id']}: {s['text']}")
        print()


if __name__ == "__main__":
    main()
