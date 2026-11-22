# -*- coding: utf-8 -*-
"""Tai lai 1 anh theo node_id (loi mang tam thoi)."""
import io, json, shutil, subprocess, sys, urllib.request, pathlib

ROOT = r"D:/TEST/Gax/amber-eyes"
MT = shutil.which("mcode-tools")
OUT = pathlib.Path(ROOT) / ".work" / "tk_img_raw_t02"
OUT.mkdir(parents=True, exist_ok=True)


def sh(cmd, timeout=180):
    r = subprocess.run('"%s" %s' % (MT, cmd), shell=True, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout)
    txt = (r.stdout or "").strip() or (r.stderr or "").strip()
    try:
        return json.loads(txt[txt.find("{"):])
    except Exception:
        raise RuntimeError("fail: %s -> %s" % (cmd, txt[:300]))


node = sys.argv[1]
name = sys.argv[2]
for attempt in range(1, 5):
    try:
        d = sh("get_asset_url %s" % node)
        url = d.get("download_url") or d.get("url")
        if not url:
            raise RuntimeError("khong co download_url")
        dst = OUT / name
        with urllib.request.urlopen(url, timeout=180) as r, open(dst, "wb") as f:
            shutil.copyfileobj(r, f)
        print("OK lan %d: %s (%d KB)" % (attempt, dst.name, dst.stat().st_size / 1024))
        break
    except Exception as e:
        print("lan %d that bai: %s" % (attempt, str(e)[:200]))
else:
    sys.exit(1)
