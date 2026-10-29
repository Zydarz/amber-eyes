import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import edition
print("EP 01:", edition.EPISODES["01"]["title"])
print("EP 05:", edition.EPISODES["05"]["act1_cue"], edition.EPISODES["05"]["silence_cue"], edition.EPISODES["05"]["click_cues"], edition.EPISODES["05"]["bed"][3])
