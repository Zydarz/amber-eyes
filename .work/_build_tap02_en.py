import json, sys, subprocess
from pathlib import Path

# Load Vietnamese parsed script
with open('.work/script_tap02.json', 'r', encoding='utf-8') as f:
    vn_script = json.load(f)

# Build translations element by element
en_translations = {}

# Act 1
en_translations['1.03'] = [
    "July 2009.",
    "At Canadian Forces Base Trenton — the largest strategic air force base in the Canadian military.",
    "A change-of-command ceremony takes place with solemnity before the highest-ranking military dignitaries.",
    "Stepping onto the podium to assume supreme command is Colonel David Russell Williams — a veteran pilot with a service record so spotless that not a single blemish could be found."
]

en_translations['1.05'] = [
    "At 46 years old, this man had personally piloted VIP transports for Queen Elizabeth II, Prince Philip, and Canadian Prime Ministers.",
    "He was celebrated as an exemplar of iron discipline, a devoted husband whose wife served as an associate director at the Heart and Stroke Foundation of Canada in Ottawa.",
    "Trenton was not merely an operational military base, but the sacred ground that received the repatriated caskets of fallen Canadian soldiers from the Afghanistan war along the 'Highway of Heroes'.",
    "The officer presiding over those solemn ceremonies was none other than Williams himself.",
    "To understand just how deep that admiration and trust ran, imagine how those who served under his command truly felt."
]

en_translations['1.07'] = [
    "In the eyes of everyone at CFB Trenton, Colonel Williams was the living embodiment of absolute perfection.",
    "He was composed, immaculate down to the sharp creases of his uniform, tirelessly dedicated, and never once raised his voice at a subordinate.",
    "Yet when the truth shattered... the entire country was shocked, and chills ran down our spines.",
    "We had stood at attention, saluting with deep respect a man who, by night, was one of the most dangerous predators alive."
]

en_translations['1.08'] = [
    "Yet who could have imagined that the man wearing a uniform covered in medals of honor would, in the dead of night after leaving the military base, vanish into the shadows of quiet suburban towns.",
    "Out there, the commanding colonel no longer existed.",
    "There was only a prowling shadow, silently slipping past fences across the snow.",
    "That very summit of status created a lethal 'Halo Effect' — an invisible shield that blinded both society and law enforcement for years."
]

en_translations['1.10'] = [
    "The night of January 28th, 2010.",
    "Jessica Lloyd — an independent, warm-hearted 27-year-old employee in the city of Belleville — suddenly vanished from her home.",
    "The Ontario Provincial Police launched an unprecedented massive search, while collective paranoia gripped the community: women wedged chairs behind their doors, and neighbors eyed each other with suspicion in the freezing winter cold."
]

en_translations['1.12'] = [
    "Police found no leads during those first few days.",
    "Yet one week later, on the evening of February 4th, a mobile roadblock was established on the road near the victim's home, lasting through the night.",
    "The sole objective of that checkpoint was to hunt for a specific clue: a rare, distinct off-road tire impression embedded in the snow near Jessica Lloyd's house."
]

en_translations['1.14'] = [
    "Among the vehicles passing through the checkpoint that night was a Nissan Pathfinder.",
    "That evening, the owner drove his Pathfinder instead of the BMW he usually took.",
    "The driver rolled down his window — it was the Wing Commander of CFB Trenton.",
    "The tread pattern on his tires bore a striking resemblance to the tracks in the snow.",
    "Yet before such a poised, high-ranking officer, the patrol officers could not detain him, merely logging his details before saluting respectfully and letting him pass.",
    "And for the next three days, he remained a free colonel.",
    "Let us hear the Investigator reconstruct what took place during those three tense days."
]

en_translations['1.17'] = [
    "Fresh snowfall had preserved a highly distinct tire impression near the victim's residence: a relatively rare Kumho off-road tread pattern, alongside a large footprint from a winter boot.",
    "When the patrol stopped Colonel Russell Williams's Nissan Pathfinder, it seemed like a routine traffic check.",
    "Yet when the flashlight beam struck the tire, the striking match was immediately recorded and relayed back to the command center.",
    "That was the very first time Colonel Russell Williams's shadow world collided with the investigative apparatus.",
    "Over the next three days, investigators worked around the clock: matching tire treads, verifying travel itineraries, and drafting emergency search warrants for both of his homes — one in Ottawa, and one in the town of Tweed.",
    "And rather than staging a noisy public arrest, Colonel Russell Williams received a polite telephone call: inviting him to provincial police headquarters to help eliminate him as a person of interest."
]

