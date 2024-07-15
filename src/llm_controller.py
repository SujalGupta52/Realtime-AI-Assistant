from llama_cpp import Llama

llm = Llama(
    model_path="models/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
    n_gpu_layers=-1,  # Uncomment to use GPU acceleration
    verbose=True,
    flash_attn=True,
    # seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)
output = []
for i in range(10):
    output.append(
        llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": """You are a very helpful tour guide, fluent in English and JSON.
                        Your task is to parse user intent and list of locations user need.

                        Rules:
                        - leave unknown fields blank

                        Respond with no other text but a JSON document like this example JSON document:
                        {
                        "intent": <navigation | general_query | mark_location>,
                        "to": <only in case of navigation intent>,
                        "from":  <only in case of navigation intent>,
                        "answer": <Reply as a helpful assistant, keep in very short>,
                        "places_required": <Array of locations from above answers, only in case of mark_location or general_query>,
                        }
                        """,
                },
                {
                    "role": "user",
                    "content": "Input Data: Hey, kolkata se howrah station kaise jaye",
                },
            ],
            temperature=0.7,
        )
    )
    print(output[-1])
