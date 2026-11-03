#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""measure_quality_utmos.py — Đánh giá chất lượng âm thanh toàn diện bằng Whisper (CER) và UTMOSv2 (MOS).
Usage:
  python3 .work/measure_quality_utmos.py --ep 04 --lang en
  python3 .work/measure_quality_utmos.py --dir .work/audio_s_higgs_EN_t04
"""
import os
import sys
import json
import argparse
import pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import en_cer

import whisper
import utmosv2

def main():
    parser = argparse.ArgumentParser(description="Đo chất lượng âm thanh qua Whisper CER và UTMOSv2 MOS")
    parser.add_argument("--ep", type=str, default="04", help="Mã tập (ví dụ 04, 05)")
    parser.add_argument("--lang", type=str, default="en", help="Ngôn ngữ (en, vi, ja, ko)")
    parser.add_argument("--dir", type=str, default=None, help="Đường dẫn thư mục audio cần đo")
    parser.add_argument("--limit", type=int, default=None, help="Giới hạn số câu đo (test nhanh)")
    args = parser.parse_args()

    if args.dir:
        audio_dir = pathlib.Path(args.dir)
    else:
        suffix = f"_{args.lang.upper()}_t{args.ep.zfill(2)}" if args.lang != "vi" else f"_t{args.ep.zfill(2)}"
        audio_dir = HERE / f"audio_s_higgs{suffix}"

    if not audio_dir.exists():
        print(f"!! Thư mục không tồn tại: {audio_dir}")
        sys.exit(1)

    print("=" * 80)
    print(f"KIỂM SOÁT CHẤT LƯỢNG AUDIO: WHISPER (CER) & UTMOSv2 (MOS)")
    print(f"Thư mục: {audio_dir}")
    print("=" * 80, flush=True)

    # 1. Load manifest if available
    man_path = audio_dir / "higgs_manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8")) if man_path.exists() else {}

    wav_files = sorted(audio_dir.glob("*.wav"))
    if args.limit:
        wav_files = wav_files[:args.limit]
    print(f"Tìm thấy {len(wav_files)} file .wav cần đánh giá.", flush=True)

    # 2. Load models
    print("\n[1/3] Đang tải mô hình Whisper...")
    asr_model = whisper.load_model("base", device="cpu")
    print("  Whisper base đã sẵn sàng.")

    print("\n[2/3] Đang tải mô hình UTMOSv2...")
    utmos_model = utmosv2.create_model(pretrained=True)
    print("  UTMOSv2 đã sẵn sàng.")

    # 3. Predict & Measure
    print("\n[3/3] Đang phân tích âm thanh...", flush=True)
    results = []
    
    for idx, wpath in enumerate(wav_files):
        sid = None
        orig_text = ""
        role = "Unknown"
        # Match with manifest
        for k, v in man.items():
            if v.get("file") == wpath.name or wpath.name.endswith(v.get("file", "")):
                sid = k
                orig_text = v.get("text", "")
                role = v.get("role", "Unknown")
                break
        
        # Whisper ASR
        res_asr = asr_model.transcribe(str(wpath), language=args.lang if args.lang != "en" else "en")
        hyp_text = res_asr.get("text", "").strip()
        if args.lang == "ja":
            import ja_cer
            cer_val = ja_cer.cer_pair(orig_text, hyp_text) if orig_text else 0.0
        elif args.lang == "vi":
            import vi_cer
            cer_val = vi_cer.cer_pair(orig_text, hyp_text) if orig_text else 0.0
        else:
            cer_val = en_cer.cer_pair(orig_text, hyp_text) if orig_text else 0.0

        # UTMOSv2 MOS
        try:
            mos_score = float(utmos_model.predict(input_path=str(wpath), device="cpu", verbose=False))
        except Exception as ex:
            print(f"  !! Lỗi UTMOS {wpath.name}: {ex}")
            mos_score = 0.0

        results.append({
            "file": wpath.name,
            "id": sid or wpath.stem,
            "role": role,
            "orig_text": orig_text,
            "asr_text": hyp_text,
            "cer": cer_val,
            "utmos": mos_score
        })

        tag = "OK" if cer_val <= 0.02 and mos_score >= 3.0 else "WARN"
        print(f"  [{idx+1:03d}/{len(wav_files)}] {wpath.name} | Vai: {role} | CER: {cer_val*100:5.2f}% | MOS: {mos_score:.2f} [{tag}]", flush=True)

    # Summary
    print("\n" + "=" * 80)
    print("TỔNG KẾT CHẤT LƯỢNG:")
    cers = [r["cer"] for r in results if r["orig_text"]]
    moss = [r["utmos"] for r in results if r["utmos"] > 0]
    if cers:
        print(f"  Whisper CER: trung bình = {np.mean(cers)*100:.2f}%, trung vị = {np.median(cers)*100:.2f}%, >2%: {sum(1 for c in cers if c > 0.02)}/{len(cers)}")
    if moss:
        print(f"  UTMOSv2 MOS: trung bình = {np.mean(moss):.2f}/5.0, min = {np.min(moss):.2f}, max = {np.max(moss):.2f}")
    print("=" * 80)

    # Save report
    out_json = HERE / f"quality_qc_utmos_ep{args.ep}_{args.lang}.json"
    out_json.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Đã lưu kết quả chi tiết vào: {out_json}")

if __name__ == "__main__":
    main()