en_translations['1.18'] = [
    "Welcome to our criminal psychology dossier.",
    "Today, we unlock one of the most bizarre and shocking cases in criminological history: The File of Colonel Russell Williams.",
    "This episode will delve into two dark mechanisms of the human mind: **The law of behavioral escalation** and **Cognitive compartmentalization** — to answer the haunting question: How could an elite mind live two parallel lives, directly behind the uniform of honor?"
]

# Act 2
en_translations['2.02'] = [
    "When Jessica Lloyd vanished into the snowy winter night, the Ontario Provincial Police understood they were not merely facing an isolated incident.",
    "Tracing scene evidence and unsolved cold cases across the Tweed and Belleville areas, a chilling portrait began to emerge."
]

en_translations['2.04'] = [
    "The abductor did not emerge from a vacuum.",
    "He was a phantom who had quietly perfected his predatory craft over years in the darkness.",
    "The disappearance of Jessica Lloyd was merely the tip of an iceberg — a descent into depravity constructed across **4 distinct steps of behavioral escalation** spanning years.",
    "We invite the Investigator to break down the perpetrator's operational methods."
]

en_translations['2.05'] = [
    "Based on digital forensic evidence and seized exhibits, we reconstructed Russell Williams's predatory trajectory across four clear phases of escalation:",
    "**Step One: Nighttime Peeping.** Initially, Williams prowled quiet neighborhoods late at night, lurking in the dark to spy on women through their windows.",
    "**Step Two: Breaking and entering for intimate items.** When gazing through windows no longer satisfied him, he began slipping into empty homes. The earliest break-ins traced by police dated back to 2006. Between September 2007 and November 2009, he committed a total of 82 burglaries and attempted burglaries. He never stole money or valuable jewelry. What he took was women's underwear and intimate apparel. His ritual repeated identically in every home: photographing, taking items, and keeping meticulous records.",
    "**Step Three: Home invasion while occupants were present.** By September 2009, his threshold of arousal had grown completely desensitized. He invaded the homes of two women around the town of Tweed while they were inside, restraining them and committing sexual assaults.",
    "**And the final step: Taking human life.** In late November 2009, he struck against Marie-France Comeau — a dedicated 37-year-old corporal with 437 Squadron, serving at the very base where he held supreme command. And barely two months later, his next victim was Jessica Lloyd."
]

en_translations['2.07'] = [
    "Looking at the identities of both tragic victims, we see the ruthless power asymmetry of the predator at work.",
    "Corporal Marie-France Comeau was a subordinate serving inside his own military base, a soldier who placed complete trust in her commander. Meanwhile, Jessica Lloyd was an independent young woman living in a secluded standalone house. Both were robbed of their lives by a man who exploited isolation and institutional authority to the utmost.",
    "What makes his modus operandi truly terrifying is the fusion of deviant predatory impulses with rigid military discipline.",
    "He repeated an exact sequence, photographed everything, and logged every intrusion as if drafting an operational tactical report.",
    "We invite the Investigator to clarify the distinction between his operational method and his psychological signature."
]

en_translations['2.08'] = [
    "In professional behavioral analysis, we draw a clear line between two distinct concepts:",
    "Williams's *Modus Operandi* comprised the functional mechanics he used to complete the crimes and escape: walking in stocking feet to leave no shoe prints inside, wearing gloves, cutting telephone wires, and timing his attacks during heavy snowfall to erase tire tracks. This operational method evolved constantly across 82 burglaries.",
    "Yet his *Psychological Signature* — the immutable core that never changed — was the collection of **Trophies** and the enactment of deviant rituals.",
    "He did not steal intimate apparel to sell. He wore the victims' garments, posed before their bedroom mirrors taking self-portraits with an emotionless, chilling expression, and archived them systematically.",
    "That was what he required to sustain his psychological arousal and feed his fantasy addiction when sitting alone.",
    "Tire impressions in the snow brought investigators near him. But that secret digital vault documenting his psychological signature was the ultimate key that stripped away every shred of the colonel's disguise."
]

# Act 3
en_translations['3.02'] = [
    "Confronting the dossier of Russell Williams, any of us must grapple with a question that chills the soul:",
    "Why would a man who seemingly possessed everything — supreme status, renown, an accomplished wife, and the reverence of an entire nation — gamble it all away for lingerie and horrific violence?"
]

