# -*- coding: utf-8 -*-
"""Tập 11 — parse bảng shot mục 6 (VI) + in nhóm theo nền để lập kế hoạch tách (H25)."""
import re, json, collections, sys

MD = "02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/KeHoach_Video_Tap11.md"
ROW = re.compile(r"^\|\s*([1-5]-\d+)\s*\|(.*)$")


def parse(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        m = ROW.match(line.rstrip("\n"))
        if not m:
            continue
        sid, rest = m.group(1), m.group(2)
        cells = [c.strip() for c in rest.split("|")]
        # cells[0]=Câu cells[1]=Vai cells[2]=Mẫu cells[3]=Nền+bóng cells[4]=Chữ ...
        cau_raw = cells[0]
        dur = sum(float(x.replace(",", ".")) for x in re.findall(r"\((\d+(?:[.,]\d+)?) ?s\)", cau_raw))
        cau = re.search(r"`([^`]+)`", cau_raw)
        bg = re.search(r"`(t\d+_[a-z0-9_]+)`", cells[3] if len(cells) > 3 else "")
        cam = re.findall(r"`([^`]+)`", cells[3] if len(cells) > 3 else "")
        rows.append(dict(
            sid=sid, dur=dur,
            cau=cau.group(1) if cau else cau_raw,
            vai=cells[1] if len(cells) > 1 else "",
            mau=cells[2] if len(cells) > 2 else "",
            bg=bg.group(1) if bg else None,
            cam=cam[-1] if len(cam) > 1 else "",
            chu=cells[4] if len(cells) > 4 else "",
            card=bool(re.search(r"nghỉ chuyển hồi|hết tập", cau_raw)),
            raw=line.rstrip("\n"),
        ))
    return rows


if __name__ == "__main__":
    rows = parse(MD)
    print("tổng dòng:", len(rows), "| card:", sum(r["card"] for r in rows),
          "| bg=None (dùng nền trước):", sum(1 for r in rows if r["bg"] is None))
    groups = collections.OrderedDict()
    for r in rows:
        if r["card"]:
            continue
        groups.setdefault(r["bg"], []).append(r)
    print("nhóm nền:", len(groups))
    out = []
    for bg, rs in groups.items():
        out.append(dict(bg=bg, n=len(rs), sec=round(sum(r["dur"] for r in rs), 1),
                        shots=[dict(sid=r["sid"], cau=r["cau"], dur=r["dur"], chu=r["chu"]) for r in rs]))
    json.dump(out, open(".work/_t11_groups.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for g in out:
        print(f"\n### {g['bg']}  ({g['n']} shot · {g['sec']} s)")
        for s in g["shots"]:
            print(f"   {s['sid']:>6} {s['cau']:>9} {s['dur']:>5}s  {s['chu'][:110]}")
