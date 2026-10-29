#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B5 — turn the shot table (plan v9 section 6) into .work/shots.json.

Every row -> {id, start, end, act, role, template, variant, bg, bg2, camera,
              segments[], beats[], flags{}, transition}
Times come only from .work/timeline_s.json (measured audio).
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402  (AE_LANG=en -> English edition)

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
PLAN = ED.PLAN
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SENT = {it["id"]: it for it in TL["items"]}
MARK = {m.get("id"): m for m in TL["markers"] if m.get("id")}
ACTS = [m for m in TL["markers"] if m["type"] == "ACT"]
BG_FILES = {p.stem for p in (ROOT / "assets" / "bg").glob("*.png")}

COMBO = ED.EP["combo"]      # shots whose plan cell is "background + silhouette" -> generated combined scene
INSET = ED.EP["inset"]      # small picture pinned on the board
BG2 = ED.EP["bg2"]          # crossfade within the shot
ALIASES = {"wheelchair_room": "wheelchair_room", "evidence": "records", "casefile": "records",
           "red": "void", "dark": "void"}


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def sent_range(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


def parse_text(cell):
    """Split on ' → ' into timed segments; inside: **bold**, *italic*, “quote”."""
    segs = []
    # an arrow inside **bold**, *italic* or “quote” is part of the text, not a beat separator
    cell = re.sub(r"\*\*.+?\*\*|\*[^*]+?\*|“.+?”", lambda m: m.group(0).replace("→", "⟶"), cell)
    for raw in re.split(r"\s+→\s+", cell):
        raw = raw.replace("⟶", "→")
        at = None
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?\s*(.*)", raw)
        if m:
            at, raw = int(m.group(1)), m.group(2)
        elems = []
        for tok in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", raw):
            if tok.group(1):
                elems.append(("bold", tok.group(1)))
            elif tok.group(2):
                elems.append(("ital", tok.group(2)))
            else:
                elems.append(("quote", tok.group(3)))
        if elems:
            segs.append({"at_sentence": at, "elems": elems})
    return segs


def main():
    text = PLAN.read_text(encoding="utf-8")
    # the real heading / end marker start a line (the standard part only quotes them)
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
    sec = text[m.end():]
    sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
    rows = [cells(l) for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
    shots = []
    first_voice = TL["items"][0]["start"]
    end_voice = TL["items"][-1]["end"]
    for r in rows:
        sid, cau, vai, mau, nen, chu, beat, nv, tr = (r + [""] * 9)[:9]
        act = int(sid.split("-")[0])
        sents = sent_range(cau)
        if sents:
            start = SENT[sents[0]]["start"] - 0.20
            end = SENT[sents[-1]]["end"]
        elif "chuyển hồi" in cau:
            m = next(a for a in ACTS if a["act"] == act + 1)
            start, end = m["start"], m["end"]
        elif sid == "1-00":
            start, end = 20.5, first_voice - 0.20
        elif r is rows[-1]:                      # dòng cuối: từ hết lời tới hết tập
            start, end = end_voice, TL["total"]
        else:
            codes = re.findall(r"`(\d\.\d+)`", cau)
            ms = [MARK[c] for c in codes if c in MARK and "start" in MARK[c]]
            if not ms:
                raise SystemExit(f"không tìm thấy mốc cho {sid}: {cau}")
            start, end = ms[0]["start"], ms[-1]["end"]
        tm = re.search(r"T(\d+)", mau)
        template = f"T{tm.group(1)}" if tm else None
        variant = ("strike" if "gạch bỏ" in mau else "flags" if "cờ" in mau else
                   "testimony" if "lời kể" in mau else "date" if "ngày" in mau else
                   "compare" if "so sánh" in mau else "")
        codes = re.findall(r"`([a-z_0-9]+)`", nen)
        bg = COMBO.get(sid) or next((ALIASES.get(c, c) for c in codes if ALIASES.get(c, c) in BG_FILES), None)
        if bg is None and template == "T10":
            bg = "void"
        if bg is None and not template:
            bg = None                           # "giữ" rows inherit the previous shot
        cam = ("hero" if "hero" in mau else "pull" if "`pull`" in nen else "pan" if "`pan`" in nen
               else "still" if "`still`" in nen else "push")
        flags = {"bust": "🅑" in nv, "nobust": "⊘" in nv, "intro": "✦" in nv,
                 "handoff": re.findall(r"→([A-Z0-9+]+)", nv), "dual": "hai badge" in nv,
                 "guests": "dàn khách mời" in nv, "p2": "P2" in nv}
        hold = (not sents) and template is None
        shots.append({"id": sid, "act": act, "start": round(start, 3), "end": round(end, 3),
                      "role": vai[:2].strip() if vai and vai != "—" else None, "sentences": sents,
                      "template": template, "variant": variant, "bg": bg, "bg2": BG2.get(sid),
                      "inset": INSET.get(sid),
                      "camera": cam, "segments": parse_text(chu),
                      "beats": re.findall(r"ở \"([^\"]+)\"", beat), "beat_text": beat,
                      "flags": flags, "hold": hold,
                      "transition": "cut" if "✂" in tr else "dip" if "◼" in tr else "dissolve"})
    # contiguous: each shot lasts until the next starts; holds inherit bg/template
    for i, s in enumerate(shots):
        if i + 1 < len(shots):
            s["end"] = shots[i + 1]["start"]
        if s["hold"] and i > 0:
            p = shots[i - 1]
            s.update({k: p[k] for k in ("bg", "bg2", "template", "variant", "segments", "camera")})
            s["inherit"] = p["id"]
        if s["bg"] is None and i > 0:           # "camera dời tới thẻ 1", "cờ 2"… keep the scene
            s["bg"] = shots[i - 1]["bg"]
            s["bg_inherited"] = True
        if s["bg"] is None:
            raise SystemExit(f"thiếu nền cho {s['id']}")
    ED.w("shots.json").write_text(json.dumps({"total": TL["total"], "shots": shots},
                                                ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(shots), "shot · dài nhất",
          max((round(s['end'] - s['start'], 1), s['id']) for s in shots),
          "· ngắn nhất", min((round(s['end'] - s['start'], 1), s['id']) for s in shots))
    missing = sorted({s["bg"] for s in shots} - BG_FILES)
    print("nền chưa có file:", missing)


if __name__ == "__main__":
    main()
