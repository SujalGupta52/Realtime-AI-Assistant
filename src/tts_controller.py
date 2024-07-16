import wave
from piper.voice import PiperVoice


class TTS_controller:
    def __init__(self):
        self.voice = PiperVoice.load(
            "/home/sujal/repos/untitled-ai-project/models/en_US-lessac-medium.onnx",
            "/home/sujal/repos/untitled-ai-project/models/en_US-lessac-medium.onnx.json",
            use_cuda=False,
        )

    def generate(self, text, output_path):
        wav_file = wave.open(output_path, "w")
        audio = self.voice.synthesize(text, wav_file)


if __name__ == "__main__":
    tts = TTS_controller()
    import time

    start_time = time.time()
    print(
        tts.generate(
            "Hello World, this is a example of a real time chatbot",
            "sample_audio/output.wav",
        )
    )
    print("--- %s seconds ---" % (time.time() - start_time))
