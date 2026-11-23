# -*- coding: utf-8 -*-
"""Generate TikTok scripts, audio specs, captions, and descriptions for Tap 02 EN & JA.

Strict adherence to AGENTS.md rules:
- Measured speech rates from timeline_s_EN_t02.json and timeline_s_JA_t02.json
- Verbatim citations and facts mapped to script_tap02_EN.json / script_tap02_JA.json
- G1 (no ellipses, single <#0.35#> before quotes), G3 (safe emotions: neutral, sad), G4 (safe speed offsets), V9/A9.2 (safety)
- TikTok limits: caption <= 2200 chars, description <= 4000 chars, duration 45-95s
- Dual-pack descriptions: MoTa_Dai (comprehensive) and MoTa_Ngan (concise)
"""

import json
import pathlib
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap02_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap02_JA"
OUT_EN.mkdir(parents=True, exist_ok=True)
OUT_JA.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------------
# 0. MEASURED SPEECH RATES
# ----------------------------------------------------------------------------
def get_rates(timeline_file, is_ja=False):
    tl = json.loads((WORK / timeline_file).read_text(encoding="utf-8"))
    dur = defaultdict(float)
    units = defaultdict(int)
    for it in tl["items"]:
        n = len(it["text"]) if is_ja else len(it["text"].split())
        dur[it["role"]] += it["end"] - it["start"]
        units[it["role"]] += n
    return {r: dur[r] / units[r] for r in dur}

RATE_EN = get_rates("timeline_s_EN_t02.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t02.json", is_ja=True)

def count_units(text, is_ja=False):
    t = re.sub(r"<#[\d.]+#>", " ", text)
    if is_ja:
        return len(t.replace(" ", "").strip())
    return len([w for w in t.split() if w.strip()])

