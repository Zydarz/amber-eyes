import json, sys
sys.stdout.reconfigure(encoding='utf-8')

script = json.load(open(".work/script_tap05.json", encoding="utf-8"))
for el in script:
    if el.get("kind") == "LOI":
        act = el["act"]
        role = el["role"]
        for s in el["sentences"]:
            sid = s["id"]
            txt = s["text"]
            # Print important sentences
            if any(w in txt.lower() for w in ["b-t-k", "vicki", "nín thở", "nghịch lý", "lòng tự tôn", "ngăn kéo", "nhân tố x", "lãng quên", "home depot", "đĩa mềm", "thẩm vấn", "mặt nạ", "chung thân"]):
                print(f"{sid} ({role}): {txt[:80]}...")
