# -*- coding: utf-8 -*-
"""Tập 11 — parse bảng shot mục 6 và lập kế hoạch TÁCH NỀN theo H25.

Quy tắc:
  - mỗi nền ≤ 3 shot VÀ ≤ 30 s (H22)
  - mục tiêu 1,5–2 shot/nền (H25)
  - shot giữ nguyên mã, mẫu, camera; chỉ đổi mã nền
"""
import re, json, sys, collections

PLAN = {
    "vi": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/KeHoach_Video_Tap11.md",
    "en": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap11_EN/KeHoach_Video_Tap11_EN.md",
    "ja": "02_SAN_XUAT/Ho_So_Toi_Pham/Tap11_JA/KeHoach_Video_Tap11_JA.md",
}

ROW = re.compile(r"^\|\s*([0-9]+-[0-9]+)\s*\|\s*`([^`]+)`\s*\(([\d,]+)\s*s\)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+)`\s*,\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|")


def parse(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        m = ROW.match(line.rstrip("\n"))
        if not m:
            continue
        sid, cau, dur, vai, mau, bg, cam = m.groups()[:7]
        chu = m.group(7) if len(m.groups()) > 7 else ""
        rows.append(dict(sid=sid, cau=cau, dur=float(dur.replace(",", ".")), vai=vai,
                         mau=mau, bg=bg, cam=cam, chu=chu, raw=line.rstrip("\n")))
    return rows


def plan_split(rows, target_per_bg=2.0, max_shots=3, max_sec=30.0):
    """Chia mỗi nền cũ thành các nhóm nền mới."""
    by_bg = collections.OrderedDict()
    for r in rows:
        by_bg.setdefault(r["bg"], []).append(r)

    assign = {}          # sid -> mã nền mới
    groups = []          # (mã nền, [shot])
    for bg, rs in by_bg.items():
        # số nhóm tối thiểu để đạt target shot/nền
        k = max(1, int(round(len(rs) / target_per_bg)))
        # chia đều các nhóm
        chunks = []
        base, extra = divmod(len(rs), k)
        i = 0
        for gi in range(k):
            n = base + (1 if gi < extra else 0)
            chunks.append(rs[i:i + n])
            i += n
        # tách tiếp nếu nhóm vượt 30 s
        final = []
        for ch in chunks:
            cur, cur_t = [], 0.0
            for r in ch:
                if cur and (len(cur) >= max_shots or cur_t + r["dur"] > max_sec):
                    final.append(cur); cur, cur_t = [], 0.0
                cur.append(r); cur_t += r["dur"]
            if cur:
                final.append(cur)
        for gi, ch in enumerate(final, 1):
            new = bg if len(final) == 1 else f"{bg}_s{gi}"
            groups.append((new, ch))
            for r in ch:
                assign[r["sid"]] = new
    return assign, groups


if __name__ == "__main__":
    rows = parse(PLAN["vi"])
    print("rows VI:", len(rows))
    for lang in PLAN:
        rr = parse(PLAN[lang])
        print(f"  {lang}: {len(rr)} dòng, {len(set(r['bg'] for r in rr))} mã nền")
    assign, groups = plan_split(rows)
    print("\nsau khi tách:", len(groups), "nhóm nền")
    sizes = collections.Counter(len(g) for _, g in groups)
    secs = [(n, round(sum(r["dur"] for r in g), 1)) for n, g in groups]
    print("phân bố shot/nền:", dict(sorted(sizes.items())))
    bad = [(n, s, len(g)) for (n, g), s in zip(groups, secs) if s > 30 or len(g) > 3]
    print("vi phạm (≤3 shot & ≤30 s):", len(bad), bad[:10])
    # kiểm tra đồng bộ 3 ngôn ngữ
    for lang in PLAN:
        rr = parse(PLAN[lang])
        m = {r["sid"]: r["bg"] for r in rr}
        diff = [s for s in m if s in assign and m[s] != assign[s]]
        print(f"  đồng bộ {lang}: {len(diff)} shot lệch")
    json.dump({"assign": assign,
               "groups": [{"bg": n, "sids": [r["sid"] for r in g],
                           "dur": round(sum(r["dur"] for r in g), 1),
                           "cau": [r["cau"] for r in g],
                           "chu": [r["chu"] for r in g]} for n, g in groups]},
              open(".work/_t11_split_plan.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\n-> .work/_t11_split_plan.json")
