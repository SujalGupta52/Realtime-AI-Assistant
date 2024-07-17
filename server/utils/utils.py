from pydub import AudioSegment
from pydub.utils import make_chunks
import os, shutil


def split_audio(file):
    myaudio = AudioSegment.from_file(file, "mp3")
    chunk_length_ms = 20000
    chunks = make_chunks(myaudio, chunk_length_ms)
    files = []
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.mp3".format(i)
        chunk.export(f"temp/{chunk_name}", format="wav")
        files.append(f"temp/{chunk_name}")
    return files


def clear_temp():
    folder = "temp"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))
