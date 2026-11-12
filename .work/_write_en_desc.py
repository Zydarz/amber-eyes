# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding="utf-8")

en_text = """Episode 01: Poison in the Name of Mother’s Love | Criminal Psychology: Gypsy Rose & Dee Dee Blanchard (FDIA & 10 Behavioral Markers) | Amber eyes

In the summer of 2015, Springfield, Missouri was shaken when Dee Dee Blanchard—celebrated nationwide as a devoted caregiver—was found murdered in her pink home. Her daughter Gypsy Rose—believed to suffer from leukemia, muscular dystrophy, and severe cognitive impairment—vanished. A frantic search began under the terrifying assumption that the girl would perish without medication.

Yet 48 hours later in Wisconsin, Gypsy walked into an interrogation room on her own feet. No wheelchair. No leukemia. No intellectual disability. A horrifying deception was exposed: for 23 years, Dee Dee had imprisoned her daughter in an artificial medical dungeon, poisoning and mutilating a healthy child to extract societal pity and narcissistic supply.

In this episode, Amber eyes dissects the Gypsy Rose Blanchard case through the Ecosystem of 10 Core Psychological & Behavioral Markers:
1. SOCIAL AFTERSHOCK & CRISIS OF COMPASSION: Exploitation of charity goodwill (Habitat for Humanity, Make-A-Wish) and fatal systemic blind spots in multi-institution healthcare oversight.
2. OBJECTIFICATION OF THE VICTIM: Reducing Gypsy to a "living prop" for narcissistic supply; deficits in Theory of Mind and total affective indifference to a child's suffering.
3. COMPARTMENTALIZATION: Splitting reality—the gentle mother singing lullabies vs. the tyrant chaining her child to a bed and forcing neuroleptic drugs; weaponizing motherhood as a shield of normalcy.
4. ATTITUDE TOWARD SENTENCING & PSYCHOLOGICAL PARADOX: Prosecutorial balance under Dan Patterson; 10-year plea deal; Gypsy's chilling confession: "I feel more free in prison than living with my mother."
5. TECHNIQUES OF NEUTRALIZATION: Rationalizing abuse via a Hero Complex ("She is too fragile, only my control saves her"); exploiting Hurricane Katrina to erase medical paper trails.
6. PSYCHOLOGICAL TRIGGER & THE BREAKING POINT: Adolescent autonomy; failed 2011 escape leading to 2 weeks chained to a bed; catastrophic descent into Folie à Deux with Nicholas Godejohn.
7. SIGNATURE VS. MODUS OPERANDI (MO): Evolving MO (doctor shopping, fake disaster records, learned nursing jargon) vs. immutable Signature (forced infantilization, shaved head, princess gowns).
8. MEDICAL ESCALATION TRAJECTORY (4 STAGES): 3 months: fake sleep apnea -> Age 7: wheelchair confinement -> Feeding tube, Tegretol-induced tooth decay, salivary gland excision -> Identity erasure.
9. THE HALO EFFECT & SOCIAL BLIND SPOTS: The "saintly caregiver" archetype created an invisible shield, paralyzing skepticism from neighbors, doctors, and media for 23 years.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Decoding Gypsy's paralysis through Learned Helplessness and Trauma Bonding; 4 crucial clinical red flags for identifying FDIA in domestic settings.

⏱ TIMESTAMPS
00:00 Intro
00:23 Act 1 · The Moment Trust Broke & Social Blind Spots
05:30 Act 2 · Crime Scene & The Escalating Medical Abyss
11:00 Act 3 · Psychological Autopsy — Inside the Mind of FDIA
16:30 Act 4 · The Victim's Perspective — Why Couldn't Gypsy Just Stand Up?
22:15 Act 5 · Forensic Verdict, Psychological Judgment & Survival Red Flags

⚠️ DISCLAIMER
• Not intended for children. Educational & criminal psychology analysis only; does not replace medical or legal counsel.
• Sourced from verified public judicial records & peer-reviewed literature. The channel does not defame any individual.
• Animal avatars (Owl, Wolf, Fox, Sheep, Cat) are stylized narrators. Dialogues are reconstructed from factual case files.
• Narration, visual artwork, and soundtrack generated via dedicated AI production workflows.

📚 REFERENCES & COURT FILES
Verified against certified public judicial records:
• Greene County Circuit Court: State v. Gypsy R. Blanchard (No. 1531-CR03348) & State v. Nicholas Godejohn (No. 1531-CR03347)
• APA DSM-5-TR: Factitious Disorder Imposed on Another (FDIA / Munchausen by Proxy)
• Dr. Marc D. Feldman: 'Playing Sick? Untangling the Web of Munchausen Syndrome, Munchausen by Proxy, and Malingering'
• Children’s Mercy Hospital (2007): Clinical notes & FDIA suspicions by Dr. Bernardo Flasterstein
• Greene County Sheriff's Office: Official interrogation files & transcripts
• Investigative Reporting: Michelle Dean (BuzzFeed News 2016) & 'Mommy Dead and Dearest' (HBO 2017)
• NCMEC: Medical Child Abuse & FDIA Identification Protocols

📞 HOTLINES & REPORTING
If you suspect a child is suffering medical abuse, neglect, or violence:
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 (Toll-Free, 24/7)
• National Domestic Violence Hotline: 1-800-799-SAFE (7233)
• Crisis Text Line: Text HOME to 741741

#AmberEyes #TrueCrime #CriminalPsychology #GypsyRoseBlanchard #DeeDeeBlanchard #FDIA #MunchausenByProxy #LearnedHelplessness #TraumaBonding #10PsychologicalMarkers #RedFlags #ForensicPsychology
"""

for path in ["02_SAN_XUAT/Tap01_EN/mo_ta.txt", "02_SAN_XUAT/Tap01_EN/xuat_ban/mo_ta.txt"]:
    with open(path, "w", encoding="utf-8") as f:
        f.write(en_text.strip() + "\n")
    print(f"Wrote {path} ({len(en_text.strip())} chars)")


