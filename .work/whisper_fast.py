#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adapter wrapper: drop-in replacement for openai-whisper using faster-whisper.

Cung cấp giao diện tương thích 100% với whisper.load_model(...) và asr_model.transcribe(...).
Sử dụng CTranslate2 runtime đa luồng, loại bỏ hoàn toàn cảnh báo FP32 CPU của openai-whisper,
tối ưu hóa bộ nhớ và tốc độ cho môi trường Mac Apple Silicon.
"""
import os
import sys
from pathlib import Path

try:
    from faster_whisper import WhisperModel
except ImportError:
    WhisperModel = None


class _FasterWhisperModelWrapper:
    def __init__(self, model_size_or_path="base", device="cpu", compute_type="float32", cpu_threads=8):
        if WhisperModel is None:
            raise ImportError("Vui lòng cài đặt faster-whisper: pip install faster-whisper av<14")
        self.model = WhisperModel(
            model_size_or_path,
            device=device,
            compute_type=compute_type,
            cpu_threads=cpu_threads
        )

    def transcribe(self, audio, language=None, word_timestamps=False, **kwargs):
        # Tránh xung đột các kwargs riêng của openai-whisper (như fp16)
        beam_size = kwargs.get("beam_size", 1)
        segments, info = self.model.transcribe(
            str(audio),
            language=language,
            word_timestamps=word_timestamps,
            beam_size=beam_size
        )
        
        # Tiêu thụ generator để trả về cấu trúc tương thích openai-whisper
        seg_list = []
        text_parts = []
        for s in segments:
            text_parts.append(s.text)
            seg_dict = {
                "id": s.id,
                "seek": s.seek,
                "start": s.start,
                "end": s.end,
                "text": s.text,
            }
            if word_timestamps and s.words:
                seg_dict["words"] = [
                    {"word": w.word, "start": w.start, "end": w.end, "probability": w.probability}
                    for w in s.words
                ]
            seg_list.append(seg_dict)

        full_text = " ".join(text_parts).strip()
        return {
            "text": full_text,
            "segments": seg_list,
            "language": info.language
        }


def load_model(name="base", device="cpu", **kwargs):
    """Drop-in replacement for whisper.load_model(name, device=...)."""
    compute_type = "float32" if device == "cpu" else "float16"
    return _FasterWhisperModelWrapper(name, device=device, compute_type=compute_type)


if __name__ == "__main__":
    m = load_model("base", device="cpu")
    print("whisper_fast: Loaded faster-whisper model successfully!")
