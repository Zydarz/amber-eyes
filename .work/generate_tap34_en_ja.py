# -*- coding: utf-8 -*-
"""
Generate exact 240-sentence scripts for Episode 34 across Vietnamese, English, and Japanese.
Aligns 1:1 across all 3 languages, passes V1-V9 and K10.
"""
import os, sys

from generate_tap34_vn import VN_SECTIONS

EN_SECTIONS = [
    # Act 1 (Total: 53 sentences)
    # Dlg 00 (Host): 10 lines
    (
        "**HOST** *(slowly, in a warm and grave tone, evoking historical gravity)*:",
        [
            "In mid-May 2010, a horrifying incident at the high-rise residential complex G4 Trung Yen in Hanoi sent shockwaves throughout Vietnamese society.",
            "In the heart of one of the capital's most modern and civilized urban districts, no one could fathom that a sinister and brutal crime could unfold right next door.",
            "Modern urban residents routinely live behind securely locked steel doors, convinced that their personal safety is unconditionally guaranteed.",
            "They believe that regardless of how chaotic the outside world becomes, a high-rise apartment remains an impenetrable and isolated sanctuary.",
            "Yet that very isolation and collective bystander apathy inadvertently forged an exceedingly perilous urban blind spot.",
            "In contemporary apartment buildings, people seldom pay attention or investigate peculiar noises originating from neighboring units.",
            "A fast-paced urban lifestyle and comfortable routines have dulled humanity's natural survival instincts against mortal threats.",
            "Malice did not select dark alleyways or deserted suburban wasteland to orchestrate its sinister design.",
            "It camouflaged itself behind the glittering facade of a model high-rise community, defying all security protocols and ordinary perception.",
            "One of the most shocking homicide files in Vietnam's modern judicial history commenced within such a stifling urban enclosure.",
        ]
    ),
    # Dlg 01 (Host): 7 lines
    (
        "**HOST** *(slowly, probing into family background and the disappearance)*:",
        [
            "Prior to the discovery of the crime scene on the afternoon of May 17, the victim's family endured nearly two weeks of agonizing desperation.",
            "Nguyen Phuong Linh departed her home on the evening of May 4, 2010, and vanished completely without a trace.",
            "Her mobile phone became permanently unreachable, and all her social media communications abruptly ceased.",
            "Her father, Nguyen Van Ba, a parent who cherished his daughter unconditionally, sensed profound dread from the very first night.",
            "He reported her disappearance to law enforcement and tirelessly retraced her social circles alongside relatives.",
            "Yet in a metropolis of millions, searching for a mysteriously vanished young woman was akin to seeking a needle in a boundless ocean.",
            "No one could have foreseen that the key to her disappearance was held by her first love from her university years.",
        ]
    ),
    # Dlg 02 (Investigator): 8 lines (+2)
    (
        "**INVESTIGATOR** *(composed and razor-sharp, recounting the initial forensics)*:",
        [
            "On the afternoon of May 17, 2010, police received a chilling report from building management and residents of the G4 tower.",
            "On the rooftop level housing technical installations and garbage chute facilities, a severely decomposed female corpse was discovered.",
            "What profoundly shocked the entire investigative team was that the scene bore no resemblance to an ordinary scuffle or accident.",
            "The perpetrator had deliberately eradicated all facial identification features and all ten fingertips of the victim.",
            "This represented an exceptionally brutal and calculated attempt at evidence destruction, rarely witnessed in criminal cases of that era.",
            "The subject's clear objective was to completely annihilate the victim's identity, rendering the remains an anonymous corpse to derail investigation.",
            "Yet all sophisticated calculations to conceal identity could never withstand the rigorous scientific techniques of modern forensics.",
            "That very night, all biological samples and residual epidermal ridge patterns recovered from the rooftop were subjected to emergency forensic analysis.",
        ]
    ),
    # Dlg 03 (Investigator): 9 lines (+2)
    (
        "**INVESTIGATOR** *(firm and authoritative, analyzing the crime scene and trace evidence)*:",
        [
            "At the rooftop crime scene of building G4, post-mortem examinations and forensic inspections were executed with utmost rigor.",
            "The location where the remains lay was an obscure corner on the technical utility floor, virtually unvisited by ordinary residents.",
            "Forensic examiners detected faint dragging marks and subtle biological traces trailing backward toward the emergency stairwell.",
            "Tracing each incompletely sanitized micro-droplet of blood, the perpetrator's route pointed directly down to the eleventh floor.",
            "And inside apartment number 1101, investigators encountered unmistakable, highly suspicious anomalies.",
            "A pungent odor of chemical cleaning agents hung in the air alongside hastily applied coats of fresh paint masking splatters on the walls.",
            "Those clumsy attempts at evidence concealment ironically served as the most damning evidence establishing the primary crime scene.",
            "Under specialized ultraviolet lighting and chemical luminol testing, latent micro-bloodstains concealed beneath the white paint and door trims fluoresced vividly.",
            "The perpetrator never anticipated that modern forensic science could decipher the truth even after a surface had been repeatedly scrubbed.",
        ]
    ),
    # Dlg 04 (Ordinary Person N1): 5 lines
    (
        "**ORDINARY PERSON** *(N1 - G4 resident, trembling with shock)*:",
        [
            "Several days beforehand, we had noticed an overpowering stench wafting through the emergency stairwells and air ventilation shafts.",
            "However, everyone assumed it was merely a dead rodent or accumulated domestic waste that had gone uncollected.",
            "None of us could ever have imagined that right above our ceilings lay such an unthinkable horror.",
            "The entire apartment complex plunged into absolute panic; households bolted their doors securely and forbade children from venturing into hallways.",
            "The most spine-chilling sensation was realizing that the perpetrator might have shared an elevator with us every single day.",
        ]
    ),
    # Dlg 05 (Psychologist): 8 lines (+2)
    (
        "**PSYCHOLOGIST** *(calm and scholarly, dissecting social psychology and the halo effect)*:",
        [
            "From the vantage point of behavioral psychology, this tragedy vividly illustrates the trap of the Intellectual Halo Effect and Social Reflex Paralysis.",
            "Our society instinctively associates elite education, refined appearances, and respectable family backgrounds with moral integrity.",
            "When an individual exhibits a scholarly demeanor, spectacles, and polite speech, the psychological defense systems of those around him are effectively disarmed.",
            "That positive cognitive bias constructs a flawless camouflage for covert narcissistic impulses and psychopathic deviations to flourish undetected.",
            "Furthermore, the Bystander Effect prevalent in modern urban metropolises created fertile ground for crime to proceed unimpeded.",
            "The apathy of the crowd did not stem from inherent cruelty, but rather from the psychological diffusion of responsibility: everyone assumes someone else will intervene.",
            "Within enclosed urban living environments, physical proximity between apartments is tight, yet psychological distance remains vast.",
            "That breakdown in social connectivity inadvertently transforms modern residential buildings into ideal blind spots for covert criminality.",
        ]
    ),
    # Dlg 06 (Psychologist): 6 lines
    (
        "**PSYCHOLOGIST** *(profoundly analyzing victim depersonalization)*:",
        [
            "The act of severing the victim's head and ten fingertips constitutes one of the most severe psychological markers in this case dossier.",
            "In behavioral science, this manifests Victim Depersonalization, also characterized as profound dehumanization.",
            "The perpetrator sought not merely to hinder identification procedures deployed by forensic investigators.",
            "At an unconscious level, this horrific act mirrored the perpetrator's absolute terror when confronting what he had just committed.",
            "He could not endure gazing upon the eyes and facial features of a human being he had once held in his embrace and loved.",
            "By transforming the victim into a faceless entity, the killer's psyche deceived itself into believing he had merely disposed of an object rather than a human life.",
        ]
    ),

    # Act 2 (Total: 53 sentences)
    # Dlg 07 (Host): 9 lines
    (
        "**HOST** *(slowly, exposing the stark reality behind the refined facade)*:",
        [
            "When the suspect's identity was gradually unveiled, the entire social fabric endured a psychological earthquake.",
            "The mastermind behind this heinous act was neither an underworld thug nor a hardened habitual criminal.",
            "It was Nguyen Duc Nghia, an accomplished alumnus of one of the nation's most prestigious elite universities.",
            "He was raised within a disciplined and respected family in the port city of Hai Phong, his father an esteemed military veteran.",
            "Nghia consistently presented himself to peers and mentors as a cultured, well-mannered, and intellectually gifted young gentleman.",
            "Yet lurking behind those scholarly spectacles was a clandestine double life consumed by reckless sports betting and debt.",
            "Ever-escalating debts cornered a fragile narcissistic ego into a desperate cul-de-sac from which there seemed no escape.",
            "He could not bear the prospect of his immaculate academic facade collapsing before his family and social circle.",
            "To salvage his pristine mask, the subject cold-bloodedly engineered a scheme to seize the valuable assets of the person who once cherished him most.",
        ]
    ),
    # Dlg 08 (Host): 9 lines (+2)
    (
        "**HOST** *(slowly, reconstructing the fateful moments leading to the tragedy)*:",
        [
            "To comprehend this harrowing tragedy, we must rewind the clock to the fateful afternoon of May 4.",
            "Nguyen Phuong Linh arrived at the G4 apartment in the completely relaxed and trusting spirit of an old companion.",
            "The two had shared bright university years together, filled with fond memories and mutual affection.",
            "Linh remained completely oblivious to the fact that her gentle former partner had sunken deep into a quagmire of gambling debts.",
            "Throughout their conversation, Nghia maintained an amiable expression, yet his mind was cold-bloodedly calculating how to secure her scooter and laptop.",
            "He patiently waited for the exact moment when the victim was most off-guard to strike from behind, depriving her of any defensive reaction.",
            "The crime was carried out with chilling premeditation, extinguishing a young woman's vibrant life merely to resolve trivial financial deadlocks.",
            "The victim's luxury scooter and modern laptop represented, in the killer's eyes, an immediate lifeline to redeem his own pawned belongings.",
            "Material greed and financial desperation completely wiped away the sacred innocence of their past romance.",
        ]
    ),
    # Dlg 09 (Investigator): 8 lines (+2)
    (
        "**INVESTIGATOR** *(firm and authoritative, analyzing criminal methodology and the familiarity trap)*:",
        [
            "Apartment 1101 in the G4 building belonged to Nghia's new romantic partner, who had entrusted him with the keys while visiting her hometown.",
            "Nghia deliberately exploited this prolonged absence to convert the apartment into an airtight lethal trap.",
            "He proactively reached out and arranged a rendezvous with Nguyen Phuong Linh, his university sweetheart, under the pretext of catching up.",
            "The victim entered the private residence entirely voluntarily without the slightest inkling of suspicion.",
            "Their past intimacy served as the fateful key that unlocked the door leading the victim directly into catastrophe.",
            "After fatally assaulting the victim to plunder her property, the suspect casually sanitized the premises and pawned her motorcycle and computer.",
            "The subject systematically weaponized the established trust of his former girlfriend to isolate her in a completely enclosed domain.",
            "This was an exceptionally cold-blooded modus operandi, transforming someone's genuine goodwill into a vehicle for violent robbery.",
        ]
    ),
    # Dlg 10 (Investigator): 8 lines (+2)
    (
        "**INVESTIGATOR** *(firm and authoritative, analyzing the suspect's testimony and post-offense conduct)*:",
        [
            "Following the homicide, Nguyen Duc Nghia's behavior displayed a degree of composure that sent shivers down one's spine.",
            "He did not panic or flee the scene immediately like impulsive perpetrators of crimes of passion.",
            "The subject spent extensive hours systematically scrubbing surfaces, disposing of materials, and attempting to eradicate biological evidence.",
            "He transported the victim's scooter and laptop to a pawnshop on Dang Dung Street to settle debts and redeem his own pawned items.",
            "Remarkably, the subject even operated the victim's mobile phone to dispatch deceptive text messages to her relatives, manufacturing a false alibi.",
            "Such methodical, step-by-step premeditated conduct unequivocally demolished any defense asserting an impulsive crime provoked by jealousy.",
            "He utilized the proceeds plundered from the victim's property to pay off gambling bookmakers and retrieve his own previously mortgaged motorbike.",
            "Every consecutive action, from pawning items to broadcasting fraudulent messages, demonstrated a premeditated sequence of self-preservation.",
        ]
    ),
    # Dlg 11 (Psychologist): 6 lines
    (
        "**PSYCHOLOGIST** *(academic, dissecting compartmentalization and emotional numbness)*:",
        [
            "The phenomenon of an individual eating, sleeping, and residing serenely inside an apartment that just hosted a homicide exemplifies Compartmentalization.",
            "In clinical psychology, compartmentalization represents the subconscious mechanism of partitioning awareness into hermetically sealed mental vaults.",
            "The perpetrator isolates the criminal deed into a dark, segregated chamber, allowing remaining compartments to conduct daily social routines seamlessly.",
            "He could laugh with acquaintances and converse casually with his current partner without his nervous system triggering guilt or panic alarms.",
            "This reflects neither temporary insanity nor psychosis, but rather a severe manifestation of Pathological Emotional Numbness.",
            "The subject had totally extinguished affective empathy, perceiving fellow human beings merely as utilitarian objects or obstacles to be cleared away.",
        ]
    ),
    # Dlg 12 (Psychologist): 8 lines (+2)
    (
        "**PSYCHOLOGIST** *(academic, dissecting gambling addiction and moral degeneration)*:",
        [
            "It must be emphasized that compulsive gambling is not merely an unsavory vice, but a recognized neurobiological disorder that alters brain circuitry.",
            "When individuals sink into chronic gambling debt, cognitive executive function and moral judgment centers suffer catastrophic degradation.",
            "Relentless debt pressure activates chronic hyper-stress, plunging the subject into severe tunnel vision.",
            "He fixates solely upon an immediate objective: obtaining cash instantaneously to resolve the existential crisis threatening his self-image.",
            "All moral values, past relationships, and reverence for human sanctity are pulverized beneath this relentless psychological mechanism.",
            "The confluence of a covert narcissistic personality and compulsive gambling deadlock formed the volatile catalyst culminating in homicide.",
            "For those ensnared within the gambler's psychological ruin, the delusion of recouping losses is inevitably shadowed by moral decay.",
            "They will brazenly trample every ethical boundary merely to preserve their deceptive persona before family and community.",
        ]
    ),
    # Dlg 13 (Psychologist): 5 lines
    (
        "**PSYCHOLOGIST** *(profoundly analyzing psychological manipulation and betrayal of trust)*:",
        [
            "Another deeply unsettling dimension of the perpetrator's behavior was his capacity for sophisticated psychological manipulation.",
            "He deceived not only the victim, but also converted his current romantic partner into an unwitting human shield concealing his crime.",
            "Permitting his partner to return to the apartment shortly after committing atrocities demonstrated an astounding level of affective callousness.",
            "The subject genuinely believed he could orchestrate external reality through fabricated explanations delivered with plausible charm.",
            "This represents the classic hallmark of the Covert Antisocial Personality: articulate and charming externally, yet utterly hollow morally.",
        ]
    ),

    # Act 3 (Total: 49 sentences)
    # Dlg 14 (Host): 6 lines
    (
        "**HOST** *(in a grave tone, depicting the high-stakes interrogation)*:",
        [
            "Following a relentless manhunt lasting less than twenty-four hours after the corpse was uncovered, the suspect was apprehended in Thai Nguyen.",
            "The iron door of the interrogation chamber at Hanoi Criminal Police Headquarters slammed shut, initiating a suffocating battle of wits.",
            "Seated before veteran detectives was a bespectacled young man projecting an attitude of icy, deliberate composure.",
            "He believed his elaborate disposal plan had severed all physical evidentiary links tying him to the crime scene.",
            "An educated individual frequently harbors intellectual arrogance, convinced his own logic can outmaneuver the mechanisms of the law.",
            "Yet he failed to comprehend that every fabricated falsehood constructed was merely another knot tightening around his own future.",
        ]
    ),
    # Dlg 15 (Host): 8 lines (+2)
    (
        "**HOST** *(slowly, detailing the collapse of the manufactured alibi)*:",
        [
            "Throughout his fugitive escape, Nguyen Duc Nghia nurtured the illusion that law enforcement could never retrace his footsteps.",
            "He trusted that discarding identifying remains into a river in Quang Ninh and relocating the torso to the rooftop would render the case an unsolvable mystery.",
            "He retreated to Thai Nguyen, lodging at the home of a distant relative and preserving a relaxed demeanor as if returning from a vacation.",
            "Yet the net of justice is vast and unyielding; Hanoi detectives mobilized dozens of operational strike teams with unswerving determination.",
            "Every movement of the subject, from the pawnshop transactions to communication logs, was gathered and analyzed minute by minute.",
            "When handcuffs snapped around the killer's wrists in the dead of night, his illusion of a flawless crime disintegrated completely.",
            "At the precise moment handcuffs restrained him in Thai Nguyen, Nghia's everyday aura of relaxed confidence vanished without a trace.",
            "He understood that the prestigious academic mask he had fought so desperately to maintain had finally shattered before the law.",
        ]
    ),
    # Dlg 16 (Investigator): 8 lines (+2)
    (
        "**INVESTIGATOR** *(authoritative and razor-sharp, detailing the strategy to dismantle deceit)*:",
        [
            "Confronting educated and psychologically fortified suspects like Nguyen Duc Nghia, a blunt frontal interrogation proves ineffective.",
            "We deployed a strategy of logical encirclement, permitting the subject complete freedom to elaborate his contradictory rationalizations.",
            "When Nghia insisted he had merely inadvertently stained the apartment during an accidental nosebleed, we systematically laid forensic evidence on the table.",
            "Microscopic blood spatters behind the bookshelf, pawn tickets for the victim's scooter, and corroborating statements from pawnshop witnesses.",
            "Most decisively, retrieved surveillance footage and cellular triangulation data completely smashed the suspect's fortified lines of defense.",
            "Witnessing his intricate logical fortress collapse, the veneer of false composure across his face began to fracture into pieces.",
            "Targeted professional inquiries zeroing in on unaccounted chronological intervals backed the suspect into an untenable corner.",
            "The intellectual vanity of a former elite university student quickly surrendered before the seasoned expertise of detectives at Number 7 Thien Quang.",
        ]
    ),
    # Dlg 17 (Investigator): 8 lines (+2)
    (
        "**INVESTIGATOR** *(composed and razor-sharp, recounting psychological transitions in custody)*:",
        [
            "When transferred to headquarters at Number 7 Thien Quang Street, Nguyen Duc Nghia's initial posture was obstinacy and evasive maneuvering.",
            "He persistently attempted to blame external circumstances, claiming he had experienced emotional distress and sudden provocation.",
            "Nonetheless, investigators patiently persevered, methodically illuminating the stark contradictions between his testimony and his premeditated preparations.",
            "Faced with unassailable logic and irrefutable physical proof, the subject's final protective wall crumbled irrevocably.",
            "He was compelled to lower his head, confess every detail of his criminal acts, and direct authorities to the locations where evidence had been discarded.",
            "That marked the precise moment intellectual arrogance was utterly subjugated before the authority of the law and human conscience.",
            "Across multiple handwritten pages of confession, the subject was forced to acknowledge the premeditated scheme to murder for robbery.",
            "His trembling pen strokes on the white paper officially brought an end to every calculated attempt at evasion.",
        ]
    ),
    # Dlg 18 (Psychologist): 6 lines
    (
        "**PSYCHOLOGIST** *(astutely dissecting the collapse of the narcissistic ego)*:",
        [
            "The moment irrefutable scientific proof was unveiled marked the exact instant the narcissistic ego sustained a catastrophic shock.",
            "The perpetrator recognized that the flawless intellectual persona he had painstakingly curated over years was irrevocably demolished.",
            "The autonomic nervous system immediately responded with acute panic: pupils dilated, respiration accelerated, and his gaze trembled uncontrollably.",
            "When denial of reality became mathematically impossible, the subject's psyche defaulted to intense self-pity.",
            "He began realizing the cataclysmic societal retribution crashing down upon him, a ruin that completely overwhelmed his fragile inner core.",
            "This represented the decisive psychological inflection point, propelling the suspect from extreme arrogance into theatrical torment before the judicial bench.",
        ]
    ),
    # Dlg 19 (Psychologist): 6 lines
    (
        "**PSYCHOLOGIST** *(academic, analyzing psychological defense mechanisms facing retribution)*:",
        [
            "The transition from stubborn defiance to confession in the interrogation room represents an inevitable psychological trajectory as defense energies deplete.",
            "The human brain cannot sustain complex, multi-layered deception across prolonged periods under high-intensity investigative scrutiny.",
            "When fabricated narratives rupture, cognitive dissonance reaches a critical crescendo, compelling the subject to confess to relieve unbearable internal tension.",
            "However, acknowledging criminal acts does not automatically equate to authentic, heartfelt repentance.",
            "It frequently constitutes merely a mechanical surrender before the sheer weight of incontrovertible evidence and irreversible reality.",
            "The arduous passage from legal surrender to genuine moral awakening remains an intensely agonizing and conflicted psychological journey.",
        ]
    ),
    # Dlg 20 (Investigator): 7 lines (+2)
    (
        "**INVESTIGATOR** *(authoritative, detailing the multi-provincial search for physical evidence)*:",
        [
            "To solidify the indictment beyond all reasonable doubt, the special task force spared no effort in recovering discarded evidence.",
            "For consecutive days and nights, police officers and specialized divers searched every meter along the Cam River in Dong Trieu, Quang Ninh Province.",
            "Beneath the murky depths and swift currents, locating small items discarded days earlier presented an immensely formidable ordeal.",
            "Yet upholding the highest devotion to human sanctity and judicial integrity, our units resolutely refused to abandon the mission.",
            "When critical evidentiary components were recovered and DNA matching confirmed identity unequivocally, the prosecutorial dossier became an airtight indictment.",
            "The tireless recovery efforts of the investigative force restored complete truth to the victim's grieving family.",
            "It stood as a resounding affirmation that no criminal disposal can ever remain permanently buried beneath deep waters.",
        ]
    ),

    # Act 4 (Total: 47 sentences)
    # Dlg 21 (Host): 8 lines (+2)
    (
        "**HOST** *(slowly, entering the courtroom and the core theme of genuine remorse)*:",
        [
            "In July 2010, the Hanoi People's Court formally convened the first-instance trial of the case.",
            "The judicial proceedings captivated the dedicated attention of millions of citizens nationwide.",
            "Within the courtroom, the public observed intensely intricate and contradictory psychological transformations among the parties involved.",
            "Above all lingered the profound inquiry that troubled every observer: What constitutes the true essence of remorse?",
            "Why would a perpetrator who executed such chilling brutality suddenly break into convulsive weeping and plead for death before television cameras?",
            "Did this signal an authentic awakening of conscience, or merely a novel psychological mask to escape humiliating public condemnation?",
            "The atmosphere inside the courtroom was suffocating as the killer stood face to face with the portrait of his former girlfriend.",
            "Those tears streaming down behind his spectacles became the focal point of impassioned public debate across the country.",
        ]
    ),
    # Dlg 22 (Investigator): 7 lines (+1)
    (
        "**INVESTIGATOR** *(composed, providing perspectives on the accessory and the two fathers)*:",
        [
            "During the trial, the new girlfriend, Hoang Thi Yen, was prosecuted for failing to report a crime.",
            "Her belated tears reflected profound disorientation upon realizing that the man she loved was the embodiment of malice.",
            "Yet the most agonizing tragedy belonged to the two fathers standing on opposite poles of the courtroom.",
            "Nguyen Van Ba, the victim's father, who had endured unspeakable grief while trekking alongside detectives to recover his daughter's remains.",
            "And Nguyen Duc Hung, the perpetrator's father, a dignified patriarch bowing his head in sheer despair to beg forgiveness for his son.",
            "The sight of two aging fathers confronting each other in court stood as the most heartbreaking testament to the collateral devastation of reckless crime.",
            "The legal accountability imposed upon the new girlfriend served as an unequivocal warning against turning a blind eye to wrongdoing.",
        ]
    ),
    # Dlg 23 (Ordinary Person N2): 5 lines
    (
        "**ORDINARY PERSON** *(N2 - Hoang Thi Yen, voice trembling with immense remorse)*:",
        [
            "I never could have imagined that my affection and trust would be exploited to facilitate such a horrific crime.",
            "When I returned home and noticed fresh paint and faint stains on the bookshelves, I questioned him and believed his claim that he had suffered a nosebleed.",
            "I engaged in self-deception because I lacked the courage to fathom that the man I loved could ever commit an unthinkable deed.",
            "Yet when detectives knocked on my door, the brutal reality crashed down, leaving me utterly paralyzed and broken.",
            "The suspended fifteen-month sentence was the bitterest lesson of my life, but the enduring agony of conscience before the victim's family remains the heaviest sentence that will haunt me forever.",
        ]
    ),
    # Dlg 24 (Psychologist): 8 lines (+2)
    (
        "**PSYCHOLOGIST** *(profoundly analyzing remorse and survival conflicts)*:",
        [
            "Psychologically, the subject's tears and theatrical plea for execution at the first trial represented an acute Narcissistic Ego Injury.",
            "When a narcissistic persona is unmasked before the public, subjective humiliation and intense self-disgust reach an excruciating peak.",
            "His request for death did not necessarily equate to genuine empathy for the victim's suffering, but rather an unconscious impulse to extinguish his own unbearable shame.",
            "The empirical proof arrived immediately after the trial: once the theatrical hysteria subsided, biological survival instincts surged back.",
            "The defendant filed an appeal begging for clemency, revealing the profound chasm between performative remorse and visceral dread of mortality.",
            "Authentic remorse only crystallizes through prolonged introspection, when the ego ceases self-pity and genuinely internalizes the irreversible void inflicted upon others.",
            "The dramatic pendulum swing between demanding execution and submitting an appeal laid bare the fragility of a narcissistic personality confronting accountability.",
            "He dreaded public disgrace, yet he harbored far greater terror regarding the permanent termination of his own biological existence.",
        ]
    ),
    # Dlg 25 (Host): 7 lines (+1)
    (
        "**HOST** *(slowly, depicting the deepening tragedy following the trial)*:",
        [
            "The capital sentence pronounced at the first-instance trial was met with overwhelming societal consensus.",
            "Yet the profound tragedy enveloping the families on both sides lingered like an open wound that time could never heal.",
            "For the victim's family, the agonizing loss of a vibrant daughter left an eternal void that no judicial penalty could ever fill.",
            "And for the perpetrator's family, public shame and despair drove an honorable household into utter devastation.",
            "Most heartbreakingly, the tragic demise of the perpetrator's father in a road collision on October 30, 2010, piled catastrophe upon catastrophe.",
            "It was a harrowing testament to fate, wherein elderly parents were forced to bear the most agonizing cross for the sins of their children.",
            "The sudden passing of his father on the eve of the appellate trial drew a sorrowful curtain over a once-respectable family.",
        ]
    ),
    # Dlg 26 (Psychologist): 7 lines (+1)
    (
        "**PSYCHOLOGIST** *(profoundly summarizing psychological shifts in the final days)*:",
        [
            "During his final years in the solitary confinement of death row, Nguyen Duc Nghia's psychological landscape underwent profound shifts.",
            "As every legal avenue closed and life was measured in dwindling days, the former arrogant narcissistic ego evaporated entirely.",
            "Following the rejection of his appeal, the condemned man submitted a clemency petition to the State President, pleading for a chance to atone through life.",
            "At this juncture, remorse was no longer performative tears before cameras or self-serving rationalizations.",
            "It was an absolute silence beneath the crushing gravity of guilt, an acute realization of the catastrophic ruin he had inflicted on both families and society.",
            "His execution by lethal injection on July 22, 2014, drew the final curtain on a man who once possessed everything, only to forfeit it all to moral depravity.",
            "Those long years spent facing the four walls of death row completely stripped away every vestige of intellectual hubris from a fallen scholar.",
        ]
    ),
    # Dlg 27 (Psychologist): 5 lines
    (
        "**PSYCHOLOGIST** *(academic, analyzing crowd psychology and social retribution)*:",
        [
            "The social shockwaves emanating from the Nguyen Duc Nghia trial generated an unprecedented tsunami of public outrage.",
            "The collective demand for the harshest statutory punishment reflected the vigorous awakening of society's collective moral immune system.",
            "When fundamental boundaries of human decency are transgressed with extreme savagery, society reflexively triggers punitive instincts to preserve common values.",
            "Yet, the boundary between legitimate demands for justice and indiscriminate vengeful hostility can often become exceedingly fragile.",
            "What proved most admirable was that amid that tempest of public fury, the victim's family maintained profound dignity and composure in court.",
        ]
    ),

    # Act 5 (Total: 38 sentences)
    # Dlg 28 (Host): 7 lines (+1)
    (
        "**HOST** *(slowly, delivering the final verdict and the redemption of compassion)*:",
        [
            "The appellate court subsequently dismissed the appeal, upholding the capital sentence for Nguyen Duc Nghia.",
            "After his clemency petition was officially denied, the death sentence was carried out in July 2014.",
            "The definitive sanction of the law closed the ledger on one of the darkest criminal dossiers in modern memory.",
            "Yet behind that stern sentence, the element that moved hearts most profoundly was the transcendent grace of human compassion.",
            "When the perpetrator's father tragically perished in a traffic accident, the victim's own father sent condolences and memorial flowers.",
            "That noble humanitarian gesture transcended all vengeance, proving that the shadows of crime can never extinguish the light of human benevolence.",
            "The extraordinary magnanimity of the victim's father planted an unshakeable faith in the redemption of empathy amidst overwhelming grief.",
        ]
    ),
    # Dlg 29 (Investigator): 7 lines (+2)
    (
        "**INVESTIGATOR** *(composed, summarizing investigative lessons and the value of justice)*:",
        [
            "The Nguyen Duc Nghia case dossier stands as a historic benchmark in combating urban crime and technologically assisted offenses.",
            "It affirms an immutable truth: no matter how cunning a perpetrator's schemes, forensic science and investigative acumen will inevitably unmask the truth.",
            "Every biological trace and micro-droplet constitutes an unyielding voice testifying against criminality before the light of justice.",
            "The swift resolution of this case not only delivered closure for the deceased, but also issued a stern warning to anyone tempted to betray basic humanity.",
            "Justice may traverse grueling battles of wits, but it will never retreat before the dark.",
            "The triumph of this special investigation demonstrated the discipline, professional sharpness, and devotion of the capital city's police force.",
            "Every thoroughly solved case builds another solid pillar reinforcing societal faith in the majesty of the rule of law.",
        ]
    ),
    # Dlg 30 (Ordinary Person N1): 5 lines
    (
        "**ORDINARY PERSON** *(N1 - G4 resident, speaking in a reflective and awakened tone)*:",
        [
            "Many years have elapsed since that unforgettable summer, and daily existence at the G4 complex has returned to its peaceful rhythm.",
            "Yet for those who lived through those harrowing days, memories of the tragedy endure as a profound, perpetual reminder.",
            "We have learned to genuinely care for our neighbors, abandoning the indifferent and insulated posture of the past.",
            "Community cohesion and vigilance toward the unusual constitute the strongest fortress shielding every domestic hearth.",
            "We pray that the soul of the departed finds eternal peace, and that such an unthinkable tragedy never recurs anywhere again.",
        ]
    ),
    # Dlg 31 (Psychologist): 7 lines (+2)
    (
        "**PSYCHOLOGIST** *(calm, summarizing three core red-flag survival principles)*:",
        [
            "From the Nguyen Duc Nghia case, behavioral psychology synthesizes three essential red-flag survival principles for every individual.",
            "First, never permit the Intellectual Halo Effect or family background to disarm your personal danger reflexes.",
            "Second, maintain vigilance against the Familiarity Trap; never agree to meet privately with anyone exhibiting severe distress or debt in closed quarters.",
            "Third, respect and obey your survival intuition; upon detecting sudden behavioral anomalies or deceit, seek external support without delay.",
            "A profound comprehension of criminal psychology serves as the sturdiest shield safeguarding ourselves and our loved ones from deceptive hazards.",
            "Never allow social politeness or blind trust to shepherd you into high-risk environments beyond your control.",
            "Vigilance and self-preservation skills do not make us cynical paranoids; they empower us to live safely and responsibly.",
        ]
    ),
    # Dlg 32 (Psychologist): 6 lines (+1)
    (
        "**PSYCHOLOGIST** *(humanistic, expanding upon post-traumatic growth and forgiveness)*:",
        [
            "The forgiveness and magnanimity exhibited by the victim's father toward the perpetrator's family exemplifies Post-Traumatic Growth.",
            "In psychology, forgiveness does not mean erasing the crime or sanctioning the malice committed.",
            "Forgiveness represents the ultimate act of courage to liberate oneself from the self-destructive prison of resentment and agony.",
            "By dispatching condolences and funeral flowers for the killer's deceased father, the victim's father terminated an endless chain reaction of hatred.",
            "It offers the most profound lesson on human strength: evil can extinguish a mortal life, but it can never annihilate dignity and empathy within our souls.",
            "Only authentic human empathy can truly heal the deepest wounds that seem impossible to close within the human spirit.",
        ]
    ),
    # Dlg 33 (Host): 6 lines
    (
        "**HOST** *(in a warm tone, concluding the episode with a profound humanistic message)*:",
        [
            "Our journey decoding criminal psychology alongside Amber Eyes seeks not to stoke fear or vindictive wrath.",
            "Our ultimate purpose is to illuminate human consciousness, fostering deeper understanding of the labyrinthine corridors within the human psyche.",
            "The immaculate mask of malice may deceive transient glances, but vigilance and compassion will forever serve as the lighthouse guiding justice.",
            "Please cherish every precious moment of existence, listen to the voice of conscience, and maintain vigilance against temptation.",
            "Thank you, esteemed audience, for consistently accompanying our channel through every investigative dossier.",
            "Farewell, and we look forward to reuniting with you in our upcoming journeys.",
        ]
    ),
]

