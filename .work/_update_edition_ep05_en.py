import sys
from pathlib import Path

p = Path(".work/edition.py")
text = p.read_text(encoding="utf-8")

old_block = """    "05": {
        "script": WORK / "script_tap05.json",
        "dir": "Tap05",
        "plan": "KeHoach_Video_Tap05.md",
        "master": "Tap05_master",
        "srt": "Tap05.srt",
        "n_element": {"1.09": "N1", "4.15": "N2"},
        "acting": WORK / "acting_tap05.json",
        "sfx_sheet": WORK / "sfx_tap05.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 4: "bgm_ambient_deep.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {"2-06": "t5_park_trashcan_drop", "2-10": "t5_church_council_altar"},
        "flag_hold_shots": (),
        "route_pins": {},                                      # T7 Tập 02: ghim không nhãn (không nêu địa điểm nhà nạn nhân)
        "thumb": ("CHIẾC ĐĨA MỀM", "MÀU TÍM"), "thumb_bg": "t5_purple_floppy_disk",
        "title": "Chiếc Đĩa Mềm Màu Tím — Sự phân mảnh tâm trí và cơn nghiện ái kỷ (vụ BTK Dennis Rader)",
        "act_titles": {1: "Hồi 1 · Bức thư tái xuất sau 13 năm lặng căm", 2: "Hồi 2 · Chữ ký tâm lý của con thú hai mặt",
                       3: "Hồi 3 · Bên trong bộ não ái kỷ ác tính", 4: "Hồi 4 · Đấu trí thẩm vấn và bẫy công nghệ đĩa mềm",
                       5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ và lời kết"},
        "summary": ("1.10#5", "3.02#1"),
        "need": [],
        "case": "Rader", "n1": ("NGƯỜI DÂN PARK CITY", "Hàng xóm ngoại ô", "NGƯỜI DÂN"),
        "n2": ("KERRI RAWSON", "Con gái ruột", "KERRI"),
        "cast": None,
    },"""

new_block = """    "05": {
        "script": WORK / ("script_tap05_EN.json" if EN else "script_tap05.json"),
        "dir": "Tap05_EN" if EN else "Tap05",
        "plan": "KeHoach_Video_Tap05_EN.md" if EN else "KeHoach_Video_Tap05.md",
        "master": "Tap05_EN_master" if EN else "Tap05_master",
        "srt": "Tap05_EN.srt" if EN else "Tap05.srt",
        "intro": "intro_kenh_EN_t05.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.09": "N1", "4.15": "N2"},
        "acting": WORK / ("acting_tap05_EN.json" if EN else "acting_tap05.json"),
        "sfx_sheet": WORK / "sfx_tap05.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 4: "bgm_ambient_deep.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {"2-06": "t5_park_trashcan_drop", "2-10": "t5_church_council_altar"},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("THE PURPLE", "FLOPPY DISK") if EN else ("CHIẾC ĐĨA MỀM", "MÀU TÍM"),
        "thumb_bg": "t5_purple_floppy_disk",
        "title": ("The Purple Floppy Disk: Narcissistic Addiction & Compartmentalization (The BTK Dennis Rader Case) | Amber eyes"
                  if EN else "Chiếc Đĩa Mềm Màu Tím — Sự phân mảnh tâm trí và cơn nghiện ái kỷ (vụ BTK Dennis Rader)"),
        "act_titles": ({1: "Act 1 · The Letter Resurfaces After 13 Years of Silence",
                        2: "Act 2 · The Crime Scene & Psychological Signature of a Two-Faced Predator",
                        3: "Act 3 · Inside the Mind of Malignant Narcissism",
                        4: "Act 4 · The Interrogation & The Digital Forensic Trap",
                        5: "Act 5 · The Verdict, Red Flags & Closing Thoughts"} if EN else
                       {1: "Hồi 1 · Bức thư tái xuất sau 13 năm lặng căm", 2: "Hồi 2 · Chữ ký tâm lý của con thú hai mặt",
                        3: "Hồi 3 · Bên trong bộ não ái kỷ ác tính", 4: "Hồi 4 · Đấu trí thẩm vấn và bẫy công nghệ đĩa mềm",
                        5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ và lời kết"}),
        "summary": ("1.10#5", "3.02#1"),
        "need": [],
        "case": "Rader",
        "n1": (("PARK CITY RESIDENT", "Suburban Neighbor", "RESIDENT") if EN else
               ("NGƯỜI DÂN PARK CITY", "Hàng xóm ngoại ô", "NGƯỜI DÂN")),
        "n2": (("KERRI RAWSON", "Daughter of Dennis Rader", "KERRI") if EN else
               ("KERRI RAWSON", "Con gái ruột", "KERRI")),
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("PARK CITY RESIDENT", "Suburban Neighbor"),
                     "N2": ("KERRI RAWSON", "Daughter of Dennis Rader")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "PARK CITY RESIDENT", "N2": "KERRI RAWSON"},
        "cards_en": (
            ("ABOUT THIS DOCUMENTARY", [
                [("Educational content:", 1),
                 (" A forensic & criminal psychology analysis based strictly on public records, "
                  "trial exhibits, and official police interrogation transcripts.", 0)],
                [("Investigative purpose:", 1),
                 (" Produced solely for educational, criminological, and public safety awareness.", 0)],
                [("No defamation:", 1),
                 (" Not intended to defame, harass, or inflict distress upon any innocent individuals "
                  "or victims’ families.", 0)]]),
            ("VIEWER DISCRETION & ADVISORY", [
                [("Mature audience only:", 1),
                 (" Contains mature themes, discussions of serial homicide, and non-graphic "
                  "accounts of violent crime. Viewer discretion is advised.", 0)],
                [("AI & Dramatization:", 1),
                 (" Narrated with synthetic AI voices. Visuals and character avatars are dramatized "
                  "illustrations and do not depict real persons.", 0)],
                [("Professional boundaries:", 1),
                 (" Not a substitute for professional legal, medical, or psychiatric advice.", 0)]])),
        "cast": None,
    },"""

norm_text = text.replace("\r\n", "\n")
norm_old = old_block.replace("\r\n", "\n")
norm_new = new_block.replace("\r\n", "\n")

if norm_old not in norm_text:
    print("ERROR: old_block not found in edition.py!")
    sys.exit(1)

norm_text = norm_text.replace(norm_old, norm_new, 1)
p.write_text(norm_text, encoding="utf-8")
print("SUCCESS: Updated edition.py Episode 05 with full English configuration!")
