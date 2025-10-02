from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="RichardErkhov/webbigdata_-_ALMA-7B-Ja-V2-gguf",
    filename="ALMA-7B-Ja-V2.Q3_K_M.gguf",
    n_gpu_layers=23,
    verbose=False
)

def translateSentence(inputSentence: str) -> str:

    translation_prompt = (
        f"English: {inputSentence.strip()}\n"
        "Japanese:"
    )

    translation_output = llm(
        translation_prompt,
        max_tokens=50,
        stop=["\n"], # Stop at the end of the line
        echo=False
    )
    
    return translation_output['choices'][0]['text'].strip()