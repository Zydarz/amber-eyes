# -*- coding: utf-8 -*-
"""Tập 11 — lập kế hoạch tách nền theo H25 (chặn trước khi viết prompt).

Cách chia:
  - Mỗi lần xuất hiện LIỀN MẠCH của một mã nền trong kịch bản = 1 "cụm".
    Cùng mã nền dùng lại ở hồi khác (cách quãng) = cảnh khác ⇒ phải tách mã.
  - Mỗi cụm chia thành các nhóm ≤ 2 shot (≤ 3 shot nếu thời lượng cho phép),
    tổng ≤ 30 s (≤ 28 s nếu ngay sau là thẻ chuyển hồi vì cổng --plan gán
    thẻ "void" (+1 shot, +2 s) vào nền trước).
  - Nhóm đầu tiên của mã cũ GIỮ mã cũ (dùng lại ảnh đã có).
  - Các nhóm còn lại cần MÃ MỚI + ẢNH MỚI.
"""
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
        cau_raw = cells[0]
        dur = sum(float(x.replace(",", ".")) for x in re.findall(r"\((\d+(?:[.,]\d+)?) ?s\)", cau_raw))
        cau = re.search(r"`([^`]+)`", cau_raw)
        bg = re.search(r"`(t\d+_[a-z0-9_]+)`", cells[3] if len(cells) > 3 else "")
        is_card = bool(re.search(r"nghỉ chuyển hồi|hết tập", cau_raw))
        rows.append(dict(sid=sid, dur=dur, cau=cau.group(1) if cau else cau_raw,
                         vai=cells[1] if len(cells) > 1 else "",
                         mau=cells[2] if len(cells) > 2 else "",
                         bg=bg.group(1) if bg else None,
                         cam=(re.findall(r"`([^`]+)`", cells[3])[-1] if len(re.findall(r"`([^`]+)`", cells[3])) > 1 else ""),
                         chu=cells[4] if len(cells) > 4 else "",
                         card=is_card, end_card=bool(re.search(r"hết tập", cau_raw))))
    return rows


def build(rows, max_shot_per_chunk=2, max_sec=30.0):
    # tách thẻ kết (hết tập) ra khỏi cụm: nó dùng mẫu T2, cần nền riêng
    content = [r for r in rows if not r["card"]]
    end_card = next((r for r in rows if r["end_card"]), None)
    # gom cụm liền mạch
    runs = []
    for r in content:
        if runs and runs[-1][0] == r["bg"]:
            runs[-1][1].append(r)
        else:
            runs.append((r["bg"], [r]))
    # chia nhóm
    chunks = []
    for bg, rs in runs:
        i = 0
        ci = 0
        while i < len(rs):
            take, t = [], 0.0
            while i < len(rs) and len(take) < max_shot_per_chunk:
                r = rs[i]
                if take and t + r["dur"] > max_sec:
                    break
                take.append(r); t += r["dur"]; i += 1
            ci += 1
            chunks.append(dict(parent=bg, run_bg=bg, run_idx=ci, rows=take,
                               sec=round(t, 1), n=len(take)))
    return chunks, end_card


if __name__ == "__main__":
    rows = parse(MD)
    chunks, end_card = build(rows)
    print("dòng:", len(rows), "| content:", len([r for r in rows if not r["card"]]),
          "| thẻ kết:", end_card["sid"] if end_card else None)
    # cảnh báo: nhóm 2 shot sát thẻ chuyển hồi
    warns = []
    for idx, c in enumerate(chunks):
        nxt = chunks[idx + 1] if idx + 1 < len(chunks) else None
        if nxt is None:
            continue
        # thẻ chuyển hồi nằm sau shot cuối của cụm nếu sid kế tiếp là card
        after = [r for r in rows if r["card"] and not r["end_card"]]
        nxt_row = next((r for r in rows if r["sid"] > c["rows"][-1]["sid"]), None)
        if nxt_row and nxt_row["card"] and not nxt_row["end_card"]:
            if c["n"] + 1 > 3 or c["sec"] + 2 > 30:
                warns.append((c["parent"], c["rows"][-1]["sid"], c["n"], c["sec"]))
    print("nhóm sát thẻ chuyển hồi có nguy cơ vượt:", warns)
    print("TỔNG NHÓM (chưa gồm thẻ kết):", len(chunks))
    print("thẻ kết -> 1 nhóm riêng => TỔNG mã nền =", len(chunks) + 1)
    dist = collections.Counter(c["n"] for c in chunks)
    print("phân bố shot/nhóm:", dict(sorted(dist.items())))
    # mã cũ giữ lại vs mã mới
    keep = collections.Counter()
    for c in chunks:
        keep[c["parent"]] += 1
    new_needed = sum(v - 1 for v in keep.values())
    print("mã cũ giữ nguyên:", len(keep), "| MÃ MỚI cần sinh:", new_needed)
    json.dump({"chunks": [dict(parent=c["parent"], run_idx=c["run_idx"], n=c["n"], sec=c["sec"],
                               sids=[r["sid"] for r in c["rows"]],
                               caus=[r["cau"] for r in c["rows"]],
                               chus=[r["chu"] for r in c["rows"]]) for c in chunks],
               "end_card": end_card["sid"] if end_card else None},
              open(".work/_t11_chunks.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("-> .work/_t11_chunks.json")
