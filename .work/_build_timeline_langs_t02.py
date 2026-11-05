# -*- coding: utf-8 -*-
"""Dựng lại timeline cho Tập 02 của các bản dịch (EN / JA / KO) theo kịch bản viết lại 05/11.

Cách làm
--------
* EN / JA: có timeline đo thật từ audio master cũ -> GIỮ NGUYÊN mốc element (nhịp phim, khoảng
  lặng, vị trí SFX), chỉ CHIA LẠI thời lượng từng câu theo độ dài câu MỚI.
  (Âm thanh cũ ứng với kịch bản cũ; kịch bản mới đổi nội dung 134/203 câu nên mốc câu phải dựng lại.)
* KO: chưa có audio master -> dùng timeline VN (đo thật) làm khung nhịp, nhân với hệ số
  độ dài văn bản KO/VN, rồi nhân toàn cục theo tỉ lệ tốc độ đọc ước tính (tiếng Hàn ~ tiếng Nhật).

Mọi timeline sinh ra đều là TẠM THỜI: khi có audio master mới phải dựng lại bằng
`_align_timeline_*.py` (Whisper) như bản VN.

python .work/_build_timeline_langs_t02.py [--apply]
"""
import json, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r'D:/TEST/Gax/amber-eyes')
W = ROOT / ".work"


def load_script(lang):
    p = W / f"script_tap02_{lang}.json"
    els = json.loads(p.read_text(encoding="utf-8"))
    S, ELEM = {}, {}
    for e in els:
        if e.get("kind") == "LOI":
            for s in e["sentences"]:
                S[s["id"]] = s["text"]
                ELEM.setdefault(s["id"].split("#")[0], []).append(s["id"])
    return S, ELEM


def measure(text, lang):
    if lang == "EN":
        return max(1, len(text.split()))
    # JA / KO: số ký tự (bỏ khoảng trắng)
    return max(1, len(re.sub(r"\s+", "", text)))


def rebuild(base, S, ELEM, lang, global_scale=1.0):
    """Trả về timeline mới: giữ mốc element của `base`, chia lại câu theo độ dài câu mới.

    Câu nào chưa có trong `base` (15 câu mới của bản dịch) vẫn được đặt vào đúng element,
    chen theo thứ tự đọc, dùng thời lượng của timeline VN làm neo tương đối.
    """
    bitems = {it["id"]: it for it in base["items"]}
    out_items, cursor = [], None
    prev_base_end = None

    # nhóm câu theo element, chỉ giữ những element có trong base
    belems = {}
    for it in base["items"]:
        belems.setdefault(it.get("element") or it["id"].split("#")[0], []).append(it["id"])
    elems = [e for e in ELEM if e in belems]
    intro_end = base.get("intro", 22.41)
    missing = 0

    for el in elems:
        ids = list(ELEM[el])                       # thứ tự đọc trong kịch bản mới
        ids = [i for i in ids if i in S]
        if not ids:
            continue
        inb = [i for i in ids if i in bitems]
        if inb:
            inb.sort(key=lambda i: bitems[i]["start"])
            b0, b1 = bitems[inb[0]]["start"], bitems[inb[-1]]["end"]
        else:
            b0 = b1 = None

        # thời lượng gốc + khoảng lặng gốc của từng câu
        base_dur, base_gap = {}, {}
        for k, i in enumerate(ids):
            if i in bitems:
                base_dur[i] = bitems[i]["end"] - bitems[i]["start"]
                if k > 0 and ids[k - 1] in bitems:
                    base_gap[i] = max(0.0, bitems[i]["start"] - bitems[ids[k - 1]]["end"])
                else:
                    base_gap[i] = 0.0
            else:
                base_dur[i] = 0.0
                base_gap[i] = 0.0
                missing += 1

        bw = sum(measure(bitems[i]["text"], lang) for i in inb) or sum(
            measure(S.get(i, ""), lang) for i in ids)
        nw = sum(measure(S.get(i, ""), lang) for i in ids)
        ratio = (nw / bw) if bw else 1.0

        if b0 is None:
            b0 = b1 = intro_end
        span = b1 - b0
        new_total = span * ratio
        gap_total = sum(base_gap.values()) * ratio
        speech_total = max(0.0, new_total - gap_total)

        # vị trí bắt đầu của element: giữ khoảng lặng giữa các element như bản gốc
        if prev_base_end is None:
            start_el = intro_end + (b0 - intro_end) * global_scale
        else:
            start_el = cursor + (b0 - prev_base_end) * global_scale

        # chia speech_total cho các câu theo trọng số độ dài câu mới
        wts = [measure(S.get(i, ""), lang) for i in ids]
        sw = sum(wts) or 1
        t = start_el
        for k, i in enumerate(ids):
            d = speech_total * wts[k] / sw
            out_items.append({"id": i, "element": el, "act": bitems.get(i, {}).get("act", 1),
                              "role": bitems.get(i, {}).get("role", "H"),
                              "start": round(t, 3), "end": round(t + d, 3),
                              "text": S.get(i, "")})
            t += d
            t += gap_total * (base_gap[i] / (sum(base_gap.values()) or 1))
        cursor = t
        prev_base_end = b1

    if missing:
        print(f"  ({missing} câu mới — chưa có trong timeline gốc, đặt theo thứ tự đọc)")

    # markers
    markers = []
    for m in base.get("markers", []):
        mm = dict(m)
        for k in ("start", "end", "at"):
            if isinstance(mm.get(k), (int, float)):
                mm[k] = round(mm[k] * global_scale, 3)
        markers.append(mm)

    total = max([it["end"] for it in out_items] + [m.get("end", 0) for m in markers if isinstance(m.get("end"), (int, float))])
    acts = {}
    for k, v in base.get("acts", {}).items():
        acts[k] = [round(v[0] * global_scale, 3), round(v[1] * global_scale, 3)]
    return {"total": round(total, 2), "intro": round(base.get("intro", 22.41) * global_scale, 2),
            "items": out_items, "markers": markers, "acts": acts}


