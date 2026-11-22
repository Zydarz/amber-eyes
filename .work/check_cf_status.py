import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path('.').resolve()
WORK = ROOT / '.work'
sys.path.insert(0, str(WORK))
from flux_client import get_account_pool

pool = get_account_pool()
print(f"--- ĐANG KIỂM TRA TRẠNG THÁI {len(pool)} TÀI KHOẢN CLOUDFLARE ---")

for i, acc in enumerate(pool):
    account_id = acc["id"]
    api_token = acc["token"]
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell"
    payload = json.dumps({"prompt": "A test simple noir scene", "steps": 4}).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("success"):
                print(f"[+] Tài khoản {i+1} ({account_id[:6]}...{account_id[-4:]}): SẴN SÀNG (ĐÃ RESET QUOTA / HOẠT ĐỘNG TỐT)")
            else:
                print(f"[-] Tài khoản {i+1} ({account_id[:6]}...{account_id[-4:]}): Phản hồi không có ảnh: {data}")
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="ignore")
        try:
            err_j = json.loads(err)
            msg = err_j.get("errors", [{}])[0].get("message", err[:80])
        except Exception:
            msg = err[:80]
        if e.code == 429:
            print(f"[-] Tài khoản {i+1} ({account_id[:6]}...{account_id[-4:]}): HẾT QUOTA (HTTP 429 - 10,000 neurons)")
        else:
            print(f"[-] Tài khoản {i+1} ({account_id[:6]}...{account_id[-4:]}): LỖI HTTP {e.code} -> {msg}")
    except Exception as ex:
        print(f"[-] Tài khoản {i+1} ({account_id[:6]}...{account_id[-4:]}): Lỗi kết nối: {ex}")
