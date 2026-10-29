import sys, os, re, json

sys.stdout.reconfigure(encoding="utf-8")

# Load script sentences
with open(".work/script_tap07.json", "r", encoding="utf-8") as f:
    script_data = json.load(f)

all_sent_ids = []
for el in script_data:
    if el.get("kind") == "LOI":
        for s in el.get("sentences", []):
            all_sent_ids.append(s["id"])

print(f"Total script sentences: {len(all_sent_ids)} (from {all_sent_ids[0]} to {all_sent_ids[-1]})")

# Load mapping from Danh_Sach_Anh_Tap07.md
with open("02_SAN_XUAT/Tap07/Danh_Sach_Anh_Tap07.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

mapped_ranges = []
for line in lines:
    if line.strip().startswith("|") and "`t7_" in line:
        parts = [p.strip() for p in line.split("|")]
        # cols: empty, stt, filename, content, cue_range, empty
        if len(parts) >= 5:
            cue_part = parts[4].replace("`", "").strip()
            bg_name = parts[2].replace("`", "").strip()
            mapped_ranges.append((bg_name, cue_part))

print(f"Total mapped entries in MD: {len(mapped_ranges)}")

# Parse each cue_part into list of sentence ids
def expand_cue(cue_str):
    res = []
    # e.g. 1.02#1–#3 or 1.04#3 or 4.03#5–#8 or 5.04#16–#17
    # could have multiple like "1.06#1–#2"
    chunks = [c.strip() for c in cue_str.split(",")]
    for chunk in chunks:
        m = re.match(r"^(\d+\.\d+)#(\d+)[–-]#(\d+)$", chunk)
        if m:
            el_id = m.group(1)
            start_idx = int(m.group(2))
            end_idx = int(m.group(3))
            for i in range(start_idx, end_idx + 1):
                res.append(f"{el_id}#{i}")
            continue
        m2 = re.match(r"^(\d+\.\d+)#(\d+)$", chunk)
        if m2:
            res.append(f"{m2.group(1)}#{m2.group(2)}")
            continue
        # single element id without #?
        m3 = re.match(r"^(\d+\.\d+)$", chunk)
        if m3:
            res.append(m3.group(1))
            continue
        print(f"Unrecognized cue format: '{chunk}'")
    return res

mapped_sents = {}
for bg_name, cue_str in mapped_ranges:
    sents = expand_cue(cue_str)
    for s in sents:
        if s in mapped_sents:
            print(f"WARNING: Sentence {s} mapped multiple times! (first: {mapped_sents[s]}, now: {bg_name})")
        mapped_sents[s] = bg_name

missing_in_mapping = [s for s in all_sent_ids if s not in mapped_sents]
extra_in_mapping = [s for s in mapped_sents if s not in all_sent_ids]

print(f"Covered sentences: {len(mapped_sents)} / {len(all_sent_ids)}")
if missing_in_mapping:
    print(f"Missing sentences in mapping ({len(missing_in_mapping)}):", missing_in_mapping)
if extra_in_mapping:
    print(f"Extra sentences in mapping ({len(extra_in_mapping)}):", extra_in_mapping)
