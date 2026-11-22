# -*- coding: utf-8 -*-
# Tap 32 builder
import json, re
from pathlib import Path

ROOT = Path('.').resolve()
OUT = ROOT / '.work' / 'bg_jobs_tap32.json'

jobs = []
print('Tap 32 builder started')
