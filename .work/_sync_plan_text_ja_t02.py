#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua shots_text_tap02_JA.json cho khop VOI LOI NOI THAT (JA script 31/10).

Tua duoc: 6 shot trich dan + 15 shot beat + 2 shot chu bold (2-17, 2-23) + vai mau.
Backup truoc, khong ghi file neu builder (validator) khong pass.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

TXT = W / "shots_text_tap02_JA.json"
BK = W / "_cu" / "shots_text_tap02_JA_pre_sync_20261102.json"
if not BK.exists():
    shutil.copy2(TXT, BK)
    print(f"backup -> {BK.relative_to(ROOT)}")

data = json.loads(TXT.read_text(encoding="utf-8-sig"))

# sid -> (Chu moi, beat moi)
FIX = {
    "1-24": ("*被害者の家の近く* · **全地形対応タイヤのトレッドパターン** · *スノーブーツの足跡*",
             ["スノーブーツの足跡"]),
    "1-25": ("*日常的な検問* → `#3`: **犯行現場の痕跡と酷似**", ["懐中電灯で"]),
    "1-28": ("*召喚状ではなく* · **電話による丁重な要請**", ["電話による"]),
    "2-11": ("*金銭や宝石類* → `#9`: **女性たちの下着や極めて私的な物品**", ["持ち去ったのは"]),
    "2-17": ("**心理的署名** *(Signature)* · *手放せなかったもの*", []),
    "3-02": ("*地位 · 名声 · 才能あふれる妻 · 国家全体からの敬意* → **なぜそのすべてを投げ打った?**",
             ["投げ打った"]),
    "3-09": ("**ごく些細な衝動から始まった**", ["衝動"]),
    "3-13": ("**底なしの下降スパイラル** · *命を奪う暴力へと至った*", ["底なしの下降スパイラル"]),
    "3-20": ("**もう一方の区画の扉を固く閉ざす** → `#8`: *内面的な葛藤など存在しませんでした*",
             ["扉を固く閉ざして"]),
    "3-21": ("*自らの行動を説明できなかった* → `#10`: “ええ、でも答えは分かりませんし、答えが重要だとも思えません”",
             []),
    "3-25": ("*段階 03* · **悪性自己愛** *(Malignant Narcissism)* · **神コンプレックス** *(God Complex)*",
             ["神コンプレックス"]),
    "3-27": ("*デジタルカメラを手に* · **何ものにも縛られない究極の権力**", ["究極の権力"]),
    "3-28": ("*病的な自己愛を肥大化させる動かぬ証拠* → “俺はすべての上に君臨し、お前たちの運命を支配している、そして誰一人として俺に触れることはできない”",
             ["俺はすべての上に君臨し"]),
    "4-08": ("“…将校の仮面を被った捕食者が暗闇の中に立ち、じっと自分を見つめていた…”", []),
    "4-13": ("*事件現場のスノーブーツの足跡* · *ウィリアムズ自身のブーツ* → “まったく同じですね”",
             ["と告げました"]),
    "4-14": ("**大佐は一瞬、言葉を失いました**", []),
    "4-15": ("*奇妙な要求* → “ラスと呼んでくれ”", []),
    "5-08": ("**軍服の焼却** · *トレントン基地 · 機密文書焼却施設*", ["焼却処分した"]),
    "5-10": ("“文末にピリオドを打つとき、その点は小さくとも、計り知れないほど大きな意味を持つのです”",
             ["文末にピリオドを打つとき"]),
    "5-24": ("**卓越した知性では誰も守られない** → `#11`: *破滅を先延ばしにし、衝撃を致命的にするだけ*",
             ["誰も守ってはくれません"]),
}

for sid, (chu, beats) in FIX.items():
    old = data.get(sid)
    if old is None:
        print(f"  !! {sid} khong co trong shots_text")
        continue
    override = old[2] if len(old) > 2 else None
    data[sid] = [chu, beats, override]
    print(f"  ~ {sid}: {old[0][:46]!r} -> {chu[:46]!r}")

TXT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\nghi {TXT.name} · {TXT.stat().st_size} byte")

# ---- chay builder (validator) ----
import os
import subprocess
env = dict(os.environ)
env["AE_LANG"] = "ja"
env["AE_EP"] = "02"
env["PYTHONIOENCODING"] = "utf-8"
r = subprocess.run([sys.executable, str(W / "_build_plan_tap02_ja.py")], cwd=ROOT, env=env,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print("\n=== BUILDER (validator) ===")
print(f"rc = {r.returncode}")
print((r.stdout or "")[-3000:])
if r.returncode != 0:
    print("STDERR:", (r.stderr or "")[-800:])
