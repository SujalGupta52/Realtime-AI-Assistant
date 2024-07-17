from styletts2 import tts

# No paths provided means default checkpoints/configs will be downloaded/cached.
my_tts = tts.StyleTTS2()

# Optionally create/write an output WAV file.
out = my_tts.inference(
    "Hello there, I am now a python package.", output_wav_file="temp/test.wav"
)