en_translations['3.04'] = [
    "Before diving into analysis, we must emphasize one essential truth: **no public clinical psychiatric diagnosis exists** for Russell Williams.",
    "The theoretical frameworks below are common analytical tools in criminal psychology — they help us ask the right questions, rather than serving as definitive clinical judgments.",
    "We invite our Psychological Expert to dissect the layers of cognitive mechanisms operating inside the mind of this two-faced colonel."
]

en_translations['3.05'] = [
    "When examining the case of Russell Williams, we cannot view him as an insane or psychotic individual. On the contrary, Williams was fully lucid and possessed superior intellect. His behavior operated through 3 extremely dangerous psychological layers.",
    "**The first layer is: The fantasy addiction cycle, dopamine desensitization, and the precipitating trigger.**",
    "Williams's early actions exhibited classic characteristics of fetishistic disorder. When he first stole intimate items, fear coupled with violating a severe taboo triggered a massive surge of dopamine — producing an intense rush of omnipotent arousal.",
    "Yet the human brain adapts through tolerance buildup. Once the initial behavior became routine, the predator fell into 'fantasy starvation'. He was compelled to escalate the stakes to recapture that initial high: from window-peeping, to unoccupied burglaries, to breaching homes while victims slept.",
    "Critically, in July 2009, when Williams was promoted to Wing Commander of CFB Trenton, that milestone acted as a **Precipitating Trigger**: absolute authority combined with overwhelming operational stress shattered his final cognitive inhibitions, sending him hurtling down the path to homicide."
]

en_translations['3.07'] = [
    "Yet what astounds the public most is: how could he live comfortably beside an accomplished spouse and command thousands of troops by day, only to morph into a cold-blooded predator by night without losing his sanity or suffering pangs of conscience?"
]

en_translations['3.08'] = [
    "The answer lies in **The Second Layer: Absolute Cognitive Compartmentalization and Rationalization Mechanisms.**",
    "In psychology, *Compartmentalization* is a defense mechanism enabling the brain to isolate conflicting thoughts and emotions into completely separate drawers.",
    "Williams appears to have constructed two distinct personas within a single body:",
    "**Drawer One:** Colonel Williams — the model commander, the attentive husband tending the garden, devoted to military honor, discipline, and moral standing in Ottawa.",
    "**Drawer Two:** The nocturnal predator — where he unleashed his darkest, most depraved impulses in Tweed.",
    "When in one drawer, he slammed the door shut on the other.",
    "He utilized his wife and respectable marriage as a 'Shield of Normalcy' to reassure himself: *I am still an honorable, distinguished man*.",
    "To silence his conscience, he fully deployed *Techniques of Neutralization*: across his first 82 break-ins, he told himself 'I am only looking, I harm no one, I am merely keeping a souvenir'.",
    "When he escalated to murder, he rationalized that 'the victim had seen my face, she forced my hand to protect myself'.",
    "And ultimately, he could never offer a genuine moral explanation.",
    "When the interrogator asked whether he had ever wondered why he did those things, his response in the transcript was chillingly vacant: 'Yes, but I don't know the answers, and I'm pretty sure the answers don't matter.'",
    "That is perhaps the most shameless statement ever recorded, laying bare the absolute moral disengagement of a cold-blooded predator.",
    "And it demonstrates just how deeply ingrained his self-justifying rationalizations had become."
]

en_translations['3.10'] = [
    "And what was his view of women, expert? Why could he strike so coldly against his own military subordinate?"
]

en_translations['3.11'] = [
    "That brings us to **The Third Layer: Victim Objectification and Malignant Narcissism.**",
    "Williams possessed a total deficit in Theory of Mind and affective empathy. In his perception, women were not human beings endowed with lives, dreams, or agony. They were demoted to 'living props' within his private theater of voyeurism and domination.",
    "A victim's tears, pleading, or terror did not trigger compassion; instead, they ignited **power arousal** — the ultimate fantasy that he held the power of life and death like a god.",
    "He photographed his victims not merely for fleeting gratification, but to transform them into permanent trophies feeding his malignant ego: *I control you, and no one can touch me.*"
]

