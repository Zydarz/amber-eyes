"""Nghe mu (Q1): ghep xen ke H(prod) / D(v9) / C(v9) cau neutral, hoi mo hinh co may nguoi noi."""
import json, sys, wave, pathlib, subprocess
import numpy as np
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "kaggle_higgs" / "_v9_blind"; OUT.mkdir(exist_ok=True)
R = json.load(open(HERE / "pilot_v9_result.json", encoding="utf-8"))
PROD = HERE / "kaggle_higgs" / "out_higgs_prod" / "out_higgs_prod"
pman = json.load(open(next(PROD.rglob("higgs_manifest.json")), encoding="utf-8"))
Hs = [PROD / r["file"] for r in pman if r.get("ok") and r["role"] == "H" and r["emotion"] == "neutral" and 4 < r["duration_s"] < 9][int(__import__("os").environ.get("OFF","5")):int(__import__("os").environ.get("OFF","5"))+3]
ORDER = ["H", "D", "C", "D", "H", "C", "D", "H", "C"]

def rd(p):
    with wave.open(str(p)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), np.int16), w.getframerate()

def mcode(args):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
    if r.returncode: raise RuntimeError(r.stderr[:200])
    return json.loads(r.stdout)

PROMPT = ("Đoạn audio gồm 9 đoạn nói ngắn, ngăn bởi tiếng bíp. Hãy trả lời: (1) Có tổng cộng bao nhiêu NGƯỜI NÓI khác nhau? "
          "(2) Gán mỗi đoạn 1..9 cho một người nói (A, B, C...), các đoạn cùng một người dùng cùng chữ. "
          "(3) Mô tả ngắn giới tính, độ tuổi, chất giọng của từng người. Chỉ dựa vào giọng, không dựa vào nội dung.")
res = {}
for D in sys.argv[1:]:
    C = "C2_AB03"
    pick = lambda ref: [pathlib.Path(r["path"]) for r in R["rows"] if r["ref"] == ref and r["emotion"] == "neutral" and r["variant"] == 0]
    pools = {"H": list(Hs), "D": pick(D)[int(__import__("os").environ.get("OFFV","2")):int(__import__("os").environ.get("OFFV","2"))+3], "C": pick(C)[int(__import__("os").environ.get("OFFV","2")):int(__import__("os").environ.get("OFFV","2"))+3]}
    parts = []; sr = 24000
    beep = (0.15 * 32767 * np.sin(2 * np.pi * 1000 * np.arange(int(0.25 * sr)) / sr)).astype(np.int16)
    sil = np.zeros(int(0.4 * sr), np.int16)
    for role in ORDER:
        a, sr = rd(pools[role].pop(0)); parts += [a, sil, beep, sil]
    dst = OUT / f"blind_H_{D}_{C}_o{__import__("os").environ.get("OFFV","2")}.wav"
    with wave.open(str(dst), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(np.concatenate(parts).tobytes())
    up = mcode(["upload-temp-url", str(dst), "--mime-type", "audio/wav"])
    af = OUT / f"{dst.stem}.args.json"
    af.write_text(json.dumps({"audio_info": {"url": up["temp_url"], "mime_type": "audio/wav", "prompt": PROMPT}}, ensure_ascii=False), encoding="utf-8")
    out = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)])
    res[D] = out.get("transcription") or out
    print("=" * 80, "\n", D, "| dap an that:", " ".join(ORDER), "\n", res[D])
json.dump(res, open(OUT / f"blind_result_o{__import__('os').environ.get('OFFV','2')}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
