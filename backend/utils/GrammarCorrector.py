from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_path = "shozuru/t5-japanese-grammar-corrector"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def getCorrectedSentence(sentence: str) -> str:
    inputs = tokenizer(sentence, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=128)
    correctedSentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return correctedSentence