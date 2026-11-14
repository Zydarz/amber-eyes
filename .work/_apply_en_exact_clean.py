# -*- coding: utf-8 -*-
import sys

# Dòng chính xác từ file EN
en_insertions = [
    (
        "Standing before the bench, both David and Louise Turpin wept and offered trembling statements of apology.",
        "Were those courtroom tears a genuine awakening of long-dormant conscience, or merely the pathetic collapse of narcissistic grandiosity once their absolute power evaporated?"
    ),
    (
        "A son shared a profound message of grace, stating that he still loved his parents and forgave them, even though the past could never be erased.",
        "The son's expression of forgiveness was never an absolution of heinous acts, but rather an act of psychological liberation, stripping his parents of their lingering power to hurt him."
    ),
    (
        "The defendants' tearful display in court reflected Narcissistic Collapse upon losing all dominion, rather than genuine remorse.",
        "The mother's invocation of God having a special plan was a textbook case of moral disengagement and spiritual bypassing, deflecting personal accountability for systemic cruelty.\nBoth perpetrators grieved only when their tyrannical domestic kingdom vanished, leaving them to face absolute isolation behind prison walls for the rest of their lives."
    ),
    (
        "Their resilience proves that the darkness of coercive control cannot extinguish the core human desire for identity and love.",
        "By refusing to remain hostages of hatred, the survivors accomplished a monumental psychological leap, proving that human empathy ultimately triumphs over tyrannical control."
    ),
    (
        "Keen observation, genuine concern, and a timely telephone call to authorities can save vulnerable lives from unseen torment.",
        "Every citizen must actively dismantle the bystander effect, for hesitation and silence in the face of red flags provide fertile ground for hidden abuse to fester."
    ),
    (
        "Sustained psychological guidance and community solidarity are vital in helping survivors of coercive control reclaim their true identity.",
        "The paradigm of post-traumatic growth affirms that even the deepest psychological wounds can serve as the bedrock for profound self-realization and boundless compassion."
    ),
    (
        "No child born into this world deserves to live in terror, filth, and deprivation of nourishment, education, and love.",
        "Collective empathy and vigilance are the only light capable of piercing the darkness of invisible prisons concealed behind closed suburban walls."
    )
]

def apply_remaining_en():
    path = '01_KICH_BAN/Tap17_EN/kichban_tap17_EN.md'
    mirror = '01_KICH_BAN/Tap17/kichban_tap17_EN.md'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    for idx, (target, addition) in enumerate(en_insertions):
        if target not in text:
            print(f"FAILED on [{idx}]: {repr(target[:40])}")
            return False
        text = text.replace(target, target + "\n" + addition, 1)
        print(f"Applied remaining EN [{idx}]")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    with open(mirror, 'w', encoding='utf-8') as f:
        f.write(text)
    return True

print("=== APPLYING REMAINING EN ===")
ok = apply_remaining_en()
print("Success:", ok)
