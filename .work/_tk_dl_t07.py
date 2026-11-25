# -*- coding: utf-8 -*-
"""Tai anh da sinh ve .work/tk_img_raw_t07/ (node_id -> file)."""
import json
import pathlib
import subprocess
import sys
import urllib.request

MCODE = r"C:\Users\ADMIN\.minimax\bin\hosts\prod-deaf713c4da71f8d\mcode-tools.cmd"
HERE = pathlib.Path(__file__).resolve().parent
DST = HERE / "tk_img_raw_t07"
DST.mkdir(exist_ok=True)


def asset_url(node_id):
    out = subprocess.run([MCODE, "get_asset_url", node_id],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    if out.returncode != 0:
        raise SystemExit("get_asset_url FAIL %s\n%s\n%s" % (node_id, out.stdout, out.stderr))
    data = json.loads(out.stdout)
    return data.get("download_url") or data.get("url")


def main():
    for arg in sys.argv[1:]:
        node_id, name = arg.split("=", 1)
        url = asset_url(node_id)
        ext = pathlib.Path(name).suffix or ".jpg"
        dst = DST / (pathlib.Path(name).stem + ext)
        urllib.request.urlretrieve(url, dst)
        print("%-46s <- %s  %d KB" % (dst.name, node_id, dst.stat().st_size // 1024))


if __name__ == "__main__":
    main()
