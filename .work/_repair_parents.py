"""Sua loi cu phap: `Path(__file__).resolve().parents[3]` -> `Path(__file__).resolve().parents[1]s[N]`.

- `Path(x).parent/..` KHONG phai cu phap Python hop le.
- Dung `Path(x).resolve().parents[1]s[N]`: N = so cap len tu file den repo root.
- GIU NGUYEN line ending (CRLF/LF) cua file goc.

Chay: python .work/_repair_parents.py
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parents[1].parent

# Path(<expr>).resolve().parents[1](/..)*   ->   Path(<expr>).resolve().parents[1]s[N]
PAT = re.compile(r"Path\((?P<expr>[^()]*)\)\.resolve\(\)\.parent(?P<dots>(?:/\.\.)*)")


def fix_text(src: str, depth: int) -> str:
    def rep(m):
        n = m.group("dots").count("/..")
        return f"Path({m.group('expr')}).resolve().parents[{depth + n}]"
    return PAT.sub(rep, src)


changed = []
for p in sorted(ROOT.rglob("*.py")):
    if any(x in p.parts for x in (".git", "node_modules", "ffmpeg", "__pycache__", ".venv")):
        continue
    try:
        raw = p.read_bytes()
    except Exception:
        continue
    try:
        src = raw.decode("utf-8")
    except Exception:
        continue
    if ".resolve().parent" not in src:
        continue
    rel = p.relative_to(ROOT)
    depth = len(rel.parts) - 1
    new = fix_text(src, depth)
    if new != src:
        crlf = b"\r\n" in raw
        data = new.replace("\r\n", "\n")
        if crlf:
            data = data.replace("\n", "\r\n")
        p.write_bytes(data.encode("utf-8"))
        changed.append(str(rel))

print(f"DA SUA {len(changed)} file")
for c in changed[:12]:
    print("  ", c)
if len(changed) > 12:
    print(f"  ... +{len(changed)-12} file nua")
