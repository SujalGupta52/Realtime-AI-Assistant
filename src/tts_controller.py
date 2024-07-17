import wave
from piper.voice import PiperVoice
import time


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
    # TODO: Crashes if try to generate from same instance twice, creating a new instance take 1s extra
    start_time = time.time()
    tts = TTS_controller()

    print(
        tts.generate(
            "Please generate a itenary for my kolkata trip  ",
            "sample_audio/sample_command.wav",
        )
    )
    print("--- %s seconds ---" % (time.time() - start_time))
