from llama_cpp import Llama
import json

err = 0
llm = Llama(
    model_path="data/models/llama-2-7b.Q4_K_M.gguf",
    n_gpu_layers=-1,  # Uncomment to use GPU acceleration
    verbose=False,
    flash_attn=True,
    # seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)
for i in range(50):
    output = llm.create_chat_completion(
        messages=[
            {
                "role": "system",
                "content": "You are a classsifier that classify if user want to go somewhere(navigation intent) or not, you always outputs in JSON.",
            },
            {"role": "user", "content": "How to reach ballygunge from liluah"},
        ],
        response_format={
            "type": "json_object",
            "schema": {
                "type": "object",
                "properties": {"navigation_intent": {"type": "boolean"}},
                "required": ["navigation_intent"],
            },
        },
        temperature=0.7,
    )
    if "false" in output["choices"][0]["message"]["content"]:
        err = err + 1

print(err)
