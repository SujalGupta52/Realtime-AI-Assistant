# Real Time AI Assistant
A real-time communication AI system that integrates speech-to-text, natural language processing, and text-to-speech functionalities. It leverages self-hosted Whisper STT and Llama 3 8B model to enable seamless and fluid real-time conversations with minimal latency. 

## Techonolgy Used
- Backend: Flask
- Speech-to-Text: Whisper
- Natural Language Processing: Llama 3 8B
- Text-to-Speech: PiperTTS or in-browser SpeechUtterance API
- Hosting: Self-hosted

## Features
- Speech-to-Text (STT): Utilizes Whisper for accurate and fast speech recognition.
- Text-to-Speech (TTS): Employs PiperTTS or in-browser SpeechUtterance API for generating fast and high-quality speech from text.
- Natural Language Processing (NLP): Powered by Llama 3 8B model for understanding and generating human-like text.
- Low Latency: Achieves a processing delay of only 2-3 seconds on RTX 3060, ensuring real-time interaction.
- Flask Backend: Robust and efficient backend architecture built with Flask, integrating all components smoothly. Can be extended for different needs.

## Installation
1. Clone the repository
    ``` 
    git clone 
    cd repository-name
2. Install `cuda, cudann, llama-cpp-python, whispers2t` following instruction on their respective repos
3. Setup the python enviroment
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
4. Download `Meta-Llama-3-8B-Instruct.Q4_K_M.gguf` from huggingface and add it to the `./models` folder 
5. Run `app.py`

## TODO
- [ ] Add feature remeber context
- [ ] Reduce latency further
- [ ] Fix some bugs

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## Contact
For questions or collaboration, reach out to me through [Linkedin](https://www.linkedin.com/in/sujal-gupta-a7534a201/)

