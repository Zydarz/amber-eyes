# -*- coding: utf-8 -*-
"""Bổ sung lớp bass điện tử cho T29 Hồi 1.

Lý do: sau khi sửa T29 H2 (ambient_deep -> cello_sad), H1 và H2 cùng dùng
bgm_cello_sad.mp3 -> mất tương phản chuyển hồi. Kịch bản 1.01 của T29 ghi
"Tiếng đàn Cello u uất, kết hợp với tiếng bass điện tử âm ỉ" -> cần 2 lớp.

Chạy:  py -3 .work/_patch_bgm_beds.py
"""
import pathlib
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORK = pathlib.Path(__file__).resolve().parents[1] / ".work"
EP = WORK / "edition.py"
NEW = {("29", 1): '("bgm_cello_sad.mp3", "bgm_sub_drone.mp3")'}

src = EP.read_text(encoding="utf-8")
bak = WORK / "_cu" / f"edition.py.bak_bgm_{time.strftime('%y%m%d_%H%M%S')}"
bak.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(EP, bak)
print(f"SAO LUU: {bak}")

ep_re = re.compile(r'^\s{4}"(\d\d)":\s*\{', re.M)
out = src
for ep in sorted({k[0] for k in NEW}):
    ep_pos = [(m.group(1), m.start(), m.end()) for m in ep_re.finditer(out)]
    idx = next(i for i, x in enumerate(ep_pos) if x[0] == ep)
    s = ep_pos[idx][2]
    end = ep_pos[idx + 1][1] if idx + 1 < len(ep_pos) else len(out)
    chunk = out[s:end]
    i0 = chunk.index("{", chunk.find('"bed":'))
    depth, j = 0, i0
    while j < len(chunk):
        if chunk[j] == "{":
            depth += 1
        elif chunk[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    lit = chunk[i0:j + 1]
    for (k_ep, act), val in NEW.items():
        if k_ep != ep:
            continue
        m = re.search(rf'(?<![\w.]){act}: (?:"[^"]*"|\([^()]*\))', lit)
        if not m:
            raise SystemExit(f"T{ep} H{act}: khong khop")
        print(f"  T{ep} H{act}: {m.group(0)}  ->  {act}: {val}")
        lit = lit[:m.start()] + f"{act}: {val}" + lit[m.end():]
    out = out[:s + i0] + lit + out[s + j + 1:]

EP.write_text(out, encoding="utf-8")
print(f"DA GHI: {EP}")

sys.path.insert(0, str(WORK))
for m in list(sys.modules):
    if m == "edition":
        del sys.modules[m]
import edition  # noqa: E402

print("\nKIEM TRA RUNTIME:")
for ep in ("29",):
    print(f"  T{ep}: {edition.EPISODES[ep]['bed']}")
