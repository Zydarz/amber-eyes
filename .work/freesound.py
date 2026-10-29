#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Freesound.org API v2 Client & SFX Pipeline Integration cho Amber Eyes.

Cung cấp:
  1. FreesoundClient: tìm kiếm, lấy metadata, tải audio (HQ preview hoặc bản gốc qua OAuth2).
  2. Xử lý audio bằng FFmpeg theo chuẩn kênh: 44.1 kHz, 16-bit PCM WAV, 2 kênh, chuẩn hoá đỉnh.
  3. Quản lý bản quyền & tự động ghi nhận vào provenance.json (quy tắc L7, A3, V8).
  4. Giao diện dòng lệnh (CLI): test, search, info, download, import, oauth-url, oauth-token.

Sử dụng:
  py -3 .work/freesound.py test
  py -3 .work/freesound.py search "gunshot" --cc0
  py -3 .work/freesound.py info 80928
  py -3 .work/freesound.py download 80928 --out my_sound.wav
  py -3 .work/freesound.py import 80928 --code fx_door_slam --ep 03
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
CONFIG_PATH = ROOT / ".work" / "freesound_config.json"
PROV_PATH = ROOT / "provenance.json"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFP = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

API_BASE = "https://freesound.org/apiv2"
DEFAULT_USER_AGENT = "AmberEyes-SFX/1.0 (https://youtube.com/@AmberEyes)"


def load_config():
    """Tải cấu hình từ freesound_config.json hoặc biến môi trường."""
    cfg = {
        "name": "TruyenKyAudio",
        "client_id": os.environ.get("FREESOUND_CLIENT_ID", "bL3AVUIgSQ6SnXzHIQjT"),
        "api_key": os.environ.get("FREESOUND_API_KEY", "TRVMxItbI2YoljN8he5ONZIAJcKgP2kfIw6XPvhK"),
        "client_secret": os.environ.get("FREESOUND_CLIENT_SECRET", "TRVMxItbI2YoljN8he5ONZIAJcKgP2kfIw6XPvhK"),
        "redirect_uri": "https://freesound.org/home/app_permissions/permission_granted/",
        "access_token": None,
        "refresh_token": None,
        "token_type": "Token"
    }
    if CONFIG_PATH.exists():
        try:
            with io.open(CONFIG_PATH, "r", encoding="utf-8") as f:
                saved = json.load(f)
                cfg.update(saved)
        except Exception as e:
            print(f"[CẢNH BÁO] Không đọc được file config {CONFIG_PATH}: {e}")
    return cfg


def save_config(cfg):
    """Lưu cấu hình vào freesound_config.json."""
    with io.open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def analyze_license(license_url):
    """Phân tích giấy phép Creative Commons cho thương mại và YouTube."""
    lic_lower = (license_url or "").lower()
    if "zero/1.0" in lic_lower or "publicdomain" in lic_lower:
        return {
            "type": "CC0",
            "commercial": "đạt (CC0 - Public Domain, được dùng thương mại không cần ghi công)",
            "safe_for_monetization": True,
            "requires_attribution": False,
            "term": "Creative Commons 0 (Public Domain Dedication) — Miễn phí hoàn toàn, không bắt buộc ghi công."
        }
    elif "/by-nc/" in lic_lower:
        return {
            "type": "CC-BY-NC",
            "commercial": "KHÔNG ĐẠT (CC-BY-NC: Cấm dùng cho video bật kiếm tiền)",
            "safe_for_monetization": False,
            "requires_attribution": True,
            "term": "Creative Commons Attribution Non-Commercial — CẤM sử dụng trong nội dung có tạo doanh thu / kiếm tiền."
        }
    elif "/by/" in lic_lower:
        return {
            "type": "CC-BY",
            "commercial": "đạt (có điều kiện: phải ghi công tác giả trong phần mô tả video)",
            "safe_for_monetization": True,
            "requires_attribution": True,
            "term": "Creative Commons Attribution (CC-BY) — Cho phép thương mại nhưng BẮT BUỘC ghi tên tác giả, link sound và link license trong mô tả video."
        }
    elif "sampling" in lic_lower:
        return {
            "type": "Sampling+",
            "commercial": "cần kiểm tra kỹ (Sampling Plus 1.0)",
            "safe_for_monetization": False,
            "requires_attribution": True,
            "term": "Sampling+ License — Cần kiểm tra kỹ trước khi dùng cho video thương mại."
        }
    else:
        return {
            "type": "Khác",
            "commercial": f"chưa xác định rõ ({license_url})",
            "safe_for_monetization": False,
            "requires_attribution": True,
            "term": f"License URL: {license_url}"
        }


