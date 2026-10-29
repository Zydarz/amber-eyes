import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

src_vi = open("01_KICH_BAN/Tap04/kichban_tap04_23102026.md", encoding="utf-8").readlines()
src_en = open("01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md", encoding="utf-8").readlines()

els_vi = {e["id"]: e for e in PK.parse_lines(src_vi) if e["kind"] == "LOI"}
els_en = {e["id"]: e for e in PK.parse_lines(src_en) if e["kind"] == "LOI"}

diff_ids = ["2.11", "3.02", "4.12", "5.02"]

for did in diff_ids:
    print(f"\n{'='*80}\nELEMENT {did}")
    ev = els_vi[did]
    ee = els_en[did]
    print(f"VI ({len(ev['sentences'])} sentences):")
    for s in ev["sentences"]:
        print(f"  [{s['id']}]: {s['text']}")
    print(f"\nEN ({len(ee['sentences'])} sentences):")
    for s in ee["sentences"]:
        print(f"  [{s['id']}]: {s['text']}")
