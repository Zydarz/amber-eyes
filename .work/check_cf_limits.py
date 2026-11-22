import urllib.request
import urllib.error
import json
from pathlib import Path

WORK = Path('.work')
pool_file = WORK / '.cloudflare_accounts'
accounts = []
cur_acc = {}
for line in pool_file.read_text(encoding='utf-8').splitlines():
    line = line.strip()
    if not line or line.startswith('#'): continue
    if line.startswith('[') and line.endswith(']'):
        if cur_acc.get('id') and cur_acc.get('token'):
            accounts.append(cur_acc)
        cur_acc = {}
    elif line.startswith('CLOUDFLARE_ACCOUNT_ID='):
        cur_acc['id'] = line.split('=', 1)[1].strip()
    elif line.startswith('CLOUDFLARE_API_TOKEN='):
        cur_acc['token'] = line.split('=', 1)[1].strip()
if cur_acc.get('id') and cur_acc.get('token'):
    accounts.append(cur_acc)

url_model = 'https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell'

for i, acc in enumerate(accounts, 1):
    url = url_model.format(account_id=acc['id'])
    req = urllib.request.Request(
        url,
        data=json.dumps({'prompt': 'test'}).encode('utf-8'),
        headers={'Authorization': f"Bearer {acc['token']}", 'Content-Type': 'application/json'}
    )
    try:
        resp = urllib.request.urlopen(req, timeout=5)
        print(f"Account {i}: OK!")
    except urllib.error.HTTPError as e:
        headers_dict = dict(e.headers)
        err_body = e.read().decode('utf-8', errors='ignore')
        print(f"Account {i}: HTTP {e.code} | body: {err_body[:100]}")
    except Exception as e:
        print(f"Account {i}: Error {e}")
