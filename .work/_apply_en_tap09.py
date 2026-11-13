# -*- coding: utf-8 -*-
"""Cập nhật kịch bản Tập 09 tiếng Anh (EN) để đạt parity 100% với bản VN."""
import re

EN_1_02 = '''**HOST** *(measured, warm baritone setting historical context)*:
"In the late 1960s, America was deeply immersed in the vibrant peak of the Hippie movement.
Hundreds of thousands of young people flocked to California from across the nation to take part in the Summer of Love.
They wore flowers in their hair and dreamed together of a free world without prejudice.
In the eyes of the youth at that time, the golden sunshine of Los Angeles stood as the ultimate symbol of spiritual awakening and liberation.
People placed unreserved trust in complete strangers with natural, naive openness.
The media continually romanticized this free-spirited ethos, inadvertently creating a collective blind spot of naivety across society.
It was precisely this collapse of vigilance that created an immense opening for predatory manipulators to operate in plain sight.
Yet they could never have imagined that this era of innocence was about to close forever in a horrific nightmare."'''

EN_2_06 = '''**INVESTIGATOR** *(analyzing five escalation phases and erosion of boundaries)*:
"Through investigative intelligence and evidence reconstruction, we determined that Manson's crimes did not erupt spontaneously, but followed a distinct behavioral escalation trajectory comprising five stages:
Stage One: Juvenile Delinquency and Manipulation.
Manson refined his techniques of coercive psychological control and pathological deception through decades of incarceration.
Stage Two: Cult Formation and Mental Enslavement.
Administering high doses of LSD and orchestrating communal sexual rituals to dismantle the personality frameworks of young recruits at Spahn Ranch.
Stage Three: The Nocturnal “Creepy Crawling” Drills.
Manson led disciples on midnight burglaries into suburban homes, taking nothing but rearranging furniture to rehearse their sense of omnipotence and invisible dominance.
With each violation of domestic privacy left unpunished, the threshold for deviance expanded another step in their impressionable minds.
Stage Four: Outbreak of Armed Lethal Violence.
In late July 1969, Manson critically shot drug supplier Bernard Crowe and commanded the slaying of musician Gary Hinman following a monetary extortion dispute.
Stage Five: Climax of Mass Symbolic Slaughter.
With his threshold of violence desensitized, Manson mandated the coordinated strikes on Cielo Drive and Waverly Drive to produce symbolic carnage.
This trajectory exemplifies a fundamental behavioral reality: when boundary-testing goes unchecked, the appetite for dark fantasy demands ever more destructive realities.
Yet inside the stifling confines of Spahn Ranch, Linda Kasabian, a young mother with her sixteen-month-old daughter, was already beginning to feel a creeping sense of dread within this fanatical machinery."'''

EN_3_08 = '''**PSYCHOLOGIST** *(analyzing neutralization techniques, objectification, and cognitive dissociation)*:
"He twisted the lyrics of The Beatles' song “Helter Skelter” from the White Album into a prophetic divine scripture of an impending racial war.
He crowned himself both the reincarnation of Jesus Christ and the sole arbiter of truth.
To silence the dormant conscience of his disciples, Manson drilled them in Techniques of Neutralization outlined by criminologists Sykes and Matza:
Appeal to Higher Loyalties: Manson preached that taking lives in Helter Skelter was not murder, but a transcendent spiritual liberation serving universal love.
Objectification and Dehumanization: Victims were not human beings, but mere “Pigs” – corrupt avatars of a hypocritical capitalist establishment destined for cleansing.
Denial of Responsibility: Moral agency was displaced onto cosmic destiny, reducing the disciples to blameless instruments executing divine necessity.
Concurrently, a state of Extreme Cognitive Dissociation coupled with Moral Coma severed these young executioners entirely from agonizing reality.
They did not perceive living human beings pleading for their lives; their manipulated minds only saw stage props in a cosmic drama.
For Manson himself, he suffered from a total Theory of Mind deficit and complete emotional empathy void.
A victim's pleas for mercy did not awaken compassion, but triggered pathological power arousal, intoxicating a mind structured by malignant narcissism.
He never viewed his disciples as loved ones, but rather as disposable extensions of his grandiose self to satisfy fantasies of absolute dominion."'''

EN_4_05 = '''**ORDINARY PERSON** *(N2: Linda Kasabian, witness stand testimony, young female voice trembling with dread)*:
"Standing on the witness stand and looking into the eyes of Charles Manson, an icy dread ran down my spine.
The friends I had shared meals with at Spahn Ranch now sat there with empty, hollow eyes like wooden marionettes.
They had lost all perception of human suffering and empathy.
I had watched them lose themselves piece by piece under Manson's insidious spell.
On that fateful night at Cielo Drive, as I stood frozen outside the gates listening to frantic cries in the dark, something profound inside me shattered.
I could never harm another human being, because back at Spahn Ranch my baby daughter was waiting for me.
The terror of losing my child and sheer revulsion toward slaughter woke me from that dark trance to flee into the desert night.
Taking the stand was the most terrifying decision of my life, but I had to tell the truth to deliver justice for the victims and free my own soul from that phantom of guilt."'''

