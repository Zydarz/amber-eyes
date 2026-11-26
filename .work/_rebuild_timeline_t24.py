#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap24 — DỰNG LẠI timeline_s từ SRT + master audio (audio đã dựng xong ở máy khác).

Vì .work/timeline_s_t24*.json không tồn tại (audio làm trên Mac, chỉ copy về master + SRT),
ta dựng lại timeline TỪ SRT theo đúng thuật toán subtitles.py (ngược):
  - subtitles.py: item -> split_text(text) -> parts; part k có thời lượng d*len(p)/total
  - => start của cue đầu tiên của MỌI CÂU = item.start (chính xác)
  - => start của part k (k>=1) = item.start + d*cum_k/total_len  => suy ra d

KIỂM CHỨNG: chạy lại subtitles.py rồi so SRT mới với SRT gốc (phải khớp từng cue).
"""
import json, os, re, sys, subprocess, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

INTRO = 22.41
FIRST_VOICE = 23.0
GAP_ACT, GAP_SPEAKER, GAP_SENT, GAP_Q, MAX_PAUSE = 2.0, 0.65, 0.40, 0.60, 3.0
LANGS = [("vi", "Tap24", "Tap24.srt", "timeline_s_t24.json"),
         ("en", "Tap24_EN", "Tap24_EN.srt", "timeline_s_EN_t24.json"),
         ("ja", "Tap24_JA", "Tap24_JA.srt", "timeline_s_JA_t24.json")]

_state = {}


def load_ed(lang):
    """Nạp edition.py với đúng AE_EP/AE_LANG (cache theo lang)."""
    if lang not in _state:
        os.environ["AE_EP"] = "24"
        os.environ["AE_LANG"] = lang
        sys.modules.pop("edition", None)
        sys.path.insert(0, str(WORK))
        import edition as ED
        _state[lang] = ED
    return _state[lang]


def split_text(t, maxc, ja):
    """Bản sao nguyên văn của subtitles.split_text (tránh import vì nó đọc timeline lúc import)."""
    t = t.strip()
    if len(t) <= maxc:
        return [t]
    mid = len(t) / 2
    pattern = r"[,;:–—―…、。』」）\)]\s*" if ja else r"[,;:–—]\s*"
    cuts = [m.end() for m in re.finditer(pattern, t)
            if 0 < m.end() < len(t) and (not ja or 3 <= m.end() <= len(t) - 3)]
    if not cuts:
        cuts = [m.start() for m in re.finditer(r"\s", t) if 0 < m.start() < len(t)]
    if not cuts:
        cuts = [int(mid)]
    c = min(cuts, key=lambda k: abs(k - mid))
    left, right = t[:c].strip(), t[c:].strip()
    if not left:
        return split_text(right, maxc, ja)
    if not right:
        return split_text(left, maxc, ja)
    return split_text(left, maxc, ja) + split_text(right, maxc, ja)


def ts2s(s):
    h, m, rest = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(rest.replace(",", "."))


def parse_srt(p):
    t = p.read_text(encoding="utf-8-sig")
    out = []
    for b in re.split(r"\n\s*\n", t.strip()):
        ls = b.splitlines()
        if len(ls) < 2:
            continue
        m = re.match(r"(\d+:\d+:\d+[,.]\d+)\s*-->\s*(\d+:\d+:\d+[,.]\d+)", ls[1])
        if m:
            out.append((ts2s(m.group(1)), ts2s(m.group(2)), "\n".join(ls[2:]).strip()))
    return out


def master_dur(p):
    FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
    r = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return float(r.stdout.strip())


def build(lang, epdir, srtname, outname):
    ED = load_ed(lang)
    MAXC = 40 if ED.JA else 84
    JA = ED.JA
    TAG = ED.SUB_TAG
    NELEM = ED.EP["n_element"]
    script = json.loads(ED.SCRIPT_JSON.read_text(encoding="utf-8"))
    srt_p = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / epdir / "xuat_ban" / srtname
    cues = parse_srt(srt_p)
    master = master_dur(srt_p.with_name(srtname.replace(".srt", "_master.mp3")))

    def role_of(e):
        return NELEM.get(e["id"], e["role"])

    # ---- 1. danh sách câu + số part/cue
    items, ptr, prev_el = [], 0, None
    for e in script:
        if e["kind"] in ("BGM", "SFX", "NGHI"):
            continue
        role = role_of(e)
        for s in e["sentences"]:
            parts = split_text(s["text"], MAXC, JA)
            if e["id"] != prev_el:
                parts = split_text(parts[0], MAXC - len(TAG[role]) - 3, JA) + parts[1:]
            items.append({"id": s["id"], "element": e["id"], "act": e["act"], "role": role,
                          "text": s["text"], "parts": parts})
            prev_el = e["id"]

    need = sum(len(it["parts"]) for it in items)
    print(f"  cue SRT={len(cues)} · cần={need} · câu={len(items)}")
    if need != len(cues):
        raise SystemExit("  LỆCH số cue — dừng")

    # ---- 2. gán cue, suy thời lượng
    for it in items:
        grp = cues[ptr:ptr + len(it["parts"])]
        ptr += len(it["parts"])
        it["cues"] = grp
        it["start"] = grp[0][0]
        total_len = sum(len(p) for p in it["parts"])
        cum, est = 0, []
        for k, p in enumerate(it["parts"]):
            if k:
                # start(part k) = start + d * (tổng độ dài các part 0..k-1) / total_len
                est.append((grp[k][0] - grp[0][0]) * total_len / cum)
            cum += len(p)
        if est:
            it["dur"] = statistics.median(est)
        else:
            cd = grp[0][1] - grp[0][0]
            it["dur"] = cd if cd < 5.999 else None
        if it["dur"] is not None:
            it["end"] = it["start"] + it["dur"]

    unk = [it["id"] for it in items if it["dur"] is None]
    print(f"  câu chưa suy được thời lượng (cue ≥ 6 s bị cắt): {len(unk)} {unk[:8]}")

    # ---- 3. suy gap + PAUSE_AFTER
    pause_after, gaps = {}, {}
    last_in_el = set()
    for e in script:
        if "sentences" in e:
            last_in_el.add(e["sentences"][-1]["id"])
    for i, it in enumerate(items[:-1]):
        nxt = items[i + 1]
        if nxt["element"] == it["element"]:
            g = GAP_Q if it["text"].rstrip("”\" ").endswith("?") else GAP_SENT
        else:
            g = GAP_SPEAKER if nxt["role"] != it["role"] else GAP_SENT
            if it["text"].rstrip("”\" ").endswith("?"):
                g = max(g, GAP_Q)
        gaps[nxt["id"]] = g
        if it["dur"] is not None:
            pause_after[it["id"]] = round(nxt["start"] - it["end"] - g, 3)

    def med(v):
        return statistics.median(v) if v else 0.0
    grp_last = [v for k, v in pause_after.items() if k in last_in_el]
    grp_mid = [v for k, v in pause_after.items() if k not in last_in_el]
    p_last, p_mid = med(grp_last), med(grp_mid)
    print(f"  pause_after đã biết: cuối PT n={len(grp_last)} TB {p_last:.3f} · "
          f"giữa PT n={len(grp_mid)} TB {p_mid:.3f}")

    # "pitch" = khoảng cách giữa hết câu này và bắt đầu câu sau (thực nghiệm)
    pitch_last, pitch_mid = [], []
    for i, it in enumerate(items[:-1]):
        if it["dur"] is None:
            continue
        p = items[i + 1]["start"] - it["end"]
        (pitch_last if it["id"] in last_in_el else pitch_mid).append(p)
    P_last, P_mid = med(pitch_last), med(pitch_mid)
    print(f"  pitch thực nghiệm: cuối PT TB {P_last:.3f} · giữa PT TB {P_mid:.3f}")

    # câu chưa biết thời lượng (1 part, cue bị cắt 6 s): d = start(câu sau) - pitch
    for i, it in enumerate(items):
        if it["dur"] is not None:
            it["end"] = it["start"] + it["dur"]
            continue
        if i + 1 < len(items):
            p = P_last if it["id"] in last_in_el else P_mid
            it["dur"] = round(items[i + 1]["start"] - it["start"] - p, 3)
            it["est"] = True
        else:
            it["dur"] = 6.0
            it["est"] = True
        it["end"] = it["start"] + it["dur"]

    # ---- 4. markers + acts
    by_sent = {it["id"]: it for it in items}
    el_first = {}
    for e in script:
        if "sentences" in e:
            el_first[e["id"]] = by_sent[e["sentences"][0]["id"]]["start"]
    markers = [{"type": "INTRO", "start": 0.0, "end": INTRO}]
    acts, cur_act, t = {}, None, FIRST_VOICE
    for e in script:
        act = e["act"]
        if cur_act is not None and act != cur_act:
            st = el_first.get(e["id"])
            at_act = (st - GAP_ACT) if st is not None else t
            markers.append({"type": "ACT", "act": act, "start": round(at_act, 3),
                            "end": round(at_act + GAP_ACT, 3)})
            t = at_act + GAP_ACT
        cur_act = act
        if act not in acts:
            acts[act] = [t, t]
        if e["kind"] == "NGHI":
            sec = min(e["sec"], MAX_PAUSE)
            markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3),
                            "end": round(t + sec, 3), "desc": e.get("desc", "")})
            t += sec
        elif e["kind"] in ("SFX", "BGM"):
            markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3),
                            "desc": e.get("desc", "")})
        else:
            t = el_first[e["id"]]
            last = by_sent[e["sentences"][-1]["id"]]
            t = last["end"] + pause_after.get(last["id"], 0.0)
        acts[act][1] = t

    # mốc SFX/BGM giữa 2 phần tử thoại: "at" = start lời kế sau - gap
    order = [e["id"] for e in script if "sentences" in e]
    for m in markers:
        if m["type"] not in ("SFX", "BGM"):
            continue
        try:
            pos = next(i for i, e in enumerate(script) if e["id"] == m["id"])
        except StopIteration:
            continue
        for e2 in script[pos + 1:]:
            if "sentences" in e2:
                m["at"] = round(el_first[e2["id"]] - gaps.get(by_sent[e2["sentences"][0]["id"]]["id"], GAP_SENT), 3)
                break

    end_voice = items[-1]["end"] + pause_after.get(items[-1]["id"], 0.0)
    total = master          # đích: khớp đúng master audio (video phải dài bằng audio)
    acts[max(acts)][1] = round(end_voice, 3)

    tl = {"total": round(total, 3), "intro": INTRO,
          "items": [{"id": it["id"], "element": it["element"], "act": it["act"],
                     "role": it["role"], "start": round(it["start"], 3),
                     "end": round(it["end"], 3), "text": it["text"]} for it in items],
          "markers": markers,
          "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}}
    (WORK / outname).write_text(json.dumps(tl, ensure_ascii=False, indent=1), encoding="utf-8")
    pa = [v for v in pause_after.values() if v > -0.05]
    print(f"  total={total:.3f} (master {master:.3f}, lệch {total-master:+.3f}) · "
          f"lời đầu {items[0]['start']:.2f} · lời cuối {end_voice:.2f} · "
          f"pause_after>0: {len(pa)}/{len(pause_after)} · trung vị {statistics.median(pa):.3f}" if pa else "")
    return tl


if __name__ == "__main__":
    for lang, epdir, srt, out in LANGS:
        print(f"=== {lang.upper()} ===")
        build(lang, epdir, srt, out)
