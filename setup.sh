python3 -m venv venv
source .venv/bin/activate
pip install -r requirement.txt
wget https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf -P ./models