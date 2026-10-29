# -*- coding: utf-8 -*-
"""
Lay ung vien SFX tu Freesound (CC0) cho cac ma SFX hien duung track THAY THE
(trong 02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md muc 4.2).

QUY TRINH
  1. Tim theo bo tu khoa viet tay (Freesound coi MOI tu trong query la bat buoc,
     nen tu khoa nhieu tu -> 0 ket qua).
  2. Chi loc license CC0 (du dieu khoan cho thuong mai) - mac dinh.
  3. Tai PREVIEW hq mp3 (Token auth khong tai duoc file goc).
  4. Do bang ffmpeg: thoi luong, mean/max dBFS.
  5. Viet bao cao JSON + Markdown + dong provenance (CHUA dua vao assets/sfx/).

QUY TAC
  L4  tai san tai ngoai -> moi tai vao .work/freesound/ de USER DUYET,
      khong tu cho vao assets/sfx/ hay video.
  L7  moi file phai co dong trong provenance.json (o trang thai "chua nghe duyet").
  A3  phai nghe kiem truoc khi nhap - script chi ghi "ung vien", khong ghi "da dung".

Dung:
  py -3 .work/fs_fetch.py --codes amb_fastfood_cafeteria,fx_sigh_female --top 3
  py -3 .work/fs_fetch.py --all --top 2
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from freesound_client import FreesoundClient, FreesoundError  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
FFMPEG = (
    WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
)
FFPROBE = FFMPEG.with_name("ffprobe.exe")
OUT_DIR = WORK / "freesound"
REPORT_JSON = WORK / "freesound_candidates.json"
REPORT_MD = WORK / "freesound_candidates.md"

# --------------------------------------------------------------------------
# 19 ma dang dung track thay the (muc 4.2). Key = ma SFX, value = bo tu khoa.
#
# ⚠ BAI HOC: Freesound coi MOI tu trong query la BAT BUOC. Tru khoa 3-4 tu
#   (vd "library quiet room tone") luon tra 0 ket qua. Phai dung 1-2 tu.
#   Do la ly do 7 ma tra 0 lan chay dau.
# --------------------------------------------------------------------------
SUBSTITUTE_CODES = {
    "amb_crowd_outside_press_anger": ["angry shouting", "crowd yelling"],
    "amb_fastfood_cafeteria": ["fast food restaurant", "fastfood restaurant"],
    "amb_lawyers_discussion": ["people talking", "office discussion"],
    "amb_library_quiet": ["library ambience", "reading room"],
    "fx_computer_beep_restore": ["computer beep", "beep error"],
    "fx_courtroom_dead_silence": ["courtroom", "court"],
    "fx_crowd_relief_sigh": ["crowd sigh", "sighing crowd"],
    "fx_defib_charge_shock": ["defibrillator", "heart monitor beep"],
    "fx_door_slam_indoor": ["door slam", "door close"],
    "fx_evidence_measure_tape": ["tape measure", "measuring tape"],
    "fx_inkjet_printer_run": ["inkjet printer", "printer running"],
    "fx_metal_lock_open": ["lock open", "padlock unlock"],
    "fx_monitor_case_close": ["plastic latch", "case close"],
    "fx_phone_unlock_click": ["unlock click", "phone click"],
    "fx_printer_thermal": ["thermal printer", "receipt printer"],
    "fx_sigh_emotional": ["sigh", "man sigh"],
    "fx_sigh_female": ["woman sigh", "female sigh"],
    "fx_wooden_hinge_creak_open": ["wooden hinge", "door creak"],
    "fx_wooden_lid_slam_latch": ["wooden lid", "latch"],
}

# Thoi luong toi da (giay) cho tung loai - dung de loai sound qua ngan/qua dai
DUR_RANGE = {
    "amb": (8, 90),
    "fx": (0.2, 12),
}
# Override cho ma co nhu cau dac biet (vd "dead silence" la nen phai dai)
DUR_OVERRIDE = {
    "fx_courtroom_dead_silence": (5, 90),
}
# Tieng dong ngan phai dung < 6 s de khong keu suot tap
MAX_DUR = 120


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_").lower()
    return s[:48] or "sound"


# Tu khoa trong ma SFX hay bi viet tat -> bo qua khi so sanh ten
STOPWORDS = {"amb", "fx", "bgm", "the", "a", "of", "and"}

# Tu khoa ma SFX <-> tu trong ten sound (Freesound dat ten tu do)
SYNONYMS = {
    "anger": ["anger", "angry", "mad"],
    "outside": ["outside", "outdoor"],
    "cafeteria": ["cafeteria", "restaurant", "food", "diner"],
    "lawyers": ["lawyer", "lawyers", "people", "talking"],
    "discussion": ["discussion", "discussing", "talking", "conversation"],
    "creak": ["creak", "creaking", "squeak", "squeaking"],
    "wooden": ["wooden", "wood"],
    "printer": ["printer", "print", "printing"],
    "phone": ["phone", "smartphone", "mobile"],
    "beep": ["beep", "beeps", "beeping"],
    "sigh": ["sigh", "sighing", "sighs", "sighed"],
    "defib": ["defibrillator", "defib"],
    "court": ["court", "courtroom"],
    "lid": ["lid", "cover", "chest"],
    "latch": ["latch", "latches", "clip"],
    "hinge": ["hinge", "hinges"],
    "measure": ["measure", "measuring", "tape"],
    "crowd": ["crowd", "people", "audience"],
    "sighs": ["sigh", "sighing"],
    "quiet": ["quiet", "calm", "ambience"],
    "reading": ["reading", "read", "library"],
    "library": ["library", "reading", "book"],
    "reload": ["restore", "reset", "reboot"],
    "restore": ["restore", "reload", "reset"],
}


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def name_hits(code: str, sound_name: str) -> list[str]:
    """Tu khoa cua ma SFX xuat hien trong ten sound -> kiem nhanh nhanh.

    So sanh tren dang chuan hoa (bo khoang trang, dau, gach) nen
    `fastfood` khop `Fast Food restaurant` (chuoi "fastfood" co trong
    "fastfoodrestaurant"). Bo sung bang tu dong nghĩa cho truong hop
    `anger`/`angry`, `cafeteria`/`restaurant`...
    """
    if not sound_name:
        return []
    flat = _norm(sound_name)
    hits = []
    for tok in code.lower().split("_"):
        if tok in STOPWORDS or len(tok) < 3:
            continue
        variants = SYNONYMS.get(tok, [tok])
        if any(_norm(v) in flat for v in variants):
            hits.append(tok)
    return hits


def needs_review(code: str, sound_name: str, duration: float | None,
                 mean_db: float | None) -> str | None:
    """Canh bao tu dong cho ung vien co kha nang sai."""
    hits = name_hits(code, sound_name or "")
    key = [t for t in code.lower().split("_")
           if t not in STOPWORDS and len(t) >= 4 and t not in SYNONYMS]
    if key and not hits:
        return "TEN KHONG KHOP MA - nghe ky truoc"
    if duration is not None and duration > 30 and code.startswith("fx_"):
        return "fx_ nhung dai >30s - co the keu suot tap"
    if mean_db is not None and mean_db < -40:
        return "RAT NHE (mean %.0f dBFS) - can khu gain" % mean_db
    return None


def probe_duration(path: Path) -> float | None:
    try:
        out = subprocess.run(
            [str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(path)],
            capture_output=True, text=True, timeout=60,
        )
        return round(float(out.stdout.strip()), 3)
    except Exception:
        return None


def probe_levels(path: Path) -> dict:
    """mean/max dBFS bang ffmpeg volumedetect."""
    res = {"mean_db": None, "max_db": None}
    try:
        out = subprocess.run(
            [str(FFMPEG), "-hide_banner", "-nostats", "-i", str(path),
             "-af", "volumedetect", "-f", "null", "-"],
            capture_output=True, text=True, timeout=120,
        )
        txt = out.stderr or ""
        m = re.search(r"mean_volume:\s*(-?[\d.]+) dB", txt)
        if m:
            res["mean_db"] = float(m.group(1))
        m = re.search(r"max_volume:\s*(-?[\d.]+) dB", txt)
        if m:
            res["max_db"] = float(m.group(1))
    except Exception:
        pass
    return res


def fetch_code(client: FreesoundClient, code: str, top: int, license_mode: str,
               download: bool) -> dict:
    queries = SUBSTITUTE_CODES.get(code)
    if not queries:
        base = re.sub(r"^(amb|fx|bgm)_", "", code).replace("_", " ")
        queries = [base]

    lic = None if license_mode == "any" else license_mode
    lo, hi = DUR_OVERRIDE.get(code, DUR_RANGE.get(code.split("_")[0], (0.5, MAX_DUR)))

    seen: dict[int, dict] = {}
    for q in queries:
        try:
            results = client.search(
                q, limit=top * 4, license=lic,
                duration_max=hi, fallback=False,
            )
        except FreesoundError as e:
            print(f"    ! loi tim '{q}': {e}", file=sys.stderr)
            continue
        for s in results:
            dur = s.get("duration") or 0
            if dur < lo or dur > hi:
                continue
            sid = s["id"]
            if sid not in seen:
                seen[sid] = s
        if len(seen) >= top:
            break

    out_rows = []
    for s in list(seen.values())[:top]:
        row = {
            "code": code,
            "sound_id": s["id"],
            "name": s.get("name"),
            "author": s.get("username"),
            "attribution": s.get("license_attribution"),
            "license": s.get("license"),
            "license_id": client.license_id(s),
            "duration_api": s.get("duration"),
            "tags": (s.get("tags") or [])[:10],
            "url": f"https://freesound.org/s/{s['id']}/",
            "num_downloads": s.get("num_downloads"),
            "name_hits": name_hits(code, s.get("name") or ""),
        }
        if download:
            dest_dir = OUT_DIR / code
            dest = dest_dir / f"{s['id']}_{slugify(s.get('name') or str(s['id']))}.mp3"
            try:
                client.download_preview(s, dest)
                row["file_local"] = str(dest.relative_to(ROOT)).replace("\\", "/")
                row["bytes"] = dest.stat().st_size
                row["duration_file"] = probe_duration(dest)
                row.update(probe_levels(dest))
            except Exception as e:
                row["error"] = str(e)
        row["canh_bao"] = needs_review(
            code, s.get("name"), row.get("duration_file"), row.get("mean_db")
        )
        out_rows.append(row)

    return {"code": code, "queries": queries, "candidates": out_rows}


def write_markdown(report: list[dict], license_mode: str) -> None:
    lines = [
        "# Ứng viên SFX từ Freesound (CC0) — chờ nghe duyệt",
        "",
        f"Nguồn: freesound.org (Token auth) · license lọc: `{license_mode}` · "
        f"mỗi ứng viên là **PREVIEW hq mp3 160 kbps stereo**, KHÔNG phải file gốc.",
        "",
        "> ⚠ Chưa file nào được đưa vào `assets/sfx/` hay video. "
        "Theo A3, phải **nghe kiểm** trước khi nhập.",
        "> Cột ⚠ là cảnh báo tự động theo tên — ưu tiên nghe ứng viên không bị gạch.",
        "",
        "| Mã SFX | Sound ID | Thời lượng | mean dBFS | License | Tác giả | Tên sound | ⚠ |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for r in report:
        for c in r["candidates"]:
            warn = c.get("canh_bao") or ""
            if c.get("extra"):
                warn = (warn + " · DỰ PHÒNG").strip(" ·")
            lines.append(
                f"| `{r['code']}` | [{c['sound_id']}]({c['url']}) | "
                f"{c.get('duration_file')}s | {c.get('mean_db')} | "
                f"{c['license_id']} | {c.get('author')} | "
                f"{(c.get('name') or '')[:38]} | {warn} |")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def sync_staging(client: FreesoundClient) -> int:
    """
    Quet .work/freesound/ lai, bo sung ung vien da tai nhung chua co trong
    bao cao (thi du 17 file con lai tu lan truy van dau voi bo tu khoa cu).
    Muc dich: khong bo soat file nao trong staging ma khong xuat hien trong bao cao.
    """
    if not REPORT_JSON.exists():
        print(f"Thieu {REPORT_JSON}", file=sys.stderr)
        return 0
    data = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    known = {c["sound_id"] for e in data["codes"] for c in e["candidates"]}

    by_code: dict[str, list[Path]] = {}
    for p in OUT_DIR.rglob("*.mp3"):
        code = p.parent.name
        try:
            sid = int(p.name.split("_")[0])
        except ValueError:
            continue
        if sid in known:
            continue
        by_code.setdefault(code, []).append(p)

    added = 0
    for code, paths in by_code.items():
        entry = next((e for e in data["codes"] if e["code"] == code), None)
        if entry is None:
            entry = {"code": code, "queries": [], "candidates": []}
            data["codes"].append(entry)
        for p in sorted(paths):
            sid = int(p.name.split("_")[0])
            try:
                s = client.sound(sid)
            except FreesoundError as e:
                print(f"    ! {sid}: {e}", file=sys.stderr)
                continue
            row = {
                "code": code,
                "sound_id": s["id"],
                "name": s.get("name"),
                "author": s.get("username"),
                "attribution": s.get("license_attribution"),
                "license": s.get("license"),
                "license_id": client.license_id(s),
                "duration_api": s.get("duration"),
                "tags": (s.get("tags") or [])[:10],
                "url": f"https://freesound.org/s/{s['id']}/",
                "num_downloads": s.get("num_downloads"),
                "name_hits": name_hits(code, s.get("name") or ""),
                "file_local": str(p.relative_to(ROOT)).replace("\\", "/"),
                "bytes": p.stat().st_size,
                "duration_file": probe_duration(p),
                "extra": True,
            }
            row.update(probe_levels(p))
            row["canh_bao"] = needs_review(
                code, s.get("name"), row.get("duration_file"), row.get("mean_db")
            )
            entry["candidates"].append(row)
            known.add(sid)
            added += 1
            print(f"    + {code}/{sid} ({s.get('name')})")

    REPORT_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    write_markdown(data["codes"], data.get("license", "cc0"))
    return added


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes", default=None,
                    help="danh sach ma SFX, phan tach bang dau phay")
    ap.add_argument("--all", action="store_true", help="lay tat ca ma thay the")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--license", default="cc0", choices=["cc0", "cc-by", "any"])
    ap.add_argument("--no-download", action="store_true")
    ap.add_argument("--report", action="store_true",
                    help="chi sinh lai bao cao MD tu JSON hien co (khong goi API)")
    ap.add_argument("--sync", action="store_true",
                    help="quet staging, bo sung ung vien con thua vao bao cao")
    ap.add_argument("--key", default=None)
    args = ap.parse_args()

    if args.sync:
        client = FreesoundClient(args.key)
        n = sync_staging(client)
        print(f"Da bo sung {n} ung vien vao bao cao.")
        return 0

    if args.report:
        data = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
        # Tinh lai canh bao cho cac dong cu (dam bao bao cao luon khop)
        for e in data["codes"]:
            for c in e["candidates"]:
                c["canh_bao"] = needs_review(
                    e["code"], c.get("name"), c.get("duration_file"), c.get("mean_db")
                )
        REPORT_JSON.write_text(
            json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        write_markdown(data["codes"], data.get("license", "cc0"))
        n = sum(1 for e in data["codes"] for c in e["candidates"] if c.get("canh_bao"))
        print(f"Da sinh lai {REPORT_MD} ({n} canh bao)")
        return 0

    if args.codes:
        codes = [c.strip() for c in args.codes.split(",") if c.strip()]
    elif args.all:
        codes = list(SUBSTITUTE_CODES.keys())
    else:
        print("Can --codes hoac --all", file=sys.stderr)
        return 2

    client = FreesoundClient(args.key)
    u = client.usage()
    print(f"Han muc: burst {u['current']['burst']['num']}/{u['current']['burst']['limit']}"
          f" · sustained {u['current']['sustained']['num']}/{u['current']['sustained']['limit']}")
    print(f"Xu ly {len(codes)} ma, moi ma toi da {args.top} ung vien,"
          f" license={args.license}\n")

    report = []
    for i, code in enumerate(codes, 1):
        print(f"[{i}/{len(codes)}] {code}")
        r = fetch_code(client, code, args.top, args.license, not args.no_download)
        for c in r["candidates"]:
            mark = "OK " if c.get("file_local") else "-- "
            flag = " !!" if c.get("canh_bao") else "   "
            print(f"    {mark}{c['sound_id']:>7} {str(c.get('duration_api')):>6}s "
                  f"{c['license_id']:<9} {(c.get('name') or '')[:44]:<46}{flag}")
        if not r["candidates"]:
            print("    (khong co ung vien)")
        report.append(r)

    REPORT_JSON.write_text(
        json.dumps({"license": args.license, "codes": report},
                   ensure_ascii=False, indent=1),
        encoding="utf-8")
    write_markdown(report, args.license)

    n = sum(len(r["candidates"]) for r in report)
    warn = sum(1 for r in report for c in r["candidates"] if c.get("canh_bao"))
    print(f"\nXong: {n} ung vien cho {len(codes)} ma ({warn} co canh bao).")
    print(f"  -> {REPORT_JSON}")
    print(f"  -> {REPORT_MD}")
    print("  -> file tai o .work/freesound/ (CHUA dua vao assets/sfx/)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
