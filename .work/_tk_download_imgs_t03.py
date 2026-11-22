# -*- coding: utf-8 -*-
"""Tai anh nen DOC 9:16 Tap 03 vua sinh (node_id -> download_url -> file .jpg).

Input : .work/_tk_img_receipt_t03_b*.json   (receipt tu connector__matrix__generate_image)
Output: .work/tk_img_raw_t03/tk03_<ten>.jpg
"""
import json
import pathlib
import shutil
import subprocess
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t03 import PAIRS  # noqa: E402

OUT = HERE / "tk_img_raw_t03"
OUT.mkdir(parents=True, exist_ok=True)


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
    receipts = sorted(HERE.glob("_tk_img_receipt_t03_b*.json"))
    if not receipts:
        raise SystemExit("khong co receipt nao - hay chay _tk_gen_bg_t03.py truoc")
    items = []
    for rp in receipts:
        d = read_json_any(rp)
        for it in d.get("success_items", []):
            items.append(it)
    print("receipt: %d file, %d thanh cong" % (len(receipts), len(items)))

    ok, fail = 0, []
    for it in items:
        node = it.get("node_id")
        fname = it.get("file_name")
        if not node or not fname:
            continue
        try:
            d = sh("get_asset_url %s" % node)
            url = d.get("download_url") or d.get("url")
            if not url:
                raise RuntimeError("khong co download_url: %s" % json.dumps(d, ensure_ascii=False)[:200])
            dst = OUT / fname
            with urllib.request.urlopen(url, timeout=300) as r, open(dst, "wb") as f:
                shutil.copyfileobj(r, f)
            print("  %-32s %8.0f KB  node=%s" % (fname, dst.stat().st_size / 1024, node))
            ok += 1
        except Exception as e:  # noqa: BLE001
            fail.append((fname, str(e)[:160]))
            print("  FAIL %-30s %s" % (fname, str(e)[:160]))

    print("\ntai %d/%d file -> %s" % (ok, len(items), OUT))
    if fail:
        print("FAIL:", fail)

    missing = []
    for name, _ in PAIRS:
        if not (OUT / (name + ".jpg")).exists() and not (OUT / (name + ".png")).exists():
            missing.append(name)
    if missing:
        (HERE / "_tk_img_missing_t03.json").write_text(
            json.dumps(missing, ensure_ascii=False, indent=1), encoding="utf-8")
        print("CHUA CO (%d): %s" % (len(missing), ", ".join(missing)))
    else:
        p = HERE / "_tk_img_missing_t03.json"
        if p.exists():
            p.unlink()
        print("DA DU 28/28")


if __name__ == "__main__":
    main()
