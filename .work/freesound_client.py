# -*- coding: utf-8 -*-
"""
Client Freesound APIv2 cho du an AMBER EYES.

XAC THUC
--------
Freesound co 2 kieu:
  1. Token authentication  -> dung truc tiep cot "Client secret/Api key" lam API key.
     Header:  Authorization: Token <API_KEY>     (hoac ?token=<API_KEY>)
     DUOC DUNG O DAY. Khong can trinh duyet, khong can redirect URL.
  2. OAuth2 authorization_code -> CHI can khi muon tai FILE GOC (wav/aiff)
     hoac upload/rate/comment. Freesound KHONG ho tro grant_type=client_credentials
     (tra 400 unauthorized_client) nen khong the lay token bang script.

  Endpoint `download/` (file goc) la OAuth2-required => voi Token auth tra 401.
  Token auth van tai duoc PREVIEW (mp3/ogg 128kbps stereo) qua CDN.

HAN MUC (do bang GET /apiv2/usage/)
  burst     : 60 request / phut   -> client throttling toi da 1.1s/gioi tu (~54/min)
  sustained : 2000 request / ngay
  Endpoint /usage/ khong bi throttle nen khong tinh vao han muc.
  ⚠ Han muc ap tai cap USER, khong phai CLIENT: nhieu client cung 1 tai khoan se
    dung chung han muc.

DOC CHINH THUC
--------------
  https://freesound.org/docs/api/authentication.html
  https://freesound.org/docs/api/resources_apiv2.html

QUY TAC (AGENTS.md)
------------------
  L4  tai san tai veo tu ngoai -> phai hoi nguoi dung truoc khi dua vao video.
  L7  moi tai san phai co dong trong provenance.json.
  A3  SFX tai veo phai duoc nghe kiem truoc khi nhap.
  T6  Windows: PYTHONIOENCODING=utf-8 khi chay.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

import requests

WORK = Path(__file__).resolve().parent
ROOT = WORK.parent

API_BASE = "https://freesound.org/apiv2"
USER_AGENT = "TruyenKyAudio/1.0 (AMBER EYES)"

# Ten giaphep trong filter cua Freesound
LICENSE_CC0 = "Creative Commons 0"
LICENSE_CC_BY = "Creative Commons Attribution"
LICENSE_NAMES = {
    "cc0": LICENSE_CC0,
    "cc-by": LICENSE_CC_BY,
}

# Preview tot nhat cho video: hq mp3 (128 kbps stereo) - dung cho nen & SFX
PREVIEW_QUALITY = "preview-hq-mp3"
PREVIEW_QUALITY_OGG = "preview-hq-ogg"


def get_api_key(cli_key: str | None = None) -> str | None:
    """Thu tu: tham so CLI -> bien moi truong -> file .work/.freesound_key."""
    if cli_key:
        return cli_key.strip()
    env = os.environ.get("FREESOUND_API_KEY")
    if env:
        return env.strip()
    key_file = WORK / ".freesound_key"
    if key_file.exists():
        return key_file.read_text(encoding="utf-8").strip()
    return None


class FreesoundError(RuntimeError):
    pass


class FreesoundClient:
    """Client Token-auth cho Freesound APIv2."""

    def __init__(
        self,
        api_key: str | None = None,
        min_interval: float = 1.1,
        retries: int = 3,
        timeout: int = 60,
    ):
        key = get_api_key(api_key)
        if not key:
            raise FreesoundError(
                "Chua co Freesound API key. Truyen --key, gan bien moi truong "
                "FREESOUND_API_KEY, hoac luu vao .work/.freesound_key"
            )
        self.api_key = key
        self.min_interval = min_interval
        self.retries = retries
        self.timeout = timeout
        self._last_call = 0.0
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Token {key}", "User-Agent": USER_AGENT}
        )

    # ------------------------------------------------------------------ core
    def _throttle(self) -> None:
        gap = time.monotonic() - self._last_call
        if gap < self.min_interval:
            time.sleep(self.min_interval - gap)
        self._last_call = time.monotonic()

    def _get(self, path: str, params: dict | None = None, raw: bool = False):
        url = path if path.startswith("http") else f"{API_BASE}{path}"
        last_err = None
        for attempt in range(self.retries):
            self._throttle()
            try:
                r = self.session.get(url, params=params, timeout=self.timeout)
            except requests.RequestException as e:
                last_err = e
                time.sleep(1.5 * (attempt + 1))
                continue
            if r.status_code == 429 or 500 <= r.status_code < 600:
                last_err = FreesoundError(f"HTTP {r.status_code}: {r.text[:200]}")
                # 429 = vuot han muc burst (60/phut). Cho them 10s truoc lan thu lai.
                time.sleep(10.0 * (attempt + 1))
                continue
            if r.status_code == 401:
                raise FreesoundError(
                    "401 Unauthorized - API key sai hoac endpoint yeu cau OAuth2 "
                    f"({url})"
                )
            if r.status_code >= 400:
                raise FreesoundError(f"HTTP {r.status_code}: {r.text[:300]}")
            if raw:
                return r
            return r.json()
        raise FreesoundError(f"Het so lan thu: {last_err}")

    # ---------------------------------------------------------------- public
    def usage(self) -> dict:
        """Hạn mức API: burst (60/phút) + sustained (2000/ngày). Endpoint này KHÔNG bị throttle."""
        return self._get("/usage/")

    def _build_params(
        self,
        query: str,
        limit: int,
        license: str | None,
        extra_filter: str | None,
        sort: str | None,
        duration_max: int | None,
        min_rating: int | None,
        page: int,
    ) -> dict:
        filters = []
        lic = LICENSE_NAMES.get((license or "").lower())
        if lic:
            filters.append(f'license:"{lic}"')
        if extra_filter:
            filters.append(extra_filter)
        if duration_max is not None:
            filters.append(f"duration:[0 TO {duration_max}]")
        if min_rating is not None:
            filters.append(f"rating:[{min_rating} TO 5]")

        params = {
            "query": query,
            "page": page,
            "page_size": min(max(limit, 1), 60),
            "fields": (
                "id,name,duration,license,license_attribution,username,"
                "tags,type,previews,download,num_downloads,rating"
            ),
        }
        if filters:
            params["filter"] = " ".join(filters)
        if sort:
            params["sort"] = sort
        return params

    def search(
        self,
        query: str,
        limit: int = 15,
        license: str | None = None,
        extra_filter: str | None = None,
        sort: str | None = None,
        duration_max: int | None = None,
        min_rating: int | None = None,
        page: int = 1,
        fallback: bool = True,
    ) -> list[dict]:
        """
        Tim sound theo tu khoa.

        license: 'cc0' | 'cc-by' | None (mac dinh khong loc)
        duration_max: chi lay sound ngan hon N giay (gioi han de dung trong video)
        fallback: Freesound coi MOI tu trong query la bat buoc. Query 3+ tu
                  thuong tra 0 ket qua. Khi fallback=True, client se bo dan
                  tu tu hao mot chieu cho den khi ra ket qua.
        """
        params = self._build_params(
            query, limit, license, extra_filter, sort, duration_max,
            min_rating, page,
        )
        data = self._get("/search/text/", params)
        results = data.get("results", [])
        if results or not fallback:
            return results

        # Fallback: bo tu cuoi mot chieu
        terms = query.split()
        for cut in range(1, len(terms)):
            shorter = " ".join(terms[: len(terms) - cut])
            if not shorter:
                break
            params["query"] = shorter
            data = self._get("/search/text/", params)
            results = data.get("results", [])
            if results:
                return results
        return []

    def sound(self, sound_id: int) -> dict:
        """Chi tiet 1 sound (co previews + attribution)."""
        return self._get(
            f"/sounds/{int(sound_id)}/",
            {
                "fields": (
                    "id,name,duration,license,license_attribution,username,"
                    "tags,type,previews,download,num_downloads,num_ratings,"
                    "rating,created,description,bookmark"
                )
            },
        )

    def preview_url(self, sound: dict, quality: str = PREVIEW_QUALITY) -> str | None:
        previews = sound.get("previews") or {}
        return previews.get(quality) or previews.get(PREVIEW_QUALITY_OGG)

    def download_preview(
        self, sound: dict, dest: Path, quality: str = PREVIEW_QUALITY
    ) -> Path:
        """Tai preview (mp3/ogg). KHONG tai duoc file goc voi Token auth."""
        url = self.preview_url(sound, quality)
        if not url:
            raise FreesoundError(f"Sound {sound.get('id')} khong co preview")
        dest = Path(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        r = self._get(url, raw=True)
        dest.write_bytes(r.content)
        return dest

    def license_id(self, sound: dict) -> str:
        """Rut ngan license de ghi provenance: cc0 / cc-by / cc-by-nc / ..."""
        url = (sound.get("license") or "").lower()
        if "creativecommons.org/publicdomain/zero" in url or "zero/1.0" in url:
            return "cc0"
        if "by-nc" in url:
            return "cc-by-nc"
        if "by-nd" in url:
            return "cc-by-nd"
        if "by-sa" in url:
            return "cc-by-sa"
        if "/by/" in url or "licenses/by" in url:
            return "cc-by"
        return url or "unknown"

    def provenance(self, sound: dict, dest_rel: str, extra: dict | None = None) -> dict:
        """Dong provenance theo dung format cua provenance.json cua du an."""
        lic = self.license_id(sound)
        row = {
            "file": dest_rel,
            "loai": "sfx_freesound",
            "cong_cu": "Freesound APIv2 (Token auth) - .work/freesound_client.py",
            "ngay": time.strftime("%Y-%m-%d"),
            "prompt": None,
            "seed": None,
            "font": None,
            "dieu_khoan": (
                f"Freesound sound id={sound.get('id')} | {sound.get('license')} | "
                f"tac gia: {sound.get('license_attribution') or sound.get('username')} | "
                f"link: https://freesound.org/s/{sound.get('id')}/ | "
                f"ban tai: PREVIEW {'hq mp3' if quality_is_mp3(sound) else 'ogg'} "
                f"(khong phai file goc)"
            ),
            "kiem_tra_thuong_mai": (
                "chua kiem tra - can nghe duyet va kiem dieu khoan"
                if lic != "cc0"
                else "cc0 - cho phep thuong mai, van can nghe duyet"
            ),
        }
        if extra:
            row.update(extra)
        return row


def quality_is_mp3(sound: dict) -> bool:
    previews = sound.get("previews") or {}
    return bool(previews.get(PREVIEW_QUALITY))


def append_provenance(rows: list[dict], path: Path | None = None) -> tuple[Path, int]:
    """
    Ghi them dong vao provenance.json (giu nguyen format list).

    ⚠ Format cua provenance.json la `indent=1` — dung `indent=1` de khong lam
      file bi doi dinh dang (1.83 MB -> 1.89 MB neu dung indent=2).
    ⚠ Dong bi BO QUA neu `file` da co trong sổ. Vi du 57 ung vien Freesound
      deu tro toi `assets/sfx/tXX/<ma>.wav` — ma do da co dong tu YouTube Audio
      Library => bi skip het. Dung `fs_provenance.py --staging` truoc khi duyet.
    """
    path = Path(path or (ROOT / "provenance.json"))
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = []
    existing = {r.get("file") for r in data}
    added = 0
    for r in rows:
        if r.get("file") in existing:
            continue
        data.append(r)
        existing.add(r.get("file"))
        added += 1
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    return path, added


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Thu Freesound APIv2")
    ap.add_argument("cmd", choices=["search", "sound", "download"])
    ap.add_argument("arg", nargs="?", default="", help="query hoac sound id")
    ap.add_argument("--key", default=None)
    ap.add_argument("--license", default="cc0", choices=["cc0", "cc-by", "none"])
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--out", default=None)
    ap.add_argument("--maxdur", type=int, default=None)
    args = ap.parse_args()

    c = FreesoundClient(args.key)
    if args.cmd == "search":
        lic = None if args.license == "none" else args.license
        for s in c.search(args.arg, limit=args.limit, license=lic,
                          duration_max=args.maxdur):
            print(
                f"{s['id']:>8}  {s.get('duration', 0):>7.2f}s  "
                f"{c.license_id(s):<8} {s.get('name', '')[:60]}"
            )
    elif args.cmd == "sound":
        s = c.sound(int(args.arg))
        print(json.dumps(s, ensure_ascii=False, indent=2)[:2000])
    elif args.cmd == "download":
        s = c.sound(int(args.arg))
        out = Path(args.out or f".work/freesound/{s['id']}.mp3")
        p = c.download_preview(s, out)
        print(f"da tai: {p} ({p.stat().st_size} bytes)")
