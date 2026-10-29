import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
os.environ["AE_EP"] = "05"
sys.path.insert(0, '.work')
import tts_sentences as tts

items = tts.plan_items()
print(f"Tổng số câu TTS plan: {len(items)}")
for i, it in enumerate(items[:5]):
    print(f"{it['id']} ({it['role']}) [{it['voice']}, emo={it['emotion']}, spd={it['speed']}]: {it['text'][:60]}...")
print("...")
for i, it in enumerate(items[-3:]):
    print(f"{it['id']} ({it['role']}) [{it['voice']}, emo={it['emotion']}, spd={it['speed']}]: {it['text'][:60]}...")
