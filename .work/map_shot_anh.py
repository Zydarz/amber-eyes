#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lập bảng MAPPING shot <-> ảnh nền từ bg_jobs_tapXX.json + kịch bản VN.
Dùng: py -3 .work/map_shot_anh.py [XX ...]   (mặc định 26-63,65,67)
      py -3 .work/map_shot_anh.py --shots XX [--lang vi|en|ja] [--endcard NAME]   # tạo shots_tXX.json cho build_video3 TỪ mapping + timeline đo thật
      py -3 .work/map_shot_anh.py --check XX   # CỔNG trước khi dựng: bảng còn khớp bg_jobs + kịch bản? mọi ảnh có file? exit 1 = TRƯỢT
Ra: 02_SAN_XUAT/Ho_So_Toi_Pham/TapXX/Bang_Shot_Anh_TapXX.md + .work/shot_map_tapXX.json
1 job = 1 shot = 1 ảnh (mỗi ảnh đúng 1 lần -> không lặp). Thời lượng là ƯỚC LƯỢNG (3,6 tiếng/s + nghỉ 0,45 s/câu); thời lượng thật lấy từ timeline sau khi có audio.
"""
import glob, importlib.util, json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]; WORK = ROOT / ".work"
spec = importlib.util.spec_from_file_location("pk", WORK / "parse_kichban.py")
pk = importlib.util.module_from_spec(spec); spec.loader.exec_module(pk)
DEFAULT = [n for n in range(26, 69) if n not in (64, 66, 68)]   # 64/66/68: kịch bản chưa mở rộng, để nguyên
SPS, PAUSE = 3.6, 0.45

def script_file(n):
    fs = [f for f in glob.glob(str(ROOT / f"01_KICH_BAN/Ho_So_Toi_Pham/Tap{n:02d}/kichban_tap{n:02d}_*.md")) if not re.search(r"_cu|_EN|_JA|_KO|backup", f)]
    return sorted(fs)[-1]

def build(n):
    """Gán theo TỪNG CÂU: câu -> job liệt kê nó (nhiều job -> job có mã gần nhất trong cùng cụm; thiếu -> job liền trước).
    Shot = đoạn câu liên tiếp cùng một ảnh. Ảnh xuất hiện >1 đoạn bị báo."""
    els = pk.parse_file(script_file(n))
    order, text, act = [], {}, {}
    for e in els:
        for s in e.get("sentences") or []:
            order.append(s["id"]); text[s["id"]] = s; act[s["id"]] = e["act"]
    pos = {c: i for i, c in enumerate(order)}
    jobs = json.load(open(WORK / f"bg_jobs_tap{n:02d}.json", encoding="utf-8"))
    own, desc, issues = {}, {}, []
    for j in jobs:
        desc[j["name"]] = j.get("desc", "")
        for c in re.split(r"[,;s]+", str(j.get("sentences", ""))):
            if c in pos: own.setdefault(pos[c], []).append(j["name"])
    multi = {p: o for p, o in own.items() if len(o) > 1}
    # ảnh "neo" của mỗi câu: với câu nhiều chủ, chọn job có CÂU LIỀN KỀ cùng job (hàng xóm) nhiều nhất
    def pick(p, cands):
        sc = []
        for c in cands:
            k = sum(1 for d in (-2, -1, 1, 2) if (p + d) in own and own[p + d] == [c])
            sc.append((-k, 0, c))
        return sorted(sc)[0][2]
    for p, o in sorted(multi.items()):
        issues.append(f"câu {order[p]} có {len(o)} ảnh {o} -> chọn 1")
        own[p] = [pick(p, o)]
    seq, last = [], None
    for p in range(len(order)):
        if p in own: last = own[p][0]
        elif last is None: issues.append(f"câu {order[p]} chưa có ảnh"); continue
        else: issues.append(f"câu {order[p]} không job nào liệt kê -> dùng ảnh liền trước"); 
        seq.append((p, last))
    rows = []
    for p, nm in seq:
        if rows and rows[-1]["name"] == nm and rows[-1]["last"] == p - 1 and act[order[p]] == rows[-1]["act"]:
            rows[-1]["last"] = p
        else:
            rows.append({"name": nm, "first": p, "last": p, "act": act[order[p]], "desc": desc[nm]})
    cnt = {}
    for i, r in enumerate(rows):
        r["id"] = f"{r['act']}-{i+1:03d}"
        r["n"] = r["last"] - r["first"] + 1
        r["codes"] = order[r["first"]:r["last"] + 1]
        w = sum(text[c]["words"] for c in r["codes"])
        r["est"] = round(w / SPS + PAUSE * r["n"], 1)
        r["span"] = f"{order[r['first']]} – {order[r['last']]}" if r["n"] > 1 else order[r["first"]]
        cnt.setdefault(r["name"], []).append(r["id"])
        if r["est"] > 15: issues.append(f"{r['id']}: ước {r['est']} s > 15 s (H10)")
        if r["est"] > 30: issues.append(f"{r['id']}: ước {r['est']} s > 30 s (H22)")
    for nm, ids in cnt.items():
        if len(ids) > 1: issues.append(f"LẶP ẢNH {nm} ở các shot {ids}")
    unused = [j["name"] for j in jobs if j["name"] not in cnt]
    if unused: issues.append(f"{len(unused)} ảnh không shot nào dùng: {unused[:3]}")
    return rows, issues, len(order)

def check(n):
    """Cổng dựng video: shot_map trên đĩa == bản dựng lại từ bg_jobs + kịch bản hiện tại; 0 lỗi mapping; mọi ảnh có file."""
    rows, issues, ns = build(n)
    crit = [i for i in issues if "H10" not in i and "H22" not in i]
    cur = [{k: r[k] for k in ("id", "act", "name", "codes", "est")} for r in rows]
    try: disk = json.load(open(WORK / f"shot_map_tap{n:02d}.json", encoding="utf-8"))
    except Exception: disk = None
    stale = disk != cur
    miss = [r["name"] for r in rows if not (ROOT / "assets/bg" / f"{r['name']}.png").exists()]
    ok = not crit and not stale and not miss
    print(f"Tập {n:02d}: {'ĐẠT' if ok else 'TRƯỢT'} · {len(rows)} shot · lỗi mapping {len(crit)} · bảng cũ/lệch {'CÓ' if stale else 'không'} · ảnh thiếu file {len(miss)}")
    for c in crit[:10]: print("    ", c)
    if stale: print("     -> chạy lại: py -3 .work/map_shot_anh.py", n)
    for m in miss[:10]: print("     thiếu ảnh:", m)
    return ok

def make_shots(n, lang="vi", timeline=None, out=None, endcard=None, allow_missing=False):
    """Tạo shots_tXX.json (ĐỦ khoá như parse_shots.py) cho build_video3.py TỪ bảng mapping + timeline_s ĐO THẬT.
    Ảnh của mỗi shot = ảnh trong Bang_Shot_Anh_TapXX.md. Thẻ kết (H12): dùng --endcard NAME, mặc định mượn ảnh shot cuối (cảnh báo)."""
    rows, issues, ns = build(n)
    crit = [i for i in issues if "H10" not in i and "H22" not in i]
    if crit: sys.exit("CỔNG H28 TRƯỢT — lỗi mapping, sửa trước: " + "; ".join(crit[:5]))
    suf = {"vi": "", "en": "_EN", "ja": "_JA"}[lang]
    tl_path = Path(timeline) if timeline else WORK / f"timeline_s{suf}_t{n:02d}.json"
    if not tl_path.exists(): sys.exit(f"CHƯA CÓ timeline đo thật: {tl_path} (cần audio master trước — T20/H14)")
    TL = json.load(open(tl_path, encoding="utf-8"))
    st = {i["id"]: i for i in TL["items"]}
    lost = [c for r in rows for c in r["codes"] if c not in st]
    if lost: sys.exit(f"timeline thiếu {len(lost)} mã câu của bảng mapping (kịch bản {lang} lệch bản VN): {lost[:5]}")
    ids = [i["id"] for i in TL["items"]]
    flat = [c for r in rows for c in r["codes"]]
    if flat != [c for c in ids if c in set(flat)]: sys.exit("thứ tự câu trong timeline khác bảng mapping")
    miss = [r["name"] for r in rows if not (ROOT / "assets/bg" / f"{r['name']}.png").exists()]
    if miss and not allow_missing: sys.exit(f"CỔNG H28 TRƯỢT — {len(miss)} ảnh chưa có file (vd {miss[0]}); sinh ảnh trước hoặc --allow-missing để thử")
    cams = ("push", "pull", "pan")
    shots = []
    for i, r in enumerate(rows):
        start = st[r["codes"][0]]["start"] - (0.2 if i == 0 else 0)
        shots.append({"id": r["id"], "act": r["act"], "start": round(start, 3), "end": 0, "role": None, "sentences": r["codes"],
                      "template": None, "variant": "", "bg": r["name"], "bg2": None, "inset": None, "camera": cams[i % 3],
                      "segments": [], "beats": [], "beat_text": "",
                      "flags": {"bust": False, "nobust": False, "intro": False, "handoff": [], "dual": False, "guests": False, "p2": False},
                      "hold": False, "transition": "dissolve"})
    ec = endcard or rows[-1]["name"]
    if not (ROOT / "assets/bg" / f"{ec}.png").exists() and not allow_missing: sys.exit(f"ảnh thẻ kết thiếu file: {ec}")
    shots.append({**{k: v for k, v in shots[-1].items()}, "id": f"{rows[-1]['act']}-{len(rows)+1:03d}", "start": round(st[ids[-1]]["end"], 3),
                  "sentences": [], "bg": ec, "camera": "still", "transition": "dissolve", "act": rows[-1]["act"]})
    for i, sh in enumerate(shots): sh["end"] = shots[i + 1]["start"] if i + 1 < len(shots) else TL["total"]
    for sh in shots:
        if sh["end"] <= sh["start"]: sh["end"] = round(sh["start"] + 0.3, 3)
    dst = Path(out) if out else WORK / f"shots{suf}_t{n:02d}.json"
    json.dump({"total": TL["total"], "shots": shots}, open(dst, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    d = [sh["end"] - sh["start"] for sh in shots]
    print(f"Tập {n:02d} [{lang}]: {len(shots)} shot (gồm 1 thẻ kết) -> {dst.name} · min {min(d):.1f}s max {max(d):.1f}s · >15s: {sum(x>15 for x in d)} · >30s: {sum(x>30 for x in d)} · thẻ kết dùng ảnh {ec}" + ("" if endcard else " (MƯỢN ảnh shot cuối — nên truyền --endcard)"))


def main():
    if sys.argv[1:2] == ["--shots"]:
        import argparse
        ap = argparse.ArgumentParser(); ap.add_argument("--shots", action="store_true"); ap.add_argument("ep", type=int)
        ap.add_argument("--lang", default="vi"); ap.add_argument("--timeline"); ap.add_argument("--out"); ap.add_argument("--endcard"); ap.add_argument("--allow-missing", action="store_true")
        a = ap.parse_args(); make_shots(a.ep, a.lang, a.timeline, a.out, a.endcard, a.allow_missing); return
    if sys.argv[1:2] == ["--check"]:
        sys.exit(0 if all([check(int(a)) for a in sys.argv[2:]]) else 1)
    eps = [int(a) for a in sys.argv[1:]] or DEFAULT
    for n in eps:
        rows, issues, ns = build(n)
        have = sum((ROOT / "assets/bg" / f"{r['name']}.png").exists() for r in rows)
        tot = sum(r["est"] for r in rows)
        crit = [i for i in issues if "H10" not in i and "H22" not in i]
        longs = [i for i in issues if "H10" in i or "H22" in i]
        nrep = sum(1 for i in crit if i.startswith("LẶP"))
        nuniq = len({r["name"] for r in rows})
        d = ROOT / f"02_SAN_XUAT/Ho_So_Toi_Pham/Tap{n:02d}"
        L = [f"# BẢNG MAPPING SHOT ↔ ẢNH NỀN · TẬP {n:02d}", "",
             f"- Nguồn: `.work/bg_jobs_tap{n:02d}.json` + kịch bản VN hiện tại · **{len(rows)} shot · {nuniq} ảnh khác nhau · ảnh bị dùng lặp ở >1 shot: {nrep}** · phủ {ns}/{ns} câu",
             f"- Ảnh đã có file `assets/bg/`: **{have}/{len(rows)}** · Tổng thời lượng ƯỚC LƯỢNG: {tot/60:.1f} phút (chỉ để tham khảo; thời lượng thật lấy từ `timeline_s` sau khi có audio, H14)",
             f"- **LUẬT DỰNG (AGENTS.md H28):** AI dựng video PHẢI đọc file này (hoặc `.work/shot_map_tap{n:02d}.json`) và dùng **đúng ảnh ở cột Tên ảnh cho đúng câu ở cột Câu** — CẤM tự chọn ảnh theo chủ đề, CẤM lặp ảnh, CẤM đổi thứ tự. Trước khi dựng chạy `py -3 .work/map_shot_anh.py --check {n:02d}` phải ĐẠT.",
             f"- Cách dùng: dựng theo đúng thứ tự dòng; shot bắt đầu ở câu đầu của cột Câu và kéo tới hết câu cuối; ảnh = cột Tên ảnh.",
             f"- Lỗi mapping (cần xử lý): {len(crit)}" + ("" if not crit else " — " + "; ".join(crit[:20])),
             f"- Shot dài ước > 15 s (H10, chỉ ước lượng — kiểm lại khi có timeline): {sum('H10' in i for i in longs)} · > 30 s (H22): {sum('H22' in i for i in longs)}", "",
             "| Shot | Hồi | Câu (đầu – cuối) | Số câu | Ước (s) | Tên ảnh (`assets/bg/<tên>.png`) | Có file | Mô tả cảnh |", "|---|---|---|---|---|---|---|---|"]
        for r in rows:
            ok = "✅" if (ROOT / "assets/bg" / f"{r['name']}.png").exists() else "⏳"
            L.append(f"| {r['id']} | {r['act']} | `{r['span']}` | {r['n']} | {r['est']} | `{r['name']}` | {ok} | {r['desc'].replace('|','/')} |")
        (d / f"Bang_Shot_Anh_Tap{n:02d}.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
        json.dump([{k: r[k] for k in ("id", "act", "name", "codes", "est")} for r in rows], open(WORK / f"shot_map_tap{n:02d}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        mx = max(r["est"] for r in rows)
        print(f"Tập {n:02d}: {len(rows)} shot · {have} có file · tổng ~{tot/60:.1f} ph · max {mx:.0f} s · >15s: {sum(r['est']>15 for r in rows)} · LỖI {len(crit)} (lặp ảnh {nrep}) · >30s {sum('H22' in i for i in longs)}")
        for s_ in crit[:20]: print("    ", s_)

main()
