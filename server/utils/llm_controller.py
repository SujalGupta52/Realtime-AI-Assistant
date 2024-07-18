from llama_cpp import Llama
import json


class LLM_controller:
    def __init__(
        self,
        model_path,
        verbose=True,
        temperature=0.5,
    ):
        self.temperature = temperature
        self.llm = Llama(
            model_path=model_path,
            n_gpu_layers=-1,
            verbose=verbose,
            flash_attn=True,
        )

    def generate(self, message):
        out = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": """You are a very helpful tour guide, fluent in English and JSON.
                        Your task is to parse user intent and list of locations user need.
                        Pretend you are connected to a map and can control it and mark location according to user query, answer as such, but DONT GIVE ANY DIRECTION TO THE USER, GIVE GENERIC ANSWER like "I marked it on your map" and  "I marked the route", be creative

                        Rules:
                        - leave unknown fields blank

                        Respond with no other text but a JSON document exactly like this example JSON document:
                        {
                        "intent": <navigation | general_query | get_location>,
                        "to": <only in case of navigation intent>,
                        "from":  <only in case of navigation intent>,
                        "answer": <Required, Give a detailed answer under 60 words>,
                        "places_required": <Array of locations user want from the query, make sure to mention relevant places, only in case of get_location or general_query>,
                        }
                        """,
                },
                {
                    "role": "user",
                    "content": f"Input Data: {message}",
                },
            ],
            temperature=self.temperature,
        )["choices"][0]["message"]["content"]
        print(out)
        return out

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
    out = llm.generate("Generate a itenary for my kolkata trip")
    print(out)
