import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
FORB_VN = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập", "đầu độc",
            "diệt cỏ", "bỏ đói", "móc áo", "đồ lót", "quan hệ tình dục", "hiếp", "cưỡng ép"]
SAFE_VN = ["ung thư máu", "đấu tập", "bàn tay", "cánh tay", "đầu tư", "đầu học", "đầu tiên",
           "đầu não", "trọng đầu", "bầu cửa", "bầu trời", "đập đầu", "trói buộc"]
FORB_EN = ["blood", "corpse", "strangle", "choke", "struggle", "raped", "rape",
           "underwear", "sexual intercourse", "orgasm", "penis", "vagina", "suffocat",
           "mutilat", "dismember", "torture"]
SAFE_EN = ["blood type", "blood pressure", "blood vessel", "bloodstream", "blood cell",
           "struggle to survive", "struggled to"]

files = {
    "VN": ROOT / "02_SAN_XUAT" / "Tap08" / "KeHoach_Video_Tap08.md",
    "EN": ROOT / "02_SAN_XUAT" / "Tap08_EN" / "KeHoach_Video_Tap08_EN.md",
    "JA": ROOT / "02_SAN_XUAT" / "Tap08_JA" / "KeHoach_Video_Tap08_JA.md",
}
for lang, p in files.items():
    forb = FORB_EN if lang == "EN" else FORB_VN
    safe = SAFE_EN if lang == "EN" else SAFE_VN
    text = p.read_text(encoding="utf-8")
    i = text.find("## 6. DANH SÁCH SHOT")
    for line in text[i:].splitlines():
        m = re.match(r"\|\s*([1-5]-\d+)\s*\|", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        chu = cells[5] if len(cells) > 5 else ""
        low = chu.lower()
        for w in forb:
            if not re.search(r"(?<!\w)" + r"\s+".join(re.escape(x) for x in w.split()) + r"(?!\w)", low):
                continue
            if any(g in low for g in safe if g in w or w in g):
                continue
            print(f"[{lang}] {m.group(1)}: tu cam “{w}”  →  {chu[:150]}")
print("xong")