JA_SECTIONS = [
    # Act 1 (Total: 53 sentences)
    # Dlg 00 (Host): 10 lines
    (
        "**ホスト** *(低く落ち着いた声で、歴史的ドキュメンタリーの重厚感を漂わせながら)*:",
        [
            "2010年5月中旬、ハノイ市チュンイエン地区の高層マンションG4で起きた戦慄すべき事件は、ベトナム社会全体に巨大な衝撃を与えました。",
            "首都屈指の近代的な文化都市の只中で、これほどまでに残虐極まりない凶行が隣室で密かに進行していたとは、誰も想像すらしていませんでした。",
            "現代の都市生活者たちは頑丈な鉄扉の背後に身を隠し、自らの安全は完全に保障されていると信じ切っています。",
            "外界がいかに混沌としていようとも、高層階の居室だけは侵すべからざる孤立した聖域であると思い込んでいるのです。",
            "しかし、その閉鎖性と集合的無関心こそが、結果として極めて危険な「都市の死角」を作り出してしまいました。",
            "近代的な集合住宅において、隣家から微かに漏れ聞こえる異音に注意を払ったり詮索したりする者はほとんどいません。",
            "快適な日常と多忙な日々の生活リズムが、生命の危機に対する人間の生来の警戒本能を麻痺させてしまったのです。",
            "悪意は自らの凶行を果たす場所として、薄暗い裏路地や郊外の荒れ地を選ぶことはありませんでした。",
            "それは模範的な高級高層マンションの華麗な外観の背後に巧妙に身を潜め、あらゆる防犯網と日常の常識をあざ笑ったのです。",
            "ベトナムの司法史において最も衝撃的な殺人事件の一つは、まさにこのような息苦しい都市空間の密室から幕を開けました。",
        ]
    ),
    # Dlg 01 (Host): 7 lines
    (
        "**ホスト** *(静かに言葉を紡ぎ、家族の背景と失踪の悲劇に迫る)*:",
        [
            "5月17日午後に事件が発覚するまでの間、被害者の家族はおよそ2週間にわたり絶望の淵を彷徨っていました。",
            "グエン・フオン・リンさんは、2010年5月4日の夕方に自宅を出たまま、完全に消息を絶ちました。",
            "彼女の携帯電話は一切通じなくなり、すべてのソーシャルメディアの更新も突然途絶えてしまったのです。",
            "娘を心から愛していた父親のグエン・ヴァン・バー氏は、失踪した初日の夜からただならぬ不吉な予感を抱いていました。",
            "彼は直ちに警察へ捜索願を提出し、親族と共に娘の交友関係を必死に調べ上げました。",
            "しかし、数百万人もの人々が蠢く巨大都市の中で、謎の失踪を遂げた若い女性を捜し出すことは、砂漠で一粒の針を探すようなものでした。",
            "その失踪の謎を握る鍵が、学生時代に初めて交際した元恋人の手に握られていようとは、夢にも思わなかったのです。",
        ]
    ),
    # Dlg 02 (Investigator): 8 lines (+2)
    (
        "**捜査官** *(沈着かつ鋭利な口調で、初動の現場検証を振り返る)*:",
        [
            "2010年5月17日午後、警察本部はG4マンションの管理事務所および住民から戦慄の通報を受理しました。",
            "マンション最上階の屋上、機械室とゴミ投下口が設置された薄暗いエリアにおいて、激しく腐敗した女性の遺体が発見されたのです。",
            "捜査員一同を震撼させたのは、現場が単なる事故や偶発的な争いによるものでは決してないという事実でした。",
            "犯人は被害者の身元特定を阻むため、意図的に頭部および両手の指先10本を完全に切除していたのです。",
            "これは極めて残忍であり、当時の刑事事件でも類を見ないほど綿密に計算された証拠隠滅工作でした。",
            "犯人の明白な狙いは被害者の身元を徹底的に抹殺し、事件を身元不明の迷宮入り死体として処理させて捜査を逃れることでした。",
            "しかし、犯人が企てた巧妙な身元偽装工作も、科学捜査研究所の専門的な鑑定技術を欺くことはできませんでした。",
            "その日の夜のうちに、屋上現場に残された微細な生体試料と隆線紋様はすべて緊急鑑定へと回されました。",
        ]
    ),
    # Dlg 03 (Investigator): 9 lines (+2)
    (
        "**捜査官** *(冷徹な口調で、科学捜査と痕跡追跡の成果を解説する)*:",
        [
            "G4マンション屋上の現場において、遺体検分と鑑識活動は極めて慎重に進められました。",
            "遺体が遺棄されていた場所は屋上の機械室フロアの死角であり、一般の住民が立ち入ることは滅多にありませんでした。",
            "法医学鑑定員は、階段室へと逆方向に続いている微かな引きずり痕と生体反応を捉えました。",
            "完全に拭き取られずに残っていた微小な血痕を一つ一つ追跡していくと、犯人の足取りは11階の廊下へと真っ直ぐ導かれていました。",
            "そして1101号室の室内において、捜査本部は隠蔽しきれなかった決定的な異常を発見したのです。",
            "鼻を突く化学洗剤の強い刺激臭と、飛び散った痕跡を隠すために壁面に急遽塗り重ねられた真新しいペンキの跡でした。",
            "それらの不自然な隠滅の試みこそが、ここが第一の犯行現場であることを雄弁に物語る動かぬ証拠となりました。",
            "特殊な紫外線ライトとルミノール試薬の化学反応により、白いペンキの奥やドア枠の隙間に隠された微細な血痕が鮮やかに発光しました。",
            "何度も入念に清掃された表面であっても、現代の鑑識技術が真実を暴き出せることを、犯人は計算しきれていなかったのです。",
        ]
    ),
    # Dlg 04 (Ordinary Person N1): 5 lines
    (
        "**一般人** *(N1 - G4マンション住民、恐怖に声を震わせながら)*:",
        [
            "事件の数日前から、非常階段や吹き抜けのダクトのあたりで酷い悪臭が漂っていることには気づいていました。",
            "けれど誰もが、排水溝のネズミの死骸か、長期間放置された家庭ゴミの臭いだろうと思い込んでいたのです。",
            "まさか自分たちの部屋の真上に、そのようなおぞましい悪夢が横たわっているなどとは、誰一人想像もできませんでした。",
            "マンション中が底知れぬパニックに陥り、どの家庭も二重に鍵をかけ、子供たちを廊下に出すことすら禁じました。",
            "何よりも背筋が凍ったのは、その凶悪犯が毎日のように私たちと同じエレベーターに乗り合わせていたかもしれないという恐怖でした。",
        ]
    ),
    # Dlg 05 (Psychologist): 8 lines (+2)
    (
        "**心理学者** *(穏やかで知的な口調で、社会心理メカニズムとハロー効果を解明する)*:",
        [
            "行動心理学の観点から見れば、この悲劇は「知性のハロー効果」と「社会的防御反射の麻痺」という罠を浮き彫りにしています。",
            "現代社会は高い学歴、洗練された容姿、そして良家育ちという属性を、道徳的な善良さと無意識に結びつけてしまいがちです。",
            "書生風の端正な風貌に眼鏡をかけ、言葉遣いも丁寧な人物を前にすると、周囲の人間の心理的警戒網はほぼ完全に解除されてしまいます。",
            "その好意的な先入観こそが、自己愛的な破壊衝動や人格的歪曲が水面下で増殖するための完璧なカモフラージュとなってしまったのです。",
            "さらに、大都市特有の「傍観者効果」が、凶行が何ら邪魔されることなく遂行される環境を決定づけました。",
            "大衆の無関心は冷酷さからではなく、「誰か他の人が通報するだろう」という責任の分散メカニズムによって引き起こされます。",
            "閉鎖的な都市空間において、住戸間の物理的な距離は至近でありながら、心理的な距離は果てしなく隔絶されています。",
            "そのような社会的絆の断絶が、意図せずして近代的なマンションを犯罪者の格好の死角へと変貌させてしまったのです。",
        ]
    ),
    # Dlg 06 (Psychologist): 6 lines
    (
        "**心理学者** *(深層心理に迫り、被害者の人間性剥奪行為を分析する)*:",
        [
            "被害者の頭部と10本の指先を切除した行為は、この事件記録において最も重篤な心理的指標の一つです。",
            "行動科学において、これは「被害者の個体識別抹殺」、すなわち人格の脱個性化と呼ばれる現象です。",
            "犯人は鑑識捜査による身元特定を単に妨害しようとしただけではありませんでした。",
            "無意識の深層において、この行為は自らが引き起こした凶行に対する犯人自身の極限の恐怖を反映していたのです。",
            "かつて愛し合い抱きしめた女性の眼差しや顔立ちを、彼は直視し続ける勇気を持てませんでした。",
            "被害者を顔のない物体へと変えることで、自分は人間を殺したのではなく、単に不要な障害物を片付けたのだと自らの心を偽ったのです。",
        ]
    ),

    # Act 2 (Total: 53 sentences)
    # Dlg 07 (Host): 9 lines
    (
        "**ホスト** *(静かに、外見の背後に隠された冷酷な真実を描き出す)*:",
        [
            "容疑者の素性が次第に明らかになるにつれ、社会全体が激しい心理的地殻変動に見舞われました。",
            "凶行の黒幕は、裏社会のアウトローや前科を重ねた凶悪犯などではありませんでした。",
            "それは、国内屈指の難関名門国立大学である外国貿易大学の優秀な元学生、グエン・ドゥック・ギアだったのです。",
            "彼は港湾都市ハイフォンの厳格な家庭で育ち、父親は周囲から深く尊敬される退役軍人でした。",
            "ギア自身も友人や恩師の前では、常に礼儀正しく知性にあふれた好青年という完璧なイメージを保っていました。",
            "しかし、その知的な眼鏡の奥底には、自堕落で危険なサッカー賭博に溺れる闇の私生活が潜んでいたのです。",
            "雪だるま式に膨れ上がった借金は、肥大化した自己愛を逃げ場のない破滅の袋小路へと追い詰めました。",
            "彼は家族や友人の前で、自らが誇る完璧なエリート像が崩壊することを決して受け入れられませんでした。",
            "プライドを守り抜くため、彼は自らを最も深く愛してくれた人物の財産を強奪するという冷酷な計画を企てたのです。",
        ]
    ),
    # Dlg 08 (Host): 9 lines (+2)
    (
        "**ホスト** *(静かに、事件直前の運命的な時間軸を再現する)*:",
        [
            "この悲劇の深層を理解するためには、運命の日となった5月4日の午後に時計の針を戻さねばなりません。",
            "グエン・フオン・リンさんは、懐かしい旧友に再会する完全に打ち解けた穏やかな心境でG4マンションを訪れました。",
            "二人はかつて学生時代の輝かしい青春を共に過ごし、多くの美しい思い出を分かち合った間柄でした。",
            "かつての優しい恋人が、今や破滅的な賭博の借金地獄に飲み込まれていることなど、彼女は露ほども知りませんでした。",
            "歓談の最中もギアは穏やかな笑みを浮かべていましたが、その脳裏では彼女の高級スクーターと高価なノートパソコンを奪う算段が冷酷に巡っていました。",
            "彼は被害者が最も警戒を解いた瞬間を冷徹に見計らい、抵抗の機会を一切与えずに背後から凶行に及んだのです。",
            "その凶行は冷酷な計算づくで実行され、卑小な金銭的困窮を打開するためだけに、一人のうら若き女性の命を無慈悲に奪い去りました。",
            "被害者の高価なスクーターとパソコンは、犯人にとって自らが以前質入れした物品を取り戻すための生命線に過ぎなかったのです。",
            "金銭への執着と借金苦という暗雲が、清らかだった初恋の記憶を完全に塗りつぶしてしまいました。",
        ]
    ),
    # Dlg 09 (Investigator): 8 lines (+2)
    (
        "**捜査官** *(毅然とした口調で、手口と親近感の罠を分析する)*:",
        [
            "G4マンション1101号室は元々、ギアの現在の交際相手の住居であり、彼女が帰省する際に鍵の管理を信頼して預けられたものでした。",
            "ギアはその不在を狡猾に悪用し、この部屋を完全な密室の殺人トラップへと変貌させたのです。",
            "彼は大学時代の元恋人であるリンさんに自ら連絡を入れ、昔話をする口実で部屋へと呼び出しました。",
            "被害者は完全に自発的な意志で、何の警戒心も抱かずにその部屋へと足を踏み入れました。",
            "過去の親密な信頼関係こそが、被害者を悲劇へと引きずり込む運命の鍵となってしまったのです。",
            "財産を強奪するために被害者を殺害した後、容疑者は何食わぬ顔で現場を清掃し、バイクとパソコンを質屋へと持ち込みました。",
            "容疑者は元恋人が抱いていた無防備な信頼を極限まで利用し、完全に孤立した空間へと誘い込みました。",
            "他者の純粋な善意を強盗殺人の道具へとすり替えた、極めて冷酷な手口でした。",
        ]
    ),
    # Dlg 10 (Investigator): 8 lines (+2)
    (
        "**捜査官** *(厳格な口調で、容疑者の供述と犯行後の行動を暴く)*:",
        [
            "犯行直後におけるグエン・ドゥック・ギアの行動は、背筋が凍るほどの異様な沈着さを示していました。",
            "彼は突発的な激情犯罪者のように、パニックに陥って現場から逃亡するようなことはありませんでした。",
            "容疑者は数時間もの時間を費やし、清掃と遺体の損壊、そして生体痕跡の隠蔽工作を機械的に遂行しました。",
            "彼は被害者のバイクとパソコンをダンズン通りの質屋に持ち込み、賭博の負債返済と自らの私物を請け出すための現金を手にしました。",
            "そればかりか、容疑者は被害者の携帯電話を操作して親族に偽装メッセージを送り、虚偽のアリバイ工作まで図ったのです。",
            "この組織的かつ段階的な冷徹な行動は、嫉妬による突発的な犯行であるという弁解を完全に粉砕するものでした。",
            "彼は強奪した金品を即座に賭博の清算と、以前自ら差し入れた原付バイクの請け出し費用へと充当していました。",
            "質入れから偽装メッセージの送信に至る一連の行動は、すべてが周到に計算された自己保身の連鎖でした。",
        ]
    ),
    # Dlg 11 (Psychologist): 6 lines
    (
        "**心理学者** *(学術的視点から、心の区画化メカニズムと感情の麻痺を解明する)*:",
        [
            "殺人を犯したまさにその現場の部屋で平然と生活し、飲食や睡眠をとることができた事実は、「心の区画化」の典型例です。",
            "心理学において区画化とは、脳が無意識のうちに認知を独立した密閉カプセルへと分断する防衛機制を指します。",
            "犯人は犯行の記憶を暗い孤立した区画へと隔離し、残りの区画では普段通りの社会生活を平然と継続させていたのです。",
            "友人たちと談笑し、現在の恋人と何食わぬ顔で会話を交わしても、彼の神経系はパニックや罪悪感の警報を発しませんでした。",
            "これは決して精神錯乱の証拠ではなく、むしろ病的な「感情麻痺」の顕著な兆候に他なりません。",
            "容疑者は他者への共感性を完全に消失させ、同胞の人間を単なる物体や片付けるべき障害物としか見なせなくなっていたのです。",
        ]
    ),
    # Dlg 12 (Psychologist): 8 lines (+2)
    (
        "**心理学者** *(学術的視点から、賭博中毒の心理と道徳的堕落を解き明かす)*:",
        [
            "サッカー賭博中毒は単なる悪癖ではなく、脳の構造的機能を著しく変容させる病的症候群であることを強調せねばなりません。",
            "ギャンブルの借金地獄に深く沈んでいくと、認知制御と倫理的判断を司る脳の中枢機能は深刻な機能不全に陥ります。",
            "執拗な借金の督促による極度のストレスは、対象者を極端な「トンネル視野」へと追い詰めます。",
            "自らの社会的自己崩壊を回避するため、今すぐ目の前の現金を確保することしか見えなくなってしまうのです。",
            "道徳的価値観や過去の情愛、そして人命への畏敬の念は、この病的な心理メカニズムによって完全に粉砕されました。",
            "隠蔽型自己愛パーソナリティと絶望的な賭博中毒の結合こそが、この未曾有の惨劇を引き起こした最も危険な火種でした。",
            "ギャンブラーの心理的罠に囚われた者において、損失を取り戻そうとする妄想は、倫理観の急速な崩壊と常に表裏一体です。",
            "家族や世間の前で自らの偽りの虚飾を維持するためなら、彼らはあらゆる道徳的境界線を平然と踏みにじるのです。",
        ]
    ),
    # Dlg 13 (Psychologist): 5 lines
    (
        "**心理学者** *(深層心理を分析し、心理操作の罠と裏切りを暴く)*:",
        [
            "犯人の行動におけるもう一つの恐るべき側面は、周囲の人間を巧妙にコントロールする高度な心理的操作能力でした。",
            "彼は被害者を騙しただけでなく、新たな交際相手をも自らの罪を隠蔽するための無自覚な人間の盾として利用したのです。",
            "残虐な凶行を終えた直後の部屋に恋人を迎え入れたという事実は、驚くべき感情の冷酷さを証明しています。",
            "もっともらしい虚偽の言い訳を弄することで、他者の認識を自由自在に操れると信じ込んでいたのです。",
            "これこそは隠蔽型反社会性パーソナリティの典型的な特徴です。外見は知性的で魅力的に見えながら、内面は道徳的に完全に空虚なのです。",
        ]
    ),

    # Act 3 (Total: 49 sentences)
    # Dlg 14 (Host): 6 lines
    (
        "**ホスト** *(張り詰めた空気の中、息詰まる取調室の攻防へといざなう)*:",
        [
            "遺体発見から24時間も経たない電撃的な捜査網の展開により、凶悪犯はタイグエン省において身柄を拘束されました。",
            "ハノイ市警察本部刑事局の重い鉄扉が閉ざされ、息詰まる心理戦の火蓋が切って落とされました。",
            "百戦錬磨のベテラン取調官の前に座る眼鏡の青年は、凍りつくような冷淡さと不敵な落ち着きを湛えていました。",
            "彼は自らが綿密に企てた証拠隠滅工作によって、犯行現場と自分を結びつける一切の物証は消滅したと信じ込んでいたのです。",
            "高い知性を誇る者は往々にして「知的な傲慢さ」を抱き、自らの論理で法の網を欺けると過信しがちです。",
            "しかし彼が気づいていなかったのは、重ねられた嘘の供述こそが、自らの未来を締め上げる首輪に他ならなかったということです。",
        ]
    ),
    # Dlg 15 (Host): 8 lines (+2)
    (
        "**ホスト** *(静かに、偽りのアリバイ網が崩壊していく過程を描く)*:",
        [
            "逃亡生活中、グエン・ドゥック・ギアは捜査機関が自らの足取りを決して掴めないだろうという甘い希望を抱き続けていました。",
            "クアンニン省の川に身元特定部位を投げ捨て、胴体を屋上に隠せば、事件は永遠の迷宮入りになると信じていたのです。",
            "彼はタイグエン省の遠縁の親戚宅に身を寄せ、何事もなかったかのように平然と振る舞い続けていました。",
            "しかし天網恢々疎にして漏らさず、ハノイ市警察の捜査陣は不退転の決意をもって数十もの追跡班を一斉に展開していました。",
            "質屋の足取りから通信履歴に至るまで、容疑者のあらゆる行動経路は分刻みで精密に分析されていたのです。",
            "真夜中に冷たい手錠がその手首に掛けられた瞬間、完全犯罪を夢見た彼の妄想は完全に水泡に帰しました。",
            "タイグエンで手錠をかけられたまさにその時、ギアが日常見せていた落ち着き払った自信は跡形もなく消え去りました。",
            "自らが必死に守り抜こうとした名門エリート学生の仮面が、司法の正義の前に完全に剥ぎ取られたことを悟ったのです。",
        ]
    ),
    # Dlg 16 (Investigator): 8 lines (+2)
    (
        "**捜査官** *(重厚かつ鋭利な口調で、欺瞞の鎧を打ち砕いた戦術を語る)*:",
        [
            "グエン・ドゥック・ギアのように高い教養を持ち周到な心理的準備を整えた容疑者に対し、正面からの威圧は通用しません。",
            "私たちは「論理的包囲戦術」を採用し、容疑者にまずは矛盾に満ちた自己弁護を自由に語らせる手法をとりました。",
            "部屋を汚したのは鼻血による単なる事故だとギアが主張した際、私たちは科学捜査によって得られた動かぬ物証を次々と突きつけました。",
            "本棚の裏側に微小に残存していた血痕、被害者のバイクを質入れした伝票、そして質屋店主の決定的な証言記録です。",
            "とりわけ監視カメラの映像データと携帯電話の基地局測位ログは、容疑者が築いた最も強固な防御壁を完全に粉砕しました。",
            "自らの詭弁の罠が自壊していく様を目の当たりにして、彼の顔に張り付いていた偽りの平静は音を立てて瓦解し始めたのです。",
            "説明不能な時間の空白を突く的確な質問の数々が、容疑者を弁解不能な袋小路へと追い詰めました。",
            "名門大学のエリート学生という自惚れは、ティエンクアン7番地のベテラン刑事たちの練達した眼力と気迫の前に、瞬く間に屈服したのです。",
        ]
    ),
    # Dlg 17 (Investigator): 8 lines (+2)
    (
        "**捜査官** *(沈着かつ鋭い口調で、拘置所内における心理の激変を振り返る)*:",
        [
            "ティエンクアン7番地の警察本部へ身柄が移送された直後、グエン・ドゥック・ギアの態度は頑迷そのものであり、言い逃れを繰り返しました。",
            "彼は常に自らの置かれた境遇を嘆き、突発的な諍いによって感情が高ぶったのだと、責任を環境に転嫁しようと試みました。",
            "しかし捜査員たちは粘り強く対峙を重ね、彼の供述と事前に凶器を準備していた行動との間の決定的な矛盾を浮き彫りにしました。",
            "鉄壁の論理と動かしがたい証拠の前に、容疑者の最後の心理的防壁は完全に崩壊しました。",
            "彼はついに深々と頭を垂れ、凶行の全容を詳細に自供し、証拠品を遺棄した正確な場所を白状するに至ったのです。",
            "それこそは、知的な傲慢さが法の正義と人間の良心の重みの前に完全に叩き伏せられた瞬間でした。",
            "複数枚に及ぶ自筆の供述書において、容疑者は強盗を目的とした計画的な殺害計画の全貌を認めざるを得ませんでした。",
            "白紙の上に震える手で書き殴られた文字は、彼のあらゆる往生際の悪い言い逃れに決定的な終止符を打ちました。",
        ]
    ),
    # Dlg 18 (Psychologist): 6 lines
    (
        "**心理学者** *(鋭くメスを入れ、自己愛の崩壊の瞬間を解き明かす)*:",
        [
            "反論不能な科学的証拠が白日の下に晒された瞬間こそ、自己愛的な自我が壊滅的な衝撃を受けた決定的な時点でした。",
            "犯人は、自らが長年にわたって心血を注ぎ構築してきた完璧なエリートの仮面が完全に粉砕されたことを悟ったのです。",
            "自律神経系は即座に極度のパニック反応を示しました。瞳孔は散大し、呼吸は浅く荒くなり、視線は激しく泳ぎ始めました。",
            "現実逃避の防衛機制がもはや通用しなくなった時、対象者の精神は自己憐憫の心理状態へと急転換します。",
            "彼は自らに降りかかろうとしている破滅的な社会的代償を実感し、その現実は脆弱な自我の許容量を遥かに超えていたのです。",
            "これは極端な傲慢さから、法廷における劇的な葛藤のパフォーマンスへと犯人を突き動かす、決定的な心理的分水嶺でした。",
        ]
    ),
    # Dlg 19 (Psychologist): 6 lines
    (
        "**心理学者** *(学術的視点から、処罰に直面した心理的自己防衛反応を解剖する)*:",
        [
            "取調室において頑なな拒絶から罪の自白へと移行するプロセスは、防衛エネルギーが枯渇した際の必然的な心理軌跡です。",
            "人間の脳は、高密度の専門的な追及を受け続ける極限状態の中で、複雑な嘘の網を維持し続けることはできません。",
            "捏造されたシナリオが破綻した時、認知の緊張は沸点に達し、内なる重圧から解放されるために自白へと追い込まれるのです。",
            "しかしながら、犯行を口頭で認めたという事実が、直ちに心の底からの真摯な悔悟を意味するわけではありません。",
            "それは往々にして、動かぬ証拠と逆転不可能な現実の圧力に屈した、機械的な降伏に過ぎない場合が多いのです。",
            "法的な屈服から真の良心の目覚めに至る道は、常に激しい葛藤と痛みを伴う極めて過酷な精神の歩みなのです。",
        ]
    ),
    # Dlg 20 (Investigator): 7 lines (+2)
    (
        "**捜査官** *(重厚な口調で、広域に及んだ物証捜索作戦を語る)*:",
        [
            "起訴状を寸分の隙もない強固なものとするため、捜査本部は遺棄された証拠品の発見に全力を注ぎました。",
            "幾日もの昼夜にわたり、警察官と熟練の潜水士たちはクアンニン省ドンチエウ地域のカム川沿いの水域を1メートルずつ徹底捜索しました。",
            "深く濁った川底と激しい潮流の中で、数日前に投げ捨てられた小さな物証を探し出す作業は困難を極めました。",
            "しかし、人命の尊厳と司法の威信に対する崇高な責任感を胸に、捜査隊は決して諦めませんでした。",
            "そして重要な証拠品が発見され、DNA型が被害者のものと完全に一致した時、犯人の罪状は完璧に立証されたのです。",
            "捜査隊の不屈の捜索活動は、被害者遺族に完全な真実を届け、無念を晴らす力となりました。",
            "それは、いかなる証拠隠滅工作も、冷たい水底に永遠に真実を沈めておくことはできないという明確な証明でした。",
        ]
    ),

    # Act 4 (Total: 47 sentences)
    # Dlg 21 (Host): 8 lines (+2)
    (
        "**ホスト** *(静かに、法廷の開廷と後悔の深層という核心テーマに踏み込む)*:",
        [
            "2010年7月、ハノイ市人民裁判所において、本件の第一審公判が厳粛に開廷されました。",
            "この裁判は、全国数百万人の国民の異例なまでの関心と注視を集めました。",
            "法廷において世論が目撃したのは、関係者たちの極めて複雑で矛盾に満ちた心理的葛藤の数々でした。",
            "とりわけ、裁判を見守るすべての者の胸を締めつけた大きな問いは、「後悔の真の本質とは何か」ということでした。",
            "かつて何の躊躇もなく残忍な凶行に及んだ者が、なぜテレビカメラの前で激しく号泣し、自ら死刑を望むような発言をしたのでしょうか。",
            "それは真の良心の目覚めだったのか、それとも世間の痛烈な非難から逃れるための新たな心理的仮面に過ぎなかったのでしょうか。",
            "元恋人の遺影と対峙した際、法廷内の空気は窒息しそうなほどの重圧に包まれました。",
            "眼鏡の奥から流れ落ちたその涙は、当時の社会世論において激しい賛否両論の議論を巻き起こす中心点となったのです。",
        ]
    ),
    # Dlg 22 (Investigator): 7 lines (+1)
    (
        "**捜査官** *(沈着な口調で、不通報幇助の交際相手と二人の父親の悲劇を語る)*:",
        [
            "公判において、新たな交際相手であったホアン・ティ・イエンは犯罪不通報罪で法廷に立たされました。",
            "彼女が流した遅すぎた涙は、自らが信じ愛した男性が悪魔の化身であったことを悟った者の底知れぬ混乱を物語っていました。",
            "しかし、最も痛ましい悲劇を背負ったのは、法廷の両極に立つこととなった二人の父親でした。",
            "被害者の父グエン・ヴァン・バー氏は、愛娘の遺骨を捜索するため警察と共に奔走し、引き裂かれるような悲痛に耐え抜きました。",
            "そして加害者の父グエン・ドゥック・フン氏は、深い絶望の中で息子に代わって世間に頭を下げ、許しを請い続けました。",
            "法廷で相対する二人の老いた父親の姿こそは、分別のない犯罪がもたらす破滅的な連鎖の、最も胸を締めつける証拠でした。",
            "交際相手に科された法的責任は、盲目的な情愛から犯罪の隠蔽に加担することの危険性を社会に強く警告するものでした。",
        ]
    ),
    # Dlg 23 (Ordinary Person N2): 5 lines
    (
        "**一般人** *(N2 - ホアン・ティ・イエン、深い自責の念に声を震わせながら)*:",
        [
            "自らの純粋な愛情と信頼が、このような戦慄すべき凶行の道具として悪用されたとは、夢にも思いませんでした。",
            "部屋に戻り、塗り直されたペンキや本棚の微細な汚れに気づいて問い詰めた時、鼻血が出たという彼の言い訳を私は信じてしまったのです。",
            "愛していた男性が恐ろしい罪を犯しているかもしれないという現実に直面する勇気がなく、私は自分自身を欺いていました。",
            "しかし警察が扉を叩いた時、突きつけられた無慈悲な真実は、私の心を完全に粉砕し麻痺させました。",
            "執行猶予付きの有罪判決は人生で最も過酷な教訓でしたが、被害者遺族に対する生涯消えない良心の苛みこそが、私に課せられた真の終身刑なのです。",
        ]
    ),
    # Dlg 24 (Psychologist): 8 lines (+2)
    (
        "**心理学者** *(後悔の深層心理と生存本能の相克を鋭く分析する)*:",
        [
            "心理学的な観点から見れば、第一審における被疑者の号泣と死刑嘆願は、劇症的な「自己愛の負傷」への衝動的反応でした。",
            "完璧を誇った自己像が大衆の前で白日の下に晒された時、主観的な屈辱感と自己嫌悪は耐えがたい頂点へと達します。",
            "その際の死の嘆願は、被害者の苦痛への真の共感というよりも、自らの耐えがたい恥辱を終わらせたいという無意識の衝動だったのです。",
            "その決定的な証拠は公判直後に現れ、興奮が鎮静化するや否や、生物学的な生存本能が猛烈に息を吹き返したのです。",
            "被告は減刑を求める控訴状を提出し、劇的な悔悟のパフォーマンスと死への根源的恐怖との間にある深い乖離を露呈しました。",
            "真の後悔とは、自己憐憫の殻を脱ぎ捨て、自らが他者に与えた取り返しのつかない喪失の痛みを真に内在化させた時にのみ宿るものなのです。",
            "死刑を望みながらも減刑を求めて控訴するという激しい揺らぎは、自らの罪の報いに直面した自己愛者の本質的な脆さを露呈しました。",
            "彼は世間の前で恥を晒すことを極度に恐れながらも、自らの肉体的な死という完全な消滅をそれ以上に恐れていたのです。",
        ]
    ),
    # Dlg 25 (Host): 7 lines (+1)
    (
        "**ホスト** *(静かに、裁判後に展開した過酷な運命の連鎖を描き出す)*:",
        [
            "第一審判決で言い渡された死刑判決は、社会世論の圧倒的な支持をもって受け止められました。",
            "しかし法廷の背後で傷ついた家族たちにとって、その悲劇は決して癒えることのない生々しい傷口として刻まれ続けました。",
            "愛する娘を理不尽に奪われた被害者遺族にとって、いかなる極刑をもってしても埋めることのできない永遠の空白が残されました。",
            "そして加害者の家族にとっても、世間の指弾と絶望は、由緒ある家庭を修復不可能な崩壊へと叩き落としたのです。",
            "さらに痛ましいことに、2010年10月30日に加害者の父親が交通事故で突如命を落としたことは、悲劇の上に更なる悲劇を重ねることになりました。",
            "それは、子供の犯した過ちによって老いた両親が最も過酷な十字架を背負わされるという、あまりにも無慈悲な運命の皮肉でした。",
            "控訴審の直前に訪れた父親の急死は、かつて誇り高く生きてきた一族にとって、あまりにも惨憺たる幕切れでした。",
        ]
    ),
    # Dlg 26 (Psychologist): 7 lines (+1)
    (
        "**心理学者** *(深遠な心理学的視点から、死刑囚の最期の精神変容を総括する)*:",
        [
            "死刑囚監房の孤独な独房で過ごした最後の歳月において、グエン・ドゥック・ギアの精神世界は劇的な変容を遂げました。",
            "あらゆる法的手段が尽き、自らの余命が日一日と縮まりゆく中で、かつての傲慢な自己愛の残滓は完全に消滅したのです。",
            "控訴が棄却された後、死刑囚は国家主席に宛てて恩赦嘆願書を提出し、生きて罪を償う機会を涙ながらに懇願しました。",
            "この段階における後悔は、もはや大衆の面前で見せた劇的な涙や自己正当化の弁明ではありませんでした。",
            "それは自らが犯した罪の圧倒的な重みの前での完全な沈黙であり、双方の家族と社会に撒き散らした破滅に対する真の自覚だったのです。",
            "2014年7月22日の薬物注射による死刑執行は、かつて全てを持ちながら道徳的堕落によって全てを失った一人の青年の生涯に、最終的な幕を下ろしました。",
            "独房の四つの冷たい壁と向き合い続けた長い日々は、道を踏み外したエリートのあらゆる知性的虚栄を完全に剥ぎ取ったのです。",
        ]
    ),
    # Dlg 27 (Psychologist): 5 lines
    (
        "**心理学者** *(学術的視点から、大衆心理の沸騰と処罰のメカニズムを解説する)*:",
        [
            "グエン・ドゥック・ギアの裁判が引き起こした社会的衝撃は、かつてないほどの激しい大衆の怒りの怒涛を巻き起こしました。",
            "極刑を求める世論の沸騰は、社会共同体が備える道徳的免疫システムが力強く作動した証拠でした。",
            "人間性の根源的な境界線が極めて残虐に蹂躙された時、社会は共通の価値観を守り抜くために本能的な処罰欲求を発動させるのです。",
            "しかしながら、正当な正義の希求と、盲目的な復讐心との境界線は、時に極めて曖昧になりがちです。",
            "最も賞賛されるべきは、怒りの嵐が吹き荒れる法廷の中にあっても、被害者遺族が一貫して気高い品格と静かな自制を保ち続けたことでした。",
        ]
    ),

    # Act 5 (Total: 38 sentences)
    # Dlg 28 (Host): 7 lines (+1)
    (
        "**ホスト** *(静かに、最終判決の執行と慈悲による魂の救済を語る)*:",
        [
            "控訴審裁判所はその後、被告の控訴を棄却し、グエン・ドゥック・ギアに対する死刑判決を維持しました。",
            "恩赦嘆願が正式に退けられた後、2014年7月に死刑が厳粛に執行されました。",
            "法が下した厳正な判決は、現代司法史における最も暗い事件記録の一つに最終的な終止符を打ちました。",
            "しかしその厳しい判決の背後で、人々の心を最も深く揺さぶり深い思索へと誘ったのは、人間の慈悲の奇跡でした。",
            "加害者の父親が無念の交通事故で亡くなった際、被害者の父親自らが悔やみの手紙を送り、哀悼の花輪を捧げたのです。",
            "その崇高な人道的行為はあらゆる怨嗟を超越し、犯罪の暗雲が決して人の心の温もりを消し去ることはできないことを証明しました。",
            "被害者の父親が見せた並外れた慈悲の心は、計り知れない悲嘆の中にあっても、人間性の救済に対する揺るぎない希望の灯を灯したのです。",
        ]
    ),
    # Dlg 29 (Investigator): 7 lines (+2)
    (
        "**捜査官** *(沈着な口調で、捜査教訓の総括と司法的正義の不滅の価値を宣言する)*:",
        [
            "グエン・ドゥック・ギア事件の捜査記録は、都市型犯罪および頭脳的証拠隠滅犯罪との戦いにおける不滅の金字塔です。",
            "それは動かしがたい真理を証明しました。いかに犯人が狡猾な手口を弄そうとも、科学捜査と捜査陣の執念が必ずや真実を白日の下に晒すということです。",
            "微細な生体痕跡や見落とされそうな滴り斑の一つ一つが、法の光の前で悪事を告発する揺るぎない声となるのです。",
            "迅速な事件解決は、無念の死を遂げた被害者の魂を慰めただけでなく、人の道を外れようとする者に対する峻厳な警告となりました。",
            "正義は時に過酷な頭脳戦を潜り抜けねばなりませんが、決して暗闇の前に屈服することはありません。",
            "この特別捜査の完全な勝利は、首都警察部隊の鋼の規律と卓越した捜査能力、そして国民への献身精神を力強く示しました。",
            "事件の一つ一つが完璧に解明されることこそが、法と正義の厳正さに対する社会の揺るぎない信頼を強固に築き上げるのです。",
        ]
    ),
    # Dlg 30 (Ordinary Person N1): 5 lines
    (
        "**一般人** *(N1 - G4マンション住民、静かに省察と覚醒を語る)*:",
        [
            "あの忘れられない夏から長い年月が流れ、G4マンションの日常には再び穏やかな平穏が戻ってきました。",
            "しかし、あの戦慄の日々を生きた私たちにとって、事件の記憶は今もなお風化することのない深い戒めとなっています。",
            "私たちは過去の冷淡で閉鎖的な態度を改め、周囲の隣人たちに心を開いて気遣うことの大切さを学びました。",
            "地域社会の温かい絆と、身の回りの異変に対する静かな警戒心こそが、各家庭を守る最も堅固な防壁なのです。",
            "亡くなられた方の魂が天国で安らかに眠りにつくことを祈るとともに、このような悲劇が二度と繰り返されないことを切に願っています。",
        ]
    ),
    # Dlg 31 (Psychologist): 7 lines (+2)
    (
        "**心理学者** *(穏やかな口調で、生存のための三大レッドフラッグ原則を提示する)*:",
        [
            "グエン・ドゥック・ギア事件から、行動心理学は私たちが胸に刻むべき三つの核心的な「生存のレッドフラッグ原則」を導き出します。",
            "第一に、知性のハロー効果や名門の家柄を前にして、自己の防衛本能と危険察知力を決して麻痺させてはなりません。",
            "第二に、「親近感の罠」を常に警戒することです。心理的に不安定な兆候や借金苦を抱えた人物と、密室で個人的に会うことは絶対に避けてください。",
            "第三に、自らの生存直感を信じ尊重することです。相手の急激な言動の変化や欺瞞を察知したならば、直ちに周囲に助けを求めてください。",
            "犯罪心理学に対する深い洞察こそが、狡猾な危険から自らと愛する人々を守り抜く最も確固たる盾となるのです。",
            "過度な遠慮や盲目的な信頼によって、自らコントロールできない危険な環境へと足を踏み入れてはなりません。",
            "適切な警戒心と危機管理能力を身につけることは、決して人間不信になることではなく、自分自身の命に対して誠実に生きる知恵なのです。",
        ]
    ),
    # Dlg 32 (Psychologist): 6 lines (+1)
    (
        "**心理学者** *(人間味あふれる温かい口調で、心の癒やしと真の赦しの力を説く)*:",
        [
            "被害者の父親が加害者遺族に対して示した寛容と赦しは、「心的外傷後成長」の至高の体現です。",
            "心理学において、赦しとは犯された罪を帳消しにしたり、悪行を肯定したりすることではありません。",
            "赦しとは、怨嗟と激痛という自らを縛り付ける牢獄から、自らの魂を解き放つための最も勇敢な決断なのです。",
            "亡くなった加害者の父親へ哀悼の手紙を送り花を捧げたことで、被害者の父は憎悪の無限の連鎖反応に自ら終止符を打ちました。",
            "それこそは人間の強さに関する最も深い教訓です。悪は命を奪うことはできても、私たちの魂にある気高さと慈愛を滅ぼすことは決してできないのです。",
            "真の慈愛の光だけが、人間の魂に刻まれた決して癒えることのないかに思われた深い傷跡を、真に癒やすことができるのです。",
        ]
    ),
    # Dlg 33 (Host): 6 lines
    (
        "**ホスト** *(温かく包み込むような声で、深い人道的メッセージと共に番組を締めくくる)*:",
        [
            "アンバー・アイズと共に歩む犯罪心理学の旅路は、決して恐怖や盲目的な憎悪を煽るためのものではありません。",
            "私たちの究極の目的は人間の意識を覚醒させ、人の心に潜む複雑で深遠な迷宮をより深く理解することにあります。",
            "悪意が纏う完璧な仮面は一時的に目を欺くかもしれませんが、絶え間なき覚醒と深い慈悲こそが、正義を導く不滅の灯台であり続けます。",
            "どうか人生の一瞬一瞬を大切に慈しみ、内なる良心の声に耳を傾け、あらゆる甘い誘惑に対して揺るぎない警戒を保ち続けてください。",
            "毎回、専門的な深層ファイルに熱心にお付き合いくださる視聴者の皆様に、心より感謝を申し上げます。",
            "それでは皆様、次なる探求の旅路で再びお会いいたしましょう。",
        ]
    ),
]

print(f"EN sections: {len(EN_SECTIONS)}, total lines: {sum(len(lines) for _, lines in EN_SECTIONS)}")
print(f"JA sections: {len(JA_SECTIONS)}, total lines: {sum(len(lines) for _, lines in JA_SECTIONS)}")
