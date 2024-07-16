from llama_cpp import Llama
import json


class LLM_controller:
    def __init__(
        self,
        model_path,
        verbose=True,
        temperature=0.3,
    ):
        self.temperature = temperature
        self.llm = Llama(
            model_path=model_path,
            n_gpu_layers=-1,
            verbose=verbose,
            flash_attn=True,
        )

    def generate(self, message):
        return self.llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": """You are a very helpful tour guide, fluent in English and JSON.
                        Your task is to parse user intent and list of locations user need.

                        Rules:
                        - leave unknown fields blank

                        Respond with no other text but a JSON document like this example JSON document:
                        {
                        "intent": <navigation | general_query | get_location>,
                        "to": <only in case of navigation intent>,
                        "from":  <only in case of navigation intent>,
                        "answer": <Reply as a helpful assistant, keep in very short and to the point>,
                        "places_required": <Array of locations user want from above answers, only in case of get_location or general_query>,
                        }
                        """,
                },
                {
                    "role": "user",
                    "content": f"Input Data: {message}",
                },
            ],
            temperature=self.temperature,
        )

    def parse_json_from_llm(self, message_with_json):
        str = message_with_json.replace("\n", "")
        start_idx = -1
        end_idx = -1
        for i in range(len(str)):
            if str[i] == "{":
                start_idx = i
                break
        for i in range(len(str) - 1, -1, -1):
            if str[i] == "}":
                end_idx = i
                break
        json_output = str[start_idx : end_idx + 1]
        return json.loads(json_output)


if __name__ == "__main__":
    llm = LLM_controller(
        model_path="models/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
        verbose=False,
        temperature=0.1,
    )
    out = llm.generate("Generate a itenary for my banglore trip")["choices"][0][
        "message"
    ]["content"]
    print(llm.parse_json_from_llm(out))
