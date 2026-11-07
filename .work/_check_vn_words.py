# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

parsed = PK.parse_file("01_KICH_BAN/Tap15/kichban_tap15_23102026.md")

ALLOWED_NON_VN = {
    "jodi", "arias", "travis", "alexander", "mesa", "arizona", "yreka", "cancun",
    "flores", "martinez", "esteban", "janeen", "demarte", "samuels", "maricopa",
    "perryville", "california", "utah", "las", "vegas", "redding", "debbie", "hughes",
    "bpd", "ptsd", "mo", "signature", "halo", "victimology", "sykes", "matza", "mormon",
    "sony", "cyber", "flash", "doctor", "borderline"
}

unusual = []
for el in parsed:
    if el["kind"] == "LOI":
        for s in el.get("sentences", []):
            txt = s["text"]
            raw_words = re.findall(r"[a-zA-ZàáảãạăằắẳẵặâầấẩẫậeèéẻẽẹêềếểễệiìíỉĩịoòóỏõọôồốổỗộơờớởỡợuùúủũụưừứửữựyỳýỷỹỵđĐ]+", txt)
            for w in raw_words:
                wl = w.lower()
                if any(c in wl for c in ["j", "w", "z", "f"]):
                    if wl not in ALLOWED_NON_VN:
                        unusual.append((s["id"], wl, txt))

print(f"Số từ chứa ký tự ngoại ngữ bất thường: {len(unusual)}")
for sid, w, txt in unusual:
    print(f"  [{sid}] '{w}': {txt}")