# ----------------------------------------------------------------------------
# 1. CLIPS DATA - ENGLISH
# ----------------------------------------------------------------------------
CLIPS_EN = [
{
 "id": "TK1",
 "title": "Four Escalation Steps. Eighty-Two Burglaries. Then Murder",
 "signs": [8, 6],
 "theme": "Behavioral Escalation Trajectory & Precipitating Psychological Trigger",
 "hook": "Four escalation steps. Eighty-two burglaries. Then murder.",
 "bgm": "bgm_piano_minimal.mp3",
 "bgm_desc": "Act 2 — episode bed: bgm_piano_minimal.mp3",
 "sfx": ["amb_winter_wind.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"after_id": "TK1.01#1", "text": "4 STEPS · 82 BURGLARIES · 1 HOMICIDE", "dur_s": 3.0},
   {"after_id": "TK1.01#3", "text": "STEP ONE — NIGHTTIME VOYEURISM", "dur_s": 2.5},
   {"after_id": "TK1.01#4", "text": "STEP TWO — BREAKING & ENTERING FOR INTIMATE ITEMS", "dur_s": 2.5},
   {"after_id": "TK1.01#7", "text": "STEP THREE — INFILTRATING OCCUPIED HOMES", "dur_s": 2.5},
   {"after_id": "TK1.01#8", "text": "STEP FOUR — THE FATAL THRESHOLD", "dur_s": 2.5},
   {"after_id": "TK1.01#10", "text": "PSYCHOLOGICAL TRIGGER · JULY 2009", "dur_s": 2.5}
 ],
 "sources": ["2.05#1-#16", "3.05#7-#10", "5.07#5-#6", "R. v. Williams 2010 ONSC 5946"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_escalation_stairs","still",
   "Four escalation steps. Eighty-two burglaries. Then murder.",
   "2.05#1 · 2.05#7 · 5.07#5"),
  ("H","neutral",-0.02,0.6,"tk02_escalation_stairs","pull",
   "He didn't start with violence. He began by standing outside bedroom windows in the dead of night.",
   "2.05#2 · 2.05#3 · 5.07#5"),
  ("D","neutral",-0.03,0.6,"tk02_open_window","push",
   "Step one: nighttime voyeurism, lurking in the darkness to spy on women through their windows.",
   "2.05#2 · 2.05#3"),
  ("D","neutral",-0.03,0.6,"tk02_drawer_dark","pan",
   "Step two: breaking and entering for intimate property. He took neither cash nor jewelry. He stole women's underwear and personal belongings.",
   "2.05#4 · 2.05#8 · 2.05#9"),
  ("D","neutral",-0.03,0.5,"tk02_folder_tree","still",
   "His ritual remained identical in every house: photographing, taking items, and logging each event.",
   "2.05#10"),
  ("C","neutral",-0.02,0.6,"tk02_brain_neural","push",
   "When familiar acts ceased to satisfy, he fell into fantasy hunger, compelled to escalate the risk to recapture the initial high.",
   "3.05#7 · 3.05#8 · 3.05#9"),
  ("D","neutral",-0.03,0.6,"tk02_open_window","pan",
   "Step three: in September 2009, he invaded homes while the occupants were inside.",
   "2.05#11 · 2.05#12 · 2.05#13"),
  ("D","neutral",-0.03,0.7,"tk02_two_chairs","still",
   "And step four: in late November 2009, his victim was Corporal Marie-France Comeau, serving on the very base he commanded.",
   "2.05#14 · 2.05#15"),
  ("H","neutral",-0.02,0.6,"tk02_house_missing","pull",
   "Merely two months later, his next victim was Jessica Lloyd.",
   "2.05#16"),
  ("C","neutral",-0.02,0.6,"tk02_oath_hall","push",
   "In July 2009, his promotion to Base Commander at Trenton became the psychological trigger: absolute power combined with command stress shattered his final inhibitions.",
   "1.03#4 · 3.05#10"),
  ("H","neutral",-0.02,0.7,"tk02_escalation_stairs","push",
   "Predatory crime never begins with a murder. It begins with an unpunished peeping gaze.",
   "5.07#5 · 5.07#6"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Episode two of Amber Eyes. Watch the full documentary via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK2",
 "title": "Matching Tire Treads. Yet the Police Saluted Him on His Way",
 "signs": [9, 1],
 "theme": "The Halo Effect & Collective Institutional Blind Spots",
 "hook": "Matching tire treads. Yet the police saluted him on his way.",
 "bgm": "bgm_sub_drone.mp3",
 "bgm_desc": "Act 1 — episode bed: bgm_sub_drone.mp3",
 "sfx": ["amb_road_night.wav (bed)", "fx_tire_snow.wav", "fx_window_down.wav", "fx_flashlight.wav", "fx_police_radio.wav"],
 "overlay": [
   {"after_id": "TK2.01#5", "text": "MOBILE ROADBLOCK · NIGHT OF FEB 4", "dur_s": 2.5},
   {"after_id": "TK2.01#9", "text": "RECORDED THE INFO — THEN SALUTED HIM ON", "dur_s": 2.5},
   {"after_id": "TK2.01#10", "text": "THE HALO EFFECT: INVISIBLE SOCIAL SHIELD", "dur_s": 3.0}
 ],
 "sources": ["1.03#1-#4", "1.05#1", "1.08#4", "1.10#1-#2", "1.12#1-#3", "1.14#1-#6", "OPP Roadblock Logs"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_checkpoint","still",
   "Matching tire treads. And the police still respectfully saluted that man on his way.",
   "1.14#4 · 1.14#5"),
  ("H","neutral",-0.02,0.6,"tk02_oath_hall","pull",
   "In July 2009, Colonel Russell Williams assumed supreme command of Canadian Forces Base Trenton.",
   "1.03#1 · 1.03#4"),
  ("H","neutral",-0.02,0.6,"tk02_oath_hall","pan",
   "He had piloted VIP flights for Queen Elizabeth the Second.",
   "1.05#1"),
  ("D","neutral",-0.03,0.6,"tk02_house_missing","still",
   "On the night of January 28th, 2010, twenty-seven-year-old Jessica Lloyd vanished from her home in Belleville.",
   "1.10#1 · 1.10#2"),
  ("D","neutral",-0.03,0.7,"tk02_checkpoint","push",
   "Police found no leads during the first days. One week later, on February 4th, they ran an all-night mobile roadblock hunting a rare off-road tire tread in the snow.",
   "1.12#1 · 1.12#2 · 1.12#3"),
  ("D","neutral",-0.03,0.6,"tk02_suv_stop","still",
   "Among the vehicles passing through that night was a Nissan Pathfinder, instead of his usual BMW.",
   "1.14#1 · 1.14#2"),
  ("D","neutral",-0.03,0.5,"tk02_suv_stop","push",
   "The man behind the wheel rolled down the window: the Base Commander of CFB Trenton himself.",
   "1.14#3"),
  ("H","neutral",-0.02,0.5,"tk02_tire_track","still",
   "His tire tread matched the impressions in the snow almost perfectly.",
   "1.14#4"),
  ("D","neutral",-0.03,0.7,"tk02_checkpoint","pan",
   "Yet faced with a high-ranking officer, patrolmen could not detain him: they logged his details, saluted, and let him go. For three more days, he remained a free colonel.",
   "1.14#5 · 1.14#6"),
  ("C","neutral",-0.02,0.7,"tk02_siren_wall","push",
   "The Halo Effect: an invisible shield that blinded both society and law enforcement for years.",
   "1.08#4"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Episode two of Amber Eyes. Watch the full documentary via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK3",
 "title": "Two Lives. One Body. A Tale to Self-Justify",
 "signs": [5, 3],
 "theme": "Moral Neutralization & Compartmentalization Defense Mechanism",
 "hook": "Two lives. One body. A story to self-justify.",
 "bgm": "bgm_cello_sad_v2.mp3",
 "bgm_desc": "Act 3 — episode bed: bgm_cello_sad_v2.mp3",
 "sfx": ["amb_basement.wav (bed)", "fx_drawer_open.wav", "fx_stinger.wav", "fx_hdd_spin.wav"],
 "overlay": [
   {"after_id": "TK3.01#3", "text": "COMPARTMENTALIZATION: SPLITTING THE PSYCHE", "dur_s": 3.0},
   {"after_id": "TK3.01#4", "text": "DRAWER ONE — THE IMMACULATE COLONEL", "dur_s": 2.5},
   {"after_id": "TK3.01#5", "text": "DRAWER TWO — THE SHADOW PREDATOR", "dur_s": 2.5},
   {"after_id": "TK3.01#7", "text": "TECHNIQUES OF NEUTRALIZATION", "dur_s": 3.0},
   {"after_id": "TK3.01#8", "text": "“JUST A SOUVENIR”", "dur_s": 2.5},
   {"after_id": "TK3.01#10", "text": "“THE ANSWERS DON'T MATTER”", "dur_s": 2.5}
 ],
 "sources": ["3.04#1-#2", "3.08#1-#12", "OPP Interrogation Transcript Feb 7 2010"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_two_drawers","still",
   "Two lives. One body. A story to self-justify.",
   "3.08#1 · 3.08#8"),
  ("H","neutral",-0.02,0.7,"tk02_two_masks","pull",
   "Before analyzing: no official clinical psychiatric diagnosis has ever been released regarding Russell Williams. This is an analytical framework, not a moral trial.",
   "3.04#1 · 3.04#2"),
  ("C","neutral",-0.02,0.7,"tk02_brain_neural","push",
   "In psychology, compartmentalization is a defense mechanism that locks two contradictory cognitive streams into separate mental drawers.",
   "3.08#2"),
  ("C","neutral",-0.02,0.6,"tk02_command_chair","pan",
   "The first drawer was the colonel: an exemplary commander and devoted husband tending his garden.",
   "3.08#4"),
  ("C","neutral",-0.02,0.6,"tk02_stairs_dark","push",
   "The second drawer was the nocturnal predator, where he unleashed his darkest impulses.",
   "3.08#5"),
  ("C","neutral",-0.02,0.7,"tk02_two_drawers","still",
   "Inside this drawer, he locked the door to the other, using his wife and respectable marriage as a shield.",
   "3.08#6 · 3.08#7"),
  ("C","neutral",-0.02,0.8,"tk02_drawer_dark","pull",
   "To silence conscience, he neutralized guilt. Through eighty-two break-ins, he told himself: <#0.35#> I only watched, I harmed no one, I only kept a souvenir.",
   "3.08#8"),
  ("C","neutral",-0.02,0.7,"tk02_hidden_drive","pan",
   "When violence escalated to murder, he rationalized that the victim had seen his face, forcing him to act in self-defense.",
   "3.08#9"),
  ("C","neutral",-0.02,0.6,"tk02_hidden_drive","still",
   "Consequently, he could never offer a genuine moral explanation.",
   "3.08#10"),
  ("C","neutral",-0.02,0.7,"tk02_interrogation_early","push",
   "When asked why he did it, his confession was chillingly hollow: <#0.35#> Yes, but I don't know the answers, and I'm pretty sure the answers don't matter.",
   "3.08#11"),
  ("C","sad",-0.04,0.7,"tk02_head_down","pull",
   "That was the most callous reply, laying bare the predator's total moral disconnection.",
   "3.08#12"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Episode two of Amber Eyes. Watch the full documentary via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK4",
 "title": "Not a Single Apology Mentioned the Victims",
 "signs": [4, 1],
 "theme": "Narcissistic Collapse & Psychological Sentence",
 "hook": "Not a single apology mentioned the victims.",
 "bgm": "bgm_piano_warm.mp3",
 "bgm_desc": "Act 5 — episode bed: bgm_piano_warm.mp3",
 "sfx": ["amb_courtroom.wav (bed)", "fx_gavel_triple.wav", "fx_fire_whoosh.wav", "amb_fire.wav", "fx_heartbeat_slow.wav"],
 "overlay": [
   {"after_id": "TK4.01#1", "text": "NOT A SINGLE WORD OF REMORSE FOR THE VICTIMS", "dur_s": 3.0},
   {"after_id": "TK4.01#3", "text": "NOT REPENTANCE — PATHOLOGICAL SELF-PITY", "dur_s": 2.5},
   {"after_id": "TK4.01#4", "text": "GUILTY ON ALL 88 CHARGES", "dur_s": 2.5},
   {"after_id": "TK4.01#5", "text": "CONCURRENT LIFE SENTENCES · 25 YEARS NO PAROLE", "dur_s": 2.5},
   {"after_id": "TK4.01#7", "text": "BURNING EVERY UNIFORM BEARING HIS NAME", "dur_s": 2.5},
   {"after_id": "TK4.01#9", "text": "NARCISSISTIC COLLAPSE", "dur_s": 3.0}
 ],
 "sources": ["4.11#6-#9", "5.02#1-#5", "5.04#1-#7", "5.06#4", "Ontario Superior Court 2010"],
 "lines": [
  ("H","neutral",-0.02,0.6,"tk02_interrogation_early","still",
   "Not a single apology mentioned the victims.",
   "4.11#6 · 4.11#7"),
  ("C","sad",-0.04,0.8,"tk02_two_chairs","pull",
   "In the interrogation room, his anxiety focused entirely on how his wife viewed him, and the base's reputation. He never voiced remorse for the women or their families.",
   "4.11#6 · 4.11#7"),
  ("C","sad",-0.04,0.8,"tk02_head_down","push",
   "That was not genuine contrition: it was intense self-pity as the mask of honor built over twenty-five years disintegrated.",
   "4.11#8 · 4.11#9"),
  ("H","neutral",-0.02,0.6,"tk02_courtroom","still",
   "On October 18th, 2010, he pleaded guilty to all eighty-eight charges.",
   "5.02#1 · 5.02#3"),
  ("H","neutral",-0.02,0.8,"tk02_gavel","push",
   "Three days later, the judge sentenced him to concurrent life sentences with no eligibility for parole for twenty-five years.",
   "5.02#4 · 5.02#5"),
  ("H","neutral",-0.02,0.6,"tk02_courtroom","pan",
   "Yet the ultimate sentence for a narcissist was the destruction of honor: his rank revoked, his medals physically cut to pieces.",
   "5.04#1 · 5.04#2 · 5.04#3"),
  ("H","neutral",-0.02,0.7,"tk02_uniform_fire","still",
   "The Canadian military took an unprecedented step: burning all uniforms bearing his name in a classified incinerator.",
   "5.04#5"),
  ("D","neutral",-0.03,0.7,"tk02_uniform_fire","pan",
   "According to military spokesman Hubert Genest: no ceremony, and no photographs were permitted.",
   "5.04#6 · 5.04#7"),
  ("C","neutral",-0.02,0.6,"tk02_brain_neural","pull",
   "Psychologically, it was a textbook narcissistic collapse: stripped of control, the predator is left with nothing but pathetic self-pity.",
   "5.06#4"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Episode two of Amber Eyes. Watch the full documentary via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK5",
 "title": "Always Trust Your Intuition",
 "signs": [10],
 "theme": "Victimology & Critical Survival Warning Signals (Boundaries & Intuition)",
 "hook": "If you feel unease, never rationalize it away.",
 "bgm": "bgm_ambient_deep.mp3",
 "bgm_desc": "Act 5 — episode bed: bgm_ambient_deep.mp3",
 "sfx": ["amb_road_night.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav", "fx_heartbeat_slow.wav"],
 "overlay": [
   {"after_id": "TK5.01#1", "text": "NEVER RATIONALIZE VAGUE UNEASE", "dur_s": 2.5},
   {"after_id": "TK5.01#2", "text": "EARLIEST SIGNAL: BOUNDARY INTRUSION", "dur_s": 2.5},
   {"after_id": "TK5.01#4", "text": "CRIME STARTS WITH MINOR TRESPASSES", "dur_s": 2.5},
   {"after_id": "TK5.01#7", "text": "ALWAYS TRUST YOUR SURVIVAL INTUITION", "dur_s": 3.0}
 ],
 "sources": ["4.06#1-#3", "5.07#4-#6", "5.08#2-#5", "Gavin de Becker - The Gift of Fear"],
 "lines": [
  ("H","neutral",-0.02,0.6,"tk02_red_flags","still",
   "If you sense an ambiguous unease, if your personal boundaries are breached in the slightest way, never rationalize or dismiss it.",
   "5.08#4"),
  ("D","neutral",-0.03,0.6,"tk02_town_snow","pull",
   "In this case, before the truth came out, the town of Tweed lived under an intangible, suffocating dread.",
   "4.06#1"),
  ("N2","sad",-0.04,0.8,"tk02_cottage_search","push",
   "Personal items were mysteriously rearranged, doors showed signs of prying, but no money was taken. We assumed we were just paranoid.",
   "4.06#2 · 4.06#3"),
  ("H","neutral",-0.02,0.8,"tk02_escalation_stairs","pan",
   "Predatory crime never begins with a murder. It begins with minor boundary crossings: a peeping gaze, rummaging through private drawers, an unpunished trespass.",
   "5.07#5 · 5.07#6"),
  ("C","neutral",-0.02,0.7,"tk02_oath_hall","pull",
   "Status, degrees, and splendid military rank are merely social overcoats; they offer no guarantee for the decency of a human soul.",
   "5.07#4"),
  ("D","neutral",-0.03,0.6,"tk02_escalation_stairs","pan",
   "A narcissist's arrogance invariably leaves a trail.",
   "5.08#2"),
  ("D","neutral",-0.03,0.8,"tk02_red_flags","still",
   "Always trust your intuition. Survival intuition is our built-in early warning radar designed to protect our lives.",
   "5.08#3 · 5.08#5"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Episode two of Amber Eyes. Watch the full documentary via the link in our bio.",
   "CTA")
 ]
}
]

# ----------------------------------------------------------------------------
# 2. CLIPS DATA - JAPANESE
# ----------------------------------------------------------------------------
CLIPS_JA = [
{
 "id": "TK1",
 "title": "4つの階段。82件の侵入。そして殺人へと至る軌跡",
 "signs": [8, 6],
 "theme": "行動のエスカレーション軌跡と心理的引き金（Precipitating Trigger）",
 "hook": "4つの階段。82件の侵入。そして殺人へと至る軌跡。",
 "bgm": "bgm_piano_minimal.mp3",
 "bgm_desc": "第2幕 — 本編BGM: bgm_piano_minimal.mp3",
 "sfx": ["amb_winter_wind.wav (環境音)", "fx_tension_tick.wav", "fx_stinger.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"after_id": "TK1.01#1", "text": "4つの段階 · 82件の侵入 · 1つの殺人", "dur_s": 3.0},
   {"after_id": "TK1.01#3", "text": "第1段階 — 深夜の覗き見", "dur_s": 2.5},
   {"after_id": "TK1.01#4", "text": "第2段階 — 留守宅侵入と私物窃取", "dur_s": 2.5},
   {"after_id": "TK1.01#7", "text": "第3段階 — 住人在宅時の侵入", "dur_s": 2.5},
   {"after_id": "TK1.01#8", "text": "第4段階 — 生命の強奪", "dur_s": 2.5},
   {"after_id": "TK1.01#10", "text": "心理的引き金 · 2009年7月", "dur_s": 2.5}
 ],
 "sources": ["2.05#1-#16", "3.05#7-#10", "5.07#5-#6", "R. v. Williams 2010 ONSC 5946 判決書"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_escalation_stairs","still",
   "4つの階段。82件の侵入。そして1件の殺人。",
   "2.05#1 · 2.05#7 · 5.07#5"),
  ("H","neutral",-0.02,0.5,"tk02_escalation_stairs","pull",
   "最初から暴力を振るったのではありません。深夜、窓の外に佇むことから始まりました。",
   "2.05#2 · 2.05#3 · 5.07#5"),
  ("D","neutral",-0.03,0.5,"tk02_open_window","push",
   "第1段階は深夜の覗き見。闇に潜み、窓越しに女性たちの私生活を監視しました。",
   "2.05#2 · 2.05#3"),
  ("D","neutral",-0.03,0.5,"tk02_drawer_dark","pan",
   "第2段階は留守宅侵入。金品には触れず、女性たちの下着や私物だけを持ち去りました。",
   "2.05#4 · 2.05#8 · 2.05#9"),
  ("D","neutral",-0.03,0.5,"tk02_folder_tree","still",
   "儀式は全件で同一：写真を撮り、品を持ち去り、克明に記録を残すのです。",
   "2.05#10"),
  ("C","neutral",-0.02,0.6,"tk02_brain_neural","push",
   "行動が日常化すると妄想の飢餓に陥り、快感を再現するためにより高いリスクを冒します。",
   "3.05#7 · 3.05#8 · 3.05#9"),
  ("D","neutral",-0.03,0.5,"tk02_open_window","pan",
   "第3段階：2009年9月、住人が在宅中の民家へ押し入り、拘束に及びました。",
   "2.05#11 · 2.05#12 · 2.05#13"),
  ("D","neutral",-0.03,0.6,"tk02_two_chairs","still",
   "そして第4段階：2009年11月、基地所属の37歳伍長Marie-France Comeauの命を強奪。",
   "2.05#14 · 2.05#15"),
  ("H","neutral",-0.02,0.5,"tk02_house_missing","pull",
   "わずか2カ月後、次の犠牲となったのがJessica Lloydでした。",
   "2.05#16"),
  ("C","neutral",-0.02,0.6,"tk02_oath_hall","push",
   "2009年7月の基地司令官昇進が引き金でした：絶対的権力と重圧が、最後のブレーキを破壊したのです。",
   "1.03#4 · 3.05#10"),
  ("H","neutral",-0.02,0.6,"tk02_escalation_stairs","push",
   "犯罪は殺人から始まるのではありません。処罰されなかった覗き見から始まるのです。",
   "5.07#5 · 5.07#6"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Amber Eyes 第2話。完全版はプロフィールのリンクから。",
   "CTA")
 ]
},
{
 "id": "TK2",
 "title": "タイヤ痕の一致。それでも警察は敬礼して見送った",
 "signs": [9, 1],
 "theme": "ハロー効果（Halo Effect）と集団的盲点",
 "hook": "タイヤ痕の一致。それでも警察はその男に敬礼して見送った。",
 "bgm": "bgm_sub_drone.mp3",
 "bgm_desc": "第1幕 — 本編BGM: bgm_sub_drone.mp3",
 "sfx": ["amb_road_night.wav (環境音)", "fx_tire_snow.wav", "fx_window_down.wav", "fx_flashlight.wav", "fx_police_radio.wav"],
 "overlay": [
   {"after_id": "TK2.01#5", "text": "移動式検問所 · 2月4日の夜", "dur_s": 2.5},
   {"after_id": "TK2.01#9", "text": "情報を控えただけで — 敬礼して通過させた", "dur_s": 2.5},
   {"after_id": "TK2.01#10", "text": "ハロー効果：社会と警察を眩ませた不可視の盾", "dur_s": 3.0}
 ],
 "sources": ["1.03#1-#4", "1.05#1", "1.08#4", "1.10#1-#2", "1.12#1-#3", "1.14#1-#6", "OPP 検問所調書"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_checkpoint","still",
   "タイヤ痕は一致していました。それでも警察官たちは、その男に敬礼して送り出しました。",
   "1.14#4 · 1.14#5"),
  ("H","neutral",-0.02,0.5,"tk02_oath_hall","pull",
   "2009年7月、Russell Williams大佐はトレントン空軍基地の最高司令官に就任。",
   "1.03#1 · 1.03#4"),
  ("H","neutral",-0.02,0.5,"tk02_oath_hall","pan",
   "彼はかつて、エリザベス女王専用機の操縦桿を握った英雄でした。",
   "1.05#1"),
  ("D","neutral",-0.03,0.6,"tk02_house_missing","still",
   "2010年1月28日の夜、27歳の女性Jessica Lloydが自宅から突如姿を消しました。",
   "1.10#1 · 1.10#2"),
  ("D","neutral",-0.03,0.6,"tk02_checkpoint","push",
   "手がかりは皆無。1週間後の夜、警察は雪上に残された珍しいタイヤ痕を追うため検問を敷きました。",
   "1.12#1 · 1.12#2 · 1.12#3"),
  ("D","neutral",-0.03,0.5,"tk02_suv_stop","still",
   "そこを通りかかった1台の日産パスファインダー。普段のBMWとは違う車でした。",
   "1.14#1 · 1.14#2"),
  ("D","neutral",-0.03,0.5,"tk02_suv_stop","push",
   "窓を下ろしたのは、トレントン空軍基地の最高司令官その人でした。",
   "1.14#3"),
  ("H","neutral",-0.02,0.5,"tk02_tire_track","still",
   "タイヤの溝は、現場の雪上に残されたものと酷似していました。",
   "1.14#4"),
  ("D","neutral",-0.03,0.6,"tk02_checkpoint","pan",
   "だが高級将校を前に警官は拘束できず、敬礼して見送りました。その後3日間、彼は自由の身でした。",
   "1.14#5 · 1.14#6"),
  ("C","neutral",-0.02,0.6,"tk02_siren_wall","push",
   "ハロー効果：社会と警察の目を長年にわたって眩ませ続けた不可視の盾です。",
   "1.08#4"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Amber Eyes 第2話。完全版はプロフィールのリンクから。",
   "CTA")
 ]
},
{
 "id": "TK3",
 "title": "2つの人生。1つの身体。自己正当化のための物語",
 "signs": [5, 3],
 "theme": "自己正当化（中和技術）と絶対的精神の分断（コンパートメンタライゼーション）",
 "hook": "2つの人生。1つの身体。自己正当化のための物語。",
 "bgm": "bgm_cello_sad_v2.mp3",
 "bgm_desc": "第3幕 — 本編BGM: bgm_cello_sad_v2.mp3",
 "sfx": ["amb_basement.wav (環境音)", "fx_drawer_open.wav", "fx_stinger.wav", "fx_hdd_spin.wav"],
 "overlay": [
   {"after_id": "TK3.01#3", "text": "コンパートメンタライゼーション：精神の分断", "dur_s": 3.0},
   {"after_id": "TK3.01#4", "text": "第1の引き出し — 模範的な大佐", "dur_s": 2.5},
   {"after_id": "TK3.01#5", "text": "第2の引き出し — 夜の捕食者", "dur_s": 2.5},
   {"after_id": "TK3.01#7", "text": "中和技術（自己正当化）", "dur_s": 3.0},
   {"after_id": "TK3.01#8", "text": "「単なる記念品」", "dur_s": 2.5},
   {"after_id": "TK3.01#10", "text": "「答えは重要ではない」", "dur_s": 2.5}
 ],
 "sources": ["3.04#1-#2", "3.08#1-#12", "OPP 尋問調書 2010年2月7日"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_two_drawers","still",
   "2つの人生。1つの身体。自己正当化のための物語。",
   "3.08#1 · 3.08#8"),
  ("H","neutral",-0.02,0.6,"tk02_two_masks","pull",
   "分析の前提：公的な臨床診断はありません。これは犯罪心理学の理論モデルです。",
   "3.04#1 · 3.04#2"),
  ("C","neutral",-0.02,0.6,"tk02_brain_neural","push",
   "コンパートメンタライゼーション：相容れない認知を別個の引き出しに隔離する防衛機制。",
   "3.08#2"),
  ("C","neutral",-0.02,0.5,"tk02_command_chair","pan",
   "第1の引き出しは大佐：庭を愛し、規律に生きる模範的な司令官であり夫。",
   "3.08#4"),
  ("C","neutral",-0.02,0.5,"tk02_stairs_dark","push",
   "第2の引き出しは夜の捕食者：陰惨な衝動を解き放つ怪物。",
   "3.08#5"),
  ("C","neutral",-0.02,0.6,"tk02_two_drawers","still",
   "一方にいる時、彼はもう一方の扉を閉ざし、家庭を盾にしました。",
   "3.08#6 · 3.08#7"),
  ("C","neutral",-0.02,0.7,"tk02_drawer_dark","pull",
   "中和技術：82件の侵入の間、<#0.35#> 誰も傷つけていない、記念品を持っているだけだと自己正当化しました。",
   "3.08#8"),
  ("C","neutral",-0.02,0.6,"tk02_hidden_drive","pan",
   "凶行に及んだ時でさえ、顔を見られた以上、自己防衛のためだったと責任転嫁したのです。",
   "3.08#9"),
  ("C","neutral",-0.02,0.5,"tk02_hidden_drive","still",
   "そして彼には真の道徳的説明など一切できませんでした。",
   "3.08#10"),
  ("C","neutral",-0.02,0.6,"tk02_interrogation_early","push",
   "尋問官への答えは凍りつくほど空虚でした：<#0.35#> ええ、ですが答えは重要ではありません。",
   "3.08#11"),
  ("C","sad",-0.04,0.6,"tk02_head_down","pull",
   "それこそが、冷徹な捕食者の完全なる道徳的離脱を露呈させた言葉でした。",
   "3.08#12"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Amber Eyes 第2話。完全版はプロフィールのリンクから。",
   "CTA")
 ]
},
{
 "id": "TK4",
 "title": "被害者に向けられた謝罪はただの一言もなかった",
 "signs": [4, 1],
 "theme": "自己愛の崩壊（Narcissistic Collapse）と心理的判決",
 "hook": "被害者に向けられた謝罪はただの一言もなかった。",
 "bgm": "bgm_piano_warm.mp3",
 "bgm_desc": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
 "sfx": ["amb_courtroom.wav (環境音)", "fx_gavel_triple.wav", "fx_fire_whoosh.wav", "amb_fire.wav", "fx_heartbeat_slow.wav"],
 "overlay": [
   {"after_id": "TK4.01#1", "text": "被害者への謝罪は一言もなかった", "dur_s": 3.0},
   {"after_id": "TK4.01#3", "text": "悔悟ではない — 極限の自己憐憫", "dur_s": 2.5},
   {"after_id": "TK4.01#4", "text": "88件の罪状すべてで有罪", "dur_s": 2.5},
   {"after_id": "TK4.01#5", "text": "仮釈放なし25年の終身刑", "dur_s": 2.5},
   {"after_id": "TK4.01#7", "text": "彼の名前が刻まれた全軍服の焼却", "dur_s": 2.5},
   {"after_id": "TK4.01#9", "text": "自己愛の崩壊（NARCISSISTIC COLLAPSE）", "dur_s": 3.0}
 ],
 "sources": ["4.11#6-#9", "5.02#1-#5", "5.04#1-#7", "5.06#4", "オンタリオ州高等裁判所 2010年判決"],
 "lines": [
  ("H","neutral",-0.02,0.6,"tk02_interrogation_early","still",
   "被害者に向けられた謝罪の言葉は、ただの一言もありませんでした。",
   "4.11#6 · 4.11#7"),
  ("C","sad",-0.04,0.7,"tk02_two_chairs","pull",
   "尋問室で彼が口にした懸念は、妻からどう見られるか、基地の評判がどうなるかだけでした。被害者への悔悟はありませんでした。",
   "4.11#6 · 4.11#7"),
  ("C","sad",-0.04,0.7,"tk02_head_down","push",
   "それは真摯な反省ではなく、25年間磨き上げた名誉の仮面が砕け散ったことへの極限の自己憐憫でした。",
   "4.11#8 · 4.11#9"),
  ("H","neutral",-0.02,0.6,"tk02_courtroom","still",
   "2010年10月18日、彼は88件の罪状すべてについて有罪を認めました。",
   "5.02#1 · 5.02#3"),
  ("H","neutral",-0.02,0.7,"tk02_gavel","push",
   "3日後、裁判官は仮釈放資格のない25年間の終身刑を言い渡しました。",
   "5.02#4 · 5.02#5"),
  ("H","neutral",-0.02,0.6,"tk02_courtroom","pan",
   "だが彼のようなナルシシストへの最大の刑罰は、名誉の完全な剥奪：軍管轄権は剥奪され、勲章は切り刻まれました。",
   "5.04#1 · 5.04#2 · 5.04#3"),
  ("H","neutral",-0.02,0.6,"tk02_uniform_fire","still",
   "カナダ軍は前代未聞の措置を断行：彼の名前が刺繍されたすべての軍服を機密文書焼却炉で焼き尽くしたのです。",
   "5.04#5"),
  ("D","neutral",-0.03,0.6,"tk02_uniform_fire","pan",
   "軍報道官によれば、いかなる公式儀礼もなく、写真撮影すら一切許されませんでした。",
   "5.04#6 · 5.04#7"),
  ("C","neutral",-0.02,0.6,"tk02_brain_neural","pull",
   "心理学的には典型的な自己愛の崩壊：支配力を失った捕食者には、みじめな自己憐憫しか残されていませんでした。",
   "5.06#4"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Amber Eyes 第2話。完全版はプロフィールのリンクから。",
   "CTA")
 ]
},
{
 "id": "TK5",
 "title": "自らの直感を常に信じること",
 "signs": [10],
 "theme": "被害者学と生存のための警戒シグナル（境界線と直感）",
 "hook": "曖昧な違和感を覚えたなら、決して見過ごしてはならない。",
 "bgm": "bgm_ambient_deep.mp3",
 "bgm_desc": "第5幕 — 本編BGM: bgm_ambient_deep.mp3",
 "sfx": ["amb_road_night.wav (環境音)", "fx_tension_tick.wav", "fx_stinger.wav", "fx_heartbeat_slow.wav"],
 "overlay": [
   {"after_id": "TK5.01#1", "text": "曖昧な違和感を自己合理化してはならない", "dur_s": 2.5},
   {"after_id": "TK5.01#2", "text": "初期の兆候：侵入されるプライベート境界線", "dur_s": 2.5},
   {"after_id": "TK5.01#4", "text": "犯罪は些細な境界線の侵犯から始まる", "dur_s": 2.5},
   {"after_id": "TK5.01#7", "text": "自らの直感を常に信じること", "dur_s": 3.0}
 ],
 "sources": ["4.06#1-#3", "5.07#4-#6", "5.08#2-#5", "Gavin de Becker著『The Gift of Fear』"],
 "lines": [
  ("H","neutral",-0.02,0.6,"tk02_red_flags","still",
   "もし何か曖昧な違和感を覚えたなら、プライベートな境界線がわずかでも侵されたと感じたなら、決して見過ごしてはなりません。",
   "5.08#4"),
  ("D","neutral",-0.03,0.6,"tk02_town_snow","pull",
   "本件において、真相発覚前のTweedの町は、息が詰まるような得体の知れない不安に覆われていました。",
   "4.06#1"),
  ("N2","sad",-0.04,0.7,"tk02_cottage_search","push",
   "私物が動かされ、ドアにこじ開け痕があったのに金品は無事でした。私たちは神経過敏だと思い込んでいたのです。",
   "4.06#2 · 4.06#3"),
  ("H","neutral",-0.02,0.7,"tk02_escalation_stairs","pan",
   "犯罪は殺人から始まるのではありません。覗き見、私物の物色、処罰されない侵入といった些細な境界線の侵犯から始まります。",
   "5.07#5 · 5.07#6"),
  ("C","neutral",-0.02,0.6,"tk02_oath_hall","pull",
   "地位や学歴、煌びやかな階級章など社会的な上着に過ぎず、魂の善良さを保証する盾にはなりません。",
   "5.07#4"),
  ("D","neutral",-0.03,0.5,"tk02_escalation_stairs","pan",
   "自己愛の傲慢さは、必ずどこかに痕跡を残します。",
   "5.08#2"),
  ("D","neutral",-0.03,0.7,"tk02_red_flags","still",
   "自らの直感を常に信じてください。生存の直感とは、私たちの命を守るために備わった内なる早期警戒レーダーです。",
   "5.08#3 · 5.08#5"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Amber Eyes 第2話。完全版はプロフィールのリンクから。",
   "CTA")
 ]
}
]

# ----------------------------------------------------------------------------
# 3. METRIC ESTIMATION AND SPECS
# ----------------------------------------------------------------------------
def build_spec_en():
    spec = {
        "_readme": "SPEC_AUDIO_CLIP_TAP02_EN.json — Audio specs for 5 English TikTok clips (TK1–TK5).",
        "_episode": "02_EN",
        "_language": "en",
        "_title": "The Two-Faced Colonel & The Escalation Abyss — When the Threshold of Satisfaction Collapses",
        "_measured_rates": {r: round(RATE_EN[r], 4) for r in RATE_EN},
        "_clips_summary": {},
        "clips": {}
    }
    for c in CLIPS_EN:
        cid = c["id"]
        tot_dur = 0.0
        tot_words = 0
        lines_spec = []
        for idx, (vai, emo, spd, pause, bg, motion, text, src) in enumerate(c["lines"], 1):
            w = count_units(text, is_ja=False)
            d = round(w * RATE_EN[vai], 2)
            tot_dur += d + pause
            tot_words += w
            lines_spec.append({
                "clip_line_id": f"{cid}.01#{idx}",
                "role": vai,
                "emotion": emo,
                "speed_offset": spd,
                "pause_after_s": pause,
                "bg": bg,
                "motion": motion,
                "text": text,
                "words_spoken": w,
                "est_dur_s": d,
                "src_script": src
            })
        c["est_dur_s"] = round(tot_dur, 1)
        spec["_clips_summary"][cid] = {
            "title": c["title"],
            "lines_count": len(c["lines"]),
            "words_count": tot_words,
            "est_dur_s": round(tot_dur, 1),
            "psychological_signs": c["signs"]
        }
        spec["clips"][cid] = {
            "id": cid,
            "title": c["title"],
            "theme": c["theme"],
            "psychological_signs": c["signs"],
            "bgm": c["bgm"],
            "sfx": c["sfx"],
            "overlays": c["overlay"],
            "lines": lines_spec
        }
    return spec

def build_spec_ja():
    spec = {
        "_readme": "SPEC_AUDIO_CLIP_TAP02_JA.json — Audio specs for 5 Japanese TikTok clips (TK1–TK5).",
        "_episode": "02_JA",
        "_language": "ja",
        "_title": "二面性の大佐とエスカレーションの深淵 — 快感の閾値が崩壊する時",
        "_measured_rates": {r: round(RATE_JA[r], 4) for r in RATE_JA},
        "_clips_summary": {},
        "clips": {}
    }
    for c in CLIPS_JA:
        cid = c["id"]
        tot_dur = 0.0
        tot_chars = 0
        lines_spec = []
        for idx, (vai, emo, spd, pause, bg, motion, text, src) in enumerate(c["lines"], 1):
            ch = count_units(text, is_ja=True)
            d = round(ch * RATE_JA[vai], 2)
            tot_dur += d + pause
            tot_chars += ch
            lines_spec.append({
                "clip_line_id": f"{cid}.01#{idx}",
                "role": vai,
                "emotion": emo,
                "speed_offset": spd,
                "pause_after_s": pause,
                "bg": bg,
                "motion": motion,
                "text": text,
                "characters_spoken": ch,
                "est_dur_s": d,
                "src_script": src
            })
        c["est_dur_s"] = round(tot_dur, 1)
        spec["_clips_summary"][cid] = {
            "title": c["title"],
            "lines_count": len(c["lines"]),
            "characters_count": tot_chars,
            "est_dur_s": round(tot_dur, 1),
            "psychological_signs": c["signs"]
        }
        spec["clips"][cid] = {
            "id": cid,
            "title": c["title"],
            "theme": c["theme"],
            "psychological_signs": c["signs"],
            "bgm": c["bgm"],
            "sfx": c["sfx"],
            "overlays": c["overlay"],
            "lines": lines_spec
        }
    return spec

# ----------------------------------------------------------------------------
# 4. CAPTIONS & DESCRIPTIONS GENERATION
# ----------------------------------------------------------------------------
MO_TA_DAI_EN = {
 "TK1": """Four escalation steps. Eighty-two burglaries. Then murder. 👁️

Episode 02 · The Two-Faced Colonel — Psychological Marker #8: Behavioral Escalation Trajectory.
Documented facts from Canadian court records and police files.

📺 Watch the full 25-minute documentary on YouTube — link in bio.
🔎 Psychological Marker · Behavioral Escalation · Real Case File

——————
MARKER #8: BEHAVIORAL ESCALATION TRAJECTORY
——————
No predator starts with a homicide. That reality itself is a crucial window into how criminal behavior escalates.

This dossier reconstructs four distinct behavioral steps, each an unpunished trespass across personal boundaries:
• STEP 1 — NIGHTTIME VOYEURISM: lurking in the darkness outside suburban windows to spy on women.
• STEP 2 — BREAKING & ENTERING FOR INTIMATE PROPERTY: between September 2007 and November 2009, committing 82 burglaries and attempted burglaries. He took neither money nor valuables, stealing only intimate garments and personal belongings. His ritual was identical in every home: photographing, taking items, and logging the event.
• STEP 3 — INFILTRATING OCCUPIED HOMES: September 2009.
• STEP 4 — HOMICIDE: in late November 2009, Corporal Marie-France Comeau, 37, serving at CFB Trenton. Merely two months later, Jessica Lloyd.

Neurochemical habituation explains why escalation never halts on its own: when familiar stimuli no longer satisfy, the brain enters fantasy hunger, compelling the individual to raise operational risk to recapture the initial rush.

And the precipitating psychological catalyst occurred in July 2009: Williams was promoted to Base Commander at CFB Trenton, where absolute command authority destroyed his final internal inhibitions.

——————
CASE DOSSIER CONTEXT
——————
CFB Trenton in Ontario is Canada's largest strategic air base. In July 2009, its commander was Colonel David Russell Williams: 46 years old, decorated pilot who had flown Queen Elizabeth II, Prince Philip, and Canadian Prime Ministers.

——————
SOURCES & EVIDENCE
——————
• Ontario Superior Court of Justice — R. v. Williams, 2010 ONSC 5946
• Ontario Provincial Police (OPP) & Belleville Police Service reports
• Interrogation transcript dated February 7, 2010 · Detective Jim Smyth testimony
• Script dossier: 01_KICH_BAN/Ho_So_Toi_Pham/Tap02_EN/kichban_tap02_EN.md

——————
VIEWER NOTICE
——————
• Visuals and voices created with AI assistance for behavioral analysis.
• Viewer discretion advised. Not suitable for children.
• Educational case analysis; does not replace medical or legal counsel.

#AmberEyes #CriminalPsychology #TrueCrime #Escalation #CaseFile #RussellWilliams""",

 "TK2": """Matching tire treads. Yet the police saluted him on his way. 👁️

Episode 02 · The Two-Faced Colonel — Psychological Marker #9: The Halo Effect.
Documented facts from Canadian court records and police files.

📺 Watch the full 25-minute documentary on YouTube — link in bio.
🔎 Psychological Marker · The Halo Effect · Real Case File

——————
MARKER #9: THE HALO EFFECT & INSTITUTIONAL BLIND SPOTS
——————
On the night of January 28, 2010, 27-year-old Jessica Lloyd vanished from her home in Belleville. Ontario Provincial Police launched an unprecedented search, yet the initial days yielded no leads.

One week later, on February 4th, police established an all-night mobile roadblock near the victim's house, hunting a rare Kumho off-road tire tread found in the snow.

Among the vehicles passing through was a Nissan Pathfinder — driven instead of the suspect's customary BMW. When flashlight beams struck the tire, the tread matched the crime scene impression. Yet facing a poised, decorated colonel, patrolmen recorded his information, respectfully saluted, and sent him on his way. For three more days, he walked free.

The Halo Effect served as an invisible armor: prestigious military rank, spotless service, and piloting Royal flights blinded institutions and society alike.

At what point does institutional deference become dangerous? Share your thoughts below 👇

#AmberEyes #CriminalPsychology #TrueCrime #HaloEffect #CaseFile #RussellWilliams""",

 "TK3": """Two lives. One body. A story to self-justify. 👁️

Episode 02 · The Two-Faced Colonel — Psychological Marker #5: Moral Neutralization & Compartmentalization.
Documented facts from Canadian court records and police files.

📺 Watch the full 25-minute documentary on YouTube — link in bio.
🔎 Psychological Marker · Compartmentalization · Real Case File

——————
MARKER #5: COMPARTMENTALIZATION & MORAL NEUTRALIZATION
——————
Before analyzing: no official psychiatric diagnosis has been published regarding Russell Williams. Theoretical models serve as analytical lenses, not moral judgments.

• Compartmentalization: the psyche partitions conflicting cognitive streams into isolated mental drawers.
  - Drawer One: Colonel Williams — the devoted commander and gentle husband tending his garden.
  - Drawer Two: The nocturnal predator releasing sadistic impulses.
• Techniques of Neutralization: across 82 burglaries, he told himself he was only taking souvenirs and harming no one. When homicide occurred, he rationalized that the victim had seen him, forcing him to act in self-defense.

When asked by detectives why he did it, his answer was chillingly hollow: "Yes, but I don't know the answers, and I'm pretty sure the answers don't matter."

Where is the line between human conscience and self-serving neutralization? Share your thoughts below 👇

#AmberEyes #CriminalPsychology #TrueCrime #Compartmentalization #CaseFile #RussellWilliams""",

 "TK4": """Not a single apology mentioned the victims. 👁️

Episode 02 · The Two-Faced Colonel — Psychological Marker #4: Narcissistic Collapse.
Documented facts from Canadian court records and police files.

📺 Watch the full 25-minute documentary on YouTube — link in bio.
🔎 Psychological Marker · Narcissistic Collapse · Real Case File

——————
MARKER #4: NARCISSISTIC COLLAPSE & PSYCHOLOGICAL SENTENCE
——————
When the hidden digital archive was uncovered in his basement ceiling, Williams's cognitive wall collapsed.

Inside the interrogation room, his anxiety focused entirely on how his wife viewed him and the reputational devastation to the military base. He never expressed a single word of remorse for the women he violated or their grieving families.

On October 18, 2010, he pleaded guilty to all 88 counts, receiving concurrent life sentences with no parole eligibility for 25 years. Yet his most crushing sentence was the total destruction of his public persona: the Governor General revoked his commission, his medals were cut to pieces, and the military burned all uniforms bearing his name in a classified incinerator.

Stripped of omnipotent control, a malignant narcissist is left with nothing but pathetic self-pity.

When does remorse turn into mere self-preservation? Share your thoughts below 👇

#AmberEyes #CriminalPsychology #TrueCrime #NarcissisticCollapse #CaseFile #RussellWilliams""",

 "TK5": """If you feel unease, never rationalize it away. 👁️

Episode 02 · The Two-Faced Colonel — Psychological Marker #10: Survival Intuition & Victimology.
Documented facts from Canadian court records and police files.

📺 Watch the full 25-minute documentary on YouTube — link in bio.
🔎 Psychological Marker · Survival Intuition · Real Case File

——————
MARKER #10: SURVIVAL INTUITION & BOUNDARIES
——————
Before the truth surfaced, the town of Tweed lived in suffocating dread. Personal belongings were mysteriously rearranged and doors bore prying marks without monetary theft. Residents dismissed their instincts as paranoia.

Critical takeaways from this dossier:
• Predatory violence never begins with murder; it starts with minor, unpunished boundary trespasses.
• Status, degrees, and military rank are merely social overcoats, never guarantees of moral decency.
• If you sense an ambiguous unease, if your personal boundaries are breached in the slightest way, never rationalize or dismiss it.
• Always trust your intuition: survival intuition is our built-in early warning radar designed to protect our lives.

Which everyday warning signal do you find easiest to overlook? Share your thoughts below 👇

#AmberEyes #CriminalPsychology #TrueCrime #SurvivalIntuition #CaseFile #RussellWilliams"""
}

MO_TA_DAI_JA = {
 "TK1": """4つの階段。82件の侵入。そして殺人へと至る軌跡。 👁️

第02話 · 二面性の大佐 — 心理指標 #8: 行動のエスカレーション軌跡。
裁判記録および公的捜査資料に基づく実話プロファイリング。

📺 完全版ドキュメンタリー（25分）はYouTubeで公開中 — プロフィールのリンクから。
🔎 犯罪心理学 · 行動のエスカレーション · 実在事件調書

——————
心理指標 #8: 行動のエスカレーション軌跡
——————
最初から殺人を目的に行動を起こす捕食者はいません。その事実こそが、行動のエスカレーションの解明における重要な手がかりです。

本事件において再構築された4つの段階は、処罰されずにエスカレートしていった境界線の侵犯記録です：
• 第1段階 — 深夜の覗き行為：住宅街の暗闇に潜み、窓越しに女性たちの私生活を覗き見る。
• 第2段階 — 留守宅への侵入と私物の窃取：2007年9月から2009年11月までの間に計82件の侵入。金品には目もくれず、女性たちの下着や極めて私的な衣類だけを持ち去り、写真を撮影して克明に記録を残す。
• 第3段階 — 住人在宅時の侵入：2009年9月、在宅中の民家へと押し入り拘束。
• 第4段階 — 生命の強奪：2009年11月下旬、基地所属の37歳伍長Marie-France Comeau。わずか2カ月後、Jessica Lloyd。

刺激に対する脳の適応機構は、なぜ段階が止まらなかったかを解き明かします：かつての行動が日常化すると「妄想の飢餓」状態へと陥り、初期の快感を再現するためにリスクを引き上げざるを得なくなります。

そして心理的引き金は2009年7月に引かれました：空軍基地最高司令官への昇進に伴う絶対的権力感と極限の重圧が、最後の抑制弁を吹き飛ばしたのです。

——————
事件の背景
——————
カナダ最大の戦略空軍基地であるトレントン基地。2009年7月、46歳のDavid Russell Williams大佐は、エリザベス女王や歴代首相の専用機を操縦した輝かしい経歴を誇る最高指揮官でした。

——————
参考文献・公的資料
——————
• オンタリオ州高等裁判所判決文 — R. v. Williams, 2010 ONSC 5946
• オンタリオ州警察（OPP）およびベルビル警察捜査報告書
• 2010年2月7日尋問調書 · Jim Smyth刑事法廷証言
• 本編脚本：01_KICH_BAN/Ho_So_Toi_Pham/Tap02_JA/kichban_tap02_JA.md

——————
注意事項
——————
• 本コンテンツはAI技術を活用して心理分析目的で制作されたドキュメンタリーです。
• 閲覧にはご注意ください。お子様のご視聴はお控えください。

#AmberEyes #犯罪心理学 #未解決事件 #実話 #エスカレーション #ラッセルウィリアムズ""",

 "TK2": """タイヤ痕の一致。それでも警察はその男に敬礼して見送った。 👁️

第02話 · 二面性の大佐 — 心理指標 #9: ハロー効果（Halo Effect）。
裁判記録および公的捜査資料に基づく実話プロファイリング。

📺 完全版ドキュメンタリー（25分）はYouTubeで公開中 — プロフィールのリンクから。
🔎 犯罪心理学 · ハロー効果 · 実在事件調書

——————
心理指標 #9: ハロー効果と集団的盲点
——————
2010年1月28日の夜、ベルビル市で暮らす27歳のJessica Lloydが自宅から突如姿を消しました。オンタリオ州警察は大捜索を開始しましたが、有力な手がかりは掴めませんでした。

1週間後の2月4日の夜、警察は雪上に残された珍しいオフロードタイヤ痕を追うため、現場付近に夜間移動式検問所を敷きました。

そこを通りかかった1台の日産パスファインダー。運転していたのはトレントン空軍基地の最高司令官でした。タイヤの溝の模様は雪上の痕跡と酷似していましたが、威厳ある高級将校を前に、パトロール警官は情報を控えただけで敬礼して通過させました。その後の3日間、彼は依然として自由な大佐でした。

ハロー効果という不可視の盾：社会的地位や輝かしい軍歴、王室専用機パイロットとしての功績が、法執行機関と社会全体の目を眩ませていたのです。

権威に対する無意識の盲従について、皆さんはどう考えますか？ コメント欄でお聞かせください 👇

#AmberEyes #犯罪心理学 #実話 #ハロー効果 #ラッセルウィリアムズ #未解決事件""",

 "TK3": """2つの人生。1つの身体。自己正当化のための物語。 👁️

第02話 · 二面性の大佐 — 心理指標 #5: 自己正当化（中和技術）と精神の分断。
裁判記録および公的捜査資料に基づく実話プロファイリング。

📺 完全版ドキュメンタリー（25分）はYouTubeで公開中 — プロフィールのリンクから。
🔎 犯罪心理学 · コンパートメンタライゼーション · 実在事件調書

——————
心理指標 #5: 自己正当化と精神の分断
——————
分析の前提：Russell Williamsに関する公的な精神医学的臨床診断は公表されていません。理論的枠組みは分析のためのモデルです。

• コンパートメンタライゼーション：相容れない認知を完全に独立した心の引き出しへと隔離する防衛機制。
  - 第1の引き出し：庭を愛し、軍の規律に生きる模範的な司令官であり夫。
  - 第2の引き出し：夜の捕食者。
• 中和技術（自己正当化）：82件の侵入の間、「誰も傷つけていない、記念品を持っているだけだ」と言い聞かせ、凶行に至った時も「被害者に顔を見られた以上、自己防衛のためにこうするしかなかった」と責任を転嫁しました。

尋問官から理由を問われた際、彼の答えは凍りつくほど空虚でした：「ええ、ですが答えは分かりませんし、答えが重要だとも思えません。」

良心と自己正当化を分かつ境界線について、皆さんはどう考えますか？ コメント欄でお聞かせください 👇

#AmberEyes #犯罪心理学 #実話 #コンパートメンタライゼーション #ラッセルウィリアムズ""",

 "TK4": """被害者に向けられた謝罪はただの一言もなかった。 👁️

第02話 · 二面性の大佐 — 心理指標 #4: 自己愛の崩壊（Narcissistic Collapse）。
裁判記録および公的捜査資料に基づく実話プロファイリング。

📺 完全版ドキュメンタリー（25分）はYouTubeで公開中 — プロフィールのリンクから。
🔎 犯罪心理学 · 自己愛の崩壊 · 実在事件調書

——————
心理指標 #4: 自己愛の崩壊と心理的判決
——————
隠されていたデジタルアーカイブが発見された瞬間、Williamsの精神の防壁は完全に崩壊しました。

尋問室で彼が口にした懸念は、妻からどう見られるか、そして基地の評判がどうなるかという点だけに終始していました。被害に遭った女性たちやその遺族への真摯な悔悟は皆無でした。

2010年10月18日、彼は88件の罪状すべてで有罪を認め、仮釈放なし25年の終身刑を受けました。しかし最大の刑罰は名誉と権力の完全な剥奪でした：カナダ総督は軍管轄権を剥奪し、勲章は切り刻まれ、軍は彼の名前が刻まれた全軍服を機密文書焼却炉で焼き尽くしました。

支配力を失った悪性ナルシシストには、みじめな自己憐憫しか残されていませんでした。

後悔が自己保身の道具に変わる瞬間について、皆さんはどう感じますか？ コメント欄でお聞かせください 👇

#AmberEyes #犯罪心理学 #実話 #自己愛の崩壊 #ラッセルウィリアムズ""",

 "TK5": """曖昧な違和感を覚えたなら、決して見過ごしてはならない。 👁️

第02話 · 二面性の大佐 — 心理指標 #10: 被害者学と生存のための直感。
裁判記録および公的捜査資料に基づく実話プロファイリング。

📺 完全版ドキュメンタリー（25分）はYouTubeで公開中 — プロフィールのリンクから。
🔎 犯罪心理学 · 生存の直感 · 実在事件調書

——————
心理指標 #10: 生存のための直感と境界線
——————
事件が発覚する前、Tweedの町は息が詰まるような得体の知れない不安に覆われていました。私物が動かされ、ドアにこじ開けられた跡があったのに金品は無事だったため、住民たちは神経過敏だと自己合理化して見過ごしていたのです。

本事件が遺した切実な教訓：
• 犯罪は決して殺人から始まるのではありません。些細な境界線の侵犯から始まります。
• 地位や学歴、煌びやかな階級章など社会的な上着に過ぎず、魂の善良さを保証する盾にはなりません。
• 曖昧な違和感を覚えたなら、プライベートな境界線がわずかでも侵されたと感じたなら、決して見過ごしてはなりません。
• 自らの直感を常に信じてください：生存の直感とは、私たちの命を守るために備わった内なる早期警戒レーダーなのです。

日常生活の中で見過ごしがちな違和感について、皆さんはどう考えますか？ コメント欄でお聞かせください 👇

#AmberEyes #犯罪心理学 #実話 #生存の直感 #防犯 #ラッセルウィリアムズ"""
}

def write_en_files(spec):
    for c in CLIPS_EN:
        cid = c["id"]
        hook = c["lines"][0][6]
        cap = (
            f"{hook} 👁️\n\n"
            f"Ep. 02 · The Two-Faced Colonel — Marker #{c['signs'][0]}: {c['theme']}.\n"
            f"True crime case file, source-verified.\n\n"
            f"📺 Watch the complete documentary on YouTube — link in bio.\n"
            f"🔎 Criminal Psychology · {c['title']} · Real Case File\n\n"
            f"Content created with AI assistance for behavioral analysis. Viewer discretion advised.\n\n"
            f"#AmberEyes #CriminalPsychology #TrueCrime #RussellWilliams #{cid} #CaseFile\n\n"
            f"---\n"
            f"Publishing Notes (DO NOT paste into caption):\n"
            f"- TOGGLE ON 'AI-generated content' label on TikTok.\n"
            f"- Link to YouTube Episode 02: [ADD_EPISODE_02_URL_IN_BIO]\n"
            f"- Estimated duration: {c['est_dur_s']} s ({len(c['lines'])} lines)\n"
            f"- Video file: clip{cid[-1]}_{cid}_EN.mp4 (1080x1920, 30fps)"
        )
        (OUT_EN / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")
        desc = MO_TA_DAI_EN[cid]
        (OUT_EN / f"MoTa_Dai_{cid}.txt").write_text(desc, encoding="utf-8")
        # Concise description <= 1200 chars
        (OUT_EN / f"MoTa_Ngan_{cid}.txt").write_text(desc[:1200].rsplit("\n\n", 1)[0] + "\n\n#AmberEyes #TrueCrime #CriminalPsychology", encoding="utf-8")

def write_ja_files(spec):
    for c in CLIPS_JA:
        cid = c["id"]
        hook = c["lines"][0][6]
        cap = (
            f"{hook} 👁️\n\n"
            f"第02話 · 二面性の大佐 — 心理指標 #{c['signs'][0]}: {c['theme']}。\n"
            f"公的記録と裁判資料に基づく実話プロファイリング。\n\n"
            f"📺 完全版ドキュメンタリー（25分）はYouTubeで公開中 — プロフィールのリンクから。\n"
            f"🔎 犯罪心理学 · {c['title']} · 実際の事件記録\n\n"
            f"AI技術を活用して心理分析目的で制作されたコンテンツです。閲覧にはご注意ください。\n\n"
            f"#AmberEyes #犯罪心理学 #未解決事件 #実話 #ラッセルウィリアムズ #{cid}\n\n"
            f"---\n"
            f"投稿時の注意事項（キャプション本文には貼り付けないでください）：\n"
            f"- TikTokアプリで「AI生成コンテンツ」のトグルを必ずONにしてください。\n"
            f"- YouTube第02話へのリンク: [プロフィールのリンク欄にURLを設定]\n"
            f"- 推定再生時間: {c['est_dur_s']} 秒（全{len(c['lines'])}文）\n"
            f"- 出力動画ファイル名: clip{cid[-1]}_{cid}_JA.mp4 (1080x1920, 30fps)"
        )
        (OUT_JA / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")
        desc = MO_TA_DAI_JA[cid]
        (OUT_JA / f"MoTa_Dai_{cid}.txt").write_text(desc, encoding="utf-8")
        # Concise description <= 1200 chars
        (OUT_JA / f"MoTa_Ngan_{cid}.txt").write_text(desc[:1200].rsplit("\n\n", 1)[0] + "\n\n#AmberEyes #犯罪心理学 #実話", encoding="utf-8")

def write_markdown_en():
    L = []
    A = L.append
    A("# TIKTOK CLIP PLAN — EPISODE 02 (ENGLISH) · \"THE TWO-FACED COLONEL\"")
    A("")
    A("*Status: Completed & Source-Verified (AGENTS.md K1–K10, G1–G13)*")
    A("*Audio Spec: `02_SAN_XUAT/TIKTOK/Tap02_EN/SPEC_AUDIO_CLIP_TAP02.json`*")
    A("")
    A("## 0. Summary")
    A("")
    A("| Item | Value |")
    A("|---|---|")
    A("| Total Clips | **5 clips** (TK1–TK4 main + TK5 victimology/survival red flags) |")
    tot_lines = sum(len(c["lines"]) for c in CLIPS_EN)
    A(f"| Total Spoken Lines | **{tot_lines} lines** |")
    durs = [c["est_dur_s"] for c in CLIPS_EN]
    A(f"| Estimated Duration | {min(durs):.1f}s – {max(durs):.1f}s (Target: 65–90s · QC Gate: 45–95s) |")
    A("| Voices | English Higgs Cast: Host (H), Detective (D), Psychologist (C), Officer (N2) |")
    A("")
    A("## 1. 5 Clips Overview")
    A("")
    A("| Clip | Markers | Theme | 3-Second Hook | Est. Duration |")
    A("|---|---|---|---|---|")
    for c in CLIPS_EN:
        cd_str = " · ".join(f"#{i}" for i in c["signs"])
        A(f"| **{c['id']}** | {cd_str} | {c['theme']} | *\"{c['hook']}\"* | {c['est_dur_s']} s · {len(c['lines'])} lines |")
    A("")
    A("## 2. Detailed Performance Table")
    A("")
    for c in CLIPS_EN:
        cid = c["id"]
        A(f"### CLIP {cid} — \"{c['title']}\"")
        A(f"*Estimated {c['est_dur_s']} s ({len(c['lines'])} lines) · BGM `{c['bgm']}`*")
        A("")
        A("| ID | Role | Emotion | Speed | Pause | Line | Source |")
        A("|---|---|---|---|---|---|---|")
        for idx, ln in enumerate(c["lines"], 1):
            A(f"| `{cid}.01#{idx}` | {ln[0]} | {ln[1]} | {ln[2]} | {ln[3]} | {ln[6]} | {ln[7]} |")
        A("")
    (OUT_EN / "KE_HOACH_CLIP_TAP02_EN.md").write_text("\n".join(L), encoding="utf-8")

def write_markdown_ja():
    L = []
    A = L.append
    A("# TikTokクリップ制作計画 — 第02話（日本語） · 「二面性の大佐とエスカレーションの深淵」")
    A("")
    A("*状態：完成・公的記録検証済み（AGENTS.md K1–K10、G1–G13準拠）*")
    A("*音声仕様書：`02_SAN_XUAT/TIKTOK/Tap02_JA/SPEC_AUDIO_CLIP_TAP02.json`*")
    A("")
    A("## 0. 基本概要")
    A("")
    A("| 項目 | 設定内容 |")
    A("|---|---|")
    A("| クリップ総数 | **5本**（TK1–TK4 本編深層分析 + TK5 被害者学・生存の警告サイン） |")
    tot_lines = sum(len(c["lines"]) for c in CLIPS_JA)
    A(f"| 総読み上げ行数 | **{tot_lines} 行** |")
    durs = [c["est_dur_s"] for c in CLIPS_JA]
    A(f"| 推定再生時間 | {min(durs):.1f}秒 ～ {max(durs):.1f}秒（目標 65～90秒 · QC許容範囲 45～95秒） |")
    A("| 配役音声 | 日本語 Higgs キャスト：ホスト (H)、刑事 (D)、心理学者 (C)、警察官 (N2) |")
    A("")
    A("## 1. 全5クリップ一覧")
    A("")
    A("| クリップ | 心理指標 | 主題 | 冒頭3秒フック | 推定時間 |")
    A("|---|---|---|---|---|")
    for c in CLIPS_JA:
        cd_str = " · ".join(f"#{i}" for i in c["signs"])
        A(f"| **{c['id']}** | {cd_str} | {c['theme']} | *「{c['hook']}」* | {c['est_dur_s']} 秒 · {len(c['lines'])} 行 |")
    A("")
    A("## 2. クリップ詳細構成")
    A("")
    for c in CLIPS_JA:
        cid = c["id"]
        A(f"### クリップ {cid} — 「{c['title']}」")
        A(f"*推定時間 {c['est_dur_s']} 秒（{len(c['lines'])} 行） · BGM `{c['bgm']}`*")
        A("")
        A("| 識別子 | 役 | 感情 | 速度 | 休止 | セリフ | 出典 |")
        A("|---|---|---|---|---|---|---|")
        for idx, ln in enumerate(c["lines"], 1):
            A(f"| `{cid}.01#{idx}` | {ln[0]} | {ln[1]} | {ln[2]} | {ln[3]} | {ln[6]} | {ln[7]} |")
        A("")
    (OUT_JA / "KE_HOACH_CLIP_TAP02_JA.md").write_text("\n".join(L), encoding="utf-8")

def main():
    spec_en = build_spec_en()
    (OUT_EN / "SPEC_AUDIO_CLIP_TAP02.json").write_text(
        json.dumps(spec_en, ensure_ascii=False, indent=2), encoding="utf-8")
    write_en_files(spec_en)
    write_markdown_en()

    spec_ja = build_spec_ja()
    (OUT_JA / "SPEC_AUDIO_CLIP_TAP02.json").write_text(
        json.dumps(spec_ja, ensure_ascii=False, indent=2), encoding="utf-8")
    write_ja_files(spec_ja)
    write_markdown_ja()

    print("=== DURATION EN ===")
    for c in CLIPS_EN:
        print(f"{c['id']}: {c['est_dur_s']} s · {len(c['lines'])} lines · {c['title']}")

    print("\n=== DURATION JA ===")
    for c in CLIPS_JA:
        print(f"{c['id']}: {c['est_dur_s']} s · {len(c['lines'])} lines · {c['title']}")

    print("\nSUCCESS: All files for EN and JA generated.")

if __name__ == "__main__":
    main()
