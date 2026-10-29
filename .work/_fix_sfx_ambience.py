import json
from pathlib import Path

p = Path(".work/sfx_tap07.json")
data = json.loads(p.read_text(encoding="utf-8"))

for row in data["ambience"]:
    if row[1] == "1.08#6":
        row[1] = "1.07#6"
    elif row[1] == "2.05#6":
        row[1] = "2.04#6"
    elif row[1] == "4.04#8":
        row[1] = "4.03#8"

p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("Updated sfx_tap07.json successfully!")