# Act 4
en_translations['4.03'] = [
    "Sunday, February 7th, 2010. Provincial police headquarters in Ottawa, exactly 3:00 PM.",
    "Inside a cramped interrogation room, seated on one side of the table is Colonel Russell Williams in civilian clothing.",
    "Facing him is Detective Staff Sergeant Jim Smyth — a seasoned behavioral sciences investigator with the Ontario Provincial Police.",
    "The colonel had walked in voluntarily following a phone invitation. Brimming with the arrogance of a man who had never failed, he sat comfortably, declined counsel, and believed his military intellect would easily outmaneuver his interrogator."
]

en_translations['4.05'] = [
    "While that historic duel unfolded behind closed doors, listen to the voices of the residents who lived in Williams's shadow."
]

en_translations['4.06'] = [
    "For years, our small town of Tweed lived in an unspoken, suffocating unease.",
    "Intimate belongings were occasionally disturbed, doors showed signs of prying, yet no money was stolen. We thought we were paranoid... until the truth came out. That realization was more horrifying than any nightmare: you realize that while you were sound asleep, a man disguised as a high-ranking officer was standing right in your bedroom, staring at you in the dark."
]

en_translations['4.07'] = [
    "That haunting terror endured until the Nissan Pathfinder passed through the roadblock in the winter snow.",
    "Yet to compel a seasoned military mind to confess, Detective Jim Smyth executed a masterclass in psychological interrogation.",
    "Let us hear the Investigator reconstruct that suffocating chess match inside the interrogation room."
]

en_translations['4.08'] = [
    "Throughout the opening hours, Detective Jim Smyth never raised his voice or slammed the table in aggression. He maintained a calm, respectful tone, subtly walking Williams into the trap of his own hubris.",
    "Smyth asked: what was Williams prepared to provide to help police eliminate him as a suspect? And the confident colonel agreed: DNA samples, fingerprints, and footwear impressions.",
    "While the two men spoke, search teams were quietly executing search warrants at his residence in Ottawa and his cottage in Tweed.",
    "When Smyth placed the crime-scene snowboot photograph beside Williams's boot print and said: 'They are identical.'",
    "The colonel froze momentarily, feeling the first tremor of unease, and made a request: 'Call me Russ, please.'",
    "The invisible noose began to tighten."
]

en_translations['4.10'] = [
    "Smyth's phone vibrated: the search team in Ottawa had just discovered hidden hard drives concealed within the basement ceiling — containing thousands of photographs and meticulous logs of every single break-in.",
    "Smyth looked up, stared directly into Williams's eyes, and delivered the decisive blow: 'Investigators are at your house right now.'",
    "'Your wife now knows what is going on.'",
    "Williams froze completely.",
    "His entire constructed world of military prestige, honor, and his stature before his wife — the thing he feared losing most — shattered into dust.",
    "Trembling, he could only utter: 'I don't know what to say.'",
    "Exactly 4 hours and 40 minutes after the interrogation began, Smyth asked softly: 'So, where is she?'",
    "Williams bowed his head, his voice cracking: 'Got a map?'",
    "And over the next six hours, he systematically confessed to everything."
]

en_translations['4.11'] = [
    "That was the exact moment the wall of cognitive compartmentalization collapsed entirely.",
    "When the hard drives were uncovered, the barrier between his two mental drawers shattered.",
    "And Detective Jim Smyth had struck Williams's ultimate psychological vulnerability: **his wife**.",
    "According to the transcript, Williams repeated obsessively: 'I want to minimize the impact on my wife.'",
    "Smyth replied that he wanted that too — and the only way forward was the truth.",
    "And here is the most revealing insight: the anxieties he voiced centered entirely on how his wife viewed him and the reputational devastation to CFB Trenton.",
    "He never shed a single tear for the agony of the women or their grieving families.",
    "That was not genuine remorse.",
    "It was intense Pathological Self-Pity at realizing that the pristine mask of honor he had cultivated for twenty-five years had disintegrated before his loved ones and the world."
]

en_translations['4.12'] = [
    "Under the weight of objective physical evidence, the man who once commanded Canada's largest air base officially surrendered.",
    "Williams marked on a map the secluded location where he had abandoned Jessica Lloyd's body. Over the ensuing hours, he admitted to his fatal assault on Corporal Marie-France Comeau and two home invasions in Tweed.",
    "From that very digital archive meticulously hidden in his basement ceiling, police identified an additional 82 covert break-ins.",
    "One single man — 88 catastrophic criminal counts. The glamorous veneer behind the colonel's uniform vanished into thin air."
]

