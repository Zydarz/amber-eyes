# -*- coding: utf-8 -*-
with open('.work/build_tap31_216.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix unescaped single quotes inside single-quoted strings:
# E.g. 'The attacker's targets...' -> "The attacker's targets..." or 'The attacker\'s targets...'
lines = text.splitlines()
fixed_lines = []
for l in lines:
    if "'" in l and "targets shifted" in l:
        l = l.replace("'The attacker's targets", "\"The attacker's targets").replace("executives.',", "executives.\",")
    if "'" in l and "perpetrator's primary" in l:
        l = l.replace("'The name derived from the perpetrator's", "\"The name derived from the perpetrator's").replace("Airlines.',", "Airlines.\",")
    if "'" in l and "perpetrator's lethality" in l:
        l = l.replace("'The perpetrator's lethality", "\"The perpetrator's lethality").replace("1985.',", "1985.\",")
    if "'" in l and "Unabomber's first" in l:
        l = l.replace("'This marked the Unabomber's first", "\"This marked the Unabomber's first").replace("murder.',", "murder.\",")
    if "'" in l and "scholar's mind" in l:
        l = l.replace("'He wanted to inject pervasive terror into every scholar's mind", "\"He wanted to inject pervasive terror into every scholar's mind").replace("threat.',", "threat.\",")
    if "'" in l and "brother's life" in l:
        l = l.replace("'He engaged legal counsel to deliver the correspondence to the FBI with a single desperate plea: Please spare my brother's life.'", "\"He engaged legal counsel to deliver the correspondence to the FBI with a single desperate plea: Please spare my brother's life.\"")
    if "'" in l and "Ted's 1971" in l:
        l = l.replace("'Yet the moment Ted's 1971 23-page essay was laid upon Fitzgerald's analytical desk, the briefing room fell dead silent.',", "\"Yet the moment Ted's 1971 23-page essay was laid upon Fitzgerald's analytical desk, the briefing room fell dead silent.\",")
    if "'" in l and "Armed with Fitzgerald's 50-page" in l:
        l = l.replace("'Armed with Fitzgerald's 50-page forensic linguistic affidavit comparing the manifesto against family letters, a federal judge granted a historic warrant.',", "\"Armed with Fitzgerald's 50-page forensic linguistic affidavit comparing the manifesto against family letters, a federal judge granted a historic warrant.\",")
    if "'" in l and "Unabomber's secretive" in l:
        l = l.replace("'As the weathered timber door was pulled open, the blinding light of justice pierced the Unabomber's secretive universe.',", "\"As the weathered timber door was pulled open, the blinding light of justice pierced the Unabomber's secretive universe.\",")
    if "'" in l and "families of Ted's bombings" in l:
        l = l.replace("'After legal fees, I distributed the vast majority directly to the surviving victims and grieving families of Ted's bombings.',", "\"After legal fees, I distributed the vast majority directly to the surviving victims and grieving families of Ted's bombings.\",")
    if "'" in l and "Ted's bomb in Salt Lake City" in l:
        l = l.replace("'Then, the most profound grace of my life occurred: Gary Wright, who had been maimed by Ted's bomb in Salt Lake City, reached out to me.',", "\"Then, the most profound grace of my life occurred: Gary Wright, who had been maimed by Ted's bomb in Salt Lake City, reached out to me.\",")
    if "'" in l and "Unabomber's rage" in l:
        l = l.replace("'Entering the 1990s, the Unabomber's rage escalated into an increasingly lethal and bloodsoaked campaign.',", "\"Entering the 1990s, the Unabomber's rage escalated into an increasingly lethal and bloodsoaked campaign.\",")
    fixed_lines.append(l)

with open('.work/build_tap31_216.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(fixed_lines))

print('Fixed quotes in build_tap31_216.py.')
