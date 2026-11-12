import io, json, os, re
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
jobs = json.loads((ROOT/".work/bg_jobs_tap09.json").read_text(encoding="utf-8"))
print("jobs:", len(jobs))
print("keys:", list(jobs[0].keys()))
lens = [len(j["prompt"]) for j in jobs]
print("prompt len min/max/avg:", min(lens), max(lens), sum(lens)//len(lens))
print()
print("=== all names + sentences + desc (for mapping rebuild) ===")
for j in jobs:
    print(f"{j['name']:46s} | {j['sentences']:>14s} | {j['desc'][:60]}")
print()
print("=== prompts containing style boilerplate already? ===")
n_style = sum(1 for j in jobs if "graphic novel noir" in j["prompt"].lower())
n_neg = sum(1 for j in jobs if "no text" in j["prompt"].lower())
print("  has 'graphic novel noir':", n_style, "/", len(jobs))
print("  has 'no text':", n_neg, "/", len(jobs))
print()
print("=== sample full prompts ===")
for j in jobs[:2] + jobs[30:32] + jobs[-2:]:
    print(f"-- {j['name']}\n   {j['prompt']}\n")
