import json, pathlib
live = json.loads(pathlib.Path(__file__).resolve().parents[1] / ".work" / "_voice_list_live_20261027.json".read_text(encoding="utf-8-sig"))
ids = {v["voice_id"]: v["voice_name"] for v in live["available_voices"]}
sets = {
 "Tap01 (VN ghim)": ["audiobook_male_1","male-qn-qingse","audiobook_female_1"],
 "Bo A (VN)": ["English_CaptivatingStoryteller","Korean_ColdYoungMan","English_AssertiveQueen","Vietnamese_kindhearted_girl","English_captivating_female1"],
 "Bo EN": ["English_magnetic_voiced_man","English_Trustworth_Man","English_Wiselady","English_SentimentalLady","English_captivating_female1"],
 "Bo JA": ["Japanese_GentleButler","Japanese_SeriousCommander","Japanese_DependableWoman","Japanese_KindLady","Japanese_DecisivePrincess"],
 "Bo KO": ["Korean_CalmGentleman","Korean_ColdYoungMan","Korean_DecisiveQueen","Korean_GentleWoman","Korean_SweetGirl"],
}
print(f"Tong giong live: {len(ids)}\n")
missing_total = 0
for name, lst in sets.items():
    print(f"--- {name} ---")
    for v in lst:
        if v in ids:
            print(f"  OK    {v}  ({ids[v]})")
        else:
            print(f"  MISS  {v}  <-- KHONG co trong danh sach live")
            missing_total += 1
    print()
print("Tong voice_id khong tim thay:", missing_total)
# dem theo ngon ngu trong kho
from collections import Counter
pref = Counter(v.split("_")[0] for v in ids)
print("Phan bo theo tien to:", dict(sorted(pref.items(), key=lambda x:-x[1])))