# Act 5
en_translations['5.02'] = [
    "October 2010. Superior Court of Justice in Ontario, Justice Robert Scott presiding in the town of Belleville.",
    "On October 18th, Russell Williams entered guilty pleas to all 88 charges. Three days later, on October 21st, the judge handed down the sentence: two concurrent life terms for first-degree murder, an additional 10 years for each sexual assault, 10 years for each forcible confinement, and 1 year for each of the 82 break-ins — all running concurrently. A life sentence with 25 years before parole eligibility.",
    "That was the mandatory statutory minimum under Canadian criminal law for first-degree murder."
]

en_translations['5.04'] = [
    "Yet the most devastating sentence for a malignant narcissist like Williams was the total annihilation of his honor and authority.",
    "The Governor General of Canada revoked his commission and expelled him from the military in disgrace.",
    "His service medals were severed into pieces, and his scroll of appointment was nullified.",
    "Immediately following his arrest, his biography was scrubbed from the Department of National Defence website.",
    "The Canadian military took an unprecedented step: burning all uniforms and clothing bearing his name in a classified disposal incinerator at CFB Trenton.",
    "According to military spokesman Hubert Genest, there was no ceremony, and no photographs were permitted.",
    "And it was the first time in twenty-five years of service that he had witnessed a military uniform burned.",
    "Reflecting on Williams's expulsion, Genest compared it to a sentence: 'When you put a period at the end of a sentence, the period is small, but it means a lot.'",
    "The Nissan Pathfinder that once drove through the roadblock was crushed into scrap, and hundreds of stolen items were incinerated entirely."
]

en_translations['5.06'] = [
    "And what was Williams's psychological posture before his judgment?",
    "Before the court, he recited a dry, mechanical apology like an automaton reciting a script.",
    "Yet once confined inside Kingston Penitentiary, stripped of every privilege and despised as an outcast, he engaged in hunger strikes and attempted suicide in his cell.",
    "That was a textbook manifestation of **Narcissistic Collapse**: when all control is lost and naked humiliation is unavoidable, the predator is left with nothing but pathetic self-pity."
]

en_translations['5.07'] = [
    "The case of Colonel Russell Williams inflicted deep societal trauma across Canada.",
    "It shattered public faith in revered national institutions, compelling the Canadian Armed Forces to overhaul security clearance vetting and psychological assessments for high-ranking commanders.",
    "Yet the paramount lesson for all of us is: **Never allow the Halo Effect to lull your intuition to sleep.**",
    "Prestige, academic credentials, or splendid military rank are merely social overcoats; they offer no guarantee for the decency of a human soul.",
    "Crime never begins with a fatal strike or a murder.",
    "It always begins with small, incremental boundary crossings: a peeping gaze, rummaging through private drawers, an unpunished trespass.",
    "When deviant impulses are nurtured in darkness, the threshold of gratification will continuously expand until it devours both victim and perpetrator alike."
]

en_translations['5.08'] = [
    "Forensically, military discipline enabled Williams to conceal his conduct for years, yet his compulsion to archive trophies for sick fantasies made him the author of his own indictment.",
    "The arrogance of a narcissist always leaves a trail.",
    "And the vital survival takeaway from this dossier is: **Always trust your intuition.**",
    "If you sense an ambiguous unease, if your personal boundaries are breached in the slightest way, never rationalize or dismiss it.",
    "Survival intuition is our built-in early warning radar designed to protect our lives."
]

en_translations['5.10'] = [
    "The dossier of Colonel Russell Williams serves as a chilling reminder of the unfathomable depths of the human psyche.",
    "An elite intellect protects no one.",
    "It merely ensures that the eventual collapse arrives later, and with catastrophic force.",
    "Never forget that throughout this entire ordeal, the only person who held the secret was that very man.",
    "The photographs arranged with precision.",
    "The stolen items hidden with meticulous care.",
    "And a ten-hour interrogation chess match — long enough for an arrogant predator to realize his mask of honor could never be repaired.",
    "Let us always remember: the greatest lesson in the wake of tragedy is not fear, but awakening to recognize and defend the safe boundaries of our lives."
]

en_translations['5.12'] = [
    "Our sincere thanks to the expert guests who accompanied us in dissecting today's dossier.",
    "Thank you for listening through to the final minutes of this story.",
    "Always maintain a vigilant perspective, trust your inner intuition, and cherish the peace of everyday life.",
    "Farewell, and we look forward to seeing you in our next criminal psychology analysis."
]

