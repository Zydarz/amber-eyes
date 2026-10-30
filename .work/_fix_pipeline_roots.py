"""Sua ROOT cu cho CAC FILE DUONG DAN DANH (tracked) — dung nhanh, kiem chung duoc.

Nguyen tac:
1. CHI sua file co `Path(r"D:\\TEST\\Gax\\Audi...")` — dung duong dan cu.
2. Moi file doi 1 dong; dung `parents[N]` dung so cap:
   `.work/x.py` -> parents[1] | `.work/a/x.py` -> parents[2] | `x.py` -> parent
3. KHONG doi `.resolve().parent` dang tot (nghia thu muc chua file).
4. KHONG dua file archive (`.work/_cu`, `.work/yt_audio_library`, `.work/tap03_review`) vao pham vi
   — chung khong phai pipeline Tập 02.

Chay: python .work/_fix_pipeline_roots.py
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent.parent
OLD = "D:\\TEST\\Gax\\Audi"
SKIP_DIRS = {"_cu", "yt_audio_library", "tap03_review", "__pycache__", "ffmpeg", ".git", "node_modules"}

PAT = re.compile(r'Path\(r"' + re.escape(OLD) + r'(?P<suffix>[^"]*)?"\)')


def depth_for(rel: pathlib.Path) -> int:
    return len(rel.parts) - 1


changed = []
for p in sorted(ROOT.rglob("*.py")):
    rel = p.relative_to(ROOT)
    if any(part in SKIP_DIRS for part in rel.parts):
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
    depth = depth_for(rel)
    base = (f"Path(__file__).resolve().parents[{depth}]" if depth >= 1
            else "Path(__file__).resolve().parent")

    def rep(m):
        suffix = (m.group("suffix") or "").replace("\\", "/").strip("/")
        segs = [s for s in suffix.split("/") if s]
        return base + ((" / " + " / ".join(f'"{s}"' for s in segs)) if segs else "")

    new = PAT.sub(rep, src)
    if new != src:
        crlf = b"\r\n" in raw
        d = new.replace("\r\n", "\n")
        if crlf:
            d = d.replace("\n", "\r\n")
        p.write_bytes(d.encode("utf-8"))
        changed.append(str(rel))

print(f"DA SUA {len(changed)} file (ngoai kho archive)")
for c in changed:
    print("  ", c)
