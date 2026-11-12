import io, json, re
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
jobs = json.loads((ROOT/".work/bg_jobs_tap09.json").read_text(encoding="utf-8"))

RISK = re.compile(r"text|letter|label|sign|writ|word|readab|headline|signed|signature|"
                  r"inscription|engraved|diagramm|chart|title|caption|plaque|dossier labeled|"
                  r"scrawled|graffiti|printed|typeset|newspaper|magazine|book spine|"
                  r"stamp|emblem on|badge", re.I)
BLOOD = re.compile(r"blood|bloody|corpse|strangle|rape|violent|bloodstain", re.I)

print("=== PROMPTS THAT ASK AI TO DRAW TEXT/LETTERING (H5 risk) ===")
for j in jobs:
    if RISK.search(j["prompt"]):
        print(f"\n-- {j['name']}\n   {j['prompt']}")

print("\n\n=== PROMPTS WITH BLOOD/VIOLENCE (V9 risk) ===")
for j in jobs:
    if BLOOD.search(j["prompt"]):
        print(f"\n-- {j['name']}\n   {j['prompt']}")

print("\n\n=== PROMPTS MENTIONING A FACE / PERSON REVEAL (H1/V5 risk) ===")
FACE = re.compile(r"face|portrait|photograph of|photo of|woman|man|girl|boy|people|"
                  r"silhouette of a|figure|human", re.I)
for j in jobs:
    if FACE.search(j["prompt"]):
        print(f"\n-- {j['name']}\n   {j['prompt']}")
