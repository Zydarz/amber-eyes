#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""I — ĐO CER tiếng Việt cho 3 giọng bộ A đang dùng ở Tập 02.

Cách làm:
  * Audio TTS của Tập 02 ĐÃ CÓ SẴN trong .work/audio_s_t02/  -> không tổng hợp lại,
    đo trên đúng thành phẩm thật.
  * Chuẩn tham chiếu = trường `text` của tts_manifest_t02.json (đúng thứ đã gửi cho engine).
  * ASR = connector__matrix__listen_audio (đúng hạ tầng dự án đang dùng).
  * CER = hàm cer() y hệt voice_audition.py.
  * 2 giọng đối chứng: Vietnamese_kindhearted_girl (kỳ vọng ~0%) và
    English_CalmWoman (kỳ vọng ~9%) -> chứng minh phép đo không sai.
"""
import json
import re
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT = WORK / "cer_bo_a_tap02"
AUDIO = WORK / "audio_s_t02"
MAN = WORK / "tts_manifest_t02.json"

N_MAIN = 15          # so cau moi giong chinh
N_CTRL = 5           # so cau moi giong doi chung


def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:400])
    return json.loads(r.stdout)


def norm(t):
    t = unicodedata.normalize("NFC", t.lower())
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def cer(ref, hyp):
    a, b = norm(ref), norm(hyp)
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(b) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return d[-1] / max(1, len(a))


def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.mp3"


def asr(local_mp3, prompt="Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."):
    """upload -> listen_audio -> transcription (có cache theo tên file)."""
    cache = OUT / f"asr_{local_mp3.stem}.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    up = mcode(["upload_temp_url", str(local_mp3), "--mime-type", "audio/mpeg"], 300)
    url = up.get("temp_url") or up.get("url")
    af = OUT / f"req_{local_mp3.stem}.json"
    af.write_text(json.dumps({"audio_info": {"url": url, "mime_type": "audio/mpeg", "prompt": prompt}},
                             ensure_ascii=False), encoding="utf-8")
    tr = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)], 600)
    cache.write_text(json.dumps(tr, ensure_ascii=False), encoding="utf-8")
    return tr


def hyp_of(tr):
    if isinstance(tr, str):
        return tr
    for k in ("transcription", "text", "content", "result"):
        if isinstance(tr, dict) and tr.get(k):
            v = tr[k]
            if isinstance(v, str):
                return v
            if isinstance(v, list) and v:
                return " ".join(str(x) for x in v)
            return json.dumps(v, ensure_ascii=False)
    return json.dumps(tr, ensure_ascii=False)[:200]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    items = json.loads(MAN.read_text(encoding="utf-8"))

    # loại cau co loi van ban da biet (G1 '...', G7 ngoac) -> do chat luong GIONG, khong do loi script
    BAD = re.compile(r"\.\.\.|\([^)]*[A-Za-z][^)]*\)")
    ok = [it for it in items if not BAD.search(it["text"])]

    def clean(t):
        return re.sub(r"<#[\d.]+#>", " ", t).strip()

    by_role = {}
    for r in ("H", "D", "C"):
        cand = [it for it in ok if it["role"] == r and 12 <= len(it["text"].split()) <= 38]
        step = max(1, len(cand) // N_MAIN)
        by_role[r] = cand[::step][:N_MAIN]

    rows = []
    for r in ("H", "D", "C"):
        for it in by_role[r]:
            f = AUDIO / fname(it["id"])
            if not f.exists():
                continue
            try:
                tr = asr(f)
                hyp = hyp_of(tr)
            except Exception as e:  # noqa: BLE001
                hyp = f"(LOI: {e})"
            rows.append({"role": r, "voice": it["voice"], "id": it["id"],
                         "ref": clean(it["text"]), "hyp": hyp, "cer": cer(clean(it["text"]), hyp)})
        print(f"xong vai {r}: {sum(1 for x in rows if x['role'] == r)} cau", flush=True)

    # ---- 2 giong doi chung: tai len 5 cau chung (lay tu vai H) ----
    ctrl_src = by_role["H"][:N_CTRL]
    ctrl_refs = [{"id": it["id"], "text": clean(it["text"])} for it in ctrl_src]
    CTRL = [("Vietnamese_kindhearted_girl", "Vo luc 0% (ky vong ~0%)"),
            ("English_CalmWoman", "Am lich 9,3% (ky vong cao)")]
    for vid, note in CTRL:
        reqs = []
        idmap = {}
        for i, c in enumerate(ctrl_refs):
            base = f"ctrl_{i:02d}_{vid}"
            idmap[base] = c["id"]
            reqs.append({"text": c["text"], "voice_id": vid, "emotion": "neutral", "speed": 0.9,
                         "pitch": 0, "volume": 1.0, "output_file": base})
        af = OUT / f"tts_ctrl_{vid}.json"
        af.write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")
        try:
            res = mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)], 900)
        except Exception as e:  # noqa: BLE001
            print(f"  !! TTS doi chung {vid} that bai: {e}", flush=True)
            continue
        for ok_i in res.get("success_items", []):
            fn = ok_i["file_name"]
            base = fn.rsplit(".", 1)[0]
            cid = idmap.get(base)
            if cid is None:
                cid = next((v for k, v in idmap.items() if fn.startswith(k)), None)
            try:
                url = mcode(["get_asset_url", ok_i["node_id"]], 180)["download_url"]
            except Exception as e:  # noqa: BLE001
                print(f"  !! get_asset_url that bai: {e}", flush=True)
                continue
            local = OUT / fn
            urllib.request.urlretrieve(url, local)
            ref = next((c["text"] for c in ctrl_refs if c["id"] == cid), "")
            try:
                tr = asr(local)
                hyp = hyp_of(tr)
            except Exception as e:  # noqa: BLE001
                hyp = f"(LOI: {e})"
            rows.append({"role": "CTRL", "voice": vid, "id": cid or fn, "ref": ref, "hyp": hyp,
                         "cer": cer(ref, hyp) if ref else 0.0, "note": note})
        print(f"xong doi chung {vid}", flush=True)

    (OUT / "rows.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- bao cao ----
    md = ["# CER tiếng Việt — 3 giọng bộ A (Tập 02) + 2 giọng đối chứng", "",
          "Nguồn: audio TTS đã xuất của Tập 02 (`.work/audio_s_t02/`), chuẩn = `text` trong manifest.",
          "Đo bằng `listen_audio` + `cer()` y hệt `voice_audition.py`. Ngưỡng dự án: **< 2%**.", ""]
    for grp, title in [("H", "Host — `English_CaptivatingStoryteller`"),
                       ("D", "Điều tra viên — `Korean_ColdYoungMan`"),
                       ("C", "Chuyên gia — `English_AssertiveQueen`"),
                       ("CTRL", "GIỌNG ĐỐI CHỨNG (kiểm chứng phép đo)")]:
        sub = [x for x in rows if x["role"] == grp]
        if not sub:
            continue
        cers = sorted(x["cer"] for x in sub)
        med = cers[len(cers) // 2]
        md.append(f"## {title}")
        md.append(f"- Số câu: **{len(sub)}** · CER trung vị: **{100*med:.1f}%** · "
                  f"thấp nhất {100*cers[0]:.1f}% · cao nhất {100*cers[-1]:.1f}% · "
                  f"trên ngưỡng 2%: **{sum(1 for c in cers if c > 0.02)}/{len(cers)}**")
        md.append("")
        md.append("| id | CER | Nghe lại được |")
        md.append("|---|---:|---|")
        for x in sorted(sub, key=lambda y: -y["cer"]):
            md.append(f"| `{x['id']}` | {100*x['cer']:.1f}% | {x['hyp'][:150]} |")
        md.append("")
    (OUT / "report.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
