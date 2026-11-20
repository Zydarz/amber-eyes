# -*- coding: utf-8 -*-
"""Tai 26 anh nen DOC 9:16 vua sinh (node_id -> download_url -> file .jpg).

Input : .work/_tk_img_receipt_t02_b*.json   (receipt tu connector__matrix__generate_image)
Output: .work/tk_img_raw_t02/tk02_<ten>.jpg

Giong khuong cach luu anh goc cua Tap 01 (.work/tk_img_raw/).
"""
import json
import pathlib
import shutil
import subprocess
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "tk_img_raw_t02"
OUT.mkdir(parents=True, exist_ok=True)


def sh(cmd, timeout=180):
    exe = shutil.which("mcode-tools") or "mcode-tools"
    r = subprocess.run('"%s" %s' % (exe, cmd), shell=True,
                       capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError("fail: %s\n%s" % (cmd, (r.stderr or r.stdout)[:300]))
    txt = r.stdout.strip()
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        i = txt.find("{")
        return json.loads(txt[i:])


def read_json_any(path):
    """Tee-Object cua PowerShell ghi UTF-16; file Python ghi UTF-8 -> doc ca hai."""
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-16", "utf-16-le"):
        try:
            return json.loads(raw.decode(enc))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise RuntimeError("khong doc duoc JSON: %s" % path)


def main():
    receipts = sorted(HERE.glob("_tk_img_receipt_t02_b*.json"))
    if not receipts:
        raise SystemExit("khong co receipt nao")
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
            with urllib.request.urlopen(url, timeout=180) as r, open(dst, "wb") as f:
                shutil.copyfileobj(r, f)
            kb = dst.stat().st_size / 1024
            print("  %-30s %8.0f KB  node=%s" % (fname, kb, node))
            ok += 1
        except Exception as e:  # noqa: BLE001
            fail.append((fname, str(e)[:160]))
            print("  FAIL %-28s %s" % (fname, str(e)[:160]))

    print("\ntai %d/%d file -> %s" % (ok, len(items), OUT))
    if fail:
        print("FAIL:", fail)
    # ghi danh sach con thieu
    missing = []
    try:
        reqs = []
        for rp in sorted(HERE.glob("_tk_img_req_t02_b*.json")):
            reqs += json.loads(rp.read_text(encoding="utf-8-sig"))["requests"]
        for rq in reqs:
            if not (OUT / (rq["output_file"] + ".jpg")).exists():
                missing.append(rq["output_file"])
    except Exception:  # noqa: BLE001
        pass
    if missing:
        (HERE / "_tk_img_missing_t02.json").write_text(
            json.dumps(missing, ensure_ascii=False, indent=1), encoding="utf-8")
        print("CHUA CO (%d): %s" % (len(missing), ", ".join(missing)))
    else:
        p = HERE / "_tk_img_missing_t02.json"
        if p.exists():
            p.unlink()
        print("DA DU 26/26")


if __name__ == "__main__":
    main()
