"""Bản đồ mã câu CŨ -> MÃ CÂU MỚI cho Tập 04 (kịch bản sửa 31/10/2026).

Kịch bản Tập 04 sửa nội dung: 161 câu -> 154 câu. Các element con (2.06, 3.04,
4.06, 4.12...) bị đánh số lại. Bảng shot cũ trỏ mã cũ => phải dựng lại theo
NỘI DUNG, không theo số (QUY_TAC_AUDIO_HIGGS.md §0 luật 8; AGENTS.md H14).

Cách làm: so khớp câu bằng TEXT đã chuẩn hoá (bỏ dấu câu + số viết bằng chữ
-> số), không dùng chỉ số. Câu nào không khớp 1-1 sẽ được báo để sửa tay.

Chạy:  py -3 .work/_map_t04_codes.py
"""
import difflib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

OLD = WORK / "_cu" / "tap04_truoc_dung_lai_20261031" / "script_tap04.json"
NEW = WORK / "script_tap04.json"

VOWEL = "ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
NUMWORD = {
    "một": "1", "hai": "2", "ba": "3", "bốn": "4", "năm": "5", "sáu": "6", "bảy": "7",
    "tám": "8", "chín": "9", "mười": "10", "không": "0", "linh": "0",
}


def norm(t):
    """Chuẩn hoá để so: bỏ dấu câu, gộp khoảng trắng, đưa số viết bằng chữ về số."""
    t = t.lower()
    t = re.sub(r"[“”\"'’`]", "", t)
    t = re.sub(r"[^\w\sÀ-ỹ]", " ", t, flags=re.UNICODE)
    t = re.sub(r"\s+", " ", t).strip()
    words = []
    for w in t.split(" "):
        w2 = NUMWORD.get(w)
        words.append(w2 if w2 else w)
    return " ".join(words)


def sentences(path):
    sc = json.loads(path.read_text(encoding="utf-8-sig"))
    out = []
    for el in sc:
        if el.get("kind") != "LOI":
            continue
        for s in el.get("sentences", []):
            out.append((s["id"], s["text"], el.get("role"), el.get("act")))
    return out


def main():
    old = sentences(OLD)
    new = sentences(NEW)
    print(f"CU  : {len(old)} cau")
    print(f"MOI : {len(new)} cau")

    old_by_norm = {}
    for cid, txt, role, act in old:
        old_by_norm.setdefault(norm(txt), []).append(cid)

    mapping = {}       # old cid -> new cid
    unmatched = []     # old cid khong khop
    ambiguous = []     # nhieu cau moi cung noi dung
    for cid, txt, role, act in old:
        n = norm(txt)
        cands = old_by_norm.get(n)
        # khop 1-1 theo thu tu xuat hien
        hit = None
        for c in new:
            if c[0] in mapping.values():
                continue
            if norm(c[1]) == n:
                hit = c
                break
        if hit:
            mapping[cid] = hit[0]
        else:
            unmatched.append((cid, txt, role))

    print(f"\nKhop chinh xac: {len(mapping)}/{len(old)}")
    if unmatched:
        print(f"\n=== {len(unmatched)} cau CU khong khop 1-1 ===")
        for cid, txt, role in unmatched:
            n = norm(txt)
            best = difflib.get_close_matches(n, [norm(c[1]) for c in new], n=1, cutoff=0.55)
            cand = ""
            if best:
                i = [norm(c[1]) for c in new].index(best[0])
                cand = f"  -> {new[i][0]}: {new[i][1][:70]}"
            print(f"  {cid} ({role}): {txt[:88]}{cand}")

    # câu MỚI chưa được câu cũ nào chiếm
    used = set(mapping.values())
    orphan_new = [(c[0], c[1]) for c in new if c[0] not in used]
    print(f"\n=== {len(orphan_new)} cau MOI khong co ban CU ===")
    for cid, txt in orphan_new:
        print(f"  {cid}: {txt[:100]}")

    out = {"map": mapping,
           "unmatched_old": [{"id": c, "text": t, "role": r} for c, t, r in unmatched],
           "orphan_new": [{"id": c, "text": t} for c, t in orphan_new]}
    p = WORK / "_t04_code_map.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nDa ghi {p}")


if __name__ == "__main__":
    main()
