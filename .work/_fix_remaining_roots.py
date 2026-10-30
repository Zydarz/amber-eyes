"""Sua 49 file con duong dan cu o dang raw string tran (khong boc Path(...)).

Vi du:
  p = r"D:\\TEST\\Gax\\Audi\\.work\\x.json"      -> str(ROOT / ".work" / "x.json")
  BASE = r"D:\\TEST\\Gax\\Audi"                  -> str(ROOT)
  sys.path.insert(0, r'D:\\TEST\\Gax\\Audi\\.work')

Chay: python .work/_fix_remaining_roots.py
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent.parent
OLD = "D:\\TEST\\Gax\\Audi"          # chuoi trong file nguon (mot dau \)
Q = "[\"']"
PAT = re.compile(
    r"(?P<pre>(?:Path\(|rf?\(|r?f?)" + Q + r"r?)"
    + re.escape(OLD)
    + r"(?P<suffix>[^" + Q + r"]*)"
    + Q
)


def expr_for(suffix: str, base: str) -> str:
    segs = [s for s in suffix.replace("\\", "/").split("/") if s]
    joined = base + ((" / " + " / ".join('"' + s + '"' for s in segs)) if segs else "")
    return "str(" + joined + ")"


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
    if OLD not in src:
        continue
    rel = p.relative_to(ROOT)
    depth = len(rel.parts) - 1
    base = f"Path(__file__).resolve().parents[{depth}]"

    def rep(m):
        e = expr_for(m.group("suffix"), base)
        pre = m.group("pre")
        if pre.startswith("Path("):
            return "Path(" + e + ")"
        return e

    new = PAT.sub(rep, src)
    if new != src:
        crlf = b"\r\n" in raw
        d = new.replace("\r\n", "\n")
        if crlf:
            d = d.replace("\n", "\r\n")
        p.write_bytes(d.encode("utf-8"))
        changed.append(str(rel))

print(f"DA SUA {len(changed)} file")
for c in changed[:20]:
    print("  ", c)
if len(changed) > 20:
    print(f"  ... +{len(changed) - 20} file nua")

left = []
for p in sorted(ROOT.rglob("*.py")):
    if any(x in p.parts for x in (".git", "node_modules", "ffmpeg", "__pycache__", ".venv")):
        continue
    try:
        s = p.read_bytes().decode("utf-8")
    except Exception:
        continue
    if OLD in s:
        left.append(str(p.relative_to(ROOT)))
print(f"\nCON LAI: {len(left)}")
for l in left:
    print("  ", l)
