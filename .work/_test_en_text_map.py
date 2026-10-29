import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

with open('02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md', 'r', encoding='utf-8') as f:
    vn_plan = f.read()

with open('.work/script_tap05_EN.json', 'r', encoding='utf-8') as f:
    en_script = json.load(f)

# Map sentence ID to English text
en_sents = {}
for e in en_script:
    if 'sentences' in e:
        for s in e['sentences']:
            en_sents[s['id']] = s['text']

# Parse Vietnamese rows from Section 6
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", vn_plan, re.M)
sec = vn_plan[m.end():]
m_end = re.search(r"^\*\*Tổng:", sec, re.M)
if not m_end:
    m_end = re.search(r"^---", sec, re.M)
sec_table = sec[:m_end.start()]

lines = sec_table.strip().splitlines()

# We will translate shot headers and row content
translated_rows = []

# English translation dictionary for shot texts based on English script lines
# Let's verify each shot's English text
en_text_map = {
    "1-00": "*ACT 01 · THE RESURFACED LETTER AFTER 13 YEARS OF SILENCE*",
    "1-01": "**MARCH 19 · 2004** · *Wichita, Kansas · United States*",
    "1-02": "**THE WICHITA EAGLE EDITORIAL OFFICE** · *Manila envelope bearing no return address*",
    "1-03": "**PHOTOCOPY OF VICKI WEGERLE'S LICENSE** · *Accompanied by three crime scene photographs*",
    "1-04": "*MIDWEST'S TERRIFYING NIGHTMARE* · **SIGNED: B-T-K** · *Bind · Torture · Kill*",
    "1-05": "—",
    "1-06": "**SHOCKWAVES ACROSS THE UNITED STATES** · *Ten victims claimed between 1974 and 1991*",
    "1-07": "**PHANTOM VANISHED INTO THIN AIR** · *Thirteen agonizing years without a shred of evidence*",
    "1-08": "**WICHITA POLICE & FBI COLD CASE ARCHIVES** · *Believed the perpetrator was deceased or imprisoned*",
    "1-09": "—",
    "1-10": "*HEAR FROM A RESIDENT OF* · **PARK CITY SUBURBAN COMMUNITY**",
    "1-11": "“When word spread that BTK had resumed sending letters after a decade, our town held its breath…” → `#2`: “Checked window latches, bought firearms, bolted doors before sundown.”",
    "1-12": "“No one could ever have imagined the monster hunted across America… was the very man measuring grass heights every day.”",
    "1-13": "**THE MOST BIZARRE PARADOX IN JURISPRUDENCE** · *Dormant for thirteen years · Evidence gone cold* → `#3`: *Technology utterly helpless* → `#4`: *Could have lived out his days under a respected guise*",
    "1-14": "**WHAT COMPELLED THE MONSTER TO SHATTER HIS SILENCE?** · *Why deliver himself directly into a police trap?*",
    "1-15": "—",
    "1-16": "*HEAR FROM THE INVESTIGATOR* · **THE OPENING MOMENTS OF A HISTORIC BATTLE OF WITS**",
    "1-17": "**THE TASK FORCE'S FIRST QUESTION:** *Why now?* → `#2`: *Flipping back through local newspapers*",
    "1-18": "**WICHITA EAGLE 30TH ANNIVERSARY SERIES** · *Robert Beattie's book questioned if BTK was dead or incapacitated*",
    "1-19": "**A DAGGER TO MALIGNANT NARCISSISTIC PRIDE** · *Refusing to be forgotten · The BTK monster is still alive*",
    "1-20": "**THE PURPLE FLOPPY DISK & NARCISSISTIC ADDICTION** · *The Dennis Rader (BTK) Dossier* · *Addiction to attention & Total compartmentalization*",
    "1-21": "*ACT 02* · **THE CRIME SCENE & PSYCHOLOGICAL SIGNATURE OF A TWO-FACED PREDATOR**",
    "2-01": "**CRIME SCENES ACROSS 17 YEARS OF ACTIVITY** · *1974–1991 · Highly idiosyncratic modus operandi and psychological signature*",
    "2-02": "*SELF-COINED MONIKER* · **BTK: BIND, TORTURE, KILL** · *Bind, Psychological Torture, and Kill*",
    "2-03": "*FBI BEHAVIORAL SCIENCE · PSYCHOLOGICAL SIGNATURE* · *First: Absolute need for subjugation* · *Binding victims, relishing terror*",
    "2-04": "**NIGHT BURGLARY, SEVERING PHONE WIRES & BINDING** · *Prolonging time to savor sheer terror in the dark*",
    "2-05": "**SECOND: COMPULSION TO KEEP TROPHIES** · *Taking driver's licenses, watches, jewelry as emotional triggers*",
    "2-06": "**THIRD: TAUNTING THE MEDIA** · *Packages hidden in public libraries and park trash cans*",
    "2-07": "**A METICULOUS AND PATIENT PREDATOR** · *Schooled in police tradecraft, always wearing gloves* → `#3`: *The true identity behind the mask*",
    "2-08": "**DENNIS RADER · BORN IN 1945** · *Four years in the U.S. Air Force · Degree in Administration of Justice*",
    "2-09": "**6220 INDEPENDENCE STREET, PARK CITY** · *A wife of thirty years and two well-mannered children*",
    "2-10": "**CHRIST LUTHERAN CHURCH COUNCIL PRESIDENT** · *Standing at the pulpit, greeting congregants, organizing charity*",
    "2-11": "**CUB SCOUT PACK LEADER** · *Teaching children how to tie knots, pitch tents, and value honesty*",
    "2-12": "**PARK CITY COMPLIANCE OFFICER SINCE 1991** · *Driving government pickup, measuring grass height, impounding stray animals*",
    "2-13": "**STRICT TO THE POINT OF RIGID OBSESSION** · *No one could imagine the man with the measuring tape was the BTK monster*",
    "2-14": "*Daytime: Model citizen · Dedicated churchgoer · Caring father* · **NIGHT: COLD-BLOODED PREDATOR STEALING LIVES** · *How did two antithetical personas coexist for thirty years?*",
    "2-15": "*ACT 03* · **PSYCHOLOGICAL AUTOPSY — INSIDE THE MIND OF MALIGNANT NARCISSISM**",
    "3-01": "*FIRST DEFENSE MECHANISM* · **TOTAL COMPARTMENTALIZATION** · *Ability to seal off psychological compartments with flawless precision*",
    "3-02": "**AN INVISIBLE CONCRETE WALL** · *Severing family life from dark fantasy worlds*",
    "3-03": "**DELUSIONAL PSYCHOLOGICAL CONSTRUCT: 'FACTOR X'** · *Attributing crimes to an abstract external entity*",
    "3-04": "—",
    "3-05": "*A BIZARRE CONSTRUCT INDEED* · **UNDER PSYCHOLOGICAL SCRUTINY: WHAT WAS 'FACTOR X'?**",
    "3-06": "*CLASSIC DEFENSE MECHANISM* · **RATIONALIZATION & PROJECTION** · *'It wasn't me, Factor X inside made me do it'*",
    "3-07": "**STRIPPING AWAY MORAL RESPONSIBILITY** · *Satisfying dark fantasies, then returning home to dine with family*",
    "3-08": "**SOPHISTICATED RATIONALIZATION TO LULL CONSCIENCE** · *What compelled him to return to the lethal game in 2004?*",
    "3-09": "*SECOND MECHANISM* · **MALIGNANT NARCISSISM & ADDICTION TO ATTENTION** · *Control and public admiration were his vital oxygen*",
    "3-10": "**13 YEARS BASKING IN PAST GLORY** · *Silently clipping news coverage into a secret scrapbook*",
    "3-11": "**THE NARCISSIST'S GREATEST FEAR: OBLIVION** · *Risking capture so the world would see his mask, rather than dying an anonymous officer*",
    "3-12": "**ADDICTION TO ATTENTION BLINDED SURVIVAL INSTINCTS** · *Blinded hubris paving the way for a historic forensic trap*",
    "3-13": "*ACT 04* · **THE INTERROGATION & THE DIGITAL FORENSIC TRAP**",
    "4-01": "**EARLY 2005** · *Fatigued with printing and stashing packages in winter* → *Transitioning to digital computer files* → *Rader was 60 and computer illiterate*",
    "4-02": "**HOME DEPOT PARKING LOT IN WICHITA** · *Cereal box placed on pickup truck bed on January 8, 2005*",
    "4-03": "**AN ASTONISHINGLY NAIVE QUESTION:** · *'Can I communicate with Floppy Disks without being traced?'*",
    "4-04": "*WICHITA EAGLE CLASSIFIED AD 494* · **'REX, IT WILL BE OKAY TO SEND IT'** · *Lt. Ken Landwehr's brilliant psychological bluff*",
    "4-05": "**FEBRUARY 16 · 2005** · *Package delivered to KSAS-TV station*",
    "4-06": "**PURPLE MEMOREX 1.44MB FLOPPY DISK** · *The critical exhibit that sealed the predator's fate*",
    "4-07": "**POLICE DIGITAL FORENSICS LAB** · *Specialist Randy Stone scanning magnetic sectors with forensic software*",
    "4-08": "*HIDDEN METADATA PROPERTIES REVEALED:* · *Line 1: 'Last saved by: Dennis'* · *Line 2: 'Company: Christ Lutheran Church'*",
    "4-09": "—",
    "4-10": "**SEARCH ENGINE QUERY: 'Dennis Christ Lutheran Church'** · *Church Council President: Dennis Rader*",
    "4-11": "**BLACK PICKUP TRUCK ON SURVEILLANCE CAMERAS** · *Matching vehicle seen at package drop sites*",
    "4-12": "*PAP SMEAR CELL DNA COMPARISON* · **100% FAMILIAL DNA MATCH** · *Medical sample of Rader's daughter from university clinic*",
    "4-13": "**NOON ON FEBRUARY 25 · 2005** · *Dozens of police cruisers surrounding and intercepting his vehicle on highway*",
    "4-14": "**CLASSIC INTERROGATION ROOM CONFRONTATION** · *'Why did you lie to me?' — 'Because we were trying to catch you!'*",
    "4-15": "**THE FACADE SHATTERS COMPLETELY** · *Confessing continuously to each murder over 30 hours*",
    "4-16": "*HEAR THE GRIEF-STRICKEN WORDS OF* · **KERRI RAWSON — DAUGHTER OF DENNIS RADER**",
    "4-17": "“The world knows him as a monster, but to me he was the best father…” → `#4`: **“THE PREDATOR HUNTED NATIONWIDE HUGGED ME GOODNIGHT EVERY NIGHT.”**",
    "4-18": "*ACT 05* · **THE VERDICT, RED FLAGS & CLOSING THOUGHTS**",
    "5-01": "**AUGUST 18 · 2005** · *Sedgwick County Court · Judge Gregory Waller*",
    "5-02": "**TEN CONSECUTIVE LIFE TERMS** · *Minimum 175-year sentence without possibility of parole*",
    "5-03": "**EL DORADO CORRECTIONAL FACILITY** · *Complete isolation from human society*",
    "5-04": "—",
    "5-05": "**FOUR CRITICAL RED FLAGS** · *Recognizing malignant narcissistic personalities in everyday life*",
    "5-06": "**RED FLAG 01: EXTREME OBSESSION WITH RULES & CONTROL** · *Morbid rigidity over minor regulations to subjugate others*",
    "5-07": "**RED FLAG 02: SHALLOW AFFECT BEHIND A CHARMING EXTERIOR** · *Active in social/religious circles yet lacking authentic empathy*",
    "5-08": "**RED FLAG 03: SECRET COMPULSION TO KEEP TROPHIES** · *Hoarding private mementos, personal items, or documents of others*",
    "5-09": "**RED FLAG 04: INSATIABLE NARCISSISTIC CRAVING FOR RECOGNITION** · *Fragile ego easily unravelling when challenged*",
    "5-10": "—",
    "5-11": "**JUSTICE MAY DELAY, BUT TRUTH INEVITABLY TRIUMPHS** · *Darkness must always yield to the light of truth*",
    "5-12": "—",
    "5-13": "**SPECIAL THANKS TO OUR GUESTS & VALUED LISTENERS** · *Stay vigilant and nurture an upright heart*",
    "5-14": "**UNTIL NEXT TIME IN OUR UPCOMING CRIMINAL PSYCHOLOGY DOSSIER**",
    "5-15": "**DOSSIER EPISODE 05 · CLOSED** · *AMBER EYES · Criminal psychology through real case files*"
}

print(f"Total mapped English shot texts: {len(en_text_map)}")
assert len(en_text_map) == 83, f"Expected 83 texts, got {len(en_text_map)}"
print("All 83 shots mapped successfully!")
