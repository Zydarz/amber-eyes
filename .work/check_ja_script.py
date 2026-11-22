import re
with open('.work/generate_higgs_prod_t19ja.py', 'r') as f:
    code = f.read()
print(code[code.find("[Step 5/7]"):code.find("[Step 5/7]") + 1200])
