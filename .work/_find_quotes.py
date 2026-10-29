"""In vi tri + nguon canh cua tung dau nhay trong file VN."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
raw = Path(sys.argv[1]).read_text(encoding="utf-8")
for i, line in enumerate(raw.splitlines(), 1):
    for m in re.finditer(r"'([^']{2,})'", line):
        print(f"L{i:>4} [{m.group(1)}]")
        print(f"      {line.strip()[:220]}")
