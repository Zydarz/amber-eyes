# -*- coding: utf-8 -*-
import sys
sys.path.append(".work")
import act_en

header_en = """# CRIMINAL PSYCHOLOGY AUDIO / PODCAST SCRIPT
**Theme:** The 10 Psychological Indicators & The Halo Effect, Exploitation of Compassion, Omnipotent Grandiosity & Transactional Remorse – The Ted Bundy Case and The Trap of the Fake Arm Cast.
**Edition:** Standard A2c/K10 — Criminal Psychological Ecology & Safety Rule V9 (November 19, 2026).

---

## PRODUCTION BRIEF & NARRATIVE STRUCTURE

| Category | Standard Setup for Audio Episode (Host-Driven Documentary) |
| :--- | :--- |
| **Episode Title** | Episode 32: Ted Bundy — The Trap of Compassion & The Illusion of Absolute Control |
| **Format** | Investigative Documentary Podcast (Narrator-led Documentary) – The **Host** maintains the narrative backbone, connecting historical data, regulating emotional pacing, and bringing in specialized perspectives (Investigator, Psychologist, Ordinary Person) at precise dramatic beats according to the 10 Psychological Indicators. |
| **Estimated Total Duration** | 28 – 32 minutes (5 narrative acts + dramatic audio transitions) |
| **Suggested Background Music (BGM)** | Suffocating Dark Ambient, Somber Solo Cello, Minimalist Piano blended with chilling Electronic Drone, Harrowing Courtroom Violin, and Warm Piano for solemn reflection. Volume: -26dB under narration, rising to -14dB at scene transitions. |
| **Voice Allocation Mechanism** | - **Host (~48% duration):** Warm, deep, reflective male voice, guiding the narrative with a humanistic lens, social aftermath, halo effect, and survival lessons.<br>- **Investigator (~24%):** Sharp, cold, authoritative male voice representing casework files, physical evidence, Signature vs MO, and legal strategy of law enforcement.<br>- **Psychologist (~22%):** Calm, deeply academic female voice deconstructing malignant narcissism, predatory cognitive empathy, cognitive compartmentalization, and transactional regret.<br>- **Ordinary Person (~6%):** N1 (Carol DaRonch - Act 1, 6 sentences) bewildered yet resilient youthful female voice; N2 (Carole Ann Boone - Act 4, 8 sentences) trembling, guilt-ridden mature female voice. |
| **Quotation Rule** | All verbatim quotes on screen must match archival sources 100%. Formatting convention: ‘…’ = verbatim quote. |
| **Key Reference Sources** | Federal Bureau of Investigation FBI Case Files (Ted Bundy Case, Special Agent Bill Hagmaier) · Florida Supreme Court Records (Chi Omega & Kimberly Leach Cases, Judge Edward Cowart) · Trial Transcripts of Surviving Victim Carol DaRonch at Utah District Court · *The Stranger Beside Me* (Ann Rule, 1980) · *The Phantom Prince: My Life with Ted Bundy* (Elizabeth Kloepfer / Kendall, 1981) · Psychopathy Checklist-Revised PCL-R Research (Dr. Robert Hare) · *The Gift of Fear* Principles (Gavin de Becker, 1997). |

---

---
"""

full_en = "\n\n".join([header_en, act_en.ACT1_EN, act_en.ACT2_EN, act_en.ACT3_EN, act_en.ACT4_EN, act_en.ACT5_EN])
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32_EN/kichban_tap32_EN.md", "w", encoding="utf-8") as f:
    f.write(full_en)

import subprocess, json
subprocess.run(["py", "-3", ".work/parse_kichban.py", "01_KICH_BAN/Ho_So_Toi_Pham/Tap32_EN/kichban_tap32_EN.md", ".work/t32_en.json"])
d = json.load(open(".work/t32_en.json", encoding="utf-8"))
total_sents = sum(len(x.get("sentences", [])) for x in d)
print("Generated EN sentences count:", total_sents)
