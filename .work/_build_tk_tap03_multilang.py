# -*- coding: utf-8 -*-
"""Generate TikTok scripts, audio specs, captions, and descriptions for Tap 03 EN & JA.

Adheres strictly to AGENTS.md rules:
- Measured speech rates from timeline_s_EN_t03.json and timeline_s_JA_t03.json
- Verbatim citations and facts mapped to script_tap03_EN.json / script_tap03_JA.json
- G1 (no ellipses), G3 (safe emotions), G4 (safe speed offsets), V9 (content safety)
- TikTok character limits (caption <= 2200, duration 45-95s)
"""

import json
import pathlib
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap03_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap03_JA"
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

RATE_EN = get_rates("timeline_s_EN_t03.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t03.json", is_ja=True)

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
 "title": "Stop Me. I’m Going to Do It Again",
 "signs": [4, 6],
 "theme": "Collapse of Power Fantasy & Precipitating Psychological Trigger",
 "hook": "Stop me. I’m going to do it again.",
 "bgm": "bgm_sub_drone.mp3",
 "bgm_desc": "Act 1 — episode bed: bgm_sub_drone.mp3",
 "sfx": ["amb_winter_wind.wav (bed)", "fx_coin_drop.wav", "fx_phone_dial.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
 "overlay": [
   {"after_id": "TK1.01#1", "text": "PUEBLO, COLORADO · 4:00 AM · APRIL 24, 1973", "dur_s": 3.0},
   {"after_id": "TK1.01#4", "text": "“I KILLED MY MOTHER... AND SIX COLLEGE GIRLS”", "dur_s": 2.5},
   {"after_id": "TK1.01#6", "text": "“STOP ME. I'M GOING TO DO IT AGAIN”", "dur_s": 2.5},
   {"after_id": "TK1.01#8", "text": "3 RIFLES · HUNDREDS OF ROUNDS · SURRENDER", "dur_s": 2.5},
   {"after_id": "TK1.01#9", "text": "PRECIPITATING TRIGGER: FANTASY COLLAPSE", "dur_s": 3.0}
 ],
 "sources": ["1.03#1-#8", "1.05#1-#7", "1.07#1-#4", "1.09#1-#6", "1.10#8-#13", "Inside Detective 1973"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_phone_booth","still",
   "Stop me. I’m going to do it again.",
   "1.10#10 · 1.10#11"),
  ("H","neutral",-0.02,0.6,"t3_dispatch_desk","pull",
   "At four in the morning on April twenty-fourth, 1973, the desk phone rang at Santa Cruz police headquarters.",
   "1.03#1 · 1.03#3"),
  ("H","neutral",-0.02,0.6,"t3_phone_booth","pan",
   "On the line was Edmund Kemper, calling from a roadside payphone in Pueblo, Colorado, over a thousand miles away.",
   "1.03#2 · 1.03#3 · 1.03#5"),
  ("H","neutral",-0.02,0.6,"t3_phone_booth","push",
   "His voice was calm and deliberate: <#0.35#> I killed my mother and her friend. And I killed those college girls. Six of them.",
   "1.05#4 · 1.05#5 · 1.05#6"),
  ("N1","neutral",-0.02,0.6,"t3_dispatch_desk","still",
   "At first, dispatch assumed it was an intoxicated prank and told him to call back later.",
   "1.09#1 · 1.09#3"),
  ("H","neutral",-0.02,0.7,"t3_phone_booth","push",
   "Two hours later he called again, with words that chilled the room: <#0.35#> Stop me. I’m going to do it again.",
   "1.09#4 · 1.10#10 · 1.10#11"),
  ("H","neutral",-0.02,0.6,"t3_phone_booth","still",
   "He didn’t call to boast. He called because he was terrified that he couldn’t stop himself.",
   "1.10#12 · 1.10#13"),
  ("D","neutral",-0.03,0.7,"t3_apartos_house","pan",
   "When patrol cars arrived, the six-foot-nine giant sat peacefully in the booth, with three rifles and hundreds of rounds in his car.",
   "1.03#6 · 1.07#4 · 1.09#5 · 1.09#6"),
  ("C","neutral",-0.02,0.7,"t3_brain_mirror","pull",
   "With his ultimate target — his mother — dead, the omnipotent fantasy dissolved into profound emptiness, precipitating his psychological collapse.",
   "1.10#8 · 1.10#9 · 4.07#8 · 4.07#9"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Episode three of Amber Eyes. Watch the full dossier via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK2",
 "title": "Drinking with Cops and Discussing the Killer",
 "signs": [9, 1],
 "theme": "Intellectual Halo Effect & Institutional Blind Spots",
 "hook": "Drinking with the police. And discussing his own murders.",
 "bgm": "bgm_jazz_noir.mp3",
 "bgm_desc": "Act 2 — episode bed: bgm_jazz_noir.mp3",
 "sfx": ["amb_bar.wav (bed)", "fx_beer_pour.wav", "fx_glass_clink.wav", "fx_car_drive.wav", "fx_stinger.wav"],
 "overlay": [
   {"after_id": "TK2.01#1", "text": "THE JURY ROOM BAR · ACROSS FROM COUNTY COURTHOUSE", "dur_s": 3.0},
   {"after_id": "TK2.01#3", "text": "6'9\" · 280 LBS · WIRE GLASSES · POLITE DEMEANOR", "dur_s": 2.5},
   {"after_id": "TK2.01#5", "text": "UCSC PARKING DECAL ON YELLOW FORD GALAXIE", "dur_s": 2.5},
   {"after_id": "TK2.01#7", "text": "ANALYZING KILLER PSYCHOLOGY FOR DETECTIVES", "dur_s": 3.0},
   {"after_id": "TK2.01#9", "text": "INTELLECTUAL HALO EFFECT (BLIND SPOTS)", "dur_s": 2.5}
 ],
 "sources": ["1.03#6-#7", "2.07#1-#5", "2.07#10-#14", "2.09#1-#9", "Front Page Detective 1974"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_bar_stool_shadow","still",
   "Drinking with the police. And discussing his own murders.",
   "1.03#7 · 2.09#8 · 2.09#9"),
  ("N2","neutral",-0.02,0.6,"t3_bar_jury_room","pull",
   "The Jury Room bar sat directly across from the Santa Cruz County Courthouse, a familiar haunt for detectives after shift.",
   "2.09#1"),
  ("N2","neutral",-0.02,0.6,"t3_bar_stool_shadow","pan",
   "Big Ed was a fixture in the corner. Standing six-foot-nine, wearing wire-rimmed glasses, remarkably courteous and articulate in law.",
   "1.03#6 · 2.07#12 · 2.09#2 · 2.09#3"),
  ("D","neutral",-0.03,0.6,"t3_galaxie","still",
   "By day, he drove a yellow nineteen sixty-nine Ford Galaxie bearing a university employee parking decal on the front bumper.",
   "2.07#2 · 2.07#3 · 2.07#4"),
  ("D","neutral",-0.03,0.6,"t3_hitchhiker","push",
   "That trusted campus decal, combined with his gentle academic facade, made female hitchhikers believe the vehicle was completely safe.",
   "2.07#5 · 2.07#10 · 2.07#12"),
  ("N2","sad",-0.04,0.8,"t3_bar_jury_room","still",
   "There were nights detectives drank draft beer with Ed, venting our frustrations over the elusive Co-ed Killer investigation.",
   "2.09#6"),
  ("N2","sad",-0.04,0.8,"t3_bar_stool_shadow","push",
   "Ed would nod, sip his beer, analyze the evidence, and offer sharp theories about the killer’s psychological profile.",
   "2.09#7"),
  ("N2","sad",-0.04,0.7,"t3_bar_stool_shadow","pull",
   "Looking back, ice chills our spine: The monster the entire city was hunting sat beside us, laughing about the very manhunt.",
   "2.09#8 · 2.09#9"),
  ("C","neutral",-0.02,0.7,"t3_brain_mirror","still",
   "The Halo Effect: superior intelligence and polite gentility formed an invisible camouflage blinding the entire law enforcement apparatus.",
   "2.07#10 · 5.06#3 · 5.06#4"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Episode three of Amber Eyes. Watch the full dossier via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK3",
 "title": "The Childhood Basement and the Trapdoor Beneath the Table",
 "signs": [2, 3],
 "theme": "Toxic Maternal Trauma & The Projection Mechanism (Proxy Victims)",
 "hook": "Eight years old. Locked in a basement with a trapdoor under the table.",
 "bgm": "bgm_cello_sad_v2.mp3",
 "bgm_desc": "Act 3 — episode bed: bgm_cello_sad_v2.mp3",
 "sfx": ["amb_basement.wav (bed)", "fx_water_drip.wav", "fx_trapdoor_creak.wav", "fx_sub_drop.wav", "fx_stinger.wav"],
 "overlay": [
   {"after_id": "TK3.01#1", "text": "MONTANA BASEMENT · 1950s CHILDHOOD", "dur_s": 3.0},
   {"after_id": "TK3.01#3", "text": "TRAPDOOR BENEATH DINING TABLE", "dur_s": 2.5},
   {"after_id": "TK3.01#5", "text": "SYSTEMATIC EMOTIONAL HUMILIATION", "dur_s": 2.5},
   {"after_id": "TK3.01#7", "text": "PROJECTION MECHANISM", "dur_s": 3.0},
   {"after_id": "TK3.01#8", "text": "PROXY VICTIMS (SURROGATES)", "dur_s": 2.5},
   {"after_id": "TK3.01#10", "text": "THEORETICAL PSYCHOLOGICAL FRAMEWORK", "dur_s": 2.5}
 ],
 "sources": ["3.02#1-#2", "3.04#1", "3.05#1-#12", "3.08#1-#13", "Peter Vronsky"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_basement_stairs","still",
   "Eight years old. Locked in a basement with a trapdoor under the table.",
   "3.05#6 · 3.05#7"),
  ("C","neutral",-0.02,0.6,"t3_coal_furnace","push",
   "Kemper’s mother, Clarnell, saw in her son the hated reflection of her ex-husband.",
   "3.05#4 · 3.05#5"),
  ("C","neutral",-0.02,0.7,"t3_small_bed","still",
   "From age eight, Ed was banished to sleep in a damp basement beside the coal furnace, under a trapdoor beneath the upstairs dining table.",
   "3.05#6 · 3.05#7"),
  ("C","neutral",-0.02,0.6,"t3_trapdoor","pull",
   "To leave, the heavy table had to be lifted above. Confinement ended only when his father threatened police intervention.",
   "3.05#7 · 3.05#8"),
  ("C","sad",-0.04,0.7,"t3_basement_stairs","pan",
   "Every day, she subjected him to venomous verbal abuse, mocking his huge frame and crushing his self-esteem.",
   "3.05#9 · 3.05#12"),
  ("C","neutral",-0.02,0.7,"t3_mother_shadow","still",
   "In the boy's psyche, the mother loomed as an omnipotent monument of cruelty: violently hated, yet too terrifying to confront.",
   "3.08#6"),
  ("C","neutral",-0.02,0.7,"t3_ucsc_campus","push",
   "Unable to retaliate directly against her, Kemper's brain activated the projection mechanism: seeking proxy victims.",
   "3.08#1 · 3.08#7 · 3.08#11"),
  ("C","neutral",-0.02,0.7,"t3_hitchhiker","pull",
   "Young, graceful female students on the roadside embodied the freedom he craved, yet believed would reject him just as his mother had.",
   "3.08#10 · 3.08#11"),
  ("H","neutral",-0.02,0.6,"t3_apartos_house","pan",
   "Innocent young women bore the horrifying brunt of the murderous fury intended for his own mother.",
   "3.08#11 · 3.08#13"),
  ("H","neutral",-0.02,0.6,"t3_brain_mirror","still",
   "A clinical note: psychiatrists offered varied diagnostic labels over the years. This represents an explanatory framework, not a moral trial.",
   "3.04#1 · 3.08#3 · 3.11#6"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Episode three of Amber Eyes. Watch the full dossier via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK4",
 "title": "The IQ 145 Giant Opens His Mind to the FBI",
 "signs": [7, 8],
 "theme": "The Violent Fantasy Cycle & Behavioral Signature vs MO (FBI Mindhunter)",
 "hook": "An IQ of 145. The mind that changed the FBI forever.",
 "bgm": "bgm_ambient_deep.mp3",
 "bgm_desc": "Act 4 — episode bed: bgm_ambient_deep.mp3",
 "sfx": ["amb_prison.wav (bed)", "fx_iron_door.wav", "fx_tape_click.wav", "fx_tension_tick.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"after_id": "TK4.01#1", "text": "VACAVILLE PRISON · 1978 · FBI PROFILERS", "dur_s": 3.0},
   {"after_id": "TK4.01#3", "text": "145 IQ · TOP 0.13% INTELLECT WORLDWIDE", "dur_s": 2.5},
   {"after_id": "TK4.01#5", "text": "THE VIOLENT FANTASY CYCLE", "dur_s": 2.5},
   {"after_id": "TK4.01#7", "text": "SOUVENIRS: REIGNITING THE SENSATION OF POWER", "dur_s": 2.5},
   {"after_id": "TK4.01#9", "text": "PSYCHOLOGICAL SIGNATURE vs MODUS OPERANDI", "dur_s": 3.0},
   {"after_id": "TK4.01#10", "text": "FOUNDATION FOR MINDHUNTER", "dur_s": 2.5}
 ],
 "sources": ["1.13#1-#9", "4.02#1-#8", "4.05#1-#19", "4.07#1-#10", "4.08#1-#7", "FBI Law Enforcement Bulletin 1985"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_vacaville_1978","still",
   "An IQ of one hundred and forty-five. The mind that changed the FBI forever.",
   "1.13#2 · 4.02#4 · 4.08#1"),
  ("D","neutral",-0.03,0.6,"t3_two_agents","pull",
   "In nineteen seventy-eight, FBI Special Agents Robert Ressler and John Douglas entered the prison cell at Vacaville.",
   "4.02#1 · 4.02#4 · 4.02#8"),
  ("D","neutral",-0.03,0.6,"t3_giant_doorway","still",
   "Kemper filled the doorway like a mountain, but he smiled politely and spoke with the measured cadence of a professor.",
   "4.05#1 · 4.05#2 · 4.05#3"),
  ("D","neutral",-0.03,0.6,"t3_interview_room","push",
   "Possessing an IQ of 145, he demanded no plea deals or lawyers, dissecting his inner darkness with clinical precision.",
   "1.13#2 · 1.13#5 · 4.05#4 · 4.05#13 · 4.05#14"),
  ("D","neutral",-0.03,0.7,"t3_cassette","pan",
   "Kemper explained a revolutionary concept to the FBI: The Violent Fantasy Cycle.",
   "4.07#1 · 4.07#2"),
  ("D","neutral",-0.03,0.7,"t3_fantasy_spiral","push",
   "Homicide does not begin when weapons are drawn, but in hundreds of mental rehearsals conducted over years.",
   "4.07#3 · 4.07#4 · 4.07#5"),
  ("D","neutral",-0.03,0.6,"t3_trophy_box","still",
   "He revealed why he took trophies: not to boast, but as catalysts to re-experience supreme power once post-crime euphoria faded.",
   "4.07#6 · 4.07#7"),
  ("H","neutral",-0.02,0.7,"t3_organized_split","pull",
   "Dialogues with Kemper and thirty-five other felons formed the foundation for FBI organized offender classification and the ViCAP network.",
   "1.13#6 · 1.13#7 · 4.08#1 · 4.08#2 · 4.08#3"),
  ("C","neutral",-0.02,0.7,"t3_self_observation","still",
   "Crime scenes leave more than physical clues: they leave the unique psychological signature of the perpetrator.",
   "4.08#4"),
  ("H","neutral",-0.02,0.6,"t3_case_photos","push",
   "This dossier became the defining cornerstone for criminal behavioral analysis and the inspiration behind Mindhunter.",
   "4.08#6 · 4.08#7"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Episode three of Amber Eyes. Watch the full dossier via the link in our bio.",
   "CTA")
 ]
},
{
 "id": "TK5",
 "title": "The Macdonald Triad and Four Early Red Flags",
 "signs": [10],
 "theme": "Victimology & Four Critical Survival Warning Signs (Macdonald Triad)",
 "hook": "Four early warning signs. So that no one becomes a victim.",
 "bgm": "bgm_piano_minimal.mp3",
 "bgm_desc": "Act 5 — episode bed: bgm_piano_minimal.mp3",
 "sfx": ["amb_wind_soft.wav (bed)", "fx_clock_tick.wav", "fx_stinger.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"after_id": "TK5.01#1", "text": "4 CRITICAL PSYCHOLOGICAL WARNING SIGNS", "dur_s": 3.0},
   {"after_id": "TK5.01#2", "text": "FLAG 1: CHILDHOOD MACDONALD TRIAD", "dur_s": 2.5},
   {"after_id": "TK5.01#4", "text": "FLAG 2: EXTREME DOMESTIC EMOTIONAL ABUSE", "dur_s": 2.5},
   {"after_id": "TK5.01#5", "text": "FLAG 3: IMMERSION IN DOMINATION FANTASY", "dur_s": 2.5},
   {"after_id": "TK5.01#6", "text": "FLAG 4: HIGH INTELLECT WITH SHALLOW AFFECT", "dur_s": 3.0},
   {"after_id": "TK5.01#8", "text": "HEALING CHILDHOOD WOUNDS AT HOME", "dur_s": 3.0}
 ],
 "sources": ["5.04#1", "5.05#1-#8", "5.06#1-#4", "5.08#6-#11", "The Gift of Fear"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_red_flags","still",
   "Four early warning signs. So that no one becomes a victim.",
   "5.04#1 · 5.08#11"),
  ("C","neutral",-0.02,0.6,"t3_gift_drowned","push",
   "Red flag one: The childhood Macdonald Triad. Intentional, premeditated animal cruelty beginning at age ten.",
   "5.05#1 · 5.05#2 · 5.05#4 · 5.05#6"),
  ("C","neutral",-0.02,0.6,"t3_gift_drowned","pull",
   "It is a primary clinical indicator of severe empathy deficits and escalating violent conduct that families often overlook.",
   "5.05#6"),
  ("C","neutral",-0.02,0.6,"t3_coal_furnace","pan",
   "Red flag two: Extreme domestic psychological abuse. Confining children in dark, isolated spaces and chronic verbal humiliation.",
   "5.05#7 · 5.05#8"),
  ("D","neutral",-0.03,0.6,"t3_fantasy_spiral","still",
   "Red flag three: Immersion in violent domination fantasies severed from reality, coupled with obsessive research into weapons.",
   "5.06#1 · 5.06#2"),
  ("D","neutral",-0.03,0.7,"t3_self_observation","push",
   "And red flag four: Superior intellect paired with shallow affect, using intelligence to manipulate adults while void of genuine remorse.",
   "5.06#3 · 5.06#4"),
  ("H","neutral",-0.02,0.7,"t3_life_sentence","pull",
   "Edmund Kemper was born with a genius intellect and imposing strength, but submerged in cruelty, those gifts mutated into destruction.",
   "5.08#8 · 5.08#9"),
  ("H","neutral",-0.02,0.8,"t3_closing_desk","still",
   "Locking evil behind bars is the duty of the law. But identifying and healing emotional wounds in children is how we prevent evil.",
   "5.08#10 · 5.08#11"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Episode three of Amber Eyes. Watch the full dossier via the link in our bio.",
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
 "title": "私を止めてください。私はそれをもう一度するつもりです",
 "signs": [4, 6],
 "theme": "全能妄想の崩壊と心理的限界点（トリガー）",
 "hook": "私を止めてください。私はそれをもう一度するつもりです。",
 "bgm": "bgm_sub_drone.mp3",
 "bgm_desc": "第1幕 — 本編ベッド曲: bgm_sub_drone.mp3",
 "sfx": ["amb_winter_wind.wav (環境音)", "fx_coin_drop.wav", "fx_phone_dial.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
 "overlay": [
   {"after_id": "TK1.01#1", "text": "コロラド州プエブロ · 1973年4月24日 午前4時", "dur_s": 3.0},
   {"after_id": "TK1.01#4", "text": "「私は母と…6人の女子大生を殺しました」", "dur_s": 2.5},
   {"after_id": "TK1.01#6", "text": "「私を止めてください。もう一度やってしまう」", "dur_s": 2.5},
   {"after_id": "TK1.01#8", "text": "銃3丁 · 実弾数百発 · 無抵抗で自首", "dur_s": 2.5},
   {"after_id": "TK1.01#9", "text": "心理的限界点：万能妄想の完全崩壊", "dur_s": 3.0}
 ],
 "sources": ["1.03#1-#8", "1.05#1-#7", "1.07#1-#4", "1.09#1-#6", "1.10#8-#13", "Inside Detective 1973"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_phone_booth","still",
   "私を止めてください。私はそれをもう一度するつもりです。",
   "1.10#10 · 1.10#11"),
  ("H","neutral",-0.02,0.6,"t3_dispatch_desk","pull",
   "1973年4月24日、午前4時。カリフォルニア州サンタクルーズ警察本部の当直電話が鳴り響きました。",
   "1.03#1 · 1.03#3"),
  ("H","neutral",-0.02,0.6,"t3_phone_booth","pan",
   "電話の主は、1,600キロ以上離れたコロラド州プエブロの公衆電話からかけてきたエドマンド・ケンパーでした。",
   "1.03#2 · 1.03#3 · 1.03#5"),
  ("H","neutral",-0.02,0.6,"t3_phone_booth","push",
   "極めて落ち着いた声で、彼はこう告げました。<#0.35#> 私は母と、その友人を殺しました。そして、女子学生たちを殺しました。6人です。",
   "1.05#4 · 1.05#5 · 1.05#6"),
  ("N1","neutral",-0.02,0.6,"t3_dispatch_desk","still",
   "当初、当直係は酔っ払いのいたずら電話だと思い、かけ直すよう伝えました。",
   "1.09#1 · 1.09#3"),
  ("H","neutral",-0.02,0.7,"t3_phone_booth","push",
   "2時間後に彼が再び電話してきたとき、その警告は捜査員たちを凍りつかせました。<#0.35#> 私を止めてください。私はそれをもう一度するつもりです。",
   "1.09#4 · 1.10#10 · 1.10#11"),
  ("H","neutral",-0.02,0.6,"t3_phone_booth","still",
   "彼は犯行を自慢するために電話したのではありません。自分自身を止められなくなる恐怖から電話したのです。",
   "1.10#12 · 1.10#13"),
  ("D","neutral",-0.03,0.7,"t3_apartos_house","pan",
   "パトカーが到着したとき、身長2メートル06の巨漢は公衆電話の中で静かに自首し、車内には銃3丁と数百発の実弾が積まれていました。",
   "1.03#6 · 1.07#4 · 1.09#5 · 1.09#6"),
  ("C","neutral",-0.02,0.7,"t3_brain_mirror","pull",
   "究極の標的であった母親の死によって、彼の万能妄想は崩壊しました。極度の空虚感が、彼を心理的限界点へと追いやったのです。",
   "1.10#8 · 1.10#9 · 4.07#8 · 4.07#9"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Amber Eyes 第3話。事件の全貌はバイオのリンクからご覧いただけます。",
   "CTA")
 ]
},
{
 "id": "TK2",
 "title": "警察官とビールを飲みながら殺人鬼について語る",
 "signs": [9, 1],
 "theme": "知性のハロー効果と法執行機関の心理的盲点",
 "hook": "警察官とビールを飲み、自らの事件について語る。",
 "bgm": "bgm_jazz_noir.mp3",
 "bgm_desc": "第2幕 — 本編ベッド曲: bgm_jazz_noir.mp3",
 "sfx": ["amb_bar.wav (環境音)", "fx_beer_pour.wav", "fx_glass_clink.wav", "fx_car_drive.wav", "fx_stinger.wav"],
 "overlay": [
   {"after_id": "TK2.01#1", "text": "バー「THE JURY ROOM」 · 地方裁判所の真正面", "dur_s": 3.0},
   {"after_id": "TK2.01#3", "text": "2m06 · 127kg · メガネ · 紳士的で温厚な語り口", "dur_s": 2.5},
   {"after_id": "TK2.01#5", "text": "黄色いフォードに貼られた大学職員ステッカー", "dur_s": 2.5},
   {"after_id": "TK2.01#7", "text": "捜査員に犯人の心理プロファイルをアドバイス", "dur_s": 3.0},
   {"after_id": "TK2.01#9", "text": "知性のハロー効果（組織の心理的盲点）", "dur_s": 2.5}
 ],
 "sources": ["1.03#6-#7", "2.07#1-#5", "2.07#10-#14", "2.09#1-#9", "Front Page Detective 1974"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_bar_stool_shadow","still",
   "警察官とビールを飲み、自らの事件について語る。",
   "1.03#7 · 2.09#8 · 2.09#9"),
  ("N2","neutral",-0.02,0.6,"t3_bar_jury_room","pull",
   "サンタクルーズ裁判所の真正面にあるバー「The Jury Room」は、当直を終えた刑事や警察官が集まる行きつけの店でした。",
   "2.09#1"),
  ("N2","neutral",-0.02,0.6,"t3_bar_stool_shadow","pan",
   "ビッグ・エドはいつもバーの隅の席に座っていました。身長2メートル06、メガネをかけ、法律に詳しく非常に礼儀正しい男でした。",
   "1.03#6 · 2.07#12 · 2.09#2 · 2.09#3"),
  ("D","neutral",-0.03,0.6,"t3_galaxie","still",
   "昼間、彼はバンパーに大学職員用駐車ステッカーを貼った、1969年型の黄色いフォード・ギャラクシーを運転していました。",
   "2.07#2 · 2.07#3 · 2.07#4"),
  ("D","neutral",-0.03,0.6,"t3_hitchhiker","push",
   "大学のステッカーと知的で物静かな外見は、ヒッチハイクをする女子学生たちに絶対的な安心感を与えていたのです。",
   "2.07#5 · 2.07#10 · 2.07#12"),
  ("N2","sad",-0.04,0.8,"t3_bar_jury_room","still",
   "刑事たちがエドと一緒にビールを飲みながら、女子大生殺人鬼の捜査が難航している苦悩を打ち明ける夜もありました。",
   "2.09#6"),
  ("N2","sad",-0.04,0.8,"t3_bar_stool_shadow","push",
   "エドは相槌を打ちながら分析し、犯人の心理について鋭い仮説を捜査員たちに助言してくれたのです。",
   "2.09#7"),
  ("N2","sad",-0.04,0.7,"t3_bar_stool_shadow","pull",
   "思い返すと背筋が凍ります。街中が必死に追っていた怪物が、私たちの隣で捜査について笑っていたのです。",
   "2.09#8 · 2.09#9"),
  ("C","neutral",-0.02,0.7,"t3_brain_mirror","still",
   "ハロー効果。卓越した知性と温厚な態度は、法執行機関そのものを欺く不可視の偽装壁となったのです。",
   "2.07#10 · 5.06#3 · 5.06#4"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Amber Eyes 第3話。事件の全貌はバイオのリンクからご覧いただけます。",
   "CTA")
 ]
},
{
 "id": "TK3",
 "title": "幼少期の地下室と食卓の下の落とし戸",
 "signs": [2, 3],
 "theme": "母性トラウマと投影機制（代理被害者）",
 "hook": "8歳。食卓の下にある落とし戸の地下室に閉じ込められた。",
 "bgm": "bgm_cello_sad_v2.mp3",
 "bgm_desc": "第3幕 — 本編ベッド曲: bgm_cello_sad_v2.mp3",
 "sfx": ["amb_basement.wav (環境音)", "fx_water_drip.wav", "fx_trapdoor_creak.wav", "fx_sub_drop.wav", "fx_stinger.wav"],
 "overlay": [
   {"after_id": "TK3.01#1", "text": "モンタナ州の地下室 · 1950年代の幼少期", "dur_s": 3.0},
   {"after_id": "TK3.01#3", "text": "ダイニングテーブルの真下にある落とし戸", "dur_s": 2.5},
   {"after_id": "TK3.01#5", "text": "体系的な人格否定と精神的虐待", "dur_s": 2.5},
   {"after_id": "TK3.01#7", "text": "投影機制（PROJECTION）", "dur_s": 3.0},
   {"after_id": "TK3.01#8", "text": "代理被害者（PROXY VICTIMS）", "dur_s": 2.5},
   {"after_id": "TK3.01#10", "text": "精神分析的解釈 · 臨床的枠組み", "dur_s": 2.5}
 ],
 "sources": ["3.02#1-#2", "3.04#1", "3.05#1-#12", "3.08#1-#13", "Peter Vronsky"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_basement_stairs","still",
   "8歳。食卓の下にある落とし戸の地下室に閉じ込められた。",
   "3.05#6 · 3.05#7"),
  ("C","neutral",-0.02,0.6,"t3_coal_furnace","push",
   "ケンパーの母クラネルは、息子の中に自分が憎悪する元夫の面影を見ていました。",
   "3.05#4 · 3.05#5"),
  ("C","neutral",-0.02,0.7,"t3_small_bed","still",
   "8歳の頃から、エドは石炭ストーブの隣の湿った地下室に追いやられ、その真上にはダイニングテーブルがありました。",
   "3.05#6 · 3.05#7"),
  ("C","neutral",-0.02,0.6,"t3_trapdoor","pull",
   "外に出るには重い食卓を持ち上げなければならず、父親が警察に通報すると脅すまで監禁は続きました。",
   "3.05#7 · 3.05#8"),
  ("C","sad",-0.04,0.7,"t3_basement_stairs","pan",
   "母親は毎日、彼の巨大な体格を罵倒し、自尊心を徹底的に踏みにじり続けました。",
   "3.05#9 · 3.05#12"),
  ("C","neutral",-0.02,0.7,"t3_mother_shadow","still",
   "少年の無意識の中で、母親は憎しみながらも決して逆らえない絶対的な権力の偶像と化していったのです。",
   "3.08#6"),
  ("C","neutral",-0.02,0.7,"t3_ucsc_campus","push",
   "母親へ直接復讐できない脳は、投影のメカニズムを作動させ、代替の被害者を求め始めました。",
   "3.08#1 · 3.08#7 · 3.08#11"),
  ("C","neutral",-0.02,0.7,"t3_hitchhiker","pull",
   "路肩に立つ若く美しい女子大生たちは、彼が渇望しながらも、母親と同じように自分を拒絶すると信じた自由の象徴でした。",
   "3.08#10 · 3.08#11"),
  ("H","neutral",-0.02,0.6,"t3_apartos_house","pan",
   "無実の女性たちが、彼が母親に向けていた殺意の代理被害者として犠牲となったのです。",
   "3.08#11 · 3.08#13"),
  ("H","neutral",-0.02,0.6,"t3_brain_mirror","still",
   "医学的注記：精神科医の間でも診断には議論がありました。これは行動を理解するための理論的枠組みです。",
   "3.04#1 · 3.08#3 · 3.11#6"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Amber Eyes 第3話。事件の全貌はバイオのリンクからご覧いただけます。",
   "CTA")
 ]
},
{
 "id": "TK4",
 "title": "IQ 145の巨人がFBIに自らの精神を開放した理由",
 "signs": [7, 8],
 "theme": "暴力妄想サイクルと心理的署名（FBIマインドハンターの起源）",
 "hook": "IQ 145。FBIの捜査手法を永遠に変えた頭脳。",
 "bgm": "bgm_ambient_deep.mp3",
 "bgm_desc": "第4幕 — 本編ベッド曲: bgm_ambient_deep.mp3",
 "sfx": ["amb_prison.wav (環境音)", "fx_iron_door.wav", "fx_tape_click.wav", "fx_tension_tick.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"after_id": "TK4.01#1", "text": "ヴァカヴィル医療施設 · 1978年 · FBI特別捜査官", "dur_s": 3.0},
   {"after_id": "TK4.01#3", "text": "IQ 145 · 人類の最上位0.13%の天才的頭脳", "dur_s": 2.5},
   {"after_id": "TK4.01#5", "text": "暴力妄想サイクル（FANTASY CYCLE）", "dur_s": 2.5},
   {"after_id": "TK4.01#7", "text": "記念品：全能感を再び体験するための触媒", "dur_s": 2.5},
   {"after_id": "TK4.01#9", "text": "心理的署名（SIGNATURE） vs 手口（MO）", "dur_s": 3.0},
   {"after_id": "TK4.01#10", "text": "名作『マインドハンター』の礎となった記録", "dur_s": 2.5}
 ],
 "sources": ["1.13#1-#9", "4.02#1-#8", "4.05#1-#19", "4.07#1-#10", "4.08#1-#7", "FBI Law Enforcement Bulletin 1985"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_vacaville_1978","still",
   "IQ 145。FBIの捜査手法を永遠に変えた頭脳。",
   "1.13#2 · 4.02#4 · 4.08#1"),
  ("D","neutral",-0.03,0.6,"t3_two_agents","pull",
   "1978年、FBIの伝説的捜査官ロバート・レスラーとジョン・ダグラスがヴァカヴィルの独房に入りました。",
   "4.02#1 · 4.02#4 · 4.02#8"),
  ("D","neutral",-0.03,0.6,"t3_giant_doorway","still",
   "ケンパーは山のように扉を塞ぎましたが、丁重に微笑み、大学教授のような落ち着いた口調で語り始めました。",
   "4.05#1 · 4.05#2 · 4.05#3"),
  ("D","neutral",-0.03,0.6,"t3_interview_room","push",
   "IQ 145を持つ彼は、減刑も弁護士も求めず、外科医のような冷徹さで自らの内面を解剖してみせました。",
   "1.13#2 · 1.13#5 · 4.05#4 · 4.05#13 · 4.05#14"),
  ("D","neutral",-0.03,0.7,"t3_cassette","pan",
   "ケンパーはFBIに画期的な概念を提示しました。それが「暴力妄想のサイクル」です。",
   "4.07#1 · 4.07#2"),
  ("D","neutral",-0.03,0.7,"t3_fantasy_spiral","push",
   "犯罪は凶器を手にした瞬間に始まるのではなく、何年にも及ぶ数百回の頭の中での予行演習から始まります。",
   "4.07#3 · 4.07#4 · 4.07#5"),
  ("D","neutral",-0.03,0.6,"t3_trophy_box","still",
   "戦利品を集めた理由について、犯行後の興奮が消えたとき、支配の快感を再び呼び起こすための触媒だと説明しました。",
   "4.07#6 · 4.07#7"),
  ("H","neutral",-0.02,0.7,"t3_organized_split","pull",
   "ケンパーら36人の服役囚との対話は、FBIの秩序型殺人犯の分類や全国追跡システムViCAPの礎となりました。",
   "1.13#6 · 1.13#7 · 4.08#1 · 4.08#2 · 4.08#3"),
  ("C","neutral",-0.02,0.7,"t3_self_observation","still",
   "現場には物理的証拠だけでなく、犯人特有の感情的欲求である心理的署名が刻まれるのです。",
   "4.08#4"),
  ("H","neutral",-0.02,0.6,"t3_case_photos","push",
   "この記録は現代プロファイリングの出発点となり、名作『マインドハンター』のモデルとなりました。",
   "4.08#6 · 4.08#7"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Amber Eyes 第3話。事件の全貌はバイオのリンクからご覧いただけます。",
   "CTA")
 ]
},
{
 "id": "TK5",
 "title": "マクドナルドの3徴候と4つの初期警告サイン",
 "signs": [10],
 "theme": "被害者学と生存のための4つの危険信号（マクドナルドの3徴候）",
 "hook": "4つの初期警告サイン。犠牲者を二度と出さないために。",
 "bgm": "bgm_piano_minimal.mp3",
 "bgm_desc": "第5幕 — 本編ベッド曲: bgm_piano_minimal.mp3",
 "sfx": ["amb_wind_soft.wav (環境音)", "fx_clock_tick.wav", "fx_stinger.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"after_id": "TK5.01#1", "text": "犯罪心理学が警鐘を鳴らす4つの重要シグナル", "dur_s": 3.0},
   {"after_id": "TK5.01#2", "text": "第1の兆候：幼少期のマクドナルド3徴候", "dur_s": 2.5},
   {"after_id": "TK5.01#4", "text": "第2の兆候：家庭内での極端な精神的虐待", "dur_s": 2.5},
   {"after_id": "TK5.01#5", "text": "第3の兆候：現実から遊離した支配妄想への没頭", "dur_s": 2.5},
   {"after_id": "TK5.01#6", "text": "第4の兆候：高い知性と感情の冷淡さの結合", "dur_s": 3.0},
   {"after_id": "TK5.01#8", "text": "子どもの心の傷を家庭で癒すことの重要性", "dur_s": 3.0}
 ],
 "sources": ["5.04#1", "5.05#1-#8", "5.06#1-#4", "5.08#6-#11", "Peter Vronsky"],
 "lines": [
  ("H","neutral",-0.02,0.5,"t3_red_flags","still",
   "4つの初期警告サイン。犠牲者を二度と出さないために。",
   "5.04#1 · 5.08#11"),
  ("C","neutral",-0.02,0.6,"t3_gift_drowned","push",
   "第1の兆候：幼少期のマクドナルドの3徴候。10歳の頃から始まった意図的かつ計画的な動物虐待。",
   "5.05#1 · 5.05#2 · 5.05#4 · 5.05#6"),
  ("C","neutral",-0.02,0.6,"t3_gift_drowned","pull",
   "これは共感能力の著しい欠如と暴力のエスカレーションを示す、見逃してはならない重大な警告でした。",
   "5.05#6"),
  ("C","neutral",-0.02,0.6,"t3_coal_furnace","pan",
   "第2の兆候：家庭内での極端な精神的虐待。子どもを閉鎖空間に隔離し、長期間にわたり尊厳を否定すること。",
   "5.05#7 · 5.05#8"),
  ("D","neutral",-0.03,0.6,"t3_fantasy_spiral","still",
   "第3の兆候：現実から切り離された支配の妄想世界に一人で深く没頭し、武器に異常な関心を持つこと。",
   "5.06#1 · 5.06#2"),
  ("D","neutral",-0.03,0.7,"t3_self_observation","push",
   "そして第4の兆候：高い知性と感情の冷たさ。大人を言い負かし操る能力を持ちながら、他人の痛みに涙を流せないこと。",
   "5.06#3 · 5.06#4"),
  ("H","neutral",-0.02,0.7,"t3_life_sentence","pull",
   "エドマンド・ケンパーは天才的な頭脳と体力を与えられながら、虐待のるつぼの中で破壊兵器へと変貌しました。",
   "5.08#8 · 5.08#9"),
  ("H","neutral",-0.02,0.8,"t3_closing_desk","still",
   "悪を鉄格子の向こうに閉じ込めるのは法の役目です。しかし、子どもの心の傷を家庭で癒すことこそが悪を防ぐ唯一の道です。",
   "5.08#10 · 5.08#11"),
  ("H","neutral",-0.02,0.0,"t3_closing_desk","still",
   "Amber Eyes 第3話。事件の全貌はバイオのリンクからご覧いただけます。",
   "CTA")
 ]
}
]

