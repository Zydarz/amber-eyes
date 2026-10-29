#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dịch lại các câu JA bị rác model (tiếng Nhật lai tiếng Anh/Trung).

Cách làm: gọi LLM TỪNG CÂU (1 job = 1 câu) với đúng prompt/style của pipeline,
rồi kiểm tra lại bằng chính hàm check của pipeline + quét rác. Chỉ ghi vào
cache khi bản mới SẠCH và vẫn giữ đúng số câu.

    py -3 .work/_ja_repair_latin.py            # dry-run (không ghi)
    py -3 .work/_ja_repair_latin.py --do
    py -3 .work/_ja_repair_latin.py --do --only 27
"""
import json
import re
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
import ja_llm  # noqa: E402

APPLY = "--do" in sys.argv
ONLY = None
if "--only" in sys.argv:
    ONLY = sys.argv[sys.argv.index("--only") + 1].zfill(2)

# ------------------------------------------------------------------ phát hiện rác
CN_WORDS = ["氛围", "气氛", "同步", "特意", "素质", "内在", "外在", "心灵", "情绪",
            "媳妇", "里面", "层面", "结局", "精髓", "束缚", "尴尬", "煎熬", "龟裂",
            "挑逗", "绽放", "狂喜", "沮丧", "体贴", "笼罩", "弥漫", "洋溢", "流淌",
            "闪烁", "苏醒", "抽搐", "狰狞", "凝重", "飘逸", "诡异", "凄凉", "悲壮",
            "豪迈", "澎湃", "压抑", "沉闷", "悦耳", "清脆", "浑厚", "沙哑", "恍惚",
            "迟疑", "狠心", "狡猾", "贪婪", "慷慨", "冷漠"]
LAT_OK = {"dna", "tv", "sns", "fbi", "street", "avenue", "road", "court", "act",
          "foundation", "school", "hospital", "prison", "center", "centre",
          "university", "penitentiary", "county", "general", "state", "no",
          "reality", "night", "stalker", "mindhunter", "malin", "malingering",
          "mind", "hunter", "minimalist", "piano", "ambient", "dark", "the",
          "silence", "of", "lambs", "and", "the", "co", "ed", "killer", "bunny",
          "mun", "chausen", "munchausen"}
RX_LAT = re.compile(r"[A-Za-z\u00C0-\u024F]{2,}")
RX_HANGUL = re.compile(r"[\u3131-\u318e\uac00-\ud7a3]")


def is_cjk(c):
    return ("\u3000" <= c <= "\u30ff") or ("\u3400" <= c <= "\u9fff")


def artifacts(ja: str, vn_text: str):
    out = []
    vl = vn_text.lower()
    for m in RX_LAT.finditer(ja):
        w = m.group(0)
        if w.lower() in vl or w.lower() in LAT_OK:
            continue
        a = ja[m.start() - 1] if m.start() > 0 else ""
        b = ja[m.end()] if m.end() < len(ja) else ""
        if is_cjk(a) or is_cjk(b):
            out.append("LAT:" + w)
    for w in CN_WORDS:
        if w in ja:
            out.append("CNW:" + w)
    if RX_HANGUL.search(ja):
        out.append("HANGUL")
    for c in ja:
        if c in M.CN_ONLY_CHARS:
            out.append("CN:" + c)
            break
    return out


# ------------------------------------------------------------------ lấy nguồn VN
def jobs_for(ep):
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    out = []
    for u in units:
        if u["kind"] == "RAW":
            continue
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            if parts:
                for k, p in enumerate(parts):
                    out.append({"id": f"{u['id']}#{k}", "vi": p, "ctx": u["vi"],
                                "kind": "dialogue", "n": 1})
                continue
            out.append({"id": f"{u['id']}#L", "vi": u["vi"], "ctx": u["vi"],
                        "kind": "line", "n": u.get("n", 0)})
            continue
        if u["kind"] == "TABLE":
            out.append({"id": u["id"], "vi": u["vi"], "kind": "table",
                        "cells": u["vi"].split("\t"), "n": 0})
            continue
        out.append({"id": u["id"], "vi": u["vi"], "kind": "meta", "n": 0})
    return out, units


STRICT = """下のベトナム語台本の1文を、日本語に翻訳し直してください。

前回の訳には、英語・中国語・韓国語由来の誤った語句が混ざっています。
- 日本語の語彙だけで書き直してください。固有名詞・略号・製品名など、原語のまま残すものは除きます。
- 句点（。／？／！）は1文につき1個だけ。1文を2文に割らないでください。
- 音読したときの語orderingが自然になるようにしてください。

