# -*- coding: utf-8 -*-
"""Thu thap so do thuc te cho BTT 8 - Tap04 (15 clip)."""
import json, os, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TK = ROOT / "02_SAN_XUAT" / "TIKTOK"
FF = sorted((ROOT / ".work" / "ffmpeg").glob("*/bin/ffmpeg.exe"))[0]
FP = str(FF).replace("ffmpeg.exe", "ffprobe.exe")

LANGS = [("VN", "Tap04"), ("EN", "Tap04_EN"), ("JA", "Tap04_JA")]

out = {}
for lang, d in LANGS:
    folder = TK / d
    spec = json.loads((folder / "SPEC_AUDIO_CLIP_TAP04.json").read_text(encoding="utf-8"))
    for k, v in sorted(spec["clips"].items()):
        vid = folder / f"{k}_video.mp4"
        r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration,size",
                            "-show_entries", "stream=codec_name,width,height,r_frame_rate",
                            "-of", "json", str(vid)], capture_output=True, text=True, encoding="utf-8")
        j = json.loads(r.stdout or "{}")
        fmt = j.get("format", {})
        st = j.get("streams", [])
        v0 = next((s for s in st if s.get("codec_name") not in ("aac",)), {})
        a0 = next((s for s in st if s.get("codec_name") == "aac"), {})
        lines = v.get("lines", [])
        out[f"{lang}_{k}"] = {
            "lang": lang, "clip": k,
            "n_lines": len(lines),
            "dur_s": round(float(fmt.get("duration", 0)), 2),
            "size_mb": round(int(fmt.get("size", 0)) / 1048576, 1),
            "w": v0.get("width"), "h": v0.get("height"),
            "vcodec": v0.get("codec_name"), "acodec": a0.get("codec_name"),
            "fps": v0.get("r_frame_rate"),
            "caption_chars": len((folder / f"Caption_{k}.txt").read_text(encoding="utf-8")),
        }

print(json.dumps(out, ensure_ascii=False, indent=1))
(ROOT / ".work" / "_tk04_pkg_measure.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

# provenance structure
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
print("PROV TYPE", type(prov).__name__, list(prov.keys())[:8] if isinstance(prov, dict) else len(prov))
if isinstance(prov, dict):
    for k, v in prov.items():
        print("KEY", k, type(v).__name__, (len(v) if hasattr(v, "__len__") else ""))
        break
