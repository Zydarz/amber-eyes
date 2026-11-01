"""Dung MASTER Tap 02 tu audio Higgs (buoc cuoi cua vong san xuat).

Chay sau khi kernel `amber-eyes-higgs-prod-t02-kaggle-gpu` xong va output da
tai ve `.work/kaggle_higgs/out_higgs_prod/`.

Chuoi:
  1. install_higgs_audio.py  -> .work/audio_s_higgs_t02/*.wav (203 file)
  2. build_audio3.py (AE_EP=02, AE_AUDIO_DIR=audio_s_higgs)
       -> 02_SAN_XUAT/Tap02/xuat_ban/Tap02_master.mp3  (+ .work/audio_master_t02.wav,
          .work/timeline_s_t02.json, .work/stems_t02/)

LUU Y ten thu muc: voi AE_EP=02, edition.w("audio_s_higgs") = ".work/audio_s_higgs_t02"
(khong phai "audio_s_higgs_t02" — se ra ".work/audio_s_higgs_t02_t02").
"""
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent          # .work/
ROOT = HERE.parent
PY = sys.executable
# Tap (L8) + ngon ngu (AE_LANG=en -> Tap02_EN/xuat_ban/Tap02_EN_master.mp3): Tap 02 VN giu ten cu (L9).
sys.path.insert(0, str(HERE))
import higgs_paths as P  # noqa: E402
EPN = P.EPN
PROD = P.PROD_EP
AUDIO_OUT = P.AUDIO_OUT
MASTER_DIR = P.MASTER_DIR
# so cau cua tap = so item trong payload nguon
N_SENT = len(json.loads(P.PAYLOAD_SRC.read_text(encoding="utf-8-sig"))["items"])

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def find_manifest():
    cands = sorted(PROD.rglob("higgs_manifest.json"))
    if not cands:
        raise SystemExit("!! khong tim thay higgs_manifest.json trong %s" % PROD)
    return cands[0]


def run(cmd, env=None):
    print("\n$", " ".join(str(c) for c in cmd), flush=True)
    r = subprocess.run([str(c) for c in cmd], env=env, cwd=str(ROOT))
    if r.returncode != 0:
        raise SystemExit("!! lenh that bai (rc=%d): %s" % (r.returncode, cmd[1] if len(cmd) > 1 else cmd[0]))
    return r


def main():
    man_p = find_manifest()
    rows = json.loads(man_p.read_text(encoding="utf-8-sig"))
    ok = [r for r in rows if r.get("ok")]
    ids = {r["id"] for r in ok}
    print("manifest:", man_p)
    print("task OK: %d / %d | cau co it nhat 1 ban: %d" % (len(ok), len(rows), len(ids)))
    if len(ids) < N_SENT:
        print("!! chi %d/%d cau co audio — master se thieu. Can chay catch-up." % (len(ids), N_SENT))

    # 1. cai audio vao thu muc rieng
    excl = P.EXCLUDE     # ban lech cao do >= 4 nc (khong uu tien)
    run([PY, HERE / "install_higgs_audio.py", "--dir", man_p.parent,
         "--out", AUDIO_OUT] + (["--exclude", excl] if excl.exists() else []))
    n = len(list(AUDIO_OUT.glob("*.wav")))
    print("\nfile wav da cai:", n)
    if n < N_SENT:
        raise SystemExit("!! thieu file audio (%d/%d) — dung catch-up truoc" % (n, N_SENT))

    # 2. dung master
    env = os.environ.copy()
    env["AE_EP"] = EPN
    env["AE_AUDIO_DIR"] = "audio_s_higgs"
    env["PYTHONIOENCODING"] = "utf-8"
    run([PY, HERE / "build_audio3.py"], env=env)

    mp3 = P.MASTER_MP3
    if mp3.exists():
        print("\n== MASTER ==")
        print(mp3, "%.2f MB" % (mp3.stat().st_size / 1e6))
    else:
        raise SystemExit("!! khong tao duoc master")


if __name__ == "__main__":
    main()
