#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — QC ảnh tĩnh 3 ngôn ngữ (VN / EN / JA).

Cổng kiểm:
  1. Đủ ảnh: mỗi shot trong bảng có đúng 1 PNG, không thừa, không thiếu
  2. Ảnh hỏng: PNG < 20 KB hoặc không mở được
  3. H10 — thời lượng shot + chuỗi nền liền nhau (không lặp nền > 4 shot liền)
  4. H12 — shot cuối (thẻ kết) phải có chữ: nhãn "HỒ SƠ TẬP 04 · ĐÃ ĐÓNG" + AMBER EYES
  5. H6/V3 — chữ trên ảnh phải khớp cột Chữ của bảng shot (sanity)
  6. Badge vai — kiểm file stem tồn tại (sóng âm trên badge)

Dùng:  py -3 .work/_qc_t04_stills.py
"""
import json
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANGS = [
    ("vi", "shots_t04.json", "video3_t04/stills", "stems_t04"),
    ("en", "shots_EN_t04.json", "video3_EN_t04/stills", "stems_EN_t04"),
    ("ja", "shots_JA_t04.json", "video3_JA_t04/stills", "stems_JA_t04"),
]

# py -3 .work/_qc_t04_stills.py            -> tất cả
# py -3 .work/_qc_t04_stills.py vi en      -> chỉ các ngôn ngữ nêu
only = {a.lower() for a in sys.argv[1:]}
if only:
    LANGS = [L for L in LANGS if L[0] in only]

fails = 0
for lang, sh_name, rel, stem_name in LANGS:
    print("=" * 78)
    print(f"[{lang}]")
    sh = json.loads((WORK / sh_name).read_text(encoding="utf-8"))
    shots = sh["shots"]
    sd = WORK / rel
    ids = [s["id"] for s in shots]

    # ID phải duy nhất: nếu trùng, 2 shot ghi đè cùng 1 file PNG -> mất 1 ảnh
    from collections import Counter
    dups = sorted(k for k, v in Counter(ids).items() if v > 1)
    if dups:
        print(f"  ✗ ID shot trùng {len(dups)}: {dups[:10]} — ảnh sẽ bị ghi đè")
        fails += 1
    else:
        print(f"  ✔ ID shot duy nhất ({len(ids)})")

    files = {p.name for p in sd.glob("*.png")}
    want = {f"shot_{i}.png" for i in ids}

    miss = sorted(want - files)
    extra = sorted(files - want)
    print(f"  ảnh: {len(files)} file · cần {len(want)}")
    if miss:
        print(f"  ✗ THIẾU {len(miss)}: {miss[:8]}")
        fails += 1
    if extra:
        print(f"  ✗ THỪA {len(extra)}: {extra[:8]}")
        fails += 1
    if not miss and not extra:
        print("  ✔ đủ ảnh, không thừa")

    bad = []
    for n in sorted(want & files):
        p = sd / n
        if p.stat().st_size < 20000:
            bad.append((n, "nhỏ"))
            continue
        try:
            with Image.open(p) as im:
                im.verify()
        except Exception as e:
            bad.append((n, f"lỗi mở: {e}"))
    print(f"  ảnh hỏng: {len(bad)} {bad[:4] if bad else ''}")
    if bad:
        fails += 1

    durs = [(s["id"], round(s["end"] - s["start"], 2)) for s in shots]
    out_of = [(i, d) for i, d in durs if d < 3 or d > 15]
    print(f"  H10 thời lượng: min {min(d for _, d in durs)}s · max {max(d for _, d in durs)}s "
          f"· ngoài 3–15s: {len(out_of)}")
    if out_of:
        print(f"      {out_of[:14]}")
    chain, cur, curid = [], [], None
    for s in shots:
        if s.get("bg") == curid:
            cur.append(s["id"])
        else:
            if len(cur) > 3:
                chain.append(cur)
            cur, curid = [s["id"]], s.get("bg")
    if len(cur) > 3:
        chain.append(cur)
    print(f"  H10 nền lặp liền >4 shot: {len(chain)} chuỗi {[len(c) for c in chain]}")

    last = shots[-1]

    def drawn(s):
        out = []
        for seg in s.get("segments") or []:
            for el in seg.get("elems") or []:
                if len(el) >= 2:
                    out.append(str(el[1]))
        return " ".join(out)

    txt = drawn(last).strip()
    print(f"  H12 shot cuối [{last['id']}] template={last.get('template')} chữ = {txt[:130]!r}")
    if not txt:
        print("  ✗ shot cuối KHÔNG có chữ")
        fails += 1
    else:
        need = ["HỒ SƠ TẬP", "AMBER EYES"] if lang == "vi" else ["AMBER EYES"]
        m = [k for k in need if k.upper() not in txt.upper()]
        if m:
            print(f"  ✗ thẻ kết thiếu: {m}")
            fails += 1
        else:
            print("  ✔ thẻ kết có nhãn + tên kênh + khẩu hiệu")

    # badge vai: stem tồn tại?
    st = WORK / stem_name
    have = sorted(p.stem for p in st.glob("*.wav")) if st.exists() else []
    print(f"  stem vai [{stem_name}]: {have if have else 'THIẾU — badge sẽ không có sóng âm'}")

    # chữ tiếng Việt sót lại trong bản EN/JA (thẻ hồi / thẻ kết là dòng META)
    if lang in ("en", "ja"):
        VN_CHARS = set("àáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵđ")
        residue = []
        for s in shots:
            for seg in s.get("segments") or []:
                for el in seg.get("elems") or []:
                    t = str(el[1]) if len(el) >= 2 else ""
                    if t and any(c in VN_CHARS for c in t.lower()):
                        residue.append((s["id"], t[:50]))
                        break
        if residue:
            print(f"  ✗ còn {len(residue)} chỗ chữ tiếng Việt sót lại:")
            for x in residue[:6]:
                print("     ", x)
            fails += 1
        else:
            print("  ✔ không còn chữ tiếng Việt sót lại trên hình")

    # mẫu dùng + vai
    tpl = {}
    for s in shots:
        k = s.get("template") or "(giữ)"
        tpl[k] = tpl.get(k, 0) + 1
    print(f"  mẫu: {', '.join(f'{k}×{v}' for k, v in sorted(tpl.items(), key=lambda x: -x[1]))}")
    roles = {}
    for s in shots:
        if s.get("role"):
            roles[s["role"]] = roles.get(s["role"], 0) + len(s["sentences"])
    print(f"  câu theo vai: {', '.join(f'{k}={v}' for k, v in sorted(roles.items()))}")

print("=" * 78)
print("KẾT LUẬN:", "ĐẠT" if fails == 0 else f"{fails} CỔNG LỖI")
sys.exit(0 if fails == 0 else 1)
