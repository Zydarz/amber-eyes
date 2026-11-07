import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('01_KICH_BAN/Tap10/kichban_tap10_23102026.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Checking all {len(lines)} lines of kichban_tap10_23102026.md...')

issues = []
for i, line in enumerate(lines, 1):
    raw = line.strip()
    if not raw:
        continue

    # 1. Check if line has unclosed parenthesis or brackets
    if raw.count('(') != raw.count(')'):
        issues.append((i, 'Mismatched ()', raw))
    if raw.count('[') != raw.count(']'):
        issues.append((i, 'Mismatched []', raw))
    if raw.count('“') != raw.count('”'):
        issues.append((i, 'Mismatched curly quotes', raw))
    if raw.count('"') % 2 != 0:
        issues.append((i, 'Mismatched straight quotes', raw))

    # 2. Check stage directions: *(...)*
    # If there is * ( ... ) * without matching
    if '*(' in raw and ')*' not in raw:
        issues.append((i, 'Unclosed stage direction *(*', raw))

    # 3. Check for double spaces
    if '  ' in raw and not raw.startswith('|') and not raw.startswith(' '):
        # markdown 2 spaces at end of line is fine, but in middle of text?
        mid_double_space = re.sub(r'  $', '', raw)
        if '  ' in mid_double_space:
            issues.append((i, 'Double space inside text', raw))

    # 4. Check punctuation spacing
    # space before comma/period
    if not raw.startswith('|'):
        m = re.findall(r'\s+([,.:;?!])', raw)
        if m:
            issues.append((i, f'Space before punct: {m}', raw))

print(f'Total issues found in raw lines: {len(issues)}')
for iss in issues:
    print(f'Line {iss[0]} [{iss[1]}]:\n  {iss[2]}\n')
