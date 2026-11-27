# -*- coding: utf-8 -*-
"""Dựng timeline_s[_EN|_JA]_t25.json từ SRT + kịch bản (Tập 25 mất file TTS từng câu, chỉ còn master đã trộn).

  py -3 .work/_timeline_from_srt_t25.py [--lang vi|en|ja] [--write]

Cách làm: chuẩn hoá chữ (NFKC, bỏ ký tự không phải chữ/số), ghép nối mọi câu kịch bản và mọi cue SRT
(bỏ thẻ [VAI]), mỗi câu chiếm một đoạn ký tự -> start/end = nội suy tuyến tính trong cue chứa ký tự đầu/cuối.
total = thời lượng master (ffmpeg), intro 22.41. Cổng: tổng ký tự khớp, câu đầu = 23.0 s, các câu tăng dần,
câu cuối end <= total.  Chỉ ghi file khi có --write.
"""
import argparse, bisect, json, re, subprocess, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import parse_kichban as pk  # noqa: E402

B = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham"
CFG = {
    "vi": ("01_KICH_BAN/Ho_So_Toi_Pham/Tap25/kichban_tap25_23102026.md", "Tap25/xuat_ban/Tap25.srt", "Tap25/xuat_ban/Tap25_master.mp3", "timeline_s_t25.json"),
    "en": ("01_KICH_BAN/Ho_So_Toi_Pham/Tap25_EN/kichban_tap25_EN.md", "Tap25_EN/xuat_ban/Tap25_EN.srt", "Tap25_EN/xuat_ban/Tap25_EN_master.mp3", "timeline_s_EN_t25.json"),
    "ja": ("01_KICH_BAN/Ho_So_Toi_Pham/Tap25_JA/kichban_tap25_JA.md", "Tap25_JA/xuat_ban/Tap25_JA.srt", "Tap25_JA/xuat_ban/Tap25_JA_master.mp3", "timeline_s_JA_t25.json"),
}
NMAP = {"1.07": "N1", "4.09": "N2"}  # = EPISODES["25"]["n_element"]
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"


def norm(s):
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", s).lower())


def duration(p):
    r = subprocess.run([str(FF), "-i", str(p)], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])


def ts(a):
    h, m, s = a.replace(",", ".").split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def build(lang):
    kb, srt, mst, outn = CFG[lang]
    els = pk.parse_file(str(ROOT / kb))
    sents = []
    for e in els:
        for s in e.get("sentences") or []:
            sents.append((s["id"], e["id"], e["act"], NMAP.get(e["id"], e["role"]) if e["role"] == "N" else e["role"], s["text"]))
    cues = []
    for blk in re.split(r"\n\n+", (B / srt).read_text(encoding="utf-8").replace("\r", "").strip()):
        l = blk.split("\n", 2)
        a, b = l[1].split(" --> ")
        cues.append((ts(a), ts(b), norm(re.sub(r"\[[^\]]+\]", "", l[2]))))
    cum, pos = [], 0
    for c in cues:
        cum.append(pos); pos += len(c[2])
    total_c = pos
    sn = [norm(s[4]) for s in sents]
    tot_s = sum(map(len, sn))
    assert tot_s == total_c, f"{lang}: tổng ký tự câu {tot_s} != SRT {total_c}"

    def at(off):
        k = max(0, bisect.bisect_right(cum, off) - 1)
        s, e, t = cues[k]
        f = 0 if not t else min(1.0, (off - cum[k]) / len(t))
        return s + f * (e - s)

    items, p = [], 0
    for (sid, eid, act, role, text), n in zip(sents, map(len, sn)):
        st = cues[min(bisect.bisect_right(cum, p) - 1, len(cues) - 1)][0] if p < total_c else cues[-1][0]
        # start = đầu cue chứa ký tự đầu nếu câu mở đầu cue; ngược lại nội suy
        k = max(0, bisect.bisect_right(cum, p) - 1)
        st = cues[k][0] if cum[k] == p else at(p)
        en = at(p + n)
        if p + n >= total_c: en = cues[-1][1]
        items.append({"id": sid, "element": eid, "act": act, "role": role, "start": round(st, 3), "end": round(en, 3), "text": text})
        p += n
    total = round(duration(B / mst), 3)
    errs = []
    if abs(items[0]["start"] - 23.0) > 0.3: errs.append(f"câu đầu bắt đầu {items[0]['start']} (mong 23.0)")
    for a, b in zip(items, items[1:]):
        if b["start"] < a["start"] - 1e-6: errs.append(f"đảo thứ tự {a['id']}->{b['id']}")
    if items[-1]["end"] > total + 0.05: errs.append(f"câu cuối end {items[-1]['end']} > total {total}")
    acts, markers = {}, [{"type": "INTRO", "start": 0.0, "end": 22.41}]
    for it in items:
        a = str(it["act"])
        acts.setdefault(a, [it["start"], it["end"]])[1] = it["end"]
    for a, (s, e) in acts.items():
        if a != "1": markers.append({"type": "ACT", "act": int(a), "start": round(s - 2.0, 3), "end": round(s, 3)})
    return {"total": total, "intro": 22.41, "items": items, "markers": markers, "acts": list(acts.items())}, errs, outn


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lang", default="vi"); ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    tl, errs, outn = build(a.lang)
    it = tl["items"]
    gaps = [b["start"] - a_["end"] for a_, b in zip(it, it[1:])]
    print(f"[{a.lang}] {len(it)} câu · total {tl['total']} s · câu đầu {it[0]['start']} · câu cuối end {it[-1]['end']} · "
          f"khoảng giữa câu: min {min(gaps):.2f} med {sorted(gaps)[len(gaps)//2]:.2f} max {max(gaps):.2f} · acts {tl['acts']}")
    for e in errs: print("  LỖI:", e)
    if errs: sys.exit(1)
    if a.write:
        dst = WORK / outn
        if dst.exists(): sys.exit(f"{dst.name} đã tồn tại — sao lưu/xoá thủ công trước (L5)")
        json.dump(tl, open(dst, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
        print("ghi", dst)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
