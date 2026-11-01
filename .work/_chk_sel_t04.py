import json, pathlib
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
sel = json.loads((HERE / "higgs_selection_t04.json").read_text(encoding="utf-8-sig"))
print("source_manifest:", sel["source_manifest"])
print("n_sentences:", sel["n_sentences"], "| over_max_cer:", sel["n_over_max_cer"], "| max_cer:", sel["max_cer"])
s = sel["selection"]
from collections import Counter
print("variant histogram:", dict(Counter(v["variant"] for v in s.values())))
print("cer > 2%:", sum(1 for v in s.values() if v["cer"] is not None and v["cer"] > 0.02))
print("cer None:", sum(1 for v in s.values() if v["cer"] is None))
# 3 cau bi loai toan bo -> ban fallback duoc dung la gi
for sid in ("2.08#1", "3.02#2", "5.08#5"):
    v = s.get(sid)
    if v:
        print("  %s -> %s (variant %s, cer %s)" % (sid, v["src_file"], v["variant"], v["cer"]))
# mau: cau co round 2 (variant >= 2) de xac nhan dung ban vong 2
n2 = [(k, v["src_file"], v["cer"]) for k, v in s.items() if v["variant"] >= 2]
print("cau chon ban vong 2 (variant>=2):", len(n2))
for k, f, c in n2[:6]:
    print("   %-10s %-34s cer=%s" % (k, f, ("%.3f%%" % (100*c)) if c is not None else "NA"))
