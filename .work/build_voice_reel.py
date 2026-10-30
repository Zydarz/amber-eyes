"""Dung REEL nghe thu giong Higgs (Tay 02) tu pilot v6 da co tren dia.

Y tuong: pilot v6 vua san 5 o clone DUNG mapping san xuat cuoi cung
(H<-H.wav, D<-M_HIGH.wav, C<-C.wav, N1<-W6_LOW.wav, N2<-W5_HIGH.wav),
cung `temperature 0.8` va cung bo seed theo cau => giong nghe ra y het
ban san xuat 416 file, chi khac o so cau.

Output:
  02_SAN_XUAT/Tap02/xuat_ban/DEMO_giong_Higgs.mp3   (reel lien mach)
  02_SAN_XUAT/Tap02/xuat_ban/DEMO_giong_Higgs.txt   (bang thoi gian <-> vai/cau)
"""
import json
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent          # .work/
ROOT = HERE.parent
FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
V6 = HERE / "kaggle_higgs" / "out_higgs_v6" / "out_higgs_v6"
PAYLOAD_P = HERE / "kaggle_higgs" / "dataset_voxcpm2" / "pilot_payload_v6.json"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban"
SR = 24000
GAP = 0.8          # giua 2 cau trong cung vai
GROUP_GAP = 2.2    # giua 2 vai (dau moi nhom)

# (nhom vai, nhan vai, [ten file mau])   -- bien the s0
GROUPS = [
    ("H", "H — người dẫn (nam, English_CaptivatingStoryteller)",
     ["P6_H__H__0_H_H_t0.8_s0.wav", "P6_H__H__1_H_H_t0.8_s0.wav", "P6_H__H__5_H_H_t0.8_s0.wav"]),
    ("D", "D — điều tra viên (nam 50+ khàn, M_HIGH)",
     ["P6_D__M_HIGH__2_D_M_HIGH_t0.8_s0.wav", "P6_D__M_HIGH__3_D_M_HIGH_t0.8_s0.wav"]),
    ("C", "C — chuyên gia tâm lý (nữ 50, C.wav)",
     ["P6_C__C__0_C_C_t0.8_s0.wav", "P6_C__C__3_C_C_t0.8_s0.wav"]),
    ("N1", "N1 — nhân vật nữ phụ (nữ, W6_LOW)",
     ["P6_N1__W6_LOW__0_N1_W6_LOW_t0.8_s0.wav", "P6_N1__W6_LOW__3_N1_W6_LOW_t0.8_s0.wav"]),
    ("N2", "N2 — nhân vật nữ phụ (nữ cao, W5_HIGH)",
     ["P6_N2__W5_HIGH__4_N2_W5_HIGH_t0.8_s0.wav", "P6_N2__W5_HIGH__1_N2_W5_HIGH_t0.8_s0.wav"]),
]


def load_wav(p):
    r = subprocess.run([str(FF), "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR),
                        "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).copy()


def main():
    payload = json.loads(PAYLOAD_P.read_text(encoding="utf-8-sig"))
    items = payload["items"]
    # ten file pilot = "<item_id>_<role>_<ref>_t<t>_s<v>.wav" -> item_id la tien to
    by_file = {}
    for fn in sorted({i["id"] for i in items}):
        by_file[fn] = next(i for i in items if i["id"] == fn)

    def item_for(fname):
        stem = fname[:-4] if fname.lower().endswith(".wav") else fname
        best = None
        for pid in by_file:
            if stem.startswith(pid + "_") or stem == pid:
                if best is None or len(pid) > len(best):
                    best = pid
        return by_file.get(best) if best else None

    chunks, tmap = [], []
    t = 0.0
    for g, (role, label, files) in enumerate(GROUPS):
        tmap.append((t, "== %s" % label))
        for j, fn in enumerate(files):
            p = V6 / fn
            if not p.exists():
                print("!! thieu:", fn)
                continue
            x = load_wav(p)
            it = item_for(fn)
            src = it.get("src_id", "?") if it else "?"
            emo = it.get("emotion", "") if it else ""
            chunks.append(x)
            tmap.append((t, "[%s] %s %s" % (role, src, ("(" + emo + ")") if emo else "")))
            t += len(x) / SR
            tmap.append((t, "      “%s”" % ((it.get("text_plain", "") if it else "")[:110])))
            if j < len(files) - 1:
                chunks.append(np.zeros(int(GAP * SR), np.float32))
                t += GAP
        if g < len(GROUPS) - 1:
            chunks.append(np.zeros(int(GROUP_GAP * SR), np.float32))
            t += GROUP_GAP

    audio = np.concatenate(chunks)
    # chuan hoa -16 LUFS (dung ffmpeg 2 pass nhu build_audio3)
    wav = HERE / "demo_voice_reel.wav"
    x = audio
    x = x / max(1e-9, np.abs(x).max()) * 0.89
    pcm = (x * 32767).astype(np.int16)
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "s16le", "-ar", str(SR), "-ac", "1",
                    "-i", "pipe:0", str(wav)], input=pcm.tobytes(), check=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    mp3 = OUT_DIR / "DEMO_giong_Higgs.mp3"
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(wav), "-af",
                        "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    js = r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1]
    m = json.loads(js)
    af = (f"loudnorm=I=-16:TP=-1.5:LRA=11:linear=true:measured_I={m['input_i']}:"
          f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
          f"offset={m['target_offset']},aresample=48000")
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(wav), "-af", af, "-ac", "2",
                    "-c:a", "libmp3lame", "-b:a", "192k", str(mp3)], check=True)

    lines = ["REEL NGHE THU GIONG HIGGS — TAP 02 (Higgs Audio v3, 24 kHz)",
             "Nguon: pilot v6, DUNG 5 mapping san xuat cuoi cung",
             "  H<-H.wav · D<-M_HIGH.wav · C<-C.wav · N1<-W6_LOW.wav · N2<-W5_HIGH.wav",
             "  temperature 0.8 · top_p 0.95 · top_k 50 · bien the s0 (seed co dinh theo cau)",
             "",
             "Dung de danh gia: chat luong doc, phan biet giong nam H vs D, cam xuc.",
             "Khong phai ban thanh pham cuoi cung (ban do dung 416 file, se doi sau khi do CER).",
             ""]
    for tt, s in tmap:
        lines.append("%7.1f s | %s" % (tt, s))
    (OUT_DIR / "DEMO_giong_Higgs.txt").write_text("\n".join(lines), encoding="utf-8")

    print("reel: %d cau | %.1f s" % (sum(len(g[2]) for g in GROUPS), t))
    print("->", mp3, mp3.stat().st_size, "bytes")
    print("->", OUT_DIR / "DEMO_giong_Higgs.txt")


if __name__ == "__main__":
    main()
