import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))

configs = [
    ("vi", None, ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap22" / "xuat_ban"),
    ("en", "en", ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap22_EN" / "xuat_ban"),
    ("ja", "ja", ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap22_JA" / "xuat_ban"),
]

for code, lang_env, out_dir in configs:
    os.environ["AE_EP"] = "22"
    if lang_env:
        os.environ["AE_LANG"] = lang_env
    else:
        os.environ.pop("AE_LANG", None)

    # Force reimport
    for mod in ["edition", "package"]:
        if mod in sys.modules:
            del sys.modules[mod]

    import edition as ED
    import package as P

    out_dir.mkdir(parents=True, exist_ok=True)
    P.OUT_DIR = out_dir
    P.thumbnail()
    target_file = out_dir / "thumbnail.png"
    print(f"[{code.upper()}] thumbnail created: {target_file} ({target_file.stat().st_size:,} bytes)")
    print(f"       thumb lines: {ED.EP['thumb']}")
    print(f"       thumb_bg   : {ED.EP.get('thumb_bg')}")