入力：{vi}

出力は次の JSON オブジェクトだけ（説明・コードフェンスなし）：
{{"ja": "日本語の1文"}}"""


def repair_one(ep, item, ep_tokens, old_ja):
    kind = item["kind"]
    errs, warns = {}, {}
    try:
        res = M.call_batch([item], kind, tries=3, ep_tokens=ep_tokens,
                            err_sink=errs, warn_sink=warns)
    except Exception as e:
        return None, f"llm error: {str(e)[:120]}"
    ja = res.get(item["id"])
    if ja and not artifacts(ja, item["vi"]):
        return ja, None
    # vòng 2: prompt siết
    for _ in range(2):
        try:
            prompt = STRICT.format(vi=item["vi"])
            txt = ja_llm.call(prompt, M.STYLE if kind in ("dialogue", "line") else M.STYLE_META,
                              model=M.MODEL, max_tokens=8000, temperature=0.1, timeout=300)
            data = M.parse_json_array(txt)
        except Exception as e:
            return None, f"strict error: {str(e)[:120]}"
        cand = None
        for row in data:
            if isinstance(row, dict) and isinstance(row.get("ja"), str):
                cand = M._clean_ja(row["ja"], item["vi"])
                break
        if not cand:
            continue
        cand = M.repair_ja(cand, item["vi"])
        if kind == "dialogue":
            ok, _r, _k = M.check_sentence(cand, item["vi"], ep_tokens, item.get("ctx", ""))
        elif kind == "line":
            ok, _r, _k = M.check_line(cand, item["vi"], item.get("n", 0), ep_tokens)
        else:
            ok, _r, _k = M.check_meta(cand, item["vi"], ep_tokens)
        if ok and not artifacts(cand, item["vi"]):
            return cand, None
    return None, "van con rac: " + ", ".join(artifacts(ja or old_ja, item["vi"]))


def main():
    targets = []          # (ep, item, old_ja)
    for i in range(1, 30):
        ep = "%02d" % i
        if ONLY and ep != ONLY:
            continue
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        if not cp.exists():
            continue
        d = json.loads(cp.read_text(encoding="utf-8"))
        jobs, _u = jobs_for(ep)
        vmap = {j["id"]: j for j in jobs}
        vn_text = M.canonical_vn(ep).read_text(encoding="utf-8")
        for k, v in d.items():
            if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
                continue
            ja = v.get("ja", "")
            if not isinstance(ja, str) or not ja:
                continue
            item = vmap.get(k)
            if item is None:
                continue
            art = artifacts(ja, vn_text)
            if art:
                targets.append((ep, item, ja, art))

    print(f"=== {len(targets)} muc can dich lai ===")
    for ep, item, ja, art in targets:
        print(f"  Tap{ep} {item['id']} [{item['kind']}] {art}")
        print(f"      VN: {item['vi'][:110]}")
        print(f"      JA: {ja[:110]}")

    if not APPLY:
        print("\nDRY-RUN. Them --do de dich lai.")
        return

    ok_map, fail = {}, []
    for ep in sorted({t[0] for t in targets}):
        ep_tokens = M.vn_tokens_of(M.canonical_vn(ep).read_text(encoding="utf-8"))
        sub = [t for t in targets if t[0] == ep]
        with ThreadPoolExecutor(max_workers=4) as ex:
            futs = {ex.submit(repair_one, ep, it, ep_tokens, old): (ep, it, old, art)
                    for _ep, it, old, art in sub}
            for f, meta in futs.items():
                ja, err = f.result()
                if ja:
                    ok_map.setdefault(ep, {})[meta[1]["id"]] = ja
                else:
                    fail.append((meta[0], meta[1]["id"], err))
    print("\n=== KET QUA ===")
    for ep, m in sorted(ok_map.items()):
        print(f"  Tap{ep}: sua {len(m)} muc")
    print(f"  That bai: {len(fail)}")
    for ep, uid, err in fail:
        print(f"    Tap{ep} {uid}: {err}")

    for ep, m in ok_map.items():
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        shutil.copy2(cp, cp.with_suffix(".json.bak_latin"))
        d = json.loads(cp.read_text(encoding="utf-8"))
        for uid, ja in m.items():
            d[uid] = {"ja": ja}
        cp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"   da ghi tap{ep}.json")


if __name__ == "__main__":
    main()
