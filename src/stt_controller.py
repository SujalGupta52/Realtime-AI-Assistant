import whisper_s2t


class STT_controller:
    def __init__(self, model_name="tiny"):
        self.model = whisper_s2t.load_model(
            model_identifier=model_name, backend="CTranslate2"
        )

    def generate(self, file):  # Takes file path
        lang_codes = ["en", "hi"]
        tasks = ["transcribe"]
        initial_prompts = [None]
        files = [file]
        out = self.model.transcribe(
            files,
            lang_codes=lang_codes,
            tasks=tasks,
            initial_prompts=initial_prompts,
            batch_size=64,
        )
        final_output = ""
        for chunks in out[0]:
            final_output += chunks["text"]
        return final_output


if __name__ == "__main__":
    stt = STT_controller()
    print(stt.generate("sample_audio/output.wav"))
