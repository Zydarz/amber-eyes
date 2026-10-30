#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B3 — build the episode audio master from per-sentence TTS (plan v9 section 3).

Outputs
  Tap01_master.mp3 / .work/audio_master.wav   loudness-normalised mix (-16 LUFS, linear)
  .work/timeline_s.json                       measured start/end of every sentence + markers
  .work/stems/{H,D,C,N1,N2}.wav               per-character voice (for badge waveforms)
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np

# console Windows mặc định cp1252 -> không in được tiếng Việt có dấu
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402  (AE_LANG=en -> English edition)

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
BGM = ROOT / "assets" / "bgm"
SFX = ROOT / "assets" / "sfx"
OUT_DIR = ED.OUT_DIR                                       # thành phẩm của tập
SR = 44100

INTRO = 22.41            # music box length, intro picture length
FIRST_VOICE = 23.0
GAP_SENT, GAP_Q, GAP_SPEAKER, GAP_ACT, MAX_PAUSE = 0.35, 0.60, 0.70, 2.0, 2.5
BED = ED.EP["bed"]                       # nhạc theo hồi của tập (edition.EPISODES)

# ---- SFX (assets/sfx/*.wav, tự tổng hợp bằng .work/make_sfx.py) ----
# (file, marker_id, offset_s, rel_db)  -> đặt tại  marker_at + offset_s
# offset âm = đặt TRƯỚC mốc để tiếng nối vào câu thoại kế tiếp.
# Mức tính theo RMS lời, hiệu chuẩn bằng cách nghe thật trong bản thành phẩm
# (mốc tham chiếu: tiếng "Tách" ở −6 dB, đã rõ tai). Tập 01: 11 dòng; Tập 02 dùng ED.EP["sfx_sheet"].
SFX_CUES = ED.EP["sfx_cues"]

# nghỉ thêm sau câu do file diễn xuất quy định (Tập 02: acting_tap02.json "_pause_after")
PAUSE_AFTER = (json.loads(ED.ACTING.read_text(encoding="utf-8")).get("_pause_after", {})
               if ED.ACTING and ED.ACTING.exists() else {})


def db(x):
    return 10 ** (x / 20)


def load(path, channels=1):
    r = subprocess.run([str(FF), "-v", "error", "-i", str(path), "-ac", str(channels), "-ar", str(SR),
                        "-f", "f32le", "-"], capture_output=True, check=True)
    x = np.frombuffer(r.stdout, np.float32).copy()
    return x.reshape(-1, 2) if channels == 2 else x


def rms(x):
    x = x[np.abs(x) > 1e-4]
    return float(np.sqrt((x ** 2).mean())) if len(x) else 1e-6


def loop_to(x, n, xf=0.5):
    """Loop x to length n; consecutive copies overlap by xf s with equal-gain fades."""
    k = int(xf * SR)
    fin = np.linspace(0, 1, k, dtype=np.float32)
    out = np.zeros(n + len(x), np.float32)
    pos, first = 0, True
    while pos < n:
        seg = x.copy()
        if not first:
            seg[:k] *= fin
        seg[-k:] *= fin[::-1]
        out[pos:pos + len(seg)] += seg
        pos += len(seg) - k
        first = False
    return out[:n]


def place(track, x, t, gain=1.0):
    i = int(round(t * SR))
    j = min(len(track), i + len(x))
    if j > i:
        track[i:j] += x[: j - i] * gain


def click(length=0.06):
    n = int(length * SR)
    rng = np.random.default_rng(3)
    x = rng.normal(0, 1, n).astype(np.float32)
    x = np.diff(np.concatenate([[0], x])).astype(np.float32)        # high-pass-ish
    env = np.exp(-np.linspace(0, 9, n)).astype(np.float32)
    return x * env * 0.5


