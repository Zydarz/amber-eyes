# -*- coding: utf-8 -*-
"""Comprehensive QC for Episode 22 across all 4 languages (VN, EN, JA, KO)."""

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))

import parse_kichban as PK

files = [
    ("VN", ROOT / "01_KICH_BAN" / "Tap22" / "kichban_tap22_23102026.md"),
    ("EN", ROOT / "01_KICH_BAN" / "Tap22_EN" / "kichban_tap22_EN.md"),
    ("JA", ROOT / "01_KICH_BAN" / "Tap22_JA" / "kichban_tap22_JA.md"),
    ("KO", ROOT / "01_KICH_BAN" / "Tap22_KO" / "kichban_tap22_KO.md"),
]

forbidden = {
    "VN": ["máu", "thi thể", "xác chết", "tự sát", "cắt cổ", "bóp cổ", "chặt xác", "khí độc", "ngạt thở", "đâm", "trói", "diệt chủng", "đầu độc", "bỏ đói"],
    "EN": ["blood", "corpse", "decapitat", "strangl", "suicide", "dismember"],
    "JA": ["自殺", "死体", "血液", "窒息", "切断"],
    "KO": ["자살", "시체", "혈흔", "질식", "절단"],
}

parsed_all = {}
all_green = True

print("=" * 70)
print("COMPREHENSIVE QC AUDIT: EPISODE 22 (ALL 4 LANGUAGES)")
print("=" * 70)

for lang, path in files:
    print(f"\n--- AUDITING: {lang} ({path.relative_to(ROOT)}) ---")
    
    # Check EOL
    raw_bytes = open(path, "rb").read()
    double_cr = raw_bytes.count(b"\r\r\n")
    print(f"Double CR (\\r\\r\\n): {double_cr} (Must be 0)")
    if double_cr > 0:
        all_green = False
        print("FAIL: Double CR found!")

    p = PK.parse_file(str(path))
    parsed_all[lang] = p
    
    total_elements = len(p)
    loi = [e for e in p if e["kind"] == "LOI"]
    total_sentences = sum(len(x.get("sentences", [])) for x in loi)
    total_words = sum(sum(s["words"] for s in x["sentences"]) for x in loi)
    
    print(f"Elements: {total_elements} (Expected: 51)")
    print(f"LOI turns: {len(loi)} (Expected: 32)")
    print(f"Sentences: {total_sentences} (Expected: 212)")
    print(f"Words: {total_words}")
    
    fb_hits = []
    ellipsis_hits = []
    
    fb_list = forbidden.get(lang, [])
    for e in loi:
        for s in e["sentences"]:
            txt = s["text"]
            sid = s["id"]
            for fb in fb_list:
                if lang in ["VN", "EN"]:
                    if re.search(r"\b" + re.escape(fb) + r"\b", txt, re.IGNORECASE):
                        fb_hits.append((sid, fb, txt))
                else:
                    if fb in txt:
                        fb_hits.append((sid, fb, txt))
            if "..." in txt or "…" in txt:
                ellipsis_hits.append((sid, txt))
                
    print(f"Forbidden word hits (V9): {len(fb_hits)}")
    for h in fb_hits:
        print(f"  - {h[0]}: forbidden '{h[1]}' in '{h[2]}'")
    print(f"Ellipsis hits (G1): {len(ellipsis_hits)}")
    for d in ellipsis_hits:
        print(f"  - {d[0]}: ellipsis in '{d[1]}'")
        
    status = (
        len(fb_hits) == 0
        and len(ellipsis_hits) == 0
        and total_sentences == 212
        and total_elements == 51
        and double_cr == 0
    )
    print(f"Result for {lang}: {'PASS' if status else 'FAIL'}")
    all_green = all_green and status

# Parity check
print("\n" + "=" * 70)
print("1:1 PARITY VERIFICATION ACROSS ALL LANGUAGES (VN vs EN vs JA vs KO)")
print("=" * 70)
parity_pass = True
vn_p = parsed_all["VN"]

for lang in ["EN", "JA", "KO"]:
    lp = parsed_all[lang]
    if len(lp) != len(vn_p):
        print(f"FAIL: Element count mismatch VN({len(vn_p)}) vs {lang}({len(lp)})")
        parity_pass = False
        continue
    mismatches = []
    for i in range(len(vn_p)):
        evn = vn_p[i]
        el = lp[i]
        if evn["kind"] != el["kind"]:
            mismatches.append(f"Element {evn['id']}: Kind mismatch VN({evn['kind']}) vs {lang}({el['kind']})")
        if evn.get("role") != el.get("role"):
            mismatches.append(f"Element {evn['id']}: Role mismatch VN({evn.get('role')}) vs {lang}({el.get('role')})")
        svn = len(evn.get("sentences", []))
        sl = len(el.get("sentences", []))
        if svn != sl:
            mismatches.append(f"Element {evn['id']}: Sentence count mismatch VN({svn}) vs {lang}({sl})")
    if mismatches:
        print(f"FAIL Parity VN vs {lang} ({len(mismatches)} errors):")
        for m in mismatches[:10]:
            print("  - " + m)
        parity_pass = False
    else:
        print(f"PASS Parity: VN vs {lang} (100% matched across 51 elements, 32 turns, 212 sentences)")

# Check edition.py hooks
print("\n" + "=" * 70)
print("PIPELINE HOOKS VERIFICATION (edition.py)")
print("=" * 70)
vn_sids = set()
for e in vn_p:
    for s in e.get("sentences", []):
        vn_sids.add(s["id"])

summary_keys = ["1.02#1", "3.02#1"]
for k in summary_keys:
    if k in vn_sids:
        print(f"PASS Summary Key: {k} exists in parsed script.")
    else:
        print(f"FAIL Summary Key: {k} NOT found in parsed script!")
        all_green = False

n_element_expected = {"1.07": "N", "4.09": "N"}
for eid, role in n_element_expected.items():
    el = [x for x in vn_p if x["id"] == eid][0]
    if el.get("role") == role:
        print(f"PASS N element: {eid} has role '{role}'")
    else:
        print(f"FAIL N element: {eid} expected '{role}', got '{el.get('role')}'")
        all_green = False

print("\n" + "=" * 70)
final_result = all_green and parity_pass
print(f"FINAL AUDIT RESULT: {'>>> ALL CHECKS PASSED (100% GREEN) <<<' if final_result else '>>> AUDIT FAILED <<<'}")
print("=" * 70)