# Generate English Markdown content
en_md_lines = [
    "# CRIMINAL PSYCHOLOGY AUDIO / PODCAST SCRIPT — ENGLISH EDITION",
    "**Topic:** The 10 Psychological Markers & Behavioral Escalation — the case of Colonel Russell Williams.",
    "**Translated from:** `01_KICH_BAN/Tap02/kichban_tap02_22102026.md`. One English sentence for every Vietnamese sentence, same structure, same IDs.",
    "**Fact and legal review:** Based on public trial reporting, Ontario Provincial Police interrogation transcripts, Canadian court proceedings, and verified public records; analysis of real people is framed as opinion.",
    "",
    "---",
    "",
    "## PRODUCTION BRIEF",
    "",
    "| Item | Standard setting (host-driven documentary) |",
    "| :--- | :--- |",
    "| **Episode title** | Episode 02: The Two-Faced Colonel & The Escalation Abyss — When the Threshold of Satisfaction Collapses |",
    "| **Format** | Narrator-led investigative documentary — the **Host** carries the core narrative, pacing emotional beats and introducing each expert perspective (Investigator, Psychologist, Ordinary person) at pivotal dramatic moments. |",
    "| **Voices** | Host (narration) · Investigator (steely, factual, investigative tradecraft) · Psychologist (calm, academic, behavioral dynamics) · Ordinary person (shocked, candid; representing community reaction). |",
    "",
    "---",
    ""
]

# Map role headers
role_headers = {
    '1.03': "**HOST** *(slow, low, objective distance)*:",
    '1.05': "**HOST** *(slow, reflective)*:",
    '1.07': "**ORDINARY PERSON** *(emotional, sincere)*:",
    '1.08': "**HOST** *(low, reflective)*:",
    '1.10': "**HOST** *(slow, measured pace)*:",
    '1.12': "**HOST** *(narrative momentum)*:",
    '1.14': "**HOST** *(measured tone)*:",
    '1.17': "**INVESTIGATOR** *(steely, precise, analytical)*:",
    '1.18': "**HOST** *(slow, low, inviting narration)*:",
    '2.02': "**HOST** *(slow, low, narrative pace)*:",
    '2.04': "**HOST** *(reflective, grave)*:",
    '2.05': "**INVESTIGATOR** *(steely, factual, clinical precision)*:",
    '2.07': "**HOST** *(reflective, somber)*:",
    '2.08': "**INVESTIGATOR** *(steady, analytical tone)*:",
    '3.02': "**HOST** *(slow, low, narrative pace)*:",
    '3.04': "**HOST** *(measured, analytical)*:",
    '3.05': "**PSYCHOLOGIST** *(academic, incisive, lucid analysis)*:",
    '3.07': "**HOST** *(troubled, searching)*:",
    '3.08': "**PSYCHOLOGIST** *(lowering tone, slower, deliberate)*:",
    '3.10': "**HOST** *(slow, low, narrative pace)*:",
    '3.11': "**PSYCHOLOGIST** *(steady, razor-sharp analysis)*:",
    '4.03': "**HOST** *(lowering tone, slower, intense)*:",
    '4.05': "**HOST** *(lowering tone, slower)*:",
    '4.06': "**ORDINARY PERSON** *(shaken, emotional)*:",
    '4.07': "**HOST** *(lowering tone, slower)*:",
    '4.08': "**INVESTIGATOR** *(recollective, cold, precise)*:",
    '4.10': "**INVESTIGATOR** *(intense, climactic delivery)*:",
    '4.11': "**PSYCHOLOGIST** *(academic, deeply reflective)*:",
    '4.12': "**HOST** *(somber, moved)*:",
    '5.02': "**HOST** *(commanding, resolute yet reflective)*:",
    '5.04': "**HOST** *(grave, solemn)*:",
    '5.06': "**HOST** *(probing, analytical)*:",
    '5.07': "**PSYCHOLOGIST** *(somber, profound)*:",
    '5.08': "**INVESTIGATOR** *(resolute, concluding)*:",
    '5.10': "**HOST** *(warm, resonant, closing reflection)*:",
    '5.12': "**HOST** *(warm, concluding podcast episode)*:"
}

