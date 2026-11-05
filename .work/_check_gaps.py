# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

tl_en = json.load(open(".work/timeline_s_EN_t06.json", encoding="utf-8"))
items = {it["id"]: it for it in tl_en["items"]}

print("1.04#2:", items.get("1.04#2"))
print("1.06#1:", items.get("1.06#1"))
print("2.11#6:", items.get("2.11#6"))
print("3.02#1:", items.get("3.02#1"))
print("3.13#3:", items.get("3.13#3"))
print("4.02#1:", items.get("4.02#1"))
print("4.10#2:", items.get("4.10#2"))
print("5.02#1:", items.get("5.02#1"))
print("5.04#4:", items.get("5.04#4"))
print("5.06#1:", items.get("5.06#1"))
