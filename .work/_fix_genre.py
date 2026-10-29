# -*- coding: utf-8 -*-
from pathlib import Path
mp = Path(r"D:\TEST\Gax\Audi\.work\yt_map.tsv")
GEN = {
 "Death Rattle Breath": "Giọng của con người",
 "Battle Agony Moans": "Đám đông",
 "Voices Moaning": "Đám đông",
 "Quiet Whirring": "Phương tiện giao thông",
 "Paper Stacking": "Tiếng động thực tế",
 "Flipping Newspaper Pages": "Tiếng động thực tế",
 "Sheet Flap In Large Hall": "Tiếng động trong nhà",
 "Tweeter Electric Static": "Tiếng động thực tế",
 "Transporting A Camera": "Công cụ",
 "Ladle Food into Carton": "Tiếng động thực tế",
 "Voices Murmur": "Đám đông",
 "Voices Angry": "Đám đông",
}
lines = mp.read_text(encoding="utf-8-sig").splitlines()
out, n = [], 0
for l in lines:
    p = l.split("\t")
    if len(p) >= 6 and p[0].strip() in GEN:
        if p[4].strip() != GEN[p[0].strip()]:
            p[4] = GEN[p[0].strip()]; n += 1
        l = "\t".join(p)
    out.append(l)
mp.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"cap nhat the loai cho {n} dong")