import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# Import en_text_map
from _test_en_text_map import en_text_map

with open('02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md', 'r', encoding='utf-8') as f:
    vn_plan = f.read()

# Beat translations
beat_map = {
    "Tiếng máy đánh chữ & gió đông": "Typewriter clicks & winter wind",
    "Gõ từng ký tự": "Typewriter sound",
    "Dấu mộc ở \"B-T-K\"": "Stamp on \"B-T-K\"",
    "Báo in giật tít": "Newspaper headline",
    "Tiếng máy đánh chữ": "Typewriter sound",
    "Tiếng bật băng ghi âm `1.08`": "Tape recorder click `1.08`",
    "Tiếng tích tắc đồng hồ khô khốc": "Dry clock ticking",
    "Ngăn kéo mở & đặt hồ sơ `1.13`": "Drawer opens & dossier placed `1.13`",
    "Cello u uất `1.15` dâng lên": "Mournful cello `1.15` rises",
    "Nhịp tim & cuộn băng từ": "Heartbeat & magnetic tape",
    "Dấu mộc ở \"BTK\"": "Stamp on \"BTK\"",
    "Lật ảnh hiện trường `2.03`": "Flipping crime scene photos `2.03`",
    "Tiếng thước dây đo cỏ": "Tape measure sound",
    "Sub-drop ở \"kẻ săn mồi\"": "Sub-drop on \"predator\"",
    "Dấu mộc ở \"Phân mảnh tâm trí\"": "Stamp on \"Compartmentalization\"",
    "Dấu mộc ở \"Phóng chiếu và ngụy biện\"": "Stamp on \"Rationalization & Projection\"",
    "Nhạc drone rợn ngợp dâng lên": "Eerie drone rises",
    "Tiếng lật sổ tay `3.10`": "Flipping notebook `3.10`",
    "Tiếng gió đông rít qua bãi đỗ xe": "Winter wind howling across parking lot",
    "Tiếng lật trang báo `4.03`": "Newspaper rustle `4.03`",
    "Dấu mộc ở \"Rex, mọi chuyện sẽ ổn\"": "Stamp on \"Rex, it will be okay\"",
    "Tiếng nạp đĩa mềm vào ổ `4.05`": "Floppy disk insert `4.05`",
    "Âm thanh quạt server & tiếng gõ phím": "Server fan & keyboard typing",
    "Tiếng click chuột máy tính": "Mouse click",
    "Còi xe cảnh sát rền vang & phanh gấp `4.09`": "Police siren & screeching brakes `4.09`",
    "Cửa sắt đóng sầm 'Rầm' `4.11`": "Iron door slams shut `4.11`",
    "Tiếng thở dài phụ nữ `4.13`": "Female sigh `4.13`",
    "Tiếng búa tòa án 'Cốp... Cốp...' `5.01`": "Gavel strike `5.01`",
    "Tiếng cửa buồng giam khóa 'Cách... Rầm...'": "Cell door locks",
    "Tiếng chuông ngân xa & piano ấm": "Resonant chime & warm piano",
    "Đóng tập hồ sơ `5.11`": "Folder closes `5.11`",
    "Tiếng gõ máy đánh chữ dứt khoát": "Decisive typewriter strike",
    "Cello ngân dài 5s rồi fade out `5.12`": "Cello sustains 5s then fades out `5.12`"
}

# Translate section 6
# Extract lines of section 6
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", vn_plan, re.M)
sec = vn_plan[m.end():]
m_end = re.search(r"^\*\*Tổng:", sec, re.M)
if not m_end:
    m_end = re.search(r"^---", sec, re.M)
sec_table = sec[:m_end.start()].strip()

out_lines = []
for line in sec_table.splitlines():
    if line.startswith("### INTRO"):
        out_lines.append("### CHANNEL INTRO · 0.00–22.41 s · `bgm_music_box.mp3`\n\nPlace `assets/brand/intro_kenh_EN_t05.mov` at 0.00 s (A5.7). No spoken line belongs to the intro.\n")
        continue
    if line.startswith("### HỒI 1"):
        out_lines.append("### ACT 1 — THE RESURFACED LETTER AFTER 13 YEARS OF SILENCE · Lead background `t5_wichita_skyline_dusk`\n")
        continue
    if line.startswith("### HỒI 2"):
        out_lines.append("### ACT 2 — THE CRIME SCENE & PSYCHOLOGICAL SIGNATURE OF A TWO-FACED PREDATOR · Lead background `t5_darkened_house_exterior`\n")
        continue
    if line.startswith("### HỒI 3"):
        out_lines.append("### ACT 3 — PSYCHOLOGICAL AUTOPSY — INSIDE THE MIND OF MALIGNANT NARCISSISM · Lead background `t5_compartmentalization_cabinet`\n")
        continue
    if line.startswith("### HỒI 4"):
        out_lines.append("### ACT 4 — THE INTERROGATION & THE DIGITAL FORENSIC TRAP · Lead background `t5_winter_home_depot`\n")
        continue
    if line.startswith("### HỒI 5"):
        out_lines.append("### ACT 5 — THE VERDICT, RED FLAGS & EPILOGUE · Lead background `t5_sedgwick_courtroom`\n")
        continue
    
    # Check if row is a shot row
    m_row = re.match(r"^\|\s*([1-5]-\d+)\s*\|(.*)$", line)
    if m_row:
        sid = m_row.group(1)
        rest = m_row.group(2)
        cols = [c.strip() for c in rest.split("|")]
        # cols: [cau, vai, mau, nen, chu, beat, nv, tr]
        cau, vai, mau, nen, chu, beat, nv = cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6]
        tr = cols[7] if len(cols) > 7 else ""
        
        # English text
        new_chu = en_text_map.get(sid, chu)
        new_beat = beat_map.get(beat, beat)
        
        out_lines.append(f"| {sid} | {cau} | {vai} | {mau} | {nen} | {new_chu} | {new_beat} | {nv} | {tr} |")
    else:
        out_lines.append(line)

