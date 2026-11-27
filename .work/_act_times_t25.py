# -*- coding: utf-8 -*-
"""Trich moc chuong THAT cho Tap25 (VN/EN/JA) tu SRT + canh gioi, luu JSON.

T25 chua co timeline_s_t25*.json (chi co Tap23/T24), nen moc chuong duoc
do truc tiep tu phu de (SRT) + bao cao nghe (CanNghe_Tap25_higgs.md).
VN: lay tu CanNghe (230 dong, co moc gioi tung cau).
EN/JA: khop cau dau moi ho voi SRT.
KO: chua co audio -> dung uoc luong.
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")


def first_sentence_of_act(script_path, act_re):
    out, cur = {}, None
    for ln in script_path.read_text(encoding="utf-8").splitlines():
        m = re.match(act_re, ln)
        if m:
            cur = int(m.group(1))
            continue
        if cur is None or cur in out:
            continue
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith("---"):
            continue
        if s.startswith("**["):
            continue
        if s.startswith("**") and s.endswith("):"):
            continue
        if s.startswith("**") and ":" in s:
            s = s.split(":", 1)[1].strip()
        if not s:
            continue
        out[cur] = s
    return out


def srt_cues(p):
    raw = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    cues = []
    for blk in re.split(r"\n\s*\n", raw):
        mm = re.search(r"(\d\d):(\d\d):(\d\d),(\d\d\d) --> (\d\d):(\d\d):(\d\d),(\d\d\d)", blk)
        if not mm:
            continue
        g = [int(x) for x in mm.groups()]
        start = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        txt = " ".join(l for l in blk.splitlines()
                       if not re.match(r"^\d+$", l) and "-->" not in l)
        txt = re.sub(r"\[[^\]]*\]", "", txt)
        cues.append((start, txt))
    return cues


def norm(t):
    return re.sub(r"[\s\u3000]+", "", unicodedata.normalize("NFKC", t).lower())


def match(cues, sentence):
    ns = norm(sentence)
    for k in (45, 35, 28, 20, 15):
        for off in range(0, max(1, len(ns) - k + 1), 5):
            key = ns[off:off + k]
            for start, txt in cues:
                if key in norm(txt):
                    return start
    return None


def vn_from_cannghe():
    p = (ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap25" / "xuat_ban" /
         "CanNghe_Tap25_higgs.md")
    starts = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+):(\d{2})\.(\d{2})\s*\|\s*(\d)\.(\d{2})#\d+\s*\|",
                     line)
        if not m:
            continue
        mm, ss, cs, act = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        t = mm * 60 + ss + cs / 100
        starts.setdefault(act, t)
    return starts


def mmss(t):
    total = int(t + 0.5)
    return f"{total // 60:02d}:{total % 60:02d}"


def main():
    out = {}
    vn = vn_from_cannghe()
    out["VN"] = {a: vn[a] for a in sorted(vn)}
    print("VN (tu CanNghe):", {a: mmss(v) for a, v in out["VN"].items()})

    specs = [
        ("EN", ROOT / "01_KICH_BAN/Ho_So_Toi_Pham/Tap25_EN/kichban_tap25_EN.md",
         r"^## ACT (\d)",
         ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap25_EN/xuat_ban/Tap25_EN.srt"),
        ("JA", ROOT / "01_KICH_BAN/Ho_So_Toi_Pham/Tap25_JA/kichban_tap25_JA.md",
         r"^## 第(\d)幕",
         ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap25_JA/xuat_ban/Tap25_JA.srt"),
    ]
    for lang, sp, are, srtp in specs:
        acts = first_sentence_of_act(sp, are)
        cues = srt_cues(srtp)
        res = {}
        for a in sorted(acts):
            t = match(cues, acts[a])
            res[a] = t
        out[lang] = res
        print(f"{lang}:", {a: (mmss(v) if v else None) for a, v in res.items()},
              "| srt cues", len(cues), "last", mmss(cues[-1][0]))

    # KO: chua co master -> uoc luong theo ti le thoi luong EN
    out["KO"] = None
    p = ROOT / ".work" / "_act_times_t25.json"
    p.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print("saved ->", p)


if __name__ == "__main__":
    main()