EN_4_09 = '''**PSYCHOLOGIST** *(analyzing courtroom spectacle, collapse of delusions, and nature of remorse)*:
"At the 1970 trial, the defendants' conduct was a textbook display of Shared Delusion and extreme psychological denial.
Manson carved an “X” into his forehead, declaring he had crossed himself out of society's world; his female disciples carved identical marks, laughing and singing as they entered court.
That eerie laughter was a desperate psychological shield to avoid confronting the crushing reality that they had become monstrous killers.
Yet true psychological reckoning began only when sentences were handed down and they were physically severed from Manson in solitary confinement.
Stripped of drugs and mob dynamics, the cognitive fog dissolved, revealing naked truth: Helter Skelter was a fraudulent delusion and their own hands had destroyed innocent lives.
The phenomenon of Moral Injury erupted, unleashing an overwhelming tempest of self-revulsion.
Over the ensuing decades behind bars, Leslie Van Houten and Patricia Krenwinkel endured immense internal torment, ceased blaming Manson, and accepted retribution as deserved karma.
Their remorse evolved into authentic moral contrition, yet fraught with the duality of an innate human yearning for freedom.
In stark contrast, Charles Manson never once experienced genuine remorse; his Malignant Narcissism trapped him in Pathological Self-Pity, playing the perpetual victim of society until his death."'''

EN_5_04 = '''**INVESTIGATOR** *(assessing judicial legacy, victims' rights movement, and final demise)*:
"The Manson prosecution established an enduring judicial precedent across modern jurisprudence: a manipulative mastermind bears equal criminal responsibility to those who execute the physical deeds.
Furthermore, the resilience of Sharon Tate's mother, Doris Tate, forged a historic turning point for humane justice.
She mobilized over 350,000 citizens, spearheading California's Victims' Rights Movement that culminated in the landmark 1982 Victims' Bill of Rights.
For the first time in history, surviving family members were guaranteed the right to deliver Victim Impact Statements at parole hearings to defend the dignity of the deceased.
As for Charles Manson, he spent the remainder of his life in California's maximum-security prisons until succumbing to illness on November 19, 2017, at age eighty-three.
He ended his days in absolute isolation behind steel bars, leaving an indelible stain across American history."'''

EN_5_05 = '''**PSYCHOLOGIST** *(drawing profound behavioral insights and psychological reckoning)*:
"Psychologically, the most devastating sentence endured by Charles Manson was not physical incarceration, but social irrelevance.
Until his final days, Manson desperately sought media interviews to satisfy his insatiable addiction to attention.
That desperation revealed the raw pathetic nature of Pathological Self-Pity when a grandiose ego faces irrevocable collapse.
Meanwhile, after more than fifty years of rehabilitation confronting her Moral Injury, Leslie Van Houten was finally granted parole in July 2023 at age seventy-three, concluding a haunting human tragedy.
This tragedy reminds us: whenever humans experience isolation and existential vacuum, we become vulnerable prey to predators claiming to offer salvation.
Psychological predators never arrive wearing devil's horns.
They present themselves cloaked as empathic friends and selfless mentors."'''

with open('01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace elements carefully
# 1.02
text = re.sub(r'\*\*HOST\*\* \*\([^)]*setting historical context\)\*:.*?(?=\n\n\*\*\[SFX\])', EN_1_02, text, flags=re.S)

# 2.06
text = re.sub(r'\*\*INVESTIGATOR\*\* \*\([^)]*5-stage escalation trajectory\)\*:.*?(?=\n\n\*\*\[Pause 1\.5 seconds\])', EN_2_06, text, flags=re.S)

# 3.08
text = re.sub(r'\*\*PSYCHOLOGIST\*\* \*\([^)]*neutralization and objectification\)\*:.*?(?=\n\n\*\*\[Pause 1\.5 seconds\])', EN_3_08, text, flags=re.S)

# 4.05
text = re.sub(r'\*\*ORDINARY PERSON\*\* \*\(N2: Linda Kasabian[^\n]*\n.*?(?=\n\n\*\*\[SFX\]:)', EN_4_05, text, flags=re.S)

# 4.09
text = re.sub(r'\*\*PSYCHOLOGIST\*\* \*\([^)]*narcissistic collapse and the letter X\)\*:.*?(?=\n\n\*\*HOST\*\*)', EN_4_09, text, flags=re.S)

# 5.04
text = re.sub(r'\*\*INVESTIGATOR\*\* \*\([^)]*reflecting on judicial precedent\)\*:.*?(?=\n\n\*\*PSYCHOLOGIST\*\*)', EN_5_04, text, flags=re.S)

# 5.05
text = re.sub(r'\*\*PSYCHOLOGIST\*\* \*\([^)]*delivering psychological synthesis and inner sentence\)\*:.*?(?=\n\n\*\*\[Pause 2\.0 seconds\])', EN_5_05, text, flags=re.S)

with open('01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md', 'w', encoding='utf-8') as f:
    f.write(text)

with open('01_KICH_BAN/Tap09/kichban_tap09_EN.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated 01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md successfully!")