# Cues and Act headers
act_headers = {
    1: "## ACT 1: THE HOOK — THE EXTREME CONTRAST BEHIND A COLONEL’S RANK (00:00 – 05:15)",
    2: "## ACT 2: CRIME SCENE & CRIMINAL DOSSIER — THE 4 STEPS OF THE ESCALATION ABYSS (05:15 – 09:30)",
    3: "## ACT 3: PSYCHOLOGICAL AUTOPSY — INSIDE THE TWO-FACED KILLER’S BRAIN (09:30 – 15:00)",
    4: "## ACT 4: INTERROGATION ROOM CHESS MATCH — THE ART OF BREAKING A MILITARY MIND (15:00 – 21:00)",
    5: "## ACT 5: VERDICT, PSYCHOLOGICAL SENTENCE & SURVIVAL RED FLAGS (21:00 – 26:30)"
}

cues_en = {
    '1.01': "**[BGM]:** The roar of a jet engine rumbles in the distance, then plunges into a hollow, suffocating sub-bass drone. The steady, dry ticking of a clock echoes.",
    '1.02': "**[SFX]:** Tires grinding slowly over ice and packed snow on a freezing winter night.",
    '1.04': "**[Pause 1.5 seconds]**",
    '1.06': '**[SFX]:** A tape recorder clicks on softly "Click".',
    '1.09': "**[Pause 2 seconds — the music stops abruptly]**",
    '1.11': "**[SFX]:** Wind howling, boots crunching on crisp snow.",
    '1.13': '**[SFX]:** A knock on car window "Rap... rap...".',
    '1.15': '**[SFX]:** A heavy iron door slams shut "Slam".',
    '1.16': "**[BGM]:** Somber cello melody surges, merging with a driving sub-bass pulse.",
    '2.01': "**[BGM]:** Minimalist piano notes scatter cold melodies, interwoven with slow typing sounds in the dead of night.",
    '2.03': "**[SFX]:** Paper shuffling and mouse clicks echoing.",
    '2.06': "**[Pause 1.5 seconds]**",
    '3.01': "**[BGM]:** A somber cello weaves sorrowful low notes with a resonant sub-bass drone, setting an atmosphere akin to a psychiatric autopsy.",
    '3.03': "**[Pause 2 seconds]**",
    '3.06': "**[Pause 1.5 seconds]**",
    '3.09': "**[Pause 2 seconds]**",
    '4.01': "**[BGM]:** Soundscape shifts to the hum of interrogation room fluorescent lights. A solitary bass drone strains like a taut wire.",
    '4.02': '**[SFX]:** A metal chair scrapes across tile, a coffee mug sets down on wood with a sharp "Thud".',
    '4.04': "**[Pause 2 seconds]**",
    '4.09': '**[SFX]:** Phone vibrates softly "Buzz... buzz...", a photograph slides across the table "Zip".',
    '5.01': '**[BGM]:** The gavel strikes "Crack... Crack... Crack" in cathedral-like silence, followed by contemplative, awakening piano.',
    '5.03': "**[Pause 2 seconds]**",
    '5.05': "**[Pause 2 seconds]**",
    '5.09': "**[Pause 2 seconds — warm piano melody rises softly]**",
    '5.11': "**[Pause 1.5 seconds]**",
    '5.13': '**[SFX]:** A case file closes with a decisive "Snap", followed by a tape recorder shutting off.',
    '5.14': "**[BGM]:** Somber piano plays for 5 seconds before gently fading out."
}

current_act = 0
for e in vn_script:
    act = e['act']
    if act != current_act:
        current_act = act
        en_md_lines.append(act_headers[act])
        en_md_lines.append("")

    eid = e['id']
    kind = e['kind']
    if kind in ('BGM', 'SFX', 'NGHI'):
        en_md_lines.append(cues_en[eid])
        en_md_lines.append("")
    elif kind == 'LOI':
        header = role_headers[eid]
        en_md_lines.append(header)
        sents = en_translations[eid]
        # Format sentences
        for s in sents:
            en_md_lines.append(s)
        en_md_lines.append("")

content = "\n".join(en_md_lines)

# Write to both paths
out_p1 = Path("01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md")
out_p2 = Path("01_KICH_BAN/Tap02/kichban_tap02_EN.md")

out_p1.write_text(content, encoding='utf-8')
out_p2.write_text(content, encoding='utf-8')
print("Successfully generated English scripts.")
