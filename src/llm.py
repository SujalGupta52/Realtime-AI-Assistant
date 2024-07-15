from llama_cpp import Llama

err = 0
llm = Llama(
    model_path="data/models/llama-2-7b.Q4_K_M.gguf",
    n_gpu_layers=-1,  # Uncomment to use GPU acceleration
    verbose=True,
    flash_attn=True,
    # seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)
output = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": """You are a diligent and honest data entry expert, fluent in English and JSON.
                        Your task is to parse user intent and required location out of text snippets.

                        Rules:
                        - leave unknown fields blank

                        Respond with no other text but a JSON document like this example JSON document:
                        {
                        "intent": "",
                        "locations": "",
                        "to": in case of navigation intent,
                        "from": in case of navigation intent,
                        "answer": Reply as a helpful assistant
                        }
                        """,
        },
        {
            "role": "user",
            "content": "Input Data: I am new to kolkata, what are the good tourist spots",
        },
    ],
    # response_format={
    #     "type": "json_object",
    #     "schema": {
    #         "type": "object",
    #         "properties": {"navigation_intent": {"type": "boolean"}},
    #         "required": ["navigation_intent"],
    #     },
    # },
    temperature=0.7,
)
print(output)