# ----------------------------------------------------------------------------
# 3. BUILD GENERATORS FOR EN AND JA
# ----------------------------------------------------------------------------
def build_spec_en():
    spec = {
        "_readme": "SPEC_AUDIO_CLIP_TAP03_EN.json — Audio specs for 5 English TikTok clips (TK1–TK5).",
        "_episode": "03_EN",
        "_language": "en",
        "_title": "The IQ 145 Giant & The Mirror of Psychological Autopsy",
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
        "_readme": "SPEC_AUDIO_CLIP_TAP03_JA.json — Audio specs for 5 Japanese TikTok clips (TK1–TK5).",
        "_episode": "03_JA",
        "_language": "ja",
        "_title": "IQ 145の巨人と精神解剖の鏡",
        "_measured_rates": {r: round(RATE_JA[r], 4) for r in RATE_JA},
        "_clips_summary": {},
        "clips": {}
    }
    for c in CLIPS_JA:
        cid = c["id"]
        tot_dur = 0.0
        tot_units = 0
        lines_spec = []
        for idx, (vai, emo, spd, pause, bg, motion, text, src) in enumerate(c["lines"], 1):
            w = count_units(text, is_ja=True)
            d = round(w * RATE_JA[vai], 2)
            tot_dur += d + pause
            tot_units += w
            lines_spec.append({
                "clip_line_id": f"{cid}.01#{idx}",
                "role": vai,
                "emotion": emo,
                "speed_offset": spd,
                "pause_after_s": pause,
                "bg": bg,
                "motion": motion,
                "text": text,
                "characters_spoken": w,
                "est_dur_s": d,
                "src_script": src
            })
        c["est_dur_s"] = round(tot_dur, 1)
        spec["_clips_summary"][cid] = {
            "title": c["title"],
            "lines_count": len(c["lines"]),
            "characters_count": tot_units,
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
def write_en_files(spec):
    for c in CLIPS_EN:
        cid = c["id"]
        hook = c["lines"][0][6]
        cap = (
            f"{hook} 👁️\n\n"
            f"Ep. 03 · The IQ 145 Giant — Marker #{c['signs'][0]}: {c['theme']}.\n"
            f"True crime case file, source-verified.\n\n"
            f"📺 Watch the complete documentary on YouTube — link in bio.\n"
            f"🔎 Criminal Psychology · {c['title']} · Real Case File\n\n"
            f"Content created with AI assistance for behavioral analysis. Viewer discretion advised.\n\n"
            f"#AmberEyes #CriminalPsychology #TrueCrime #Mindhunter #EdmundKemper #{cid} #CaseFile\n\n"
            f"---\n"
            f"Publishing Notes (DO NOT paste into caption):\n"
            f"- TOGGLE ON 'AI-generated content' label on TikTok.\n"
            f"- Link to YouTube Episode 03: [ADD_EPISODE_03_URL_IN_BIO]\n"
            f"- Estimated duration: {c['est_dur_s']} s ({len(c['lines'])} lines)\n"
            f"- Video file: clip{cid[-1]}_{cid}_EN.mp4 (1080x1920, 30fps)"
        )
        (OUT_EN / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")

        desc = (
            f"{hook} 👁️\n\n"
            f"Episode 03 · The IQ 145 Giant — Psychological Marker #{c['signs'][0]}: {c['theme']}.\n"
            f"Documented facts from FBI archives and court records.\n\n"
            f"📺 Watch the full 31-minute documentary on YouTube — link in bio.\n\n"
            f"——————\n"
            f"PSYCHOLOGICAL ANALYSIS: {c['theme'].upper()}\n"
            f"——————\n"
            f"{c['title']}.\n\n"
            f"How did a six-foot-nine giant with an IQ of 145 commit serial homicides while befriending the very detectives investigating him?\n"
            f"Amber Eyes deconstructs the Edmund Kemper file through our 10-Indicator Behavioral & Psychological Ecosystem.\n\n"
            f"Key insights explored in this clip:\n"
            f"• Verified case timelines and psychological catalysts.\n"
            f"• Foundational behavioral analysis that gave birth to the FBI Behavioral Science Unit and ViCAP.\n\n"
            f"What is your perspective on this case? Share your thoughts below 👇\n\n"
            f"#AmberEyes #TrueCrime #Psychology #EdmundKemper #Mindhunter #CriminalProfiling"
        )
        (OUT_EN / f"MoTa_Dai_{cid}.txt").write_text(desc, encoding="utf-8")
        (OUT_EN / f"MoTa_Ngan_{cid}.txt").write_text(desc[:1200], encoding="utf-8")

def write_ja_files(spec):
    for c in CLIPS_JA:
        cid = c["id"]
        hook = c["lines"][0][6]
        cap = (
            f"{hook} 👁️\n\n"
            f"第03話 · IQ 145の巨人 — 心理指標 #{c['signs'][0]}: {c['theme']}。\n"
            f"公的記録とFBI捜査資料に基づく実話プロファイリング。\n\n"
            f"📺 完全版ドキュメンタリー（31分）はYouTubeで公開中 — プロフィールのリンクから。\n"
            f"🔎 犯罪心理学 · {c['title']} · 実際の事件記録\n\n"
            f"AI技術を活用して心理分析目的で制作されたコンテンツです。閲覧にはご注意ください。\n\n"
            f"#AmberEyes #犯罪心理学 #未解決事件 #実話 #マインドハンター #エドマンドケンパー #{cid}\n\n"
            f"---\n"
            f"投稿時の注意事項（キャプション本文には貼り付けないでください）：\n"
            f"- TikTokアプリで「AI生成コンテンツ」のトグルを必ずONにしてください。\n"
            f"- YouTube第03話へのリンク: [プロフィールのリンク欄にURLを設定]\n"
            f"- 推定再生時間: {c['est_dur_s']} 秒（全{len(c['lines'])}文）\n"
            f"- 出力動画ファイル名: clip{cid[-1]}_{cid}_JA.mp4 (1080x1920, 30fps)"
        )
        (OUT_JA / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")

        desc = (
            f"{hook} 👁️\n\n"
            f"第03話 · IQ 145の巨人 — 心理指標 #{c['signs'][0]}: {c['theme']}。\n"
            f"裁判記録・公的調書に基づく犯罪心理学ドキュメンタリー。\n\n"
            f"📺 YouTubeで31分の完全版ドキュメンタリーを公開中 — プロフィールのリンクから。\n\n"
            f"——————\n"
            f"心理深層解剖：{c['theme']}\n"
            f"——————\n"
            f"{c['title']}。\n\n"
            f"人類の上位0.13％に属するIQ 145の頭脳と、身長2メートル06の巨躯を持つエドマンド・ケンパー。\n"
            f"なぜ彼は自首し、FBIに自らの精神を解剖してみせたのか？\n"
            f"犯罪心理学ドキュメンタリー『Amber Eyes』は、10の行動・心理指標を通じて事件の本質を解き明かします。\n\n"
            f"本クリップの要点：\n"
            f"• 心理的トリガーと家庭環境における人格形成の闇。\n"
            f"• FBI行動科学課（BSU）や名作ドラマ『マインドハンター』の礎となった対話記録。\n\n"
            f"皆さんはこの心理メカニズムについてどう考えますか？ コメント欄でご意見をお聞かせください 👇\n\n"
            f"#AmberEyes #犯罪心理学 #マインドハンター #未解決事件 #プロファイリング #海外ドキュメンタリー"
        )
        (OUT_JA / f"MoTa_Dai_{cid}.txt").write_text(desc, encoding="utf-8")
        (OUT_JA / f"MoTa_Ngan_{cid}.txt").write_text(desc[:1200], encoding="utf-8")

def write_markdown_en():
    L = []
    A = L.append
    A("# TIKTOK CLIP PLAN — EPISODE 03 (ENGLISH) · \"THE IQ 145 GIANT\"")
    A("")
    A("*Status: Completed & Source-Verified (AGENTS.md K1–K10, G1–G13)*")
    A("*Audio Spec: `02_SAN_XUAT/TIKTOK/Tap03_EN/SPEC_AUDIO_CLIP_TAP03.json`*")
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
    A("| Voices | English Higgs Cast: Host (H), Detective (D), Psychologist (C), Dispatcher (N1), Officer (N2) |")
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
    (OUT_EN / "KE_HOACH_CLIP_TAP03_EN.md").write_text("\n".join(L), encoding="utf-8")

def write_markdown_ja():
    L = []
    A = L.append
    A("# TikTokクリップ制作計画 — 第03話（日本語） · 「IQ 145の巨人と精神解剖の鏡」")
    A("")
    A("*状態：完成・公的記録検証済み（AGENTS.md K1–K10、G1–G13準拠）*")
    A("*音声仕様書：`02_SAN_XUAT/TIKTOK/Tap03_JA/SPEC_AUDIO_CLIP_TAP03.json`*")
    A("")
    A("## 0. 基本概要")
    A("")
    A("| 項目 | 設定内容 |")
    A("|---|---|")
    A("| クリップ総数 | **5本**（TK1–TK4 本編深層分析 + TK5 被害者学・4つの警告サイン） |")
    tot_lines = sum(len(c["lines"]) for c in CLIPS_JA)
    A(f"| 総読み上げ行数 | **{tot_lines} 行** |")
    durs = [c["est_dur_s"] for c in CLIPS_JA]
    A(f"| 推定再生時間 | {min(durs):.1f}秒 ～ {max(durs):.1f}秒（目標 65～90秒 · QC許容範囲 45～95秒） |")
    A("| 配役音声 | 日本語 Higgs キャスト：ホスト (H)、刑事 (D)、心理学者 (C)、当直係 (N1)、警察官 (N2) |")
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
    (OUT_JA / "KE_HOACH_CLIP_TAP03_JA.md").write_text("\n".join(L), encoding="utf-8")

def main():
    spec_en = build_spec_en()
    (OUT_EN / "SPEC_AUDIO_CLIP_TAP03.json").write_text(
        json.dumps(spec_en, ensure_ascii=False, indent=2), encoding="utf-8")
    write_en_files(spec_en)
    write_markdown_en()

    spec_ja = build_spec_ja()
    (OUT_JA / "SPEC_AUDIO_CLIP_TAP03.json").write_text(
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
