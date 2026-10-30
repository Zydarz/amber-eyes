"""Sua ROOT cu trong toan repo: `D:\\TEST\\Gax\\Audi` -> tu dong theo vi tri file.

QUY TAC (dung lai 1 lan, idempotent):
  File tai `<repo>/.work/ten.py`      -> ROOT = Path(__file__).resolve().parents[1]
  File tai `<repo>/.work/a/b/ten.py`  -> ROOT = Path(__file__).resolve().parents[2]
  File tai `<repo>/ten.py`            -> ROOT = Path(__file__).resolve().parent

  `parents[N]`: N = so cap thu muc giua file va repo root
  (parents[0] = thu muc chua file, parents[1] = cha, ...)

KHONG dung `parent/..` (khong phai cu phap Python hop le) va KHONG double-apply.

Chay: python .work/_fix_all_roots.py
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent.parent
OLD = r"D:\TEST\Gax\Audi"

# Path(__file__).resolve().parents[1]           -> Path(__file__).resolve().parents[N]
# Path(__file__).resolve().parents[1] / "assets" / "bg" -> Path(__file__).resolve().parents[N] / "assets" / "bg"
PAT = re.compile(r'Path\(r"' + re.escape(OLD) + r'(?P<suffix>[^"]*)?"\)')


def depth_for(rel: pathlib.Path) -> int:
    """So cap tu file len repo root (parents[N])."""
    parts = rel.parts
    return len(parts) - 1


def fix_text(src: str, depth: int) -> str:
    base = f"Path(__file__).resolve().parents[{depth}]"

    def rep(m):
        suffix = (m.group("suffix") or "").replace("\\", "/").strip("/")
        if not suffix:
            return base
        segs = [s for s in suffix.split("/") if s]
        return base + " / " + " / ".join(f'"{s}"' for s in segs)

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
    if OLD not in src:
        continue
    rel = p.relative_to(ROOT)
    new = fix_text(src, depth_for(rel))
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

# ---- verify: khong con duong dan cu, va moi file tro dung goc ----
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
print(f"\nCON LAI duong dan cu: {len(left)}")
for l in left[:10]:
    print("  ", l)
