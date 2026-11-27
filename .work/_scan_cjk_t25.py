# -*- coding: utf-8 -*-
"""Quet Han chu (Trung) la tron trong ban mo ta KO + kiem tra chu La/China cho JA."""
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
SAN = Path(r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Ho_So_Toi_Pham")

# Han chu hop le trong tieng Han (tu Hanja dung trong tieng Han hien dai — rat it)
KO_OK = set("死刑判決名書自首監獄警察事件記錄殺人傷害者")
# Han chu KHONG nen xuat hien trong tieng Nhat ban tap (ke ca tu Trung)
JA_BAD_HINTS = ["里", "這", "個", "們", "說", "來", "會", "對", "後", "過", "還", "從",
                "為", "與", "於", "發", "當", "樣", "種", "頭", "買", "賣", "車", "東", "西",
                "門", "風", "飛", "魚", "鳥", "雞", "馬", "門", "開", "關", "韓", "中", "國"]


def han_runs(text):
    out = []
    for m in re.finditer(r"[\u3400-\u9fff\u3040-\u30ff]+", text):
        out.append(m.group(0))
    return out


ko = (SAN / "Tap25_KO" / "description.txt").read_text(encoding="utf-8")
ko2 = re.sub(r"https?://\S+", " ", ko)
ko2 = re.sub(r"#[A-Za-z0-9]+", " ", ko2)
bad = []
for run in han_runs(ko2):
    for ch in run:
        if ch not in KO_OK and not ("\u3040" <= ch <= "\u30ff"):
            i = ko2.find(ch)
            bad.append((ch, ko2[max(0, i - 40):i + 40].replace("\n", " ")))
print(f"KO: {len(bad)} Han chu khong hop le (ke ca kanji Nhat/CJK la lan)")
for ch, ctx in bad[:15]:
    print(f"   '{ch}' :: {ctx}")

ja = (SAN / "Tap25_JA" / "description.txt").read_text(encoding="utf-8")
ja2 = re.sub(r"https?://\S+", " ", ja)
susp = []
for run in han_runs(ja2):
    for ch in run:
        if ch in JA_BAD_HINTS:
            i = ja2.find(ch)
            susp.append((ch, ja2[max(0, i - 35):i + 35].replace("\n", " ")))
print(f"\nJA: {len(susp)} Han chu canh bao (chu Trung/rac)")
for ch, ctx in susp[:15]:
    print(f"   '{ch}' :: {ctx}")

# Kiem tra lai tat ca ky tu Han trong JA de review nhanh
print("\nJA tat ca chuoi Han (de review):")
print("  " + " | ".join(sorted(set("".join(han_runs(ja2))))))