def rate_per_char(tl, lang, S):
    """giây lời / ký tự (phần lời) — dùng để suy ra tỉ lệ toàn cục cho KO"""
    speech = tl["total"] - tl.get("intro", 22.41)
    chars = sum(measure(S.get(it["id"], it["text"]), lang) for it in tl["items"])
    return speech / chars, chars, speech


def main():
    apply = "--apply" in sys.argv
    langs = [("EN", "timeline_s_EN_t02.json"), ("JA", "timeline_s_JA_t02.json"), ("KO", None)]

    # tỉ lệ toàn cục cho KO: dùng tốc độ đọc của tiếng Nhật (cùng hệ âm tiết CJK)
    ja_tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8"))
    S_JA, _ = load_script("JA")
    r_ja, c_ja, s_ja = rate_per_char(ja_tl, "JA", S_JA)
    vn_tl = json.loads((W / "timeline_s_t02.json").read_text(encoding="utf-8"))
    S_VN, _ = load_script("VN")
    r_vn, c_vn, s_vn = rate_per_char(vn_tl, "VN", S_VN)
    S_KO, ELEM_KO = load_script("KO")
    c_ko = sum(measure(S_KO.get(i, ""), "KO") for i in S_KO)
    pred_ko_speech = c_ko * r_ja
    print(f"toc do doc: JA {r_ja:.4f} s/ky tu ({c_ja} ky tu) · VN {r_vn:.4f} s/ky tu ({c_vn}) · "
          f"KO {c_ko} ky tu -> du doan {pred_ko_speech:.1f}s lời")

    for lang, base_name in langs:
        if base_name is None:
            base = vn_tl
            S, ELEM = S_KO, ELEM_KO
            gs = 1.0
        else:
            base = json.loads((W / base_name).read_text(encoding="utf-8"))
            S, ELEM = load_script(lang)
            gs = 1.0
        tl = rebuild(base, S, ELEM, lang, global_scale=gs)

        if lang == "KO":
            # nhân toàn cục theo tỉ lệ du đoán
            cur_speech = tl["total"] - tl["intro"]
            f = pred_ko_speech / (cur_speech or 1)
            tl = {"total": round(tl["total"] * f, 2), "intro": round(tl["intro"], 2),
                  "items": [dict(it, start=round(it["start"] * f, 3), end=round(it["end"] * f, 3)) for it in tl["items"]],
                  "markers": [dict(m, **{k: (round(m[k] * f, 3) if isinstance(m.get(k), (int, float)) else m.get(k))
                                        for k in ("start", "end", "at")}) for m in tl["markers"]],
                  "acts": {k: [round(v[0] * f, 3), round(v[1] * f, 3)] for k, v in tl["acts"].items()}}
            print(f"KO: nhan toan cuc x{f:.4f} -> total {tl['total']}s")

        out = W / f"timeline_s_{lang}_t02.json"
        bak = W / "_cu" / f"timeline_s_{lang}_t02_pre_20261105.json"
        if apply and out.exists():
            bak.parent.mkdir(parents=True, exist_ok=True)
            bak.write_bytes(out.read_bytes())
        print(f"{lang}: items={len(tl['items'])} total={tl['total']}s intro={tl['intro']} "
              f"first={tl['items'][0]['id']}@{tl['items'][0]['start']} last={tl['items'][-1]['id']}@{tl['items'][-1]['end']}")
        # kiểm tra trùng/chồng
        bad = [(a["id"], b["id"]) for a, b in zip(tl["items"], tl["items"][1:]) if b["start"] < a["end"] - 0.001]
        if bad:
            print(f"  !! CHONG LAP: {bad[:5]}")
        if apply:
            out.write_text(json.dumps(tl, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"  -> ghi {out}")
    if not apply:
        print("\n(dry-run) them --apply de ghi file")


if __name__ == "__main__":
    main()
