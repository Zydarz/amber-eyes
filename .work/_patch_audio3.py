from pathlib import Path

p = Path(".work/build_audio3.py")
content = p.read_text(encoding="utf-8")

old_part = """    floor = norm_to_voice(loop_to(amb, N, xf=1.0), -34)
    music += floor

    # voice-activity envelope for ducking: -26 under speech, -14 in pauses
    act_env = np.zeros(N, np.float32)
    for it in items:
        i, j = int(it["start"] * SR), int(it["end"] * SR)
        act_env[max(0, i - int(0.25 * SR)):j + int(0.25 * SR)] = 1
    k = int(0.4 * SR)
    act_env = np.convolve(act_env, np.ones(k, np.float32) / k, mode="same")
    duck = db(-14) + (db(-26) - db(-14)) * act_env"""

new_part = """    floor = norm_to_voice(loop_to(amb, N, xf=1.0), -31)
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
    duck = db(-14) + (db(-26) - db(-14)) * act_env"""

assert old_part in content, "old_part not found!"
content = content.replace(old_part, new_part)

old_tail = """    # end: piano tail 5 s fade-out after last voice
    pw = load(BGM / "bgm_piano_warm.mp3")
    tail = pw[: int(6 * SR)] * (v_rms / rms(pw)) * db(-14)
    tail *= np.concatenate([np.ones(int(1 * SR)), np.linspace(1, 0, len(tail) - int(1 * SR))]).astype(np.float32)
    place(music, tail, end_voice + 1.0)"""

new_tail = """    # end: piano tail 7.5 s fade-out after last voice
    pw = load(BGM / "bgm_piano_warm.mp3")
    tail = pw[: int(7.8 * SR)] * (v_rms / rms(pw)) * db(-14)
    tail *= np.concatenate([np.ones(int(1.5 * SR)), np.linspace(1, 0, len(tail) - int(1.5 * SR))]).astype(np.float32)
    place(music, tail, end_voice + 1.0)"""

assert old_tail in content, "old_tail not found!"
content = content.replace(old_tail, new_tail)

p.write_text(content, encoding="utf-8", newline="\n")
print("build_audio3.py patched successfully!")
