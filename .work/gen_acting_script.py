import re, json
from pathlib import Path

content = Path(".work/make_acting_tap10.py").read_text(encoding="utf-8")
content = content.replace("tap10", "tap40").replace("Tap10", "Tap40").replace("4.05", "4.06").replace("Colleen Stan", "Patrice Alègre")
Path(".work/make_acting_tap40.py").write_text(content, encoding="utf-8")
print("Wrote .work/make_acting_tap40.py successfully")
