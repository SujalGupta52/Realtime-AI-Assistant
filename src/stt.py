import whisper_s2t
from pydub import AudioSegment
from pydub.utils import make_chunks
import shutil
import os
import time


def split_audio(file):
    myaudio = AudioSegment.from_file(file, "mp3")
    chunk_length_ms = 20000
    chunks = make_chunks(myaudio, chunk_length_ms)
    files = []
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.mp3".format(i)
        chunk.export(f"./data/temp/{chunk_name}", format="mp3")
        files.append(f"./data/temp/{chunk_name}")
    return files


def stt(file):  # Takes file path
    try:
        os.mkdir("./data/temp")
    except:
        shutil.rmtree("./data/temp")
    model = whisper_s2t.load_model(model_identifier="tiny", backend="CTranslate2")
    lang_codes = ["en"]
    tasks = ["transcribe"]
    initial_prompts = [None]
    files = split_audio(file)
    time.sleep(0.3)
    for i, file in enumerate(files):
        out = model.transcribe(
            files,
            lang_codes=lang_codes,
            tasks=tasks,
            initial_prompts=initial_prompts,
            batch_size=32,
        )
        yield out[i][0]
    shutil.rmtree("./data/temp")


if __name__ == "__main__":
    for data in stt("data/sample_audio/White_Knights_Aleesha_Bake.mp3"):
        print(data['text'])
