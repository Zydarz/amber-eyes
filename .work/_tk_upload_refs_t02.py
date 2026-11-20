# -*- coding: utf-8 -*-
"""Upload 26 anh nen 16:9 cua Tap 02 (assets/bg/_raw/t2_*) va lay temp_url
de lam ANH THAM CHIEU cho viec sinh anh nen DOC 9:16 cho clip TikTok Tap 02.

Output: .work/_tk_refs_t02.json   { "<ten nen 16:9>": "<temp_url>" }

Ghi chu: dung `mcode-tools upload_temp_url` — cung khuong dung voi Tap 01
(.work/_tk_refs_t01.json).
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = ROOT / "assets" / "bg" / "_raw"
OUT = HERE / "_tk_refs_t02.json"

# ten nen DOC (tk02_*) -> ten nen 16:9 goc (t2_*)
MAP = {
    "tk02_brain_neural": "t2_brain_neural",
    "tk02_checkpoint": "t2_checkpoint",
    "tk02_command_chair": "t2_command_chair",
    "tk02_cottage_search": "t2_cottage_search",
    "tk02_courtroom": "t2_courtroom",
    "tk02_drawer_dark": "t2_drawer_dark",
    "tk02_escalation_stairs": "t2_escalation_stairs",
    "tk02_folder_tree": "t2_folder_tree",
    "tk02_gavel": "t2_gavel",
    "tk02_head_down": "t2_head_down",
    "tk02_hidden_drive": "t2_hidden_drive",
    "tk02_house_missing": "t2_house_missing",
    "tk02_interrogation_early": "t2_interrogation_early",
    "tk02_oath_hall": "t2_oath_hall",
    "tk02_open_window": "t2_open_window",
    "tk02_podcast_desk": "t2_podcast_desk",
    "tk02_red_flags": "t2_red_flags",
    "tk02_siren_wall": "t2_siren_wall",
    "tk02_stairs_dark": "t2_stairs_dark",
    "tk02_suv_stop": "t2_suv_stop",
    "tk02_tire_track": "t2_tire_track",
    "tk02_town_snow": "t2_town_snow",
    "tk02_two_chairs": "t2_two_chairs",
    "tk02_two_drawers": "t2_two_drawers",
    "tk02_two_masks": "t2_two_masks",
    "tk02_uniform_fire": "t2_uniform_fire",
}


def pick_file(base):
    """Uu tien ban .png (da xu ly 2112x1188), lui ve .jpg (2752x1536)."""
    for ext in (".png", ".jpg"):
        p = RAW / (base + ext)
        if p.exists():
            return p
    return None


def upload(path):
    # mcode-tools la wrapper .cmd -> CreateProcess khong tu tim theo PATHEXT,
    # phai goi qua cmd.exe (shell=True) va dung duong dan .cmd goc.
    exe = shutil.which("mcode-tools") or "mcode-tools"
    cmd = '"%s" upload_temp_url "%s"' % (exe, path)
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
    if r.returncode != 0:
        raise RuntimeError("upload fail %s: %s" % (path.name, (r.stderr or r.stdout)[:400]))
    txt = r.stdout.strip()
    try:
        d = json.loads(txt)
    except json.JSONDecodeError:
        # CLI co the in them dong truoc JSON -> lay phan dau {..}
        i = txt.find("{")
        d = json.loads(txt[i:])
    url = d.get("temp_url") or d.get("url") or d.get("download_url")
    if not url:
        raise RuntimeError("khong lay duoc temp_url cho %s: %s" % (path.name, txt[:300]))
    return url


def main():
    refs = {}
    missing = []
    for name, base in sorted(MAP.items()):
        f = pick_file(base)
        if f is None:
            missing.append(base)
            continue
        refs[name] = upload(f)
        print("  %-24s <- %-28s OK" % (name, f.name))
    if missing:
        raise SystemExit("thieu file goc: %s" % missing)
    OUT.write_text(json.dumps(refs, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n%d anh tham chieu -> %s" % (len(refs), OUT))


if __name__ == "__main__":
    main()
