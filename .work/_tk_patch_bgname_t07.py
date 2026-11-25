# -*- coding: utf-8 -*-
"""Doi token nen TikTok Tap 07: t7_* (anh 16:9 goc) -> tk07_* (anh doc 9:16).

Tach H22: t7_digital_lighthouse_beacon bi 4 shot (TK1#2, TK5#1, TK5#2, TK5#8)
=> tach 2 + 2 bang 2 GOC QUAY khac nhau:
     TK1.01#2, TK5.01#2  -> tk07_digital_lighthouse_beacon
     TK5.01#1, TK5.01#8  -> tk07_digital_lighthouse_beacon_wide

Ghi 6 file: 3 KE_HOACH_CLIP (md) + 3 SPEC_AUDIO_CLIP (json). Script chay lai duoc (idempotent).
"""
import json
import pathlib
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
TIK = ROOT / "02_SAN_XUAT" / "TIKTOK"
sys.path.insert(0, str(HERE))
from _tk_src_t07 import PAIRS  # noqa: E402

# nen doc 9:16 <- token 16:9 goc (dien giai tu ten)
TOK = {n.replace("tk07_", "t7_"): n for n, _ in PAIRS}
TOK["t7_digital_lighthouse_beacon"] = "tk07_digital_lighthouse_beacon"

# theo ma cau: nen thay the cho phong hai
BY_LINE = {
    "TK1.01#2": "tk07_digital_lighthouse_beacon",
    "TK5.01#1": "tk07_digital_lighthouse_beacon_wide",
    "TK5.01#2": "tk07_digital_lighthouse_beacon",
    "TK5.01#8": "tk07_digital_lighthouse_beacon_wide",
}

CODE_RE = re.compile(r"TK\d\.01#\d+")


def new_bg(line_code, old):
    if old == "t7_digital_lighthouse_beacon" and line_code in BY_LINE:
        return BY_LINE[line_code]
    return TOK.get(old, old)


def patch_md(p):
    txt = p.read_text(encoding="utf-8-sig")
    out = []
    n = 0
    for line in txt.splitlines(keepends=True):
        m = CODE_RE.search(line)
        code = m.group(0) if m else None
        # PHONG HAI: tach H22 truoc, de len generic khong ghi de
        if code and code in BY_LINE and "t7_digital_lighthouse_beacon" in line:
            line = line.replace("t7_digital_lighthouse_beacon", BY_LINE[code])
            n += 1
        for old, new in TOK.items():
            pat = re.compile(r"(?<![\w])" + re.escape(old) + r"\b")
            if pat.search(line):
                line = pat.sub(new, line)
                n += 1
        out.append(line)
    p.write_text("".join(out), encoding="utf-8")
    return n


def patch_json(p):
    spec = json.loads(p.read_text(encoding="utf-8-sig"))
    n = 0
    for c in spec["clips"].values():
        for ln in c["lines"]:
            new = new_bg(ln["code"], ln["bg"])
            if new != ln["bg"]:
                ln["bg"] = new
                n += 1
    p.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    return n


def main():
    bak = HERE / "_cu" / ("tk07_patch_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)

    targets = [
        ("Tap07", "KE_HOACH_CLIP_TAP07.md", patch_md),
        ("Tap07_EN", "KE_HOACH_CLIP_TAP07_EN.md", patch_md),
        ("Tap07_JA", "KE_HOACH_CLIP_TAP07_JA.md", patch_md),
        ("Tap07", "SPEC_AUDIO_CLIP_TAP07.json", patch_json),
        ("Tap07_EN", "SPEC_AUDIO_CLIP_TAP07.json", patch_json),
        ("Tap07_JA", "SPEC_AUDIO_CLIP_TAP07.json", patch_json),
    ]
    for d, fn, func in targets:
        p = TIK / d / fn
        shutil.copy2(p, bak / ("%s__%s" % (d, fn)))
        n = func(p)
        print("%-34s -> %d dong doi token" % (d + "/" + fn, n))
    print("\nbackup:", bak)

    # kiem tra con token t7_*?
    left = 0
    for d, fn, _ in targets:
        p = TIK / d / fn
        left += len(re.findall(r"(?<![\w])t7_[a-z0-9_]+", p.read_text(encoding="utf-8-sig")))
    print("token t7_* con lai:", left)


if __name__ == "__main__":
    main()
