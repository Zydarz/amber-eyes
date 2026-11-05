import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import parse_shots
print([attr for attr in dir(parse_shots) if not attr.startswith("__")])
