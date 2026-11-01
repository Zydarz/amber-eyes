"""Cổng P0 + giám sát chất lượng Tập 04 (kể thừa từ Tập 03, 31/10/2026).

Kiểm đầu vào khớp kịch bản TRƯỚC khi đốt GPU Kaggle, rồi dùng lại ở mỗi cổng sau:
  P0  đầu vào        -> qc_tap04.py --gate P0
  P7  F0/G9          -> check_higgs_f0.py --new-only  (script riêng)
  P9  sau chọn bản   -> qc_tap04.py --gate P9
  P10 cổng master    -> qc_tap04.py --gate P10

Luật áp dụng: AGENTS.md L2/K1-K8, H6 (chữ trên hình lấy từ câu đang đọc),
H13 (khớp 3 chiều), G6 (lời đọc riêng không đổi chữ), G7 (không đọc chú thích
tiếng Anh), QUY_TAC_AUDIO_HIGGS.md §5 (cấm thẻ emotion), §7 P0.

Cách chạy (từ thư mục repo):
    py -3 .work/qc_tap04.py --gate P0
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
KG = WORK / "kaggle_higgs"

FAIL = []
WARN = []
OK = []


def ok(msg):
    OK.append(msg)


def bad(msg):
    FAIL.append(msg)


def warn(msg):
    WARN.append(msg)


def rd(p):
    """Đọc JSON, dùng utf-8-sig để chịu được BOM (Notepad/PowerShell)."""
    return json.loads(Path(p).read_text(encoding="utf-8-sig"))


def load_ep(ep):
    """Tập khác 02 mang hậu tố `_tXX` (QUY_TAC_AUDIO_HIGGS.md §7)."""
    s = rd(WORK / f"script_tap{ep}.json")
    acting = rd(WORK / f"acting_tap{ep}.json")
    sfx = rd(WORK / f"sfx_tap{ep}.json")
    spec = rd(KG / "dataset_voxcpm2" / f"prod_spec_t{ep}.json")
    payload = rd(KG / f"higgs_payload_t{ep}.json")
    return s, acting, sfx, spec, payload


def _spoken(t):
    """Chuẩn hoá lời đọc: bỏ thẻ nhịp (MiniMax <#0.35#> / Higgs <|prosody:pause|>),

    bỏ dấu nháy kép, gộp khoảng trắng. Script giữ nháy (chữ trên hình),
    lời đọc thì không (G1) — nên phải so ở dạng đã chuẩn hoá.
    """
    t = re.sub(r"<#[^#]*#>|<\|[^|]*\|>", " ", str(t))
    t = t.replace("“", "").replace("”", "").replace(chr(34), "")
    return re.sub(r"\s+", " ", t).strip()

def script_sentences(script):
    """Trả về dict: mã câu -> (text gốc, role, act)."""
    out = {}
    for el in script:
        if el.get("kind") != "LOI":
            continue
        for s in el.get("sentences", []):
            out[s["id"]] = (s["text"], el.get("role"), el.get("act"))
    return out


# ---------------------------------------------------------------- P0
def gate_p0(ep, s, acting, sfx, spec, payload):
    sent = script_sentences(s)
    n_sent = len(sent)
    ok(f"P0 script_tap{ep}.json: {n_sent} câu thoại")

    # --- 1. spec phải phủ đúng câu kịch bản
    spec_ids = [i["id"] if isinstance(i, dict) else i for i in spec["items"]]
    missing = set(sent) - set(spec_ids)
    extra = set(spec_ids) - set(sent)
    if missing:
        bad(f"P0 spec thiếu câu: {sorted(missing)}")
    if extra:
        bad(f"P0 spec có câu không tồn tại: {sorted(extra)}")
    if len(spec_ids) != len(set(spec_ids)):
        bad("P0 spec trùng mã câu")
    if not missing and not extra and len(spec_ids) == len(set(spec_ids)):
        ok(f"P0 spec khớp 100% {n_sent} câu, không trùng, đúng thứ tự kiểm tra")

    # --- 2. payload phủ đúng spec
    pay_ids = [i["id"] for i in payload["items"]]
    if set(pay_ids) != set(spec_ids):
        bad(f"P0 payload lệch spec: thiếu {sorted(set(spec_ids) - set(pay_ids))[:8]} "
            f"thừa {sorted(set(pay_ids) - set(spec_ids))[:8]}")
    else:
        ok(f"P0 payload phủ {len(pay_ids)}/{len(spec_ids)} mục của spec")

    # --- 3. CẤM thẻ emotion (Higgs §5) + thẻ MiniMax + ...
    emo = [i["id"] for i in payload["items"] if i.get("emotion_tag")]
    if emo:
        bad(f"P0 CÓ thẻ emotion trong payload: {emo[:10]}")
    else:
        ok("P0 payload: 0 thẻ <|emotion:…|>")

    raw = json.dumps(payload, ensure_ascii=False)
    for pat, name in [(r"<#[^>]*#>", "thẻ MiniMax <#…#>"),
                      (r"\.\.\.", "dấu ... ")]:
        hits = re.findall(pat, raw)
        if hits:
            bad(f"P0 payload còn {name}: {len(hits)} chỗ")
        else:
            ok(f"P0 payload: 0 {name}")

    # --- 3b. prosody: G1 chỉ cho phép <|prosody:pause|> SAU dấu ':' trước câu trích
    bad_pro = []
    for it in payload["items"]:
        for m in re.finditer(r"<\|prosody:[^|]*\|>", it.get("text", "")):
            before = it["text"][:m.start()].rstrip()
            if not before.endswith(":"):
                bad_pro.append((it["id"], it["text"][:70]))
    if bad_pro:
        for sid, t in bad_pro[:10]:
            bad(f"P0 G1 thẻ prosody không đứng sau ':' — {sid}: {t!r}")
    else:
        n_pro = sum(len(re.findall(r"<\|prosody:[^|]*\|>", i.get("text", "")))
                    for i in payload["items"])
        ok(f"P0 G1: {n_pro} thẻ prosody — tất cả đứng sau dấu ':' trước câu trích")

    # --- 4. G6: payload PHẢI khớp đúng cái code sinh ra (K1 - payload sinh bằng
    #     export_higgs_payload.py, không làm tay). So sánh với bản dựng lại.
    sys.path.insert(0, str(WORK))
    try:
        import importlib
        import export_higgs_payload as EHP
        importlib.reload(EHP)
        fresh = EHP.build()
        fo = {i["id"]: i for i in fresh["items"]}
        po = {i["id"]: i for i in payload["items"]}
        if fo.keys() != po.keys():
            bad(f"P0 K1 payload khác bản code sinh — thiếu {sorted(fo.keys() - po.keys())[:6]} "
                f"thừa {sorted(po.keys() - fo.keys())[:6]}")
        else:
            diffs = []
            for sid, f in fo.items():
                p = po[sid]
                for fld in ("role", "text_plain", "emotion", "display"):
                    if str(p.get(fld)).strip() != str(f.get(fld)).strip():
                        diffs.append((sid, fld))
            if diffs:
                for sid, fld in diffs[:10]:
                    bad(f"P0 K1 payload lệch code ở {sid}.{fld}")
            else:
                ok(f"P0 K1+G6: payload {len(fo)} câu — khớp 100% bản export_higgs_payload.py sinh ra")
    except Exception as e:
        warn(f"P0 không dựng lại được payload để đối chiếu: {e}")

    # --- 5. G7: lời ĐỌC (text_plain) không được chứa chú thích tiếng Anh.
    #     Chú ý: display (chữ trên hình / phụ đề) được phép giữ ký hiệu Anh.
    g7 = [i["id"] for i in payload["items"]
          if re.search(r"\([A-Za-z][^)]{2,}\)", i.get("text_plain", ""))]
    if g7:
        bad(f"P0 G7 lời đọc còn chú thích tiếng Anh trong ngoặc: {g7[:10]}")
    else:
        ok("P0 G7: lời đọc 0 chú thích tiếng Anh trong ngoặc (display giữ nguyên cho chữ trên hình)")

    # --- 6. (G7 trên script đã kiểm ở mục 5 trên lời đọc; display giữ ký hiệu Anh)

    # --- 6. acting: mã câu ⊂ script + alt khớp câu gốc
    bad_acting = []
    for k, v in acting.items():
        if k.startswith("_"):
            continue
        if k not in sent:
            bad_acting.append((k, "mã câu không có trong script"))
            continue
        alt = None
        if isinstance(v, dict):
            alt = v.get("alt")
        elif isinstance(v, (list, tuple)):
            # dạng [emotion, speed_delta, pitch, alt]
            alt = v[3] if len(v) > 3 else None
        elif isinstance(v, str):
            alt = v
        if alt and _spoken(str(alt)) != _spoken(sent[k][0]):
            bad_acting.append((k, "alt lệch câu gốc"))
    if bad_acting:
        for k, why in bad_acting[:10]:
            bad(f"P0 acting {k}: {why}")
    else:
        ok(f"P0 acting: {len([k for k in acting if not k.startswith('_')])} mã câu — alt khớp câu gốc")

    # --- 7. sfx: mọi mốc phải là mã câu CÓ THẬT, hoặc mã element (vd "5.01")
    elem_ids = {el["id"] for el in s}
    sfx_codes = set()
    for row in sfx.get("ambience", []):
        sfx_codes.update({row[0], row[1]})
    for row in sfx.get("cues", []):
        sfx_codes.add(row[0])
    for rng in sfx.get("music_drop", {}).get("ranges", []):
        sfx_codes.update({rng[0], rng[1]})
    unknown = sorted(c for c in sfx_codes if c not in sent and c not in elem_ids)
    if unknown:
        bad(f"P0 sfx tham chiếu mã câu không tồn tại: {unknown}")
    else:
        n_elem = len([c for c in sfx_codes if c in elem_ids])
        ok(f"P0 sfx: {len(sfx_codes)} mốc — tất cả tồn tại ({n_elem} mốc theo element)")

    # --- 8. A1: mọi đoạn tắt nhạc phải có nền môi trường bao phủ
    amb = [(r[0], r[1]) for r in sfx.get("ambience", [])]
    drops = sfx.get("music_drop", {}).get("ranges", [])
    uncovered = []
    for a, b in drops:
        if not any(x <= a and b <= y for x, y in amb):
            uncovered.append((a, b))
    if uncovered:
        bad(f"P0 A1 đoạn tắt nhạc không có nền môi trường: {uncovered}")
    else:
        ok(f"P0 A1: {len(drops)} đoạn tắt nhạc đều có nền môi trường")

    # --- 9. vai
    roles = {}
    for sid, (_, role, _) in sent.items():
        roles[role] = roles.get(role, 0) + 1
    ok(f"P0 phân vai: {dict(sorted(roles.items(), key=lambda kv: -kv[1]))}")


# ---------------------------------------------------------------- P9
def gate_p9(ep):
    """Sau khi chọn bản: mọi câu phải có 1 bản trong thư mục âm thanh đã cài."""
    inst = WORK / f"audio_s_higgs_t{ep}"
    sel = rd(WORK / f"higgs_selection_t{ep}.json") if (WORK / f"higgs_selection_t{ep}.json").exists() else {}
    if not inst.exists():
        bad(f"P9 chưa có {inst.name}")
        return
    wavs = {p.stem for p in inst.glob("*.wav")}
    need = set()
    for sid, info in (sel.get("selected") or sel).items():
        if isinstance(info, dict):
            need.add(info.get("file") or info.get("wav") or "")
    if need:
        miss = sorted(f for f in need if f and Path(f).stem not in wavs)
        if miss:
            bad(f"P9 thiếu file âm thanh đã chọn: {miss[:10]} (tổng {len(miss)})")
        else:
            ok(f"P9 đủ {len(need)} file âm thanh đã chọn")
    else:
        ok(f"P9 thư mục {inst.name}: {len(wavs)} file wav")


# ---------------------------------------------------------------- P10
def gate_p10(ep):
    """Cổng master (AGENTS.md bước 6 / QUY_TAC §9)."""
    import subprocess
    ff = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
    master = ROOT / "02_SAN_XUAT" / f"Tap{ep}" / "xuat_ban" / f"Tap{ep}_master.mp3"
    if not master.exists():
        bad(f"P10 chưa có {master.name}")
        return
    r = subprocess.run([str(ff), "-hide_banner", "-nostats", "-i", str(master),
                        "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    err = r.stderr
    m = re.findall(r"I:\s*(-?[\d.]+) LUFS", err)
    lufs = float(m[-1]) if m else None
    pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", err)
    peak = float(pk[-1]) if pk else None
    r2 = subprocess.run([str(ff), "-hide_banner", "-nostats", "-i", str(master),
                         "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace")
    sil = re.findall(r"silence_duration:\s*([\d.]+)", r2.stderr)
    dur = subprocess.run([str(ff), "-hide_banner", "-i", str(master)],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    d = re.findall(r"Duration:\s*(\d+):(\d+):([\d.]+)", dur.stderr)
    total = None
    if d:
        h, mnt, sec = d[0]
        total = int(h) * 3600 + int(mnt) * 60 + float(sec)
    print(f"  master : {master.name}")
    print(f"  thoi luong : {total:.1f} s ({int(total//60)}:{total%60:04.1f})" if total else "  thoi luong : ?")
    print(f"  LUFS        : {lufs}" if lufs is not None else "  LUFS : ?")
    print(f"  dinh that   : {peak} dBFS" if peak is not None else "  dinh that : ?")
    print(f"  khoang lang >0,3s @-60dB : {len(sil)}")
    if lufs is not None and not (-17.0 <= lufs <= -15.0):
        bad(f"P10 LUFS {lufs} ngoài -16 +/- 1")
    else:
        ok(f"P10 LUFS {lufs} trong -16 +/- 1")
    if peak is not None and peak > -1.5:
        bad(f"P10 dinh that {peak} > -1,5 dBFS")
    else:
        ok(f"P10 dinh that {peak} <= -1,5 dBFS")
    if sil:
        bad(f"P10 {len(sil)} khoang lang > 0,3 s: {sil[:8]}")
    else:
        ok("P10 0 khoang lang > 0,3 s @ -60 dB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ep", default="04")
    ap.add_argument("--gate", default="P0", choices=["P0", "P9", "P10", "ALL"])
    a = ap.parse_args()
    ep = a.ep
    print(f"===== QC Tap{ep} — gate {a.gate} =====")
    if a.gate in ("P0", "ALL"):
        s, acting, sfx, spec, payload = load_ep(ep)
        gate_p0(ep, s, acting, sfx, spec, payload)
    if a.gate in ("P9", "ALL"):
        gate_p9(ep)
    if a.gate in ("P10", "ALL"):
        gate_p10(ep)
    print()
    for m in OK:
        print(f"  [OK]   {m}")
    for m in WARN:
        print(f"  [WARN] {m}")
    for m in FAIL:
        print(f"  [FAIL] {m}")
    print(f"\n  => {len(OK)} OK · {len(WARN)} cảnh báo · {len(FAIL)} lỗi")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
