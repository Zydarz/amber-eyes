# -*- coding: utf-8 -*-
"""Check Vietnamese vocabulary, potential typos and telex artifacts."""
import sys, re, io
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

p_vn = PK.parse_file("01_KICH_BAN/Tap14/kichban_tap14_23102026.md")

# Collect all tokens
word_pattern = re.compile(r"[a-zA-ZÀ-ỹà-ỹĐđ0-9]+(?:-[a-zA-ZÀ-ỹà-ỹĐđ0-9]+)*")
sentences = []
for e in p_vn:
    if e["kind"] == "LOI":
        for s in e.get("sentences", []):
            sentences.append((s["id"], s["text"]))

# Potential telex errors / strange combinations
# like 'aa', 'ee', 'oo', 'uw', 'dd', or double accents, or invalid syllable endings
suspicious = []
for sid, text in sentences:
    words = word_pattern.findall(text)
    for w in words:
        wl = w.lower()
        # Look for English telex artifacts inside Vietnamese words
        if any(x in wl for x in ['aa', 'ee', 'oo', 'dd', 'w', 'j', 'z', 'f']) and not any(
            name in wl for name in ['broderick', 'daniel', 'dan', 'betty', 'linda', 'kolkena', 'kim', 'lee', 'rhett', 'jolla', 'marston', 'coral', 'reef', 'harvard', 'cornell', 'gaslighting', 'tupperware', 'avon', 'jazz', 'new', 'york', 'sdpd', 'diane', 'black', 'wells', 'whelan', 'gavin', 'becker', 'fear', 'eyes', 'amber', 'mo', 'signature']
        ):
            suspicious.append((sid, w, "Chứa ký tự lạ/telex sót", text))

print(f"Tổng số từ nghi vấn telex/chính tả: {len(suspicious)}")
for s in suspicious:
    print(f"  [{s[0]}] Từ '{s[1]}' ({s[2]}) -> Câu: \"{s[3]}\"")
