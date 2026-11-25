# -*- coding: utf-8 -*-
"""Tai anh nen DOC 9:16 Tap 05 vua sinh (node_id -> download_url -> file .jpg).

Input : .work/_tk_img_receipt_t05_b*.json
Output: .work/tk_img_raw_t05/tk05_<ten>.jpg
Chay lai duoc: bo qua file da co, thu lai file bi loi tai.
"""
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t05 import PAIRS  # noqa: E402

OUT = HERE / "tk_img_raw_t05"
OUT.mkdir(parents=True, exist_ok=True)
MT = shutil.which("mcode-tools") or "mcode-tools"


def sh(cmd, timeout=300):
    exe = shutil.which("mcode-tools") or "mcode-tools"
    r = subprocess.run('"%s" %s' % (exe, cmd), shell=True,
                       capture_output=True, text=True, timeout=timeout,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError("fail: %s\n%s" % (cmd, (r.stderr or r.stdout)[:300]))
    txt = r.stdout.strip()
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        i = txt.find("{")
        return json.loads(txt[i:])


def read_json_any(path):
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-16", "utf-16-le"):
        try:
            return json.loads(raw.decode(enc))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise RuntimeError("khong doc duoc JSON: %s" % path)


def main():
    receipts = sorted(HERE.glob("_tk_img_receipt_t05_b*.json"))
    if not receipts:
        raise SystemExit("khong co receipt nao - hay chay _tk_gen_bg_t05.py truoc")
    items = []
    for rp in receipts:
        d = read_json_any(rp)
        for it in d.get("success_items", []):
            items.append(it)
    print("receipt: %d file · %d thanh cong" % (len(receipts), len(items)))

    ok, fail = 0, []
    for it in items:
        node = it.get("node_id")
        fname = it.get("file_name")
        if not node or not fname:
            continue
        dst = OUT / fname
        if dst.exists():
            print("  skip (da co): %s" % fname)
            continue
        for attempt in (1, 2, 3):
            try:
                d = sh("get_asset_url %s" % node)
                url = d.get("download_url") or d.get("url")
                if not url:
                    raise RuntimeError("khong co download_url")
                with urllib.request.urlopen(url, timeout=600) as r, open(dst, "wb") as f:
                    shutil.copyfileobj(r, f)
                print("  %-42s %8.0f KB  node=%s" % (fname, dst.stat().st_size / 1024, node))
                ok += 1
                break
            except Exception as e:  # noqa: BLE001
                if attempt == 3:
                    fail.append((fname, str(e)[:160]))
                    print("  FAIL %-38s %s" % (fname, str(e)[:160]))
                else:
                    print("     thu lai %s (%s)" % (fname, str(e)[:80]))

    print("\ntai %d file -> %s" % (ok, OUT))
    if fail:
        print("FAIL:", fail)
    missing = [n for n, _ in PAIRS
               if not (OUT / (n + ".jpg")).exists() and not (OUT / (n + ".png")).exists()]
    (HERE / "_tk_img_missing_t05.json").write_text(
        json.dumps(missing, ensure_ascii=False, indent=1), encoding="utf-8")
    print("DA DU %d/%d · thieu %d" % (len(PAIRS) - len(missing), len(PAIRS), len(missing)))
    if missing:
        print("THIEU:", ", ".join(missing))


if __name__ == "__main__":
    main()
