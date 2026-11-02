#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""env_load: tai lazy theo vai + doc theo khoi de khong lam ngo RAM (A11 build).

Truoc: moi worker nap 5 stem float32 (~800 MB) -> ArrayMemoryError khi 6 worker.
Sau: chi tai vai dang ve, va tinh RMS theo khoi (~4 MB tam).

build_video3.py dung ket thuong "\r\r\n" -> giu nguyen khi ghi lai.
"""
import sys
from pathlib import Path

P = Path(r"D:\TEST\Gax\amber-eyes\.work\build_video3.py")
src = P.read_bytes().decode("utf-8")
NL = "\r\r\n"

OLD = NL.join([
    "ENV = None",
    "",
    "",
    "def env_load():",
    "    global ENV",
    "    if ENV is not None:",
    "        return",
    "    ENV = {}",
    "    for role in ROLE_COLOR:",
    "        with wave.open(str(ED.w(\"stems\") / f\"{role}.wav\")) as wf:",
    "            x = np.frombuffer(wf.readframes(wf.getnframes()), np.int16).astype(np.float32) / 32768",
    "            sr = wf.getframerate()",
    "        hop = sr // FPS",
    "        n = len(x) // hop",
    "        e = np.sqrt((x[: n * hop].reshape(n, hop) ** 2).mean(axis=1))",
    "        ENV[role] = np.clip(e / 0.12, 0, 1)",
])

NEW = NL.join([
    "ENV = {}",
    "ENV_CHUNK = 1 << 20          # so frame doc mot lan (RAM tam ~4 MB)",
    "",
    "",
    "def _env_for(role):",
    "    \"\"\"RMS moi frame (30 Hz) cua stem role — doc theo khoi, khong nap ca file.\"\"\"",
    "    with wave.open(str(ED.w(\"stems\") / f\"{role}.wav\")) as wf:",
    "        sr = wf.getframerate()",
    "        hop = sr // FPS",
    "        n = wf.getnframes() // hop",
    "        e = np.zeros(n, dtype=np.float32)",
    "        rows = max(1, ENV_CHUNK // hop)",
    "        done = 0",
    "        while done < n:",
    "            k = min(rows, n - done)",
    "            a = np.frombuffer(wf.readframes(k * hop), np.int16)",
    "            if a.size < k * hop:",
    "                k = a.size // hop",
    "                if k <= 0:",
    "                    break",
    "                a = a[: k * hop]",
    "            blk = a.astype(np.float32)",
    "            e[done:done + k] = np.sqrt((blk.reshape(k, hop) ** 2).mean(axis=1))",
    "            done += k",
    "    return np.clip(e / 0.12, 0, 1)",
    "",
    "",
    "def env_load(role=None):",
    "    \"\"\"Tai envelope theo vai (lazy): chi vai dang ve moi can.\"\"\"",
    "    if role is None:",
    "        for r in ROLE_COLOR:",
    "            env_load(r)",
    "        return",
    "    if role not in ENV:",
    "        ENV[role] = _env_for(role)",
])

OLD2 = NL.join([
    "    if wave_on and not dim:",
    "        env_load()",
    "        e = ENV[role]",
])

NEW2 = NL.join([
    "    if wave_on and not dim:",
    "        env_load(role)",
    "        e = ENV[role]",
])

fail = 0
for old, new in ((OLD, NEW), (OLD2, NEW2)):
    n = src.count(old)
    if n != 1:
        print(f"[FAIL] khop {n} lan (can 1): {old.splitlines()[0]!r}")
        fail += 1
        continue
    src = src.replace(old, new)
    print(f"[OK ] {old.splitlines()[0]!r}")

if fail:
    print("\nKHONG ghi file.")
    sys.exit(1)
with open(P, "w", encoding="utf-8", newline="") as f:
    f.write(src)
chk = P.read_bytes()
print("\nDa ghi. BOM:", chk[:3].hex(), "| CRLF:", chk.count(b"\r\r\n"), "| LF:", chk.count(b"\n"))