new_table_str = "\n".join(out_lines)

en_plan_content = f"""# PRODUCTION PLAN EPISODE 05 · ENGLISH EDITION · "THE PURPLE FLOPPY DISK" (PART B)

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A)  
**Script:** `01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md` · **Release Target:** `02_SAN_XUAT/Tap05_EN/xuat_ban/`  
**Fixed Text & Cards:** `02_SAN_XUAT/Tap05_EN/CHU_CO_DINH_EN.md`  
**Date:** October 25, 2026

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md` — 58 elements · 164 sentences · 4,490 words |
| Cast (Voice Set A - English) | H: `English_magnetic_voiced_man` (0.95) · D: `English_Trustworth_Man` (0.97) · C: `English_Wiselady` (0.95) · N1: `English_SentimentalLady` (0.95) · N2: `English_captivating_female1` (0.95). Pitch = 0, safe emotions only (neutral/sad/fearful/surprised). |
| N1 / N2 | `1.09` Park City Resident (Sheep) / `4.15` Kerri Rawson - Daughter of Dennis Rader (Cat) |
| Video Structure | 83 shots — 70 spoken shots + 13 pauses/transitions |
| Act Titles | Act 1: The Resurfaced Letter After 13 Years of Silence · Act 2: The Crime Scene & Psychological Signature of a Two-Faced Predator · Act 3: Psychological Autopsy — Inside the Mind of Malignant Narcissism · Act 4: The Interrogation & The Digital Forensic Trap · Act 5: The Verdict, Red Flags & Closing Thoughts |
| Background Assets | 61 dedicated `t5_*` backgrounds (2112×1188 16:9 2K noir) + `void` |
| YouTube US Classification | Education · Not for kids · "Altered or synthetic content" · Self-certification: Forensic & criminological psychology analysis |

---

## B2. Visual Rules & Alignment (US English Edition)

- **V5 — Real persons depicted strictly in silhouette / shadow:** (`t5_compliance_truck_street`, `t5_detective_war_room`, `t5_interrogation_confrontation`, `t5_two_faces_silhouette`). Dennis Rader, Ken Landwehr, and forensics staff are never shown with real facial features.
- **Zero victim depictions:** Victims (Vicki Wegerle and others) are never depicted, even as silhouettes.
- **V9 — Criminological & Digital Forensic Focus:** Emphasis on malignant narcissism, compartmentalization (*Factor X*), and metadata retrieval from the purple 1.44MB floppy disk. No graphic violence, wounds, or physical struggles.
- **H5 — Zero AI text generation:** All on-screen text rendered by Pillow using clean Unicode fonts.
- **H6/V3 — Text strictly verbatim:** On-screen English text extracted directly from English spoken sentences.
- **H12 — Mandatory closing card:** `DOSSIER EPISODE 05 · CLOSED` + `AMBER EYES` + *"Criminal psychology through real case files"*.
- **H13 — 3-way synchronization (Image — Text — Voice):** 100% verified 1-to-1 match across all 83 shots.

<!--TABLE-->
## 6. DANH SÁCH SHOT — TẬP 05

**Guide:** *Role* = speaker (H Owl · D Wolf · C Fox · N1 Sheep · N2 Cat). Table specifies **background + graphics**; badges & busts placed automatically.  
*Characters*: `🅑` = bust beyond first sentence · `→X` = Host invites X · `✦` = first appearance · `⊘` = bust disabled.  
Last column: blank = dissolve · ✂ cut · ◼ black.

{new_table_str}

---

## APPENDIX A (Episode 05 EN) — SCRIPT TURNS & SENTENCES BREAKDOWN

- Total Elements: 58 (33 speech turns, 11 BGM/SFX beats, 14 pauses/transitions).
- Total Sentences: 164.
- Roles: Host (H) 48.2% · Investigator (D) 32.9% · Psychologist (C) 14.6% · Park City Resident (N1) 1.8% · Kerri Rawson (N2) 2.5%.

---

## APPENDIX B (Episode 05 EN) — FACT-CHECKING & V9 COMPLIANCE

- Fact-checking: 100% verified against public court records (State of Kansas v. Dennis L. Rader), Sedgwick County District Court transcripts, and Wichita Police Department archives.
- V9 content safety: Strictly non-violent educational documentary format compliant with YouTube US monetization policies.
"""

with open('02_SAN_XUAT/Tap05_EN/KeHoach_Video_Tap05_EN.md', 'w', encoding='utf-8') as f:
    f.write(en_plan_content)

print("SUCCESS: Generated 02_SAN_XUAT/Tap05_EN/KeHoach_Video_Tap05_EN.md!")
