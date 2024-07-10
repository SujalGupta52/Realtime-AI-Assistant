from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

# generate speech by cloning a voice using default settings
tts.tts_to_file(
    text="It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.",
    file_path="output.wav",
    speaker_wav="data/sample_audio/White_Knights_Aleesha_Bake.mp3",
    language="en",
)
