from llm_controller import LLM_controller
from stt_controller import STT_controller
from tts_controller import TTS_controller
import time


class Model_handler:
    def __init__(self):
        self.stt = STT_controller("tiny")
        self.llm = LLM_controller(
            model_path="models/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf", verbose=False
        )

    def generate(self, speech_file):
        stt_output = self.stt.generate(speech_file)
        llm_output = self.llm.generate(stt_output)
        TTS_controller().generate(llm_output["answer"], "temp/output.wav")
        return llm_output


if __name__ == "__main__":
    model = Model_handler()
    start = time.time()
    model.generate("sample_audio/sample_command.wav")
    print("--- %s seconds ---" % (time.time() - start))
    start = time.time()
    model.generate("sample_audio/sample_command.wav")
    print("--- %s seconds ---" % (time.time() - start))
    start = time.time()
    model.generate("sample_audio/sample_command.wav")
    print("--- %s seconds ---" % (time.time() - start))
