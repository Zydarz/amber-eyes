# -*- coding: utf-8 -*-
"""Build args JSON cho connector__matrix__generate_image (Tap 07 - nen doc 9:16).

Usage:  python .work/_tk_build_req_t07.py <batch_index> <name1> <name2> ...
  - Upload MOI anh 16:9 goc (mcode-tools upload_temp_url) -> temp_url (het han 1 gio)
  - Ghi .work/tk_req_t07/batch<k>.json  (mcode-tools connector call --args-file)
"""
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _tk_src_t07 import MIME, PAIRS, prompt_for, src_path  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
REQD = HERE / "tk_req_t07"
REQD.mkdir(exist_ok=True)

REF = dict(PAIRS)


MCODE = r"C:\Users\ADMIN\.minimax\bin\hosts\prod-deaf713c4da71f8d\mcode-tools.cmd"


def upload(path):
    out = subprocess.run(
        [MCODE, "upload_temp_url", path],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if out.returncode != 0:
        raise SystemExit("UPLOAD FAIL %s\n%s\n%s" % (path, out.stdout, out.stderr))
    data = json.loads(out.stdout)
    return data["temp_url"], data.get("mime_type")


def main():
    batch = int(sys.argv[1])
    names = sys.argv[2:]
    if not names:
        raise SystemExit("can danh sach nen")
    requests = []
    for name in names:
        src = src_path(REF[name])
        url, mime = upload(src)
        ext = pathlib.Path(REF[name]).suffix.lower().lstrip(".")
        requests.append({
            "prompt": prompt_for(name),
            "reference_images": [{"url": url, "mime_type": MIME.get(ext, "image/png")}],
            "aspect_ratio": "9:16",
            "area": "2K",
            "output_format": "jpeg",
            "output_file": name,
            "n": 1,
        })
        print("uploaded %-44s %s" % (name, url[:60] + "..."))

    args = {"requests": requests}
    p = REQD / ("batch%d.json" % batch)
    p.write_text(json.dumps(args, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\nargs file:", p, "· so requests:", len(requests))


if __name__ == "__main__":
    main()
