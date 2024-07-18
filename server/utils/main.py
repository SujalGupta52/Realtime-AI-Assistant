from utils.llm_controller import LLM_controller
from utils.stt_controller import STT_controller
from utils.tts_controller import TTS_controller
import time


class Model_handler:
    def __init__(self):
        self.stt = STT_controller("base")
        self.llm = LLM_controller(
            model_path="models/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf", verbose=False
        )
        self.tts = TTS_controller()
        self.id = 0

    def generate(self, input_file, output_dir):
        stt_output = self.stt.generate(input_file)
        llm_output = self.llm.generate(stt_output)
        self.tts.generate(
            self.llm.parse_json_from_llm(llm_output)["answer"],
            output_dir + "output.wav",
        )
        self.id = self.id + 1
        return llm_output


if __name__ == "__main__":
    model = Model_handler()
    start = time.time()
    model.generate("sample_audio/test.wav", "server/static/generated/")
    print("--- %s seconds ---" % (time.time() - start))
    start = time.time()
    model.generate("sample_audio/test.wav", "server/static/generated/")
    print("--- %s seconds ---" % (time.time() - start))
    start = time.time()
    model.generate("sample_audio/test.wav", "server/static/generated/")
    print("--- %s seconds ---" % (time.time() - start))
