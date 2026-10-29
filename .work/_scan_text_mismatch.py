import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:\TEST\Gax\Audi")
shots = json.loads((ROOT / ".work" / "shots_t04.json").read_text(encoding="utf-8"))["shots"]
script = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8"))

sents_dict = {}
for e in script:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents_dict[s["id"]] = s["text"]

print("=" * 100)
print("RÀ SOÁT TẤT CẢ CÁC SHOT CÓ CHỮ TRÊN HÌNH SO VỚI LỜI ĐỌC (RULE H6)")
print("=" * 100)

for s in shots:
    sid = s["id"]
    segs = s.get("segments", [])
    s_sents = s.get("sentences", [])
    tmpl = s.get("template") or ""
    
    if not s_sents or not segs:
        continue
        
    combined_sent = " ".join(sents_dict.get(k, "") for k in s_sents)
    combined_clean = re.sub(r"[^\w\s]", " ", combined_sent.lower())
    
    mismatched_elems = []
    for sg in segs:
        at_s = sg.get("at_sentence")
        if at_s:
            t_sids = [k for k in s_sents if k.endswith(f"#{at_s}")]
            active_sent = sents_dict.get(t_sids[0], combined_sent) if t_sids else combined_sent
        else:
            active_sent = combined_sent
        active_clean = re.sub(r"[^\w\s]", " ", active_sent.lower())

        for kind, text in sg.get("elems", []):
            # Kiểm tra xem các từ khóa chính trong text có nằm trong active_sent không
            # Tách các từ có độ dài >= 4
            words = [w for w in re.findall(r"\w+", text.lower()) if len(w) >= 3 and not w.isdigit()]
            if not words:
                continue
            hits = [w for w in words if w in active_clean]
            hit_ratio = len(hits) / len(words)
            if hit_ratio < 0.4 and tmpl not in ("T10", "T5"):
                mismatched_elems.append((kind, text, hit_ratio, active_sent[:60]))

    if mismatched_elems:
        print(f"\n[!] SHOT {sid} (Mẫu {tmpl}): CHỮ TRÊN HÌNH KHÔNG CÓ TRONG LỜI ĐỌC:")
        for k, txt, ratio, ref in mismatched_elems:
            print(f"    - Loại [{k}]: \"{txt}\" (khớp {ratio*100:.0f}%)")
            print(f"      Lời đang đọc: \"{ref}...\"")
