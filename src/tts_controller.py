from TTS.api import TTS


class TTS_controller:
    def __init__(self, source_voice):
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
        self.source_voice = source_voice

    def generate(self, text, output_path):
        self.tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker_wav=self.source_voice,
            language="en",
        )


if __name__ == "__main__":
    tts = TTS_controller("sample_audio/White_Knights_Aleesha_Bake.mp3")
    import time

    start_time = time.time()
    print(
        tts.generate(
            "Hello World, this is a example of a real time chatbot",
            "sample_audio/output.wav",
        )
    )
    print("--- %s seconds ---" % (time.time() - start_time))
