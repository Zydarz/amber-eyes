import sys
import time

print("Testing environment...")
try:
    from mlx_audio.tts.utils import load as load_higgs
    print("mlx_audio load imported successfully!")
except Exception as e:
    print("Error importing mlx_audio:", e)
