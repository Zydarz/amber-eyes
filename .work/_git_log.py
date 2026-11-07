# -*- coding: utf-8 -*-
import subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
res = subprocess.run(['git', 'log', '-S', 'strip(\'"“”\')', '-p', '.work/parse_kichban.py'], capture_output=True, text=True, encoding='utf-8')
print(res.stdout[:1500])
