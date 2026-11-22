# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
from gen_core import clean_prompt

# Standard act prompt blueprints for 5 acts
# Act 1: Establishing, Social blindspot, early warning signs, initial trigger, incident
# Act 2: Deep psychological dive, pathology, childhood/escalation, MO vs Signature, compartmentalization
# Act 3: Forensic investigation, breakthrough, interrogation, tactical confrontation, collapse
# Act 4: Trial, legal confrontation, victim testimony, genuine vs transactional remorse, verdict
# Act 5: Sentence execution, surviving legacy, 3 red flags, forensic achievements, closing dossier

print('Engine ready.')