class FreesoundClient:
    def __init__(self, config=None):
        self.config = config or load_config()
        self.api_key = self.config.get("api_key")
        self.client_id = self.config.get("client_id")
        self.client_secret = self.config.get("client_secret")
        self.access_token = self.config.get("access_token")

    def _get_headers(self, use_oauth_if_available=True):
        headers = {"User-Agent": DEFAULT_USER_AGENT}
        if use_oauth_if_available and self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        elif self.api_key:
            headers["Authorization"] = f"Token {self.api_key}"
        return headers

    def test_connection(self):
        """Kiểm tra kết nối đến Freesound API và trả về thông tin trạng thái."""
        headers = self._get_headers(use_oauth_if_available=False)
        # Tìm thử 1 sound bất kỳ để kiểm tra API key
        url = f"{API_BASE}/search/text/?query=test&page_size=1&fields=id,name"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                result = {
                    "status": "connected",
                    "http_code": resp.status,
                    "auth_method": "Token (API Key)",
                    "app_name": self.config.get("name"),
                    "client_id": self.client_id,
                    "total_database_results": data.get("count", 0),
                    "oauth_authenticated": bool(self.access_token)
                }
                # Nếu có access_token OAuth2, kiểm tra thêm /me/
                if self.access_token:
                    try:
                        me_req = urllib.request.Request(f"{API_BASE}/me/", headers=self._get_headers(True))
                        with urllib.request.urlopen(me_req, timeout=10) as me_resp:
                            me_data = json.loads(me_resp.read().decode("utf-8"))
                            result["oauth_user"] = me_data.get("username")
                            result["auth_method"] = "OAuth2 (User Authenticated)"
                    except Exception:
                        result["oauth_error"] = "Access token hết hạn hoặc không hợp lệ"
                return result
        except urllib.error.HTTPError as e:
            return {
                "status": "error",
                "http_code": e.code,
                "reason": e.reason,
                "detail": e.read().decode("utf-8", errors="replace")
            }
        except Exception as e:
            return {"status": "error", "reason": str(e)}

    def search(self, query, filter_expr=None, sort="score", page=1, page_size=15, cc0_only=False):
        """Tìm kiếm âm thanh trên Freesound.

        Args:
            query: từ khóa tìm kiếm (tiếng Anh)
            filter_expr: biểu thức lọc (vd: 'duration:[0.5 TO 10.0]')
            sort: cách sắp xếp (score, rating_desc, downloads_desc, duration_asc, duration_desc)
            page: trang
            page_size: số kết quả mỗi trang (tối đa 150)
            cc0_only: chỉ lấy giấy phép CC0 (Public Domain) an toàn nhất
        """
        filters = []
        if filter_expr:
            filters.append(filter_expr)
        if cc0_only:
            filters.append('license:"Creative Commons 0"')

        params = {
            "query": query,
            "sort": sort,
            "page": page,
            "page_size": min(page_size, 150),
            "fields": "id,name,tags,description,license,duration,samplerate,channels,filesize,bitrate,bitdepth,username,previews,num_downloads,avg_rating"
        }
        if filters:
            params["filter"] = " ".join(filters)

        url = f"{API_BASE}/search/text/?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers=self._get_headers(False))
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            # Bổ sung phân tích license
            for item in data.get("results", []):
                item["license_analysis"] = analyze_license(item.get("license"))
            return data

    def get_sound(self, sound_id):
        """Lấy thông tin chi tiết của 1 âm thanh theo ID."""
        url = f"{API_BASE}/sounds/{sound_id}/"
        req = urllib.request.Request(url, headers=self._get_headers(False))
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            data["license_analysis"] = analyze_license(data.get("license"))
            return data

    def download_sound(self, sound_id, raw_output_path, prefer_original=True):
        """Tải file âm thanh về đĩa.

        Nếu có OAuth2 token và prefer_original=True: tải file gốc qua /sounds/<id>/download/
        Ngược lại hoặc khi lỗi: tải preview chất lượng cao (HQ MP3 preview).
        """
        raw_output_path = Path(raw_output_path)
        raw_output_path.parent.mkdir(parents=True, exist_ok=True)

        downloaded_type = None

        if prefer_original and self.access_token:
            orig_url = f"{API_BASE}/sounds/{sound_id}/download/"
            req = urllib.request.Request(orig_url, headers=self._get_headers(True))
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    with open(raw_output_path, "wb") as f:
                        f.write(resp.read())
                    downloaded_type = "original"
                    return raw_output_path, downloaded_type
            except Exception as e:
                print(f"[LƯU Ý] Không tải được bản gốc qua OAuth2 ({e}), chuyển sang tải HQ preview.")

        # Tải qua HQ preview
        info = self.get_sound(sound_id)
        previews = info.get("previews", {})
        preview_url = previews.get("preview-hq-mp3") or previews.get("preview-hq-ogg")
        if not preview_url:
            raise RuntimeError(f"Sound ID {sound_id} không có URL preview khả dụng.")

        req = urllib.request.Request(
            preview_url,
            headers={"User-Agent": DEFAULT_USER_AGENT, "Authorization": f"Token {self.api_key}"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(raw_output_path, "wb") as f:
                f.write(resp.read())
        downloaded_type = "preview-hq"
        return raw_output_path, downloaded_type

    def get_oauth_authorize_url(self):
        """Tạo URL cho người dùng xác thực tài khoản Freesound qua trình duyệt."""
        redirect_uri = self.config.get("redirect_uri")
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri
        }
        return f"{API_BASE}/oauth2/authorize/?{urllib.parse.urlencode(params)}"

    def exchange_oauth_code(self, code):
        """Đổi mã code OAuth lấy access_token & refresh_token."""
        data = urllib.parse.urlencode({
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.config.get("redirect_uri")
        }).encode("utf-8")

        req = urllib.request.Request(
            f"{API_BASE}/oauth2/access_token/",
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": DEFAULT_USER_AGENT}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            tokens = json.loads(resp.read().decode("utf-8"))
            self.access_token = tokens.get("access_token")
            self.config["access_token"] = tokens.get("access_token")
            self.config["refresh_token"] = tokens.get("refresh_token")
            save_config(self.config)
            return tokens


# ==============================================================================
# XỬ LÝ AUDIO BẰNG FFMPEG THEO TIÊU CHUẨN KÊNH
# ==============================================================================

def probe_audio(file_path):
    """Kiểm tra thông số kỹ thuật của file audio qua ffprobe."""
    if not FFP.exists():
        return {}
    cmd = [
        str(FFP), "-v", "error",
        "-show_entries", "format=duration,size:stream=codec_name,sample_rate,channels",
        "-of", "json", str(file_path)
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    try:
        d = json.loads(r.stdout or "{}")
        st = (d.get("streams") or [{}])[0]
        fmt = d.get("format") or {}
        return {
            "codec": st.get("codec_name"),
            "sample_rate": int(st.get("sample_rate") or 0),
            "channels": int(st.get("channels") or 0),
            "duration": float(fmt.get("duration") or 0.0),
            "size": int(fmt.get("size") or 0)
        }
    except Exception:
        return {}


def detect_peak_volume(file_path):
    """Đo peak volume (dBFS) bằng ffmpeg volumedetect."""
    if not FF.exists():
        return None
    cmd = [str(FF), "-hide_banner", "-i", str(file_path), "-af", "volumedetect", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    m = re.search(r"max_volume:\s*(-?[\d.]+)\s*dB", r.stderr)
    return float(m.group(1)) if m else None


def convert_to_channel_standard(input_path, output_path, target_peak=-0.5, cut_start=None, cut_duration=None):
    """Chuyển đổi âm thanh về chuẩn của kênh Amber Eyes:

    - Codec: pcm_s16le (WAV 16-bit)
    - Sample rate: 44,100 Hz
    - Channels: 2 (Stereo)
    - Peak chuẩn hoá: target_peak dBFS (mặc định -0.5 dBFS)
    """
    input_path = Path(input_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Bước 1: Cắt & convert cơ bản sang wav tạm
    temp_wav = output_path.with_suffix(".tmp.wav")

    cmd = [str(FF), "-hide_banner", "-y"]
    if cut_start is not None:
        cmd.extend(["-ss", str(cut_start)])
    cmd.extend(["-i", str(input_path)])
    if cut_duration is not None:
        cmd.extend(["-t", str(cut_duration)])

    cmd.extend([
        "-ac", "2",
        "-ar", "44100",
        "-c:a", "pcm_s16le",
        str(temp_wav)
    ])

    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if r.returncode != 0 or not temp_wav.exists():
        raise RuntimeError(f"FFmpeg convert lỗi: {r.stderr}")

    # Bước 2: Đo peak volume và điều chỉnh độ lợi (gain)
    current_peak = detect_peak_volume(temp_wav)
    if current_peak is not None and current_peak > -90.0:
        gain = target_peak - current_peak
        if abs(gain) >= 0.1:
            cmd_gain = [
                str(FF), "-hide_banner", "-y",
                "-i", str(temp_wav),
                "-af", f"volume={gain:+.2f}dB",
                "-c:a", "pcm_s16le",
                str(output_path)
            ]
            subprocess.run(cmd_gain, capture_output=True, text=True, errors="replace")
            if temp_wav.exists():
                temp_wav.unlink()
        else:
            if output_path.exists():
                output_path.unlink()
            temp_wav.rename(output_path)
    else:
        if output_path.exists():
            output_path.unlink()
        temp_wav.rename(output_path)

    pr = probe_audio(output_path)
    new_peak = detect_peak_volume(output_path)
    return {
        "output_path": str(output_path),
        "duration": pr.get("duration", 0.0),
        "sample_rate": pr.get("sample_rate"),
        "channels": pr.get("channels"),
        "codec": pr.get("codec"),
        "peak_db": new_peak
    }


# ==============================================================================
# QUẢN LÝ NGUỒN GỐC (PROVENANCE.JSON) — QUY TẮC L7
# ==============================================================================

def append_provenance_entry(entry):
    """Ghi thêm một mục tài sản vào provenance.json (bảo tồn mục cũ)."""
    prov_data = []
    if PROV_PATH.exists():
        try:
            with io.open(PROV_PATH, "r", encoding="utf-8") as f:
                prov_data = json.load(f)
                if not isinstance(prov_data, list):
                    prov_data = []
        except Exception as e:
            print(f"[CẢNH BÁO] Không đọc được provenance.json: {e}")
            prov_data = []

    # Kiểm tra xem file đã tồn tại trong provenance chưa
    existing_idx = None
    for i, item in enumerate(prov_data):
        if item.get("file") == entry.get("file"):
            existing_idx = i
            break

    if existing_idx is not None:
        prov_data[existing_idx] = entry
    else:
        prov_data.append(entry)

    with io.open(PROV_PATH, "w", encoding="utf-8") as f:
        json.dump(prov_data, f, ensure_ascii=False, indent=2)


def import_sfx_from_freesound(sound_id, code_name, ep=None, subfolder=None, category="tiếng động (SFX)",
                              target_peak=-0.5, cut_start=None, cut_duration=None):
    """Tải SFX từ Freesound, chuẩn hoá sang WAV, lưu vào assets/sfx/ và ghi provenance.json.

    Args:
        sound_id: Freesound sound ID (int hoặc str)
        code_name: mã hiệu ứng (vd: fx_gunshot, amb_rain)
        ep: số tập (vd: '03' hoặc 3) nếu lưu theo tập assets/sfx/tXX/
        subfolder: thư mục con tuỳ chọn trong assets/sfx/
        category: 'tiếng động (SFX)' hoặc 'nền môi trường (ambience)'
    """
    client = FreesoundClient()
    sound_info = client.get_sound(sound_id)
    lic_info = sound_info["license_analysis"]

    # Xác định đường dẫn file đích trong assets/sfx/
    if ep:
        ep_str = f"t{int(ep):02d}"
        dest_dir = ROOT / "assets" / "sfx" / ep_str
        rel_path = f"assets/sfx/{ep_str}/{code_name}.wav"
    elif subfolder:
        dest_dir = ROOT / "assets" / "sfx" / subfolder
        rel_path = f"assets/sfx/{subfolder}/{code_name}.wav"
    else:
        dest_dir = ROOT / "assets" / "sfx"
        rel_path = f"assets/sfx/{code_name}.wav"

    dest_dir.mkdir(parents=True, exist_ok=True)
    final_wav_path = dest_dir / f"{code_name}.wav"

    # Thư mục tạm tải về
    temp_dir = ROOT / ".work" / "_freesound_dl"
    temp_dir.mkdir(parents=True, exist_ok=True)
    temp_raw = temp_dir / f"fs_{sound_id}_raw"

    print(f">> Đang tải Freesound #{sound_id}: '{sound_info.get('name')}' của {sound_info.get('username')}...")
    raw_path, dl_type = client.download_sound(sound_id, temp_raw)

    print(f">> Đang chuyển đổi sang chuẩn kênh (WAV 44.1kHz stereo, peak {target_peak} dBFS)...")
    res = convert_to_channel_standard(
        raw_path,
        final_wav_path,
        target_peak=target_peak,
        cut_start=cut_start,
        cut_duration=cut_duration
    )

    # Dọn dẹp file thô tạm
    if raw_path.exists():
        raw_path.unlink()

    # Tạo mục provenance.json tuân thủ quy tắc L7 và V8
    author = sound_info.get("username", "Unknown")
    license_url = sound_info.get("license", "")
    attribution_text = f"'{sound_info.get('name')}' by {author} ({sound_info.get('url', f'https://freesound.org/s/{sound_id}/')})"

    prov_entry = {
        "file": rel_path,
        "loai": category,
        "cong_cu": f"Freesound.org (API v2) — tải qua .work/freesound.py (Freesound ID: {sound_id})",
        "ngay": str(date.today()),
        "prompt": None,
        "seed": None,
        "mo_ta": f"{sound_info.get('name', code_name)} (tác giả: {author})",
        "font": None,
        "dieu_khoan": f"Freesound.org — License: {license_url}. {lic_info['term']}",
        "kiem_tra_thuong_mai": lic_info["commercial"],
        "freesound_id": sound_id,
        "freesound_user": author,
        "freesound_license": license_url,
        "freesound_license_type": lic_info["type"],
        "freesound_url": sound_info.get("url", f"https://freesound.org/s/{sound_id}/"),
        "thoi_luong_sau_cat": res["duration"],
        "thoi_luong_goc": sound_info.get("duration", 0.0),
        "peak_dbfs": res.get("peak_db")
    }

    if lic_info["requires_attribution"]:
        prov_entry["ghi_chu_mo_ta_youtube"] = f"Sound effect: {attribution_text} licensed under {lic_info['type']}"

    append_provenance_entry(prov_entry)
    print(f">> Đã nhập thành công: {rel_path} ({res['duration']:.2f}s, peak {res['peak_db']} dBFS)")
    print(f">> Trạng thái thương mại: {lic_info['commercial']}")
    if lic_info["requires_attribution"]:
        print(f">> [LƯU Ý GHI CÔNG] Cần thêm vào mô tả YouTube: Sound effect: {attribution_text}")

    return {
        "file": rel_path,
        "dest": str(final_wav_path),
        "audio_info": res,
        "provenance": prov_entry
    }


# ==============================================================================
# GIAO DIỆN DÒNG LỆNH (CLI)
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Freesound.org API Tool cho Amber Eyes")
    subparsers = parser.add_subparsers(dest="subcommand", help="Lệnh cần thực hiện")

    # Command: test
    subparsers.add_parser("test", help="Kiểm tra kết nối và trạng thái API Freesound")

    # Command: search
    p_search = subparsers.add_parser("search", help="Tìm kiếm âm thanh trên Freesound")
    p_search.add_argument("query", help="Từ khóa tìm kiếm (tiếng Anh)")
    p_search.add_argument("--filter", dest="filter_expr", help="Bộ lọc (vd: duration:[0.5 TO 5.0])")
    p_search.add_argument("--cc0", action="store_true", help="Chỉ lấy âm thanh CC0 (Public Domain - an toàn nhất)")
    p_search.add_argument("--sort", default="score", help="Sắp xếp: score, rating_desc, downloads_desc, duration_asc")
    p_search.add_argument("--limit", type=int, default=10, help="Số kết quả hiển thị (mặc định: 10)")
    p_search.add_argument("--page", type=int, default=1, help="Số trang (mặc định: 1)")

    # Command: info
    p_info = subparsers.add_parser("info", help="Xem chi tiết một âm thanh theo ID")
    p_info.add_argument("sound_id", type=int, help="ID của âm thanh trên Freesound")

    # Command: download
    p_dl = subparsers.add_parser("download", help="Tải âm thanh về file chỉ định")
    p_dl.add_argument("sound_id", type=int, help="ID của âm thanh")
    p_dl.add_argument("--out", required=True, help="Đường dẫn file lưu (sẽ tự động chuyển thành WAV chuẩn)")
    p_dl.add_argument("--peak", type=float, default=-0.5, help="Đỉnh dBFS chuẩn hoá (mặc định -0.5)")

    # Command: import
    p_imp = subparsers.add_parser("import", help="Tải và nhập trực tiếp vào assets/sfx/ + cập nhật provenance.json")
    p_imp.add_argument("sound_id", type=int, help="ID của âm thanh trên Freesound")
    p_imp.add_argument("--code", required=True, help="Mã SFX (vd: fx_metal_gate, amb_dark_hall)")
    p_imp.add_argument("--ep", help="Số tập (vd: 03 hoặc 2) để lưu vào assets/sfx/tXX/")
    p_imp.add_argument("--amb", action="store_true", help="Đánh dấu là nền môi trường (mặc định là tiếng động)")
    p_imp.add_argument("--peak", type=float, default=-0.5, help="Đỉnh dBFS chuẩn hoá")
    p_imp.add_argument("--start", type=float, help="Thời điểm bắt đầu cắt (giây)")
    p_imp.add_argument("--dur", type=float, help="Thời lượng cắt (giây)")

    # Command: oauth-url
    subparsers.add_parser("oauth-url", help="Tạo URL ủy quyền OAuth2 để tải file gốc chất lượng cao nhất")

    # Command: oauth-token
    p_oauthtok = subparsers.add_parser("oauth-token", help="Đổi authorization code lấy access token OAuth2")
    p_oauthtok.add_argument("code", help="Authorization code nhận được sau khi bấm Authorize trên Freesound")

    args = parser.parse_args()

    if not args.subcommand or args.subcommand == "test":
        client = FreesoundClient()
        res = client.test_connection()
        print("=== KẾT QUẢ KẾT NỐI FREESOUND.ORG ===")
        print(f"Trạng thái: {'THÀNH CÔNG' if res.get('status') == 'connected' else 'THẤT BẠI'}")
        for k, v in res.items():
            print(f" - {k}: {v}")
        if res.get("status") == "connected":
            print("\n[OK] Đã kết nối thành công với Freesound.org API v2 bằng API key của TruyenKyAudio.")
        return

    client = FreesoundClient()

    if args.subcommand == "search":
        print(f">> Đang tìm kiếm: '{args.query}' (CC0 only: {args.cc0}, Sort: {args.sort})...")
        res = client.search(
            query=args.query,
            filter_expr=args.filter_expr,
            sort=args.sort,
            page=args.page,
            page_size=args.limit,
            cc0_only=args.cc0
        )
        total = res.get("count", 0)
        items = res.get("results", [])
        print(f">> Tìm thấy tổng cộng: {total} kết quả (hiển thị {len(items)} mục):")
        print("-" * 88)
        print(f"{'ID':<8} | {'Thời lượng':<10} | {'Giấy phép':<10} | {'Tác giả':<16} | {'Tên âm thanh'}")
        print("-" * 88)
        for s in items:
            lic = s["license_analysis"]["type"]
            dur = f"{s.get('duration', 0.0):.1f}s"
            name = s.get("name", "")[:35]
            user = s.get("username", "")[:16]
            print(f"{s['id']:<8} | {dur:<10} | {lic:<10} | {user:<16} | {name}")
        print("-" * 88)

    elif args.subcommand == "info":
        sound = client.get_sound(args.sound_id)
        lic = sound["license_analysis"]
        print(f"=== CHI TIẾT ÂM THANH #{sound.get('id')}: {sound.get('name')} ===")
        print(f"- Tác giả: {sound.get('username')}")
        print(f"- Thời lượng: {sound.get('duration')}s")
        print(f"- Định dạng gốc: {sound.get('type')} ({sound.get('samplerate')}Hz, {sound.get('channels')}ch, {sound.get('bitdepth')}bit)")
        print(f"- Lượt tải: {sound.get('num_downloads')} | Đánh giá: {sound.get('avg_rating', 0):.2f}/5")
        print(f"- Giấy phép: {sound.get('license')} ({lic['type']})")
        print(f"- Khả năng dùng thương mại: {lic['commercial']}")
        print(f"- Mô tả: {sound.get('description', '')[:200]}...")
        print(f"- URL Freesound: {sound.get('url')}")
        previews = sound.get("previews", {})
        print(f"- Preview MP3: {previews.get('preview-hq-mp3')}")

    elif args.subcommand == "download":
        dest = Path(args.out)
        temp_raw = ROOT / ".work" / "_freesound_dl" / f"raw_{args.sound_id}"
        temp_raw.parent.mkdir(parents=True, exist_ok=True)
        print(f">> Đang tải sound #{args.sound_id}...")
        raw_path, dl_type = client.download_sound(args.sound_id, temp_raw)
        print(f">> Chuyển đổi sang {dest}...")
        res = convert_to_channel_standard(raw_path, dest, target_peak=args.peak)
        if raw_path.exists():
            raw_path.unlink()
        print(f"[OK] Đã lưu file: {dest} ({res['duration']:.2f}s, peak {res['peak_db']} dBFS)")

    elif args.subcommand == "import":
        cat = "nền môi trường (ambience)" if args.amb else "tiếng động (SFX)"
        import_sfx_from_freesound(
            sound_id=args.sound_id,
            code_name=args.code,
            ep=args.ep,
            category=cat,
            target_peak=args.peak,
            cut_start=args.start,
            cut_duration=args.dur
        )

    elif args.subcommand == "oauth-url":
        url = client.get_oauth_authorize_url()
        print("=== FREESOUND OAUTH2 AUTHORIZATION ===")
        print("Nếu bạn muốn tải trực tiếp file gốc không nén (lossless WAV/FLAC) thay vì HQ MP3 preview:")
        print("1. Mở URL sau trong trình duyệt đã đăng nhập tài khoản Freesound của bạn:")
        print(f"\n   {url}\n")
        print("2. Bấm nút 'Authorize'.")
        print("3. Trình duyệt sẽ chuyển hướng đến Redirect URL kèm tham số '?code=...'.")
        print("4. Sao chép chuỗi mã code đó và chạy lệnh:")
        print("   py -3 .work/freesound.py oauth-token <MA_CODE>")

    elif args.subcommand == "oauth-token":
        print(f">> Đang đổi authorization code lấy access token...")
        try:
            tokens = client.exchange_oauth_code(args.code)
            print("[THÀNH CÔNG] Đã lưu OAuth2 access token vào .work/freesound_config.json!")
            print(f"- Scope: {tokens.get('scope')}")
            print(f"- Expires in: {tokens.get('expires_in')} seconds")
        except Exception as e:
            print(f"[LỖI] Đổi code thất bại: {e}")


if __name__ == "__main__":
    main()
