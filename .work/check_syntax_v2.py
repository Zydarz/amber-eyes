# -*- coding: utf-8 -*-
import json, re

def check_script(lang, json_path):
    print(f"=== CHECKING {lang} ===")
    d = json.load(open(json_path, encoding="utf-8"))
    issues = 0
    for el in d:
        if el.get("kind") == "LOI":
            for s in el["sentences"]:
                t = s["text"]
                sid = s["id"]
                # Quote checks
                if t.count("“") != t.count("”"):
                    print(f"[{sid}] Unmatched curly quotes: {t}")
                    issues += 1
                if t.count('"') % 2 != 0:
                    print(f"[{sid}] Unmatched double quotes: {t}")
                    issues += 1
                if t.count("「") != t.count("」"):
                    print(f"[{sid}] Unmatched Japanese corner quotes: {t}")
                    issues += 1
                if t.count("(") != t.count(")"):
                    print(f"[{sid}] Unmatched parentheses: {t}")
                    issues += 1
                if t.count("（") != t.count("）"):
                    print(f"[{sid}] Unmatched Japanese parentheses: {t}")
                    issues += 1
                # Check for un-paired single quotes that are NOT apostrophes
                # An apostrophe is between two word characters like word's or in contractions like didn't
                isolated_single_quotes = re.findall(r"(?<![A-Za-z])['‘](?![A-Za-z])|(?<![A-Za-z])['’](?![A-Za-z])", t)
                if isolated_single_quotes:
                    print(f"[{sid}] Isolated single quotes: {t}")
                    issues += 1
                # Sentence ending check
                if lang == "JA":
                    if not t.endswith(("。", "！", "？", "」", "』", "）", "…")):
                        print(f"[{sid}] Suspicious JA ending: {t}")
                        issues += 1
                else:
                    if not t.endswith((".", "!", "?", "”", "’", '"', "…", ":")):
                        print(f"[{sid}] Suspicious {lang} ending: {t}")
                        issues += 1
    if issues == 0:
        print(f"Result {lang}: 100% CLEAN! (0 issues found)\n")
    else:
        print(f"Result {lang}: Found {issues} issues.\n")

check_script("VN", ".work/t32_vn.json")
check_script("EN", ".work/t32_en.json")
check_script("JA", ".work/t32_ja.json")