def main():
    script = json.loads(ED.SCRIPT_JSON.read_text(encoding="utf-8"))
    man = {m["id"]: m for m in json.loads(ED.w("tts_manifest.json").read_text(encoding="utf-8"))}
    # L5: thu muc audio mac dinh = MiniMax (`audio_s_t02`).
    # Dat AE_AUDIO_DIR=audio_s_higgs_t02 de dung audio Higgs (WAV 24 kHz),
    # thu muc MiniMax giu nguyen khong bi ghi de.
    audio_dir = os.environ.get("AE_AUDIO_DIR", "audio_s")
    if audio_dir != "audio_s":
        print("nguon audio:", ED.w(audio_dir))

    def audio_path(m):
        p = ED.w(audio_dir) / m["file"]
        if not p.exists():
            p = p.with_suffix(".wav")          # audio Higgs: .wav 24 kHz
        return p

    voice_cache = {sid: load(audio_path(m)) for sid, m in man.items()}

    # ---------------- 1. lay out the timeline
    t = FIRST_VOICE
    items, markers = [], [{"type": "INTRO", "start": 0.0, "end": INTRO}]
    acts = {}
    cur_act = None
    pending = None          # (role, last_text) of the turn just spoken, gap not yet added
    for e in script:
        act = e["act"]
        if cur_act is not None and act != cur_act:
            markers.append({"type": "ACT", "act": act, "start": round(t, 3), "end": round(t + GAP_ACT, 3)})
            t += GAP_ACT
            pending = None
        if act not in acts:
            acts[act] = [t, t]
        cur_act = act
        if e["kind"] == "NGHI":
            sec = min(e["sec"], MAX_PAUSE)
            markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3), "end": round(t + sec, 3),
                            "desc": e.get("desc", "")})
            t += sec
            pending = None                    # the pause replaces the gap
        elif e["kind"] in ("SFX", "BGM"):
            markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3), "desc": e.get("desc", "")})
        else:
            role = man[e["sentences"][0]["id"]]["role"]
            if pending:
                g = GAP_SPEAKER if pending[0] != role else GAP_SENT
                if pending[1].rstrip("”\" ").endswith("?"):
                    g = max(g, GAP_Q)
                t += g
            for k, s in enumerate(e["sentences"]):
                d = len(voice_cache[s["id"]]) / SR
                items.append({"id": s["id"], "element": e["id"], "act": act, "role": role,
                              "start": round(t, 3), "end": round(t + d, 3), "text": man[s["id"]]["display"]})
                t += d
                t += PAUSE_AFTER.get(s["id"], 0.0)  # khoảnh khắc cần lặng (file diễn xuất)
                if k < len(e["sentences"]) - 1:
                    t += GAP_Q if s["text"].rstrip("”\" ").endswith("?") else GAP_SENT
                    if ED.EN and man[s["id"]]["emotion"] in ("sad", "fearful"):
                        t += 0.2                   # let heavy lines land (English edition)
            pending = (role, e["sentences"][-1]["text"])
        acts[act][1] = t
    end_voice = t
    total = end_voice + 1.0 + 5.0 + 3.0          # click, piano tail 5 s, 3 s silence (plan 5.13–5.14)
    N = int(total * SR) + SR

    # ---------------- 2. voice + stems
    voice = np.zeros(N, np.float32)
    stems = {r: np.zeros(N, np.float32) for r in ("H", "D", "C", "N1", "N2")}
    for it in items:
        x = voice_cache[it["id"]]
        place(voice, x, it["start"])
        place(stems[it["role"]], x, it["start"])
    v_rms = rms(voice)

    # ---------------- 3. music
    music = np.zeros(N, np.float32)
    def norm_to_voice(x, rel_db):
        return x * (v_rms / rms(x)) * db(rel_db)

    mb = load(BGM / "bgm_music_box.mp3")
    place(music, norm_to_voice(mb, -4), 0.0)                                   # intro

    # ambient floor for the whole episode (V4). The source file has silent
    # stretches (0–0.44 s, 13.5–15 s, 20.2 s–end): loop only its continuous
    # 0.5–13.4 s part with a 1 s crossfade, at -34 dB under the voice.
    amb_full = load(BGM / "bgm_ambient_deep.mp3")
    amb = amb_full[int(0.5 * SR):int(13.4 * SR)]
    floor = norm_to_voice(loop_to(amb, N, xf=1.0), -31)
    music += floor

    # voice-activity envelope for ducking: -26 under speech, -14 in pauses
    act_env = np.zeros(N, np.float32)
    for it in items:
        i, j = int(it["start"] * SR), int(it["end"] * SR)
        act_env[max(0, i - int(0.25 * SR)):j + int(0.25 * SR)] = 1
    k = int(0.4 * SR)
    pad_left = k // 2
    pad_right = k - 1 - pad_left
    pad = np.pad(act_env, (pad_left + 1, pad_right), mode="constant")
    cs = np.cumsum(pad, dtype=np.float64)
    act_env = ((cs[k:] - cs[:-k]) / k).astype(np.float32)
    duck = db(-14) + (db(-26) - db(-14)) * act_env

    # drone: 19.5 s fade-in -> until the act-1 music cue (Tập 01: 1.12 · Tập 02: 1.16)
    cue_112_m = next((m for m in markers if m.get("id") == ED.EP["act1_cue"]), None)
    cue_112 = cue_112_m.get("at", cue_112_m.get("start", 23.0)) if cue_112_m else 23.0
    drone = load(BGM / "bgm_sub_drone.mp3")
    a, b = 19.5, cue_112 + 2.0
    seg = loop_to(drone, int((b - a) * SR))
    seg = seg * (v_rms / rms(seg))
    env = np.ones(len(seg), np.float32) * db(-26)
    fi = int(2.9 * SR)
    env[:fi] = np.linspace(db(-40), db(-26), fi)
    env[-int(2 * SR):] *= np.linspace(1, 0, int(2 * SR))
    place(music, seg * env, a)

    # beds per act (act 1 bed starts at the cello cue) — riêng một lớp để "tắt nhạc" được ở câu hé lộ
    beds = np.zeros(N, np.float32)
    for act, (s, e) in acts.items():
        # act 1 bed starts at the cello cue; later beds start at the act
        # boundary so the 2 s act card is never left without music
        s = cue_112 if act == 1 else s - GAP_ACT
        files = BED[act] if isinstance(BED[act], tuple) else (BED[act],)
        if files == ("bgm_ambient_deep.mp3",):
            src = amb                          # silent stretches removed (see floor)
        else:
            src = np.concatenate([load(BGM / f) for f in files])
        n = int((e - s + 2.0) * SR)
        seg = loop_to(src, n)
        seg = seg * (v_rms / rms(seg))
        fade = int(1.5 * SR)
        seg[:fade] *= np.linspace(0, 1, fade)
        seg[-fade:] *= np.linspace(1, 0, fade)
        i = int(s * SR)
        j = min(N, i + n)
        beds[i:j] += seg[: j - i] * duck[i:j]

    sheet = (json.loads(ED.EP["sfx_sheet"].read_text(encoding="utf-8"))
             if ED.EP["sfx_sheet"] and ED.EP["sfx_sheet"].exists() else {})
    sent = {it["id"]: it for it in items}
    for a, b in sheet.get("music_drop", {}).get("ranges", []):        # im lặng làm câu hé lộ nặng hơn
        i, j = int((sent[a]["start"] - 0.3) * SR), int((sent[b]["end"] + 0.6) * SR)
        f = int(0.3 * SR)
        beds[i - f:i] *= np.linspace(1, 0, f)
        beds[i:j] = 0
        beds[j:j + f] *= np.linspace(0, 1, f)
    music += beds

    # "nhạc nền dừng đột ngột" (mốc của tập): mute melodic beds, ambient floor stays
    silence_id = ED.EP.get("silence_cue")
    m109 = next((m for m in markers if m.get("id") == silence_id), None)
    if m109 and "start" in m109 and "end" in m109:
        i, j = int(m109["start"] * SR), int(m109["end"] * SR)
        music[i:j] = floor[i:j]

    # end: piano tail 7.5 s fade-out after last voice
    pw = load(BGM / "bgm_piano_warm.mp3")
    tail = pw[: int(7.8 * SR)] * (v_rms / rms(pw)) * db(-14)
    tail *= np.concatenate([np.ones(int(1.5 * SR)), np.linspace(1, 0, len(tail) - int(1.5 * SR))]).astype(np.float32)
    place(music, tail, end_voice + 1.0)

    # ---------------- 4. SFX: recorder click (host's signature)
    sfx = np.zeros(N, np.float32)
    c = click() * (v_rms / rms(click())) * db(-6)
    for cid in ED.EP["click_cues"]:
        m_at = next((m["at"] for m in markers if m.get("id") == cid), None)
        if m_at is None:
            m_at = next((it["start"] for it in items if it.get("id") == cid or it.get("element") == cid), None)
        if m_at is not None:
            place(sfx, c, m_at - 0.30)
    place(sfx, c, end_voice + 0.8)

    # ---------------- 4b. SFX files trong assets/sfx (bổ sung 22/10/2026)
    # Mỗi tiếng đặt trước mốc để nối vào câu thoại kế tiếp; mức tương đối so
    # với RMS lời (giống quy ước nhạc nền). Thiếu file -> bỏ qua, không làm hỏng cả tập.
    for fname, mid, off, rel in SFX_CUES:
        fp = SFX / fname
        if not fp.exists():
            print(f"  [SFX] THIEU FILE {fname} -> bo qua")
            continue
        at = next(m["at"] for m in markers if m.get("id") == mid)
        x = load(fp)
        place(sfx, norm_to_voice(x, rel), at + off)
        print(f"  [SFX] {fname:<26} moc {mid} +{off:+.2f}s  muc {rel} dB", flush=True)

    # ---------------- 4c. SFX theo shot (bản EN, .work/sfx_shots_EN.json) — cần shots của lượt trước
    place_shot_sfx(sfx, items, total, norm_to_voice, N)

    # ---------------- 4d. bảng âm thanh STEREO của tập (Tập 02: nền môi trường + tiếng động)
    sfx2 = place_sheet(sheet, items, markers, act_env, v_rms, N) if sheet else None

    mix = voice + music + sfx
    if sfx2 is not None:
        mix = mix[:, None] + sfx2
    mix = mix[: int(total * SR)]
    peak = np.abs(mix).max()
    if peak > 0.98:
        mix *= 0.98 / peak
    wav = ED.w("audio_mix_raw.wav")
    write_wav(wav, mix)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # ---------------- 5. loudnorm two-pass, linear
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(wav), "-af",
                        "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    js = r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1]
    m = json.loads(js)
    af = (f"loudnorm=I=-16:TP=-1.5:LRA=11:linear=true:measured_I={m['input_i']}:"
          f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
          f"offset={m['target_offset']},aresample=48000")
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(wav), "-af", af, "-ac", "2",
                    str(ED.w("audio_master.wav"))], check=True)
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(ED.w("audio_master.wav")),
                    "-c:a", "libmp3lame", "-b:a", "192k", str(OUT_DIR / (ED.MASTER + ".mp3"))], check=True)

    # ---------------- 6. stems (16 kHz is enough for waveforms)
    sd = ED.w("stems")
    sd.mkdir(exist_ok=True)
    for role, x in stems.items():
        write_wav(sd / f"{role}.wav", x[: int(total * SR)], resample_to=16000)
    # stem SFX giữ nguyên 44.1 kHz để kiểm chứng được (đối chiếu tương quan chéo)
    write_wav(sd / "SFX.wav", sfx[: int(total * SR)])
    if sfx2 is not None:
        write_wav(sd / "SFX_stereo.wav", sfx2[: int(total * SR)])

    ED.w("timeline_s.json").write_text(json.dumps(
        {"total": round(total, 3), "intro": INTRO, "items": items, "markers": markers,
         "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}},
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"tổng {total:.1f} s · {len(items)} câu · lời đầu {items[0]['start']} s · lời cuối hết {end_voice:.1f} s")
    print("hồi:", {k: f"{a:.1f}–{b:.1f}" for k, (a, b) in acts.items()})


def place_shot_sfx(sfx, items, total, norm_to_voice, N):
    """Shot-anchored SFX. Times come from shots_*.json, which parse_shots builds from the
    timeline of the previous run: run build_audio3 -> parse_shots -> build_audio3 again."""
    cfg_p = ED.w("sfx_shots.json")
    shots_p = ED.w("shots.json")
    if not cfg_p.exists():
        return
    if not shots_p.exists():
        print("  [SFX shot] chưa có shots -> chạy parse_shots.py rồi chạy lại build_audio3.py")
        return
    sh = json.loads(shots_p.read_text(encoding="utf-8"))
    if abs(sh["total"] - round(total, 3)) > 0.01:
        print(f"  [SFX shot] shots cũ ({sh['total']} s ≠ {total:.3f} s) -> chạy parse_shots.py rồi chạy lại build_audio3.py")
        return
    S = {s["id"]: s for s in sh["shots"]}
    sent = {it["id"]: it for it in items}
    cfg = json.loads(cfg_p.read_text(encoding="utf-8"))
    cache = {}

    def clip(name):
        if name not in cache:
            cache[name] = load(SFX / name)
        return cache[name]

    def phrase_at(s, p):
        p = p.lower()
        for sid in s["sentences"]:
            it = sent[sid]
            k = it["text"].lower().find(p)
            if k >= 0:
                return it["start"] + (it["end"] - it["start"]) * k / max(1, len(it["text"]))
        return None

    def anchor(s, a):
        first = sent[s["sentences"][0]]["start"] if s["sentences"] else s["start"]
        if a == "start":
            return first
        if a == "end":
            return s["end"]
        if a == "beat":
            return phrase_at(s, s["beats"][0]) if s["beats"] else None
        if a.startswith("p:"):
            return phrase_at(s, a[2:])
        if a.startswith("s") and a[1:].isdigit():
            k = int(a[1:]) - 1
            return sent[s["sentences"][k]]["start"] if k < len(s["sentences"]) else None
        return None

    n_ok, miss = 0, []
    for sid, name, a, off, rel in cfg.get("cues", []):
        t = anchor(S[sid], a) if sid in S else None
        if t is None or not (SFX / name).exists():
            miss.append(f"{sid}:{name}:{a}")
            continue
        place(sfx, norm_to_voice(clip(name), rel), max(0.0, t + off))
        n_ok += 1
    for b in cfg.get("beds", []):
        a, z = S[b["from"]]["start"], S[b["to"]]["end"]
        n = int((z - a) * SR)
        seg = loop_to(clip(b["file"]), n, xf=1.0)
        f = int(2.0 * SR)
        seg[:f] *= np.linspace(0, 1, f)
        seg[-f:] *= np.linspace(1, 0, f)
        place(sfx, norm_to_voice(seg, b["db"]), a)
        n_ok += 1
    print(f"  [SFX shot] đặt {n_ok} tiếng" + (f" · bỏ qua {len(miss)}: {miss}" if miss else ""))


def place_sheet(sheet, items, markers, act_env, v_rms, N):
    """Bảng âm thanh của tập (.work/sfx_tapXX.json) → lớp STEREO (N, 2).

    ambience: [từ câu, đến câu, file, dB] — nền liên tục, mờ vào/ra 1,5 s, hạ thêm 4 dB khi có lời.
    cues:     [mốc, 'start'|'end', lệch s, file, dB] — mốc là mã câu ('4.10#9') hoặc mã SFX/BGM/NGHI của kịch bản.
    Mức tính theo RMS lời như mọi lớp khác. Thiếu file -> bỏ qua, không làm hỏng cả tập.
    """
    out = np.zeros((N, 2), np.float32)
    sent = {it["id"]: it for it in items}
    mk = {m["id"]: m for m in markers if m.get("id")}
    cache = {}

    def clip(name):
        if name not in cache:
            cache[name] = load(SFX / name, channels=2)
        return cache[name]

    def scaled(x, rel):
        return x * (v_rms / rms(x.mean(1))) * db(rel)

    def anchor(ref, where):
        if ref in sent:
            return sent[ref]["start"] if where == "start" else sent[ref]["end"]
        m = mk.get(ref)
        if m is None:
            return None
        return m.get("at", m.get("start") if where == "start" else m.get("end"))

    under = (1 - (1 - db(-4)) * np.clip(act_env, 0, 1))[:, None]
    n_amb = n_fx = 0
    miss = []
    for a, b, name, rel in sheet.get("ambience", []):
        if (SFX / name).exists():
            fp = SFX / name
        elif (SFX / "t2" / name).exists():
            fp = SFX / "t2" / name
            name = "t2/" + name
        else:
            miss.append(name)
            continue
        if a not in sent or b not in sent:
            miss.append(name)
            continue
        s0, s1 = max(0.0, sent[a]["start"] - 1.0), sent[b]["end"] + 1.0
        n = int((s1 - s0) * SR)
        src = clip(name)
        xf = min(int(1.0 * SR), len(src) // 4)            # nền ngắn (8 s từ video AI) -> hoà chồng chỗ nối
        seg = np.zeros((n + len(src), 2), np.float32)
        ramp = np.linspace(0, 1, xf, dtype=np.float32)[:, None]
        pos = 0
        while pos < n:
            c = src.copy()
            if pos:
                c[:xf] *= ramp
            c[-xf:] *= ramp[::-1]
            seg[pos:pos + len(c)] += c
            pos += len(c) - xf
        seg = seg[:n]
        f = min(int(1.5 * SR), n // 3)
        seg[:f] *= np.linspace(0, 1, f)[:, None]
        seg[-f:] *= np.linspace(1, 0, f)[:, None]
        i = int(s0 * SR)
        j = min(N, i + n)
        out[i:j] += scaled(seg, rel)[: j - i] * under[i:j]
        n_amb += 1
    for ref, where, off, name, rel in sheet.get("cues", []):
        t = anchor(ref, where)
        if (SFX / name).exists():
            pass
        elif (SFX / "t2" / name).exists():
            name = "t2/" + name
        else:
            miss.append(f"{ref}:{name}")
            continue
        if t is None:
            miss.append(f"{ref}:{name}")
            continue
        x = scaled(clip(name), rel)
        i = int(max(0.0, t + off) * SR)
        j = min(N, i + len(x))
        out[i:j] += x[: j - i]
        n_fx += 1
    print(f"  [SFX bảng] {n_amb} đoạn nền · {n_fx} tiếng động" + (f" · bỏ qua {miss}" if miss else ""))
    return out


def write_wav(path, x, resample_to=None):
    raw = path.with_suffix(".f32")
    x = np.asarray(x, np.float32)
    ch = 2 if x.ndim == 2 else 1
    raw.write_bytes(x.tobytes())
    args = [str(FF), "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", str(ch), "-i", str(raw)]
    if resample_to:
        args += ["-ar", str(resample_to)]
    args += ["-c:a", "pcm_s16le", str(path)]
    subprocess.run(args, check=True)
    raw.unlink()


if __name__ == "__main__":
    main()
